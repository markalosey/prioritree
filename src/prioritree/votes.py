# Copyright (C) 2026 Mark Losey. All rights reserved.
"""votes — the append-only vote ledger: cast a judgment, read the census back.

The votes unit (U3): every comparison judgment lands as a frozen VoteRecord
stamped with its provenance (R5: comparator id + class on every line, equal
weight at birth), the winner drawn from the RUN'S OWN declared verdict set
(R4: the manifest's operator.verdicts, never the module constant), and the
append-and-accumulate discipline (R9: a byte-identical re-send is a loud ack,
a changed verdict is a new sample, corrections ride supersedes; no edit, no
delete — append-only). The write discipline: schema gate, ground-truth check
against the manifest at write time (FR-MEM-0001), the per-store max+1 mint in
the same synchronous act as the append (the atomic window — the synchronous
method body IS the single-process window; the lock-file layer is the service
tier's per R9's design requirements). NO score field — the Parnas fold: the
tally's choice cannot cross the vote interface (there is no field to leak
through); abstention needs no record (R4). Zero runtime dependencies; no
subprocess; votes stored verbatim (the system has no opinion about them —
noise is data).
The presentation_order datum (the prior-art's anti-order-bias field, the
order-bias probe's MEASURE-stage instrument): every record carries the
presented order — 'canonical' (item_a first, the standing form at every
tier) or 'swapped' (item_b first, the both-orders experiment's second
presentation). The cast door composes its swapped-citation refusal with
the field (the fieldless swap never silently re-ordered; the fielded swap
the explicit, citable act), maps the presented pair onto the canonical
Pair and the presented-order winner onto the canonical frame — the tally
NEVER reads the presentation (R12's fence: the count reads the canonical
pair + the mapped winner; the record's bytes byte-identical at the
canonical form).
"""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from typing import cast

from prioritree.registry import WEAK_ORDER_TRIPLE, Registry, RegistryRefusedError, RunManifest
from prioritree.scheduler import Pair, schedule_pairs

# R5's class set as data (content-in-configuration): the vocabulary is a
# module-level frozenset constant, never inline logic.
COMPARATOR_CLASSES: frozenset[str] = frozenset({"human", "llm"})

# The presentation vocabulary (the prior-art's anti-order-bias datum, the
# order-bias probe's instrument — the store's own input): the two orders a
# pair can be presented in — canonical (item_a first, the standing form at
# every tier) or swapped (item_b first, the both-orders experiment's second
# presentation). Content-in-configuration: the vocabulary is a module-level
# frozenset constant, never inline logic.
PRESENTATION_CANONICAL: str = "canonical"
PRESENTATION_SWAPPED: str = "swapped"
PRESENTATION_ORDERS: frozenset[str] = frozenset({PRESENTATION_CANONICAL, PRESENTATION_SWAPPED})

# The presented-to-canonical winner mapping's positional tokens (the declared
# triple's positional members — prefer-a the first-presented, prefer-b the
# second; the tie positionless, mapped unchanged). The literals mirror the
# registry's own WEAK_ORDER_TRIPLE members; the guard keeps the vocabulary
# unforked (the mcp_server drift school, this the door's own tier).
_FORKED_POSITIONAL: str = "the positional verdict tokens forked from the registry's WEAK_ORDER_TRIPLE"
_PREFER_A: str = "prefer-a"
_PREFER_B: str = "prefer-b"
_TIE: str = "tie"
if frozenset({_PREFER_A, _PREFER_B, _TIE}) != WEAK_ORDER_TRIPLE:
    raise ImportError(_FORKED_POSITIONAL)
_POSITIONAL_SWAP: dict[str, str] = {_PREFER_A: _PREFER_B, _PREFER_B: _PREFER_A}

# The handle grammar on the public surface — the citation contract.
VOTE_PREFIX: str = "VOTE-"

# Structural constants (named, per the zero-magic-value-in-src discipline).
_PAIR_LENGTH = 2


