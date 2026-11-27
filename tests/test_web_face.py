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
200/409/404 — the sitting's corroboration-aware arcs beside them: the
uncorroborated pair still SERVED, the done page rendered for the plain
browser, the deliberate lane's picker + chosen pair, either presentation;
the resume stems carrying `required` — the empty click teaches, never a
dead button);
the fragment arcs (register 201/422/bad-quorum, the two-step
chain, the chain-carry links, the deliberate stay-put at both queues,
the idempotent echo, the HX-Redirect, the 422 pair-untouched, the state
strip, the fold fragment); the CSRF arcs (the token minted in the
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

import os
import re
import subprocess
import sys
from pathlib import Path

import httpx2
import pytest
from fastapi.testclient import TestClient
from starlette.middleware.sessions import SessionMiddleware

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
# The voter-session arcs' own vocabulary (votersessionspec §4): the remember cookie's name
# and priced max_age, the correction route at this file's fixed run id, the fold's two pinned
# refusal copies (the micro-fold Ruling 2, togo 2026-11-26T19:39:09Z: the empty session's
# lapse bytes; the live session's stale-tab reload bytes), the T-form env knob names (the
# fold's Ruling 1), the strength-check arc's fixed in-source program, and the identified
# form's shape without the ask's field.
_REMEMBER_COOKIE = "remember"
_REMEMBER_MAX_AGE = 14 * 24 * 60 * 60  # 1209600 — the 14-day default, keisan's pricing
_UNREMEMBER = f"/ui/runs/{_RUN_ID}/unremember"
_LAPSE_COPY = "your identification lapsed — reload, the page re-asks your name"
_RELOAD_COPY = "reload the page and re-send — the re-render mints a fresh token"
_IMPORT_PROBE = "import prioritree.service"  # service-first — the standing import cycle resolves this order alone
_ANON_VOTE = {"item_a": "a", "item_b": "b", "winner": "prefer-a"}  # no name field — the identified form's shape


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


def _scrape_unremember_token(page: str) -> str:
    """Read the correction form's token from an IDENTIFIED render — the sitting's first csrf_token input.

    Purpose: the correction arcs' own scraper (votersessionspec §4): on the
    identified sitting the conditional renders the un-remember form BEFORE the
    pair include, so the page's FIRST csrf_token input is the correction lane's
    own mint — the vote lanes' tokens scraped from the pair fragment instead
    (its page carries the one token).
    Refuses when: never — the assert IS the scrape's own gate (an identified
    page without the correction token a test bug, never a value).
    Re-run: deterministic — the same page yields the same token.
    Touches: nothing — a pure read over the response's text.
    Provenance: votersessionspec §4 (the correction arcs), togo's fold Ruling 2,
    G-VOTERSESSIONSPEC-BRIEF.
    """
    matches = re.findall(r'name="csrf_token" value="([^"]+)"', page)
    assert matches
    return matches[0]


def _identified(client: TestClient) -> httpx2.Response:
    """Register a three-pair run and identify this browser — the identify-once act, the jar armed.

    Purpose: the session arcs' shared setup (votersessionspec §4): the register
    through the service lane (NO session write), then the identifying vote —
    the body's comparator_id the identifying act, the epoch minted, the cookie
    landed in httpx2's native jar automatically; the returned response the
    identifying POST's own (the cookie arcs read its headers).
    Refuses when: never — a setup (the assert is the act's own gate).
    Re-run: deterministic — a fresh run id per store.
    Touches: the run file through the service (the register + the vote).
    Provenance: votersessionspec §2e/§4, G-VOTERSESSIONSPEC-BRIEF.
    """
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    token = _scrape_csrf(client.get(f"/runs/{_RUN_ID}").text)
    identified = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "comparator_id": "mark", "csrf_token": token},
    )
    assert identified.status_code == 200
    return identified


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


def test_resume_stems_carry_required(client: TestClient) -> None:
    """The three rendered resume stems carry `required` — the empty click teaches, never a dead button."""
    landing = client.get("/")
    unknown = client.get("/runs/RUN-9999")
    assert landing.status_code == 200
    assert unknown.status_code == 404
    assert landing.text.count('<input name="stem" required placeholder="RUN-0001">') == 2
    assert '<input name="stem" required placeholder="RUN-0001">' in unknown.text


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


def test_sitting_done_renders_the_done_page(client: TestClient) -> None:
    """The done run's sitting renders the done page for the plain browser — no bare HX-Redirect."""
    client.post(_RUNS, json={"items": _TWO_ITEMS, **_OPERATOR})
    client.post(f"/runs/{_RUN_ID}/votes", json={"pair": ["a", "b"], "winner": "prefer-a", **_VOTE})
    client.post(
        f"/runs/{_RUN_ID}/votes",
        json={"pair": ["a", "b"], "winner": "prefer-a", **_VOTE, "comparator_class": "llm"},
    )
    response = client.get(f"/runs/{_RUN_ID}")
    assert response.status_code == 200
    assert "hx-redirect" not in response.headers
    assert "The sitting is complete." in response.text
    assert "corroborated" in response.text
    assert f'href="/runs/{_RUN_ID}/result"' in response.text
    assert f'href="/runs/{_RUN_ID}/pairs"' in response.text


