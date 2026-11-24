<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — build/serving-tier-integration

**Route:** prioritree-auth (executing) | **Events:** 23 | **Reports:** 11

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-24T21:48:05Z |
| 2 | report | jikko | 2026-11-24T21:55:50Z |
| 3 | dispatch | shinko | 2026-11-24T21:56:11Z |
| 4 | report | jikko | 2026-11-24T22:07:48Z |
| 5 | dispatch | shinko | 2026-11-24T22:08:09Z |
| 6 | dispatch | shinko | 2026-11-24T22:08:09Z |
| 7 | report | jikko | 2026-11-24T22:10:56Z |
| 8 | report | jikko | 2026-11-24T22:27:19Z |
| 9 | dispatch | shinko | 2026-11-24T22:27:54Z |
| 10 | dispatch | shinko | 2026-11-24T22:27:54Z |
| 11 | dispatch | shinko | 2026-11-24T22:27:54Z |
| 12 | dispatch | shinko | 2026-11-24T22:27:54Z |
| 13 | report | jikko | 2026-11-24T22:29:54Z |
| 14 | report | jikko | 2026-11-24T22:36:26Z |
| 15 | report | jikko | 2026-11-24T22:42:54Z |
| 16 | dispatch | shinko | 2026-11-24T22:43:29Z |
| 17 | report | jikko | 2026-11-24T22:51:29Z |
| 18 | dispatch | shinko | 2026-11-24T22:51:56Z |
| 19 | dispatch | shinko | 2026-11-24T22:51:56Z |
| 20 | report | jikko | 2026-11-24T22:52:38Z |
| 21 | report | jikko | 2026-11-24T23:07:30Z |
| 22 | dispatch | shinko | 2026-11-24T23:07:47Z |
| 23 | report | jikko | 2026-11-24T23:29:54Z |
## Reported by jikko — 2026-11-24T21:55:50Z

