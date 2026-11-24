# Copyright (C) 2026 Mark Losey. All rights reserved.
"""service — the wire face: the five routes REST 1:1 + the sixth query over the lock seam.

The service-face unit (Q-service-routes' ruling + the ux design's sixth
query: the five routes REST 1:1 through Serialize — register/serve/cast/
census/rank, one route per verb — plus THE SIXTH QUERY (GET /runs/{run_id}/
manifest: the store-tier manifest read; NOT one of the five ops — the
interface untouched); the fence: the routes compose Serialize ONLY, zero
edits to any core module, no Persist at this tier). The handlers sync def —
FastAPI's threadpool runs them off the event loop, the seam's process-wide
lock serializing the acts across threads (Q-service-concurrency held at the
handler tier); each body reads the seam as cast(Serialize, request.app.state.seam)
— the one Depends family the auth doors carry rides the TYPE annotation
(Annotated), never a default argument: B008 never fires by construction and
pyright's reportCallInDefaultInitializer is dodged by the same act.
THE STATUS MAPPING (Q-service-routes + the ux build's ThreePart cures): 200
success AND DONE (the exhausted queue a STATE, never an error — the signal's
three fields + the done marker, the tally pointer already in next_action);
201 register's alone; 401 the unverified key (KeyVerifyError — the auth
door's authentication half: absent-or-unknown the SAME three fields, the
identity oracle never fed; the dedicated handler, never the fold); 403 the
scope-denied key (KeyScopeError — the authorization half's own refusal) and
the supersedes author mismatch (SupersedeRefusedError at the cast route —
found elides the author); 404 StoreRefusedError's both families (the unknown
run AND the corrupt file — the honest label, the found field carrying the
family's own words verbatim) AND the framework's unmatched path (the refuse
handler — the bare Not Found never on the wire); 405 the disallowed method
(the same handler — the route table taught); 422 EXCLUSIVELY the door's
value refusals (VotesRefusedError) — THE RE-BADGE, taught (R5's cure): the
native RequestValidationError re-badged to 400 (the ruled record — the
wire's consumers dispatch on refusal KIND, not framework default; the body
the family grammar CONSTRUCTED from the route's schema + the violation as
carried); 409 the SAFE HALT (TallyRefusedError); 500 THE CRASH ENVELOPE
(Q-error-teaching's gap 1 — crashes first-class citizens: the article's
three-part form, expected the request attempted, found the exception
verbatim, next_action the escalation path; Starlette's ServerErrorMiddleware
sends the envelope then re-raises — the traceback rides uvicorn's LOG channel,
never the body). The refusals caught BY TYPE, the three fields read as DATA
(never str(e) reparsed), rendered at ONE point (render_refusal). The module-level
app the whole ASGI surface — the launch form uvicorn prioritree.service:app; NO
uvicorn.run in src (S104 never fires, the boot the operator's command); the seam
injected at construction (app.state.seam = Serialize(STORE_HOME) — STORE_HOME the CLI's
own constant carried 1:1, the lock minted per process; the tests' isolation rides the
injection itself); the AUTH knob read ONCE at the same construction (F1:
app.state.auth over resolve_auth_mode — the thin carrier, the on/off pair's
resolution the key_store module's own; a typo'd value refuses loudly AT BOOT, the
process dies honestly, never a silent on-or-off) with the boot marker rendered to
the log channel (the store module's own three-state form: on+present the
mode+count, on+absent THE HONEST LINE — the failopen named, the mint cited; off
the operator's explicit degrade). THREE PRICED RECONCILIATIONS, named where they live: the vote route
cast_vote (the seam's verb `cast` would shadow typing's typed assertion at module
scope — the door's own verb carried); every response a JSONResponse (ruff's ANN201
demands annotated returns, and a `dict | JSONResponse` annotation cannot build FastAPI's
response model at import — the ruled wire bytes ride byte-exact inside the uniform
envelope); and the tally body's coverage.pair_counts keyed by the pair-string form
(a Pair dataclass key cannot ride a JSON object — asdict's whole held everywhere the
wire permits). The tree's FIRST runtime deps (fastapi, pydantic) live at THIS tier
alone — the core and CLI stay zero-dep (the tier fence). Five-field docstrings on every
public symbol; content-in-configuration (the route paths and every body key named
constants); no asserts, no prints — the wire replaces stdout.
"""

from __future__ import annotations