def test_sitting_unknown_run_404(client: TestClient) -> None:
    """The unknown stem renders the unknown-run page at the honest 404, the wire's found."""
    response = client.get("/runs/RUN-9999")
    assert response.status_code == 404
    assert "Unknown run." in response.text
    assert "RUN-9999" in response.text
    assert 'data-pt-path="/runs/{stem}"' in response.text


def test_done_page_states_coverage(client: TestClient) -> None:
    """The done page renders the DONE body's expected VERBATIM + the tally's and the deliberate lane's links."""
    client.post(_RUNS, json={"items": _TWO_ITEMS, **_OPERATOR})
    client.post(f"/runs/{_RUN_ID}/votes", json={"pair": ["a", "b"], "winner": "prefer-a", **_VOTE})
    client.post(
        f"/runs/{_RUN_ID}/votes",
        json={"pair": ["a", "b"], "winner": "prefer-a", **_VOTE, "comparator_class": "llm"},
    )
    response = client.get(f"/runs/{_RUN_ID}/done")
    assert response.status_code == 200
    assert "all 1 scheduled pairs at quorum k=1 AND corroborated" in response.text
    assert "&gt;=1 human AND &gt;=1 llm per pair" in response.text  # Jinja's autoescape — the bytes as served
    assert f'href="/runs/{_RUN_ID}/result"' in response.text
    assert f'href="/runs/{_RUN_ID}/pairs"' in response.text


def test_done_reopened_redirects(client: TestClient) -> None:
    """A pair body at the done page redirects back to the sitting (the re-opened edge — the true 302, unfollowed)."""
    client.post(_RUNS, json={"items": _TWO_ITEMS, **_OPERATOR})
    response = client.get(f"/runs/{_RUN_ID}/done", follow_redirects=False)
    assert response.status_code == 302
    assert response.headers["location"] == f"/runs/{_RUN_ID}"


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


# The lane-separation set (donedetourspec §4 — the done-detour's four arcs: the
# chain lane's carry links + the deliberate lane's stay-put at both queues, the
# sitting lane's fetch proof byte-standing above; the fragment route never
# called at the deliberate lane — the done bounce dead).


def test_vote_chain_carry_next_pair(client: TestClient) -> None:
    """The chain vote's ack links the head's judge URL — the P-token dropped, the swap knob carried, no fetch div."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    # The card's first pair — the chain form carries BOTH conditional fields (the chain first, the datum second).
    card = client.get(f"/runs/{_RUN_ID}/pair?item_a=a&item_b=b&chain=P02,P03")
    assert 'name="chain" value="P02,P03"' in card.text
    assert 'name="deliberate" value="true"' in card.text
    token = _scrape_csrf(card.text)
    first = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "chain": "P02,P03", "deliberate": "true", "csrf_token": token},
    )
    assert first.status_code == 200
    assert "You preferred one (A) over two (B)." in first.text
    # The head's judge URL (P02 = (a, c)) — the chain riding the URL, the served bytes autoescaped.
    assert f'href="/runs/{_RUN_ID}/pair?item_a=a&amp;item_b=c&amp;chain=P02,P03"' in first.text
    assert "next-pair" in first.text
    assert 'hx-get="/ui/runs' not in first.text  # the chain lane never fetches
    assert f'href="/runs/{_RUN_ID}/pairs"' not in first.text  # the datum read and discarded at the chain lane
    # The second hop at the swapped presentation (a second TestClient IS a second browser — its own empty jar).
    browser_b = TestClient(app)
    swapped = browser_b.get(f"/runs/{_RUN_ID}/pair?item_a=a&item_b=c&swap=true&chain=P02,P03")
    assert 'name="item_a" value="c"' in swapped.text  # the presented pair swapped at the head's page
    hop_token = _scrape_csrf(swapped.text)
    second = browser_b.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={
            **_FORM_VOTE,
            "item_a": "c",
            "item_b": "a",
            "presentation_order": "swapped",
            "comparator_id": "y",
            "chain": "P02,P03",
            "deliberate": "true",
            "csrf_token": hop_token,
        },
    )
    assert second.status_code == 200
    assert "You preferred three (A) over one (B)." in second.text
    # The just-voted P02 dropped — the shrunken chain riding the head's URL, the swap knob carried.
    assert f'href="/runs/{_RUN_ID}/pair?item_a=b&amp;item_b=c&amp;swap=true&amp;chain=P03"' in second.text
    assert 'hx-get="/ui/runs' not in second.text


def test_vote_chain_carry_done_link(client: TestClient) -> None:
    """The chain's empty rest renders the done link + the list-ended teaching — no fetch div at the chain lane."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    # The card's last hop — the chain carrying the just-voted token alone (P03 = (b, c)).
    token = _scrape_csrf(client.get(f"/runs/{_RUN_ID}/pair?item_a=b&item_b=c&chain=P03").text)
    response = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "item_a": "b", "item_b": "c", "chain": "P03", "deliberate": "true", "csrf_token": token},
    )
    assert response.status_code == 200
    assert "You preferred two (A) over three (B)." in response.text
    assert "the list has ended" in response.text  # the list-ended teaching
    assert f'href="/runs/{_RUN_ID}/done"' in response.text
    assert 'hx-get="/ui/runs' not in response.text  # NO fetch div — the chain lane never fetches
    assert "next-pair" not in response.text  # the rest empty — no head link
    assert f'href="/runs/{_RUN_ID}/pairs"' not in response.text  # the datum discarded


