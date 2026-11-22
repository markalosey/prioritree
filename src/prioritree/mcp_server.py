# Copyright (C) 2026 Mark Losey. All rights reserved.
"""mcp_server -- the member tier: the five ops as OunceMCP tools.

The mcp-server unit (the approved design brief reports/synthesize/mcp-design.md;
the exact-task spec reports/synthesize/mcpserverspec.md): the module-level
OunceServer serving the five ops as five typed tools -- runs.register,
runs.next, votes.cast, votes.census, runs.tally -- each body a SYNC def riding
the same door the service rides: the Serialize verbs, whose own composition
acquires the machine-wide flock around each WHOLE store act and releases it
before the body renders (store_lock.Lock -- the bodies never wrap a second
Lock around a seam call: a second open file description on the same lockfile
would block forever, flock binding the open description; the module's _lock
guards the halt shaper's fresh read window alone). The refusals as VALUES:
the three fields read as DATA at ONE render point (the service's
render_refusal precedent, service.py:168-183 -- never str(e) reparsed) and
raised as the OunceMCP error VALUE carrying the structured ThreePart; DONE a
VALUE never an error (done=true a RESULT, the CLI's exit-0 precedent); the
SAFE HALT rendered with the K=10 cap at this tier alone (F8: legs 1-2 whole,
the shortfall total named, the first ten shown). NO runner at import (the
service's app precedent): the boot the host's command -- bare
python -m prioritree.mcp_server is stdio per session; the --serve flag is
the shared streamable-HTTP form.
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Final, Literal, get_args

from ouncemcp import Effect, InvalidInput, NotFound, OunceServer
from pydantic import BaseModel, Field, field_validator

from prioritree.registry import WEAK_ORDER_TRIPLE, OperatorDeclaration
from prioritree.run_store import STORE_HOME, Persist, StoreRefusedError
from prioritree.scheduler import schedule_pairs
from prioritree.service_store import Serialize
from prioritree.session import ExhaustedQueue
from prioritree.store_lock import Lock
from prioritree.tally import TallyRefusedError
from prioritree.votes import COMPARATOR_CLASSES, VotesRefusedError

if TYPE_CHECKING:
    from collections.abc import Sequence
    from pathlib import Path

    from prioritree.scheduler import Pair

__all__ = ["server"]

# The Field texts (the design brief Section 2's authored texts VERBATIM, the
# em-dashes rendered "--" per the ASCII law -- the build's acceptance).
TEXT_PAIR: Final[str] = (
    "The two item ids as served by runs.next -- [item_a, item_b]; order matters "
    "(the verdicts are positional); legal on any registered pair."
)
TEXT_WINNER: Final[str] = (
    "The judgment -- one of the run's declared verdicts (runs.register's ack echoes "
    "them): prefer-a (the pair's first), prefer-b (the second), or tie."
)
TEXT_COMPARATOR_ID: Final[str] = (
    "Your stable identity for this sitting -- pick one id and keep it; "
    "the same id's re-sent judgment is one voice, a different id a different voter."
)
TEXT_COMPARATOR_CLASS: Final[str] = "human or llm -- the judgment's provenance class (equal weight)."
TEXT_ACKNOWLEDGED: Final[str] = (
    "true = a re-send that matched an existing judgment -- the original acked, the "
    "count unchanged, never double-counted; false = a fresh judgment, newly "
    "recorded, the count grew by one."
)
TEXT_VERDICTS: Final[str] = (
    "The run's judgment vocabulary -- votes.cast's winner comes from this set "
    "(default: prefer-a, prefer-b, tie -- positional over the pair as sent)."
)
BUDGET_REASON_TALLY: Final[str] = (
    "the frozen whole at n=100 minus the elided pair mass -- 100 ids in ranked "
    "groups + components + the three per-item maps ~= 3,860; 4,500 holds the "
    "verified ceiling with 640 tokens (~16%) headroom."
)

# The register schema's own gate (the validator's message, a named constant)
# and the SAFE HALT's render cap (F8: K=10 -- the under-quorum enumeration
# names the total plus the first ten pairs).
_ITEMS_RULE: Final[str] = "items must be at least two, all unique, none empty"
_FORKED_CLASSES: Final[str] = "the comparator-class vocabulary forked from the core's COMPARATOR_CLASSES"
_HALT_CAP: Final[int] = 10

# The comparator-class vocabulary: the literal mirrors the core's own set
# (votes.py:33 -- the vocabulary never forks, content-in-configuration held);
# the guard refuses the import if the core's set ever drifts (the
# import-verification lesson carried by construction, never by memory).
ComparatorClass = Literal["human", "llm"]
if frozenset(get_args(ComparatorClass)) != COMPARATOR_CLASSES:
    raise ImportError(_FORKED_CLASSES)

# The module-level objects (the spec Section 2(c); the service.py:158-165
# precedent): the seam injected at construction over the CLI's own store home,
# the server minted plain (OunceServer(name=...) per the census's form; NO
# Budget override -- the startup whole is 25% of the 4,000 default, the
# design brief Section 4), NO runner at import. The naming law: the
# act-statement "Serve the five ops as OunceMCP tools" -- the first word the
# symbol: server.
LOCK_HOME: Final[Path] = STORE_HOME
_seam = Serialize(STORE_HOME)
_lock = Lock(STORE_HOME)
server = OunceServer(name="prioritree")


class RegisterInput(BaseModel):
    """RegisterInput -- the register tool's body: the items as bare ids, the operator, the quorum."""

    items: list[str] = Field(
        min_length=2,
        description="The items to rank, one id per entry; at least two, all unique, none empty",
    )
    quorum: int = Field(ge=1, default=1)
    operator_id: str = Field(min_length=1)
    question: str = Field(min_length=1)

    @field_validator("items")
    @classmethod
    def _unique_nonempty(cls, values: list[str]) -> list[str]:
        """Refuse duplicate or empty ids at the schema -- the core's gates ride beneath."""
        if len(set(values)) != len(values) or any(not value.strip() for value in values):
            raise ValueError(_ITEMS_RULE)
        return values


