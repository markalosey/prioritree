<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — build/web

**Route:** prioritree-ux (executing) | **Events:** 39 | **Reports:** 14

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T16:14:48Z |
| 2 | dispatch | shinko | 2026-11-22T16:33:01Z |
| 3 | dispatch | shinko | 2026-11-22T16:34:04Z |
| 4 | dispatch | shinko | 2026-11-22T16:34:11Z |
| 5 | dispatch | shinko | 2026-11-22T17:28:05Z |
| 6 | dispatch | shinko | 2026-11-22T17:28:10Z |
| 7 | dispatch | shinko | 2026-11-22T17:33:51Z |
| 8 | dispatch | shinko | 2026-11-22T17:33:59Z |
| 9 | dispatch | shinko | 2026-11-22T17:34:05Z |
| 10 | dispatch | shinko | 2026-11-22T17:34:12Z |
| 11 | dispatch | shinko | 2026-11-22T17:38:16Z |
| 12 | dispatch | shinko | 2026-11-22T17:39:13Z |
| 13 | dispatch | shinko | 2026-11-22T17:39:21Z |
| 14 | report | jikko | 2026-11-22T17:40:07Z |
| 15 | report | jikko | 2026-11-22T17:42:01Z |
| 16 | dispatch | shinko | 2026-11-22T17:42:22Z |
| 17 | report | jikko | 2026-11-22T17:52:00Z |
| 18 | dispatch | shinko | 2026-11-22T17:52:31Z |
| 19 | dispatch | shinko | 2026-11-22T17:52:39Z |
| 20 | dispatch | shinko | 2026-11-22T17:52:46Z |
| 21 | report | jikko | 2026-11-22T17:54:24Z |
| 22 | report | jikko | 2026-11-22T17:54:48Z |
| 23 | report | jikko | 2026-11-22T18:01:55Z |
| 24 | dispatch | shinko | 2026-11-22T18:02:42Z |
| 25 | report | jikko | 2026-11-22T18:03:14Z |
| 26 | dispatch | shinko | 2026-11-22T18:03:45Z |
| 27 | report | jikko | 2026-11-22T18:06:04Z |
| 28 | dispatch | shinko | 2026-11-22T18:12:20Z |
| 29 | dispatch | shinko | 2026-11-22T18:12:25Z |
| 30 | dispatch | shinko | 2026-11-22T18:12:31Z |
| 31 | report | jikko | 2026-11-22T18:13:28Z |
| 32 | report | jikko | 2026-11-22T18:13:33Z |
| 33 | report | jikko | 2026-11-22T18:13:37Z |
| 34 | dispatch | shinko | 2026-11-22T18:13:47Z |
| 35 | report | jikko | 2026-11-22T18:16:23Z |
| 36 | dispatch | shinko | 2026-11-22T18:17:47Z |
| 37 | report | jikko | 2026-11-22T18:18:14Z |
| 38 | dispatch | shinko | 2026-11-22T18:18:25Z |
| 39 | report | jikko | 2026-11-22T18:19:13Z |
## Reported by jikko — 2026-11-22T17:40:07Z

build/web steps 1-6 — the completed steps, verified at disk before this report (glob/read; the tree is the truth).

1. Zombie removal: scripts/generation/web_scaffold.py and scripts/generation/web_structure.py — glob returns no files for either; both zombies absent.

2. pyproject regions: dependencies = ["fastapi", "httpx2", "jinja2", "uvicorn[standard]"] (pyproject.toml:7); dev slimmed to ["pytest", "pyright", "ruff"] (:144); rulings placed — "src/prioritree/service.py" = ["BLE001", "PLC0415"] (:109), "src/prioritree/web.py" = ["BLE001"] (:122); [tool.pyright] include = ["src", "tests"] unchanged (:138).

3. Sync refusal, named verbatim: this pack carries no make/uv verb — the fixed-argv acts are lint/test only, so the sync was refused from this seat. The lock already carries jinja2 3.1.6 (uv.lock:211-219), so the new dep is resolved on disk regardless.