def test_deliberate_vote_stays_put(client: TestClient) -> None:
    """The bare deliberate vote stays put — the confirmation + both links; the re-cast echoes at the same form."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    # The picker-sourced judge page — the datum carried by the hidden field, the chain absent.
    judge = client.get(f"/runs/{_RUN_ID}/pair?item_a=a&item_b=b")
    assert 'name="deliberate" value="true"' in judge.text
    assert 'name="chain"' not in judge.text
    token = _scrape_csrf(judge.text)
    response = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "deliberate": "true", "csrf_token": token},
    )
    assert response.status_code == 200
    assert "You preferred one (A) over two (B)." in response.text  # the confirmation standing
    assert "Recorded. Judge the next pair from the picker, or close out the sitting at the done page." in response.text
    assert f'href="/runs/{_RUN_ID}/pairs"' in response.text  # BOTH links, their exact forms
    assert f'href="/runs/{_RUN_ID}/done"' in response.text
    assert 'hx-get="/ui/runs' not in response.text  # NO fetch div — the fragment never called
    assert "hx-redirect" not in response.headers  # NO redirect — the ack stays put
    assert "next-pair" not in response.text  # the chain arm not taken (no chain carried)
    assert "the list has ended" not in response.text  # the done_url arm not taken
    # The idempotent re-cast — the acknowledged echo at the SAME stay-put form (the identified state's token law).
    again_token = _scrape_csrf(client.get(f"/ui/runs/{_RUN_ID}/pair").text)
    again = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "deliberate": "true", "csrf_token": again_token},
    )
    assert again.status_code == 200
    assert "already recorded with the same answer" in again.text
    assert f'href="/runs/{_RUN_ID}/pairs"' in again.text  # the stay-put form held at the echo
    assert f'href="/runs/{_RUN_ID}/done"' in again.text
    assert 'hx-get="/ui/runs' not in again.text
    assert "hx-redirect" not in again.headers


def test_deliberate_vote_stays_put_at_the_done_queue(client: TestClient) -> None:
    """The deliberate vote at the fully-corroborated run stays put — the bounce dead, no HX-Redirect on the POST."""
    client.post(_RUNS, json={"items": _TWO_ITEMS, **_OPERATOR})
    # The exhausted queue composed exactly as the HX-Redirect arc sets its state — the human + the llm votes.
    client.post(f"/runs/{_RUN_ID}/votes", json={"pair": ["a", "b"], "winner": "prefer-a", **_VOTE})
    client.post(
        f"/runs/{_RUN_ID}/votes",
        json={"pair": ["a", "b"], "winner": "prefer-a", **_VOTE, "comparator_class": "llm"},
    )
    token = _scrape_csrf(client.get(f"/runs/{_RUN_ID}/pair?item_a=a&item_b=b").text)
    response = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "deliberate": "true", "csrf_token": token},
    )
    assert response.status_code == 200
    assert "You preferred alpha (A) over bravo (B)." in response.text  # the confirmation standing
    assert "already recorded with the same answer" in response.text  # the pre-seeded judge's re-send
    assert "Recorded. Judge the next pair from the picker, or close out the sitting at the done page." in response.text
    assert f'href="/runs/{_RUN_ID}/pairs"' in response.text  # BOTH links at the exhausted queue
    assert f'href="/runs/{_RUN_ID}/done"' in response.text
    assert 'hx-get="/ui/runs' not in response.text  # the fetch div dead — the fragment never called
    assert "hx-redirect" not in response.headers  # THE BOUNCE DEAD — the POST's own response never redirects


def test_vote_echo_already_recorded(client: TestClient) -> None:
    """The byte-identical re-send renders the idempotent echo in words."""
    client.post(_RUNS, json={"items": _TWO_ITEMS, **_OPERATOR})
    token = _scrape_csrf(client.get(f"/runs/{_RUN_ID}").text)
    fresh = client.post(f"/ui/runs/{_RUN_ID}/vote", data={**_FORM_VOTE, "csrf_token": token})
    assert fresh.status_code == 200
    assert "already recorded with the same answer" not in fresh.text
    # §2e's note: the identifying POST minted the epoch, so the page's path-bound token is
    # stale AFTER the identification — the browser's own token source is the chain's fresh
    # fragment (epoch-bound); the second POST's token scraped per the session's law.
    again_token = _scrape_csrf(client.get(f"/ui/runs/{_RUN_ID}/pair").text)
    again = client.post(f"/ui/runs/{_RUN_ID}/vote", data={**_FORM_VOTE, "csrf_token": again_token})
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
    """The exhausted pair fragment answers 200 with the HX-Redirect response header (the HTMX lane intact)."""
    client.post(_RUNS, json={"items": _TWO_ITEMS, **_OPERATOR})
    client.post(f"/runs/{_RUN_ID}/votes", json={"pair": ["a", "b"], "winner": "prefer-a", **_VOTE})
    client.post(
        f"/runs/{_RUN_ID}/votes",
        json={"pair": ["a", "b"], "winner": "prefer-a", **_VOTE, "comparator_class": "llm"},
    )
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
    # the fold's Ruling 2 re-derived pin: the anonymous drive-by is the EMPTY-session case —
    # the LAPSE copy, never the stale-tab reload copy (the micro-fold, togo 2026-11-26T19:39:09Z).
    assert "your identification lapsed — reload, the page re-asks your name" in response.text
    assert "Something broke" not in response.text  # never the fold's clothes
    assert client.get(f"/runs/{_RUN_ID}").status_code == 404  # the write never landed


def test_csrf_mismatched_token_refused(client: TestClient) -> None:
    """A well-formed but wrong token => the SAME refusal — the compare's mismatch leg, the write never lands."""
    response = client.post("/ui/register", data={**_REGISTER_FORM, "csrf_token": "f" * 64})
    assert response.status_code == 200
    assert "absent-or-mismatched" in response.text
    # the fold's Ruling 2 re-derived pin (the mismatch leg — the same empty-session copy).
    assert "your identification lapsed — reload, the page re-asks your name" in response.text
    assert client.get(f"/runs/{_RUN_ID}").status_code == 404


