# Copyright (C) 2026 Mark Losey. All rights reserved.
"""test_web_face — the mounted web tier's falsification set, in-process.

The web unit's test surface (web-brief §6.1 + servingtierintegrationspec
§7b, the grown nine): the mounted app under the injection fixture — the
SAME app now carries the mount; the child's controllers call the service
through the in-process client and the service reads the PARENT's
state.seam (the fixture's injection) — the isolation extends to the web
tier whole (store-as-parameter; no env, no CWD games — the resolver arcs
alone chdir, by pytest's own monkeypatch fixture with its guaranteed
restore: the CWD IS the resolution's own input). The fixture's auth-off
member (app.state.auth = "off"): the standing arcs ride the degrade —
their request bytes byte-standing, the suite green with NO key store; the
auth-on arcs overwrite the state per test (the seam's own law).
The arcs: the page arcs (landing, sitting, done, progress, result
200/409/404); the fragment arcs (register 201/422/bad-quorum, the two-step
chain, the idempotent echo, the HX-Redirect, the 422 pair-untouched, the
state strip, the fold fragment); the CSRF arcs (the token minted in the
three render contexts; the valid token's register + vote; the drive-by
refused — the write never lands; the mismatched token; the stale secret's
re-render cure); the auth-lane arcs (the 401 page — the service's mint
verbatim, never the fold; the 403 scope page; the tier key riding the
client's default header — the key never rendered; the auth-off bare
calls); the static pair (the chrome's app.css +
app.js — the 200s pinned, a mis-named home fails loudly); the resolver arcs (the loader
seam's ordered resolution: the CWD's copy first, the package's the
fallback, the fold preserved at a wrong cwd); the no-anchoring
pins (byte-level: no sitting-context response carries the count; the
sitting surface never links state/tally). The S101/PLR2004 tests ruling
stands.

Provenance: web-brief §6.1, servingtierintegrationspec §7b (the grown
arcs' fence), packet build/serving-tier-integration step 9 of 9, route
prioritree-auth, 2026-11-24 session.
"""

from __future__ import annotations

import re
from pathlib import Path

import httpx2
import pytest
from fastapi.testclient import TestClient

from prioritree import web
from prioritree.key_store import KeyStore
from prioritree.key_verify import AUTH_HEADER_DEFAULT
from prioritree.service import ESCALATION, app
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
# The CSRF + tier-key vocabulary (servingtierintegrationspec §7b — the
# wire's own literals carried 1:1): the register form's posted fields,
# the six-token grant whole, the in-process client's base URL (the
# transport-ignored literal the child's own module constant carries),
# and the keys file's name.
_REGISTER_FORM = {
    "operator_id": "op-1",
    "question": "Which matters more?",
    "quorum": "1",
    "item-id": ["a", "b"],
    "item-label": ["one", "two"],
}
_ALL_SCOPES = ("register", "next", "cast", "state", "tally", "manifest")
_SERVICE_BASE = "http://prioritree.internal"
_KEYS_FILE = "keys.jsonl"


@pytest.fixture
def client(tmp_path: Path) -> TestClient:
    """Isolate the seam by injection — the mounted whole under the face fixture's own form.

    The auth-off member (servingtierintegrationspec §7b): app.state.auth =
    "off" — the standing arcs ride the degrade, their request bytes
    byte-standing, the suite green with NO key store; the auth-on arcs
    overwrite the state per test (the seam's own law).
    """
    app.state.seam = Serialize(tmp_path)
    app.state.auth = "off"
    return TestClient(app)


def _scrape_csrf(page: str) -> str:
    """Read the served page's minted csrf_token — the form's own carrier, scraped verbatim.

    Purpose: the fence's per-arc form (servingtierintegrationspec §7b —
    the standing arcs' token scraped per arc): the served page's hidden
    input read from the rendered bytes; the assert IS the presence claim
    (the token a render-context law, its absence a test bug).
    Refuses when: never — the assert IS the scrape's own gate.
    Re-run: deterministic — the same page yields the same token.
    Touches: nothing — a pure read over the response's text.
    Provenance: servingtierintegrationspec §7b (the token growth),
    G-SERVING-TIER-INTEGRATION-BRIEF.
    """
    match = re.search(r'name="csrf_token" value="([^"]+)"', page)
    assert match is not None
    return match.group(1)


