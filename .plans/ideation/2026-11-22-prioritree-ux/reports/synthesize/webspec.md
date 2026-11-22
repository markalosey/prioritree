<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/webspec

**Route:** prioritree-ux (executing) | **Events:** 20 | **Reports:** 13

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T15:50:55Z |
| 2 | report | togo | 2026-11-22T16:07:28Z |
| 3 | report | togo | 2026-11-22T16:09:32Z |
| 4 | report | togo | 2026-11-22T16:10:30Z |
| 5 | report | togo | 2026-11-22T16:12:24Z |
| 6 | report | togo | 2026-11-22T16:12:58Z |
| 7 | report | togo | 2026-11-22T16:13:24Z |
| 8 | result | shinko | 2026-11-22T16:13:54Z |
| 9 | gate | shinko | 2026-11-22T16:14:37Z |
| 10 | result | shinko | 2026-11-22T17:03:07Z |
| 11 | dispatch | shinko | 2026-11-22T17:03:17Z |
| 12 | report | togo | 2026-11-22T17:11:57Z |
| 13 | report | togo | 2026-11-22T17:12:12Z |
| 14 | report | togo | 2026-11-22T17:13:03Z |
| 15 | report | togo | 2026-11-22T17:13:41Z |
| 16 | report | togo | 2026-11-22T17:14:09Z |
| 17 | result | shinko | 2026-11-22T17:14:39Z |
| 18 | dispatch | shinko | 2026-11-22T17:22:04Z |
| 19 | report | togo | 2026-11-22T17:26:11Z |
| 20 | report | togo | 2026-11-22T17:26:23Z |
## Reported by togo — 2026-11-22T16:07:28Z

# THE WEB UNIT'S EXACT-TASK SPEC — PART 1 (synthesize/webspec; togo, 2026-11-22 — §1 the web module whole; parts 2-4 carry the structure, the generator, the edits, the tests, the sequence, the proofs)

READ-BACK (files read, whole): reports/synthesize/web.md (my approved unit brief — rendered via kumi_render for the untruncated §3e tail) · reports/discover/web.md + reports/understand/web.md (the discovery legs) · reports/synthesize/ux-design.md (the approved design §§1/4/5/7/8/9/10/12/13) · reports/design/presentation.md (the ruled render) · src/prioritree/service.py (whole at HEAD, 528 lines) + src/prioritree/tally.py (TallyResult's frozen shape) + src/prioritree/session.py (the DONE body's expected bytes, :229) · tests/test_service_face.py (whole) + tests/test_service_acceptance.py (:1-110, the probe) · pyproject.toml (whole) · Makefile (whole) · the ux store's junro.json (G-WEBSPEC-BRIEF's three conditions; R1-R6) · the birth store's junro.json (R11 the cycle policy; Q-frontend-stack the projection law) · the installed libraries, verified at source: httpx2/__init__.py + _client.py (AsyncClient, ASGITransport both top-level exports; AsyncClient(base_url=..., transport=...) the form; ASGITransport(app=..., raise_app_exceptions=False), asgi.py:82-93/:163-171) · starlette/templating.py (Jinja2Templates(directory=...):84-97; TemplateResponse(request, name, context, status_code, headers):117-156) · starlette/staticfiles.py (StaticFiles(directory=...):41-57) · starlette/routing.py (:380-434 the Mount FULL-match on path alone; :695-735 the first-FULL-wins loop; scope["path"] NEVER rewritten by the Mount — the child handler renders the parent-identical address grammar) · starlette/datastructures.py (URL.path reads scope["path"] verbatim) · fastapi/templating.py + fastapi/staticfiles.py + fastapi/exceptions.py (the re-export surface the brief rules: the child's imports resolve). READ-ONLY held — nothing written beyond these report events.

## §0 THE SPEC'S VERDICT

The spec lands: 5 authored Python files whole (web.py, web_structure.py, web_scaffold.py, test_web_face.py, test_web_check.py) + 3 exact-region edits (service.py's tail; pyproject.toml x4 regions; Makefile x3 regions) + the ONE test amendment (the 405 arc's re-targeted literals) + 14 generated artifacts (12 templates + app.css + app.js — every byte emitted by the generator from web_structure.py, every file regen-stamped; the manifest at §4). The CDN pins, spec-lane literals: Shoelace 2.20.1, HTMX 2.0.7. THE SPEC'S OWN RULINGS, each named where it lives: (1) the child's refuse handler returns JSONResponse (the family grammar's BYTE form — the pinned unmatched-path 404 arc asserts response.json(); an HTML rendering would break it — the child's body must be JSON); (2) the render-gate branch reuses halt.html's no-ranking-content body with a gated flag (an 8th screen refused — the screen inventory stands at seven, the brief's own list); (3) the landing's resume + direct-result navigation rides the generated pt-go Web Component (authored JS is out of grammar for VALIDATION — but the Web Components surface is generated from structure by R1's own letter: "including the entire Web Components surface"); (4) the generator carries a --root argv (the --check divergence test must never mutate the tracked tree — the test copies web/ to tmp and runs --check against the copy); (5) the register controller's non-numeric-quorum branch constructs the ONLY web-authored ThreePart refusal inline (the fragment tier emits no 4xx; a ValueError raised would hit the child's fold — the honest cure is the family grammar at 200, the wire still ruling the legal values through the very next POST).

## §1 src/prioritree/web.py — THE WEB MODULE, WHOLE (new file; the five-field docstring law; the naming law on every symbol)

```python
# Copyright (C) 2026 Mark Losey. All rights reserved.
"""web — the web fronts: the child app over the service's wire, the nine routes.

The web unit (web-brief §1.1 + the approved design §8): the CHILD application
(FastAPI with the docs routes disabled — the web tier is the human's surface,
not an API), mounted at the service app's TAIL (service.py's mount line, the
one touch); the nine routes (5 pages at honest statuses + 4 rendering
fragments at 200); the in-process service client (httpx2.AsyncClient over
ASGITransport against the imported service app — raise_app_exceptions=False
REQUIRED: the service fold sends its envelope then always re-raises, and the
fold case needs the envelope RETURNED, rikai finding 1 ruled); the child's OWN
fold + refuse handlers (the mount's price: after the tail mount every path
the parent does not fully match lands on the child — starlette routing.py
serves the FIRST FULL match and the Mount matches FULL on path alone, so the
child owns the unmatched-path and disallowed-method surface; its refuse
handler renders the IDENTICAL family grammar as a JSONResponse so the pinned
parent-face arcs survive unedited); the no-anchoring law held by
construction (the count fields are UNREAD at every sitting-context controller
— they never enter a render context); the fragment routes parse form bodies
MANUALLY (no typed Form fields: FastAPI's validation 422 would emit outside
the family grammar, and the fragment tier holds no 4xx — the wire is the sole
validator). All imports via fastapi/starlette's re-export surface + httpx2
(the lock's name — NEVER `import httpx`, the stale unlocked venv copy;
alias_httpx() library-forbidden). Five-field docstrings on every public
symbol; content-in-configuration (the paths and template names named
constants); no asserts, no prints.
"""

from __future__ import annotations

from typing import Any, Final

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

import httpx2

from prioritree.service import ESCALATION, app as service_app
from prioritree.web_structure import UNION_LANES

__all__ = ["web_app"]

# The web tier's named constants (content-in-configuration): the route paths
# (the child's own surface, collision-free against the service's six), the
# emission homes (CWD-relative, the repo-root launch discipline), the
# in-process client's base URL (httpx demands absolute URLs — a literal the
# transport ignores: no socket, no port, no second process).
_LANDING: Final[str] = "/"
_SITTING: Final[str] = "/runs/{stem}"
_DONE: Final[str] = "/runs/{stem}/done"
_PROGRESS: Final[str] = "/runs/{stem}/progress"
_RESULT: Final[str] = "/runs/{stem}/result"
_REGISTER: Final[str] = "/ui/register"
_PAIR: Final[str] = "/ui/runs/{stem}/pair"
_VOTE: Final[str] = "/ui/runs/{stem}/vote"
_STATE_STRIP: Final[str] = "/ui/runs/{stem}/state"
_TEMPLATES_HOME: Final[str] = "web/templates"
_STATIC_HOME: Final[str] = "web/static"
_BASE_URL: Final[str] = "http://prioritree.internal"
_OK: Final[int] = 200
_CREATED: Final[int] = 201
_NOT_FOUND: Final[int] = 404
_METHOD_NOT_ALLOWED: Final[int] = 405
_UNPROCESSABLE: Final[int] = 422
_CONFLICT: Final[int] = 409
_CRASH: Final[int] = 500
_SEE_OTHER: Final[int] = 303
_FRAGMENT_LANE: Final[str] = "/ui/"

# The child app (web-brief §3e: the docs routes DISABLED — the parent's own
# /docs, /redoc, /openapi.json stay live, registered before the mount).
web_app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
web_app.mount("/static", StaticFiles(directory=_STATIC_HOME), name="static")
templates = Jinja2Templates(directory=_TEMPLATES_HOME)

# THE IN-PROCESS CLIENT (web-brief §3a, ruled exact): ONE module-level
# instance, built at import against the imported service app, shared by all
# controllers, process-lifetime — no per-request construction, no teardown
# (ASGITransport holds no socket). raise_app_exceptions=False REQUIRED.
_client = httpx2.AsyncClient(
    base_url=_BASE_URL,
    transport=httpx2.ASGITransport(app=service_app, raise_app_exceptions=False),
)


async def _service(method: str, path: str, json: Any | None = None) -> httpx2.Response:
    """Call the service over the in-process client — the one service path.

    Purpose: every controller's service lane rides this one call (the layering
    held mechanically: the web tier is a true HTTP client of the service
    surface over the same app — its stack, its fold, its door).
    Refuses when: never — the response (any status) IS the return.
    Re-run: deterministic given the store state.
    Touches: nothing — the transport is in-process.
    Provenance: web-brief §3a (the async form), rikai finding 1, G-WEB.
    """
    return await _client.request(method, path, json=json)


def _labels(manifest: dict[str, Any]) -> dict[str, str]:
    """Map the manifest's items to labels — the id->label law (design §7a).

    Purpose: build {id: label} from the manifest body's [[id, label], ...]
    rows — the sitting cards and the ranked whole render labels, ids the
    stable key; an id absent from the map falls back to the id itself.
    Refuses when: never — a pure projection over the manifest's own rows.
    Re-run: deterministic.
    Touches: nothing.
    Provenance: the design §2 (the sixth query's response form), §7a, G-WEB.
    """
    return {str(row[0]): str(row[1]) for row in manifest["items"]}


def _fields(body: dict[str, Any]) -> dict[str, str]:
    """Read a ThreePart body's three fields as data — the one read point.

    Purpose: the service wire's every refusal (and the DONE state's own
    three fields) carries expected/found/next_action; this one function
    reads them as data for the render contexts — never re-derived (the body
    is the source, the web renders, never authors).
    Refuses when: never — a pure read over the body's own keys.
    Re-run: deterministic.
    Touches: nothing.
    Provenance: R5 (the ThreePart mandate), web-brief §5, G-WEB.
    """
    return {
        "expected": str(body["expected"]),
        "found": str(body["found"]),
        "next_action": str(body["next_action"]),
    }


def _unknown(request: Request, body: dict[str, Any]) -> Response:
    """Render the unknown-run page at the honest 404.

    Purpose: every page route's unknown-stem branch — the landing's resume
    affordance + the wire's own found field (the live set, verbatim).
    Refuses when: never — the 404 IS the input; the page renders honestly.
    Re-run: deterministic.
    Touches: nothing.
    Provenance: web-brief §5 (the 404 page), the design §4, G-WEB.
    """
    return templates.TemplateResponse(
        request, "unknown.html", {"fields": _fields(body)}, status_code=_NOT_FOUND
    )


def _refuse_fragment(request: Request, fields: dict[str, str], fold: bool = False) -> Response:
    """Render the ONE refusal renderer as a fragment at 200.

    Purpose: the fragment inventory's refusal member (never its own route):
    the three fields labeled verbatim + the cure affordance beside them, at
    200 — core HTMX swaps it; the refusal is SEEN, never a silent OK. The
    fold flag renders the crash envelope's escalation wording (§5's fold
    case: the fragment controller receiving 500, or itself raising — the
    same renderer, the envelope's three fields).
    Refuses when: never — the refusal IS the input; the fragment renders.
    Re-run: deterministic.
    Touches: nothing.
    Provenance: web-brief §5 (the 422/400 inline refusal + the fold
    fragment), the design §4, R5, G-WEB.
    """
    return templates.TemplateResponse(
        request, "refuse.html", {"fields": fields, "fold": fold}, status_code=_OK
    )


@web_app.exception_handler(StarletteHTTPException)
def refuse(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    """Refuse the child's framework HTTP exceptions in the family grammar — 404/405 taught.

    Purpose: the mount's price, ruled (web-brief §3e): the child owns every
    path the parent does not fully match — this handler renders the
    IDENTICAL family grammar as the parent's shadowed handler, as a
    JSONResponse (the pinned parent-face arcs assert the JSON body):
    expected the method + path as addressed, found the routing violation
    named (404: no route matches the path; 405: the method not allowed at
    the path), next_action the MOUNTED WHOLE's legal set (the nine web
    routes + the six service routes, from the structure's UNION_LANES —
    the mounted whole IS the tree's HTTP face). The status rides
    exc.status_code verbatim — machine-dispatchable.
    Refuses when: never — the handler renders; the framework's refusal IS
    the input (exc.status_code + exc.detail, never re-derived).
    Re-run: deterministic — the same request renders the same body.
    Touches: nothing.
    Provenance: web-brief §3e (the child's own handler), R5, G-WEBSPEC-BRIEF.
    """
    _address = f"{request.method} {request.url.path}"
    if exc.status_code == _NOT_FOUND:
        _found = f"no route matches the path {request.url.path}"
    elif exc.status_code == _METHOD_NOT_ALLOWED:
        _found = f"the method {request.method} is not allowed at the path {request.url.path}"
    else:
        _found = str(exc.detail)
    return JSONResponse(
        status_code=exc.status_code,
        content={"expected": _address, "found": _found, "next_action": UNION_LANES},
    )


@web_app.exception_handler(Exception)
def fold(request: Request, exc: Exception) -> Response:
    """Fold the child's own escapes — the web app's last resort, in the family grammar.

    Purpose: the child is a SEPARATE application (own middleware stack; the
    parent's fold never re-sends once the child's response started) — this
    handler is the child's own catch-all: expected the attempted act, found
    the exception's type + message verbatim, next_action the service fold's
    own ESCALATION constant. FRAGMENT lane (/ui/*): the fold fragment at
    200 (the sitting context preserved — the fold is SEEN, never a stale
    screen). PAGE lane: the honest 500 page. BLE001 rides the named
    pyproject ruling (the service.py precedent re-carried at the child).
    Refuses when: never — the crash IS the input; the handler renders,
    never re-raises.
    Re-run: deterministic in form.
    Touches: nothing.
    Provenance: web-brief §3b (the child's own fold), Q-error-teaching,
    G-WEBSPEC-BRIEF.
    """
    _fields_fold = {
        "expected": f"{request.method} {request.url.path}",
        "found": f"{type(exc).__name__}: {exc}",
        "next_action": ESCALATION,
    }
    if request.url.path.startswith(_FRAGMENT_LANE):
        return _refuse_fragment(request, _fields_fold, fold=True)
    return templates.TemplateResponse(
        request, "fold.html", {"fields": _fields_fold}, status_code=_CRASH
    )


@web_app.get(_LANDING)
async def landing(request: Request) -> Response:
    """Land the operator — the register form + the plain-words bridges, no service calls.

    Purpose: the static landing: the register form (operator id, stated
    question, quorum, six item rows, the resume field, the direct-result
    field), the site's explanation, the vocabulary statement, the jargon
    bridges — every copy string from the structure (content-in-configuration:
    the copy lives in data, the template renders). The form hx-posts to the
    register fragment; the resume + result fields navigate via the generated
    pt-go component (the Web Components surface, generated from structure).
    Refuses when: never — a static render.
    Re-run: deterministic.
    Touches: nothing — no service call (the only call-free route).
    Provenance: web-brief §4 route 1, the design §7/§8, G-WEBSPEC-BRIEF.
    """
    return templates.TemplateResponse(request, "landing.html", {})


@web_app.get(_SITTING)
async def sitting(request: Request, stem: str) -> Response:
    """Sit the comparator — the question as prompt, the first pair server-side.

    Purpose: consume the manifest (the question, the declared verdicts, the
    quorum) + next (the FIRST PAIR rendered server-side — a pure query
    render; the two-step law bars the POST's RESPONSE from carrying the
    pair, never the page's query). Cards A/B marked + labeled (the label
    map); the count UNREAD — never in the render context (the no-anchoring
    law, by construction). DONE => redirect to the done page; 404 => the
    unknown-run page at the honest 404. The buttons hx-post the vote; the
    comparator entry rides every post.
    Refuses when: never by this hand — the branches render honestly.
    Re-run: deterministic given the store state.
    Touches: nothing — queries only.
    Provenance: web-brief §4 route 2, the design §7a/§8, G-WEBSPEC-BRIEF.
    """
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code == _NOT_FOUND:
        return _unknown(request, manifest.json())
    nxt = await _service("GET", f"/runs/{stem}/next")
    if nxt.status_code == _NOT_FOUND:
        return _unknown(request, nxt.json())
    if nxt.status_code == _UNPROCESSABLE:
        return _refuse_fragment(request, _fields(nxt.json()))
    body = nxt.json()
    if body.get("done"):
        return RedirectResponse(f"/runs/{stem}/done", status_code=_SEE_OTHER)
    manifest_body = manifest.json()
    labels = _labels(manifest_body)
    return templates.TemplateResponse(
        request,
        "sitting.html",
        {
            "stem": stem,
            "question": str(manifest_body["question"]),
            "verdicts": list(manifest_body["verdicts"]),
            "quorum": int(manifest_body["quorum"]),
            "item_a": str(body["item_a"]),
            "item_b": str(body["item_b"]),
            "label_a": labels.get(str(body["item_a"]), str(body["item_a"])),
            "label_b": labels.get(str(body["item_b"]), str(body["item_b"])),
        },
    )


@web_app.get(_DONE)
async def done(request: Request, stem: str) -> Response:
    """State the run's coverage honestly — the DONE body's expected verbatim.

    Purpose: consume next (the DONE body — a VALUE, never an error):
    done:true => the coverage statement (the body's expected field VERBATIM —
    "all {N} scheduled pairs at quorum k={K}" — + the plain-words restatement
    + the result link); a pair body (the re-opened edge — the signal is a
    state read, not a latch) => redirect to the sitting page; 404 => the
    unknown-run page.
    Refuses when: never by this hand.
    Re-run: deterministic given the store state.
    Touches: nothing — a query.
    Provenance: web-brief §4 route 3, the design §7c, G-WEBSPEC-BRIEF.
    """
    nxt = await _service("GET", f"/runs/{stem}/next")
    if nxt.status_code == _NOT_FOUND:
        return _unknown(request, nxt.json())
    body = nxt.json()
    if not body.get("done"):
        return RedirectResponse(f"/runs/{stem}", status_code=_SEE_OTHER)
    return templates.TemplateResponse(
        request, "done.html", {"stem": stem, "fields": _fields(body)}, status_code=_OK
    )


@web_app.get(_PROGRESS)
async def progress(request: Request, stem: str) -> Response:
    """Show the operator the census — the state read verbatim, the 5s poll armed.

    Purpose: the OPERATOR's deliberate navigation (never linked from the
    sitting surface): consume state ({"total", "items"} — per_pair_counts
    stays elided at the seam, never resurrected), render the census
    verbatim; the state-strip region carries hx-get to the state fragment
    with the every-5s trigger. 404 => the unknown-run page.
    Refuses when: never by this hand.
    Re-run: deterministic given the store state.
    Touches: nothing — a query.
    Provenance: web-brief §4 route 4, the design §8, G-WEBSPEC-BRIEF.
    """
    result = await _service("GET", f"/runs/{stem}/state")
    if result.status_code == _NOT_FOUND:
        return _unknown(request, result.json())
    body = result.json()
    return templates.TemplateResponse(
        request,
        "progress.html",
        {"stem": stem, "total": int(body["total"]), "items": dict[str, int](body["items"])},
    )


@web_app.get(_RESULT)
async def result(request: Request, stem: str) -> Response:
    """Render the ranked whole, or the safe halt at the honest 409 — the binary held.

    Purpose: consume tally + manifest. 200 => THE RANKED WHOLE (the render
    gate: a body with groups but done:false REFUSES to render — the gated
    branch renders halt.html's no-ranking-content body with the honest
    withholding + the sitting/progress affordances): the semantic table,
    competition ranks (1, 2, 2, 4), tie groups rowspan'd, members in frozen
    id-order, LABELS via the map, W/L/T verbatim + comparisons (the one
    sanctioned derivation), NO win-fraction column, the coverage strip, the
    cycle neutral + the honest-numbers one-liner, pair_counts re-split on
    "|", the algorithm_version footer badge. 409 => the SAFE HALT at the
    HONEST 409, the body's three fields verbatim + the affordances. 404 =>
    the unknown-run page.
    Refuses when: never by this hand — the branches render honestly; the
    ranked whole NEVER renders at done:false (R12, absolute).
    Re-run: deterministic given the store state.
    Touches: nothing — queries.
    Provenance: web-brief §4 route 5, presentation.md (the ruled render),
    R10/R11/R12, G-WEBSPEC-BRIEF.
    """
    tally = await _service("GET", f"/runs/{stem}/tally")
    if tally.status_code == _CONFLICT:
        return templates.TemplateResponse(
            request,
            "halt.html",
            {"stem": stem, "fields": _fields(tally.json()), "gated": False},
            status_code=_CONFLICT,
        )
    if tally.status_code == _NOT_FOUND:
        return _unknown(request, tally.json())
    whole = tally.json()
    if not bool(whole["coverage"]["done"]):
        return templates.TemplateResponse(
            request, "halt.html", {"stem": stem, "gated": True}, status_code=_OK
        )
    labels = _labels((await _service("GET", f"/runs/{stem}/manifest")).json())
    ranked: list[tuple[int, list[str]]] = []
    for group in whole["ranked_groups"]:
        _previous = len(ranked[-1][1]) if ranked else 0
        ranked.append((ranked[-1][0] + _previous if ranked else 1, [str(item) for item in group]))
    ordered = sorted(str(item) for item in whole["per_item_wins"])
    rows = [
        {
            "id": item,
            "label": labels.get(item, item),
            "wins": int(whole["per_item_wins"][item]),
            "losses": int(whole["per_item_losses"][item]),
            "ties": int(whole["per_item_ties"][item]),
        }
        for item in ordered
    ]
    return templates.TemplateResponse(
        request,
        "result.html",
        {
            "stem": stem,
            "ranked": ranked,
            "rows": rows,
            "components": [list(component) for component in whole["coverage"]["components"]],
            "cycle": [list(edge) for edge in whole["coverage"]["cycle"]],
            "pair_counts": dict[str, int](whole["coverage"]["pair_counts"]),
            "algorithm_version": str(whole["algorithm_version"]),
        },
    )


@web_app.post(_REGISTER)
async def register(request: Request) -> Response:
    """Register the run through the form — the ack panel, or the inline refusal at 200.

    Purpose: parse the form MANUALLY (await request.form() — no typed fields:
    the wire is the sole validator), pair the item rows, cast the quorum (a
    non-numeric quorum renders the family grammar inline — constructed at
    the controller, the only web-authored refusal), POST /runs. 201 => the
    register-ack: the BEGIN THE SITTING link, the run_id with the
    click-to-copy affordance (the generated pt-copy component), the
    shareable sitting URL rendered from the REQUEST's own base URL + the
    run path — never a configured port (the port policy lives in the
    lifecycle targets, never in src), shown always, emphasized when
    quorum>1 (the quorum from the form's OWN posted body — the 201 body is
    {"run_id"} alone, no extra call), the frozen-run warning in plain
    words. 422/400 => the ONE refusal renderer inline at 200, at the form.
    Refuses when: never by this hand — the branches render honestly.
    Re-run: deterministic given the store state.
    Touches: the run file through the service (the command).
    Provenance: web-brief §4 route 6, the design §7b, G-WEBSPEC-BRIEF.
    """
    form = await request.form()
    form_ids = [str(value) for value in form.getlist("item-id")]
    form_labels = [str(value) for value in form.getlist("item-label")]
    rows = [
        [item_id, label]
        for item_id, label in zip(form_ids, form_labels, strict=False)
        if item_id.strip() and label.strip()
    ]
    try:
        quorum = int(str(form.get("quorum", "1")))
    except ValueError:
        return _refuse_fragment(
            request,
            {
                "expected": "the quorum field a whole number 1 or greater",
                "found": f"the quorum field carried {form.get('quorum')!r}",
                "next_action": "enter a whole number for the quorum (1 means just you) and re-send",
            },
        )
    payload = {
        "items": rows,
        "operator_id": str(form.get("operator_id", "")),
        "question": str(form.get("question", "")),
        "quorum": quorum,
    }
    outcome = await _service("POST", "/runs", json=payload)
    if outcome.status_code == _CREATED:
        run_id = str(outcome.json()["run_id"])
        return templates.TemplateResponse(
            request,
            "ack.html",
            {"run_id": run_id, "sitting_url": f"{request.base_url}runs/{run_id}", "quorum": quorum},
        )
    return _refuse_fragment(request, _fields(outcome.json()))


@web_app.get(_PAIR)
async def pair(request: Request, stem: str) -> Response:
    """Serve the bare pair as a fragment — or the HX-Redirect on DONE.

    Purpose: consume next (+ the manifest's label map, §7a's label law —
    /next the route's defining call, the map its label-bearing companion).
    200 => the bare-pair fragment (cards A/B marked + labeled; the count
    UNREAD — dropped at the controller); its buttons hx-post the vote as
    the sitting's pair. DONE => the HX-Redirect RESPONSE HEADER to the done
    page (core HTMX's navigation verb — no extension, no JS). 404/422 =>
    the refusal fragment at 200.
    Refuses when: never by this hand.
    Re-run: deterministic given the store state.
    Touches: nothing — a query.
    Provenance: web-brief §4 route 7, the design §7a/§8, G-WEBSPEC-BRIEF.
    """
    nxt = await _service("GET", f"/runs/{stem}/next")
    if nxt.status_code == _NOT_FOUND or nxt.status_code == _UNPROCESSABLE:
        return _refuse_fragment(request, _fields(nxt.json()))
    body = nxt.json()
    if body.get("done"):
        return Response(status_code=_OK, headers={"HX-Redirect": f"/runs/{stem}/done"})
    labels = _labels((await _service("GET", f"/runs/{stem}/manifest")).json())
    return templates.TemplateResponse(
        request,
        "pair.html",
        {
            "stem": stem,
            "item_a": str(body["item_a"]),
            "item_b": str(body["item_b"]),
            "label_a": labels.get(str(body["item_a"]), str(body["item_a"])),
            "label_b": labels.get(str(body["item_b"]), str(body["item_b"])),
        },
    )


@web_app.post(_VOTE)
async def vote(request: Request, stem: str) -> Response:
    """Cast the vote through the form — the ack chains to the next pair.

    Purpose: parse the form MANUALLY, POST the service's cast command, then
    the TWO-STEP CHAIN on 200: the vote-ack restates the verdict in
    ITEM-LABEL TERMS (§7a — "you preferred {label_a} (A) over {label_b}
    (B)" / the tie form; acknowledged:false => the idempotent echo in
    words; the count UNREAD, never rendered) and embeds hx-trigger="load" +
    hx-get to the pair fragment targeting the pair region — the POST's
    response NEVER carries the pair; the load fires the fetch. 422/400 =>
    the inline refusal at 200 — THE PAIR REGION UNTOUCHED (the same pair
    retryable: the refusal swaps into the ack region, never the pair
    region). 404/500 => the same renderer with the wire's fields.
    Refuses when: never by this hand — the branches render honestly.
    Re-run: deterministic given the store state.
    Touches: the run file through the service (the command).
    Provenance: web-brief §4 route 8, the design §7a/§8, G-WEBSPEC-BRIEF.
    """
    form = await request.form()
    payload = {
        "pair": [str(form.get("item_a", "")), str(form.get("item_b", ""))],
        "winner": str(form.get("winner", "")),
        "comparator_id": str(form.get("comparator_id", "")),
        "comparator_class": str(form.get("comparator_class", "human")),
    }
    outcome = await _service("POST", f"/runs/{stem}/votes", json=payload)
    if outcome.status_code != _OK:
        return _refuse_fragment(request, _fields(outcome.json()))
    labels = _labels((await _service("GET", f"/runs/{stem}/manifest")).json())
    return templates.TemplateResponse(
        request,
        "vote-ack.html",
        {
            "stem": stem,
            "winner": payload["winner"],
            "acknowledged": bool(outcome.json()["acknowledged"]),
            "label_a": labels.get(payload["pair"][0], payload["pair"][0]),
            "label_b": labels.get(payload["pair"][1], payload["pair"][1]),
        },
    )


@web_app.get(_STATE_STRIP)
async def state_strip(request: Request, stem: str) -> Response:
    """Serve the state strip — the poll's swap target, the trigger re-armed.

    Purpose: consume state (the query — never refuses on coverage): the
    census read verbatim (total + the per-item involvement) at 200; the
    returned fragment carries the same every-5s trigger — the poll re-arms.
    404 (the unknown stem) => the refusal fragment at 200.
    Refuses when: never by this hand.
    Re-run: deterministic given the store state.
    Touches: nothing — a query.
    Provenance: web-brief §4 route 9, the design §8, G-WEBSPEC-BRIEF.
    """
    result = await _service("GET", f"/runs/{stem}/state")
    if result.status_code != _OK:
        return _refuse_fragment(request, _fields(result.json()))
    body = result.json()
    return templates.TemplateResponse(
        request,
        "state-strip.html",
        {"stem": stem, "total": int(body["total"]), "items": dict[str, int](body["items"])},
    )
```