def test_csrf_stale_secret_refused_re_render_cures(
    client: TestClient,
    monkeypatch: pytest.MonkeyPatch,
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
    client: TestClient,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
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
    client: TestClient,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
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
    client: TestClient,
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
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


def test_sitting_swap_presents_swapped(client: TestClient) -> None:
    """The sitting at ?swap=true renders the presented pair swapped, the hidden field carrying the token."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    response = client.get(f"/runs/{_RUN_ID}?swap=true")
    assert response.status_code == 200
    # The hidden fields carry the SERVED pair (b first) and the token; card A = the first-presented.
    assert 'name="item_a" value="b"' in response.text
    assert 'name="item_b" value="a"' in response.text
    assert 'name="presentation_order" value="swapped"' in response.text


def test_vote_swapped_hidden_field_resends(client: TestClient) -> None:
    """The swapped sitting's vote re-sends the hidden token — the cast lands, the ack chains the swap carry."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    token = _scrape_csrf(client.get(f"/runs/{_RUN_ID}?swap=true").text)
    response = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={
            **_FORM_VOTE,
            "item_a": "b",
            "item_b": "a",
            "presentation_order": "swapped",
            "csrf_token": token,
        },
    )
    assert response.status_code == 200
    # The ack restates in the PRESENTED labels — the first-presented (b's label) preferred.
    assert "You preferred two (A) over one (B)." in response.text
    # The ack chain carries the swap — the fragment's fetch re-presents swapped.
    assert f'hx-get="/ui/runs/{_RUN_ID}/pair?swap=true"' in response.text


def test_sitting_uncorroborated_still_serves(client: TestClient) -> None:
    """The at-quorum-but-uncorroborated pair stays SERVED — the sitting renders the card, never the done page."""
    client.post(_RUNS, json={"items": _TWO_ITEMS, **_OPERATOR})
    client.post(f"/runs/{_RUN_ID}/votes", json={"pair": ["a", "b"], "winner": "prefer-a", **_VOTE})
    response = client.get(f"/runs/{_RUN_ID}")
    assert response.status_code == 200
    assert 'id="pair-region"' in response.text
    assert "The sitting is complete." not in response.text


def test_sitting_lists_the_pair_picker(client: TestClient) -> None:
    """The sitting page carries the deliberate lane's picker: every scheduled pair, both presentations' links."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    response = client.get(f"/runs/{_RUN_ID}")
    assert response.status_code == 200
    assert 'id="pair-picker"' in response.text
    # the three-pair universe whole, each pair openable in EITHER presentation (6 links)
    assert response.text.count('href="/runs/RUN-0001/pair?item_a=') == 6
    assert 'href="/runs/RUN-0001/pair?item_a=a&item_b=b"' in response.text
    assert 'href="/runs/RUN-0001/pair?item_a=a&item_b=b&swap=true"' in response.text
    assert 'href="/runs/RUN-0001/pair?item_a=b&item_b=c&swap=true"' in response.text


def test_picker_page_lists_the_pairs(client: TestClient) -> None:
    """The deliberate lane's picker page serves the list at any coverage point — the done page's link target."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    response = client.get(f"/runs/{_RUN_ID}/pairs")
    assert response.status_code == 200
    assert 'id="pair-picker"' in response.text
    assert response.text.count('href="/runs/RUN-0001/pair?item_a=') == 6
    assert 'href="/runs/RUN-0001/pair?item_a=b&item_b=c"' in response.text
    assert f'href="/runs/{_RUN_ID}"' in response.text  # the back-to-the-sitting link


