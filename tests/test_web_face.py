# Copyright (C) 2026 Mark Losey. All rights reserved.
"""test_web_face — the mounted web tier's falsification set, in-process.

The web unit's test surface (web-brief §6.1): the mounted app under the
injection fixture — the SAME app now carries the mount; the child's
controllers call the service through the in-process client and the service
reads the PARENT's state.seam (the fixture's injection) — the isolation
extends to the web tier whole (store-as-parameter; no env, no CWD games —
the resolver arcs alone chdir, by pytest's own monkeypatch fixture with
its guaranteed restore: the CWD IS the resolution's own input).
The arcs: the page arcs (landing, sitting, done, progress, result
200/409/404); the fragment arcs (register 201/422/bad-quorum, the two-step
chain, the idempotent echo, the HX-Redirect, the 422 pair-untouched, the
state strip, the fold fragment); the static pair (the chrome's app.css +
app.js — the 200s pinned, a mis-named home fails loudly); the resolver arcs (the loader
seam's ordered resolution: the CWD's copy first, the package's the
fallback, the fold preserved at a wrong cwd); the no-anchoring
pins (byte-level: no sitting-context response carries the count; the
sitting surface never links state/tally). The S101/PLR2004 tests ruling
stands.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from prioritree.service import app
from prioritree.service_store import Serialize
from prioritree.web import resolve

# The wire's own vocabulary (the service face file's literals, carried 1:1 —
# the literals ARE the specification under test).
_RUNS = "/runs"
_ITEMS = [["a", "one"], ["b", "two"], ["c", "three"]]
_TWO_ITEMS = [["a", "alpha"], ["b", "bravo"]]
_OPERATOR = {"operator_id": "op-1", "question": "Which matters more?"}
_RUN_ID = "RUN-0001"
_VOTE = {"comparator_id": "x", "comparator_class": "human"}
_FORM_VOTE = {"item_a": "a", "item_b": "b", "winner": "prefer-a", **_VOTE}


@pytest.fixture
def client(tmp_path: Path) -> TestClient:
    """Isolate the seam by injection — the mounted whole under the face fixture's own form."""
    app.state.seam = Serialize(tmp_path)
    return TestClient(app)


def test_landing_serves(client: TestClient) -> None:
    """GET / serves the landing: the register form, the resume + result fields, the copy."""
    response = client.get("/")
    assert response.status_code == 200
    assert 'hx-post="/ui/register"' in response.text
    assert "judge the items two at a time" in response.text
    assert 'data-pt-path="/runs/{stem}"' in response.text
    assert 'data-pt-path="/runs/{stem}/result"' in response.text


def test_static_pair_serves(client: TestClient) -> None:
    """The static home serves its pair: app.css + app.js at 200, a byte each."""
    css = client.get("/static/app.css")
    js = client.get("/static/app.js")
    assert css.status_code == 200
    assert js.status_code == 200
    assert "--pt-gap" in css.text
    assert "pt-copy" in js.text