class NextInput(BaseModel):
    """NextInput -- the next tool's body: the run id and the optional seed."""

    run_id: str = Field(min_length=1)
    seed: int | None = None


class CastInput(BaseModel):
    """CastInput -- the cast tool's body: the pair, the verdict, the stamps, the correction."""

    run_id: str = Field(min_length=1)
    pair: list[str] = Field(description=TEXT_PAIR, min_length=2, max_length=2)
    winner: str = Field(description=TEXT_WINNER)
    comparator_id: str = Field(description=TEXT_COMPARATOR_ID)
    comparator_class: ComparatorClass = Field(description=TEXT_COMPARATOR_CLASS)
    notes: str | None = None
    supersedes: str | None = None


class CensusInput(BaseModel):
    """CensusInput -- the census tool's body: the run id."""

    run_id: str = Field(min_length=1)


class TallyInput(BaseModel):
    """TallyInput -- the tally tool's body: the run id."""

    run_id: str = Field(min_length=1)


class RegisterAck(BaseModel):
    """RegisterAck -- the register tool's ack: the stem, the count, the quorum, the verdicts."""

    run_id: str
    count: int
    quorum: int
    verdicts: list[str] = Field(description=TEXT_VERDICTS)


class NextOutcome(BaseModel):
    """NextOutcome -- the next tool's return: the served pair or the done state, done the tag."""

    done: bool
    item_a: str = ""
    item_b: str = ""
    count: int = 0
    expected: str = ""
    found: str = ""
    next_action: str = ""


class CastAck(BaseModel):
    """CastAck -- the cast tool's ack: the vote id, the count, the acknowledged marker."""

    vote_id: str
    count: int
    acknowledged: bool = Field(description=TEXT_ACKNOWLEDGED)


class CensusView(BaseModel):
    """CensusView -- the census tool's view: the total and the per-item counts."""

    total: int
    items: dict[str, int]


class CoverageView(BaseModel):
    """CoverageView -- the coverage block's summary: the components, the cycle, the pair totals."""

    components: list[list[str]]
    cycle: list[list[str]]
    pairs_expected: int
    pairs_at_quorum: int
    done: bool


