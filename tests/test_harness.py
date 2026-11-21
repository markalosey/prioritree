# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The CLI-acceptance unit's tests — the arcs map (cli-acceptance-brief §1-§4).

The TIER FENCE named: this harness drives the REAL binary — the console
script's full path via FIXED-ARGV subprocess lists (the no-shell law), NO
prioritree import at all (kensho's act-4 gap closed by construction; a
missing shim FAILS the arc, never skips). The arcs: (1) the success arc —
7 invocations on one --home tmp home, each step's returncode + exact stdout
bytes, the persistence seam proven in the arc itself (each vote a separate
process, the file the sole carrier); (2) the determinism replay — the full
arc's stdout sequence on two fresh homes, byte-identical element-for-element;
(3) the refusal arcs R1-R3 — rc 1, stderr "refused —" prefix + the distinctive
needle, stdout == b"" (never a partial report on the pipe); R4 argparse's
channel — rc 2, the OS receipt of SystemExit (the usage bytes on stderr).

Provenance: cli-acceptance-brief §1-§4, packet synthesize/cli-acceptance,
route prioritree-cli, Q-cli-acceptance, G-CLI-ACCEPTANCE, 2026-11-21 session.
The S101/PLR2004 tests ruling stands.
"""

import subprocess
import sys
from pathlib import Path

# The invocation instrument (§1): the console script's FULL path — sibling of
# the active interpreter, the editable install's script home under uv run.
_SHIM = Path(sys.executable).parent / "prioritree"
# Payload constants (content-in-configuration): the grammar's tokens, the
# expected stdout bytes per step, and the tally frozen whole as BYTES — the
# same ten lines test_cli.py asserts in-process, byte-encoded for the pipe.
_ITEMS = ("a:alpha", "b:bravo", "c:charlie")
_OPERATOR_ID = "operator-1"
_QUESTION = "which comes first?"
_COMPARATOR_ID = "comparator-1"
_HUMAN = "human"
_PREFER_A = "prefer-a"
_HOME_FLAG = "--home"
_RUN_ONE = "RUN-0001"
_REGISTER_OUT = b"RUN-0001\n"
_NEXT_PAIR_OUT = b"pair\ta\tb\t0\n"
_VOTE_ONE_OUT = b"vote\tVOTE-0001\t1\n"
_VOTE_TWO_OUT = b"vote\tVOTE-0002\t2\n"
_VOTE_THREE_OUT = b"vote\tVOTE-0003\t3\n"
_EXHAUSTED_PREFIX = "exhausted —".encode()
_TALLY_NEEDLE = b"tally"
_REFUSED_PREFIX = "refused —".encode()
_TALLY_ABC = (
    b"rank\ta\n"
    b"rank\tb\n"
    b"rank\tc\n"
    b"counts\ta\t2\t0\t0\n"
    b"counts\tb\t1\t1\t0\n"
    b"counts\tc\t0\t2\t0\n"
    b"coverage\t1\tTrue\n"
    b"pairs\ta\tb\t1\n"
    b"pairs\ta\tc\t1\n"
    b"pairs\tb\tc\t1\n"
    b"version\twin-rate-v1\n"
)


def _run(argv: list[str]) -> subprocess.CompletedProcess[bytes]:
    """Invoke the real binary — the fixed-argv, no-shell invocation instrument (the no-shell law)."""
    return subprocess.run([str(_SHIM), *argv], check=False, capture_output=True)


def _register_argv(home: Path) -> list[str]:
    """Compose the register step's argv — subcommand, args, then --home (the AFTER placement)."""
    return ["register", *_ITEMS, "--operator-id", _OPERATOR_ID, "--question", _QUESTION, _HOME_FLAG, str(home)]


def _vote_argv(home: Path, item_a: str, item_b: str) -> list[str]:
    """Compose one vote step's argv — the served canonical order, prefer-a each."""
    return ["vote", _RUN_ONE, item_a, item_b, _PREFER_A, _COMPARATOR_ID, _HUMAN, _HOME_FLAG, str(home)]


