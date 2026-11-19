# synthesize/harness-brief — the harness unit's build brief (G-HARNESS-BRIEF)

**Seat:** togo (統合, integrate) · **Date:** 2026-11-19 · **Packet:** synthesize/harness, route prioritree-birth
**Inputs read:** discover/harness.md (tansa's census), understand/harness.md (rikai's mechanism record, §1-§14), .junro/junro.json (amendment 21's three rulings; Q-harness's ruling; Q-tool-registration ruled; G-HARNESS's five conditions; Q-typecheck-alignment PYRIGHT), plan/keikaku-composition.md (the unit's steps), plus the exact-byte sources: hikari/scripts/generation/clarity_scaffold.py, hikari/scripts/generation/sources/input-seats.yaml (the template), hikari's rendered wrappers (calculate/patch/friction/test/curate/junro .ts), tane's _run.ts + calculate.ts + test.ts + junro.ts, hikari/.gitignore:198-200, prioritree/.gitignore.
**Land:** shinko lands this at store/synthesize/harness-brief.md verbatim, nothing edited.

---

## 1. THE HIKARI-SIDE EDIT (jikko, through hikari's shinko-git choreography)

Two files only: `scripts/generation/clarity_scaffold.py` and the new `scripts/generation/sources/prioritree-seats.yaml`.

### 1.1 clarity_scaffold.py — the four constants, exact bytes

**(a) PRIORITREE_LAW_MD** — first line adapted per understand/harness.md §11-1's banked candidate; the remainder VERBATIM after INPUT_LAW_MD's body (clarity_scaffold.py:254-268):

```
PRIORITREE_LAW_MD = """## Standing Laws

- Prioritree has NO worktrees and HAS a `.plans` directory — the efforts' stores live there,
  git-tracked (the record home); design docs ride the hikari tree, cited by absolute path, never hunted.
- Never return an empty final message — a report saying "not started" is a legitimate completion; silence is not.
- No claim without evidence on disk — the report describes, the tree is the truth.
- The naming law: a new symbol's name is the first word of its act-statement.
- Five-field docstrings: Purpose / Refuses when / Re-run / Touches / Provenance.
- Zero-ignore strictness: a lint or type ignore is a ruling, never a convenience — the
  zero-findings bar stands.
- The no-shell law: subprocess only through the fixed-argv acts.
- Content-in-configuration: content lives in data; code renders.
- Never hand-edit cycle-generated files — the generated surfaces regenerate; the fix is a re-run.
- Questions open in the store (junro route add-question); dispatched opinions land as packet
  results with evidence files under the store's evidence home (.junro/evidence/{question-id}/) —
  never stray root directories.
- Patch is the one mutation verb: edit and write are denied; a unified diff applies under strict
  semantics and the type-appropriate checks ride the same output — fix findings in the same turn,
  never a batch pile."""
```

