# Copyright (C) 2026 Mark Losey. All rights reserved.
"""web — the web fronts: the child app over the service's wire, the twelve routes.

The web unit (web-brief §1.1 + the approved design §8, re-settled per
Q-ux-surface R9/R10 — the template-source law): the CHILD application
(FastAPI with the docs routes disabled — the web tier is the human's
surface, not an API), mounted at the service app's TAIL (service.py's mount
line, the one touch); the twelve routes (7 pages at honest statuses + 5
fragment-lane routes at 200 — register, pair, vote, state_strip,
unremember, the un-remember lane a POST answering HX-Redirect, never a
render — the deliberate-pair lane's two pages riding amendment 22: the
picker + the chosen pair, the existing card and door re-used); the
in-process service client (httpx2
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
emits, nothing regens, no --check). The web homes resolve IN ORDER
(install-brief §2/§3): the CWD-relative copy FIRST (the repo-root launch
discipline, STORE_HOME run_store.py:67 the precedent — the authored files
win when present), the shipped package's copy the FALLBACK
(importlib.resources over the wheel's force-include mapping — the
installed lane renders from the package); the static mount's
check_dir=False is the named cure for the acceptance harness's
scratch-cwd boot (StaticFiles raises at import on an absent directory;
the store mkdirs on demand — the asymmetry named at the re-settle; a
wrong cwd in the clone folds honestly — both branches miss). The child's OWN fold + refuse handlers (the mount's price:
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

import hmac
import logging
import os
import secrets
from importlib.resources import files
from pathlib import Path
from typing import Any, Final

import httpx2
from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse, Response
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.sessions import SessionMiddleware

from prioritree.key_verify import AUTH_HEADER_DEFAULT
from prioritree.scheduler import schedule_pairs
from prioritree.service import ESCALATION
from prioritree.service import app as service_app
from prioritree.votes import PRESENTATION_CANONICAL, PRESENTATION_SWAPPED

__all__ = ["resolve", "web_app"]

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
_PICKER: Final[str] = "/runs/{stem}/pairs"
_DELIBERATE: Final[str] = "/runs/{stem}/pair"
_REGISTER: Final[str] = "/ui/register"
_PAIR: Final[str] = "/ui/runs/{stem}/pair"
_VOTE: Final[str] = "/ui/runs/{stem}/vote"
_STATE_STRIP: Final[str] = "/ui/runs/{stem}/state"
_UNREMEMBER: Final[str] = "/ui/runs/{stem}/unremember"
_TEMPLATES_HOME: Final[str] = "web/templates"
_STATIC_HOME: Final[str] = "web/static"
# The fallback's own vocabulary (install-brief §2): the shipped package's
# name — the force-include dest root, pyproject's mapping naming the same
# package — + the two tails (the dests' tails; one spelling across the
# mapping, these constants, and the resolver's derivation).
_PACKAGE: Final[str] = "prioritree"
_TEMPLATES_TAIL: Final[str] = "templates"
_STATIC_TAIL: Final[str] = "static"
_BASE_URL: Final[str] = "http://prioritree.internal"
_OK: Final[int] = 200
_CREATED: Final[int] = 201
_FOUND: Final[int] = 302
_NOT_FOUND: Final[int] = 404
_METHOD_NOT_ALLOWED: Final[int] = 405
_CONFLICT: Final[int] = 409
_CRASH: Final[int] = 500
_FRAGMENT_LANE: Final[str] = "/ui/"

_UNAUTHORIZED: Final[int] = 401
_FORBIDDEN: Final[int] = 403

# The signing secrets' env-or-boot-mint school (the CSRF region's own form,
# extended): each knob reads its env ONCE at import — unset => a boot-minted
# 256-bit secret (the restart-invalidation price carried honestly: a boot's
# outstanding tokens and sessions die, the re-render and the re-ask cure); an
# env secret UNDER THE FLOOR refuses AT IMPORT in the ThreePart grammar (the
# zero-findings bar applied to the knob — a weak secret weakens every
# artifact it signs, the CSRF token and the remembered session both).
_SECRET_FLOOR_BYTES: Final[int] = 32  # 256 bits — the boot-mint school's own length
_CSRF_SECRET_ENV: Final[str] = "PRIORITYTREE_WEB_CSRF_SECRET"
_REMEMBER_SECRET_ENV: Final[str] = "PRIORITYTREE_WEB_REMEMBER_SECRET"


def _boot_secret(env_name: str) -> bytes:
    """Read the env secret or boot-mint the 256-bit fallback — an under-floor env secret refused at import.

    Purpose: the shared home of both knobs' strength check (the CSRF secret
    + the remember secret — the same floor, the same grammar); the env value
    wins when present and at the floor; unset => the boot-mint (256 bits);
    an under-floor env value REFUSES AT IMPORT (the ThreePart bytes in the
    raise — the loud form, never a silent weak boot).
    Refuses when: the env set and shorter than the floor (RuntimeError, the
    ThreePart message).
    Re-run: deterministic given the environment.
    Touches: nothing — the environment read alone.
    Provenance: the design §1f/§2c (the twin at both knobs, hyoka's cure 5),
    the unit brief §2c, G-VOTERSESSIONSPEC-BRIEF.
    """
    given = os.environ.get(env_name, "")
    if given and len(given.encode()) < _SECRET_FLOOR_BYTES:
        _message = (
            f"expected: the {env_name} env secret {_SECRET_FLOOR_BYTES} bytes "
            f"(256 bits) or longer, or unset for the boot-mint; "
            f"found: {len(given.encode())} bytes; "
            f"next_action: set {env_name} to a 256-bit secret "
            f'(python -c "import secrets; print(secrets.token_urlsafe(32))") or unset it'
        )
        raise RuntimeError(_message)
    return given.encode() or secrets.token_urlsafe(32).encode()


_csrf_secret: Final[bytes] = _boot_secret(_CSRF_SECRET_ENV)
_remember_secret: Final[bytes] = _boot_secret(_REMEMBER_SECRET_ENV)
_CSRF_FIELD: Final[str] = "csrf_token"

# The remembered session's payload keys (content-in-configuration): the
# carried name + the CSRF epoch — the two values the cookie rides; the epoch
# minted ONCE at identification, never re-minted at renders (the
# concurrent-tab cure by construction: no per-render session write, two tabs
# hold the same epoch, the same token, both POSTs pass).
_SESSION_NAME: Final[str] = "name"
_SESSION_EPOCH: Final[str] = "epoch"
_REMEMBER_COOKIE: Final[str] = "remember"
_REMEMBER_MAX_AGE: Final[int] = 14 * 24 * 60 * 60  # 14 days — keisan's pricing: the 780-s card covered 1550x


def _remembered(request: Request) -> str:
    """Read the remembered name — the session's carried identity, "" when the browser is unidentified.

    Purpose: the ONE read helper every render context and the vote controller
    ride (the sitting, the judge, the pair fragment, the landing's pre-fill,
    the vote's cast read); the conditional ask's own branch key (a non-empty
    return renders the identity line, never the ask).
    Refuses when: never — a pure read ("" a VALUE, the anonymous state).
    Re-run: deterministic given the session state.
    Touches: the session read alone.
    Provenance: the unit brief §1c/§2a, G-VOTERSESSIONSPEC-BRIEF.
    """
    return str(request.session.get(_SESSION_NAME, ""))


def _remember(request: Request, name: str) -> None:
    """Identify the browser ONCE — the name written, the epoch minted; the session's ONE write act.

    Purpose: the identification's single write home (the first vote's
    identifying act and the correction verb's re-identification ride the same
    act — the epoch minted at every identification, ROTATED at every
    re-identification: the old tabs' tokens die at the next guard, the
    refusal's copy teaches the reload); NO per-render session write ever
    (the concurrent-tab cure).
    Refuses when: never — the write IS the act (the caller gates the empty name).
    Re-run: deterministic in form (the epoch random by design — the 256-bit school).
    Touches: the session alone (the browser's cookie via the engine's write intercept).
    Provenance: the unit brief §1d/§2a/§2b, hyoka's cure 8, G-VOTERSESSIONSPEC-BRIEF.
    """
    request.session[_SESSION_NAME] = name
    request.session[_SESSION_EPOCH] = secrets.token_urlsafe(32)


class CsrfRefusedError(Exception):
    """CsrfRefusedError — the drive-by's death: expected, found, next_action.

    Purpose: carry the CSRF refusal's three fields as typed data for the
    child's DEDICATED handler (never the child's fold — the crash page's
    clothes never worn); found "absent-or-mismatched" the elision discipline
    (the remote page could not have READ the served form — which leg fired
    teaches nothing).
    Refuses when: never — the class CARRIES, never gates (the guard raises
    at the guarded POST; the dedicated handler renders).
    Re-run: deterministic given the raised refusal's fields (the three
    carried verbatim, never re-derived).
    Touches: nothing — typed data alone (the fields the guard minted).
    Provenance: the design's F2, the unit brief §1b/§3c, rikai map 2,
    G-SERVING-TIER-INTEGRATION-BRIEF.
    """

    def __init__(self, expected: str, found: str, next_action: str) -> None:
        """Initialize the refusal with its three named fields."""
        self.expected = expected
        self.found = found
        self.next_action = next_action
        super().__init__(f"refused — expected: {expected} | found: {found} | next: {next_action}")


def _mint_csrf(payload: str) -> str:
    """Mint the HMAC-SHA256 token over the bound payload — the stateless signed form."""
    return hmac.new(_csrf_secret, payload.encode(), "sha256").hexdigest()


def _mint_bound(path: str, request: Request) -> str:
    """Mint the epoch-bound token over a path — pre-identification the path alone.

    Purpose: the ONE composition home of the CSRF payload's epoch binding
    (the sitting/judge/pair renders' mints and the guard's recompute the
    same form): the path, then "|", then the SESSION's epoch when one rides —
    never a client-echoed value (the fixation discipline held); the epoch
    absent (the anonymous browser) => the path alone (the identifying vote's
    own guard passes — its page minted path-bound, the guard recomputes
    path-bound). The register lane NEVER composes here (§2e — the binding
    never presumed).
    Refuses when: never — a pure composition.
    Re-run: deterministic given the session state.
    Touches: the session read alone (never a write — no per-render mint).
    Provenance: the unit brief §1d/§2b, hyoka's 1b (the concurrent-tab cure),
    G-VOTERSESSIONSPEC-BRIEF.
    """
    epoch = str(request.session.get(_SESSION_EPOCH, ""))
    return _mint_csrf(f"{path}|{epoch}" if epoch else path)


async def _csrf_guard(request: Request) -> None:
    """Validate the form's CSRF token BEFORE _service — the per-route dependency (F2's cure).

    Purpose: recompute the expected token over the request's own path + the
    SESSION's epoch (the server-side recompute, never a client-echoed value)
    + hmac.compare_digest (the timing discipline, key_verify's ONE-compare
    school); the drive-by's POST carries an absent-or-mismatched token => the
    refusal fires BEFORE _service (the write never lands). THE EXPIRY'S
    TEACHING branches on the session's own state: an EMPTY session (the cookie
    died at max_age or the secret rotated — the sitting chain's fragment trap
    never re-renders the ask) teaches the LAPSE in the human's words ("your
    identification lapsed — reload, the page re-asks your name"); a LIVE
    session (the stale tab at a rotated epoch) teaches the standing reload
    cure. Starlette caches request.form() — the route's own parse reads the
    same cached body, no double-read.
    Refuses when: the token absent or mismatched (CsrfRefusedError).
    Provenance: the unit brief §1d/§2b, moho's walk §1d (the fragment trap's
    only channel), hyoka's 1b/8, G-VOTERSESSIONSPEC-BRIEF.
    """
    form = await request.form()
    presented = str(form.get(_CSRF_FIELD, ""))
    # §86 — the register validates PATH-BOUND even when the session now exists:
    # the path-bound mint mirrors the landing's mint at :616; every other lane
    # (the vote + unremember POSTs) — the epoch-bound recompute byte-standing.
    expected = _mint_csrf(_REGISTER) if request.url.path == _REGISTER else _mint_bound(request.url.path, request)
    if not hmac.compare_digest(presented, expected):
        if str(request.session.get(_SESSION_EPOCH, "")):
            _next_action = "reload the page and re-send — the re-render mints a fresh token"
        else:
            _next_action = "your identification lapsed — reload, the page re-asks your name"
        raise CsrfRefusedError(
            expected=f"the form's {_CSRF_FIELD} field (minted into the served page)",
            found="absent-or-mismatched",
            next_action=_next_action,
        )


# The mounted whole's legal set (web-brief §3e): the web routes (the
# child's own path constants above) + the six service routes (the frozen
# wire's literals, cited) — the child's refusal handler teaches the whole
# face honestly.
_WEB_LANES: Final[tuple[str, ...]] = (
    f"GET {_LANDING}",
    f"GET {_SITTING}",
    f"GET {_DONE}",
    f"GET {_PROGRESS}",
    f"GET {_RESULT}",
    f"GET {_PICKER}",
    f"GET {_DELIBERATE}",
    f"POST {_REGISTER}",
    f"GET {_PAIR}",
    f"POST {_VOTE}",
    f"GET {_STATE_STRIP}",
    f"POST {_UNREMEMBER}",
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


def resolve(home: str, tail: str) -> str:
    """Resolve the web home: the CWD's copy first, the shipped package's the fallback.

    Purpose: the ordered resolution for both authored homes (the templates
    + the static): the CWD-relative copy WINS when present (the clone's
    repo-root discipline byte-preserved — the mounts receive the same
    bytes they receive today), else the shipped package's own copy
    (importlib.resources' files() over the wheel's force-include mapping
    — the installed lane renders from the package).
    Refuses when: never — a missing directory is a VALUE, never an error
    (the resolution lands on the derived path; the fold is the render
    tier's honest behavior — the wrong-cwd clone folds at the honest 500,
    the scratch-cwd boot stands on check_dir=False).
    Re-run: deterministic given the filesystem (the CWD's state + the
    package's own).
    Touches: nothing — a pure resolution over the filesystem's state.
    Provenance: install-brief §2/§3 (the ordered resolution),
    Q-repo-review ruling 4, G-INSTALLSPEC-BRIEF.
    """
    if Path(home).is_dir():
        return home
    return str(files(_PACKAGE).joinpath(tail))


# The child app (web-brief §3e: the docs routes DISABLED — the parent's own
# /docs, /redoc, /openapi.json stay live, registered before the mount). The
# static mount's check_dir=False: the acceptance harness boots at a scratch
# cwd (test_service_acceptance.py:81 — Popen(cwd=home)); StaticFiles raises
# at construction on an absent directory, the store mkdirs on demand — the
# flag is the asymmetry's named cure (the re-settle's §5).
web_app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
# THE REMEMBER SEAM'S MOUNT (the design §1f/§2B — THE CHILD): the session
# rides the web lanes ALONE (the service's six JSON routes session-free, the
# llm/stdio/tools lanes never see a session — the humans'-lane constraint
# MECHANICAL at the bytes); the cookie minted "remember" (the naming law's
# wire artifact), max_age the 14-day default (the sitting's floor cleared
# WHOLE — the 780-s card covered 1550x), same_site=lax (the shareable URL's
# top-level entry preserved — Strict refused), HttpOnly HARDCODED at the
# engine (sessions.py:34 — never a knob).
web_app.add_middleware(
    SessionMiddleware,
    secret_key=_remember_secret.decode(),
    session_cookie=_REMEMBER_COOKIE,
    max_age=_REMEMBER_MAX_AGE,
    same_site="lax",
)
# THE ASSERT-GUARD (the parent-service silent bypass refused): Starlette's
# own request.session read asserts the mount (requests.py:170-177 —
# "SessionMiddleware must be installed to access request.session"); the
# CHILD alone carries it, so a future service-tier controller touching the
# session REFUSES LOUDLY and this construction check refuses the same drift
# at import — a web.py edit that drops the mount never serves silently.
if not any(middleware.cls is SessionMiddleware for middleware in web_app.user_middleware):
    _message = (
        "expected: SessionMiddleware mounted on the child web app (the remember seam); "
        "found: no SessionMiddleware in the child's middleware stack; "
        "next_action: restore the web_app.add_middleware(SessionMiddleware, ...) line — the remember region's own law"
    )
    raise RuntimeError(_message)
web_app.mount("/static", StaticFiles(directory=resolve(_STATIC_HOME, _STATIC_TAIL), check_dir=False), name="static")
templates = Jinja2Templates(directory=resolve(_TEMPLATES_HOME, _TEMPLATES_TAIL))

# THE IN-PROCESS CLIENT (web-brief §3a, ruled exact): ONE module-level
# instance, built at import against the imported service app, shared by all
# controllers, process-lifetime — no per-request construction, no teardown
# (ASGITransport holds no socket). raise_app_exceptions=False REQUIRED.
_WEB_KEY_ENV: Final[str] = "PRIORITYTREE_WEB_KEY"
_web_key: Final[str] = os.environ.get(_WEB_KEY_ENV, "")
_client = httpx2.AsyncClient(
    base_url=_BASE_URL,
    transport=httpx2.ASGITransport(app=service_app, raise_app_exceptions=False),
    headers={AUTH_HEADER_DEFAULT: _web_key} if _web_key else None,
)
logging.getLogger("uvicorn.error").info(
    "web tier key: %s (expected: the six-token grant)%s",
    "present" if _web_key else "absent",
    "" if _web_key else " — wire PRIORITYTREE_WEB_KEY at the next boot",
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


def _scheduled_pairs(manifest: dict[str, Any]) -> list[tuple[str, str]]:
    """Return the manifest's scheduled pairs — the picker list's datum, the pair set's one home cited.

    Purpose: the deliberate lane's list datum — schedule_pairs over the
    manifest body's item ids (the scheduler's own enumeration, CITED never
    re-derived — the same pair universe the chain walks and the door
    legalizes), rendered as (item_a, item_b) tuples for the templates
    (the canonical id-sorted order; the picker's links compose the ?swap
    form over it — either presentation openable).
    Refuses when: never — a pure projection over the manifest's own rows.
    Re-run: deterministic — the same items yield the same pair list.
    Touches: nothing.
    Provenance: amendment 22 (the deliberate-pair lane — the manifest's
    data), R7 (the pair set's one home), G-WEB.
    """
    ids = [str(row[0]) for row in manifest["items"]]
    return [(pair.item_a, pair.item_b) for pair in schedule_pairs(ids)]


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
        request,
        "unknown.html",
        {"fields": _fields(body)},
        status_code=_NOT_FOUND,
    )


def _auth_page(request: Request, body: dict[str, Any], *, forbidden: bool) -> Response:
    """Render the auth lane's page — the service's OWN three fields verbatim, the path's heading.

    (The fold's clothes never worn.)

    Provenance: the unit brief §1c, rikai map 3, G-SERVING-TIER-INTEGRATION-BRIEF.
    """
    return templates.TemplateResponse(
        request,
        "auth.html",
        {"fields": _fields(body), "forbidden": forbidden},
        status_code=_FORBIDDEN if forbidden else _UNAUTHORIZED,
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
        request,
        "refuse.html",
        {"fields": fields, "fold": fold},
        status_code=_OK,
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
    the path), next_action the MOUNTED WHOLE's legal set (the web
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
        request,
        "fold.html",
        {"fields": _fields_fold},
        status_code=_CRASH,
    )


@web_app.exception_handler(CsrfRefusedError)
def refuse_csrf(request: Request, exc: CsrfRefusedError) -> Response:
    """Render the CSRF refusal as the refusal fragment at 200 — the drive-by SEEN, never a silent OK.

    Purpose: the child's DEDICATED handler for the typed CSRF refusal —
    never the fold's clothes (the crash page's garb never worn): the
    refusal's three fields rendered as the refusal fragment at 200 (the
    page context preserved — the refusal is SEEN, never a silent OK).
    Refuses when: never — the handler renders; the refusal IS the input
    (exc.expected/found/next_action verbatim, never re-derived).
    Re-run: deterministic — the same refusal renders the same fragment.
    Touches: nothing.

    Provenance: the unit brief §3c, rikai map 2 (the landing mechanics' seam),
    G-SERVING-TIER-INTEGRATION-BRIEF.
    """
    return _refuse_fragment(
        request,
        {"expected": exc.expected, "found": exc.found, "next_action": exc.next_action},
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
    return templates.TemplateResponse(
        request,
        "landing.html",
        {"csrf_token": _mint_csrf(_REGISTER), "remembered_name": _remembered(request)},
    )


@web_app.get(_SITTING)
async def sitting(request: Request, stem: str, *, swap: bool = False) -> Response:
    """Sit the comparator — the question as prompt, the first pair server-side.

    Purpose: consume the manifest (the question, the declared verdicts, the
    quorum) + next (the FIRST PAIR rendered server-side — a pure query
    render; the two-step law bars the POST's RESPONSE from carrying the
    pair, never the page's query). Cards A/B marked + labeled (the label
    map); the count UNREAD — never in the render context (the no-anchoring
    law, by construction). DONE => the done page rendered whole for the
    plain browser (the bare 200 + HX-Redirect an HTMX-only affordance a
    plain browser never honors — the white screen's cure, amendment 22;
    the teaching + the tally's and the deliberate lane's links riding the
    template). The swap the query knob: the pair PRESENTED in the swapped
    order (the order-bias probe's instrument — the served body's
    item_a/item_b the presented pair, the hidden presentation_order field
    re-sent at the vote). 404 => the unknown-run page at the honest 404;
    any other non-200 => the fold page at the response's own status. The
    buttons hx-post the vote; the comparator entry rides every post; the
    deliberate lane's picker rides below the card (the manifest's pairs,
    each openable in either presentation).
    Refuses when: never by this hand — the branches render honestly.
    Re-run: deterministic given the store state.
    Touches: nothing — queries only.
    Provenance: web-brief §4 route 2, the design §7a/§8, amendment 22 (the
    done-state page + the sitting page's pair-picker), G-WEBSPEC-BRIEF.
    """
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code != _OK:
        if manifest.status_code == _NOT_FOUND:
            return _unknown(request, manifest.json())
        if manifest.status_code == _UNAUTHORIZED:
            return _auth_page(request, manifest.json(), forbidden=False)
        if manifest.status_code == _FORBIDDEN:
            return _auth_page(request, manifest.json(), forbidden=True)
        return templates.TemplateResponse(
            request,
            "fold.html",
            {"fields": _fields(manifest.json())},
            status_code=manifest.status_code,
        )
    nxt = await _service("GET", f"/runs/{stem}/next?swap=true" if swap else f"/runs/{stem}/next")
    if nxt.status_code != _OK:
        if nxt.status_code == _NOT_FOUND:
            return _unknown(request, nxt.json())
        if nxt.status_code == _UNAUTHORIZED:
            return _auth_page(request, nxt.json(), forbidden=False)
        if nxt.status_code == _FORBIDDEN:
            return _auth_page(request, nxt.json(), forbidden=True)
        return templates.TemplateResponse(
            request,
            "fold.html",
            {"fields": _fields(nxt.json())},
            status_code=nxt.status_code,
        )
    body = nxt.json()
    if body.get("done"):
        return templates.TemplateResponse(
            request,
            "done.html",
            {"stem": stem, "fields": _fields(body)},
            status_code=_OK,
        )
    manifest_body = manifest.json()
    labels = _labels(manifest_body)
    return templates.TemplateResponse(
        request,
        "sitting.html",
        {
            "stem": stem,
            "csrf_token": _mint_bound(f"/ui/runs/{stem}/vote", request),
            "remembered_name": _remembered(request),
            "unremember_token": _mint_bound(f"/ui/runs/{stem}/unremember", request),
            "question": str(manifest_body["question"]),
            "verdicts": list(manifest_body["verdicts"]),
            "quorum": int(manifest_body["quorum"]),
            "item_a": str(body["item_a"]),
            "item_b": str(body["item_b"]),
            "label_a": labels.get(str(body["item_a"]), str(body["item_a"])),
            "label_b": labels.get(str(body["item_b"]), str(body["item_b"])),
            "presentation_order": str(body["presentation_order"]),
            "labels": labels,
            "pairs": _scheduled_pairs(manifest_body),
        },
    )


@web_app.get(_DONE)
async def done(request: Request, stem: str) -> Response:
    """State the run's coverage honestly — the DONE body's expected verbatim.

    Purpose: consume next (the DONE body — a VALUE, never an error):
    done:true => the coverage statement (the body's expected field VERBATIM —
    every pair at quorum k={K} AND corroborated — + the plain-words
    restatement + the tally's link + the deliberate lane's link); a pair
    body (the re-opened edge — the signal is a state read, not a latch) =>
    the TRUE 302 + Location to the sitting page (the docstring's own stated
    intent kept; the page's inbound lanes the plain anchors alone — a plain
    browser honors it; the fragment tier's HX-Redirect lane untouched);
    THE CACHE'S LAW: the redirect STATE-DEPENDENT (one URL, two states by
    the queue) — 302/303 never cached by default, the permanent verbs
    301/308 BARRED — they would pin the queue's state into the browser's
    cache; 404 => the unknown-run page; any other non-200 => the fold page
    at the response's own status.
    Refuses when: never by this hand.
    Re-run: deterministic given the store state.
    Touches: nothing — a query.
    Provenance: web-brief §4 route 3, the design §7c, G-WEBSPEC-BRIEF; the
    bridge brief §1(a) (the true-302 cure), packet build/bridge.
    """
    nxt = await _service("GET", f"/runs/{stem}/next")
    if nxt.status_code != _OK:
        if nxt.status_code == _NOT_FOUND:
            return _unknown(request, nxt.json())
        if nxt.status_code == _UNAUTHORIZED:
            return _auth_page(request, nxt.json(), forbidden=False)
        if nxt.status_code == _FORBIDDEN:
            return _auth_page(request, nxt.json(), forbidden=True)
        return templates.TemplateResponse(
            request,
            "fold.html",
            {"fields": _fields(nxt.json())},
            status_code=nxt.status_code,
        )
    body = nxt.json()
    if not body.get("done"):
        return RedirectResponse(f"/runs/{stem}", status_code=_FOUND)
    return templates.TemplateResponse(
        request,
        "done.html",
        {"stem": stem, "fields": _fields(body)},
        status_code=_OK,
    )


@web_app.get(_PICKER)
async def pick(request: Request, stem: str) -> Response:
    """Pick the pair deliberately — the lane's picker page: every scheduled pair, both presentations.

    Purpose: the deliberate-pair lane's HOME (the done page's link target —
    the lane reachable at ANY coverage point): consume the manifest (the
    items — the picker list's datum), render the picker page listing every
    scheduled pair with BOTH presentations' links (the ?swap form composed
    into the links — the order-bias probe's instrument at the deliberate
    lane); NO next consult (the lane coverage-blind: the chain's done state
    never gates the deliberate judgment — every judgment appended, the
    record keeps them all). 404 => the unknown-run page; 401/403 => the auth
    pages; any other non-200 => the fold page at the response's own status.
    Refuses when: never by this hand — the branches render honestly.
    Re-run: deterministic given the store state.
    Touches: nothing — a query.
    Provenance: amendment 22 (the deliberate-pair lane — the picker's
    list), web-brief §4's page school, G-WEBSPEC-BRIEF.
    """
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code != _OK:
        if manifest.status_code == _NOT_FOUND:
            return _unknown(request, manifest.json())
        if manifest.status_code == _UNAUTHORIZED:
            return _auth_page(request, manifest.json(), forbidden=False)
        if manifest.status_code == _FORBIDDEN:
            return _auth_page(request, manifest.json(), forbidden=True)
        return templates.TemplateResponse(
            request,
            "fold.html",
            {"fields": _fields(manifest.json())},
            status_code=manifest.status_code,
        )
    manifest_body = manifest.json()
    return templates.TemplateResponse(
        request,
        "pairs.html",
        {"stem": stem, "labels": _labels(manifest_body), "pairs": _scheduled_pairs(manifest_body)},
    )


@web_app.get(_DELIBERATE)
async def judge(
    request: Request,
    stem: str,
    item_a: str = "",
    item_b: str = "",
    *,
    swap: bool = False,
) -> Response:
    """Judge the chosen pair deliberately — the existing card + cast form, either presentation.

    Purpose: the deliberate lane's CARD (the picker's link target): consume
    the manifest, render the CHOSEN pair on the sitting surface (the
    existing pair card + the existing cast form re-used whole — the door
    UNCHANGED: the stamps via the tier key at the authenticated door, the
    body's claim at the degrade; presentation_order carried by the hidden
    field; every judgment appended — the record keeps them all). The
    presented pair: (item_a, item_b) as cited at the canonical form; the
    swap query knob presents the SWAPPED order (the order-bias probe's
    instrument — the same knob the sitting page carries); NO next consult
    (the chosen pair rendered whatever the chain serves — a vote legal on
    any registered pair at any coverage point). 404 => the unknown-run
    page; 401/403 => the auth pages; any other non-200 => the fold page at
    the response's own status.
    The chain query param (default "", read from the request's query)
    passes through to the sitting context — the ack-carry lane's remaining
    list (the flow fix: the count's P-tokens comma-joined; non-empty rides
    pair.html's hidden carry page to page, absent/empty renders no field —
    the sitting lane byte-untouched).
    The deliberate datum (the done-detour cure — the ROUTE's own
    knowledge, never a query param): the constant "true" rides the
    sitting context at EVERY judge-page render (the bare form + the
    chain form alike) — pair.html's conditional carry holds the
    field page to page.
    Refuses when: never by this hand — the page renders the pair AS CITED
    (the wire the sole validator: a mangled citation renders honestly, the
    vote's legality the door's own act).
    Re-run: deterministic given the store state.
    Touches: nothing — a query.
    Provenance: amendment 22 (the deliberate-pair lane — the existing card
    + the door unchanged), web-brief §4 route 2's surface re-used, the
    flow-fix folds (the ack-carry — the chain param's pass-through),
    G-WEBSPEC-BRIEF.
    """
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code != _OK:
        if manifest.status_code == _NOT_FOUND:
            return _unknown(request, manifest.json())
        if manifest.status_code == _UNAUTHORIZED:
            return _auth_page(request, manifest.json(), forbidden=False)
        if manifest.status_code == _FORBIDDEN:
            return _auth_page(request, manifest.json(), forbidden=True)
        return templates.TemplateResponse(
            request,
            "fold.html",
            {"fields": _fields(manifest.json())},
            status_code=manifest.status_code,
        )
    manifest_body = manifest.json()
    labels = _labels(manifest_body)
    chain = request.query_params.get("chain", "").strip()
    presented_a, presented_b = (item_b, item_a) if swap else (item_a, item_b)
    return templates.TemplateResponse(
        request,
        "sitting.html",
        {
            "stem": stem,
            "csrf_token": _mint_bound(f"/ui/runs/{stem}/vote", request),
            "remembered_name": _remembered(request),
            "unremember_token": _mint_bound(f"/ui/runs/{stem}/unremember", request),
            "question": str(manifest_body["question"]),
            "verdicts": list(manifest_body["verdicts"]),
            "quorum": int(manifest_body["quorum"]),
            "item_a": presented_a,
            "item_b": presented_b,
            "label_a": labels.get(presented_a, presented_a),
            "label_b": labels.get(presented_b, presented_b),
            "presentation_order": PRESENTATION_SWAPPED if swap else PRESENTATION_CANONICAL,
            "labels": labels,
            "pairs": _scheduled_pairs(manifest_body),
            "chain": chain,
            "deliberate": "true",
        },
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
        if result.status_code == _UNAUTHORIZED:
            return _auth_page(request, result.json(), forbidden=False)
        if result.status_code == _FORBIDDEN:
            return _auth_page(request, result.json(), forbidden=True)
        return templates.TemplateResponse(
            request,
            "fold.html",
            {"fields": _fields(result.json())},
            status_code=result.status_code,
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
        if tally.status_code == _UNAUTHORIZED:
            return _auth_page(request, tally.json(), forbidden=False)
        if tally.status_code == _FORBIDDEN:
            return _auth_page(request, tally.json(), forbidden=True)
        return templates.TemplateResponse(
            request,
            "fold.html",
            {"fields": _fields(tally.json())},
            status_code=tally.status_code,
        )
    whole = tally.json()
    if not bool(whole["coverage"]["done"]):
        return templates.TemplateResponse(
            request,
            "halt.html",
            {"stem": stem, "gated": True},
            status_code=_OK,
        )
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code != _OK:
        if manifest.status_code == _UNAUTHORIZED:
            return _auth_page(request, manifest.json(), forbidden=False)
        if manifest.status_code == _FORBIDDEN:
            return _auth_page(request, manifest.json(), forbidden=True)
        return templates.TemplateResponse(
            request,
            "fold.html",
            {"fields": _fields(manifest.json())},
            status_code=manifest.status_code,
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


@web_app.post(_REGISTER, dependencies=[Depends(_csrf_guard)])
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
async def pair(request: Request, stem: str, item_a: str = "", item_b: str = "", *, swap: bool = False) -> Response:
    """Serve the bare pair as a fragment — or the HX-Redirect on DONE.

    Purpose: TWO SERVE LANES. THE CITED RE-SERVE (the undo's lane, the
    cardspec): item_a/item_b both present => the CITED pair rendered per
    the judge route's citation law (the wire the sole validator: a mangled
    citation renders honestly, the vote's legality the wire's act) — NO
    next consult (the pair as cited, whatever the coverage; the
    no-anchoring law held), the presentation DERIVED from the cited order
    (the reversed citation the explicit swapped presentation — the
    fieldless swap never served); the supersedes/deliberate/chain query
    carries ride the re-served form's hidden fields (the undo's supersede
    carry + the lane's own datum, read from the request's query — the
    judge route's chain precedent); the fresh token minted, the question
    threaded (the legend's context — the fieldset binding the pair's
    question at EVERY serve). THE /NEXT SERVE (the defining call when no
    pair cited): consume next (+ the manifest's label map, §7a's label
    law — the map its label-bearing companion). 200 => the bare-pair
    fragment (cards A/B marked + labeled; the count UNREAD — dropped at
    the controller); its buttons hx-post the vote as the sitting's pair.
    DONE => the HX-Redirect RESPONSE HEADER to the done page (core
    HTMX's navigation verb — no extension, no JS). The swap the query
    knob: the pair PRESENTED in the swapped order (the order-bias
    probe's instrument — the served presentation re-sent at the vote).
    Any non-200 on either call => the refusal fragment at 200 (the fold
    wording at 500).
    Refuses when: never by this hand.
    Re-run: deterministic given the store state.
    Touches: nothing — a query.
    Provenance: web-brief §4 route 7, the design §7a/§8, G-WEBSPEC-BRIEF;
    the journey design 1.1/1.4 + the cardspec (the cited re-serve, the
    question thread, the carries), G-CARDSPEC-BRIEF.
    """
    supersedes = request.query_params.get("supersedes", "").strip()
    deliberate = request.query_params.get("deliberate", "").strip()
    chain = request.query_params.get("chain", "").strip()
    cited = bool(item_a.strip() and item_b.strip())
    served: dict[str, Any] = {}  # the /next body's pre-binding — the cited lane never reads it
    if not cited:
        nxt = await _service("GET", f"/runs/{stem}/next?swap=true" if swap else f"/runs/{stem}/next")
        if nxt.status_code != _OK:
            return _refuse_fragment(request, _fields(nxt.json()), fold=nxt.status_code == _CRASH)
        served = nxt.json()
        if served.get("done"):
            return Response(status_code=_OK, headers={"HX-Redirect": f"/runs/{stem}/done"})
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code != _OK:
        return _refuse_fragment(request, _fields(manifest.json()), fold=manifest.status_code == _CRASH)
    manifest_body = manifest.json()
    labels = _labels(manifest_body)
    if cited:
        presented_a, presented_b = item_a.strip(), item_b.strip()
        presentation = PRESENTATION_SWAPPED if presented_a > presented_b else PRESENTATION_CANONICAL
    else:
        presented_a, presented_b = str(served["item_a"]), str(served["item_b"])
        presentation = str(served["presentation_order"])
    return templates.TemplateResponse(
        request,
        "pair.html",
        {
            "stem": stem,
            "csrf_token": _mint_bound(f"/ui/runs/{stem}/vote", request),
            "remembered_name": _remembered(request),
            "question": str(manifest_body["question"]),
            "item_a": presented_a,
            "item_b": presented_b,
            "label_a": labels.get(presented_a, presented_a),
            "label_b": labels.get(presented_b, presented_b),
            "presentation_order": presentation,
            "verdicts": list(manifest_body["verdicts"]),
            "supersedes": supersedes,
            "deliberate": deliberate,
            "chain": chain,
        },
    )


@web_app.post(_VOTE, dependencies=[Depends(_csrf_guard)])
async def vote(request: Request, stem: str) -> Response:
    """Cast the vote through the form — the ack chains to the next pair.

    Purpose: parse the form MANUALLY, POST the service's cast command, then
    the TWO-STEP CHAIN on 200: the vote-ack restates the verdict in
    ITEM-LABEL TERMS (§7a — "you preferred {label_a} (A) over {label_b}
    (B)" / the tie form; acknowledged:true => the idempotent echo in
    words; the count UNREAD, never rendered; the identifying vote's ack
    carries the re-cast teaching — the epoch minted at this vote, the
    page's path-bound token stale: to judge the pair again, reload first,
    the one step refreshing token + pair, never a queue consult) and
    embeds hx-trigger="load" +
    hx-get to the pair fragment targeting the pair region — the POST's
    response NEVER carries the pair; the load fires the fetch. THE CHAIN
    FORM FIELD (the flow fix's ack-carry), when present, REPLACES the
    fetch: the just-voted P-token (the schedule's index of the id-sorted
    pair, 02d) dropped from the comma-joined token list; non-empty rest =>
    the ack links the head's judge URL (the swap knob carried when the
    page's mode is swapped — the chain rides the page's presentation; the
    shrunken chain riding the URL); empty rest => the done-page LINK + the
    list-has-ended teaching — the ack STAYS (no fetch embedded: the /done
    bounce never fires at the deliberate lane). THE DELIBERATE FORM
    FIELD (the done-detour cure — the judge page's own datum, read AFTER
    the chain so a chain form carrying both fields takes the chain arms,
    the datum discarded): the bare lane HOLDS THE ACK — queue-blind,
    nothing computed (the stay-put arm); the template renders the
    confirmation + BOTH LINKS (the picker + the done page, static from
    the stem) — no fetch at the bare lane, the fragment never called.
    THE SUPERSEDES READ (the undo's wire, the cardspec): the payload
    gains the field at the optional-text form (absent/empty => None —
    the wire's own schema, votes.py:578); the corrected click rides the
    correction's citation (a NEW record citing the old, both standing —
    R9; the tally's weighting walks the link, the cell's weight
    unchanged). THE UNDO'S AFFORDANCE AT THE ACK (every arm): the
    context carries the cast's own vote_id (the original handle at the
    idempotent arm) + the pair as presented + the lane's carries — the
    template composes the re-serve's citation (5's fence); the re-serve
    targets #pair-region at the ack region's persistence (the region
    the swap's target, never its victim — the affordance survives the
    fetch, self-healing at the second click; the sub-second race the
    named residual, no new machinery).
    Any non-200
    on either call => the inline refusal at 200 — THE PAIR REGION UNTOUCHED
    (the same pair retryable: the refusal swaps into the ack region, never
    the pair region).
    Refuses when: never by this hand — the branches render honestly.
    Re-run: deterministic given the store state.
    Touches: the run file through the service (the command).
    Provenance: web-brief §4 route 8, the design §7a/§8, the flow-fix folds
    (the ack-carry — the chain's next link), G-WEBSPEC-BRIEF; the bridge
    brief §1(b) (the re-cast copy), packet build/bridge; the journey
    design 1.4 + the cardspec (the supersedes read, the undo's context),
    G-CARDSPEC-BRIEF.
    """
    form = await request.form()
    name = _remembered(request)
    identifying = not name  # the identifying act — the ack's re-cast teaching rides this flag
    if not name:
        name = str(form.get("comparator_id", "")).strip()
        if not name:
            return _refuse_fragment(
                request,
                {
                    "expected": "your remembered name, or the ask's answer at the first judgment",
                    "found": "no remembered entry and no name in the request",
                    "next_action": "your identification lapsed — reload the page, it re-asks your name",
                },
            )
        _remember(request, name)
    presentation = str(form.get("presentation_order", PRESENTATION_CANONICAL))
    payload: dict[str, Any] = {
        "pair": [str(form.get("item_a", "")), str(form.get("item_b", ""))],
        "winner": str(form.get("winner", "")),
        "comparator_id": name,
        "comparator_class": str(form.get("comparator_class", "human")),
        "presentation_order": presentation,
        "supersedes": str(form.get("supersedes", "")).strip() or None,
    }
    outcome = await _service("POST", f"/runs/{stem}/votes", json=payload)
    if outcome.status_code != _OK:
        return _refuse_fragment(request, _fields(outcome.json()), fold=outcome.status_code == _CRASH)
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code != _OK:
        return _refuse_fragment(request, _fields(manifest.json()), fold=manifest.status_code == _CRASH)
    labels = _labels(manifest.json())
    chain = str(form.get("chain", "")).strip()
    deliberate = str(form.get("deliberate", "")).strip()
    next_url = ""
    done_url = ""
    if chain:
        schedule = _scheduled_pairs(manifest.json())
        voted_a, voted_b = sorted(payload["pair"])
        just_token = f"P{schedule.index((voted_a, voted_b)) + 1:02d}"
        rest = [token for token in (part.strip() for part in chain.split(",")) if token and token != just_token]
        if rest:
            head = schedule[int(rest[0][1:]) - 1]
            swap_form = "&swap=true" if presentation == PRESENTATION_SWAPPED else ""
            next_url = f"/runs/{stem}/pair?item_a={head[0]}&item_b={head[1]}{swap_form}&chain={','.join(rest)}"
        else:
            done_url = f"/runs/{stem}/done"
    elif deliberate:
        # the stay-put arm: the bare deliberate lane — the ack template renders the
        # confirmation + both links (queue-blind, static from the stem); no fetch, no redirect
        pass
    return templates.TemplateResponse(
        request,
        "vote-ack.html",
        {
            "stem": stem,
            "winner": payload["winner"],
            "acknowledged": bool(outcome.json()["acknowledged"]),
            "vote_id": str(outcome.json()["vote_id"]),
            "identifying": identifying,
            "item_a": payload["pair"][0],
            "item_b": payload["pair"][1],
            "label_a": labels.get(payload["pair"][0], payload["pair"][0]),
            "label_b": labels.get(payload["pair"][1], payload["pair"][1]),
            "swap": presentation == PRESENTATION_SWAPPED,
            "chain": chain,
            "next_url": next_url,
            "done_url": done_url,
            "deliberate": deliberate,
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


@web_app.post(_UNREMEMBER, dependencies=[Depends(_csrf_guard)])
async def unremember(request: Request, stem: str) -> Response:
    """Un-remember this browser — the engine's deletion cookie wired, the sitting re-rendered.

    Purpose: the correction affordance's route (one affordance, two verbs:
    "not you? change your name" — the redirect's re-ask IS the
    re-identification, the epoch minting at the next identifying vote — and
    un-remember, the anonymous state); request.session.clear() arms the
    ENGINE'S OWN deletion cookie (sessions.py:80-89: the emptied-intercept
    emits remember=null; expires=Thu, 01 Jan 1970 — the identity-erase verb
    EXISTS at the engine, absent at the product until this route); the
    HX-Redirect response header navigates to the sitting page (the pair
    fragment's done-edge precedent, :924's form — the fresh render shows the
    ask, the conditional's own return). THE VERB'S HONESTY at [i]'s bound: it
    clears THIS browser's cookie, never a server kill — a stolen cookie
    elsewhere rides to max_age or the secret's rotation.
    Refuses when: never by this hand — the clear is the act (an empty session
    clears to the same empty state: no deletion cookie, nothing to erase).
    Re-run: deterministic given the session state.
    Touches: the session alone (the browser's cookie).
    Provenance: the unit brief §1f/§2, moho's findings 3+6 (the DIY
    cookie-edit's silent death), G-VOTERSESSIONSPEC-BRIEF.
    """
    request.session.clear()
    return Response(status_code=_OK, headers={"HX-Redirect": f"/runs/{stem}"})