def test_deliberate_pair_card_either_presentation(client: TestClient) -> None:
    """The picked pair's page re-uses the existing card + cast form, in the chosen presentation."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    canonical = client.get(f"/runs/{_RUN_ID}/pair?item_a=b&item_b=c")
    assert canonical.status_code == 200
    assert 'id="pair-region"' in canonical.text
    assert 'name="item_a" value="b"' in canonical.text
    assert 'name="item_b" value="c"' in canonical.text
    assert 'name="presentation_order" value="canonical"' in canonical.text
    swapped = client.get(f"/runs/{_RUN_ID}/pair?item_a=b&item_b=c&swap=true")
    assert swapped.status_code == 200
    assert 'name="item_a" value="c"' in swapped.text
    assert 'name="item_b" value="b"' in swapped.text
    assert 'name="presentation_order" value="swapped"' in swapped.text
    assert "three" in swapped.text  # the first-presented label (c = three)


def test_deliberate_vote_lands_stamped_and_mapped(client: TestClient) -> None:
    """The deliberate vote rides the unchanged door — the swapped citation mapped, the classes corroborating."""
    client.post(_RUNS, json={"items": _TWO_ITEMS, **_OPERATOR})
    token = _scrape_csrf(client.get(f"/runs/{_RUN_ID}/pair?item_a=a&item_b=b&swap=true").text)
    deliberate = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={
            "item_a": "b",
            "item_b": "a",
            "winner": "prefer-a",
            "presentation_order": "swapped",
            **_VOTE,
            "csrf_token": token,
        },
    )
    assert deliberate.status_code == 200
    # the ack restates in the PRESENTED labels — the first-presented (b = bravo) preferred.
    assert "You preferred bravo (A) over alpha (B)." in deliberate.text
    corroborating = client.post(
        f"/runs/{_RUN_ID}/votes",
        json={"pair": ["a", "b"], "winner": "prefer-b", "comparator_id": "y", "comparator_class": "llm"},
    )
    assert corroborating.status_code == 200
    tally = client.get(f"/runs/{_RUN_ID}/tally")
    assert tally.status_code == 200
    # the deliberate swapped vote mapped canonical (prefer-a on the presented (b, a) = b's win) + the llm's prefer-b
    assert tally.json()["ranked_groups"] == [["b"], ["a"]]
    assert tally.json()["coverage"]["pair_class_counts"] == {"a|b": {"human": 1, "llm": 1}}


# The voter-session arcs (votersessionspec §4 — the 23; the fold's Ruling 1 T-form env
# names + Ruling 2's re-derived lapse pins carried, the echo arc's second-token cure
# landed above). The S101/PLR2004 tests ruling stands; the strength-check arc's
# subprocess rides the S603/S607 ruling at pyproject.


def test_remember_cookie_lands_in_the_jar(client: TestClient) -> None:
    """The identifying vote's response carries Set-Cookie — the jar holds 'remember', the attributes pinned."""
    identified = _identified(client)
    assert client.cookies.get(_REMEMBER_COOKIE) is not None
    set_cookie = "; ".join(identified.headers.get_list("set-cookie")).lower()
    assert "httponly" in set_cookie  # the engine's hardwired flag (sessions.py:34 — never a knob)
    assert "samesite=lax" in set_cookie  # the shareable URL's top-level entry preserved


def test_remember_max_age_fourteen_days(client: TestClient) -> None:
    """The cookie's own Max-Age attribute pinned at 1209600 — the 14-day default, keisan's priced floor."""
    identified = _identified(client)
    set_cookie = "; ".join(identified.headers.get_list("set-cookie")).lower()
    assert f"max-age={_REMEMBER_MAX_AGE}" in set_cookie


def test_anonymous_get_never_mints(client: TestClient) -> None:
    """The anonymous landing, sitting, and pair fragment GETs carry no Set-Cookie — nothing to fixate pre-identify."""
    landing = client.get("/")
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    sitting = client.get(f"/runs/{_RUN_ID}")
    fragment = client.get(f"/ui/runs/{_RUN_ID}/pair")
    for response in (landing, sitting, fragment):
        assert "set-cookie" not in response.headers


def test_service_lanes_never_see_a_session(client: TestClient) -> None:
    """The service app's middleware stack carries no SessionMiddleware; its lanes set no cookie."""
    assert not any(middleware.cls is SessionMiddleware for middleware in app.user_middleware)
    client.post(_RUNS, json={"items": _TWO_ITEMS, **_OPERATOR})
    pair = client.get(f"/runs/{_RUN_ID}/next")
    assert pair.status_code == 200
    assert "set-cookie" not in pair.headers


