# understand/tool-grants — the tool-grants unit's mechanism pricing

## Provenance

| field | value |
|---|---|
| seat | rikai (理解, understand) — packet `understand/tool-grants`, route `prioritree-birth`, unit `build/tool-grants` |
| date | 2026-11-19 |
| method | mechanism pricing over tansa's census (`discover/tool-grants.md` — the ground truth), with every load-bearing claim the pricing leans on re-measured at source: the adapter (prioritree-seats.yaml:314-360), the scaffold (clarity_scaffold.py:312-337 universe, :559-616 emission, :683-706 rot detector, :719-724 argparse), the landed emission (prioritree/opencode.json, all 13 blocks read), the wrapper bases (hikari web.ts:1-335, lint.ts:1-66, git.ts:1-131; prioritree junro.ts:1-258, _run.ts:1-58), the earned baseline (kumi-manifest.yaml:474-609, :662-667), the git engine (git_tool.py:1-1250), the store (junro.json:267-282, :474, :495), both Makefiles, and two calculate-surface derivation checks (24/24 artifacts; 13×2 sibling re-byte lines) |
| boundary held | read-only — zero writes, zero store mutations, zero filings, zero friction writes, zero emissions fired; reads and derivations only; single return (this document, landed by shinko verbatim) |

**Zero web calls; zero hikari-prod calls.** Tier convention: `[TIER: measured]` = read at source this session; `[TIER: census]` = tansa's citation, leaned on without re-measurement where not load-bearing.

---

## §1 — The adapter pack rows (banked exact YAML)

All rows land in `hikari/scripts/generation/sources/prioritree-seats.yaml` `packs:` (the adapter-packs-edit step; hikari-side, landed through hikari's shinko-git choreography). Condition 1 (junro.json:270) — every grant carries its earned-baseline citation or the collaborator's ruling — rides each row's comment.

### 1.1 keikaku's junro row — the composition lane (the mandated cure, G-TOOL-GRANTS condition 4)

`keikaku: *read_pack` (prioritree-seats.yaml:344) becomes the merge form (jikko's precedent, :346-355):

```yaml
  keikaku:
    <<: *read_pack
    # THE COMPOSITION LANE (Q-SEATS-1's ruling 2026-09-29 — the earned baseline,
    # kumi-manifest.yaml:518: "keikaku writes junro, that is its entire purpose";
    # Q-harness's ruling, junro.json:532; the mandated cure, G-TOOL-GRANTS
    # condition 4, junro.json:273): the 11 route ops, hikari's earned form
    # verbatim — NOT the packet/query ops (those are shinko's, :586).
    junro: ["route add-question", "route set-question", "route add-ruling", "route add-increment", "route amend-increment", "route add-gate", "route close-gate", "route compose-stage", "route record-amendment", "route set-checkpoint-ruling", "route set-route-status"]
```

**The op-scope question, priced and named honestly** [TIER: measured]: the derived-tree permission model is TOOL-GRANULAR — the emission renders `"junro": "allow"` at keikaku from the row's keys alone (clarity_scaffold.py:582–588: `allows` = the pack row's keys; the loop emits allow/deny per universe id); the op list rides the adapter as **documentation**. The wrapper's enum carries all 18 ops (prioritree junro.ts:25), so keikaku *could* technically call packet/query ops; the narrowing to the 11 route ops rides the **seat prompt** (keikaku's act already carries it — "Compose the route through the junro machinery — stages, increments, gates, questions", prioritree-seats.yaml:164). Hikari's manifest-validated op scope ("op granularity is tool-internal validation against the manifest — ONE enforcement point", kumi-manifest.yaml:662-667) **has no derived-tree equivalent**. Options: (i) single shared wrapper + prompt-carried narrowing [recommended — zero extra files, the landed family shape]; (ii) a keikaku-scoped junro wrapper variant with an 11-op enum [mechanical narrowing; cost: a second wrapper file, render-drift risk, the registration law satisfied twice — not recommended at birth].

### 1.2 tansa's web row — and the anchor restructure it forces