class TallyView(BaseModel):
    """TallyView -- the tally tool's view: the ranked whole minus the elided pair mass."""

    ranked_groups: list[list[str]]
    per_item_wins: dict[str, int]
    per_item_losses: dict[str, int]
    per_item_ties: dict[str, int]
    coverage: CoverageView
    algorithm_version: str


def _render_refusal(
    refusal: StoreRefusedError | VotesRefusedError | TallyRefusedError,
) -> dict[str, str]:
    """Render the refusal's three fields as the structured body -- the one render point.

    Purpose: ONE render point for every typed refusal -- the three fields read
    as DATA (expected/found/next_action as attributes, never str(e) reparsed)
    returned as the three-key body the error value carries; a second rendering
    would fork the grammar (the service.py:168-183 precedent re-carried).
    Refuses when: never -- a pure rendering over the refusal's own fields.
    Re-run: deterministic -- the same refusal renders the same body.
    Touches: nothing -- a read of the injected refusal.
    Provenance: the spec Section 2(f) (the one render point), R5 (the
    ThreePart mandatory), G-MCPSERVERSPEC-BRIEF.
    """
    return {"expected": refusal.expected, "found": refusal.found, "next_action": refusal.next_action}


def _render_three_part(expected: str, found: str, next_action: str) -> str:
    """Render the ThreePart's labeled message -- the structured payload of the error value.

    Purpose: the structured ThreePart as the error's payload -- the three
    fields labeled with the grammar's own names, '|'-joined; the census's
    NotFound(msg, hint) style declined for the structured ThreePart per the
    design brief Section 2.
    Refuses when: never -- a pure rendering over the injected fields.
    Re-run: deterministic -- the same fields render the same message.
    Touches: nothing.
    Provenance: the spec Section 2(g) (the error value carrying the
    ThreePart), R5, G-MCPSERVERSPEC-BRIEF.
    """
    return f"expected: {expected} | found: {found} | next_action: {next_action}"


def _refuse(refusal: StoreRefusedError | VotesRefusedError) -> InvalidInput | NotFound:
    """Refuse through the OunceMCP error value -- the family's class, the ThreePart the payload.

    Purpose: the raise-at-the-render form -- the refusal's three fields read
    as data at the one render point, rendered as the labeled ThreePart, and
    raised (by the caller) as the OunceMCP error VALUE with the family's
    class: StoreRefusedError => NotFound (the service's 404 lineage -- the
    unknown run, the corrupt file), VotesRefusedError => InvalidInput (the
    422 lineage -- the door's value refusals).
    Refuses when: never -- the return IS the error value; the caller raises.
    Re-run: deterministic -- the same refusal renders the same error value.
    Touches: nothing -- a rendering over the injected refusal.
    Provenance: the spec Section 2(g), the service's status map (the family
    lineage), G-MCPSERVERSPEC-BRIEF.
    """
    part = _render_refusal(refusal)
    message = _render_three_part(part["expected"], part["found"], part["next_action"])
    if isinstance(refusal, StoreRefusedError):
        return NotFound(message)
    return InvalidInput(message)


def _shown(entries: Sequence[str]) -> str:
    """Show the shortfall entries at the cap -- the whole list under ten, the elision named over.

    Purpose: F8's elision -- at most ten entries rendered: over ten, the
    total named and the first ten shown (the K cap the render's bound,
    "N under-quorum pairs total; first 10 shown"); the whole enumeration
    otherwise (the core's own form, byte-matched at the bound).
    Refuses when: never -- a pure rendering over the injected entries.
    Re-run: deterministic -- the same entries render the same text.
    Touches: nothing.
    Provenance: F8 (the K=10 cap), the spec Section 2(f), G-MCPSERVERSPEC-BRIEF.
    """
    if len(entries) <= _HALT_CAP:
        return ", ".join(entries)
    return f"{len(entries)} under-quorum pairs total; first {_HALT_CAP} shown: {', '.join(entries[:_HALT_CAP])}"