def test_resolve_prefers_the_cwd_home(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """A present CWD home resolves to itself — the clone's form, the order's first branch."""
    monkeypatch.chdir(tmp_path)
    (tmp_path / "web" / "templates").mkdir(parents=True)
    assert resolve("web/templates", "templates") == "web/templates"


def test_resolve_falls_back_to_the_package(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """An absent CWD home derives the package path — the installed form, the order's second branch."""
    monkeypatch.chdir(tmp_path)
    resolved = resolve("web/templates", "templates")
    assert resolved != "web/templates"
    assert Path(resolved).is_absolute()
    assert resolved.endswith("templates")


def test_resolve_keeps_the_fold_at_a_wrong_cwd(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """The wrong-cwd fold preserved: both branches miss, the resolution never raises."""
    monkeypatch.chdir(tmp_path)
    resolved = resolve("web/templates", "templates")
    assert not Path(resolved).exists()


def test_sitting_serves_first_pair_server_side(client: TestClient) -> None:
    """The sitting page renders the question, the marked cards, the declared buttons."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    response = client.get(f"/runs/{_RUN_ID}")
    assert response.status_code == 200
    assert "Which matters more?" in response.text
    assert 'id="pair-region"' in response.text
    assert "one" in response.text
    assert "two" in response.text
    assert 'slot="header">A<' in response.text
    assert 'value="prefer-a"' in response.text
    assert f'hx-post="/ui/runs/{_RUN_ID}/vote"' in response.text
    assert "count" not in response.text
    assert "/state" not in response.text
    assert "tally" not in response.text


def test_sitting_done_redirects(client: TestClient) -> None:
    """The exhausted run's sitting redirects to the done page (the DONE state read)."""
    client.post(_RUNS, json={"items": _TWO_ITEMS, **_OPERATOR})
    client.post(f"/runs/{_RUN_ID}/votes", json={"pair": ["a", "b"], "winner": "prefer-a", **_VOTE})
    response = client.get(f"/runs/{_RUN_ID}")
    assert response.status_code == 200
    assert response.headers["hx-redirect"] == f"/runs/{_RUN_ID}/done"


def test_sitting_unknown_run_404(client: TestClient) -> None:
    """The unknown stem renders the unknown-run page at the honest 404, the wire's found."""
    response = client.get("/runs/RUN-9999")
    assert response.status_code == 404
    assert "Unknown run." in response.text
    assert "RUN-9999" in response.text
    assert 'data-pt-path="/runs/{stem}"' in response.text


def test_done_page_states_coverage(client: TestClient) -> None:
    """The done page renders the DONE body's expected VERBATIM + the result link."""
    client.post(_RUNS, json={"items": _TWO_ITEMS, **_OPERATOR})
    client.post(f"/runs/{_RUN_ID}/votes", json={"pair": ["a", "b"], "winner": "prefer-a", **_VOTE})
    response = client.get(f"/runs/{_RUN_ID}/done")
    assert response.status_code == 200
    assert "all 1 scheduled pairs at quorum k=1" in response.text
    assert f'href="/runs/{_RUN_ID}/result"' in response.text


def test_done_reopened_redirects(client: TestClient) -> None:
    """A pair body at the done page redirects back to the sitting (the re-opened edge)."""
    client.post(_RUNS, json={"items": _TWO_ITEMS, **_OPERATOR})
    response = client.get(f"/runs/{_RUN_ID}/done")
    assert response.status_code == 200
    assert response.headers["hx-redirect"] == f"/runs/{_RUN_ID}"


def test_progress_serves_the_strip(client: TestClient) -> None:
    """The progress page serves the state strip with the 5s poll armed."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    response = client.get(f"/runs/{_RUN_ID}/progress")
    assert response.status_code == 200
    assert 'id="state-strip"' in response.text
    assert f'hx-get="/ui/runs/{_RUN_ID}/state"' in response.text
    assert 'hx-trigger="every 5s"' in response.text


def test_result_ranks_the_whole(client: TestClient) -> None:
    """The full-coverage result renders the ranked whole: labels, the version, the table."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    for pair in (("a", "b"), ("a", "c"), ("b", "c")):
        client.post(f"/runs/{_RUN_ID}/votes", json={"pair": list(pair), "winner": "prefer-a", **_VOTE})
    response = client.get(f"/runs/{_RUN_ID}/result")
    assert response.status_code == 200
    assert "one" in response.text
    assert "three" in response.text
    assert "win-rate-v1" in response.text
    assert "<table" in response.text


def test_result_safe_halt_409(client: TestClient) -> None:
    """The under-covered result renders the safe halt at the HONEST 409, fields verbatim."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    client.post(f"/runs/{_RUN_ID}/votes", json={"pair": ["a", "b"], "winner": "prefer-a", **_VOTE})
    response = client.get(f"/runs/{_RUN_ID}/result")
    assert response.status_code == 409
    assert "at quorum" in response.text
    assert "Resume the sitting" in response.text
    assert f'href="/runs/{_RUN_ID}/progress"' in response.text


def test_register_fragment_ack(client: TestClient) -> None:
    """The register fragment's 201 renders the ack: the run id, the copy affordance, the link."""
    response = client.post(
        "/ui/register",
        data={
            "operator_id": "op-1",
            "question": "Which matters more?",
            "quorum": "1",
            "item-id": ["a", "b"],
            "item-label": ["one", "two"],
        },
    )
    assert response.status_code == 200
    assert _RUN_ID in response.text
    assert "BEGIN THE SITTING" in response.text
    assert f'href="/runs/{_RUN_ID}"' in response.text
    assert "<pt-copy" in response.text
    assert "share this sitting URL" not in response.text


def test_register_fragment_share_at_quorum_2(client: TestClient) -> None:
    """Quorum>1 emphasizes the share copy with the form's own quorum."""
    response = client.post(
        "/ui/register",
        data={
            "operator_id": "op-1",
            "question": "Which matters more?",
            "quorum": "2",
            "item-id": ["a", "b"],
            "item-label": ["one", "two"],
        },
    )
    assert response.status_code == 200
    assert "share this sitting URL" in response.text
    assert "Each pair needs 2 judgments" in response.text


def test_register_refusal_inline_at_200(client: TestClient) -> None:
    """The <2-items refusal renders inline at 200 — the wire's three fields, labeled."""
    response = client.post(
        "/ui/register",
        data={
            "operator_id": "op-1",
            "question": "Which matters more?",
            "quorum": "1",
            "item-id": ["a"],
            "item-label": ["one"],
        },
    )
    assert response.status_code == 200
    assert "Expected" in response.text
    assert "Found" in response.text
    assert "Next action" in response.text


def test_register_refusal_bad_quorum(client: TestClient) -> None:
    """A non-numeric quorum renders the controller's family-grammar refusal inline at 200."""
    response = client.post(
        "/ui/register",
        data={
            "operator_id": "op-1",
            "question": "Which matters more?",
            "quorum": "two",
            "item-id": ["a", "b"],
            "item-label": ["one", "two"],
        },
    )
    assert response.status_code == 200
    assert "the quorum field a whole number 1 or greater" in response.text


def test_vote_then_pair_chain(client: TestClient) -> None:
    """The vote ack restates in item-label terms, chains to the pair, no echo on the fresh cast."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    response = client.post(f"/ui/runs/{_RUN_ID}/vote", data=_FORM_VOTE)
    assert response.status_code == 200
    assert "You preferred one (A) over two (B)." in response.text
    assert "already recorded with the same answer" not in response.text
    assert f'hx-get="/ui/runs/{_RUN_ID}/pair"' in response.text
    assert 'hx-trigger="load"' in response.text
    assert 'hx-target="#pair-region"' in response.text
    assert "count" not in response.text
    served = client.get(f"/ui/runs/{_RUN_ID}/pair")
    assert served.status_code == 200
    assert 'id="pair-region"' in served.text


def test_vote_echo_already_recorded(client: TestClient) -> None:
    """The byte-identical re-send renders the idempotent echo in words."""
    client.post(_RUNS, json={"items": _TWO_ITEMS, **_OPERATOR})
    fresh = client.post(f"/ui/runs/{_RUN_ID}/vote", data=_FORM_VOTE)
    assert fresh.status_code == 200
    assert "already recorded with the same answer" not in fresh.text
    again = client.post(f"/ui/runs/{_RUN_ID}/vote", data=_FORM_VOTE)
    assert again.status_code == 200
    assert "already recorded with the same answer" in again.text


def test_vote_refusal_pair_untouched(client: TestClient) -> None:
    """The out-of-set verdict renders the inline refusal at 200 — the pair region absent."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    response = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "winner": "bogus-winner"},
    )
    assert response.status_code == 200
    assert "Expected" in response.text
    assert "bogus-winner" in response.text
    assert 'id="pair-region"' not in response.text


def test_pair_fragment_done_redirects(client: TestClient) -> None:
    """The exhausted pair fragment answers 200 with the HX-Redirect response header."""
    client.post(_RUNS, json={"items": _TWO_ITEMS, **_OPERATOR})
    client.post(f"/runs/{_RUN_ID}/votes", json={"pair": ["a", "b"], "winner": "prefer-a", **_VOTE})
    response = client.get(f"/ui/runs/{_RUN_ID}/pair")
    assert response.status_code == 200
    assert response.headers["hx-redirect"] == f"/runs/{_RUN_ID}/done"


def test_pair_fragment_refuses_unknown_run(client: TestClient) -> None:
    """The unknown stem's pair fragment renders the refusal at 200."""
    response = client.get("/ui/runs/RUN-9999/pair")
    assert response.status_code == 200
    assert "Expected" in response.text
    assert "RUN-9999" in response.text


def test_state_strip_serves(client: TestClient) -> None:
    """The state strip serves the census verbatim, the poll re-armed."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    response = client.get(f"/ui/runs/{_RUN_ID}/state")
    assert response.status_code == 200
    assert 'hx-trigger="every 5s"' in response.text
    assert "a: 0" in response.text


def test_fold_fragment_500_envelope() -> None:
    """A crashing seam verb renders the fold fragment at 200 — the envelope's fields seen."""

    class _BoomSeam:
        """The stub seam — serve raises; the fold's forced input, zero scaffolding."""

        def serve(self, _run_id: str, _seed: int | None = None) -> tuple[str, str, int]:
            """Raise the boom — the crash the fold renders."""
            msg = "boom"
            raise RuntimeError(msg)

    app.state.seam = _BoomSeam()
    crashed = TestClient(app)
    response = crashed.get(f"/ui/runs/{_RUN_ID}/pair")
    assert response.status_code == 200
    assert "RuntimeError: boom" in response.text
    assert "check the server logs" in response.text