@dataclass(frozen=True)
class VoteRecord:
    """VoteRecord — one frozen judgment, provenance stamped.

    Purpose: carry one comparison judgment as data — the handle, the run, the
    canonical pair, the presented order (the prior-art's non-optional
    anti-order-bias datum — 'canonical' the standing form, 'swapped' the
    both-orders experiment's second presentation), the declared-set winner,
    the comparator's stamps (R5: identity recorded, never anonymous), the
    recorded_at stamp, and the clerical correction's reference; the tally's
    ENTIRE input (U4) and the
    audit surface's unit (U5).
    Refuses when: never at construction — validation happens at cast_vote;
    every gate raises VotesRefusedError before any byte lands there.
    Re-run: idempotent — a frozen value type; the same judgment constructs
    the same record (the store always holds the canonical Pair).
    Touches: nothing — a pure value; held by the VoteLedger store and read
    back by the census.
    Provenance: R4 (the winner from the run's declared verdict set; abstention
    needs no record), R5 (the provenance stamps, equal weight at birth), R9
    (append-and-accumulate; supersedes rides the clerical correction), op 3,
    G-VOTES, votes-brief §2 (NO score field — the Parnas fold); discover/votes
    and understand/votes (the legs riding the brief).
    """

    vote_id: str
    run_id: str
    pair: Pair
    winner: str
    comparator_id: str
    comparator_class: str
    recorded_at: str
    notes: str | None = None
    supersedes: str | None = None
    presentation_order: str = PRESENTATION_CANONICAL


@dataclass(frozen=True)
class VoteCensus:
    """VoteCensus — the census read-back snapshot of one run's vote state.

    Purpose: hold the per-pair counts over the FULL pair universe (0 included),
    the per-item comparison counts over every manifest id (0 included; each
    record increments BOTH pair members — a tie still compares; sum equals
    2 x total votes), and the full vote log in mint order — the audit surface
    (U5's quorum consult, every gate's evidence leg; the op that catches
    silent-loss and gap classes).
    Refuses when: never at construction — read_vote_state refuses the unknown
    run ONLY; the census NEVER refuses on coverage (the zero-vote run reads
    back all-zero maps over the full universe + the empty log: a VALUE,
    never a refusal — the audit surface reads back broken states, especially
    broken states; that is its job).
    Re-run: pure — a fresh frozen value per call; later casts never mutate a
    returned census.
    Touches: nothing — a pure value; the maps are fresh plain dicts built
    per call, the log a frozen tuple of frozen records.
    Provenance: op 4, G-VOTES condition 4 (the census read-back green; never
    refusing on coverage), R9 (the log is append-only — the full history,
    corrections included), votes-brief §4 (the census without manifest or
    verdict: the counts as data; the verdicts compute where the quorum lives).
    """

    run_id: str
    per_pair_counts: Mapping[Pair, int]
    per_item_counts: Mapping[str, int]
    vote_log: tuple[VoteRecord, ...]


class VotesRefusedError(Exception):
    """VotesRefusedError — the typed refusal: expected, found, next_action.

    Purpose: carry the votes surface's refusal grammar (expected/found/
    next-action) as data the CLI/service wrappers catch and render; raised,
    never returned; the ONE refusal grammar downstream units catch (the
    registry's refusals ride through verbatim via the wrap).
    Refuses when: never — it IS the refusal; the message renders all three
    fields so an uncaught traceback still names the legal form.
    Re-run: deterministic — the same violation raises the same three fields.
    Touches: nothing — a plain Exception subclass (zero runtime deps).
    Provenance: the RegistryRefusedError precedent (registry.py:89-115, the
    Error-suffix family form, N818), votes-brief §2; the expected/found/
    next-action grammar (op 3's refusal list, votes-brief §3).
    """

    def __init__(self, expected: str, found: str, next_action: str) -> None:
        """Initialize the refusal with its three named fields.

        Purpose: carry expected/found/next_action plus the rendered message.
        Refuses when: never.
        Re-run: idempotent.
        Touches: nothing.
        Provenance: registry-brief §2 (the typed exception, RefusedError precedent).
        """
        self.expected = expected
        self.found = found
        self.next_action = next_action
        super().__init__(f"refused — expected: {expected} | found: {found} | next: {next_action}")


