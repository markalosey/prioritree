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

THE RULED SHAPE — 30 deterministic ops (Q-CALC-1's six arithmetic and
counting + Q-CALC-EXPANSION's 24: statistics, combinatorics, distribution,
seeded permutation),
each a PURE QUERY:
  stateless      no store, no session, no sidecar, no lock — nothing mutates.
  actorless      no --actor anywhere; a query refuses nothing on the
                 provenance axis.
  deterministic  the same inputs always return the same number.
  output         THE TRACE LINE, and only the trace line, on stdout —
                 {"op","args","result"} compact JSON (Q-CALC-EXPANSION Q1,
                 2026-11-25: the provenance law made structural — the op,
                 the operands, the result in one quotable byte-string; the
                 raw flag values as sent; an integral float coerced to int
                 at result; NO timestamp — the same inputs yield the same
                 trace bytes).

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
  - a NON-FINITE ELEMENT (NaN or Infinity in a values array) refuses naming
    the finiteness contract (Q-CALC-EXPANSION Q5, 2026-11-25: sum tightens —
    a live leak closed; NaN sorts undefined and totals to 'nan', which is
    not a number).
  - a DOMAIN violation (the log's non-positive a, the ppf's q outside
    (0, 1), the chisquare's mismatched lengths or non-positive expected
    cells, the shuffle's non-integer seed) refuses naming the domain
    (Q-CALC-EXPANSION Q4).

EXPANSION PROVENANCE (Q-CALC-EXPANSION, ruled 2026-11-25): the six ops'
  grammar extends to 30 — the 24 statistical ops LANDED band by band (the
  staged sub-ask law, complete at this final band); the op-count prose
  updated here.

Usage:
    uv run python scripts/calculate.py <subcommand> [--flag=value ...]

Exit codes: 0 = the op succeeded (the number on stdout); 1 = a named
refusal (fail-loud, on stderr); 2 = unusable invocation (argparse).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import random
import re
import statistics
import sys
from collections.abc import Callable

_INT_RE = re.compile(r"[+-]?\d+")
_FLOAT_RE = re.compile(r"[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?")


def _refuse(expected: str, found: str, next_action: str) -> int:
    """Print the doctrine-shaped refusal block on stderr; stdout stays empty."""
    sys.stderr.write(f"REFUSED\nExpected: {expected}\nFound: {found}\nNext-action: {next_action}\n")
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


def _coerce_result(result: int | float) -> int | float:
    """An integral float carries no .0 in the trace (the _render law held)."""
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result


def _emit(op: str, args: argparse.Namespace, result: int | float) -> int:
    """Print THE TRACE LINE on stdout — guarding the representable range.

    Purpose: one JSON object per run — {"op","args","result"} — the raw
    flag values as sent (the exact invocation, re-runnable), the result
    coerced (integral floats to int), compact and timestamp-free.
    Refuses when: never on shape — the inf guard only (the range refusal).
    Re-run: deterministic — same inputs, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q1 (the collaborator's ruling, 2026-11-25).
    """
    if isinstance(result, float) and math.isinf(result):
        return _refuse(
            expected="a representable result (a number the engine can print)",
            found="the result is infinite — outside the representable numeric range",
            next_action=("rescale the operands (smaller magnitudes), or reformulate the derivation"),
        )
    raw_args = {key: value for key, value in vars(args).items() if key not in ("handler", "subcommand")}
    print(json.dumps({"op": op, "args": raw_args, "result": _coerce_result(result)}))
    return 0


def _emit_pair(op: str, args: argparse.Namespace, values: tuple[float, float]) -> int:
    """Print the pair trace line on stdout — guarding the representable range.

    Purpose: one JSON object per run — {"op","args","result"} — the
    result a TWO-ELEMENT ARRAY (the multi-value form: wilson's [lo,
    hi], chisquare's [statistic, df]); each element coerced (integral
    floats to int), compact and timestamp-free.
    Refuses when: never on shape — the inf guard only (the range
    refusal, per element).
    Re-run: deterministic — same inputs, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q1/Q2 (the collaborator's ruling,
    2026-11-25).
    """
    coerced = [_coerce_result(value) for value in values]
    for value in coerced:
        if isinstance(value, float) and math.isinf(value):
            return _refuse(
                expected="representable results (numbers the engine can print)",
                found="a result element is infinite — outside the representable numeric range",
                next_action="rescale the operands (smaller magnitudes), or reformulate the derivation",
            )
    raw_args = {key: value for key, value in vars(args).items() if key not in ("handler", "subcommand")}
    print(json.dumps({"op": op, "args": raw_args, "result": coerced}))
    return 0


def _refuse_operand(name: str, raw: str) -> None:
    """The type-contract refusal — numbers, not prose (the ruled boundary)."""
    _refuse(
        expected=f"{name} as a number (as a string) — the type contract",
        found=f"{name}='{raw}' — a non-numeric string (prose, not a number)",
        next_action=(f"pass {name} as a number — arithmetic and counting only, never prose"),
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
    return _emit("add", args, a + b)


def _cmd_subtract(args: argparse.Namespace) -> int:
    operands = _require_operands(args)
    if operands is None:
        return 1
    a, b = operands
    return _emit("subtract", args, a - b)


def _cmd_multiply(args: argparse.Namespace) -> int:
    operands = _require_operands(args)
    if operands is None:
        return 1
    a, b = operands
    return _emit("multiply", args, a * b)


def _cmd_divide(args: argparse.Namespace) -> int:
    operands = _require_operands(args)
    if operands is None:
        return 1
    a, b = operands
    if b == 0:
        return _refuse(
            expected="a nonzero divisor b (a number)",
            found=(f"b='{args.b}' — division by zero is mathematically impossible; no number is the quotient of n / 0"),
            next_action=(
                "pass a nonzero b, or reformulate the derivation (the boundary is arithmetic and counting only)"
            ),
        )
    return _emit("divide", args, a / b)


def _require_array(raw: str) -> list[object] | None:
    """Strictly parse values as a JSON array; refuse on the array contract."""
    expected = "values as a JSON array (e.g. '[1, 2, 3]')"
    try:
        parsed: object = json.loads(raw)
    except json.JSONDecodeError:
        _refuse(
            expected=expected,
            found=(f"values='{raw}' — not parseable as JSON (a comma-separated string is not the array)"),
            next_action=("pass a JSON array — bracket it and quote its strings"),
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
        if (
            isinstance(element, bool)
            or not isinstance(element, int | float)
            or (isinstance(element, float) and not math.isfinite(element))
        ):
            _refuse(
                expected="a JSON array of numbers",
                found=(
                    f"values carries a non-number element at index {index} "
                    f"({json.dumps(element)}) — sum totals finite numbers "
                    "only (NaN and Infinity refuse: the finiteness contract)"
                ),
                next_action=("pass a JSON array whose elements are all numbers, or use count for element counting"),
            )
            return 1
        total += element
    return _emit("sum", args, total)


def _cmd_count(args: argparse.Namespace) -> int:
    values = _require_array(str(args.values))
    if values is None:
        return 1
    return _emit("count", args, len(values))


def _require_int(name: str, raw: str) -> int | None:
    """Strict integer parse — an int, or None (never a fraction)."""
    text = raw.strip()
    if _INT_RE.fullmatch(text):
        return int(text)
    _refuse(
        expected=f"{name} as an integer (as a string) — the int contract",
        found=(f"{name}='{raw}' — a non-integer string (whole counts only, never fractions)"),
        next_action=f"pass {name} as an integer — whole counts only",
    )
    return None


def _require_enum(raw: str, legal: tuple[str, ...], name: str) -> str | None:
    """The enum flag's value gate — a legal token, or None."""
    text = raw.strip()
    if text in legal:
        return text
    _refuse(
        expected=f"{name} as one of the legal tokens ({', '.join(legal)})",
        found=f"{name}='{raw}' — outside the legal vocabulary",
        next_action=f"pass {name} as one of: {', '.join(legal)}",
    )
    return None


def _require_numeric_array(raw: str, op: str) -> list[int | float] | None:
    """A JSON array of finite numbers — the statistical ops' shared gate.

    Purpose: values as a JSON array whose every element is a finite
    number (not bool, not NaN, not Infinity) — the finiteness contract
    carried to every new array op; the empty array REFUSES (the one
    refusal domain with live reach).
    Refuses when: not a JSON array; a non-number or non-finite element;
    the array is empty.
    Re-run: deterministic — the same raw string yields the same list or
    the same refusal.
    Touches: nothing — a pure parse.
    Provenance: Q-CALC-EXPANSION Q4/Q5 (the collaborator's ruling,
    2026-11-25).
    """
    values = _require_array(raw)
    if values is None:
        return None
    if not values:
        _refuse(
            expected=f"a non-empty JSON array of finite numbers (the {op} of nothing is undefined)",
            found=f"values='{raw}' — an empty array",
            next_action="pass a non-empty JSON array of finite numbers",
        )
        return None
    numbers: list[int | float] = []
    for index, element in enumerate(values):
        if (
            isinstance(element, bool)
            or not isinstance(element, int | float)
            or (isinstance(element, float) and not math.isfinite(element))
        ):
            _refuse(
                expected="a JSON array of finite numbers",
                found=(
                    f"values carries a non-finite or non-number element at index {index} "
                    f"({json.dumps(element)}) — {op} operates on finite numbers only "
                    "(NaN and Infinity refuse: the finiteness contract)"
                ),
                next_action=("pass a JSON array whose elements are all finite numbers"),
            )
            return None
        numbers.append(element)
    return numbers


def _cmd_sqrt(args: argparse.Namespace) -> int:
    """sqrt — the principal square root of a.

    Purpose: √a — math.sqrt, the deterministic real root.
    Refuses when: a is non-numeric, or a < 0 (a negative radicand has
    no real root; complex results are outside the type contract).
    Re-run: deterministic — same a, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25).
    """
    a = _parse_number(str(args.a))
    if a is None:
        _refuse_operand("a", str(args.a))
        return 1
    if a < 0:
        return _refuse(
            expected="a non-negative radicand a (a real square root exists only for a >= 0)",
            found=(
                f"a='{args.a}' — a negative radicand has no real root (complex results are outside the type contract)"
            ),
            next_action="pass a >= 0, or reformulate the derivation",
        )
    return _emit("sqrt", args, math.sqrt(a))


def _cmd_power(args: argparse.Namespace) -> int:
    """power — a raised to b (b real).

    Purpose: a^b — the ** operator; an int base keeps exact int at a
    whole int exponent, float64 otherwise.
    Refuses when: an operand is non-numeric; a = 0 with b <= 0 (0^0
    indeterminate, 0^negative is 1/0); a < 0 with a non-integer b
    (no real value — Python's complex result is outside the type
    contract); the result unrepresentable (the range guard at _emit).
    Re-run: deterministic — same operands, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 + hyoka A6 (2026-11-25): the
    complex leak refused at birth; 0^0 named (Python returns 1 — the
    engine refuses instead, the ruled semantics over the stdlib's
    convenience).
    """
    operands = _require_operands(args)
    if operands is None:
        return 1
    a, b = operands
    if a == 0 and b <= 0:
        return _refuse(
            expected="a nonzero base or a positive exponent (0^0 is indeterminate; 0^negative is 1/0)",
            found=f"a='{args.a}', b='{args.b}' — the zero-base form is mathematically impossible",
            next_action="pass a nonzero a, or b > 0 at a=0",
        )
    if a < 0 and not float(b).is_integer():
        return _refuse(
            expected="a non-negative base at a non-integer exponent (a real value exists only for a >= 0)",
            found=(
                f"a='{args.a}', b='{args.b}' — a negative base with a non-integer exponent has no real "
                "value (Python's complex result is outside the type contract)"
            ),
            next_action="pass a >= 0, or a whole exponent b",
        )
    return _emit("power", args, a**b)


def _cmd_factorial(args: argparse.Namespace) -> int:
    """factorial — n! in exact, arbitrary-precision int.

    Purpose: math.factorial — exact int, any n (the engine's int is
    unbounded; the 171! float boundary rides any downstream float
    conversion, never this op).
    Refuses when: n is non-numeric or non-integer (the int contract
    — '5.0' refuses), or n < 0.
    Re-run: deterministic — same n, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25).
    """
    n = _require_int("n", str(args.n))
    if n is None:
        return 1
    if n < 0:
        return _refuse(
            expected="a non-negative integer n (no negative factorial exists)",
            found=f"n='{args.n}' — the factorial of a negative count is undefined",
            next_action="pass n >= 0",
        )
    return _emit("factorial", args, math.factorial(n))


def _cmd_combination(args: argparse.Namespace) -> int:
    """combination — C(n, k) in exact int.

    Purpose: math.comb — the binomial coefficient, exact int.
    Refuses when: n or k is non-numeric or non-integer; n < 0; k < 0;
    k > n (the selection is empty — the stdlib returns 0; the engine
    refuses instead: an impossible selection is a domain error,
    never a silent zero).
    Re-run: deterministic — same n, k — same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 + keisan's pricing (2026-11-25):
    the k>n class priced engine-side.
    """
    n = _require_int("n", str(args.n))
    if n is None:
        return 1
    k = _require_int("k", str(args.k))
    if k is None:
        return 1
    if n < 0 or k < 0:
        return _refuse(
            expected="non-negative integer counts n and k",
            found=(f"n='{args.n}', k='{args.k}' — a negative count is outside the domain"),
            next_action="pass n >= 0 and k >= 0",
        )
    if k > n:
        return _refuse(
            expected="k <= n (the selection cannot exceed the population)",
            found=(
                f"n='{args.n}', k='{args.k}' — the selection exceeds the population; "
                "the stdlib's 0 is a convenience, never the answer"
            ),
            next_action="pass k <= n (an impossible selection is a domain error, never a silent zero)",
        )
    return _emit("combination", args, math.comb(n, k))


def _cmd_proportion(args: argparse.Namespace) -> int:
    """proportion — the share part/whole.

    Purpose: part / whole — the share form (a percentage is the
    proportion x 100, stepwise via multiply: two citable traces beat
    one sugar op).
    Refuses when: an operand is non-numeric, or whole = 0 (no number
    is the quotient of n / 0).
    Re-run: deterministic — same operands, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25).
    """
    part = _parse_number(str(args.part))
    if part is None:
        _refuse_operand("part", str(args.part))
        return 1
    whole = _parse_number(str(args.whole))
    if whole is None:
        _refuse_operand("whole", str(args.whole))
        return 1
    if whole == 0:
        return _refuse(
            expected="a nonzero whole (a number)",
            found=(
                f"whole='{args.whole}' — division by zero is mathematically impossible; "
                "no number is the quotient of n / 0"
            ),
            next_action=(
                "pass a nonzero whole, or reformulate the derivation (the boundary is arithmetic and counting only)"
            ),
        )
    return _emit("proportion", args, part / whole)


def _cmd_mean(args: argparse.Namespace) -> int:
    """mean — the arithmetic mean of a JSON array.

    Purpose: statistics.fmean — the deterministic arithmetic mean.
    Refuses when: values is not a JSON array of finite numbers, or
    the array is empty (no mean of nothing).
    Re-run: deterministic — same values, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25).
    """
    numbers = _require_numeric_array(str(args.values), "mean")
    if numbers is None:
        return 1
    return _emit("mean", args, statistics.fmean(numbers))


def _cmd_variance(args: argparse.Namespace) -> int:
    """variance — the population or sample variance of a JSON array.

    Purpose: statistics.pvariance (form=population) /
    statistics.variance (form=sample) — the deterministic dispersion.
    Refuses when: values is not a JSON array of finite numbers, or
    the array is empty; the sample form additionally at n < 2 (the
    zero-denominator class: one observation carries no dispersion);
    --form outside the legal vocabulary (population|sample).
    Re-run: deterministic — same values+form, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25); RUN-0006's single vote the live n<2 trigger.
    """
    form = _require_enum(str(args.form), ("population", "sample"), "form")
    if form is None:
        return 1
    numbers = _require_numeric_array(str(args.values), "variance")
    if numbers is None:
        return 1
    if form == "population":
        return _emit("variance", args, statistics.pvariance(numbers))
    if len(numbers) < 2:
        return _refuse(
            expected=(
                "at least two observations for the sample variance "
                "(the zero-denominator class: one observation carries no dispersion)"
            ),
            found=(f"values carries {len(numbers)} element(s) at form='sample' — the sample denominator n-1 is zero"),
            next_action="pass >= 2 observations, or use --form=population",
        )
    return _emit("variance", args, statistics.variance(numbers))


def _cmd_stddev(args: argparse.Namespace) -> int:
    """stddev — the population or sample standard deviation of a JSON array.

    Purpose: statistics.pstdev (form=population) / statistics.stdev
    (form=sample) — the deterministic spread.
    Refuses when: values is not a JSON array of finite numbers, or the
    array is empty; the sample form additionally at n < 2 (the
    zero-denominator class); --form outside the legal vocabulary.
    Re-run: deterministic — same values+form, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25).
    """
    form = _require_enum(str(args.form), ("population", "sample"), "form")
    if form is None:
        return 1
    numbers = _require_numeric_array(str(args.values), "stddev")
    if numbers is None:
        return 1
    if form == "population":
        return _emit("stddev", args, statistics.pstdev(numbers))
    if len(numbers) < 2:
        return _refuse(
            expected=(
                "at least two observations for the sample standard deviation "
                "(the zero-denominator class: one observation carries no spread)"
            ),
            found=(f"values carries {len(numbers)} element(s) at form='sample' — the sample denominator n-1 is zero"),
            next_action="pass >= 2 observations, or use --form=population",
        )
    return _emit("stddev", args, statistics.stdev(numbers))


def _cmd_max(args: argparse.Namespace) -> int:
    """max — the greatest element of a JSON array.

    Purpose: max() — the deterministic maximum.
    Refuses when: values is not a JSON array of finite numbers, or the
    array is empty (the max of nothing is undefined).
    Re-run: deterministic — same values, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25).
    """
    numbers = _require_numeric_array(str(args.values), "max")
    if numbers is None:
        return 1
    return _emit("max", args, max(numbers))


def _cmd_min(args: argparse.Namespace) -> int:
    """min — the least element of a JSON array.

    Purpose: min() — the deterministic minimum.
    Refuses when: values is not a JSON array of finite numbers, or the
    array is empty (the min of nothing is undefined).
    Re-run: deterministic — same values, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25).
    """
    numbers = _require_numeric_array(str(args.values), "min")
    if numbers is None:
        return 1
    return _emit("min", args, min(numbers))


def _cmd_median(args: argparse.Namespace) -> int:
    """median — the middle value of a JSON array.

    Purpose: statistics.median — the deterministic median (the mean
    of the two middle elements at even n).
    Refuses when: values is not a JSON array of finite numbers, or the
    array is empty (the median of nothing is undefined).
    Re-run: deterministic — same values, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25).
    """
    numbers = _require_numeric_array(str(args.values), "median")
    if numbers is None:
        return 1
    return _emit("median", args, statistics.median(numbers))


def _cmd_quantile(args: argparse.Namespace) -> int:
    """quantile — the p-quantile by fixed (n-1)-based linear interpolation.

    Purpose: the p-quantile of the sorted array at the (n-1) method —
    pos = p * (n - 1); a whole position returns the element; the
    fractional position interpolates linearly between neighbors. THE
    METHOD IS FIXED AND NAMED HERE (determinism demands one method,
    never a flag); n = 1 is legal (the single element at any p).
    Refuses when: values is not a JSON array of finite numbers, or
    the array is empty; p is non-numeric or outside [0, 1].
    Re-run: deterministic — same values+p, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 + keisan's pricing (2026-11-25):
    no stdlib backing — the interpolation is engine-owned; the KAT the
    only guard.
    """
    numbers = _require_numeric_array(str(args.values), "quantile")
    if numbers is None:
        return 1
    p = _parse_number(str(args.p))
    if p is None:
        _refuse_operand("p", str(args.p))
        return 1
    if p < 0 or p > 1:
        return _refuse(
            expected=("p as a quantile position in [0, 1] (the 0-quantile is the minimum, the 1-quantile the maximum)"),
            found=f"p='{args.p}' — outside [0, 1]",
            next_action="pass p in [0, 1]",
        )
    ordered = sorted(numbers)
    position = p * (len(ordered) - 1)
    lower = int(position)
    if lower == len(ordered) - 1:
        return _emit("quantile", args, ordered[lower])
    fraction = position - lower
    return _emit("quantile", args, ordered[lower] + fraction * (ordered[lower + 1] - ordered[lower]))


def _cmd_wilson(args: argparse.Namespace) -> int:
    """wilson — the Wilson score interval of k successes in n trials at z.

    Purpose: the score interval [lo, hi] — phat = k/n; d = 1 + z^2/n;
    center = (phat + z^2/(2n))/d; half = z*sqrt(phat(1-phat)/n +
    z^2/(4n^2))/d — the deterministic bound pair (the COMPOSITE
    ruled in at Q2: the interior is where transcription errors enter).
    Refuses when: k or n is non-integer (the int contract); k < 0;
    n <= 0; k > n; z is non-numeric or z <= 0.
    Re-run: deterministic — same k+n+z, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q2 (the collaborator's ruling,
    2026-11-25); the result rides the pair form (Q1's multi-value).
    """
    k = _require_int("k", str(args.k))
    if k is None:
        return 1
    n = _require_int("n", str(args.n))
    if n is None:
        return 1
    z = _parse_number(str(args.z))
    if z is None:
        _refuse_operand("z", str(args.z))
        return 1
    if k < 0 or n <= 0 or k > n or z <= 0:
        return _refuse(
            expected="integers k in [0, n] and n >= 1, and a positive z (a number)",
            found=(f"k='{args.k}', n='{args.n}', z='{args.z}' — outside the Wilson domain"),
            next_action="pass 0 <= k <= n, n >= 1, and z > 0",
        )
    phat = k / n
    d = 1 + z * z / n
    center = (phat + z * z / (2 * n)) / d
    half = z * math.sqrt(phat * (1 - phat) / n + z * z / (4 * n * n)) / d
    return _emit_pair("wilson", args, (center - half, center + half))


def _cmd_binom_test(args: argparse.Namespace) -> int:
    """binom-test — the exact binomial tail probability of k in n at p.

    Purpose: P(X >= k | n, p) one-sided; two-sided = 2*min(upper
    tail, lower tail) capped at 1. At p = 0.5 the tail sums run in
    EXACT arbitrary-precision ints (sum C(n, j) over the tail; the
    final division the only float); at general p in float terms
    (each term <= 1; tail underflow contributes 0).
    Refuses when: k or n is non-integer; k < 0; n < 0; k > n; p is
    non-numeric or outside [0, 1]; sided outside {two, one}; the
    general-p conversion overflows (the large-m boundary — the
    log-space lane is the honest route there).
    Re-run: deterministic — same k+n+p+sided, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q2 (the collaborator's ruling,
    2026-11-25) — the COMPOSITE ruled in (the sign test, the power
    ladder, the class bars).
    """
    k = _require_int("k", str(args.k))
    if k is None:
        return 1
    n = _require_int("n", str(args.n))
    if n is None:
        return 1
    p = _parse_number(str(args.p))
    if p is None:
        _refuse_operand("p", str(args.p))
        return 1
    sided = _require_enum(str(args.sided), ("two", "one"), "sided")
    if sided is None:
        return 1
    if k < 0 or n < 0 or k > n or p < 0 or p > 1:
        return _refuse(
            expected="integers k in [0, n] and n >= 0, and p in [0, 1]",
            found=(f"k='{args.k}', n='{args.n}', p='{args.p}' — outside the binomial domain"),
            next_action="pass 0 <= k <= n, n >= 0, and p in [0, 1]",
        )
    if p == 0.5:
        upper = sum(math.comb(n, j) for j in range(k, n + 1))
        if sided == "one":
            return _emit("binom-test", args, upper / (2**n))
        lower = sum(math.comb(n, j) for j in range(0, k + 1))
        return _emit("binom-test", args, min(1.0, 2 * min(upper, lower) / (2**n)))
    try:
        upper = sum(math.comb(n, j) * p**j * (1 - p) ** (n - j) for j in range(k, n + 1))
    except OverflowError:
        return _refuse(
            expected="a representable exact-int tail (the general-p float terms fit float64)",
            found=(f"n='{args.n}' — the binomial coefficients overflow float64 at general p"),
            next_action="the log-space lane is the large-m route (log-combination + log-beta)",
        )
    if sided == "one":
        return _emit("binom-test", args, upper)
    lower = sum(math.comb(n, j) * p**j * (1 - p) ** (n - j) for j in range(0, k + 1))
    return _emit("binom-test", args, min(1.0, 2 * min(upper, lower)))


def _emit_list(op: str, args: argparse.Namespace, values: list[object]) -> int:
    """Print the list trace line on stdout — the structural result form.

    Purpose: one JSON object per run — {"op","args","result"} — the
    result an ARRAY of arbitrary JSON values (shuffle's permutation:
    the structural class, never the numeric — no coercion, the values
    as-is), compact and timestamp-free.
    Refuses when: never on shape — the emission is structural.
    Re-run: deterministic — same inputs, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q1/Q4 (the collaborator's ruling,
    2026-11-25).
    """
    raw_args = {key: value for key, value in vars(args).items() if key not in ("handler", "subcommand")}
    print(json.dumps({"op": op, "args": raw_args, "result": values}))
    return 0


def _cmd_normal_cdf(args: argparse.Namespace) -> int:
    """normal-cdf — the standard normal CDF at x.

    Purpose: statistics.NormalDist().cdf — Phi(x), deterministic.
    Refuses when: x is non-numeric (the function is total: no domain
    refusals).
    Re-run: deterministic — same x, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25).
    """
    x = _parse_number(str(args.x))
    if x is None:
        _refuse_operand("x", str(args.x))
        return 1
    return _emit("normal-cdf", args, statistics.NormalDist().cdf(x))


def _cmd_normal_ppf(args: argparse.Namespace) -> int:
    """normal-ppf — the standard normal inverse CDF at q.

    Purpose: statistics.NormalDist().inv_cdf — Phi^-1(q), the
    threshold-constant source (1.96 at q=0.975).
    Refuses when: q is non-numeric or outside the open interval
    (0, 1) — at 0 or 1 the inverse is -/+ infinity, outside the
    representable contract.
    Re-run: deterministic — same q, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25).
    """
    q = _parse_number(str(args.q))
    if q is None:
        _refuse_operand("q", str(args.q))
        return 1
    if q <= 0 or q >= 1:
        return _refuse(
            expected="q as a probability strictly inside (0, 1)",
            found=f"q='{args.q}' — at 0 or 1 the inverse CDF is infinite, outside the range",
            next_action="pass q strictly inside (0, 1)",
        )
    return _emit("normal-ppf", args, statistics.NormalDist().inv_cdf(q))


def _cmd_log(args: argparse.Namespace) -> int:
    """log — the natural logarithm of a.

    Purpose: math.log — ln(a), the log-space front door (any base
    stepwise: log(a)/log(b)).
    Refuses when: a is non-numeric or a <= 0 (the log domain).
    Re-run: deterministic — same a, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25 — Tier 2, the measurement diet).
    """
    a = _parse_number(str(args.a))
    if a is None:
        _refuse_operand("a", str(args.a))
        return 1
    if a <= 0:
        return _refuse(
            expected="a positive a (the logarithm's domain)",
            found=f"a='{args.a}' — the log of a non-positive number is undefined",
            next_action="pass a > 0",
        )
    return _emit("log", args, math.log(a))


def _cmd_exp(args: argparse.Namespace) -> int:
    """exp — e raised to a.

    Purpose: math.exp — e^a, the log-space chains' return step.
    Refuses when: a is non-numeric, or the result unrepresentable
    (the inf guard: e^710 overflows float64 — the range refusal).
    Re-run: deterministic — same a, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25).
    """
    a = _parse_number(str(args.a))
    if a is None:
        _refuse_operand("a", str(args.a))
        return 1
    try:
        result = math.exp(a)
    except OverflowError:
        return _refuse(
            expected="a representable result (a number the engine can print)",
            found=(f"a='{args.a}' — e^a overflows float64 (the representable range)"),
            next_action="rescale the exponent, or route the chain through the log-space lane",
        )
    return _emit("exp", args, result)


def _cmd_log_factorial(args: argparse.Namespace) -> int:
    """log-factorial — the natural log of n!.

    Purpose: math.lgamma(n + 1) — ln(n!), the large-m route past the
    171! float boundary (the boundary rides the conversion, never
    this op).
    Refuses when: n is non-numeric or non-integer, or n < 0.
    Re-run: deterministic — same n, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25).
    """
    n = _require_int("n", str(args.n))
    if n is None:
        return 1
    if n < 0:
        return _refuse(
            expected="a non-negative integer n (no negative factorial exists)",
            found=f"n='{args.n}' — the log-factorial of a negative count is undefined",
            next_action="pass n >= 0",
        )
    return _emit("log-factorial", args, math.lgamma(n + 1))


def _cmd_log_combination(args: argparse.Namespace) -> int:
    """log-combination — the natural log of C(n, k).

    Purpose: lgamma(n+1) - lgamma(k+1) - lgamma(n-k+1) — ln C(n,k),
    the far-ladder route (the combination's domain, log-carried).
    Refuses when: n or k is non-integer; n < 0; k < 0; k > n (the
    combination domain held at the log tier).
    Re-run: deterministic — same n+k, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25).
    """
    n = _require_int("n", str(args.n))
    if n is None:
        return 1
    k = _require_int("k", str(args.k))
    if k is None:
        return 1
    if n < 0 or k < 0 or k > n:
        return _refuse(
            expected="integers with 0 <= k <= n (the combination domain)",
            found=(f"n='{args.n}', k='{args.k}' — outside the combination domain"),
            next_action="pass 0 <= k <= n",
        )
    return _emit("log-combination", args, math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1))


def _cmd_log_beta(args: argparse.Namespace) -> int:
    """log-beta — the natural log of the Beta function B(a, b).

    Purpose: lgamma(a) + lgamma(b) - lgamma(a + b) — ln B(a,b), the
    Bayes-factor chain's core term.
    Refuses when: a or b is non-numeric or non-positive (the Beta
    domain).
    Re-run: deterministic — same a+b, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25).
    """
    a = _parse_number(str(args.a))
    if a is None:
        _refuse_operand("a", str(args.a))
        return 1
    b = _parse_number(str(args.b))
    if b is None:
        _refuse_operand("b", str(args.b))
        return 1
    if a <= 0 or b <= 0:
        return _refuse(
            expected="positive a and b (the Beta function's domain)",
            found=(f"a='{args.a}', b='{args.b}' — the Beta of a non-positive argument is undefined"),
            next_action="pass a > 0 and b > 0",
        )
    return _emit("log-beta", args, math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b))


def _cmd_chisquare(args: argparse.Namespace) -> int:
    """chisquare — the goodness-of-fit statistic of observed vs expected.

    Purpose: chi^2 = sum((O - E)^2 / E) over the paired cells, with
    df = len - 1 — the pair result [statistic, df] (the multi-value
    form). The p-VALUE at df > 1 is NOT stdlib-carried (the honest
    limit): the op emits the statistic; the df=1 p composes stepwise
    (sqrt -> normal-cdf -> complement -> x2); df > 1 rides the ruled
    critical-value table, never a silent approximation.
    Refuses when: observed or expected is not a JSON array of finite
    numbers, or an array is empty; the lengths differ; any expected
    cell is <= 0.
    Re-run: deterministic — same arrays, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25); the class-balance consumers.
    """
    observed = _require_numeric_array(str(args.observed), "chisquare")
    if observed is None:
        return 1
    expected = _require_numeric_array(str(args.expected), "chisquare")
    if expected is None:
        return 1
    if len(observed) != len(expected):
        return _refuse(
            expected="observed and expected as equal-length arrays",
            found=(f"observed carries {len(observed)} cells, expected {len(expected)} — the lengths differ"),
            next_action="pass equal-length arrays",
        )
    if any(cell <= 0 for cell in expected):
        return _refuse(
            expected="expected cells all positive (the statistic divides by E)",
            found="an expected cell is <= 0 — the statistic is undefined there",
            next_action="pass expected cells all > 0",
        )
    statistic = sum((o - e) ** 2 / e for o, e in zip(observed, expected, strict=True))
    return _emit_pair("chisquare", args, (statistic, float(len(observed) - 1)))


def _cmd_shuffle(args: argparse.Namespace) -> int:
    """shuffle — the deterministic permutation of a JSON array under a seed.

    Purpose: random.Random(seed).shuffle — the seeded permutation
    (the S311 ruled seam precedent: the seeded simulation,
    stdlib-reproducible; the seed IS the input — same seed, same
    permutation, process- and PYTHONHASHSEED-independent). THE SEED
    IS REQUIRED (determinism demands the operand — the one place
    entropy could creep, foreclosed by construction). The values are
    STRUCTURAL (any JSON elements — the presentation-draw class);
    the result is the permuted array (the list form).
    Refuses when: values is not a JSON array or is empty; the seed
    is non-integer (the int contract).
    (the seed refusal teaches the derive-seed route — the tool's own law)
    Re-run: deterministic — same values+seed, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 + the purity ruling (2026-11-25):
    the explicit-seed law; NO RNG-without-seed op exists anywhere in
    the engine.
    """
    values = _require_array(str(args.values))
    if values is None:
        return 1
    if not values:
        return _refuse(
            expected="a non-empty JSON array (the shuffle of nothing is the empty list)",
            found=f"values='{args.values}' — an empty array",
            next_action="pass a non-empty JSON array",
        )
    seed = _require_int("seed", str(args.seed))
    if seed is None:
        return _refuse(
            expected=(
                "seed as an integer (as a string) — the seed is REQUIRED: determinism "
                "demands the operand (the one place entropy could creep, foreclosed "
                "by construction; the same seed always yields the same permutation)"
            ),
            found=f"seed='{args.seed}' — not an integer",
            next_action=(
                "pass an explicit integer seed — or derive one from any handle "
                "(a run_id, a sitting's name) via derive-seed, then pass it here"
            ),
        )
    permutation = list(values)
    random.Random(seed).shuffle(permutation)
    return _emit_list("shuffle", args, permutation)


def _cmd_derive_seed(args: argparse.Namespace) -> int:
    """derive-seed — the stable integer seed derived from a text handle.

    Purpose: the blake2b digest of the text (first 8 bytes,
    big-endian) as an integer — prioritree's own derive_seed form
    (scheduler.py: the run_id -> seed mapping), tool-carried so a
    seed never enters a report as a bare prose constant.
    Refuses when: never on domain (a pure function of its text
    argument — the string exemption, total).
    Re-run: deterministic — same text, same trace bytes.
    Touches: stdout only.
    Provenance: Q-CALC-EXPANSION Q4 (the collaborator's ruling,
    2026-11-25); the replay story citable as a trace.
    """
    digest = hashlib.blake2b(str(args.text).encode("utf-8")).digest()[:8]
    return _emit("derive-seed", args, int.from_bytes(digest, "big"))


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="calculate.py",
        description=(
            "pure-query arithmetic and counting (Q-CALC-1) — 30 "
            "deterministic ops (Q-CALC-1's six arithmetic and counting + "
            "Q-CALC-EXPANSION's 24: statistics, combinatorics, "
            "distribution, seeded permutation)"
        ),
    )
    subparsers = parser.add_subparsers(dest="subcommand", required=True, metavar="<subcommand>")

    for name, handler, help_text in (
        ("add", _cmd_add, "a + b — the sum of two numbers"),
        ("subtract", _cmd_subtract, "a - b — the difference of two numbers"),
        ("multiply", _cmd_multiply, "a * b — the product of two numbers"),
        ("divide", _cmd_divide, "a / b — the quotient of two numbers"),
    ):
        sub = subparsers.add_parser(name, help=help_text)
        sub.add_argument("--a", required=True, help="the first operand (a number, as a string)")
        sub.add_argument("--b", required=True, help="the second operand (a number, as a string)")
        sub.set_defaults(handler=handler)

    for name, handler, help_text in (
        ("sum", _cmd_sum, "the total of a JSON array of numbers"),
        ("count", _cmd_count, "the number of elements in a JSON array"),
    ):
        sub = subparsers.add_parser(name, help=help_text)
        sub.add_argument("--values", required=True, help="the list to aggregate (a JSON array)")
        sub.set_defaults(handler=handler)

    sub = subparsers.add_parser("sqrt", help="the principal square root of a")
    sub.add_argument("--a", required=True, help="the radicand (a number, as a string)")
    sub.set_defaults(handler=_cmd_sqrt)

    sub = subparsers.add_parser("power", help="a raised to b (b real)")
    sub.add_argument("--a", required=True, help="the base (a number, as a string)")
    sub.add_argument("--b", required=True, help="the exponent (a number, as a string)")
    sub.set_defaults(handler=_cmd_power)

    sub = subparsers.add_parser("factorial", help="n! in exact, arbitrary-precision int")
    sub.add_argument("--n", required=True, help="the count (an integer, as a string)")
    sub.set_defaults(handler=_cmd_factorial)

    sub = subparsers.add_parser("combination", help="C(n, k) in exact int")
    sub.add_argument("--n", required=True, help="the population count (an integer, as a string)")
    sub.add_argument("--k", required=True, help="the selection count (an integer, as a string)")
    sub.set_defaults(handler=_cmd_combination)

    sub = subparsers.add_parser("proportion", help="the share part/whole")
    sub.add_argument("--part", required=True, help="the part (a number, as a string)")
    sub.add_argument("--whole", required=True, help="the whole (a nonzero number, as a string)")
    sub.set_defaults(handler=_cmd_proportion)

    sub = subparsers.add_parser("mean", help="the arithmetic mean of a JSON array of finite numbers")
    sub.add_argument("--values", required=True, help="the list (a non-empty JSON array of numbers)")
    sub.set_defaults(handler=_cmd_mean)

    sub = subparsers.add_parser("variance", help="the population or sample variance of a JSON array")
    sub.add_argument("--values", required=True, help="the list (a non-empty JSON array of numbers)")
    sub.add_argument("--form", required=True, help="the form: population or sample")
    sub.set_defaults(handler=_cmd_variance)

    sub = subparsers.add_parser("stddev", help="the population or sample standard deviation of a JSON array")
    sub.add_argument("--values", required=True, help="the list (a non-empty JSON array of numbers)")
    sub.add_argument("--form", required=True, help="the form: population or sample")
    sub.set_defaults(handler=_cmd_stddev)

    sub = subparsers.add_parser("max", help="the greatest element of a JSON array of finite numbers")
    sub.add_argument("--values", required=True, help="the list (a non-empty JSON array of numbers)")
    sub.set_defaults(handler=_cmd_max)

    sub = subparsers.add_parser("min", help="the least element of a JSON array of finite numbers")
    sub.add_argument("--values", required=True, help="the list (a non-empty JSON array of numbers)")
    sub.set_defaults(handler=_cmd_min)

    sub = subparsers.add_parser("median", help="the middle value of a JSON array of finite numbers")
    sub.add_argument("--values", required=True, help="the list (a non-empty JSON array of numbers)")
    sub.set_defaults(handler=_cmd_median)

    sub = subparsers.add_parser("quantile", help="the p-quantile by fixed (n-1)-based linear interpolation")
    sub.add_argument("--values", required=True, help="the list (a non-empty JSON array of numbers)")
    sub.add_argument("--p", required=True, help="the quantile position in [0, 1] (a number, as a string)")
    sub.set_defaults(handler=_cmd_quantile)

    sub = subparsers.add_parser("wilson", help="the Wilson score interval [lo, hi] of k in n at z")
    sub.add_argument("--k", required=True, help="the success count (an integer, as a string)")
    sub.add_argument("--n", required=True, help="the trial count (an integer >= 1, as a string)")
    sub.add_argument("--z", required=True, help="the z constant (a positive number, as a string)")
    sub.set_defaults(handler=_cmd_wilson)

    sub = subparsers.add_parser("binom-test", help="the exact binomial tail p of k in n at p (one or two sided)")
    sub.add_argument("--k", required=True, help="the success count (an integer, as a string)")
    sub.add_argument("--n", required=True, help="the trial count (an integer >= 0, as a string)")
    sub.add_argument("--p", required=True, help="the null probability in [0, 1] (a number, as a string)")
    sub.add_argument("--sided", required=True, help="the sidedness: two or one")
    sub.set_defaults(handler=_cmd_binom_test)
    sub = subparsers.add_parser("normal-cdf", help="the standard normal CDF at x")
    sub.add_argument("--x", required=True, help="the point (a number, as a string)")
    sub.set_defaults(handler=_cmd_normal_cdf)

    sub = subparsers.add_parser("normal-ppf", help="the standard normal inverse CDF at q")
    sub.add_argument("--q", required=True, help="the probability strictly inside (0, 1) (a number, as a string)")
    sub.set_defaults(handler=_cmd_normal_ppf)

    sub = subparsers.add_parser("log", help="the natural logarithm of a")
    sub.add_argument("--a", required=True, help="the argument (a positive number, as a string)")
    sub.set_defaults(handler=_cmd_log)

    sub = subparsers.add_parser("exp", help="e raised to a")
    sub.add_argument("--a", required=True, help="the exponent (a number, as a string)")
    sub.set_defaults(handler=_cmd_exp)

    sub = subparsers.add_parser("log-factorial", help="the natural log of n!")
    sub.add_argument("--n", required=True, help="the count (a non-negative integer, as a string)")
    sub.set_defaults(handler=_cmd_log_factorial)

    sub = subparsers.add_parser("log-combination", help="the natural log of C(n, k)")
    sub.add_argument("--n", required=True, help="the population count (an integer, as a string)")
    sub.add_argument("--k", required=True, help="the selection count (an integer, as a string)")
    sub.set_defaults(handler=_cmd_log_combination)

    sub = subparsers.add_parser("log-beta", help="the natural log of the Beta function B(a, b)")
    sub.add_argument("--a", required=True, help="the first shape (a positive number, as a string)")
    sub.add_argument("--b", required=True, help="the second shape (a positive number, as a string)")
    sub.set_defaults(handler=_cmd_log_beta)

    sub = subparsers.add_parser("chisquare", help="the goodness-of-fit [statistic, df] of observed vs expected")
    sub.add_argument("--observed", required=True, help="the observed counts (a non-empty JSON array of numbers)")
    sub.add_argument("--expected", required=True, help="the expected counts (a JSON array of positive numbers)")
    sub.set_defaults(handler=_cmd_chisquare)

    sub = subparsers.add_parser("shuffle", help="the deterministic permutation of a JSON array under a seed")
    sub.add_argument("--values", required=True, help="the list (a non-empty JSON array)")
    sub.add_argument("--seed", required=True, help="the seed (an integer, as a string — required, never random)")
    sub.set_defaults(handler=_cmd_shuffle)

    sub = subparsers.add_parser("derive-seed", help="the stable integer seed derived from a text handle")
    sub.add_argument("--text", required=True, help="the handle (any string)")
    sub.set_defaults(handler=_cmd_derive_seed)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    handler: Callable[[argparse.Namespace], int] = args.handler
    return handler(args)


if __name__ == "__main__":
    sys.exit(main())