import logging
import os
from dataclasses import asdict, replace
from typing import TYPE_CHECKING, Annotated, Final, cast

from fastapi import Depends, FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette.exceptions import HTTPException as StarletteHTTPException

from prioritree.key_store import KeyRecord, KeyStore, render_boot_marker, resolve_auth_mode, resolve_keys_home
from prioritree.key_verify import AUTH_HEADER_DEFAULT, KeyScopeError, KeyVerifyError, verify
from prioritree.registry import OperatorDeclaration
from prioritree.run_store import STORE_HOME, StoreRefusedError
from prioritree.service_store import Serialize
from prioritree.session import ExhaustedQueue
from prioritree.tally import TallyRefusedError
from prioritree.votes import SupersedeRefusedError, VotesRefusedError

if TYPE_CHECKING:
    from collections.abc import Callable

__all__ = ["app"]

# The wire's body keys (content-in-configuration): every JSON body key a named
# constant — the door's field names carried byte-exact on the wire, never
# re-typed at each return site.
RUN_ID: Final[str] = "run_id"
ITEM_A: Final[str] = "item_a"
ITEM_B: Final[str] = "item_b"
COUNT: Final[str] = "count"
VOTE_ID: Final[str] = "vote_id"
ACKNOWLEDGED: Final[str] = "acknowledged"
DONE: Final[str] = "done"
TOTAL: Final[str] = "total"
ITEMS: Final[str] = "items"
QUESTION: Final[str] = "question"
VERDICTS: Final[str] = "verdicts"
QUORUM: Final[str] = "quorum"
EXPECTED: Final[str] = "expected"
FOUND: Final[str] = "found"
NEXT_ACTION: Final[str] = "next_action"

_UNAUTHORIZED: Final[int] = 401
_FORBIDDEN: Final[int] = 403
_SERVICE_AUDIENCE: Final[str] = "service"
_AUTH_OFF: Final[str] = "off"

# The 500 envelope's escalation path (the crash a first-class citizen: the
# traceback rides uvicorn's logging channel, never the body — the next_action
# names the only true path).
ESCALATION: Final[str] = "check the server logs — the traceback is recorded there; escalate to the operator"

# The boot marker's log channel (content-in-configuration): uvicorn's own boot
# logger — the channel the operator's server.log captures at make start (the
# marker rides the LOG channel, never stdout — the wire replaces stdout; under
# pytest the channel is unconfigured, the INFO render silent by design).
_BOOT_LOG_CHANNEL: Final[str] = "uvicorn.error"

# The route paths (content-in-configuration): the REST resource hierarchy named
# once, cited by the decorators (Q-service-routes' REST 1:1).
_RUNS_PATH: Final[str] = "/runs"
_NEXT_PATH: Final[str] = "/runs/{run_id}/next"
_VOTES_PATH: Final[str] = "/runs/{run_id}/votes"
_STATE_PATH: Final[str] = "/runs/{run_id}/state"
_MANIFEST_PATH: Final[str] = "/runs/{run_id}/manifest"


class RegisterRunRequest(BaseModel):
    """RegisterRunRequest — the register wire body: the items, the operator, the question, the quorum.

    Purpose: carry the register route's request body as the validated door into the
    seam's register — items (the [id, label] pairs, payload order preserved: the
    pairs pass through to the door byte-exact, no token parsing invented at the
    route — the token form is argv's grammar, never the wire's), operator_id and
    question (the OperatorDeclaration built from the two at the route — the verdicts
    field the dataclass default's triple, the CLI's own construction re-carried),
    and quorum (default 1, the door's own default).
    Refuses when: never in Python — the VALIDATION is the model's own: a body missing
    a field or carrying a mistyped value raises RequestValidationError at FastAPI's
    door, re-badged to 400 by the app-level handler (the malformed request's own
    status — 422 stays exclusively the door's).
    Re-run: idempotent — a value type; the same bytes construct the same model (the
    door's own re-run semantics ride through the seam unchanged).
    Touches: nothing — a request model (Pydantic's own validation, the module's only
    in-flight state).
    Provenance: service-face-brief §2 (the request models — open question 2 ruled:
    pairs, never tokens), §3 (the 400's source), Q-service-routes, G-SERVICE-FACE.
    """

    items: list[tuple[str, str]]
    operator_id: str
    question: str
    quorum: int = 1


