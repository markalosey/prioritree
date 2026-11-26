# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The G-engine's KAT — the calculate-expansion effort's first seed.

The verification seat's composed battery (packet build/engine-verification,
the G-ENGINE second eyes, kensho, 2026-11-25): the complete engine (30 ops,
scripts/calculate.py at the tool-ambiguity-reduction worktree) fired LIVE —
every case banked at the known-ask specs' section-2 validation lists (the
2026-11-24-calculate-expansion store: build/engine-ask-a.md, -b.md, -c.md,
-d.md, -e.md + engine-exp-residue.md), plus the floor row (ruff + pyright
zero-and-zero, fired from this battery — the kensho pack carries no lint
tool).

THE FORM (the S603 fixed-argv subprocess battery, the U-5 seat-composed
precedent): every row fires the engine as a subprocess — subprocess.run over
[sys.executable, the engine path, the op, the --flag=value argv] — and
asserts stdout BYTES. The positive rows build the expected trace line by
json.dumps of the expected {"op","args","result"} object, reproducing the
engine's exact bytes (the compact shape, the raw flag values as sent, the
int coercion at result — 4, never 4.0); the refusal rows pin the doctrine
shape (exit 1, stdout byte-empty, REFUSED / Expected / Found / Next-action
on stderr — never a traceback).

THE HONEST BOUNDARY (FR-MEM-0488): the wrapper channel (the calculate tool
at the seat) serves main's stale engine — this battery's subprocess fire IS
the live proof; the wrapper-channel re-fire rides the post-restart
corollary. The battery channel's sandbox law inherits (the engine is a
pure query; the lake never touched).