class SupersedeRefusedError(Exception):
    """SupersedeRefusedError — the author-refusal: expected, found, next_action.

    Purpose: carry the supersedes door check's refusal (a correction corrects
    the CALLER'S OWN vote — the author mismatch) as typed data; found ELIDES
    the target's author (the identity oracle never fed — the 401's
    "absent-or-unknown" discipline at the 403); the service route maps it to
    403 (the wire's authorization half).
    Refuses when: never — it IS the refusal; the message renders all three
    fields so an uncaught traceback still names the legal form.
    Re-run: deterministic — the same violation raises the same three fields.
    Touches: nothing — a plain Exception subclass (zero runtime deps).
    Provenance: the design's F4, the unit brief §1d/§3e, rikai map 4,
    G-SERVING-TIER-INTEGRATION-BRIEF.
    """

    def __init__(self, expected: str, found: str, next_action: str) -> None:
        """Initialize the refusal with its three named fields.

        Purpose: carry expected/found/next_action plus the rendered message
        (the em dash per this module's own :134 bytes).
        Refuses when: never.
        Re-run: idempotent.
        Touches: nothing.
        Provenance: the VotesRefusedError __init__ school (:122-134),
        servingtierintegrationspec §2a.
        """
        self.expected = expected
        self.found = found
        self.next_action = next_action
        super().__init__(f"refused — expected: {expected} | found: {found} | next: {next_action}")


def _require_text(value: object, field_name: str) -> str:
    """Return the stripped non-empty string or refuse (the _req_text precedent).

    Purpose: enforce the non-empty-string discipline on run_id and comparator_id.
    Refuses when: the value is not a string or is empty/whitespace-only.
    Re-run: deterministic.
    Touches: nothing (raises before any store write).
    Provenance: registry.py:118-133 (_require_text), votes-brief §3 stage 1.
    """
    if not isinstance(value, str) or not value.strip():
        raise VotesRefusedError(
            expected=(
                "the schema's public types (run_id a non-empty string; pair a Pair or "
                "2-length sequence of strings; winner a string; comparator_id a non-empty "
                f"string; comparator_class from {sorted(COMPARATOR_CLASSES)}; "
                f"presentation_order from {sorted(PRESENTATION_ORDERS)}; notes a string "
                "or None; supersedes a string or None)"
            ),
            found=f"{field_name} got {value!r}",
            next_action="re-send per the schema — the module's public types (VoteRecord's fields)",
        )
    return value.strip()


def _coerce_pair(pair: object) -> Pair:
    """Coerce the dual-form pair into the canonical Pair, AS SENT.

    Purpose: accept a Pair instance (members checked strings) or a 2-length
    sequence of strings; return the pair as sent, never re-ordered — the
    swapped citation is refused at stage 3 naming the canonical form.
    Refuses when: the value is neither a Pair with string members nor a
    2-length sequence of strings (a bare string is a sequence — refused).
    Re-run: deterministic.
    Touches: nothing (raises before any store write).
    Provenance: the _coerce_rows precedent (registry.py:149-195), votes-brief
    §3 stage 1 (the dual-form pair).
    """
    if isinstance(pair, Pair):
        return Pair(item_a=pair.item_a, item_b=pair.item_b)
    if isinstance(pair, Sequence) and not isinstance(pair, str):
        raw = cast("Sequence[object]", pair)
        if len(raw) == _PAIR_LENGTH:
            first, second = raw[0], raw[1]
            if isinstance(first, str) and isinstance(second, str):
                return Pair(item_a=first, item_b=second)
    raise VotesRefusedError(
        expected=(
            "the schema's public types (run_id a non-empty string; pair a Pair or "
            "2-length sequence of strings; winner a string; comparator_id a non-empty "
            f"string; comparator_class from {sorted(COMPARATOR_CLASSES)}; "
            f"presentation_order from {sorted(PRESENTATION_ORDERS)}; notes a string "
            "or None; supersedes a string or None)"
        ),
        found=f"pair got {pair!r}",
        next_action="re-send per the schema — the module's public types (VoteRecord's fields)",
    )


