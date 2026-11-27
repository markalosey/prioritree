<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/numbers

**Route:** prioritree-polish (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-27T00:49:16Z |
| 2 | report | keisan | 2026-11-27T00:57:06Z |
## Reported by keisan — 2026-11-27T00:57:06Z

# THE NUMBERS LEG — keisan (計算), packet census/numbers, route prioritree-polish, 2026-11-27

The lived counts computed at the tool, every number carrying its trace line (the claims lane held: never hand-counted; the calculate instrument + the grep/glob/read/vote_query/test surfaces the only sources). tansa's counts census rides in parallel — this leg the source of truth the told counts are verified against.

## 1. THE STRUCTURAL COUNTS (src/prioritree/* at the bytes)

- **service.py's routes — LIVED 6.** Grep at the bytes: 6 route decorators — :478 @app.post(_RUNS_PATH), :507 @app.get(_NEXT_PATH), :556 @app.post(_VOTES_PATH), :605 @app.get(_STATE_PATH), :639 @app.get(_TALLY_PATH), :676 @app.get(_MANIFEST_PATH) (3 POST + 3 GET). Trace: {"op":"count","args":{"values":"[478,507,556,605,639,676]"},"result":6}. TOLD service.py:2 "the five routes REST 1:1 + the sixth query" (5+1) — DELTA 0.
- **web.py's lanes — LIVED 12.** Grep: 12 route decorators — :599 _LANDING, :623 _SITTING, :710 _DONE, :751 _PICKER, :792 _DELIBERATE, :872 _PROGRESS, :909 _RESULT, :1001 POST _REGISTER, :1059 _PAIR, :1106 POST _VOTE, :1193 _STATE_STRIP, :1217 POST _UNREMEMBER (9 GET + 3 POST). Trace: {"op":"count","args":{"values":"[599,623,710,751,792,872,909,1001,1059,1106,1193,1217]"},"result":12}. TOLD: web.py:2 "the eleven routes" — DELTA +1; web.py:8 "the eleven routes (7 pages at honest statuses + 4 rendering fragments at 200" — told 7+4=11, DELTA +1 (the lived kinds: 9 GET + 3 POST); web.py:287 "the nine web routes" — DELTA +3; web.py:527 "the nine web routes" — DELTA +3. [the honest-docs fold's four stale sites — the polish set's cure targets]
- **mcp_server.py's tools — LIVED 5.** Grep: 5 @server.tool decorators — :505 runs.register, :534 runs.next, :565 votes.cast, :616 votes.census, :628 runs.tally. Trace: {"op":"count","args":{"values":"[505,534,565,616,628]"},"result":5}. TOLD mcp_server.py:2 "the five ops as OunceMCP tools" + README:57 — DELTA 0.
- **The suite's collected count — LIVED 475 AT MY OWN RUN.** Trace (the run whole): "475 passed in 41.66s". TOLD README:61 + README:322 "475 tests green" — DELTA 0, the floor standing BEFORE any cure (the no-break proof's before-number). The test files: 24 modules (glob tests/**/*.py). Trace: {"op":"count","args":{"values":"[\"test_store_lock_face.py\",\"test_votes.py\",\"test_policy.py\",\"test_budget_curve.py\",\"test_key_mint.py\",\"test_cli.py\",\"test_key_verify.py\",\"test_service_auth.py\",\"test_service_acceptance.py\",\"test_calculate_expansion_kat.py\",\"test_service_store.py\",\"test_acceptance.py\",\"test_mcp_server_face.py\",\"test_tally.py\",\"test_web_face.py\",\"test_smoke.py\",\"test_scheduler.py\",\"test_run_store.py\",\"test_key_store.py\",\"test_session.py\",\"test_harness.py\",\"test_service_face.py\",\"test_mcp_auth.py\",\"test_registry.py\"]"},"result":24}.
- **The templates + static — LIVED 17 + 2.** Glob: web/templates/ = 17 files; web/static/ = app.js + app.css. Traces: {"op":"count","args":{"values":"[\"vote-ack.html\",\"ack.html\",\"landing.html\",\"pairs.html\",\"result.html\",\"halt.html\",\"state-strip.html\",\"fold.html\",\"sitting.html\",\"done.html\",\"refuse.html\",\"unknown.html\",\"progress.html\",\"picker.html\",\"auth.html\",\"base.html\",\"pair.html\"]"},"result":17}; {"op":"count","args":{"values":"[\"app.js\",\"app.css\"]"},"result":2}. TOLD README:56 "17 authored Jinja2 templates + 2 static files" — DELTA 0 ×2.
- **The modules' line counts.** web.py LIVED 1241 — the read tool's own count ("Showing lines 1-80 of 1241"); TOLD README:56 "1241 lines" — DELTA 0. mcp_server.py LIVED 681 ("of 681"); TOLD README:57 "681 lines" — DELTA 0. service.py LIVED 726 ("of 726") — no told form at the tree (context).
- **The package's modules — LIVED 19.** The directory read: 19 .py modules in src/prioritree. Trace: {"op":"count","args":{"values":"[\"__init__.py\",\"acceptance.py\",\"budget_curve.py\",\"cli.py\",\"key_store.py\",\"key_verify.py\",\"mcp_auth.py\",\"mcp_server.py\",\"policy.py\",\"registry.py\",\"run_store.py\",\"scheduler.py\",\"service.py\",\"service_store.py\",\"session.py\",\"store_lock.py\",\"tally.py\",\"votes.py\",\"web.py\"]"},"result":19}. TOLD pyproject.toml:28 "the fifteen modules packages carry" — DELTA +4 — a stale count BEYOND the banked set (the polish set's ground; CONTINUATION:79 the historical record's same form).

