# Copyright (C) 2026 Mark Losey. All rights reserved.
"""vote_query.py — the axis-query engine over the vote data (FR-MEM-0043's cure).

The vote-data query surface (the axis-query build, packet
recommend/calc-ops, route order-bias-probe, 2026-11-26): the census
serves total + per-item only, so every analytical question over the
class x presentation x pair axes was re-derived by hand at the seats
(FR-MEM-0043 — the collaborator's challenge, verbatim: "how is that
not just a single call with a number returned"). THIS engine is that
single call — the calculate engine's own school (Q-CALC-1, 2026-09-28
+ the Q-CALC-EXPANSION provenance law, 2026-11-25 — the harness lane,
prioritree's own code, zero product bytes):

  pure          no store, no session, no mutation — the run file and
                the items source read whole, nothing touched.
  deterministic the same inputs (the same file bytes + the same
                items) always return the same trace bytes — NO
                timestamp.
  fixed-argv    --flag=value only; no shell, no subprocess; stdlib
                only.
  output        THE TRACE LINE, and only the trace line, on stdout —
                {"op","args","result"} compact JSON: the op, the raw
                flag values as sent, the result (the provenance
                inseparable from the table).

THE OP — cell-table: the structured table over the run file's votes —
every pair x class x presentation -> count + the winners list per cell
(the DOUBLES visible: a cell's winners list showing both votes).
THE CELL RULE'S GROUND IS SERVED, NEVER THE RULE: each cell's winners
list carries the votes' winners AS RECORDED — positional over the
SERVED pair, never mapped to the canonical — so the flips analysis
(the concordance, the unanimous/split doubles rule) stays the analysis
seats' (keisan's), built on the quoted table.

  the grid      every pair of the items (the items' index order, i <
                j) x every observed comparator_class (sorted) x every
                observed presentation_order (sorted; an ABSENT
                presentation_order reads canonical — the honest
                default, the product's own load pre-pass form). The
                empty cells ride at count 0 (the remaining-cells list
                derivable at this one call); a run with no votes
                serves the empty table, never a refusal.
  the trace     {"op":"cell-table","args":{...},"result":
                {"total_votes":N,"cells":[{"pair":[a,b],"class":c,
                "presentation":p,"count":n,"winners":[...]},...]}}

REFUSALS (the doctrine shape — REFUSED / Expected / Found /
Next-action on stderr, stdout byte-empty, exit 1; never a traceback):
  - an unreadable run file; an items source that is neither a JSON id
    array nor a readable manifest file; a manifest file with no
    manifest line, or a non-JSON line.
  - a run-file line that is not a JSON object, or whose kind is
    neither manifest nor vote.
  - a vote's consumed fields mistyped or outside the ruled sets:
    comparator_class from {human, llm} (the class stamp's schema);
    presentation_order from {canonical, swapped}; winner from the
    standing verdict trio {prefer-a, prefer-b, tie} (the tally's own
    win/loss/tie axes — a file carrying otherwise is corrupt, and the
    product's own load refuses it first).
  - a pair id outside the items list (the integrity contract — a vote
    over an unregistered item is corrupt, never silently dropped); a
    pair carrying one item twice.
  - an items list under two entries, with an empty id, or with
    duplicate ids (the register's own law re-carried).

Usage:
    uv run python .opencode/scripts/vote_query.py cell-table \
        --run-file=<the run file's path> --items=<the id list | the manifest file's path>
    (the seat-facing form: the vote_query tool's cell-table op — the wrapper
    fires this engine; the registration rides opencode.json's seat maps)

Exit codes: 0 = the trace line on stdout; 1 = a named refusal
(fail-loud, on stderr); 2 = unusable invocation (argparse).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Callable

_KIND_MANIFEST = "manifest"
_KIND_VOTE = "vote"
_MINIMUM_ITEMS = 2
_PAIR_ARITY = 2
_CLASSES = ("human", "llm")
_PRESENTATIONS = ("canonical", "swapped")
_PRESENTATION_DEFAULT = "canonical"
_VERDICTS = ("prefer-a", "prefer-b", "tie")


def _refuse(expected: str, found: str, next_action: str) -> int:
    """Refuse — print the doctrine-shaped block on stderr; stdout stays byte-empty.

    Purpose: the school's one refusal form — REFUSED / Expected /
    Found / Next-action on stderr, exit 1, stdout byte-empty (never a
    traceback, never a partial table on the pipe).
    Refuses when: never — this is the refusal's own printer.
    Re-run: deterministic — the same inputs print the same refusal bytes.
    Touches: stderr only.
    Provenance: the calculate engine's _refuse (Q-CALC-1, 2026-09-28).
    """
    sys.stderr.write(f"REFUSED\nExpected: {expected}\nFound: {found}\nNext-action: {next_action}\n")
    return 1


def _normalize_ids(elements: list[object], source: str) -> list[str] | None:
    """Normalize the items entries — the id itself, or the manifest's [id, label] pair.

    Purpose: one ordered id list from either items form — a bare id
    (a string) or the manifest's [id, label] pair (the id at the first
    position); the register's own law re-carried — at least two ids,
    none empty, all unique.
    Refuses when: an entry is neither form; the list is under two ids;
    an id is the empty string; a duplicate id rides the list.
    Re-run: deterministic — the same entries normalize to the same ids.
    Touches: nothing — a pure normalization.
    Provenance: the axis-query build (packet recommend/calc-ops, route
    order-bias-probe, 2026-11-26).
    """
    ids: list[str] = []
    for position, element in enumerate(elements):
        if isinstance(element, str):
            ids.append(element)
        elif (
            isinstance(element, list)
            and len(element) == _PAIR_ARITY
            and isinstance(element[0], str)
            and isinstance(element[1], str)
        ):
            ids.append(element[0])
        else:
            _refuse(
                expected="item ids as strings, or the manifest's [id, label] pairs (two strings each)",
                found=f"{source} carries {json.dumps(element)} at position {position} — neither the id nor the pair",
                next_action="pass the items as a JSON array of ids (or [id, label] pairs), in the manifest's order",
            )
            return None
    if len(ids) < _MINIMUM_ITEMS:
        _refuse(
            expected="an items list of at least two ids (the register's own law)",
            found=f"{source} carries {len(ids)} item(s)",
            next_action="pass the run's registered item ids, in the manifest's order",
        )
        return None
    if any(not item for item in ids):
        _refuse(
            expected="item ids all non-empty (the register's own law)",
            found=f"{source} carries an empty id",
            next_action="pass the run's registered item ids, in the manifest's order",
        )
        return None
    if len(set(ids)) != len(ids):
        _refuse(
            expected="item ids all unique (the register's own law)",
            found=f"{source} carries a duplicate id",
            next_action="pass the run's registered item ids, in the manifest's order",
        )
        return None
    return ids


def _scan_manifest_ids(text: str, source: str) -> list[str] | None:
    """Scan the items file's lines — the manifest line found, its items normalized.

    Purpose: the file read whole's lines walked in order — the first
    manifest line (kind='manifest') supplies the items, normalized at
    its line; every refusal names its line.
    Refuses when: a line is not parseable JSON, or not an object; the
    manifest line carries no items array; no manifest line rides the
    file.
    Re-run: deterministic — the same file text scans to the same ids.
    Touches: nothing — a pure scan over the given text.
    Provenance: the axis-query build (packet recommend/calc-ops, route
    order-bias-probe, 2026-11-26).
    """
    for position, line in enumerate(text.splitlines(), start=1):
        try:
            record: object = json.loads(line)
        except json.JSONDecodeError:
            _refuse(
                expected=f"line {position} of the items file as a JSON object",
                found="the line is not parseable JSON",
                next_action="pass the manifest's own file (the run JSONL) unmodified, or the id list as a JSON array",
            )
            return None
        if not isinstance(record, dict):
            _refuse(
                expected=f"line {position} of the items file as a JSON object",
                found=f"the line parses as {type(record).__name__}, not an object",
                next_action="pass the manifest's own file (the run JSONL) unmodified, or the id list as a JSON array",
            )
            return None
        if record.get("kind") != _KIND_MANIFEST:
            continue
        items = record.get("items")
        if not isinstance(items, list):
            _refuse(
                expected="the manifest line's items as a JSON array",
                found=f"the manifest line at {position} carries no items array",
                next_action="pass the run JSONL (the manifest line rides its head) or the id list as a JSON array",
            )
            return None
        return _normalize_ids(items, f"the manifest line at {position}")
    _refuse(
        expected="a manifest line (kind='manifest') among the items file's lines",
        found=f"{source} carries no manifest line",
        next_action="pass the run JSONL (the manifest line rides its head) or the id list as a JSON array",
    )
    return None


def _resolve_ids(raw: str) -> list[str] | None:
    """Resolve the items flag — a JSON id array, or a manifest file's path read whole.

    Purpose: the items in canonical order from either form — a JSON
    array (the id list), or a file path (read whole: the JSONL's
    manifest line found by kind, its items normalized). A JSON array
    wins; anything else is treated as the path.
    Refuses when: the flag is neither a JSON array nor a readable
    file; the file carries a non-JSON line, a line that is not an
    object, no manifest line, or a manifest line whose items refuse at
    the normalization.
    Re-run: deterministic — the same flag resolves to the same ids.
    Touches: the items file, read-only, when the flag is a path.
    Provenance: the axis-query build (packet recommend/calc-ops, route
    order-bias-probe, 2026-11-26).
    """
    try:
        parsed: object = json.loads(raw)
    except json.JSONDecodeError:
        parsed = None
    if isinstance(parsed, list):
        return _normalize_ids(parsed, "the items flag")
    try:
        with Path(raw).open(encoding="utf-8") as handle:
            text = handle.read()
    except OSError:
        _refuse(
            expected="items as a JSON array of ids, or a readable manifest file's path",
            found=f"items='{raw}' — not a JSON array, and the file cannot be read",
            next_action="pass the id list as a JSON array, or the run/manifest JSONL's path",
        )
        return None
    return _scan_manifest_ids(text, raw)


def _load_vote_records(raw: str) -> list[dict[str, object]] | None:
    """Load the run file's vote records — the file read whole, the line kinds gated.

    Purpose: the vote records in file order (the ground's
    chronology), the manifest line skipped (the items ride the
    --items flag, never the run file's own manifest line — the
    two-argument contract).
    Refuses when: the file cannot be read; a line is not parseable
    JSON, or not an object; a line's kind is neither manifest nor
    vote.
    Re-run: deterministic — the same file bytes load to the same
    records.
    Touches: the run file, read-only.
    Provenance: the axis-query build (packet recommend/calc-ops, route
    order-bias-probe, 2026-11-26).
    """
    try:
        with Path(raw).open(encoding="utf-8") as handle:
            lines = handle.read().splitlines()
    except OSError:
        _refuse(
            expected="run_file as a readable JSONL path (the votes' run file)",
            found=f"run_file='{raw}' — the file cannot be read",
            next_action="pass the run file's path (e.g. .prioritree/runs/RUN-0008.jsonl)",
        )
        return None
    records: list[dict[str, object]] = []
    for position, line in enumerate(lines, start=1):
        try:
            record: object = json.loads(line)
        except json.JSONDecodeError:
            _refuse(
                expected=f"line {position} of the run file as a JSON object",
                found="the line is not parseable JSON",
                next_action="pass the run file's JSONL unmodified",
            )
            return None
        if not isinstance(record, dict):
            _refuse(
                expected=f"line {position} of the run file as a JSON object",
                found=f"the line parses as {type(record).__name__}, not an object",
                next_action="pass the run file's JSONL unmodified",
            )
            return None
        kind = record.get("kind")
        if kind == _KIND_MANIFEST:
            continue
        if kind != _KIND_VOTE:
            _refuse(
                expected=f"line {position}'s kind as one of ({_KIND_MANIFEST}, {_KIND_VOTE})",
                found=f"line {position} carries kind={json.dumps(kind)}",
                next_action="pass the run file's JSONL unmodified (a manifest line rides its head; the votes follow)",
            )
            return None
        records.append(record)
    return records


def _canonicalize_pair(pair: object, position: int, index: dict[str, int]) -> tuple[str, str] | None:
    """Canonicalize the vote's pair — the two-id form gated, the ids ordered.

    Purpose: the pair re-ordered to the items' index (the cell key's
    canonical form, so one pair's canonical and swapped legs land at
    one pair row); the ids' membership gated (the integrity
    contract); the two-element form gated (the pair contract, the
    schedule never serving one item against itself).
    Refuses when: the pair is not two id strings; an id is outside
    the items list; the pair carries one item twice.
    Re-run: deterministic — the same pair parses to the same tuple.
    Touches: nothing — a pure parse.
    Provenance: the axis-query build (packet recommend/calc-ops, route
    order-bias-probe, 2026-11-26).
    """
    if not (
        isinstance(pair, list)
        and len(pair) == _PAIR_ARITY
        and isinstance(pair[0], str)
        and isinstance(pair[1], str)
    ):
        _refuse(
            expected=f"vote {position}'s pair as two id strings — the pair contract",
            found=f"pair={json.dumps(pair)} — not the two-string form",
            next_action="pass the run file's JSONL unmodified",
        )
        return None
    item_a, item_b = pair[0], pair[1]
    if item_a not in index or item_b not in index:
        _refuse(
            expected="every pair id among the items (the integrity contract — an unregistered id is corrupt)",
            found=f"vote {position}'s pair ({item_a!r}, {item_b!r}) carries an id outside the items list",
            next_action="pass the manifest whose items cover every vote's pair, or the id list that does",
        )
        return None
    if item_a == item_b:
        _refuse(
            expected="a pair of two distinct items (the schedule never serves one item against itself)",
            found=f"vote {position}'s pair carries {item_a!r} twice",
            next_action="pass the run file's JSONL unmodified",
        )
        return None
    return (item_a, item_b) if index[item_a] < index[item_b] else (item_b, item_a)


def _validate_vote_axes(record: dict[str, object], position: int) -> tuple[str, str, str] | None:
    """Validate the vote's axes — the class stamp, the presentation, the winner.

    Purpose: the consumed value-set fields gated — comparator_class
    from the class stamp's schema, presentation_order from the
    presentation set (an ABSENT field reads canonical — the honest
    default), the winner from the standing verdict trio — each value
    AS RECORDED, never interpreted.
    Refuses when: a field is mistyped or outside its ruled set.
    Re-run: deterministic — the same record validates to the same axes.
    Touches: nothing — a pure validation.
    Provenance: the axis-query build (packet recommend/calc-ops, route
    order-bias-probe, 2026-11-26).
    """
    vote_class = record.get("comparator_class")
    if not (isinstance(vote_class, str) and vote_class in _CLASSES):
        _refuse(
            expected=f"comparator_class from {list(_CLASSES)} — the class stamp's schema",
            found=f"vote {position} carries comparator_class={json.dumps(vote_class)}",
            next_action="pass the run file's JSONL unmodified",
        )
        return None
    presentation = record.get("presentation_order", _PRESENTATION_DEFAULT)
    if not (isinstance(presentation, str) and presentation in _PRESENTATIONS):
        _refuse(
            expected=f"presentation_order from {list(_PRESENTATIONS)} (an absent field reads canonical)",
            found=f"vote {position} carries presentation_order={json.dumps(record.get('presentation_order'))}",
            next_action="pass the run file's JSONL unmodified",
        )
        return None
    winner = record.get("winner")
    if not (isinstance(winner, str) and winner in _VERDICTS):
        _refuse(
            expected=f"winner from {list(_VERDICTS)} — the standing verdict trio (win/loss/tie axes)",
            found=f"vote {position} carries winner={json.dumps(winner)}",
            next_action="pass the run file's JSONL unmodified",
        )
        return None
    return (vote_class, presentation, winner)


def _parse_votes(
    records: list[dict[str, object]], items: list[str],
) -> list[tuple[str, str, str, str, str]] | None:
    """Parse the votes' consumed fields — the pair canonicalized, the value sets gated.

    Purpose: each vote's (canonical pair, class, presentation,
    winner) — the pair re-ordered to the items' index (the cell key's
    canonical form, so one pair's canonical and swapped legs land at
    one pair row), the winner AS RECORDED (positional over the
    SERVED pair — the ground, never the rule); an ABSENT
    presentation_order reads canonical (the honest default).
    Refuses when: a consumed field is mistyped or outside the ruled
    sets (comparator_class, presentation_order, winner); a pair id
    is outside the items list; a pair carries one item twice.
    Re-run: deterministic — the same records and items parse to the
    same tuples.
    Touches: nothing — a pure parse.
    Provenance: the axis-query build (packet recommend/calc-ops, route
    order-bias-probe, 2026-11-26).
    """
    index = {item: position for position, item in enumerate(items)}
    parsed: list[tuple[str, str, str, str, str]] = []
    for position, record in enumerate(records, start=1):
        pair = _canonicalize_pair(record.get("pair"), position, index)
        if pair is None:
            return None
        axes = _validate_vote_axes(record, position)
        if axes is None:
            return None
        parsed.append((*pair, *axes))
    return parsed


def _compose_table(items: list[str], parsed: list[tuple[str, str, str, str, str]]) -> dict[str, object]:
    """Compose the cell table — the full grid, every cell's count and winners list.

    Purpose: every pair of the items (the index order, i < j) x every
    observed class (sorted) x every observed presentation (sorted) —
    each cell {"pair", "class", "presentation", "count", "winners"},
    the winners in the file's record order (the ground's
    chronology); the empty cells ride at count 0 with the empty
    winners list (the remaining-cells list derivable at this one
    call); the total rides as total_votes. A run with no votes serves
    {"total_votes": 0, "cells": []} (the observed sets empty, the
    grid empty), never a refusal.
    Refuses when: never — a pure composition over the parsed votes.
    Re-run: deterministic — the same inputs compose to the same table.
    Touches: nothing — a pure composition.
    Provenance: the axis-query build (packet recommend/calc-ops, route
    order-bias-probe, 2026-11-26).
    """
    winners_by_cell: dict[tuple[str, str, str, str], list[str]] = {}
    classes: set[str] = set()
    presentations: set[str] = set()
    for item_a, item_b, vote_class, presentation, winner in parsed:
        winners_by_cell.setdefault((item_a, item_b, vote_class, presentation), []).append(winner)
        classes.add(vote_class)
        presentations.add(presentation)
    cells: list[dict[str, object]] = []
    for i, first in enumerate(items):
        for second in items[i + 1 :]:
            for vote_class in sorted(classes):
                for presentation in sorted(presentations):
                    winners = winners_by_cell.get((first, second, vote_class, presentation), [])
                    cells.append(
                        {
                            "pair": [first, second],
                            "class": vote_class,
                            "presentation": presentation,
                            "count": len(winners),
                            "winners": winners,
                        },
                    )
    return {"total_votes": len(parsed), "cells": cells}


def _emit_trace(op: str, args: argparse.Namespace, result: dict[str, object]) -> int:
    """Emit the trace line on stdout — the structural object form.

    Purpose: one JSON object per run — {"op","args","result"} — the
    raw flag values as sent (the exact invocation, re-runnable),
    the result the table object (no coercion, the values as
    composed), compact and timestamp-free (the same inputs yield
    the same trace bytes).
    Refuses when: never on shape — the emission is structural.
    Re-run: deterministic — the same inputs, the same trace bytes.
    Touches: stdout only.
    Provenance: the calculate engine's emission law (Q-CALC-EXPANSION
    Q1, 2026-11-25 — the trace line made structural).
    """
    raw_args = {key: value for key, value in vars(args).items() if key not in ("handler", "subcommand")}
    sys.stdout.write(json.dumps({"op": op, "args": raw_args, "result": result}) + "\n")
    return 0


def _cmd_cell_table(args: argparse.Namespace) -> int:
    """Build the cell table — the structured table over the run file's votes.

    Purpose: THE ONE CALL — the items resolved (the id list, or the
    manifest file read whole), the run file's vote records loaded
    (the manifest line skipped), the votes parsed (the pairs
    canonicalized over the items, the value sets gated), the full
    grid composed (every pair x class x presentation -> count + the
    winners list per cell — the doubles visible at their cells), the
    trace line emitted.
    Refuses when: the items source or the run file is unreadable or
    corrupt (the doctrine blocks named in the module docstring, each
    naming its line).
    Re-run: deterministic — the same file bytes + the same items
    yield the same trace bytes.
    Touches: stdout only — the run file and the items source
    read-only.
    Provenance: the axis-query build (packet recommend/calc-ops,
    route order-bias-probe, 2026-11-26) — FR-MEM-0043's cure, the
    calculate expansion's own precedent (a fixed-argv engine at
    .opencode/scripts/ + the wrapper op).
    """
    items = _resolve_ids(str(args.items))
    if items is None:
        return 1
    records = _load_vote_records(str(args.run_file))
    if records is None:
        return 1
    parsed = _parse_votes(records, items)
    if parsed is None:
        return 1
    return _emit_trace("cell-table", args, _compose_table(items, parsed))


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="vote_query.py",
        description="the axis query over the vote data — the structured cell table at one call (FR-MEM-0043's cure)",
    )
    subparsers = parser.add_subparsers(dest="subcommand", required=True, metavar="<subcommand>")
    sub = subparsers.add_parser(
        "cell-table",
        help="the structured table — every pair x class x presentation -> count + the winners list per cell",
    )
    sub.add_argument("--run-file", required=True, help="the run file's path (the votes' JSONL)")
    sub.add_argument(
        "--items",
        required=True,
        help="the manifest's items — the id list (a JSON array) or the manifest file's path (read whole)",
    )
    sub.set_defaults(handler=_cmd_cell_table)
    return parser


def main(argv: list[str] | None = None) -> int:
    """Parse the argv and run the op's handler — the engine's single entry."""
    parser = _build_parser()
    args = parser.parse_args(argv)
    handler: Callable[[argparse.Namespace], int] = args.handler
    return handler(args)


if __name__ == "__main__":
    sys.exit(main())
