# Copyright (C) 2026 Mark Losey. All rights reserved.
"""run_store — the wrapper-tier persistence seam: persist the run state across CLI invocations.

The run-store unit (Q-cli-persistence's ruling: FILE-BACKED — a flat JSON run
store, a NEW wrapper-tier surface; the core stays in-memory, zero-dep, untouched
— "no DB" held, a file is not a database). The fence held by construction: the
door composed ONLY (fresh Registry() + Session(registry), register_run,
cast_vote — public only, the stores private); NO persistence verb added to the
five-op door; zero edits to any core module. The write path: SAVE-AT-CAST — the
capture point at cast_vote's OWN return (each subcommand cast IS its own
process; no exit to defer to), one complete line + newline per write, flush —
the crash window bounded to one cast, named honestly. The honesty pin (the
acceptance.py precedent, cited): byte-reproducibility over the FIELD-SELECTED
CLOCK-FREE surface only — the wall-clock stamps (registered_at, recorded_at)
are named and excluded by construction, never the impossible full-log
byte-identity. The corrupt file refuses whole (the pre-pass parses and
validates every line BEFORE the first re-cast — never a silent partial load).
Single-writer BY CONTRACT (the subcommand shape is sequential; a concurrent
double-write surfaces at the next load as the id-sequence refusal — loud,
never silent). Five-field docstrings on every public symbol; zero runtime
dependencies (json + pathlib, stdlib).
The presentation_order field (the order-bias probe's MEASURE instrument):
the vote line carries the cast's WIRE bytes — the pair as cited (the
PRESENTED order), the winner as sent (positional over the presented
order), the presentation_order token naming the form; the load's pre-pass
form-checks the token (the LEGACY pre-field lines' absent field the honest
canonical default — the presentation at every tier WAS the canonical
order), and the in-order re-casts replay the door's presented-to-canonical
mapping identically — the reconstructed record whole.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING, Final, cast

from prioritree.registry import OperatorDeclaration, Registry
from prioritree.session import Session
from prioritree.votes import (
    COMPARATOR_CLASSES,
    PRESENTATION_CANONICAL,
    PRESENTATION_ORDERS,
    PRESENTATION_SWAPPED,
    VOTE_PREFIX,
)

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence

    from prioritree.registry import ItemRow, RunManifest
    from prioritree.scheduler import Pair
    from prioritree.tally import TallyResult
    from prioritree.votes import VoteCensus, VoteRecord

__all__ = [
    "STORE_HOME",
    "Persist",
    "StoreRefusedError",
]

# The store home's default (run-store-brief §2): CWD-relative, per-project
# state — the .git form (visible, gitignore-able, no hidden global). A named
# module-level constant (content-in-configuration); every verb takes the home
# as a PARAMETER — the constant is the command face's default, never a hidden
# global (test isolation).
STORE_HOME: Final[Path] = Path(".prioritree/runs")

# Structural constants (named, per the zero-magic-value-in-src discipline).
_RUN_FILE_PREFIX: Final[str] = "RUN-"
_RUN_FILE_SUFFIX: Final[str] = ".jsonl"
_KIND_MANIFEST: Final[str] = "manifest"
_KIND_VOTE: Final[str] = "vote"
_PAIR_LENGTH: Final[int] = 2


class StoreRefusedError(Exception):
    """StoreRefusedError — the typed refusal: expected, found, next_action.

    Purpose: carry the store's OWN refusal grammar (expected/found/
    next-action) as data the CLI wrapper catches and renders; raised, never
    returned — the store's refusal is the FILE's (the door did not refuse —
    a distinct type keeps the lineage honest: the door's refusals and
    ExhaustedQueue ride through verbatim, never wrapped, never conflated).
    Refuses when: never — it IS the refusal; the message renders all three
    fields so an uncaught traceback still names the legal form.
    Re-run: deterministic — the same violation raises the same three fields.
    Touches: nothing — a plain Exception subclass (zero runtime deps).
    Provenance: the VotesRefusedError precedent (votes.py:106-134, the
    Error-suffix family form, N818), run-store-brief §4 (the store's own
    refusal type); Q-cli-persistence (the seam's ruled shape).
    """

    def __init__(self, expected: str, found: str, next_action: str) -> None:
        """Initialize the refusal with its three named fields.

        Purpose: carry expected/found/next_action plus the rendered message.
        Refuses when: never.
        Re-run: idempotent.
        Touches: nothing.
        Provenance: registry-brief §2 (the typed exception, RefusedError
        precedent); run-store-brief §4.
        """
        self.expected = expected
        self.found = found
        self.next_action = next_action
        _prefix = "refused"
        super().__init__(f"{_prefix} — expected: {expected} | found: {found} | next: {next_action}")


def _repair_path(run_file: Path) -> str:
    """Return the shared next_action for a corrupt-file refusal.

    Purpose: render the repair path once — every pre-pass refusal names it
    (the load refuses the corrupt file whole, never a silent partial load).
    Refuses when: never.
    Re-run: deterministic.
    Touches: nothing.
    Provenance: run-store-brief §4 (the trigger set's shared next-action
    clause), Q-cli-persistence.
    """
    _head = "repair the run file — the load refuses the corrupt file whole, never a silent"
    return f"{_head} partial load ({run_file}); the door re-validates every field at the re-casts"


def _parse_lines(raw: str, run_file: Path) -> list[dict[str, object]]:
    """Parse the whole file's lines into flat objects, refusing the ill-formed.

    Purpose: one flat self-describing JSON object per line (the JSONL
    precedent) — json.loads each line, refuse the parse failure naming the
    line number and the parser's message verbatim; refuse a non-object line.
    Refuses when: a line is not well-formed JSON, or parses to a non-object
    (found carries the line number + the parser's message verbatim).
    Re-run: deterministic.
    Touches: nothing — a read of the bytes already in hand.
    Provenance: run-store-brief §2 (the JSONL form), §4 trigger 1 (parse
    failure) and trigger 4 (wrong types, the non-object line).
    """
    lines: list[dict[str, object]] = []
    for position, raw_line in enumerate(raw.splitlines(), start=1):
        try:
            value = json.loads(raw_line)
        except json.JSONDecodeError as parse_error:
            _expected = f"line {position} well-formed JSON (one flat self-describing object)"
            raise StoreRefusedError(
                expected=_expected,
                found=f"line {position}: {parse_error.msg} — {raw_line!r}",
                next_action=_repair_path(run_file),
            ) from parse_error
        if not isinstance(value, dict):
            _expected = f"line {position} a flat JSON object"
            raise StoreRefusedError(
                expected=_expected,
                found=f"line {position}: a {type(value).__name__} — {raw_line!r}",
                next_action=_repair_path(run_file),
            )
        lines.append(cast("dict[str, object]", value))
    return lines


def _require_str_field(line: Mapping[str, object], field: str, position: int, run_file: Path) -> str:
    """Return the line's string field, refusing the missing or mistyped.

    Purpose: enforce the grammar field's presence and JSON string type.
    Refuses when: the field is missing (trigger 3) or not a string (trigger 4).
    Re-run: deterministic.
    Touches: nothing.
    Provenance: run-store-brief §4 triggers 3-4; the registry school's
    hand-rolled validation precedent (registry.py:118-133).
    """
    if field not in line:
        _expected = f"a '{field}' field on line {position}"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: the field is missing",
            next_action=_repair_path(run_file),
        )
    value = line[field]
    if not isinstance(value, str):
        _expected = f"the '{field}' field a JSON string"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: {value!r}",
            next_action=_repair_path(run_file),
        )
    return value


def _require_optional_str_field(
    line: Mapping[str, object],
    field: str,
    position: int,
    run_file: Path,
) -> str | None:
    """Return the line's string-or-None field, refusing the missing or mistyped.

    Purpose: enforce the optional field's presence and JSON type (a string or
    null — the notes/supersedes wire form).
    Refuses when: the field is missing (trigger 3) or neither string nor null
    (trigger 4).
    Re-run: deterministic.
    Touches: nothing.
    Provenance: run-store-brief §2 (the seven cast fields on the wire), §4
    triggers 3-4.
    """
    if field not in line:
        _expected = f"a '{field}' field on line {position}"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: the field is missing",
            next_action=_repair_path(run_file),
        )
    value = line[field]
    if value is not None and not isinstance(value, str):
        _expected = f"the '{field}' field a JSON string or null"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: {value!r}",
            next_action=_repair_path(run_file),
        )
    return value


def _require_int_field(line: Mapping[str, object], field: str, position: int, run_file: Path) -> int:
    """Return the line's integer field, refusing the missing or mistyped.

    Purpose: enforce the grammar field's presence and JSON integer type (bool
    refused — the registry's quorum precedent).
    Refuses when: the field is missing (trigger 3), not an integer, or a bool
    (trigger 4).
    Re-run: deterministic.
    Touches: nothing.
    Provenance: run-store-brief §4 triggers 3-4; registry.py:274-294 (the
    bool-refusing integer check precedent).
    """
    if field not in line:
        _expected = f"a '{field}' field on line {position}"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: the field is missing",
            next_action=_repair_path(run_file),
        )
    value = line[field]
    if isinstance(value, bool) or not isinstance(value, int):
        _expected = f"the '{field}' field a JSON integer"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: {value!r}",
            next_action=_repair_path(run_file),
        )
    return value


def _require_pair_field(line: Mapping[str, object], field: str, position: int, run_file: Path) -> tuple[str, str]:
    """Return the line's pair field as (item_a, item_b), refusing the malformed.

    Purpose: enforce the pair's wire form — a 2-length JSON array of strings,
    canonical, AS SENT (never re-ordered; the door's swapped-citation check
    re-fires at the re-casts).
    Refuses when: the field is missing, not a 2-length array, or its members
    are not strings (triggers 3-4).
    Re-run: deterministic.
    Touches: nothing.
    Provenance: run-store-brief §2 (the pair as [item_a, item_b], canonical),
    §4 triggers 3-4; the _coerce_pair precedent (votes.py:160-190).
    """
    if field not in line:
        _expected = f"a '{field}' field on line {position}"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: the field is missing",
            next_action=_repair_path(run_file),
        )
    value = line[field]
    if not isinstance(value, list):
        _expected = f"the '{field}' field a 2-length JSON array of strings"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: {value!r}",
            next_action=_repair_path(run_file),
        )
    members = cast("list[object]", value)
    if len(members) != _PAIR_LENGTH or not isinstance(members[0], str) or not isinstance(members[1], str):
        _expected = f"the '{field}' field a 2-length JSON array of strings"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: {value!r}",
            next_action=_repair_path(run_file),
        )
    return (members[0], members[1])


def _read_presentation_order_field(line: Mapping[str, object], position: int, run_file: Path) -> str:
    """Read the line's presentation_order — the absent field the honest canonical default.

    Purpose: the pre-field corpus's honest read — the LEGACY lines (written
    before the field existed) carry no presentation_order, and the
    presentation at every tier WAS the canonical order by construction
    (the pair IS the order at the canonical form) — the absent field reads
    back 'canonical', never a refusal; a PRESENT field must be a string
    from the legal presentation set (the form check — trigger 4's form, an
    unknown token naming the legal set).
    Refuses when: the field is present but not a string from
    PRESENTATION_ORDERS.
    Re-run: deterministic.
    Touches: nothing — a pure validation over its arguments.
    Provenance: run-store-brief §4 triggers 3-4 (the form-check school),
    the order-bias probe's MEASURE instrument (the design synthesis §2.2's
    load clause — the legacy corpus loads clean, the absent field the
    honest default).
    """
    if "presentation_order" not in line:
        return PRESENTATION_CANONICAL
    value = line["presentation_order"]
    if not isinstance(value, str) or value not in PRESENTATION_ORDERS:
        _expected = f"the 'presentation_order' field a JSON string from {sorted(PRESENTATION_ORDERS)}"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: {value!r}",
            next_action=_repair_path(run_file),
        )
    return value


def _require_items_field(line: Mapping[str, object], position: int, run_file: Path) -> list[tuple[str, str]]:
    """Return the manifest's items as (id, label) pairs, payload order preserved.

    Purpose: enforce the items' wire form — a JSON array of [id, label]
    arrays, the payload order the round-trip's equality surface asserts.
    Refuses when: the field is missing, not an array, or a member is not a
    2-length array of strings (triggers 3-4).
    Re-run: deterministic.
    Touches: nothing.
    Provenance: run-store-brief §2 (items [[id, label], ...] — payload order
    preserved), §4 triggers 3-4.
    """
    if "items" not in line:
        _expected = "an 'items' field on the manifest line"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: the field is missing",
            next_action=_repair_path(run_file),
        )
    value = line["items"]
    if not isinstance(value, list):
        _expected = "the 'items' field a JSON array of [id, label] arrays"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: {value!r}",
            next_action=_repair_path(run_file),
        )
    rows: list[tuple[str, str]] = []
    raw_rows = cast("list[object]", value)
    for slot, row in enumerate(raw_rows):
        if (
            not isinstance(row, list)
            or len(cast("list[object]", row)) != _PAIR_LENGTH
            or not isinstance(cast("list[object]", row)[0], str)
            or not isinstance(cast("list[object]", row)[1], str)
        ):
            _expected = f"items[{slot}] a 2-length JSON array of strings"
            raise StoreRefusedError(
                expected=_expected,
                found=f"line {position}: {row!r}",
                next_action=_repair_path(run_file),
            )
        members = cast("list[str]", row)
        rows.append((members[0], members[1]))
    return rows


def _require_verdicts_field(line: Mapping[str, object], position: int, run_file: Path) -> list[str]:
    """Return the operator's declared verdicts as the sorted-wire array.

    Purpose: enforce the verdicts' wire form — a JSON array of strings (the
    frozenset serialized SORTED for deterministic bytes, restored type-exact
    as a frozenset at the re-register; the store never constructs the frozen
    value itself — the door re-derives it).
    Refuses when: the field is missing, not an array, or a member is not a
    string (triggers 3-4).
    Re-run: deterministic.
    Touches: nothing.
    Provenance: run-store-brief §2 (the frozenset as a SORTED array on the
    wire), §4 triggers 3-4.
    """
    if "verdicts" not in line:
        _expected = "a 'verdicts' field on the operator object"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: the field is missing",
            next_action=_repair_path(run_file),
        )
    value = line["verdicts"]
    if not isinstance(value, list) or any(not isinstance(member, str) for member in cast("list[object]", value)):
        _expected = "the 'verdicts' field a JSON array of strings"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: {value!r}",
            next_action=_repair_path(run_file),
        )
    return cast("list[str]", value)


def _require_operator_field(line: Mapping[str, object], position: int, run_file: Path) -> dict[str, object]:
    """Return the manifest's operator object, refusing the missing or mistyped.

    Purpose: enforce the operator's wire form — a flat JSON object (its id,
    question, verdicts validated by their own field helpers).
    Refuses when: the field is missing or not an object (triggers 3-4).
    Re-run: deterministic.
    Touches: nothing.
    Provenance: run-store-brief §2 (operator: id, question, verdicts), §4
    triggers 3-4.
    """
    if "operator" not in line:
        _expected = "an 'operator' field on the manifest line"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: the field is missing",
            next_action=_repair_path(run_file),
        )
    value = line["operator"]
    if not isinstance(value, dict):
        _expected = "the 'operator' field a flat JSON object (id, question, verdicts)"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: {value!r}",
            next_action=_repair_path(run_file),
        )
    return cast("dict[str, object]", value)


def _validate_vote_line(
    line: Mapping[str, object],
    position: int,
    ground: tuple[str, frozenset[str], set[str], Mapping[str, tuple[str, str]]],
    run_file: Path,
) -> tuple[str, tuple[str, str], str, str, str, str | None, str | None, str]:
    """Validate one vote line against the manifest's ground, refusing the corrupt.

    Purpose: the pre-pass's per-line core — extract the nine grammar fields
    (the seven cast fields + the two stamps carried as data + the
    presentation_order token — the absent field the honest canonical
    default), then the six
    value triggers: the winner from the manifest's declared verdicts, the
    comparator_class from the ruled class set, the pair's ids from the
    manifest's items, the supersedes resolving to an EARLIER line's pair,
    the vote_id in mint order (VOTE-{i+1:04d} — gaps, dups, disorder all
    refused: a shifted re-mint would orphan every correction), and the
    run_id matching the manifest's; every refusal in the three-field
    grammar naming the line; the accumulated earlier_pairs consulted for
    the supersedes ground truth (an earlier line's pair, same run).
    Refuses when: any field missing or mistyped (the field helpers' own
    refusals); any value trigger violated — each raising StoreRefusedError
    before any byte rebuilds (the pre-pass's own law: the re-casts cannot
    refuse mid-rebuild).
    Re-run: deterministic — the same line against the same ground raises
    the same verdict.
    Touches: nothing — a pure validation over its arguments.
    Provenance: run-store-brief §4 (the trigger set, the pre-pass), the
    C901 extraction precedent (tally's _dominance_adjacency — the load
    restructure cure).
    """
    manifest_run_id, declared_verdicts_set, item_id_set, earlier_pairs = ground
    vote_id = _require_str_field(line, "vote_id", position, run_file)
    vote_run_id = _require_str_field(line, "run_id", position, run_file)
    pair = _require_pair_field(line, "pair", position, run_file)
    winner = _require_str_field(line, "winner", position, run_file)
    comparator_id = _require_str_field(line, "comparator_id", position, run_file)
    comparator_class = _require_str_field(line, "comparator_class", position, run_file)
    _recorded_at = _require_str_field(line, "recorded_at", position, run_file)
    notes = _require_optional_str_field(line, "notes", position, run_file)
    supersedes = _require_optional_str_field(line, "supersedes", position, run_file)
    presentation_order = _read_presentation_order_field(line, position, run_file)
    if winner not in declared_verdicts_set:
        _expected = f"a winner from the manifest's declared verdicts {sorted(declared_verdicts_set)}"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: winner got {winner!r}",
            next_action=_repair_path(run_file),
        )
    if comparator_class not in COMPARATOR_CLASSES:
        _expected = f"a comparator_class from {sorted(COMPARATOR_CLASSES)}"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: comparator_class got {comparator_class!r}",
            next_action=_repair_path(run_file),
        )
    if pair[0] not in item_id_set or pair[1] not in item_id_set:
        _expected = f"a pair of ids from the manifest's {len(item_id_set)} items"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: pair got {list(pair)!r}",
            next_action=_repair_path(run_file),
        )
    if supersedes is not None:
        target_pair = earlier_pairs.get(supersedes)
        if target_pair is None or target_pair != pair:
            _expected = "a supersedes resolving to an EARLIER vote line, same run, same pair"
            raise StoreRefusedError(
                expected=_expected,
                found=f"line {position}: supersedes got {supersedes!r}",
                next_action=_repair_path(run_file),
            )
    expected_vote_id = f"{VOTE_PREFIX}{position - 1:04d}"
    if vote_id != expected_vote_id:
        _expected = f"line {position - 1}'s vote_id to be {expected_vote_id} (mint order, no gaps, no dups)"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: vote_id got {vote_id!r}",
            next_action=_repair_path(run_file),
        )
    if vote_run_id != manifest_run_id:
        _expected = f"every vote line's run_id to match the manifest's ({manifest_run_id!r})"
        raise StoreRefusedError(
            expected=_expected,
            found=f"line {position}: run_id got {vote_run_id!r}",
            next_action=_repair_path(run_file),
        )
    return (vote_id, pair, winner, comparator_id, comparator_class, notes, supersedes, presentation_order)


class Persist:
    """Persist — the run's file-backed container: the door composed, the bytes appended.

    Purpose: Persist the run state across CLI invocations — ONE JSONL file per
    run (the manifest line FIRST, then one vote line per cast in mint order),
    the door composed ONLY (fresh Registry() + Session(registry) at the
    factories; the reads delegate through the door — the manifest read the
    one held-record exception (register_run's own mint, re-minted at load's
    reconstruction); no core store attribute ever touched — the fence held
    by construction); SAVE-AT-CAST: the capture
    point at cast_vote's OWN return, one write of one complete line + newline,
    flush (the crash window bounded to one cast, named); acknowledged=True
    appends NOTHING (the dedup IS the idempotence); the failed append refuses
    loudly; single-writer BY CONTRACT; the round-trip property over the
    FIELD-SELECTED CLOCK-FREE surface (the stamps named and excluded by
    construction — registered_at, recorded_at re-mint at the re-register and
    the re-casts); the corrupt file refused whole (the pre-pass before the
    first re-cast); the two id spaces named, never conflated (the in-file
    run_id the door's verbatim handle; the file's stem the cross-process
    identity).
    Refuses when: StoreRefusedError — the store's OWN refusal (the missing
    file at load, the corrupt file's trigger set, the failed append); the
    door's refusals (VotesRefusedError, TallyRefusedError) and ExhaustedQueue
    ride through VERBATIM, BY TYPE, never wrapped (the lineage kept honest).
    Re-run: the reads are the door's (pure over its stores); cast is
    append-only at both tiers; load reconstructs identically over the
    clock-free surface (the round-trip property, run-store-brief §3).
    Touches: only its own run file (append-only; the manifest line written
    once at register) — no core store, no subprocess, no DB; the core stays
    untouched.
    Provenance: Q-cli-persistence (FILE-BACKED, the seam's ruling),
    G-RUN-STORE (the four conditions), run-store-brief §1-§4 (the container,
    the mechanics, the round-trip, the refusals), the naming law ("Persist
    the run state across CLI invocations" — the act's first word).
    """

    def __init__(self, session: Session, handle: str, run_file: Path, manifest: RunManifest) -> None:
        """Initialize the container over the injected parts.

        Purpose: hold the door's session, the run's in-file handle (the door's
        verbatim run_id), the run file's path, and the run's frozen ground (the
        RunManifest register_run mints — captured whole at BOTH factories:
        register's own mint, load's reconstruction — the parts injected; the
        factories compose (store-as-parameter; never a module-level
        singleton — test isolation).
        Refuses when: never.
        Re-run: idempotent — a fresh container over the given parts.
        Touches: only its own references.
        Provenance: run-store-brief §1 (the container's constructor, the
        parts-injected ruling), the ux build's sixth query (the manifest held
        from construction), G-RUN-STORE.
        """
        self._session = session
        self._handle = handle
        self._run_file = run_file
        self._manifest = manifest

    @classmethod
    def register(
        cls,
        store_home: Path,
        items: Sequence[Sequence[str] | ItemRow],
        operator: OperatorDeclaration,
        quorum: int = 1,
    ) -> Persist:
        """Register the run at the door and write its manifest line.

        Purpose: compose the door fresh (Registry() + Session(registry)),
        register_run (the door's refusals riding through verbatim — raised
        before any byte lands), mint the FILE name per the store-home scan
        (max RUN-{n} + 1 — the store's own mint, continuing post-load: the
        dir is the truth), and write the manifest line ONCE (one write of one
        complete line + newline, flush) — the door's own run_id riding the
        line verbatim (the accepted oddity named: file RUN-0007.jsonl's lines
        may say RUN-0001 — the equality surface is door-side, translation
        buys no stability).
        Refuses when: the door refuses registration (VotesRefusedError,
        verbatim — before any byte lands); the append refuses loudly
        (StoreRefusedError, the OS error verbatim).
        Re-run: deterministic given the store home's state; the file-name
        mint continues the home's max (the dir is the truth).
        Touches: the store home (created if absent) and the new run file —
        nothing of the core's.
        Provenance: run-store-brief §1 (the register factory), §2 (the
        file-name mint, the manifest line written ONCE), §3 (the two id
        spaces), Q-cli-persistence, G-RUN-STORE condition 2.
        """
        session = Session(Registry())
        run_id, manifest, _count = session.register_run(items, operator, quorum)
        store_home.mkdir(parents=True, exist_ok=True)
        run_file = store_home / f"{_RUN_FILE_PREFIX}{cls._scan_next_run_number(store_home):04d}{_RUN_FILE_SUFFIX}"
        persist = cls(session, run_id, run_file, manifest)
        manifest_line = {
            "kind": _KIND_MANIFEST,
            "run_id": manifest.run_id,
            "items": [[row.id, row.label] for row in manifest.items],
            "operator": {
                "id": manifest.operator.id,
                "question": manifest.operator.question,
                "verdicts": sorted(manifest.operator.verdicts),
            },
            "quorum": manifest.quorum,
            "registered_at": manifest.registered_at,
        }
        persist._append_line(
            manifest_line,
            expected="the manifest line durable on disk at register_run's return (the single write, once)",
        )
        return persist

    @classmethod
    def load(cls, store_home: Path, run_id: str) -> Persist:
        """Load the run's file into a fresh single-run session, refusing the corrupt file whole.

        Purpose: the pre-pass — read the whole file, refuse truncation (the
        crash-tail: the last line without its newline), parse every line
        (trigger 1), then validate BEFORE any re-cast: the manifest line
        first and not duplicated (trigger 6), every grammar field present
        and rightly typed (triggers 3-4), the value-set triggers (winner
        outside the declared verdicts; comparator_class outside the class
        set; the pair's ids outside the manifest's items), the orphaned
        supersedes (not resolving to an EARLIER line, same run, same pair —
        trigger 5), the id-sequence violations (line i's vote_id !=
        VOTE-{i+1:04d}; a vote line's run_id != the manifest's — trigger 6);
        then the reconstruction — a fresh door, register_run from the wire's
        arrays (the door re-derives every frozen type; the stamps RE-MINTED
        — named and excluded from the equality surface), the minted
        RunManifest CAPTURED (the container's own holding — the manifest
        accessor's return), then the in-order re-casts through the door
        (the dedup index rebuilt BY the re-casts themselves; a doubled line
        absorbs loudly as the ack — the count unchanged, never
        double-counted).
        Refuses when: the file is missing (found renders the home's live
        set); the file is corrupt — every trigger in StoreRefusedError's
        three-field grammar, found carrying the line number + the parser's
        message verbatim; the container never constructed on refusal (the
        partial load unrepresentable). The door's own re-registration
        refusals ride through verbatim (the pre-pass validated structure;
        the door re-fires its checks identically, never bypassed).
        Re-run: deterministic given the file — the clock-free surface
        reconstructs identically (the round-trip property); the stamps
        (registered_at, recorded_at) are carried as data, validated for
        type, never for value, and re-minted at reconstruction.
        Touches: only the run file (a read) and the fresh in-memory stores.
        Provenance: run-store-brief §3 (the round-trip property, the
        field-selected equality surface), §4 (the pre-pass, the trigger
        set), Q-cli-persistence, G-RUN-STORE conditions 2-3.
        """
        run_file = store_home / f"{run_id}{_RUN_FILE_SUFFIX}"
        if not run_file.is_file():
            live: list[str] = (
                sorted(path.stem for path in store_home.glob(f"{_RUN_FILE_PREFIX}*{_RUN_FILE_SUFFIX}"))
                if store_home.is_dir()
                else []
            )
            _live_rendered = ", ".join(live) if live else "(none on disk)"
            _expected = f"a run file in the store home (live: {_live_rendered})"
            _head = "register a run first, or cite a live RUN-{####} id — the home is the"
            raise StoreRefusedError(
                expected=_expected,
                found=f"no run file for {run_id!r} in {store_home}",
                next_action=f"{_head} truth (the dir, never a hidden global)",
            )
        raw = run_file.read_text(encoding="utf-8")
        if raw and not raw.endswith("\n"):
            tail_lines = raw.splitlines()
            _expected = "the file's last line complete with its newline (one write of one complete line per append)"
            _tail = tail_lines[-1] if tail_lines else raw
            raise StoreRefusedError(
                expected=_expected,
                found=f"line {len(tail_lines)}: the crash-tail is truncated — {_tail!r}",
                next_action=_repair_path(run_file),
            )
        lines = _parse_lines(raw, run_file)
        if not lines or lines[0].get("kind") != _KIND_MANIFEST:
            _expected = "the manifest line (kind='manifest') FIRST — one manifest per run file"
            _found_head = "no manifest line first"
            raise StoreRefusedError(
                expected=_expected,
                found=f"{_found_head} — the file is empty or its first line is not a manifest",
                next_action=_repair_path(run_file),
            )
        manifest_line = lines[0]
        manifest_position = 1
        manifest_run_id = _require_str_field(manifest_line, "run_id", manifest_position, run_file)
        manifest_items = _require_items_field(manifest_line, manifest_position, run_file)
        operator_object = _require_operator_field(manifest_line, manifest_position, run_file)
        operator_id = _require_str_field(operator_object, "id", manifest_position, run_file)
        operator_question = _require_str_field(operator_object, "question", manifest_position, run_file)
        declared_verdicts = _require_verdicts_field(operator_object, manifest_position, run_file)
        quorum_value = _require_int_field(manifest_line, "quorum", manifest_position, run_file)
        _registered_at = _require_str_field(manifest_line, "registered_at", manifest_position, run_file)
        declared_verdicts_set = frozenset(declared_verdicts)
        item_id_set = {item_id for item_id, _label in manifest_items}
        votes: list[tuple[tuple[str, str], str, str, str, str | None, str | None, str]] = []
        earlier_pairs: dict[str, tuple[str, str]] = {}
        ground = (manifest_run_id, declared_verdicts_set, item_id_set, earlier_pairs)
        for index, line in enumerate(lines[1:]):
            position = index + 2
            if line.get("kind") == _KIND_MANIFEST:
                _expected = "ONE manifest line (first, never duplicated)"
                raise StoreRefusedError(
                    expected=_expected,
                    found=f"line {position}: a duplicated manifest line",
                    next_action=_repair_path(run_file),
                )
            if line.get("kind") != _KIND_VOTE:
                _expected = "a kind tag of 'manifest' (first line) or 'vote' (every later line)"
                raise StoreRefusedError(
                    expected=_expected,
                    found=f"line {position}: kind got {line.get('kind')!r}",
                    next_action=_repair_path(run_file),
                )
            fields = _validate_vote_line(
                line,
                position,
                ground,
                run_file,
            )
            vote_id, pair, winner, comparator_id, comparator_class, notes, supersedes, presentation_order = fields
            earlier_pairs[vote_id] = pair
            votes.append((pair, winner, comparator_id, comparator_class, notes, supersedes, presentation_order))
        # The reconstruction — a fresh door; the door re-derives every frozen
        # type at register_run/cast_vote (the wire's arrays feed the signatures
        # directly; the store never constructs a frozen value itself); the
        # stamps RE-MINTED here (named and excluded from the equality surface).
        session = Session(Registry())
        operator = OperatorDeclaration(
            id=operator_id,
            question=operator_question,
            verdicts=declared_verdicts_set,
        )
        _new_run_id, manifest, _count = session.register_run(manifest_items, operator, quorum_value)
        # The in-order re-casts through the door — the dedup index rebuilt BY
        # the re-casts themselves (the key's members are the eight fields,
        # neither stamp nor id; the file never carries it); a doubled line
        # (the crash-retry form) absorbs loudly as the ack — the count
        # unchanged, never double-counted (R9 at the file tier); the
        # presented-to-canonical mapping replaying identically (the wire's
        # bytes the re-cast's own input).
        for pair, winner, comparator_id, comparator_class, notes, supersedes, presentation_order in votes:
            session.cast_vote(
                manifest_run_id,
                list(pair),
                winner,
                comparator_id,
                comparator_class,
                notes,
                supersedes,
                presentation_order,
            )
        return cls(session, manifest_run_id, run_file, manifest)

    def _append_line(self, line: Mapping[str, object], expected: str) -> None:
        """Append one complete line to the run file — the single synchronous write.

        Purpose: serialize the flat object with json.dumps(..., sort_keys=True)
        (deterministic bytes), open-append, ONE write of one complete line +
        newline, flush, close — one synchronous act; the failed append refuses
        loudly (three fields: expected the line; found the OS error verbatim;
        next_action the repair path) — never swallowed.
        Refuses when: the write or flush raises (StoreRefusedError, the OS
        error verbatim — found names the divergence: the cast lives in memory,
        not on disk).
        Re-run: deterministic in bytes (sort_keys) — the append itself is
        idempotent in effect only through the ack rule (a byte-identical
        re-send appends NOTHING).
        Touches: only the run file (append mode).
        Provenance: run-store-brief §2 (the write path, the failed append's
        loud refusal), Q-cli-persistence.
        """
        payload = json.dumps(line, sort_keys=True) + "\n"
        try:
            with self._run_file.open("a", encoding="utf-8") as handle:
                handle.write(payload)
                handle.flush()
        except OSError as write_error:
            raise StoreRefusedError(
                expected=expected,
                found=f"{write_error!r} — the vote lives in memory, not on disk",
                next_action=_repair_path(self._run_file),
            ) from write_error

    @staticmethod
    def _scan_next_run_number(store_home: Path) -> int:
        """Return the store home's next file number — max RUN-{n} + 1.

        Purpose: the FILE-NAME mint is the store's own — the store-home scan
        (the dir is the truth), continuing post-load (the door's
        fresh-session mint cannot continue across files — named, the
        single-run form's own consequence).
        Refuses when: never — a scan over the home's listing.
        Re-run: deterministic given the home's state.
        Touches: nothing — a directory read.
        Provenance: run-store-brief §2 (the id ruling — the file-name mint),
        the per-store max+1 precedent (registry.py:136-146).
        """
        best = 0
        if store_home.is_dir():
            for path in store_home.glob(f"{_RUN_FILE_PREFIX}*{_RUN_FILE_SUFFIX}"):
                digits = path.stem[len(_RUN_FILE_PREFIX) :]
                if digits.isdigit() and int(digits) > best:
                    best = int(digits)
        return best + 1

    def cast(
        self,
        pair: Pair | Sequence[str],
        winner: str,
        comparator_id: str,
        comparator_class: str,
        notes: str | None = None,
        supersedes: str | None = None,
        presentation_order: str = PRESENTATION_CANONICAL,
    ) -> tuple[str, VoteRecord, int, bool]:
        """Cast the vote at the door and append its line at the cast's return.

        Purpose: SAVE-AT-CAST — the capture point at cast_vote's OWN return:
        delegate to the door's cast_vote (the quadruple returned verbatim),
        then append the line (one complete line + newline, flush); on the
        acknowledged=True ack NOTHING appends (the line is already durable —
        the dedup IS the idempotence; the cleaner file wins); the line
        carries the cast's WIRE bytes WHOLE (the cast fields in mint order,
        the pair as cited — the PRESENTED order, presentation_order naming
        it; the winner as sent — positional over the presented order; the
        recorded_at stamp carried as data — the faithful record: the load's
        re-cast replays the door's presented-to-canonical mapping
        identically, the record reconstructed whole).
        Refuses when: the door refuses (VotesRefusedError rides through
        verbatim, BY TYPE, before any byte lands); the append fails
        (StoreRefusedError, the OS error verbatim — never swallowed).
        Re-run: deterministic given the store state; a byte-identical re-send
        is the door's loud ack (appended nothing) — R9 at the file tier.
        Touches: the run file (append) and the door's own stores — nothing
        else.
        Provenance: run-store-brief §1 (the cast verb), §2 (save-at-cast, the
        ack rule, the line bytes), Q-cli-persistence, G-RUN-STORE condition 2.
        """
        vote_id, record, count, acknowledged = self._session.cast_vote(
            self._handle,
            pair,
            winner,
            comparator_id,
            comparator_class,
            notes,
            supersedes,
            presentation_order,
        )
        if acknowledged:
            return vote_id, record, count, acknowledged
        # The cited pair — the wire's own bytes (the presented order),
        # derived from the record's canonical pair + the token (the door's
        # mapping's own inverse; the load's re-cast replays the mapping
        # identically — the record reconstructed whole).
        cited_a, cited_b = (
            (record.pair.item_b, record.pair.item_a)
            if presentation_order == PRESENTATION_SWAPPED
            else (record.pair.item_a, record.pair.item_b)
        )
        vote_line = {
            "kind": _KIND_VOTE,
            "vote_id": record.vote_id,
            "run_id": record.run_id,
            "pair": [cited_a, cited_b],
            "winner": winner,
            "comparator_id": record.comparator_id,
            "comparator_class": record.comparator_class,
            "recorded_at": record.recorded_at,
            "notes": record.notes,
            "supersedes": record.supersedes,
            "presentation_order": presentation_order,
        }
        self._append_line(
            vote_line,
            expected=f"the vote line for {vote_id} durable on disk at cast_vote's return (one complete line, flushed)",
        )
        return vote_id, record, count, acknowledged

    def serve(self, seed: int | None = None) -> tuple[str, str, int]:
        """Serve the next under-quorum pair.

        Purpose: delegate to the door's next_pair verbatim — the same store
        state yields the same pair; after a crash the file is the truth and
        the re-served pair is deterministic.
        Refuses when: the door refuses (VotesRefusedError, BY TYPE, never
        wrapped); the queue exhausted — ExhaustedQueue rides through BY TYPE
        (the DONE signal, never a refusal, never swallowed).
        Re-run: pure between casts — the door's semantics verbatim.
        Touches: nothing — a read through the door.
        Provenance: run-store-brief §1 (the serve verb), Q-cli-shape (each
        cast its own process), G-RUN-STORE condition 2.
        """
        return self._session.next_pair(self._handle, seed)

    def census(self) -> VoteCensus:
        """Census the run's vote state.

        Purpose: delegate to the door's read_vote_state verbatim — the fresh
        frozen snapshot (the counts as data, the full vote log in mint
        order); the round-trip's equality surface (the maps byte-identical
        before/after; the vote_log byte-identical only over its clock-free
        fields — the stamps named and excluded).
        Refuses when: the door refuses (VotesRefusedError, BY TYPE) — never
        on coverage: the manifest-only file loads to the all-zero maps + the
        empty log, a VALUE.
        Re-run: pure — re-reading is stable between casts.
        Touches: nothing — a read through the door.
        Provenance: run-store-brief §1 (the census verb), §3 (the equality
        surface), G-RUN-STORE condition 2.
        """
        return self._session.read_vote_state(self._handle)

    def rank(self) -> TallyResult:
        """Rank the run by its tallied votes.

        Purpose: delegate to the door's tally_rank verbatim — the frozen
        TallyResult WHOLE (tally_votes consumes no stamp; the ranking is
        byte-identical across the round trip).
        Refuses when: the door refuses (VotesRefusedError, BY TYPE);
        the coverage gate fails — TallyRefusedError rides through VERBATIM
        (the SAFE HALT, never swallowed, never wrapped).
        Re-run: pure — same store state yields the byte-identical emission.
        Touches: nothing — a read through the door.
        Provenance: run-store-brief §1 (the rank verb), §3 (the TallyResult
        whole on the equality surface), G-RUN-STORE condition 2.
        """
        return self._session.tally_rank(self._handle)

    def manifest(self) -> RunManifest:
        """Manifest the run's frozen ground — the container's own held record, whole.

        Purpose: return the run's RunManifest VERBATIM — the container's own
        holding (minted at register_run, captured at BOTH factories: register's
        own mint, load's reconstruction — the clock-free fields re-derived
        identically at every load, the stamp named and excluded from any
        equality claim). The sixth query's store-tier read: the face route's
        five-key body builds from this whole, the elisions (the operator id,
        the registration stamp) riding at the FACE alone — the store tier
        returns the frozen whole, never projecting.
        Refuses when: never — the record IS the container's own holding (the
        pre-pass already refused the corrupt file whole at load; this read
        adds no refusal of its own).
        Re-run: deterministic given the store state — the clock-free surface
        re-derives identically at every load (the round-trip property held).
        Touches: nothing — a read of the container's own holding.
        Provenance: the service unit brief §1-§2 (the sixth query's
        store-tier accessor), the ux design §2 (the mechanism named),
        run-store-brief §1 (the verb tail), the naming law ("Manifest the
        run's frozen ground" — the act's first word), G-RUN-STORE.
        """
        return self._manifest

    @property
    def run_id(self) -> str:
        """Run id — the file's name, the cross-process identity.

        Purpose: return the run file's stem (the EXTERNAL id — the
        cross-process identity the command face cites); the two id spaces
        named, never conflated (the in-file run_id is the door's ephemeral
        single-run handle; the stem is the run's own address).
        Refuses when: never — the file's own name.
        Re-run: deterministic — the stem is unchanged by construction.
        Touches: nothing — a read of the injected path.
        Provenance: run-store-brief §1 (the run_id property), §3 (the two id
        spaces), G-RUN-STORE.
        """
        return self._run_file.stem
