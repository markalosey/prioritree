# Copyright (C) 2026 Mark Losey. All rights reserved.
"""test_service_auth — the auth doors' falsification set, in-process (servingtierintegrationspec §7a).

The serving-tier-integration unit's auth test surface — the six gated routes'
doors over TestClient(app), the seam AND the key store injected per test (the
test_service_face.py:64 fixture school extended: app.state.seam +
app.state.keys + app.state.auth): the sixteen arcs (the two parametrizes: the
six no-key 401 lanes, the two scope-denial lanes) — (1) the no-key 401 at
every route, the SAME ThreePart bytes at each (the oracle never fed); (2) the
wrong key's SAME 401; (3) the wrong audience's SAME 401, mcp never named; (4)
the scope denials at 403 — the auditor's key at votes and the comparator's key
at runs (the default deny); (5) the six-token key's own route bodies —
register 201 through tally 200 at full coverage; (6) the mid-flight mint
through a second container lands live (the stat ride); (7) the auth-off
degrade — the six routes' bodies as today, no key anywhere; (8) the 401's
handler lane — the fold never re-badges, the mint taught, never ESCALATION;
(9) the supersedes author mismatch at 403 — found elides the author, the
target pair untouched; (10) the own-author supersede passes (the ack chain);
(11) the verified id wired over the body's claim; (12) the class stamp over
the body's claim; (13) the auth-off class fallback to the claim (the
degrade's price); (14) the fence — the route-table walk, every service route
gated, the exemptions named; (15) the fence's kin — the source scan, six door
tokens; (16) the docs trio 404s at both tiers. The S101/PLR2004 tests ruling
stands.

Provenance: servingtierintegrationspec §7a (the arcs' fence), the unit brief
§1/§3 (the doors and the handlers), packet build/serving-tier-integration
step 8 of 9, route prioritree-auth, 2026-11-24 session.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from collections.abc import Sequence

from fastapi.routing import APIRoute
from fastapi.testclient import TestClient

from prioritree.key_store import KeyStore
from prioritree.key_verify import AUTH_HEADER_DEFAULT
from prioritree.service import app
from prioritree.service_store import Serialize

# The wire's own vocabulary (service.py's constants cited as literals — the
# literals ARE the specification under test): the route paths, the item set
# (three items -> three scheduled pairs — the corroboration law needs BOTH
# classes per pair, six votes the coverage drive), the six-scope grant whole,
# and the refusal grammar's three keys.
_RUNS = "/runs"
_RUN_ID = "RUN-0001"
_ITEMS = [["a", "one"], ["b", "two"], ["c", "three"]]
_OPERATOR = {"operator_id": "op-1", "question": "Which matters more?"}
_REGISTER_BODY = {"items": _ITEMS, **_OPERATOR}
_VOTE_BODY = {
    "pair": ["a", "b"],
    "winner": "prefer-a",
    "comparator_id": "x",
    "comparator_class": "human",
}
_MANIFEST_BODY = {
    "run_id": _RUN_ID,
    "question": "Which matters more?",
    "verdicts": ["prefer-a", "prefer-b", "tie"],
    "quorum": 1,
    "items": _ITEMS,
}
_ALL = ("register", "next", "cast", "state", "tally", "manifest")
_REFUSAL_KEYS = frozenset({"expected", "found", "next_action"})
_KEYS_FILE = "keys.jsonl"
_SIX_PATHS = frozenset(
    {
        "/runs",
        "/runs/{run_id}/next",
        "/runs/{run_id}/votes",
        "/runs/{run_id}/state",
        "/runs/{run_id}/tally",
        "/runs/{run_id}/manifest",
    },
)


@pytest.fixture
def client(tmp_path: Path) -> TestClient:
    """Isolate the seam and the key store by injection — a fresh store per test, no env, no CWD games.

    Purpose: overwrite app.state.seam with Serialize(tmp_path), app.state.keys
    with the mint-at-tmp key store (KeyStore over tmp_path / "keys.jsonl"),
    and app.state.auth with "on" — the seam-injection precedent extended to
    the doors' own state (the boot's construction the default; the auth-off
    arcs overwrite app.state.auth per test, the seam's own law); the keys
    container is the door's own read surface — every mint lands in its home.
    Refuses when: never — a fixture (the isolate-then-yield form).
    Re-run: deterministic — a fresh tmp home per test.
    Touches: the tmp home only (pytest's own tmp_path).
    Provenance: servingtierintegrationspec §7a (the fixture fence), the
    test_service_face.py:64 injection precedent, G-SERVING-TIER-INTEGRATION-BRIEF.
    """
    app.state.seam = Serialize(tmp_path)
    app.state.keys = KeyStore(tmp_path / _KEYS_FILE)
    app.state.auth = "on"
    return TestClient(app)


def _grant(
    scopes: Sequence[str],
    *,
    audience: str = "service",
    comparator_class: str = "human",
    home: KeyStore,
) -> str:
    """Mint one key at the injected home — the arcs' shared grant (the fence's own helper).

    Purpose: mint through the injected container (comparator_id "key-holder"
    the fence's fixed id — the verified-stamp arcs' noun), returning the
    plaintext key for the door's header; the audience and class knobs the
    wrong-audience and class-stamp arcs' own.
    Refuses when: the mint's own typed refusal rides (KeyStoreRefusedError —
    an invalid scope/audience a test bug, never caught here).
    Re-run: a fresh random key per call — the mint's own law (a re-grant a
    NEW key, never a replay).
    Touches: the tmp home's key file (one minted line).
    Provenance: servingtierintegrationspec §7a (the _grant fence),
    G-SERVING-TIER-INTEGRATION-BRIEF.
    """
    key, _digest = home.mint("key-holder", comparator_class, scopes, audience)
    return key


def _assert_same_401(body: dict[str, str]) -> None:
    """Assert the 401's three fields — the SAME bytes at every refusing leg (the oracle never fed)."""
    assert set(body) == _REFUSAL_KEYS
    assert body["expected"] == f"the key in the {AUTH_HEADER_DEFAULT} header"
    assert body["found"] == "absent-or-unknown"
    assert body["next_action"].startswith("mint a key: prioritree key mint")


