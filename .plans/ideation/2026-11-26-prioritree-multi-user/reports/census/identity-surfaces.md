<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/identity-surfaces

**Route:** prioritree-multi-user (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-26T17:04:53Z |
| 2 | report | tansa | 2026-11-26T17:10:46Z |
## Reported by tansa — 2026-11-26T17:10:46Z

# THE IDENTITY CENSUS — every identity-asking form in the prioritree tree, line-pinned (tansa, packet census/identity-surfaces, 2026-11-26)

The ground read whole: the store's heart (Q-multi-user + the convening ruling — the shape earned: "identify once per browser... built into the system as opposed to trying to get the user to identify themselves on each individual operation"), the composition (reports/compose/route.md — tansa's leg: "every identity-asking form in the tree found"), FR-MEM-0041 (the lived cost, .plans/state/friction-ledger.jsonl line 51: the completion card's 78 swapped judgments abandoned at the repeated identification, RUN-0008 blocked at 234/312). This census answers WHAT EXISTS: every form that asks WHO, every form that remembers WHO, the machinery a session composes with — nothing decided, everything pinned.

## THE HEADLINE

**12 identity-asking surfaces in the product (web 5, service 2, CLI 3, MCP 2) — EVERY ONE per-operation; 2 carried forms (the sitting chain's DOM carry [page-lifetime], the tier key's record [process/token-lifetime]) — ZERO carry survives a browser navigation; 2 precedent surfaces (the acceptance harness, the test fixtures); ZERO cookie surfaces (src + tests grepped: no set_cookie, no cookie read, no SessionMiddleware, no Cookie import — session.py is U5's chain composition, not a browser session).**

## (1) THE WEB TIER'S IDENTITY SURFACES WHOLE

### W1 — the register form's operator field
- landing.html:12: `<label>Your name for yourself on this run. <input name="operator_id" required minlength="1"></label>` — the operator asked once per registration, carried NOWHERE (not the URL, not any later page).
- The POST read: web.py:885 `"operator_id": str(form.get("operator_id", ""))` → the service payload; the ack (ack.html:2-9) renders the run id + the sitting URL (click-to-copy), no identity.

### W2 — the sitting chain's hidden-field carry (THE ONE IDENTITY CARRIER THE PRODUCT HAS TODAY)
Mechanism, pinned whole:
- sitting.html:6-7: the label "Your name for yourself as a judge — it stamps your votes. The same entry rides every judgment you cast on this page." + `<input id="comparator-id" name="comparator_id" required minlength="1">` — NO value attribute: fresh at every page render.
- sitting.html:9: `{% include "pair.html" %}` — the pair region inside the page.
- pair.html:3: the vote form `hx-post="/ui/runs/{{ stem }}/vote" hx-target="#ack-region" hx-swap="innerHTML" hx-include="[name='comparator_id']"` — at every POST, HTMX pulls the page's input value into the form body.
- The chain's persistence: the pair fragment (GET /ui/runs/{stem}/pair, web.py:900-943) swaps #pair-region (vote-ack.html:5 `hx-target="#pair-region" hx-swap="outerHTML"`); the comparator input (sitting.html:7) sits OUTSIDE the swapped region — it SURVIVES fragment swaps within the page's lifetime. The carry rides the DOM's persistence alone — no server-side state, no cookie, no URL parameter.
- WHERE IT'S LOST: (a) any page navigation or reload — the input re-renders empty; (b) the deliberate judge page (W4) — a fresh render per pair; (c) the shareable URL (ack.html:5-6, the quorum>1 share line) — a second browser starts empty. The carry's lifetime IS the page's lifetime.

### W3 — the sitting page's comparator ask
- GET /runs/{stem} (web.py:476-558) renders sitting.html — the ask at sitting.html:6-7 rides EVERY sitting visit (a reload re-asks).

### W4 — the deliberate judge page's fresh per-visit form (FR-MEM-0041'S EXACT SURFACE)
- GET /runs/{stem}/pair (the `judge` controller, web.py:643-710) renders sitting.html TOO (web.py:693-710) — the SAME ask at sitting.html:6-7, fresh at EVERY deliberate pair visit, NO value carried from any prior page.
- The picker (pairs.html via web.py:602-640; the list at picker.html:2-10, both presentations' links at :6-7) asks NOTHING — every link lands on the judge page, which asks fresh.
- The done page (done.html, web.py:561-599) asks NOTHING — its "Judge a pair deliberately" link (done.html:10) lands on the picker → the judge page → the ask.
- FR-MEM-0041 (the ledger line 51, severity high, verbatim): "the judge page's form requires the voter name at every visit (the deliberate lane's forms fresh per pair, no identity carry), the sitting chain's hidden-field memory the only identity carrier in the product — the deliberate lane broke it; the collaborator abandoned the card at the repeated identification."

### W5 — the vote POST handler's comparator_id reads
- web.py:970-971: `"comparator_id": str(form.get("comparator_id", "")), "comparator_class": str(form.get("comparator_class", "human"))` — the id read from the form (the hx-include's pull); the class DEFAULTED "human": NO web form ever asks the class (grep over web/templates/: no comparator_class field anywhere) — the web tier's votes ride human by construction. A POST without the sitting page's input carries "" (the browser's `required` is the only guard; the wire the sole validator).
- The CSRF minted over the vote path at all three render contexts: web.py:546 (sitting), :698 (deliberate), :935 (pair fragment) — `_mint_csrf(f"/ui/runs/{stem}/vote")`.

## (2) THE OTHER TIERS' IDENTITY FORMS

### S — the service tier (2 surfaces)
- The register body's operator claim: service.py:158 (`operator_id: str`, RegisterRunRequest :135-160); consumed at :480 `OperatorDeclaration(id=body.operator_id, question=body.question)` — the operator identity is a SELF-CLAIM at the door (the register scope governs the right to register under auth-on; no operator verification exists at any tier).
- The cast body's comparator claims: service.py:187-188 (`comparator_id`, `comparator_class`, CastVoteRequest :163-191).
- THE VERIFIED-CLASS STAMPING AT THE DOOR: service.py:564-565 — `comparator_id = record.comparator_id if record.digest else body.comparator_id` (same for class) — under a VERIFIED key the record's stamps OVERRIDE the body's claims (F8: the self-claim dies at the cast door); under the degrade (auth off, _ANONYMOUS at service.py:224-231, digest="") the body's claims stand.
- THE LOAD-BEARING SEAM FOR THE SESSION: the web tier's in-process client carries the tier key (web.py:239-245, PRIORITYTREE_WEB_KEY → the AUTH_HEADER_DEFAULT header, process-lifetime) — under auth-on with the web key present, EVERY browser's vote is stamped the WEB KEY's comparator_id/class at the door, the browser's typed name overridden — the id-binding residual the heart names ("the browser's self-claim at the web tier"). The session's stamping must compose with this door's law honestly.

### C — the CLI tier (3 surfaces)
- register's --operator-id: cli.py:54 (FLAG_OPERATOR_ID), :181 (required), consumed :262.
- vote's positionals: cli.py:193 `comparator_id` ("who compared"), :194 `comparator_class`, consumed :321-322 (passed through UNVALIDATED, the door's exit-1 the validator, cli.py:302).
- key mint's identity at birth: cli.py:216 `comparator_id` positional ("the operator id the key names"), :217-222 `--class` (default human), :223 --scopes, :224 --audience; the record born at key_store.py:419-491 (validation :456-465: non-empty id, class in COMPARATOR_CLASSES).

### M — the MCP tier (2 surfaces)
- runs.register's operator_id: mcp_server.py:156 (RegisterInput :148-157); consumed :521.
- votes.cast's comparator_id + comparator_class: mcp_server.py:182-183 (CastInput :176-186); the verified-claims stamping at :589-595 — `identity.claims["comparator_id"]`/`["comparator_class"]` when authenticated (F8 tier-agnostic, service.py's school; the body's claim NEVER consulted at the verified door — the fabrication hole stays closed), else the body's claims (the degrade's fallback).
- The claims' birth: mcp_auth.py:178-188 — the KeyRecord mapped to the substrate's AccessToken: subject the comparator id (:182), the claims carry the stamps (:185-186); the adapter's verify at :158-177 (key_verify's verify WHOLE, audience "mcp"); the policy gate at :196-226 (the five-tool grant map :86-94, votes.census → the state token).

## (3) THE SESSION-ADJACENT MACHINERY ALREADY LANDED

### The CSRF token's stateless signed form (the session composes with it)
- web.py:119-121: PRIORITYREE_WEB_CSRF_SECRET the env knob (the configurability law's precedent form); unset ⇒ a boot-minted random secret (secrets.token_urlsafe(32)) — the restart-invalidation price carried (a boot's outstanding tokens die, the re-render mints fresh).
- web.py:144-146: _mint_csrf — HMAC-SHA256 over the payload (the form's own path).
- web.py:149-170: _csrf_guard — recompute over request.url.path (:164), hmac.compare_digest (:165), the refusal CsrfRefusedError (web.py:124-141) → the dedicated handler (web.py:441-453) rendering the refusal fragment at 200.
- The binding TODAY is PER-PATH: minted into the register form (web.py:473), the sitting (:546), the deliberate (:698), the pair fragment (:935); the per-path difference pinned by test_web_face.py:470. The session adds the per-browser binding; the HMAC-over-payload mint/validate is the composition precedent.

### The tier key (the class verification — the session composes, never replaces)
- key_verify.py:141-208: THE VERIFY CONTRACT — the sha256 digest lookup (:177-179), the F9 dummy compute (:181-188), the ONE compare (:192), F5 the audience check (:196 — a wrong-audience key the SAME 401, the oracle never fed), F8 at :198-200 ("the record's class the verified truth — no claim parameter exists, the body's self-claim never taken"), the scope check (:202-207).
- key_store.py:117-122: the record {digest, comparator_id, comparator_class, scopes, audience, created_at} — the carried identity per key (hashed-at-rest).
- The three doors: the service door (service.py:234-259 require_key; the degrade carrier :224-231), the web client's own carry (web.py:239-245), the MCP door (mcp_auth.py:121-188 + the gate :196-226).

### The cookie surfaces: NONE (named honestly)
- grep over src/prioritree/ AND tests/ for `set_cookie|cookies|SessionMiddleware|Cookie`: ZERO matches. The tree sets no cookie, reads no cookie, mounts no session middleware. The session would be the tree's FIRST cookie surface. (src/prioritree/session.py exists but is U5's chain composition — register→vote→tally over the two stores, docstring session.py:2-26; no browser-session machinery.)

## (4) THE STANDING PRECEDENTS IN-TREE

### The acceptance harness's identity forms
- acceptance.py:89: HARNESS_COMPARATOR_ID = "acceptance-noisy-comparator" (R5: the identity recorded, never anonymous, :85-88).
- acceptance.py:255: the operator `OperatorDeclaration(id="acceptance-op", question="Which is more important?")`.
- acceptance.py:271-272: the per-pair stamps `comparator_id=f"{HARNESS_COMPARATOR_ID}-{pair_count + 1}"`, the class cycling HARNESS_JUDGE_CLASSES (:90, sorted COMPARATOR_CLASSES — the corroboration floor's mix grown at the harness).

### The test fixtures' identity injection (the session tests' future form)
- test_web_face.py:61-64: the identity as PER-REQUEST FORM DATA — `_OPERATOR = {"operator_id": "op-1", ...}`, `_VOTE = {"comparator_id": "x", "comparator_class": "human"}`, `_FORM_VOTE = {"item_a": "a", "item_b": "b", "winner": "prefer-a", **_VOTE}`; posted per arc (e.g. :368).
- test_web_face.py:82-93: the client fixture — TestClient(app) with app.state.seam/auth injection (the auth-off member at :92); NO cookie handling anywhere in tests/ (grep: zero matches).
- test_web_face.py:96-109: _scrape_csrf — the served page's token scraped per arc (the per-request form; a session moves the carrier to the cookie jar).
- test_service_face.py:46, :97 et al.: the identity as per-request JSON body fields ("op-1", "x").
- test_cli.py: argv identity (the positionals/flags at C above).
- The future session tests' form: the TestClient (httpx2) carries a cookie jar — the fixture's injection seam (app.state.* overwrite) already isolates the store; the session middleware rides the same app the fixture builds.

## (5) THE HONEST COUNT (the cost map's raw material)

**The product's identity-asking surfaces: 12 — every one PER-OPERATION.**
- Web (5): W1 the landing ask (landing.html:12); W2 the register read (web.py:885); W3 the sitting ask (sitting.html:6-7); W4 the judge ask fresh-per-visit (sitting.html:6-7 via web.py:693-710 — FR-MEM-0041's surface); W5 the vote read (web.py:970-971 — the class defaulted, never asked).
- Service (2): the register body's operator claim (service.py:158/:480); the cast body's comparator claims (service.py:187-188).
- CLI (3): --operator-id (cli.py:54/:181); the vote positionals (cli.py:193-194); the key mint (cli.py:216-222).
- MCP (2): register's operator_id (mcp_server.py:156); cast's comparator_id+class (mcp_server.py:182-183).

**The carried forms: 2 (+2 record forms).**
- The sitting chain's DOM carry (sitting.html:7 + pair.html:3) — PAGE-lifetime only; lost at every navigation; the deliberate lane's every visit re-asks (the measured cost).
- The tier key's record (key_store.py:117-122; verified at key_verify.py:141-208) — the service/MCP callers' identity carried per key; the web tier's own process-lifetime carry (web.py:239-245).
- Record forms (persistence, not identification): the vote line's stamps (run_store.py:469-470, :742-769 — comparator_id/class on every vote line) and the MCP AccessToken claims (mcp_auth.py:183-187).

**Precedents: 2** (the acceptance harness's simulated stamps; the fixtures' per-request injections). **Cookie surfaces: 0.**

**THE SPLIT'S HEADLINE: 12 per-operation asks vs 0 carries that survive navigation** — the browser tier's human has NO identity carry beyond one page's DOM; the service/MCP/CLI tiers' callers carry ONLY by the tier key (a process/token-lifetime form). The session's earn (FR-MEM-0041): a carry that survives navigation, per browser.

## THE COMPOSITION POINTS (pinned, never decided)

1. THE CSRF'S STATELESS FORM (web.py:119-170): the HMAC-over-payload precedent + the env-knob form — the session's secret knob composes here; the per-path binding today, the session adds the per-browser binding.
2. THE TIER KEY'S CLASS VERIFICATION (key_verify.py:141-208, F8 at :198): the session composes, never replaces — the llm-class constraint's mechanical ground (the class rides the key at the service/MCP doors; the session is the HUMANS' lane).
3. THE CAST DOOR'S STAMPING LAW (service.py:564-565; mcp_server.py:589-595): under a verified digest the body's claims die — under the web key the browser's typed name is overridden TODAY (the id-binding residual); the session's stamping must rule its composition with this door honestly.
4. THE COOKIE VOID: no cookie machinery exists (0 matches src+tests) — the session lands as the tree's first; SessionMiddleware and the signed-cookie forms are rikai's lane at the sources.
5. THE FIXTURE SEAM (test_web_face.py:82-93): the injection fixture + the per-request form-data identity — the session tests' future form rides the same TestClient's cookie jar.

— tansa, the census whole; every finding a pointer, nothing decided.
