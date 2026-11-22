# Copyright (C) 2026 Mark Losey. All rights reserved.
"""service — the wire face: the five routes REST 1:1 over the lock seam.

The service-face unit (Q-service-routes' ruling: the five routes REST 1:1 through
Serialize — register/serve/cast/census/rank, one route per verb; the fence: the routes
compose Serialize ONLY, zero edits to any core module, no Persist at this tier). The
handlers sync def — FastAPI's threadpool runs them off the event loop, the seam's
process-wide lock serializing the acts across threads (Q-service-concurrency held at
the handler tier); each body reads the seam as cast(Serialize, request.app.state.seam)
— no Depends, no default-argument calls, B008 never fires by construction.
THE STATUS MAPPING (Q-service-routes): 200 success AND DONE (the exhausted queue a
STATE, never an error — the signal's three fields + the done marker, the tally pointer
already in next_action); 201 register's alone; 404 StoreRefusedError's both families
(the unknown run AND the corrupt file — the honest label, the found field carrying the
family's own words verbatim); 422 EXCLUSIVELY the door's value refusals
(VotesRefusedError) — THE RE-BADGE: the native RequestValidationError re-badged to 400
(the ruled record — the wire's consumers dispatch on refusal KIND, not framework
default; the 400 body carries the native detail grammar, the client's own fix map);
409 the SAFE HALT (TallyRefusedError); 500 THE CRASH ENVELOPE (Q-error-teaching's gap 1
— crashes first-class citizens: the article's three-part form, expected the request
attempted, found the exception verbatim, next_action the escalation path; Starlette's
ServerErrorMiddleware sends the envelope then re-raises — the traceback rides uvicorn's
LOG channel, never the body). The refusals caught BY TYPE, the three fields read as
DATA (never str(e) reparsed), rendered at ONE point (render_refusal). The module-level
app the whole ASGI surface — the launch form uvicorn prioritree.service:app; NO
uvicorn.run in src (S104 never fires, the boot the operator's command); the seam
injected at construction (app.state.seam = Serialize(STORE_HOME) — STORE_HOME the CLI's
own constant carried 1:1, the lock minted per process; the tests' isolation rides the
injection itself). THREE PRICED RECONCILIATIONS, named where they live: the vote route
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

from dataclasses import asdict, replace
from typing import Final, cast

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from prioritree.registry import OperatorDeclaration
from prioritree.run_store import STORE_HOME, StoreRefusedError
from prioritree.service_store import Serialize
from prioritree.session import ExhaustedQueue
from prioritree.tally import TallyRefusedError
from prioritree.votes import VotesRefusedError

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
EXPECTED: Final[str] = "expected"
FOUND: Final[str] = "found"
NEXT_ACTION: Final[str] = "next_action"
DETAIL: Final[str] = "detail"

# The 500 envelope's escalation path (the crash a first-class citizen: the
# traceback rides uvicorn's logging channel, never the body — the next_action
# names the only true path).
ESCALATION: Final[str] = "check the server logs — the traceback is recorded there; escalate to the operator"

# The route paths (content-in-configuration): the REST resource hierarchy named
# once, cited by the decorators (Q-service-routes' REST 1:1).
_RUNS_PATH: Final[str] = "/runs"
_NEXT_PATH: Final[str] = "/runs/{run_id}/next"
_VOTES_PATH: Final[str] = "/runs/{run_id}/votes"
_STATE_PATH: Final[str] = "/runs/{run_id}/state"


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
app = FastAPI()
app.state.seam = Serialize(STORE_HOME)


def render_refusal(
    refusal: StoreRefusedError | VotesRefusedError | TallyRefusedError,
) -> dict[str, str]:
    """Render the refusal's three fields as the wire body — the one render point.

    Purpose: one render point for every typed refusal — the three fields read as DATA
    (expected/found/next_action as attributes, never str(e) reparsed) returned as
    the three-key body the wire's consumers dispatch on; every refusal route cites
    this one function (a second rendering would fork the grammar).
    Refuses when: never — a pure rendering over the refusal's own fields.
    Re-run: deterministic — the same refusal renders the same body.
    Touches: nothing — a read of the injected refusal.
    Provenance: service-face-brief §3 (one render point), Q-service-routes (the
    three-field refusal grammar), Q-error-teaching (the fields as data).
    """
    return {EXPECTED: refusal.expected, FOUND: refusal.found, NEXT_ACTION: refusal.next_action}


@app.exception_handler(RequestValidationError)
def rebadge(_request: Request, exc: RequestValidationError) -> JSONResponse:
    """Re-badge the native validation errors to 400 — 422 exclusively the door's.

    Purpose: THE 422 RE-BADGE — the join's key reconciliation carried as the ruled
    form: FastAPI's native validation failure re-badged from its framework-default
    422 to 400 (the request's own grammar — the wire's consumers dispatch on refusal
    KIND, not framework default), the body carrying the native detail grammar
    ({DETAIL: exc.errors()} — loc/msg/type, the client's own fix map, machine-
    readable; the three-field form is the door's VALUE-refusal grammar — fabricating
    expected/found/next_action for a schema violation would dress the wrong family).
    Refuses when: never — the handler renders; the validation refusal IS the input
    (the error object rides the door's own grammar — never re-derived).
    Re-run: deterministic — the same validation error renders the same body.
    Touches: nothing — a rendering over the validation exception's own payload (the
    request body never re-read here; the door already refused it).
    Provenance: service-face-brief §3 (THE RE-BADGE — the join's key reconciliation,
    open question 5 ruled: the native detail grammar re-badged), Q-service-routes
    ("400 the request's own grammar" + "422 exclusively the door's"), G-SERVICE-
    ACCEPTANCE (the malformed request => 400), G-SERVICE-FACE.
    """
    return JSONResponse(status_code=400, content={DETAIL: exc.errors()})


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
_TALLY_PATH: Final[str] = "/runs/{run_id}/tally"


@app.post(_RUNS_PATH, status_code=201)
def register(request: Request, body: RegisterRunRequest) -> JSONResponse:
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
def serve(request: Request, run_id: str, seed: int | None = None) -> JSONResponse:
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
def cast_vote(request: Request, run_id: str, body: CastVoteRequest) -> JSONResponse:
    """Cast the vote over the seam — 200 the ack, the VoteRecord elided.

    Purpose: the vote route 1:1 — the seam's verb named cast_vote here (its own
    `cast` would shadow typing's typed assertion at module scope — the door's verb
    carried); delegate with the body's seven fields (the pair as a list — the
    door's own Sequence form), return 200 with the ack object {"vote_id",
    "count", "acknowledged"} — the VoteRecord elided (durable in the run file; the
    wire carries the ack).
    Refuses when: never by this hand — the seam's refusals ride through BY TYPE:
    StoreRefusedError => 404, VotesRefusedError => 422.
    Re-run: deterministic given the store state — a byte-identical re-send is the
    door's loud ack (the count unchanged, never double-counted).
    Touches: the run file through the seam (the append rides inside the lock).
    Provenance: service-face-brief §2 (the cast/ack body), §3 (the catch table),
    Q-service-routes, G-SERVICE-FACE.
    """
    seam = cast("Serialize", request.app.state.seam)
    try:
        vote_id, _record, count, acknowledged = seam.cast(
            run_id,
            list(body.pair),
            body.winner,
            body.comparator_id,
            body.comparator_class,
            body.notes,
            body.supersedes,
        )
    except StoreRefusedError as refusal:
        return JSONResponse(status_code=404, content=render_refusal(refusal))
    except VotesRefusedError as refusal:
        return JSONResponse(status_code=422, content=render_refusal(refusal))
    _ack = {VOTE_ID: vote_id, COUNT: count, ACKNOWLEDGED: acknowledged}
    return JSONResponse(status_code=200, content=_ack)


@app.get(_STATE_PATH)
def census(request: Request, run_id: str) -> JSONResponse:
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
def rank(request: Request, run_id: str) -> JSONResponse:
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
