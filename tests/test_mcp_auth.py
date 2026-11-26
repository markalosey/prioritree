# Copyright (C) 2026 Mark Losey. All rights reserved.
"""test_mcp_auth -- the mcp door's falsification set, in-process (mcpverifiedtokenspec §3a).

The mcp-verified-token unit's auth test surface -- the door whole in ONE
falsification set, the mint-at-tmp fixture isolating BOTH stores (the run
store the face's rebind school, the key store the door's rebind seam) and
the granted make_token harness riding the armed gate: (1) THE ADAPTER-RIDDEN
ARCS -- the true chain exercised (the digest lookup, the ONE compare, F5):
the right key mapped to the AccessToken whole, the wrong/absent/service-
audience keys the SAME None (the oracle never fed), the mid-flight mint
live through the stat ride, the mcp key at the SERVICE door the landed
family's same 401 bytes (the cross-tier replay dead BOTH directions); (2)
THE POLICY ARCS -- the make_token form (the chain exercised, the adapter
bypassed, the brief §2d's ruled split): the granted five pass each tool,
the eight per-role denials (DEFAULT-DENY live at the map's own leg), the
hide from tools/list per caller, the guessed-name refusal OPAQUE (the
teaching loss PINNED as tested behavior), the off degrade's no-hide; (3)
THE CONSTRUCTION'S ARCS -- the armed compose (auth + policy, NEVER
stdio_policy: the trust default preserved), the plain form at the re-bound
off (the degrade never a lockout); (4) THE BOOT'S ARCS -- the marker's
three exact states (the store module's renderer reused whole, never
re-authored), the typo'd AUTH refusing loudly at the door's resolve; (5)
THE STDIO-TRUST ARCS -- the transport's own skip asserted in-process (the
anonymous call reaches the core's own refusal, the door never consulted)
and the harness's bare spawn source-scanned (the spawn IS the credential);
(6) THE STAMPING ARCS -- the verified class and the verified id over the
body's claims at the authenticated door, the degrade's fallback to the
body's stamps, the supersedes author-refusal as the PermissionDenied value
(found eliding the author), the own-author pass under the verified id;
(7) THE FORK-GUARD -- the map's keys the five registered tool names, the
tokens within the SCOPE_TOKENS vocabulary (cited as literals, never by
import coupling). The S101/PLR2004 tests ruling stands.

Provenance: mcpverifiedtokenspec §3a (the arcs' fence), the unit brief
§1-§3 (mcp-verified-token), packet build/mcp-verified-token step 3 of 5,
route prioritree-auth, 2026-11-24 session.
"""

from __future__ import annotations

import asyncio
import json
from itertools import count
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from fastmcp.server.context import reset_transport, set_transport
from mcp_types import TextContent
from ouncemcp import Effect
from ouncemcp.security.identity import identity_from_token
from ouncemcp.security.policy import PolicyRequest
from ouncemcp.testing import as_caller, make_token

from prioritree import mcp_auth, mcp_server
from prioritree.key_store import KeyStore, KeyStoreRefusedError, render_boot_marker, resolve_auth_mode
from prioritree.key_verify import AUTH_HEADER_DEFAULT, KeyVerifyError, verify
from prioritree.service_store import Serialize
from prioritree.store_lock import Lock

if TYPE_CHECKING:
    from collections.abc import Iterator, Sequence

    from fastmcp.server.auth import AccessToken
    from fastmcp.tools import ToolResult

# The door's own vocabulary (the literals ARE the specification under test,
# the test_service_auth school): the keys file's name, the five scope tokens
# (the granted whole -- the map's own rows), the three roles' scope rows
# (policy.py ROLE_SCOPES cited as literals -- the fork-guard's school), the
# five registered tool names, and the sitting's own nouns (the two-item
# register, the operator body, the fresh store's first run, the verdict echo).
_KEYS_FILE = "keys.jsonl"
_FIVE = ("register", "next", "cast", "state", "tally")
_COMPARATOR = ("next", "cast", "manifest")
_OPERATOR = ("register", "state", "tally", "manifest")
_AUDITOR = ("state", "tally", "manifest")
_TOOLS = ("runs.register", "runs.next", "votes.cast", "votes.census", "runs.tally")
_ITEMS = ["a", "b"]
_REGISTER_OPERATOR = {"operator_id": "op-1", "question": "Which matters more?"}
_RUN_ID = "RUN-0001"
_VERDICTS = ["prefer-a", "prefer-b", "tie"]
_CALLERS: Iterator[int] = count(1)