@pytest.mark.parametrize(
    ("method", "path", "body"),
    [
        ("post", _RUNS, _REGISTER_BODY),
        ("get", f"/runs/{_RUN_ID}/next", None),
        ("post", f"/runs/{_RUN_ID}/votes", _VOTE_BODY),
        ("get", f"/runs/{_RUN_ID}/state", None),
        ("get", f"/runs/{_RUN_ID}/tally", None),
        ("get", f"/runs/{_RUN_ID}/manifest", None),
    ],
)
def test_no_key_refused_401_at_every_route(
    client: TestClient,
    method: str,
    path: str,
    body: dict[str, object] | None,
) -> None:
    """No key at the door => 401 at all six routes, the SAME ThreePart bytes (the oracle never fed)."""
    response = client.post(path, json=body) if method == "post" else client.get(path)
    assert response.status_code == 401
    _assert_same_401(response.json())


def test_wrong_key_same_401_three_fields(client: TestClient) -> None:
    """A bogus key at the door => the SAME 401 three fields — the oracle never fed (the digest miss)."""
    _grant(_ALL, home=app.state.keys)  # the store carries a real key — the bogus one still the SAME 401
    response = client.get(f"/runs/{_RUN_ID}/next", headers={AUTH_HEADER_DEFAULT: "bogus-key"})
    assert response.status_code == 401
    _assert_same_401(response.json())


def test_wrong_audience_same_401_mcp_never_named(client: TestClient) -> None:
    """An mcp-audience key at the service door => the SAME 401 — mcp absent from the fields whole (F5)."""
    mcp_key = _grant(("next",), audience="mcp", home=app.state.keys)
    response = client.get(f"/runs/{_RUN_ID}/next", headers={AUTH_HEADER_DEFAULT: mcp_key})
    assert response.status_code == 401
    _assert_same_401(response.json())
    assert "mcp" not in response.text