def _gated_client(key: str) -> httpx2.AsyncClient:
    """Build the child's client form with the key riding the default header — the tier-key double.

    Purpose: the auth-lane arcs' monkeypatch target
    (servingtierintegrationspec §7b arcs 6-8): a fresh AsyncClient over
    the SAME in-process ASGITransport (the imported service app,
    raise_app_exceptions=False — the fold's envelope returned, the
    child's own law), the key in the X-Api-Key header
    (AUTH_HEADER_DEFAULT carried 1:1); an empty key => the bare headers
    (the tier-key-unset form).
    Refuses when: never — a construction (the double IS the return).
    Re-run: deterministic — a fresh client per call.
    Touches: nothing — the transport is in-process (no socket).
    Provenance: servingtierintegrationspec §3c (the client's
    construction) + §7b (arcs 6-8), G-SERVING-TIER-INTEGRATION-BRIEF.
    """
    return httpx2.AsyncClient(
        base_url=_SERVICE_BASE,
        transport=httpx2.ASGITransport(app=app, raise_app_exceptions=False),
        headers={AUTH_HEADER_DEFAULT: key} if key else None,
    )


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
        client.post(
            f"/runs/{_RUN_ID}/votes",
            json={"pair": list(pair), "winner": "prefer-a", **_VOTE, "comparator_class": "llm"},
        )
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
    token = _scrape_csrf(client.get("/").text)
    response = client.post(
        "/ui/register",
        data={
            "operator_id": "op-1",
            "question": "Which matters more?",
            "quorum": "1",
            "item-id": ["a", "b"],
            "item-label": ["one", "two"],
            "csrf_token": token,
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
    token = _scrape_csrf(client.get("/").text)
    response = client.post(
        "/ui/register",
        data={
            "operator_id": "op-1",
            "question": "Which matters more?",
            "quorum": "2",
            "item-id": ["a", "b"],
            "item-label": ["one", "two"],
            "csrf_token": token,
        },
    )
    assert response.status_code == 200
    assert "share this sitting URL" in response.text
    assert "Each pair needs 2 judgments" in response.text


def test_register_refusal_inline_at_200(client: TestClient) -> None:
    """The <2-items refusal renders inline at 200 — the wire's three fields, labeled."""
    token = _scrape_csrf(client.get("/").text)
    response = client.post(
        "/ui/register",
        data={
            "operator_id": "op-1",
            "question": "Which matters more?",
            "quorum": "1",
            "item-id": ["a"],
            "item-label": ["one"],
            "csrf_token": token,
        },
    )
    assert response.status_code == 200
    assert "Expected" in response.text
    assert "Found" in response.text
    assert "Next action" in response.text


def test_register_refusal_bad_quorum(client: TestClient) -> None:
    """A non-numeric quorum renders the controller's family-grammar refusal inline at 200."""
    token = _scrape_csrf(client.get("/").text)
    response = client.post(
        "/ui/register",
        data={
            "operator_id": "op-1",
            "question": "Which matters more?",
            "quorum": "two",
            "item-id": ["a", "b"],
            "item-label": ["one", "two"],
            "csrf_token": token,
        },
    )
    assert response.status_code == 200
    assert "the quorum field a whole number 1 or greater" in response.text


def test_vote_then_pair_chain(client: TestClient) -> None:
    """The vote ack restates in item-label terms, chains to the pair, no echo on the fresh cast."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    token = _scrape_csrf(client.get(f"/runs/{_RUN_ID}").text)
    response = client.post(f"/ui/runs/{_RUN_ID}/vote", data={**_FORM_VOTE, "csrf_token": token})
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
    token = _scrape_csrf(client.get(f"/runs/{_RUN_ID}").text)
    fresh = client.post(f"/ui/runs/{_RUN_ID}/vote", data={**_FORM_VOTE, "csrf_token": token})
    assert fresh.status_code == 200
    assert "already recorded with the same answer" not in fresh.text
    again = client.post(f"/ui/runs/{_RUN_ID}/vote", data={**_FORM_VOTE, "csrf_token": token})
    assert again.status_code == 200
    assert "already recorded with the same answer" in again.text


def test_vote_refusal_pair_untouched(client: TestClient) -> None:
    """The out-of-set verdict renders the inline refusal at 200 — the pair region absent."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    token = _scrape_csrf(client.get(f"/runs/{_RUN_ID}").text)
    response = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "winner": "bogus-winner", "csrf_token": token},
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
    app.state.auth = "off"  # the fixture-less fold arc's own degrade member — no order-coupling
    crashed = TestClient(app)
    response = crashed.get(f"/ui/runs/{_RUN_ID}/pair")
    assert response.status_code == 200
    assert "RuntimeError: boom" in response.text
    assert "check the server logs" in response.text


# The CSRF + auth-lane arcs (servingtierintegrationspec §7b — the grown
# nine; the names, the fixtures, and the asserted bytes the fence's own).


def test_csrf_token_minted_in_three_render_contexts(client: TestClient) -> None:
    """The three render contexts each carry the csrf_token hidden input — the token bound per path."""
    landing = client.get("/")
    assert 'name="csrf_token"' in landing.text
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    sitting = client.get(f"/runs/{_RUN_ID}")
    assert 'name="csrf_token"' in sitting.text
    pair_fragment = client.get(f"/ui/runs/{_RUN_ID}/pair")
    assert 'name="csrf_token"' in pair_fragment.text
    assert _scrape_csrf(landing.text) != _scrape_csrf(sitting.text)  # the per-path binding


def test_csrf_valid_token_passes_register_and_vote(client: TestClient) -> None:
    """The served token posted => register 201 the ack; the vote 200 the ack chain — the cure's happy path."""
    register_token = _scrape_csrf(client.get("/").text)
    registered = client.post("/ui/register", data={**_REGISTER_FORM, "csrf_token": register_token})
    assert registered.status_code == 200
    assert _RUN_ID in registered.text
    assert "BEGIN THE SITTING" in registered.text
    vote_token = _scrape_csrf(client.get(f"/runs/{_RUN_ID}").text)
    voted = client.post(f"/ui/runs/{_RUN_ID}/vote", data={**_FORM_VOTE, "csrf_token": vote_token})
    assert voted.status_code == 200
    assert "You preferred one (A) over two (B)." in voted.text


def test_csrf_drive_by_refused_write_never_lands(client: TestClient) -> None:
    """POST /ui/register with NO token => the refusal fragment at 200; the write never lands (the resume 404s)."""
    response = client.post("/ui/register", data={**_REGISTER_FORM})
    assert response.status_code == 200
    assert "The request was refused" in response.text
    assert "the form&#39;s csrf_token field (minted into the served page)" in response.text  # the autoescaped byte
    assert "absent-or-mismatched" in response.text
    assert "reload the page and re-send" in response.text
    assert "Something broke" not in response.text  # never the fold's clothes
    assert client.get(f"/runs/{_RUN_ID}").status_code == 404  # the write never landed


def test_csrf_mismatched_token_refused(client: TestClient) -> None:
    """A well-formed but wrong token => the SAME refusal — the compare's mismatch leg, the write never lands."""
    response = client.post("/ui/register", data={**_REGISTER_FORM, "csrf_token": "f" * 64})
    assert response.status_code == 200
    assert "absent-or-mismatched" in response.text
    assert "reload the page and re-send" in response.text
    assert client.get(f"/runs/{_RUN_ID}").status_code == 404


def test_csrf_stale_secret_refused_re_render_cures(
    client: TestClient, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A new secret refuses the stale token; the re-render mints fresh and passes — the restart price, in-process."""
    stale = _scrape_csrf(client.get("/").text)
    monkeypatch.setattr(web, "_csrf_secret", b"the-restarted-process-secret")
    refused = client.post("/ui/register", data={**_REGISTER_FORM, "csrf_token": stale})
    assert refused.status_code == 200
    assert "absent-or-mismatched" in refused.text
    fresh = _scrape_csrf(client.get("/").text)
    assert fresh != stale
    cured = client.post("/ui/register", data={**_REGISTER_FORM, "csrf_token": fresh})
    assert cured.status_code == 200
    assert _RUN_ID in cured.text


def test_web_401_page_lane_key_path_never_fold(
    client: TestClient, tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Auth on + an empty key store + the tier key unset => the sitting page renders the auth page at 401.

    The service's own next_action (the mint) verbatim — NEVER fold.html's
    ESCALATION clothes (the dedicated lane's own law).
    """
    app.state.auth = "on"
    app.state.keys = KeyStore(tmp_path / _KEYS_FILE)
    monkeypatch.setattr(web, "_client", _gated_client(""))
    response = client.get(f"/runs/{_RUN_ID}")
    assert response.status_code == 401
    assert "The service asked for a key" in response.text
    assert "the key in the X-Api-Key header" in response.text
    assert "absent-or-unknown" in response.text
    assert "mint a key: prioritree key mint" in response.text
    assert ESCALATION not in response.text


def test_web_403_page_lane_scope_path(
    client: TestClient, tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """A cast-only key at the child's client => the sitting page renders the scope path at 403."""
    app.state.auth = "on"
    store = KeyStore(tmp_path / _KEYS_FILE)
    key, _digest = store.mint("narrow-holder", "human", ("cast",), "service")
    app.state.keys = store
    monkeypatch.setattr(web, "_client", _gated_client(key))
    response = client.get(f"/runs/{_RUN_ID}")
    assert response.status_code == 403
    assert "The key lacks this act's scope" in response.text
    assert "the manifest scope" in response.text
    # Jinja's autoescape renders the apostrophes and brackets as entities — the bytes asserted as served:
    assert "the key&#39;s scopes [&#39;cast&#39;]" in response.text
    assert "--scopes &lt;csv&gt;+manifest" in response.text


def test_tier_key_rides_the_client_default_header(
    client: TestClient, tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
) -> None:
    """The six-token key on the child's client => the register fragment's ack through the gated service.

    The key ABSENT from every rendered page body — the browser never sees it.
    """
    app.state.auth = "on"
    store = KeyStore(tmp_path / _KEYS_FILE)
    key, _digest = store.mint("web-tier", "human", _ALL_SCOPES, "service")
    app.state.keys = store
    monkeypatch.setattr(web, "_client", _gated_client(key))
    token = _scrape_csrf(client.get("/").text)
    response = client.post("/ui/register", data={**_REGISTER_FORM, "csrf_token": token})
    assert response.status_code == 200
    assert _RUN_ID in response.text
    assert key not in response.text
    sitting = client.get(f"/runs/{_RUN_ID}")
    assert sitting.status_code == 200
    assert key not in sitting.text


def test_auth_off_web_calls_pass_bare(client: TestClient) -> None:
    """Auth off — no key store, no tier key: the register fragment's ack, the sitting page 200.

    The child's calls pass bare — the door's degrade short-circuits every gate.
    """
    token = _scrape_csrf(client.get("/").text)
    response = client.post("/ui/register", data={**_REGISTER_FORM, "csrf_token": token})
    assert response.status_code == 200
    assert _RUN_ID in response.text
    assert "BEGIN THE SITTING" in response.text
    sitting = client.get(f"/runs/{_RUN_ID}")
    assert sitting.status_code == 200
    assert "Which matters more?" in sitting.text
