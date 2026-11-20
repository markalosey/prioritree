# discover/tool-grants — the tool-grants unit's assessment census (raw-first)

## Provenance

| field | value |
|---|---|
| seat | tansa (探査, discover) — packet `discover/tool-grants`, route `prioritree-birth`, unit `build/tool-grants` |
| date | 2026-11-19 |
| method | measure at source, cite every claim at path:line — direct file reads across four trees (hikari, prioritree, tane, kepric-input) + one read-only corpus scan (`content-query exact`, hikari's own index) to locate `KUMI_BUILTIN_UNIVERSE`. **Zero web calls** (the ruling's own line — "no web search for discover" — honored under either reading: this census measured at source only). |
| boundary held | read-only by design — zero writes, zero store mutations, zero filings, zero friction writes, zero hikari-prod calls; reads and citations only |
| session binding set (the session-start law) | Visible MCP surface, enumerated verbatim: `hikari-prod_query_capabilities`, `hikari-prod_query_entity_capabilities`, `hikari-prod_query_genesis`, `hikari-prod_render_deliverable`, `hikari-prod_run_macro`, `hikari-prod_run_query`, `hikari-prod_validate_query`. Reconciled against the pin (kumi-manifest.yaml:812-836): 7 of the 9 `hikari-prod_*` ids visible; `hikari-prod_graph_ego_batch` and `hikari-prod_query_membership` ABSENT; all 9 `hikari-local_*` ids ABSENT (the hikari-local server not connected in this session); `sequential-thinking_sequentialthinking` ABSENT. Binding role per the carriage (kumi-manifest.yaml:808-810): hikari-prod = deploy-corollary — not used in this census (0 calls). Harness-side tools (out-of-band, the pin cannot reach them): read, glob, calculate, content-query, friction, inspect, test, web + list_mcp_resources / list_mcp_resource_templates / read_mcp_resource. The unearned set honored: code-graph-context, edit, etl, junro, reflect, script, symbol-lookup, write — all absent from the surface. |

---

## §0 — The ruling assessed for (verbatim)

> "We already have issues we need to solve. We do not have the tools we need to build the system properly. no web search for discover. etc... we need to have a proper assessment of the tools needed and provide them. We know what earned as a baseline."
> — the collaborator's ruling, 2026-11-19, recorded at `.plans/ideation/2026-11-19-prioritree-birth/.junro/junro.json:474` (the tool-grants lane amendment)

The unit composed in response: `build/tool-grants` under `G-TOOL-GRANTS` (junro.json:109-134), the per-each pipeline (assessment census → pricing → brief → the collaborator's grant-set ruling at `G-TOOL-GRANTS-BRIEF` → adapter+wrapper build → kensho's verification), with the gate's four conditions at junro.json:267-274.

---

## §1 — The earned baseline (the floor): hikari's current packs + evidence

### 1.1 What exists as wrappers at hikari (the registration inventory)

`.opencode/tools/` — 27 entries: acquire.ts, calculate.ts, code-graph-context.ts, content-query.ts, curate.ts, dev.ts, docker.ts, duckdb.ts, etl.ts, friction.ts, git.ts, graph.ts, help.ts, inspect.ts, junro.ts, langfuse.ts, lint.ts, manifest.yaml, patch.ts, reflect.ts, regen.ts, script.ts, symbol-lookup.ts, test.ts, testdata/, tool-redirect-map.generated.ts, web.ts.

The tool definitions (`.opencode/tools/manifest.yaml`), 24 domain tools: web (:404), lint (:492), test (:584), dev (:628), etl (:722), langfuse (:929), script (:1076), graph (:1145), docker (:1205), duckdb (:1294), help (:1368), symbol-lookup (:1394), code-graph-context (:1435), content-query (:1491), friction (:1571), patch (:1909), git (:2021), junro (:2269), reflect (:2850), calculate (:2900), curate (:3033), acquire (:3099), inspect (:3186), regen (:3269) — plus the builtin pack-projections write/edit (:313-354).

### 1.2 Per-seat earned rows (pack + lineage evidence + the unearned lists)