def _require_optional_text(value: object, field_name: str) -> str | None:
    """Return the string-or-None field as-is (verbatim, opacity).

    Purpose: enforce the notes/supersedes form — any string, stored verbatim,
    or None.
    Refuses when: the value is neither a string nor None.
    Re-run: deterministic.
    Touches: nothing (raises before any store write).
    Provenance: votes-brief §2 (notes/supersedes stored verbatim), §3 stage 1.
    """
    if value is None or isinstance(value, str):
        return value
    raise VotesRefusedError(
        expected=(
            "the schema's public types (run_id a non-empty string; pair a Pair or "
            "2-length sequence of strings; winner a string; comparator_id a non-empty "
            f"string; comparator_class from {sorted(COMPARATOR_CLASSES)}; "
            f"presentation_order from {sorted(PRESENTATION_ORDERS)}; notes a string "
            "or None; supersedes a string or None)"
        ),
        found=f"{field_name} got {value!r}",
        next_action="re-send per the schema — the module's public types (VoteRecord's fields)",
    )


def _require_verdict(value: object, field_name: str) -> str:
    """Return the string verdict token or refuse (the object-boundary form).

    Purpose: enforce the winner's string form at the untyped boundary (the
    public annotation says str; the runtime check guards the untyped caller).
    Refuses when: the value is not a string.
    Re-run: deterministic.
    Touches: nothing (raises before any store write).
    Provenance: the object-typed validator precedent (amendment 16), votes-brief §3 stage 1.
    """
    if not isinstance(value, str):
        raise VotesRefusedError(
            expected=(
                "the schema's public types (run_id a non-empty string; pair a Pair or "
                "2-length sequence of strings; winner a string; comparator_id a non-empty "
                f"string; comparator_class from {sorted(COMPARATOR_CLASSES)}; "
                f"presentation_order from {sorted(PRESENTATION_ORDERS)}; notes a string "
                "or None; supersedes a string or None)"
            ),
            found=f"{field_name} got {value!r}",
            next_action="re-send per the schema — the module's public types (VoteRecord's fields)",
        )
    return value


def _resolve_cited_pair(
    pair: object,
    cited_pair: Pair,
    presentation_order: str,
    legal_pairs: frozenset[Pair],
    manifest_id_count: int,
) -> Pair:
    """Resolve the cited pair onto the canonical Pair — the presented order composed with the field.

    Purpose: the cast door's stage-3 composition — the citation rides the
    PRESENTED order: the canonical citation legal at the canonical
    presentation; the swapped citation legal ONLY as the explicit swapped
    presentation (the field the license — a swap is never silently
    re-ordered); a field contradicting the pair's order refused; the
    presented pair mapped onto the canonical Pair (the record's pair
    canonical, the presentation_order field the citable datum).
    Refuses when: the cited pair is outside the legal set (neither the
    canonical form nor its swap — the unknown-pair refusal); the cited pair
    is the swapped citation without presentation_order='swapped' (the
    standing refusal naming the canonical form, the field taught as the
    explicit act); the canonical citation carries presentation_order
    'swapped' (the contradiction — the field and the pair's order must
    agree).
    Re-run: deterministic.
    Touches: nothing (raises before any store write).
    Provenance: the order-bias probe's MEASURE instrument (the design
    synthesis §2.2's cast-side composition — the door's refusal of swapped
    citations COMPOSED with the field); votes-brief §3 stage 3 (the legal
    set's source, the swapped-citation refusal's bytes); the C901 extraction
    precedent (tally's _dominance_adjacency).
    """
    if cited_pair in legal_pairs:
        if presentation_order != PRESENTATION_SWAPPED:
            return cited_pair
        raise VotesRefusedError(
            expected=(
                "the pair cited as presented — the canonical citation at presentation_order "
                "'canonical', the swapped citation at 'swapped' (the field and the pair's "
                "order agree)"
            ),
            found=f"{pair!r} with presentation_order {presentation_order!r}",
            next_action=(
                "re-send the pair in the presented order with presentation_order naming "
                "it — the field and the pair's order must agree"
            ),
        )
    swapped_cited = Pair(item_a=cited_pair.item_b, item_b=cited_pair.item_a)
    if swapped_cited not in legal_pairs:
        raise VotesRefusedError(
            expected=(
                f"a canonical pair from schedule_pairs over the run's {manifest_id_count} "
                "manifest ids (the legal set's source)"
            ),
            found=f"{pair!r}",
            next_action=(
                "cite a canonical scheduled pair — the scheduler suggests; it does not "
                "confer permission, but a vote cites the canonical form"
            ),
        )
    if presentation_order != PRESENTATION_SWAPPED:
        raise VotesRefusedError(
            expected=(
                f"a canonical pair (item_a < item_b) — the canonical form of these "
                f"ids is {swapped_cited!r}"
            ),
            found=f"{pair!r}",
            next_action=(
                "re-send the pair id-sorted — the verdict vocabulary is positional "
                "over the canonical form; a swap is never silently re-ordered "
                "(to record a swapped presentation, cite the pair as presented "
                "with presentation_order='swapped')"
            ),
        )
    return swapped_cited