def _arc_argv_sequence(home: Path) -> list[list[str]]:
    """Compose the full 7-invocation arc's argv sequence (§2) — one --home, seven processes."""
    return [
        _register_argv(home),
        ["next", _RUN_ONE, _HOME_FLAG, str(home)],
        _vote_argv(home, "a", "b"),
        _vote_argv(home, "a", "c"),
        _vote_argv(home, "b", "c"),
        ["next", _RUN_ONE, _HOME_FLAG, str(home)],
        ["tally", _RUN_ONE, _HOME_FLAG, str(home)],
    ]


def _drive_arc(home: Path) -> list[subprocess.CompletedProcess[bytes]]:
    """Drive the full arc on one home — each step a separate process, the file the sole carrier."""
    return [_run(argv) for argv in _arc_argv_sequence(home)]


def test_arc_seven_invocations_green(tmp_path: Path) -> None:
    """The success arc: 7 invocations on one tmp home — every rc 0 and the exact stdout bytes per step."""
    steps = _drive_arc(tmp_path)
    assert [step.returncode for step in steps] == [0, 0, 0, 0, 0, 0, 0]
    register, next_one, vote_ab, vote_ac, vote_bc, next_two, tally = steps
    assert register.stdout == _REGISTER_OUT
    assert next_one.stdout == _NEXT_PAIR_OUT
    assert vote_ab.stdout == _VOTE_ONE_OUT
    assert vote_ac.stdout == _VOTE_TWO_OUT
    assert vote_bc.stdout == _VOTE_THREE_OUT
    assert next_two.stdout.startswith(_EXHAUSTED_PREFIX)
    assert _TALLY_NEEDLE in next_two.stdout
    assert tally.stdout == _TALLY_ABC


def test_determinism_replay_byte_identical(tmp_path: Path) -> None:
    """The determinism replay: the full arc on two fresh homes yields byte-identical stdout sequences."""
    one = _drive_arc(tmp_path / "one")
    two = _drive_arc(tmp_path / "two")
    assert [step.returncode for step in one] == [0, 0, 0, 0, 0, 0, 0]
    assert [step.returncode for step in two] == [0, 0, 0, 0, 0, 0, 0]
    assert [step.stdout for step in one] == [step.stdout for step in two]


def test_refusal_unknown_run_exit_one(tmp_path: Path) -> None:
    """R1 the unknown run: next RUN-9999 → rc 1, the refused prefix + the run id on stderr, stdout empty."""
    step = _run(["next", "RUN-9999", _HOME_FLAG, str(tmp_path)])
    assert step.returncode == 1
    assert step.stderr.startswith(_REFUSED_PREFIX)
    assert b"RUN-9999" in step.stderr
    assert step.stdout == b""


def test_refusal_out_of_set_verdict_exit_one(tmp_path: Path) -> None:
    """R2 the out-of-set verdict: register first (rc 0 asserted), then bogus-winner → rc 1, stdout empty."""
    registered = _run(_register_argv(tmp_path))
    assert registered.returncode == 0
    argv = ["vote", _RUN_ONE, "a", "b", "bogus-winner", _COMPARATOR_ID, _HUMAN, _HOME_FLAG, str(tmp_path)]
    step = _run(argv)
    assert step.returncode == 1
    assert step.stderr.startswith(_REFUSED_PREFIX)
    assert b"bogus-winner" in step.stderr
    assert step.stdout == b""


def test_safe_halt_exit_one_no_partial_ranking(tmp_path: Path) -> None:
    """R3 the safe halt: one vote cast, tally → rc 1, "at quorum" verbatim on stderr, stdout empty."""
    assert _run(_register_argv(tmp_path)).returncode == 0
    assert _run(_vote_argv(tmp_path, "a", "b")).returncode == 0
    step = _run(["tally", _RUN_ONE, _HOME_FLAG, str(tmp_path)])
    assert step.returncode == 1
    assert step.stderr.startswith(_REFUSED_PREFIX)
    assert b"at quorum" in step.stderr
    assert step.stdout == b""


def test_argparse_channel_exit_two() -> None:
    """R4 argparse's channel: an unknown subcommand → rc 2, the OS receipt of SystemExit, usage bytes non-empty."""
    step = _run(["frobnicate"])
    assert step.returncode == 2
    assert step.stderr
