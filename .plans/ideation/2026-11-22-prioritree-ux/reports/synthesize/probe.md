<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/probe

**Route:** prioritree-ux (executing) | **Events:** 3 | **Reports:** 2

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T12:00:51Z |
| 2 | report | togo | 2026-11-22T12:18:43Z |
| 3 | report | togo | 2026-11-22T12:19:14Z |
## Reported by togo — 2026-11-22T12:18:43Z

# THE SERVICE UNIT'S EXACT-TASK SPEC — PART 1 (synthesize/probe — the bytes-level build plan; togo, 2026-11-22)

THE GROUND, READ + CITED: reports/synthesize/service.md (my unit brief — the approved shape, G-SERVICE-BRIEF green) · reports/discover/service.md (tansa's line regions) · reports/understand/service.md (rikai's verified mechanisms) · reports/synthesize/ux-design.md (§§1-2, §10, §12) · src/prioritree/service.py (whole, 393 l.), service_store.py (whole, 209 l.), run_store.py (l.1-130, 468-882), registry.py (l.30-109 — RunManifest's frozen shape), session.py (l.130-189 — the register_run triple) · tests/test_service_face.py (whole, 265 l.), test_service_acceptance.py (whole, 417 l.) · pyproject.toml (the standing rulings), Makefile (the floor) · the ux store's junro.json (G-PROBE-BRIEF's conditions; the amendment naming this lane "the EXACT-TASK SPEC — FR-MEM-0011's doctrine: the bytes authored at synthesis, nothing to figure out at the execution seat") · FR-MEM-0011 (the doctrine verbatim) · the git reflog (the commit-shape precedent). READ-ONLY held — nothing written beyond this report.

## §0 THE TRADE-OFF THE SPEC CARRIES (named, per the seat's law)

Persist.manifest returns the l.690 reconstruction by HOLDING it from construction: the container's __init__ grows a FOURTH injected part (manifest: RunManifest), captured at BOTH factories (register's own mint at l.552; load's reconstruction at l.690). THE ALTERNATIVES REFUSED: (a) re-deriving through the door at read time — session._read_manifest is PRIVATE (the fence: privates never touched) and the five-op interface has no manifest op (Q-solution-space's frozen ruling); (b) a line-1-only file read at the store tier — a second parse fork of load's pre-pass, refusing the file's whole-integrity price (the brief §0's priced-and-refused alternative). THE PRICE: Persist(session, handle, run_file) becomes Persist(session, handle, run_file, manifest) — a construction-signature change; the census verified the factories are the ONLY construction sites (the cls() calls: run_store.py l.555 + l.706, both amended in this build; zero direct Persist(...) callers anywhere in src or tests) — the price fully paid inside this increment. SECOND PRICE, named: the 400/404/405 body wordings are AUTHORED HERE (expected/found/next_action strings byte-set at this seat, their tests pinning substrings of exactly these bytes) — jikko never phrases a field.

## §1 THE SIXTH QUERY, WHOLE (file → insertion point → fenced bytes)

### Region 1 — src/prioritree/run_store.py (882 l. at HEAD)

**1a. The TYPE_CHECKING import — REPLACE l.37:**
```
OLD:     from prioritree.registry import ItemRow
NEW:     from prioritree.registry import ItemRow, RunManifest
```

**1b. The class docstring's reads clause — REPLACE l.475-478:**
```
OLD:
    run (the manifest line FIRST, then one vote line per cast in mint order),
    the door composed ONLY (fresh Registry() + Session(registry) at the
    factories; the reads delegate through the door; no core store attribute
    ever touched — the fence held by construction); SAVE-AT-CAST: the capture
NEW:
    run (the manifest line FIRST, then one vote line per cast in mint order),
    the door composed ONLY (fresh Registry() + Session(registry) at the
    factories; the reads delegate through the door — the manifest read the
    one held-record exception (register_run's own mint, re-minted at load's
    reconstruction); no core store attribute ever touched — the fence held
    by construction); SAVE-AT-CAST: the capture
```

**1c. __init__ — REPLACE l.504-519 whole:**
```python
    def __init__(self, session: Session, handle: str, run_file: Path, manifest: RunManifest) -> None:
        """Initialize the container over the injected parts.

        Purpose: hold the door's session, the run's in-file handle (the door's
        verbatim run_id), the run file's path, and the run's frozen ground (the
        RunManifest register_run mints — captured whole at BOTH factories:
        register's own mint, load's reconstruction — the parts injected; the
        factories compose (store-as-parameter; never a module-level
        singleton — test isolation).
        Refuses when: never.
        Re-run: idempotent — a fresh container over the given parts.
        Touches: only its own references.
        Provenance: run-store-brief §1 (the container's constructor, the
        parts-injected ruling), the ux build's sixth query (the manifest held
        from construction), G-RUN-STORE.
        """
        self._session = session
        self._handle = handle
        self._run_file = run_file
        self._manifest = manifest
```

**1d. register's construction — REPLACE l.555:**
```
OLD:         persist = cls(session, run_id, run_file)
NEW:         persist = cls(session, run_id, run_file, manifest)
```
(register's l.552 already holds the mint: `run_id, manifest, _count = session.register_run(items, operator, quorum)` — the local passes unchanged.)

**1e. load's docstring — REPLACE l.588-593:**
```
OLD:
        then the reconstruction — a fresh door, register_run from the wire's
        arrays (the door re-derives every frozen type; the stamps RE-MINTED
        — named and excluded from the equality surface), then the in-order
        re-casts through the door (the dedup index rebuilt BY the re-casts
        themselves; a doubled line absorbs loudly as the ack — the count
        unchanged, never double-counted).
NEW:
        then the reconstruction — a fresh door, register_run from the wire's
        arrays (the door re-derives every frozen type; the stamps RE-MINTED
        — named and excluded from the equality surface), the minted
        RunManifest CAPTURED (the container's own holding — the manifest
        accessor's return), then the in-order re-casts through the door
        (the dedup index rebuilt BY the re-casts themselves; a doubled line
        absorbs loudly as the ack — the count unchanged, never
        double-counted).
```

**1f. The l.690 discard — REPLACE (today's underscored form, named):**
```
OLD:         _new_run_id, _manifest, _count = session.register_run(manifest_items, operator, quorum_value)
NEW:         _new_run_id, manifest, _count = session.register_run(manifest_items, operator, quorum_value)
```

**1g. load's return — REPLACE l.706 (the new return path):**
```
OLD:         return cls(session, manifest_run_id, run_file)
NEW:         return cls(session, manifest_run_id, run_file, manifest)
```

**1h. THE ACCESSOR — INSERT after l.866 (rank's close), before l.868 (the @property line), one blank line each side:**
```python
    def manifest(self) -> RunManifest:
        """Manifest the run's frozen ground — the container's own held record, whole.

        Purpose: return the run's RunManifest VERBATIM — the container's own
        holding (minted at register_run, captured at BOTH factories: register's
        own mint, load's reconstruction — the clock-free fields re-derived
        identically at every load, the stamp named and excluded from any
        equality claim). The sixth query's store-tier read: the face route's
        five-key body builds from this whole, the elisions (the operator id,
        the registration stamp) riding at the FACE alone — the store tier
        returns the frozen whole, never projecting.
        Refuses when: never — the record IS the container's own holding (the
        pre-pass already refused the corrupt file whole at load; this read
        adds no refusal of its own).
        Re-run: deterministic given the store state — the clock-free surface
        re-derives identically at every load (the round-trip property held).
        Touches: nothing — a read of the container's own holding.
        Provenance: the service unit brief §1-§2 (the sixth query's
        store-tier accessor), the ux design §2 (the mechanism named),
        run-store-brief §1 (the verb tail), the naming law ("Manifest the
        run's frozen ground" — the act's first word), G-RUN-STORE.
        """
        return self._manifest
```
THE RETURN PATH, named whole: today's `_manifest` (l.690, underscore-discarded) → un-underscored `manifest` → carried into the container at l.706 (cls(session, manifest_run_id, run_file, manifest)) → held as self._manifest (1c) → returned by this accessor. A METHOD (the verb tail's read form — serve/census/rank the precedent; the run_id property stays the container's own name, not a door value).

### Region 2 — src/prioritree/service_store.py (209 l. at HEAD)

**2a. The TYPE_CHECKING import — REPLACE l.33:**
```
OLD:     from prioritree.registry import ItemRow, OperatorDeclaration
NEW:     from prioritree.registry import ItemRow, OperatorDeclaration, RunManifest
```

**2b. Serialize.manifest — APPEND after l.209 (the file's last line, rank's return; one blank line before):**
```python

    def manifest(self, run_id: str) -> RunManifest:
        """Manifest the run's frozen ground under the lock — the load and the read in one acquire.

        Purpose: serialize the manifest act — load the run file INSIDE the
        lock, delegate to the container's manifest accessor, return the frozen
        RunManifest WHOLE VERBATIM. The read locks too: a manifest read
        concurrent with a cast would catch the mid-append tail and fire the
        crash-tail refusal spuriously on a healthy run — inside the lock the
        read never sees a half-state. The load is the FULL pre-pass (every
        public verb rides it — a manifest read prices the file's WHOLE
        integrity: a corrupt vote line refuses it as StoreRefusedError).
        Refuses when: never its own refusal — the store's own
        (StoreRefusedError) rides through verbatim BY TYPE; no value refusal
        exists at this read (the manifest line already validated at load's
        pre-pass).
        Re-run: deterministic given the store state (the clock-free surface
        re-derives identically at every load).
        Touches: only the run file (a read) — through Persist only.
        Provenance: the service unit brief §1-§2 (the sixth query's seam
        verb — ONE lock acquisition), the ux design §2 (the mechanism named),
        Q-service-concurrency (the read-locks-too law), G-SERVICE-STORE.
        """
        with self._lock:
            return Persist.load(self._store_home, run_id).manifest()
```

### Region 3 — src/prioritree/service.py (393 l. at HEAD)

**3a. The module docstring head — REPLACE l.2-24 whole** (the docstring's own claims amended: the six routes named, the 400 clause's old defense retired, the 404/405 framework cure named; l.25 onward byte-untouched):
```
NEW:
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
— no Depends, no default-argument calls, B008 never fires by construction.
THE STATUS MAPPING (Q-service-routes + the ux build's ThreePart cures): 200
success AND DONE (the exhausted queue a STATE, never an error — the signal's
three fields + the done marker, the tally pointer already in next_action);
201 register's alone; 404 StoreRefusedError's both families (the unknown run
AND the corrupt file — the honest label, the found field carrying the
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
```

**3b. The import — INSERT after l.50 (from pydantic import BaseModel), before the blank line:**
```python
from starlette.exceptions import StarletteHTTPException
```
(the third-party block's alphabetical order held: fastapi < pydantic < starlette — I001 never fires.)

**3c. The body-key constants — REPLACE l.72-76 (the manifest's three new keys grouped after ITEMS; DETAIL RETIRES — its only uses were the old handler body l.195 and its docstring l.182, both replaced at 3e):**
```python
ITEMS: Final[str] = "items"
QUESTION: Final[str] = "question"
VERDICTS: Final[str] = "verdicts"
QUORUM: Final[str] = "quorum"
EXPECTED: Final[str] = "expected"
FOUND: Final[str] = "found"
NEXT_ACTION: Final[str] = "next_action"
```

**3d. The path constant — INSERT after l.88 (_STATE_PATH).** THE HOME SETTLED (the brief's §7(c) answered): the l.85-88 block is THE home — its own comment names "the REST resource hierarchy named once"; the sixth belongs to the hierarchy; the mid-file _TALLY_PATH at l.224 is the tally unit's insertion-seam artifact, not a second constants home:
```python
_MANIFEST_PATH: Final[str] = "/runs/{run_id}/manifest"
```

**3e. The re-badge handler — REPLACE l.174-195 whole** (§2 below carries the bytes).

**3f. The framework-refusal constants + the refuse handler + _ROUTE_TABLE — INSERT between l.223 (fold's closing paren) and l.224 (_TALLY_PATH), plus immediately after l.224** (§3 below carries the bytes).

**3g. THE SIXTH ROUTE — APPEND after l.393 (the file's tail, after rank; two blank lines before):**
```python


@app.get(_MANIFEST_PATH)
def describe(request: Request, run_id: str) -> JSONResponse:
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
```
The naming law: "Describe the run's frozen ground over the seam" → describe (the route family's verb form; no shadowing — the RunManifest local rides as manifest). FIVE keys in the brief's §2 order; operator.id + registered_at never on the wire.

## §2 THE 400 CURE, WHOLE (the re-badge handler's new body — service.py l.174-195 replaced)

THE CONSTRUCTION SETTLED (the brief's §7(a) answered): the source identified by the REQUEST'S PATH (loc alone cannot — register and cast are both "body"); found renders each error's loc + msg AS CARRIED, "; "-joined (never json.dumps — the pydantic input/url payloads are not the wire's vocabulary; never re-derived); expected names the failing route's own legal form; next_action names the cure. The strings, byte-set:

```python
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
```
THE BRANCH IS TOTAL: RequestValidationError fires only at register (POST /runs), serve's seed (GET .../next), cast (POST .../votes) — census/rank/manifest/state declare no body/query models and their run_id: str path param never fails validation; unmatched paths 404/405 before any validation door. The parameter renames _request → request (now used — ARG001 never fires). THE OLD DEFENSE LINE'S REPLACEMENT (the ask's clause): the old l.181-184 defense — "the body carrying the native detail grammar ({DETAIL: exc.errors()}) — loc/msg/type, the client's own fix map, machine-readable; the three-field form is the door's VALUE-refusal grammar — fabricating expected/found/next_action for a schema violation would dress the wrong family" — is answered by the Purpose's amendment clause above, verbatim in the fence.

## §3 THE 404/405 CURE, WHOLE (the StarletteHTTPException handler — inserted after the fold handler)

SETTLED (the brief's §7(b) answered): ONE app-level handler with 404/405-specific found construction and a general fallback (found = the framework's own detail, as carried); next_action = the route table (the legal route/method set — "enumerated or summarized" answered: ENUMERATED from the path constants, content-in-configuration); the STATUSES ride exc.status_code verbatim — FROZEN (machine-dispatchable; the acceptance harness's 404-as-ready probe rides the status, untouched); the registration rides the same @app.exception_handler surface (dispatch BY TYPE — order irrelevant; the typed refusals never reach it: the routes catch them first, DONE is a 200 VALUE).

**INSERT between l.223 (fold's closing paren) and l.224 (_TALLY_PATH...) — two blank lines after fold's close; the handler's close abuts _TALLY_PATH with ZERO blank lines (HEAD's own def→assignment pattern at l.223-224, held byte-for-byte in form):**
```python


# The framework-refusal statuses (named per the zero-magic-value-in-src
# discipline — the handler branches on them; the codes FROZEN: the cure flips
# BODIES only, never the machine-dispatchable statuses).
_NOT_FOUND: Final[int] = 404
_METHOD_NOT_ALLOWED: Final[int] = 405


@app.exception_handler(StarletteHTTPException)
def refuse(request: Request, exc: StarletteHTTPException) -> JSONResponse:
    """Refuse the framework's bare HTTP exceptions in the family grammar — 404/405 taught.

    Purpose: R5's census cure ×2 — the framework's routing refusals ride bare
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
```
The naming law: "Refuse the framework's bare HTTP exceptions in the family grammar" → refuse. THE STATUS CONSTANTS dodge PLR2004 (ruff ALL flags literal comparisons in src; the routes' status_code=404 kwargs are call arguments — untouched, never flagged; the handler's == branches needed the named constants).

**INSERT immediately after l.224 (_TALLY_PATH...) — no blank line before the comment (one constants region); the existing two blanks before register (l.225-226) held:**
```python

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
```
(Placed after _TALLY_PATH — its f-strings cite the mid-file constant; the handler cites _ROUTE_TABLE at REQUEST time, so definition order is safe. Explicit + over a join CALL result — never literal+literal: ISC003 and pyright's reportImplicitStringConcatenation both held.)

PART 1's event ends here — PART 2 completes the spec: §4 the test arcs whole, §5 the command sequence, §6 the no-break proofs. — togo, 2026-11-22
## Reported by togo — 2026-11-22T12:19:14Z

# THE SERVICE UNIT'S EXACT-TASK SPEC — PART 2 (synthesize/probe; togo, 2026-11-22 — this event completes the spec: §4 the test arcs, §5 the command sequence, §6 the no-break proofs; part 1 carried §§0-3, the whole build's code bytes)

## §4 THE TEST ARCS, WHOLE (every new/modified test, fenced)

### tests/test_service_face.py (265 l. at HEAD → 16 test functions after: 12 standing + 4 new; 1 flips)

**4a. The module docstring — REPLACE l.2-17 whole:**
```
NEW:
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
```

**4b. test_manifest_200 — INSERT after l.139 (test_tally_success's closing brace), before the "Region 2's near-use vocabulary" comment (l.142); two blank lines each side:**
```python
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
```
(The exact-dict body-equality pattern — the five keys asserted exact; the verdicts the sorted triple; the items payload-order-preserved; the elisions pinned by the key set — any operator/registered_at key would fail the equality.)

**4c. test_refusal_manifest_unknown_run — INSERT after l.159 (test_refusal_unknown_run's close), before test_refusal_out_of_set_verdict (l.162); two blank lines each side:**
```python
def test_refusal_manifest_unknown_run(client: TestClient) -> None:
    """GET manifest on an unregistered run => 404, the three fields, the stem in found."""
    response = client.get("/runs/RUN-9999/manifest")
    assert response.status_code == 404
    body = response.json()
    assert set(body) == _REFUSAL_KEYS
    assert "RUN-9999" in body["found"]
```
(_REFUSAL_KEYS is defined at l.149 — AFTER this insertion's def site; function bodies resolve names at CALL time, the acceptance file's own precedent at its l.324/l.417.)

**4d. THE 400 FLIP — REPLACE l.199-206 (test_rebadge_malformed_body_400) whole; the new assertions verbatim:**
```python
def test_rebadge_malformed_body_400(client: TestClient) -> None:
    """A register body with mistyped items => 400, the family grammar, the violation taught."""
    response = client.post(_RUNS, json={"items": "not-a-list", **_OPERATOR})
    assert response.status_code == 400
    body = response.json()
    assert set(body) == _REFUSAL_KEYS
    assert "items" in body["expected"]
    assert "body.items" in body["found"]
    assert "re-send" in body["next_action"]
```
(The old native-grammar assertions — "detail" in body, isinstance(body["detail"], list), body["detail"] — are REPLACED by the family set + three substring pins, each a substring of §2's authored bytes: "items" of the register expected, "body.items" of the loc render, "re-send" of the cure. The pins ride OUR rendering only — never pydantic's message text — version-stable.)

**4e. test_rebadge_door_refusal_422 — STANDS byte-untouched (l.209-222): the two grammars still never conflated, now BOTH family-shaped with distinct statuses.**

**4f. THE FRAMEWORK ARCS — INSERT after l.222 (test_rebadge_door_refusal_422's close), before test_done_200 (l.225); two blank lines each side:**
```python
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
    """A disallowed method at a legal path => 405, the family grammar, the method taught."""
    response = client.delete("/runs")
    assert response.status_code == 405
    body = response.json()
    assert set(body) == _REFUSAL_KEYS
    assert body["expected"] == "DELETE /runs"
    assert body["found"] == "the method DELETE is not allowed at the path /runs"
    assert "POST /runs" in body["next_action"]
```
(Exact pins — deterministic: expected is the refuse handler's _address form; found is §3's authored string verbatim; next_action carries the route table, whose first lane is POST /runs — the legal method AT the addressed path taught.)

### tests/test_service_acceptance.py (417 l. at HEAD → 4 test functions, one renamed; the arc grows the EIGHTH request)

**4g. The module docstring — REPLACE l.4-12:**
```
OLD:
The service-acceptance unit's test surface (service-acceptance-brief §1-§7):
six arcs over a live uvicorn subprocess — the seven-request arc (register
=> next => vote x3 => the exhausted turn => tally, each body asserted
against the named-constant literals); the determinism replay (two fresh
homes, byte-identical [r.content] lists); the four refusal arcs (404 the
unknown run, 422 the bogus winner, 409 the SAFE HALT, 400 the malformed
items); the concurrency arc (N=2 threads x M=2 casts through the seam's
NEW:
The service-acceptance unit's test surface (service-acceptance-brief §1-§7 +
the ux build's sixth query + ThreePart cures): six arcs over a live uvicorn
subprocess — the eight-request arc (register => manifest => next => vote x3
=> the exhausted turn => tally, each body asserted against the
named-constant literals); the determinism replay (two fresh homes,
byte-identical [r.content] lists); the four refusal arcs (404 the unknown
run, 422 the bogus winner, 409 the SAFE HALT, 400 the malformed items —
the family grammar taught, the violation named in found); the concurrency
arc (N=2 threads x M=2 casts through the seam's
```

**4h. _drive_arc — REPLACE l.174-198 whole (the manifest GET slots SECOND, after register — the brief §5's recommendation: the fresh run's manifest served over the live seam early in the lifecycle; both the arc test and the replay ride the growth):**
```python
def _drive_arc(client: httpx.Client, base_url: str) -> list[httpx.Response]:
    """Drive the eight-request arc and return the responses in arc order.

    Purpose: the arc shared by the assertion test and the replay test —
    register (POST /runs, _ITEMS + _OPERATOR), the manifest read (GET
    .../manifest — the sixth query over the live seam, the lock + the full
    load under the real process), next (GET .../next), vote x3 over the
    three pairs (a,b)/(a,c)/(b,c), each body the _VOTE_BODY form with the
    pair swapped, the exhausted next turn, and tally; return the responses
    whole — the parsed-body assertions are the CALLER's own (test 1 asserts
    .json(), test 2 compares the .content byte lists).
    Refuses when: never — a driver (the responses returned unasserted; the
    caller owns the judgment).
    Re-run: deterministic — the arc's bodies carry no timestamps (the census
    elides the vote_log; the manifest body elides the registration stamp),
    the fresh home's stems identical.
    Touches: the socket only; the home's store via the service.
    Provenance: service-acceptance-brief §3-§4 (the arc, the replay), the
    dispatch synthesize/service-acceptance-bytes (region 2), the ux build's
    sixth query (the manifest leg — the service unit brief §5).
    """
    responses: list[httpx.Response] = []
    responses.append(client.post(f"{base_url}/runs", json={"items": _ITEMS, **_OPERATOR}))
    responses.append(client.get(f"{base_url}/runs/{_RUN_ID}/manifest"))
    responses.append(client.get(f"{base_url}/runs/{_RUN_ID}/next"))
    for pair in (("a", "b"), ("a", "c"), ("b", "c")):
        responses.extend([client.post(f"{base_url}/runs/{_RUN_ID}/votes", json={**_VOTE_BODY, "pair": list(pair)})])
    responses.append(client.get(f"{base_url}/runs/{_RUN_ID}/next"))
    responses.append(client.get(f"{base_url}/runs/{_RUN_ID}/tally"))
    return responses
```

**4i. THE ARC TEST — REPLACE l.201-245 whole (the final name settled: the arc's count now eight — test_accept_the_eight_request_arc; the success literals BYTE-UNCHANGED, re-indexed for the manifest's second slot):**
```python
def test_accept_the_eight_request_arc(service: tuple[httpx.Client, str]) -> None:
    """Register => manifest => next => vote x3 => the exhausted turn => tally, each body asserted.

    Purpose: the full eight-request arc over the real socket — register
    201 {"run_id": _RUN_ID}; the manifest read 200 the five-key body (the
    stem echoed, the question, the verdicts sorted, the quorum, the items
    payload-order-preserved — the operator id and the stamp elided); next
    200 the first pair with count 0; the three votes 200 with the acks
    {"vote_id": "VOTE-000N", "count": N, "acknowledged": False} (the wire's
    count the run's census count 1..3, the running total); the exhausted
    next 200 the DONE body (done is True, "tally" in next_action — DONE a
    state, never an error); tally 200 the frozen whole, the exact literal
    the face tests assert.
    Refuses when: any step's status or body diverges — each response's
    status and .json() asserted against the named-constant literals
    (content-in-configuration).
    Re-run: deterministic — the fresh home's stems and the census's frozen
    whole carry no timestamps across the wire.
    Touches: the socket; the home's store via the service.
    Provenance: service-acceptance-brief §3 (the arc), the dispatch
    synthesize/service-acceptance-bytes (region 2), the ux build's sixth
    query (the manifest leg — the service unit brief §5).
    """
    client, base_url = service
    responses = _drive_arc(client, base_url)
    assert len(responses) == 8  # the arc's own shape: 1 register, 1 manifest, 1 next, 3 votes, 1 done, 1 tally
    assert [response.status_code for response in responses] == [201, 200, 200, 200, 200, 200, 200, 200]
    bodies = [response.json() for response in responses]
    assert bodies[0] == {"run_id": _RUN_ID}
    assert bodies[1] == {
        "run_id": _RUN_ID,
        "question": "Which matters more?",
        "verdicts": ["prefer-a", "prefer-b", "tie"],
        "quorum": 1,
        "items": [["a", "one"], ["b", "two"], ["c", "three"]],
    }
    assert bodies[2] == {"item_a": "a", "item_b": "b", "count": 0}
    assert bodies[3] == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}
    assert bodies[4] == {"vote_id": "VOTE-0002", "count": 2, "acknowledged": False}
    assert bodies[5] == {"vote_id": "VOTE-0003", "count": 3, "acknowledged": False}
    done = bodies[6]
    assert done["done"] is True
    assert "tally" in done["next_action"]
    assert bodies[7] == {
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
```

**4j. test_replay_byte_identical — docstring ONLY, REPLACE l.253-259 (the body l.260-291 byte-untouched; _drive_arc carries the growth to both homes):**
```
OLD:
    Purpose: the determinism replay — two homes (tmp_path/"one",
    tmp_path/"two"), a boot at each, the same seven-request arc against
    each via _drive_arc; assert the .content byte lists equal — THE BYTES,
    not parsed dicts; byte-identity IS the claim (no recorded_at crosses
    the wire: the register body the stem alone, the acks the triple, the
    tally the frozen whole). The teardown the test's own finally (the
    fixture manages one boot; the replay manages its pair).
NEW:
    Purpose: the determinism replay — two homes (tmp_path/"one",
    tmp_path/"two"), a boot at each, the same eight-request arc against
    each via _drive_arc; assert the .content byte lists equal — THE BYTES,
    not parsed dicts; byte-identity IS the claim (no recorded_at crosses
    the wire: the register body the stem alone, the manifest the five
    clock-free keys, the acks the triple, the tally the frozen whole).
    The teardown the test's own finally (the fixture manages one boot; the
    replay manages its pair).
```

**4k. test_refuse_the_four_arcs — REPLACE l.307-309 (the docstring's 400 clause):**
```
OLD:
    swallowed); 400 POST /runs with items "not-a-list" with the
    {"detail": [...]} array present (the native grammar re-badged — 422
    exclusively the door's value refusals).
NEW:
    swallowed); 400 POST /runs with items "not-a-list" with the family
    grammar, the violation taught in found (the re-badge cured — 422
    exclusively the door's value refusals).
```

**4l. THE 400 ARC'S FLIP — REPLACE l.340-345:**
```
OLD:
    # 400 — the malformed items (the native detail grammar re-badged).
    response = client.post(f"{base_url}/runs", json={"items": "not-a-list", **_OPERATOR})
    assert response.status_code == 400
    detail = response.json()["detail"]
    assert isinstance(detail, list)
    assert detail
NEW:
    # 400 — the malformed items (the family grammar taught; 422 the door's alone).
    response = client.post(f"{base_url}/runs", json={"items": "not-a-list", **_OPERATOR})
    assert response.status_code == 400
    body = response.json()
    assert set(body) == _REFUSAL_KEYS
    assert "items" in body["expected"]
    assert "body.items" in body["found"]
```
(The 404/422/409 arcs l.320-339 and the concurrency arc + the Persist.load oracle l.348-417: BYTE-UNTOUCHED — the frozen surfaces' pins.)

## §5 THE COMMAND SEQUENCE (jikko's exact order — one increment, one commit)

THE EDITS, PER FILE, IN ORDER (the patch verb per region; the region ids cite §§1-4):
1. src/prioritree/run_store.py — regions 1a, 1b, 1c, 1d, 1e, 1f, 1g, 1h. READ-BACK: the file shows `ItemRow, RunManifest` at the TYPE_CHECKING import; `__init__` with the fourth parameter and `self._manifest = manifest`; l.555's `cls(session, run_id, run_file, manifest)`; l.690's `_new_run_id, manifest, _count = ...`; l.706's `cls(session, manifest_run_id, run_file, manifest)`; `def manifest(self) -> RunManifest:` between rank and the run_id property, closing `return self._manifest`.
2. src/prioritree/service_store.py — regions 2a, 2b. READ-BACK: `ItemRow, OperatorDeclaration, RunManifest` at l.33; `def manifest(self, run_id: str) -> RunManifest:` at the file's tail after rank, its body `with self._lock:` / `return Persist.load(self._store_home, run_id).manifest()`.
3. src/prioritree/service.py — regions 3a-3g (in file order: 3a the docstring, 3b the import, 3c the body keys, 3d the path constant, 3e the rebadge, 3f the refuse constants/handler/table, 3g the describe route at the tail). READ-BACK: the starlette import after pydantic; QUESTION/VERDICTS/QUORUM present and DETAIL ABSENT; `_MANIFEST_PATH` at the l.85-89 block; `def rebadge(request: Request, ...)` (the param un-underscored); `_NOT_FOUND`/`_METHOD_NOT_ALLOWED` + `def refuse(...)` + `_ROUTE_TABLE` between fold and register; `@app.get(_MANIFEST_PATH)` / `def describe(...)` at the file's tail.
4. tests/test_service_face.py — regions 4a-4f. READ-BACK: the four new test defs present (`test_manifest_200`, `test_refusal_manifest_unknown_run`, `test_refusal_unmatched_path_404`, `test_refusal_method_not_allowed_405`); test_rebadge_malformed_body_400's assertions are the family set + three substring pins; the five success tests and the door-refusal-422 test byte-untouched.
5. tests/test_service_acceptance.py — regions 4g-4l. READ-BACK: `_drive_arc` appends the manifest GET second; `def test_accept_the_eight_request_arc(` (the seven-request name GONE); the replay's docstring says eight; the four-arcs 400 section carries the family grammar.

THE FLOOR, once, AFTER all five files land (the suite is only green at the whole — the face tests reference the cured handler mid-sequence):
- `make dev` — expected: uv sync resolves the lock (no dependency changes: pyproject byte-untouched).
- `make test` — expected: the suite GREEN, 0 failed, 0 errors (115 test functions after the build: the census's 111 + 4 new face arcs; parametrized expansions aside, every node passes), among them byte-named: tests/test_service_face.py::test_manifest_200, ::test_refusal_manifest_unknown_run, ::test_refusal_unmatched_path_404, ::test_refusal_method_not_allowed_405, ::test_rebadge_malformed_body_400 (flipped, passing), and tests/test_service_acceptance.py::test_accept_the_eight_request_arc (renamed, passing), ::test_replay_byte_identical, ::test_refuse_the_four_arcs, ::test_interleave_the_concurrency_arc.
- `make lint` — expected: `All checks passed!` (ruff check src/ tests/, zero findings; the standing per-file rulings suffice — NOTHING added to pyproject).
- `make typecheck` — expected: pyright strict `0 errors, 0 warnings` over src + tests.

THE COMMIT, ONE, after the floor green (the route's one-commit-per-increment law; kensho's independent re-run is G-SERVICE's verification leg, never jikko's own claim) — the shape per the tree's precedent ("prioritree-service: the service-face increment lands — U2 green, the wire seam live, the tree's first runtime deps"):
```
prioritree-ux: the probe increment lands — G-SERVICE green, the sixth query live, the error surface 21/21 ThreePart
```
Scope: the five files above (src/prioritree/run_store.py, service_store.py, service.py; tests/test_service_face.py, test_service_acceptance.py) — nothing else (the .plans records ride the store's own commits).

## §6 THE NO-BREAK PROOFS

**(1) THE FIVE SUCCESS BODIES BYTE-STABLE.** The build touches ZERO bytes of the five routes' success constructs (service.py l.253, l.281-283, l.319-320, l.346-347, l.387-393 — unedited; the manifest route is a pure append, the cures touch only handler bodies and docstring prose). The pins that already hold them, untouched by the build: tests/test_service_face.py::test_register_success (l.64-68), ::test_serve_success (l.71-76), ::test_vote_success (l.79-92), ::test_state_success (l.95-109), ::test_tally_success (l.112-139) — each an exact-dict body equality; and the acceptance arc's literals (register bodies[0], next bodies[2], votes bodies[3-5], done bodies[6], tally bodies[7]) — the SAME literals as today's bodies[0-6], re-indexed only for the manifest's second slot. DONE (a 200 VALUE) and the idempotent ack stand untouched (R5's carve-out); the typed-refusal catch tables and render_refusal (l.156-171) stand byte-untouched.

**(2) THE REPLAY-BYTES ARC UNBROKEN — why the cures cannot touch it.** test_replay_byte_identical compares [r.content] lists of the arc driven on two fresh homes: (a) every arc response is a SUCCESS (201/200) — the cured surfaces (400/404/405 handlers) never fire on the arc; (b) the eighth response (the manifest read) is byte-deterministic — five clock-free keys, registered_at elided at the route, identical stems/items/operator across fresh homes; (c) the 404-as-ready probe rides the ROUTE-LEVEL StoreRefusedError 404 (a return, never an exception — the refuse handler never sees it) and asserts the STATUS, which the refuse handler preserves verbatim (exc.status_code); (d) the concurrency arc + the Persist.load file oracle compose through the factories — the constructor's fourth part is captured inside register/load, invisible to the oracle's callers.

**(3) THE RUFF/PYRIGHT RULINGS THE NEW CODE HONORS (its own compliance, named).** service.py BLE001 — the fold's except Exception alone; the refuse handler catches StarletteHTTPException (TYPED, never blind — BLE001 cannot fire); the rebadge catches nothing. service_store.py PLR0913/PLR0917 — the seven-argument cast ruling; Serialize.manifest takes one argument — no firing. run_store.py PLR0913/PLR0917 — cast's ruling; __init__ carries four parameters (under the threshold). ruff ALL on the NEW code: PLR2004 dodged by _NOT_FOUND/_METHOD_NOT_ALLOWED (the branches never compare bare literals); no implicit string concatenation anywhere (pyproject's pyright error honored by construction — the long strings build via the _fields + f-string idiom, _ROUTE_TABLE via explicit + over a join call); E501 held (every new line ≤120 — verified at authorship); TC001/TC003 (RunManifest rides the TYPE_CHECKING blocks in both store files — annotation-only, future-annotations); ANN complete; five-field docstrings on every new public symbol (manifest ×2, refuse, describe); D401 imperative; RET504 never (branch locals feed dict constructions, the fold's own pattern); no raises (EM/TRY families dark); S104 never (no uvicorn.run); the naming law checked on every new symbol (Manifest/Refuse/Describe — the act-statements' first words; the tests carry the file's own subject+outcome convention, the brief §5's names). pyright strict: the cast keeps app.state.seam honest; RunManifest flows typed end-to-end; __init__ fully initializes (reportUninitializedInstanceVariable); errors()' ErrorDetails accessed by required keys only; exc.status_code/exc.detail typed by Starlette.

**THE GATE THIS SPEC CLOSES (G-PROBE-BRIEF's conditions, answered):** (1) THE BUILD BRIEF LANDED — this exact-task spec, the synthesis over the unit's whole discovery ground (discover/service + understand/service + the approved unit brief + the approved design), carrying the banked shapes as BYTES: the scope fence (§0's price named; the five files the whole write surface; zero core edits — registry/scheduler/votes/tally/session untouched; the five-op interface stands), the sixth query's code (§1), the cures' code (§§2-3), the test arcs (§4), the command sequence (§5), the no-break proofs (§6) — the dispatches cite this brief; (2) THE COLLABORATOR'S APPROVAL — the gate is the validation; jikko's build dispatch fires only after. FR-MEM-0011's doctrine held at this seat: every edit fenced-bytes-exact, every command exact, every expected outcome named — nothing to figure out at the execution seat.

THE SPEC CLOSES: the bytes whole, the five open questions (a)-(e) answered at their exact homes, the frozen surfaces pinned, the floor's expectations byte-named. — togo, 2026-11-22
