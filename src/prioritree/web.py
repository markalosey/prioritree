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

import httpx2
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException

from prioritree.service import ESCALATION
from prioritree.service import app as service_app

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


async def _service(method: str, path: str, json: object | None = None) -> httpx2.Response:
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
        request, "unknown.html", {"fields": _fields(body)}, status_code=_NOT_FOUND,
    )


def _refuse_fragment(request: Request, fields: dict[str, str], *, fold: bool = False) -> Response:
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
        request, "refuse.html", {"fields": fields, "fold": fold}, status_code=_OK,
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
        request, "fold.html", {"fields": _fields_fold}, status_code=_CRASH,
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
            request, "fold.html", {"fields": _fields(manifest.json())}, status_code=manifest.status_code,
        )
    nxt = await _service("GET", f"/runs/{stem}/next")
    if nxt.status_code != _OK:
        if nxt.status_code == _NOT_FOUND:
            return _unknown(request, nxt.json())
        return templates.TemplateResponse(
            request, "fold.html", {"fields": _fields(nxt.json())}, status_code=nxt.status_code,
        )
    body = nxt.json()
    if body.get("done"):
        return Response(status_code=_OK, headers={"HX-Redirect": f"/runs/{stem}/done"})
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
            request, "fold.html", {"fields": _fields(nxt.json())}, status_code=nxt.status_code,
        )
    body = nxt.json()
    if not body.get("done"):
        return Response(status_code=_OK, headers={"HX-Redirect": f"/runs/{stem}"})
    return templates.TemplateResponse(
        request, "done.html", {"stem": stem, "fields": _fields(body)}, status_code=_OK,
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
            request, "fold.html", {"fields": _fields(result.json())}, status_code=result.status_code,
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
            request, "fold.html", {"fields": _fields(tally.json())}, status_code=tally.status_code,
        )
    whole = tally.json()
    if not bool(whole["coverage"]["done"]):
        return templates.TemplateResponse(
            request, "halt.html", {"stem": stem, "gated": True}, status_code=_OK,
        )
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code != _OK:
        return templates.TemplateResponse(
            request, "fold.html", {"fields": _fields(manifest.json())}, status_code=manifest.status_code,
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
    (B)" / the tie form; acknowledged:true => the idempotent echo in
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
