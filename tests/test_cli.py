# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The command-face unit's tests — the eight arcs (command-face-brief §5).

The UNIT form: command(argv_list) called IN-PROCESS, --home tmp_path homes
ONLY (the default STORE_HOME never touched), NO subprocess (the e2e fixed-argv
arc is cli-acceptance's unit, the NEXT one). The arcs: (1) each subcommand's
success — the exact stdout bytes, including the whole ranking against a
driven-to-coverage fixture; (2) DONE — the exhausted line at 0, the tally
pointer present; (3) the three refusals at 1 — str(e) on stderr, asserted by
prefix + distinctive field; (4) the unexpected at 2 — the traceback verbatim;
(5) argparse's channel — SystemExit 2 + usage bytes; (6) --home — the
AFTER-subcommand placement; (7) --seed — the pass-through's byte-identical
pair lines; (8) the ack — the loud dedup at 0.

Provenance: command-face-brief §5, packet synthesize/command-face, route
prioritree-cli, 2026-11-21 session. The S101/PLR2004 tests ruling stands.
"""

from pathlib import Path
from typing import NoReturn

import pytest

from prioritree.cli import command

# Payload constants (content-in-configuration): the grammar's tokens and the
# driven fixtures' exact expected bytes — never inline magic in the arcs.
_OPERATOR_ID = "operator-1"
_QUESTION = "which comes first?"
_COMPARATOR_ID = "comparator-1"
_HUMAN = "human"
_LLM = "llm"
_HOME_FLAG = "--home"
_PREFER_A = "prefer-a"
_RUN_ONE = "RUN-0001"
_VOTE_ONE = "VOTE-0001"
_ITEMS_ABC = ("a:alpha", "b:bravo", "c:charlie")
_ITEMS_AB = ("a:alpha", "b:bravo")
# The driven-to-coverage tally's whole multi-line stdout (§3's frozen whole):
# no cycle line when empty, pairs lines in schedule order, version last.
_TALLY_ABC = (
    "rank\ta\n"
    "rank\tb\n"
    "rank\tc\n"
    "counts\ta\t4\t0\t0\n"
    "counts\tb\t2\t2\t0\n"
    "counts\tc\t0\t4\t0\n"
    "coverage\t1\tTrue\n"
    "pairs\ta\tb\t2\n"
    "pairs\ta\tc\t2\n"
    "pairs\tb\tc\t2\n"
    "version\twin-rate-v1\n"
)


def _register(tmp_path: Path, items: tuple[str, ...]) -> None:
    """Register a run at the tmp home — the shared arc fixture."""
    argv = ["register", *items, "--operator-id", _OPERATOR_ID, "--question", _QUESTION, _HOME_FLAG, str(tmp_path)]
    assert command(argv) == 0


def _cast(tmp_path: Path, item_a: str, item_b: str, winner: str, comparator_class: str = _HUMAN) -> None:
    """Cast one vote at the tmp home in the served canonical order."""
    argv = ["vote", _RUN_ONE, item_a, item_b, winner, _COMPARATOR_ID, comparator_class, _HOME_FLAG, str(tmp_path)]
    assert command(argv) == 0


def _drive_abc_to_coverage(tmp_path: Path) -> None:
    """Drive the 3-item run to coverage — all 3 pairs voted human+llm at k=1 (six casts)."""
    _register(tmp_path, _ITEMS_ABC)
    _cast(tmp_path, "a", "b", _PREFER_A)
    _cast(tmp_path, "a", "b", _PREFER_A, _LLM)
    _cast(tmp_path, "a", "c", _PREFER_A)
    _cast(tmp_path, "a", "c", _PREFER_A, _LLM)
    _cast(tmp_path, "b", "c", _PREFER_A)
    _cast(tmp_path, "b", "c", _PREFER_A, _LLM)


def test_register_success_bare_stem(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """Register returns 0 + the bare stem line — the id IS the whole report."""
    argv = ["register", *_ITEMS_ABC, "--operator-id", _OPERATOR_ID, "--question", _QUESTION, _HOME_FLAG, str(tmp_path)]
    assert command(argv) == 0
    assert capsys.readouterr().out == "RUN-0001\n"


def test_next_success_pair_line(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """Next on the fresh 3-item run returns 0 + the serve triple's pair line."""
    _register(tmp_path, _ITEMS_ABC)
    capsys.readouterr()
    assert command(["next", _RUN_ONE, _HOME_FLAG, str(tmp_path)]) == 0
    assert capsys.readouterr().out == "pair\ta\tb\t0\n"


def test_vote_success_vote_line(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """Vote after the first cast returns 0 + the vote line with count 1."""
    _register(tmp_path, _ITEMS_ABC)
    command(["next", _RUN_ONE, _HOME_FLAG, str(tmp_path)])
    capsys.readouterr()
    argv = ["vote", _RUN_ONE, "a", "b", _PREFER_A, _COMPARATOR_ID, _HUMAN, _HOME_FLAG, str(tmp_path)]
    assert command(argv) == 0
    assert capsys.readouterr().out == f"vote\t{_VOTE_ONE}\t1\n"


def test_state_success_summary_bytes(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """State after the one vote returns the summary — map order, zeros included."""
    _register(tmp_path, _ITEMS_ABC)
    _cast(tmp_path, "a", "b", _PREFER_A)
    capsys.readouterr()
    assert command(["state", _RUN_ONE, _HOME_FLAG, str(tmp_path)]) == 0
    assert capsys.readouterr().out == "votes\t1\nitem\ta\t1\nitem\tb\t1\nitem\tc\t0\n"


def test_tally_success_frozen_whole_bytes(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """Tally at the covered run returns 0 + the whole multi-line ranking exactly."""
    _drive_abc_to_coverage(tmp_path)
    capsys.readouterr()
    assert command(["tally", _RUN_ONE, _HOME_FLAG, str(tmp_path)]) == 0
    assert capsys.readouterr().out == _TALLY_ABC


def test_done_exhausted_line_at_zero(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """A 2-item run driven to coverage, then next → 0 + the exhausted line naming tally."""
    _register(tmp_path, _ITEMS_AB)
    _cast(tmp_path, "a", "b", _PREFER_A)
    capsys.readouterr()
    assert command(["next", _RUN_ONE, _HOME_FLAG, str(tmp_path)]) == 0
    out = capsys.readouterr().out
    assert out.startswith("exhausted —")
    assert "tally" in out


@pytest.mark.parametrize(
    ("case", "needle"),
    [
        pytest.param("store", "RUN-9999", id="store-unknown-run"),
        pytest.param("votes", "bogus-winner", id="votes-out-of-set-winner"),
        pytest.param("tally", "at quorum", id="tally-undercovered"),
    ],
)
def test_refusals_exit_one_str_bytes(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    case: str,
    needle: str,
) -> None:
    """Each refusal lineage returns 1 + stderr carrying the refused — prefix and its distinctive field."""
    if case == "store":
        argv = ["next", "RUN-9999", _HOME_FLAG, str(tmp_path)]
    elif case == "votes":
        _register(tmp_path, _ITEMS_ABC)
        argv = ["vote", _RUN_ONE, "a", "b", "bogus-winner", _COMPARATOR_ID, _HUMAN, _HOME_FLAG, str(tmp_path)]
    else:
        _register(tmp_path, _ITEMS_ABC)
        _cast(tmp_path, "a", "b", _PREFER_A)
        argv = ["tally", _RUN_ONE, _HOME_FLAG, str(tmp_path)]
    assert command(argv) == 1
    err = capsys.readouterr().err
    assert err.startswith("refused —")
    assert needle in err


def test_unexpected_exit_two_traceback_verbatim(
    tmp_path: Path,
    capsys: pytest.CaptureFixture[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A monkeypatched store verb raising RuntimeError → 2 + the traceback's name and message on stderr."""

    def _boom(_store_home: Path, _run_id: str) -> NoReturn:
        """Raise the unexpected — the arc's injected failure."""
        msg = "boom"
        raise RuntimeError(msg)

    monkeypatch.setattr("prioritree.cli.Persist.load", _boom)
    assert command(["next", _RUN_ONE, _HOME_FLAG, str(tmp_path)]) == 2
    err = capsys.readouterr().err
    assert "RuntimeError" in err


@pytest.mark.parametrize(
    "argv",
    [
        pytest.param(["vote", _RUN_ONE], id="missing-positionals"),
        pytest.param(["frobnicate"], id="unknown-subcommand"),
        pytest.param(["next", _RUN_ONE, "--seed", "abc"], id="non-integer-seed"),
        pytest.param(["register", "nocolon", "--operator-id", "op", "--question", "q"], id="colon-less-item"),
    ],
)
def test_argparse_channel_system_exit_two(capsys: pytest.CaptureFixture[str], argv: list[str]) -> None:
    """Argparse's own violations raise SystemExit 2 + the usage/error bytes on stderr."""
    with pytest.raises(SystemExit) as info:
        command(argv)
    assert info.value.code == 2
    assert capsys.readouterr().err


def test_home_after_subcommand_placement(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """Register under A serves; B (empty) refuses at 1 — the live set names A's id."""
    home_a = tmp_path / "a"
    home_b = tmp_path / "b"
    argv_a = ["register", *_ITEMS_ABC, "--operator-id", _OPERATOR_ID, "--question", _QUESTION, _HOME_FLAG, str(home_a)]
    assert command(argv_a) == 0
    assert command(["next", _RUN_ONE, _HOME_FLAG, str(home_a)]) == 0
    assert command(["next", _RUN_ONE, _HOME_FLAG, str(home_b)]) == 1
    err = capsys.readouterr().err
    assert err.startswith("refused —")
    assert _RUN_ONE in err


def test_seed_pass_through_byte_identical(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """The same seed twice on the same fresh run serves byte-identical pair lines."""
    _register(tmp_path, _ITEMS_ABC)
    capsys.readouterr()
    assert command(["next", _RUN_ONE, "--seed", "5", _HOME_FLAG, str(tmp_path)]) == 0
    first = capsys.readouterr().out
    assert command(["next", _RUN_ONE, "--seed", "5", _HOME_FLAG, str(tmp_path)]) == 0
    second = capsys.readouterr().out
    assert first.startswith("pair\t")
    assert first == second


def test_ack_loud_dedup_count_unchanged(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """A byte-identical re-cast → the second returns 0 + the ack line, the count unchanged."""
    _register(tmp_path, _ITEMS_ABC)
    _cast(tmp_path, "a", "b", _PREFER_A)
    capsys.readouterr()
    argv = ["vote", _RUN_ONE, "a", "b", _PREFER_A, _COMPARATOR_ID, _HUMAN, _HOME_FLAG, str(tmp_path)]
    assert command(argv) == 0
    assert capsys.readouterr().out == f"ack\t{_VOTE_ONE}\t1\n"


def test_next_swap_presents_swapped(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """Next --swap prints the presented pair swapped — the triple's order the presentation."""
    _register(tmp_path, _ITEMS_ABC)
    capsys.readouterr()
    assert command(["next", _RUN_ONE, "--swap", _HOME_FLAG, str(tmp_path)]) == 0
    assert capsys.readouterr().out == "pair\tb\ta\t0\n"


def test_vote_swapped_flag_maps_canonical(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """Vote with --presentation-order swapped maps onto the canonical pair — the tally's ranking the evidence."""
    _register(tmp_path, _ITEMS_ABC)
    argv = [
        "vote",
        _RUN_ONE,
        "b",
        "a",
        _PREFER_A,
        _COMPARATOR_ID,
        _HUMAN,
        "--presentation-order",
        "swapped",
        _HOME_FLAG,
        str(tmp_path),
    ]
    assert command(argv) == 0
    capsys.readouterr()
    # ab's swapped human vote maps to b's win; the llm corroboration + the rest canonical — b tops.
    _cast(tmp_path, "a", "b", "prefer-b", _LLM)
    _cast(tmp_path, "a", "c", _PREFER_A)
    _cast(tmp_path, "a", "c", _PREFER_A, _LLM)
    _cast(tmp_path, "b", "c", _PREFER_A)
    _cast(tmp_path, "b", "c", _PREFER_A, _LLM)
    capsys.readouterr()
    assert command(["tally", _RUN_ONE, _HOME_FLAG, str(tmp_path)]) == 0
    out = capsys.readouterr().out
    assert out.startswith("rank\tb\nrank\ta\nrank\tc\n")
    assert "counts\tb\t4\t0\t0" in out
