<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — validate/serving-tier-integration

**Route:** prioritree-auth (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-24T23:30:31Z |
| 2 | report | kensho | 2026-11-24T23:34:51Z |
## Reported by kensho — 2026-11-24T23:34:51Z

# THE SERVING-TIER-INTEGRATION INDEPENDENT VERIFICATION — kensho (validate/serving-tier-integration, 2026-11-24)

Unit 3's independent verify — my own instrument runs (never the build's word), the spec's clauses read against the landed source, the laws checked at the built surface, jikko's reported choices each tested for honesty. THE VERDICT: THE BUILD WORKS — the zero-errors/zero-warnings bar met, every spec clause landed, every residual named honest, every deviation reported never silent.

## 1. THE INSTRUMENTS RE-RUN (my own runs, the tree's own way — make test / make lint / make typecheck)

- TEST (uv run pytest): **"299 passed in 32.00s"** — the exact count jikko's step-9 report names (299); my run CONFIRMS.
- LINT (uv run ruff check src/ tests/): **"All checks passed!"** — zero findings.
- TYPECHECK (uv run pyright): **"0 errors, 0 warnings, 0 informations"** — the zero-warnings bar held.

## 2. THE SPEC'S CLAUSES CHECKED (the landed source against servingtierintegrationspec's fences)

### 2a. The dependency region (§1) — service.py
- The imports grown: Depends/Annotated join (:68/:70); the key_store line carries KeyRecord (:76); the key_verify line NEW (:77 — AUTH_HEADER_DEFAULT, KeyScopeError, KeyVerifyError, verify); SupersedeRefusedError (:83).
- The four constants after NEXT_ACTION (:109-112): _UNAUTHORIZED 401, _FORBIDDEN 403, _SERVICE_AUDIENCE "service", _AUTH_OFF "off" — the cited literals, never re-derived.
- _ANONYMOUS (:219-222): the module constant record, digest="" the anonymous marker.
- The factory require_key (:225-252): the §1c fence verbatim — off => _ANONYMOUS; on => the store from app.state.keys, the header via AUTH_HEADER_DEFAULT, verify(store, presented, "service", token); the typed data to the handlers.
- THE SIX ALIASES (:255-260) at the grant-map tokens 1:1: register/next/cast/state/tally/manifest — Depends on the TYPE annotation (Annotated), never a default argument; the B008/pyright dodge by construction.
- THE SIX SIGNATURES: register :445 (_RegisterDoor), serve :474 (_NextDoor — the door BEFORE seed per the pyright law), cast_vote :504 (_CastDoor), census :550 (_StateDoor), rank :584 (_TallyDoor), describe :623 (_ManifestDoor).
- render_refusal's union widened (:264-269): KeyVerifyError | KeyScopeError admitted per §1e; **SupersedeRefusedError grown beyond the fence — the checker-forced deviation jikko reported at step 2, honest** (the §1i catch renders through the one point; strict refuses the omission).
- THE TWO DEDICATED HANDLERS (:410-417 refuse_key → 401; :420-427 refuse_scope → 403): after refuse, before _TALLY_PATH; two handlers, no shared ancestor; the fold never re-badges (arc 8: 401 stays 401, "escalate" ABSENT from the body).
- app.state.keys (:210): ONE line promoted; the marker reads len(app.state.keys.records) (:212) — the module-local discarded.
- THE CAST ROUTE'S STAMPS (:527-528): record.comparator_id/comparator_class if record.digest else the body's claims — the degrade fallback keyed on the anonymous marker; the docstring names the price (:510-513).
- The SupersedeRefusedError 403 catch (:543-544) — §1i's clause.
- THE /DOCS TRIO STRIPPED (:195): app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None).
- The :13-15 no-Depends claim amended; the status paragraph grown 401/403 (:19-24 — the coordinator's fold 4).

### 2b. The 401 trio's SAME bytes (F5, the oracle never fed)
key_verify's _refuse_unknown_key constructed ONCE (:116-138), raised at the digest miss (:188), the failed compare (:193), the audience mismatch (:197) — all three legs the SAME three fields. The arcs pin it: no-key at all six routes (parametrized, the ThreePart byte-exact — expected "the key in the X-Api-Key header", found "absent-or-unknown", next_action the mint), the wrong key the SAME, the wrong-audience key the SAME with "mcp" ABSENT from the fields whole.

### 2c. The supersedes door check (§2, F4)
SupersedeRefusedError (:137-167): the three-field grammar, the em dash per :134's own bytes. THE AUTHOR CHECK (:497-505): inside stage 5's `if clean_supersedes is not None:` block, AFTER the same-pair check (:481-489), inside cast_vote's locked region by construction — no seam verb grown, no TOCTOU. found :503 ELIDES the author — target.comparator_id NEVER rendered; arc 9 pins the author's id ABSENT from the body whole and the target pair untouched (VOTE-0001 still counted). The auth-off note (:490-496) names the caller-faith price.

### 2d. The /ui/ cure (§3)
- The CSRF region (:108-166): _CSRF_SECRET_ENV :113; _csrf_secret :114-116 (the env or the boot-minted random); _CSRF_FIELD :117; CsrfRefusedError the three-field grammar; _mint_csrf HMAC-SHA256 (:140-142); _csrf_guard (:145-166) — recomputes over request.url.path, **hmac.compare_digest :161**, the ThreePart refusal.
- The child's dedicated handler refuse_csrf (:403-415): after the fold handler, renders _refuse_fragment at 200 — never the fold's clothes.
- THE TWO POST GUARDS (:652/:753): dependencies=[Depends(_csrf_guard)] — the decorator form, no route parameter grown.
- THE THREE RENDER CONTEXTS: landing :435 `{"csrf_token": _mint_csrf(_REGISTER)}` (the route constant); sitting :488 + pair :743 `"csrf_token": _mint_csrf(f"/ui/runs/{stem}/vote")`. The templates: landing.html:24 + pair.html:6 the hidden input, ONE byte-set serving both the sitting include and the fragment; the per-path binding pinned (the landing and sitting tokens differ).
- auth.html: the 14 lines byte-identical to §3d's fence.
- THE TIER KEY (:232-241): the env knob read at construction, the client's DEFAULT header `headers={AUTH_HEADER_DEFAULT: _web_key} if _web_key else None` — every _service call inherits; the boot line names the six-token grant; arc 8 pins the key ABSENT from every rendered body (:556/:559 — the browser never sees it).
- THE 401/403 LANE'S BRANCHES BEFORE EVERY FOLD SITE: sitting :460-463 + :471-474; done :520-523; progress :554-557; result :602-605 + :616-619 — _auth_page at 401/403, the fold branch last; the fragment lane untouched (the standing verbatim-fields render, no branch invented — §3d's ruling held); the 401 page lane's body carries the mint's next_action verbatim, ESCALATION absent (arc 6).