class CastVoteRequest(BaseModel):
    """CastVoteRequest — the vote wire body: the pair, the winner, the comparator, the correction.

    Purpose: carry the vote route's request body as the validated door into the
    seam's cast — pair (the two-array [item_a, item_b], canonical as sent — the
    model's tuple[str, str]), winner, comparator_id, comparator_class, and the two
    optional correction fields notes and supersedes (default None — the door's own
    optional grammar).
    Refuses when: never in Python — the VALIDATION is the model's own: a body missing
    a field, carrying a mistyped value, or a pair that is not a two-array of strings
    raises RequestValidationError at FastAPI's door, re-badged to 400 by the
    app-level handler (the malformed request's own status — 422 stays exclusively
    the door's).
    Re-run: idempotent — a value type; the same bytes construct the same model.
    Touches: nothing — a request model (Pydantic's own validation).
    Provenance: service-face-brief §2 (the request models, the vote body's pair as
    the two-array), §3 (the 400's source), Q-service-routes, G-SERVICE-FACE.
    """

    pair: tuple[str, str]
    winner: str
    comparator_id: str
    comparator_class: str
    notes: str | None = None
    supersedes: str | None = None


# The app the whole ASGI surface (Q-service-lifecycle: the module-level app, the
# launch form's own target — uvicorn prioritree.service:app; NO uvicorn.run in src —
# S104 never fires, the boot the operator's command). The injection at construction:
# the seam minted once per process over the CLI's own store home (STORE_HOME carried
# 1:1 — the plain default ruled, the env knob BANKED for the deployment era; the
# tests' isolation rides the injection itself: app.state.seam overwritten per test).
app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
app.state.seam = Serialize(STORE_HOME)

# The AUTH knob's construction (F1, the exact-task spec §5): ONE thin line
# reading the env — the on/off pair's resolution rides the key_store
# module's own resolve_auth_mode (a typo'd value refuses loudly HERE: the
# boot dies honestly, never a silent on-or-off); the routes read
# app.state.auth — the next unit's seam, NOT touched here. The boot marker
# (the log-channel render): the key store loaded once at boot for the count
# (the absent store the empty dict, never a refusal; the corrupt or
# world-writable store refuses HERE), the three states the store module's
# own render_boot_marker, emitted on uvicorn's boot channel (the log the
# operator's server.log captures; a daemon's unread marker still silent —
# the residual named).
app.state.auth = resolve_auth_mode(os.environ.get("AUTH"))
app.state.keys = KeyStore(resolve_keys_home().absolute())
logging.getLogger(_BOOT_LOG_CHANNEL).info(
    render_boot_marker(app.state.keys.home, app.state.auth, len(app.state.keys.records)),
)


# The auth-off degrade's carrier: a module constant record, digest="" the
# anonymous marker (the cast route's fallback reads it; the boot marker names
# the degrade — never per-request noise).
_ANONYMOUS: Final[KeyRecord] = KeyRecord(
    digest="", comparator_id="", comparator_class="human",
    scopes=frozenset(), audience=_SERVICE_AUDIENCE, created_at="",
)


def require_key(token: str) -> Callable[[Request], KeyRecord]:
    """Require the service-tier key carrying this route's scope token — the door.

    Purpose: THE FACTORY CLOSURE (the brief §3a): bind the route's own scope
    token; read request.app.state.auth — 'off' => the anonymous record (the
    failopen's ROUTE-TIER form, the operator's explicit degrade named at the
    boot marker, the cast door's stamp falls back to the body's claim — the
    degrade's price); 'on' => the store from app.state.keys (the boot's own
    container, the fixture's per-test overwrite the seam), the header read
    via AUTH_HEADER_DEFAULT (the name a knob from birth), verify(store,
    presented, "service", token) — the stat ride, the F9 dummy, the ONE
    compare, the F5 audience, the scope check ALL the verify seam's own; the
    KeyVerifyError/KeyScopeError typed data rides to the DEDICATED app-level
    handlers (never the fold, never the refuse lane's routing vocabulary).
    Refuses when: never here — the refusals ride verify's own typed data.
    Re-run: deterministic given the store state (the stat ride's re-load
    aside — a mid-flight mint lands live by design).
    Touches: the store's loaded state at most (the verify seam's own ride).
    Provenance: the unit brief §1a/§3a, the design's F5/F8/F9, rikai map 1,
    G-SERVING-TIER-INTEGRATION-BRIEF.
    """
    def _door(request: Request) -> KeyRecord:
        if request.app.state.auth == _AUTH_OFF:
            return _ANONYMOUS
        store = cast("KeyStore", request.app.state.keys)
        presented = request.headers.get(AUTH_HEADER_DEFAULT, "")
        return verify(store, presented, _SERVICE_AUDIENCE, token)
    return _door