@pytest.mark.parametrize(
    ("scopes", "path", "body", "expected"),
    [
        (
            ("state",),
            f"/runs/{_RUN_ID}/votes",
            _VOTE_BODY,
            {
                "expected": "the cast scope",
                "found": "the key's scopes ['state']",
                "next_action": "re-mint with the scope: prioritree key mint ... --scopes <csv>+cast",
            },
        ),
        (
            ("cast",),
            _RUNS,
            _REGISTER_BODY,
            {
                "expected": "the register scope",
                "found": "the key's scopes ['cast']",
                "next_action": "re-mint with the scope: prioritree key mint ... --scopes <csv>+register",
            },
        ),
    ],
)
def test_scope_denied_403_default_deny(
    client: TestClient,
    scopes: tuple[str, ...],
    path: str,
    body: dict[str, object],
    expected: dict[str, str],
) -> None:
    """A key lacking the route's scope => 403 — expected names the scope, found the key's scopes, the re-mint."""
    key = _grant(scopes, home=app.state.keys)
    response = client.post(path, json=body, headers={AUTH_HEADER_DEFAULT: key})
    assert response.status_code == 403
    assert response.json() == expected


def test_right_key_route_bodies_returned(client: TestClient) -> None:
    """The six-token key => every route's own body — register 201 through tally 200 at full coverage.

    The corroboration twin named: the tally gate demands >=1 human AND >=1 llm
    per pair, and the door stamps the KEY's class — a lone key cannot
    corroborate its own votes, so the llm-class twin (the same six-token
    grant) casts the corroborating half.
    """
    human_key = _grant(_ALL, home=app.state.keys)
    llm_key = _grant(_ALL, comparator_class="llm", home=app.state.keys)
    ack = client.post(_RUNS, json=_REGISTER_BODY, headers={AUTH_HEADER_DEFAULT: human_key})
    assert ack.status_code == 201
    assert ack.json() == {"run_id": _RUN_ID}
    pair = client.get(f"/runs/{_RUN_ID}/next", headers={AUTH_HEADER_DEFAULT: human_key})
    assert pair.status_code == 200
    assert pair.json() == {"item_a": "a", "item_b": "b", "count": 0, "presentation_order": "canonical"}
    vote = client.post(
        f"/runs/{_RUN_ID}/votes",
        json=_VOTE_BODY,
        headers={AUTH_HEADER_DEFAULT: human_key},
    )
    assert vote.status_code == 200
    assert vote.json() == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}
    state = client.get(f"/runs/{_RUN_ID}/state", headers={AUTH_HEADER_DEFAULT: human_key})
    assert state.status_code == 200
    assert state.json() == {"total": 1, "items": {"a": 1, "b": 1, "c": 0}}
    manifest = client.get(f"/runs/{_RUN_ID}/manifest", headers={AUTH_HEADER_DEFAULT: human_key})
    assert manifest.status_code == 200
    assert manifest.json() == _MANIFEST_BODY
    for key, (item_a, item_b) in (
        (llm_key, ("a", "b")),
        (human_key, ("a", "c")),
        (llm_key, ("a", "c")),
        (human_key, ("b", "c")),
        (llm_key, ("b", "c")),
    ):
        twin = client.post(
            f"/runs/{_RUN_ID}/votes",
            json={**_VOTE_BODY, "pair": [item_a, item_b]},
            headers={AUTH_HEADER_DEFAULT: key},
        )
        assert twin.status_code == 200
    tally = client.get(f"/runs/{_RUN_ID}/tally", headers={AUTH_HEADER_DEFAULT: human_key})
    assert tally.status_code == 200
    whole = tally.json()
    assert whole["ranked_groups"] == [["a"], ["b"], ["c"]]
    assert whole["coverage"]["done"] is True


def test_midflight_mint_lands_live_through_the_door(client: TestClient, tmp_path: Path) -> None:
    """A mint through a second container over the same home => the door sees it live (the stat ride)."""
    second = KeyStore(tmp_path / _KEYS_FILE)  # the CLI's own container over the same home
    key = _grant(_ALL, home=second)
    ack = client.post(_RUNS, json=_REGISTER_BODY, headers={AUTH_HEADER_DEFAULT: key})
    assert ack.status_code == 201  # the door's boot-time load predates the mint — the stat ride re-loaded
    response = client.get(f"/runs/{_RUN_ID}/next", headers={AUTH_HEADER_DEFAULT: key})
    assert response.status_code == 200
    assert response.json() == {"item_a": "a", "item_b": "b", "count": 0, "presentation_order": "canonical"}