4-6. The three template batches: 14 files at web/templates/, line counts read at disk — base 19, landing 40, refuse 9, fold 12, unknown 14, sitting 12, pair 15, vote-ack 6, ack 9, state-strip 8, done 11, progress 8, result 39, halt 19.

The {% if acknowledged %} flip is present at vote-ack.html:4 — the duplicate-verdict line ("This pair was already recorded with the same answer — it stands once.") renders only on acknowledge.

Parallel count race, named: the mid-race count of 9 was a read-back artifact of the batch writes; the disk's total is 14 — glob confirms the whole set.

Gaps: none found at disk; nothing from steps 1-6 left undone.
## Reported by jikko — 2026-11-22T17:42:01Z

# Step 7 of 12 (build/web) — the static pair landed, whole.

- web/static/app.css CREATED — 27 lines, byte-exact per the spec v3's §O fence (the header comment + 26 rules: the wrap/card chrome, the pair cards, the verdict buttons, the ranked table's own styling, the three-part/refusal/state-strip surfaces).
- web/static/app.js CREATED — 24 lines, byte-exact per the spec v3's §P fence (the PtCopy Web Component + customElements.define("pt-copy") + the data-pt-path submit delegation — navigation JS, never validation JS).
- READ-BACK: both files read back from disk; app.js defines pt-copy + the data-pt-path delegation (the step's read-back bar met).
- web/templates/ counted: 14 files on disk (base + the 8 screens + the 5 fragments) — the 14 expected, zero divergence.
- NOTHING else touched this step — the pair alone landed under web/static/; no other file changed.

jikko, 2026-11-22
## Reported by jikko — 2026-11-22T17:52:00Z

Step 8 landed: src/prioritree/web.py WHOLE — the spec v3's §Q bytes (the child app, the httpx2 AsyncClient over ASGITransport with raise_app_exceptions=False, the Jinja2Templates loader seam, the nine routes, the child's own refuse/fold handlers, the UNION_LANES block, the manual form parsing — no framework 422) + §Q′'s acknowledged:true docstring flip.