def _components(ids: Sequence[str], counted_pairs: Sequence[Pair]) -> tuple[tuple[str, ...], ...]:
    """Partition the comparison graph -- the union-find mirror of tally.py:226-259.

    Purpose: the same partition the core's private _components computes --
    union-find over the counted pairs, ids-sorted within each component,
    the components ordered by smallest id -- mirrored at this tier because
    the core's render members are private (the fence: no core edits) and
    the halt's capped render re-derives legs 1-2 as data, never reparsed
    from the refusal's prose.
    Refuses when: never -- a pure traversal, deterministic and near-linear.
    Re-run: deterministic -- the same (ids, edges) partition the same.
    Touches: nothing -- pure over its arguments.
    Provenance: tally.py:226-259 (the mirrored algorithm), the spec
    Section 2(f) (the shaper's re-derivation), G-MCPSERVERSPEC-BRIEF.
    """
    parent: dict[str, str] = {item_id: item_id for item_id in ids}

    def find(node: str) -> str:
        """Compress the path; return the root."""
        root = node
        while parent[root] != root:
            root = parent[root]
        while parent[node] != root:
            parent[node], node = root, parent[node]
        return root

    for pair in counted_pairs:
        root_a, root_b = find(pair.item_a), find(pair.item_b)
        if root_a != root_b:
            parent[root_b] = root_a
    members: dict[str, list[str]] = {}
    for item_id in ids:
        members.setdefault(find(item_id), []).append(item_id)
    return tuple(
        tuple(sorted(group)) for _, group in sorted(members.items(), key=lambda entry: entry[1][0])
    )


def _found_sections(
    zero_coverage: Sequence[str],
    components: tuple[tuple[str, ...], ...],
    shortfalls: Sequence[tuple[Pair, int]],
    quorum: int,
) -> str:
    """Render the halt's found -- the core's section grammar mirrored, leg 3 at the cap.

    Purpose: the core's _found_sections grammar re-carried at this tier
    (tally.py:331-360) -- leg 1's zero-coverage ids, leg 2's components,
    leg 3's under-quorum pairs each with its weighted count, '; '-joined;
    leg 3's enumeration capped at ten (F8); each section present only when
    its leg fails; the em-dash rendered "--" per the ASCII law.
    Refuses when: never -- a pure rendering over the re-derived data.
    Re-run: deterministic -- the same data renders the same text.
    Touches: nothing.
    Provenance: tally.py:331-360 (the mirrored grammar), F8, the spec
    Section 2(f), G-MCPSERVERSPEC-BRIEF.
    """
    sections: list[str] = []
    if zero_coverage:
        sections.append(f"zero-coverage items: {', '.join(zero_coverage)}")
    if len(components) > 1:
        rendered = ", ".join(f"({', '.join(component)})" for component in components)
        sections.append(f"components: {rendered}")
    if shortfalls:
        shown = _shown([f"({pair.item_a}, {pair.item_b}) {count} of {quorum}" for pair, count in shortfalls])
        sections.append(f"under-quorum pairs: {shown}")
    return "; ".join(sections)


def _next_action_sections(
    components: tuple[tuple[str, ...], ...],
    shortfalls: Sequence[tuple[Pair, int]],
    quorum: int,
) -> str:
    """Render the halt's next_action -- the core's cure grammar mirrored, the shortfall list capped.

    Purpose: the core's _next_action_sections grammar re-carried at this
    tier (tally.py:363-395) -- the spanning-tree bridges when the graph is
    disconnected ("connectivity needs NEW comparisons"), each shortfall's
    missing count ("quorum needs MORE VOTES on existing pairs"), never
    conflated; the shortfall enumeration capped at ten (F8); the em-dash
    rendered "--" per the ASCII law.
    Refuses when: never -- a pure rendering over the re-derived data.
    Re-run: deterministic -- the same data renders the same text.
    Touches: nothing.
    Provenance: tally.py:363-395 (the mirrored grammar), F8, the spec
    Section 2(f), G-MCPSERVERSPEC-BRIEF.
    """
    sections: list[str] = []
    if len(components) > 1:
        merged = set(components[0])
        bridges: list[tuple[str, str]] = []
        for component in components[1:]:
            bridges.append((min(merged), min(component)))
            merged.update(component)
        rendered = ", ".join(f"({item_a}, {item_b})" for item_a, item_b in bridges)
        sections.append(f"cast the bridging pairs: {rendered} -- connectivity needs NEW comparisons")
    if shortfalls:
        shown = _shown(
            [f"({pair.item_a}, {pair.item_b}) needs {quorum - count} more" for pair, count in shortfalls],
        )
        sections.append(f"cast the missing votes: {shown} -- quorum needs MORE VOTES on existing pairs")
    return "; ".join(sections)