def test_auth_off_degrade_six_routes_pass_bare(client: TestClient) -> None:
    """Auth off => the six routes' bodies as today, no key anywhere — the anonymous ride (the body's claims stamp)."""
    app.state.auth = "off"
    ack = client.post(_RUNS, json=_REGISTER_BODY)
    assert ack.status_code == 201
    assert ack.json() == {"run_id": _RUN_ID}
    pair = client.get(f"/runs/{_RUN_ID}/next")
    assert pair.status_code == 200
    assert pair.json() == {"item_a": "a", "item_b": "b", "count": 0, "presentation_order": "canonical"}
    vote = client.post(f"/runs/{_RUN_ID}/votes", json=_VOTE_BODY)
    assert vote.status_code == 200
    assert vote.json() == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}
    state = client.get(f"/runs/{_RUN_ID}/state")
    assert state.status_code == 200
    assert state.json() == {"total": 1, "items": {"a": 1, "b": 1, "c": 0}}
    manifest = client.get(f"/runs/{_RUN_ID}/manifest")
    assert manifest.status_code == 200
    assert manifest.json() == _MANIFEST_BODY
    for item_a, item_b, body_class in (
        ("a", "b", "llm"),
        ("a", "c", "human"),
        ("a", "c", "llm"),
        ("b", "c", "human"),
        ("b", "c", "llm"),
    ):
        twin = client.post(
            f"/runs/{_RUN_ID}/votes",
            json={**_VOTE_BODY, "pair": [item_a, item_b], "comparator_class": body_class},
        )
        assert twin.status_code == 200
    tally = client.get(f"/runs/{_RUN_ID}/tally")
    assert tally.status_code == 200
    assert tally.json()["ranked_groups"] == [["a"], ["b"], ["c"]]


def test_handler_lane_401_stays_401_never_500(client: TestClient) -> None:
    """The no-key refusal rides the DEDICATED handler — 401 stays 401, the mint taught, never the fold's ESCALATION."""
    response = client.get(f"/runs/{_RUN_ID}/next")
    assert response.status_code == 401
    body = response.json()
    _assert_same_401(body)
    assert "escalate" not in body["next_action"]


def test_supersedes_author_mismatch_403_found_elides_the_author(
    client: TestClient,
    tmp_path: Path,
) -> None:
    """Another author's supersedes => 403, found elides the author; the target pair untouched (VOTE-0001 counted)."""
    key_a = _grant(("register", "cast", "state"), home=app.state.keys)
    key_b, _digest = KeyStore(tmp_path / _KEYS_FILE).mint("other-holder", "human", ("cast",), "service")
    client.post(_RUNS, json=_REGISTER_BODY, headers={AUTH_HEADER_DEFAULT: key_a})
    first = client.post(f"/runs/{_RUN_ID}/votes", json=_VOTE_BODY, headers={AUTH_HEADER_DEFAULT: key_a})
    assert first.status_code == 200
    assert first.json() == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}
    clash = client.post(
        f"/runs/{_RUN_ID}/votes",
        json={**_VOTE_BODY, "winner": "prefer-b", "supersedes": "VOTE-0001"},
        headers={AUTH_HEADER_DEFAULT: key_b},
    )
    assert clash.status_code == 403
    body = clash.json()
    assert set(body) == _REFUSAL_KEYS
    assert "another author's vote" in body["found"]
    assert "key-holder" not in clash.text  # the author's id never named — the identity oracle starved
    census = client.get(f"/runs/{_RUN_ID}/state", headers={AUTH_HEADER_DEFAULT: key_a})
    assert census.status_code == 200
    assert census.json() == {"total": 1, "items": {"a": 1, "b": 1, "c": 0}}


def test_own_author_supersede_passes(client: TestClient) -> None:
    """The same key supersedes its own vote => 200, the ack chain (VOTE-0002, count 2, the winner differs)."""
    key = _grant(("register", "cast"), home=app.state.keys)
    client.post(_RUNS, json=_REGISTER_BODY, headers={AUTH_HEADER_DEFAULT: key})
    first = client.post(f"/runs/{_RUN_ID}/votes", json=_VOTE_BODY, headers={AUTH_HEADER_DEFAULT: key})
    assert first.status_code == 200
    correction = client.post(
        f"/runs/{_RUN_ID}/votes",
        json={**_VOTE_BODY, "winner": "prefer-b", "supersedes": "VOTE-0001"},
        headers={AUTH_HEADER_DEFAULT: key},
    )
    assert correction.status_code == 200
    assert correction.json() == {"vote_id": "VOTE-0002", "count": 2, "acknowledged": False}