@pytest.fixture
def door(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> KeyStore:
    """Isolate the door by injection -- both stores fresh, the members re-bound.

    Purpose: the run store re-bound over tmp (the test_mcp_server_face.py:124-147
    school -- the tools' bodies read the module globals at call time); the door's
    _keys container over the tmp keys file (the adapter reads it at call time);
    AUTH_MODE pinned "on" (the armed door -- the boot's own default under pytest,
    AUTH unset; the off arcs rebind per test, the member the seam).
    Refuses when: never -- a fixture (the isolate-then-yield form).
    Re-run: deterministic -- a fresh tmp home per test.
    Touches: the tmp home only (pytest's own tmp_path).
    Provenance: mcpverifiedtokenspec §3a (the fixture fence), the
    test_service_auth.py:87-106 + test_mcp_server_face.py:124-147 precedents,
    G-MCPVERIFIEDTOKENSPEC-BRIEF.
    """
    monkeypatch.setattr(mcp_server, "STORE_HOME", tmp_path)
    monkeypatch.setattr(mcp_server, "_seam", Serialize(tmp_path))
    monkeypatch.setattr(mcp_server, "_lock", Lock(tmp_path))
    store = KeyStore(tmp_path / _KEYS_FILE)
    monkeypatch.setattr(mcp_auth, "_keys", store)
    monkeypatch.setattr(mcp_auth, "AUTH_MODE", "on")
    return store


def _grant(
    scopes: Sequence[str],
    *,
    audience: str = "mcp",
    comparator_class: str = "human",
    home: KeyStore,
) -> str:
    """Mint one key at the injected home -- the arcs' shared grant (the fence's own helper).

    Purpose: mint through the injected container (comparator_id "key-holder"
    the fence's fixed id -- the adapter-mapping arcs' noun), returning the
    plaintext key for the bearer input; the audience and class knobs the
    wrong-audience and class arcs' own.
    Refuses when: the mint's own typed refusal rides (KeyStoreRefusedError --
    an invalid scope/audience a test bug, never caught here).
    Re-run: a fresh random key per call -- the mint's own law (a re-grant a
    NEW key, never a replay).
    Touches: the injected home's key file (one minted line).
    Provenance: mcpverifiedtokenspec §3a (the _grant fence), the
    test_service_auth.py:109-131 _grant school, G-MCPVERIFIEDTOKENSPEC-BRIEF.
    """
    key, _digest = home.mint("key-holder", comparator_class, scopes, audience)
    return key


def _verify(key: str) -> AccessToken | None:
    """Verify the presented bearer through the door's adapter -- a fresh stateless instance.

    Purpose: the arcs' shared verify -- a fresh McpTokenVerifier per call
    (the store read at call time from the module member, the fixture's
    rebind seam honored); the coroutine ridden through asyncio.run.
    Refuses when: never itself -- the adapter's None IS the refusal under
    test (the crash lane rides through uncaught by design).
    Re-run: deterministic given the store state (the stat ride aside).
    Touches: the door's _keys container at most.
    Provenance: mcpverifiedtokenspec §3a (the _verify fence), G-MCPVERIFIEDTOKENSPEC-BRIEF.
    """
    return asyncio.run(mcp_auth.McpTokenVerifier().verify_token(key))


def _token(
    scopes: Sequence[str] = (),
    *,
    subject: str = "caller",
    comparator_id: str = "key-holder",
    comparator_class: str = "human",
) -> AccessToken:
    """Mint the door-shaped caller token -- the make_token form (the policy arcs' own).

    Purpose: the granted/narrow/empty tokens shaped as the door's adapter
    mints them -- the claims the cast door's stamp source; the policy chain
    exercised over the scopes, the adapter bypassed (the brief §2d's ruled
    split).
    Refuses when: never -- a pure mint over the testing surface.
    Re-run: deterministic -- the same arguments mint the same token.
    Touches: nothing -- the substrate's in-memory token.
    Provenance: mcpverifiedtokenspec §3a (the _token fence), the
    ouncemcp.testing make_token surface, G-MCPVERIFIEDTOKENSPEC-BRIEF.
    """
    return make_token(
        subject=subject,
        scopes=list(scopes),
        claims={"aud": "mcp", "comparator_id": comparator_id, "comparator_class": comparator_class},
    )


def _join(result: ToolResult) -> str:
    """Join the result's text channel -- the error labels' assertable ground."""
    return "".join(part.text for part in result.content if isinstance(part, TextContent))


def test_right_key_maps_the_access_token_whole(door: KeyStore) -> None:
    """The right key at the mcp door => the AccessToken WHOLE -- the adapter's mapping field-for-field."""
    key = _grant(_FIVE, home=door)
    access = _verify(key)
    assert access is not None
    assert access.token == key
    assert access.client_id == "prioritree-mcp"
    assert access.scopes == sorted(_FIVE)
    assert access.subject == "key-holder"
    assert access.claims == {"aud": "mcp", "comparator_id": "key-holder", "comparator_class": "human"}


def test_wrong_key_refuses_none(door: KeyStore) -> None:
    """A bogus key at the mcp door => None -- the F9 dummy's lane, the SAME refusal (no leg distinguishable)."""
    _grant(_FIVE, home=door)  # the store carries a real key -- the bogus one still the SAME None
    assert _verify("not-the-key") is None


@pytest.mark.usefixtures("door")
def test_absent_token_refuses_none() -> None:
    """The empty presented bearer => None -- the digest miss's lane."""
    assert _verify("") is None


def test_service_audience_key_at_the_mcp_door_refuses_none(door: KeyStore) -> None:
    """A service-audience key at the mcp door => None -- the replay's forward leg (F5 fires, the oracle never fed)."""
    key = _grant(_FIVE, audience="service", home=door)
    assert _verify(key) is None


def test_midflight_mint_lands_live_through_the_adapter(door: KeyStore) -> None:
    """A mint through a SECOND container over the same home => the adapter sees it LIVE (the stat ride)."""
    second = KeyStore(door.home)  # the CLI's own container over the same home
    key = _grant(_FIVE, home=second)
    access = _verify(key)
    assert access is not None
    assert access.subject == "key-holder"  # the door's boot-time load predates the mint -- the stat ride re-loaded


def test_mcp_key_at_the_service_door_the_same_401_reverse_leg(door: KeyStore) -> None:
    """An mcp-audience key at the SERVICE door => the SAME landed 401 bytes -- the reverse leg, mcp never named."""
    key = _grant(_FIVE, audience="mcp", home=door)
    with pytest.raises(KeyVerifyError) as raised:
        verify(door, key, "service", None)
    refusal = raised.value
    assert refusal.expected == f"the key in the {AUTH_HEADER_DEFAULT} header"
    assert refusal.found == "absent-or-unknown"
    assert refusal.next_action.startswith("mint a key: prioritree key mint")
    assert "mcp" not in refusal.expected + refusal.found + refusal.next_action


@pytest.mark.usefixtures("door")
def test_armed_compose_carries_auth_and_policy() -> None:
    """The armed compose => exactly auth + policy -- the adapter instance and the gate callable."""
    kwargs = mcp_auth.compose_door_kwargs()
    assert set(kwargs) == {"auth", "policy"}
    assert isinstance(kwargs["auth"], mcp_auth.McpTokenVerifier)
    assert kwargs["policy"] is mcp_auth.gate


@pytest.mark.usefixtures("door")
def test_off_compose_the_plain_form_neither_kwarg(monkeypatch: pytest.MonkeyPatch) -> None:
    """The re-bound off compose => the EMPTY dict -- the plain construction byte-identical, NEITHER kwarg."""
    monkeypatch.setattr(mcp_auth, "AUTH_MODE", "off")
    assert mcp_auth.compose_door_kwargs() == {}


@pytest.mark.usefixtures("door")
def test_compose_never_passes_stdio_policy_the_trust_default(monkeypatch: pytest.MonkeyPatch) -> None:
    """The compose NEVER passes stdio_policy at either mode -- the substrate's trust default preserved."""
    assert "stdio_policy" not in mcp_auth.compose_door_kwargs()
    monkeypatch.setattr(mcp_auth, "AUTH_MODE", "off")
    assert "stdio_policy" not in mcp_auth.compose_door_kwargs()


@pytest.mark.usefixtures("door")
def test_stdio_transport_skips_the_checks_anonymous_ride_preserved() -> None:
    """Over stdio the checks are skipped -- the ANONYMOUS call reaches the CORE's refusal, never the door's."""
    token = set_transport("stdio")
    try:
        result = asyncio.run(mcp_server.server.call_tool("runs.next", {"run_id": "RUN-9999"}))
    finally:
        reset_transport(token)
    assert result.is_error is True
    assert "Not found:" in _join(result)  # the core's unknown-run refusal, never the door's hide


def test_harness_spawn_bare_no_auth_env_source_scan() -> None:
    """The harness's spawn pinned bare -- the module command, NO env, NO auth (the spawn IS the credential)."""
    config = json.loads((Path(__file__).resolve().parents[1] / "opencode.json").read_text(encoding="utf-8"))
    block = config["mcp"]["prioritree"]
    assert block["command"] == ["uv", "run", "python", "-m", "prioritree.mcp_server"]
    assert "env" not in block
    assert "auth" not in block


@pytest.mark.parametrize(
    ("mode", "state", "expected"),
    [
        ("on", "present", "auth: on | keys: {home} | count: 1"),
        ("on", "absent", "auth: on (failopen -- no key store) | keys: {home} | next-action: prioritree key mint"),
        ("off", "present", "auth: off (operator's explicit degrade) | keys: {home} | count: 1"),
    ],
)
def test_boot_marker_three_states(tmp_path: Path, mode: str, state: str, expected: str) -> None:
    """render_boot_marker's three states => the exact bytes (the store module's renderer, never re-authored)."""
    home = tmp_path / _KEYS_FILE
    count = 0
    if state == "present":
        KeyStore(home).mint("key-holder", "human", ("next",), "mcp")
        count = len(KeyStore(home).records)  # the boot's own load: a container over the present store
    assert render_boot_marker(home, mode, count) == expected.format(home=home)


@pytest.mark.usefixtures("door")
def test_typo_auth_refuses_loudly_at_the_door_boot() -> None:
    """A typo'd AUTH value refuses LOUDLY at the resolve -- never a silent on-or-off (the default 'on')."""
    with pytest.raises(KeyStoreRefusedError, match="AUTH got"):
        resolve_auth_mode("bogus")
    assert mcp_auth.AUTH_MODE == "on"


@pytest.mark.parametrize("tool", _TOOLS)
@pytest.mark.usefixtures("door")
def test_granted_caller_passes_each_tool(tool: str) -> None:
    """The granted five-token caller passes the gate at EACH tool (the chain exercised, the adapter bypassed)."""
    request = PolicyRequest(
        tool=tool,
        effect=Effect.READ,
        tags=frozenset[str](),
        identity=identity_from_token(_token(_FIVE)),
    )
    assert mcp_auth.gate(request) is True


@pytest.mark.parametrize(
    ("role_scopes", "tool"),
    [
        (_COMPARATOR, "runs.register"),
        (_COMPARATOR, "votes.census"),
        (_COMPARATOR, "runs.tally"),
        (_OPERATOR, "runs.next"),
        (_OPERATOR, "votes.cast"),
        (_AUDITOR, "runs.register"),
        (_AUDITOR, "runs.next"),
        (_AUDITOR, "votes.cast"),
    ],
)
@pytest.mark.usefixtures("door")
def test_per_role_denials_default_deny_live(role_scopes: tuple[str, ...], tool: str) -> None:
    """Each role's ungranted tool DENIES at the gate -- DEFAULT-DENY live (the ROLE_SCOPES' literals)."""
    request = PolicyRequest(
        tool=tool,
        effect=Effect.READ,
        tags=frozenset[str](),
        identity=identity_from_token(_token(role_scopes)),
    )
    assert mcp_auth.gate(request) is False


@pytest.mark.usefixtures("door")
def test_hide_from_tools_list_per_caller() -> None:
    """The same gate's list face -- the comparator next+cast, the auditor census+tally (the hide, per caller).

    The hide PER CALLER: the same AuthCheck that refuses the guessed name
    filters the tools/list ride (the substrate's one-decision composition).
    """
    with as_caller(access_token=_token(_COMPARATOR, subject=f"door-{next(_CALLERS)}")):
        names = {t.name for t in asyncio.run(mcp_server.server.list_tools())}
    assert "runs.next" in names
    assert "votes.cast" in names
    assert "runs.register" not in names
    with as_caller(access_token=_token(_AUDITOR, subject=f"door-{next(_CALLERS)}")):
        names = {t.name for t in asyncio.run(mcp_server.server.list_tools())}
    assert "votes.census" in names
    assert "runs.tally" in names
    assert "votes.cast" not in names


@pytest.mark.usefixtures("door")
def test_guessed_name_refusal_opaque_the_reason_never_disclosed() -> None:
    """The denied caller's guessed-name call => the OPAQUE unknown-tool refusal (indistinguishable from absence).

    The teaching loss PINNED as tested behavior: the refusal discloses
    nothing -- no scope, no grant, not even the guessed name (the
    unauthorized agent cannot tell broken-server from unauthorized-self)
    -- the substrate's own envelope, the design's accepted price, never
    a bug.
    """
    with as_caller(access_token=_token(_COMPARATOR, subject=f"door-{next(_CALLERS)}")):
        result = asyncio.run(
            mcp_server.server.call_tool(
                "runs.register",
                {"items": _ITEMS, "quorum": 1, **_REGISTER_OPERATOR},
            ),
        )
    assert result.is_error is True
    text = _join(result)
    assert "No such tool" in text
    assert "runs.register" not in text  # the guessed name never confirmed
    assert "scope" not in text  # the grant's noun never disclosed


@pytest.mark.usefixtures("door")
def test_auth_off_degrade_no_hide_the_scopeless_ride(monkeypatch: pytest.MonkeyPatch) -> None:
    """At the re-bound off the SCOPE-LESS token rides ALL FIVE -- no hide anywhere (the per-call member read).

    The token scope-less yet claims-carrying (the door-shaped claims -- the
    cast door's contract at the authenticated read; a claims-less token
    the §1 KeyError crash lane's own form, the honest crash, never an
    ack): the five tools all REACHED in-process -- the register ack, the
    next pair, the cast ack, the census body, the tally's own
    halt-or-done -- NO NotFoundError anywhere (the degrade never a
    lockout).
    """
    monkeypatch.setattr(mcp_auth, "AUTH_MODE", "off")
    with as_caller(access_token=_token((), subject=f"door-{next(_CALLERS)}")):
        ack = asyncio.run(
            mcp_server.server.call_tool(
                "runs.register",
                {"items": _ITEMS, "quorum": 1, **_REGISTER_OPERATOR},
            ),
        )
        assert ack.is_error is False
        assert ack.structured_content == {"run_id": _RUN_ID, "count": 2, "quorum": 1, "verdicts": _VERDICTS}
        pair = asyncio.run(mcp_server.server.call_tool("runs.next", {"run_id": _RUN_ID}))
        assert pair.is_error is False
        assert pair.structured_content == {
            "done": False,
            "item_a": "a",
            "item_b": "b",
            "count": 0,
            "presentation_order": "canonical",
            "expected": "",
            "found": "",
            "next_action": "",
        }
        cast = asyncio.run(
            mcp_server.server.call_tool(
                "votes.cast",
                {
                    "run_id": _RUN_ID,
                    "pair": _ITEMS,
                    "winner": "prefer-a",
                    "comparator_id": "x",
                    "comparator_class": "human",
                },
            ),
        )
        assert cast.is_error is False
        assert cast.structured_content == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}
        census = asyncio.run(mcp_server.server.call_tool("votes.census", {"run_id": _RUN_ID}))
        assert census.is_error is False
        assert census.structured_content == {"total": 1, "items": {"a": 1, "b": 1}}
        tally = asyncio.run(mcp_server.server.call_tool("runs.tally", {"run_id": _RUN_ID}))
        assert tally.is_error is True  # the corroboration halt -- the tally REACHED, never hidden
        assert "Invalid input:" in _join(tally)