### 2e. F6 — the coverage invariant (§4)
- The route-table walk (arc 14): every APIRoute walked — each asserted IN the six-path set AND carrying the require_key marker; gated == the six BOTH directions (no seventh route exists); the exempt set NAMED (the Mounts never walked by the isinstance filter; the docs trio absent).
- The source scan (arc 15): source.count("Depends(require_key(") == 6 — my own grep: 6 matches, exactly the aliases :255-260.
- The /docs trio's 404s (arc 16): /docs, /redoc, /openapi.json all 404 at both tiers.

### 2f. The MCP capped-halt drift (§5)
Both renderers' signatures grown missing_class_pairs (:340/:377); _found_sections' uncorroborated section (:365-370, after shortfalls); _next_action_sections' corroborating cure (:408-414 — the floor_head split, jikko's reported E501 deviation, zero rendered-byte effect); the re-derivation (:451-465): pair_class_counts accumulated in the SAME pass, **missing_classes the one home** (policy.py's predicate, never a re-derivation); the call sites pass the leg (:470-471); the within-cap early return byte-standing (:466-467).

### 2g. The folds (§6)
- The em-dash harmonization: key_store.py:95, key_verify.py:75/:113 all the em dash; test_key_mint.py:105 the harmonized byte. **My own scans: "refused --" and "_prefix} --" ZERO matches in src/ and tests/** — the code surface harmonized whole. (The 14 whole-tree matches live in the effort's own .plans record store — the reports and the append-only ledger quoting the BEFORE bytes; records never rewrite, and the fold's clause is the code surface.)
- cli.py's docstring honest (:8-17): the key tools group named, the four typed refusals, KEYS_HOME/KeyStore/KeyStoreRefusedError in the fence enumeration.
- votes.py's stage-5 sketch honest (:386-389 — SupersedeRefusedError named at the door; the coordinator's fold 5 at :469-470).
- service.py's status paragraph honest (:19-24).
- The five test files' docstrings at the grown counts: session:45 (cast six, each pair human then llm); run_store:47 (seven casts, the corroborating twins); harness:8/:82/:103 (10 invocations); acceptance:6/:186/:219/:225 (vote x6) + :227 (count 1..6 — togo's Ruling-2); cli:69 (human+llm, six casts).
- The two coordinator test-byte rulings: test_mcp_server_face.py:388 the re-placed needle ("(c, e) 0 of 1" not in payload); :487/:559 the "x" author corrections landed (the :496 different-pair arc correctly untouched — the same-pair check fires before the author check).

## 3. THE LAWS

- **The llm-class constraint**: the mint's --class a free token (no choices= — the fence), key_store validates in COMPARATOR_CLASSES (:462-465) — human and llm the SAME mint verb, the same form at every door; the verify seam never branches on class for approval (F8: no claim parameter exists); the vote scope granted identically for both classes (SCOPE_TOKENS; the 403's expected names the scope, never the class); **"approval" ZERO matches in src/ — no human-approval gate anywhere** (the tally's corroboration needs BOTH classes — a floor on the run's coverage, never a gate on a vote's landing; the llm's vote lands directly with its key).
- **The ThreePart at every auth refusal**: KeyVerifyError, KeyScopeError, SupersedeRefusedError, CsrfRefusedError all carry expected/found/next_action; render_refusal the one render point; auth.html renders the three verbatim; the fragments render the service's own fields verbatim.
- **The configurability at every knob**: AUTH (Makefile :7 `?=` + :34 the carrier; service.py :209 resolve_auth_mode); PRIORITYTREE_KEYS_HOME (key_store :48, resolve_keys_home :144-161); PRIORITYTREE_WEB_KEY (Makefile :8 `?=` + :34 the carrier; web.py :232-233); the CSRF secret's env PRIORITYTREE_WEB_CSRF_SECRET (web.py :113); the header name's carrier AUTH_HEADER_DEFAULT (key_verify :32 — "the name a knob from birth", read by name at the door :250 and the web client :237).
- **The zero-ignore strictness**: zero noqa, zero "type: ignore" in src/ and tests/ (the one textual match is tests/__init__.py's docstring NAMING the INP001 fix — "presence, never a noqa"); every pyproject entry a named ruling — service.py's grown row :134 with the ARG001 ruling paragraph :127-133 (the five non-cast doors' record parameters + the two handlers' protocol request, the spec §1d/§8 cited); web.py's grown row :156 with S105/PLR0911/C901 each named :147-155 (§3a/§3d cited).

## 4. THE RESIDUALS NAMED (jikko's reports' choices — each verified honest)

- **The 299-vs-301 arithmetic**: my run's 299 = 268 + 25 new functions (16 in test_service_auth.py + 9 in test_web_face.py — all at the spec's names) + 6 true parametrize expansions (arc 1's six lanes = +5 beyond its base; arc 4's two lanes = +1). The spec's 301 = 268 + 25 + 8 — the +8 counted the LANES (6+2) as additive over the 25 functions, double-counting the two parametrized functions' own base items. The -2 drift is honest arithmetic, never a missing arc: the true delta +6, exactly as jikko's step-9 names it.
- **The auth-off claim-fallback**: service.py :527-528 — under the degrade the anonymous record's digest is "" and the body's claim stands; the docstring names it; arc 13 pins the unverified claim stamping; the boot marker names the degrade (landed unit 1, standing).
- **The skeleton-key price**: the web child consumes ALL SIX routes (my own read: POST /runs :699; GET next :467/:516/:727; POST votes :779; GET state :550/:812; GET tally :591; GET manifest :456/:614/:733/:782) — the six-token grant the true scope set, its leak = every human's writes; the boot line names it at :239-241; the report carries the honest row.
- **The CSRF restart-invalidation price**: the boot-minted secret (:114-116, unset env => token_urlsafe(32)) kills a boot's outstanding tokens; the region's comment names the price; arc 5 pins it in-process (the stale token refused, the re-render's fresh token cures).

## 5. THE DEVIATIONS/CHOICES (each reported by jikko, each verified landing honestly)

render_refusal's union grown SupersedeRefusedError beyond §1e's fence (checker-forced); Callable in the TYPE_CHECKING block (UP035/TC003); the mcp-start carrier NOT widened (mcp_server imports neither service nor web — the key vestigial there; the additive-never-rework reasoning sound); the E501 floor_head split at mcp_server :413-414; the two docstring rewraps (the 120-line law, every word kept); arc 5's llm-class twin for the corroborating half (the tally gate demands both classes — named in the arc's docstring); the drive-by arc's autoescaped byte assertion (Jinja's served form); arc 9's "other-holder" second author; flag 3's five docstring folds found already-on-disk at step 9's start (verified true now); step 2b's R1+R2 and step 7b's two test-byte rulings all landed byte-exact.

## THE VERDICT

**THE BUILD WORKS.** The instruments: 299 passed, ruff all checks passed, pyright 0 errors/0 warnings/0 informations — the zero-errors AND zero-warnings bar met on my own runs. The spec's clauses: every fence landed (the dependency region, the 401 trio's SAME bytes, the two dedicated handlers, the supersedes door check with the author elided, the /ui/ cure whole, the F6 fences, the MCP floor leg, the folds). The laws held: the llm-class constraint (the same mint at every door, no approval gate), the ThreePart at every refusal, the configurability at every knob, the zero-ignore strictness with named rulings. The residuals honest: the 299-vs-301 drift is true arithmetic (+6 never +8), the degrade's claim-fallback, the skeleton key, the restart invalidation — each named, never silent. The gate G-SERVING-TIER-INTEGRATION's independent verify: GREEN.
