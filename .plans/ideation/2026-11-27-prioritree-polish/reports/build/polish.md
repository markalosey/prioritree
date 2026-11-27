<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — build/polish

**Route:** prioritree-polish (executing) | **Events:** 4 | **Reports:** 2

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-27T01:34:06Z |
| 2 | report | jikko | 2026-11-27T02:08:37Z |
| 3 | dispatch | shinko | 2026-11-27T02:20:53Z |
| 4 | report | jikko | 2026-11-27T02:24:10Z |
## Reported by jikko — 2026-11-27T02:08:37Z

R11 — build/polish landed (jikko; §2's fence the spec, the R8 order held; the refused set untouched).
1. web.py: :2/+:8 "eleven routes (7 pages + 4 rendering fragments)" → "the twelve routes (7 pages at honest statuses + 5 fragment-lane routes at 200 — register, pair, vote, state_strip, unremember, the un-remember lane a POST answering HX-Redirect, never a render)" (trace {"op":"count","args":{"values":"[599,623,710,751,792,872,909,1001,1059,1106,1193,1217]"},"result":12}); "the nine web routes" REMOVED ×2 (the structure citations standing); the DONE sentence REJOINED ("...RESPONSE HEADER to the done page (core HTMX's navigation verb — no extension, no JS). The swap the query knob:..."); the boot line → "web tier key: %s (expected: the six-token grant)%s" + the absent arm "— wire PRIORITYTREE_WEB_KEY at the next boot"; :27 pin → :67; refuse_csrf + CsrfRefusedError grown to the peers' five-field form.
2. service.py: serve → "the next open pair (under-quorum or uncorroborated)"; cast_vote GROWS the web-lane sentence ("the web lane's callers — the digest match at the marker — alone ride the body's comparator_id...; the class ALWAYS the record's — the id axis alone crosses, never the class", F8 held).
3. mcp_server.py: runs.next → "the next open pair (under-quorum or uncorroborated)... until done:true (every pair at quorum AND corroborated)"; runs.register the floor named (">=1 human AND >=1 llm behind it before the tally") + "serves each open pair"; runs.tally → "Under quorum OR uncorroborated the tally SAFE-HALTs (either coverage leg's failure fires it)"; NextInput/ CastInput grown; the pins re-derived (incl. the map-missed :333→tally.py:243 + :267→service.py:291; :584→service.py:586-588 at the post-cure tree).
4. store_lock.py + service_store.py: the concurrency truth landed ("THE FLOCK'S GUARANTEE, narrowed honestly: it serializes every writer THAT COMPOSES THE SEAM — ... the CLI, the web child, the mcp doors; the LOCAL CLASS'S DIRECT REACH the standing residual...; the armed doors' verification a DIFFERENT axis (identity at the wire, never file access)"); both ride-through enumerations GROW SupersedeRefusedError; the serve re-words.
5. run_store.py: :441 "the nine grammar fields" → "the ten" (trace: 10 extractions at :465-474); :902 the serve re-word.
6. cli.py: the docstring GROWS the fifth's routing sentence (SupersedeRefusedError → the exit-2 lane; 403/PermissionDenied named); the grammar grows --swap + --presentation-order; --quorum → "coverage = quorum AND corroboration (>=1 human AND >=1 llm per pair)"; the next help "the next open pair"; :216 → "the comparator id the key stamps at the door"; the vocabulary helps ×4 (human or llm; the six scope tokens; service or mcp); the probe-era trio cured (the swap sentence; "served order (canonical or swapped)"; the presentation_order sentence).
7. key_store.py: the stdlib list → "(hashlib, json, os, re, secrets, datetime, pathlib)" ("time" struck); the absent marker → "auth: {mode} (load fail-open; doors fail-closed)" + the docstring's "every request 401ing until a mint lands"; the pins re-derived. key_verify.py: the four pins → run_store.py:77.
8. THE ENGINE (.opencode/scripts/calculate.py — authored per 1c-5): factorial "any n >= 0" + the --n help "a non-negative integer" (log-factorial's phrasing); the combination/log-combination --n/--k helps the k<=n bound ("a non-negative integer <= n") ×2 sites; the Usage path ".opencode/scripts/calculate.py". The KAT untouched; the wrapper's emission untouched (the named residual).
9. TEMPLATES: landing:14 the floor's price ("every pair also stays open until one human AND one llm stand behind it") + the two stems `required`; sitting:15 both conditions ("judgments AND corroboration"); halt's third <li> ("the second class rides at the service/MCP tier"); unknown:9 `required`. The two template comments UNTOUCHED (the detour's lane, 1c-8).
10. ARC: test_resume_stems_carry_required (the three rendered stems assert `<input name="stem" required`) + the header's page-arcs map grown.
11. pyproject: "fifteen"→"nineteen" (trace: 19 at keisan's census); the "seven arguments"→eight ×4 (the fence named three; the run_store ruling's site the same drift class — cured, named); README: :47 "quorum AND corroboration", :95 the serve condition, the three pins (:137/:143/:172), the boot/marker quotes (:140/:145/:181 — the cures' own consequences); + the cascade re-pins at the post-cure tree: the line counts (web.py 1256, mcp_server 685) + nine line-pins (:145 web.py:396-400, :174 :284/:286, :181 :389, :183/:227 :126-127, :196/:215 service.py:586-587, :223 :1232-1256, :137 key_store.py:601-605).
12. HEADERS (each re-derived, the traces: count 15/25/10/12/12, add 8+2=10): votes 15, tally 25, cli ten arcs (the two swap arcs enumerated), run_store 10, session 12, registry 12 (the twelfth named).
13. THE FLOOR: "476 passed in 39.72s" (475 standing + the arc's +1) | ruff "All checks passed!" | pyright "0 errors, 0 warnings, 0 informations".
14. DIVERGENCES named for kensho: (a) the map's key_store :342 target ":536" re-derived to run_store.py:559 (the slip against the map's own delta pattern; Persist.__init__ at :559); (b) the marker's two test pins updated (test_key_store.py:242+249, test_mcp_auth.py:282) — the pins follow the cured bytes, the floor's standing demanded it; (c) the pyproject R4 comment's "verbatim cargo" phrase now disagrees with the fence's 1c-5 "authored" ruling (the fence followed, per the exact-task law); (d) the dispatch's step-3 named the vote-ack/pair.html comments — REFUSED per §1c-8 (the detour's lane, one true landing).
## Reported by jikko — 2026-11-27T02:24:10Z

R11 — Step 1b (build/polish, jikko, 2026-11-27): the fold's four cures landed, one patch (4 files, 6 hunks), NOTHING else — the ENGINE and the KAT untouched.
CURE 1 read-back — calculate.ts:35 "the count (a non-negative integer, as a string) (factorial); the population count (a non-negative integer, as a string) (combination, log-combination); the trial count (an integer >= 1, as a string) (wilson); the trial count (an integer >= 0, as a string) (binom-test); the count (a non-negative integer, as a string) (log-factorial)"; :37 "the selection count (an integer <= n, as a string) (combination, log-combination); the success count (an integer, as a string) (wilson, binom-test)".
CURE 2 read-back — mcp_server.py:130 "the service.py:217-218" (verified at the bytes: service.py:217 `app = FastAPI(...)`, :218 `app.state.seam = Serialize(STORE_HOME)`); :267 "the service.py:291 precedent re-carried" (verified: service.py:291 `def render_refusal(`).
CURE 3 read-back — README.md:61 and :322 both "The quality floor: 476 tests green, pyright clean, ruff clean." (grep over the file: exactly two floor sites, both at 476).
CURE 4 read-back — key_store.py:17-18 "Stdlib only (hashlib, json, os, re, secrets, dataclasses, datetime, pathlib, typing)." — nine roots, matching the lived imports :24-32 read first.
FLOOR 1 — the suite: "476 passed in 39.67s" (476 expected, standing).
FLOOR 2 — ruff: "All checks passed!" (zero findings).
FLOOR 3 — pyright: "0 errors, 0 warnings, 0 informations".
FINDINGS, not fixed (out of scope): patch's tsc side-emissions name the .opencode environment's missing Node/Bun typings (shell.d.ts, _run.ts, and calculate.ts:8's pre-existing `stderr: Buffer | string` header) — none introduced by the cures (the two .describe() strings the only calculate.ts bytes touched), none in the four cures' scope to fix.
