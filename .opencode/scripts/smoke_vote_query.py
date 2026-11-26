# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The vote_query engine's smoke — the axis query fired LIVE at RUN-0008.

The axis-query build's own fire (packet recommend/calc-ops, route
order-bias-probe, 2026-11-26 — FR-MEM-0043's cure): the cell-table
op at the probe's own live run, THE ONE CALL the collaborator's
ruling asked for. THE FORM: the engine's main() fired IN-PROCESS
with the seat-facing argv (argparse, the file reads, the trace
emission — the engine's whole code path; the process-spawn battery
is the KAT's lane, where pyproject's S603 ruling lives) — this smoke
holds the patch tool's zero-findings bar inside the .opencode fence:
no subprocess, no assert statement (the refusal form raises
AssertionError), no ignore.

THE FIRE IS POINT-IN-TIME: RUN-0008 is live data (the count gate
standing), so NO byte is pinned — the expectation is the table
derived in-process (an independent composition over the same file
bytes); the FIRED TRACE LINE lands VERBATIM at the artifact
(./vote-query-smoke-RUN-0008.trace beside this file — the report's
quoted evidence: the engine's own stdout, never a hand-composed
byte).

Collection law: the file is NOT test-prefixed — a bare pytest scan
never reaches it (.opencode is a hidden directory, never recursed;
the product's floor unbroken); it is collected only when passed
explicitly (the harness's test tool — the smoke's own lane).
"""

from __future__ import annotations

import io
import json
from contextlib import redirect_stdout
from pathlib import Path

from scripts.vote_query import main as engine_main

ROOT = Path(__file__).resolve().parents[2]
RUN_FILE_ARG = ".prioritree/runs/RUN-0008.jsonl"
ARTIFACT = ROOT / ".opencode" / "scripts" / "vote-query-smoke-RUN-0008.trace"


def _fire_cell_table(items_arg: str) -> tuple[int, str]:
    """Fire the engine's cell-table in-process — the exit code + the captured trace line.

    Purpose: the engine's main() invoked with the seat-facing argv,
    stdout captured whole (the trace line is the engine's own
    emission, never composed here).
    Refuses when: never — the engine's own refusals ride the exit
    code and stderr back to the caller.
    Re-run: deterministic — the same argv yields the same pair.
    Touches: stdout (captured) — the run file read-only.
    Provenance: the axis-query build (packet recommend/calc-ops, route
    order-bias-probe, 2026-11-26).
    """
    stream = io.StringIO()
    with redirect_stdout(stream):
        exit_code = engine_main(["cell-table", f"--run-file={RUN_FILE_ARG}", f"--items={items_arg}"])
    return exit_code, stream.getvalue()


def _manifest_ids() -> list[str]:
    """Read the manifest's item ids — the run file's first line's items, the id at each entry's first position."""
    manifest = json.loads((ROOT / RUN_FILE_ARG).read_text(encoding="utf-8").splitlines()[0])
    return [entry[0] if isinstance(entry, list) else entry for entry in manifest["items"]]


def _derive_table() -> dict[str, object]:
    """Derive the expected table in-process — the run file's own arithmetic.

    An independent composition over the same file bytes: the total
    (the vote-line count), the full grid (every item-pair x observed
    class x observed presentation), each cell's count and winners list
    (the file's record order) — never a pinned byte.
    """
    records = [json.loads(line) for line in (ROOT / RUN_FILE_ARG).read_text(encoding="utf-8").splitlines()]
    votes = [record for record in records if record["kind"] == "vote"]
    item_ids = [entry[0] if isinstance(entry, list) else entry for entry in records[0]["items"]]
    winners_by_cell: dict[tuple[str, str, str, str], list[str]] = {}
    classes: set[str] = set()
    presentations: set[str] = set()
    for vote in votes:
        item_a, item_b = vote["pair"]
        pair = (item_a, item_b) if item_ids.index(item_a) < item_ids.index(item_b) else (item_b, item_a)
        key = (*pair, vote["comparator_class"], vote.get("presentation_order", "canonical"))
        winners_by_cell.setdefault(key, []).append(vote["winner"])
        classes.add(vote["comparator_class"])
        presentations.add(vote.get("presentation_order", "canonical"))
    cells: list[dict[str, object]] = []
    for i, first in enumerate(item_ids):
        for second in item_ids[i + 1 :]:
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
    return {"total_votes": len(votes), "cells": cells}


def test_cell_table_the_one_call_at_run_0008() -> None:
    """The one call at RUN-0008 — the trace fired, the table held, the artifact written, the determinism proven."""
    exit_code, trace_line = _fire_cell_table(RUN_FILE_ARG)
    if exit_code != 0:
        message = "the engine refused the one call at RUN-0008"
        raise AssertionError(message)
    trace = json.loads(trace_line)
    if trace["op"] != "cell-table":
        message = f"the trace's op is not cell-table: {trace['op']!r}"
        raise AssertionError(message)
    if trace["args"] != {"run_file": RUN_FILE_ARG, "items": RUN_FILE_ARG}:
        message = f"the trace's args are not the invocation as sent: {trace['args']!r}"
        raise AssertionError(message)
    if trace["result"] != _derive_table():
        message = "the fired table differs from the in-process derivation"
        raise AssertionError(message)
    ARTIFACT.write_text(trace_line, encoding="utf-8")
    second_code, second_line = _fire_cell_table(json.dumps(_manifest_ids()))
    if second_code != 0:
        message = "the engine refused the id-list form"
        raise AssertionError(message)
    if json.loads(second_line)["result"] != trace["result"]:
        message = "the id-list form composed a different table"
        raise AssertionError(message)
    third_code, third_line = _fire_cell_table(RUN_FILE_ARG)
    if third_code != 0:
        message = "the engine refused the determinism re-fire"
        raise AssertionError(message)
    if third_line != trace_line:
        message = "the re-fire is not byte-identical (the determinism law)"
        raise AssertionError(message)