def _capped_halt(refusal: TallyRefusedError, run_id: str) -> InvalidInput:
    """Shape the SAFE HALT's refusal at the ten-pair cap -- the error value returned.

    Purpose: the K=10 cap at the halt's render (F8) -- the under-quorum
    enumeration (leg 3 in found AND next_action, both O(n^2)) rendered
    CAPPED, legs 1-2 whole; the refusal's strings reparsed NEVER (the core's
    private render members never called -- the fence): the legs re-derived
    from the run's own ground (a fresh manifest+census read through the
    door under the module's held lock, schedule_pairs the canonical order,
    the WEIGHTED count -- corrections counted, superseded excluded, the
    R9 exclusion law over the census's vote log), the refusal's expected
    carried whole, the found/next_action constructed in the core's section
    grammar; the shaper touches only the render, never the error's own
    values. At ten or fewer shortfalls the refusal's own fields pass
    through VERBATIM (the cap never fires). The CLI and service keep their
    verbatim renders -- the cap lands at this render point alone.
    Refuses when: never its own refusal -- a store refusal at the fresh
    read rides through BY TYPE to the caller's channel.
    Re-run: deterministic given the store state -- the fresh read
    re-derives the same legs; the re-tally re-fires with the next firsts
    as pairs close (F8's progressive form).
    Touches: only the run file (a read through the door, under the held
    lock).
    Provenance: F8 (the K=10 cap), the spec Section 2(f) (the shaper's
    honest form), R9 (the weighting law mirrored), G-MCPSERVERSPEC-BRIEF.
    """
    with _lock:
        persist = Persist.load(STORE_HOME, run_id)
    manifest = persist.manifest()
    census = persist.census()
    ids = [row.id for row in manifest.items]
    pairs = schedule_pairs(ids)
    excluded = {record.supersedes for record in census.vote_log if record.supersedes is not None}
    pair_counts = dict.fromkeys(pairs, 0)
    touched: set[str] = set()
    for record in census.vote_log:
        if record.vote_id in excluded:
            continue
        pair_counts[record.pair] += 1
        touched.update((record.pair.item_a, record.pair.item_b))
    shortfalls = [(pair, pair_counts[pair]) for pair in pairs if pair_counts[pair] < manifest.quorum]
    if len(shortfalls) <= _HALT_CAP:
        return InvalidInput(_render_three_part(refusal.expected, refusal.found, refusal.next_action))
    zero_coverage = sorted(item_id for item_id in ids if item_id not in touched)
    components = _components(ids, [pair for pair in pairs if pair_counts[pair] >= 1])
    found = _found_sections(zero_coverage, components, shortfalls, manifest.quorum)
    next_action = _next_action_sections(components, shortfalls, manifest.quorum)
    return InvalidInput(_render_three_part(refusal.expected, found, next_action))


@server.tool(name="runs.register", effect=Effect.WRITE, idempotency=True)
def register(body: RegisterInput) -> RegisterAck:
    """Register items for a pairwise-comparison sitting: pairs are judged one
    against another, the votes tallied into a ranked whole. The sequence:
    runs.next serves each under-quorum pair, votes.cast records the judgment,
    runs.tally emits the rank, votes.census audits. quorum is the judgments
    each pair needs before the tally. The ack's run_id is the sitting's
    handle -- carry it to every later call; re-registering the same items
    mints a NEW run.
    """
    try:
        stem = _seam.register(
            [(item_id, item_id) for item_id in body.items],
            OperatorDeclaration(id=body.operator_id, question=body.question),
            body.quorum,
        )
    except (StoreRefusedError, VotesRefusedError) as refusal:
        raise _refuse(refusal) from refusal
    return RegisterAck(
        run_id=stem, count=len(body.items), quorum=body.quorum, verdicts=sorted(WEAK_ORDER_TRIPLE),
    )