All from `/Users/marklosey/projects/kepric/hikari/.opencode/agent/kumi-manifest.yaml`. Every hikari pack carries the shared base: glob, friction, test, calculate, content-query (the Q-CALC-1/Q12 rows — e.g. tansa's at :475-479).

| seat | earned pack beyond the shared base | lineage evidence rows | unearned (the explicit DENY) |
|---|---|---|---|
| tansa | inspect [file,samples,count] (:480); **web [search,extract,research,lookup]** — granted 2026-10-01 (:481); the hikari MCP set, 7 tools (:482-488) | PF-1 write 156 + edit 37 (:176); **PF-3 web CONFIRMED (258 calls — the scout profile is SEARCH+FETCH)** (:177); etl DROPPED, zero calls (:178) | etl, symbol-lookup, code-graph-context, junro, write, edit, reflect, script (:489) |
| rikai | — (base only) | **PF-3 web CONFIRMED (32 calls** — external library mechanisms) (:198); etl DROPPED (:200) | **etl, web**, code-graph-context, symbol-lookup, junro, write, edit, reflect, script (:497) |
| togo | — (base only) | PF-1 write 524 + edit 400 — 71% of domain calls; DocWriter 4,092 (:220-221) | junro, write, edit, reflect, script (:504) |
| shindan | inspect [file,samples,count] (:511) | PF-7 citation-scope note; write 2,551 + edit 686 (:240-241) | etl, junro, write, edit, reflect, script (:512) |
| keikaku | **junro — the composition lane, 11 route ops** (add-question, set-question, add-ruling, add-increment, amend-increment, add-gate, close-gate, compose-stage, record-amendment, set-checkpoint-ruling, set-route-status) — "Q-SEATS-1's composition-lane ruling (2026-09-29): keikaku writes junro, that is its entire purpose" (:518) | PF-4 taskops 1,504 of 8,464 — the strongest single confirmation (:260); write 299 + edit 186 (:261) | write, edit, reflect, script (:520) |
| jikko | patch [apply] (:527); curate [apply] (:528); **lint [file, typecheck_file]** — RE-GRANTED 2026-10-26, amendment 40, on FR-MEM-0149's record (:530); etl (:531); acquire (:532); regen [generate-tools] (:533) | **ALL FOUR seeds CONFIRMED — the best-evidenced row in the pass: lint 4,412 / script 376 / test 453 / etl 91** (edit 6,843 + write 2,588 besides) (:280); web lookup — heaviest context7 user was an implementer (:281) | web, duckdb, junro, write, edit, reflect, script (:534) |
| kensho | etl [run,nodes,normalize_dataset,verify_dataset,battery] (:542); acquire (:543); docker [logs,restart,status] (:544); regen (:545) | **lint CONFIRMED (598)**, test CONFIRMED (201), etl present (6) (:301) | **lint**, duckdb, junro, write, edit, reflect, script (:546) |
| hyoka | — (base only) | langfuse THIN (20 calls) (:321); the first pack-differentiation warning (:322) | langfuse, junro, write, edit, reflect, script (:553) |
| hansei | — (base only) | langfuse RULED as hansei's instrument (100%) (:343); edit 177 + write 105 (:345) | langfuse, junro, write, edit, reflect, script (:560) |
| moho | the hikari MCP set, 7 tools (:566-572) | the blind-seat ruling (2026-09-22) (:365); the first ruled MCP grant class (:366) | junro, write, edit, reflect, script (:574) |
| shinko | friction + union (:577); **web** — granted 2026-10-01, "the facilitator's web search; tansa's SEARCH+FETCH profile precedent" (:580); **patch [apply]** (:581); **git [sync,drift,land,discard,move,unshroud]** — amendment 25, the landing instrument restored at the convenor's seat (:582); task (the primary marker) (:583); question (:584); junro — the FULL governed surface, 18 ops incl. packet + query (:586); the read-only hikari MCP trio (:588-589); docker (:590); regen [kumi-generate, permission-land] (:591) | the convergence ruling 2026-09-28 (:387) | script (:592) |

---

## §2 — The landed state (the gap): prioritree's adapter, emission, wrappers

### 2.1 The adapter (`hikari/scripts/generation/sources/prioritree-seats.yaml`)

The packs block (:314-360): shinko = task/question/friction/junro (:315-324); the `&read_pack` anchor at tansa = friction/read/grep/glob/test/calculate (:325-340); rikai/togo/shindan/**keikaku**/suisen all `*read_pack` (:341-345); jikko = `<<: *read_pack` + patch + curate (:346-355); kensho/keisan/hyoka/hansei/moho `*read_pack` (:356-360). Structural facts only, per the containment ruling (:11-18).

### 2.2 The emission (`/Users/marklosey/projects/prioritree/opencode.json`)

Builtins disabled (:4-12); 13 seat blocks; shinko primary (:324) with the roster-derived task map (:346-361) and junro allow (:338); jikko patch allow (:99) + curate allow (:89); **keikaku junro: deny (:131)**; tansa web: deny (:432); the tavily/context7 MCP servers disabled (:475-482). The closed-world deny is derived from the packs against `KUMI_BUILTIN_UNIVERSE` (clarity_scaffold.py:586-588).

### 2.3 The wrapper set (`/Users/marklosey/projects/prioritree/.opencode/tools/` — 7 files) + the engines (`.opencode/scripts/` — 5 files: calculate.py, curate.py, friction_ledger.py, patch.py, test_runner.py)

- `_run.ts` — runArgv, the explicit-argv channel via Bun.spawn, **FR-MEM-0145's durable fix** (:1, :7, :24-58)
- `junro.ts` — the cross-project form: `uv run --project /Users/marklosey/projects/kepric/hikari python /Users/marklosey/projects/kepric/hikari/scripts/junro/junro.py` (:97, every op), the prioritree ownership stamp (:1)
- `patch.ts`, `test.ts`, `calculate.ts`, `curate.ts`, `friction.ts` — prioritree-owned stamps (:1 of each; e.g. patch.ts:1, test.ts:1), runArgv channel; test invokes `uv run python .opencode/scripts/test_runner.py` (test.ts:36, :41)

The prioritree Makefile floor: dev (:5-6), test (:8-9), **lint (:11-12), typecheck (:14-15)** — whole-tree targets only; no per-file targets.

### 2.4 A measured anomaly (reported, not ruled): togo's emitted web grant

The emitted opencode.json carries **"web": "allow" and "webfetch": "allow" at togo** (:466-467) — the only seat so granted. The adapter gives togo `*read_pack` only (prioritree-seats.yaml:342); no ruling on the store grants togo web (the store's amendments, junro.json:287-493, carry none); the generator derives deny for any pack-unlisted universe id (clarity_scaffold.py:586-588). A fresh regen from today's adapter therefore derives togo web: deny — the on-disk allow fails the rot detector's byte-compare (clarity_scaffold.py:683-706) until re-emitted. The tool-grants re-emit resolves it mechanically (G-TOOL-GRANTS condition 3, junro.json:272): either togo's web becomes a ruled pack row with its citation (condition 1, junro.json:270) or the drift cures at the re-emit. **The collaborator's stopgap amendment (2026-11-19) names the hand-edit; the seat-level read locates the allow at togo's block (:466-467) with tansa still deny (:432-433) — the re-emit's ruled form resolves either way.**

### 2.5 The per-seat gap (what hikari's seat holds that prioritree's seat lacks)

| seat | hikari holds (beyond prioritree's) | candidate for the product effort? |
|---|---|---|
| tansa | content-query, inspect, **web**, the hikari MCP set | **web — YES** (§4.1); content-query/inspect/hikari-MCP — no (no corpus, no data/ plane, no domain plane at prioritree; Q-harness: "NONE of hikari's domain plane rides", junro.json:532) |
| rikai | content-query | web question priced at §4.5; content-query — no |
| togo | content-query | no candidate found beyond the base |
| shindan | content-query, inspect | no (no data plane) |
| keikaku | content-query, **junro (the composition lane)** | **junro — YES** (§3, §4.3) |
| suisen | content-query | no candidate found |
| jikko | content-query, **lint**, etl, acquire, regen | **lint — YES** (§4.2); etl/acquire/regen — no (hikari-domain instruments) |
| kensho | content-query, etl, acquire, docker, regen | no candidate beyond the base — kensho's instrument (test) is in the fixed five; hikari's own baseline DENIES kensho lint (kumi-manifest.yaml:546) |
| keisan | content-query | no |
| hyoka | content-query | no |
| hansei | content-query | no |
| moho | content-query, the hikari MCP set | no (no domain plane) |
| shinko | friction-union, **web**, **patch**, **git** (amendment 25), content-query, the read-only MCP trio, docker, regen | **patch — YES** (§4.4); **web — priced** (§4.4); **git — the landing-rule option** (§4.4, §7); docker/regen/MCP — no (hikari-domain) |

A structural delta, measured: prioritree's packs carry `read`/`grep` as pack rows (prioritree-seats.yaml:327-329, the tane shape) while hikari's packs do not (read is the universal_read projection, kumi-manifest.yaml:746-747; grep retired at hikari by Q14, kumi-manifest.yaml:463-465) — the derived-tree universe keeps both (clarity_scaffold.py:320-321).

---

## §3 — The under-delivery (the load-bearing defect): keikaku's composition lane

**The ruling**: Q-harness (collaborator ruling 2026-11-19): "…junro+task at shinko (the convenor holds the effort's records); **keikaku holds the composition-lane route ops per Q-SEATS-1**…" — junro.json:532 (ruling text; resolution at :537). Hikari's earned baseline encodes it: keikaku's junro row, "keikaku writes junro, that is its entire purpose" (kumi-manifest.yaml:518). Prioritree's own seat prompt carries the act: "Compose the route through the junro machinery — stages, increments, gates, questions" (prioritree-seats.yaml:164).

**The landed adapter**: `keikaku: *read_pack` — NO junro (prioritree-seats.yaml:344); the emitted permission map denies it (opencode.json:131).

**The consequence**: the next effort (prioritree-core — the product, named at G-BIRTH-RECORDS condition 3, junro.json:249; its open questions Q-problem-space/Q-granularity/Q-solution-space at junro.json:559-572) cannot be composed seat-side: keikaku's act at prioritree is route composition through the junro machinery, and the seat holds no instrument for it. The wrapper already exists (junro.ts — the cross-project form, engine stays home at hikari via `--project`, per the collaborator's ruling at junro.json:445 and the wrapper's own bytes, junro.ts:97). G-TOOL-GRANTS condition 4 mandates the cure: "The under-delivered keikaku composition lane cured in bytes (Q-harness's ruling lands in the adapter's packs)" (junro.json:273).

---

## §4 — The product build's needs (per seat, priced against the pipeline the birth just ran)

### 4.1 tansa — the prior-art census needs SEARCH+FETCH (the web tool)

The product effort's discover leg is the prior-art census over the pairwise-comparison field (TrueSkill, Elo, Bradley-Terry, LLM-as-judge) — external facts, the SEARCH+FETCH profile. The earned baseline: **tansa web CONFIRMED, 258 calls** (kumi-manifest.yaml:177); the hikari grant: web [search, extract, research, lookup], granted 2026-10-01 (:481). The landed state: tansa web deny (opencode.json:432) — the ruling's own named gap ("no web search for discover", junro.json:474).

**The wrapper, measured** (`.opencode/tools/web.ts`, 335 lines): handwritten (:1), self-contained — no engine script, no make target, no project/cwd resolution; four ops (:4); per-op timeouts (:7-12); implemented over in-wrapper `fetch` with AbortController (:25) — **NOT Bun.$ and NOT runArgv: no shell channel at all**, so the FR-MEM-0145 class does not apply to this wrapper.

**The env reads, measured**: `TAVILY_API_KEY` — read at :92 (search), :133 (extract), :178 (research); `CONTEXT7_API_KEY` — read at :204-207 (lookup, the X-Context7-Api-Key header). A missing key returns an honest error string naming it ("Error: TAVILY_API_KEY not set in environment.", :93; the CONTEXT7 form at :205). No .env file loading — the keys must ride the process env the opencode session inherits (the collaborator's shell). The API endpoints are called directly (api.tavily.com, :96/:146/:181; context7.com, :217/:236) — no MCP dependency: prioritree's disabled tavily/context7 MCP entries (opencode.json:479-481) do not affect the wrapper.

### 4.2 jikko — write-then-validate needs the lint instrument

The earned baseline: **the best-evidenced row in the pass — lint 4,412 lineage calls** (kumi-manifest.yaml:280); the hikari grant: lint [file, typecheck_file], re-granted at amendment 40 on FR-MEM-0149's record — "the write-then-validate discipline's typecheck leg returns to the author's seat (the patch tool's rode-along is ruff-only, structurally blind to type errors)" (:530). The landed state: jikko holds patch+curate only (prioritree-seats.yaml:352-355); no lint wrapper exists at prioritree (the 7-file set); `lint` is absent from the derived-tree universe (clarity_scaffold.py:312-337).

**Hikari's wrapper, measured** (`.opencode/tools/lint.ts`): @generated (:1), the **make-target invocation class via Bun.$** (:33) — `make lint` / `make format` / `make typecheck` / `make lint-file F= WHERE=` / `make typecheck-file` / `make lint-makefile` (:37-58), with the docker|local location axis (:29-30; the docker default mounts the main clone — manifest.yaml:493). Hikari's form is Docker-shaped; **prioritree has no Docker and its Makefile carries host-side whole-tree `lint` and `typecheck` targets only** (Makefile:11-15) — the derived form is a runArgv wrapper over the host targets (never Bun.$ — the _run.ts channel law, prioritree/_run.ts:1-7).

**The tane precedent, measured**: tane carries **NO lint wrapper** (the 18-file listing at tane/.opencode/tools/ has no lint.ts) and **no Makefile** (measured absent) — tane's write-then-validate rides the patch tool's own check output, the pre-commit hook, and the battery (the make-less form). The sibling range for this grant therefore spans: kepric-input (no wrapper at all), tane (no lint tool — checks ride other instruments), hikari (the lint tool at the author's seat). A per-file form additionally requires new Makefile targets (lint-file/typecheck-file do not exist at prioritree, Makefile:3-15) — a brief-level decision.

### 4.3 keikaku — the composition lane (junro)

See §3. The need: the product effort's route composition (stages, increments, gates, questions — the same per-unit pipeline shape the birth ran, junro.json:175). The earned form: the 11 route ops (kumi-manifest.yaml:518) — NOT the packet/query ops (those are shinko's at hikari, :586). The wrapper exists; the grant is adapter-only.

### 4.4 shinko — the records landings, web, and the landing-rule question

**patch**: at hikari the convenor holds patch [apply] (kumi-manifest.yaml:581); at prioritree shinko holds task/question/friction/junro only (prioritree-seats.yaml:315-324) and the emitted map denies patch, write, and bash (opencode.json:340, :366, :328). **Measured: prioritree's shinko cannot land a prose record** — CONTINUATION.md entries, evidence files, the store's birth files — seat-side; every prioritree commit rides the collaborator's hand (the standing state: "the collaborator's-hand era until prioritree's own landing rule exists", junro.json:153; "prioritree's CONTINUATION.md committed through the collaborator's hand (the two-tree hands rule — no own landing rule yet)", junro.json:160; G-BIRTH-RECORDS condition 1, junro.json:247). The wrapper exists (patch.ts) — a shinko patch grant is adapter-only. Note: a patch grant alone changes the write capability, not the landing (commit) capability — the git question below is the landing-rule proper.

**web**: hikari's shinko holds web (kumi-manifest.yaml:580 — "the facilitator's web search; tansa's SEARCH+FETCH profile precedent"); prioritree's shinko has web deny (opencode.json:364). Priced with the tansa option (§4.1) — the collaborator rules the seat set.

**THE LANDING-RULE QUESTION (git at shinko) — named as the collaborator's ruling option, never decided here**: hikari's earned form is amendment 25 — git [sync, drift, land, discard, move, unshroud] at the convenor's seat (kumi-manifest.yaml:582), the wrapper's declared seat "coordinator + SE ONLY", the never-edit-main choreography, engine scripts/git_tool.py (git.ts:21, :24, :47, :53-59; manifest.yaml:2021-2244). Prioritree's current form is the collaborator's-hand era (above). The cost side is the highest of any candidate: `git` is absent from the derived-tree universe (clarity_scaffold.py:312-337 — the closed-world loop emits only universe ids, :586-588), no git wrapper exists at prioritree, and the engine is a hikari script whose choreography is hikari-worktree-shaped (project=<slug> resolves .worktrees/<slug> — manifest.yaml:2044-2048; prioritree has NO worktrees, so only the invoking-tree seat resolution would serve). Both states are legal standing states; the ruling is the collaborator's.

### 4.5 rikai — web UNEARNED, the pipeline division

Measured both sides: the evidence row — "PF-3: web CONFIRMED (32 calls — external library mechanisms, the external-information channel)" (kumi-manifest.yaml:198); the pack's unearned list — web DENIED (kumi-manifest.yaml:497). The division as it stands at hikari: tansa (and shinko) fetch; rikai consumes the fetched artifacts. **Price for the core effort**: the product's rikai legs (mechanism analysis over the prior-art corpus, the tally/vote-scheduling mechanisms) consume tansa's fetched artifacts — the division holds without rikai web; nothing in the birth pipeline's shape forces a change. The extension option exists with its citation (:198) if the collaborator rules it; the earned baseline denies it today.

### 4.6 The remaining seats

togo, shindan, suisen, kensho, keisan, hyoka, hansei, moho: no product-build need found beyond the base pack. kensho's verification instrument (test) is in the fixed five (test_runner.py); the gates' make legs (G-FOUNDATIONS floor-green, junro.json:63) are deterministic steps at the collaborator's hand (the no-seat-shelling law, prioritree-seats.yaml:43). Hikari's own baseline DENIES kensho lint (kumi-manifest.yaml:546) — no candidate named.

---

## §5 — The registration law (the wrapper-per-grant cost)

Every granted id needs a wrapper at prioritree (G-TOOL-GRANTS condition 2, junro.json:271; the Q-tool-registration resolution — "opencode auto-discovers custom tools from .opencode/tools/*.ts — the filename IS the tool id", junro.json:543). Every wrapper addition is a new tree-owned file per the ownership precedent (the stamps: "prioritree-owned (2026-11-19, G-HARNESS-BRIEF): composed from hikari's current render + tane's channel; hand-maintained in prioritree's tree" — patch.ts:1, junro.ts:1, test.ts:1).

| candidate grant | wrapper | universe member (clarity_scaffold.py:312-337) | cost |
|---|---|---|---|
| keikaku junro (route ops) | **EXISTS** — junro.ts, cross-project, reuse (G-TOOL-GRANTS condition 2 names it: "keikaku's junro reusing the existing junro.ts", junro.json:271) | yes (:323) | adapter pack row only — zero new files |
| shinko patch | **EXISTS** — patch.ts (the seven-file set) | yes (:325) | adapter pack row only |
| tansa (and/or shinko) web | **RECIPE** — hikari's web.ts is self-contained (fetch-based, no engine/make/deps, web.ts:1-335); the derived form is a straight compose with the ownership stamp; the channel question does not arise (in-wrapper fetch, no shell) | yes (:334) | ONE new tree-owned wrapper + the env keys (TAVILY_API_KEY, CONTEXT7_API_KEY) in the session env |
| jikko lint | **RECIPE** — hikari's lint.ts is the make-target form via Bun.$ (lint.ts:33-58); the derived form re-points at prioritree's host Makefile via runArgv (the _run.ts channel); per-file ops need new Makefile targets; the op set decision rides the brief | **no** — universe addition required | universe line + ONE new wrapper (+ optional Makefile targets) |
| shinko git (the landing-rule option) | **RECIPE (cross-project, the junro.ts precedent)** — engine at hikari; the worktree seat-resolution class does not apply (no worktrees at prioritree) | **no** — universe addition required | universe line + ONE new wrapper + **the landing-rule ruling itself** (§4.4) |

Measured property of the derived-tree permission model: the emission is tool-granular (allow/deny per universe id, clarity_scaffold.py:586-596) — op-level narrowing (e.g. keikaku's route-ops-only form vs the wrapper's 18-op enum, junro.ts:25) is brief/prompt-carried at the derived tree, unlike hikari's manifest-validated op scope (kumi-manifest.yaml:663-667).

---

## §6 — The sibling forms (the precedent range)

**kepric-input — the starved precedent (the same base-only form)**: the adapter's packs block is byte-shape-identical to prioritree's (input-seats.yaml:312-358 — shinko task/question/friction/junro; the read_pack anchor; jikko patch+curate); and kepric-input carries **NO tools/ wrappers at all** (`.opencode/` — 8 entries: no tools/ directory) — the engines-without-wrappers gap the Q-tool-registration record confirms ("kepric-input ships engines without wrappers — its permission keys name tool ids that cannot register", junro.json:543).

**tane — the widened form**: 18 wrappers (tane/.opencode/tools/: _run, calculate, code-graph-context, curate, declare, find, junro, lookup, pain, patch, reconcile, reflect, report, script, symbol-lookup, test, watasu, web — **no lint.ts, no git.ts**); the emitted grants (tane/opencode.json): **lookup, pain, and report at EVERY member seat** (e.g. tansa :442, :444, :448); **script at jikko** (:110); declare/reconcile/watasu/patch/read/junro at shinko (tane/opencode.json:358 declare, :372 reconcile, :383 watasu, :369 patch, :371 read, :365 junro — the facilitator's own widened instrument set), with **web DENIED at every tane seat including shinko** (:381, tansa :456, jikko :117, keikaku :154, kensho :228, togo :493) **despite web.ts sitting on disk** (tane/.opencode/tools/web.ts — the same handwritten fetch form as hikari's, measured :1-40). Tane's tansa-equivalent, measured at both sources the dispatch named: the emitted map grants **lookup** (:442) and **report** (:448) and DENIES web (:456); the genome's verb list carries `search` (tane/src/tane/genome/seats.json:84) but no web verb. Two further tane datums: **no lint wrapper** and **no Makefile** (both measured absent) — tane's make-less write-then-validate rides the patch tool's own check output, the pre-commit hook, and the battery; and tane's shinko carries **no git** either (no git.ts wrapper, no git row).

**The range, named**: the sibling derived trees span two precedents — **kepric-input, the starved pole** (base-only packs, zero wrappers: grants that cannot register — the inverse defect) and **tane, the widened pole** (three universal member tools beyond the base, a facilitator instrument set, a script grant at jikko, wrapper files on disk beyond the granted set). Neither sibling grants web at any seat; only hikari's earned baseline does (tansa + shinko). Neither sibling carries lint or git anywhere. Prioritree's current landed state sits AT the kepric-input pole minus the registration gap (the wrappers exist) — the collaborator rules within this range, and the web/lint/git candidates all sit beyond BOTH siblings' current forms (hikari's baseline alone backs them).

---

## §7 — The consolidated option set (for the collaborator's G-TOOL-GRANTS-BRIEF ruling)

Each candidate: the earned-baseline citation, the landed state, the product need, the wrapper cost, the sibling precedent — NAMED, never ruled. The G-TOOL-GRANTS conditions every landed grant must satisfy: the earned-baseline citation on the adapter row (junro.json:270), the wrapper-per-grant law (:271), the permission-map re-derivation (:272), the three --check legs PASS 24/24 (:270).

| # | candidate grant | seat(s) | earned-baseline citation | landed state | product need | wrapper cost | sibling precedent | the census's reading |
|---|---|---|---|---|---|---|---|---|
| 1 | **junro — the composition-lane route ops** | keikaku | kumi-manifest.yaml:518 ("keikaku writes junro, that is its entire purpose" — Q-SEATS-1, 2026-09-29) | `keikaku: *read_pack`, NO junro (prioritree-seats.yaml:344); emitted deny (opencode.json:131) | The product effort's route composition — the seat's own named act (prioritree-seats.yaml:164) has no instrument | **EXISTS — reuse** (junro.ts, cross-project; G-TOOL-GRANTS condition 2 names the reuse, junro.json:271) | hikari keikaku holds it (:518); tane + kepric-input hold junro at shinko only | **THE GATE MANDATES THE CURE** — condition 4 verbatim (junro.json:273); Q-harness's ruling already on the store (junro.json:532). Not an open option — the store's own composition |
| 2 | **web** | tansa | kumi-manifest.yaml:177 (PF-3: web CONFIRMED, **258 calls — the scout profile is SEARCH+FETCH**), :481 (granted 2026-10-01) | web deny (opencode.json:432); no wrapper | The prior-art census (TrueSkill, Elo, Bradley-Terry, LLM-as-judge) — the ruling's own named gap (junro.json:474) | **RECIPE** — web.ts self-contained fetch (web.ts:1-335; no shell channel — FR-MEM-0145 does not apply); ONE new tree-owned wrapper | **No sibling grants it**: tane denies web at every seat despite the wrapper on disk; kepric-input has neither | The strongest SEARCH+FETCH evidence in the family (258 calls); the ruling names the gap itself |
| 3 | **lint** | jikko | kumi-manifest.yaml:280 (**lint 4,412 — "the best-evidenced row in the pass"**), :530 (re-granted, amendment 40, FR-MEM-0149: "the patch tool's rode-along is ruff-only, structurally blind to type errors") | jikko holds patch+curate only; no wrapper; `lint` ABSENT from the universe (clarity_scaffold.py:312-337) | Write-then-validate at the author's seat — the product effort's core-loop discipline | **RECIPE** — universe line + ONE new wrapper; the derived form re-points at prioritree's host Makefile via runArgv; whole-tree ops land on existing targets (Makefile:11-15), per-file ops need new targets — the op-set decision rides the brief | tane carries NO lint wrapper and NO Makefile (the make-less form); hikari grants it at jikko | Earned with the family's single best evidence row; the one candidate requiring a universe addition (the adapter-packs-edit step's scope, junro.json:116-118). The op-set shape rides G-TOOL-GRANTS-BRIEF |
| 4 | **patch** | shinko | kumi-manifest.yaml:581 (hikari's convenor holds patch [apply]) | shinko holds task/question/friction/junro only (prioritree-seats.yaml:315-324); emitted patch deny (opencode.json:340) | **Measured: prioritree's shinko cannot land a prose record** (§4.4) — every CONTINUATION.md entry, evidence file, and store birth rides the collaborator's hand | **EXISTS** — patch.ts; adapter pack row only | tane's shinko holds patch (tane/opencode.json:369); hikari's does (:581); kepric-input's does not | Ends the collaborator's-hand era's **write-side** dependency; the landing (commit) side is the git question (#6). The era itself is the ruled standing state — the collaborator rules whether it ends now |
| 5 | **web** | shinko | kumi-manifest.yaml:580 ("the facilitator's web search; tansa's SEARCH+FETCH profile precedent") | web deny (opencode.json:364) | The facilitator's external-facts lane at the product effort | Same wrapper recipe as #2 (one wrapper serves both seats — the file is per-tree, the grant is per-seat) | tane's shinko: web DENIED (tane/opencode.json:381) | Priced with #2; the hikari baseline grants it, no sibling does. The collaborator rules the seat set |
| 6 | **git — the landing-rule option** | shinko | kumi-manifest.yaml:582 (amendment 25, 2026-10-26: the landing instrument restored at the convenor's seat) | No git wrapper, no git row, `git` ABSENT from the universe; the collaborator's-hand era stands (junro.json:153) | The landing rule proper — who commits prioritree's records | **RECIPE (cross-project, the junro.ts precedent)** — universe line + ONE new wrapper + **the landing-rule ruling itself**; the hikari choreography's worktree seat-resolution does not apply (NO worktrees at prioritree) — only the invoking-tree resolution would serve | **No sibling carries git anywhere** — hikari's baseline is the sole form, and it is hikari-worktree-shaped | **THE LANDING-RULE QUESTION — named as the collaborator's ruling option, never decided by this census** (§4.4). Highest cost of the set; the alternative — the collaborator's-hand era — is the standing ruled state (junro.json:247). Both states legal; the ruling is the collaborator's |
| 7 | **web** | rikai | kumi-manifest.yaml:198 (PF-3: web CONFIRMED, **32 calls** — external library mechanisms) — BUT the pack's unearned list DENIES it (:497) | web deny (opencode.json:282) — matches hikari's baseline | The pipeline division as it stands: tansa fetches, rikai consumes the artifacts. **Price for the core effort: the division holds** | Same wrapper recipe if ruled | tane's rikai: web deny (tane/opencode.json:305) | UNEARNED at the baseline today — the extension option exists with its 32-call citation (:198); the core effort does not demand it |
| 8 | **web/webfetch — the emitted anomaly** | togo | **NONE on any record** — no ruling grants togo web; the adapter gives togo `*read_pack` only (prioritree-seats.yaml:342) | **The emitted map carries web/webfetch allow at togo (opencode.json:466-467) — the collaborator's stopgap hand-edit (amendment 28); a fresh regen derives deny** | — (not a product need; the stopgap drift) | — (a pack/permission question, not a wrapper question) | — | **Resolves mechanically at the re-emit either way** (conditions 1+3): either the collaborator rules togo a web pack row carrying its citation, or the deny cures at regen and the byte-compare goes green. Reported, not ruled |
| 9 | **lint** | kensho | **DENIED at hikari's own baseline** — kensho's unearned list carries lint (kumi-manifest.yaml:546) | (no candidate landed) | kensho's instrument (test) is in the fixed five; the gates' make legs are deterministic steps at the collaborator's hand | — | tane's kensho: no lint | **Named to foreclose the symmetry question** — hikari's own earning ledger denies the verifier lint; the second-eyes discipline keeps the author's instrument at the author's seat |

### 7.2 The special questions (restated for the brief)

- **The landing-rule option (git at shinko)** — §4.4 / row #6: hikari's earned form (amendment 25) vs prioritree's collaborator's-hand era. The option is named with both citations; the ruling is the collaborator's.
- **rikai's web** — §4.5 / row #7: unearned at baseline, the division holds for the core effort; the extension option exists at :198.
- **The .env/config the web wrapper needs at the derived tree** — §4.1, measured: `TAVILY_API_KEY` (web.ts:92, :133, :178) and `CONTEXT7_API_KEY` (:204-207), read from the process env; **no .env loading mechanism exists in the wrapper** — the keys must ride the session's inherited environment (the collaborator's shell). A missing key returns an honest error naming it (web.ts:93, :205). No MCP dependency — the disabled tavily/context7 entries do not affect the wrapper. **This is the standing config requirement for any web grant at prioritree.**

### 7.3 Close and caveats

- **Boundary held**: this census made zero writes anywhere — no store mutations, no filings, zero hikari-prod calls (the deploy-corollary surface unused per the binding role). Reads and citations only.
- **No web search was run in this census** — measured at source only (the ruling's own line honored under either reading).
- **The candidate set's shape**: one mandated cure (#1 — the store's own composition), two evidence-backed baseline grants with recipes (#2 web at tansa, #3 lint at jikko), two convenor options priced (#4 patch, #5 web at shinko), one ruling-question named (#6 git), one baseline-deny held (#7 rikai web), one drift resolving mechanically (#8), one symmetry foreclosed (#9).
- **The build shape if granted**: adapter pack rows carry the earned-baseline citations (condition 1); universe additions for lint/git ride the adapter-packs-edit step's scaffold scope; the wrapper additions (#2/#3, and #6 if ruled) ride the wrapper-additions step; the re-emit + three --check legs close the gate.
- **The pipeline from here**: this census (discover/tool-grants) + rikai's mechanism record (understand/tool-grants) feed togo's synthesis at `synthesize/tool-grants`; the brief lands at G-TOOL-GRANTS-BRIEF and the collaborator rules the grant set; no build dispatch fires until the brief gate is green (the pipeline law, junro.json:175-176, :276-281).

*End of the census record.*
| keisan / suisen | calculate (born with the pack) (:599 / :607) | born-clean (no pre-convergence grants) (:399-402, :427) | script (:601 / :609) |
