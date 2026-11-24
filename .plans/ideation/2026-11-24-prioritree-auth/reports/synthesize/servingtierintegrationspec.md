<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/servingtierintegrationspec

**Route:** prioritree-auth (executing) | **Events:** 3 | **Reports:** 2

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-24T21:31:29Z |
| 2 | report | togo | 2026-11-24T21:41:56Z |
| 3 | report | togo | 2026-11-24T21:42:31Z |
## Reported by togo — 2026-11-24T21:41:56Z

# THE SERVING-TIER-INTEGRATION EXACT-TASK SPEC — togo (synthesize/servingtierintegrationspec, 2026-11-24)

## 0. THE GROUND READ WHOLE (every file cited)

The approved unit brief (reports/synthesize/serving-tier-integration.md — the eight landings, §2's flag rulings, §3's mechanisms, §4's arcs, §6's opens); tansa's census (reports/discover/serving-tier-integration.md — service.py whole [:353-:560 the six routes, :200-:215 render_refusal, :296-:297 the constants stopping at 404/405, :179-:197 the construction with _boot_keys discarded, :337-:350 the route table]; web.py whole [:156 the child, :160-:167 the one _client, :92-:97 the constants stopping at 409/500, :547/:644 the plain-form POSTs, every non-200 non-404 folding]; votes.py stage 5 :434-:454 the author never consulted; run_store.py :92-:93 the em-dash precedent; key_store.py/key_verify.py/policy.py public seams; the tests' shape; the zero-Depends precedent; pyproject :187 reportCallInDefaultInitializer; the units 1-2 flags pinned); rikai's maps (reports/understand/serving-tier-integration.md — the dependency's chain, the dispatch mechanics [the fold re-badges 500 — the dedicated handler the load-bearing seam], the CSRF's three render contexts + the priced alternatives, the web lane's absence, the supersedes placements, F5/F8, F6's fence forms); auth-design.md (the blocking rulings F2/F4/F5/F6/F8, §1 the web tier's ruled form, §2 the resolutions, §3 the honest statement); the tree read direct: service.py (572), web.py (692), votes.py (532), key_store.py (600), key_verify.py (208), policy.py (89), cli.py (:1-20, :399-439, :486), mcp_server.py (:290-:449), run_store.py (:62-:93), service_store.py (:149-:178), Makefile (:7, :33, :82), pyproject.toml whole, web/templates (landing/pair/sitting/refuse), tests (test_service_face.py :48-:65 the injection fixture, test_web_face.py :45-:49, test_key_verify.py :66-:86 the _minted_store + _assert_same_401, test_key_mint.py :105 the pinned "refused --" byte, test_service_store.py :241-:245 the source-scan fence, test_session.py :45, test_run_store.py :47, test_harness.py :8/:82/:103, test_service_acceptance.py :6/:182/:215/:221, test_cli.py :69); the sibling specs' house form (keyinfrastructurespec.md, policylayerspec.md — the fenced-before/after grammar, the named-ruling family, the floor arithmetic).

## 1. service.py — THE DEPENDENCY REGION WHOLE (every byte fenced)

### (a) The imports grown
`from fastapi import Depends, FastAPI, Request` (Depends joins); `from typing import Annotated, Final, cast` (Annotated joins); the key_store line grows KeyRecord: `from prioritree.key_store import KeyRecord, KeyStore, render_boot_marker, resolve_auth_mode, resolve_keys_home`; NEW line: `from prioritree.key_verify import AUTH_HEADER_DEFAULT, KeyScopeError, KeyVerifyError, verify`.

### (b) The new constants (after :97 NEXT_ACTION)
```python
_UNAUTHORIZED: Final[int] = 401
_FORBIDDEN: Final[int] = 403
_SERVICE_AUDIENCE: Final[str] = "service"
_AUTH_OFF: Final[str] = "off"
```
(Cited values, never re-derived: "service" rides AUDIENCES' member, "off" rides resolve_auth_mode's own literal — key_store's _AUTH_MODE_OFF is private; the literals pinned by the module docstring, the fork caught by the arcs.)

### (c) The factory + the anonymous record + the six aliases
```python
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
```
THE B008/PYRIGHT DISCIPLINE: the Depends call rides the TYPE annotation, never a default argument — B008 never fires by construction and pyright's reportCallInDefaultInitializer is dodged by the same act (the two checkers' law one dodge). `Callable` joins the typing import.