@server.tool(name="runs.next", effect=Effect.READ)
def serve(body: NextInput) -> NextOutcome:
    """Serve the sitting's next under-quorum pair -- the loop's read: call
    until done:true (every pair at quorum), then runs.tally. Returns the pair
    as [item_a, item_b] (the verdicts are positional over this order) and its
    current count. seed optional -- the default order is stable per run.
    """
    try:
        item_a, item_b, count = _seam.serve(body.run_id, body.seed)
    except ExhaustedQueue as done:
        return NextOutcome(done=True, expected=done.expected, found=done.found, next_action=done.next_action)
    except (StoreRefusedError, VotesRefusedError) as refusal:
        raise _refuse(refusal) from refusal
    return NextOutcome(done=False, item_a=item_a, item_b=item_b, count=count)


@server.tool(name="votes.cast", effect=Effect.WRITE, idempotency=True)
def cast(body: CastInput) -> CastAck:
    """Cast one judgment on a pair -- the sitting's only write. The judgment
    is stamped (comparator_id, comparator_class), durable at once,
    append-only. A byte-identical re-send acks the original
    (acknowledged=true, the count unchanged -- one voice, never
    double-counted); a changed verdict is a new record; supersedes cites a
    vote_id to correct one. A vote is legal on any registered pair -- no
    serve needed.
    """
    try:
        vote_id, _record, count, acknowledged = _seam.cast(
            body.run_id,
            body.pair,
            body.winner,
            body.comparator_id,
            body.comparator_class,
            body.notes,
            body.supersedes,
        )
    except (StoreRefusedError, VotesRefusedError) as refusal:
        raise _refuse(refusal) from refusal
    return CastAck(vote_id=vote_id, count=count, acknowledged=acknowledged)


@server.tool(name="votes.census", effect=Effect.READ)
def audit(body: CensusInput) -> CensusView:
    """Audit the sitting's counts as-is: the total judgments and each item's
    count. The evidence surface -- what has landed, never what should have.
    """
    try:
        snapshot = _seam.census(body.run_id)
    except (StoreRefusedError, VotesRefusedError) as refusal:
        raise _refuse(refusal) from refusal
    return CensusView(total=len(snapshot.vote_log), items=dict(snapshot.per_item_counts))


@server.tool(name="runs.tally", effect=Effect.READ, result_tokens=4500, budget_reason=BUDGET_REASON_TALLY)
def tally(body: TallyInput) -> TallyView:
    """Tally the sitting into the ranked whole: ranked_groups (ids
    best-first, equal scores grouped), per-item wins/losses/ties, coverage.
    Under quorum the tally SAFE-HALTs: the refusal names the failing legs
    and the closing pairs -- cast them via votes.cast (a legal pair needs no
    serve); pairs beyond your one voice mean the sitting needs more voters
    (resume the sitting). Re-tally after casting names what remains.
    """
    try:
        result = _seam.rank(body.run_id)
    except TallyRefusedError as refusal:
        raise _capped_halt(refusal, body.run_id) from refusal
    except (StoreRefusedError, VotesRefusedError) as refusal:
        raise _refuse(refusal) from refusal
    return TallyView(
        ranked_groups=[list(group) for group in result.ranked_groups],
        per_item_wins=dict(result.per_item_wins),
        per_item_losses=dict(result.per_item_losses),
        per_item_ties=dict(result.per_item_ties),
        coverage=CoverageView(
            components=[list(component) for component in result.coverage.components],
            cycle=[list(edge) for edge in result.coverage.cycle],
            pairs_expected=len(schedule_pairs(result.per_item_wins.keys())),
            # At the DONE render the gate guarantees every pair at quorum:
            # the weighted-count universe IS the at-quorum count.
            pairs_at_quorum=len(result.coverage.pair_counts),
            done=result.coverage.done,
        ),
        algorithm_version=result.algorithm_version,
    )


def main() -> None:
    """Run the server -- bare stdio, --serve the shared HTTP form."""
    if "--serve" in sys.argv[1:]:
        server.run("http", host="127.0.0.1", port=8000, allowed_hosts=["127.0.0.1", "localhost"], allowed_origins=[])
    else:
        server.run("stdio")


if __name__ == "__main__":
    main()