## 2. THE DEPENDENCY + FLOOR COUNTS

- **pyproject's dependencies — LIVED 7.** pyproject.toml:9. Trace: {"op":"count","args":{"values":"[\"fastapi\",\"httpx2\",\"itsdangerous\",\"jinja2\",\"ouncemcp\",\"python-multipart\",\"uvicorn[standard]\"]"},"result":7}. TOLD README:61 "Runtime dependencies: seven" — DELTA 0.
- **The floor — LIVED 475 at my own run** ("475 passed in 41.66s") — TOLD 475 (README:61/322) — DELTA 0.
- **The lock's package count — LIVED 85.** Grep over uv.lock: 85 [[package]] heads. Trace: {"op":"count","args":{"values":"[10,22,31,40,53,62,75,84,93,128,137,210,325,334,343,406,421,430,439,452,461,479,491,547,556,565,578,651,667,676,685,694,703,715,727,736,751,766,778,790,888,913,926,935,944,956,968,983,992,1001,1010,1019,1058,1080,1089,1109,1199,1214,1223,1237,1246,1259,1275,1284,1293,1309,1363,1376,1464,1479,1492,1505,1586,1611,1624,1636,1683,1692,1701,1713,1722,1731,1754,1792,1831]"},"result":85}. No current told form (CONTINUATION:10 "uv.lock (141 lines)" the birth-era historical record, superseded at the runtime-deps era).

## 3. THE TOLD-VS-LIVED TABLE (every count the polish set will touch — each cure's before/after citable to these traces)

| surface (cite) | told N | lived N (trace) | delta |
|---|---|---|---|
| web.py:2 | "the eleven routes" | 12 | +1 |
| web.py:8 | "7 pages + 4 fragments" (11) | 12 (9 GET + 3 POST) | +1 |
| web.py:287 | "the nine web routes" | 12 | +3 |
| web.py:527 | "the nine web routes" | 12 | +3 |
| pyproject.toml:28 | "the fifteen modules" | 19 | +4 [beyond the banked set] |
| README:56 | 1241 / twelve lanes / 17 + 2 | 1241 / 12 / 17 / 2 | 0 ×4 |
| README:57 | 681 / five tools | 681 / 5 | 0 ×2 |
| README:61 | seven deps / 475 floor | 7 / 475 | 0 ×2 |
| service.py:2 | five routes + the sixth query | 6 | 0 |
| mcp_server.py:2 | five ops as five tools | 5 | 0 |