§1 NOTES THE EXECUTION SEAT READS: (1) the sitting's quorum copy branch rides the template (quorum>1 => the echo copy from the structure); (2) `dict[str, int](body["items"])` — the pyright-strict narrowing idiom (Any to typed) at each wire read; (3) the vote ack's restatement sentence is COMPOSED IN THE TEMPLATE from the structure's copy strings (the copy never lives in code); (4) the count fields appear NOWHERE in web.py — the sitting/pair/vote controllers read item_a/item_b/acknowledged and no count; the wire's count bytes ride into response.json() and die there unread.
## Reported by togo — 2026-11-22T16:09:32Z

# THE WEB UNIT'S EXACT-TASK SPEC — PART 2 (synthesize/webspec; togo, 2026-11-22 — §2 the source structure whole + §2a the part-1 amendments)

## §2a THE PART-1 AMENDMENTS (three corrections to web.py's bytes, exact — the chain's composition rules; nothing else in part 1 changes)

**(1) THE STRUCTURE IS EMISSION-ONLY — the import line DROPS.** web_structure.py lives at scripts/generation/ (the brief's ruled home, §1.3) — it does NOT ride the wheel (pyproject:16-17 packages src/prioritree alone) and is NOT importable from src. Part 1's line `from prioritree.web_structure import UNION_LANES` is therefore WRONG — DELETE IT. The refuse handler's next_action cites the module's OWN union constant (the service.py precedent: service.py composes _ROUTE_TABLE from its own path constants — the child composes its union from its own route constants + the six service lanes as the frozen wire's literals, cited). The structure carries the SAME data in its ROUTE_TABLE + SERVICE_LANES (the inventory's duty, the emission source) — the spec pins the two byte-equal; the face tests pin web.py's union (the served refusal bodies); the --check pins the structure's emission.

**(2) THE UNION BLOCK — INSERT into web.py after the route-path constants block (after `_FRAGMENT_LANE: Final[str] = "/ui/"`), exact bytes:**

```python
# The mounted whole's legal set (web-brief §3e): the nine web routes (the
# child's own path constants above) + the six service routes (the frozen
# wire's literals, cited) — the child's refusal handler teaches the whole
# face honestly; the structure's route table mirrors the same union as data.
_WEB_LANES: Final[tuple[str, ...]] = (
    f"GET {_LANDING}",
    f"GET {_SITTING}",
    f"GET {_DONE}",
    f"GET {_PROGRESS}",
    f"GET {_RESULT}",
    f"POST {_REGISTER}",
    f"GET {_PAIR}",
    f"POST {_VOTE}",
    f"GET {_STATE_STRIP}",
)
_SERVICE_LANES: Final[tuple[str, ...]] = (
    "POST /runs",
    "GET /runs/{run_id}/next",
    "POST /runs/{run_id}/votes",
    "GET /runs/{run_id}/state",
    "GET /runs/{run_id}/tally",
    "GET /runs/{run_id}/manifest",
)
UNION_LANES: Final[str] = "address a legal route — " + ", ".join(_WEB_LANES + _SERVICE_LANES)
```

The refuse handler's body is UNCHANGED (it cites UNION_LANES — now the module's own constant). The pinned arcs hold: "POST /runs" rides _SERVICE_LANES; "POST /ui/register" rides _WEB_LANES.

**(3) THE PAIR CONTROLLER'S CONTEXT GROWS `verdicts`** — pair.html is the SHARED pair region (the sitting page includes it with the sitting's context; the pair route serves it directly), and its verdict buttons render from the DECLARED set: the pair route must pass them. REPLACE the pair controller's post-DONE return block (from `labels = _labels(...)` through the closing of the TemplateResponse call) with:

```python
    manifest_body = (await _service("GET", f"/runs/{stem}/manifest")).json()
    labels = _labels(manifest_body)
    return templates.TemplateResponse(
        request,
        "pair.html",
        {
            "stem": stem,
            "item_a": str(body["item_a"]),
            "item_b": str(body["item_b"]),
            "label_a": labels.get(str(body["item_a"]), str(body["item_a"])),
            "label_b": labels.get(str(body["item_b"]), str(body["item_b"])),
            "verdicts": list(manifest_body["verdicts"]),
        },
    )
```

## §2 scripts/generation/web_structure.py — THE SOURCE STRUCTURE, WHOLE (new file; the naming law: "web-structure the front end's content as data"; the emission's ONLY source — the generator substitutes @KEY@ sentinels from COPY/PINS and writes the artifacts)

```python
# Copyright (C) 2026 Mark Losey. All rights reserved.
"""web_structure — the front end's content as data: the emission's only source.

The web unit's SOURCE STRUCTURE (web-brief §1.3, the ruled home: a sibling of
the generator — a Python module of data is IMPORT-shaped, the script-run's own
path root carries the sibling import, no importlib machinery). THE
CONTENT-IN-CONFIGURATION LAW AT THE WEB TIER (R1's ruled echo): the copy
lives in data, the generator renders — every human-facing word, the CDN pins,
the verdict triple, the route table with its service-call lanes, the form
declarations, the Shoelace inventory, the template bodies, the CSS, the
entire Web Components surface: ALL frontend things are generated from THIS
module (the projection law; hand-authored frontend artifacts are out of
grammar). The template bodies carry @KEY@ sentinels; web_scaffold substitutes
from COPY + PINS at emission ({slot} placeholders convert to Jinja2 slots)
— the emitted artifacts are byte-determined by this module alone.
"""

from __future__ import annotations

from typing import Final

__all__ = [
    "APP_JS",
    "COPY",
    "FRAGMENTS",
    "ITEM_ROWS",
    "PINS",
    "ROUTE_TABLE",
    "SCREENS",
    "SERVICE_LANES",
    "SHOELACE_INVENTORY",
    "STYLESHEET",
    "TEMPLATES",
    "VERDICT_BUTTONS",
    "VERDICTS",
]

# The CDN pins (web-brief §2.5: the exact version values spec-lane literals —
# zero shoelace/htmx bytes in-tree at HEAD; these are the pins the base
# template emits; the online-at-page-load assumption is the design §13's
# priced acceptance).
PINS: Final[dict[str, str]] = {
    "SHOELACE_THEME": "https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.20.1/cdn/themes/light.css",
    "SHOELACE_AUTOLOADER": (
        "https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.20.1/cdn/shoelace-autoloader.js"
    ),
    "HTMX": "https://cdn.jsdelivr.net/npm/htmx.org@2.0.7/dist/htmx.min.js",
}

# The verdict vocabulary (the ruled triple as data — R4's declared default).
VERDICTS: Final[tuple[str, ...]] = ("prefer-a", "prefer-b", "tie")

# The verdict buttons' labels — the markers named, the button<->card tie by
# construction (design §7a: the buttons name the MARKERS).
VERDICT_BUTTONS: Final[dict[str, str]] = {"prefer-a": "Prefer A", "prefer-b": "Prefer B", "tie": "Tie"}

# The route table — the nine routes, each with its kind + service-call lane
# (the web tier EXPERIENCES the service surface's own CQRS segregation, R2).
ROUTE_TABLE: Final[dict[str, tuple[str, str, str]]] = {
    "landing": ("GET", "/", "none — static"),
    "register": ("POST", "/ui/register", "POST /runs"),
    "sitting": ("GET", "/runs/{stem}", "GET /runs/{stem}/manifest + GET /runs/{stem}/next"),
    "pair": ("GET", "/ui/runs/{stem}/pair", "GET /runs/{stem}/next + GET /runs/{stem}/manifest"),
    "vote": ("POST", "/ui/runs/{stem}/vote", "POST /runs/{stem}/votes + GET /runs/{stem}/manifest"),
    "done": ("GET", "/runs/{stem}/done", "GET /runs/{stem}/next + GET /runs/{stem}/manifest"),
    "progress": ("GET", "/runs/{stem}/progress", "GET /runs/{stem}/state"),
    "state_strip": ("GET", "/ui/runs/{stem}/state", "GET /runs/{stem}/state"),
    "result": ("GET", "/runs/{stem}/result", "GET /runs/{stem}/tally + GET /runs/{stem}/manifest"),
}

# The six service routes' lanes (the frozen wire's literals — the union's
# other half; web.py's _SERVICE_LANES mirrors these bytes).
SERVICE_LANES: Final[tuple[str, ...]] = (
    "POST /runs",
    "GET /runs/{run_id}/next",
    "POST /runs/{run_id}/votes",
    "GET /runs/{run_id}/state",
    "GET /runs/{run_id}/tally",
    "GET /runs/{run_id}/manifest",
)

# The form field declarations (design §5: the native affordances as MARKUP,
# never logic — the wire is the sole validator; the item-count rules are
# NEVER pre-checked client-side). Six item rows; required on operator_id,
# question, and the FIRST TWO item rows (the registry's <2-items refusal
# stated as the browser's own semantics); quorum a number input, min 1.
ITEM_ROWS: Final[int] = 6

# The Shoelace inventory (presentation.md's ruled set — Shoelace ships NO
# table component: the semantic table + generated CSS is the honest pick).
SHOELACE_INVENTORY: Final[tuple[str, ...]] = (
    "sl-card",
    "sl-badge",
    "sl-tag",
    "sl-tooltip",
    "sl-details",
)

# The screen + fragment inventories (the brief §1.3's whole list — the
# fragment inventory's refusal member is the ONE renderer, never its own
# route; the fold page carries §3b's page lane).
SCREENS: Final[tuple[str, ...]] = (
    "landing",
    "sitting",
    "done",
    "progress",
    "result",
    "halt",
    "unknown",
    "fold",
)
FRAGMENTS: Final[tuple[str, ...]] = ("ack", "pair", "vote-ack", "state-strip", "refuse")

# The copy strings — every human-facing word (design §7's plain-words bridges
# whole; moho's breaks closed). {slot} placeholders convert to Jinja2 slots
# at emission ({quorum} -> {{ quorum }}, {label_a} -> {{ label_a }}, ...).
COPY: Final[dict[str, str]] = {
    "SITE_TITLE": "Priori-tree",
    "SITE_EXPLANATION": (
        "Priori-tree turns easy pairwise judgments into a reliable ranking. "
        "You register a list, then judge the items two at a time — the site "
        "tallies your judgments into a superior order."
    ),
    "VOCABULARY": (
        "Each pair is judged with three answers: prefer the first, prefer the "
        "second, or a tie."
    ),
    "OPERATOR_ID_BRIDGE": "Your name for yourself on this run.",
    "QUESTION_LABEL": "The question to answer.",
    "QUORUM_BRIDGE": (
        "How many judgments each pair needs — 1 means just you; 2 or more "
        "means you need other judges, and a pair stays open until it has them."
    ),
    "ITEMS_LEGEND": (
        "The items — an id and a label for each. The first two rows are "
        "required; the list is locked once registered."
    ),
    "REGISTER_BUTTON": "Register the run",
    "RESUME_LABEL": "Have a run id? Resume its sitting.",
    "RUN_ID_BRIDGE": (
        "The run id looks like RUN-0001 — it was shown when the run was "
        "registered."
    ),
    "RESULT_LABEL": "Have a run id? See its result.",
    "COMPARATOR_BRIDGE": (
        "Your name for yourself as a judge — it stamps your votes. The same "
        "entry rides every judgment you cast on this page."
    ),
    "QUORUM_ECHO": (
        "Each pair needs {quorum} judgments — you may see pairs you already "
        "judged until every pair has {quorum} judgments."
    ),
    "ACK_HEADING": "Run registered.",
    "ACK_BEGIN": "BEGIN THE SITTING",
    "ACK_COPY_RUN_ID": "Copy run id",
    "ACK_COPY_URL": "Copy sitting URL",
    "ACK_SHARE": (
        "Each pair needs {quorum} judgments — share this sitting URL with "
        "your other judges."
    ),
    "ACK_FROZEN": (
        "The list is locked once registered — a changed list is a new run."
    ),
    "ACK_PREFER_A": "You preferred {label_a} (A) over {label_b} (B).",
    "ACK_PREFER_B": "You preferred {label_b} (B) over {label_a} (A).",
    "ACK_TIE": "Tie: {label_a} (A) and {label_b} (B) stand equal.",
    "ACK_ECHO": (
        "This pair was already recorded with the same answer — it stands once."
    ),
    "DONE_HEADING": "The sitting is complete.",
    "DONE_RESTATED": "The run is complete — each pair has its judgments.",
    "DONE_LINK": "See the result",
    "HALT_HEADING": "The ranking is not ready.",
    "HALT_CURE_BRIDGE": (
        "Bridging pairs — connectivity needs NEW comparisons: a comparator "
        "provides them — sit again (the resume link serves exactly the named "
        "closing pairs); the solo operator re-sits under a NEW comparator id "
        "(a new id's judgments are new samples — a changed verdict is a new "
        "sample)."
    ),
    "HALT_CURE_SHORTFALL": (
        "Shortfall pairs — quorum needs MORE VOTES: more judgments from any "
        "comparator — existing judges (a changed verdict is a new sample) "
        "or new ones (share the sitting URL)."
    ),
    "HALT_RESUME": "Resume the sitting",
    "HALT_PROGRESS": "See the run's progress",
    "WITHHOLD_HEADING": "The ranking is not complete.",
    "WITHHOLD_COPY": (
        "The ranking will not be shown until every pair has its judgments — "
        "never a partial ranking dressed as whole."
    ),
    "WITHHOLD_RESUME": "Resume the sitting",
    "WITHHOLD_PROGRESS": "See the run's progress",
    "UNKNOWN_HEADING": "Unknown run.",
    "UNKNOWN_COPY": "No run answers this address — the wire's own report:",
    "PROGRESS_HEADING": "The run's progress.",
    "PROGRESS_TOTAL": "Judgments recorded:",
    "STATE_POLL_QUIET": "This strip refreshes every 5 seconds.",
    "FOLD_HEADING": "The request failed.",
    "REFUSAL_HEADING": "The request was refused — the wire's own three fields:",
    "FOLD_HEADING_FRAGMENT": "Something broke — the fold's three fields:",
    "EXPECTED_LABEL": "Expected",
    "FOUND_LABEL": "Found",
    "NEXT_ACTION_LABEL": "Next action",
    "RESULT_HEADING": "The ranked whole.",
    "RESULT_COVERAGE_STRIP": (
        "Every scheduled pair at quorum — the comparison graph is connected "
        "({components} component)."
    ),
    "RESULT_CYCLE_TAG": "A cycle is named in the coverage data: {edges}",
    "RESULT_CYCLE_ONE_LINER": (
        "This cycle is structural, never an error, never resolved by "
        "judgment — the wins, losses, and ties in the table are the honest "
        "numbers behind each item's position."
    ),
    "RESULT_PAIR_MATRIX": "The pair matrix — judgments per pair:",
    "RESULT_VERSION": "Ranked by {algorithm_version}",
    "TABLE_RANK": "Rank",
    "TABLE_ITEM": "Item",
    "TABLE_WINS": "W",
    "TABLE_LOSSES": "L",
    "TABLE_TIES": "T",
    "TABLE_COMPARISONS": "Comparisons",
    "BUTTON_COPY_DONE": "Copied",
}

# The template bodies — the artifacts' content (the emitted files carry the
# regen header + these bodies with @KEY@ sentinels substituted). Fragments
# do NOT extend the base (HTMX swaps them into the live page).
TEMPLATES: Final[dict[str, str]] = {
    "base.html": (
        "<!DOCTYPE html>\n"
        '<html lang="en">\n'
        "<head>\n"
        '  <meta charset="utf-8">\n'
        '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "  <title>{% block title %}@SITE_TITLE@{% endblock %}</title>\n"
        '  <link rel="stylesheet" href="@SHOELACE_THEME@">\n'
        '  <script type="module" src="@SHOELACE_AUTOLOADER@"></script>\n'
        '  <script src="@HTMX@"></script>\n'
        '  <link rel="stylesheet" href="/static/app.css">\n'
        '  <script type="module" src="/static/app.js"></script>\n'
        "</head>\n"
        "<body>\n"
        '<main class="wrap">\n'
        "{% block content %}{% endblock %}\n"
        "</main>\n"
        "</body>\n"
        "</html>\n"
    ),
    "landing.html": (
        '{% extends "base.html" %}\n'
        "{% block title %}@SITE_TITLE@ — begin{% endblock %}\n"
        "{% block content %}\n"
        '<section class="card">\n'
        "  <h1>@SITE_TITLE@</h1>\n"
        "  <p>@SITE_EXPLANATION@</p>\n"
        "  <p>@VOCABULARY@</p>\n"
        "</section>\n"
        '<section class="card">\n'
        "  <h2>Register a run</h2>\n"
        '  <form hx-post="/ui/register" hx-target="#register-result" hx-swap="innerHTML">\n'
        "    <label>@OPERATOR_ID_BRIDGE@ <input name=\"operator_id\" required minlength=\"1\"></label>\n"
        "    <label>@QUESTION_LABEL@ <input name=\"question\" required minlength=\"1\"></label>\n"
        '    <label>@QUORUM_BRIDGE@ <input type="number" name="quorum" value="1" min="1"></label>\n'
        "    <fieldset>\n"
        "      <legend>@ITEMS_LEGEND@</legend>\n"
        '      <div class="item-row"><input name="item-id" required minlength="1" placeholder="id">'
        ' <input name="item-label" required minlength="1" placeholder="label"></div>\n'
        '      <div class="item-row"><input name="item-id" required minlength="1" placeholder="id">'
        ' <input name="item-label" required minlength="1" placeholder="label"></div>\n'
        '      <div class="item-row"><input name="item-id" placeholder="id">'
        ' <input name="item-label" placeholder="label"></div>\n'
        '      <div class="item-row"><input name="item-id" placeholder="id">'
        ' <input name="item-label" placeholder="label"></div>\n'
        '      <div class="item-row"><input name="item-id" placeholder="id">'
        ' <input name="item-label" placeholder="label"></div>\n'
        '      <div class="item-row"><input name="item-id" placeholder="id">'
        ' <input name="item-label" placeholder="label"></div>\n'
        "    </fieldset>\n"
        '    <button type="submit">@REGISTER_BUTTON@</button>\n'
        "  </form>\n"
        '  <div id="register-result"></div>\n'
        "</section>\n"
        '<section class="card">\n'
        "  <h2>Resume</h2>\n"
        '  <form method="get" action="/" data-pt-path="/runs/{stem}">\n'
        "    <label>@RESUME_LABEL@ <input name=\"stem\" placeholder=\"RUN-0001\"></label>\n"
        '    <button type="submit">Resume the sitting</button>\n'
        "  </form>\n"
        '  <p class="quiet">@RUN_ID_BRIDGE@</p>\n'
        '  <form method="get" action="/" data-pt-path="/runs/{stem}/result">\n'
        "    <label>@RESULT_LABEL@ <input name=\"stem\" placeholder=\"RUN-0001\"></label>\n"
        '    <button type="submit">See the result</button>\n'
        "  </form>\n"
        "</section>\n"
        "{% endblock %}\n"
    ),
    "sitting.html": (
        '{% extends "base.html" %}\n'
        "{% block title %}@SITE_TITLE@ — the sitting{% endblock %}\n"
        "{% block content %}\n"
        '<section class="card">\n'
        "  <h1>{{ question }}</h1>\n"
        '  <label for="comparator-id">@COMPARATOR_BRIDGE@</label>\n'
        '  <input id="comparator-id" name="comparator_id" required minlength="1">\n'
        '  {% if quorum > 1 %}<p class="quiet">@QUORUM_ECHO@</p>{% endif %}\n'
        '  {% include "pair.html" %}\n'
        '  <div id="ack-region"></div>\n'
        "</section>\n"
        "{% endblock %}\n"
    ),
    "pair.html": (
        '<div id="pair-region">\n'
        '  <form hx-post="/ui/runs/{{ stem }}/vote" hx-target="#ack-region" hx-swap="innerHTML"'
        ' hx-include="[name=\'comparator_id\']">\n'
        '    <input type="hidden" name="item_a" value="{{ item_a }}">\n'
        '    <input type="hidden" name="item_b" value="{{ item_b }}">\n'
        '    <div class="cards">\n'
        '      <sl-card class="pair-card">'
        '<sl-badge slot="header">A</sl-badge><span class="card-label">{{ label_a }}</span></sl-card>\n'
        '      <sl-card class="pair-card">'
        '<sl-badge slot="header">B</sl-badge><span class="card-label">{{ label_b }}</span></sl-card>\n'
        "    </div>\n"
        '    <div class="verdicts">\n'
        "      {% set labels = @VERDICT_BUTTONS@ %}\n"
        '      {% for verdict in verdicts %}<button class="verdict" name="winner" value="{{ verdict }}">'
        "{{ labels.get(verdict, verdict) }}</button>{% endfor %}\n"
        "    </div>\n"
        "  </form>\n"
        "</div>\n"
    ),
    "vote-ack.html": (
        '<div id="vote-ack">\n'
        '  <p class="ack-line">'
        "{% if winner == 'prefer-a' %}@ACK_PREFER_A@"
        "{% elif winner == 'prefer-b' %}@ACK_PREFER_B@"
        "{% else %}@ACK_TIE@{% endif %}</p>\n"
        '  {% if not acknowledged %}<p class="quiet">@ACK_ECHO@</p>{% endif %}\n'
        '  <div hx-get="/ui/runs/{{ stem }}/pair" hx-trigger="load" hx-target="#pair-region"'
        ' hx-swap="outerHTML"></div>\n'
        "</div>\n"
    ),
    "ack.html": (
        '<div id="register-ack">\n'
        "  <p><strong>@ACK_HEADING@</strong></p>\n"
        '  <p>The run id: <strong>{{ run_id }}</strong>'
        ' <pt-copy value="{{ run_id }}" label="@ACK_COPY_RUN_ID@"></pt-copy></p>\n'
        '  <p>The sitting URL: <code>{{ sitting_url }}</code>'
        ' <pt-copy value="{{ sitting_url }}" label="@ACK_COPY_URL@"></pt-copy></p>\n'
        '  {% if quorum > 1 %}<p class="share">@ACK_SHARE@</p>{% endif %}\n'
        '  <p class="quiet">@ACK_FROZEN@</p>\n'
        '  <sl-button variant="primary" href="/runs/{{ run_id }}">@ACK_BEGIN@</sl-button>\n'
        "</div>\n"
    ),
    "state-strip.html": (
        '<div id="state-strip" hx-get="/ui/runs/{{ stem }}/state" hx-trigger="every 5s"'
        ' hx-swap="outerHTML">\n'
        "  <p>@PROGRESS_TOTAL@ <strong>{{ total }}</strong></p>\n"
        '  <ul class="involvement">\n'
        "    {% for item_id, involvement in items.items() %}"
        "<li>{{ item_id }}: {{ involvement }}</li>{% endfor %}\n"
        "  </ul>\n"
        '  <p class="quiet">@STATE_POLL_QUIET@</p>\n'
        "</div>\n"
    ),
    "refuse.html": (
        '<div class="refusal">\n'
        '  <p><strong>{% if fold %}@FOLD_HEADING_FRAGMENT@{% else %}@REFUSAL_HEADING@{% endif %}'
        "</strong></p>\n"
        '  <dl class="three-part">\n'
        "    <dt>@EXPECTED_LABEL@</dt><dd>{{ fields.expected }}</dd>\n"
        "    <dt>@FOUND_LABEL@</dt><dd>{{ fields.found }}</dd>\n"
        "    <dt>@NEXT_ACTION_LABEL@</dt><dd>{{ fields.next_action }}</dd>\n"
        "  </dl>\n"
        "</div>\n"
    ),
    "done.html": (
        '{% extends "base.html" %}\n'
        "{% block title %}@SITE_TITLE@ — done{% endblock %}\n"
        "{% block content %}\n"
        '<section class="card">\n'
        "  <h1>@DONE_HEADING@</h1>\n"
        '  <sl-badge variant="success">done</sl-badge>\n'
        '  <p class="coverage">{{ fields.expected }}</p>\n'
        "  <p>@DONE_RESTATED@</p>\n"
        '  <sl-button variant="primary" href="/runs/{{ stem }}/result">@DONE_LINK@</sl-button>\n'
        "</section>\n"
        "{% endblock %}\n"
    ),
    "progress.html": (
        '{% extends "base.html" %}\n'
        "{% block title %}@SITE_TITLE@ — progress{% endblock %}\n"
        "{% block content %}\n"
        '<section class="card">\n'
        "  <h1>@PROGRESS_HEADING@</h1>\n"
        '  {% include "state-strip.html" %}\n'
        "</section>\n"
        "{% endblock %}\n"
    ),
    "result.html": (
        '{% extends "base.html" %}\n'
        "{% block title %}@SITE_TITLE@ — the result{% endblock %}\n"
        "{% block content %}\n"
        '<section class="card">\n'
        "  <h1>@RESULT_HEADING@</h1>\n"
        '  <sl-badge variant="success">done</sl-badge>\n'
        '  <table class="ranked">\n'
        "    <thead><tr><th>@TABLE_RANK@</th><th>@TABLE_ITEM@</th><th>@TABLE_WINS@</th>"
        "<th>@TABLE_LOSSES@</th><th>@TABLE_TIES@</th><th>@TABLE_COMPARISONS@</th></tr></thead>\n"
        "    <tbody>\n"
        "      {% for rank, group in ranked %}\n"
        "      {% for item in group %}{% if loop.first %}<tr>{% endif %}\n"
        '        {% if loop.first %}<td rowspan="{{ group | length }}">{{ rank }}</td>{% endif %}\n'
        "      {% endfor %}{% endfor %}\n"
        "    </tbody>\n"
        "  </table>\n"
        "</section>\n"
        "{% endblock %}\n"
    ),
    "halt.html": (
        '{% extends "base.html" %}\n'
        "{% block title %}@SITE_TITLE@ — not ready{% endblock %}\n"
        "{% block content %}\n"
        '<section class="card">\n'
        "  <h1>{% if gated %}@WITHHOLD_HEADING@{% else %}@HALT_HEADING@{% endif %}</h1>\n"
        '  {% if gated %}<sl-badge variant="neutral">withheld</sl-badge>'
        '<p>@WITHHOLD_COPY@</p>{% else %}<sl-badge variant="warning">safe halt</sl-badge>\n'
        '  <dl class="three-part">\n'
        "    <dt>@EXPECTED_LABEL@</dt><dd>{{ fields.expected }}</dd>\n"
        "    <dt>@FOUND_LABEL@</dt><dd>{{ fields.found }}</dd>\n"
        "    <dt>@NEXT_ACTION_LABEL@</dt><dd>{{ fields.next_action }}</dd>\n"
        "  </dl>\n"
        '  <ul>\n'
        "    <li>@HALT_CURE_BRIDGE@</li>\n"
        "    <li>@HALT_CURE_SHORTFALL@</li>\n"
        "  </ul>{% endif %}\n"
        '  <sl-button variant="primary" href="/runs/{{ stem }}">'
        "{% if gated %}@WITHHOLD_RESUME@{% else %}@HALT_RESUME@{% endif %}</sl-button>\n"
        '  <a href="/runs/{{ stem }}/progress">'
        "{% if gated %}@WITHHOLD_PROGRESS@{% else %}@HALT_PROGRESS@{% endif %}</a>\n"
        "</section>\n"
        "{% endblock %}\n"
    ),
    "unknown.html": (
        '{% extends "base.html" %}\n'
        "{% block title %}@SITE_TITLE@ — unknown run{% endblock %}\n"
        "{% block content %}\n"
        '<section class="card">\n'
        "  <h1>@UNKNOWN_HEADING@</h1>\n"
        "  <p>@UNKNOWN_COPY@</p>\n"
        '  <p class="wire-found">{{ fields.found }}</p>\n'
        '  <form method="get" action="/" data-pt-path="/runs/{stem}">\n'
        "    <label>@RESUME_LABEL@ <input name=\"stem\" placeholder=\"RUN-0001\"></label>\n"
        '    <button type="submit">Resume the sitting</button>\n'
        "  </form>\n"
        '  <p class="quiet">@RUN_ID_BRIDGE@</p>\n'
        "</section>\n"
        "{% endblock %}\n"
    ),
    "fold.html": (
        '{% extends "base.html" %}\n'
        "{% block title %}@SITE_TITLE@ — the fold{% endblock %}\n"
        "{% block content %}\n"
        '<section class="card">\n'
        "  <h1>@FOLD_HEADING@</h1>\n"
        '  <dl class="three-part">\n'
        "    <dt>@EXPECTED_LABEL@</dt><dd>{{ fields.expected }}</dd>\n"
        "    <dt>@FOUND_LABEL@</dt><dd>{{ fields.found }}</dd>\n"
        "    <dt>@NEXT_ACTION_LABEL@</dt><dd>{{ fields.next_action }}</dd>\n"
        "  </dl>\n"
        "</section>\n"
        "{% endblock %}\n"
    ),
}
```

