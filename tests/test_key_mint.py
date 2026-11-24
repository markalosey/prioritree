# Copyright (C) 2026 Mark Losey. All rights reserved.
r"""The key mint's CLI arcs — the eight arcs (keyinfrastructurespec §4, the test_cli.py school).

The UNIT form: command(argv_list) called IN-PROCESS, --home tmp_path homes
ONLY (the default KEYS_HOME never touched), NO subprocess. The arcs: (1) the
success stdout — the key\tdigest\tmode lines, exit 0, the digest the key's own
sha256; (2) THE PLAINTEXT'S ONCE — the key on stdout exactly once, ABSENT
from the file's bytes (hashed at rest); (3) the record on disk — the digest
present, the mode 0600; (4) the vocabulary refusals at 1 — the bad class /
the bad scope / the bad audience, the store's typed door (never argparse
choices=); (5) argparse's channel at 2 — the missing comparator_id; (6) the
--home placement — AFTER the subcommand, the two homes routed never
conflated; (7) the env override home — PRIORITYTREE_KEYS_HOME the service's
boot knob, never the CLI's: the --home flag the CLI's only override; (8) the
second mint appends — two lines, two digests.

Provenance: keyinfrastructurespec §4 (the mint arcs), key-infrastructure §3,
packet build/key-infrastructure, route prioritree-auth, 2026-11-24 session.
The S101/PLR2004 tests ruling stands.
"""

import hashlib
from pathlib import Path

import pytest

from prioritree.cli import command

# Payload constants (content-in-configuration): the grammar's tokens and the
# arcs' shared forms — never inline magic in the arcs.
_COMPARATOR_ID = "comparator-1"
_SCOPES_CSV = "cast,next"
_HOME_FLAG = "--home"
_KEYS_FILE = "keys.jsonl"
_KEYS_HOME_ENV = "PRIORITYTREE_KEYS_HOME"


def _minted_digest(out: str) -> str:
    """Return the minted digest from one mint's stdout — the digest line's payload, marker checked."""
    digest_line = out.splitlines()[1]
    assert digest_line.startswith("digest\t")
    return digest_line.removeprefix("digest\t")


