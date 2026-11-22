# Copyright (C) 2026 Mark Losey. All rights reserved.
"""test_service_face — the wire face's falsification set, in-process.

The service-face unit's test surface (service-face-brief §5 + the ux build's
sixth query + ThreePart cures): seven arcs over TestClient(app) in-process —
(1) the six successes (register/serve/cast/state/tally, each route's exact
body asserted + the manifest's five-key 200, the stamps elided); (2) the
refusal arcs (404 the unknown run — next AND manifest; 422 the out-of-set
verdict; 409 the SAFE HALT); (3) the re-badge both (a malformed register body
=> 400 the family grammar, the violation taught in found; a door refusal =>
422 the family grammar — the two grammars never conflated); (4) the framework
arcs (the unmatched path => 404 the family grammar, the path named in found;
the disallowed method => 405 the family grammar, the method named in found);
(5) the DONE 200 (the exhausted turn: done marker + the three fields, the
tally pointer in next_action); (6) the 500 arc (the monkeypatched seam verb
raising, the three-part body, the traceback's absence from the body); (7) the
201 register re-assertion (the stem in the body). Isolation by injection
(Q-service-lifecycle): each test overwrites app.state.seam = Serialize(tmp_path)
— store-as-parameter, no env, no CWD games; the fixture creates the tmp home's
parent (Serialize's register does the mkdir itself, the parent the test's own
duty). The S101/PLR2004 tests ruling stands.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from pathlib import Path

from fastapi.testclient import TestClient

from prioritree.service import app
from prioritree.service_store import Serialize

# The wire's own vocabulary (service.py's constants cited as literals — the
# literals ARE the specification under test): the route paths and the item
# set a/b/c (three items -> three scheduled pairs: ab, ac, bc — full
# coverage at three prefer-a votes, the ranked whole hand-computable).
_RUNS = "/runs"
_ITEMS = [["a", "one"], ["b", "two"], ["c", "three"]]
_OPERATOR = {"operator_id": "op-1", "question": "Which matters more?"}
_RUN_ID = "RUN-0001"


@pytest.fixture
def client(tmp_path: Path) -> TestClient:
    """Isolate the seam by injection — a fresh store per test, no env, no CWD games.

    Purpose: overwrite app.state.seam with Serialize(tmp_path / "runs") —
    store-as-parameter; yield (app, TestClient(app)); restore nothing (the
    module-level seam is re-minted per test by the next overwrite; the
    module-level STORE_HOME seam is never touched on disk here — the
    fixture's home is the tmp parent the test creates, the register's own
    mkdir builds the runs dir under it).
    Refuses when: never — a fixture (the isolate-then-yield form).
    Re-run: deterministic — a fresh tmp home per test.
    Touches: the tmp home only (pytest's own tmp_path).
    Provenance: service-face-brief §5 (isolation by injection), the
    dispatch synthesize/service-face-bytes (region 1).
    """
    app.state.seam = Serialize(tmp_path)
    return TestClient(app)


def test_register_success(client: TestClient) -> None:
    """POST /runs with the pairs body => 201, the stem — register's alone."""
    response = client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    assert response.status_code == 201
    assert response.json() == {"run_id": _RUN_ID}


def test_serve_success(client: TestClient) -> None:
    """GET next after register => 200, the first under-quorum pair with count 0."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    response = client.get(f"/runs/{_RUN_ID}/next")
    assert response.status_code == 200
    assert response.json() == {"item_a": "a", "item_b": "b", "count": 0}


def test_vote_success(client: TestClient) -> None:
    """POST votes after register => 200, the ack triple (the VoteRecord elided)."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    response = client.post(
        f"/runs/{_RUN_ID}/votes",
        json={
            "pair": ["a", "b"],
            "winner": "prefer-a",
            "comparator_id": "x",
            "comparator_class": "human",
        },
    )
    assert response.status_code == 200
    assert response.json() == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}