**THE RESULT TABLE'S RENDER — the exact Jinja2 loop (the row above compresses it; the EMITTED template's tbody carries this exact form):** the `ranked` context is a list of (rank, [ids]) pairs in group order; the rows render with the rowspan on each group's FIRST member, the per-item stats looked up from the `rows` context (a dict keyed by id — the template renders `{{ rows[item] }}`-style lookups via a Jinja2 namespace loop). Because the per-group rowspan couples two loops, the emitted template's tbody is EXACTLY:

```
    <tbody>
      {% for rank, group in ranked %}{% set outer = loop %}{% for item in group %}
      <tr>
        {% if outer.first %}<td rowspan="{{ group | length }}">{{ rank }}</td>{% endif %}
        <td>{{ rows[item].label }} <sl-badge>{{ item }}</sl-badge></td>
        <td>{{ rows[item].wins }}</td>
        <td>{{ rows[item].losses }}</td>
        <td>{{ rows[item].ties }}</td>
        <td>{{ rows[item].wins + rows[item].losses + rows[item].ties }}</td>
      </tr>
      {% endfor %}{% endfor %}
    </tbody>
```

...followed in the same section, after the table: the coverage strip `<p class="coverage-strip">@RESULT_COVERAGE_STRIP@</p>` (with {components} -> {{ components | length }}), the cycle block (rendered only when the cycle list is non-empty: a neutral sl-tag with the directed edges `{{ edge[0] }} &gt; {{ edge[1] }}` per edge, comma-joined, inside an sl-tooltip whose content is @RESULT_CYCLE_ONE_LINER@), the full datum under `<sl-details summary="The coverage datum">` (the components gloss line; @RESULT_PAIR_MATRIX@ with each pair_counts key re-split on "|" — the row renders `{{ key }}` verbatim with its count, the O(n^2) content collapsed), and the footer badge `<footer><sl-badge>{{ algorithm_version }}</sl-badge> — @RESULT_VERSION@</footer>` (with {algorithm_version} -> {{ algorithm_version }}). The PART-2 template-string block above names the result.html body; the tbody + coverage block rendered here are its exact continuation — the spec's §4 manifest carries the composed whole's shape; the emitted bytes must carry: the table with six columns (Rank/Item/W/L/T/Comparisons), NO win-fraction column anywhere (R10 at the glass), the coverage strip, the sl-details datum, the footer badge. The emitted result.html is 40 lines; every element named here is an element there.

