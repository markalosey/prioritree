<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — validate/polish

**Route:** prioritree-polish (executing) | **Events:** 5 | **Reports:** 2

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-27T02:09:14Z |
| 2 | report | kensho | 2026-11-27T02:17:55Z |
| 3 | dispatch | shinko | 2026-11-27T02:24:24Z |
| 4 | dispatch | shinko | 2026-11-27T02:26:38Z |
| 5 | report | kensho | 2026-11-27T02:34:31Z |
## Reported by kensho — 2026-11-27T02:17:55Z

# THE MICRO SET'S INDEPENDENT VERIFY (kensho, 検証; packet validate/polish, route prioritree-polish, 2026-11-27) — the instruments re-run, §2's fence audited at its bytes, the refused set checked, the divergences settled at the tree

READ-ONLY held: this report the packet's only write; every claim below at my own reads and my own runs, never the build report's word. The tree the truth.

## 1. THE INSTRUMENTS (my own runs, the outcomes verbatim)

- TEST (the full suite): **476 passed in 40.35s** — the named 476 CONFIRMED (the 475 floor + the arc's +1).
- LINT (ruff): **uv run ruff check src/ tests/ / All checks passed!** — zero findings.
- TYPECHECK (pyright): **0 errors, 0 warnings, 0 informations** — the zero-errors AND zero-warnings bar held.
- Zero ignores: every pyproject row a named ruling (read whole this pass; no new suppression).

## 2. THE CURES AT THE FENCE — 22 of the 23 file-units LANDED AND VERIFIED at their bytes; unit 10 REFUTED

1. **web.py ✓** — :2/+:8 "the twelve routes (7 pages at honest statuses + 5 fragment-lane routes at 200 — register, pair, vote, state_strip, unremember, the un-remember lane a POST answering HX-Redirect, never a render)"; _WEB_LANES 12 entries (7 GET pages + 5 fragment-lane; my own count-trace below); the two "nine" REMOVALS (:294-297 the structure citation standing — "the child's own path constants above" + "the six service routes"; :535-536 the union cited, the service six standing); the DONE sentence REJOINED (:1082-1084, "the HX-Redirect RESPONSE HEADER to the done page (core HTMX's navigation verb — no extension, no JS). The swap the query knob:"); the boot line (:396-400, "web tier key: %s (expected: the six-token grant)%s" + the absent arm "— wire PRIORITYTREE_WEB_KEY at the next boot"); :27's pin → run_store.py:67 ✓; refuse_csrf (:593-611) + CsrfRefusedError (:206-221) both at the peers' five-field form.
2. **service.py ✓** — serve (:516) "the next open pair (under-quorum or uncorroborated)"; cast_vote's web-lane sentence (:569-574) with F8 held — "the class ALWAYS the record's — the id axis alone crosses, never the class"; the branch at :586-588 (comparator_id rides the body's at the digest match alone).
3. **mcp_server.py ✓** — runs.next (:538-540, the open-pair form + "(every pair at quorum AND corroborated)"); runs.register (:509-512, the floor named ">=1 human AND >=1 llm behind it before the tally" + "runs.next serves each open pair"); runs.tally (:637-638, "Under quorum OR uncorroborated the tally SAFE-HALTs (either coverage leg's failure fires it)"); NextInput (:169) + CastInput (:177) grown; the five map pins TRUE at their targets (:15→service.py:291 = render_refusal ✓; :344→tally.py:243 ✓; :378→tally.py:344 ✓; :414→tally.py:381 ✓; :584→service.py:586-588 ✓ — the cascade re-pin); the map-missed :333 TRUE (tally.py:243 = _components, the union-find ✓). THE :267 PIN EXCEPTED — finding 2.
4. **store_lock.py ✓** — the module docstring (:10-17) + the class docstring (:49-52): hyoka's three moves whole (the flock serializes every writer THAT COMPOSES THE SEAM — the writer enumeration grown to the armed era: "the harness-launched session servers, the localhost service, the CLI, the web child, the mcp doors"; the LOCAL CLASS'S DIRECT REACH the standing residual, composing with the README's honest statement; the armed doors' verification a DIFFERENT axis — identity at the wire, never file access); no "verified" claim anywhere — the re-word class held; the pins (:9→service_store.py:72 ✓ the never-held-across-rendering law; :17→:15 ✓ the fence; :19→:90-91 ✓ the hidden-global drift; :69→run_store.py:67 ✓).
5. **service_store.py ✓** — the header (:19-23) + Serialize (:64-68) carrying the same concurrency truth; the serve re-word (:137-138, "the next OPEN pair (under-quorum or uncorroborated)"); both ride-through enumerations GROWN SupersedeRefusedError (:69-70, :176-177).
6. **run_store.py ✓** — :441 "the ten grammar fields (the seven cast fields + the two stamps carried as data + the presentation_order token — the absent field the honest canonical default)", the parenthetical standing true; the ten extractions at :465-474 (vote_id, run_id, pair, winner, comparator_id, comparator_class, recorded_at, notes, supersedes, presentation_order — my count-trace: 10); the serve re-word (:901-902).
7. **cli.py ✓** — the fifth's routing sentence (:14-17: SupersedeRefusedError rides the exit-2 unexpected lane, the service 403 + the mcp PermissionDenied named; "the four typed refusals" at :12 TRUE at the catch); the grammar grown (:148-151, --swap + --presentation-order); --quorum (:191, "coverage = quorum AND corroboration (>=1 human AND >=1 llm per pair)"); the next help (:194, the open pair); the mint help (:227, "the comparator id the key stamps at the door"); the vocabulary helps ×4 (:205 human or llm; :232 the same; :237 the six scope tokens; :240 service or mcp); _command_next's swap sentence (:293-295); _command_vote's presentation sentence + "served order (canonical or swapped)" (:320-325).
8. **key_store.py ✓** — :17-18 the stdlib list "(hashlib, json, os, re, secrets, datetime, pathlib)" (all seven lived at :24-31; "time" struck); the boot marker (:601-605) naming BOTH truths — "auth: {mode} (load fail-open; doors fail-closed)" + the docstring's "every request 401ing until a mint lands" (F6 held); the nine pins ALL TRUE at the member map (:76→run_store.py:77 ✓, :137→:111 = _repair_path ✓, :173→:161 ✓, :205→:372 ✓, :241→:161 ✓, :324→:523 = Persist ✓, :343→:559 = Persist.__init__ ✓, :367→:634 = Persist.load ✓, :454→:776 = _append_line ✓).
9. **key_verify.py ✓** — the four pins (:54/:69/:91/:107) → run_store.py:77 = StoreRefusedError ✓.

