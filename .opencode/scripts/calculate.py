#!/usr/bin/env python3
"""calculate.py — the calculate composition's pure-query math engine (Q-CALC-1).

Leg B of the calculate composition (dispatch the-engine-fix/calc-b,
census-execution route, 2026-09-28, actor shinko — research+implementation):
leg A landed the manifest surface (.opencode/tools/manifest.yaml's
calculate entry); THIS engine lands against the six ops that surface
declares. Ruled by the collaborator on 2026-09-28. The evidence the
surface exists to kill: FR-MEM-0068 (the member-seat arithmetic gap —
derived numbers had no destination surface, so seats did inline math by
hand or buried it in prose).

THE RULED SHAPE — six ops (add, subtract, multiply, divide, sum, count),
each a PURE QUERY:
  stateless      no store, no session, no sidecar, no lock — nothing mutates.
  actorless      no --actor anywhere; a query refuses nothing on the
                 provenance axis.
  deterministic  the same inputs always return the same number.
  output         the number, and only the number, on stdout — the wrapper
                 renders it; the engine stays lean.

ENGINE CLASS (plain unmanaged, the friction_ledger.py engine pattern —
battery_core.py is a battery, not an engine): the generated wrapper
(.opencode/tools/calculate.ts, emitted at regen by
scripts/generation/generate_tools.py — the collaborator's hand, never this
leg's) invokes THIS script's subcommands with --flag=value argv. Fail-loud
everywhere: a refusal is a named doctrine block on stderr — never a
traceback, never a leaked Python exception — and stdout stays byte-empty
on every refusal.

REFUSALS (the doctrine shape — REFUSED / Expected / Found / Next-action; the
one refusal class a pure query can own):
  - a NON-NUMERIC a or b refuses naming the type contract (numbers, not
    prose — the ruled boundary).
  - a ZERO DIVISOR on divide refuses naming the mathematical impossibility
    (no number is the quotient of n / 0).
  - a values that is not a JSON array, or a sum over non-number elements,
    refuses naming the array contract (a JSON array, not a comma-separated
    string).
  - an UNREPRESENTABLE result (float overflow past the numeric range)
    refuses naming the range — 'inf' is not a number.

Usage:
    uv run python scripts/calculate.py <subcommand> [--flag=value ...]

Exit codes: 0 = the op succeeded (the number on stdout); 1 = a named
refusal (fail-loud, on stderr); 2 = unusable invocation (argparse).
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections.abc import Callable

_INT_RE = re.compile(r"[+-]?\d+")
_FLOAT_RE = re.compile(r"[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?")


def _refuse(expected: str, found: str, next_action: str) -> int:
    """Print the doctrine-shaped refusal block on stderr; stdout stays empty."""
    sys.stderr.write(
        "REFUSED\n"
        f"Expected: {expected}\n"
        f"Found: {found}\n"
        f"Next-action: {next_action}\n"
    )
    return 1


def _parse_number(raw: str) -> int | float | None:
    """Strict numeric parse — a number, or None (prose never passes)."""
    text = raw.strip()
    if _INT_RE.fullmatch(text):
        return int(text)
    if _FLOAT_RE.fullmatch(text):
        value = float(text)
        if math.isinf(value):
            return None  # beyond the representable range — not a printable number
        return value
    return None


def _render(value: int | float) -> str:
    """The number, naturally rendered — an integral result carries no .0."""
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value)


def _emit(result: int | float) -> int:
    """Print the number on stdout — guarding the representable range."""
    if isinstance(result, float) and math.isinf(result):
        return _refuse(
            expected="a representable result (a number the engine can print)",
            found="the result is infinite — outside the representable numeric range",
            next_action=(
                "rescale the operands (smaller magnitudes), or reformulate "
                "the derivation"
            ),
        )
    print(_render(result))
    return 0


def _refuse_operand(name: str, raw: str) -> None:
    """The type-contract refusal — numbers, not prose (the ruled boundary)."""
    _refuse(
        expected=f"{name} as a number (as a string) — the type contract",
        found=f"{name}='{raw}' — a non-numeric string (prose, not a number)",
        next_action=(
            f"pass {name} as a number — arithmetic and counting only, "
            "never prose"
        ),
    )


def _require_operands(
    args: argparse.Namespace,
) -> tuple[int | float, int | float] | None:
    """Strictly parse a and b; refuse (doctrine-shaped) on a violation."""
    a = _parse_number(str(args.a))
    if a is None:
        _refuse_operand("a", str(args.a))
        return None
    b = _parse_number(str(args.b))
    if b is None:
        _refuse_operand("b", str(args.b))
        return None
    return a, b


def _cmd_add(args: argparse.Namespace) -> int:
    operands = _require_operands(args)
    if operands is None:
        return 1
    a, b = operands
    return _emit(a + b)


def _cmd_subtract(args: argparse.Namespace) -> int:
    operands = _require_operands(args)
    if operands is None:
        return 1
    a, b = operands
    return _emit(a - b)


def _cmd_multiply(args: argparse.Namespace) -> int:
    operands = _require_operands(args)
    if operands is None:
        return 1
    a, b = operands
    return _emit(a * b)


def _cmd_divide(args: argparse.Namespace) -> int:
    operands = _require_operands(args)
    if operands is None:
        return 1
    a, b = operands
    if b == 0:
        return _refuse(
            expected="a nonzero divisor b (a number)",
            found=(
                f"b='{args.b}' — division by zero is mathematically "
                "impossible; no number is the quotient of n / 0"
            ),
            next_action=(
                "pass a nonzero b, or reformulate the derivation "
                "(the boundary is arithmetic and counting only)"
            ),
        )
    return _emit(a / b)


def _require_array(raw: str) -> list[object] | None:
    """Strictly parse values as a JSON array; refuse on the array contract."""
    expected = "values as a JSON array (e.g. '[1, 2, 3]')"
    try:
        parsed: object = json.loads(raw)
    except json.JSONDecodeError:
        _refuse(
            expected=expected,
            found=(
                f"values='{raw}' — not parseable as JSON "
                "(a comma-separated string is not the array)"
            ),
            next_action=(
                "pass a JSON array — bracket it and quote its strings"
            ),
        )
        return None
    if not isinstance(parsed, list):
        _refuse(
            expected=expected,
            found=f"values='{raw}' — valid JSON, but not an array",
            next_action="pass a JSON array — a single value is not the array",
        )
        return None
    return parsed


def _cmd_sum(args: argparse.Namespace) -> int:
    values = _require_array(str(args.values))
    if values is None:
        return 1
    total: int | float = 0
    for index, element in enumerate(values):
        if isinstance(element, bool) or not isinstance(element, int | float):
            _refuse(
                expected="a JSON array of numbers",
                found=(
                    f"values carries a non-number element at index {index} "
                    f"({json.dumps(element)}) — sum totals numbers only"
                ),
                next_action=(
                    "pass a JSON array whose elements are all numbers, "
                    "or use count for element counting"
                ),
            )
            return 1
        total += element
    return _emit(total)


def _cmd_count(args: argparse.Namespace) -> int:
    values = _require_array(str(args.values))
    if values is None:
        return 1
    print(len(values))
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="calculate.py",
        description=(
            "pure-query arithmetic and counting (Q-CALC-1) — six "
            "deterministic ops (add, subtract, multiply, divide, sum, count)"
        ),
    )
    subparsers = parser.add_subparsers(
        dest="subcommand", required=True, metavar="<subcommand>"
    )

    for name, handler, help_text in (
        ("add", _cmd_add, "a + b — the sum of two numbers"),
        ("subtract", _cmd_subtract, "a - b — the difference of two numbers"),
        ("multiply", _cmd_multiply, "a * b — the product of two numbers"),
        ("divide", _cmd_divide, "a / b — the quotient of two numbers"),
    ):
        sub = subparsers.add_parser(name, help=help_text)
        sub.add_argument(
            "--a", required=True, help="the first operand (a number, as a string)"
        )
        sub.add_argument(
            "--b", required=True, help="the second operand (a number, as a string)"
        )
        sub.set_defaults(handler=handler)

    for name, handler, help_text in (
        ("sum", _cmd_sum, "the total of a JSON array of numbers"),
        ("count", _cmd_count, "the number of elements in a JSON array"),
    ):
        sub = subparsers.add_parser(name, help=help_text)
        sub.add_argument(
            "--values", required=True, help="the list to aggregate (a JSON array)"
        )
        sub.set_defaults(handler=handler)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    handler: Callable[[argparse.Namespace], int] = args.handler
    return handler(args)


if __name__ == "__main__":
    sys.exit(main())