def test_mint_success_stdout_bytes(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    r"""Mint returns 0 + the key\tdigest\tmode lines — the digest the key's own sha256."""
    home = tmp_path / _KEYS_FILE
    argv = ["key", "mint", _COMPARATOR_ID, "--scopes", _SCOPES_CSV, _HOME_FLAG, str(home)]
    assert command(argv) == 0
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 3
    assert lines[0].startswith("key\t")
    assert lines[1].startswith("digest\t")
    assert lines[2] == "mode\t0600"
    key = lines[0].removeprefix("key\t")
    digest = lines[1].removeprefix("digest\t")
    assert digest == hashlib.sha256(key.encode("utf-8")).hexdigest()


def test_mint_plaintext_once(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """THE PLAINTEXT'S ONCE — the key on stdout exactly once, ABSENT from the file's bytes."""
    home = tmp_path / _KEYS_FILE
    argv = ["key", "mint", _COMPARATOR_ID, "--scopes", _SCOPES_CSV, _HOME_FLAG, str(home)]
    assert command(argv) == 0
    out = capsys.readouterr().out
    key_line = out.splitlines()[0]
    assert key_line.startswith("key\t")
    key = key_line.removeprefix("key\t")
    assert out.count(key) == 1
    assert key not in home.read_text(encoding="utf-8")


def test_mint_record_on_disk(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """The record lands on disk — the digest present in the file's bytes, the mode 0600."""
    home = tmp_path / _KEYS_FILE
    argv = ["key", "mint", _COMPARATOR_ID, "--scopes", _SCOPES_CSV, _HOME_FLAG, str(home)]
    assert command(argv) == 0
    digest = _minted_digest(capsys.readouterr().out)
    assert digest in home.read_text(encoding="utf-8")
    assert (home.stat().st_mode & 0o777) == 0o600


@pytest.mark.parametrize(
    ("case", "needle"),
    [
        pytest.param("class", "bogus-class", id="bad-class"),
        pytest.param("scope", "bogus-scope", id="bad-scope"),
        pytest.param("audience", "bogus-audience", id="bad-audience"),
    ],
)
def test_mint_vocabulary_refusals_exit_one(
    tmp_path: Path, capsys: pytest.CaptureFixture[str], case: str, needle: str,
) -> None:
    """The bad class / scope / audience each refuse at exit 1 — the store's door, never argparse's choices=."""
    home = tmp_path / _KEYS_FILE
    if case == "class":
        tail: list[str] = ["--class", "bogus-class", "--scopes", _SCOPES_CSV]
    elif case == "scope":
        tail = ["--scopes", "bogus-scope"]
    else:
        tail = ["--scopes", _SCOPES_CSV, "--audience", "bogus-audience"]
    argv = ["key", "mint", _COMPARATOR_ID, *tail, _HOME_FLAG, str(home)]
    assert command(argv) == 1
    err = capsys.readouterr().err
    assert err.startswith("refused — expected:")
    assert needle in err
    assert not home.exists()


def test_mint_argparse_exit_two_missing_comparator_id(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """The missing comparator_id positional rides argparse's own channel — SystemExit 2 + the usage bytes."""
    with pytest.raises(SystemExit) as info:
        command(["key", "mint", "--scopes", _SCOPES_CSV, _HOME_FLAG, str(tmp_path / _KEYS_FILE)])
    assert info.value.code == 2
    assert capsys.readouterr().err


def test_mint_home_after_subcommand_placement(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """The --home AFTER the subcommand routes the mint — A's digest lands at A, B's at B, never conflated."""
    home_a = tmp_path / "a" / _KEYS_FILE
    home_b = tmp_path / "b" / _KEYS_FILE
    argv_a = ["key", "mint", _COMPARATOR_ID, "--scopes", _SCOPES_CSV, _HOME_FLAG, str(home_a)]
    assert command(argv_a) == 0
    digest_a = _minted_digest(capsys.readouterr().out)
    argv_b = ["key", "mint", _COMPARATOR_ID, "--scopes", _SCOPES_CSV, _HOME_FLAG, str(home_b)]
    assert command(argv_b) == 0
    digest_b = _minted_digest(capsys.readouterr().out)
    raw_a = home_a.read_text(encoding="utf-8")
    raw_b = home_b.read_text(encoding="utf-8")
    assert digest_a in raw_a
    assert digest_a not in raw_b
    assert digest_b in raw_b
    assert digest_b not in raw_a


def test_mint_env_override_home(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """PRIORITYTREE_KEYS_HOME never redirects the CLI's mint — the --home flag the CLI's only override."""
    env_home = tmp_path / "env" / _KEYS_FILE
    flag_home = tmp_path / "flag" / _KEYS_FILE
    monkeypatch.setenv(_KEYS_HOME_ENV, str(env_home))
    argv = ["key", "mint", _COMPARATOR_ID, "--scopes", _SCOPES_CSV, _HOME_FLAG, str(flag_home)]
    assert command(argv) == 0
    assert flag_home.is_file()
    assert not env_home.exists()


def test_mint_second_mint_appends(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    """The second mint at the same home appends — two lines, two digests, the mint order held."""
    home = tmp_path / _KEYS_FILE
    argv = ["key", "mint", _COMPARATOR_ID, "--scopes", _SCOPES_CSV, _HOME_FLAG, str(home)]
    assert command(argv) == 0
    digest_one = _minted_digest(capsys.readouterr().out)
    assert command(argv) == 0
    digest_two = _minted_digest(capsys.readouterr().out)
    lines = home.read_text(encoding="utf-8").splitlines()
    assert len(lines) == 2
    assert digest_one != digest_two
    assert digest_one in lines[0]
    assert digest_two in lines[1]