**(b) PRIORITREE_GOAL_LINE** — the ruled line verbatim (Q-harness's ruling, junro.json:431/436):

```
PRIORITREE_GOAL_LINE = (
    "To produce superior orderings from pairwise comparison: where humans and LLMs discern "
    "the difference between two items far better than they can size either one, Priori-tree "
    "stores those judgments as votes and tallies them into a ranked whole."
)
```

**(c) PRIORITREE_SPEC + the TARGETS entry** (after INPUT_SPEC, :396-409):

```
PRIORITREE_SPEC = TargetSpec(
    name="prioritree",
    label="Prioritree",
    root=REPO_ROOT.parent / "prioritree",
    adapter_path=REPO_ROOT / "scripts" / "generation" / "sources" / "prioritree-seats.yaml",
    adapter_rel="scripts/generation/sources/prioritree-seats.yaml",
    gen_by="scripts/generation/clarity_scaffold.py",
    goal_line=PRIORITREE_GOAL_LINE,  # ruled (Q-harness, 2026-11-19)
    goal_line_ruling="Q-harness's goal-line ruling (the collaborator, 2026-11-19)",
    law_md=PRIORITREE_LAW_MD,
    builtin_universe=KUMI_BUILTIN_UNIVERSE,
    hook_bypass="PRIORITREE_HOOK_BYPASS",
)
TARGETS: dict[str, TargetSpec] = {"clarity": CLARITY_SPEC, "input": INPUT_SPEC, "prioritree": PRIORITREE_SPEC}
```

Nothing else in clarity_scaffold.py changes — argparse choices and check FIX lines derive automatically (:683, :667). Zero core emission-inventory changes; zero engine-set changes (the fixed five derive from `_ENGINE_SOURCES`).

### 1.2 prioritree-seats.yaml — the adapter, exact bytes

The input-seats.yaml shape exactly (one-file join: genome identity fields + deltas + packs in one tracked hikari file; structural facts only, zero prioritree prose). Compose per these rules — jikko copies the input adapter and edits:

**Header comment block:** the input adapter's header form, adapted — title `prioritree-seats.yaml — the prioritree-target adapter (authored input, tracked in hikari)`; cite the derived-view ruling and the containment/identity-source rulings as at input-seats.yaml:3-33 with "prioritree" substituted; the law-block paragraph names PRIORITREE_LAW_MD; the pack-rows paragraph verbatim from input-seats.yaml:35-45.

**`seats:` — 13 rows.** For each seat, the input adapter's row VERBATIM (the genome fields kanji/gloss/question/refusal, identity, responsibilities, artifact_contract, placement — the family genome, byte-identical; togo's `modes_note` included) with exactly these substitutions per row (tree-specific deltas only):
- `shinko`: all fields verbatim; `pack: shinko`.
- `tansa`/`rikai`/`shindan`/`kensho`/`keisan`/`hyoka`: in `identity`, "the input tree" → "the prioritree tree"; `pack:` per the anchors below.
- `togo`: `identity`'s "the input tree's vocabulary" → "the prioritree tree's vocabulary"; `modes_note` verbatim.
- `keikaku`: `identity`'s "for the input effort" → "for the prioritree effort".
- `jikko`: `identity`'s "in the input tree" → "in the prioritree tree"; responsibilities line 1's path → `Edit code in /Users/marklosey/projects/prioritree directly — no worktrees, never hand-edit cycle-generated files (the .plans/ record home is read-only to this seat)`.
- `suisen`, `hansei`, `moho`: all fields verbatim (tree-neutral).
- `placement` lists: verbatim everywhere.

**`packs:` — the Q-harness rows, the input adapter's form verbatim** (input-seats.yaml:312-358): `shinko:` `task/question/friction/junro: []` (NO calculate); `tansa: &read_pack` with `friction/read/grep/glob/test: []` + `calculate: [add, subtract, multiply, divide, sum, count]`; `rikai/togo/shindan/keikaku/suisen/kensho/keisan/hyoka/hansei/moho: *read_pack`; `jikko: <<: *read_pack` + `patch: []` + `curate: [apply]`. The ruling comments ride verbatim.

## 2. THE PRIORITREE-SIDE WRAPPER LANDING (jikko, patch `--root /Users/marklosey/projects/prioritree`, same build session)

Seven tracked files at `prioritree/.opencode/tools/` — composed once, prioritree-owned (the tane amendment-354 end-state). Per-wrapper recipes (jikko composes, then read-backs the bytes):

**2.1 `_run.ts`** — VERBATIM COPY of `tane/.opencode/tools/_run.ts` (58 lines; cite that path). One change: the header's line 1 ownership stamp re-worded: `// prioritree-owned (.opencode/tools/_run.ts) — maintained by hand in prioritree's tree; composed 2026-11-19 from tane's amendment-354 helper (FR-MEM-0145's durable fix — the multiline-mangling fix's recorded provenance, tane/_run.ts:1-7)`. Body bytes 9-58 verbatim.

