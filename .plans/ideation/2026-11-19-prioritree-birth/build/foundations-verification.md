**Session-start binding set (Clause 1, the session's first line):** visible tool surface enumerated verbatim — `acquire, calculate, content-query, docker, etl, friction, glob, read, list_mcp_resource_templates, list_mcp_resources, read_mcp_resource, regen, test` — reconciled against the pin's pack-routing table: the earned binding set (`acquire` acquire_dataset/acquire_group, `calculate`, `content-query`, `docker` logs/restart/status, `etl`, `friction`, `glob`, `regen` generate-tools, `test` all/one) matches exactly; the unearned set (`duckdb, edit, junro, lint, reflect, script, write`) is asserted ABSENT and confirmed absent from the visible surface; the harness trio is the out-of-band layer, unused this session (no MCP resource exercised — the gate is a prioritree-side read-back plus a captured-run adjudication; `hikari-local`/`hikari-prod` binding roles noted, unexercised). Instrument note, minor and named: the raw `kumi-manifest.yaml` is not locatable by glob in hikari's tree (only the kumi generation scripts live there); the pin's expression at this seat is the generated pack-routing table, which the reconciliation above used.

# validate/foundations — kensho's G-FOUNDATIONS gate verification

## 0. Provenance

- **Seat:** kensho (検証, verify) — packet `validate/foundations`, route `prioritree-birth`, dispatched 2026-11-19T18:26:18Z.
- **Date:** 2026-11-19.
- **Method:** the five gate conditions (route record `.junro/junro.json:184-192`, the store at `prioritree/.plans/ideation/2026-11-19-prioritree-birth/`) verified against the brief's acceptance criteria (`synthesize/foundations-brief.md` §4) — each leg's evidence labeled **[own read-back]** (this seat's instruments: read/glob/calculate over the prioritree tree) or **[captured run]** (the collaborator's verbatim terminal capture, `build/foundations-floor-green.md`, the hand named: marklosey@Mac, the prioritree root, 2026-11-19), or **[own corroboration]** (physical residue read back by this seat).
- **The instrument boundary, named:** NO seat holds a prioritree-side shell; this seat's `test` tool is hikari's Docker-bound runner — structurally unable to execute anything at the prioritree tree (firing it would run hikari's suite, theater rather than verification; not fired). The runtime legs therefore ride the collaborator's captured run as EVIDENCE — **never re-fabricated, never claimed as re-run**; each runtime leg is marked *verified against the captured run (instrument-blocked for seat-side re-run)*. The store's own capture document pre-ruled this form (its §0: "this captured run IS the runtime evidence; kensho's G-FOUNDATIONS verification reads it as such, never re-fabricating it").
- **The boundary held:** read-only beyond this single return — no writes, no store mutations, no filings, no config edits. The two ruff meta-warnings and the rider candidate are adjudicated and named below, never silently resolved or silently applied.

## 1. The chain — the store's own record: COHERENT

`packets.jsonl` (13 lines, read whole by this seat) — the pipeline packets complete, in order, artifacts present:

| Packet | Dispatched | Result | Artifact (verified present) |
|---|---|---|---|
| compose/prioritree-birth-route | 16:50:40Z | COMPLETE 17:06:13Z | `plan/keikaku-composition.md` ✓ |
| discover/foundations | 17:13:41Z | COMPLETE 17:27:20Z | `discover/foundations.md` ✓ |
| understand/foundations | 17:27:35Z | COMPLETE 17:57:05Z | `understand/foundations.md` ✓ |
| synthesize/foundations | 17:57:10Z | COMPLETE 18:15:29Z | `synthesize/foundations-brief.md` ✓ |
| **G-FOUNDATIONS-BRIEF** | — | **green** (packet 18:17:31Z; route 18:17:36Z) | — |
| build/foundations | 18:17:43Z | COMPLETE 18:20:55Z | the prioritree tree ✓ |
| validate/foundations (this packet) | 18:26:18Z | this return | — |

The pipeline law held on the record: the build dispatch (18:17:43Z) fires only after the brief gate went green (18:17:36Z). Every dispatch precedes its result; every result's artifact exists at the store; the brief's §4 acceptance criteria are keyed to the route's five conditions (§4.1↔:187, §4.2↔:188, §4.3↔:189, §4.4↔:190, §4.5↔:191 — compared, they agree).

## 2. Condition 1 — the environment: **PASS**

The pin agreement — **[own read-back]**, all four surfaces:
- `.python-version:1` = `3.13` (one line, trailing newline) ✓
- `pyproject.toml:6` `requires-python = ">=3.13"` ✓
- `pyproject.toml:50` `[tool.pyright] pythonVersion = "3.13"` ✓
- `pyproject.toml:17` `[tool.ruff] target-version = "py313"` ✓
- Agreement holds: 3.13 ↔ >=3.13 ↔ 3.13 ↔ py313; `uv.lock:3` `requires-python = ">=3.13"` concords.

The lock on disk — **[own read-back]**: 141 lines; header `version = 1` / `revision = 3` (lock:1-2); `prioritree 0.1.0` `source = { editable = "." }` (lock:51-53); dev group = pyright/pytest/ruff (lock:55-60); **11 `[[package]]` blocks** (counted: colorama, iniconfig, nodeenv, packaging, pluggy, prioritree, pygments, pyright, pytest, ruff, typing-extensions; arithmetic check via calculate: 11) ✓.

The runtime legs — **[captured run]**, *verified against the captured run (instrument-blocked for seat-side re-run)*:
- `uv lock`: "Using CPython 3.13.9 / Resolved 11 packages" — the pin resolved, 11 packages, matching the on-disk lock's count.
- `make dev` (uv sync): "Using CPython 3.13.9", venv created, "Built prioritree", `prioritree==0.1.0 (from file:///Users/marklosey/projects/prioritree)` in the install set — **the editable install**; "Installed 10 packages" (colorama is win32-marker-excluded in the lock — the 10/11 split is internally consistent); **zero warnings** in the output — the zero-and-zero bar met at this leg.

**[own corroboration]:** `.venv/pyvenv.cfg` read back: `version_info = 3.13.9`, `uv = 0.9.5`, `prompt = prioritree` — the venv's own record; the captured install list's ten versions match the lock's pins exactly.

**Catch, named (the untracked-lock state):** the lock is present on disk but **UNTRACKED** — the reflog (`.git/logs/HEAD`, read by this seat) shows the last commit `0e103a2` ("more packets", ~17:18Z) predates the build's completion (18:20:55Z); nothing since. The increment's commit — the eight files + `uv.lock` — is the **landing's own act at the gate's green** (the one-commit-per-increment rhythm, `junro.json:383`; the brief §3.4). The brief's §4.1 word "committed" names that landing, not a pre-gate state; the gate's own condition 1 (`junro.json:187`) requires "the environment reproducible from the lockfile" — the on-disk lock plus the captured sync satisfy it. Named, not smoothed.

## 3. Condition 2 — the smoke suite: **PASS**

The suite's shape — **[own read-back]**, compared byte-for-byte against the brief §1.6-1.8:
- `tests/test_smoke.py` (9 lines): the module docstring ("The born tree's smoke test — the import answers, the namespace lives."), `import prioritree` (used at :9 — no F401), the one `-> None` test `test_prioritree_imports` asserting `prioritree.__name__ == "prioritree"` ✓ — identical to §1.8.
- `tests/__init__.py` (2 lines): the INP001 declaration docstring — **presence, never a noqa** (zero noqa in the tree) ✓ — identical to §1.7.
- `src/prioritree/__init__.py` (2 lines): the namespace docstring; the `src/prioritree/` tree carries **only** `__init__.py` (glob-verified) — no subpackages, no product logic, the scope fence held ✓ — identical to §1.6.
- The suite's whole shape: exactly `__init__.py` + `test_smoke.py` under `tests/` ✓.

The runtime leg — **[captured run]**: "collected 1 item" → `tests/test_smoke.py . [100%]` → **"1 passed in 0.01s"**; **no warnings-summary** in the output — the zero-and-zero bar met. The datum named as data: `configfile: pyproject.toml` — pytest 9 anchors rootdir at the bare pyproject (no `[tool.pytest.ini_options]`, the banked bare form). The jikko-time no-venv datum (the unresolved import at build time) is **CLOSED** by the editable install: the test imports `prioritree` and passes.

**[own corroboration]:** `.pytest_cache/v/cache/nodeids` records exactly one node id — `tests/test_smoke.py::test_prioritree_imports`; `tests/__pycache__/test_smoke.cpython-313-pytest-9.2.0.pyc` — pytest 9.2.0 at CPython 3.13 ran at this tree.

## 4. Condition 3 — the quality floor: **PASS** (the meta-warnings adjudicated below)

The configs — **[own read-back]**, compared against the brief §1.1 (byte-identical, the whole 55-line file):
- **The ruff block:** `select = ["ALL"]` (:26) with the seed's strictness comment; the per-file-ignores carry **exactly one named ruling — R1**, `"tests/**" = ["S101", "PLR2004"]` (:33) with the ruling's reasoning in the comment; **zero convenience ignores** (no other ignore/extend-exclude entries in the file — read whole); INP001 closed by the declaration, never an ignore — **the zero-ignore law standing** ✓. Provenance corroborated **[own read-back]**: tane's precedent verified at `tane/pyproject.toml:89-96` (the ALL select) and `:105-112` (R1 with the same reasoning) — R1 is genuinely the family's settled ruling, inherited, not invented.
- **The pyright block:** `typeCheckingMode = "strict"`; `enableTypeIgnoreComments = false`; the no-suppression extras all `"error"` (reportImplicitStringConcatenation, reportUnnecessaryTypeIgnoreComment, reportCallInDefaultInitializer, reportUninitializedInstanceVariable, reportMatchNotExhaustive, reportDeprecated); `include = ["src", "tests"]`; `pythonVersion = "3.13"`; `venvPath`/`venv` set ✓ — the Q-typecheck-alignment ruling (PYRIGHT, `junro.json:430-442`) landed in bytes.

The runtime legs — **[captured run]**: `ruff check src/ tests/` → **"All checks passed!"** (zero findings, exit 0); `pyright` → **"0 errors, 0 warnings, 0 informations"** — the verbatim summary line exactly as banked; the `&&` chain's continuation past both proves both exited 0.

**THE ADJUDICATION — the two ruff CONFIG META-WARNINGS (D203/D211, D212/D213).** The facts: ruff's ALL-select carries mutually exclusive docstring pairs; ruff auto-resolves each (ignoring D203 and D213) and prints a config-class warning naming the resolution — both appear in the captured output, then "All checks passed!". **Ruling: NON-FINDINGS, NON-BLOCKING.** The brief's own criterion (§4.3) is "`ruff check src/ tests/` — **zero findings** ("All checks passed!")" — the warnings name no defect in `src/` or `tests/`; the findings count is zero; the exit is 0. The gate's own words (`junro.json:189`) match: "ruff zero findings over src/ and tests/". The zero-errors-AND-zero-warnings bar — the gate's spine — is named by the brief's criteria for the uv-sync leg (§4.1, met), the pytest leg (§4.2, met), and the pyright leg (§4.3, met verbatim at 0/0/0); the ruff leg's own bar is zero findings, met. The meta-warnings are a distinct class — config-resolution notices, the same class riding tane's own ALL select (corroborated by this seat's read of tane's config). Neither silently relaxed (the criterion is met on its own words; the warnings are named here) nor silently blocked (no criterion is invented stricter than the brief's). **THE RIDER CANDIDATE, named as data, never silent:** a future **named ruling** pinning the docstyle convention (selecting one member of each pair explicitly, in the zero-ignore law's ruling form) would silence both meta-warnings; it is NOT applied here — a config edit is the implementor's act under a brief, and this seat is read-only. Recorded for a future cycle.

## 5. Condition 4 — the Makefile floor: **PASS**

The Makefile — **[own read-back]**, compared against the brief §1.5 (byte-identical, the whole 18-line file):
- `.DEFAULT_GOAL := help` (:1) ✓; `.PHONY: dev test lint typecheck help` (:3 — **every target .PHONY**) ✓
- The four recipes match §1.5 exactly: `dev:` → `uv sync`; `test:` → `uv run pytest`; `lint:` → `uv run ruff check src/ tests/`; `typecheck:` → `uv run pyright`; the `help` recipe with the `$$` escapes ✓
- Family idiom corroborated **[own read-back]**: the help recipe is byte-identical to `hikari/Makefile:48-49`; `.DEFAULT_GOAL := help` matches `hikari/Makefile:1`.
- **TAB indentation:** the read-back shows the recipe lines tab-led; the decisive proof is runtime — GNU make exits non-zero ("missing separator") on space-indented recipes, and the captured chain ran all four targets to completion. A space-indented Makefile cannot produce the captured output. TAB law proven by the captured run, shape corroborated by the read.

The runtime leg — **[captured run]**: `make dev && make test && make lint && make typecheck` — the chain completed **through typecheck** and returned to the prompt; shell `&&` semantics — any non-zero exit would have stopped the chain — so **all four targets exited 0**. Datum named as data (the brief §3.3/§6.4 banks it): the route's recorded floor-green line (`junro.json:63`) is the three-target `make dev && make test && make lint`; the captured run adds the additive fourth — the recorded line remains literally true (all three ran, in order, exit 0), and the fourth exercises condition 3's checker leg through the floor. No route amendment required.

## 6. Condition 5 — the records read-back: **PASS** (all legs **[own read-back]**)

- **`.gitignore` (178 lines, read whole):** the github Python template complete (every section, `# ---> Python` through `.pypirc`) with **`.junro/` as the final line** (:178) ✓; the derived-view entries (`.opencode/`, node_modules, etc.) **honestly ABSENT** ✓ — harness-scope, sequenced to land with the harness unit before its emission (G-HARNESS condition 1 depends on that landing); the brief §1.3's datum (input's QMK appendage excluded) honored; the template's `# .python-version` and `#uv.lock` stay commented ✓. The route's condition-5 parenthetical ("the derived-view entries the harness discovery confirms") is sequenced by the approved brief: foundations lands the Python set + `.junro/`; the harness unit lands the derived-view entries before its emission. The absence at this gate is the ruled state.
- **`README.md` (22 lines, read whole):** carries **Q-purpose's ruled description** — :3 is the resolution line **byte-identical** to `junro.json:397` (compared); :5 the comparator-class line; :7-9 the ruling blockquote **verbatim** — byte-identical to `junro.json:392`'s ruled passage, the collaborator's own words preserved exactly (including the ruling's own "comparision" spelling), cited "— the collaborator's Q-purpose ruling, 2026-11-19 (verbatim)"; the Architecture section carries Q-setup-arch's four-form layering; the Status-at-birth section names honestly what exists and what does not ✓.
- **`.git/config`:** `hooksPath = .githooks` at **:8, inside the `[core]` block** ✓ — the pointer landed (the collaborator's hand, no output = success in the capture). The hook file is **honestly NOT present** — no `.githooks/` in the tree (glob-verified) — the **hookless window**, named: the pointer is inert/fail-open until the harness unit emits the hook file next.

## 7. The catches — all named as data, none smoothed

1. **The two ruff config meta-warnings** (D203/D211, D212/D213) — adjudicated **non-findings, non-blocking** per the brief's own words (§4.3: zero findings = "All checks passed!"); the rider candidate (a future named docstyle ruling) recorded, never silently applied.
2. **The configfile datum** (`configfile: pyproject.toml` in the pytest output) — the bare-form rootid anchor, by design (no `[tool.pytest.ini_options]`, the banked tane form).
3. **The untracked-lock state** — the lock on disk, uncommitted; the increment's commit (the eight files + `uv.lock`) is the landing's own act at the gate's green; the reflog corroborates no post-build commit. The brief's "committed uv.lock" describes the post-green landing, and the gate's own condition-1 words are satisfied by the on-disk lock plus the captured sync.
4. **The instrument boundary itself** — the runtime legs are not seat-side re-runs (no seat holds a prioritree-side shell); each is verified against the collaborator's captured run, marked instrument-blocked for seat-side re-run; the physical residue (the venv's pyvenv.cfg at 3.13.9/uv 0.9.5, the pytest-9.2.0/cpython-313 pycaches, the nodeids cache, the .ruff_cache) is this seat's corroboration that the captured run happened at this tree — corroboration named as corroboration, never as re-run.

## 8. THE VERDICT: **GREEN**

All five conditions PASS on their evidence; the chain is coherent on the store's own record; the zero-errors-AND-zero-warnings bar is held at every leg where the brief's criteria name it (uv sync: zero warnings; pytest: 1 passed, no warnings-summary; pyright: 0 errors, 0 warnings, 0 informations, verbatim); the ruff leg's own criterion (zero findings) is met verbatim with the meta-warnings adjudicated against the brief's own words and the rider candidate named. **G-FOUNDATIONS is green.** The gate's ruling — the packet gate and the close-gate at G-FOUNDATIONS on the route — follows this verdict (shinko's recording; the increment's one commit, the eight files + `uv.lock`, lands at the green through the collaborator's hand).

**Boundary held to the last line: read-only — no writes, no store mutations, no filings. This document is the single return; shinko lands it verbatim.**
