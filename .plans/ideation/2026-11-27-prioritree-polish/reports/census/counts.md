<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/counts

**Route:** prioritree-polish (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-27T00:49:16Z |
| 2 | report | tansa | 2026-11-27T00:58:57Z |
## Reported by tansa — 2026-11-27T00:58:57Z

# THE COUNTS CENSUS — every told count in the whole tree re-read at its source (tansa, packet census/counts, prioritree-polish, 2026-11-26/27)

The claims lane held: every count below re-read at the tree's own bytes this pass, never copied from the banked records. The instruments: the 19 src modules read whole (web.py 1241 lines, service.py 726, run_store.py 989, votes.py 732, tally.py 570, cli.py 505, mcp_server.py 681, key_store.py 603, mcp_auth.py 251, service_store.py 249, session.py 380, registry.py 393, scheduler.py 106, key_verify.py 208, policy.py 89, store_lock.py 91, acceptance.py 287, budget_curve.py 246, __init__.py 2); the 17 templates + 2 static files; the 24 test files; README.md (326 lines) whole; pyproject.toml + Makefile whole; the suite fired at my own hands: **"475 passed in 42.04s"** — the floor's count verified, never copied. RUN-0008 read at its tail: 320 lines = 1 manifest + 319 votes, VOTE-0319 the last.

## 1. THE KNOWN STALE SET — EACH CONFIRMED AT ITS BYTES

- **web.py:2 — "the eleven routes"**: lived TWELVE @web_app routes (landing :599, sitting :623, done :710, pick :751, judge :792, progress :872, result :909, register :1001, pair :1059, vote :1106, state_strip :1193, unremember :1217). TOLD 11, LIVED 12, delta +1.
- **web.py:8 — "7 pages at honest statuses + 4 rendering fragments at 200"**: 7 pages ✓ lived; fragments TOLD 4, LIVED 5 (register, pair, vote, state_strip, unremember — the un-remember lane the uncounted twelfth). delta +1.
- **web.py:287 — "the nine web routes"**: _WEB_LANES :291-304 carries TWELVE entries. TOLD 9, LIVED 12, delta +3.
- **web.py:527-529 — the refuse docstring's "the nine web routes + the six service routes"** (the fold's fourth instance): nine vs 12 lived (the six ✓ at _SERVICE_LANES :305-312). delta +3.
- **service.py:557-578 — cast_vote's F8-only docstring**: names F8 (the self-claim dies) + the degrade; the lived body :581-583 carries the THREE-way branch (the web-lane digest → the body's comparator_id; no digest → the body's; verified → the record's) — the web-lane branch un-taught. CONFIRMED (doc-truth gap).
- **mcp_server.py:537 — "(every pair at quorum)"** in runs.next's tool description: the lived done condition is quorum AND corroboration (session.py:61, tally.py:528-529). CONFIRMED STALE.
- **The done-page detour**: vote-ack.html:5's else arm (the load-triggered fetch) + web.py:1082-1083 (the fragment's done-edge HX-Redirect → /done) — the no-chain deliberate vote's confirmation vanishes within the second. CONFIRMED at the bytes (the chain form's cure stands: the ack's next_url/done_url arms).
- **The calculate blemishes**: factorial's non-negative bound lives only at the refusal — the subparser help :1117 "n! in exact, arbitrary-precision int" and the docstring :418 "any n" vs the refusal :433-434 "a non-negative integer n" (log-factorial's parallel param :1191 DOES say non-negative); the make-target closing line rides the wrapper's help emission (calculate.ts:236 per the parallel legs' reads) — and the engine's own Usage :64 says "scripts/calculate.py", hikari's path, stale at this tree's .opencode/scripts/ home. CONFIRMED.
- **store_lock.py:10-12 + :45-46 — the trust comment**: "CLOSED because all writers are local, none bypasses" stated, armed by nothing in the module. CONFIRMED (the stated-vs-armed gap).
- **The template comments**: pair.html:1 names "the sitting includes it, the fragment route serves it (web-brief §4 routes 2+7...)" — the flow fix's chain carry (:12) and the deliberate lane's judge route un-named, the flow-fix folds uncited. CONFIRMED as the flow-fix's leftover. **The "THIS PAGE" copy: CURED** — sitting.html:13 + pair.html:5 both read "from this device"; zero "THIS PAGE" bytes tree-wide (the multi-user build's finding-8 cure landed; no longer a live finding).

## 2. THE HONEST TABLE — every count found (file / line / told / lived / delta)