_RegisterDoor = Annotated[KeyRecord, Depends(require_key("register"))]
_NextDoor = Annotated[KeyRecord, Depends(require_key("next"))]
_CastDoor = Annotated[KeyRecord, Depends(require_key("cast"))]
_StateDoor = Annotated[KeyRecord, Depends(require_key("state"))]
_TallyDoor = Annotated[KeyRecord, Depends(require_key("tally"))]
_ManifestDoor = Annotated[KeyRecord, Depends(require_key("manifest"))]


def render_refusal(
    refusal: StoreRefusedError
    | VotesRefusedError
    | TallyRefusedError
    | KeyVerifyError
    | KeyScopeError
    | SupersedeRefusedError,
) -> dict[str, str]:
    """Render the refusal's three fields as the wire body — the one render point.

    Purpose: one render point for every typed refusal — the three fields read as DATA
    (expected/found/next_action as attributes, never str(e) reparsed) returned as
    the three-key body the wire's consumers dispatch on; every refusal route cites
    this one function (a second rendering would fork the grammar); the union grown
    the key family (KeyVerifyError/KeyScopeError — the doors' typed data,
    shape-identical) and the supersedes author-refusal (SupersedeRefusedError —
    the cast route's 403) — every typed family rides this one point.
    Refuses when: never — a pure rendering over the refusal's own fields.
    Re-run: deterministic — the same refusal renders the same body.
    Touches: nothing — a read of the injected refusal.
    Provenance: service-face-brief §3 (one render point), Q-service-routes (the
    three-field refusal grammar), Q-error-teaching (the fields as data).
    """
    return {EXPECTED: refusal.expected, FOUND: refusal.found, NEXT_ACTION: refusal.next_action}


@app.exception_handler(RequestValidationError)
def rebadge(request: Request, exc: RequestValidationError) -> JSONResponse:
    """Re-badge the native validation errors to 400 — the schema violation taught.

    Purpose: THE 400 RE-BADGE, cured (R5's as-we-go mandate): FastAPI's native
    validation failure re-badged from its framework-default 422 to 400 (the
    malformed request's own status — the wire's consumers dispatch on refusal
    KIND, not framework default; 422 stays exclusively the door's), the body
    now the FAMILY GRAMMAR CONSTRUCTED from schema + violation — expected the
    legal body/query form named from the address's own route (the request's
    path identifies the schema: register's body, serve's seed query, the vote
    body), found the violation AS CARRIED (each error's loc + msg verbatim,
    ';'-joined — never re-derived), next_action the named cure. The old
    defense (the native detail grammar, {DETAIL: exc.errors()}) is amended by
    this cure — the census's in-code defense answered; the two grammars still
    never conflated: 400 the request's own malformed-body status, 422 the
    door's value refusals by type at the routes.
    Refuses when: never — the handler renders; the validation refusal IS the
    input (the error objects ride the door's own grammar — never re-derived).
    Re-run: deterministic — the same validation error renders the same body.
    Touches: nothing — a rendering over the validation exception's own payload
    (the request body never re-read here; the door already refused it).
    Provenance: the service unit brief §3 (cure 1 — the family construction),
    the ux design §10 (the cure map), R5 (THE THREEPART IS MANDATORY),
    Q-service-routes ("400 the request's own grammar" + "422 exclusively the
    door's"), G-SERVICE-FACE.
    """
    _violation = "; ".join(
        f"{'.'.join(str(part) for part in error['loc'])}: {error['msg']}" for error in exc.errors()
    )
    if request.url.path == _RUNS_PATH:
        _fields = "items a list of [id, label] two-string arrays (payload order preserved)"
        _expected = f"a register body: {_fields}; operator_id, question strings; quorum an integer"
        _cure = "correct the named field(s) and re-send the register request"
    elif request.url.path.endswith("/next"):
        _expected = "an optional integer seed query parameter on the next query (GET next carries no body)"
        _cure = "correct the seed query parameter and re-send the next request"
    else:
        _fields = "pair a [item_a, item_b] two-string array; winner, comparator_id, comparator_class strings"
        _expected = f"a vote body: {_fields}; notes, supersedes strings or null"
        _cure = "correct the named field(s) and re-send the vote request"
    return JSONResponse(
        status_code=400,
        content={EXPECTED: _expected, FOUND: _violation, NEXT_ACTION: _cure},
    )


