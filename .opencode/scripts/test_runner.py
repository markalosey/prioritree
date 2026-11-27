#!/usr/bin/env python3
"""test_runner.py — the test instrument's engine: run pytest, report verbatim.

The seat's test instrument (the tane-team ruling, 2026-09-28: kensho's act is
"run the artifact and report the run" — the team needed the instrument in
its own hands; the coordinator was the copy-paste bottleneck). THE OUTPUT IS
PYTEST'S OWN, verbatim — never a summary (the run IS the evidence; the
zero-errors-and-zero-warnings bar rides pytest's verdict plus the other
instruments' own channels).

CQRS: the read side (the run reports) is a pure execution — no mutations,
no actor, nothing refused except the invocation's own shape.

Ops: all  -> the full battery (uv run pytest tests -q)
      one  -> one file (uv run pytest <test_path> -q)

Exit codes: pytest's own, passed through (the wrapper's formatOutput renders
the verdict). Deterministic; no LLM (INV-H3); fixed-argv subprocess only.
"""

from __future__ import annotations

import subprocess
import sys


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if not args or args[0] not in ("all", "one"):
        print("usage: test_runner.py all | one <test_path>", file=sys.stderr)
        return 2
    if args[0] == "one":
        if len(args) < 2 or not args[1]:
            print("REFUSED — Expected: a test path with the one op", file=sys.stderr)
            print("         Found: none given", file=sys.stderr)
            print("         Next-action: pass the file's path (e.g. tests/test_census.py)", file=sys.stderr)
            return 1
        cmd = ["uv", "run", "pytest", args[1], "-q"]
    else:
        cmd = ["uv", "run", "pytest", "tests", "-q"]
    proc = subprocess.run(cmd)  # fixed argv, no shell; pytest inherits stdio verbatim
    return proc.returncode


if __name__ == "__main__":
    sys.exit(main())