def test_underfloor_secret_refuses_at_import() -> None:
    """An under-floor env secret at either knob refuses the web tier's import — the ThreePart bytes carried."""
    for env_name in ("PRIORITYTREE_WEB_REMEMBER_SECRET", "PRIORITYTREE_WEB_CSRF_SECRET"):  # the T-form (Ruling 1)
        env = {**os.environ, env_name: "short"}
        probe = subprocess.run(  # the S603/S607 ruled form — fixed argv, never a shell
            [sys.executable, "-c", _IMPORT_PROBE],
            capture_output=True,
            env=env,
            check=False,
        )
        assert probe.returncode != 0
        stderr = probe.stderr.decode()
        expected = f"expected: the {env_name} env secret 32 bytes (256 bits) or longer, or unset for the boot-mint"
        assert expected in stderr
        assert "found: 5 bytes" in stderr
        assert f"next_action: set {env_name} to a 256-bit secret" in stderr


def test_first_vote_asks_once_then_carried(client: TestClient) -> None:
    """The anonymous sitting renders the ask; the identifying vote mints the session; the fragment pre-stamped."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    sitting = client.get(f"/runs/{_RUN_ID}")
    assert 'name="comparator_id"' in sitting.text  # the ask served INSIDE the vote form
    assert "Your name is asked once" in sitting.text
    token = _scrape_csrf(sitting.text)
    landed = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "comparator_id": "mark", "csrf_token": token},
    )
    assert landed.status_code == 200
    assert client.cookies.get(_REMEMBER_COOKIE) is not None  # the session minted at the identification
    fragment = client.get(f"/ui/runs/{_RUN_ID}/pair")
    assert fragment.status_code == 200
    assert 'name="comparator_id"' not in fragment.text  # the ask asked ONCE — the fragment pre-stamped


def test_identifying_ack_teaches_the_reload(client: TestClient) -> None:
    """The identifying vote's ack carries the re-cast teaching — the sessioned ack does not."""
    identified = _identified(client)
    assert "To judge this pair again, reload the page first." in identified.text
    token = _scrape_csrf(client.get(f"/ui/runs/{_RUN_ID}/pair").text)
    sessioned = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={"item_a": "a", "item_b": "c", "winner": "prefer-b", "csrf_token": token},
    )
    assert sessioned.status_code == 200
    assert "To judge this pair again, reload the page first." not in sessioned.text


def test_identified_renders_carry_no_ask_both_lanes(client: TestClient) -> None:
    """The identified sitting and judge pages render pre-stamped — no comparator_id field, the identity line present."""
    _identified(client)
    sitting = client.get(f"/runs/{_RUN_ID}")
    assert 'name="comparator_id"' not in sitting.text
    assert "voting as: mark" in sitting.text
    judge = client.get(f"/runs/{_RUN_ID}/pair?item_a=b&item_b=c")
    assert 'name="comparator_id"' not in judge.text
    assert "voting as: mark" in judge.text


def test_judge_page_fresh_get_carried_identity(client: TestClient) -> None:
    """The deliberate lane's fresh GET serves the carried identity — the per-visit re-ask dead."""
    _identified(client)
    judge = client.get(f"/runs/{_RUN_ID}/pair?item_a=a&item_b=b")
    assert judge.status_code == 200
    assert "voting as: mark" in judge.text


def test_vote_reads_the_remembered_id(client: TestClient, tmp_path: Path) -> None:
    """At the auth-off degrade the record's id is the sessioned name — the body's field ignored when a session rides."""
    _identified(client)
    token = _scrape_csrf(client.get(f"/ui/runs/{_RUN_ID}/pair").text)
    second = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "comparator_id": "imposter", "csrf_token": token},
    )
    assert second.status_code == 200
    log = Serialize(tmp_path).census(_RUN_ID).vote_log
    assert len(log) == 1
    assert log[0].comparator_id == "mark"  # the sessioned name stamped — the body's claim never landed


def test_expired_session_taught_refusal_reload_recovers(client: TestClient, tmp_path: Path) -> None:
    """The jar cleared, the stale POST teaches the lapse; the write never lands; the reload recovers."""
    _identified(client)
    census_before = len(Serialize(tmp_path).census(_RUN_ID).vote_log)
    stale_token = _scrape_csrf(client.get(f"/ui/runs/{_RUN_ID}/pair").text)
    client.cookies.clear()  # the cookie died at max_age — the empty-session state
    refused = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_ANON_VOTE, "csrf_token": stale_token},  # the identified form's shape — no name field
    )
    assert refused.status_code == 200
    assert _LAPSE_COPY in refused.text  # the taught lapse, in the human's words
    assert "the schema" not in refused.text  # never the schema's words
    assert len(Serialize(tmp_path).census(_RUN_ID).vote_log) == census_before  # the write never landed
    reloaded = client.get(f"/runs/{_RUN_ID}")
    assert 'name="comparator_id"' in reloaded.text  # the reload re-renders the ask
    assert "Your name is asked once" in reloaded.text
    fresh_token = _scrape_csrf(reloaded.text)
    recovered = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "item_a": "a", "item_b": "c", "comparator_id": "mark", "csrf_token": fresh_token},
    )
    assert recovered.status_code == 200  # the re-identify + re-send lands — the one-step cure