READ-BACK (the dispatch's three checks, confirmed on disk): the file at 655 lines — the spec's §Q fence count; the loader's directory literal verbatim (_TEMPLATES_HOME = "web/templates", Jinja2Templates(directory=_TEMPLATES_HOME) at :121); the client's transport form verbatim (import httpx2 — the lock's name, :50 — + httpx2.ASGITransport(app=service_app, raise_app_exceptions=False), :129). Also per the spec's step-8 read-back: UNION_LANES present (:111), check_dir=False on the static mount (:120), NO web_structure import.

FOUR LINT CURES diverge from the fenced bytes, each count-neutral (ruff ALL's zero-findings law; the findings rode the patch apply): I001 (import block reorganized — httpx2 into the sorted block, the aliased service import split in two); ANN401 (json: Any | None -> object | None — the tree's wire-body precedent, votes.py/registry.py); FBT001/2 (the fold param keyword-only — every call site already passes fold= by keyword); COM812 x11 (trailing commas on the multi-line TemplateResponse closings). Post-fix apply: zero findings.

NOT done (other steps' dispatches): no service.py tail mount (step 9), no test files (steps 10-11), no floor runs — the module is inert until the mount lands. Nothing else touched.
## Reported by jikko — 2026-11-22T17:54:24Z

Step 11 done: the 405 arc re-targeted in tests/test_service_face.py per webspec v3 §W (the step-11 fenced region; the v3 fold names no §W correction, so §W's bytes stand).

- Patch applied: one hunk — the function whole at :264-272 replaced by §W's bytes; the file's line count 315 → 325.
- The arc's new target: client.get("/ui/register") — the child's own 405 surface (the POST-only register fragment route), replacing client.delete("/runs").
- The arc's intent byte-held: status 405 asserted; set(body) == _REFUSAL_KEYS; expected == "GET /ui/register"; found == "the method GET is not allowed at the path /ui/register"; "POST /ui/register" in next_action (the mounted whole's legal set).
- The docstring carries the re-target's provenance (web-brief §3e, the mount's price, the collaborator's approved amendment); the module docstring byte-untouched.
- Read-back after apply: the region :264-282 matches §W verbatim; test_refusal_unmatched_path_404 (:253-261) and test_done_200 (:285+) byte-untouched — nothing else touched.
- Patch output: APPLIED, 1 hunk, zero findings. NOT done: the floor (step 12's own dispatch) and any self-verification — the coordinator runs the instruments.
## Reported by jikko — 2026-11-22T17:54:48Z

STEP 9 LANDED (build/web, §U verbatim): service.py's tail mount — the ONE touch, nothing else.

- APPLIED: src/prioritree/service.py APPEND after :528 (the describe route's close, the file's old end) — two blanks + the 7-line comment (web-brief §3c) + `from prioritree.web import web_app` + blank + `app.mount("/", web_app)`; file now 540 lines; the six routes' bodies byte-untouched (:1-528 unmodified; the diff showed ONLY the append).
- IMPORT FORM (read-back): `from prioritree.web import web_app` at :538; `app.mount("/", web_app)` at :540; the comment names the import cycle's only legal form + the PLC0415 ruling.
- GAP FOUND, NOT TOUCHED: the patch's ruff pass fires E402 (module-level import not at top of file) at :538. The per-file-ignores ruling stands as step 2 pinned it ("src/prioritree/service.py" = ["BLE001", "PLC0415"], pyproject:109) — PLC0415 does not suppress E402 (a module-level mid-file import is E402's domain, not PLC0415's nested-scope domain). Step 12's make lint will surface this; the E402-naming is a coordinator ruling, pyproject outside this step's touch.
- web.py present (step 8) — the import target resolves. No other file touched; not verified by this hand (kensho's eyes ahead).
## Reported by jikko — 2026-11-22T18:01:55Z

Step 10 of 12 (build/web) — tests/test_web_face.py CREATED whole per the spec v3's step-10 bytes: §V whole + §V′'s four corrections (the docstring's static-pair item; test_static_pair_serves inserted after test_landing_serves — GET /static/app.css + /static/app.js, a byte each; the chain arc's fresh-cast echo-absence pin; the echo arc re-targeted).

READ-BACK (verified at disk): the file at 311 lines (the spec's composed 310 + one lint-cure line); 21 test functions + the injection fixture in the face file's own form (app.state.seam = Serialize(tmp_path); TestClient(app)); the echo arc's fragment-path form — BOTH posts through /ui/runs/RUN-0001/vote, the echo asserted on the re-send (again) alone, its absence pinned on the fresh ack (fresh).

TWO LINT CURES diverge from the fenced bytes (ruff findings rode the first apply; fixed in-turn; post-fix apply clean — zero findings): ARG001 — the fold arc's unused `client` param dropped (the face file's test_crash_envelope_500 form); EM101 — `raise RuntimeError("boom")` → the msg-variable form (the face file's :313-314 dodge).

NOT done: nothing else touched — no service.py edit (step 9's dispatch), no test_service_face.py edit (step 11), no floor runs (step 12, the coordinator's instruments; this seat never verifies its own work).

jikko, 2026-11-22
## Reported by jikko — 2026-11-22T18:03:14Z

R11 — step 11b (spec-gap cure): the spec's own mount form completed at the rulings tier. pyproject.toml line 109, the per-file-ignores entry for src/prioritree/service.py, edited one line only: ["BLE001", "PLC0415"] → ["BLE001", "E402", "PLC0415"] — E402 names the tail's mid-file web import (the import-cycle form the step-2 ruling PLC0415 already rules; the E402 companion fires on the same line), completing the step-2 rulings list the lint floor at step 12 needs. Read-back verbatim: "src/prioritree/service.py" = ["BLE001", "E402", "PLC0415"]. Nothing else touched — the ruling comment above the line untouched, no other file edited. Not done (out of this step's scope): no lint/typecheck run — the coordinator runs the instruments; step 12's floor decides.
## Reported by jikko — 2026-11-22T18:06:04Z

Step 12 floor (the three fixed-argv acts), outcomes verbatim:
1. test act (all): `9 failed, 147 passed in 27.85s` — NOT the spec's expected green 156. The first run's uv auto-sync completed the step-3 fold (stderr: Built prioritree, 1 package swapped — jinja2 minted) before the suite ran, so the failures are stable, not sync-timing artifacts.
2. lint act (check): `All checks passed!` — as spec'd.
3. typecheck act: `0 errors, 0 warnings, 0 informations` — as spec'd.

Findings (named, never fixed — no edits made):
- 7 web face form arcs fail identically (test_register_fragment_ack, test_register_fragment_share_at_quorum_2, test_register_refusal_inline_at_200, test_register_refusal_bad_quorum, test_vote_then_pair_chain, test_vote_echo_already_recorded, test_vote_refusal_pair_untouched): `AssertionError: The python-multipart library must be installed to use form parsing.` at starlette's request.form(), reached from web.py:510 (register) and web.py:607 (vote). pyproject dependencies are fastapi, httpx2, jinja2, uvicorn[standard] — python-multipart is undeclared, so the sync cannot mint it.
- 2 web face redirect arcs fail on state reads (test_sitting_done_redirects, test_done_reopened_redirects): both `assert 200 == 303` — the exhausted sitting GET and the fresh-run done GET render at 200 instead of redirecting.
- Suite size reconciles with the spec: 156 total (147+9); 135 core arcs passed; of the 21 web face arcs, 12 passed, 9 failed.
## Reported by jikko — 2026-11-22T18:13:28Z

Step 12c done — the floor-fold cure 2's test half (webspec.md event 24, region d), applied per the addendum's exact bytes.

Edits: tests/test_web_face.py only, two assertion pairs converged to the 200-carry form — :93-94 (test_sitting_done_redirects) and :120-121 (test_done_reopened_redirects) now assert `== 200` + `headers["hx-redirect"]`, mirroring the green precedent at :274-275. The 303/`location` forms are gone; the docstrings stand per the ruling.

Read-back at disk: both arcs verbatim match the addendum's cure bytes; nothing else touched (the file's other bytes, the web.py regions, the templates all untouched — regions a/b/c are NOT this half).

Not done: verification (tests/lint/typecheck) — the coordinator runs the instruments; not my own work's verifier. No findings from the patch apply itself.

Files touched: tests/test_web_face.py (4 lines changed across 2 hunks).
## Reported by jikko — 2026-11-22T18:13:33Z

Step 12a (the floor-fold's cure 1) landed: pyproject.toml line 7 replaced with the addendum's exact bytes — dependencies = ["fastapi", "httpx2", "jinja2", "python-multipart", "uvicorn[standard]"] — python-multipart slotted alphabetically between jinja2 and uvicorn[standard] (webspec event 24, DEFECT 1: the seven form arcs' sole gap was the undeclared dep; the arcs' own bytes are right).
Read-back at line 7 verbatim: dependencies = ["fastapi", "httpx2", "jinja2", "python-multipart", "uvicorn[standard]"].
Nothing else touched: one hunk applied, zero findings; the file holds at 144 lines with every other byte unchanged.
Not done here: the uv sync that mints python-multipart into the venv + lock rides the floor's own first-run auto-sync, not this step's act.
## Reported by jikko — 2026-11-22T18:13:37Z

Step 12b done — togo's floor-fold cure 2 applied to src/prioritree/web.py, four regions, nothing else touched.
Edits: (1) sitting's DONE branch :332 now `return Response(status_code=_OK, headers={"HX-Redirect": f"/runs/{stem}/done"})`; (2) done route's re-opened branch :376 now `return Response(status_code=_OK, headers={"HX-Redirect": f"/runs/{stem}"})` — both byte-identical to the pair fragment's :568 precedent.
Companions culled: the RedirectResponse import dropped (:52 now `from fastapi.responses import JSONResponse, Response`); the _SEE_OTHER constant deleted (the constants block now runs _CRASH → _FRAGMENT_LANE).
Read-back held: grep over RedirectResponse|_SEE_OTHER returns zero matches; both regions verbatim-confirmed at disk post-apply.
Not done (not this step's): the dep cure (pyproject python-multipart) and the two test-arc retargets in tests/test_web_face.py — other hands' regions. No instruments run (the coordinator verifies).
## Reported by jikko — 2026-11-22T18:16:23Z

Step 12d — the floor re-run (jikko, build/web). The three acts' outcomes verbatim:

1. Test act (all): FAILED at collection — "ModuleNotFoundError: No module named 'httpx'" at tests/test_service_acceptance.py:32; "Interrupted: 1 error during collection"; "1 error in 0.34s". Zero tests ran — the expected 156 passed was never reached.
2. Lint act (check): "uv run ruff check src/ tests/" → "All checks passed!" — matches expectation.
3. Typecheck act: "115 errors, 0 warnings, 0 informations" + "make: *** [typecheck] Error 1" — expected 0 errors, 0 warnings. All 115 errors sit in tests/test_service_acceptance.py; the root is line 32 "Import 'httpx' could not be resolved", the other 114 unknown-type cascades off it.

Finding (report item; no edits made): the anticipated venv sync DID run — .venv/lib/python3.13/site-packages carries httpx2-2.16.2 and python_multipart-0.0.34 (pyproject.toml:7 and uv.lock:168 both name "httpx2"). The gap is the import NAME, not the mint: the httpx2 dist ships its top-level module as httpx2/, and "import httpx" resolves only after httpx2's opt-in alias_httpx() is called (httpx2/_alias.py:58-71 — "Must be called before anything imports httpx"; "Libraries should never call this"). tests/test_service_acceptance.py:32 imports httpx bare, with the comment "the floor verifies the import resolves" — nothing in the process activates the alias first, so it does not resolve, and the suite dies at collection before a single test runs.

Not done: no edits (the alias-activation call is the coordinator's call — conftest or test-side); no re-runs beyond the three dispatched acts — pytest collection and pyright, two independent instruments, agree on the same root line.
## Reported by jikko — 2026-11-22T18:18:14Z

The eviction cure's one-line flip, applied: tests/test_service_acceptance.py:32 — `import httpx` became `import httpx2 as httpx`, the comment byte-untouched (togo's fenced diff, webspec event 26). Nothing else touched — patch applied clean (1 hunk, no findings), import order stays valid (httpx2 sorts before pytest at :32-33). Read-back verified line 32 verbatim: `import httpx2 as httpx  # httpx2 the lock's name; the floor verifies the import resolves`. No downstream adaptation needed — every `httpx.` usage resolves against the httpx2 module per the spec's compat confirmation. Floor runs (lint/typecheck/tests) NOT run by this seat — the coordinator runs the instruments.
## Reported by jikko — 2026-11-22T18:19:13Z

Step 12f — the floor's third run (build/web, prioritree-ux): the pack's own fixed-argv acts, in order, all matching expectation.

1. Test act (all, full suite): "156 passed in 30.62s" — 135 service + 21 web face, as expected.
2. Lint act (check): "All checks passed!" — ruff over src/ and tests/.
3. Typecheck act: "0 errors, 0 warnings, 0 informations" — the eviction's 115 typecheck errors clear at the one-line flip.

No findings outside the expectations. The floor is clean; nothing was edited.