THE PLATFORM LAW (FR-MEM-0501, the battery's first fire): the
libm-derived bytes (math.erf's CDF, the inv_cdf refinement, math.lgamma)
are PLATFORM-CLASS — one ULP apart across libm implementations (the
x86-class literals vs this host's Apple libm). The literal rows pin only
platform-stable bytes (the exact-int arithmetic, the pure-parse
divisions); the libm-touched expectations derive IN-PROCESS (the same
stdlib call the engine makes, the same platform) — the byte-assert held,
the libm byte the engine's own determinism domain. A future platform
divergence at any remaining literal row is the venv-pair metadata's
RE-BASELINE EVENT (Q3's ruling).
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import random
import shutil
import statistics
import subprocess
import sys
from pathlib import Path
from typing import Any

import pytest

ROOT = Path(__file__).resolve().parents[1]
ENGINE = ROOT / ".opencode" / "scripts" / "calculate.py"


def _fire(*argv: str) -> subprocess.CompletedProcess[bytes]:
    """Fire the S603 fixed-argv subprocess — [sys.executable, the engine path, the op, the flags]."""
    return subprocess.run([sys.executable, str(ENGINE), *argv], capture_output=True, check=False)


def _assert_trace(argv: tuple[str, ...], expected: dict[str, Any]) -> None:
    """Assert the positive row — stdout is the trace line, byte-asserted.

    The expected object json.dumps to the exact engine bytes: the compact
    {"op","args","result"} shape, the raw flag values as sent, the int
    coercion at result (json.dumps(4) is "4" — never "4.0").
    """
    proc = _fire(*argv)
    assert proc.returncode == 0, (argv, proc.stderr.decode("utf-8"))
    assert proc.stderr == b"", (argv, proc.stderr)
    assert proc.stdout == (json.dumps(expected) + "\n").encode("utf-8"), (argv, proc.stdout)


def _assert_refused(argv: tuple[str, ...], *signatures: str) -> None:
    """Assert the refusal row — exit 1, stdout byte-empty, the ThreePart block, never a traceback."""
    proc = _fire(*argv)
    assert proc.returncode == 1, (argv, proc.stdout, proc.stderr)
    assert proc.stdout == b"", (argv, proc.stdout)
    text = proc.stderr.decode("utf-8")
    assert text.startswith("REFUSED\n"), (argv, text)
    assert "\nExpected: " in text, (argv, text)
    assert "\nFound: " in text, (argv, text)
    assert "\nNext-action: " in text, (argv, text)
    assert "Traceback" not in text, (argv, text)
    for signature in signatures:
        assert signature in text, (argv, signature, text)


# THE SIX (ask A) — the trace lines live; the int coercion pinned (result 4, never 4.0).
_THE_SIX: list[tuple[tuple[str, ...], dict[str, Any]]] = [
    (("add", "--a=2", "--b=2"), {"op": "add", "args": {"a": "2", "b": "2"}, "result": 4}),
    (("add", "--a=2", "--b=3"), {"op": "add", "args": {"a": "2", "b": "3"}, "result": 5}),
    (("divide", "--a=10", "--b=4"), {"op": "divide", "args": {"a": "10", "b": "4"}, "result": 2.5}),
    (("sum", "--values=[1,2,3]"), {"op": "sum", "args": {"values": "[1,2,3]"}, "result": 6}),
    (("count", "--values=[1,2,3]"), {"op": "count", "args": {"values": "[1,2,3]"}, "result": 3}),
]

# ASK B — the Tier-1a band: sqrt, power, factorial, combination, proportion, mean, variance.
_TIER_1A: list[tuple[tuple[str, ...], dict[str, Any]]] = [
    (("sqrt", "--a=4"), {"op": "sqrt", "args": {"a": "4"}, "result": 2}),
    (("power", "--a=0.825", "--b=8"), {"op": "power", "args": {"a": "0.825", "b": "8"}, "result": 0.214600924414215}),
    (("power", "--a=2", "--b=10"), {"op": "power", "args": {"a": "2", "b": "10"}, "result": 1024}),
    (("factorial", "--n=5"), {"op": "factorial", "args": {"n": "5"}, "result": 120}),
    (("combination", "--n=22", "--k=12"), {"op": "combination", "args": {"n": "22", "k": "12"}, "result": 646646}),
    (
        ("proportion", "--part=12", "--whole=22"),
        {"op": "proportion", "args": {"part": "12", "whole": "22"}, "result": 0.5454545454545454},
    ),
    (("mean", "--values=[1,2,3,4]"), {"op": "mean", "args": {"values": "[1,2,3,4]"}, "result": 2.5}),
    (
        ("variance", "--values=[1,2,3,4]", "--form=population"),
        {"op": "variance", "args": {"values": "[1,2,3,4]", "form": "population"}, "result": 1.25},
    ),
    (
        ("variance", "--values=[1,2,3,4]", "--form=sample"),
        {"op": "variance", "args": {"values": "[1,2,3,4]", "form": "sample"}, "result": 1.6666666666666667},
    ),
]

# ASK C — the Tier-1b band: stddev, max, min, median, quantile.
_TIER_1B: list[tuple[tuple[str, ...], dict[str, Any]]] = [
    (
        ("stddev", "--values=[1,2,3,4]", "--form=population"),
        {"op": "stddev", "args": {"values": "[1,2,3,4]", "form": "population"}, "result": 1.118033988749895},
    ),
    (
        ("stddev", "--values=[1,2,3,4]", "--form=sample"),
        {"op": "stddev", "args": {"values": "[1,2,3,4]", "form": "sample"}, "result": 1.2909944487358056},
    ),
    (("max", "--values=[1,5,3]"), {"op": "max", "args": {"values": "[1,5,3]"}, "result": 5}),
    (("min", "--values=[3,1,2]"), {"op": "min", "args": {"values": "[3,1,2]"}, "result": 1}),
    (("median", "--values=[1,3,5,7]"), {"op": "median", "args": {"values": "[1,3,5,7]"}, "result": 4}),
    (("median", "--values=[1,2,3,4]"), {"op": "median", "args": {"values": "[1,2,3,4]"}, "result": 2.5}),
    (
        ("quantile", "--values=[1,2,3,4]", "--p=0.25"),
        {"op": "quantile", "args": {"values": "[1,2,3,4]", "p": "0.25"}, "result": 1.75},
    ),
    (
        ("quantile", "--values=[1,2,3,4]", "--p=0.5"),
        {"op": "quantile", "args": {"values": "[1,2,3,4]", "p": "0.5"}, "result": 2.5},
    ),
    (
        ("quantile", "--values=[1,2,3,4]", "--p=0"),
        {"op": "quantile", "args": {"values": "[1,2,3,4]", "p": "0"}, "result": 1},
    ),
    (
        ("quantile", "--values=[1,2,3,4]", "--p=1"),
        {"op": "quantile", "args": {"values": "[1,2,3,4]", "p": "1"}, "result": 4},
    ),
    (("quantile", "--values=[7]", "--p=0.3"), {"op": "quantile", "args": {"values": "[7]", "p": "0.3"}, "result": 7}),
]

# ASK D — the composites: binom-test's exact-int lane (the KAT headline byte-asserted);
# wilson's positive and the general-p one-sided atom are the derived rows below.
_COMPOSITES: list[tuple[tuple[str, ...], dict[str, Any]]] = [
    (
        ("binom-test", "--k=12", "--n=22", "--p=0.5", "--sided=two"),
        {"op": "binom-test", "args": {"k": "12", "n": "22", "p": "0.5", "sided": "two"}, "result": 0.8318119049072266},
    ),
    (
        ("binom-test", "--k=12", "--n=22", "--p=0.5", "--sided=one"),
        {"op": "binom-test", "args": {"k": "12", "n": "22", "p": "0.5", "sided": "one"}, "result": 0.4159059524536133},
    ),
    (
        ("binom-test", "--k=0", "--n=0", "--p=0.5", "--sided=two"),
        {"op": "binom-test", "args": {"k": "0", "n": "0", "p": "0.5", "sided": "two"}, "result": 1},
    ),
]

# ASK E — the final band: normal-cdf/ppf, the log-space tier (exp's residue row below);
# log-combination, chisquare, shuffle, derive-seed are the derived rows below.
_FINAL_BAND: list[tuple[tuple[str, ...], dict[str, Any]]] = [
    (("normal-cdf", "--x=0"), {"op": "normal-cdf", "args": {"x": "0"}, "result": 0.5}),
    (("log", "--a=1"), {"op": "log", "args": {"a": "1"}, "result": 0}),
    (("exp", "--a=1"), {"op": "exp", "args": {"a": "1"}, "result": 2.718281828459045}),
    (("exp", "--a=0"), {"op": "exp", "args": {"a": "0"}, "result": 1}),
    (("exp", "--a=-1"), {"op": "exp", "args": {"a": "-1"}, "result": 0.36787944117144233}),
    (("log-beta", "--a=1", "--b=1"), {"op": "log-beta", "args": {"a": "1", "b": "1"}, "result": 0}),
]

# THE REFUSAL ROWS — every refusal domain banked at the section-2 lists (argv, signature phrases).
_REFUSALS: list[tuple[tuple[str, ...], tuple[str, ...]]] = [
    # ask A — the finiteness contract + the two standing refusals (unchanged)
    (("sum", "--values=[NaN]"), ("sum totals finite numbers only", "finiteness contract")),
    (("divide", "--a=1", "--b=0"), ("division by zero is mathematically impossible",)),
    (("add", "--a=two", "--b=2"), ("a non-numeric string (prose, not a number)",)),
    # ask B
    (("sqrt", "--a=-1"), ("negative radicand has no real root",)),
    (("power", "--a=0", "--b=0"), ("the zero-base form is mathematically impossible",)),
    (("power", "--a=-4", "--b=0.5"), ("a negative base with a non-integer exponent",)),
    (("factorial", "--n=5.0"), ("a non-integer string", "the int contract")),
    (("factorial", "--n=-1"), ("the factorial of a negative count is undefined",)),
    (("combination", "--n=5", "--k=6"), ("the selection exceeds the population",)),
    (("proportion", "--part=1", "--whole=0"), ("no number is the quotient",)),
    (("mean", "--values=[]"), ("an empty array",)),
    (("mean", "--values=[NaN]"), ("finiteness contract",)),
    (("variance", "--values=[5]", "--form=sample"), ("the sample denominator n-1 is zero",)),
    (("variance", "--values=[1,2]", "--form=bogus"), ("outside the legal vocabulary",)),
    # ask C
    (("stddev", "--values=[5]", "--form=sample"), ("the sample denominator n-1 is zero",)),
    (("stddev", "--values=[1,2]", "--form=bogus"), ("outside the legal vocabulary",)),
    (("max", "--values=[]"), ("an empty array",)),
    (("max", "--values=[NaN]"), ("finiteness contract",)),
    (("quantile", "--values=[1,2]", "--p=1.5"), ("outside [0, 1]",)),
    (("quantile", "--values=[1,2]", "--p=abc"), ("a non-numeric string (prose, not a number)",)),
    # ask D — the composites' domain guards + the OverflowError lane
    (("wilson", "--k=23", "--n=22", "--z=1.96"), ("outside the Wilson domain",)),
    (("wilson", "--k=1", "--n=0", "--z=1.96"), ("outside the Wilson domain",)),
    (("wilson", "--k=12", "--n=22", "--z=0"), ("outside the Wilson domain",)),
    (("wilson", "--k=12.5", "--n=22", "--z=1.96"), ("a non-integer string",)),
    (
        ("binom-test", "--k=1000", "--n=2000", "--p=0.3", "--sided=two"),
        ("overflow float64 at general p", "log-space lane"),
    ),
    (("binom-test", "--k=12", "--n=22", "--p=0.5", "--sided=bogus"), ("outside the legal vocabulary",)),
    (("binom-test", "--k=12", "--n=22", "--p=1.5", "--sided=two"), ("outside the binomial domain",)),
    (("binom-test", "--k=-1", "--n=22", "--p=0.5", "--sided=two"), ("outside the binomial domain",)),
    (("binom-test", "--k=12", "--n=22.5", "--p=0.5", "--sided=two"), ("a non-integer string",)),
    # ask E — the final band's domain guards
    (("normal-cdf", "--x=abc"), ("a non-numeric string (prose, not a number)",)),
    (("normal-ppf", "--q=0"), ("strictly inside (0, 1)",)),
    (("normal-ppf", "--q=1.5"), ("strictly inside (0, 1)",)),
    (("log", "--a=0"), ("the log of a non-positive number is undefined",)),
    (("log", "--a=-1"), ("the log of a non-positive number is undefined",)),
    (("log-factorial", "--n=-1"), ("the log-factorial of a negative count is undefined",)),
    (("log-factorial", "--n=5.5"), ("a non-integer string",)),
    (("log-combination", "--n=5", "--k=6"), ("outside the combination domain",)),
    (("log-beta", "--a=0", "--b=1"), ("the Beta of a non-positive argument is undefined",)),
    (("chisquare", "--observed=[1]", "--expected=[0]"), ("an expected cell is <= 0",)),
    (("chisquare", "--observed=[1,2]", "--expected=[1]"), ("the lengths differ",)),
    (
        ("shuffle", "--values=[1,2,3]", "--seed=abc"),
        (
            "the seed is REQUIRED",
            "via derive-seed",
        ),
    ),
    (("shuffle", "--values=[]", "--seed=1"), ("an empty array",)),
]


@pytest.mark.parametrize(("argv", "expected"), _THE_SIX)
def test_the_six_trace_lines(argv: tuple[str, ...], expected: dict[str, Any]) -> None:
    """Ask A's positives — the trace line live; the int coercion pinned (4, never 4.0)."""
    _assert_trace(argv, expected)


@pytest.mark.parametrize(("argv", "expected"), _TIER_1A)
def test_the_tier_1a_positives(argv: tuple[str, ...], expected: dict[str, Any]) -> None:
    """Ask B's positives — the seven Tier-1a ops fired live."""
    _assert_trace(argv, expected)


@pytest.mark.parametrize(("argv", "expected"), _TIER_1B)
def test_the_tier_1b_positives(argv: tuple[str, ...], expected: dict[str, Any]) -> None:
    """Ask C's positives — the five Tier-1b ops fired live."""
    _assert_trace(argv, expected)


@pytest.mark.parametrize(("argv", "expected"), _COMPOSITES)
def test_the_composite_positives(argv: tuple[str, ...], expected: dict[str, Any]) -> None:
    """Ask D's positives — the exact-int lane; the KAT headline byte-asserted."""
    _assert_trace(argv, expected)


@pytest.mark.parametrize(("argv", "expected"), _FINAL_BAND)
def test_the_final_band_positives(argv: tuple[str, ...], expected: dict[str, Any]) -> None:
    """Ask E's positives — the final band's banked values fired live."""
    _assert_trace(argv, expected)


@pytest.mark.parametrize(("argv", "signatures"), _REFUSALS)
def test_the_refusal_domains(argv: tuple[str, ...], signatures: tuple[str, ...]) -> None:
    """Every refusal row — exit 1, stdout byte-empty, the ThreePart block, never a traceback."""
    _assert_refused(argv, *signatures)


def test_wilson_pair_form_and_derivation() -> None:
    """Wilson 12 22 1.96 — the [lo, hi] pair; the derivation restated, the bytes pinned here."""
    phat = 12 / 22
    z = 1.96
    d = 1 + z * z / 22
    center = (phat + z * z / (2 * 22)) / d
    half = z * math.sqrt(phat * (1 - phat) / 22 + z * z / (4 * 22 * 22)) / d
    lo = center - half
    hi = center + half
    assert lo <= hi
    assert 0.34 < lo < 0.35  # ask D's derivation corroboration
    assert 0.73 < hi < 0.74
    _assert_trace(
        ("wilson", "--k=12", "--n=22", "--z=1.96"),
        {"op": "wilson", "args": {"k": "12", "n": "22", "z": "1.96"}, "result": [lo, hi]},
    )


def test_binom_test_general_p_one_sided() -> None:
    """binom-test 17 22 0.75 one — the power-ladder atom (the general-p float-terms class)."""
    expected = sum(math.comb(22, j) * 0.75**j * 0.25 ** (22 - j) for j in range(17, 23))
    _assert_trace(
        ("binom-test", "--k=17", "--n=22", "--p=0.75", "--sided=one"),
        {"op": "binom-test", "args": {"k": "17", "n": "22", "p": "0.75", "sided": "one"}, "result": expected},
    )


def test_log_combination_is_ln_646646() -> None:
    """log-combination 22 12 — the lgamma chain (ln C(22,12) = ln 646646, corroborated)."""
    expected = math.lgamma(23) - math.lgamma(13) - math.lgamma(11)
    assert abs(expected - math.log(646646)) < 1e-9
    _assert_trace(
        ("log-combination", "--n=22", "--k=12"),
        {"op": "log-combination", "args": {"n": "22", "k": "12"}, "result": expected},
    )


def test_normal_cdf_derived() -> None:
    """normal-cdf 1.96 — the erf byte is platform-class (FR-MEM-0501): derived in-process."""
    expected = statistics.NormalDist().cdf(1.96)
    _assert_trace(
        ("normal-cdf", "--x=1.96"),
        {"op": "normal-cdf", "args": {"x": "1.96"}, "result": expected},
    )


def test_normal_ppf_derived() -> None:
    """normal-ppf 0.975 — the refinement byte is platform-class (FR-MEM-0501): derived."""
    expected = statistics.NormalDist().inv_cdf(0.975)
    _assert_trace(
        ("normal-ppf", "--q=0.975"),
        {"op": "normal-ppf", "args": {"q": "0.975"}, "result": expected},
    )


def test_log_factorial_derived() -> None:
    """log-factorial 5 — the lgamma byte is platform-class (FR-MEM-0501): derived + corroborated."""
    expected = math.lgamma(6)
    assert abs(expected - math.log(120)) < 1e-9
    _assert_trace(
        ("log-factorial", "--n=5"),
        {"op": "log-factorial", "args": {"n": "5"}, "result": expected},
    )


def test_chisquare_pair_form() -> None:
    """Chisquare [14,8] vs [11,11] — the [statistic, df] pair (18/11, df 1)."""
    expected_statistic = sum((o - e) ** 2 / e for o, e in zip([14, 8], [11, 11], strict=True))
    _assert_trace(
        ("chisquare", "--observed=[14,8]", "--expected=[11,11]"),
        {"op": "chisquare", "args": {"observed": "[14,8]", "expected": "[11,11]"}, "result": [expected_statistic, 1]},
    )


def test_shuffle_permutation_and_determinism() -> None:
    """Shuffle [1,2,3] seed=42 — the deterministic permutation + the IDENTICAL RE-RUN."""
    expected_permutation = [1, 2, 3]
    random.Random(42).shuffle(expected_permutation)
    expected_line = json.dumps(
        {"op": "shuffle", "args": {"values": "[1,2,3]", "seed": "42"}, "result": expected_permutation},
    )
    first = _fire("shuffle", "--values=[1,2,3]", "--seed=42")
    assert first.returncode == 0, first.stderr
    assert first.stdout == (expected_line + "\n").encode("utf-8"), first.stdout
    second = _fire("shuffle", "--values=[1,2,3]", "--seed=42")
    assert second.stdout == first.stdout  # the determinism proof — identical trace bytes


def test_derive_seed_blake2b_form() -> None:
    """derive-seed RUN-0001 — the stable blake2b int (prioritree's derive_seed form, byte-parity)."""
    expected = int.from_bytes(hashlib.blake2b(b"RUN-0001").digest()[:8], "big")
    _assert_trace(
        ("derive-seed", "--text=RUN-0001"),
        {"op": "derive-seed", "args": {"text": "RUN-0001"}, "result": expected},
    )


def test_the_exp_residue_three_part_refusal_never_a_traceback() -> None:
    """Exp 1000 — the ruled unrepresentable refusal (FR-MEM-0496's cure), never a traceback."""
    _assert_refused(
        ("exp", "--a=1000"),
        "e^a overflows float64 (the representable range)",
        "rescale the exponent, or route the chain through the log-space lane",
    )


def test_the_floor_ruff_and_pyright_zero_and_zero() -> None:
    """The floor fired from the battery's own lane — ruff + pyright, zero findings each.

    The kensho pack carries no lint tool (FR-MEM-0434's class), so the floor
    rides the same fixed-argv subprocess form: ruff check under the worktree's
    [tool.ruff] config; pyright --outputjson with the filesAnalyzed guard
    (the 0-files false-clean class, RN-TLDH-05) at the engine and this file.
    """
    battery = Path(__file__).resolve()
    ruff = shutil.which("ruff") or str(Path(sys.executable).parent / "ruff")
    linted = subprocess.run(
        [ruff, "check", str(ENGINE), str(battery)],
        capture_output=True,
        check=False,
        cwd=str(ROOT),
    )
    assert linted.returncode == 0, (linted.stdout + linted.stderr).decode("utf-8")
    pyright = shutil.which("pyright") or str(Path(sys.executable).parent / "pyright")
    typed = subprocess.run(
        [pyright, "--outputjson", ".opencode/scripts/calculate.py", "tests/test_calculate_expansion_kat.py"],
        capture_output=True,
        check=False,
        cwd=str(ROOT),
        env={**os.environ, "PYRIGHT_PYTHON_IGNORE_WARNINGS": "1"},
    )
    payload = json.loads(typed.stdout)
    summary = payload["summary"]
    files_analyzed = payload.get("filesAnalyzed", summary.get("filesAnalyzed", 0))
    assert files_analyzed >= 1, typed.stdout
    assert summary["errorCount"] == 0, typed.stdout
    assert summary["warningCount"] == 0, typed.stdout
    assert summary["informationCount"] == 0, typed.stdout