@app.exception_handler(Exception)
def fold(request: Request, exc: Exception) -> JSONResponse:
    """Fold the unexpected exception into the same three-part envelope — the 500 crash envelope.

    Purpose: Q-error-teaching's gap 1 — CRASHES ARE FIRST-CLASS CITIZENS: the
    app-level catch-all (ONE emission point, the whole ASGI surface covered
    including framework-raised errors) folds any uncaught exception into the same
    three-part form — expected the request attempted (the method + the path), found
    the exception's type + message verbatim, next_action the escalation constant.
    Starlette's ServerErrorMiddleware sends the envelope then RE-RAISES: the
    traceback rides uvicorn's LOGGING channel, never the body. BLE001 fires here —
    the named ruling rides at the pyproject (the cli.py precedent re-cited).
    Refuses when: never — the crash IS the input; the handler renders, never re-raises.
    Re-run: deterministic in form — the same crash renders the same envelope (the
    traceback's channel is uvicorn's own logging, side of the wire).
    Touches: nothing — a rendering over the exception and the request's own method
    and path.
    Provenance: Q-error-teaching (gap 1 — the crash envelope, tane/kepric the
    references), service-face-brief §3 (the article's three-part form), §6 (the
    BLE001 ruling), G-SERVICE-FACE.
    """
    _attempted = f"{request.method} {request.url.path}"
    return JSONResponse(
        status_code=500,
        content={EXPECTED: _attempted, FOUND: f"{type(exc).__name__}: {exc}", NEXT_ACTION: ESCALATION},
    )


# The framework-refusal statuses (named per the zero-magic-value-in-src
# discipline — the handler branches on them; the codes FROZEN: the cure flips
# BODIES only, never the machine-dispatchable statuses).
_NOT_FOUND: Final[int] = 404
_METHOD_NOT_ALLOWED: Final[int] = 405


