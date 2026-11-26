<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — validate/voter-session

**Route:** prioritree-multi-user (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-26T20:54:29Z |
| 2 | report | kensho | 2026-11-26T20:57:53Z |
## Reported by kensho — 2026-11-26T20:57:53Z

# THE VOTER-SESSION VERIFICATION (kensho, validate/voter-session, route prioritree-multi-user, 2026-11-26)

The build gate G-VOTER-SESSION's independent verify — my own instruments, my own reads, the landed bytes against the approved spec (reports/synthesize/votersessionspec.md + the fold's latest events: the T-form ruling, the lapse-copy ruling, the register-branch fence). Never the build's word. THE VERDICT: GREEN at the zero-errors/zero-warnings bar; jikko's named stale counts verified and ruled (§5), one fourth instance of the "nine" class found at my own read.

## 1. THE INSTRUMENTS — MY OWN RUNS, OUTCOMES VERBATIM
- The full suite (the tree's own Docker channel): "475 passed in 42.95s" — jikko's step-6b count CONFIRMED at my own run: 475 collected, 475 passed, zero failed.
- The lint act: "uv run ruff check src/ tests/ — All checks passed!" — zero findings.
- The typecheck act: "uv run pyright — 0 errors, 0 warnings, 0 informations" — the 0/0 bar held.

## 2. THE SPEC'S CLAUSES — THE LANDED BYTES AGAINST THE FENCES (each at my own read)
- THE REMEMBER REGION: the child mount web.py:346-361 (secret_key=_remember_secret.decode(), session_cookie="remember", max_age=1209600, same_site="lax") + the assert-guard :362-374 (the ThreePart RuntimeError, assign-first) BEFORE the static mount + templates (:375-376); the parent bypass refused — SessionMiddleware in src/ at web.py ALONE (my grep: the import :68, the mount :356, the guard's mentions; ZERO hits in service.py/cli.py/mcp_server.py/mcp_auth.py); the _boot_secret home :128-153 (the floor 32, both knobs, the ThreePart bytes at :145-152); the helpers _remembered :171-183 / _remember :186-201 (the epoch minted ONCE at identification, the five-field docstrings).
- THE TWO-ROLE SEAM: the _WEB_LANE_DIGEST marker service.py:136-149 (the module-level digest + the honest-residual comment; import hashlib at :65); the door :581-582 (the three-way shape, the non-web keyed caller's id standing); the class line :583 BYTE-STANDING — F8 HELD AT MY OWN READ: key_verify.py:198-200, votes.py:44 + :553-558, mcp_server.py:591-595 all byte-standing.
- THE EPOCH-BOUND CSRF: _mint_bound :229-247 (the ONE composition home, the SESSION's epoch read server-side, never a client echo); the guard :250-284 with the register-branch TERNARY at :274 — the fold's 20:51:56Z fence LANDED (the fence's comments at :271-273, the law byte-identical); the branches: LIVE session → the reload copy :277, EMPTY session → the lapse copy :279 (Ruling 2's winning bytes verbatim); the mint sites: the landing :619 path-bound (the pre-fill read added), the sitting :688-695 + the judge :842-849 (the three-context form), the fragment :1081-1094 (the twin, no correction form).
- THE CONDITIONAL ASK: the ONE sitting.html seam serving BOTH LANES; sitting.html:6-14 (the identity line + the correction form + the widened teaching line — "from this device", never "THIS PAGE"); pair.html:3-7 (the twin INSIDE the vote form, the hx-include retired, the hidden pair fields byte-standing :8-11).
- THE VISIBLE IDENTITY: "voting as: {{ remembered_name }}" (sitting.html:7), both lanes asserted live (test_voting_as_renders_both_lanes, green at my run).
- THE CORRECTION VERBS: the un-remember route :1184-1208 (request.session.clear() → the ENGINE's deletion cookie, HX-Redirect to the sitting); the deletion cookie asserted at the arc (:1045-1046: "remember=null" + "expires=thu, 01 jan 1970", no max-age); the change verb = the re-identification's epoch rotation (:991-1017, the old token dying, the reload taught).
- THE REGISTER PRE-FILL: landing.html:12 (the visible editable value; the anonymous landing carries none — :1084-1088); the operator claim ALWAYS the body's (web.py:1036); the register lane path-bound even sessioned (test_register_token_stays_path_bound :980-988 — the fold's branch proven at the arc that named the red).
- THE ITSDEDANGEROUS DOOR: pyproject.toml:9 (the seven, alphabetical, the bare unpinned name); the lock's entries (uv.lock:695 name, :698 the sdist, :700 the ONE wheel 16234 B, :1026 + :1044 the project block's two entries, no transitive); the import live (web.py:68 rides every suite collection — 475 green; the probe arc exercises the import boundary in a subprocess).

## 3. THE LAWS — VERIFIED LIVE
- THE LLM-CLASS CONSTRAINT: the session the HUMANS' lane — SessionMiddleware in src at web.py alone (my grep, the whole src tree); the service app's stack session-free, asserted at the parent's own bytes (test_service_lanes_never_see_a_session, green at my run); the llm votes at the stdio/tools tier byte-standing (cli.py, mcp_server.py, mcp_auth.py — no session surface anywhere); the class verification untouched at my own read of every door (key_verify F8 :198-200; votes.py:44 + :553-558; mcp_server.py:591-595; service.py:583).
- THE NEVER-LOG DISCIPLINE: web.py's ONLY log line (:389-392) names the web key's PRESENCE ("present"/"absent"), never a byte; the remember region logs NOTHING; no log line in the touched files names cookie bytes — held.
- THE CONFIGURABILITY: both secrets' env forms T-FORM confirmed (web.py:124-125: PRIORITYTREE_WEB_CSRF_SECRET / PRIORITYTREE_WEB_REMEMBER_SECRET — Ruling 1 honored at the constants AND the probe arc's citations :828); the max_age knob (:168, 14 days), the cookie's name + same_site at the mount; HttpOnly hardcoded at the engine, never a knob.
- THE ZERO-IGNORE STRICTNESS: the S603/S607 row at pyproject:225-230 in the NAMED form (the ruling comment + the single entry, the test_harness precedent's school); the web.py S105 wording grown with _REMEMBER_SECRET_ENV at :147-159 (the same ruling, no new entry); no other new ignores — the bar held.

## 4. THE DEVIATIONS — JIKKO'S NAMED SET, EACH HONEST (verified at the bytes)
- The five step-2 forms: the decode (:357 — the engine's str|Secret annotation, pyright strict); the wraps (:145-151 — the rendered message identical); the single-quoted f-string (:150 — Q003's own fix); the assign-first raises at BOTH sites (:145-152 _boot_secret, :369-374 the assert-guard — EM101/EM102/TRY003's cures); all five the tree's legal forms, semantics byte-identical to the fence.
- The ternary at the register branch (:274 — the fenced if/else tripped SIM108 + E501; the ternary ruff's own suggestion; the fence's three comments carried above; the register-branch law byte-identical).
- The probe's import form (:95 — "import prioritree.service", the standing import cycle's own law named in the comment; the refusal's ThreePart bytes asserted at BOTH T-form knobs :828-841).
- The arc-23 re-derivation (:1102-1107 — keisan's 70-94 the name-only pre-epoch price; the landed session carries the 43-char epoch; the bound re-derived 137-141 at "Mark Losey", the derivation cited at the arc).
- The step-6b same-turn cures verified: the two re-pinned CSRF arcs carry the LAPSE bytes (:559, :570 — Ruling 2's charge landed); the echo arc's second POST scrapes the pair fragment's token (:451 — §2e's note); the census read rides vote_log (:890, :898).

## 5. THE STALE-COUNTS FINDING — each verified at the bytes, each RULED
1. web.py:287 — the lanes comment's "the nine web routes" against _WEB_LANES's TWELVE entries (:291-304, the un-remember lane the twelfth). A FOURTH INSTANCE at my read: the refuse handler's docstring :527 carries the same "the nine web routes" — the same class, the same fold's charge. RULE: the honest-docs fold.
2. web.py:2 + :8 — the module docstring's "the eleven routes (7 pages at honest statuses + 4 rendering fragments)" against TWELVE (7 pages + 5 fragments: register, pair, vote, state, unremember). RULE: the honest-docs fold.
3. service.py:558-578 — cast_vote's docstring F8-ONLY (the door record's verified stamps + the degrade named; the web-lane branch :581-582 absent from the docstring's account of what rides). RULE: the honest-docs fold — the docstring grows the web-lane sentence.
NONE is the README unit's act: all four sites are in-source truths inside the unit's own landed files, their falseness misleading the next maintainer at the bytes; the README unit is the public tail, never these. All ride ONE honest-docs fold (a small patch: the two counts + the refuse docstring's count + the web-lane sentence); the findings ride G-VOTER-SESSION as evidence; none blocks the floor — doc-drift, never behavior (the suite, ruff, pyright all green at my runs).

## THE VERDICT
GREEN at the bar: the instruments green at my own runs (475 passed, ruff zero findings, pyright 0/0/0); every spec clause at its fence (the mount + the guard + the seam + the ternary + the templates + the door); the four laws held live (the class verification untouched at every door, the cookie never logged, both knobs T-form, the ignores named); jikko's eight deviations each honest at the bytes; the stale counts verified and ruled to the honest-docs fold (one fourth instance found). The RUN-0008 riding check: the deliberate judge page serves the sessioned identity (test_judge_page_fresh_get_carried_identity — the card's own lane at the arc, green at my run).

— kensho (検証), the verification whole; the disk the truth, every read at the cited bytes this pass; the ask-ceiling held (the primary act + this report + the return).
