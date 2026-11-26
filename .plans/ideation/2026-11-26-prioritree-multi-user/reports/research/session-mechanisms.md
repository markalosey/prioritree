<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — research/session-mechanisms

**Route:** prioritree-multi-user (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-26T17:04:53Z |
| 2 | report | rikai | 2026-11-26T17:11:39Z |
## Reported by rikai — 2026-11-26T17:11:39Z

# THE SESSION MECHANISM MAPS (rikai, research/session-mechanisms, 2026-11-26)

## 0. THE VERIFICATION LANES + THE ABSENCE NAMED
- Installed bytes: starlette 1.10.0 (.venv/lib/python3.13/site-packages/starlette/middleware/sessions.py; the lock pins it — uv.lock:1613-1623, resolved deps = anyio alone, uv.lock:1617-1619) + uvicorn 0.54.0 (config.py:358-359). The tree's bytes: web.py, service.py, key_verify.py, key_store.py, votes.py, the web templates, the tests.
- THE ABSENCE (a finding, stated as fact): itsdangerous is imported at the sessions module's own scope (sessions.py:8-9) and is starlette's `full` extra (starlette-1.10.0.dist-info/METADATA:32) — it appears NOWHERE in uv.lock nor in site-packages. THE MIDDLEWARE IS UNIMPORTABLE AT THE TREE'S CURRENT VENV: `from starlette.middleware.sessions import SessionMiddleware` refuses at ModuleNotFoundError until itsdangerous joins [project] dependencies — the signed-cookie option's free-tier price named at the mechanism's own door (one pure-Python wheel, no service, no infra).

## 1. STARLETTE'S SESSIONMIDDLEWARE — the installed bytes' map

### 1a. The construction (sessions.py:16-40)
- `secret_key: str | Secret` REQUIRED (line 20); the signer built at construction: `itsdangerous.TimestampSigner(str(secret_key))` (line 30).
- `session_cookie: str = "session"` (line 21); `max_age: int | None = 14*24*60*60` (line 22 — 14 days); `path: str = "/"` (line 23); `same_site: Literal["lax","strict","none"] = "lax"` (line 24); `https_only: bool = False` (line 25 — True appends "; secure", lines 35-36); `domain` (lines 26, 37-38); `partitioned` (lines 27, 39-40).
- HttpOnly is HARDCODED — `"httponly; samesite=" + same_site` the security_flags' head (line 34), never a knob. The auth precedent's Starlette note ("signed cookie, HttpOnly, 'readable but not modifiable'") verified at the bytes: HttpOnly always on; readable-but-not-modifiable the signing's truth (§1b).
- max_age rides TWO CLOCKS: the signer's unsign age check (line 53) AND the cookie's Max-Age attribute (line 76 — `Max-Age={max_age}; ` only when not None); None => a browser-session cookie AND no age check.
- Every knob constructor-parameter shaped — the configurability law composes at the Makefile's ?= school (Makefile:3-8).

### 1b. The signed-cookie mechanism — "readable but not modifiable" at the code
- The write: `b64encode(json.dumps(session))` then `self.signer.sign(data)` (lines 70-71) — the itsdangerous TimestampSigner form: base64(payload).timestamp.signature. The payload is decodable by anyone holding the cookie (READABLE: the voter's own name visible in their own cookie bytes); the signature is the tamper wall (NOT MODIFIABLE: any payload byte change breaks the HMAC).
- The load: cookie -> `.encode("utf-8")` -> `self.signer.unsign(data, max_age=self.max_age)` -> `Session(json.loads(b64decode(data)))` (lines 50-55).
- THE TAMPER TRUTH (a gotcha the threat model prices): `except BadSignature: scope["session"] = Session()` (lines 56-57) — a forged/tampered cookie NEVER raises; it silently becomes a FRESH EMPTY session (the visitor re-identifies; cast votes keep their stamps). No alarm, no log line.
- The engine's internals (digest choice, timestamp encoding) are NOT verifiable at this tree: itsdangerous absent (§0). The interface the tree would run is the three call points visible at sessions.py:30/53/71.

### 1c. The lifecycle — load, write, empty-skip
- Per request `scope["session"] = Session(...)` (lines 54/57/59) — a fresh dict per request loaded from the cookie; NO server-side state in the module (the whole state rides the cookie — restart-proof by construction).
- The write intercepts `http.response.start` in the send_wrapper (lines 61-65): (1) modified AND non-empty => Set-Cookie with the signed payload (lines 68-79): `session=<signed>; path=/; Max-Age=<n>; httponly; samesite=lax`; (2) modified AND emptied AND initially non-empty => the deletion cookie `session=null; expires=Thu, 01 Jan 1970 00:00:00 GMT; ...` (lines 80-89) — the identity-erase verb; (3) NOT modified => NO Set-Cookie at all (the empty-session-skip — an anonymous GET never pays the cookie).
- `session.accessed` => `Vary: Cookie` added (lines 66-67) — the caching-honesty flag.
- The dict subclass tracks mutations (lines 95-138): __setitem__/__delitem__/clear/pop/popitem/setdefault/update/__ior__ mark modified — `request.session["comparator_id"] = name` is the write-arming form.
- The read seam: requests.py:170-177 — `request.session` asserts `"session" in self.scope` ("SessionMiddleware must be installed to access request.session"), marks accessed, returns the dict. A controller touching request.session before the middleware runs REFUSES at the assert — the mount-order law (§4).

### 1d. The gotchas, priced at the bytes
- DICT-IN-MEMORY PER-REQUEST: each request loads a fresh snapshot; two in-flight responses in one browser each sign their OWN snapshot — last-write-wins on concurrent session writes (lost update). The session would carry identity bytes only (a name + a class token), never a vote — the race's blast radius is the identity map, not a vote.
- SIZE LIMIT: the whole session rides one cookie; sessions.py has NO size guard (absent — a fact) — the browser's ~4KB cookie cap is the content budget; the identity form is bytes-trivial.
- MULTI-WORKER: the signed-cookie form is STATELESS — N workers sharing one secret all unsign identically (safe by construction). The tree's WEB_CONCURRENCY env-unset law pins the single-process truth: Makefile:34 `env -u WEB_CONCURRENCY ... uvicorn prioritree.service:app` (no --workers flag); uvicorn's rule at config.py:358-359 (`workers is None and "WEB_CONCURRENCY" in os.environ` => that count) — unset => ONE worker. The same law holds at the MCP lane (Makefile:85).
- WEBSOCKET: scope types http AND websocket both pass (lines 43-45) — no lane blocked.
- THE SECRET'S PRECEDENT: web.py:119-120 — `PRIORITYTREE_WEB_CSRF_SECRET` env or a boot-minted `secrets.token_urlsafe(32)`; the same ?= form a session secret rides, the restart-invalidation price already ruled in the module's own comment (a boot's outstanding artifacts die unless the env knob is set).

## 2. THE IDENTITY SEAMS THE SESSION COMPOSES WITH (the tree's own bytes)

### 2a. The vote POST's comparator_id — where the session substitutes
- web.py:970: `"comparator_id": str(form.get("comparator_id", ""))` — the vote fragment reads the identity from the FORM body; the session's value substitutes at exactly this read.
- web.py:971: `"comparator_class": str(form.get("comparator_class", "human"))` — the class rides the same body with the "human" default; NO form field carries it (pair.html has none) — the web default IS the humans' lane (the llm-class constraint's boundary: llm votes ride the mcp tier's keys, never this door).

### 2b. The register's operator field
- web.py:885: `"operator_id": str(form.get("operator_id", ""))`; landing.html:12 the input ("Your name for yourself on this run"). The OPERATOR's declaration is the run's ground (the registry stamps it) — a DIFFERENT identity from the comparator's sitting identity: two identities, two surfaces, one browser. The session composes here as a PRE-FILL at most, never a silent substitute (the run's owner-claim is the registration act, not a browser state).

### 2c. The sitting chain's hidden-field carry — the retirement's mechanism
- THE CHAIN TODAY: sitting.html:6-7 the comparator_id input ("The same entry rides every judgment you cast on this page") — PAGE-SCOPED memory; pair.html:3 `hx-include="[name='comparator_id']"` pulls it into each vote POST; pair.html:4-7 the hidden fields item_a/item_b/csrf_token/presentation_order (the PAIR's state, never identity); vote-ack.html:5 the ack's `hx-trigger="load"` + hx-get to the pair fragment — the chain continues WITHIN the page (the input survives the pair-region swap because it lives outside #pair-region).
- THE BREAK: the chain's memory dies at every page load (the sitting page asks afresh) and NEVER EXISTED at the deliberate lane — FR-MEM-0041 verbatim: "the judge page's form requires the voter name at every visit (the deliberate lane's forms fresh per pair, no identity carry), the sitting chain's hidden-field memory the only identity carrier in the product — the deliberate lane broke it".
- THE RETIREMENT: the session build removes sitting.html's input (with pair.html:3's hx-include) and substitutes web.py:970's read; the hidden fields item_a/item_b/presentation_order STAY (pair state, not identity); the csrf_token's mint composes (§2e). Both lanes share sitting.html (the sitting include and the judge render, web.py:693-695) — one template seam cures both.

### 2d. The deliberate judge page's forms
- web.py:643-710 (judge): the picker's chosen pair rendered ON the sitting surface — the same sitting.html, the same comparator_id ask, the csrf minted over the vote path (web.py:698), presentation_order from the swap knob (web.py:706); the picker page itself (web.py:602-640, pairs.html) and the done page ask NO identity. The session retires the ask at the shared template — the deliberate lane's per-visit cost (FR-MEM-0041's ground) cured by the same substitution.

### 2e. The CSRF guard's composition — the stateless HMAC token vs the session
- TODAY (web.py:114-170): the STATELESS SIGNED TOKEN — `_mint_csrf(payload) = HMAC-SHA256(_csrf_secret, payload)` over the request's PATH (web.py:144-146); the guard recomputes over `request.url.path` and compare_digests (web.py:162-165); the mints at web.py:473 (register), :546 (sitting), :698 (judge), :935 (pair fragment). The token binds to the PATH, never to a visitor — the same token for every visitor at the same path; the wall is the path-binding + the secret, NOT visitor-binding.
- FORM (i) UNCHANGED BENEATH (the zero-touch composition): the session lands, the stateless token keeps guarding — no rewrite; both secrets ride the same env-knob-or-boot-mint school (web.py:119-120).
- FORM (ii) THE CARRIED / DOUBLE-SUBMIT SHAPE: a per-session nonce minted at render, stored `request.session[...]`, compared at POST — the double-submit form (token in form + copy in the session). Its mechanism requires the middleware to run before the guard's read (the session rides the same request); its price: the token becomes visitor- and session-bound (a stale tab's token dies at re-identification), the refusal's cure copy (web.py:169 "reload the page and re-send") still true.
- THE TEST SEAMS: test_web_face.py:461-498 the CSRF arcs (minted-in-three-contexts, valid-passes, drive-by-refused-write-never-lands, mismatched-refused) — whichever form the design rules, the arcs ride the same TestClient.

### 2f. The tier key's layer — the class verification unchanged beneath
- THE WEB TIER'S KEY: web.py:239-245 — `PRIORITYTREE_WEB_KEY` env; the in-process client sends `AUTH_HEADER_DEFAULT: _web_key` (one credential for the whole child, every visitor behind it, httpx2 over ASGITransport in-process — no socket).
- THE SERVICE DOOR: service.py:234-263 the require_key factory — AUTH=off => `_ANONYMOUS` (digest="", service.py:224-231); AUTH=on => `verify(store, presented, "service", token)` (service.py:261), the audience pair {"service","mcp"} (key_store.py:53), the scopes' grant map (key_store.py:52).
- THE STAMP OVERRIDE (service.py:564-565): `comparator_id = record.comparator_id if record.digest else body.comparator_id`; `comparator_class = record.comparator_class if record.digest else body.comparator_class` — F8: the verified record's stamps REPLACE the body's claims at the armed door; the degrade keeps the body's claim (key_verify.py:141-208 the verify contract; the class never taken from the body at the armed door — key_verify.py:198-200).
- THE SEAM'S HONEST SHAPE: with the web key ARMED, every web visitor stamps as the key record's identity (comparator_id uniform — the per-visitor distinction dies at the door, verified-stamp arcs pinned at test_service_auth.py:366-395); with the door DEGRADED (the web tier's standing member — test_web_face.py:91-92 `app.state.auth = "off"`), the body's claim — tomorrow the SESSION's value — rides through. THE COMPOSITION: the session narrows the SELF-CLAIM at the web tier (one identification per browser); the class stays the verified layer's; the id-binding residual is narrowed NEVER erased (the signed cookie is still a browser-held artifact — the threat model's surface).
- THE CLASS GATE BENEATH: votes.py:44 `COMPARATOR_CLASSES = {"human","llm"}` — the write-time gate (votes.py:553-558) checks the class regardless of tier; the session never touches it; the llm lane rides the mcp audience's keys (key_store.py:53), never the browser — the llm-class constraint mechanical at the bytes.

## 3. THE ALTERNATIVE MECHANISMS — the divergence's options priced mechanically

### Option [i] — the signed-cookie session (the banked shape's engine, Starlette's SessionMiddleware)
- MECHANISM: §1 whole — the identity JSON rides the cookie, itsdangerous-signed; the server holds only the secret.
- PRICE: + itsdangerous (§0's absence — one pure-Python wheel, the free-tier price); the ~4KB cookie budget (identity-sized: trivial); the tamper-silence (§1b — the forged cookie silently re-identifies, an honest residual to name); the secret's boot-mint-or-env form (the CSRF precedent's restart price, web.py:119-120); restart-proof (no server state — a reboot keeps every visitor identified); multi-worker-safe though the tree pins single-process anyway (§1d).
- COMPOSITION WITH THE LANDED SURFACES: web.py:970's read substitutes; sitting.html's ask retires (both lanes at the one template); the shareable URL UNCHANGED (the run id in the path, the identity in the cookie — each browser its own voter at the same URL — ack.html:5-6 the share nudge intact); the tier key and the class gate untouched (§2f).

### Option [ii] — the server-side session store (the memory/dict form)
- MECHANISM: a module-level dict {session_id: identity}; the cookie carries only an opaque random id; the store consulted per request.
- PRICE: viable ONLY under the tree's single-process truth (§1d — one process, one dict; N workers would fork the dict and diverge the identities, WEB_CONCURRENCY's env-unset law the only thing standing between the design and that hazard); RESTART-LOSS: the dict dies with the process — every visitor re-identifies at the next boot (FR-MEM-0041's form again at a coarser cadence; the CSRF secret's boot-mint precedent prices the shape, web.py:119-120); a persistence layer (a JSONL store — the run_store school, one flat self-describing line per record) cures the loss at the price of a third store home plus its lifecycle; the fixation surface changes shape (an opaque id forgeable-by-capture, the store the oracle — the threat model's different animal).
- COMPOSITION: the same seams (§2) with the session write becoming the store's append; the cookie never carries the identity (read-side opacity — a privacy gain at the price of state).

### Option [iii] — the per-operation status quo (the measured non-completeable)
- MECHANISM (as it stands): the form-field identification at every page/visit — the sitting chain's page-scoped hidden-carry the only identity memory (§2c); the deliberate lane none.
- PRICE (MEASURED at FR-MEM-0041, severity high): the 78 swapped judgments abandoned at the repeated identification, the run blocked at 234/312, the collaborator's verbatim "basically makes the task non-completeable... too much work on the human"; the probe's completion the standing dependency (RUN-0008 riding the session unit's gate per the composition's ruling). The option's mechanism is the ABSENCE of a session — the map's baseline, priced at the lived cost, not an estimate.

## 4. THE SEAMS' MAPS WHOLE — every line a session build would touch
1. THE MIDDLEWARE'S MOUNT POINT — two legal forms: (a) the CHILD: web.py:231 the web_app construction (`add_middleware` on the child — the session rides the web lanes alone, the service's six JSON routes session-free, the llm/stdio/tools lanes never see a session — the humans'-lane constraint held mechanically); (b) the PARENT: service.py:200-201 the app construction + the tail mount at service.py:706-708 (the whole mounted-wrapped form — scope["session"] set at every lane, the service lanes' price). The child form keeps the seam local; either way the mount must precede any request.session read (requests.py:172's assert).
2. THE FORMS' READS: web.py:970 (the vote's comparator_id — THE substitution), web.py:971 (the class default — unchanged), web.py:885 (the register's operator_id — the pre-fill composition, never a substitute), the mints' paths web.py:473/:546/:698/:935 (the CSRF — unchanged or carried, §2e).
3. THE TEMPLATES: sitting.html:6-7 (the ask retires — both lanes), pair.html:3 (the hx-include retires with it), pair.html:4-7 (the hidden pair fields STAY), landing.html:12 (the operator input — unchanged), ack.html:5-6 (the shareable URL — unchanged), vote-ack.html:5 (the chain — unchanged, the pair fetch carries no identity today and needs none).
4. THE KNOBS FROM BIRTH (the configurability law): the session secret (the PRIORITYTREE_WEB_CSRF_SECRET school, web.py:119-120 — env knob + boot-mint fallback), the cookie's forms (sessions.py:21-27 the constructor's own parameters: name, max_age, same_site, https_only, domain, partitioned), the AUTH knob's ?= pair (Makefile:7, key_store.py:61-62).
5. THE TESTS' INJECTION POINTS: the per-test overwrite school — app.state.seam/keys/auth (test_web_face.py:91-92, test_service_auth.py:103-105, test_service_face.py:69-70); TestClient(app) rides cookies natively (the client's jar the session arcs' instrument); the CSRF arcs (test_web_face.py:461-498); the verified-stamp arcs (test_service_auth.py:366-395 — the door's override semantics pinned: test_verified_id_wiring_body_id_ignored, test_class_stamp_overrides_the_bodys_claim, test_auth_off_class_falls_back_to_claim); the degrade member (test_web_face.py:590 test_auth_off_web_calls_pass_bare).
6. THE NO-TOUCH FENCE (verified absent of any browser-session concern): session.py the LIBRARY's composition layer (session.py:2-26 — register->schedule->vote->tally, the sitting chain's public face; the NAME collision a naming-law fact: "session" names the sitting chain at the library tier, the browser's session a different mechanism entirely — a build names its symbol accordingly); cli.py and mcp_server.py (the stdio/tools lanes); votes.py:44/553-558 (the class gate); run_store.py (the run file); key_store.py/key_verify.py (the tier key's own layer).

— rikai, the session's machinery mapped at the installed bytes and the tree's own; the alternatives priced at their mechanisms; every claim cited to file:line.