def test_state_success(client: TestClient) -> None:
    """GET state after register + one vote => 200, the census summary form."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    client.post(
        f"/runs/{_RUN_ID}/votes",
        json={
            "pair": ["a", "b"],
            "winner": "prefer-a",
            "comparator_id": "x",
            "comparator_class": "human",
        },
    )
    response = client.get(f"/runs/{_RUN_ID}/state")
    assert response.status_code == 200
    assert response.json() == {"total": 1, "items": {"a": 1, "b": 1, "c": 0}}


def test_tally_success(client: TestClient) -> None:
    """GET tally at full coverage => 200, TallyResult's frozen whole, field-for-field."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    for pair, winner in ((["a", "b"], "prefer-a"), (["a", "c"], "prefer-a"), (["b", "c"], "prefer-a")):
        client.post(
            f"/runs/{_RUN_ID}/votes",
            json={
                "pair": pair,
                "winner": winner,
                "comparator_id": "x",
                "comparator_class": "human",
            },
        )
    response = client.get(f"/runs/{_RUN_ID}/tally")
    assert response.status_code == 200
    assert response.json() == {
        "ranked_groups": [["a"], ["b"], ["c"]],
        "per_item_wins": {"a": 2, "b": 1, "c": 0},
        "per_item_losses": {"a": 0, "b": 1, "c": 2},
        "per_item_ties": {"a": 0, "b": 0, "c": 0},
        "coverage": {
            "components": [["a", "b", "c"]],
            "done": True,
            "cycle": [],
            "pair_counts": {"a|b": 1, "a|c": 1, "b|c": 1},
        },
        "algorithm_version": "win-rate-v1",
    }


def test_manifest_200(client: TestClient) -> None:
    """GET manifest after register => 200, the five-key body, the stamps elided."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    response = client.get(f"/runs/{_RUN_ID}/manifest")
    assert response.status_code == 200
    assert response.json() == {
        "run_id": _RUN_ID,
        "question": "Which matters more?",
        "verdicts": ["prefer-a", "prefer-b", "tie"],
        "quorum": 1,
        "items": [["a", "one"], ["b", "two"], ["c", "three"]],
    }


# Region 2's near-use vocabulary (the file's continuation; service.py's own
# mid-file idiom — constants at their use): the refusal grammar's three fields
# as a set, asserted EXACTLY (the family grammar — the native detail grammar of
# the 400 re-badge never carries these keys), and the crash envelope's
# escalation text (service.py's ESCALATION cited as a literal — the literals
# ARE the specification under test, the region-1 school carried; dispatch
# synthesize/service-face-bytes region 2, service-face-brief §5).
_REFUSAL_KEYS = frozenset({"expected", "found", "next_action"})
_ESCALATION = "check the server logs — the traceback is recorded there; escalate to the operator"


def test_refusal_unknown_run(client: TestClient) -> None:
    """GET next on an unregistered run => 404, the three fields, the run id in found."""
    response = client.get("/runs/RUN-9999/next")
    assert response.status_code == 404
    body = response.json()
    assert set(body) == _REFUSAL_KEYS
    assert "RUN-9999" in body["found"]


def test_refusal_manifest_unknown_run(client: TestClient) -> None:
    """GET manifest on an unregistered run => 404, the three fields, the stem in found."""
    response = client.get("/runs/RUN-9999/manifest")
    assert response.status_code == 404
    body = response.json()
    assert set(body) == _REFUSAL_KEYS
    assert "RUN-9999" in body["found"]


def test_refusal_out_of_set_verdict(client: TestClient) -> None:
    """A vote whose winner is outside the verdict set => 422, the bogus value in found."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    response = client.post(
        f"/runs/{_RUN_ID}/votes",
        json={
            "pair": ["a", "b"],
            "winner": "bogus-winner",
            "comparator_id": "x",
            "comparator_class": "human",
        },
    )
    assert response.status_code == 422
    body = response.json()
    assert set(body) == _REFUSAL_KEYS
    assert "bogus-winner" in body["found"]