def test_verified_id_wiring_body_id_ignored(client: TestClient, tmp_path: Path) -> None:
    """The verified record's id wires into the cast — the body's 'imposter' self-claim dies at the door."""
    key = _grant(_ALL, home=app.state.keys)
    client.post(_RUNS, json=_REGISTER_BODY, headers={AUTH_HEADER_DEFAULT: key})
    ack = client.post(
        f"/runs/{_RUN_ID}/votes",
        json={**_VOTE_BODY, "comparator_id": "imposter"},
        headers={AUTH_HEADER_DEFAULT: key},
    )
    assert ack.status_code == 200
    assert ack.json() == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}
    log = Serialize(tmp_path).census(_RUN_ID).vote_log
    assert len(log) == 1
    assert log[0].comparator_id == "key-holder"  # the record's verified id — the self-claim never landed


def test_class_stamp_overrides_the_bodys_claim(client: TestClient, tmp_path: Path) -> None:
    """An llm-class key's record stamps 'llm' over the body's 'human' claim — the class is the door's truth (F8)."""
    key = _grant(_ALL, comparator_class="llm", home=app.state.keys)
    client.post(_RUNS, json=_REGISTER_BODY, headers={AUTH_HEADER_DEFAULT: key})
    ack = client.post(f"/runs/{_RUN_ID}/votes", json=_VOTE_BODY, headers={AUTH_HEADER_DEFAULT: key})
    assert ack.status_code == 200
    log = Serialize(tmp_path).census(_RUN_ID).vote_log
    assert len(log) == 1
    assert log[0].comparator_class == "llm"  # the body claimed 'human' — the door's record the truth


def test_auth_off_class_falls_back_to_claim(client: TestClient, tmp_path: Path) -> None:
    """At auth-off the body's class claim stamps — the degrade's price named: the unverified claim stands."""
    app.state.auth = "off"
    client.post(_RUNS, json=_REGISTER_BODY)
    ack = client.post(f"/runs/{_RUN_ID}/votes", json={**_VOTE_BODY, "comparator_class": "llm"})
    assert ack.status_code == 200
    log = Serialize(tmp_path).census(_RUN_ID).vote_log
    assert len(log) == 1
    assert log[0].comparator_class == "llm"  # the body's claim stood — no verified record at the degrade


def test_fence_route_table_walk_every_service_route_gated() -> None:
    """The fence — every APIRoute on the service app carries the door (the require_key factory marker).

    The exempt set NAMED: the web child's tail Mount (app.mount("/", web_app))
    is a Mount object, never an APIRoute — the walk's own isinstance filter
    never touches it (any mount beneath it — static included — lives in the
    child's own table); the docs trio is stripped at construction
    (docs_url=None, redoc_url=None, openapi_url=None — absent from the table
    whole, its 404s arc 16's own); no seventh APIRoute exists — the walk pins
    the six gated and ONLY the six.
    """
    gated: set[str] = set()
    for route in app.routes:
        if not isinstance(route, APIRoute):
            continue
        assert route.path in _SIX_PATHS
        markers = [
            dependency.call.__qualname__ for dependency in route.dependant.dependencies if dependency.call is not None
        ]
        assert any(marker.startswith("require_key") for marker in markers)  # the factory marker
        gated.add(route.path)
    assert gated == _SIX_PATHS


def test_fence_source_scan_six_door_tokens() -> None:
    """The fence's kin — service.py's bytes carry the door token six times (the six aliases, one per route)."""
    module_path = Path(__file__).resolve().parents[1] / "src" / "prioritree" / "service.py"
    source = module_path.read_text(encoding="utf-8")
    assert source.count("Depends(require_key(") == 6


def test_docs_trio_stripped_at_both_tiers(client: TestClient) -> None:
    """GET /docs, /redoc, /openapi.json => 404 — the parent's strip, the child's own standing (both tiers closed)."""
    for path in ("/docs", "/redoc", "/openapi.json"):
        response = client.get(path)
        assert response.status_code == 404