**Mechanism fact** [TIER: measured]: `tansa: &read_pack` IS the anchor (prioritree-seats.yaml:325); every alias seat (rikai/togo/shindan/keikaku/suisen/kensho/keisan/hyoka/hansei/moho + jikko's merge) receives the anchor's keys wholesale — YAML merge adds, never subtracts. A `web` key on tansa's row would grant web to **all eleven** read_pack seats. Therefore the anchor must move, and YAML requires the anchor to precede its aliases — only shinko precedes tansa, so the block reorders: **rikai takes the anchor and moves above tansa; tansa becomes a merge**. Emission-neutral (json.dumps `sort_keys=True`; the packs-mapping order feeds nothing — build_state iterates `seats:`, clarity_scaffold.py:509) and gate-neutral (the dangling-reference gate checks names, not order, :524-528).

```yaml
  rikai: &read_pack
    friction: []
    read: []
    grep: []
    glob: []
    # THE TEST RULING (2026-09-28 ...) — the anchor's two ruling comment blocks
    # (prioritree-seats.yaml:330-339) move WITH the anchor, verbatim
    test: []
    # THE CALCULATE COMPOSITION (2026-09-28, Q-CALC-1) — verbatim
    calculate: [add, subtract, multiply, divide, sum, count]
  tansa:
    <<: *read_pack
    # THE WEB GRANT (PF-3: web CONFIRMED, 258 calls — the scout profile is
    # SEARCH+FETCH — kumi-manifest.yaml:177; granted at hikari 2026-10-01,
    # :481; the ruling's own named gap, junro.json:474): hikari's op form.
    web: [search, extract, research, lookup]
```


### 1.3 shinko's patch row (and web row, if granted)

One-key additions to shinko's explicit block (prioritree-seats.yaml:315-324):

```yaml
    # THE PATCH GRANT AT THE CONVENOR (hikari's baseline, kumi-manifest.yaml:581
    # — the records landings' write side; the wrapper exists, patch.ts): the
    # op-list convention follows jikko's landed row (patch: []; hikari's
    # manifest form is [apply] — the emission is tool-granular either way).
    patch: []
    # THE WEB GRANT AT THE CONVENOR (hikari's baseline, kumi-manifest.yaml:580
    # — "the facilitator's web search; tansa's SEARCH+FETCH profile precedent").
    web: [search, extract, research, lookup]
```

### 1.4 jikko's lint row (op set per §3's ruling)

```yaml
    # THE LINT GRANT (the earned baseline — lint 4,412 lineage calls, "the
    # best-evidenced row in the pass", kumi-manifest.yaml:280; re-granted at
    # hikari 2026-10-26, amendment 40, on FR-MEM-0149's record — the patch
    # tool's rode-along is ruff-only, structurally blind to type errors —
    # kumi-manifest.yaml:530): the derived form is whole-tree over the host
    # Makefile (no Docker, no per-file targets) — the ruled [check, typecheck]
    # op set; see understand/tool-grants §3.
    lint: [check, typecheck]
```

(Option B's row is the verbatim hikari form `lint: [file, typecheck_file]` — priced in §3.)

### 1.5 shinko's git row (if the landing-rule ruling lands — §4)

```yaml
    # THE LANDING INSTRUMENT (hikari's amendment 25, 2026-10-26 —
    # kumi-manifest.yaml:582): the derived form is the cross-project wrapper
    # (the junro.ts precedent — the engine stays home at hikari). At
    # prioritree's worktree-less tree the seats derive subject==main and the
    # never-edit-main law's letter cannot carry (understand/tool-grants §4) —
    # the ruling owns that consequence. unshroud NOT carried: inert at
    # prioritree (no skip-worktree bits exist).
    git: [sync, drift, land, discard, move]
```

The wrapper's enum carries hikari's six ops verbatim; the five-op row documents the prioritree scope (prompt-carried narrowing, the §1.1 mechanism).

---

## §2 — The web wrapper recipe (banked exact composition)

**The one real question, measured at source: web.ts carries ZERO hikari-specific content.** All 335 lines read: no "hikari" substring, no tree paths, no `scripts/`, no make targets, no Docker, no `Bun.$`, no `runArgv` — the wrapper is in-wrapper `fetch` with AbortController (web.ts:25, :61), so the FR-MEM-0145 channel question does not arise (no shell channel at all) and **no channel substitution is needed**. The only externals: `api.tavily.com` (:96/:146/:181), `context7.com` (:217/:236), the two env keys, and the `@opencode-ai/plugin` import (:2 — resolves against prioritree's already-emitted `.opencode/package.json` pins and installed node_modules; zero package.json/tsconfig changes). [TIER: measured]

**The composed file** = line 1 swapped + body verbatim (lines 2–335 unchanged):

```
// prioritree-owned (2026-11-19, G-TOOL-GRANTS-BRIEF): composed from hikari's handwritten web.ts verbatim (no channel substitution — in-wrapper fetch, no shell); hand-maintained in prioritree's tree
```

**The env-keys standing config requirement** (named for the brief): `TAVILY_API_KEY` (read at :92 search, :133 extract, :178 research) and `CONTEXT7_API_KEY` (:204–207, the X-Context7-Api-Key header) ride the **process env the opencode session inherits** — the wrapper has NO .env loader; a missing key returns an honest error naming it ("Error: TAVILY_API_KEY not set in environment.", :93; the CONTEXT7 form at :205). No MCP dependency: the disabled tavily/context7 entries (opencode.json:475-482) do not affect the wrapper. **One wrapper serves every granted web seat** — the file is per-tree, the grant is per-seat (condition 2 satisfied once).

---

## §3 — The lint wrapper: universe line, sibling impact, derived form, the op-set ruling

### 3.1 The universe addition (exact bytes)

`KUMI_BUILTIN_UNIVERSE` (clarity_scaffold.py:312-337) — insert after `"junro",` (line 323):

```python
    "junro",
    "lint",
    "lsp",
```

(If git is ruled: `"git",` between `"friction",` (:319) and `"glob",` (:320).) The tuple's comment block (:305-311) gains the ruling citation per its established pattern ("calculate and curate IN (Q-CALC-1, Q-CURATE-1)" — one line per added id).

### 3.2 The sibling impact — priced exactly [TIER: measured]

All three TargetSpecs share the constant (`builtin_universe=KUMI_BUILTIN_UNIVERSE`, clarity_scaffold.py:420/:433/:446); the permission loop (:587-588) renders `"allow"/"deny"` per universe id at **every seat of every target**. Clarity's and input's packs carry no lint → each gains `"lint": "deny"` at all 13 seat blocks — **one artifact (opencode.json) MISMATCH per sibling tree; the other 23 artifacts MATCH**. Their `--check` legs **FAIL** until re-emitted (the check regenerates in memory and byte-compares, :683-706; its FIX lines name the commands, :704-705). With lint alone: 13 lines per sibling; with lint + git: 26 (derivation checked on the calculate surface). **The sibling-contracts re-emit pair MUST ride the same hands-window BEFORE the --check legs** — banked as §6's sequence.

### 3.3 The derived wrapper (banked, whole-tree form)

Hikari's lint.ts is the `Bun.$` make-target class (lint.ts:33-58) with the docker/local axis — all inapplicable at prioritree (no Docker; host Makefile lint/typecheck already exist, Makefile:11-15; no per-file targets exist, Makefile:3-18). The derived form (the _run.ts channel law — never Bun.$; prioritree/_run.ts:1-7):

```ts
// prioritree-owned (2026-11-19, G-TOOL-GRANTS-BRIEF): composed from hikari's current render, re-pointed at prioritree's host Makefile via the _run.ts channel; hand-maintained in prioritree's tree
import { tool } from "@opencode-ai/plugin"
import { runArgv } from "./_run"

function formatOutput(result: {
  exitCode: number
  text(): string
  stderr: Buffer | string
}): string {
  const stdout = result.text()
  const stderr = result.stderr.toString()
  if (result.exitCode === 0) {
    return stdout.trim() || "Done."
  }
  if (stderr.trim()) {
    return `${stdout}${stdout.trim() ? "\n" : ""}stderr:\n${stderr}`.trim()
  }
  return stdout.trim() || `Exited with code ${result.exitCode} (no output captured).`
}

export default tool({
  description: "Code quality — linting and type checking at prioritree, whole-tree via the host Makefile: check (make lint — ruff over src/ and tests/) and typecheck (make typecheck — pyright over the tree's [tool.pyright] include set). Host-only (no Docker, no worktrees); the explicit-argv runArgv channel, no shell.",
  args: {
    operation: tool.schema
      .enum(["check", "typecheck"])
      .or(tool.schema.literal("help"))
      .describe("Operation to perform (use \"help\" to print this tool's usage)"),
  },
  async execute(args, context) {
    switch (args.operation) {
      case "check": {
        return formatOutput(await runArgv(["make", "lint"], { cwd: context.directory }))
      }
      case "typecheck": {
        return formatOutput(await runArgv(["make", "typecheck"], { cwd: context.directory }))
      }
      case "help": {
        return "lint — Code quality — whole-tree via the host Makefile.\n\nOperations:\n  check  [make lint]\n    Run ruff over src/ and tests/\n  typecheck  [make typecheck]\n    Run pyright over the tree's [tool.pyright] include set"
      }
    }
    return `Unknown operation: ${args.operation}`
  },
})
```

### 3.4 THE OP-SET QUESTION — isolated for the brief, both options priced

- **Option A — whole-tree-only** (`lint: [check, typecheck]`) [RECOMMENDED]: **zero new Makefile targets, zero Makefile edits**; two wrapper ops over the existing targets. The FR-MEM-0149 cure holds whole-tree — `make typecheck` is pyright over the tree's include set, strictly **wider** coverage than per-file; at birth scale (the skeleton src/ + tests/) the whole-tree run is sub-second, so the per-file latency value is ~zero; the per-file auto-fix convenience overlaps patch.py's own rode-along (ruff at apply). Cost beyond the wrapper: none.
- **Option B — per-file parity with hikari's earned form** (`lint: [file, typecheck_file]`, kumi-manifest.yaml:530): requires **two new Makefile targets** (neither exists, Makefile:3-18) — `lint-file: uv run ruff check --fix $(F) && uv run ruff format $(F) && uv run ruff check $(F)` and `typecheck-file: uv run pyright $(F)` — plus the wrapper's `F=` arg plumbing (hikari's `WHERE=` axis drops: no docker axis), plus, honestly, the **0-files false-clean guard class**: hikari guards every per-file pyright with PYRIGHT_GUARDED (make/lint.mk:153-183 — pyright on a bare file can report a byte-identical 0-files PASS; the guard refuses exit 3 on filesAnalyzed 0) — the derived per-file form carries the guard or accepts the class. Value at a small tree: negligible now; grows with the tree. **The scale trigger is named: re-open when whole-tree typecheck latency hurts the write-then-validate loop.**

---

## §4 — THE GIT QUESTION — isolated, never decided

### 4.1 The cross-project wrapper recipe (banked — the junro.ts precedent, junro.ts:97)

```
runArgv(["uv", "run", "--project", "/Users/marklosey/projects/kepric/hikari", "python", "/Users/marklosey/projects/kepric/hikari/scripts/git_tool.py", ...eargs], { cwd: context.directory })
```

Derived from hikari's git.ts (131 lines): (1) the stamp — `// prioritree-owned (2026-11-19, G-TOOL-GRANTS-BRIEF): composed from hikari's current render, the cross-project junro.ts form (engine stays home at hikari); hand-maintained in prioritree's tree`; (2) `import { runArgv } from "./_run"`; (3) delete the `Bun.$` line; (4) **delete the per-op conditional enginePath block** (git.ts:53-58 etc. — hikari's worktree main-root resolution; the derived form's engine path is the fixed hikari absolute path on every op); (5) each op's spawn → the runArgv form above. The `project` arg forwards `--project=<slug>` verbatim — at prioritree the engine resolves `.worktrees/<slug>` under the deriving main root and **REFUSES loudly** on the missing worktree (git_tool.py:385-407, never a silent fallback): dead but correct at a worktree-less tree. `--timeout` stays CLI-only (git_tool.py:171-174). `cwd: context.directory` keeps the session cwd at prioritree — the invoking-tree seat resolution serves exactly (seats derive from the child process's cwd; `uv run --project` does not chdir — the junro.ts precedent's own recorded property).

### 4.2 The choreography at a worktree-less tree — priced honestly [TIER: measured at git_tool.py]

- **Seat derivation** (:355-382): subject = the invoking tree's toplevel; main = common-dir.parent. At prioritree `--git-common-dir` prints `.git` (relative, measured against git 2.54.0) → **main_root == the prioritree toplevel → subject == main**; the envelope itself labels the subject `"tree": "main"` (:378). Both branches read from the same tree (:370-371) → subject branch == main branch.
- **Pre-flight** (:1001-1008): both branches must carry an upstream — no upstream **REFUSES** ("refusing to guess a push target"). Precondition named: prioritree's checked-out branch needs origin tracking (a remote-config fact outside this read-only seat's measurement).
- **land** (:995-1074 + op_land): absorption pre-leg → `add --all` → commit (message + Subtask/Agent/Verified-by trailers; **prioritree's .githooks/pre-commit fires** — the pyright 0/0/0 staged check; PRIORITREE_HOOK_BYPASS the bypass) → push-subject → `merge --ff-only <branch>` at the main root — **the branch into itself: "Already up to date", a recorded no-op leg** → push-main (**the same ref again: no-op**) → tracked-ref verification (:973-987: local == tracking == remote, success reported ONLY from the comparison). **Net at prioritree: land = add-all + trailer-commit + push, structurally exit-code-verified — the collaborator's-hand mechanics, mechanized at the seat.**
- **The absorption pre-leg degenerates harmlessly**: main's dirty set IS the subject's (same tree); `ABSORBABLE_DIRTY_PATHS[0]` is `.plans/state/friction-ledger.jsonl` — **exactly prioritree's friction store home** (harness-brief §5). When the dirty set is exactly the ledger, both ledger paths resolve to the same file (:640-641), containment is trivially identical, and the "fired-cp" path (:669-715) writes the file's own bytes back — a recorded no-op leg; the reconcile rider then reads a post-commit-clean tree and no-fires. No hazard.
- **sync**: push → no-op merge → no-op push → verify (net: "push, verified"). **drift**: read-only, works anywhere (ls-remote + tracking comparisons; carries per-branch error fields honestly). **discard**: `git restore` of named paths at the subject toplevel — at prioritree that is **the main checkout**: destructive with no worktree fallback; the named-paths-only law (:120-126) still scopes it. **unshroud**: the skip-worktree dance — **inert at prioritree** (no skip-worktree bits exist; the derived-view shape gitignores, never shrouds). **move**: works.
- **The never-edit-main law's fit**: the letter — "main's checkout receives ONLY merges; run the write ops from worktree seats" (git.ts:21) — **cannot hold at prioritree: there are no worktree seats; land's add/commit legs run in the main checkout by necessity**. The law's spirit — the false-claim kill (FR-MEM-0006/0007), per-leg exit codes as data, R-9's never-march-on, tracked-ref-only success — **carries whole**. A prioritree git grant is honestly a **single-tree landing instrument**, not the two-tree choreography; the ruling owns this consequence.

### 4.3 The landing-rule ruling — both options priced, the collaborator's

- **Option 1 — the hand era continues** (the standing ruled state, junro.json:153/:160; G-BIRTH-RECORDS condition 1, :247): zero cost now; every prioritree commit keeps riding the collaborator's hand; shinko stays unable to land records seat-side (the measured write-gap, census §4.4).
- **Option 2 — the seat takes the landing** (universe line + wrapper + shinko row land): cost = one universe addition (the §6 sibling re-byte pair), one wrapper file, the §4.2 consequence set (single-tree land; main-seat discard; the upstream precondition; unshroud inert); value = the write-side grant (patch, row #4) gains its landing pair — records, store births, and CONTINUATION entries land seat-side, structurally verified; the collaborator's-hand era ends for prioritree commits.

**Priced recommendation: option 2** — the mechanism is proven (amendment 25's instrument), the degenerate case is handled by construction, and the standing state's cost is the very bottleneck the tool-grants lane exists to cure. Both states are legal standing states; the ruling is genuinely the collaborator's. **Sequencing note**: the unit's OWN landing rides the standing hands regardless — the ruling's mechanics apply from their landing forward; keep the tool-grants unit's commits on the standing hands, the instrument serves from the next landing.

---

## §5 — THE TOGO ROW — the disposition isolated, three options priced

Facts [TIER: measured]: the stopgap sits at **togo's block** (opencode.json:466-467 — `web: allow` AND `webfetch: allow`); the store's own record (amendment 28, junro.json:495) says the collaborator's statement **named tansa**; no ruling grants togo web; the adapter gives togo `*read_pack` only (:342); a fresh regen derives deny — the on-disk allow is the accepted drift (--check FAILs on opencode.json today, one artifact).

- **(a) togo web becomes a ruled row**: condition 1's literal words ("...its earned-baseline citation (the manifest's evidence rows) **or the collaborator's ruling**") permit a ruling-cited grant — but it would be the set's **only zero-evidence row** (hikari's togo holds no web, no lineage citation; the ruling's own frame: "We know what earned as a baseline", junro.json:474). Re-emit behavior: togo's `web` allow stays (drift cures on that line); `webfetch` still reverts to deny.
- **(b) the stopgap was aimed at tansa** — the re-emit lands tansa's row + togo reverts: tansa's row lands (258 calls, kumi-manifest.yaml:177/:481 — the store's own expected form, junro.json:495); togo's block re-bytes `web: allow→deny` + `webfetch: allow→deny`; **the drift cures whole; the byte-compare goes green**. Cost: any live session relying on togo's allow loses that channel — the replacement is tansa's wrapper-registered web tool (and shinko's if ruled).
- **(c) both**: tansa (evidence) + togo (ruling); webfetch still dies everywhere.

**Recommendation: (b).** The webfetch note under EVERY option: the stopgap's `webfetch: allow` (an opencode builtin, wrapper-independent) dies at the re-emit — no family pack row carries `webfetch` (the web tool supersedes it; the universe renders it deny at every seat absent a pack row). The ruled channel is the custom web tool (wrapper-gated, condition 2); its `extract` op replaces the webfetch lane. Name this in the brief so no one mistakes the webfetch reversion for a defect.

---

## §6 — The sibling-impact sequencing (banked)

Whatever universe ids are added (lint — certain if row #3 lands; git — if §4's ruling lands), clarity's and input's opencode.json re-byte (13 deny-lines per id per tree; 26 if both — derivation checked). The re-emit pair MUST ride the same hands-window BEFORE the --check legs — G-TOOL-GRANTS condition 1 requires all three legs PASS 24/24 (24 = opencode.json + AGENTS.md + package.json + tsconfig + plugin + 5 engines + pre-commit + 13 prompts; derivation checked on the calculate surface).

**The exact sequence — one hands-window, all six commands from hikari's root** (`/Users/marklosey/projects/kepric/hikari`; the emission commands are the collaborator's hands — no seat shells, prioritree-seats.yaml:43):

```
# (before the window) jikko lands the hikari-side edit — the adapter rows + the
#   universe lines at clarity_scaffold.py — through hikari's shinko-git
#   choreography; hikari's instruments green on the touched files (ruff/pyright
#   over clarity_scaffold.py; the YAML is data). The wrapper files land at
#   prioritree (tracked tree assets, NOT --check-covered) through the standing
#   hands. No .gitignore, package.json, or tsconfig changes ride this unit.
uv run python scripts/generation/clarity_scaffold.py                          # 1. clarity re-emit (the bare form is clarity's FIX-line shape; --target clarity equally legal — argparse default, :719-724)
uv run python scripts/generation/clarity_scaffold.py --target input           # 2. input re-emit (the universe re-byte cure)
uv run python scripts/generation/clarity_scaffold.py --target prioritree     # 3. prioritree re-emit — the new pack rows + the universe denies/allows + the stopgap cure, ONE overwrite
uv run python scripts/generation/clarity_scaffold.py --target clarity --check    # 4. exit 0 — 24/24
uv run python scripts/generation/clarity_scaffold.py --target input --check       # 5. exit 0 — 24/24
uv run python scripts/generation/clarity_scaffold.py --target prioritree --check  # 6. exit 0 — 24/24
```

Ordering law: 1-3 all precede 4-6 (a check before the sibling re-emit FAILs on the universe re-byte); step 3 cures prioritree's standing drift in the same overwrite. The adapter-edit and wrapper-addition steps precede the window in either order (the emission derives from the adapter only; the wrappers are not emission inputs).

---

## §7 — The isolated ruling set for G-TOOL-GRANTS-BRIEF (zero open bankable questions)

Each ruling is a choice among priced alternatives; every bankable byte is above.

| # | the ruling | the priced options | rikai's recommendation |
|---|---|---|---|
| 1 | **The grant set** (census §7's nine rows) | #1 keikaku junro — the mandated cure (banked §1.1); #2 tansa web — the strongest evidence + the ruling's own named gap (banked §1.2); #3 jikko lint — the best-evidenced row (banked §1.4 + §3); #4 shinko patch — the write-side (banked §1.3); #5 shinko web — the facilitator's lane, zero incremental wrapper cost (banked §1.3); #6 shinko git — the landing-rule ruling (§4); #7 rikai web — UNEARNED at baseline, the pipeline division holds for the core effort (the 32-call extension option exists at kumi-manifest.yaml:198 if ever ruled); #8 togo — §5; #9 kensho lint — foreclosed (hikari's own baseline denies it, :546) | Land #1-#5; hold #7 and #9; #6 and #8 per their own rulings |
| 2 | **The lint op-set** (§3.4) | A whole-tree [zero cost] vs B per-file parity [2 Makefile targets + the 0-files guard + arg plumbing] | **A** — B named with its exact cost; re-open at the scale trigger |
| 3 | **The web seat set** (§1.2/§1.3/§5) | tansa / +shinko / +rikai / +togo, each priced | tansa + shinko; rikai no; togo per ruling 4 |
| 4 | **The togo disposition** (§5) | (a) ruled standing row [zero-evidence, legal under condition 1's literal words] / (b) tansa lands + togo reverts [drift cures whole] / (c) both | **(b)** — the store's own record names tansa; webfetch dies under all options (named, not a defect) |
| 5 | **The git landing rule** (§4.3) | 1 the hand era continues [the standing ruled state] vs 2 the seat takes the landing [priced consequence set] | **2**, priced — but the ruling is genuinely the collaborator's; the unit's own landing rides the standing hands either way |

**The standing config requirement**: `TAVILY_API_KEY` + `CONTEXT7_API_KEY` must ride the session env (the collaborator's shell) before any web seat dispatches — no .env loader; honest missing-key errors name the key.

**Contradiction notes**: none found — the census's load-bearing claims re-verified at source (opencode.json:131/:340/:364/:432-433/:466-467; prioritree-seats.yaml:315-360; kumi-manifest.yaml:518/:530/:580-582/:586; clarity_scaffold.py:312-337/:586-596/:683-706; web.ts:1-335; junro.ts:25/:97). One tension named, not a contradiction: condition 1's literal "or the collaborator's ruling" branch vs the zero-evidence shape of togo option (a) — priced honestly in §5. One census datum refined: the emission is per-seat-block granular (13 blocks per tree), so the universe re-byte is 13 lines per id per sibling tree, not a whole-file rewrite.

*End of the pricing record — the pipeline from here: togo's synthesis at `synthesize/tool-grants` carries this + the census to G-TOOL-GRANTS-BRIEF; no build dispatch fires until the brief gate is green (junro.json:175-176, :276-281).*
Alternative priced and declined: an anchor on the merge value (`<<: &read_pack {...}`) is valid YAML but exotic — the family's legibility law refuses it. Note: if web were ruled at **shinko only**, no anchor move fires (shinko's block is explicit); the move is forced only by a tansa grant.