**2.2 The five engine wrappers** — base = hikari's CURRENT rendered wrapper (descriptions/args/ops verbatim; the authored source is hikari's manifest.yaml, frozen at composition). Common recipe per file:
1. Header: hikari's `@generated` line → `// prioritree-owned (2026-11-19, G-HARNESS-BRIEF): composed from hikari's current render + tane's channel; hand-maintained in prioritree's tree`.
2. Add `import { runArgv } from "./_run"`.
3. Keep the `formatOutput` helper, changing its `stderr: Buffer` type to `stderr: Buffer | string` (tane's form).
4. Delete the `Bun.$` line.
5. Channel substitution — every ``formatOutput(await $`uv run  python scripts/<engine>.py ${eargs}`.quiet())`` → ``formatOutput(await runArgv(["uv", "run", "python", ".opencode/scripts/<engine>.py", ...eargs], { cwd: context.directory }))`` (the engine re-point `scripts/` → `.opencode/scripts/`, tane/calculate.ts:41's form).
6. The `help` string: hikari's verbatim, with every `scripts/<engine>.py` → `.opencode/scripts/<engine>.py` and `test`'s "via Docker" → (nothing; see 2.2e).

Per-wrapper deltas:
- **calculate.ts**: recipe as-is; base hikari/.opencode/tools/calculate.ts (78 lines).
- **patch.ts**: recipe as-is; base hikari/patch.ts (48 lines) — the multiline `--diff` now rides the byte-preserving channel (the FR-MEM-0145 class cured at birth).
- **friction.ts**: recipe as-is; base hikari/friction.ts (188 lines); the `union` op's enum entry and help text ride verbatim (a prioritree-side union call fails loud at the lazy import — the banked verbatim-carry posture; the sibling script does NOT ride).
- **curate.ts**: recipe as-is; base hikari/curate.ts (54 lines).
- **test.ts**: base = **tane's** test.ts (tane/.opencode/tools/test.ts, 49 lines) NOT hikari's (hikari's is the make-target/Docker form; prioritree carries the engine and no Docker) — with tane's header stamp re-worded to the prioritree form above and the help text's engine path already `.opencode/scripts/` (verify: "run all tests or a single test file" — no Docker line). The `one` op's test_path is POSITIONAL (`eargs.push(args.test_path)`, the FR-MEM-0043 cure).

**2.3 junro.ts** (the cross-project form, amendment 21 ruling 1) — base = hikari's junro.ts (258 lines; hikari's 18-op enum — NOT tane's evolved 19-op render), same recipe as 2.2, EXCEPT the invocation: every ``runArgv(["uv", "run", "python", ".opencode/scripts/junro/junro.py", ...]`` becomes ``runArgv(["uv", "run", "--project", "/Users/marklosey/projects/kepric/hikari", "python", "/Users/marklosey/projects/kepric/hikari/scripts/junro/junro.py", ...eargs], { cwd: context.directory })`` — the engine stays home at hikari (deps resolve in hikari's env; prioritree's venv stays zero-runtime-deps); the session cwd stays prioritree so the ambient store walk-up finds prioritree's own hearts. Help-string engine paths → the hikari absolute path form.

- Hunk A (append after line 176, the Ruff block's end): the hikari trio with its comment form —
  ```
  # The derived-view substrate (hikari's trio form): the wrappers' plugin import must
  # resolve at opencode load; the pin file package.json is TRACKED (G-HARNESS's read-back names it).
  .opencode/node_modules/
  .opencode/package-lock.json
  .opencode/bun.lock
  ```
- Hunk B: line 178 `.junro/` → `/.junro/` (the amendment-21 root-anchor; the FR-MEM-0419 cure's form one line down — inert at prioritree, future store hearts tracked by default, G-FOUNDATIONS condition 5's words still literally satisfied).

## 3. THE COLLABORATOR'S HANDS (six steps, exact commands; no seat shells)

1. **Clarity restore** (amendment 21 ruling 3): from `/Users/marklosey/projects/kepric/hikari`: `uv run python scripts/generation/clarity_scaffold.py`
2. **Input re-emit** (the drift fix — the check's own FIX line): `uv run python scripts/generation/clarity_scaffold.py --target input`
3. **Prioritree emission-run**: `uv run python scripts/generation/clarity_scaffold.py --target prioritree`
4. **Substrate install**: `cd /Users/marklosey/projects/prioritree/.opencode && npm install` (or `bun install` — both lockforms are ignored)
5. **Prioritree-side commits** — the wrapper landing, the emission's artifacts, the .gitignore edits, the store records — through the collaborator's hand, one commit per increment (the landing rhythm)
6. **Live proof** — the friction birth-write at a prioritree seat (§5 below), then the read-back green.

## 4. THE SCOPE FENCE

- Hikari-side edit: the two files in §1 (spec constants + adapter) ONLY — no core emission-inventory changes, no engine changes, no generator (generate_tools.py) changes, no CI/DB/product logic.
- The wrapper set is the seven files of §2 (_run.ts + six). Every permission key has a wrapper: the fixed five ids match the pack keys; `junro` matches shinko's grant (the dead-grant class never rides); `task`/`question` are opencode harness builtins, not wrapper ids.
- The prioritree .gitignore edits are exactly §2.4's two hunks.
- The clarity fate question and the five-trees naming ride the close unit's lanes.

## 5. THE ACCEPTANCE CRITERIA (G-HARNESS's five conditions, with evidence lines)

1. **G-FOUNDATIONS closed green + the derived-view entries precede the emission** — evidence: the route record (packets.jsonl gate lines) + §2.4's hunks in the landed .gitignore before step 3 fires.
2. **The hikari-side edit green + sibling contracts** — evidence: `ruff`/`pyright` zero findings over clarity_scaffold.py (the YAML is data); §6's two sibling commands both exit 0.
3. **The prioritree emission whole and byte-true + the inventory read-back** — evidence: §6's `--check` exits 0 (24/24 artifacts: opencode.json 13 seat blocks/builtins disabled/shinko primary/closed-world deny; AGENTS.md @generated + the ruled goal line verbatim; .opencode/ package.json pins, tsconfig, the plugin, the fixed five verbatim, the 13 prompts; .githooks/pre-commit executable, PRIORITREE_HOOK_BYPASS, pyright) — PLUS the wrapper files (tracked tree assets, NOT `--check`-covered: their read-back is git + the load proof).
4. **The registration live** — evidence: the friction birth-write's recorded call answering at a prioritree seat (the write IS the proof — the registered wrapper answered). The entry is the seat's TRUTHFUL report of a real observed friction from the build session, never a fabricated one; schema fields per the tool's own law (surface, attempted/happened verbatim, both governed axes, severity, detectability).
5. **The friction store born + reads green + the two-tree hands** — evidence: `prioritree/.plans/state/friction-ledger.jsonl` EXISTS (a read on a missing file is green-but-birthless — the verification distinguishes) and `friction read` serves its line; the landing record names both hands (hikari-side through hikari's shinko-git choreography; prioritree-side through the collaborator's hand).

## 6. THE VERIFICATION COMMANDS (kensho re-runs at the gate)

From hikari's root (`/Users/marklosey/projects/kepric/hikari`):
```
uv run python scripts/generation/clarity_scaffold.py --target clarity --check
uv run python scripts/generation/clarity_scaffold.py --target input --check
uv run python scripts/generation/clarity_scaffold.py --target prioritree --check
```
At prioritree: the inventory read-back (the file list per criteria 3 + the seven wrapper files), `friction read` on the born store, the `--git/config` hooksPath read-back already standing.

## 7. ZERO OPEN QUESTIONS — the banked answers

- **The three rulings (amendment 21, junro.json:389-392, ruled 2026-11-19, all on rikai's recommendations):** (1) the junro grant goes LIVE via the cross-project wrapper (engine stays home at hikari through `--project`); (2) `.junro/` root-anchors to `/.junro/`; (3) the clarity tree RESTORES via the emit (§3 step 1).
- **The channel:** the explicit-argv `_run.ts` form (tane's), never hikari's Bun.$ template — the multiline-payload mangling class (FR-MEM-0145's recorded provenance at tane/_run.ts:1-7) is cured at birth.
- **The registration form:** (a-i) — prioritree-owned, tracked wrapper files (the tane amendment-354 end-state); filename = tool id auto-discovery; ids match the permission keys; the plugin pin rides the emitted package.json; node_modules installed (§3 step 4).
- **The gitignore trio:** hikari's form at the root file, package.json TRACKED.
- **The re-emit:** input refreshed by the collaborator's hand before the sibling check; the union op rides verbatim, its lazy import fail-loud, the sibling script does NOT ride.
- **The birth act:** ONE friction birth-write at a prioritree seat composing conditions 4+5, then the read-back.
- **The typechecker:** pyright (Q-typecheck-alignment, already ruled) — the hook aligns with the family template natively.

**The brief stands ready for the collaborator's G-HARNESS-BRIEF ruling; the build needs no deliberation after it.**
**2.4 The .gitignore edit** — `prioritree/.gitignore`, two hunks (BEFORE the emission fires, G-HARNESS condition 1):
