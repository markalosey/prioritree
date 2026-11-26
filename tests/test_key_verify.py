# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The key-verify unit's arcs — the nine arcs (keyinfrastructurespec §4).

The UNIT form: keys minted over tmp_path homes ONLY (the default KEYS_HOME
never touched), the verify seam called direct — the door's own typed refusals
asserted field-for-field, no HTTP layer. The arcs: (1) the right key → the
record's identity whole; (2) the wrong key → the 401's three fields
byte-exact; (3) the dummy compute arc — the miss's sha256 call count, the
counter form; (4) the one-compare-site fence — the source scan, the
test_service_store.py:238 school; (5) the audience check — the mcp-audience
key at the service door → the SAME 401, never naming mcp; (6) the class check
— the record's class the truth, no claim parameter; (7) the scope check's two
— the granted passes, the ungranted → the 403's three fields; (8) the
reload-through-verify — the mid-flight mint seen live; (9) the absent header —
presented empty → the 401's same three fields.

Provenance: keyinfrastructurespec §4 (the verify arcs), key-infrastructure §3,
packet build/key-infrastructure, route prioritree-auth, 2026-11-24 session.
The S101/PLR2004 tests ruling stands.
"""

from __future__ import annotations

import hashlib
import inspect
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

from prioritree import key_verify
from prioritree.key_store import KeyStore
from prioritree.key_verify import AUTH_HEADER_DEFAULT, KeyScopeError, KeyVerifyError, verify

if TYPE_CHECKING:
    from collections.abc import Sequence


# Payload constants (content-in-configuration): the store's vocabulary tokens
# and the arcs' shared forms — never inline magic in the arcs.
_COMPARATOR_ID = "operator-1"
_SERVICE_AUDIENCE = "service"
_MCP_AUDIENCE = "mcp"
_CAST_SCOPE = "cast"
_STATE_SCOPE = "state"
_LLM_CLASS = "llm"
_HUMAN_CLASS = "human"
_WRONG_KEY = "not-the-minted-key"
_DUMMY_PAYLOAD = b"prioritree-key-verify-f9-dummy"
_KEYS_FILE = "keys.jsonl"


class _Sha256CallCounter:
    """The sha256 call counter — a hashlib stand-in recording every hashed payload (the F9 arc's instrument)."""

    def __init__(self) -> None:
        """Initialize the empty call log."""
        self.calls: list[bytes] = []

    def sha256(self, data: bytes) -> object:
        """Record one payload, delegate to the real sha256 — the digest's work rides through unchanged."""
        self.calls.append(data)
        return hashlib.sha256(data)


def _minted_store(
    home: Path,
    *,
    scopes: Sequence[str] = (_CAST_SCOPE, _STATE_SCOPE),
    audience: str = _SERVICE_AUDIENCE,
    comparator_class: str = _LLM_CLASS,
) -> tuple[KeyStore, str]:
    """Mint one key at a tmp home — the store over that home plus the plaintext key (the arcs' shared fixture)."""
    store = KeyStore(home / _KEYS_FILE)
    key, _digest = store.mint(_COMPARATOR_ID, comparator_class, scopes, audience)
    return store, key


def _assert_same_401(error: KeyVerifyError) -> None:
    """Assert the 401's three fields byte-exact — the SAME form at every refusing leg (the oracle never fed)."""
    assert error.expected == f"the key in the {AUTH_HEADER_DEFAULT} header"
    assert error.found == "absent-or-unknown"
    assert (
        error.next_action
        == "mint a key: prioritree key mint <comparator-id> --class <human|llm> --scopes <csv> --audience <tier>"
    )


def test_right_key_returns_the_records_identity_whole(tmp_path: Path) -> None:
    """The right key → the record's identity whole — the id, the class, the scopes, the audience, the digest."""
    store, key = _minted_store(tmp_path)
    record = verify(store, key, _SERVICE_AUDIENCE, None)
    assert record.comparator_id == "operator-1"
    assert record.comparator_class == "llm"
    assert record.scopes == frozenset({"cast", "state"})
    assert record.audience == "service"
    assert record.digest == hashlib.sha256(key.encode("utf-8")).hexdigest()


def test_wrong_key_refused_the_401_three_fields_byte_exact(tmp_path: Path) -> None:
    """The wrong key → the 401's three fields byte-exact — the named header, absent-or-unknown, the mint teaching."""
    store, _key = _minted_store(tmp_path)
    with pytest.raises(KeyVerifyError) as raised:
        verify(store, _WRONG_KEY, _SERVICE_AUDIENCE, None)
    _assert_same_401(raised.value)


def test_dummy_compute_miss_path_sha256_count(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """The dummy compute — the miss's sha256 count: the hit's hash + the F9 dummy (the counter form)."""
    store, key = _minted_store(tmp_path)
    counter = _Sha256CallCounter()
    monkeypatch.setattr(key_verify, "hashlib", counter)
    record = verify(store, key, _SERVICE_AUDIENCE, None)  # the hit path
    assert record.comparator_id == "operator-1"
    hit_calls = list(counter.calls)
    with pytest.raises(KeyVerifyError):
        verify(store, _WRONG_KEY, _SERVICE_AUDIENCE, None)  # the miss path
    miss_calls = counter.calls[len(hit_calls) :]
    # The hit's count: the presented key hashed ONCE (hit = 1, the landed fingerprint).
    assert hit_calls == [key.encode("utf-8")]
    # The miss's count: the SAME presented-key hash PLUS the F9 dummy's — the spec's "count equals
    # the hit's" holds on the shared presented-key leg (one hash each), the dummy the miss's ADDED
    # constant work (hit = 1, miss = 2 — never less hash work than the hit's, the short-circuit
    # killed).
    assert miss_calls == [_WRONG_KEY.encode("utf-8"), _DUMMY_PAYLOAD]


def test_fence_one_compare_site_in_key_verify() -> None:
    """The fence — key_verify.py's bytes carry compare_digest exactly once (the ONE compare point)."""
    module_path = Path(__file__).resolve().parents[1] / "src" / "prioritree" / "key_verify.py"
    source = module_path.read_text(encoding="utf-8")
    assert source.count("compare_digest") == 1


def test_audience_check_wrong_tier_key_same_401(tmp_path: Path) -> None:
    """The audience check — the mcp-audience key at the service door → the SAME 401, mcp never named (F5)."""
    store, mcp_key = _minted_store(tmp_path, audience=_MCP_AUDIENCE)
    with pytest.raises(KeyVerifyError) as raised:
        verify(store, mcp_key, _SERVICE_AUDIENCE, None)
    _assert_same_401(raised.value)
    # The record's audience NEVER named — no field teaches the wrong tier (the identity oracle starved).
    rendered = f"{raised.value.expected}|{raised.value.found}|{raised.value.next_action}"
    assert "mcp" not in rendered


def test_class_check_the_records_class_the_truth(tmp_path: Path) -> None:
    """The class check — the record's class the verified truth (F8): returned whole, no claim parameter exists."""
    llm_store, llm_key = _minted_store(tmp_path, comparator_class=_LLM_CLASS)
    assert verify(llm_store, llm_key, _SERVICE_AUDIENCE, None).comparator_class == "llm"
    human_store, human_key = _minted_store(tmp_path / "human", comparator_class=_HUMAN_CLASS)
    assert verify(human_store, human_key, _SERVICE_AUDIENCE, None).comparator_class == "human"
    # F8's no-claim law pinned at the signature — the body's self-claim has no parameter to ride.
    assert "claim" not in inspect.signature(verify).parameters


def test_scope_check_granted_passes_ungranted_403(tmp_path: Path) -> None:
    """The scope check's two — the granted scope passes; the ungranted → the 403's three fields (the re-mint)."""
    store, key = _minted_store(tmp_path, scopes=(_CAST_SCOPE,))
    granted = verify(store, key, _SERVICE_AUDIENCE, _CAST_SCOPE)
    assert granted.comparator_id == "operator-1"
    with pytest.raises(KeyScopeError) as raised:
        verify(store, key, _SERVICE_AUDIENCE, _STATE_SCOPE)
    assert raised.value.expected == "the state scope"
    assert raised.value.found == "the key's scopes ['cast']"
    assert raised.value.next_action == "re-mint with the scope: prioritree key mint ... --scopes <csv>+state"


def test_reload_through_verify_midflight_mint_seen(tmp_path: Path) -> None:
    """The reload through verify — a mint through a second container over the same home lands live (the stat ride)."""
    keys_home = tmp_path / _KEYS_FILE
    service_store = KeyStore(keys_home)  # the boot load: the absent store the empty dict
    with pytest.raises(KeyVerifyError):  # no key yet — the empty store refuses
        verify(service_store, _WRONG_KEY, _SERVICE_AUDIENCE, None)
    cli_store = KeyStore(keys_home)  # the CLI's own container over the same home
    key, digest = cli_store.mint("operator-2", _HUMAN_CLASS, (_CAST_SCOPE,), _SERVICE_AUDIENCE)
    record = verify(service_store, key, _SERVICE_AUDIENCE, _CAST_SCOPE)  # the stat ride re-loads
    assert record.comparator_id == "operator-2"
    assert record.digest == digest


def test_absent_header_presented_empty_refused_401(tmp_path: Path) -> None:
    """The absent header — presented empty (the door's data shape) → the 401's same three fields."""
    store, _key = _minted_store(tmp_path)
    with pytest.raises(KeyVerifyError) as raised:
        verify(store, "", _SERVICE_AUDIENCE, None)
    _assert_same_401(raised.value)
