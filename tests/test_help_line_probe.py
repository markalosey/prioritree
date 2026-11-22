# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The help-line probe — a temporary instrument (deleted after the one run): the template line whole."""

from pathlib import Path


def test_probe_help_line() -> None:
    """Print junro.ts's help template line in segments — the projection edit's pre-image."""
    target = Path("/Users/marklosey/projects/prioritree/.opencode/tools/junro.ts")
    lines = target.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines, start=1):
        if 'return "junro — Effort record operations' in line:
            rows = [f"line {index} length {len(line)}"]
            for start in range(0, len(line), 1000):
                segment = line[start : start + 1000]
                rows.append(f"SEG{start // 1000:02d} len {len(segment)} >>>{segment}<<<")
            msg = "\n".join(rows)
            raise AssertionError(msg)
    tail = "the help template line not found"
    raise AssertionError(tail)
