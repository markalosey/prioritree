# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The key-store unit's tests — the thirteen arcs (keyinfrastructurespec §4).

The arcs: the mint's record bytes (six fields, sort_keys); the 0600 mode; the
second mint's append; the mint's and the load's world-writable refusals (F3);
the corrupt-line parametrizes — the seven forms each refusing with the form
named; the absent-store-empty-dict-never-a-refusal (the empty home = the
marker, not an error); the mtime re-read (the mid-flight mint live); the
mid-flight chmod refused at re-load; the marker's three renders; the AUTH
knob's three (default on, off, typo refused — parametrized); the mint's
vocabulary refusals (typed data at the store, never argparse); the scopes
sorted-deduped on the wire.

Provenance: the exact-task spec reports/synthesize/keyinfrastructurespec
§1 + §4, packet build/key-infrastructure, route prioritree-auth, 2026-11-24;
the test_run_store.py + test_cli.py fixture schools. The standing
S101/PLR2004 tests ruling covers this file; no new ignore.
"""

from __future__ import annotations

import hashlib
import json
import re
import stat
from typing import TYPE_CHECKING

import pytest

from prioritree.key_store import (
    AUDIENCES,
    SCOPE_TOKENS,
    KeyStore,
    KeyStoreRefusedError,
    render_boot_marker,
    resolve_auth_mode,
)
from prioritree.votes import COMPARATOR_CLASSES

if TYPE_CHECKING:
    from pathlib import Path

# The arcs' shared vocabulary (content-in-configuration, the store's own).
_COMPARATOR_ID = "operator-1"
_HUMAN = "human"
_SCOPES = ("cast", "tally")
_AUDIENCE = "service"
_KEY_MODE = 0o600
_WORLD_WRITABLE = 0o666
_DIGEST_LENGTH = 64
_HEX_FORM = "64-char lowercase hex string"

# The corrupt forms' named fragments (§4's seven ids) — the refusal's
# expected bytes per case, rendered from the store's cited vocabulary.
_CORRUPT_NEEDLES: dict[str, str] = {
    "digest_non_hex": _HEX_FORM,
    "digest_wrong_length": _HEX_FORM,
    "class_outside": f"a comparator_class from {sorted(COMPARATOR_CLASSES)}",
    "scope_outside": f"the 'scopes' field a JSON array of tokens from {sorted(SCOPE_TOKENS)}",
    "audience_outside": f"an audience from {sorted(AUDIENCES)}",
    "missing_field": "a 'created_at' field on line 1",
    "crash_tail": "complete with its newline",
}


def _mint(store: KeyStore, comparator_id: str = _COMPARATOR_ID) -> tuple[str, str]:
    """Mint one well-formed key at the container — the shared arc fixture."""
    return store.mint(comparator_id, _HUMAN, _SCOPES, _AUDIENCE)


def _well_formed(digest: str | None = None) -> dict[str, object]:
    """Build one well-formed key line — the corrupt arcs' ground."""
    return {
        "digest": digest or "a" * _DIGEST_LENGTH,
        "comparator_id": _COMPARATOR_ID,
        "comparator_class": _HUMAN,
        "scopes": ["cast"],
        "audience": _AUDIENCE,
        "created_at": "2026-11-24T00:00:00+00:00",
    }


def _write_keys_file(home: Path, lines: list[dict[str, object]]) -> None:
    """Write the dict lines as the store's wire bytes — sort_keys, newline each."""
    home.parent.mkdir(parents=True, exist_ok=True)
    home.write_text("".join(json.dumps(line, sort_keys=True) + "\n" for line in lines))


def _assert_three_fields(error: KeyStoreRefusedError, needle: str) -> None:
    """Assert the typed three fields render the refusal's distinctive content."""
    message = str(error)
    assert "expected:" in message
    assert "found:" in message
    assert "next:" in message
    assert needle in message


def _corrupt(case: str, lines: list[dict[str, object]]) -> list[dict[str, object]]:
    """Mutate the well-formed lines per the case — the corrupt line's form."""
    line = lines[0]
    if case == "digest_non_hex":
        line["digest"] = "g" * _DIGEST_LENGTH
    elif case == "digest_wrong_length":
        line["digest"] = "a" * (_DIGEST_LENGTH - 1)
    elif case == "class_outside":
        line["comparator_class"] = "robot"
    elif case == "scope_outside":
        line["scopes"] = ["warp"]
    elif case == "audience_outside":
        line["audience"] = "public"
    elif case == "missing_field":
        del line["created_at"]
    return lines