@pytest.mark.usefixtures("door")
def test_verified_class_overrides_the_bodys_claim() -> None:
    """The token's llm-class claims stamp over the BODY's human claim -- the halt names 'missing human'."""
    token = _token(_FIVE, comparator_class="llm", subject=f"door-{next(_CALLERS)}")
    with as_caller(access_token=token):
        registered = asyncio.run(
            mcp_server.server.call_tool(
                "runs.register",
                {"items": _ITEMS, "quorum": 2, **_REGISTER_OPERATOR},
            ),
        )
        assert registered.is_error is False
        cast = asyncio.run(
            mcp_server.server.call_tool(
                "votes.cast",
                {
                    "run_id": _RUN_ID,
                    "pair": _ITEMS,
                    "winner": "prefer-a",
                    "comparator_id": "x",
                    "comparator_class": "human",  # the body's claim -- never consulted at the verified door
                },
            ),
        )
        assert cast.is_error is False
        halt = asyncio.run(mcp_server.server.call_tool("runs.tally", {"run_id": _RUN_ID}))
        assert halt.is_error is True
        assert "missing human" in _join(halt)  # the llm stamp verified -- the halt names the OTHER class


@pytest.mark.usefixtures("door")
def test_verified_id_overrides_the_bodys_id() -> None:
    """The VERIFIED id binds the casts -- the body's changed id never forks the author (the correction lands)."""
    with as_caller(access_token=_token(_FIVE, subject=f"door-{next(_CALLERS)}")):
        registered = asyncio.run(
            mcp_server.server.call_tool(
                "runs.register",
                {"items": _ITEMS, "quorum": 1, **_REGISTER_OPERATOR},
            ),
        )
        assert registered.is_error is False
        first = asyncio.run(
            mcp_server.server.call_tool(
                "votes.cast",
                {
                    "run_id": _RUN_ID,
                    "pair": _ITEMS,
                    "winner": "prefer-a",
                    "comparator_id": "x",
                    "comparator_class": "human",
                },
            ),
        )
        assert first.structured_content == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}
        correction = asyncio.run(
            mcp_server.server.call_tool(
                "votes.cast",
                {
                    "run_id": _RUN_ID,
                    "pair": _ITEMS,
                    "winner": "prefer-b",
                    "comparator_id": "imposter",  # the body's changed id -- unread at the verified door
                    "comparator_class": "human",
                    "supersedes": "VOTE-0001",
                },
            ),
        )
        assert correction.is_error is False
        assert correction.structured_content == {"vote_id": "VOTE-0002", "count": 2, "acknowledged": False}