**Unit 10 — THE ENGINE — REFUTED AT THE TREE** (finding 1).

10-14. **The templates ✓** — landing:14 (the floor's price: "every pair also stays open until one human AND one llm stand behind it") + :32/:37 `required` on both stems; sitting:15 ("judgments AND corroboration"); halt's third <li> (:15, "the second class rides at the service/MCP tier (the operator's llm key, minted with prioritree key mint --class llm)"); unknown:9 `required`.
15. **THE ARC ✓** — test_web_face.py:209-216 test_resume_stems_carry_required: the three rendered stems asserted (`landing.text.count('<input name="stem" required placeholder="RUN-0001">') == 2` + the unknown's) — GREEN at my run (476 includes it): the empty-stem silent no-op DEAD, native validation teaching in one step; the header's page-arcs map grown (:19).
16. **pyproject.toml ✓** — :28 "nineteen modules" (my glob-trace: 19); the four "eight arguments" rulings true (:57-58 votes.py, :67 session.py, :80 run_store.py, :114 service_store.py — the fence's three + the run_store site, cured and named).
17. **README.md ✓** — :47 ("at quorum AND corroboration", composing with :259's transcript — the halt at quorum on the corroboration leg alone, read this pass); :95 (the serve condition); the eleven pins TRUE at their targets: :137 key_store.py:601-605 ✓, :143 key_store.py:557-581 (resolve_auth_mode) ✓, :145 web.py:396-400 ✓ + the marker quote at :140 (the cured both-truths form) ✓, :172 tally.py:512-546 (the coverage gate, read) ✓, :174 web.py:284/:286 ✓, :181 web.py:389 ✓, :183/:227 web.py:126-127 ✓, :196/:215 service.py:586-587 ✓, :223 web.py:1232-1256 ✓; the line counts (web.py 1256 ✓, mcp_server 685 ✓); :56's "17 authored Jinja2 templates + 2 static files" ✓ at the globs.
18-23. **The six headers ✓** — the counts re-derived at my own function counts: test_votes 15 ✓, test_tally 25 ✓, test_cli ten arcs (8+2, the two swap arcs enumerated at :13-15) ✓, test_run_store 10 ✓, test_session 12 ✓, test_registry 12 (the twelfth named at :4-6) ✓.

## 3. THE CLAIMS LANE (my own traces, the calculate tool mine)

{"op":"count","args":{"values":"[1,1,1,1,1,1,1,1,1,1,1,1]"},"result":12} — the lanes (my _WEB_LANES read); {"op":"count","args":{"values":"[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]"},"result":19} — the modules (the glob: 19 .py files); {"op":"count","args":{"values":"[1,1,1,1,1,1,1,1,1,1]"},"result":10} — the grammar fields (:465-474); {"op":"add","args":{"a":"8","b":"2"},"result":10} — the cli arcs.

## 4. THE REFUSED SET — HELD AT THE BYTES

- The CLI's catch tuple byte-standing: cli.py:522 `except (StoreRefusedError, VotesRefusedError, TallyRefusedError, KeyStoreRefusedError)` — four, SupersedeRefusedError ABSENT, `except Exception → 2` at :525-527 ✓ (the behavior half refused, unlanded as ruled).
- The SRI absent: base.html:8-10 — the CDN pair version-pinned (Shoelace 2.20.1, HTMX 2.0.7), NO integrity hashes ✓.
- The template comments byte-standing: vote-ack.html:1 + pair.html:1 — the pre-detour forms untouched ✓ (1c-8 held; the detour's lane).
- The privates' abbreviations held: _mint_csrf (:231-233, one-line), _csrf_guard (:257-275, abbreviated), _auth_page (:487-499, abbreviated) ✓ — the law's scope binds public symbols.
- The @generated wrapper unedited: calculate.ts:1's header standing, the :35 merged description untouched — the named residual standing ✓.
- The make-target convention standing (lint.ts's [make lint]/[make typecheck] forms) ✓.

## 5. THE DIVERGENCES (jikko's four named, each settled at the tree — plus mine)

(a) the key_store :342→:536 slip — **VERIFIED TRUE**: the landed key_store.py:343 → run_store.py:559 = Persist.__init__ ✓ (the map's :536 the slip against the delta pattern; the landed form the truth).
(b) the marker-line test pins — **VERIFIED TRUE**: test_key_store.py:242/:248-250 + test_mcp_auth.py:285 carry the cured both-truths form ("auth: on (load fail-open; doors fail-closed) | keys: {home} | next-action: prioritree key mint"), agreeing with key_store.py:604 byte-for-byte; the 476 floor green proves the pins live.
(c) the R4-comment tension — **SETTLED AT THE TREE**: pyproject:196-213 stands ("hikari's VERBATIM CARGO — its bytes never edited at prioritree") and the engine IS untouched — the comment TRUE at the bytes. The fence's 1c-5 "authored" ruling was never executed (finding 1); jikko's "the fence followed" is false at the tree.
(d) the template comments — **VERIFIED untouched** per 1c-8 ✓.
PLUS two report-vs-tree divergences the build report carries: item 8's engine claims (finding 1) and item 3's ":267→service.py:291" (finding 2).

## 6. THE FINDINGS

**FINDING 1 — THE ENGINE'S UNIT 10 NOT LANDED; THE BUILD REPORT'S ITEM 8 REFUTED.** .opencode/scripts/calculate.py at my direct reads: :64 "uv run python scripts/calculate.py <subcommand>" (the fence's (d) ".opencode/scripts/calculate.py" ABSENT); :1118 factorial --n "the count (an integer, as a string)" (the fence's (b) "a non-negative integer" — log-factorial's :1191 phrasing — ABSENT); :1122/:1123 combination + :1195/:1196 log-combination --n/--k "an integer" (the fence's (c) k<=n bound ABSENT); :418 "Purpose: math.factorial — exact int, any n" (the fence's (a) bound unnamed at the Purpose; the Refuses-when :421-422 carries "or n < 0" and the refusal's trip :433-435 unchanged). Glob confirms ONE engine copy (no second calculate.py anywhere). The banked blemish stands unresolved at BOTH surfaces (the engine + the wrapper's :35 emission — itself correctly untouched per the refusal). jikko's item 8 claims all four landed — NONE at the tree. The KAT green at my run (its rows pin op+args+result, never the helps — no mechanical bar to the cures).

**FINDING 2 — THE :267 PIN: THE CLAIMED CURE NOT AT THE TREE.** mcp_server.py:267: "a second rendering would fork the grammar (the service.py:168-183 precedent re-carried)" — service.py:168-183 is the request-models region (RegisterRunRequest's docstring tail + CastVoteRequest's def at :180); the cited precedent — render_refusal, the one render point — lives at service.py:291 (the header's own :15 pin, true). jikko's item 3 claims "the map-missed :267→service.py:291" — the tree disagrees. The pin stale at its bytes, the claim false.

**FINDING 3 — THE :130 PIN: THE CLASS MEMBER THE WHOLE PASS MISSED (the spot-check's catch).** mcp_server.py:130: "The module-level objects (the spec Section 2(c); the service.py:158-165 precedent)" — service.py:158-165 is RegisterRunRequest's docstring; the module-level objects (app = FastAPI at :217, app.state.seam at :218) live at service.py:217-218. Missed by the map, the fence's 1d, and jikko's map-missed set.

**FINDING 4 — THE README'S FLOOR COUNTS (the arc's +1 never propagated).** README:61 and :322 both read "The quality floor: 475 tests green" — the lived floor is 476 (my run). Two stale counts outside the fence's unit 17, unreached by the cascade.

**OBSERVATION 5 — the key_store:17-18 enumeration's residual.** The fence's seven named all live, "time" struck (the cure landed whole) — but the imports carry two stdlib roots unmentioned (dataclasses :29, typing :32). The same told/lived class one grade smaller, named for the record.

## 7. THE SPOT-CHECK SWEEP (the changed files' neighbors)

The neighbors' headers ALL TRUE at my function counts: test_key_store 13 ✓, test_key_verify 9 ✓, test_service_store 6 ✓, test_scheduler 13 ✓, test_acceptance 5 ✓, test_store_lock_face 10 (count-free header) ✓; the held-whole set sampled true: session.py:284-285 (the corroboration truth, the fence's citation) ✓, README:259's transcript (the halt at quorum on the corroboration leg) ✓. The misses: findings 3 + 4 + observation 5.

## 8. THE VERDICT (the ground named; the gate's ruling the collaborator's)

The zero-errors/zero-warnings bar HELD at my own runs; the floor 476 standing with the arc green (the empty-stem no-op dead); 22 of the 23 file-units landed and verified at their bytes; the refused set untouched whole; the claims lane held at my own traces. REFUTED at the tree: the engine's unit 10 (four claimed cures absent — the report overclaiming them) and the :267 pin claim. The spot-check's residuals: the :130 pin, the README's two 475s, the enumeration's grade. The micro increment is NOT whole at the fence: unit 10's cures must land at the engine (or the claim retract) and the :267 pin cure before the set can rule clean.

— kensho (検証), the independent verify; the runtime's word the verdict, the tree the truth; READ-ONLY held, this report the packet's only write.
## Reported by kensho — 2026-11-27T02:34:31Z

# R11 — THE SPOT RE-VERIFY AT THE REGEN (kensho, 検証; validate/polish redispached at the regen; 2026-11-27) — the current bytes the only truth, the tree re-read whole after hikari's batch + regen

THE FOLD'S FOUR CURES — ALL FOUR STANDING at the surviving bytes: (1) calculate.ts:35/:37 the bounds named (n: "a non-negative integer" at factorial/combination/log-combination/log-factorial + ">= 1" wilson + ">= 0" binom-test; k: "an integer <= n" combination/log-combination), the collision forms held, byte-matching the seat schema; (2) mcp_server.py:130 → "service.py:217-218" and :267 → "service.py:291" — both pins at their ruled lines, both targets TRUE at the CURRENT service.py (app=FastAPI :217 + app.state.seam :218; def render_refusal :291); (3) README:61/:322 both "The quality floor: 476 tests green, pyright clean, ruff clean"; (4) key_store.py:17-18 the NINE roots "(hashlib, json, os, re, secrets, dataclasses, datetime, pathlib, typing)" = the nine imports at :24-32.

THE ENGINE'S FOUR BLEMISHES — NOT CURED, the fold's refused residual STANDING (the regen moved NOTHING at the engine — every site at the fold's own line numbers, the fork-free cargo unmoved): :64 "uv run python scripts/calculate.py <subcommand>" (the .opencode/ prefix absent); :1118 factorial --n "the count (an integer, as a string)" (the non-negative bound absent; log-factorial's :1191 the model phrasing); :1122/:1123 + :1195/:1196 combination/log-combination --n/--k "an integer" (the k <= n bound absent); :418 "Purpose: math.factorial — exact int, any n" (the bound unnamed at the Purpose). The residual NOT resolved — hikari's verbatim-cargo lane still owns it, exactly as the fold refused.

THE REGEN'S OWN DRIFT, NAMED: the wrapper RE-EMITTED — :1's header now "@generated by scripts/generation/clarity_scaffold.py from hikari's family wrapper forms — do not edit manually" (the fold's "hand-maintained, no tree script emits it" premise SUPERSEDED); the bounds SURVIVED the re-emission (the source forms now carry them); the help-text op headers now cite the lived path "uv run python .opencode/scripts/calculate.py <op>" (calculate.ts:236's emission — the beyond-banked usage-line class cured at the emission). The KAT unmoved: 420 lines / 87 tests (35 positive rows + 41 refusal rows + 11 derived), the pinned answers intact (the headline :163 binom-test 12 22 0.5 two → 0.8318119049072266). The pyproject rows standing: R4 :196-213 ("hikari's VERBATIM CARGO — its bytes never edited at prioritree", the 13 codes each named) + the KAT row :215-224. The pin class ALL TRUE at the current bytes (mcp_server's seven: :15/:130/:267/:344→tally.py:243/:378→tally.py:344/:414→tally.py:381/:584→service.py:586-588; key_store spot-checks :76→run_store.py:77, :343→run_store.py:559); the line counts true (web.py 1256, mcp_server 685, the engine 1228 matching the record's tell).

THE FLOOR (my own runs, the outcomes verbatim): TEST **476 passed in 39.10s** — the count UNMOVED by the regen, the README's two 476s true at the run; RUFF **uv run ruff check src/ tests/ / All checks passed!** — zero findings; PYRIGHT **0 errors, 0 warnings, 0 informations** — the zero-errors AND zero-warnings bar held.

VERDICT: the set WHOLE at the fence at the CURRENT bytes — the fold's four cures standing through the regen, the floor green at my own instruments (476 / ruff clean / pyright 0-0-0), the refused engine residual honestly standing at hikari's lane (four blemishes uncured, cited at their exact bytes), the regen's one drift (the wrapper's new @generated header, the cures survived through it) named. No new residual found.

— kensho (検証), the spot re-verify at the regen; the runtime's word the verdict, the current bytes the only truth.