### (d) The six signatures, exact before/after (the door parameter LAST, the body's fields unchanged)
- `def register(request: Request, body: RegisterRunRequest) -> JSONResponse:` → `def register(request: Request, body: RegisterRunRequest, record: _RegisterDoor) -> JSONResponse:`
- `def serve(request: Request, run_id: str, seed: int | None = None) -> JSONResponse:` → `def serve(request: Request, run_id: str, seed: int | None = None, record: _NextDoor) -> JSONResponse:` — PYRIGHT LAW: a parameter after a defaulted one is a syntax error; serve's ruled form: the seed default RETAINS its place and the door rides before it: `def serve(request: Request, run_id: str, record: _NextDoor, seed: int | None = None) -> JSONResponse:` (FastAPI resolves the Annotated dep regardless of position; the wire's query grammar unchanged).
- `def cast_vote(request: Request, run_id: str, body: CastVoteRequest) -> JSONResponse:` → `def cast_vote(request: Request, run_id: str, body: CastVoteRequest, record: _CastDoor) -> JSONResponse:`
- `def census(request: Request, run_id: str) -> JSONResponse:` → `... , record: _StateDoor) -> JSONResponse:`
- `def rank(request: Request, run_id: str) -> JSONResponse:` → `... , record: _TallyDoor) -> JSONResponse:`
- `def describe(request: Request, run_id: str) -> JSONResponse:` → `... , record: _ManifestDoor) -> JSONResponse:`
THE GRANT MAP 1:1 (the tokens per the ask): register→register, serve→next, cast_vote→cast, census→state, rank→tally, describe→manifest. THE ARG001 RULING (the five non-cast doors' parameter unread at the route): the door IS the gate's own act — the 401/403 raised in the dependency; the parameter consumed at the cast route alone; the pyproject entry `"src/prioritree/service.py" = ["BLE001", "E402", "PLC0415", "ARG001"]` with the named-ruling comment per the family form (the ignore IS the ruling, named).

### (e) render_refusal's union widened — exact before/after
BEFORE (:201): `refusal: StoreRefusedError | VotesRefusedError | TallyRefusedError,`
AFTER: `refusal: StoreRefusedError | VotesRefusedError | TallyRefusedError | KeyVerifyError | KeyScopeError,`
(The body's three-key return byte-standing — the families are shape-identical; the docstring's one-render-point claim grows "the key family" in prose.)

### (f) THE TWO DEDICATED APP-LEVEL HANDLERS (after the refuse handler, before _TALLY_PATH; the 500-rebadge dodged — Starlette dispatches registered handlers BY CLASS, dependencies included)
```python
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
```
(Two handlers, not a shared ancestor — the shared-base alternative priced and refused at the brief §3b: a new base class minted at the integration widens the foundation's type surface for zero behavior.)

### (g) THE STORE HELD ON APP.STATE — exact before/after
BEFORE (:194-:197): `_boot_keys = KeyStore(resolve_keys_home().absolute())` + the marker's `len(_boot_keys.records)`.
AFTER: `app.state.keys = KeyStore(resolve_keys_home().absolute())` — ONE line promoted (the marker's render line reads `len(app.state.keys.records)`, the marker's three states byte-standing); the module-local discarded forever; the verify seam's per-request reload_if_changed rides the container's own stat ride.

### (h) THE CAST ROUTE'S CLASS/ID STAMPING — exact before/after (:430-:440)
BEFORE:
```python
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
```
AFTER (the verified record's stamps in place of the body's self-claims; the wire schema unchanged — CastVoteRequest still parses them; the degrade's fallback keyed on the anonymous marker):
```python
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
```
The body's comparator_id/comparator_class become UNREAD at the route under auth-on (the self-claim dies at the cast door — F8); under auth-off the anonymous record's digest is "" → the claim stands (the degrade's price, the floor's input unverified again — named at the docstring: "under the degrade the body's claim stands — the boot marker names it").

### (i) THE SUPERSEDES 403 CATCH CLAUSE (the route's catch table grows one clause, after the VotesRefusedError clause; rides the votes.py dispatch per §9's order note)
`except SupersedeRefusedError as refusal: return JSONResponse(status_code=_FORBIDDEN, content=render_refusal(refusal))`

### (j) THE /DOCS TRIO STRIPPED (the child's :156 precedent carried up)
BEFORE (:179): `app = FastAPI()`
AFTER: `app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)` — the recon surface /openapi.json (every route + body schema, ungated) closed at both tiers; the price named honestly (the operator loses the browsable schema; the README's local remedy is unit 5's own).

### (k) The module docstring's no-Depends claim AMENDED (:12-13)
BEFORE: "— no Depends, no default-argument calls, B008 never fires by construction."
AFTER: "— the one Depends family the auth doors carry rides the TYPE annotation (Annotated), never a default argument: B008 never fires by construction and pyright's reportCallInDefaultInitializer is dodged by the same act."

## 2. votes.py — THE SUPERSEDES DOOR CHECK (F4; exact before/after)

### (a) The new typed error (after VotesRefusedError :134; votes.py's OWN lineage — the three-field grammar, the em dash per :134's own bytes; N818 Error-suffix)
```python
class SupersedeRefusedError(Exception):
    """SupersedeRefusedError — the author-refusal: expected, found, next_action.

    Purpose: carry the supersedes door check's refusal (a correction corrects
    the CALLER'S OWN vote — the author mismatch) as typed data; found ELIDES
    the target's author (the identity oracle never fed — the 401's
    "absent-or-unknown" discipline at the 403); the service route maps it to
    403 (the wire's authorization half).
    Provenance: the design's F4, the unit brief §1d/§3e, rikai map 4,
    G-SERVING-TIER-INTEGRATION-BRIEF.
    """

    def __init__(self, expected: str, found: str, next_action: str) -> None:
        """Initialize the refusal with its three named fields."""
        self.expected = expected
        self.found = found
        self.next_action = next_action
        super().__init__(f"refused — expected: {expected} | found: {found} | next: {next_action}")
```

### (b) The author check — stage 5, after the same-pair check (:454's region)
BEFORE (:446-:454):
```python
            if target.pair != canonical_pair:
                raise VotesRefusedError(
                    expected=(
                        "a live VOTE-{####} handle in the same run, on the same pair "
                        "(a correction corrects the same judgment)"
                    ),
                    found=f"{clean_supersedes!r} — a record on pair {target.pair!r}",
                    next_action="cite the record being corrected",
                )
```
AFTER (the author check appended inside the `if clean_supersedes is not None:` block, after the same-pair check — the placement ruled at the brief §3e: inside the lock by construction, no seam verb grown, no TOCTOU):
```python
            if target.comparator_id != clean_comparator_id:
                raise SupersedeRefusedError(
                    expected=(
                        "a correction of the caller's own vote — the superseder's "
                        "comparator_id matches the target's author"
                    ),
                    found=f"{clean_supersedes!r} — another author's vote (the author never named)",
                    next_action="cite your own vote on this pair, or cast a new vote without supersedes",
                )
```
THE ELISION PINNED: found never renders target.comparator_id — a prober casting supersedes against harvested handles learns nothing (the identity oracle starved); the arc pins the author's id ABSENT from the rendered three fields whole.

### (c) The auth-off note (named, never silent): the door check rides the CALLER's identity — the PASSED comparator_id. Under auth-off the service route passes the body's claim (§1h's fallback) — the claim form stands at the door, the §3 floor (the offline JSONL edit) the price every placement shares; the CLI/stdio tiers pass their self-claims at every mode (the local trust, the design's own residual).

## 3. web.py — THE /ui/ CURE (the CSRF region + the tier key + the web lane)

### (a) THE CSRF REGION — the module's new region (placed after _BASE_URL's constants block)
```python
# The CSRF token's stateless signed form (the unit brief §3c): the secret at
# the child's process (the env knob the configurability law — a multi-worker
# deployment sets ONE secret; unset => a boot-minted random secret, the
# restart-invalidation price carried: a boot's outstanding tokens die, the
# re-render mints fresh, the failure's ThreePart teaches the reload).
_CSRF_SECRET_ENV: Final[str] = "PRIORITYTREE_WEB_CSRF_SECRET"
_csrf_secret: Final[bytes] = (
    os.environ.get(_CSRF_SECRET_ENV, "").encode() or secrets.token_urlsafe(32).encode()
)
_CSRF_FIELD: Final[str] = "csrf_token"


class CsrfRefusedError(Exception):
    """CsrfRefusedError — the drive-by's death: expected, found, next_action.

    Purpose: carry the CSRF refusal's three fields as typed data for the
    child's DEDICATED handler (never the child's fold — the crash page's
    clothes never worn); found "absent-or-mismatched" the elision discipline
    (the remote page could not have READ the served form — which leg fired
    teaches nothing).
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


async def _csrf_guard(request: Request) -> None:
    """Validate the form's CSRF token BEFORE _service — the per-route dependency (F2's cure).

    Purpose: recompute the expected token over the request's own path (the
    form's bound payload — the register form and the run's vote form each
    their own) + hmac.compare_digest (the timing discipline, key_verify's
    ONE-compare school); the drive-by's POST carries an absent-or-mismatched
    token => the refusal fires BEFORE _service (the write never lands).
    Starlette caches request.form() — the route's own parse reads the same
    cached body, no double-read.
    Refuses when: the token absent or mismatched (CsrfRefusedError).
    Provenance: the unit brief §3c, the design's F2, G-SERVING-TIER-INTEGRATION-BRIEF.
    """
    form = await request.form()
    presented = str(form.get(_CSRF_FIELD, ""))
    expected = _mint_csrf(request.url.path)
    if not hmac.compare_digest(presented, expected):
        raise CsrfRefusedError(
            expected=f"the form's {_CSRF_FIELD} field (minted into the served page)",
            found="absent-or-mismatched",
            next_action="reload the page and re-send — the re-render mints a fresh token",
        )
```
(`import hmac`, `import os`, `import secrets` join the stdlib block; `from fastapi import Depends` joins; `from prioritree.key_verify import AUTH_HEADER_DEFAULT` joins for the tier key.)

THE CHILD'S DEDICATED HANDLER (after the fold handler — the same handler-tier seam as the service's):
```python
@web_app.exception_handler(CsrfRefusedError)
def refuse_csrf(request: Request, exc: CsrfRefusedError) -> Response:
    """Render the CSRF refusal as the refusal fragment at 200 — the drive-by SEEN, never a silent OK, never the fold's clothes.

    Provenance: the unit brief §3c, rikai map 2 (the landing mechanics' seam),
    G-SERVING-TIER-INTEGRATION-BRIEF.
    """
    return _refuse_fragment(
        request,
        {"expected": exc.expected, "found": exc.found, "next_action": exc.next_action},
    )
```

### (b) THE TWO POST VALIDATION DEPENDENCIES + THE THREE RENDER CONTEXTS
The decorators: `@web_app.post(_REGISTER)` → `@web_app.post(_REGISTER, dependencies=[Depends(_csrf_guard)])`; `@web_app.post(_VOTE)` → `@web_app.post(_VOTE, dependencies=[Depends(_csrf_guard)])` (the decorator-dependencies form: no route parameter grown, ARG001 never fires, B008 never fires — no default-argument call).
THE THREE CONTEXTS' INJECTIONS (each render context grows the token over its own bound path):
- landing (:333): `return templates.TemplateResponse(request, "landing.html", {})` → `{"csrf_token": _mint_csrf(_REGISTER)}` (the route constant, not the literal — content-in-configuration).
- sitting (:373-:386): the context dict grows `"csrf_token": _mint_csrf(f"/ui/runs/{stem}/vote")` — the pair include's form posts THAT path (the sitting passes the token down through the include).
- pair fragment (:611-:622): the same key `"csrf_token": _mint_csrf(f"/ui/runs/{stem}/vote")` in the pair.html context.
THE TEMPLATES' HIDDEN INPUTS: landing.html's register form (after the fieldset, before the button): `<input type="hidden" name="csrf_token" value="{{ csrf_token }}">`; pair.html's vote form (after the item_b hidden input, :5): the same line. pair.html serves BOTH the sitting's include and the fragment — the token arrives via both contexts, one template byte-set.

### (c) THE TIER KEY AT THE CLIENT CONSTRUCTION (the env knob's ?= form; the browser NEVER sees it)
```python
_WEB_KEY_ENV: Final[str] = "PRIORITYTREE_WEB_KEY"
_web_key: Final[str] = os.environ.get(_WEB_KEY_ENV, "")
_client = httpx2.AsyncClient(
    base_url=_BASE_URL,
    transport=httpx2.ASGITransport(app=service_app, raise_app_exceptions=False),
    headers={AUTH_HEADER_DEFAULT: _web_key} if _web_key else None,
)
```
THE HONEST ROW (the skeleton key): the child calls ALL SIX routes (POST /runs :572; GET next :361/:600; POST votes :651; GET state :435/:684; GET tally :472; GET manifest :354/:491/:606/:654) — the web tier's true consumed set is SCOPE_TOKENS WHOLE; no grant-map row covers it; the operator mints `prioritree key mint web-tier --class human --scopes register,next,cast,state,tally,manifest --audience service` (a six-token grant, its own row); its leak = every human's writes — single-point, the mitigation process-local custody + the 0600 store, the residual carried. The child's boot log line (after the client): `logging.getLogger("uvicorn.error").info(f"web tier key: {'present' if _web_key else 'absent'} (a six-token grant)")` — the price named at the boot, never silent. At auth-off the child's calls pass bare (the dependency short-circuits), the tier key vestigial.

### (d) THE WEB 401/403 LANE (the constants + the branch dispatch + the lane's templates)
The constants (:97's block grows): `_UNAUTHORIZED: Final[int] = 401` and `_FORBIDDEN: Final[int] = 403`. THE PAGE HELPER (beside _unknown):
```python
def _auth_page(request: Request, body: dict[str, Any], *, forbidden: bool) -> Response:
    """Render the auth lane's page — the service's OWN three fields verbatim, the path's heading (the fold's clothes never worn).

    Provenance: the unit brief §1c, rikai map 3, G-SERVING-TIER-INTEGRATION-BRIEF.
    """
    return templates.TemplateResponse(
        request, "auth.html", {"fields": _fields(body), "forbidden": forbidden},
        status_code=_FORBIDDEN if forbidden else _UNAUTHORIZED,
    )
```
THE NEW TEMPLATE web/templates/auth.html:
```html
<!-- auth — the 401/403 lane: the service's own three fields verbatim, the path's heading (servingtierintegrationspec §3d) -->
{% extends "base.html" %}
{% block title %}Priori-tree — the key{% endblock %}
{% block content %}
<section class="card">
  <h1>{% if forbidden %}The key lacks this act's scope{% else %}The service asked for a key{% endif %}</h1>
  <p class="quiet">{% if forbidden %}The key is good but not granted this act — re-mint it with the scope:{% else %}Mint a key and attach it — the operator's cure:{% endif %}</p>
  <dl class="three-part">
    <dt>Expected</dt><dd>{{ fields.expected }}</dd>
    <dt>Found</dt><dd>{{ fields.found }}</dd>
    <dt>Next action</dt><dd>{{ fields.next_action }}</dd>
  </dl>
</section>
{% endblock %}
```
THE BRANCH DISPATCH at every page route — the two branches BEFORE the fold branch (sitting :358-:360 and :365-:367; done :409-:411; progress :439-:441; result :483-:485 and :493-:495). The exact insert (sitting's manifest branch shown; the same form at every fold site):
BEFORE:
```python
        return templates.TemplateResponse(
            request, "fold.html", {"fields": _fields(manifest.json())}, status_code=manifest.status_code,
        )
```
AFTER:
```python
        if manifest.status_code == _UNAUTHORIZED:
            return _auth_page(request, manifest.json(), forbidden=False)
        if manifest.status_code == _FORBIDDEN:
            return _auth_page(request, manifest.json(), forbidden=True)
        return templates.TemplateResponse(
            request, "fold.html", {"fields": _fields(manifest.json())}, status_code=manifest.status_code,
        )
```
THE FRAGMENT LANE (pair :600-:608, vote :651-:656, state-strip :684-:686): the fragments teach the paths by rendering the service's OWN fields verbatim — the existing `return _refuse_fragment(request, _fields(nxt.json()), fold=...)` branch ALREADY renders the 401/403 bodies' three fields (the fold flag False at 401/403 by its own `== _CRASH` test) — the fragment form of the lane needs NO new branch, named here so the build never invents one; the arcs pin the fragment renders the mint's next_action verbatim.

## 4. F6 THE COVERAGE INVARIANT — the fence + the /docs recon ruled

THE /DOCS TRIO: stripped at the parent (§1j) — the child's own :156 strip precedent re-cited, both tiers closed; the fence's exemption set names the trio's disposition: NONE — stripped, absent from the table whole. THE 404/405 ROUTE-TABLE RENDER: STANDING (the brief §1g's ruling — the legal lanes are the product's surface, the gates guard the ACTS, never the map; no elision invented). THE FENCE'S TWO FORMS land in tests/test_service_auth.py (§7): the route-table walk PRIMARY (each APIRoute under the six paths asserted to carry the door — `route.dependant` walked, the dependency's `call.__qualname__` startswith "require_key"; the exempt set NAMED: the static and child mounts are Mount objects, never APIRoutes — the walk's own filter; the docs trio stripped, absent) + the source-scan kin (service.py's bytes: `"Depends(require_key("` counted == 6 — the test_service_store.py:241-245 school, the textual drift-guard backing the runtime walk).

## 5. THE MCP CAPPED-HALT DRIFT — mcp_server.py's over-cap render grown the floor's leg

The mirror's renderers grow the leg-4 parameter (the tally.py leg-4 grammar carried; the em dash rendered "--" per the module's own ASCII law at :347/:377): `_found_sections(..., missing_class_pairs, quorum)` gains after the shortfalls section:
```python
    if missing_class_pairs:
        rendered = ", ".join(
            f"({pair.item_a}, {pair.item_b}) missing {', '.join(classes)}"
            for pair, classes in missing_class_pairs
        )
        sections.append(f"uncorroborated pairs: {rendered}")
```
`_next_action_sections(..., missing_class_pairs, quorum)` gains after its shortfalls section:
```python
    if missing_class_pairs:
        rendered = ", ".join(
            f"({pair.item_a}, {pair.item_b}) needs {', '.join(classes)}"
            for pair, classes in missing_class_pairs
        )
        sections.append(f"cast the corroborating votes: {rendered} -- corroboration needs votes from BOTH CLASSES on existing pairs")
```
THE LOCAL RE-DERIVATION (:428-:449) — BEFORE: the loop accumulates pair_counts/touched only; AFTER (the class counts in the SAME pass; the policy predicate the law's one home):
```python
    pair_counts = dict.fromkeys(pairs, 0)
    pair_class_counts: dict[Pair, dict[str, int]] = {pair: dict.fromkeys(COMPARATOR_CLASSES, 0) for pair in pairs}
    touched: set[str] = set()
    for record in census.vote_log:
        if record.vote_id in excluded:
            continue
        pair_counts[record.pair] += 1
        pair_class_counts[record.pair][record.comparator_class] += 1
        touched.update((record.pair.item_a, record.pair.item_b))
```
and after the shortfalls line:
```python
    missing_class_pairs = [
        (pair, tuple(sorted(missing_classes(pair_class_counts[pair]))))
        for pair in pairs
        if missing_classes(pair_class_counts[pair])
    ]
```
with `found = _found_sections(zero_coverage, components, shortfalls, missing_class_pairs, manifest.quorum)` and `next_action = _next_action_sections(components, shortfalls, missing_class_pairs, manifest.quorum)`. The imports grow `from prioritree.policy import missing_classes` and `from prioritree.votes import COMPARATOR_CLASSES` (the render re-derives the core's legs as DATA — a render, never a policy; the MCP tier's doors stay unit 4's). Within the cap the refusal's own fields pass through VERBATIM (the cap never fires) — byte-standing.

[the spec's continuation — piece 2: §6 the flags' folds, §7 the test files, §8 the no-break proofs, §9 the per-step plan]
## Reported by togo — 2026-11-24T21:42:31Z

## 6. THE FLAGS' FOLDS (each exact before/after; the brief §2's three rulings)

**FLAG 1 — cli.py's module docstring** (the widened surfaces named honest):
- :11 BEFORE: "1 the refusal lineage
(the three typed refusals, str(e) verbatim on stderr), 2 the argv+unexpected" — AFTER: "1 the refusal lineage
(the four typed refusals, str(e) verbatim on stderr), 2 the argv+unexpected".
- :13-:15 BEFORE: "The tier fence held by construction: value-type imports only —
Persist, StoreRefusedError, STORE_HOME, OperatorDeclaration, the three
refusals, ExhaustedQueue — no Registry()/Session() at this tier" — AFTER: "The tier fence held by construction: value-type imports only —
Persist, StoreRefusedError, STORE_HOME, OperatorDeclaration, the three
refusals, ExhaustedQueue, KEYS_HOME, KeyStore, KeyStoreRefusedError — no
Registry()/Session() at this tier".
- :4-:6 BEFORE: "the five subcommands 1:1 on the five ops through the run-store ONLY — register" ... AFTER: "the five subcommands 1:1 on the five ops through the run-store ONLY — register" (the clause stands; the key group named at the fence line's tail): the :8 "no op added, no op re-derived (Q-cli-shape; the frozen door cited)." grows: "no op added, no op re-derived; the key tools group (prioritree key mint — the auth foundation's issuance verb over the KEY store) is no run op (Q-cli-shape; the frozen door cited)."
A docstring-only edit, zero behavior.

**FLAG 2 — the '--' to em-dash harmonization** (all three sites or none; the run_store.py:93 precedent cited — `super().__init__(f"{_prefix} — expected: {expected} | found: {found} | next: {next_action}")`):
- key_store.py:95 BEFORE: `super().__init__(f"{_prefix} -- expected: {expected} | found: {found} | next: {next_action}")` AFTER: the em dash form.
- key_verify.py:75 BEFORE: `super().__init__(f"{_prefix} -- expected: {expected} | found: {found} | next: {next_action}")` AFTER: the em dash form.
- key_verify.py:113 BEFORE: the same "--" form AFTER: the em dash form.
- THE PINNED TEST BYTE, the fix in the same dispatch: tests/test_key_mint.py:105 BEFORE: `assert err.startswith("refused -- expected:")` AFTER: `assert err.startswith("refused — expected:")`.
The "foundation's own bytes untouched" fence carries ONE NAMED EXCEPTION here (three message-form bytes, never behavior — the exception named, the collaborator's approval the fence's own act).

**FLAG 3 — the fence-silent test docstrings' undercounts** (each file's dispatch grows its own docstrings in the same edit):
- tests/test_session.py:45 BEFORE: "The gate's fixture: register, schedule, cast three, DONE, and the exact hand-computed emission." AFTER: "The gate's fixture: register, schedule, cast six (each pair human then llm), DONE, and the exact hand-computed emission."
- tests/test_run_store.py:47 BEFORE: "Register + four casts (mixed classes, one correction) → fresh load → the §3 surface equal, stamps excluded." AFTER: "Register + seven casts (mixed classes, one correction, the corroborating twins) → fresh load → the §3 surface equal, stamps excluded."
- tests/test_harness.py:8 BEFORE: "7 invocations on one --home tmp home, each step's returncode + exact stdout" AFTER: "10 invocations on one --home tmp home, each step's returncode + exact stdout"; :82 BEFORE: "Compose the full 7-invocation arc's argv sequence (§2) — one --home, seven processes." AFTER: "Compose the full 10-invocation arc's argv sequence (§2) — one --home, ten processes."; :103 BEFORE: "The success arc: 7 invocations on one tmp home — every rc 0 and the exact stdout bytes per step." AFTER: "The success arc: 10 invocations on one tmp home — every rc 0 and the exact stdout bytes per step."
- tests/test_service_acceptance.py:6 BEFORE: "subprocess — the eleven-request arc (register => manifest => next => vote x3" AFTER: "subprocess — the eleven-request arc (register => manifest => next => vote x6"; :182 BEFORE: "load under the real process), next (GET .../next), vote x3 over the" AFTER: "... vote x6 over the"; :215 BEFORE: "Register => manifest => next => vote x3 => the exhausted turn => tally, each body asserted." AFTER: "Register => manifest => next => vote x6 => the exhausted turn => tally, each body asserted."; :221 BEFORE: "200 the first pair with count 0; the three votes 200 with the acks" AFTER: "200 the first pair with count 0; the six votes 200 with the acks".
- tests/test_cli.py:69 BEFORE: "Drive the 3-item run to coverage — all 3 pairs voted at k=1." AFTER: "Drive the 3-item run to coverage — all 3 pairs voted human+llm at k=1 (six casts)."

## 7. THE TEST FILES WHOLE (every arc fenced by name, the counts exact)

### 7a. tests/test_service_auth.py (NEW — the doors' file; the mint-at-tmp fixture)
THE FIXTURE (the seam-injection precedent extended: app.state.seam + app.state.keys + app.state.auth per test — the boot's construction the default):
```python
@pytest.fixture
def client(tmp_path: Path) -> TestClient:
    app.state.seam = Serialize(tmp_path)
    app.state.keys = KeyStore(tmp_path / "keys.jsonl")
    app.state.auth = "on"
    return TestClient(app)


def _grant(scopes: Sequence[str], *, audience: str = "service", comparator_class: str = "human", home: KeyStore) -> str:
    key, _digest = home.mint("key-holder", comparator_class, scopes, audience)
    return key
```
THE SIX-SCOPE LITERALS (SCOPE_TOKENS cited as literals — the grant map's nouns): _ALL = ("register", "next", "cast", "state", "tally", "manifest").
THE ARCS (16 functions; 2 parametrizes → 24 runtime items):
1. `test_no_key_refused_401_at_every_route` (parametrize the six (method, path, path-with-RUN-0001) lanes): no header → 401, the ThreePart byte-exact: expected "the key in the X-Api-Key header", found "absent-or-unknown", next_action startswith "mint a key: prioritree key mint".
2. `test_wrong_key_same_401_three_fields` — a bogus key → the SAME three fields (the oracle never fed).
3. `test_wrong_audience_same_401_mcp_never_named` — an mcp-audience key at the service door → the SAME 401, "mcp" absent from the rendered fields whole.
4. `test_scope_denied_403_default_deny` (parametrize 2: the auditor's key at POST votes; the comparator's key at POST runs) → 403, expected f"the {scope} scope", found "the key's scopes [...]", next_action the re-mint.
5. `test_right_key_route_bodies_returned` — the six-token key: register 201, next 200 the pair, cast 200 the ack, state 200, manifest 200, tally's 200 at full coverage — the routes' own bodies.
6. `test_midflight_mint_lands_live_through_the_door` — a second container mints over the same home; the next request's door sees it (the stat ride).
7. `test_auth_off_degrade_six_routes_pass_bare` — `app.state.auth = "off"` (no key store needed): the six routes' bodies as today (register 201 → the arc).
8. `test_handler_lane_401_stays_401_never_500` — the no-key refusal's status 401 (the fold never re-badges; the body's next_action is the MINT, never ESCALATION).
9. `test_supersedes_author_mismatch_403_found_elides_the_author` — key-holder A casts VOTE-0001; key-holder B (a second mint) supersedes it → 403, found carries "another author's vote", "A" (the author's id) ABSENT from the body whole; the target pair untouched (census still counts VOTE-0001).
10. `test_own_author_supersede_passes` — the same key supersedes its own vote → 200, the ack chain.
11. `test_verified_id_wiring_body_id_ignored` — the key minted comparator_id="key-holder"; the POST body carries comparator_id="imposter" → the census/manifest's log stamps "key-holder" (the self-claim dies at the cast door); the ack 200.
12. `test_class_stamp_overrides_the_bodys_claim` — an llm-class key; the body claims "human" → the door's record stamps "llm" (the census's log or the tally's pair_class_counts consuming it).
13. `test_auth_off_class_falls_back_to_claim` — at off the body's class stamps (the degrade's price named in the docstring).
14. `test_fence_route_table_walk_every_service_route_gated` — over app.routes: every APIRoute whose path is one of the six carries a dependency with `call.__qualname__` startswith "require_key" (the factory marker); the exempt set NAMED in the docstring (the Mounts never walked; the docs trio stripped, absent — GET /docs 404 is arc 16's own).
15. `test_fence_source_scan_six_door_tokens` — service.py's bytes: `source.count("Depends(require_key(") == 6` (the test_service_store.py:241-245 school).
16. `test_docs_trio_stripped_at_both_tiers` — GET /docs, /redoc, /openapi.json → 404 (the parent, the child's own already disabled — the census's both-tiers finding closed).

### 7b. tests/test_web_face.py (GROWN — the CSRF + the lane; ~9 new functions)
THE FIXTURE GROWS one member: `app.state.auth = "off"` (the standing arcs ride the degrade — their request bytes byte-standing, the suite green with NO key store); the auth-on arcs overwrite it per test (the seam's own law).
1. `test_csrf_token_minted_in_three_render_contexts` — landing, sitting, pair fragment each carry `name="csrf_token"` hidden input (the token bound per path).
2. `test_csrf_valid_token_passes_register_and_vote` — the served token scraped from the page, posted → register 201 → ack; vote 200 → the ack chain.
3. `test_csrf_drive_by_refused_write_never_lands` — POST /ui/register with NO token field → 200 the refusal fragment: expected the csrf_token field, found "absent-or-mismatched", next_action reload; the run never created (the resume 404s).
4. `test_csrf_mismatched_token_refused` — a well-formed but wrong token → the same refusal.
5. `test_csrf_stale_secret_refused_re_render_cures` — monkeypatch the module's `_csrf_secret`, POST the stale token → refused; the fresh GET mints a fresh token → passes (the restart-invalidation price, in-process).
6. `test_web_401_page_lane_key_path_never_fold` — auth "on", keys an EMPTY KeyStore(tmp), the tier key unset → the sitting page renders the auth page at 401 with the service's next_action (the mint) verbatim, NEVER fold.html's ESCALATION.
7. `test_web_403_page_lane_scope_path` — a narrow key on the child's client (monkeypatch `web._client` with a fresh AsyncClient over the same ASGITransport + the cast-only key header) → the sitting page renders the scope path at 403.
8. `test_tier_key_rides_the_client_default_header` — the same monkeypatched client with the six-token key → the register fragment 201 through the gated service; the key ABSENT from every rendered page body (the browser never sees it).
9. `test_auth_off_web_calls_pass_bare` — auth "off" (no key store, no tier key) → the register fragment 201, the sitting page 200 (the child's calls short-circuit).
THE STANDING ARCS byte-standing (the register 201/422/bad-quorum arcs gain the served token in their form posts — the fixture's token scraped per arc; the docstrings' counts grow where the forms change, per file's same edit).

### 7c. THE OTHER GROWN FILES (the no-break members, one line each)
- tests/test_service_face.py (:48-:65 the fixture): grows `app.state.auth = "off"` — the standing wire arcs ride the degrade, byte-standing whole.
- tests/test_service_acceptance.py (:67-:102 the boot): `Popen(_ARGV, cwd=home, stderr=PIPE, env={**os.environ, "AUTH": "off"})` — the real-socket suite's dev mode preserved (the auth-off default); the docstrings fold per §6.
- tests/test_mcp_server_face.py, tests/test_store_lock_face.py, tests/test_service_store.py, tests/test_session.py, tests/test_run_store.py, tests/test_harness.py, tests/test_cli.py, tests/test_acceptance.py: NO auth member (they drive no HTTP service route — the MCP face re-binds the module's _seam directly; the acceptance harness the store tier; the CLI in-process) — named so the build never over-grows them; the docstrings fold per §6.
- tests/test_key_mint.py:105: the harmonized byte per §6.

## 8. THE NO-BREAK PROOFS + THE NAMED RULINGS

- THE AUTH-OFF DEFAULT: the suite green with NO key store — the fixtures' `app.state.auth = "off"` members (7c) + the acceptance boot's env; the failopen's route-tier form preserved (auth on + absent store = the 401 lane at every route, the boot marker naming the absence — the boot line byte-standing).
- THE SIX ROUTES' BODIES otherwise byte-standing (§1d's signatures alone grow; the wire serializers, the catch tables, the DONE body unchanged — except the cast route's §1h stamps and §1i's one 403 clause).
- THE CLI untouched beyond the docstring fold (§6 flag 1; the five ops' argv grammar, the exit mapping :486 byte-standing — KeyStoreRefusedError already in the tuple clause).
- THE FLOOR: 268 → **301** collected — +25 test functions (test_service_auth.py 16; test_web_face.py 9) + 8 parametrize expansions (the six-route 401 lanes; the two grant-map denials) = +33 runtime items. The brief's ~314 RECONCILED: its estimate priced ~36 functions; the ruled arcs land 25 — the estimate's slack returned honestly, the build's floor-green step names the landed count; any drift ruled at the gate.
- THE PER-FILE RULINGS if new ride (never blanket): (1) service.py grows ARG001 — the five read routes' door parameters ARE the ruled gate (the dependency's raise the act; the value consumed at the cast route alone) — the scheduler.py ARG001 precedent re-carried at the door tier; (2) NO new rulings expected at web.py (the CSRF region: all params used; BLE001 standing), votes.py (PLR0913/PLR0917 standing), mcp_server.py (D205 standing; the new imports clean), or the test files (S101/PLR2004 standing); the zero-findings bar: ruff ALL + pyright strict green at the same make, zero in-code ignores.

## 9. THE PER-STEP PLAN (R8, the file-unit; 9 dispatches, the read-backs named; each dispatch cites the unit brief + this spec)

1. **votes.py** — the SupersedeRefusedError class + the stage-5 author check (§2): read-back: the author mismatch refused, found elides the author (an in-process cast at the REPL), the CLI's self-claim passes.
2. **service.py** — the dependency region whole (§1: imports, constants, factory, aliases, six signatures, union, two handlers, app.state.keys, cast wiring, the 403 catch for §2's error, the /docs strip, the docstring amendment) — the ONE two-file precedent lands HERE: the route's SupersedeRefusedError catch clause rides this dispatch (the error's own wire mapping, never separable; the import's existence precedes the use). Read-back: the six routes 401 without a key (the ThreePart bodies), 403 at a scope denial, GET /docs 404, the boot marker's bytes unchanged, `prioritree key mint` at the shell + the header through the door.
3. **web.py** — the CSRF region + the tier key + the 401/403 lane (§3): read-back: the token in the three contexts, the drive-by's POST refused (the write never lands), the tier key at the client (the boot line), the auth page at a 401 (never fold.html).
4. **web/templates (landing.html, pair.html, auth.html NEW)** — the hidden inputs + the lane's page: read-back: the token present at the three serves, the auth page renders the fields verbatim.
5. **Makefile + pyproject.toml** — `PRIORITYTREE_WEB_KEY ?=` (after :7) + the start target's env carrier widened `env -u WEB_CONCURRENCY AUTH=$(AUTH) PRIORITYTREE_WEB_KEY=$(PRIORITYTREE_WEB_KEY) .venv/bin/uvicorn ...` (the AUTH precedent's form) + the service.py ARG001 named ruling (§8): read-back: make start renders the marker + the web-key line; ruff/pyright green on the entry.
6. **mcp_server.py** — the capped-halt floor leg (§5): read-back: an over-cap halt's found names the uncorroborated pairs (the same pass), within-cap bytes verbatim.
7. **THE FLAGS' FOLDS** — cli.py's docstring (flag 1) + the three prefix sites + test_key_mint.py:105 (flag 2) — one file per dispatch within: read-back: `grep -rn "refused --"` returns zero; the CLI's five subcommands + key green at test_cli.
8. **THE NEW TEST FILE** — tests/test_service_auth.py (§7a): read-back: the 16 arcs green (24 runtime items), the fence walk green.
9. **THE GROWN TEST FILES + FLOOR-GREEN** — test_web_face.py (the fixture member + the 9 arcs), test_service_face.py + test_service_acceptance.py (the auth-off members, the boot env), the five docstring folds (flag 3, each its file's same edit) — then `make` (pytest + ruff + pyright at the same make): read-back: 301 collected, all green, the exact count named in the build's report.

THE TRADE-OFF THE PLAN MUST CARRY: the skeleton key at the web tier (its leak = every human's writes — single-point; the mitigation process-local custody + the 0600 store, the residual in the honest statement); the id-binding never fires at the browser (the form's self-claim behind the tier key); the CSRF secret's restart invalidation (the standing POST's failure the re-render's cure); the supersedes door check's local-tier caller-faith (every placement prices to the §3 floor — the offline JSONL edit); the /docs strip's operator price (the browsable schema lost — the README's remedy, unit 5); the auth-off degrade's unverified class stamp (the floor's input the claim again — the operator's explicit act, the marker naming it). Every price named, never silent — the door wired to the rooms, the honest statement carried whole.

THE SPEC LANDED WHOLE — two report pieces composing one document; the projection at reports/synthesize/servingtierintegrationspec.md; the collaborator rules on this record at G-SERVINGTIERINTEGRATIONSPEC-BRIEF.