def _mint_vote_id(count: int) -> str:
    """Mint the VOTE-{####} handle — 4-digit zero-pad, natural overflow.

    Purpose: name the vote per the per-STORE max+1 mint (count is the live
    size; append-only keeps len == max; two ledgers mint independently).
    Refuses when: never — the count is the container's own live state.
    Re-run: deterministic for a given store state.
    Touches: nothing — pure over its argument.
    Provenance: the RUN-{####} precedent (registry.py:136-146), votes-brief
    §3 stage 6 (the per-store mint).
    """
    return f"{VOTE_PREFIX}{count + 1:04d}"


class VoteLedger:
    """VoteLedger — the append-only vote store: cast, then read the census back.

    Purpose: hold one process's VoteRecords minted via cast_vote and read the
    run's state back via read_vote_state — the census instrument (the manifest
    resolved per write via the injected registry's read_manifest, never
    cached: the ground-truth check reads the store's own truth at write
    time — FR-MEM-0001's discipline).
    Refuses when: cast_vote refuses (malformed payload; unknown run — the
    registry's refusal re-raised as VotesRefusedError carrying the same three
    fields verbatim; pair outside the legal set, the swapped citation named
    with the canonical form — the fieldless swap; the explicit swapped
    presentation rides presentation_order, a field contradicting the pair's
    order or outside the legal set likewise refused; winner outside the run's
    declared set; invalid supersede target) — raising BEFORE any byte lands;
    read_vote_state refuses the unknown run ONLY and NEVER refuses on coverage.
    Re-run: read_vote_state is pure over the store; cast_vote is append-only
    — the mint is per-store max+1 in the same synchronous act as the append
    (the synchronous method body IS the atomic window at the single-process
    tier; no threading primitive at birth; the loud concurrent-write refusal
    rides the service tier's lock-file layer per R9's design requirements).
    Touches: only its own in-memory records and dedup index — no files, no
    subprocess, no DB; SINGLE-PROCESS by contract (the service tier later
    owns serialization).
    Provenance: R4/R5/R9, the five-op interface, scope-synthesis PART 3 §3.2
    ops 3-4, G-VOTES (the five conditions), votes-brief §3-§4 (Option A —
    the store-as-parameter container, registry-injected); discover/votes and
    understand/votes (the legs riding the brief).
    """

    def __init__(self, registry: Registry) -> None:
        """Initialize an empty vote store over the injected registry.

        Purpose: construct the container the caller holds (store-as-parameter;
        the registry injected by the caller — the manifest resolved per write,
        never cached; never a module-level singleton — test isolation).
        Refuses when: never.
        Re-run: idempotent — a fresh empty store.
        Touches: only its own state.
        Provenance: votes-brief §3 (the constructor-injected registry).
        """
        self._registry = registry
        self._votes: dict[str, VoteRecord] = {}
        self._dedup: dict[tuple[str, Pair, str, str, str, str | None, str | None, str], str] = {}

    def _read_manifest(self, run_id: str) -> RunManifest:
        """Resolve the manifest via the registry, wrapping its refusal.

        Purpose: the wrap — catch RegistryRefusedError, re-raise
        VotesRefusedError carrying the same expected/found/next_action
        verbatim, from refusal (the votes surface speaks ONE refusal grammar;
        the registry's rendered live-set rides through unchanged — the live
        handles named are the REGISTRY's manifests; a never-voted run is legal
        ground; the ledger has no run-domain authority).
        Refuses when: the run_id is not a live registry handle — naming the
        live set (the registry's own rendering).
        Re-run: deterministic.
        Touches: nothing — a read through the registry.
        Provenance: votes-brief §3 stage 2 (the wrap), census gap (b)(iv).
        """
        try:
            return self._registry.read_manifest(run_id)
        except RegistryRefusedError as refusal:
            raise VotesRefusedError(
                expected=refusal.expected,
                found=refusal.found,
                next_action=refusal.next_action,
            ) from refusal

    def cast_vote(
        self,
        run_id: str,
        pair: Pair | Sequence[str],
        winner: str,
        comparator_id: str,
        comparator_class: str,
        notes: str | None = None,
        supersedes: str | None = None,
        presentation_order: str = PRESENTATION_CANONICAL,
    ) -> tuple[str, VoteRecord, int, bool]:
        """Cast one judgment: validate, dedup, mint, append — the ONE mutating op.

        Purpose: the seven-stage chain — (1) schema (run_id non-empty stripped;
        pair a Pair or 2-length sequence of strings, AS SENT, never
        re-ordered; winner a string; comparator_id non-empty stripped;
        comparator_class in COMPARATOR_CLASSES; presentation_order in
        PRESENTATION_ORDERS; notes/supersedes string or None); (2) the run
        live via the registry (the wrap); (3) the pair in the legal set, the
        presented order composed with the field (schedule_pairs over the
        manifest's ids; the canonical citation legal at the canonical
        presentation; the swapped citation legal ONLY as the explicit swapped
        presentation — the fieldless swap still refused naming the canonical
        form, a swap never silently re-ordered; a field contradicting the
        pair's order refused) with the presented pair mapped onto the
        canonical Pair here; (4) the winner in the RUN'S OWN declared verdict
        set (manifest.operator.verdicts, never the module constant) — the
        WIRE winner, positional over the PRESENTED order; (4b) the
        presented-to-canonical winner mapping at the swapped presentation
        (prefer-a mapped to prefer-b, prefer-b to prefer-a; the tie
        positionless, unchanged) — the record's winner positional over the
        CANONICAL pair, the tally never reading the presentation (R12's
        fence); (5) the supersede ground truth (a correction corrects the
        same judgment — the target live in the same run, on the same pair,
        by the caller's own hand — the author check) then the dedup key
        (run_id, canonical pair, the mapped winner, comparator_id,
        comparator_class, notes, supersedes, presentation_order — a pair's
        two orders two distinct judgments) — a hit is the LOUD idempotent
        ack: (the original handle, the original record, the UNCHANGED
        count, acknowledged=True); (6) the VOTE-{####} per-store max+1 mint
        + the UTC microsecond ISO stamp; (7) the append + verify in one
        synchronous act — return (vote_id, record, len(store),
        acknowledged=False); the count reads the store post-append, never a
        local counter.
        Refuses when: malformed payload; unknown run (the wrap); pair outside
        the legal set, the fieldless swapped citation included;
        presentation_order outside the legal set or contradicting the
        pair's order; winner outside the declared set; supersede target not
        a live handle in the same run on the same pair, or another author's
        vote — every refusal raises VotesRefusedError, the door's author
        mismatch SupersedeRefusedError, before any byte lands. NEVER
        refuses on content plausibility (the system has no opinion about
        votes — noise is data); no quorum or count check here (an
        over-quorum vote lands as a legal new sample); abstention needs no
        record (a comparator who cannot judge does not cast).
        Re-run: deterministic given the same store state; the re-vote
        semantics (R9) — a changed verdict from the same (comparator, pair)
        is a NEW record (a revote is a new sample; both count); a
        byte-identical re-send is the loud ack (zero weight pollution);
        a clerical correction is a NEW record citing the old via supersedes
        (both stand in the log — the tally's weighting walks the link); a
        correction-of-a-correction chains linearly; the same judgment at the
        pair's OTHER order a NEW record too (the dedup key carries the
        presentation — a pair's two orders two distinct judgments).
        Touches: only the store's own records and dedup index — the single
        mutating op (append-only; no edit, no delete — unrepresentable).
        Provenance: R4 (the winner from the run's own declared set), R5 (the
        provenance stamps, equal weight), R9 (the re-vote classes, the loud
        ack, the FR-MEM-0143/0001 fold-ins), op 3, G-VOTES conditions 1-3,
        votes-brief §3 (the seven stages, the five refusal texts); the
        scheduler-suggests-it-does-not-confer-permission seam (a vote is
        valid on any registered pair — ingestion independent of scheduling).
        """
        # Stage 1 — schema (hand-rolled, the registry school; the pair AS SENT).
        clean_run_id = _require_text(run_id, "run_id")
        cited_pair = _coerce_pair(pair)
        winner = _require_verdict(winner, "winner")
        clean_comparator_id = _require_text(comparator_id, "comparator_id")
        if comparator_class not in COMPARATOR_CLASSES:
            raise VotesRefusedError(
                expected=(
                    "the schema's public types (run_id a non-empty string; pair a Pair or "
                    "2-length sequence of strings; winner a string; comparator_id a non-empty "
                    f"string; comparator_class from {sorted(COMPARATOR_CLASSES)}; "
                    f"presentation_order from {sorted(PRESENTATION_ORDERS)}; notes a string "
                    "or None; supersedes a string or None)"
                ),
                found=f"comparator_class got {comparator_class!r}",
                next_action="re-send per the schema — the module's public types (VoteRecord's fields)",
            )
        if presentation_order not in PRESENTATION_ORDERS:
            raise VotesRefusedError(
                expected=(
                    "the schema's public types (run_id a non-empty string; pair a Pair or "
                    "2-length sequence of strings; winner a string; comparator_id a non-empty "
                    f"string; comparator_class from {sorted(COMPARATOR_CLASSES)}; "
                    f"presentation_order from {sorted(PRESENTATION_ORDERS)}; notes a string "
                    "or None; supersedes a string or None)"
                ),
                found=f"presentation_order got {presentation_order!r}",
                next_action="re-send per the schema — the module's public types (VoteRecord's fields)",
            )
        clean_notes = _require_optional_text(notes, "notes")
        clean_supersedes = _require_optional_text(supersedes, "supersedes")

        # Stage 2 — the run live (the wrap: one refusal grammar at this surface).
        manifest = self._read_manifest(clean_run_id)

        # Stage 3 — the pair in the legal set, the presented order composed
        # with the field (_resolve_cited_pair: the record's pair canonical,
        # the presentation_order field the citable datum).
        manifest_ids = [row.id for row in manifest.items]
        legal_pairs = frozenset(schedule_pairs(manifest_ids))
        canonical_pair = _resolve_cited_pair(
            pair,
            cited_pair,
            presentation_order,
            legal_pairs,
            len(manifest_ids),
        )

        # Stage 4 — the winner in the RUN'S OWN declared set (R4: one source of truth).
        declared_verdicts = manifest.operator.verdicts
        if winner not in declared_verdicts:
            raise VotesRefusedError(
                expected=f"a verdict from the run's declared set {sorted(declared_verdicts)}",
                found=f"{winner!r}",
                next_action="cast a verdict from the declared set",
            )

        # Stage 4b — the presented-to-canonical winner mapping (the
        # store/record boundary): the wire winner rides the PRESENTED order;
        # the record's winner rides the CANONICAL pair. At the swapped
        # presentation prefer-a (the first-presented, the canonical item_b)
        # maps to prefer-b and prefer-b maps to prefer-a; the tie carries no
        # positional preference (unchanged). The tally NEVER reads the
        # presentation (R12's fence: the count reads the canonical pair +
        # the mapped winner — the byte-identity held).
        if presentation_order == PRESENTATION_SWAPPED:
            winner = _POSITIONAL_SWAP.get(winner, winner)

        # Stage 5 — the supersede ground truth, then the dedup key (in one place).
        if clean_supersedes is not None:
            target = self._votes.get(clean_supersedes)
            if target is None or target.run_id != clean_run_id:
                raise VotesRefusedError(
                    expected=(
                        "a live VOTE-{####} handle in the same run, on the same pair "
                        "(a correction corrects the same judgment)"
                    ),
                    found=f"{clean_supersedes!r}",
                    next_action="cite the record being corrected",
                )
            if target.pair != canonical_pair:
                raise VotesRefusedError(
                    expected=(
                        "a live VOTE-{####} handle in the same run, on the same pair "
                        "(a correction corrects the same judgment)"
                    ),
                    found=f"{clean_supersedes!r} — a record on pair {target.pair!r}",
                    next_action="cite the record being corrected",
                )
            # The door check rides the CALLER's identity — the PASSED
            # comparator_id (servingtierintegrationspec §2c): under auth-off
            # the service route passes the body's claim (the §1h fallback)
            # — the claim form stands at the door; the CLI/stdio tiers pass
            # their self-claims at every mode (the local trust — the §3
            # floor the offline JSONL edit, the price every placement
            # shares).
            if target.comparator_id != clean_comparator_id:
                raise SupersedeRefusedError(
                    expected=(
                        "a correction of the caller's own vote — the superseder's "
                        "comparator_id matches the target's author"
                    ),
                    found=f"{clean_supersedes!r} — another author's vote (the author never named)",
                    next_action="cite your own vote on this pair, or cast a new vote without supersedes",
                )
        dedup_key = (
            clean_run_id,
            canonical_pair,
            winner,
            clean_comparator_id,
            comparator_class,
            clean_notes,
            clean_supersedes,
            presentation_order,
        )
        original_id = self._dedup.get(dedup_key)
        if original_id is not None:
            # The LOUD ack — the original handle, the original record, the
            # UNCHANGED count, acknowledged=True (never a silent dup).
            return original_id, self._votes[original_id], len(self._votes), True

        # Stages 6-7 — the mint + the append + verify, ONE synchronous act
        # (the atomic window at the single-process tier).
        vote_id = _mint_vote_id(len(self._votes))
        record = VoteRecord(
            vote_id=vote_id,
            run_id=clean_run_id,
            pair=canonical_pair,
            winner=winner,
            comparator_id=clean_comparator_id,
            comparator_class=comparator_class,
            recorded_at=datetime.now(UTC).isoformat(timespec="microseconds"),
            notes=clean_notes,
            supersedes=clean_supersedes,
            presentation_order=presentation_order,
        )
        self._votes[vote_id] = record
        self._dedup[dedup_key] = vote_id
        return vote_id, record, len(self._votes), False

    def read_vote_state(self, run_id: str) -> VoteCensus:
        """Read the run's vote state — the census read-back instrument.

        Purpose: build the frozen snapshot — the per-pair counts over the
        FULL pair universe from schedule_pairs (0 included; +1 per record on
        the pair), the per-item counts over every manifest id (0 included;
        each record increments BOTH pair members — a tie still compares; sum
        equals 2 x total votes), and the full vote log in mint order (the
        run's records filtered from the flat store; insertion order = mint
        order) — a fresh value per call (later casts never mutate a returned
        census).
        Refuses when: the unknown run ONLY (the same wrap, naming the live
        handles) — NEVER refuses on coverage: the zero-vote run reads back
        all-zero maps over the full universe + the empty log, a VALUE, never
        a refusal (the audit surface must read back even a broken state,
        especially a broken state; that is its job — the op that catches the
        silent-loss and gap classes; every gate's evidence leg rides it).
        Re-run: pure — re-reading is stable between casts; a fresh frozen
        snapshot per call.
        Touches: nothing — a read (side effects: zero).
        Provenance: op 4, G-VOTES condition 4 (the census read-back green),
        votes-brief §4 (the reconciliation — the manifest is U1's own
        read-back, the coverage verdict computes where the quorum lives;
        the census carries the counts as data); discover/votes and
        understand/votes (the legs riding the brief).
        """
        clean_run_id = _require_text(run_id, "run_id")
        manifest = self._read_manifest(clean_run_id)
        manifest_ids = [row.id for row in manifest.items]
        per_pair_counts: dict[Pair, int] = dict.fromkeys(schedule_pairs(manifest_ids), 0)
        per_item_counts: dict[str, int] = dict.fromkeys(manifest_ids, 0)
        vote_log: list[VoteRecord] = []
        for record in self._votes.values():
            if record.run_id != clean_run_id:
                continue
            vote_log.append(record)
            per_pair_counts[record.pair] = per_pair_counts.get(record.pair, 0) + 1
            per_item_counts[record.pair.item_a] = per_item_counts.get(record.pair.item_a, 0) + 1
            per_item_counts[record.pair.item_b] = per_item_counts.get(record.pair.item_b, 0) + 1
        return VoteCensus(
            run_id=clean_run_id,
            per_pair_counts=per_pair_counts,
            per_item_counts=per_item_counts,
            vote_log=tuple(vote_log),
        )