STEP 1/9 LANDED — votes.py's supersedes door check per servingtierintegrationspec §2 (packet build/serving-tier-integration).
- src/prioritree/votes.py ONLY: SupersedeRefusedError :137-167 (after VotesRefusedError, the three-field grammar, found ELIDES the target's author, the 403 named in the class docstring); the author check :495-503 inside stage 5's locked block, after the same-pair check; the auth-off note :488-494 (§2c — the door rides the PASSED comparator_id; under auth-off the claim form stands).
- The refusal's three fields verbatim: expected "a correction of the caller's own vote — the superseder's comparator_id matches the target's author"; found "{handle} — another author's vote (the author never named)"; next_action "cite your own vote on this pair, or cast a new vote without supersedes".
- CHOICE (reported): the fence's compressed docstrings completed to the five-field school (the VotesRefusedError/KeyVerifyError/KeyScopeError precedent — the seat's five-field law); every fenced byte landed verbatim within.
- INSTRUMENTS (run per the dispatch's "if you run them"): ruff check src/ tests/ → "All checks passed!"; pyright → "0 errors, 0 warnings, 0 informations".
- GAP (predicted, NOT fixed — outside the fence): tests/test_mcp_server_face.py :487 (test_supersedes_same_pair_lands) and :559 (test_census_as_is_after_correction) cast "y" correcting "x"'s VOTE-0001 — the check now refuses both; the spec §7c names the file no-break with no edit ruled — the coordinator's call (tests not run here; the floor decides).
- GAP (stale claim, NOT touched): cast_vote's docstring still reads "every refusal raises VotesRefusedError before any byte lands" — false as of this landing; a docstring fold could ride a later dispatch.
- Nothing else: one file, no tests run, no other edits.
## Reported by jikko — 2026-11-24T22:07:48Z

jikko — build/serving-tier-integration step 2 of 9 (service.py's dependency region whole; servingtierintegrationspec §1). One file: src/prioritree/service.py, 572→667 lines.
LANDED: imports grown (Depends/Annotated/KeyRecord/the key_verify line/SupersedeRefusedError/Callable); the four constants after NEXT_ACTION; _ANONYMOUS; the factory + six aliases; the six signatures; render_refusal's union; the two dedicated handlers; app.state.keys promoted (marker's render reads app.state.keys, three states byte-standing); the cast route's if-record-else-body stamps + the degrade named in the docstring; the SupersedeRefusedError 403 catch; the /docs trio stripped; the :13 no-Depends claim amended.
FACTORY (verbatim, :220-247): def require_key(token: str) -> Callable[[Request], KeyRecord]: / def _door(request: Request) -> KeyRecord: if request.app.state.auth == _AUTH_OFF: return _ANONYMOUS; store = cast("KeyStore", request.app.state.keys); presented = request.headers.get(AUTH_HEADER_DEFAULT, ""); return verify(store, presented, _SERVICE_AUDIENCE, token); return _door — off => _ANONYMOUS, on => verify("service", token), typed data to the handlers.
SIGNATURES (verbatim, :440/:469/:499/:545/:579/:618): register(request: Request, body: RegisterRunRequest, record: _RegisterDoor) -> JSONResponse; serve(request: Request, run_id: str, record: _NextDoor, seed: int | None = None) -> JSONResponse; cast_vote(request: Request, run_id: str, body: CastVoteRequest, record: _CastDoor) -> JSONResponse; census(request: Request, run_id: str, record: _StateDoor) -> JSONResponse; rank(request: Request, run_id: str, record: _TallyDoor) -> JSONResponse; describe(request: Request, run_id: str, record: _ManifestDoor) -> JSONResponse — grant map 1:1 (register/next/cast/state/tally/manifest), serve's door before seed per the pyright law.
HANDLERS (verbatim registrations, :405/:415 — after refuse, before _TALLY_PATH): @app.exception_handler(KeyVerifyError) def refuse_key -> 401 render_refusal(exc); @app.exception_handler(KeyScopeError) def refuse_scope -> 403 render_refusal(exc) — the fold's 500-rebadge dodged.
DEVIATIONS (checker-forced, both reported): (1) render_refusal's union grew "| SupersedeRefusedError" beyond §1e's AFTER line (wrapped per E501) — §1i's fenced catch renders it through the one point and pyright strict + §8's zero-findings bar refuse the omission; (2) Callable rides an `if TYPE_CHECKING:` block (collections.abc — UP035/TC003), not §1c's "joins the typing import" (key_verify.py:24-27 school).
FINDINGS STANDING (the spec's own named class): ARG001 x7 — the five doors' unread `record` + the two handlers' protocol `request`; §1d/§8 rule them, the pyproject entry ["BLE001","E402","PLC0415","ARG001"] is §9 STEP 5's dispatch; zero pyproject bytes landed here (R8's one-file law).
INSTRUMENTS (allowed as the patch's findings): pyright 0/0/0; ruff — UP035/TC003 cured same-turn, the seven ARG001 alone remain; the suite NOT run (the floor step's own).
NOT DONE: pyproject ARG001 (step 5); web.py/templates (steps 3-4); tests (steps 8-9); named residual — the module docstring's status-mapping paragraph names no 401/403 (§1k amends the Depends clause alone; unfenced bytes left standing, the coordinator's call).
## Reported by jikko — 2026-11-24T22:10:56Z

Step 2b landed — the fold's R1+R2 via patch (3 hunks, 2 files, findings none); nothing else touched.
R1 tests/test_mcp_server_face.py:487 — `    result = _cast(caller, ["a", "b"], "prefer-b", "x", supersedes="VOTE-0001")`
R1 tests/test_mcp_server_face.py:559 — `    _cast(caller, ["a", "b"], "prefer-b", "x", supersedes="VOTE-0001")`
R2 src/prioritree/votes.py:386 — `        the same pair, or another author's vote — every refusal raises`
R2 src/prioritree/votes.py:387 — `        VotesRefusedError, the door's author mismatch SupersedeRefusedError,`
R2 src/prioritree/votes.py:388 — `        before any byte lands. NEVER refuses on content plausibility (the system has no`
Choices: the "NEVER refuses..." tail rides the fence's last added line byte-untouched; :496's different-pair arc untouched (same-pair check :479 fires before the author check :495) — no assertion changed, per the fold's re-derivation.
Gaps: none. Not done: everything else — the ruling's NOTHING else held; no self-verification run (the instruments run at the floor).
## Reported by jikko — 2026-11-24T22:27:19Z

# Step 3/9 — web.py's /ui/ cure landed (servingtierintegrationspec §3, one file: src/prioritree/web.py)

Read-back, CSRF region verbatim (:108-166): `_CSRF_SECRET_ENV: Final[str] = "PRIORITYTREE_WEB_CSRF_SECRET"`; `_csrf_secret: Final[bytes] = (os.environ.get(_CSRF_SECRET_ENV, "").encode() or secrets.token_urlsafe(32).encode())`; `_mint_csrf` = `hmac.new(_csrf_secret, payload.encode(), "sha256").hexdigest()`; `_csrf_guard` recomputes over request.url.path + `hmac.compare_digest`, absent-or-mismatched => CsrfRefusedError(expected the form's csrf_token field, found "absent-or-mismatched", next_action "reload the page and re-send — the re-render mints a fresh token"); the child's dedicated handler `refuse_csrf` renders it at 200 via _refuse_fragment (:403-414, after the fold handler).
Read-back, tier key (:232-241): `_WEB_KEY_ENV: Final[str] = "PRIORITYTREE_WEB_KEY"`; `headers={AUTH_HEADER_DEFAULT: _web_key} if _web_key else None` at the client's construction; the boot line `logging.getLogger("uvicorn.error").info("web tier key: %s (a six-token grant)", "present" if _web_key else "absent",)` — G004's lazy-% form, rendered bytes identical to the fence.
Read-back, the lane's branches — the exact insert at every fold site (six: sitting manifest/nxt, done nxt, progress result, result tally/manifest): `if X.status_code == _UNAUTHORIZED: return _auth_page(request, X.json(), forbidden=False)` + `if X.status_code == _FORBIDDEN: return _auth_page(request, X.json(), forbidden=True)` before the fold return; the fragment lane untouched (the standing verbatim-fields render, no branch invented); _auth_page beside _unknown (:306-313, auth.html's render call — the template itself is step 4).
The two POST guards: `@web_app.post(_REGISTER, dependencies=[Depends(_csrf_guard)])` (:652), `@web_app.post(_VOTE, dependencies=[Depends(_csrf_guard)])` (:753); the three render contexts: landing `{"csrf_token": _mint_csrf(_REGISTER)}` (:435), sitting (:488) + pair (:743) `"csrf_token": _mint_csrf(f"/ui/runs/{stem}/vote")`.
Choices: two fenced docstring summaries rewrapped at sentence boundaries (the 120 line-length law, every word kept); _UNAUTHORIZED/_FORBIDDEN inserted ascending after _CREATED; the CSRF region placed after _FRAGMENT_LANE (after _BASE_URL's block); the class docstring landed as fenced (the refuse_key/refuse_scope precedent).
GAPS FOUND (the spec §8 "if new ride" ruling row, NOT landed — one-file law, no in-code ignores, never redesign the ruled form): S105 on _CSRF_SECRET_ENV's value :113 (a public env-knob name, never a credential); PLR0911 sitting (10>6 returns) and result (10>6); C901 result (11>10) — the spec's exact two-branch insert at every fold site is the cause; proposed step-5 pyproject row: `"src/prioritree/web.py" = ["BLE001", "S105", "PLR0911", "C901"]` with the named comment citing §3d's ruled form.
Also named for the gate: the four page routes' "any other non-200 => the fold page" docstring clauses now exclude 401/403 — no web.py docstring fold was fenced, so unamended here (the R2 school applies if the gate wants it).
NOT done (step 4's own): the templates' hidden inputs + auth.html. Instruments unrun (the floor is step 9).
## Reported by jikko — 2026-11-24T22:29:54Z

STEP 4/9 (R8 file-unit law) — web/templates: the hidden inputs + the lane's page. LANDED via patch (3 files, one apply; first attempt refused on a context-indent mis-anchor — re-anchored in-turn, zero findings).
READ-BACK changed regions verbatim — landing.html:24 `    <input type="hidden" name="csrf_token" value="{{ csrf_token }}">` (after </fieldset>, before the button); pair.html:6 the same line (after item_b hidden :5) — one byte-set serving BOTH the sitting include and the fragment.
READ-BACK auth.html WHOLE — the 14 lines byte-identical to spec §3d's fenced block (extends base.html; the forbidden flag's two forms: "The key lacks this act's scope"/"The service asked for a key" + the two quiet cure lines; fields.expected/found/next_action rendered verbatim in the three-part dl) — read-back whole on disk, zero drift.
NOT done: sitting.html (the token rides the pair include — the spec's one-byte-set ruling); the /docs strip's template consequences (§4 fences none — the trio strip is service.py's step-2 act); tests + the instruments (the floor step 9's own).
Ground confirmed: web.py's :435/:488/:743 contexts pre-landed carrying csrf_token; _auth_page :306 renders fields+forbidden — the templates' context keys match the served seams.
## Reported by jikko — 2026-11-24T22:36:26Z

# STEP 6 LANDED — mcp_server.py's capped-halt floor leg (servingtierintegrationspec §5; 588 -> 611 lines)

IMPORTS: `from prioritree.policy import missing_classes` (:33, isort-first); COMPARATOR_CLASSES already rides :41 (the module's fork-guard birth) — the spec's named votes import stands, no byte moved.
RENDERERS GROWN: both signatures gained `missing_class_pairs: Sequence[tuple[Pair, tuple[str, ...]]]` before quorum (:340, :377 — tally.py's own annotation); _found_sections' uncorroborated section lands after its shortfalls section (:365-370, head "uncorroborated pairs: ... missing ..."); _next_action_sections' corroborating cure lands after its shortfalls (:408-414, "cast the corroborating votes: ... -- corroboration needs votes from BOTH CLASSES on existing pairs").
READ-BACK — the re-derivation region :451-465 verbatim:
    pair_counts = dict.fromkeys(pairs, 0)
    pair_class_counts: dict[Pair, dict[str, int]] = {pair: dict.fromkeys(COMPARATOR_CLASSES, 0) for pair in pairs}
    touched: set[str] = set()
    for record in census.vote_log:
        if record.vote_id in excluded:
            continue
        pair_counts[record.pair] += 1
        pair_class_counts[record.pair][record.comparator_class] += 1
        touched.update((record.pair.item_a, record.pair.item_b))
    shortfalls = [(pair, pair_counts[pair]) for pair in pairs if pair_counts[pair] < manifest.quorum]
    missing_class_pairs = [
        (pair, tuple(sorted(missing_classes(pair_class_counts[pair]))))
        for pair in pairs
        if missing_classes(pair_class_counts[pair])
    ]
THE CALL SITES pass the leg (:470-471: `found = _found_sections(zero_coverage, components, shortfalls, missing_class_pairs, manifest.quorum)` / `next_action = _next_action_sections(components, shortfalls, missing_class_pairs, manifest.quorum)`); the within-cap early return byte-standing (:466-467) — the refusal's own fields verbatim, the cap never fires; the comprehension placed directly after the shortfalls line (the fence's own words), mirroring tally.py:526-533.
DEVIATION (named): the fence's one-line `sections.append(f"cast the corroborating votes: {rendered} -- corroboration needs votes from BOTH CLASSES on existing pairs")` (133 chars) — ruff E501 flagged it in the patch findings; the floor_head split landed (:413-414, tally.py:426-427's own form under the ASCII law's "--") — zero rendered-byte effect, fixed same-turn per the zero-findings bar (the policy-layer step-2 COM812 precedent's form).
OBSERVED 1: the renderers' + _capped_halt's docstrings still name the pre-leg-4 section sets — §5 fences no docstring bytes; left untouched per the fence (the step-2 OBSERVED precedent).
OBSERVED 2: tests/test_mcp_server_face.py:388 `assert "(c, e)" not in payload` (the zero-votes over-cap arc, 15 pairs) — the uncapped uncorroborated section now renders (c, e) in the payload, voiding the assertion's premise ("the eleventh capped out"); §7c rules that file untouched and flag 3 omits it — named for the ruling before the step-9 floor.
NOT done: the floor-green instruments (step 9) + kensho's verification — never my own eyes.
## Reported by jikko — 2026-11-24T22:42:54Z

# Step 7/9 — the flags' folds landed (spec §6 + the two coordinator folds; one patch, 11 files, 17 hunks applied)
Fold 1, cli.py docstring — read-back verbatim: :8-10 "added, no op re-derived; the key tools group (prioritree key mint — the auth foundation's issuance verb over the KEY store) is no run op (Q-cli-shape; the frozen door cited)."; :12-13 "(the four typed refusals, str(e) verbatim on stderr)"; :16-17 "OperatorDeclaration, the three refusals, ExhaustedQueue, KEYS_HOME, KeyStore, KeyStoreRefusedError — no Registry()/Session() at this tier".
Fold 2, the em dash (run_store.py:93 precedent) — key_store.py:95, key_verify.py:75/:113 now `super().__init__(f"{_prefix} — expected: {expected} | found: {found} | next: {next_action}")`; test_key_mint.py:105 `assert err.startswith("refused — expected:")`; "refused --"/`_prefix} --` zero tree-wide.
Fold 3, the undercounts — test_session.py:45-48 """The gate's fixture: register, schedule, cast six (each pair human then llm), DONE. / And the exact hand-computed emission."""; test_run_store.py:47-50 """Register + seven casts (mixed classes, one correction, the corroborating twins). / → fresh load → the §3 surface equal, stamps excluded."""; test_harness.py:8 "10 invocations on one --home tmp home…", :82 "the full 10-invocation arc's argv sequence (§2) — one --home, ten processes", :103 "The success arc: 10 invocations on one tmp home…"; test_service_acceptance.py:6/:182 "vote x6", :215 "vote x6 => the exhausted turn => tally", :221 "the six votes 200 with the acks"; test_cli.py:69 "all 3 pairs voted human+llm at k=1 (six casts)".
Coordinator fold 4, service.py:19-24 — "201 register's alone; 401 the unverified key (KeyVerifyError — the auth door's authentication half: absent-or-unknown the SAME three fields, the identity oracle never fed; the dedicated handler, never the fold); 403 the scope-denied key (KeyScopeError — the authorization half's own refusal) and the supersedes author mismatch (SupersedeRefusedError at the cast route — found elides the author); 404 …".
Coordinator fold 5, votes.py:375-376 — "(5) the supersede ground truth (a correction corrects the same judgment — the target live in the same run, on the same pair, by the caller's own hand — the author check) then the dedup key…".
CHOICE (priced, reported): the two fenced sentences exceed one physical line (test_session:45 = 130 chars, test_run_store:47 = 140; E501 at 120) and a 2-line same-paragraph wrap fires D205 (the mcp_server.py named-ruling precedent) — landed as the tree's summary+blank+body test-docstring form, split at the sentence's natural clause boundary, EVERY word kept, the split's punctuation adjusted (", DONE, and" → ", DONE." + "And …"; "twins) →" → "twins)." + "→ …"); lint confirms my 11 files carry ZERO findings.
GAPS FOUND (pre-existing, not mine, untouched): lint = 11 findings — service.py ARG001 x7 (:411/:421 request, :445/:474/:550/:584/:623 record — the doors' ruled surface; spec §1d's pyproject entry "ARG001" is STEP 5's act, not yet landed: pyproject:128 still reads ["BLE001","E402","PLC0415"], no PRIORITYTREE_WEB_KEY in the Makefile) + web.py 4 (S105 :113 _CSRF_SECRET_ENV, PLR0911 :439/:570, C901 :570 — step 3's lane grown past the rule bars; UNRULED, spec §8 expected none at web.py — triage before the floor). Residual: test_service_acceptance.py:223 "the run's census count 1..3" stale at six votes — outside §6's fence, reported not touched.
NOT DONE: nothing else (the NOTHING-else fence held); no pytest/pyright/floor runs (step 9's act; docstring-only edits — the patch's same-turn checks + one routed lint check the finding loop, both green on my surfaces).
## Reported by jikko — 2026-11-24T22:51:29Z

Step 5b landed — the re-run's two files, one patch (pyproject.toml + Makefile, 4 hunks applied, zero findings); NOTHING else touched.
pyproject :134 "src/prioritree/service.py" = ["BLE001", "E402", "PLC0415", "ARG001"] — the existing row grown (§1d's fenced row, never a new row); the ARG001 paragraph :127-133 cites the spec §1d/§8 + G-SERVING-TIER-INTEGRATION-BRIEF, naming the seven findings: the five non-cast doors' record parameters ARE the ruled gate (the dependency's 401/403 raise IS the act; the value consumed at the cast route alone — the scheduler.py precedent re-carried at the door tier) + the two key-refusal handlers' protocol request (Starlette's fixed (request, exc) signature — the body renders the refusal alone).
pyproject :156 "src/prioritree/web.py" = ["BLE001", "S105", "PLR0911", "C901"] — the existing row grown (the tests/test_harness.py grown-entry form, no duplicate row); the RULING paragraph :147-155 cites the spec §3a/§3d + G-SERVING-TIER-INTEGRATION-BRIEF: S105 — _CSRF_SECRET_ENV's literal is the env knob's own public NAME (never a credential in source; the boot-mint fallback the configurability law); PLR0911 — sitting's and result's return counts ARE the ruled lane's own form (§3d's exact two-branch insert at every fold site); C901 — result's complexity likewise the ruled lane's branches.
tests/test_service_auth.py — NO entry landed: §7a/§8 name no per-file row (§8 rules the test files' S101/PLR2004 standing under the tests/** blanket).
Makefile :8 `PRIORITYTREE_WEB_KEY ?=` (after :7 `AUTH ?= on`, §9's fenced form verbatim); Makefile :34 the start target's carrier widened: `@nohup env -u WEB_CONCURRENCY AUTH=$(AUTH) PRIORITYTREE_WEB_KEY=$(PRIORITYTREE_WEB_KEY) .venv/bin/uvicorn prioritree.service:app --host $(HOST) --port $(PORT) ...` (the AUTH precedent's env -u form; the line's tail byte-standing).
CHOICE (reported): mcp-start's carrier (:83) NOT widened — §9's step-5 region fences the start target's uvicorn carrier alone, and mcp_server.py imports neither service nor web (the key vestigial at the MCP launch; a uniform AUTH-precedent carrier there would be additive, never rework).
NOT DONE: everything else — steps 8-9's test files + the floor instruments (kensho's/the coordinator's eyes, never my own); no ruff/pyright run here.
## Reported by jikko — 2026-11-24T22:52:38Z

R11 — step 7b landed (the fold's landing: the two test-byte rulings per togo's second fold, the spec's latest event).
Files: tests/test_mcp_server_face.py:388, tests/test_service_acceptance.py:223 — one patch, two lines, zero findings, nothing else touched.
Read-back (verbatim):
- tests/test_mcp_server_face.py:388: `assert "(c, e) 0 of 1" not in payload` (the needle re-placed, the shortfall form)
- tests/test_service_acceptance.py:223: `count the run's census count 1..6, the running total); the exhausted` (the acks' running total honest at six votes)
Choices: none — both rulings fenced before/after, applied byte-exact. Gaps: none found.
Not done: the floor's instruments (test/lint/typecheck) — the coordinator's leg, never this seat's own verification.
## Reported by jikko — 2026-11-24T23:07:30Z

Step 8 of 9 — tests/test_service_auth.py landed WHOLE (NEW, 435 lines) per servingtierintegrationspec §7a's fence; nothing else touched.
The 16 arcs at the spec's names: test_no_key_refused_401_at_every_route (parametrized, the six lanes — the SAME ThreePart bytes at each, the oracle never fed) · test_wrong_key_same_401_three_fields · test_wrong_audience_same_401_mcp_never_named · test_scope_denied_403_default_deny (parametrized 2: the auditor's key at votes, the comparator's at runs) · test_right_key_route_bodies_returned · test_midflight_mint_lands_live_through_the_door · test_auth_off_degrade_six_routes_pass_bare · test_handler_lane_401_stays_401_never_500 · test_supersedes_author_mismatch_403_found_elides_the_author · test_own_author_supersede_passes · test_verified_id_wiring_body_id_ignored · test_class_stamp_overrides_the_bodys_claim · test_auth_off_class_falls_back_to_claim · test_fence_route_table_walk_every_service_route_gated (the Mounts named, the docs trio absent) · test_fence_source_scan_six_door_tokens (source.count("Depends(require_key(") == 6) · test_docs_trio_stripped_at_both_tiers.
The runtime count: the fence's 24 runtime items (16 functions + the 8 parametrize lanes — six no-key 401s + two scope denials); the floor's collected count decides.
Choices reported: arc 5 mints the llm-class six-token twin for the corroborating half (the tally gate demands >=1 human AND >=1 llm per pair and the door stamps the key's class — named in the arc's docstring); arcs 11-13 observe the durable stamp through Serialize(tmp_path).census's vote_log (the wire elides it); arc 9's second author minted as "other-holder" (the fence's _grant fixes id "key-holder" for the author); arc 1's POST lanes carry well-formed bodies (the door's 401 outcome independent of body-parse order).
Patch findings fixed same-turn: COM812 ×3, E501, PLR0913/PLR0917 at arc 4's six-arg signature (folded to four params — the expected body one dict; NO new ruling, §8 held) + pyright's Optional on dependency.call (the walk's markers comprehension); the final apply rode zero findings.
NOT done: the pytest/lint/typecheck full-floor runs — step 9's act; no other file touched.
## Reported by jikko — 2026-11-24T23:29:54Z

R11 — step 9 of 9 (the grown test files + the floor), jikko, landed:

READ-BACKS (the disk the truth):
- tests/test_web_face.py: the fixture's app.state.auth = "off" member; the nine arcs at the spec's names — test_csrf_token_minted_in_three_render_contexts, test_csrf_valid_token_passes_register_and_vote, test_csrf_drive_by_refused_write_never_lands, test_csrf_mismatched_token_refused, test_csrf_stale_secret_refused_re_render_cures, test_web_401_page_lane_key_path_never_fold, test_web_403_page_lane_scope_path, test_tier_key_rides_the_client_default_header, test_auth_off_web_calls_pass_bare — all green; the standing register/vote form arcs carry the served csrf_token (the _scrape_csrf helper); the auth-lane arcs monkeypatch web._client via _gated_client.
- tests/test_service_face.py: the fixture's app.state.auth = "off" member; the crash arc's own degrade member (the fixture-less fold arc refuses order-coupling).
- tests/test_service_acceptance.py: the boot's env={**os.environ, "AUTH": "off"} member (+ import os); the real-socket suite green under it.
- Flag 3's five docstring folds: found ALREADY on disk at the step's start (session:45, run_store:47, harness:8/:82/:103, acceptance:6/:182/:215/:221, cli:69 — all carry the grown counts) — verified, no edit made.

THE FLOOR, the three outcomes verbatim:
- TEST: "299 passed in 31.87s" — the EXACT landed count 299 (the spec's 301 the estimate; the -2 drift is the parametrize-expansion arithmetic — the true delta +6, never +8 — rides to the fold).
- LINT: "uv run ruff check src/ tests/" → "All checks passed!"
- TYPECHECK: "uv run pyright" → "0 errors, 0 warnings, 0 informations"

CHOICES (reported): the drive-by arc's expected needle asserted at the AUTOESCAPED byte ("the form&#39;s csrf_token field…" — Jinja's served form; the 403 lane's found likewise); the mid-run findings fixed SAME-TURN (import os at acceptance; the escaped needle) — never batched. The build's last step landed.