def test_mint_record_bytes_six_fields_sort_keys(tmp_path: Path) -> None:
    """The mint's line: the six fields present, json sort_keys bytes, the digest hashed-at-rest."""
    home = tmp_path / "keys.jsonl"
    store = KeyStore(home)
    key, digest = _mint(store)
    assert hashlib.sha256(key.encode()).hexdigest() == digest
    assert re.fullmatch(r"[0-9a-f]{64}", digest) is not None
    raw = home.read_text()
    assert raw.endswith("\n")
    line = json.loads(raw)
    assert set(line) == {"digest", "comparator_id", "comparator_class", "scopes", "audience", "created_at"}
    assert line["digest"] == digest
    assert line["comparator_id"] == _COMPARATOR_ID
    assert line["comparator_class"] == _HUMAN
    assert line["scopes"] == sorted(set(_SCOPES))
    assert line["audience"] == _AUDIENCE
    assert isinstance(line["created_at"], str)
    assert raw == json.dumps(line, sort_keys=True) + "\n"
    assert key not in raw


def test_mint_mode_is_0600(tmp_path: Path) -> None:
    """The mint lands the file at mode 0600 — umask-proof, stat-checked."""
    home = tmp_path / "keys.jsonl"
    store = KeyStore(home)
    _mint(store)
    assert stat.S_IMODE(home.stat().st_mode) == _KEY_MODE


def test_second_mint_appends_two_lines(tmp_path: Path) -> None:
    """The second mint appends — two lines, two digests, the mode held."""
    home = tmp_path / "keys.jsonl"
    store = KeyStore(home)
    first_key, first_digest = _mint(store, "operator-one")
    second_key, second_digest = _mint(store, "operator-two")
    assert first_digest != second_digest
    assert first_key != second_key
    lines = home.read_text().splitlines()
    assert len(lines) == 2
    assert {json.loads(line)["digest"] for line in lines} == {first_digest, second_digest}
    assert stat.S_IMODE(home.stat().st_mode) == _KEY_MODE


def test_mint_world_writable_refused_no_widen(tmp_path: Path) -> None:
    """A chmod'd 0o666 store refuses at the mint — the ThreePart loud, the file never widened."""
    home = tmp_path / "keys.jsonl"
    store = KeyStore(home)
    _mint(store)
    home.chmod(_WORLD_WRITABLE)
    with pytest.raises(KeyStoreRefusedError) as info:
        _mint(store, "operator-two")
    _assert_three_fields(info.value, "world-writable")
    assert len(home.read_text().splitlines()) == 1


def test_load_stat_refusal_three_fields(tmp_path: Path) -> None:
    """A chmod'd 0o666 store refuses at the load — the three fields, the chmod named."""
    home = tmp_path / "keys.jsonl"
    _write_keys_file(home, [_well_formed()])
    home.chmod(_WORLD_WRITABLE)
    with pytest.raises(KeyStoreRefusedError) as info:
        KeyStore(home)
    _assert_three_fields(info.value, "chmod 600")


@pytest.mark.parametrize(
    "case",
    [
        pytest.param("digest_non_hex", id="non-hex-digest"),
        pytest.param("digest_wrong_length", id="wrong-length-digest"),
        pytest.param("class_outside", id="class-outside"),
        pytest.param("scope_outside", id="scope-outside"),
        pytest.param("audience_outside", id="audience-outside"),
        pytest.param("missing_field", id="missing-field"),
        pytest.param("crash_tail", id="crash-tail"),
    ],
)
def test_corrupt_line_refused_form_named(tmp_path: Path, case: str) -> None:
    """Each corrupt form refuses the load WHOLE — the form named, the line number carried."""
    home = tmp_path / "keys.jsonl"
    lines = _corrupt(case, [_well_formed()])
    if case == "crash_tail":
        home.parent.mkdir(parents=True, exist_ok=True)
        home.write_text(json.dumps(lines[0], sort_keys=True))
    else:
        _write_keys_file(home, lines)
    with pytest.raises(KeyStoreRefusedError) as info:
        KeyStore(home)
    _assert_three_fields(info.value, _CORRUPT_NEEDLES[case])
    assert "line 1" in info.value.found


def test_absent_store_empty_dict_never_a_refusal(tmp_path: Path) -> None:
    """The absent home loads the empty dict — the absence is the marker's, never the load's error."""
    home = tmp_path / "absent" / "keys.jsonl"
    store = KeyStore(home)
    assert store.records == {}
    assert store.mtime() is None