@pytest.mark.usefixtures("door")
def test_auth_off_class_falls_back_to_the_bodys_claim(monkeypatch: pytest.MonkeyPatch) -> None:
    """At auth-off the ANONYMOUS cast falls back to the body's claim -- the halt names 'missing human'."""
    monkeypatch.setattr(mcp_auth, "AUTH_MODE", "off")
    registered = asyncio.run(
        mcp_server.server.call_tool(
            "runs.register",
            {"items": _ITEMS, "quorum": 2, **_REGISTER_OPERATOR},
        ),
    )
    assert registered.is_error is False
    cast = asyncio.run(
        mcp_server.server.call_tool(
            "votes.cast",
            {
                "run_id": _RUN_ID,
                "pair": _ITEMS,
                "winner": "prefer-a",
                "comparator_id": "x",
                "comparator_class": "llm",  # the body's claim stamps -- no verified record at the degrade
            },
        ),
    )
    assert cast.is_error is False
    halt = asyncio.run(mcp_server.server.call_tool("runs.tally", {"run_id": _RUN_ID}))
    assert halt.is_error is True
    assert "missing human" in _join(halt)


@pytest.mark.usefixtures("door")
def test_supersedes_author_refusal_through_the_door_found_elides() -> None:
    """Another author's supersedes => the PermissionDenied VALUE -- found elides the author (the ThreePart)."""
    with as_caller(access_token=_token(_FIVE, comparator_id="author-a", subject=f"door-{next(_CALLERS)}")):
        registered = asyncio.run(
            mcp_server.server.call_tool(
                "runs.register",
                {"items": _ITEMS, "quorum": 1, **_REGISTER_OPERATOR},
            ),
        )
        assert registered.is_error is False
        first = asyncio.run(
            mcp_server.server.call_tool(
                "votes.cast",
                {
                    "run_id": _RUN_ID,
                    "pair": _ITEMS,
                    "winner": "prefer-a",
                    "comparator_id": "x",
                    "comparator_class": "human",
                },
            ),
        )
        assert first.structured_content == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}
    with as_caller(access_token=_token(_FIVE, comparator_id="author-b", subject=f"door-{next(_CALLERS)}")):
        clash = asyncio.run(
            mcp_server.server.call_tool(
                "votes.cast",
                {
                    "run_id": _RUN_ID,
                    "pair": _ITEMS,
                    "winner": "prefer-b",
                    "comparator_id": "y",
                    "comparator_class": "human",
                    "supersedes": "VOTE-0001",
                },
            ),
        )
    assert clash.is_error is True
    text = _join(clash)
    assert "Not permitted:" in text
    assert "expected:" in text
    assert "found:" in text
    assert "next_action:" in text
    assert "another author's vote" in text
    assert "author-a" not in text  # the author's id never named -- the identity oracle starved