### 2a. STALE (told ≠ lived) — the polish set's counts ground

| file:line | told | lived | delta |
|---|---|---|---|
| src/prioritree/web.py:2 | eleven routes | 12 routes | +1 |
| src/prioritree/web.py:8 | 4 fragments (7+4=11) | 5 fragments (7+5=12) | +1 |
| src/prioritree/web.py:287 | nine web routes | 12 _WEB_LANES entries | +3 |
| src/prioritree/web.py:527 | nine web routes (refuse docstring) | 12 | +3 |
| src/prioritree/run_store.py:441 | "the nine grammar fields" | TEN extraction calls :465-474 (vote_id, run_id, pair, winner, comparator_id, comparator_class, recorded_at, notes, supersedes, presentation_order); the parenthetical itself decomposes 7 cast + 2 stamps + 1 presentation = 10 | +1 |
| src/prioritree/key_store.py:17 | "Stdlib only (json, hashlib, os, pathlib, secrets, time)" — 6 modules | 7 stdlib modules lived: json, hashlib, os, **re** (:27), secrets, pathlib, **datetime** (:30); "time" NOT imported | +1 (and two names drift) |
| pyproject.toml:28 | "the fifteen modules packages carries" | 19 .py files in src/prioritree (the auth trio + mcp_auth added since the install era) | +4 |
| pyproject.toml:57-62 | "cast_vote's seven arguments" (votes.py ruling) | 8 lived (presentation_order the probe's additive eighth) | +1 |
| pyproject.toml:63-67 | "cast_vote's seven arguments" (session.py ruling) | 8 lived — session.py:326's own docstring says "the eight arguments ... the probe's instrument additive" | +1 |
| pyproject.toml:112-117 | "the seven-argument form" (service_store.py ruling) | Serialize.cast: 8 args (run_id + the seven) | +1 |
| tests/test_votes.py:2 | "the twelve named edges" | 15 test functions (the probe's 3 presentation edges uncounted) | +3 |
| tests/test_tally.py:2 | "the twelve named edges" | 25 test functions (the floor's arcs + the halt trio + the probe's edge uncounted) | +13 |
| tests/test_cli.py:2 | "the eight arcs" (enumerated 1-8) | 10 arcs lived (the probe's 2 swap arcs un-enumerated; 14 functions) | +2 |
| tests/test_run_store.py:2 | "the six named edges" | 10 test functions (the probe's 4 presentation edges uncounted) | +4 |
| tests/test_session.py:2 | "the nine named edges" | 12 test functions (amendment 22's 2 corroboration edges + the probe's 1 uncounted) | +3 |
| tests/test_registry.py:2 | "the eleven named edges" | 12 test functions | +1 |
| README.md:137 | pin "key_store.py:596-600" (the marker's three states) | the three states lived at :599-603 (the function :584-603) | pin off by 3 |
| README.md:143 | pin "key_store.py:554-578" (the typo refusal) | resolve_auth_mode lived at :557-581 | pin off by 3 |
| README.md:172 | pin "tally.py:534-548" (the gate) | the coverage gate lived at :512-546 (the raise :531-546) | pin off by ~22 |
| web/templates/vote-ack.html:1 | "the verdict restated + the embedded pair fetch" | the three-arm form lived (next_url link / done_url link + the list-ended teaching / the fetch in the else arm) — the flow fix's arms un-named | comment stale (same class as pair.html:1) |

### 2b. THE ACCURATE SPINE — told = lived, verified at the bytes

- service.py:2 "the five routes REST 1:1 + the sixth query" ✓ (6 routes; _ROUTE_TABLE :466-475 = 6 lanes); :50 "THREE PRICED RECONCILIATIONS" ✓ (3); :682 "the five-key body" ✓ (5 keys :707-713); :717-718 "the six JSON routes above" ✓.
- web.py:79 "the service's six" ✓; :123 "32 bytes / 256 bits" ✓; :168 "the 780-s card covered 1550x" ✓ (1209600/780 = 1550.77); :349 "the service's six JSON routes" ✓; :390 "a six-token grant" ✓ (SCOPE_TOKENS = 6).
- cli.py:5 "the five subcommands 1:1 on the five ops" ✓ (5+5; the key group named apart); :12 "the four typed refusals" ✓ (4 at the tuple clause :499); :141 "ALL FIVE subparsers" ✓ (5).
- votes.py:120 "sum equals 2 x total votes" ✓; :393 "4-digit zero-pad" ✓; :488 "the seven-stage chain" ✓ (stages 1-7, 4b under 4); :544 "the seven stages" ✓; run_store.py:757 "the key's members are the eight fields" ✓ (8 at votes.py:653-662); session.py:326 "the eight arguments" ✓ (8); session.py:6-7 "the five ops" ✓ (5).
- key_store.py:50 "the six scope tokens" ✓ (6); :53 the audience pair ✓ (2); :227 "one key line's six fields" ✓ (6); :425-453 "the ceremony's seven steps" ✓ (7); :435 "token_urlsafe(32) ... 43 chars" ✓ (32B=256bit, 43 chars).
- key_verify.py: the verify steps (1)-(6) ✓; :189-191 "the ONE compare point" ✓ (one hmac.compare_digest in the flow).
- registry.py:340 "the seven refusal texts" ✓ (7 distinct expected-texts at the register_run surface); scheduler.py:4 "n(n-1)/2" ✓; :61 "10 → 45, 100 → 4,950" ✓ (45, 4950).
- tally.py: the coverage gate's four legs ✓ (zero-coverage, connectivity, quorum, corroboration — :512-524); :54-56 "numerator 2·wins + 1·ties over denominator 2·comparisons" ✓ (_WIN_WEIGHT=2, _TIE_WEIGHT=1); run_store.py:444 "the six value triggers" ✓ (6 checks :475-519).
- policy.py:31-33 "the three seats" ✓ (3 ROLES); :35 "three rows over the six scope tokens" ✓ (3 rows, 6 tokens); mcp_auth.py:13-16 "the five tools' scope tokens ... five of the six SCOPE_TOKENS" ✓ (TOOL_SCOPES = 5 entries, 5 distinct tokens); :33-36 "manifest rides the SERVICE tier's sixth route alone" ✓.
- mcp_server.py:2/:6 "the five ops as five typed tools" ✓ (5 @server.tool); :18 "K=10 cap" ✓ (_HALT_CAP=10); :91 "the three per-item maps ... ~= 3,860; 4,500 ... 640 tokens (~16%)" ✓ (4500−3860=640; 640/4000=16%); store_lock.py:36-38 "the three writer tiers" ✓ (MCP, service Serialize, CLI).
- acceptance.py:8-9 "recovery >= 4/5 at noise 0.10-0.20 for n = 10-30" ✓ (Fraction(4,5); rates (0.10,0.15,0.20); counts (10,20,30)); :52-62 "the same three named seeds" ✓ (3); :73-77 "8 of 27 in-band cells" ✓ (3×3×3=27); :59 "30/sqrt(1800) ~ 0.71" ✓ (0.7071); :67-70 the 0.30-cell trio (0.8343 clears 0.8; 0.6121/0.6453/0.7336 all below) ✓; budget_curve.py:139 "B = n0 x max(quorum, len(HARNESS_JUDGE_CLASSES))" ✓ (= code :179-180).
- The tests told-true: test_scheduler.py:2 "thirteen" ✓ (13); test_service_store.py:2 "six" ✓ (6); test_key_store.py:2 "thirteen arcs" ✓ (13); test_key_verify.py:2 "nine arcs" ✓ (9); test_acceptance.py:2 "the five named edges + the matrix" ✓ (5 functions, the matrix within); test_service_auth.py:170/:233/:293/:440 "six routes / six-token / six aliases" ✓ (service.py's six require_key calls); test_calculate_expansion_kat.py:255/:261 "the seven Tier-1a ops / the five Tier-1b ops" ✓ (consistent with the 30-op registry: 6 base + 7 + 5 + 2 composites + 10 Tier-2 + shuffle + derive-seed = 30).
- The templates/static: base.html:2 "the CDN pins (Shoelace 2.20.1 + HTMX 2.0.7)" ✓ (:8-10 match); state-strip.html:1 "routes 4+9" ✓; ack.html:1 "route 6" ✓; picker.html:1 "amendment 22's web-lane fix" ✓; app.js:1 "pt-copy + the data-pt-path navigation delegation" ✓ (2 surfaces lived); app.css — no counts.
- README.md — the just-landed set ALL TRUE: :5 "51 of 54 (94.4%)" ✓ (budget-curve-record.md:65); :51 "Five tiers" ✓ (5); :55 "six routes" ✓; :56 "1241 lines, twelve lanes, 17 authored Jinja2 templates + 2 static files" ✓ (web.py = 1241 lines exactly; 12 lanes; 17 templates; 2 static); :57 "681 lines, the five OunceMCP tools" ✓ (681 lines; 5); :61/:316 "seven dependencies" ✓ (7 at pyproject.toml:9); :61/:322 "475 tests green" ✓ (my own run: 475 passed); :118 "43-char / 64-hex" ✓; :124 "AUTH ?= on (Makefile:7)" ✓; :145 "web.py:389-392" ✓; :147 "key_store.py:53" ✓; :170 "policy.py:41-47" ✓; :172 "policy.py:69-89" ✓; :174 "web.py:277 / :279" ✓; :176 "mcp_auth.py:86-94" ✓; :181 "web.py:382 / Makefile:8" ✓; :182 "key_store.py:45-48" ✓; :183 "web.py:124-125" ✓; :184 "key_verify.py:32" ✓; :196/:215 "service.py:581-582" ✓; :223 "sitting.html:10 / web.py:1217-1241" ✓; :228 "the 780-s card covered 1550×" ✓; :230 "241 of 312" + "319 votes" ✓ (RUN-0008: 320 lines = 1+319, VOTE-0319 last); :322 "the six doors / 26 of 155 classifiable cells / ±0.192" ✓ (probe.md:815: 26 of 155; the record's ±0.19 the rounded form); :118/:297 the ports 8000/8100 ✓ (Makefile :3/:5).
- CONTINUATION.md's standing counts: "475 (449+26)" ✓ (arithmetic + my run); "319 VOTES" ✓ (the file); "156 = 3 seats × 52" ✓; the historical cell counts citable to their stores (not re-derived here).

## 3. THE SURPRISES — beyond the banked set

1. **run_store.py:441's "nine grammar fields"** — the largest in-src count drift beyond the fold: ten extraction calls lived; the docstring's own parenthetical sums to ten (7+2+1) while the told number says nine. The presentation_order fold updated the parenthetical, never the count.
2. **key_store.py:17's stdlib list** — "time" told, never imported; "re" and "datetime" lived, never told. A list-count drift of the same honest-docs class.
3. **pyproject.toml's three "seven arguments" rulings** (votes.py/session.py/service_store.py) — the probe's additive eighth left all three behind while session.py's own docstring was updated to "eight" (the ruling comments and the code's docstrings now disagree).
4. **pyproject.toml:28's "fifteen modules"** — 19 lived (the auth trio + mcp_auth since the install era).
5. **Six test files' docstring counts left behind by the folds** — test_votes 12→15, test_tally 12→25, test_cli 8→10 arcs, test_run_store 6→10, test_session 9→12, test_registry 11→12: the probe's presentation edges, amendment 22's corroboration edges, and the auth floor arcs all landed without the headers' counts moving. (test_registry's +1 predates the recent folds — the twelfth function rides unnamed.)
6. **Three README auth-era line pins drifted**: key_store.py:596-600 → 599-603; key_store.py:554-578 → 557-581 (both off by exactly +3 — key_store grew above the pins); tally.py:534-548 → 512-546 (off ~22). The pins were true at the auth era; the bytes moved under them.
7. **vote-ack.html:1's comment** — "the embedded pair fetch" told; the flow fix's three-arm form lived. The same leftover class as the banked pair.html comment, at the flow fix's other touched template.
8. **A routing note (not a count error)**: cli.py:499's four-typed-refusal clause is accurate as told, but the door's FIFTH typed refusal — SupersedeRefusedError (votes.py:175, plain Exception, no VotesRefusedError parent) — rides the CLI's `except Exception` → exit 2 + traceback, while the service maps it to 403 and the MCP to PermissionDenied. A supersede author-mismatch at the CLI is taught as an unexpected crash, never the ThreePart at exit 1. Named for the synthesis's scope ruling.

## 4. THE VERDICT AT MY SEAT

The tree's told counts: **~70 verified true** (the accurate spine — the just-landed README set whole, the service/policy/key surfaces whole, the arithmetic all closing), **20 stale** (the fold's four + sixteen beyond: one in run_store, one in key_store, four in pyproject, six test headers, three README pins, one template comment, and the web.py quartet). The drift's shape is consistent: the additive folds (the probe's presentation_order, amendment 22's corroboration, the auth floor, the multi-user session) updated the bodies and the specs, left the counted headers behind. Every stale member is a one-line honest-docs cure at its source; none touches behavior; the floor stands green at my own run. The census is the ground; the cure set's ruling is the synthesis's own act.
