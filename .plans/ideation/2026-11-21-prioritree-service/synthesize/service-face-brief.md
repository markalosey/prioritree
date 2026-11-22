# synthesize/service-face-brief — THE SERVICE-FACE UNIT'S BUILD BRIEF (the exact-task spec)

**Status: PROPOSAL.** Togo proposes; the collaborator rules at G-SERVICE-FACE-BRIEF. Every [PROPOSED] element is an offered default with its one-line reason. The brief IS the spec (the exact-task law): once approved, jikko executes exactly, kensho re-runs independently.

## §0 THE GROUND — the join

- The legs joined: tansa's census + rikai's mechanisms, both read whole — NO divergence survives; the one priced reconciliation (the 422's two sources) carries as the ruled form at §3.
- The seam frozen (the routes' 1:1 targets, byte-exact): Serialize(store_home: Path); register(items, operator, quorum=1) -> str; serve(run_id, seed=None) -> the triple; cast(run_id, pair, winner, comparator_id, comparator_class, notes?, supersedes?) -> the ack quadruple; census(run_id) -> VoteCensus; rank(run_id) -> TallyResult — refusals ride through BY TYPE, never wrapped; the routes compose Serialize ONLY (the fence: zero edits to any core module).
- The rulings binding: Q-service-routes (REST 1:1; the mapping 200/201/404/422/409/400/500; the JSON bodies; the run-id the FILE STEM); Q-service-deps; Q-service-lifecycle; Q-service-floor; Q-error-teaching gap 1 (the crash envelope — the article's three-part form; tane/kepric the references).
- THE TRADE-OFF THE PLAN CARRIES: the wire seam bought at the tree's FIRST runtime deps (the zero-dep era's end, named honestly) and one platform convention deliberately left (the native 422 re-badged to 400 — the wire's consumers dispatch on refusal KIND, not framework default).

## §1 THE MODULE + THE APP'S CONSTRUCTION (src/prioritree/service.py)

- The module: service.py — the launch form's own target (uvicorn prioritree.service:app); the module-level app = FastAPI() the whole ASGI surface; NO uvicorn.run in src (S104 never fires; the boot the operator's command).
- The injection at construction: app.state.seam = Serialize(STORE_HOME) — STORE_HOME the CLI's own constant, the lock minted per process; the routes read request.app.state.seam INSIDE the handler bodies (the B008-dodge: no Depends, no default-argument calls — B008 never fires by construction).
- THE LAUNCH-CONFIG QUESTION priced: [PROPOSED the plain default — STORE_HOME at import time, CWD-relative, the CLI's own form carried 1:1; the env knob BANKED for the deployment-era widening]. Alternative: PRIORITREE_STORE_HOME read at construction. REASON: the CLI's CWD-relative home is today's one truth; the env knob buys a deployment that does not exist; the tests' isolation rides the ruled injection (app.state.seam overwritten per test — store-as-parameter), never the env.
- The pyright-strict edge at the injection: cast(Serialize, request.app.state.seam) — the registry school's typed assertion (State a dynamic bag; the cast the assertion, never an ignore).

## §2 THE FIVE ROUTES + THE MODELS (REST 1:1 — Q-service-routes)

- The handlers plain def (sync — the seam's threading.Lock form; FastAPI's threadpool runs them off the event loop, the lock serializing acts across threads — Q-service-concurrency held at the handler tier). The names per the naming law, the seam's verbs 1:1: POST /runs => register => 201 {"run_id": the stem}; GET /runs/{run_id}/next => serve => 200 the pair object; THE SEED: [PROPOSED the optional query param seed: int | None = None — serve's own knob mirrored; GET carries no body]; POST /runs/{run_id}/votes => cast => 200 the cast/ack object (201 is register's alone); GET /runs/{run_id}/state => census => 200 the census object; GET /runs/{run_id}/tally => rank => 200 TallyResult's frozen whole.
- THE REQUEST MODELS (Pydantic — the validation the 400's own source): RegisterRunRequest — items, operator_id, question, quorum: int = 1; CastVoteRequest — pair, winner, comparator_id, comparator_class, notes: str | None = None, supersedes: str | None = None. The register body's items form: [PROPOSED pairs — two-element arrays ["id", "label"], the model's list[tuple[str, str]]] (the seam accepts Sequence[Sequence[str] | ItemRow] directly — pairs pass through byte-exact, no token parsing invented at the route; the token form is argv's grammar, never the wire's). The vote body's pair: the two-array (the model's tuple[str, str]). OperatorDeclaration built from the body's operator_id + question (the CLI's own construction re-carried).
- THE RESPONSE BODIES ruled — [PROPOSED plain dicts for the responses; Pydantic models for the requests] (the responses render frozen values — models would re-declare the door's shapes, a second surface to keep true; the requests need validation, and the models ARE it): the register body {"run_id": the stem}; the pair object {"item_a", "item_b", "count"}; the cast/ack object {"vote_id", "count", "acknowledged"} (the VoteRecord elided — durable in the run file; the wire carries the ack); the census object [PROPOSED {"total": len(vote_log), "items": {id: count, ...}} — the CLI's summary form mirrored; the vote_log elided because the stamps re-mint at load (rendering lies)]; the ranking: TallyResult's frozen whole rendered faithfully — dataclasses.asdict (the field names tally.py's own, never re-declared).
- Content-in-configuration: the route paths and every body key named constants at the module top; five-field docstrings at every public symbol (the routes too).

## §3 THE STATUS MAPPING + THE 422 RE-BADGE + THE 500 CRASH ENVELOPE

- The per-route catch table (the typed refusals caught BY TYPE; the catches read the three fields as DATA — expected/found/next_action as attributes, never str(e) reparsed; one render point render_refusal): POST /runs: StoreRefusedError=>404, VotesRefusedError=>422; GET next: 404, 422, ExhaustedQueue=>200 DONE; POST votes: 404, 422; GET state: 404, 422; GET tally: 404, 422, TallyRefusedError=>409.
- THE HONEST LABEL priced (StoreRefusedError's two families): [PROPOSED 404 both — the unknown run AND the corrupt file] (the seam rides refusals BY TYPE — the route catches the type once; the found field carries the family's own words verbatim; a family split re-parses the message or forks the core type).
- THE DONE 200 body: {"done": true, "expected": ..., "found": ..., "next_action": ...} — the signal's three fields + the marker; the tally pointer already in next_action (DONE a state, never an error).
- THE 422 RE-BADGE — THE JOIN'S KEY RECONCILIATION, carried as the ruled form: @app.exception_handler(RequestValidationError) => rebadge ("Re-badge the native validation errors to 400") returning 400; 422 stays EXCLUSIVELY the door's (VotesRefusedError's lineage) — Q-service-routes' "400 the request's own grammar" + G-SERVICE-ACCEPTANCE's "the malformed request => 400"; leaving the native 422 convention fails the ruled acceptance arc. The 400 body priced: [PROPOSED FastAPI's own detail grammar re-badged — {"detail": exc.errors()} (loc/msg/type — the client's own fix map, machine-readable)] (the three-field form is the door's value-refusal grammar — fabricating expected/found/next_action for a schema violation dresses the wrong family; the native array is actionable as-is).
- THE 500 CRASH ENVELOPE (Q-error-teaching's gap 1 — "crashes are first-class citizens"; tane/kepric the references): @app.exception_handler(Exception) => fold ("Fold the unexpected exception into the same three-part envelope") — the app-level catch-all (ONE emission point, the whole ASGI surface covered including framework-raised errors; the route-level alternative five duplicated catches that still leak — rejected). THE BODY: expected = the request attempted (the method + the path); found = the exception's type + message verbatim; next_action = the escalation path (a named constant). Starlette's ServerErrorMiddleware sends the response then RE-RAISES: the traceback travels uvicorn's logging channel, NEVER the body; the body keys named constants — the same envelope keys as the refusals.

## §4 THE DEPS' LANDING (Q-service-deps; the tree's FIRST runtime deps)

- pyproject's exact opening: [project] dependencies = ["fastapi", "uvicorn[standard]"] (unbounded, uv.lock the pin); the dev group grows "httpx" => ["pytest", "pyright", "ruff", "httpx"].
- uv.lock regenerated at floor-green: uv lock + uv sync (the fixed-argv forms); the read-back named — the resolved set grows the known closure (fastapi => starlette => anyio => sniffio + idna; pydantic => pydantic-core + annotated-types + typing-extensions; uvicorn[standard] => click + h11 + httptools + python-dotenv + PyYAML + uvloop + watchfiles + websockets; httpx => certifi + httpcore).
- The tier fence: the core and CLI stay zero-dep; the service tier carries the framework.

## §5 THE TESTS (tests/test_service_face.py — fastapi.testclient.TestClient, in-process; Q-service-lifecycle)

- Isolation by injection: each test overwrites app.state.seam = Serialize(tmp_path) — store-as-parameter; no env, no CWD games. (1) THE FIVE SUCCESSES — each route's exact body asserted. (2) THE REFUSAL ARCS — 404 the unknown run (the live set in the body); 422 the out-of-set verdict (the three fields); 409 the SAFE HALT ("at quorum" verbatim). (3) THE RE-BADGE BOTH — a malformed register body => 400 (the native detail grammar); a door refusal => 422 (the family grammar) — the two grammars never conflated. (4) THE DONE 200 — the exhausted turn: done: true + the three fields; the tally pointer in next_action. (5) THE 500 ARC — the forced raise priced: [PROPOSED the monkeypatched seam verb — app.state.seam swapped for a stub whose verb raises RuntimeError; TestClient(app, raise_server_exceptions=False) (the production form); assert the three-part body AND the traceback's absence from the body] (the monkeypatch exercises the catch-all on a REAL route, zero product scaffolding; a test-only route lands a route that never serves — rejected). (6) THE 201 REGISTER — the stem in the body.

## §6 THE FLOOR (Q-service-floor; G-SERVICE-FACE's fourth condition)

- pyright 0 errors 0 warnings 0 informations (0/0/0); ruff zero findings — the zero-findings bar, zero ignores. THE ONE proposed named ruling: "src/prioritree/service.py" = ["BLE001"] — the 500 handler's except Exception (the cli.py precedent re-cited); other candidates named as they surface: B008 dodged by construction, S104 never in-tree. The pyright-strict framework edges cast-typed per the registry school (typed assertions, never ignores) — the State-bag seam read the one named edge. Five-field docstrings at every public symbol (the five handlers, the two models, render_refusal, rebadge, fold); the naming law; content-in-configuration; NO uvicorn.run in src; one-commit-per-increment.

## THE CARRIERS TABLE (G-SERVICE-FACE's four → the spec's carriers)

| the gate's condition | carried by |
|---|---|
| 1. the face lands per its approved brief — the exact-task law | the whole spec (§0-§6): the brief IS the spec |
| 2. the five routes 1:1 through the seam; the deps table opens; uv.lock regenerated; the tier fence | §1 (the module + the injection), §2 (the five routes, the frozen door cited), §4 (the deps + the lockfile's read-back) |
| 3. the status mapping green; the JSON report shapes ruled | §2 (the five bodies), §3 (the mapping table + the re-badge + the crash envelope) |
| 4. pyright 0/0 + ruff zero; kensho's independent re-run green | §5 (the falsification set), §6 (the floor) |

## THE OPEN QUESTIONS (each [PROPOSED] + alternative + reason — the collaborator rules)

1. THE LAUNCH-CONFIG KNOB — [PROPOSED the plain default, the env knob BANKED] / alternative: PRIORITREE_STORE_HOME now / reason: the CLI's own form carried 1:1; the knob buys a deployment that does not exist.
2. THE REGISTER BODY'S ITEMS FORM — [PROPOSED pairs] / alternative: id:label tokens / reason: the seam accepts pairs byte-exact; tokens are argv's grammar, never the wire's.
3. THE RESPONSE MODELS — [PROPOSED dicts for the responses, Pydantic for the requests] / alternative: Pydantic everywhere / reason: response models re-declare the door's frozen shapes — a second surface to keep true.
4. THE CENSUS BODY'S SHAPE — [PROPOSED {"total", "items"}] / alternative: the whole VoteCensus / reason: the CLI's summary form mirrored; the vote_log elided (the stamps re-mint at load — rendering lies).
5. THE 400 BODY'S GRAMMAR — [PROPOSED the native detail grammar re-badged] / alternative: the three-field re-render / reason: the three-field form is the door's value-refusal grammar; the native array is the client's own fix map.
6. THE 500 ARC'S FALSIFICATION — [PROPOSED the monkeypatched seam verb] / alternative: a test-only route / reason: the catch-all exercised on a REAL route, zero product scaffolding.
7. THE BLE001 RULING — [PROPOSED the per-file named ruling, the cli.py precedent re-cited] / alternative: none if the landed form fires no finding / reason: the 500 handler's except Exception is the CLI's exit-2 shape carried to the wire.
8. THE HONEST LABEL — [PROPOSED StoreRefusedError's both families at 404] / alternative: the corrupt family at 500 / reason: the type is the dispatch unit; the found field carries the family verbatim — a split re-parses or forks the core.

*The tree is the truth; the brief cites it. G-SERVICE-FACE-BRIEF awaits the collaborator's ruling — ready-to-build judged on these eight defaults; no build dispatch fires before.*