THE CURE TARGETS: web.py's four stale sites (the docstring's "eleven" ×2 + the comments' "nine" ×2) + pyproject.toml:28's "fifteen" → nineteen (the new finding beyond the banked set). Every honest count verified standing at the bytes.

## 4. THE PROBE'S TOLD FORMS RE-VERIFIED (RUN-0008's final state — the living traces at one call each)

- **THE AXIS QUERY (one call):** {"op":"cell-table","args":{"run_file":"/Users/marklosey/projects/prioritree/.prioritree/runs/RUN-0008.jsonl","items":"[\"w01:river\",\"w02:meadow\",\"w03:lantern\",\"w04:harbor\",\"w05:cedar\",\"w06:ember\",\"w07:tide\",\"w08:orchard\",\"w09:willow\",\"w10:granite\",\"w11:fennel\",\"w12:thistle\",\"w13:clover\"]"},"result":{"total_votes":319,"cells":[every pair × class × presentation → count + the winners list per cell]}} — **TOTAL_VOTES 319**. TOLD README:230 "RUN-0008 completed at 319 votes" + README:322 + CONTINUATION:121/135 — VERIFIED. (The run file: 320 lines = the manifest line + 319 votes — the read tool's "of 320".)
- **m 26, k 16** (TOLD CONTINUATION:122 "the pooled flip asymmetry θ — m 26, k 16") — verified transitively: both dependent forms reproduce byte-exact at (k=16, n=26).
- **THE P:** {"op":"binom-test","args":{"k":"16","n":"26","p":"0.5","sided":"two"},"result":0.32693958282470703} → told "exact two-sided p 0.3269" — VERIFIED.
- **THE WILSON BOUND:** {"op":"wilson","args":{"k":"16","n":"26","z":"1.96"},"result":[0.42534520039420076,0.7757164048816557]} → told "Wilson 95 [0.4253, 0.7757]" — VERIFIED (the interval carries 0.5).
- **θ̂:** {"op":"divide","args":{"a":"16","b":"26"},"result":0.6153846153846154} → told "θ̂ 0.615" — VERIFIED.
- **φ̂:** {"op":"divide","args":{"a":"26","b":"155"},"result":0.16774193548387098} → told "φ̂ 0.168 — 26 of 155 classifiable cells" — VERIFIED.
- **THE NULL'S REALIZED BOUND** (the pre-registered form |θ−0.5| ≲ ±1.96·0.5/√m at the realized m=26): {"op":"multiply","args":{"a":"1.96","b":"0.5"},"result":0.98}; {"op":"sqrt","args":{"a":"26"},"result":5.0990195135927845}; {"op":"divide","args":{"a":"0.98","b":"5.0990195135927845"},"result":0.19219381243542036} → told "±0.192" (README:230/322, CONTINUATION:122) — VERIFIED.
- **THE REALIZED CRITICAL k≥19:** {"op":"binom-test","args":{"k":"19","n":"26","p":"0.5","sided":"two"},"result":0.028959274291992188} (≤ 0.05) and {"op":"binom-test","args":{"k":"18","n":"26","p":"0.5","sided":"two"},"result":0.07551869750022888} (> 0.05) → told "the realized critical k≥19 against the realized 16" — VERIFIED.
- **THE SLICES:** {"op":"binom-test","args":{"k":"10","n":"14","p":"0.5","sided":"two"},"result":0.1795654296875} → told human "10/14 … p 0.1796" — VERIFIED; {"op":"divide","args":{"a":"6","b":"12"},"result":0.5} → told llm "6/12 = 0.500" — VERIFIED.

**THE VERDICT:** the tree's told forms stand or fall at named bytes — the datum's every number verified against the living traces (the README's and CONTINUATION's told forms byte-consistent with the tool's own results: 319 at the axis query, p 0.3269, Wilson [0.4253, 0.7757], ±0.192, θ̂ 0.615, φ̂ 0.168); the polish set's count-cure targets are web.py's four stale sites and pyproject.toml:28's "fifteen" (lived 19); the floor 475 standing at my own run before any cure.