def test_two_browsers_two_sessions(client: TestClient, tmp_path: Path) -> None:
    """Two TestClients, two names — both votes land distinct in the log, the multi-user truth at the record."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    token_a = _scrape_csrf(client.get(f"/runs/{_RUN_ID}").text)
    first = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "comparator_id": "alice", "csrf_token": token_a},
    )
    assert first.status_code == 200
    browser_b = TestClient(app)  # a second TestClient IS a second browser (its own empty jar)
    token_b = _scrape_csrf(browser_b.get(f"/runs/{_RUN_ID}").text)
    second = browser_b.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "comparator_id": "bob", "csrf_token": token_b},
    )
    assert second.status_code == 200
    log = Serialize(tmp_path).census(_RUN_ID).vote_log
    assert {record.comparator_id for record in log} == {"alice", "bob"}


def test_epoch_token_minted_once(client: TestClient) -> None:
    """Two identified sitting GETs hold the SAME token — the epoch minted once, no per-render session write."""
    _identified(client)
    first = _scrape_unremember_token(client.get(f"/runs/{_RUN_ID}").text)
    second = _scrape_unremember_token(client.get(f"/runs/{_RUN_ID}").text)
    assert first == second


def test_concurrent_tabs_same_token_both_pass(client: TestClient) -> None:
    """Two votes posted with the same held token both land — the concurrent-tab cure asserted."""
    _identified(client)
    held = _scrape_csrf(client.get(f"/ui/runs/{_RUN_ID}/pair").text)
    one = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={"item_a": "a", "item_b": "c", "winner": "prefer-a", "csrf_token": held},
    )
    assert one.status_code == 200
    two = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={"item_a": "b", "item_b": "c", "winner": "prefer-b", "csrf_token": held},
    )
    assert two.status_code == 200


def test_scraped_token_dead_in_another_browser(client: TestClient, tmp_path: Path) -> None:
    """Client A's identified token posted from client B (its own empty jar) is refused — the write never lands."""
    _identified(client)
    census_before = len(Serialize(tmp_path).census(_RUN_ID).vote_log)
    stolen = _scrape_csrf(client.get(f"/ui/runs/{_RUN_ID}/pair").text)
    browser_b = TestClient(app)  # its own empty jar — the scraped token's new browser
    refused = browser_b.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "comparator_id": "mallory", "csrf_token": stolen},
    )
    assert refused.status_code == 200
    assert "absent-or-mismatched" in refused.text
    assert "set-cookie" not in refused.headers  # the theft identified no one
    assert len(Serialize(tmp_path).census(_RUN_ID).vote_log) == census_before  # the write never landed


def test_register_token_stays_path_bound(client: TestClient) -> None:
    """The identified landing's token stays path-bound (never epoch-composed); the register POST lands the ack."""
    _identified(client)
    landing_token = _scrape_csrf(client.get("/").text)
    anonymous_token = _scrape_csrf(TestClient(app).get("/").text)
    assert landing_token == anonymous_token  # the register lane's mint NEVER epoch-composed, even sessioned
    registered = client.post("/ui/register", data={**_REGISTER_FORM, "csrf_token": landing_token})
    assert registered.status_code == 200
    assert "BEGIN THE SITTING" in registered.text  # the ack landed — the binding never presumed


def test_reidentification_rotates_epoch_old_token_dies(client: TestClient) -> None:
    """The un-remember then the re-identification rotates the epoch — the pre-rotation token dies, the fresh passes."""
    _identified(client)
    stale_token = _scrape_csrf(client.get(f"/ui/runs/{_RUN_ID}/pair").text)  # the pre-rotation epoch's mint
    correction_token = _scrape_unremember_token(client.get(f"/runs/{_RUN_ID}").text)
    forgotten = client.post(_UNREMEMBER, data={"csrf_token": correction_token})
    assert forgotten.status_code == 200
    reask = client.get(f"/runs/{_RUN_ID}")
    assert 'name="comparator_id"' in reask.text  # the ask returned at the anonymous render
    reidentify_token = _scrape_csrf(reask.text)
    reidentified = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "item_a": "a", "item_b": "c", "comparator_id": "mark", "csrf_token": reidentify_token},
    )
    assert reidentified.status_code == 200  # the re-identification — a NEW epoch minted
    refused = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={"item_a": "b", "item_b": "c", "winner": "prefer-a", "csrf_token": stale_token},
    )
    assert refused.status_code == 200
    assert _RELOAD_COPY in refused.text  # the live session's stale-tab cure — the reload taught
    served = _scrape_csrf(client.get(f"/ui/runs/{_RUN_ID}/pair").text)
    passed = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={"item_a": "b", "item_b": "c", "winner": "prefer-a", "csrf_token": served},
    )
    assert passed.status_code == 200  # the fresh token passes — the reload's own cure