def test_mtime_reload_mid_flight_mint_live(tmp_path: Path) -> None:
    """The mtime re-read: a mid-flight mint by another container lands live at the next read."""
    home = tmp_path / "keys.jsonl"
    store = KeyStore(home)
    _mint(store)
    _, digest = _mint(KeyStore(home), "operator-two")
    assert store.reload_if_changed() is True
    record = store.records[digest]
    assert record.comparator_id == "operator-two"
    assert record.scopes == frozenset(_SCOPES)
    assert store.reload_if_changed() is False


def test_mid_flight_chmod_refused_at_reload(tmp_path: Path) -> None:
    """A mid-flight chmod 0o666 refuses at the re-load — the last-good state stands."""
    home = tmp_path / "keys.jsonl"
    store = KeyStore(home)
    _mint(store)
    home.chmod(_WORLD_WRITABLE)
    with pytest.raises(KeyStoreRefusedError) as info:
        store.reload_if_changed()
    _assert_three_fields(info.value, "chmod 600")
    assert store.records == {}


def test_boot_marker_renders_three_states(tmp_path: Path) -> None:
    """The marker's three states: on+present, on+absent (load fail-open, doors fail-closed), off (the degrade)."""
    home = tmp_path / "keys.jsonl"
    _write_keys_file(home, [_well_formed()])
    absolute = home.absolute()
    assert render_boot_marker(absolute, "on", 1) == f"auth: on | keys: {absolute} | count: 1"
    absent_home = tmp_path / "absent.jsonl"
    assert render_boot_marker(absent_home, "on", 0) == (
        f"auth: on (load fail-open; doors fail-closed) | keys: {absent_home} | next-action: prioritree key mint"
    )
    assert render_boot_marker(absolute, "off", 0) == (
        f"auth: off (operator's explicit degrade) | keys: {absolute} | count: 0"
    )


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        pytest.param(None, "on", id="default-on"),
        pytest.param("off", "off", id="explicit-off"),
        pytest.param("onX", None, id="typo-refused"),
    ],
)
def test_resolve_auth_mode_the_three(raw: str | None, expected: str | None) -> None:
    """The knob's three: unset -> on, off -> off, the typo refused loudly — never a silent on-or-off."""
    if expected is None:
        with pytest.raises(KeyStoreRefusedError) as info:
            resolve_auth_mode(raw)
        _assert_three_fields(info.value, "onX")
    else:
        assert resolve_auth_mode(raw) == expected


@pytest.mark.parametrize(
    ("case", "needle"),
    [
        pytest.param("class", f"a comparator_class from {sorted(COMPARATOR_CLASSES)}", id="class-outside"),
        pytest.param(
            "scope",
            f"a non-empty --scopes list of tokens from {sorted(SCOPE_TOKENS)}",
            id="scope-outside",
        ),
        pytest.param("audience", f"an --audience from {sorted(AUDIENCES)}", id="audience-outside"),
    ],
)
def test_mint_vocabulary_refusals_typed(tmp_path: Path, case: str, needle: str) -> None:
    """The mint's argument gates refuse with typed three-field data — the store validates, never argparse."""
    home = tmp_path / "keys.jsonl"
    store = KeyStore(home)
    if case == "class":
        with pytest.raises(KeyStoreRefusedError) as info:
            store.mint(_COMPARATOR_ID, "robot", _SCOPES, _AUDIENCE)
    elif case == "scope":
        with pytest.raises(KeyStoreRefusedError) as info:
            store.mint(_COMPARATOR_ID, _HUMAN, ["warp"], _AUDIENCE)
    else:
        with pytest.raises(KeyStoreRefusedError) as info:
            store.mint(_COMPARATOR_ID, _HUMAN, _SCOPES, "public")
    _assert_three_fields(info.value, needle)
    assert "re-run the mint" in info.value.next_action
    assert not home.exists()


def test_scopes_sorted_deduped_on_the_wire(tmp_path: Path) -> None:
    """The mint's scopes land sorted and deduped — deterministic bytes on the wire."""
    home = tmp_path / "keys.jsonl"
    store = KeyStore(home)
    loud = [*SCOPE_TOKENS, "cast", "next"]
    _, digest = store.mint(_COMPARATOR_ID, _HUMAN, loud, _AUDIENCE)
    line = json.loads(home.read_text())
    assert line["scopes"] == sorted(set(loud))
    reloaded = KeyStore(home)
    assert reloaded.records[digest].scopes == frozenset(SCOPE_TOKENS)