**THE CSS + THE WEB COMPONENTS (the structure's data, whole):**

```python
# The generated stylesheet (the semantic table's CSS — Shoelace ships NO
# table component, the honest pick carries its own styling).
STYLESHEET: Final[str] = (
    ":root { --pt-gap: 0.75rem; }\n"
    "body { margin: 0; font-family: system-ui, sans-serif; background: #fafafa; color: #1a1a1a; }\n"
    ".wrap { max-width: 40rem; margin: 0 auto; padding: var(--pt-gap); }\n"
    ".card { background: white; border-radius: 0.5rem; padding: var(--pt-gap); margin-bottom: var(--pt-gap); }\n"
    "label { display: block; margin: 0.5rem 0; }\n"
    "input { display: block; width: 100%; box-sizing: border-box; padding: 0.4rem; margin-top: 0.2rem; }\n"
    ".item-row input { display: inline-block; width: calc(50% - 0.25rem); }\n"
    ".cards { display: flex; gap: var(--pt-gap); margin: var(--pt-gap) 0; }\n"
    ".pair-card { flex: 1; }\n"
    ".card-label { font-size: 1.1rem; }\n"
    ".verdicts { display: flex; gap: var(--pt-gap); flex-wrap: wrap; }\n"
    "button.verdict { padding: 0.6rem 1.2rem; }\n"
    "table.ranked { border-collapse: collapse; width: 100%; margin: var(--pt-gap) 0; }\n"
    "table.ranked th, table.ranked td { border: 1px solid #ddd; padding: 0.4rem; text-align: left; }\n"
    "table.ranked th { background: #f0f0f0; }\n"
    ".coverage-strip { color: #666; }\n"
    ".three-part dt { font-weight: bold; margin-top: 0.5rem; }\n"
    ".three-part dd { margin: 0; }\n"
    ".wire-found { font-family: monospace; background: #f4f4f4; padding: 0.5rem; border-radius: 0.3rem; }\n"
    ".quiet { color: #666; }\n"
    ".share { background: #eef6ff; padding: 0.5rem; border-radius: 0.3rem; }\n"
    ".refusal { background: #fff7f0; border-left: 3px solid #e67e22; padding: var(--pt-gap); }\n"
    "#state-strip { background: #f4f4f4; padding: var(--pt-gap); border-radius: 0.3rem; }\n"
    ".involvement { columns: 2; margin: 0.5rem 0; }\n"
    ".ack-line { font-size: 1.1rem; }\n"
    "footer { color: #666; margin-top: var(--pt-gap); }\n"
)

# The entire Web Components surface (R1: ALL frontend things generated from
# Python — the JS itself is structure data). pt-copy: the click-to-copy
# affordance (the clipboard call is the component's own generated JS — in
# grammar). The pt-path delegation: the landing's resume + direct-result
# fields NAVIGATE (the page routes) without a query-string landing — a
# delegated submit listener reads the form's data-pt-path, substitutes the
# stem, and assigns the location (navigation JS, never validation JS: the
# wire stays the sole validator, the design §5's dropped-pre-checks ruling
# held).
APP_JS: Final[str] = (
    "class PtCopy extends HTMLElement {\n"
    "  connectedCallback() {\n"
    '    const value = this.getAttribute("value") ?? "";\n'
    '    const label = this.getAttribute("label") ?? "Copy";\n'
    '    const button = document.createElement("sl-button");\n'
    "    button.textContent = label;\n"
    '    button.addEventListener("click", () => {\n'
    "      navigator.clipboard.writeText(value);\n"
    '      button.textContent = "Copied";\n'
    "      window.setTimeout(() => { button.textContent = label; }, 2000);\n"
    "    });\n"
    "    this.replaceChildren(button);\n"
    "  }\n"
    "}\n"
    'customElements.define("pt-copy", PtCopy);\n'
    "document.addEventListener(\"submit\", (event) => {\n"
    "  const form = event.target;\n"
    '  const path = form.getAttribute("data-pt-path");\n'
    "  if (path === null) { return; }\n"
    "  event.preventDefault();\n"
    '  const stem = form.querySelector("input[name=\'stem\']").value.trim();\n'
    "  if (stem) { window.location.assign(path.replace(\"{stem}\", encodeURIComponent(stem))); }\n"
    "});\n"
)
```

§2 NOTES THE EXECUTION SEAT READS: (1) the @VERDICT_BUTTONS@ sentinel in pair.html substitutes to the JSON form of VERDICT_BUTTONS — the generator renders it as `{"prefer-a": "Prefer A", "prefer-b": "Prefer B", "tie": "Tie"}` (a valid Jinja2 dict literal; the generator composes it via json.dumps over the map); (2) the COPY values' {slot} placeholders convert to Jinja2 slots at emission — the generator's one conversion: value.replace("{", "{{").replace("}", "}}") applied ONLY to slot-bearing copy keys (the keys named with {slot} in their value: QUORUM_ECHO, ACK_SHARE, ACK_PREFER_A, ACK_PREFER_B, ACK_TIE, RESULT_COVERAGE_STRIP, RESULT_CYCLE_TAG, RESULT_VERSION); the RESULT_CYCLE_TAG's {edges} is substituted in-template (the cycle block renders the edges inline — the tag line's copy is "A cycle is named in the coverage data:" followed by the rendered edges — the {edges} placeholder DROPS from the emitted copy, the edges render as markup after the colon); (3) the templates are static string data — the Jinja2 {{ }} rides literally; the generator performs ONLY the @KEY@ substitution (+ the {slot} conversion); (4) every template line is ≤120 bytes in the EMITTED artifact (the long copy strings wrap in the source constants via adjacent-literal + — pyright's implicit-concatenation error honored by using explicit + operators).
## Reported by togo — 2026-11-22T16:10:30Z

# THE WEB UNIT'S EXACT-TASK SPEC — PART 3 (synthesize/webspec; togo, 2026-11-22 — §3 the generator whole, §4 the emission rules + the artifact manifest)

## §3 scripts/generation/web_scaffold.py — THE GENERATOR, WHOLE (new file; the naming law: "web-scaffold the front end from the source structure"; the ONLY writer of the front end's artifacts — R1's projection law at the bytes level)

```python
# Copyright (C) 2026 Mark Losey. All rights reserved.
"""web-scaffold the front end from the source structure — the only writer.

The web unit's GENERATOR (web-brief §1.2/§3d): a REGEN-TIME emitter, never a
runtime render — `uv run python scripts/generation/web_scaffold.py --target
web` writes the front end's artifacts from web_structure.py (the sibling
data module; the script-run's own path root carries the import — no
importlib machinery), every file regen-stamped with the two-line header in
its file type's comment form; `--check` regenerates IN MEMORY and diffs the
tree — a divergence is a REFUSAL naming the re-run (the never-hand-edit law
enforced, the zero-findings bar's sibling; the Makefile's web-check target
rides the same argv). The `--root` argv (default the working directory)
names the tree the artifacts live under — the --check divergence test runs
against a tmp copy, never mutating the tracked tree. THE EMISSION
DISCIPLINE: the @KEY@ sentinels substitute from the structure's PINS +
COPY (the copy values' {slot} placeholders convert to Jinja2 slots at
substitution — the mechanical brace doubling, applied ONLY to the values,
never to the template bodies' own {stem} literals which the generated JS
substitutes at browse time); @VERDICT_BUTTONS@ substitutes the verdict
button map as a JSON dict literal (a valid Jinja2 dict). Hand-authored
artifacts are out of grammar; this script is the only writer.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import web_structure

__all__ = ["main"]

# The regen idiom (the AGENTS.md:1-2 precedent, the structure named IN the
# header) — composed per file type's comment form at emission.
_GENERATED_NOTE: str = (
    "@generated by scripts/generation/web_scaffold.py "
    "from scripts/generation/web_structure.py — do not edit manually"
)
_REGEN_LINE: str = "regen: uv run python scripts/generation/web_scaffold.py --target web"


def _slots(value: str) -> str:
    """Convert a copy value's {slot} placeholders to Jinja2 slots.

    Purpose: the mechanical brace doubling applied ONLY to substitution
    values — {quorum} becomes {{ quorum }} (a slot name may carry a filter:
    {components | length} becomes {{ components | length }}); the template
    bodies' own {stem} literals (data-pt-path, the generated JS's runtime
    substitution) are NEVER passed through here.
    Refuses when: never — a pure string transform.
    Re-run: deterministic — the same value converts the same way.
    Touches: nothing.
    Provenance: web-brief §8.3 (the emission discipline), G-WEBSPEC-BRIEF.
    """
    return value.replace("{", "{{").replace("}", "}}")


def _expand(body: str) -> str:
    """Expand a template body's @KEY@ sentinels from the structure's data.

    Purpose: one substitution pass — PINS (the CDN URLs) + COPY (the copy
    values, slot-converted) + the VERDICT_BUTTONS map as a JSON dict
    literal; the structure is the emission's only source (R1: the entire
    front end generated from Python).
    Refuses when: never — unknown sentinels ride through untouched (an
    authoring error surfaces at the --check diff or the face tests, never
    silently).
    Re-run: deterministic — the same body expands to the same bytes.
    Touches: nothing — the in-memory expansion; the writer persists it.
    Provenance: web-brief §3d (the emission channel), G-WEBSPEC-BRIEF.
    """
    expanded = body
    for key, value in web_structure.PINS.items():
        expanded = expanded.replace(f"@{key}@", value)
    for key, value in web_structure.COPY.items():
        expanded = expanded.replace(f"@{key}@", _slots(value))
    return expanded.replace("@VERDICT_BUTTONS@", json.dumps(web_structure.VERDICT_BUTTONS))


def _headers(suffix: str) -> str:
    """Compose the two-line regen header in the file type's comment form.

    Purpose: every artifact carries the idiom — HTML the comment form, CSS
    the block-comment form, JS the line-comment form; the header names the
    generator, the structure, and the re-run command (the never-hand-edit
    law, readable at every artifact's head).
    Refuses when: an unknown suffix — ValueError (an emission form for an
    unmapped file type is an authoring error, loud at generation time).
    Re-run: deterministic.
    Touches: nothing.
    Provenance: web-brief §3d (the regen-stamp), the AGENTS.md:1-2 idiom.
    """
    if suffix == ".html":
        return f"<!-- {_GENERATED_NOTE} -->\n<!-- {_REGEN_LINE} -->\n"
    if suffix == ".css":
        return f"/* {_GENERATED_NOTE} */\n/* {_REGEN_LINE} */\n"
    if suffix == ".js":
        return f"// {_GENERATED_NOTE}\n// {_REGEN_LINE}\n"
    message = f"no regen header form for the suffix {suffix!r}"
    raise ValueError(message)


def _plan(root: Path) -> list[tuple[Path, str]]:
    """Plan the artifact set — every (path, bytes) the emission owns.

    Purpose: the ONE plan both writers share: the 14 templates under
    web/templates/ (the base + the eight screens + the five fragments, in
    the structure's inventory order) + web/static/app.css (the structure's
    stylesheet) + web/static/app.js (the structure's Web Components surface)
    — 16 artifacts, each the header + the expanded body, byte-determined by
    the structure alone.
    Refuses when: never — a pure projection.
    Re-run: deterministic — the same structure plans the same bytes.
    Touches: nothing — the caller writes or diffs.
    Provenance: web-brief §1.4 (the emission home), §3d, G-WEBSPEC-BRIEF.
    """
    artifacts: list[tuple[Path, str]] = []
    for name, body in web_structure.TEMPLATES.items():
        path = root / "web" / "templates" / name
        artifacts.append((path, _headers(path.suffix) + _expand(body)))
    artifacts.append((root / "web" / "static" / "app.css", _headers(".css") + web_structure.STYLESHEET))
    artifacts.append((root / "web" / "static" / "app.js", _headers(".js") + web_structure.APP_JS))
    return artifacts


def _emit(root: Path) -> None:
    """Write the artifact set — the front end's only writer at work.

    Purpose: create the homes (mkdir parents), write every artifact with
    UTF-8 encoding, print the count + the home (the tool's report channel —
    the T201 named ruling rides pyproject; the cli.py precedent re-carried).
    Refuses when: never — an unwritable root raises through the OS (loud).
    Re-run: idempotent — the same structure re-emits byte-identical bytes.
    Touches: the web/ tree under the root — the 16 artifacts, nothing else.
    Provenance: web-brief §3d (the emission channel), G-WEBSPEC-BRIEF.
    """
    artifacts = _plan(root)
    for path, content in artifacts:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    print(f"emitted {len(artifacts)} web artifacts under {root / 'web'}")


def _check(root: Path) -> int:
    """Diff the tree against the in-memory regeneration — the never-hand-edit law's enforcement.

    Purpose: regenerate every artifact in memory and compare with the
    disk's bytes; a divergence prints each divergent path + the re-run
    command and returns 1 (the refusal names the cure — a REFUSAL, never a
    silent diff); sync prints the all-clear and returns 0. The web-check
    make target and the --check test ride this one exit code.
    Refuses when: the tree diverges — that is the op's one refusal (a
    missing artifact is a divergence: None never equals the planned bytes).
    Re-run: deterministic — the same tree checks the same way.
    Touches: nothing — the check never writes (the tracked tree is never
    mutated by a check).
    Provenance: web-brief §3d (--check), §6.2, G-WEBSPEC-BRIEF.
    """
    divergences: list[str] = []
    for path, content in _plan(root):
        on_disk = path.read_text(encoding="utf-8") if path.exists() else None
        if on_disk != content:
            divergences.append(str(path))
    if divergences:
        for divergence in divergences:
            print(f"web artifacts diverge from the source structure: {divergence}")
        print(f"re-run: uv run python scripts/generation/web_scaffold.py --target web --root {root}")
        return 1
    print("web artifacts in sync with the source structure")
    return 0


def main() -> int:
    """Drive the scaffold — --target web writes; --check diffs.

    Purpose: the argparse surface: --target (the emission's target, "web"
    the only one — the ruling names the future widening), --check (the diff
    mode), --root (the tree under which web/ lives, the working directory
    by default — the repo-root launch discipline held; the divergence test
    passes a tmp root). Returns the process exit code (0 sync/emitted, 1
    divergence).
    Refuses when: --target anything but web — argparse's choices refusal
    (exit 2, the named-cure form).
    Re-run: deterministic — the same argv checks/emits the same way.
    Touches: the web/ tree under --root on the write path; nothing on --check.
    Provenance: web-brief §3d (the argv), §1.8 (web-check), G-WEBSPEC-BRIEF.
    """
    parser = argparse.ArgumentParser(description="web-scaffold the front end from the source structure")
    parser.add_argument("--target", choices=["web"], required=True)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--root", type=Path, default=Path("."))
    args = parser.parse_args()
    if args.check:
        return _check(args.root)
    _emit(args.root)
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

§3 NOTES THE EXECUTION SEAT READS: (1) THE SIBLING IMPORT — `import web_structure` resolves because the script-run's own path root (scripts/generation) is sys.path[0] when run as `python scripts/generation/web_scaffold.py` — the brief's ruled form, no importlib machinery; (2) THE PYRIGHT RESOLUTION — pyproject's [tool.pyright] grows `executionEnvironments = [{ root = "scripts/generation" }]` so the sibling resolves under the checker (the exact region at §5c); ruff's INP001 (implicit namespace package) fires on both script files — the NAMED RULINGS at §5c carry `scripts/generation/web_scaffold.py" = ["T201", "INP001"]` and `"scripts/generation/web_structure.py" = ["INP001"]` (scripts/generation is the ruled script-run home, not an importable package — the ruling is named with its reason, the zero-ignore law's family form); (3) THE RESULT COVERAGE SLOT — part 2's COPY["RESULT_COVERAGE_STRIP"] value's slot is `{components | length}` (the filter rides the slot name; the mechanical conversion emits `{{ components | length }}` — the count renders, never the list repr). This amends part 2's literal: the value reads `"Every scheduled pair at quorum — the comparison graph is connected ({components | length} component)."` — all other part-2 bytes stand.

## §4 THE EMISSION RULES + THE ARTIFACT MANIFEST (the web/ artifacts, byte-shaped)

**THE MANIFEST — 16 artifacts, every byte emitted by the generator:**
- web/templates/base.html (the base: the CDN tags — the exact pins from PINS; the static tags /static/app.css + /static/app.js; the title block; the content block)
- web/templates/landing.html, sitting.html, done.html, progress.html, result.html, halt.html, unknown.html, fold.html (the eight screens — the pages extend the base)
- web/templates/ack.html, pair.html, vote-ack.html, state-strip.html, refuse.html (the five fragments — bare swap content, never extending the base)
- web/static/app.css (the structure's STYLESHEET)
- web/static/app.js (the structure's APP_JS — the pt-copy component + the data-pt-path submit delegation)

**THE RULES (each one the --check's diff surface):** (1) every artifact = the two-line regen header in its type's comment form (§3's _headers) + the expanded body, UTF-8, trailing newline (every template body string ends "\n" — the last byte of every artifact is 0x0A); (2) the artifacts LAND git-tracked, nothing web gitignored (.gitignore UNTOUCHED — tansa §4: the generated-and-tracked precedent), serving as-is (no browse-time build); (3) hand-authored artifacts are OUT OF GRAMMAR (R1) — the generator is the only writer; the --check refuses a divergence naming the re-run (exit 1); (4) the bytes are DETERMINED by web_structure.py alone — the @KEY@ substitution (§3's _expand) composes the final Jinja2; the runtime never re-sources copy (web.py carries zero human-facing words); (5) the base template's CDN pins are the EXACT literals: Shoelace 2.20.1 (the theme CSS + the autoloader, jsdelivr), HTMX 2.0.7 (htmx.min.js, jsdelivr) — the online-at-page-load assumption priced at the design §13 (the collaborator's acceptance at G-UX-DESIGN-BRIEF); (6) THE PROJECTION LAW'S PROOF SURFACE: `--check` green at HEAD pins structure↔disk; the face tests pin runtime↔templates (the served markup's hrefs/hx-* URLs asserted); the union (web.py's constants) pins against the served refusal bodies — the three surfaces bound by the test suite (§6) + web-check.
## Reported by togo — 2026-11-22T16:12:24Z

# THE WEB UNIT'S EXACT-TASK SPEC — PART 4 (synthesize/webspec; togo, 2026-11-22 — §5 the edit regions; parts 5-6 carry the tests, the sequence, the proofs)

## §5a THE PART-1 CONTROLLER-BRANCH AMENDMENTS (the uniform error-swap law, closing part 1's guard gaps — every branch named, exact bytes)

THE LAW (part 1's controllers amended to its full form): every service call's non-success response renders the body's three fields verbatim — FRAGMENTS render refuse.html at 200 (fold=True when the status is 500, the crash envelope's escalation wording); PAGES render fold.html at the RESPONSE'S OWN honest status; a page's 404 renders the unknown-run page. The per-controller bytes REPLACE as follows (all other part-1 bytes stand, with §2a's three amendments):

**sitting — REPLACE the two guard blocks with:**
```python
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code != _OK:
        if manifest.status_code == _NOT_FOUND:
            return _unknown(request, manifest.json())
        return templates.TemplateResponse(
            request, "fold.html", {"fields": _fields(manifest.json())}, status_code=manifest.status_code
        )
    nxt = await _service("GET", f"/runs/{stem}/next")
    if nxt.status_code != _OK:
        if nxt.status_code == _NOT_FOUND:
            return _unknown(request, nxt.json())
        return templates.TemplateResponse(
            request, "fold.html", {"fields": _fields(nxt.json())}, status_code=nxt.status_code
        )
```

**done — REPLACE the head guard with:** the same two-branch form over `nxt` (404 => _unknown; other non-200 => fold.html at nxt.status_code), then the unchanged body/done/redirect logic.

**progress — REPLACE the head guard with:** the same two-branch form over the state call.

**result — REPLACE from the `tally = await _service(...)` line through the `labels = ...` line with:**
```python
    tally = await _service("GET", f"/runs/{stem}/tally")
    if tally.status_code == _CONFLICT:
        return templates.TemplateResponse(
            request,
            "halt.html",
            {"stem": stem, "fields": _fields(tally.json()), "gated": False},
            status_code=_CONFLICT,
        )
    if tally.status_code != _OK:
        if tally.status_code == _NOT_FOUND:
            return _unknown(request, tally.json())
        return templates.TemplateResponse(
            request, "fold.html", {"fields": _fields(tally.json())}, status_code=tally.status_code
        )
    whole = tally.json()
    if not bool(whole["coverage"]["done"]):
        return templates.TemplateResponse(
            request, "halt.html", {"stem": stem, "gated": True}, status_code=_OK
        )
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code != _OK:
        return templates.TemplateResponse(
            request, "fold.html", {"fields": _fields(manifest.json())}, status_code=manifest.status_code
        )
    labels = _labels(manifest.json())
```
(The manifest call moves AFTER the render gate — the gated branch needs no labels; the rest of the controller stands.)

**register — REPLACE the final non-201 return with:** `return _refuse_fragment(request, _fields(outcome.json()), fold=outcome.status_code == _CRASH)`.

**pair — REPLACE the head guard and the manifest region with:**
```python
    nxt = await _service("GET", f"/runs/{stem}/next")
    if nxt.status_code != _OK:
        return _refuse_fragment(request, _fields(nxt.json()), fold=nxt.status_code == _CRASH)
    body = nxt.json()
    if body.get("done"):
        return Response(status_code=_OK, headers={"HX-Redirect": f"/runs/{stem}/done"})
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code != _OK:
        return _refuse_fragment(request, _fields(manifest.json()), fold=manifest.status_code == _CRASH)
    manifest_body = manifest.json()
    labels = _labels(manifest_body)
```
...followed by the §2a(3) context block (with "verdicts": list(manifest_body["verdicts"])).

**vote — REPLACE the outcome guard and the manifest read with:**
```python
    if outcome.status_code != _OK:
        return _refuse_fragment(request, _fields(outcome.json()), fold=outcome.status_code == _CRASH)
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code != _OK:
        return _refuse_fragment(request, _fields(manifest.json()), fold=manifest.status_code == _CRASH)
    labels = _labels(manifest.json())
```

**state_strip — REPLACE the head guard with:** `if result.status_code != _OK: return _refuse_fragment(request, _fields(result.json()), fold=result.status_code == _CRASH)`.

## §5b src/prioritree/service.py — THE TAIL MOUNT (the ONE touch; APPEND after line 528, the file's end — nothing else in the file changes)

```python


# The web tier's tail mount (web-brief §3c): the child app mounted at the
# root — the six JSON routes above match FIRST (the router serves the first
# FULL match, the Mount catching the rest); the web module imports THIS app
# at its own top, bound above before the tail import fires (the import
# cycle's only legal form — a top-of-file import would fire before the app
# binds; an importlib dodge would HIDE the cycle, not name it; the PLC0415
# named ruling rides pyproject).
from prioritree.web import web_app

app.mount("/", web_app)
```

## §5c pyproject.toml — FIVE REGIONS (the deps move + the rulings + the pyright scope)

**(1) REPLACE line 7:** `dependencies = ["fastapi", "httpx2", "jinja2", "uvicorn[standard]"]` (alphabetical; jinja2 NEW — the lock mints it at landing; httpx2 PROMOTED dev->runtime — moved, not duplicated).

**(2) REPLACE the service.py per-file-ignores comment block + entry (lines 100-105) with:**
```toml
# RULING (service-face-brief §6, G-SERVICE-FACE-BRIEF approved 2026-11-21): BLE001 —
# the 500 crash-envelope handler's except Exception IS the ruled catch-all (the app-level
# fold: crashes first-class citizens, the article's three-part form; Starlette re-raises
# so the traceback rides the log channel, never the body — the cli.py precedent re-cited).
# PLC0415 (web-brief §3c + G-WEBSPEC-BRIEF approved 2026-11-22): the tail's mid-file
# web import IS the import cycle's only legal form — the web module binds service.app at
# ITS top, so the import must fire AFTER the app binds; a top-of-file import would fire
# before, an importlib dodge would HIDE the cycle, not name it. The ignores ARE the
# rulings, named.
"src/prioritree/service.py" = ["BLE001", "PLC0415"]
```

**(3) INSERT after the tests/test_service_acceptance.py entry (after line 112) the four new entries:**
```toml
# RULING (web-brief §3b + G-WEBSPEC-BRIEF approved 2026-11-22): BLE001 — the child's own
# fold handler's except Exception IS the ruled catch-all (the service.py precedent
# re-carried at the child: crashes first-class citizens; the fragment lane renders the
# fold at 200, the page lane the honest 500). The ignore IS the ruling, named.
"src/prioritree/web.py" = ["BLE001"]

# RULING (web-brief §1.8-9 + G-WEBSPEC-BRIEF approved 2026-11-22): the floor's scope
# grows over the generator (the projection law's only writer — the zero-findings bar
# must cover it, else the lint condition holds vacuously for the very code R1 rides on).
# T201 — print IS the tool's ruled report channel (the cli.py precedent re-carried at
# the generator: the emission count + the --check refusal naming the re-run). INP001 —
# scripts/generation is the ruled script-run home (web-brief §1.2-3), not an importable
# package; the sibling import rides the script-run's own path root. The ignores ARE the
# rulings, named.
"scripts/generation/web_scaffold.py" = ["T201", "INP001"]
"scripts/generation/web_structure.py" = ["INP001"]

# RULING (web-brief §1.9 + G-WEBSPEC-BRIEF approved 2026-11-22): S603 — the --check
# harness's subprocess IS the no-shell law's own form (the fixed-argv invocation, the
# sibling python executable; the untrusted-input intent never rides a deterministic
# regen check). S607 named for the ruling's form's stability — the
# tests/test_harness.py + tests/test_service_acceptance.py rulings re-carried at the
# web tier. The entry IS the ruling, named.
"tests/test_web_check.py" = ["S603", "S607"]
```

**(4) REPLACE line 128 with + INSERT the execution environment after it:**
```toml
include = ["scripts", "src", "tests"]
executionEnvironments = [{ root = "scripts/generation" }]
```
(the execution environment makes the generator's sibling import resolve under the checker — the brief's ruled include-growth carried with its enabling line).

**(5) REPLACE line 134:** `dev = ["pytest", "pyright", "ruff"]` (httpx2 slimmed from the dev group — the promotion).

## §5d Makefile — THREE REGIONS

**(1) REPLACE line 3:** `.PHONY: dev test lint typecheck web-check help`
**(2) REPLACE lines 11-12 (the lint target):**
```makefile
lint:      ## Ruff over src/, tests/ and scripts/
	uv run ruff check src/ tests/ scripts/
```
**(3) INSERT after the typecheck target (after line 15):**
```makefile
web-check: ## Regenerate the web artifacts in memory and diff (refuses on divergence)
	uv run python scripts/generation/web_scaffold.py --target web --check
```
## Reported by togo — 2026-11-22T16:12:58Z

# THE WEB UNIT'S EXACT-TASK SPEC — PART 5 (synthesize/webspec; togo, 2026-11-22 — §6a the web face test file whole)

## §6a tests/test_web_face.py — WHOLE (new file)

```python
# Copyright (C) 2026 Mark Losey. All rights reserved.
"""test_web_face — the mounted web tier's falsification set, in-process.

The web unit's test surface (web-brief §6.1): the mounted app under the
injection fixture — the SAME app now carries the mount; the child's
controllers call the service through the in-process client and the service
reads the PARENT's state.seam (the fixture's injection) — the isolation
extends to the web tier whole (store-as-parameter; no env, no CWD games).
The arcs: the page arcs (landing, sitting, done, progress, result
200/409/404); the fragment arcs (register 201/422/bad-quorum, the two-step
chain, the idempotent echo, the HX-Redirect, the 422 pair-untouched, the
state strip, the fold fragment); the no-anchoring pins (byte-level: no
sitting-context response carries the count; the sitting surface never
links state/tally). The S101/PLR2004 tests ruling stands.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from pathlib import Path

from fastapi.testclient import TestClient

from prioritree.service import app
from prioritree.service_store import Serialize

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
    assert response.status_code == 303
    assert response.headers["location"] == f"/runs/{_RUN_ID}/done"


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
    assert response.status_code == 303
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
    """The vote ack restates in item-label terms and chains to the pair fragment."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    response = client.post(f"/ui/runs/{_RUN_ID}/vote", data=_FORM_VOTE)
    assert response.status_code == 200
    assert "You preferred one (A) over two (B)." in response.text
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
    client.post(f"/ui/runs/{_RUN_ID}/vote", data=_FORM_VOTE)
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


def test_fold_fragment_500_envelope(client: TestClient) -> None:
    """A crashing seam verb renders the fold fragment at 200 — the envelope's fields seen."""

    class _BoomSeam:
        """The stub seam — serve raises; the fold's forced input, zero scaffolding."""

        def serve(self, _run_id: str, _seed: int | None = None) -> tuple[str, str, int]:
            """Raise the boom — the crash the fold renders."""
            raise RuntimeError("boom")

    app.state.seam = _BoomSeam()
    crashed = TestClient(app)
    response = crashed.get(f"/ui/runs/{_RUN_ID}/pair")
    assert response.status_code == 200
    assert "RuntimeError: boom" in response.text
    assert "check the server logs" in response.text
```

§6a NOTES THE EXECUTION SEAT READS: (1) the fixture is the service face's own form extended — the SAME app (the mount rides it); (2) TestClient does not follow redirects by default — the 303 arcs assert the status + the location header; (3) the register fragment posts form-encoded (data=...) — the fragment controllers parse request.form() manually (urlencoded, no multipart dep); (4) the no-anchoring pins ride test_sitting_serves_first_pair_server_side + test_vote_then_pair_chain (the count assertions) — kensho's leg re-runs them verbatim; (5) test_done_reopened_redirects: the two-item run with ZERO votes — next serves a pair body at the done page => the redirect back to the sitting (the re-opened edge); (6) the fold fragment's stub seam mirrors test_crash_envelope_500's own _BoomSeam precedent.
## Reported by togo — 2026-11-22T16:13:24Z

# THE WEB UNIT'S EXACT-TASK SPEC — PART 6 (synthesize/webspec; togo, 2026-11-22 — §6b the check test, the one amendment, §7 the command sequence, §8 the no-break proofs; the spec closes)

## §6b tests/test_web_check.py — WHOLE (new file)

```python
# Copyright (C) 2026 Mark Losey. All rights reserved.
"""test_web_check — the generator's --check: the regen-faithfulness pin + the divergence refusal.

The web unit's generator test (web-brief §6.2): the fixed-argv subprocess (the
test_harness/test_service_acceptance precedent; the S603/S607 named ruling
rides pyproject). The pass arc at HEAD (the regen-faithfulness pin — zero
divergence, exit 0); the divergence-refusal semantics (a mutated COPY of the
web tree under tmp_path — the tracked tree NEVER mutated by a test — the
--check refuses naming the re-run, exit 1).
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pathlib import Path as _Path  # noqa: F401 — hmm, see note (2)
```

**THE FILE, WHOLE (note (2) below resolves the import form — the block above is superseded by this one):**

```python
# Copyright (C) 2026 Mark Losey. All rights reserved.
"""test_web_check — the generator's --check: the regen-faithfulness pin + the divergence refusal.

The web unit's generator test (web-brief §6.2): the fixed-argv subprocess (the
test_harness/test_service_acceptance precedent; the S603/S607 named ruling
rides pyproject). The pass arc at HEAD (the regen-faithfulness pin — zero
divergence, exit 0); the divergence-refusal semantics (a mutated COPY of the
web tree under tmp_path — the tracked tree NEVER mutated by a test — the
--check refuses naming the re-run, exit 1).
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

_REPO: Path = Path(__file__).resolve().parent.parent
_SCAFFOLD: Path = _REPO / "scripts" / "generation" / "web_scaffold.py"
_ARGV_BASE: list[str] = [sys.executable, str(_SCAFFOLD), "--target", "web"]
_RERUN = "re-run: uv run python scripts/generation/web_scaffold.py --target web"


def test_check_passes_at_head() -> None:
    """The regen-faithfulness pin: --check at the repo root exits 0 (zero divergence)."""
    result = subprocess.run(
        [*_ARGV_BASE, "--check"], cwd=_REPO, capture_output=True, text=True, check=False
    )
    assert result.returncode == 0


def test_check_refuses_on_divergence(tmp_path: Path) -> None:
    """A divergent copy refuses: exit 1, the re-run named — the tracked tree never touched."""
    shutil.copytree(_REPO / "web", tmp_path / "web")
    target = tmp_path / "web" / "templates" / "pair.html"
    target.write_text(target.read_text(encoding="utf-8") + "<!-- hand edit -->\n", encoding="utf-8")
    result = subprocess.run(
        [*_ARGV_BASE, "--check", "--root", str(tmp_path)],
        cwd=_REPO,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 1
    assert result.stdout is not None
    assert _RERUN in result.stdout
```

§6b NOTES: (1) the file imports `Path` directly (used at module scope — no TYPE_CHECKING block needed); (2) the divergence arc copies web/ (16 small artifacts) into tmp_path, appends a hand edit to pair.html, and runs --check with --root tmp_path — the tracked tree is never touched (the brief's own law); the refusal's stdout names the re-run (the §3 _check print); (3) a MISSING artifact is also a divergence (None != bytes) — the hand-edit arc suffices as the divergence mechanism's proof.

## §6c THE ONE AMENDMENT — test_service_face.py's 405 arc (REPLACE the function whole, lines 264-272; the module docstring byte-untouched — it names the arc's intent, never the path)

```python
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
```

## §7 THE COMMAND SEQUENCE (jikko's exact execution order; a read-back after every edit — the landing discipline)

1. **CREATE scripts/generation/web_structure.py** (§2 whole, with §3's RESULT_COVERAGE_STRIP amendment: the slot is `{components | length}`). READ-BACK: the file read back; TEMPLATES carries 14 entries; COPY carries the §7 bridges whole.
2. **CREATE scripts/generation/web_scaffold.py** (§3 whole). READ-BACK: the file read back; `--target/--check/--root` the argparse surface.
3. **EDIT pyproject.toml** (§5c's five regions). READ-BACK: the deps line; the five per-file-ignores entries; include + executionEnvironments; the dev group slimmed.
4. **RUN `uv sync`** (the lock mints jinja2; httpx2's pin 2.16.2 stands — a promotion never re-pins). READ-BACK: uv.lock's prioritree entry carries httpx2 + jinja2; jinja2's package entry minted.
5. **RUN `uv run python scripts/generation/web_scaffold.py --target web`** — 16 artifacts emitted (14 templates + app.css + app.js under web/). READ-BACK: `uv run python scripts/generation/web_scaffold.py --target web --check` exits 0 ("in sync"); the 16 files exist; each file's head carries the two-line regen header.
6. **CREATE src/prioritree/web.py** (§1 whole + §2a's amendments + §5a's controller-branch amendments). READ-BACK: the file read back; the UNION_LANES block present; NO web_structure import.
7. **EDIT src/prioritree/service.py** — APPEND the tail mount (§5b, after line 528). READ-BACK: the diff shows ONLY the append; the six routes' bodies byte-untouched.
8. **CREATE tests/test_web_face.py** (§6a whole). READ-BACK.
9. **CREATE tests/test_web_check.py** (§6b whole). READ-BACK.
10. **EDIT tests/test_service_face.py** — REPLACE the one 405 arc (§6c). READ-BACK: the diff shows ONLY that function.
11. **EDIT Makefile** (§5d's three regions). READ-BACK: .PHONY carries web-check; lint's argv carries scripts/; the web-check target present.
12. **THE FLOOR, IN ORDER:** `make dev` (uv sync green) · `make test` (every suite green: the service face's 16 arcs with the re-targeted 405 + the web face's 19 + the web check's 2 + every standing suite) · `make lint` (ruff ALL over src/ tests/ scripts/ — zero findings; the named rulings the only ignores) · `make typecheck` (pyright strict 0/0 over the grown include) · `make web-check` (exit 0).
13. **ONE COMMIT** (the increment's close — one-commit-per-increment): the 5 new files + web/'s 16 artifacts + uv.lock + pyproject.toml + Makefile + service.py + the amended test_service_face.py — one commit, the unit whole.

## §8 THE NO-BREAK PROOFS

**(1) THE FROZEN SURFACES' PINS.** The six JSON routes' bodies byte-untouched — service.py's ONLY change is the tail append after :528 (the diff is the proof). The service face tests byte-untouched EXCEPT the one 405 arc (§6c, the collaborator's approved amendment). The acceptance harness unbroken: the 404-as-ready probe (GET /runs/RUN-0001/next) is a parent route — matched before the mount (the router serves the FIRST FULL match, verified at the installed starlette routing.py:697-705; the Mount appends LAST at :740-742); the boot argv unchanged; the eight-request arc rides parent routes only. The parent's own /docs, /redoc, /openapi.json keep serving (registered at construction, before the mount).

**(2) THE UNMATCHED-PATH 404 ARC — HELD BY MECHANISM, NEVER A TEST EDIT.** The child's refuse handler renders the identical family grammar as a JSONResponse at 404; the Mount never rewrites scope["path"] (starlette routing.py:403-434 sets root_path/path_params only; Request.url reads scope["path"] verbatim — datastructures.py:39) — so the child's body carries expected "GET /no-such-path", found "no route matches the path /no-such-path", next_action the union carrying "POST /runs": the arc's three asserts hold unedited.

**(3) THE PROJECTION LAW'S PROOFS.** Every web/ byte is emitted by the generator from web_structure.py: the --check regenerates in memory and diffs (a divergence refuses naming the re-run, exit 1); every artifact carries the two-line regen header in its type's comment form; zero hand-authored artifacts (the generator is the only writer); the artifacts land git-tracked (.gitignore untouched — nothing web ignored); serving as-is (no browse-time build). The divergence test proves the refusal semantics on a tmp copy — the tracked tree never mutated by a test.

**(4) THE NO-ANCHORING PINS (kensho's leg re-runs them).** The count fields NEVER enter any sitting-context render context — the controllers never read them (the no-anchoring law by construction, not template diligence): asserted byte-level at the sitting page + the pair fragment + the vote ack ("count" absent). The sitting surface NEVER links state/tally: asserted ("/state" and "tally" absent from the sitting page).

**(5) THE RUFF/PYRIGHT RULINGS THE NEW CODE HONORS.** Ruff ALL — the named rulings the ONLY ignores: service.py BLE001+PLC0415 (the fold + the tail import, the cycle's only legal form); web.py BLE001 (the child's fold — the precedent re-carried); scripts/generation/web_scaffold.py T201+INP001; scripts/generation/web_structure.py INP001 (the ruled script-run home, not an importable package); tests/test_web_check.py S603/S607 (the fixed-argv subprocess family); the tests/** S101/PLR2004 ruling standing. Pyright strict — the include grows scripts with the executionEnvironments root (the sibling import resolves); every controller annotated `-> Response`; the wire reads narrowed at each read (str()/int()/dict[str, int](...)); no implicit string concatenation (explicit + only — pyproject's error honored); E501 ≤120 held at authoring; PLR2004 dodged by the named status constants (the service.py precedent).

**(6) THE G-WEB MAPPING (the build gate's four conditions, named).** (1) The exact-task law → this spec: five files whole + every modified file's exact regions + insertion points + the command sequence (the execution seat receives nothing to figure out). (2) R1 → §3+§4: the generator the only writer, the structure the only source, --check the enforcement, the artifacts tracked + regen-stamped — the ENTIRE front end (templates, CSS, the Web Components JS, the copy, the CDN pins) generated from Python. (3) The comparator's flow end-to-end → §6a's arcs: register → the sitting's server-side pair → the vote's two-step chain → the 5s progress poll → the ranked whole; the render gate; the 409-verbatim; the HX-Redirect. (4) R5 + the floor → §8's proofs: every refusal ThreePart-verbatim on every touched surface (the child's 404/405 in the family grammar, the fragments' 200s rendering refusals visibly, the pages' honest statuses); pyright 0/0 + ruff zero findings over the GROWN scope; kensho's independent re-run green (validate/web).

THE SPEC CLOSES: the fence exact (5 new files + 3 edited + 1 amended arc), every byte authored (whole files whole, modified files as exact regions with insertion points), the artifacts byte-determined by the structure, the command sequence ordered with read-backs, the no-break proofs named per frozen surface. G-WEBSPEC-BRIEF's conditions are met by this spec; the collaborator's approval is the gate. — togo, 2026-11-22
## Reported by togo — 2026-11-22T17:11:57Z

# THE RETHINK — PART 1: THE RE-SETTLED ARCHITECTURE (synthesize/webspec; togo, 2026-11-22 — per Q-ux-surface R9/R10, the template-source law stated twice; parts 2-4 carry the re-spec whole: the template files, the static pair, web.py, the edits, the tests, the per-step command sequence, the no-break proofs)

READ-BACK (the ground, whole): the ux store's junro.json — R9 verbatim ("Generating all the things from python is not putting the content in python...but having separate jinja template files that are loaded to generate the surface. Not putting all the jinja content directly inside functions as giant concatenations...") + R10 verbatim ("the main point of templates is template file, load them, generate the output from them.") + the supersession amendment (the spec SUPERSEDED; web_scaffold.py's fate mine to rule) + R7/R8 (the per-step dispatch law) + R1-R6 (the stack, CQRS, the service ground, the governance form, the ThreePart, the report authorship) · packets.jsonl (the chain whole — my v1's six report events, the G-WEBSPEC-BRIEF green, the fat build's failure, the 13-dispatch law) · reports/synthesize/webspec.md (my own v1 whole, 2080 lines — the standing content inventory's source) · reports/synthesize/web.md (my approved unit brief — the clauses this rethink amends) · reports/synthesize/ux-design.md (the approved design — via the brief's citations; §§4/5/7/8/9/10/12/13 the content's ground) · THE TREE AT HEAD: scripts/generation/web_scaffold.py (202 lines — LANDED) + scripts/generation/web_structure.py (563 lines — LANDED, see §0) · src/prioritree/service.py (:486-528 — describe at the tail, the file ends :528) · tests/test_service_acceptance.py (:25-104 — the boot instrument: Popen(_ARGV, cwd=home) — THE SCRATCH-CWD BOOT, load-bearing for §5) · tests/test_service_face.py (:264 — the 405 arc to re-target) · pyproject.toml (whole) · Makefile (whole) · the globs: src/prioritree/web.py ABSENT, tests/test_web*.py ABSENT, web/** ABSENT (zero emission landed). READ-ONLY held — nothing written beyond these report events.

## §0 THE VERDICT + THE TREE TRUTH

The web unit's architecture is RE-SETTLED per R9/R10: the front end's content lives in AUTHORED FILES — fourteen Jinja2 template files + the CSS + the Web Components JS — and Python LOADS them and GENERATES the served surface from them at request time (template + context → the page). The v1 form (the 14 template bodies + the CSS + the JS as Python string constants in web_structure.py, emitted by web_scaffold.py) is out of grammar — R9's own named supersession. ZERO generated artifacts remain: nothing emits, nothing regens, nothing carries a regen header; the never-hand-edit law's scope reaches NOTHING web (AUTHORED files are edited by definition — the dispatch's own parenthetical, and R10's: "template FILES (authored, on disk, the source of truth)").

THE TREE TRUTH, named against the ledger: the supersession amendment records "web_structure.py never landed (step 1 cancelled)" — the DISK disagrees: scripts/generation/web_structure.py EXISTS at 563 lines (read at :1-60, the v1 §2 bytes verbatim). The tree is the truth (the no-claim-without-evidence law): BOTH stranded files landed from the superseded bytes. The removal step (the re-planned sequence's step 1) therefore removes BOTH — web_scaffold.py (202 lines) AND web_structure.py (563 lines) — one act, the supersession's cleanup.

## §1 THE ARCHITECTURE SETTLED (each choice cited to R9/R10 + the standing laws)

**(1) THE TEMPLATE SOURCE HOME: web/templates/ at the repo root — RULED.** The authored Jinja2 files' home: web/templates/ (the base + the 8 screens + the 5 fragments, 14 files) + web/static/ (app.css + app.js). REASONS: (a) THE WHEEL'S PACKAGING — pyproject:16-17 packages = ["src/prioritree"] carries the library alone; the web tier is repo-tree surface, served at the repo-root launch (the design §12's launch discipline), never a wheel-served thing — a src/prioritree/templates/ home would demand package-data pyproject growth serving no ruled need (the tree is the deployment) and would smuggle a data directory into the 11-flat-module package convention; (b) THE LAUNCH DISCIPLINE — the homes resolve CWD-relative in web.py, the SAME law STORE_HOME rides (Path(".prioritree/runs"), run_store.py:53, CWD-relative): the repo-root launch (uvicorn prioritree.service:app) resolves both; the brief §1.4's ruled home carries — the supersession changes the files' KIND (generated → AUTHORED), never their home; (c) THE LOADER'S FORM — Jinja2Templates(directory="web/templates"): the filesystem loader's directory form (starlette templating.py:84-97, verified at source at v1's read-back), CWD-relative, exactly the ruled form. THE ALTERNATIVE REFUSED: src/prioritree/templates/ (in-package data) — the wheel-trap named above; the brief's approved home ruling stands.

**(2) THE LOADER/RENDER SEAM: Jinja2Templates' filesystem form in web.py.** `templates = Jinja2Templates(directory="web/templates")` at the module head; every controller: `templates.TemplateResponse(request, "<name>.html", {context}, status_code=...)` — R10's three beats held mechanically: the FILES (authored, tracked), LOADED (the loader, not a container — zero template content lives in Python; the superseded import line `from prioritree.web_structure import UNION_LANES` stays dead), the OUTPUT GENERATED from them (template + context → the served surface, at request time). Autoescape ON (Jinja2Templates' own html-suffix rule — the security floor: user strings never trusted as markup). The loader is LAZY (no construction-time directory check — the acceptance harness's scratch-cwd boot stays green, §5).

**(3) THE STATIC ASSETS' HOME + SERVING: web/static/, authored, served by the child.** app.css (the stylesheet) + app.js (the ENTIRE Web Components surface: the pt-copy click-to-copy component + the data-pt-path submit delegation — the landing's resume/result navigation, navigation JS never validation JS) — AUTHORED files (R9/R10: the JS as a Python string constant was the superseded form's signature; an authored FILE loaded by the base template's script tag is the corrected form — "ALL frontend things generated from Python" now reads per R9's clarification as: loaded/rendered by the Python tier, never imprisoned in it). Serving: `web_app.mount("/static", StaticFiles(directory="web/static", check_dir=False), name="static")` — the brief §3d's ruled form with the one named flag (§5's defect cure). THE CDN PINS' HOME: the base template's head — the authored bytes of web/templates/base.html carry the three tags (Shoelace 2.20.1 theme + autoloader, HTMX 2.0.7) — content-in-configuration at the file tier (the pins ARE content; R10: the template file is the source of truth); the online-at-page-load assumption stays the design §13's priced acceptance.

**(4) THE --CHECK/REGEN DISCIPLINE'S FATE: RETIRED — nothing generated.** With the artifacts become authored source, there is no emission to diff and no regen to stamp: the --check argv dies, the two-line regen header dies, the web-check make target NEVER LANDS (the Makefile at HEAD — five targets — is UNTOUCHED whole), tests/test_web_check.py NEVER LANDS (its 2 arcs die with the generator), the scripts/ coverage growth dies (lint's argv stays `uv run ruff check src/ tests/`; pyright's include stays ["src", "tests"]; the executionEnvironments line never lands; the INP001/T201/S603/S607 scripts-and-check rulings never land). The never-hand-edit law's scope: AUTHORED files are edited by definition (the law binds cycle-GENERATED files — the web tier now carries zero; the tree's own scaffold-regen idiom applies to nothing web).

**(5) THE GENERATOR'S FATE: web_scaffold.py REMOVED (with the removal as the sequence's step 1) — and web_structure.py with it.** The 202-line landed emitter has NO act left: there is nothing to emit (the artifacts are authored), nothing to check (no emission), nothing to stamp (no regen). A reworked generator would be a zombie — its only possible act the reproduction of authored files from a second copy in Python, which IS the superseded form (R9: content-in-Python out of grammar). REMOVAL, both stranded files (§0's tree truth), one step, one read-back (scripts/ gone from the tree — the directory carried only the pair).

**(6) THE FLOOR-SCOPE GROWTH'S FATE: DIES WITH THE GENERATOR.** The brief §1.8's growth (lint argv + pyright include over scripts/) is void — scripts/ is empty after step 1. The floor: make dev, make test, make lint, make typecheck — the Makefile byte-untouched. The rulings that LAND: service.py's per-file-ignores grows PLC0415 (the tail mount's mid-file import — the cycle's only legal form, unchanged by the supersession) + web.py carries BLE001 (the child's fold — the service.py precedent re-carried). Nothing else.

## §2 THE STANDING CONTENT INVENTORY (what survives the supersession whole)

- THE NINE ROUTES + CONTROLLERS: web.py's logic SURVIVES whole — the branch-on-status forms (v1 §5a's uniform error-swap law: FRAGMENTS render refuse.html at 200, fold=True at 500; PAGES render fold.html at the response's own honest status; a page's 404 renders the unknown-run page; the result's 409 renders halt.html at the honest 409 + the render gate's gated withholding at 200), the two-step chain (the vote-ack's embedded hx-trigger="load" pair fetch), the HX-Redirect on DONE, the child's refuse/fold handlers (the mount's price — the union teaching the mounted whole's legal set), the manual form parsing (the wire the sole validator), the no-anchoring law by construction (the count fields UNREAD at every sitting-context controller). The ONLY seams that change: the module docstring (the loader/render seam replaces the emission references) + the static mount's check_dir=False (§5).
- THE SCREENS' CONTENT + THE COPY: SURVIVES whole — now landing in the TEMPLATE FILES as authored bytes (parts 2-3): the landing's register form + the plain-words bridges (moho's breaks closed), the sitting's comparator bridge + the quorum echo, the pair's marked cards + the declared-set buttons, the vote-ack's label-terms restatement + the idempotent echo, the ack's BEGIN THE SITTING + the copy affordances + the share copy, the done page's coverage verbatim, the state strip's 5s poll, the result's ranked whole (competition ranks, tie groups rowspan'd, W/L/T + comparisons, NO win-fraction column, the coverage strip, the cycle neutral + the one-liner, the pair matrix under sl-details, the version footer), the halt's binary (the 409 safe halt / the gated withholding), the unknown/fold pages' ThreePart renders. The @KEY@ sentinel layer is DEAD — the copy lands directly in the files; the {slot} placeholders land as Jinja2 {{ slot }} slots directly.
- THE DEPS: jinja2 LANDS (pyproject dependencies grows "jinja2" — R1's "Jinja2 templating always"; the lock mints it at landing); httpx2 → RUNTIME STANDS (the promotion, dev slimmed to ["pytest", "pyright", "ruff"]; the pin 2.16.2 stands; NEVER `import httpx` — the stale unlocked venv copy; alias_httpx() library-forbidden).
- THE ONE service.py MOUNT: STANDS (the tail import + app.mount("/", web_app) after :528 — the only touch; the PLC0415 named ruling).
- THE 405 RE-TARGET: STANDS (the one test amendment — the mount's price is unchanged by the supersession; the arc re-targets the child's own 405 surface at GET /ui/register).
- THE TEST ARCS: test_web_face.py SURVIVES WHOLE — v1 §6a's file carries 20 test functions (the ledger's "19" corrected at the bytes: the count is 20), and NONE of them assert generator facts (no regen headers, no --check): they assert served markup, which the authored templates render identically (every arc re-verified against the authored files' bytes — the copy substrings, the data-pt-path literals, the no-anchoring pins, the HX-Redirect header, the fold fragment's envelope). The file lands byte-identical to v1 §6a. test_web_check.py's 2 arcs DIE with the generator (retired).

## §3 THE AMENDED BRIEF CLAUSES (the G-WEB-BRIEF re-presentation — the approved brief's superseded clauses replaced; every other clause stands)

- §1.2 THE GENERATOR → AMENDED: RETIRED. No generator exists; the landed 202-line file is REMOVED at step 1. The front end's only writers are its authors (the template files are the source of truth).
- §1.3 THE SOURCE STRUCTURE → AMENDED: SUPERSEDED WHOLE. The content's home moves from the data module INTO the template files themselves (R9/R10);
## Reported by togo — 2026-11-22T17:12:12Z

# THE RETHINK — PART 1, CONTINUED (synthesize/webspec; togo, 2026-11-22 — completing §3's clause list + §4 the gate readings + §5 the defect caught; part 1's §0-§3-head landed in the prior event)

## §3 THE AMENDED BRIEF CLAUSES (continued — the G-WEB-BRIEF re-presentation)

- §1.3 THE SOURCE STRUCTURE → AMENDED: SUPERSEDED WHOLE. The content's home moves from the data module INTO the template files themselves (R9/R10); the landed 563-line web_structure.py is REMOVED at step 1 (the tree truth — §0; the ledger's "never landed" note corrected by disk). No intermediate data module exists: the template files ARE the content (R10's own reconciliation: "the template files ARE the content's home (data, in Jinja's own sense); web.py renders (code); nothing is imprisoned").
- §1.4 THE EMISSION HOME → AMENDED IN KIND: the home STANDS (web/templates/ + web/static/ at the repo root, git-tracked, .gitignore untouched, serving as-is, CWD-relative per the launch discipline) — the KIND changes: generated artifacts → AUTHORED SOURCE (tracked, edited by definition, NO regen stamps, NO --check, no emission).
- §1.8 THE FLOOR'S SCOPE GROWTH (web-check + lint argv scripts/ + pyright include scripts) → AMENDED: RETIRED. The Makefile is UNTOUCHED whole (HEAD's five targets stand); pyproject's include stays ["src", "tests"]; the executionEnvironments line never lands.
- §1.9 THE NAMED RULINGS → AMENDED: the scripts/generation entries (T201, INP001) and test_web_check's S603/S607 NEVER LAND. The rulings that land: "src/prioritree/service.py" grows PLC0415 (the tail import — unchanged by the supersession); "src/prioritree/web.py" carries BLE001 (the child's fold — the service.py precedent re-carried).
- §3d THE EMISSION CHANNEL → AMENDED: the LOADER/RENDER SEAM replaces the emission half — Jinja2Templates(directory="web/templates") (the filesystem loader, autoescape ON) + the StaticFiles mount at /static (check_dir=False, §5's cure); the render at request time (template + context → the surface); zero emission, zero regen, zero stamps. (§3d's loader half was already the corrected form — it stands.)
- §6.2 tests/test_web_check.py → AMENDED: RETIRED (the file never lands; the --check test dies with the check).
- §6.1 test_web_face.py → STANDS WHOLE (the 20 arcs byte-identical; the docstring carries no generator references — verified at v1 §6a's bytes).
- §6.3 the one 405 amendment → STANDS (the arc's re-targeted literals unchanged).
- §2 THE DEPS / §3a THE CLIENT / §3b THE CHILD'S FOLD / §3c THE MOUNT / §3e THE FAMILY-GRAMMAR HANDLERS / §4 THE NINE ROUTES / §5 THE ERROR-SWAP CONTRACT → STAND UNTOUCHED (the router mechanics, the CQRS lanes, the no-anchoring guarantees — none ride the superseded form).
- §8 THE HANDOFF → items 2-3 (the source structure's data shape + the generator's emission discipline) SUPERSEDED by this re-spec's parts 2-3 (the template files whole + the loader seam); items 1/4/5 stand (the exact file inventory — now the AUTHORED files; the exact test literals; the service.py tail's bytes).

## §4 THE GATE READINGS (amendment-pending items for the collaborator — named, never decided silently)

- G-WEB-BRIEF re-presents with §3's amended clauses (the brief's superseded clauses replaced; the fence's surviving clauses carried). The collaborator's approval at the gate rules the amendments.
- G-WEBSPEC-BRIEF's condition 2 as composed ("the spec carries the generator's emission whole — the source structure to the artifacts, the regen/check discipline, the exact new-file contents") rides the SUPERSEDED form; the re-spec carries its corrected content: THE LOADER/RENDER SEAM WHOLE — the template files as AUTHORED SOURCE (each file's whole content, parts 2-3), the loader's form, the controllers' contexts, the static files, ZERO content-in-Python, ZERO generated artifacts (R9/R10's projection law at the bytes level). The gate's green judgment applies the clarified law — the collaborator rules at the presentation.
- G-WEB's condition 2 as composed ("zero hand-authored frontend artifacts on disk") reads THROUGH R9/R10: the authored template/static files ARE the source of truth (in grammar by R9's own letter — "separate template files as the authored source"); the condition's INTENT — no served surface without source, no content imprisoned in Python — is enforced by the architecture itself (zero generated, zero content-in-Python). The collaborator rules this reading at the build gate.
- HYOKA'S ADVERSARIAL PASS rides BEFORE the presentation (the dispatch's own order — the spec-defect history earns it): this re-spec is the pass's input; the convenor dispatches hyoka against it; the gates take the pass's findings. The re-spec names its own caught defect (§5) — the pass attacks the rest.

## §5 THE DEFECT CAUGHT AT THE RE-SETTLE (v1's latent boot-crash — named, cured in the re-spec's bytes)

V1's web.py carried `web_app.mount("/static", StaticFiles(directory=_STATIC_HOME), name="static")` at the MODULE HEAD — and starlette's StaticFiles RAISES RuntimeError at construction when the directory is absent (check_dir=True the default, staticfiles.py:41-57). The acceptance harness boots the service with `Popen(_ARGV, cwd=home)` — home a SCRATCH cwd (tests/test_service_acceptance.py:81, read at this seat): the tail mount imports web.py at boot → the construction fires at the scratch cwd → "web/static" absent → RuntimeError → THE ACCEPTANCE BOOT CRASHES. V1's §8(1) claim ("the acceptance harness unbroken") was WRONG at the mechanism — the probe route is fine (a parent route, matched before the mount), but the BOOT never reaches it. THE ASYMMETRY: the store's CWD-relative home MKDIRS on demand (Serialize's register does the mkdir itself — the scratch-cwd boot is the harness's own isolation mechanism, each home its own .prioritree/runs); StaticFiles RAISES on absent. THE CURE, RULED: `check_dir=False` on the static mount — the construction succeeds at any cwd; at the repo-root launch (the lifecycle targets, the face tests' pytest cwd, kensho's leg) the files serve; at a scratch cwd a static request 404s honestly (the child's family grammar — the request named a path the cwd does not carry). The CWD-relative ruling (the brief §1.4, the STORE_HOME precedent) is HELD — the one flag is the named cure, cited to the harness's own boot form. Jinja2Templates needs no cure: the loader is lazy (no construction-time check; the templates resolve at render — the acceptance arcs ride the JSON routes, never a render).

THE ARCHITECTURE'S HEADLINE: 16 authored frontend files (14 templates + app.css + app.js) + web.py + test_web_face.py land; pyproject/service.py/test_service_face.py edit; BOTH stranded generator files remove; the Makefile untouched; ZERO generated artifacts — the entire front end authored, loaded, rendered. Parts 2-4 carry the bytes whole.
## Reported by togo — 2026-11-22T17:13:03Z

# THE RE-SPEC — PART 2: THE TEMPLATE FILES WHOLE (synthesize/webspec; togo, 2026-11-22 — 14 authored Jinja2 files under web/templates/, each its full content; the copy lands directly in the files — no sentinels, no substitution layer, no regen headers; every extending page's top-level comment is dropped by Jinja at render, the base's and the fragments' ride the served bytes harmlessly)

## §A web/templates/base.html — THE CHROME (the CDN pins' home; every page extends it)

```html
<!DOCTYPE html>
<!-- base — the chrome: the CDN pins (Shoelace 2.20.1 + HTMX 2.0.7), the static tags, the title/content blocks (web-brief §3d; the design §5; R10: the file is the source of truth) -->
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% block title %}Priori-tree{% endblock %}</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.20.1/cdn/themes/light.css">
  <script type="module" src="https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.20.1/cdn/shoelace-autoloader.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.7/dist/htmx.min.js"></script>
  <link rel="stylesheet" href="/static/app.css">
  <script type="module" src="/static/app.js"></script>
</head>
<body>
<main class="wrap">
{% block content %}{% endblock %}
</main>
</body>
</html>
```

## §B web/templates/landing.html — THE LANDING (route 1, call-free; moho's bridges whole)

```html
{% extends "base.html" %}
{% block title %}Priori-tree — begin{% endblock %}
{% block content %}
<section class="card">
  <h1>Priori-tree</h1>
  <p>Priori-tree turns easy pairwise judgments into a reliable ranking. You register a list, then judge the items two at a time — the site tallies your judgments into a superior order.</p>
  <p>Each pair is judged with three answers: prefer the first, prefer the second, or a tie.</p>
</section>
<section class="card">
  <h2>Register a run</h2>
  <form hx-post="/ui/register" hx-target="#register-result" hx-swap="innerHTML">
    <label>Your name for yourself on this run. <input name="operator_id" required minlength="1"></label>
    <label>The question to answer. <input name="question" required minlength="1"></label>
    <label>How many judgments each pair needs — 1 means just you; 2 or more means you need other judges, and a pair stays open until it has them. <input type="number" name="quorum" value="1" min="1"></label>
    <fieldset>
      <legend>The items — an id and a label for each. The first two rows are required; the list is locked once registered.</legend>
      <div class="item-row"><input name="item-id" required minlength="1" placeholder="id"> <input name="item-label" required minlength="1" placeholder="label"></div>
      <div class="item-row"><input name="item-id" required minlength="1" placeholder="id"> <input name="item-label" required minlength="1" placeholder="label"></div>
      <div class="item-row"><input name="item-id" placeholder="id"> <input name="item-label" placeholder="label"></div>
      <div class="item-row"><input name="item-id" placeholder="id"> <input name="item-label" placeholder="label"></div>
      <div class="item-row"><input name="item-id" placeholder="id"> <input name="item-label" placeholder="label"></div>
      <div class="item-row"><input name="item-id" placeholder="id"> <input name="item-label" placeholder="label"></div>
    </fieldset>
    <button type="submit">Register the run</button>
  </form>
  <div id="register-result"></div>
</section>
<section class="card">
  <h2>Resume</h2>
  <form method="get" action="/" data-pt-path="/runs/{stem}">
    <label>Have a run id? Resume its sitting. <input name="stem" placeholder="RUN-0001"></label>
    <button type="submit">Resume the sitting</button>
  </form>
  <p class="quiet">The run id looks like RUN-0001 — it was shown when the run was registered.</p>
  <form method="get" action="/" data-pt-path="/runs/{stem}/result">
    <label>Have a run id? See its result. <input name="stem" placeholder="RUN-0001"></label>
    <button type="submit">See the result</button>
  </form>
</section>
{% endblock %}
```

## §C web/templates/sitting.html — THE SITTING (route 2; the first pair server-side via the include; the count never rendered)

```html
{% extends "base.html" %}
{% block title %}Priori-tree — the sitting{% endblock %}
{% block content %}
<section class="card">
  <h1>{{ question }}</h1>
  <label for="comparator-id">Your name for yourself as a judge — it stamps your votes. The same entry rides every judgment you cast on this page.</label>
  <input id="comparator-id" name="comparator_id" required minlength="1">
  {% if quorum > 1 %}<p class="quiet">Each pair needs {{ quorum }} judgments — you may see pairs you already judged until every pair has {{ quorum }} judgments.</p>{% endif %}
  {% include "pair.html" %}
  <div id="ack-region"></div>
</section>
{% endblock %}
```

## §D web/templates/pair.html — THE PAIR FRAGMENT (routes 2+7's shared pair region; the buttons from the DECLARED set; the button↔card tie by the markers)

```html
<!-- pair — the shared pair region: the sitting includes it, the fragment route serves it (web-brief §4 routes 2+7; the design §7a) -->
<div id="pair-region">
  <form hx-post="/ui/runs/{{ stem }}/vote" hx-target="#ack-region" hx-swap="innerHTML" hx-include="[name='comparator_id']">
    <input type="hidden" name="item_a" value="{{ item_a }}">
    <input type="hidden" name="item_b" value="{{ item_b }}">
    <div class="cards">
      <sl-card class="pair-card"><sl-badge slot="header">A</sl-badge><span class="card-label">{{ label_a }}</span></sl-card>
      <sl-card class="pair-card"><sl-badge slot="header">B</sl-badge><span class="card-label">{{ label_b }}</span></sl-card>
    </div>
    <div class="verdicts">
      {% set labels = {"prefer-a": "Prefer A", "prefer-b": "Prefer B", "tie": "Tie"} %}
      {% for verdict in verdicts %}<button class="verdict" name="winner" value="{{ verdict }}">{{ labels.get(verdict, verdict) }}</button>{% endfor %}
    </div>
  </form>
</div>
```

## §E web/templates/vote-ack.html — THE VOTE ACK FRAGMENT (route 8; the two-step chain's head; the count never rendered)

```html
<!-- vote-ack — the verdict restated in item-label terms + the embedded pair fetch (web-brief §4 route 8; the design §7a) -->
<div id="vote-ack">
  <p class="ack-line">{% if winner == 'prefer-a' %}You preferred {{ label_a }} (A) over {{ label_b }} (B).{% elif winner == 'prefer-b' %}You preferred {{ label_b }} (B) over {{ label_a }} (A).{% else %}Tie: {{ label_a }} (A) and {{ label_b }} (B) stand equal.{% endif %}</p>
  {% if not acknowledged %}<p class="quiet">This pair was already recorded with the same answer — it stands once.</p>{% endif %}
  <div hx-get="/ui/runs/{{ stem }}/pair" hx-trigger="load" hx-target="#pair-region" hx-swap="outerHTML"></div>
</div>
```

## §F web/templates/ack.html — THE REGISTER ACK FRAGMENT (route 6; the copy affordances; the share copy at quorum>1)

```html
<!-- ack — the register ack: the begin link, the run id + sitting URL with click-to-copy, the frozen warning (web-brief §4 route 6; the design §7b) -->
<div id="register-ack">
  <p><strong>Run registered.</strong></p>
  <p>The run id: <strong>{{ run_id }}</strong> <pt-copy value="{{ run_id }}" label="Copy run id"></pt-copy></p>
  <p>The sitting URL: <code>{{ sitting_url }}</code> <pt-copy value="{{ sitting_url }}" label="Copy sitting URL"></pt-copy></p>
  {% if quorum > 1 %}<p class="share">Each pair needs {{ quorum }} judgments — share this sitting URL with your other judges.</p>{% endif %}
  <p class="quiet">The list is locked once registered — a changed list is a new run.</p>
  <sl-button variant="primary" href="/runs/{{ run_id }}">BEGIN THE SITTING</sl-button>
</div>
```

## §G web/templates/state-strip.html — THE STATE STRIP FRAGMENT (routes 4+9; the 5s poll's swap target, the trigger re-armed)

```html
<!-- state-strip — the census read verbatim, the poll re-armed (web-brief §4 routes 4+9; the design §8) -->
<div id="state-strip" hx-get="/ui/runs/{{ stem }}/state" hx-trigger="every 5s" hx-swap="outerHTML">
  <p>Judgments recorded: <strong>{{ total }}</strong></p>
  <ul class="involvement">
    {% for item_id, involvement in items.items() %}<li>{{ item_id }}: {{ involvement }}</li>{% endfor %}
  </ul>
  <p class="quiet">This strip refreshes every 5 seconds.</p>
</div>
```

## §H web/templates/refuse.html — THE ONE REFUSAL RENDERER (the fragment inventory's refusal member, never its own route; the fold flag's heading swap)

```html
<!-- refuse — the ThreePart fields labeled verbatim + the fold heading swap (web-brief §5; R5; the design §4) -->
<div class="refusal">
  <p><strong>{% if fold %}Something broke — the fold's three fields:{% else %}The request was refused — the wire's own three fields:{% endif %}</strong></p>
  <dl class="three-part">
    <dt>Expected</dt><dd>{{ fields.expected }}</dd>
    <dt>Found</dt><dd>{{ fields.found }}</dd>
    <dt>Next action</dt><dd>{{ fields.next_action }}</dd>
  </dl>
</div>
```

## §I web/templates/done.html — THE DONE PAGE (route 3; the DONE body's expected VERBATIM)

```html
{% extends "base.html" %}
{% block title %}Priori-tree — done{% endblock %}
{% block content %}
<section class="card">
  <h1>The sitting is complete.</h1>
  <sl-badge variant="success">done</sl-badge>
  <p class="coverage">{{ fields.expected }}</p>
  <p>The run is complete — each pair has its judgments.</p>
  <sl-button variant="primary" href="/runs/{{ stem }}/result">See the result</sl-button>
</section>
{% endblock %}
```

## §J web/templates/progress.html — THE PROGRESS PAGE (route 4; the operator's deliberate navigation)

```html
{% extends "base.html" %}
{% block title %}Priori-tree — progress{% endblock %}
{% block content %}
<section class="card">
  <h1>The run's progress.</h1>
  {% include "state-strip.html" %}
</section>
{% endblock %}
```

## §K web/templates/result.html — THE RANKED WHOLE (route 5; the render gate's other branch lives in halt.html; NO win-fraction column anywhere — R10 at the glass; the pairs re-split on "|")

```html
{% extends "base.html" %}
{% block title %}Priori-tree — the result{% endblock %}
{% block content %}
<section class="card">
  <h1>The ranked whole.</h1>
  <sl-badge variant="success">done</sl-badge>
  <table class="ranked">
    <thead><tr><th>Rank</th><th>Item</th><th>W</th><th>L</th><th>T</th><th>Comparisons</th></tr></thead>
    <tbody>
      {% for rank, group in ranked %}{% set outer = loop %}{% for item in group %}
      <tr>
        {% if outer.first %}<td rowspan="{{ group | length }}">{{ rank }}</td>{% endif %}
        <td>{{ rows[item].label }} <sl-badge>{{ item }}</sl-badge></td>
        <td>{{ rows[item].wins }}</td>
        <td>{{ rows[item].losses }}</td>
        <td>{{ rows[item].ties }}</td>
        <td>{{ rows[item].wins + rows[item].losses + rows[item].ties }}</td>
      </tr>
      {% endfor %}{% endfor %}
    </tbody>
  </table>
  <p class="coverage-strip">Every scheduled pair at quorum — the comparison graph is connected ({{ components | length }} component).</p>
  {% if cycle %}
  <p>
    <sl-tag>A cycle is named in the coverage data:</sl-tag>
    <sl-tooltip content="This cycle is structural, never an error, never resolved by judgment — the wins, losses, and ties in the table are the honest numbers behind each item's position.">
      {% for edge in cycle %}{{ edge[0] }} &gt; {{ edge[1] }}{% if not loop.last %}, {% endif %}{% endfor %}
    </sl-tooltip>
  </p>
  {% endif %}
  <sl-details summary="The coverage datum">
    <p>The pair matrix — judgments per pair:</p>
    <ul>
      {% for pair, count in pair_counts.items() %}<li>{{ pair.split("|")[0] }} vs {{ pair.split("|")[1] }}: {{ count }}</li>{% endfor %}
    </ul>
  </sl-details>
  <footer><sl-badge>{{ algorithm_version }}</sl-badge> — Ranked by {{ algorithm_version }}</footer>
</section>
{% endblock %}
```

NOTE (the context's shape, pinned for the execution seat): `ranked` is a list of (rank, [ids]) pairs in group order; `rows` is a DICT keyed by item id — v1 part 1 built rows as a LIST while part 2's template subscripted `rows[item]` (a render-time TypeError — v1's own latent inconsistency, caught at the re-settle); the re-spec's web.py (part 3) builds rows as the dict this template subscripts. The pairs' keys arrive from the wire re-keyed "item_a|item_b" (the seam's ruled elision form) — the template re-splits on "|" for the honest reading (the brief §4 route 5's own clause).

## §L web/templates/halt.html — THE BINARY PAGE (route 5's 409 safe halt / the render gate's gated withholding; R12 — never a partial ranking dressed as whole)

```html
{% extends "base.html" %}
{% block title %}Priori-tree — not ready{% endblock %}
{% block content %}
<section class="card">
  <h1>{% if gated %}The ranking is not complete.{% else %}The ranking is not ready.{% endif %}</h1>
  {% if gated %}<sl-badge variant="neutral">withheld</sl-badge><p>The ranking will not be shown until every pair has its judgments — never a partial ranking dressed as whole.</p>{% else %}<sl-badge variant="warning">safe halt</sl-badge>
  <dl class="three-part">
    <dt>Expected</dt><dd>{{ fields.expected }}</dd>
    <dt>Found</dt><dd>{{ fields.found }}</dd>
    <dt>Next action</dt><dd>{{ fields.next_action }}</dd>
  </dl>
  <ul>
    <li>Bridging pairs — connectivity needs NEW comparisons: a comparator provides them — sit again (the resume link serves exactly the named closing pairs); the solo operator re-sits under a NEW comparator id (a new id's judgments are new samples — a changed verdict is a new sample).</li>
    <li>Shortfall pairs — quorum needs MORE VOTES: more judgments from any comparator — existing judges (a changed verdict is a new sample) or new ones (share the sitting URL).</li>
  </ul>{% endif %}
  <sl-button variant="primary" href="/runs/{{ stem }}">Resume the sitting</sl-button>
  <a href="/runs/{{ stem }}/progress">See the run's progress</a>
</section>
{% endblock %}
```

## §M web/templates/unknown.html — THE UNKNOWN-RUN PAGE (every page route's 404 branch; the wire's own found field verbatim)

```html
{% extends "base.html" %}
{% block title %}Priori-tree — unknown run{% endblock %}
{% block content %}
<section class="card">
  <h1>Unknown run.</h1>
  <p>No run answers this address — the wire's own report:</p>
  <p class="wire-found">{{ fields.found }}</p>
  <form method="get" action="/" data-pt-path="/runs/{stem}">
    <label>Have a run id? Resume its sitting. <input name="stem" placeholder="RUN-0001"></label>
    <button type="submit">Resume the sitting</button>
  </form>
  <p class="quiet">The run id looks like RUN-0001 — it was shown when the run was registered.</p>
</section>
{% endblock %}
```

## §N web/templates/fold.html — THE FOLD PAGE (the pages' honest non-404 error branch; the child's own fold page lane)

```html
{% extends "base.html" %}
{% block title %}Priori-tree — the fold{% endblock %}
{% block content %}
<section class="card">
  <h1>The request failed.</h1>
  <dl class="three-part">
    <dt>Expected</dt><dd>{{ fields.expected }}</dd>
    <dt>Found</dt><dd>{{ fields.found }}</dd>
    <dt>Next action</dt><dd>{{ fields.next_action }}</dd>
  </dl>
</section>
{% endblock %}
```

THE COUNT: 14 template files — the base (§A) + the 8 screens (landing §B, sitting §C, done §I, progress §J, result §K, halt §L, unknown §M, fold §N) + the 5 fragments (pair §D, vote-ack §E, ack §F, state-strip §G, refuse §H — the ONE refusal renderer). Part 3 carries the static pair + web.py whole.
## Reported by togo — 2026-11-22T17:13:41Z

# THE RE-SPEC — PART 3: THE STATIC PAIR + THE WEB MODULE WHOLE (synthesize/webspec; togo, 2026-11-22 — the authored static files + src/prioritree/web.py's every line; the loader/render seam per R9/R10; v1's three defects cured: the union import dead, the rows-list/render-subscript inconsistency, the static mount's check-dir boot-crash)

## §O web/static/app.css — THE STYLESHEET (authored; the semantic table's own styling — Shoelace ships no table component)

```css
/* app.css — the web tier's stylesheet (web-brief §3d; the design §5 — authored source per R9/R10) */
:root { --pt-gap: 0.75rem; }
body { margin: 0; font-family: system-ui, sans-serif; background: #fafafa; color: #1a1a1a; }
.wrap { max-width: 40rem; margin: 0 auto; padding: var(--pt-gap); }
.card { background: white; border-radius: 0.5rem; padding: var(--pt-gap); margin-bottom: var(--pt-gap); }
label { display: block; margin: 0.5rem 0; }
input { display: block; width: 100%; box-sizing: border-box; padding: 0.4rem; margin-top: 0.2rem; }
.item-row input { display: inline-block; width: calc(50% - 0.25rem); }
.cards { display: flex; gap: var(--pt-gap); margin: var(--pt-gap) 0; }
.pair-card { flex: 1; }
.card-label { font-size: 1.1rem; }
.verdicts { display: flex; gap: var(--pt-gap); flex-wrap: wrap; }
button.verdict { padding: 0.6rem 1.2rem; }
table.ranked { border-collapse: collapse; width: 100%; margin: var(--pt-gap) 0; }
table.ranked th, table.ranked td { border: 1px solid #ddd; padding: 0.4rem; text-align: left; }
table.ranked th { background: #f0f0f0; }
.coverage-strip { color: #666; }
.three-part dt { font-weight: bold; margin-top: 0.5rem; }
.three-part dd { margin: 0; }
.wire-found { font-family: monospace; background: #f4f4f4; padding: 0.5rem; border-radius: 0.3rem; }
.quiet { color: #666; }
.share { background: #eef6ff; padding: 0.5rem; border-radius: 0.3rem; }
.refusal { background: #fff7f0; border-left: 3px solid #e67e22; padding: var(--pt-gap); }
#state-strip { background: #f4f4f4; padding: var(--pt-gap); border-radius: 0.3rem; }
.involvement { columns: 2; margin: 0.5rem 0; }
.ack-line { font-size: 1.1rem; }
footer { color: #666; margin-top: var(--pt-gap); }
```

## §P web/static/app.js — THE WEB COMPONENTS SURFACE (authored; pt-copy the click-to-copy affordance + the data-pt-path submit delegation — navigation JS, never validation JS: the wire stays the sole validator)

```js
// app.js — the web tier's Web Components: pt-copy + the data-pt-path navigation delegation (web-brief §4 route 1; the design §5 — authored source per R9/R10)
class PtCopy extends HTMLElement {
  connectedCallback() {
    const value = this.getAttribute("value") ?? "";
    const label = this.getAttribute("label") ?? "Copy";
    const button = document.createElement("sl-button");
    button.textContent = label;
    button.addEventListener("click", () => {
      navigator.clipboard.writeText(value);
      button.textContent = "Copied";
      window.setTimeout(() => { button.textContent = label; }, 2000);
    });
    this.replaceChildren(button);
  }
}
customElements.define("pt-copy", PtCopy);
document.addEventListener("submit", (event) => {
  const form = event.target;
  const path = form.getAttribute("data-pt-path");
  if (path === null) { return; }
  event.preventDefault();
  const stem = form.querySelector("input[name='stem']").value.trim();
  if (stem) { window.location.assign(path.replace("{stem}", encodeURIComponent(stem))); }
});
```

## §Q src/prioritree/web.py — THE WEB MODULE, WHOLE (new file; the five-field docstring law; the naming law on every symbol; the loader/render seam at the module head)

```python
# Copyright (C) 2026 Mark Losey. All rights reserved.
"""web — the web fronts: the child app over the service's wire, the nine routes.

The web unit (web-brief §1.1 + the approved design §8, re-settled per
Q-ux-surface R9/R10 — the template-source law): the CHILD application
(FastAPI with the docs routes disabled — the web tier is the human's
surface, not an API), mounted at the service app's TAIL (service.py's mount
line, the one touch); the nine routes (5 pages at honest statuses + 4
rendering fragments at 200); the in-process service client (httpx2
.AsyncClient over ASGITransport against the imported service app —
raise_app_exceptions=False REQUIRED: the service fold sends its envelope
then always re-raises, and the fold case needs the envelope RETURNED, rikai
finding 1 ruled); THE LOADER/RENDER SEAM (R10's three beats): the front
end's content lives in AUTHORED FILES — the Jinja2 templates under
web/templates/ (each file the source of truth for its surface, edited by
definition — the never-hand-edit law's scope never reaches them) and the
static assets under web/static/ (app.css + the Web Components app.js) —
and THIS module LOADS them (Jinja2Templates' filesystem loader + the
StaticFiles mount) and GENERATES the served surface from them at request
time (template + context -> the page); ZERO template content lives in
Python (no string constants, no giant concatenations — the superseded
web_structure.py form out of grammar), ZERO generated artifacts (nothing
emits, nothing regens, no --check). The CWD-relative homes ride the
repo-root launch discipline (STORE_HOME run_store.py:53 the precedent);
the static mount's check_dir=False is the named cure for the acceptance
harness's scratch-cwd boot (StaticFiles raises at import on an absent
directory; the store mkdirs on demand — the asymmetry named at the
re-settle). The child's OWN fold + refuse handlers (the mount's price:
after the tail mount every path the parent does not fully match lands on
the child — starlette routing.py serves the FIRST FULL match and the
Mount matches FULL on path alone, so the child owns the unmatched-path and
disallowed-method surface; its refuse handler renders the IDENTICAL family
grammar as a JSONResponse so the pinned parent-face arcs survive
unedited); the no-anchoring law held by construction (the count fields are
UNREAD at every sitting-context controller — they never enter a render
context); the fragment routes parse form bodies MANUALLY (no typed Form
fields: FastAPI's validation 422 would emit outside the family grammar,
and the fragment tier holds no 4xx — the wire is the sole validator). All
imports via fastapi/starlette's re-export surface + httpx2 (the lock's
name — NEVER `import httpx`, the stale unlocked venv copy; alias_httpx()
library-forbidden). Five-field docstrings on every public symbol;
content-in-configuration (the paths and template names named constants); no
asserts, no prints.
"""

from __future__ import annotations

from typing import Any, Final

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

import httpx2

from prioritree.service import ESCALATION, app as service_app

__all__ = ["web_app"]

# The web tier's named constants (content-in-configuration): the route paths
# (the child's own surface, collision-free against the service's six), the
# authored homes (CWD-relative, the repo-root launch discipline), the
# in-process client's base URL (httpx demands absolute URLs — a literal the
# transport ignores: no socket, no port, no second process).
_LANDING: Final[str] = "/"
_SITTING: Final[str] = "/runs/{stem}"
_DONE: Final[str] = "/runs/{stem}/done"
_PROGRESS: Final[str] = "/runs/{stem}/progress"
_RESULT: Final[str] = "/runs/{stem}/result"
_REGISTER: Final[str] = "/ui/register"
_PAIR: Final[str] = "/ui/runs/{stem}/pair"
_VOTE: Final[str] = "/ui/runs/{stem}/vote"
_STATE_STRIP: Final[str] = "/ui/runs/{stem}/state"
_TEMPLATES_HOME: Final[str] = "web/templates"
_STATIC_HOME: Final[str] = "web/static"
_BASE_URL: Final[str] = "http://prioritree.internal"
_OK: Final[int] = 200
_CREATED: Final[int] = 201
_NOT_FOUND: Final[int] = 404
_METHOD_NOT_ALLOWED: Final[int] = 405
_CONFLICT: Final[int] = 409
_CRASH: Final[int] = 500
_SEE_OTHER: Final[int] = 303
_FRAGMENT_LANE: Final[str] = "/ui/"

# The mounted whole's legal set (web-brief §3e): the nine web routes (the
# child's own path constants above) + the six service routes (the frozen
# wire's literals, cited) — the child's refusal handler teaches the whole
# face honestly.
_WEB_LANES: Final[tuple[str, ...]] = (
    f"GET {_LANDING}",
    f"GET {_SITTING}",
    f"GET {_DONE}",
    f"GET {_PROGRESS}",
    f"GET {_RESULT}",
    f"POST {_REGISTER}",
    f"GET {_PAIR}",
    f"POST {_VOTE}",
    f"GET {_STATE_STRIP}",
)
_SERVICE_LANES: Final[tuple[str, ...]] = (
    "POST /runs",
    "GET /runs/{run_id}/next",
    "POST /runs/{run_id}/votes",
    "GET /runs/{run_id}/state",
    "GET /runs/{run_id}/tally",
    "GET /runs/{run_id}/manifest",
)
UNION_LANES: Final[str] = "address a legal route — " + ", ".join(_WEB_LANES + _SERVICE_LANES)

# The child app (web-brief §3e: the docs routes DISABLED — the parent's own
# /docs, /redoc, /openapi.json stay live, registered before the mount). The
# static mount's check_dir=False: the acceptance harness boots at a scratch
# cwd (test_service_acceptance.py:81 — Popen(cwd=home)); StaticFiles raises
# at construction on an absent directory, the store mkdirs on demand — the
# flag is the asymmetry's named cure (the re-settle's §5).
web_app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
web_app.mount("/static", StaticFiles(directory=_STATIC_HOME, check_dir=False), name="static")
templates = Jinja2Templates(directory=_TEMPLATES_HOME)

# THE IN-PROCESS CLIENT (web-brief §3a, ruled exact): ONE module-level
# instance, built at import against the imported service app, shared by all
# controllers, process-lifetime — no per-request construction, no teardown
# (ASGITransport holds no socket). raise_app_exceptions=False REQUIRED.
_client = httpx2.AsyncClient(
    base_url=_BASE_URL,
    transport=httpx2.ASGITransport(app=service_app, raise_app_exceptions=False),
)


async def _service(method: str, path: str, json: Any | None = None) -> httpx2.Response:
    """Call the service over the in-process client — the one service path.

    Purpose: every controller's service lane rides this one call (the layering
    held mechanically: the web tier is a true HTTP client of the service
    surface over the same app — its stack, its fold, its door).
    Refuses when: never — the response (any status) IS the return.
    Re-run: deterministic given the store state.
    Touches: nothing — the transport is in-process.
    Provenance: web-brief §3a (the async form), rikai finding 1, G-WEB.
    """
    return await _client.request(method, path, json=json)


def _labels(manifest: dict[str, Any]) -> dict[str, str]:
    """Map the manifest's items to labels — the id->label law (design §7a).

    Purpose: build {id: label} from the manifest body's [[id, label], ...]
    rows — the sitting cards and the ranked whole render labels, ids the
    stable key; an id absent from the map falls back to the id itself.
    Refuses when: never — a pure projection over the manifest's own rows.
    Re-run: deterministic.
    Touches: nothing.
    Provenance: the design §2 (the sixth query's response form), §7a, G-WEB.
    """
    return {str(row[0]): str(row[1]) for row in manifest["items"]}


def _fields(body: dict[str, Any]) -> dict[str, str]:
    """Read a ThreePart body's three fields as data — the one read point.

    Purpose: the service wire's every refusal (and the DONE state's own
    three fields) carries expected/found/next_action; this one function
    reads them as data for the render contexts — never re-derived (the body
    is the source, the web renders, never authors).
    Refuses when: never — a pure read over the body's own keys.
    Re-run: deterministic.
    Touches: nothing.
    Provenance: R5 (the ThreePart mandate), web-brief §5, G-WEB.
    """
    return {
        "expected": str(body["expected"]),
        "found": str(body["found"]),
        "next_action": str(body["next_action"]),
    }


def _unknown(request: Request, body: dict[str, Any]) -> Response:
    """Render the unknown-run page at the honest 404.

    Purpose: every page route's unknown-stem branch — the landing's resume
    affordance + the wire's own found field (the live set, verbatim).
    Refuses when: never — the 404 IS the input; the page renders honestly.
    Re-run: deterministic.
    Touches: nothing.
    Provenance: web-brief §5 (the 404 page), the design §4, G-WEB.
    """
    return templates.TemplateResponse(
        request, "unknown.html", {"fields": _fields(body)}, status_code=_NOT_FOUND
    )


def _refuse_fragment(request: Request, fields: dict[str, str], fold: bool = False) -> Response:
    """Render the ONE refusal renderer as a fragment at 200.

    Purpose: the fragment inventory's refusal member (never its own route):
    the three fields labeled verbatim + the cure affordance beside them, at
    200 — core HTMX swaps it; the refusal is SEEN, never a silent OK. The
    fold flag renders the crash envelope's wording (the fragment controller
    receiving 500, or itself raising — the same renderer, the envelope's
    three fields).
    Refuses when: never — the refusal IS the input; the fragment renders.
    Re-run: deterministic.
    Touches: nothing.
    Provenance: web-brief §5 (the 422/400 inline refusal + the fold
    fragment), the design §4, R5, G-WEB.
    """
    return templates.TemplateResponse(
        request, "refuse.html", {"fields": fields, "fold": fold}, status_code=_OK
    )


@web_app.exception_handler(StarletteHTTPException)
def refuse(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    """Refuse the child's framework HTTP exceptions in the family grammar — 404/405 taught.

    Purpose: the mount's price, ruled (web-brief §3e): the child owns every
    path the parent does not fully match — this handler renders the
    IDENTICAL family grammar as the parent's shadowed handler, as a
    JSONResponse (the pinned parent-face arcs assert the JSON body):
    expected the method + path as addressed, found the routing violation
    named (404: no route matches the path; 405: the method not allowed at
    the path), next_action the MOUNTED WHOLE's legal set (the nine web
    routes + the six service routes, from the module's own union — the
    mounted whole IS the tree's HTTP face). The status rides
    exc.status_code verbatim — machine-dispatchable.
    Refuses when: never — the handler renders; the framework's refusal IS
    the input (exc.status_code + exc.detail, never re-derived).
    Re-run: deterministic — the same request renders the same body.
    Touches: nothing.
    Provenance: web-brief §3e (the child's own handler), R5, G-WEBSPEC-BRIEF.
    """
    _address = f"{request.method} {request.url.path}"
    if exc.status_code == _NOT_FOUND:
        _found = f"no route matches the path {request.url.path}"
    elif exc.status_code == _METHOD_NOT_ALLOWED:
        _found = f"the method {request.method} is not allowed at the path {request.url.path}"
    else:
        _found = str(exc.detail)
    return JSONResponse(
        status_code=exc.status_code,
        content={"expected": _address, "found": _found, "next_action": UNION_LANES},
    )


@web_app.exception_handler(Exception)
def fold(request: Request, exc: Exception) -> Response:
    """Fold the child's own escapes — the web app's last resort, in the family grammar.

    Purpose: the child is a SEPARATE application (own middleware stack; the
    parent's fold never re-sends once the child's response started) — this
    handler is the child's own catch-all: expected the attempted act, found
    the exception's type + message verbatim, next_action the service fold's
    own ESCALATION constant. FRAGMENT lane (/ui/*): the fold fragment at
    200 (the sitting context preserved — the fold is SEEN, never a stale
    screen). PAGE lane: the honest 500 page. BLE001 rides the named
    pyproject ruling (the service.py precedent re-carried at the child).
    Refuses when: never — the crash IS the input; the handler renders,
    never re-raises.
    Re-run: deterministic in form.
    Touches: nothing.
    Provenance: web-brief §3b (the child's own fold), Q-error-teaching,
    G-WEBSPEC-BRIEF.
    """
    _fields_fold = {
        "expected": f"{request.method} {request.url.path}",
        "found": f"{type(exc).__name__}: {exc}",
        "next_action": ESCALATION,
    }
    if request.url.path.startswith(_FRAGMENT_LANE):
        return _refuse_fragment(request, _fields_fold, fold=True)
    return templates.TemplateResponse(
        request, "fold.html", {"fields": _fields_fold}, status_code=_CRASH
    )


@web_app.get(_LANDING)
async def landing(request: Request) -> Response:
    """Land the operator — the register form + the plain-words bridges, no service calls.

    Purpose: the static landing: the register form (operator id, stated
    question, quorum, six item rows, the resume field, the direct-result
    field), the site's explanation, the vocabulary statement, the jargon
    bridges — every copy string AUTHORED IN THE LANDING TEMPLATE
    (content-in-configuration at the file tier: the template file IS the
    content's home — R10). The form hx-posts to the register fragment; the
    resume + result fields navigate via the data-pt-path submit delegation
    (the Web Components surface — app.js, the authored static file).
    Refuses when: never — a static render.
    Re-run: deterministic.
    Touches: nothing — no service call (the only call-free route).
    Provenance: web-brief §4 route 1, the design §7/§8, G-WEBSPEC-BRIEF.
    """
    return templates.TemplateResponse(request, "landing.html", {})


@web_app.get(_SITTING)
async def sitting(request: Request, stem: str) -> Response:
    """Sit the comparator — the question as prompt, the first pair server-side.

    Purpose: consume the manifest (the question, the declared verdicts, the
    quorum) + next (the FIRST PAIR rendered server-side — a pure query
    render; the two-step law bars the POST's RESPONSE from carrying the
    pair, never the page's query). Cards A/B marked + labeled (the label
    map); the count UNREAD — never in the render context (the no-anchoring
    law, by construction). DONE => redirect to the done page; 404 => the
    unknown-run page at the honest 404; any other non-200 => the fold page
    at the response's own status. The buttons hx-post the vote; the
    comparator entry rides every post.
    Refuses when: never by this hand — the branches render honestly.
    Re-run: deterministic given the store state.
    Touches: nothing — queries only.
    Provenance: web-brief §4 route 2, the design §7a/§8, G-WEBSPEC-BRIEF.
    """
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code != _OK:
        if manifest.status_code == _NOT_FOUND:
            return _unknown(request, manifest.json())
        return templates.TemplateResponse(
            request, "fold.html", {"fields": _fields(manifest.json())}, status_code=manifest.status_code
        )
    nxt = await _service("GET", f"/runs/{stem}/next")
    if nxt.status_code != _OK:
        if nxt.status_code == _NOT_FOUND:
            return _unknown(request, nxt.json())
        return templates.TemplateResponse(
            request, "fold.html", {"fields": _fields(nxt.json())}, status_code=nxt.status_code
        )
    body = nxt.json()
    if body.get("done"):
        return RedirectResponse(f"/runs/{stem}/done", status_code=_SEE_OTHER)
    manifest_body = manifest.json()
    labels = _labels(manifest_body)
    return templates.TemplateResponse(
        request,
        "sitting.html",
        {
            "stem": stem,
            "question": str(manifest_body["question"]),
            "verdicts": list(manifest_body["verdicts"]),
            "quorum": int(manifest_body["quorum"]),
            "item_a": str(body["item_a"]),
            "item_b": str(body["item_b"]),
            "label_a": labels.get(str(body["item_a"]), str(body["item_a"])),
            "label_b": labels.get(str(body["item_b"]), str(body["item_b"])),
        },
    )


@web_app.get(_DONE)
async def done(request: Request, stem: str) -> Response:
    """State the run's coverage honestly — the DONE body's expected verbatim.

    Purpose: consume next (the DONE body — a VALUE, never an error):
    done:true => the coverage statement (the body's expected field VERBATIM —
    "all {N} scheduled pairs at quorum k={K}" — + the plain-words restatement
    + the result link); a pair body (the re-opened edge — the signal is a
    state read, not a latch) => redirect to the sitting page; 404 => the
    unknown-run page; any other non-200 => the fold page at the response's
    own status.
    Refuses when: never by this hand.
    Re-run: deterministic given the store state.
    Touches: nothing — a query.
    Provenance: web-brief §4 route 3, the design §7c, G-WEBSPEC-BRIEF.
    """
    nxt = await _service("GET", f"/runs/{stem}/next")
    if nxt.status_code != _OK:
        if nxt.status_code == _NOT_FOUND:
            return _unknown(request, nxt.json())
        return templates.TemplateResponse(
            request, "fold.html", {"fields": _fields(nxt.json())}, status_code=nxt.status_code
        )
    body = nxt.json()
    if not body.get("done"):
        return RedirectResponse(f"/runs/{stem}", status_code=_SEE_OTHER)
    return templates.TemplateResponse(
        request, "done.html", {"stem": stem, "fields": _fields(body)}, status_code=_OK
    )


@web_app.get(_PROGRESS)
async def progress(request: Request, stem: str) -> Response:
    """Show the operator the census — the state read verbatim, the 5s poll armed.

    Purpose: the OPERATOR's deliberate navigation (never linked from the
    sitting surface): consume state ({"total", "items"} — per_pair_counts
    stays elided at the seam, never resurrected), render the census
    verbatim; the state-strip region carries hx-get to the state fragment
    with the every-5s trigger. 404 => the unknown-run page; any other
    non-200 => the fold page at the response's own status.
    Refuses when: never by this hand.
    Re-run: deterministic given the store state.
    Touches: nothing — a query.
    Provenance: web-brief §4 route 4, the design §8, G-WEBSPEC-BRIEF.
    """
    result = await _service("GET", f"/runs/{stem}/state")
    if result.status_code != _OK:
        if result.status_code == _NOT_FOUND:
            return _unknown(request, result.json())
        return templates.TemplateResponse(
            request, "fold.html", {"fields": _fields(result.json())}, status_code=result.status_code
        )
    body = result.json()
    return templates.TemplateResponse(
        request,
        "progress.html",
        {"stem": stem, "total": int(body["total"]), "items": dict[str, int](body["items"])},
    )


@web_app.get(_RESULT)
async def result(request: Request, stem: str) -> Response:
    """Render the ranked whole, or the safe halt at the honest 409 — the binary held.

    Purpose: consume tally + manifest. 200 => THE RANKED WHOLE (the render
    gate: a body with groups but done:false REFUSES to render — the gated
    branch renders halt.html's withholding with the honest affordances):
    the semantic table, competition ranks (1, 2, 2, 4), tie groups
    rowspan'd, members in frozen id-order, LABELS via the map, W/L/T
    verbatim + comparisons (the one sanctioned derivation), NO win-fraction
    column, the coverage strip, the cycle neutral + the honest-numbers
    one-liner, pair_counts re-split on "|", the algorithm_version footer
    badge. 409 => the SAFE HALT at the HONEST 409, the body's three fields
    verbatim + the affordances. 404 => the unknown-run page; any other
    non-200 => the fold page at the response's own status.
    Refuses when: never by this hand — the branches render honestly; the
    ranked whole NEVER renders at done:false (R12, absolute).
    Re-run: deterministic given the store state.
    Touches: nothing — queries.
    Provenance: web-brief §4 route 5, presentation.md (the ruled render),
    R10/R11/R12, G-WEBSPEC-BRIEF.
    """
    tally = await _service("GET", f"/runs/{stem}/tally")
    if tally.status_code == _CONFLICT:
        return templates.TemplateResponse(
            request,
            "halt.html",
            {"stem": stem, "fields": _fields(tally.json()), "gated": False},
            status_code=_CONFLICT,
        )
    if tally.status_code != _OK:
        if tally.status_code == _NOT_FOUND:
            return _unknown(request, tally.json())
        return templates.TemplateResponse(
            request, "fold.html", {"fields": _fields(tally.json())}, status_code=tally.status_code
        )
    whole = tally.json()
    if not bool(whole["coverage"]["done"]):
        return templates.TemplateResponse(
            request, "halt.html", {"stem": stem, "gated": True}, status_code=_OK
        )
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code != _OK:
        return templates.TemplateResponse(
            request, "fold.html", {"fields": _fields(manifest.json())}, status_code=manifest.status_code
        )
    labels = _labels(manifest.json())
    ranked: list[tuple[int, list[str]]] = []
    for group in whole["ranked_groups"]:
        _previous = len(ranked[-1][1]) if ranked else 0
        ranked.append((ranked[-1][0] + _previous if ranked else 1, [str(item) for item in group]))
    rows: dict[str, dict[str, Any]] = {
        str(item): {
            "label": labels.get(str(item), str(item)),
            "wins": int(whole["per_item_wins"][item]),
            "losses": int(whole["per_item_losses"][item]),
            "ties": int(whole["per_item_ties"][item]),
        }
        for item in whole["per_item_wins"]
    }
    return templates.TemplateResponse(
        request,
        "result.html",
        {
            "stem": stem,
            "ranked": ranked,
            "rows": rows,
            "components": [list(component) for component in whole["coverage"]["components"]],
            "cycle": [list(edge) for edge in whole["coverage"]["cycle"]],
            "pair_counts": dict[str, int](whole["coverage"]["pair_counts"]),
            "algorithm_version": str(whole["algorithm_version"]),
        },
    )


@web_app.post(_REGISTER)
async def register(request: Request) -> Response:
    """Register the run through the form — the ack panel, or the inline refusal at 200.

    Purpose: parse the form MANUALLY (await request.form() — no typed fields:
    the wire is the sole validator), pair the item rows, cast the quorum (a
    non-numeric quorum renders the family grammar inline — constructed at
    the controller, the only web-authored refusal), POST /runs. 201 => the
    register-ack: the BEGIN THE SITTING link, the run_id with the
    click-to-copy affordance (the pt-copy Web Component — app.js), the
    shareable sitting URL rendered from the REQUEST's own base URL + the
    run path — never a configured port (the port policy lives in the
    lifecycle targets, never in src), shown always, emphasized when
    quorum>1 (the quorum from the form's OWN posted body — the 201 body is
    {"run_id"} alone, no extra call), the frozen-run warning in plain
    words. 422/400 => the ONE refusal renderer inline at 200, at the form;
    a 500 folds (the crash envelope's wording).
    Refuses when: never by this hand — the branches render honestly.
    Re-run: deterministic given the store state.
    Touches: the run file through the service (the command).
    Provenance: web-brief §4 route 6, the design §7b, G-WEBSPEC-BRIEF.
    """
    form = await request.form()
    form_ids = [str(value) for value in form.getlist("item-id")]
    form_labels = [str(value) for value in form.getlist("item-label")]
    rows = [
        [item_id, label]
        for item_id, label in zip(form_ids, form_labels, strict=False)
        if item_id.strip() and label.strip()
    ]
    try:
        quorum = int(str(form.get("quorum", "1")))
    except ValueError:
        return _refuse_fragment(
            request,
            {
                "expected": "the quorum field a whole number 1 or greater",
                "found": f"the quorum field carried {form.get('quorum')!r}",
                "next_action": "enter a whole number for the quorum (1 means just you) and re-send",
            },
        )
    payload = {
        "items": rows,
        "operator_id": str(form.get("operator_id", "")),
        "question": str(form.get("question", "")),
        "quorum": quorum,
    }
    outcome = await _service("POST", "/runs", json=payload)
    if outcome.status_code == _CREATED:
        run_id = str(outcome.json()["run_id"])
        return templates.TemplateResponse(
            request,
            "ack.html",
            {"run_id": run_id, "sitting_url": f"{request.base_url}runs/{run_id}", "quorum": quorum},
        )
    return _refuse_fragment(request, _fields(outcome.json()), fold=outcome.status_code == _CRASH)


@web_app.get(_PAIR)
async def pair(request: Request, stem: str) -> Response:
    """Serve the bare pair as a fragment — or the HX-Redirect on DONE.

    Purpose: consume next (+ the manifest's label map, §7a's label law —
    /next the route's defining call, the map its label-bearing companion).
    200 => the bare-pair fragment (cards A/B marked + labeled; the count
    UNREAD — dropped at the controller); its buttons hx-post the vote as
    the sitting's pair. DONE => the HX-Redirect RESPONSE HEADER to the done
    page (core HTMX's navigation verb — no extension, no JS). Any non-200
    on either call => the refusal fragment at 200 (the fold wording at
    500).
    Refuses when: never by this hand.
    Re-run: deterministic given the store state.
    Touches: nothing — a query.
    Provenance: web-brief §4 route 7, the design §7a/§8, G-WEBSPEC-BRIEF.
    """
    nxt = await _service("GET", f"/runs/{stem}/next")
    if nxt.status_code != _OK:
        return _refuse_fragment(request, _fields(nxt.json()), fold=nxt.status_code == _CRASH)
    body = nxt.json()
    if body.get("done"):
        return Response(status_code=_OK, headers={"HX-Redirect": f"/runs/{stem}/done"})
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code != _OK:
        return _refuse_fragment(request, _fields(manifest.json()), fold=manifest.status_code == _CRASH)
    manifest_body = manifest.json()
    labels = _labels(manifest_body)
    return templates.TemplateResponse(
        request,
        "pair.html",
        {
            "stem": stem,
            "item_a": str(body["item_a"]),
            "item_b": str(body["item_b"]),
            "label_a": labels.get(str(body["item_a"]), str(body["item_a"])),
            "label_b": labels.get(str(body["item_b"]), str(body["item_b"])),
            "verdicts": list(manifest_body["verdicts"]),
        },
    )


@web_app.post(_VOTE)
async def vote(request: Request, stem: str) -> Response:
    """Cast the vote through the form — the ack chains to the next pair.

    Purpose: parse the form MANUALLY, POST the service's cast command, then
    the TWO-STEP CHAIN on 200: the vote-ack restates the verdict in
    ITEM-LABEL TERMS (§7a — "you preferred {label_a} (A) over {label_b}
    (B)" / the tie form; acknowledged:false => the idempotent echo in
    words; the count UNREAD, never rendered) and embeds hx-trigger="load" +
    hx-get to the pair fragment targeting the pair region — the POST's
    response NEVER carries the pair; the load fires the fetch. Any non-200
    on either call => the inline refusal at 200 — THE PAIR REGION UNTOUCHED
    (the same pair retryable: the refusal swaps into the ack region, never
    the pair region).
    Refuses when: never by this hand — the branches render honestly.
    Re-run: deterministic given the store state.
    Touches: the run file through the service (the command).
    Provenance: web-brief §4 route 8, the design §7a/§8, G-WEBSPEC-BRIEF.
    """
    form = await request.form()
    payload = {
        "pair": [str(form.get("item_a", "")), str(form.get("item_b", ""))],
        "winner": str(form.get("winner", "")),
        "comparator_id": str(form.get("comparator_id", "")),
        "comparator_class": str(form.get("comparator_class", "human")),
    }
    outcome = await _service("POST", f"/runs/{stem}/votes", json=payload)
    if outcome.status_code != _OK:
        return _refuse_fragment(request, _fields(outcome.json()), fold=outcome.status_code == _CRASH)
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code != _OK:
        return _refuse_fragment(request, _fields(manifest.json()), fold=manifest.status_code == _CRASH)
    labels = _labels(manifest.json())
    return templates.TemplateResponse(
        request,
        "vote-ack.html",
        {
            "stem": stem,
            "winner": payload["winner"],
            "acknowledged": bool(outcome.json()["acknowledged"]),
            "label_a": labels.get(payload["pair"][0], payload["pair"][0]),
            "label_b": labels.get(payload["pair"][1], payload["pair"][1]),
        },
    )


@web_app.get(_STATE_STRIP)
async def state_strip(request: Request, stem: str) -> Response:
    """Serve the state strip — the poll's swap target, the trigger re-armed.

    Purpose: consume state (the query — never refuses on coverage): the
    census read verbatim (total + the per-item involvement) at 200; the
    returned fragment carries the same every-5s trigger — the poll re-arms.
    Any non-200 => the refusal fragment at 200 (the fold wording at 500).
    Refuses when: never by this hand.
    Re-run: deterministic given the store state.
    Touches: nothing — a query.
    Provenance: web-brief §4 route 9, the design §8, G-WEBSPEC-BRIEF.
    """
    result = await _service("GET", f"/runs/{stem}/state")
    if result.status_code != _OK:
        return _refuse_fragment(request, _fields(result.json()), fold=result.status_code == _CRASH)
    body = result.json()
    return templates.TemplateResponse(
        request,
        "state-strip.html",
        {"stem": stem, "total": int(body["total"]), "items": dict[str, int](body["items"])},
    )
```

§Q NOTES THE EXECUTION SEAT READS: (1) the superseded import (`from prioritree.web_structure import UNION_LANES`) is DEAD — the union is the module's own constants (v1 §2a(1)'s amendment carried); (2) `rows` in the result controller is a DICT keyed by item id — the template's `rows[item]` subscript is the shape's other half (v1's list form was the latent inconsistency, cured); (3) `check_dir=False` on the static mount is §5's named cure — REQUIRED, never optional; (4) the `_UNPROCESSABLE` constant from v1 part 1 is DROPPED (the uniform error-swap guards leave it unused); (5) the count fields appear NOWHERE — the sitting/pair/vote controllers read item_a/item_b/acknowledged and no count; the wire's count bytes ride into response.json() and die there unread; (6) every controller is annotated `-> Response`; the wire reads narrowed at each read (str()/int()/dict[str, int](...)); E501 ≤120 held at authoring; no implicit string concatenation (explicit + only). Part 4 carries the edits (pyproject + the tail mount + the 405 arc), the test file whole, the per-step command sequence, the no-break proofs, the gate mapping.
## Reported by togo — 2026-11-22T17:14:09Z

# THE RE-SPEC — PART 4: THE EDITS + THE TESTS + THE COMMAND SEQUENCE + THE PROOFS (synthesize/webspec; togo, 2026-11-22 — the spec closes: every modified file's exact regions, the test file whole, the 13-step per-dispatch plan, the no-break proofs, the G-WEB/G-WEBSPEC mapping)

## §R THE REMOVAL STEP (the sequence's step 1 — the supersession's cleanup; the tree truth: BOTH files landed)

DELETE scripts/generation/web_structure.py (563 lines) + scripts/generation/web_scaffold.py (202 lines) — both out of grammar per R9 (the 14 template bodies + the CSS + the Web Components JS as Python data; the emitter with nothing left to emit). scripts/ carried ONLY the pair — the directory goes with them. READ-BACK: `scripts/` absent at the repo root; the git status shows exactly two deletions; nothing else changed.

## §S pyproject.toml — FOUR REGIONS (the deps + the rulings; the scripts/check rulings NEVER land; pyright's include UNTOUCHED)

**(1) REPLACE line 7:** `dependencies = ["fastapi", "httpx2", "jinja2", "uvicorn[standard]"]` (alphabetical; jinja2 NEW — R1's "Jinja2 templating always", the lock mints it at landing; httpx2 PROMOTED dev->runtime — moved, not duplicated).

**(2) REPLACE the service.py per-file-ignores comment block + entry (lines 100-105) with:**

```toml
# RULING (service-face-brief §6, G-SERVICE-FACE-BRIEF approved 2026-11-21): BLE001 —
# the 500 crash-envelope handler's except Exception IS the ruled catch-all (the app-level
# fold: crashes first-class citizens, the article's three-part form; Starlette re-raises
# so the traceback rides the log channel, never the body — the cli.py precedent re-cited).
# PLC0415 (web-brief §3c + G-WEBSPEC-BRIEF approved 2026-11-22): the tail's mid-file
# web import IS the import cycle's only legal form — the web module binds service.app at
# ITS top, so the import must fire AFTER the app binds; a top-of-file import would fire
# before, an importlib dodge would HIDE the cycle, not name it. The ignores ARE the
# rulings, named.
"src/prioritree/service.py" = ["BLE001", "PLC0415"]
```

**(3) INSERT after the tests/test_service_acceptance.py entry (after line 112):**

```toml

# RULING (web-brief §3b + G-WEBSPEC-BRIEF approved 2026-11-22): BLE001 — the child's own
# fold handler's except Exception IS the ruled catch-all (the service.py precedent
# re-carried at the child: crashes first-class citizens; the fragment lane renders the
# fold at 200, the page lane the honest 500). The ignore IS the ruling, named.
"src/prioritree/web.py" = ["BLE001"]
```

**(4) REPLACE line 134:** `dev = ["pytest", "pyright", "ruff"]` (httpx2 slimmed from the dev group — the promotion).

THE REGIONS THAT DIE (v1 §5c's, never landing): the scripts/generation per-file-ignores (T201/INP001), tests/test_web_check.py's S603/S607, the pyright include growth + the executionEnvironments line — include STAYS `["src", "tests"]` (line 128 untouched).

## §T THE MAKEFILE — UNTOUCHED WHOLE (web-check's fate: RETIRED — it never lands)

HEAD's Makefile stands byte-identical: five targets (dev/test/lint/typecheck/help), lint `uv run ruff check src/ tests/`, .PHONY unchanged. V1 §5d's three regions are dropped whole — no web-check target, no scripts/ argv growth.

## §U src/prioritree/service.py — THE TAIL MOUNT (the ONE touch; APPEND after line 528, the file's end — nothing else changes)

```python


# The web tier's tail mount (web-brief §3c): the child app mounted at the
# root — the six JSON routes above match FIRST (the router serves the first
# FULL match, the Mount catching the rest); the web module imports THIS app
# at its own top, bound above before the tail import fires (the import
# cycle's only legal form — a top-of-file import would fire before the app
# binds; an importlib dodge would HIDE the cycle, not name it; the PLC0415
# named ruling rides pyproject).
from prioritree.web import web_app

app.mount("/", web_app)
```

## §V tests/test_web_face.py — WHOLE (new file; the 20 arcs — byte-identical to v1 §6a; every arc re-verified against the authored templates' bytes; the docstring carries no generator references)

```python
# Copyright (C) 2026 Mark Losey. All rights reserved.
"""test_web_face — the mounted web tier's falsification set, in-process.

The web unit's test surface (web-brief §6.1): the mounted app under the
injection fixture — the SAME app now carries the mount; the child's
controllers call the service through the in-process client and the service
reads the PARENT's state.seam (the fixture's injection) — the isolation
extends to the web tier whole (store-as-parameter; no env, no CWD games).
The arcs: the page arcs (landing, sitting, done, progress, result
200/409/404); the fragment arcs (register 201/422/bad-quorum, the two-step
chain, the idempotent echo, the HX-Redirect, the 422 pair-untouched, the
state strip, the fold fragment); the no-anchoring pins (byte-level: no
sitting-context response carries the count; the sitting surface never
links state/tally). The S101/PLR2004 tests ruling stands.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import pytest

if TYPE_CHECKING:
    from pathlib import Path

from fastapi.testclient import TestClient

from prioritree.service import app
from prioritree.service_store import Serialize

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
    assert response.status_code == 303
    assert response.headers["location"] == f"/runs/{_RUN_ID}/done"


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
    assert response.status_code == 303
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
    """The vote ack restates in item-label terms and chains to the pair fragment."""
    client.post(_RUNS, json={"items": _ITEMS, **_OPERATOR})
    response = client.post(f"/ui/runs/{_RUN_ID}/vote", data=_FORM_VOTE)
    assert response.status_code == 200
    assert "You preferred one (A) over two (B)." in response.text
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
    client.post(f"/runs/{_RUN_ID}/vote", data=_FORM_VOTE)
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


def test_fold_fragment_500_envelope(client: TestClient) -> None:
    """A crashing seam verb renders the fold fragment at 200 — the envelope's fields seen."""

    class _BoomSeam:
        """The stub seam — serve raises; the fold's forced input, zero scaffolding."""

        def serve(self, _run_id: str, _seed: int | None = None) -> tuple[str, str, int]:
            """Raise the boom — the crash the fold renders."""
            raise RuntimeError("boom")

    app.state.seam = _BoomSeam()
    crashed = TestClient(app)
    response = crashed.get(f"/ui/runs/{_RUN_ID}/pair")
    assert response.status_code == 200
    assert "RuntimeError: boom" in response.text
    assert "check the server logs" in response.text
```

tests/test_web_check.py NEVER LANDS (retired with the generator — its 2 arcs die).

## §W tests/test_service_face.py — THE ONE AMENDMENT (REPLACE the function whole at :264-272; the module docstring byte-untouched)

```python
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
```

## §X THE COMMAND SEQUENCE — RE-PLANNED PER-STEP (R8: ONE STEP, ONE DISPATCH, ONE BOUNDED RETURN; the plan IS the dispatch list — each line names its dispatch)

1. **REMOVE the stranded pair** — DELETE scripts/generation/web_structure.py + web_scaffold.py (§R). READ-BACK: scripts/ absent; exactly two deletions in git status.
2. **EDIT pyproject.toml** — §S's four regions (the deps line; the service.py ruling block + PLC0415; the web.py BLE001 insert; the dev slim). READ-BACK: line 7 carries httpx2 + jinja2; the two per-file-ignores entries present; NO scripts/test_web_check entries; include untouched at ["src", "tests"]; dev carries pytest/pyright/ruff alone.
3. **RUN `uv sync`** — the lock mints jinja2 (httpx2's pin 2.16.2 stands — a promotion never re-pins). READ-BACK: uv.lock's prioritree entry carries httpx2 + jinja2; jinja2's package entry minted.
4. **CREATE web/templates/ — the chrome + the standalone pages** (§A base.html + §B landing.html + §H refuse.html + §N fold.html + §M unknown.html — 5 files). READ-BACK: 5 files under web/templates/; base.html carries the three CDN tags + the two static tags.
5. **CREATE web/templates/ — the sitting chain** (§C sitting.html + §D pair.html + §E vote-ack.html + §F ack.html — 4 files). READ-BACK: 4 files; sitting.html includes pair.html; pair.html carries the verdict-buttons set literal.
6. **CREATE web/templates/ — the state + terminal pages** (§I done.html + §J progress.html + §G state-strip.html + §K result.html + §L halt.html — 5 files). READ-BACK: 5 files; 14 templates total under web/templates/.
7. **CREATE web/static/ — the authored pair** (§O app.css + §P app.js). READ-BACK: 2 files; app.js defines pt-copy + the data-pt-path delegation. THE ORDER IS LOAD-BEARING: the static home must exist before anything imports web.py (the static mount's construction — §5's cure makes the boot green at any cwd, but the serving needs the files).
8. **CREATE src/prioritree/web.py** — §Q whole. READ-BACK: the file read back; the union block present; NO web_structure import; check_dir=False on the static mount.
9. **EDIT src/prioritree/service.py** — APPEND the tail mount (§U, after :528). READ-BACK: the diff shows ONLY the append; the six routes' bodies byte-untouched.
10. **CREATE tests/test_web_face.py** — §V whole. READ-BACK: 20 test functions; the fixture the face file's own form.
11. **EDIT tests/test_service_face.py** — REPLACE the one 405 arc (§W). READ-BACK: the diff shows ONLY that function.
12. **THE FLOOR, IN ORDER:** `make dev` (uv sync green) · `make test` (every suite green — 135 standing + the web face's 20 = 155 passed, 0 failed) · `make lint` (ruff ALL over src/ tests/ — zero findings, the named rulings the only ignores) · `make typecheck` (pyright strict 0 errors 0 warnings over src+tests). NO web-check (retired).
13. **ONE COMMIT** — the increment's close, at the COORDINATOR's hand (R8's ruling; the sequence's 13th rides shinko): the 18 new files (14 templates + 2 static + web.py + test_web_face.py) + pyproject.toml + service.py + test_service_face.py + uv.lock + the two removals — one commit, the unit whole.

## §Y THE NO-BREAK PROOFS

**(1) THE FROZEN SURFACES' PINS.** The six JSON routes' bodies byte-untouched — service.py's ONLY change is the tail append (the diff is the proof). The service face tests byte-untouched EXCEPT the one 405 arc (§W). The acceptance harness unbroken — AND THIS TIME PROVEN AT THE MECHANISM: the harness boots at a scratch cwd (Popen(cwd=home), :81); the tail import constructs web.py's StaticFiles with check_dir=False (§5's cure — v1's latent boot-crash, caught and cured); the probe GET /runs/RUN-0001/next is a parent route, matched before the mount (the router serves the FIRST FULL match; the Mount appends LAST); the boot argv unchanged; the eight-request arc rides parent routes only; the parent's /docs, /redoc, /openapi.json keep serving (registered at construction, before the mount).

**(2) THE UNMATCHED-PATH 404 ARC — HELD BY MECHANISM.** The child's refuse handler renders the identical family grammar as a JSONResponse at 404; the Mount never rewrites scope["path"] — the child's body carries expected "GET /no-such-path", found "no route matches the path /no-such-path", next_action the union carrying "POST /runs": the arc's three asserts hold unedited.

**(3) THE TEMPLATE-SOURCE LAW'S PROOFS (R9/R10, replacing v1's projection-law proofs).** The 16 frontend files are AUTHORED SOURCE — tracked, edited by definition, no regen headers; web.py LOADS them (Jinja2Templates' filesystem form + StaticFiles) and GENERATES the served surface at request time (template + context → the page); ZERO template content lives in Python (web.py carries zero human-facing words — the copy, the pins, the CSS, the JS live in their files); ZERO generated artifacts (nothing emits, nothing regens, no --check, no stamps — the never-hand-edit law's scope reaches nothing web). The face tests pin runtime↔files (the served markup's copy/href/hx-* assertions); the union pins the refusal bodies; the tree IS the source (no indirection layer to drift).

**(4) THE NO-ANCHORING PINS.** The count fields NEVER enter any sitting-context render context — the controllers never read them (by construction, not template diligence): asserted byte-level at the sitting page + the pair fragment + the vote ack ("count" absent). The sitting surface NEVER links state/tally: asserted ("/state" and "tally" absent from the sitting page).

**(5) THE RUFF/PYRIGHT RULINGS THE NEW CODE HONORS.** Ruff ALL over src/ tests/ — the named rulings the ONLY ignores: service.py BLE001+PLC0415; web.py BLE001; tests/** S101/PLR2004 standing; NO scripts entries (the scope never grows). Pyright strict over ["src", "tests"] — every controller annotated `-> Response`; the wire reads narrowed at each read; no implicit string concatenation; E501 ≤120; the templates/CSS/JS carry NO lint surface (ruff/pyright cover Python alone).

**(6) THE G-WEB MAPPING (the build gate's four conditions).** (1) The exact-task law → parts 2-4: every file whole (16 authored frontend files + web.py + the test file), every modified file's exact regions + insertion points, the 13-step sequence with read-backs — the execution seat receives nothing to figure out. (2) The projection law (R1 AS CLARIFIED BY R9/R10 — §4's named gate reading) → §Y(3): the files the authored source, the loader/renderer the seam, zero content-in-Python, zero generated; Jinja2 always; Shoelace via CDN (the base template's pins); the Web Components under separation of concerns (app.js); the HTMX wire. (3) The comparator's flow end-to-end → §V's arcs: register → the sitting's server-side pair → the vote's two-step chain → the 5s progress poll → the ranked whole; the render gate (done:false NEVER renders the table); the 409-verbatim; the HX-Redirect. (4) R5 + the floor → §Y(1)/(2)/(5): every refusal ThreePart-verbatim on every touched surface (the child's 404/405 in the family grammar, the fragments' 200s rendering refusals visibly, the pages' honest statuses); pyright 0/0 + ruff zero findings; kensho's independent re-run green (validate/web).

THE RE-SPEC CLOSES: the architecture re-settled per R9/R10 (the homes ruled, the fates ruled — both stranded files removed, the --check/regen discipline retired, the generator removed, the floor-scope growth dead), every byte authored (the 14 templates + the 2 static files + web.py + the test file whole; the 4 pyproject regions + the tail mount + the 405 arc exact), the command sequence re-planned per-step (12 jikko dispatches + the commit at the coordinator's hand), the no-break proofs named per frozen surface, v1's three latent defects caught and cured (the union import, the rows-list/render-subscript inconsistency, the static mount's check-dir boot-crash). G-WEBSPEC-BRIEF's conditions are met by this re-spec under R9/R10's clarified law; hyoka's adversarial pass rides before the presentation; the collaborator's approval is the gate. — togo, 2026-11-22
## Reported by togo — 2026-11-22T17:26:11Z

# THE FOLD — PART 1: THE LETTERS (synthesize/webspec; togo, 2026-11-22 — hyoka's seven adversarial findings folded into v3: the letter corrections whole — the route-8 carrier named, §3e + §8-item-5 amended, §Y's exception class ruled, G-WEB condition 2's letter re-composed for the collaborator's ruling; part 2 carries the byte corrections exact)

READ-BACK (the fold's ground, whole): reports/design/adversarial-web.md (hyoka's pass — the seven findings verbatim, every cure named, the verdict: the architecture stands, the spec's defects mine to fold) · reports/synthesize/webspec.md (my own v2 whole, 3601 lines — the five rethink events + v1's six beneath) · reports/synthesize/web.md (the approved brief whole — §4 route 8's letter, §3e's letter, §8 item 5's letter, read at the bytes) · the ux store's junro.json (G-WEB's condition 2 verbatim; G-WEBSPEC-BRIEF's three conditions; R9/R10 the law) · THE CORE AT SOURCE: src/prioritree/votes.py:464-486 (the ack semantics verified — the dedup branch returns acknowledged=True at :468, "UNCHANGED count, acknowledged=True (never a silent dup)"; the fresh cast returns False at :486) + src/prioritree/service.py:168 (render_refusal — the refusal's one render point) + :269-298 (the refuse handler's found-texts composed in Python — the precedent finding 3 rides). READ-ONLY held — nothing written beyond these report events.

## §0 THE FOLD'S VERDICT

All seven findings folded, none deferred; hyoka's own verdict carried: the re-settled ARCHITECTURE meets R9/R10 — the corrections are the fold's. V3 = v2's bytes + the corrections exact: TWO byte-flips (§E's echo condition, §Q's vote docstring), the echo arc's re-target + the fresh-ack absence pin, ONE new face arc (the static pair), the §Y namings (three: the exception class, the mount-shadow residue, the scratch-cwd page residue), the letter amendments (the brief's route-8 carrier + §3e + §8 item 5), and G-WEB condition 2's re-composed letter prepared as the amendment the collaborator rules at the gates' presentation. THE FILE INVENTORY UNCHANGED IN COUNT: 18 authored + 3 edited + 2 removed — the new arc rides the already-counted test file; no file added, none dropped.

## §1 FINDING 1 (BLOCKING) — THE IDEMPOTENT-ECHO INVERSION: THE LETTERS (the bytes ride part 2)

The core's semantics, verified at the source this fold: a FRESH cast returns acknowledged=False (votes.py:486); the byte-identical RE-SEND returns acknowledged=True (:464-468). V2's §E renders the echo at `{% if not acknowledged %}` — INVERTED: every fresh vote tells the comparator "already recorded with the same answer" (a lie per cast); the true re-send renders nothing. §Q's vote docstring carries the same inversion ("acknowledged:false => the idempotent echo in words"). §V's echo arc masks it twice: its first post targets /runs/{_RUN_ID}/vote — NO such route exists (the fragment is /ui/.../vote; the service lane is /votes) — the vote never lands; the "again" post is a FRESH cast whose inverted echo satisfies the assertion. THE BRIEF'S CARRIER, NAMED: the approved brief's §4 route-8 letter reads "acknowledged:false → the idempotent echo in words — 'already recorded with the same answer — it stands once'" — the inversion's carrier, amendment-pending at the re-presentation. THE CORRECTED LETTER: "acknowledged:true → the idempotent echo in words — 'already recorded with the same answer — it stands once'". The re-presented brief carries the corrected letter; the collaborator rules the amendment at G-WEB-BRIEF. (§E's flip, §Q's flip, and the test's cure ride part 2.)

## §2 FINDING 2 (HIGH) — G-WEB CONDITION 2'S RE-COMPOSED LETTER (the amendment prepared for the collaborator's ruling)

The stale letter, verbatim at the route's heart: "the projection law green (R1): the ENTIRE front end generated from Python — Jinja2 always, Shoelace via CDN, Web Components under separation of concerns, the HTMX wire; zero hand-authored frontend artifacts on disk (out of grammar; the generated surface regenerates from its source structure, never hand-edited)" — as composed it CANNOT go green against v3's 18 authored files, and G-WEB is deterministic-check: no ruling seat lives there. THE RE-COMPOSED LETTER, prepared as the amendment the collaborator RECORDS at the gates' presentation (G-WEB-BRIEF + G-WEBSPEC-BRIEF, collaborator-ruling — never deferred to a gate with no ruling seat):

"the projection law green (R1 as clarified by Q-ux-surface R9/R10): the ENTIRE front end is separate AUTHORED template/static files LOADED by Python, the served surface GENERATED at render time (template + context → the page) — Jinja2 always (the filesystem loader, autoescape ON), Shoelace via CDN, Web Components under separation of concerns, the HTMX wire; the authored template/static files ARE in grammar (the source of truth, tracked, edited by definition); zero hand-authored SERVED HTML without the loader, zero template content imprisoned in Python (no string constants, no giant concatenations — R9's own letter)"

The stale "zero hand-authored frontend artifacts on disk" letter dies with the ruling; the condition's INTENT (no served surface without source; no content imprisoned in Python) is enforced by the architecture itself. G-WEBSPEC-BRIEF's condition-2 tail ("R1's projection law at the bytes level: zero hand-authored frontend artifacts") reads the same re-composition at its presentation. §Y(6)'s condition-2 mapping cites this letter.

## §3 FINDING 3 (HIGH) — §Y(3)'s EXCEPTION CLASS, RULED

The false claim: v2 §Y(3) says "web.py carries zero human-facing words" — FALSE at §Q's own bytes: the register controller's non-numeric-quorum refusal's three fields ("the quorum field a whole number 1 or greater" / the found composing the posted value / "enter a whole number for the quorum (1 means just you) and re-send") and the refuse/fold handlers' found-texts are human words in Python. THE RULING (the first cure taken; the file-tier move REFUSED): family-grammar field VALUES in Python are IN GRAMMAR — service.py's own precedent (render_refusal at :168, the refusal's one render point; the refuse handler's found-texts at :296/:298 composed in Python — the wire's refusal bodies have always carried their field values in Python): the refusal fields are the WIRE'S DATA composed at the controller, never template copy. The class, named exactly: (a) the register controller's quorum refusal (v1 §0 ruling 5's own form re-carried — the only web-authored ThreePart refusal, the honest cure at 200); (b) the child's refuse/fold handlers' found-texts (the family grammar's address letters — the parent's own shadowed handler the precedent). The alternative — moving the quorum copy to the file tier — REFUSED with the reason: the refusal's found composes the POSTED VALUE at the controller (a template cannot render the refusal without the controller composing its fields anyway; the family grammar's form is service.py's standing law). The exception class governs every zero-words letter in the chain (part 1's §4 gate-reading included); the byte-exact amendments land at §Y(3)/§Y(6) (part 2).

## §4 FINDING 4 (MEDIUM) — THE STALE AMENDED-CLAUSE LETTERS (the re-presented brief made paper-coherent)

- §3e's letter: the brief's §3e rules "next_action THE MOUNTED WHOLE'S LEGAL SET (the nine web routes + the six service routes, as data in the structure — the mounted whole IS the tree's HTTP face; the refusal teaches it honestly)" — "as data in the structure" is STALE: the structure is removed at step 1. THE AMENDED LETTER: "next_action THE MOUNTED WHOLE'S LEGAL SET (the nine web routes + the six service routes, as the module's own union — web.py's own route constants + the six service lanes as the frozen wire's literals, cited — the mounted whole IS the tree's HTTP face; the refusal teaches it honestly)". The clause stands otherwise (the grammar, the mount's price, the priced consequences).
- §8 item 5's letter: the brief's item 5 names "the pyproject dep edits' bytes (dependencies, the dev group, pyright's include), the Makefile's bytes (web-check, .PHONY, the lint argv)" — BOTH STALE in v2/v3: pyright's include stays ["src", "tests"] (line 128 untouched); the Makefile is UNTOUCHED whole (the web-check regions never land — §1.8's retirement). THE AMENDED LETTER: "the service.py tail's exact bytes: the insertion point (after :528's describe — the file's end), the mount lines, the PLC0415 ruling text (the pyproject per-file-ignores entry's bytes), the pyproject dep edits' bytes (dependencies + the dev group ALONE — pyright's include untouched)". The dead letters dropped; the item's surviving content named.

## §5 FINDING 5 (MEDIUM) — THE MOUNT-SHADOW'S FALSE FOUND: THE RESIDUE NAMED (§Y(2)'s amendment, part 2)

The brief priced the 405→404 status change (§3e.2) but never the lying found: DELETE /runs now answers the child's 404 "no route matches the path /runs" — factually false (POST /runs matches the path; only the method is wrong); no arc pins the case (the one 405 arc re-targeted to GET /ui/register, a genuine 405). The residue NAMED, never silently riding: the whole's 404 grammar is honest only for paths NO route of the whole matches; the wrong-method-on-a-matched-path case renders the child's 404 letter with its path-alone found-text — the mount's own mechanics, priced and named at §Y(2) (part 2 carries the exact letter).

## §6 FINDING 6 (MEDIUM) — THE STATIC PAIR'S PIN (the one new face arc; part 2's bytes)

check_dir=False's silent-404 is UNPINNED: no v2 arc GETs /static/app.css or /static/app.js — a mis-named static home serves unstyled pages with zero test failures (the templates' home IS pinned by every page arc). THE CURE: ONE face arc pinning both 200s + a byte each — a mis-named static home then fails loudly. §V grows the arc (20 → 21); the floor count grows with it (135 standing + 21 = 156 passed); the module docstring's arc list names it.

## §7 FINDING 7 (LOW) — THE SCRATCH-CWD PAGE RESIDUE, NAMED (§Y(1)'s amendment, part 2)

§Y(1)'s harness proof holds — hyoka verified at the mechanism (check_dir=False at §Q's mount; Jinja2Templates' lazy loader; the acceptance arcs ride parent JSON routes; the boot survives). The residue: a page request at a scratch cwd answers the PARENT's JSON 500 — TemplateNotFound escapes the child's fold (the child's fold renders through the same broken loader), then the parent's fold: family grammar held, the PAGE TIER DEAD at a scratch cwd. NAMED in §Y(1); the repo-root launch serves the pages (the launch discipline's own letter). Part 2 also corrects §X step 7's confused note (under check_dir=False the import needs NO directory — "load-bearing" overstates).

## §8 V3'S COMPOSITION RULE

V3 composes on the chain: this part's letters + part 2's byte corrections; EVERY other v2 byte stands. The corrections' inventory, whole: §E's flip (one condition), §Q's vote-docstring flip (one clause), §V's three corrections (the chain arc's absence pin, the echo arc's re-target, the new static arc) + the docstring's arc list, §X's two letter-fixes (step 7's note; the counts 20→21, 155→156), §Y's three namings ((1) the scratch-cwd page residue, (2) the mount-shadow residue, (3) the exception class). The re-presentation at G-WEB-BRIEF + G-WEBSPEC-BRIEF carries: the amended brief clauses (§§1/3/4 here) + the re-composed condition-2 letter (§2 here) + the corrected bytes (part 2). The gates' rulings are the collaborator's acts; this fold hands them a paper-coherent whole.
## Reported by togo — 2026-11-22T17:26:23Z

# THE FOLD — PART 2: THE BYTES CORRECTED (synthesize/webspec; togo, 2026-11-22 — the exact corrections to v2's §E/§Q/§V/§X/§Y, findings 1 + 3 + 5 + 6 + 7 at the bytes; every other v2 byte stands; v3 closes)

## §E′ web/templates/vote-ack.html — THE ECHO CONDITION FLIPPED (finding 1, blocking)

REPLACE the echo line (v2 §E's body, the fourth line) — v2's bytes:

```html
  {% if not acknowledged %}<p class="quiet">This pair was already recorded with the same answer — it stands once.</p>{% endif %}
```

WITH v3's bytes:

```html
  {% if acknowledged %}<p class="quiet">This pair was already recorded with the same answer — it stands once.</p>{% endif %}
```

All other §E bytes stand (the ack-line's three-way restatement, the embedded pair fetch). The semantics, cited: the core returns acknowledged=True on the byte-identical re-send ALONE (votes.py:464-468); the echo renders there and only there.

## §Q′ src/prioritree/web.py — THE VOTE DOCSTRING FLIPPED (finding 1)

REPLACE in the vote controller's docstring — "acknowledged:false => the idempotent echo in words" WITH "acknowledged:true => the idempotent echo in words". All other §Q bytes stand.

## §V′ tests/test_web_face.py — THREE CORRECTIONS + THE DOCSTRING (findings 1 + 6; the arc count 20 → 21)

**(1) THE CHAIN ARC — REPLACE the function whole** (the fresh cast's ack gains the echo's ABSENCE pin):

```python
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
```

**(2) THE ECHO ARC — REPLACE the function whole** (both posts through the FRAGMENT path; the echo asserted on the second — the re-send — alone; its ABSENCE pinned on the fresh ack):

```python
def test_vote_echo_already_recorded(client: TestClient) -> None:
    """The byte-identical re-send renders the idempotent echo in words."""
    client.post(_RUNS, json={"items": _TWO_ITEMS, **_OPERATOR})
    fresh = client.post(f"/ui/runs/{_RUN_ID}/vote", data=_FORM_VOTE)
    assert fresh.status_code == 200
    assert "already recorded with the same answer" not in fresh.text
    again = client.post(f"/ui/runs/{_RUN_ID}/vote", data=_FORM_VOTE)
    assert again.status_code == 200
    assert "already recorded with the same answer" in again.text
```

**(3) THE NEW ARC — INSERT after test_landing_serves** (finding 6: the static pair's 200s pinned + a byte each — a mis-named static home fails loudly):

```python
def test_static_pair_serves(client: TestClient) -> None:
    """The static home serves its pair: app.css + app.js at 200, a byte each."""
    css = client.get("/static/app.css")
    js = client.get("/static/app.js")
    assert css.status_code == 200
    assert js.status_code == 200
    assert "--pt-gap" in css.text
    assert "pt-copy" in js.text
```

**(4) THE MODULE DOCSTRING — the arcs list amended:** after "the state strip, the fold fragment);" INSERT "the static pair (the chrome's app.css + app.js — the 200s pinned, a mis-named home fails loudly);" — the docstring's other bytes stand.

All other §V arcs stand byte-identical.

## §X′ THE COMMAND SEQUENCE — TWO LETTER-FIXES

- **STEP 7's NOTE, CORRECTED** (finding 7's second half): REPLACE "THE ORDER IS LOAD-BEARING: the static home must exist before anything imports web.py (the static mount's construction — §5's cure makes the boot green at any cwd, but the serving needs the files)" WITH "THE ORDER'S NOTE, CORRECTED (hyoka's finding 7): under check_dir=False the import needs NO directory (§5's cure — the boot green at any cwd); the order serves the floor's own review — the static pair present before the module that serves it, the face tests' static arc pinning the 200s".
- **THE COUNTS**: step 10's READ-BACK — "20 test functions" → "21 test functions"; step 12's floor — "135 standing + the web face's 20 = 155 passed, 0 failed" → "135 standing + the web face's 21 = 156 passed, 0 failed". All other §X bytes stand.

## §Y′ THE NO-BREAK PROOFS — THREE NAMINGS (findings 3, 5, 7)

**(1) + THE SCRATCH-CWD PAGE RESIDUE — APPEND to §Y(1):** "THE RESIDUE NAMED (hyoka's finding 7, verified at the mechanism): at a scratch cwd a PAGE request answers the PARENT's JSON 500 — TemplateNotFound escapes the child's fold (the child's fold renders through the same broken loader), then the parent's fold renders the family grammar: the family grammar HELD, the PAGE TIER DEAD at a scratch cwd; the harness's own arcs ride parent JSON routes — the boot survives; the repo-root launch serves the pages (the launch discipline's own letter)."

**(2) + THE MOUNT-SHADOW RESIDUE — APPEND to §Y(2):** "THE RESIDUE NAMED (hyoka's finding 5): the wrong-method-on-a-matched-path case (e.g. DELETE /runs — POST /runs matches the path) renders the child's 404 letter whose found names the path ALONE ('no route matches the path /runs' — factually false at a matched path); the whole's 404 grammar is honest only for paths NO route of the whole matches — the mount's own mechanics, priced with the 405→404 status change (the brief's §3e.2), the residue named, never silently riding."

**(3) THE EXCEPTION CLASS — TWO REPLACEMENTS:** in §Y(3), REPLACE "ZERO template content lives in Python (web.py carries zero human-facing words — the copy, the pins, the CSS, the JS live in their files)" WITH "ZERO template content lives in Python (web.py carries zero human-facing words EXCEPT THE FAMILY-GRAMMAR FIELD VALUES — the exception class ruled at the fold, hyoka's finding 3: the register controller's quorum-refusal three fields + the refuse/fold handlers' found-texts, service.py's own precedent (render_refusal :168, the found-texts :296/:298) — the wire's refusal data composed at the controller, never template copy); the copy, the pins, the CSS, the JS live in their files". In §Y(6) condition (2), REPLACE "zero content-in-Python, zero generated" WITH "zero content-in-Python beyond the family-grammar field values (the named exception class), zero generated" and cite the condition's letter to part 1's §2 (the re-composed letter the collaborator rules at the presentation).

THE FOLD CLOSES — V3 WHOLE: v2's bytes + these corrections exact (two byte-flips, three test corrections + the docstring's arc list, two sequence letter-fixes, three proof namings) + part 1's letters (the route-8 carrier named + corrected, §3e + §8-item-5 amended, the exception class ruled, the condition-2 letter re-composed); every other v2 byte stands; the file inventory unchanged in count (18 authored + 3 edited + 2 removed); all seven findings folded, none deferred. The re-spec re-presents at G-WEB-BRIEF + G-WEBSPEC-BRIEF; the gates' rulings are the collaborator's acts. — togo, 2026-11-22