def test_voting_as_renders_both_lanes(client: TestClient) -> None:
    """The visible identity line at both lanes — the cookie-swap, the typo, the shared-machine bleed all SEEN."""
    _identified(client)
    assert "voting as: mark" in client.get(f"/runs/{_RUN_ID}").text
    assert "voting as: mark" in client.get(f"/runs/{_RUN_ID}/pair?item_a=a&item_b=b").text


def test_anonymous_never_renders_identity_line(client: TestClient) -> None:
    """The anonymous render shows the ask's twin — never the identity line nor the correction form."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    sitting = client.get(f"/runs/{_RUN_ID}")
    assert "Your name is asked once" in sitting.text
    assert 'name="comparator_id"' in sitting.text
    assert "voting as:" not in sitting.text
    assert "not you?" not in sitting.text
    assert "unremember" not in sitting.text  # the correction form's action absent at the anonymous render


def test_unremember_deletion_cookie_ask_returns(client: TestClient) -> None:
    """The un-remember POST carries the engine's deletion cookie + the HX-Redirect; the next render shows the ask."""
    _identified(client)
    correction_token = _scrape_unremember_token(client.get(f"/runs/{_RUN_ID}").text)
    forgotten = client.post(_UNREMEMBER, data={"csrf_token": correction_token})
    assert forgotten.status_code == 200
    header = "; ".join(forgotten.headers.get_list("set-cookie")).lower()
    assert "remember=null" in header  # the engine's own deletion cookie (sessions.py:80-89)
    assert "expires=thu, 01 jan 1970" in header  # the 1970 expiry — the identity-erase verb
    assert "max-age" not in header  # the deletion's own form — expires alone, no max-age
    assert forgotten.headers["hx-redirect"] == f"/runs/{_RUN_ID}"  # the sitting re-render navigation
    after = client.get(f"/runs/{_RUN_ID}")
    assert 'name="comparator_id"' in after.text  # the ask returned
    assert "voting as:" not in after.text


def test_change_verb_reidentifies_new_name_lands(client: TestClient, tmp_path: Path) -> None:
    """The change verb's re-identification: the new name lands in the log, the render shows it, the epoch rotated."""
    _identified(client)
    before_token = _scrape_csrf(client.get(f"/ui/runs/{_RUN_ID}/pair").text)  # the old epoch's mint
    correction_token = _scrape_unremember_token(client.get(f"/runs/{_RUN_ID}").text)
    client.post(_UNREMEMBER, data={"csrf_token": correction_token})
    reask = client.get(f"/runs/{_RUN_ID}")
    assert 'name="comparator_id"' in reask.text  # the ask returns — the re-identification's entry
    rename_token = _scrape_csrf(reask.text)
    changed = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "item_a": "a", "item_b": "c", "comparator_id": "makr", "csrf_token": rename_token},
    )
    assert changed.status_code == 200
    log = Serialize(tmp_path).census(_RUN_ID).vote_log
    assert [record.comparator_id for record in log] == ["mark", "makr"]  # the typo's stamps kept; the new name lands
    assert "voting as: makr" in client.get(f"/runs/{_RUN_ID}").text  # the render shows it
    after_token = _scrape_csrf(client.get(f"/ui/runs/{_RUN_ID}/pair").text)
    assert after_token != before_token  # the epoch rotated — asserted via the token change


def test_landing_prefills_operator_when_remembered(client: TestClient) -> None:
    """The identified landing's operator field carries the visible editable prefill — the claim still the body's own."""
    _identified(client)
    match = re.search(r'<input name="operator_id"[^>]*>', client.get("/").text)
    assert match is not None
    assert 'value="mark"' in match.group(0)  # the visible editable value — a prefill, never a substitute
    assert "readonly" not in match.group(0)  # the input stays editable — the claim rides what the operator types


def test_anonymous_landing_no_prefill(client: TestClient) -> None:
    """The anonymous landing's operator field carries no value attribute — no prefill to silently substitute."""
    match = re.search(r'<input name="operator_id"[^>]*>', client.get("/").text)
    assert match is not None
    assert "value=" not in match.group(0)


def test_cookie_roundtrip_within_priced_bound(client: TestClient) -> None:
    """The cookie's signed value lands within the re-derived priced bound — keisan's unpadding residual verified."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    token = _scrape_csrf(client.get(f"/runs/{_RUN_ID}").text)
    identified = client.post(
        f"/ui/runs/{_RUN_ID}/vote",
        data={**_FORM_VOTE, "comparator_id": "Mark Losey", "csrf_token": token},
    )
    assert identified.status_code == 200
    jarred = client.cookies.get(_REMEMBER_COOKIE)
    assert jarred is not None
    # keisan's priced form re-derived at the landed session (the spec's 70-94 was the name-only
    # research-stage price; the session carries the 43-char epoch per §2b): the payload
    # {"name": "Mark Losey", "epoch": <43>} = 78 B -> b64encode 104 chars (sessions.py:70's
    # standard form, padding kept) + the TimestampSigner's "." + 6-char timestamp + "." +
    # 27-char sha1 signature (signer.py:220 + timed.py:48) = 139, the 2-B unpadding variance.
    assert 137 <= len(jarred) <= 141