@app.exception_handler(StarletteHTTPException)
def refuse(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    """Refuse the framework's bare HTTP exceptions in the family grammar — 404/405 taught.

    Purpose: R5's census cure x2 — the framework's routing refusals ride bare
    from Starlette ({"detail": "Not Found"} / {"detail": "Method Not
    Allowed"}); this handler renders them in the family grammar CONSTRUCTED
    from the request's own address — expected the method + path as addressed
    (the fold's own _attempted form), found the routing violation named (404:
    no route matches the path; 405: the method not allowed at the path), and
    next_action the route table's legal lanes (the route/method set taught —
    the constant cited, content-in-configuration). The STATUS rides
    exc.status_code verbatim — the codes FROZEN (machine-dispatchable; the
    acceptance harness's 404-as-ready probe rides the status, untouched);
    any other StarletteHTTPException (none raised by this surface) carries
    the family fields with found the framework's own detail. The typed
    refusals ride through BY TYPE untouched — the routes' catch tables stand;
    this handler never sees them.
    Refuses when: never — the handler renders; the framework's refusal IS the
    input (exc.status_code + exc.detail, never re-derived).
    Re-run: deterministic — the same request renders the same body.
    Touches: nothing — a rendering over the exception and the request's own
    method and path.
    Provenance: the service unit brief §3 (cure 2 — the framework defaults),
    the ux design §10 (the cure map), R5, G-SERVICE-FACE.
    """
    _address = f"{request.method} {request.url.path}"
    if exc.status_code == _NOT_FOUND:
        _found = f"no route matches the path {request.url.path}"
    elif exc.status_code == _METHOD_NOT_ALLOWED:
        _found = f"the method {request.method} is not allowed at the path {request.url.path}"
    else:
        _found = exc.detail
    return JSONResponse(
        status_code=exc.status_code,
        content={EXPECTED: _address, FOUND: _found, NEXT_ACTION: _ROUTE_TABLE},
    )


@app.exception_handler(KeyVerifyError)
def refuse_key(request: Request, exc: KeyVerifyError) -> JSONResponse:
    """Refuse the unverified key in the family grammar at 401 — the door's own typed data rendered.

    Provenance: the unit brief §3b, rikai map 1 (the dispatch mechanics),
    G-SERVING-TIER-INTEGRATION-BRIEF.
    """
    return JSONResponse(status_code=_UNAUTHORIZED, content=render_refusal(exc))


@app.exception_handler(KeyScopeError)
def refuse_scope(request: Request, exc: KeyScopeError) -> JSONResponse:
    """Refuse the scope-denied key in the family grammar at 403 — the authorization half's own refusal.

    Provenance: the unit brief §3b, Q-auth-design's scope ruling,
    G-SERVING-TIER-INTEGRATION-BRIEF.
    """
    return JSONResponse(status_code=_FORBIDDEN, content=render_refusal(exc))
_TALLY_PATH: Final[str] = "/runs/{run_id}/tally"
# The route table as the wire's own cure vocabulary (the legal lanes named
# ONCE from the path constants — content-in-configuration; the framework-
# refusal handler's next_action cites it: the route/method set taught).
_ROUTE_TABLE: Final[str] = "address a legal route — " + ", ".join(
    (
        f"POST {_RUNS_PATH}",
        f"GET {_NEXT_PATH}",
        f"POST {_VOTES_PATH}",
        f"GET {_STATE_PATH}",
        f"GET {_TALLY_PATH}",
        f"GET {_MANIFEST_PATH}",
    ),
)


@app.post(_RUNS_PATH, status_code=201)
def register(request: Request, body: RegisterRunRequest, record: _RegisterDoor) -> JSONResponse:
    """Register the run over the seam — 201 the stem, the door's refusals mapped.

    Purpose: the register route 1:1 — build OperatorDeclaration(id=body.operator_id,
    question=body.question) at the body (the CLI's own construction re-carried, the
    verdicts field the dataclass default's triple), delegate to the seam's register,
    return 201 with {"run_id": the file's stem} (the cross-process identity; the
    manifest durable in the file).
    Refuses when: never by this hand — the seam's refusals ride through BY TYPE:
    StoreRefusedError => 404 (both families — the honest label), VotesRefusedError
    => 422 (the door's value refusal — 422 exclusively the door's).
    Re-run: deterministic given the store home's state — the stem continues the
    home's max (the dir is the truth).
    Touches: only the run file through the seam (the fence: Serialize ONLY).
    Provenance: service-face-brief §2 (the register body), §3 (the catch table),
    Q-service-routes, G-SERVICE-FACE.
    """
    seam = cast("Serialize", request.app.state.seam)
    operator = OperatorDeclaration(id=body.operator_id, question=body.question)
    try:
        stem = seam.register(body.items, operator, body.quorum)
    except StoreRefusedError as refusal:
        return JSONResponse(status_code=404, content=render_refusal(refusal))
    except VotesRefusedError as refusal:
        return JSONResponse(status_code=422, content=render_refusal(refusal))
    return JSONResponse(status_code=201, content={RUN_ID: stem})


@app.get(_NEXT_PATH)
def serve(request: Request, run_id: str, record: _NextDoor, seed: int | None = None) -> JSONResponse:
    """Serve the next under-quorum pair over the seam — 200 the triple, DONE a state.

    Purpose: the serve route 1:1 — the seed the optional query param (serve's own
    knob mirrored; GET carries no body), delegate to the seam's serve, return 200
    with the pair object {"item_a", "item_b", "count"}. The queue exhausted:
    ExhaustedQueue is DONE, a STATE never an error — 200 with the signal's three
    fields plus the done marker (the tally pointer already in next_action).
    Refuses when: never by this hand — the seam's refusals ride through BY TYPE:
    StoreRefusedError => 404, VotesRefusedError => 422.
    Re-run: deterministic given the store state — pure between casts (the door's
    semantics verbatim).
    Touches: only the run file through the seam (a read).
    Provenance: service-face-brief §2 (the seed param, the pair body), §3 (the DONE
    200 body), Q-service-routes, G-SERVICE-FACE.
    """
    seam = cast("Serialize", request.app.state.seam)
    try:
        item_a, item_b, count = seam.serve(run_id, seed)
    except StoreRefusedError as refusal:
        return JSONResponse(status_code=404, content=render_refusal(refusal))
    except VotesRefusedError as refusal:
        return JSONResponse(status_code=422, content=render_refusal(refusal))
    except ExhaustedQueue as done:
        _done_body = {DONE: True, EXPECTED: done.expected, FOUND: done.found, NEXT_ACTION: done.next_action}
        return JSONResponse(status_code=200, content=_done_body)
    return JSONResponse(status_code=200, content={ITEM_A: item_a, ITEM_B: item_b, COUNT: count})


@app.post(_VOTES_PATH)
def cast_vote(request: Request, run_id: str, body: CastVoteRequest, record: _CastDoor) -> JSONResponse:
    """Cast the vote over the seam — 200 the ack, the VoteRecord elided.

    Purpose: the vote route 1:1 — the seam's verb named cast_vote here (its own
    `cast` would shadow typing's typed assertion at module scope — the door's verb
    carried); delegate with the pair, winner, notes, and supersedes from the body
    plus the DOOR RECORD'S verified stamps — comparator_id and comparator_class
    from the dependency's KeyRecord in place of the body's self-claims (F8: the
    self-claim dies at the cast door; under the degrade the body's claim stands —
    the boot marker names it), return 200 with the ack object {"vote_id",
    "count", "acknowledged"} — the VoteRecord elided (durable in the run file; the
    wire carries the ack).
    Refuses when: never by this hand — the seam's refusals ride through BY TYPE:
    StoreRefusedError => 404, VotesRefusedError => 422, SupersedeRefusedError =>
    403 (the supersedes author mismatch — found elides the author).
    Re-run: deterministic given the store state — a byte-identical re-send is the
    door's loud ack (the count unchanged, never double-counted).
    Touches: the run file through the seam (the append rides inside the lock).
    Provenance: service-face-brief §2 (the cast/ack body), §3 (the catch table),
    Q-service-routes, G-SERVICE-FACE; the stamps and the 403 clause at
    servingtierintegrationspec §1h/§1i, G-SERVING-TIER-INTEGRATION-BRIEF.
    """
    seam = cast("Serialize", request.app.state.seam)
    comparator_id = record.comparator_id if record.digest else body.comparator_id
    comparator_class = record.comparator_class if record.digest else body.comparator_class
    try:
        vote_id, _record, count, acknowledged = seam.cast(
            run_id,
            list(body.pair),
            body.winner,
            comparator_id,
            comparator_class,
            body.notes,
            body.supersedes,
        )
    except StoreRefusedError as refusal:
        return JSONResponse(status_code=404, content=render_refusal(refusal))
    except VotesRefusedError as refusal:
        return JSONResponse(status_code=422, content=render_refusal(refusal))
    except SupersedeRefusedError as refusal:
        return JSONResponse(status_code=_FORBIDDEN, content=render_refusal(refusal))
    _ack = {VOTE_ID: vote_id, COUNT: count, ACKNOWLEDGED: acknowledged}
    return JSONResponse(status_code=200, content=_ack)


@app.get(_STATE_PATH)
def census(request: Request, run_id: str, record: _StateDoor) -> JSONResponse:
    """Census the run over the seam — 200 the summary, the vote_log elided.

    Purpose: the census route 1:1 — delegate to the seam's census, return 200 with
    the summary object {"total": len(vote_log), "items": {id: count, ...}} (the
    CLI's summary form mirrored) — the vote_log elided because the stamps re-mint
    at load (rendering lies); the per-item counts as data (0 included).
    Refuses when: never by this hand — the seam's refusals ride through BY TYPE:
    StoreRefusedError => 404, VotesRefusedError => 422 — never on coverage (the
    manifest-only file is the all-zero maps + the empty log, a VALUE).
    Re-run: deterministic given the store state — pure between casts.
    Touches: only the run file through the seam (a read).
    Provenance: service-face-brief §2 (the census body — open question 4 ruled), §3
    (the catch table), Q-service-routes, G-SERVICE-FACE.
    """
    seam = cast("Serialize", request.app.state.seam)
    try:
        snapshot = seam.census(run_id)
    except StoreRefusedError as refusal:
        return JSONResponse(status_code=404, content=render_refusal(refusal))
    except VotesRefusedError as refusal:
        return JSONResponse(status_code=422, content=render_refusal(refusal))
    _state = {TOTAL: len(snapshot.vote_log), ITEMS: dict(snapshot.per_item_counts)}
    return JSONResponse(status_code=200, content=_state)


# The tally body's coverage-block keys (tally.py's own field names, cited
# verbatim — the one place the face unit reads TallyResult's nested shape: the
# pair_counts reconciliation's own vocabulary, content-in-configuration).
COVERAGE: Final[str] = "coverage"
PAIR_COUNTS: Final[str] = "pair_counts"


@app.get(_TALLY_PATH)
def rank(request: Request, run_id: str, record: _TallyDoor) -> JSONResponse:
    """Rank the run over the seam — 200 the frozen whole, 409 the SAFE HALT.

    Purpose: the tally route 1:1 — delegate to the seam's rank, return 200 with
    asdict(result): TallyResult's frozen whole, the field names tally.py's own,
    never re-declared. THE ONE PRICED RECONCILIATION: coverage.pair_counts is keyed
    by Pair (a frozen dataclass) — a JSON object's keys must be strings, so those
    keys render as the "item_a|item_b" string form (each pair's ids verbatim, the
    canonical order, the bar the separator); every other field rides asdict's
    faithful whole (the ruled form held everywhere the wire permits).
    Refuses when: never by this hand — the seam's refusals ride through BY TYPE:
    StoreRefusedError => 404, VotesRefusedError => 422, TallyRefusedError => 409
    (the SAFE HALT, never swallowed).
    Re-run: deterministic given the store state — the purity property rides through
    (same store state, byte-identical emission).
    Touches: only the run file through the seam (a read).
    Provenance: service-face-brief §2 (the ranking: asdict the frozen whole), §3
    (the 409), Q-service-routes, G-SERVICE-FACE; the reconciliation priced at this
    packet's report (synthesize/service-face-bytes).
    """
    seam = cast("Serialize", request.app.state.seam)
    try:
        result = seam.rank(run_id)
    except StoreRefusedError as refusal:
        return JSONResponse(status_code=404, content=render_refusal(refusal))
    except VotesRefusedError as refusal:
        return JSONResponse(status_code=422, content=render_refusal(refusal))
    except TallyRefusedError as refusal:
        return JSONResponse(status_code=409, content=render_refusal(refusal))
    stripped = replace(result, coverage=replace(result.coverage, pair_counts={}))
    whole = asdict(stripped)
    _counts = {
        f"{pair.item_a}|{pair.item_b}": pair_count for pair, pair_count in result.coverage.pair_counts.items()
    }
    whole[COVERAGE][PAIR_COUNTS] = _counts
    return JSONResponse(status_code=200, content=whole)


@app.get(_MANIFEST_PATH)
def describe(request: Request, run_id: str, record: _ManifestDoor) -> JSONResponse:
    """Describe the run's frozen ground over the seam — 200 the manifest body, the stamps elided.

    Purpose: the manifest route 1:1 — THE SIXTH QUERY (the ux design's
    blocker-2 amendment; NOT one of the five ops — the store-tier read):
    delegate to the seam's manifest verb, return 200 with the five-key body
    — the STEM echoed from the path param (the wire's id law: the in-file
    handle never crosses), the stated question, the declared verdict set as
    a sorted array, the quorum as data, the items the [id, label] pairs
    payload order preserved; the operator id and the registration stamp
    ELIDED (the census's discipline — the query returns what the front end
    renders; the register ack holds the operator id from its own posted
    body).
    Refuses when: never by this hand — the seam's refusals ride through BY
    TYPE: StoreRefusedError => 404 (both families — the honest label); no
    value refusal exists at this read (422 never — the manifest line already
    validated at load's pre-pass).
    Re-run: deterministic given the store state — the manifest's clock-free
    fields re-derive identically at every load (the stamp named and excluded
    from any equality claim).
    Touches: only the run file through the seam (a read).
    Provenance: the service unit brief §2 (the sixth query's exact spec),
    the ux design §2 (BLOCKER 2's amendment), Q-ux-surface R2 (the query
    lane), G-SERVICE-FACE.
    """
    seam = cast("Serialize", request.app.state.seam)
    try:
        manifest = seam.manifest(run_id)
    except StoreRefusedError as refusal:
        return JSONResponse(status_code=404, content=render_refusal(refusal))
    _body = {
        RUN_ID: run_id,
        QUESTION: manifest.operator.question,
        VERDICTS: sorted(manifest.operator.verdicts),
        QUORUM: manifest.quorum,
        ITEMS: [[row.id, row.label] for row in manifest.items],
    }
    return JSONResponse(status_code=200, content=_body)


# The web tier's tail mount (web-brief §3c): the child app mounted at the
# root — the six JSON routes above match FIRST (the router serves the first
# FULL match, the Mount catching the rest); the web module imports THIS app
# at its own top, bound above before the tail import fires (the import
# cycle's only legal form — a top-of-file import would fire before the app
# binds; an importlib dodge would HIDE the cycle, not name it; the PLC0415
# named ruling rides pyproject).
from prioritree.web import web_app

app.mount("/", web_app)