@pytest.mark.usefixtures("door")
def test_own_author_supersede_passes_under_the_verified_id() -> None:
    """The own-author supersedes passes under the VERIFIED id -- the correction lands (VOTE-0002, the ack chain)."""
    with as_caller(access_token=_token(_FIVE, subject=f"door-{next(_CALLERS)}")):
        registered = asyncio.run(
            mcp_server.server.call_tool(
                "runs.register",
                {"items": _ITEMS, "quorum": 1, **_REGISTER_OPERATOR},
            ),
        )
        assert registered.is_error is False
        first = asyncio.run(
            mcp_server.server.call_tool(
                "votes.cast",
                {
                    "run_id": _RUN_ID,
                    "pair": _ITEMS,
                    "winner": "prefer-a",
                    "comparator_id": "x",
                    "comparator_class": "human",
                },
            ),
        )
        assert first.structured_content == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}
        correction = asyncio.run(
            mcp_server.server.call_tool(
                "votes.cast",
                {
                    "run_id": _RUN_ID,
                    "pair": _ITEMS,
                    "winner": "prefer-b",
                    "comparator_id": "x",
                    "comparator_class": "human",
                    "supersedes": "VOTE-0001",
                },
            ),
        )
        assert correction.is_error is False
        assert correction.structured_content == {"vote_id": "VOTE-0002", "count": 2, "acknowledged": False}


def test_fork_guard_the_map_keys_and_tokens() -> None:
    """The fork-guard -- the map's keys the five tool names, the tokens within the SCOPE_TOKENS vocabulary."""
    assert set(mcp_auth.TOOL_SCOPES) == set(_TOOLS)
    assert set(mcp_auth.TOOL_SCOPES.values()) <= {"register", "next", "cast", "state", "tally", "manifest"}