def test_refusal_safe_halt(client: TestClient) -> None:
    """GET tally before full coverage => 409 the SAFE HALT, 'at quorum' verbatim in found."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    client.post(
        f"/runs/{_RUN_ID}/votes",
        json={
            "pair": ["a", "b"],
            "winner": "prefer-a",
            "comparator_id": "x",
            "comparator_class": "human",
        },
    )
    response = client.get(f"/runs/{_RUN_ID}/tally")
    assert response.status_code == 409
    body = response.json()
    assert set(body) == _REFUSAL_KEYS
    assert "at quorum" in body["expected"]


def test_rebadge_malformed_body_400(client: TestClient) -> None:
    """A register body with mistyped items => 400, the family grammar, the violation taught."""
    response = client.post(_RUNS, json={"items": "not-a-list", **_OPERATOR})
    assert response.status_code == 400
    body = response.json()
    assert set(body) == _REFUSAL_KEYS
    assert "items" in body["expected"]
    assert "body.items" in body["found"]
    assert "re-send" in body["next_action"]


def test_rebadge_door_refusal_422(client: TestClient) -> None:
    """The door's value refusal => 422 the family grammar — the two grammars never conflated."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    response = client.post(
        f"/runs/{_RUN_ID}/votes",
        json={
            "pair": ["a", "b"],
            "winner": "bogus-winner",
            "comparator_id": "x",
            "comparator_class": "human",
        },
    )
    assert response.status_code == 422
    assert set(response.json()) == _REFUSAL_KEYS


def test_refusal_unmatched_path_404(client: TestClient) -> None:
    """A path no route matches => 404, the family grammar, the path named in found."""
    response = client.get("/no-such-path")
    assert response.status_code == 404
    body = response.json()
    assert set(body) == _REFUSAL_KEYS
    assert body["expected"] == "GET /no-such-path"
    assert body["found"] == "no route matches the path /no-such-path"
    assert "POST /runs" in body["next_action"]


def test_refusal_method_not_allowed_405(client: TestClient) -> None:
    """A disallowed method at a legal web path => 405, the family grammar, the method taught.

    The arc re-targeted (web-brief §3e, the mount's price, the collaborator's
    approved amendment): the tail mount makes the CHILD own the
    disallowed-method surface (the parent's partial-match 405 never fires —
    the Mount fully matches any path the parent does not); the child's own
    handler renders the identical grammar, so the arc's INTENT holds exactly
    (a disallowed method at a legal path => 405, the method named in found,
    the legal set taught — now the mounted whole's set, which carries
    POST /ui/register).
    """
    response = client.get("/ui/register")
    assert response.status_code == 405
    body = response.json()
    assert set(body) == _REFUSAL_KEYS
    assert body["expected"] == "GET /ui/register"
    assert body["found"] == "the method GET is not allowed at the path /ui/register"
    assert "POST /ui/register" in body["next_action"]


def test_done_200(client: TestClient) -> None:
    """The exhausted two-item run => 200 DONE, the tally pointer riding in next_action."""
    client.post(_RUNS, json={"items": [["a", "alpha"], ["b", "bravo"]], **_OPERATOR})
    client.post(
        f"/runs/{_RUN_ID}/votes",
        json={
            "pair": ["a", "b"],
            "winner": "prefer-a",
            "comparator_id": "x",
            "comparator_class": "human",
        },
    )
    response = client.get(f"/runs/{_RUN_ID}/next")
    assert response.status_code == 200
    body = response.json()
    assert body["done"] is True
    assert set(body) == _REFUSAL_KEYS | {"done"}
    assert "tally" in body["next_action"]


def test_crash_envelope_500() -> None:
    """The monkeypatched seam verb raising at the real route => 500, the envelope, no traceback."""

    class _BoomSeam:
        """The stub seam — serve raises; the catch-all's forced input, zero scaffolding."""

        def serve(self, _run_id: str, _seed: int | None = None) -> tuple[str, str, int]:
            """Raise the boom — the crash the envelope folds."""
            msg = "boom"
            raise RuntimeError(msg)

    app.state.seam = _BoomSeam()
    client = TestClient(app, raise_server_exceptions=False)
    response = client.get(f"/runs/{_RUN_ID}/next")
    assert response.status_code == 500
    body = response.json()
    assert set(body) == _REFUSAL_KEYS
    assert body["expected"] == f"GET /runs/{_RUN_ID}/next"
    assert body["found"].startswith("RuntimeError: boom")
    assert body["next_action"] == _ESCALATION
    assert "Traceback" not in response.text
