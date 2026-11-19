# understand/foundations — the foundations unit's mechanism analysis

## 0. Provenance

- **Seat:** rikai (理解, understand) — packet `understand/foundations`, route `prioritree-birth`, unit `build/foundations`; the dispatch record confirmed at store/.junro/packets.jsonl:5 (shinko, 2026-11-19T17:27:35Z).
- **Date:** 2026-11-19.
- **Method:** the ground read in the ruled order (tansa's census `discover/foundations.md` → the composition brief `plan/keikaku-composition.md` → the store's rulings `.junro/junro.json`), then every load-bearing claim verified at its source by direct read: tane's 226-line pyproject whole, input's pyproject + hooks + lock header + init files, hikari's pyproject (:1-15, :140-217) + Makefile + dev.mk/test.mk/lint.mk/hooks.mk, both sibling .git/configs, prioritree's .git/config, tane's init/tests/conftest/test grammar. Mechanism derivation over the measured facts; the census's measurements treated as ground truth, NOT re-run — only verified where a mechanism judgment leaned on a specific line.
- **Boundary held:** read-only — no writes anywhere, no store mutations, no friction filings (the friction tool unused entirely; the test tool unused — no execution needed, every question settled at source + census). Reads, citations, and mechanism reasoning only. Held.
- **Session binding set (session-start law, Clause 1):** visible surface enumerated verbatim at session start — `calculate, content-query, friction, glob, list_mcp_resource_templates, list_mcp_resources, read, read_mcp_resource, test` — reconciled against the pin: the earned binding set (`calculate`/`content-query`/`friction`/`glob`/`test`) matches the pack-routing table exactly; the nine unearned tools (code-graph-context, edit, etl, junro, reflect, script, symbol-lookup, web, write) confirmed ABSENT from the visible surface. **Manifest datum, named honestly:** `kumi-manifest.yaml` is not glob-visible in hikari's tree (glob `**/kumi*` returns only the generation scripts `kumi_*.py`); the pin was reconciled against the pack-routing table carried verbatim in the seat prompt (the generated artifact of that manifest — its header names `scripts/generation/kumi_prompts.py`); per Clause 1 the enumeration IS the instrument — binding set clean, zero drift.
- **Tree roots (citations are tree-relative):** `store/` = `/Users/marklosey/projects/prioritree/.plans/ideation/2026-11-19-prioritree-birth` · `input/` = `/Users/marklosey/projects/kepric/kepric-input` · `tane/` = `/Users/marklosey/projects/kepric/tane` · `hikari/` = `/Users/marklosey/projects/kepric/hikari` · `prioritree/` = `/Users/marklosey/projects/prioritree`.
- **Tier vocabulary (evidence discipline):** **T1** measured-at-source this session (path:line cited) · **T2** census-carried (tansa's measurement, cited to the census) · **T3** ruled (the store's ruling records) · **T4** mechanism-derived (reasoning over T1–T3, the derivation named — never bare speculation). All claims dated 2026-11-19.

## 1. The six mechanisms, banked at a glance

| # | Mechanism | BANKED ANSWER | Head precedent |
|---|---|---|---|
| 1 | pyproject/uv | Library-first pyproject, zero runtime deps, dev group `["pytest","pyright","ruff"]` bare, hatchling + `packages=["src/prioritree"]`; pin **3.13** agreeing across four surfaces; `uv lock` run by **the collaborator's hand at the build, between project-floor and floor-green** | input/pyproject.toml:1-6,37-42; tane/pyproject.toml:60-65,218; hikari/pyproject.toml:3 |
| 2 | pyright | tane's strict block verbatim + `include=["src","tests"]` + **`pythonVersion="3.13"` SET** + `venvPath`/`venv`; born-green 0/0/0 achievable; the bar's teeth = exit code (errors) **plus the summary-line read-back (warnings+informations)** | tane/pyproject.toml:202-215; hikari/pyproject.toml:199-202 |
| 3 | ruff | **tane's tier: `select=["ALL"]`** with exactly ONE named ruling inherited — R1 `"tests/**" = ["S101","PLR2004"]`; INP001 closed by the **declaration** (tests/__init__.py present+docstringed), never an ignore; py313/120/`["src"]`/double | tane/pyproject.toml:96,106-112,199-200; tane/tests/__init__.py:2-19 |
| 4 | Makefile floor | Single root Makefile, no make/ dir; bare `uv run` recipes; `.PHONY` on all; **help target INCLUDED** (`.DEFAULT_GOAL := help`); **the hikari split** — `lint`=ruff, `typecheck`=pyright as a fourth target; floor-green runs the route's three **plus `make typecheck`** | hikari/Makefile:1,47-49; hikari/make/lint.mk:188-198 |
| 5 | hooks | Foundations = the **config pointer only** (`git config core.hooksPath .githooks`, the collaborator's hand); the pointer with no hook file is **inert, fail-open** — the gate's read-back records the config key, not a hook execution; foundations-before-harness is load-bearing three ways | junro.json:58,191,197; tane/.git/config:8; input/.githooks/pre-commit:5-7,28-29 |
| 6 | skeleton + smoke | `src/prioritree/__init__.py` = **tane's 2-line form** (input's empty form CANNOT pass D104 under ALL); smoke test = docstring + `import prioritree` + one `-> None` test + one assert; tests/__init__.py **present-and-declared**; **no conftest, no pytest ini_options** at birth | tane/src/tane/__init__.py:1-2; tane/tests/test_readme.py:1-16; input/tests (empty form, out-tier) |

**Open edges for togo: ZERO** (§9) — the census's three brief-level edges (§6.1-6.3 of the census: the pin spread, lint/typecheck composition, the smoke shape) are all closed by the banks below.

---

## 2. Mechanism 1 — the pyproject/uv mechanics

**[CLAIM]** A minimal library-first pyproject of the banked shape makes `uv sync` + `make dev/test/lint` work greenfield with zero runtime dependencies; the lock is generated by `uv lock` at the build by the collaborator's hand; the Python pin is 3.13 and must agree across four surfaces. [SOURCE input/pyproject.toml:1-6,37-42,56-61 | T1 | 2026-11-19] [SOURCE tane/pyproject.toml:60-65,217-218 | T1] [SOURCE hikari/pyproject.toml:3 | T1] [SOURCE store/.junro/junro.json:397,405 | T3]

**The answer — the banked [project] block and its reasoning:**

- `name = "prioritree"`, `version = "0.1.0"` (hikari's measured birth version, hikari/pyproject.toml:3 — both elder siblings' first recorded version; input is at 0.3.0, its maturity), `description` = Q-purpose's resolution line verbatim (the census's bank, §3.1; the ruled words at store/.junro/junro.json:397 — nothing invented), `readme = "README.md"` (input/pyproject.toml:5 — the named precedent carries the key; hikari omits it, but input is the named precedent and G-FOUNDATIONS condition 5 reads the README — the key binds the file into the project's declared surfaces), `requires-python = ">=3.13"` (input/pyproject.toml:6, exact form).
- **`dependencies = []` — zero runtime deps at birth**: the pure-logic ruling (Q-setup-arch: "Data plane = pure logic: stateless scoring/ranking core, votes are data in/out, no DB at birth", store/.junro/junro.json:405). The empty array states the ruling in bytes — the venv at birth carries only the dev group + the editable project itself, and the lock stays small.
- **No `[project.scripts]` at birth** — the CLI is the product effort's layer over the core (junro.json:51's skeleton ruling; input's scripts stanza at input/pyproject.toml:34-35 is its v0.1+ maturity, not the skeleton's).
- **Build system: hatchling + the wheel stanza** — `[build-system] requires = ["hatchling"] / build-backend = "hatchling.build"` + `[tool.hatch.build.targets.wheel] packages = ["src/prioritree"]` (input/pyproject.toml:37-42 and tane/pyproject.toml:60-65, both siblings' identical form). The stanza is load-bearing beyond wheel builds: **`uv sync` installs the project itself as an editable install, and the editable mapping `prioritree → src/prioritree` is what resolves `import prioritree` for BOTH pytest and pyright** (mechanism: uv installs the root project editable by default; `uv run` activates the venv; pyright/pytest resolve first-party imports through site-packages). This is proven live at tane — 121 test files importing `tane`, NO pytest `pythonpath` config, NO pyright `venv` config, strict pyright passing 0/0/0 — the editable install carries the resolution (tane/pyproject.toml:64-65,215,218; measured absence of ini_options over the full file). [T4]
- **The dev group, bare names:** `[dependency-groups] dev = ["pytest", "pyright", "ruff"]` — tane's set (tane/pyproject.toml:218) minus `pyinstaller` (tane's PyInstaller binary-delivery need, its root entry.py — not prioritree's) and minus `pytest-asyncio` (no async at birth). Bare names, not floors: the committed `uv.lock` pins exact versions — the lock IS the reproducibility pin (input's floors at :56-61 are belt; tane's bare form is the leaner live precedent). **Mechanism:** `uv sync` installs the `dev` dependency group by default (uv's default-groups), which is why `make dev: uv sync` needs no `--extra`/`--group` flag — tane's dev group resolving `uv run pyright` with no Makefile at all is the live proof. [T4]
- **Not carried, named:** no `[tool.uv.index]`/`[tool.uv.sources]` (tane's :220-226 exist for its private-registry `kepric-decomp` dep — prioritree has no private deps); no pytest stanza (Mechanism 6); ruff/pyright stanzas per Mechanisms 2-3.

**The .python-version pin — BANKED: `3.13`, one line.** Reasoning: (a) the gate REQUIRES the file and its resolution (G-FOUNDATIONS condition 1: "the pinned Python resolved from `.python-version`", store/.junro/junro.json:187); (b) the named precedent tree pins 3.13 (input/.python-version:1, measured `3.13` — T1); (c) the family is otherwise split — hikari 3.12 (hikari/.python-version:1, the older floor tree) and tane unpinned (no file — the outlier the census's §6.1 divergence names); (d) 3.13 is the family's forward pin (the most recent scaffolded sibling's measured choice). **The agreement law, banked as four surfaces:** `.python-version` = `3.13` ↔ `requires-python` = `>=3.13` (the pin satisfies the floor; no surface allows less than the pin) ↔ `[tool.pyright] pythonVersion = "3.13"` (Mechanism 2) ↔ `[tool.ruff] target-version = "py313"` (Mechanism 3). Mechanism: uv reads `.python-version` as the project's interpreter (downloading a managed 3.13 if the host lacks it — the pin is runnable on any host); `pythonVersion` fixes pyright's checked language surface against interpreter drift; `target-version` fixes ruff's idiom bar (UP rules to py313 forms). [T4]

**uv.lock — what, who, when.** What: `uv lock` resolves the full graph (the project + the dev group + transitives — pytest's pluggy/iniconfig/packaging, ruff's standalone wheel, pyright's pip wrapper) into `uv.lock` with the header `version = 1 / revision = 3 / requires-python = ">=3.13"` mirroring the pyproject floor (input/uv.lock:1-3, T1 — prioritree's birth lock will be tens of lines, not input's 2197: zero runtime deps). **WHO: the collaborator's hand — NOT jikko.** jikko's kumi pack per the Q-harness ruling carries read/glob/grep/calculate/friction/test + patch/curate (store/.junro/junro.json:418) — file verbs, **no shell**; and the route's own words name the hand for the other shell act ("the collaborator's hand sets git config core.hooksPath=.githooks — the no-seat-shelling rule", junro.json:58). **WHEN: at the build, after the project-floor files land and before floor-green** — the census §3.3's "generated at the build," made precise: the lock derives from pyproject + .python-version, so it fires after project-floor; floor-green's `make dev` (`uv sync`) then consumes the committed lock and proves reproducibility (G-FOUNDATIONS condition 1: "the environment reproducible from the lockfile", junro.json:187). The floor-green deterministic step itself (junro.json:61-64) runs by the same hand — the two-tree hands rule: prioritree-side commits and commands through the collaborator's hand until prioritree's own landing rule exists (plan/keikaku-composition.md:56).

**jikko's dispatch must carry (Mechanism 1):** the exact pyproject bytes (§10), `.python-version` = `3.13`, and the hands-split line for the dispatch text: *jikko writes the files; the collaborator's hand runs `uv lock` (after project-floor lands, before floor-green) and commits the lock at the root; the same hand runs the floor-green line and sets the hooksPath pointer.*

---

## 3. Mechanism 2 — the pyright mechanics

**[CLAIM]** Tane's strict block is the config precedent; a three-file skeleton passes it born-green 0/0/0 under four load-bearing conditions; the 0-errors-AND-zero-warnings bar rides pyright's exit code for errors PLUS the summary-line read-back for warnings and informations — the grep the family hook uses exists precisely because the exit code under-enforces. [SOURCE tane/pyproject.toml:202-215 | T1 | 2026-11-19] [SOURCE input/.githooks/pre-commit:5-7,28-29 | T1] [SOURCE store/.junro/junro.json:189,373 | T3]

**The answer — the banked [tool.pyright] block** (tane's shape, verified verbatim at tane/pyproject.toml:202-215, adapted: `include` without tane's frozen engine; `pythonVersion` SET; the environment pair added):

```toml
[tool.pyright]
typeCheckingMode = "strict"
enableTypeIgnoreComments = false
reportImplicitStringConcatenation = "error"
# THE PYRIGHT TWIN (the no-suppression law's other half; tane/pyproject.toml:206-210
# the precedent): dead type-ignore comments are reported lies, not tolerated text.
reportUnnecessaryTypeIgnoreComment = "error"
reportCallInDefaultInitializer = "error"
reportUninitializedInstanceVariable = "error"
reportMatchNotExhaustive = "error"
reportDeprecated = "error"
include = ["src", "tests"]
pythonVersion = "3.13"
venvPath = "."
venv = ".venv"
```

- **What strict + the no-suppression extras mean for a two-file-plus-smoke skeleton:** strict turns every reportable diagnostic class to error (unused imports, implicit Optional, unknown types where they flow); the twin `enableTypeIgnoreComments = false` + `reportUnnecessaryTypeIgnoreComment = "error"` **bans suppression outright** — a `# type: ignore` both fails to suppress AND is itself reported. **Born-green 0/0/0 is achievable** at `src/prioritree/__init__.py` (docstring only — nothing to check), `tests/__init__.py` (docstring only), and `tests/test_smoke.py` (one import, used; `__name__` is `str`, fully known; no calls, no classes, no matches). [T4, derivation: the only imports at birth are first-party `prioritree` (pyright checks it from source — no stub needed) — tane's live tree proves the class: strict pyright passing over tests importing `tane` with no venv config in its block.]
- **What would violate it** (the dispatch's question, answered): any `# type: ignore` anywhere (double-faulted); an unused import (reportUnusedImport is error in strict — the smoke test's single import must be used, as the assert uses it); implicit-Optional defaults (`x: str = None`); an untyped third-party import (reportMissingTypeStubs is error in strict — none exist at birth: the only import is first-party); and — for the 0/0/0 bar — ANY diagnostic, **informations included**.
- **`include = ["src", "tests"]`** — tane's form (tane/pyproject.toml:215) minus `scripts/junro` (tane's frozen engine; prioritree has no scripts dir at birth). Tests ARE included: the family bar type-checks the test suite (tane's precedent; the gate's condition 3 covers the tree's quality floor whole).
- **`pythonVersion` — BANKED: SET to "3.13".** tane omits it — but tane omits the entire pin discipline (no .python-version either; its omission is its unpinned stance, not a strictness precedent); hikari SETS it (`pythonVersion = "3.12"`, hikari/pyproject.toml:200) and hikari is the only tree that both pins and type-checks. Reasoning: the pin must agree across surfaces (Mechanism 1's law), and setting it makes pyright's checked surface independent of interpreter drift — protecting kensho's independent runs and any bare invocation. **`venvPath = "."` / `venv = ".venv"` — BANKED: SET** (hikari's pair, :201-202): pins pyright's import resolution to the project's own venv deterministically; the future hook's `uv run pyright` finds the same venv either way (uv activates it), so the pair is coherent with every invocation form. [T1 precedents; T4 choice]
- **The 0-errors-AND-zero-warnings bar's mechanics:** pyright exits 1 on error-level diagnostics; **warnings alone exit 0** — the exit code under-enforces the bar. The family hook therefore greps the output line **"0 errors, 0 warnings, 0 informations"** verbatim (input/.githooks/pre-commit:28-29; tane's identical :58-59) — the grep is what makes a warning fail the commit. The same line is the gate's condition-3 read-back datum: kensho's independent run reads pyright's summary line, not just the exit code. One verification note the brief must carry so the read-back is unambiguous: **the pip wrapper's "new pyright version available" notice (stderr, out-of-band — hikari documents the class and silences it via `PYRIGHT_PYTHON_IGNORE_WARNINGS=1`, hikari/make/lint.mk:41-47) is not a checker diagnostic** — the read-back datum is pyright's own summary line. [T1/T4]

**jikko's dispatch must carry (Mechanism 2):** the exact block above; the note that pyright lands in the dev group (Mechanism 1) and in the Makefile as `typecheck` (Mechanism 4); the verification note naming the summary line as the condition-3 read-back datum.

---

## 4. Mechanism 3 — the ruff mechanics

**[CLAIM]** The banked tier is tane's `select=["ALL"]` — but the census's "can pass 0/0 with no ignores" is CORRECTED by the measured evidence: an asserting test file cannot pass ALL with zero ignores. The banked config is ALL + exactly ONE named ruling inherited — R1 (`"tests/**" = ["S101","PLR2004"]`) — and INP001 is closed by the declaration (present-and-declared tests/__init__.py), never an ignore. [SOURCE tane/pyproject.toml:96,106-112 | T1 | 2026-11-19] [SOURCE tane/tests/__init__.py:2-19 | T1] [SOURCE tane/tests/test_readme.py:1-16; tane/tests/test_marker.py:1-13; tane/.githooks/pre-commit:18-21 | T1] [SOURCE store/.junro/junro.json:189 | T3]

**The answer — the banked ruff config** (the whole block; tane's stance, birth-scale):

```toml
[tool.ruff]
target-version = "py313"
line-length = 120
src = ["src"]

[tool.ruff.lint]
# THE SEED'S OWN STRICTNESS (tane/pyproject.toml:90-96 the precedent): every rule on;
# the ONLY exceptions are NAMED RULINGS — where a rule's intent and a stated law
# of the tree genuinely disagree, the disagreement goes to a ruling — never resolved
# silently. Nothing else is ignored, ever.
select = ["ALL"]

[tool.ruff.lint.per-file-ignores]
# RULING R1 (inherited from tane/pyproject.toml:106-112, the family's settled ruling):
# assert IS pytest's assertion form — S101's intent (assert stripped under -O) never
# applies to tests. R1's second limb: the tests' assertions compare against concrete
# expected values — the literals ARE the specification under test. PLR2004 rides R1.
"tests/**" = ["S101", "PLR2004"]

[tool.ruff.format]
quote-style = "double"
```

- **The tier — BANKED: tane's ALL.** Reasoning: (a) the zero-ignore law binds either tier (G-FOUNDATIONS condition 3: "an ignore is a ruling, never a convenience", store/.junro/junro.json:189) — the law is about the DISCIPLINE, not the count; (b) a born-green skeleton has zero backlog by construction — ALL forces every future finding into the named-ruling lane from day one, exactly the discipline the gate's words demand; (c) input's defaults tier (input/pyproject.toml:44-46) is the weaker named-precedent form and would leave the born tree un-strict; hikari's curated select (hikari/pyproject.toml:150-156) is a hand-maintained subset — a moving target of remembered rules. ALL is the only tier whose exceptions are all rulings by construction.
- **The verification the dispatch demanded — does ALL pass zero-ignores over the three skeleton files? The measured answer: NO, not literally.** The empirical proof is tane's own R1, carried live in the strictest tree: `"tests/**" = ["S101", "PLR2004"]` (tane/pyproject.toml:112) with its recorded ruling (:106-111 — "assert IS pytest's assertion form… the literals ARE the specification under test"). The smoke test's shape is gate-mandated ("at least one passing test importing src/prioritree", junro.json:188; the dispatch's ruled shape carries one assertion) — and an asserting test fires S101 (and the name-comparison fires PLR2004). **The zero-ignore law is satisfied honestly by inheriting R1 as a named ruling with its reasoning carried in the config comment** — the census's "no ignores" claim held only for the non-test skeleton; the correction is recorded here (§8, contradiction note 1). Every other tane ruling (R2-R14: subprocess acts, broad catches, function-local imports, rendered-prose line lengths, complexity classes, doctrine messages, naming) names surface classes that DO NOT EXIST in a three-file skeleton — none applies at birth.

**The specific rules most likely to bite a skeleton — named, with their settled answers:**

| Rule | Bite | BANKED answer | Precedent |
|---|---|---|---|
| **S101 / PLR2004** | the smoke test's assert + literal comparison | R1 named ruling (tests/**) | tane/pyproject.toml:106-112 |
| **INP001** | `tests/test_smoke.py` if tests/ lacked `__init__.py` (implicit namespace package) | **the declaration, present-and-declared — never an ignore, never a noqa**: tests/__init__.py exists, docstringed | tane/tests/__init__.py:2-19 — "never a noqa, the declaration the fix" (:8) |
| **D104** (undocumented-public-package) | an EMPTY `src/prioritree/__init__.py` or `tests/__init__.py` | the docstring forms (Mechanism 6); input's empty form CANNOT pass the banked tier | input's empty init passes only because input selects defaults (input/pyproject.toml:44-46); tane's docstringed init passes ALL |
| **D100 / ANN201** | a bare test module (no docstring; `def test():` without `-> None`) | the smoke test carries a module docstring + `-> None` | tane's mature grammar (test_readme.py:2,12) vs its old bare files standing in the sequenced "docstring sweep" backlog its hook names (tane/.githooks/pre-commit:18-21) — a born-green tree cannot afford a backlog, so the mature grammar is the only bankable form |
| **D401/D400/E501** | docstring mood, first-line period, line length | the family grammar: "Pin the …" test docstrings; periods; ≤120 | tane/tests/test_readme.py:13,20 (all "Pin the …"); tane/pyproject.toml:69 |

**target-version / line-length / src / quote-style — BANKED each:** `py313` (the pin — both elders pin their own: tane py312 at :68, hikari py312 at :151; prioritree's target must match Mechanism 1's pin) · `line-length = 120` (both elder siblings agree — tane/pyproject.toml:69, hikari/pyproject.toml:152) · `src = ["src"]` (tane :87, hikari :153 — the first-party detection root) · `quote-style = "double"` under `[tool.ruff.format]` (tane :199-200 — banks the tree's canonical style for any future `ruff format` run; the floor itself runs `ruff check` only). **Not carried:** `extend-exclude` (tane's excludes are its frozen-engine/superseded-infra needs, tane/pyproject.toml:79-86; input's pb2 exclude is its gRPC need — prioritree has neither, census §4) and `[tool.ruff.lint.pylint] max-args` (tane's execute()-shape ruling — no function at birth carries >6 args; the setting births with its ruling when needed).

**One drift note for the record:** ALL's rule set grows with ruff versions — the committed lock pins the exact ruff at birth, so birth-green is reproducible; a future ruff upgrade re-runs the bar, and any new firing is ruled then, never silently ignored. [T4]

**jikko's dispatch must carry (Mechanism 3):** the exact block above (R1's comment included verbatim-adapted); the scope line — the floor recipe checks `src/ tests/` only (hikari's LINT_PATHS form, hikari/make/lint.mk:188).

---

## 5. Mechanism 4 — the Makefile floor mechanics

**[CLAIM]** The floor is a single root Makefile (no make/ directory), bare `uv run` recipes (no Docker — prioritree has no compose plane), .PHONY on every target, the ##-comment help grammar with the help target INCLUDED, and the hikari split: `lint` = ruff, `typecheck` = pyright as a fourth target — with the brief's floor-green run extending the route's recorded three-target line by the additive fourth, satisfying the gate's condition 4 (dev/test/lint exit 0) and condition 3 (the ruled checker at zero) honestly and separately. [SOURCE hikari/Makefile:1,29-49 | T1 | 2026-11-19] [SOURCE hikari/make/dev.mk:76-77,79-80; hikari/make/lint.mk:188-198 | T1] [SOURCE store/.junro/junro.json:63,187-191 | T3]

**The answer — the banked Makefile (the whole file):**

```make
.DEFAULT_GOAL := help

.PHONY: dev test lint typecheck help

dev:       ## Sync the environment (project + dev group, from the lock)
	uv sync

test:      ## Run the test suite
	uv run pytest

lint:      ## Ruff over src/ and tests/
	uv run ruff check src/ tests/

typecheck: ## Pyright over the tree's [tool.pyright] include set
	uv run pyright

help: ## Show this help
	@grep -hE '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
```

- **Single root, no make/ directory:** hikari's include chain over 17 `make/*.mk` files (hikari/Makefile:29-45) is its maturity; at floor scale the single file is the same idiom's minimal form (the census's §3.10 ruling, banked here).
- **The recipes via bare `uv run`:** hikari's `test`/`lint` recipes are compose-exec (hikari/make/test.mk:5-6 — `$(COMPOSE) exec hikari pytest tests/`; lint.mk's docker channel) — prioritree has NO Docker (census §4's not-carried set); the host-local channel is the recipe precedent (`uv run …`, the measured local-channel form at lint.mk:20-28,49 — prioritree's simpler form drops hikari's `--active --no-sync`, which exist for hikari's worktree/multi-tree discipline, not a single-tree floor). `dev: uv sync` — NOT hikari's `uv sync --extra dev` (dev.mk:77): that flag is hikari's optional-dependencies form (its dev tools live in `[project.optional-dependencies]`, hikari/pyproject.toml:70-76); prioritree's dev tools live in `[dependency-groups]`, which `uv sync` installs by default (Mechanism 1). `test: uv run pytest` — bare discovery from the rootdir: pytest skips dot-directories by default, so `.plans/` and `.venv/` are never scanned; the tree's only collectible path is `tests/`. `lint` = `ruff check src/ tests/` (hikari's LINT_PATHS form, lint.mk:188,192). `typecheck` = `uv run pyright` — bare, the include set from pyproject (hikari's typecheck form, lint.mk:197-198); errors fail by exit code, and the warnings+informations legs are the gate's summary-line read-back (Mechanism 2) — the grep belt arrives mechanically with the harness unit's hook (input/.githooks/pre-commit:29).
- **.PHONY discipline — BANKED: every target phony** (hikari's own form: `.PHONY:` lines at dev.mk:12, test.mk:3, lint.mk:74; none of the floor targets corresponds to a real file, and phony-ness makes them immune to same-named files forever).
- **The help target — BANKED: floor-green NEEDS it.** Three reasons: (1) `.DEFAULT_GOAL := help` (hikari/Makefile:1) is a SAFETY guard — without a default goal, bare `make` runs the first declared target (`dev`), silently re-syncing; with help as default, bare `make` prints the menu; (2) the `##` comments are inert decorations without the grep target (hikari/Makefile:47-49 — copy verbatim, it greps `$(MAKEFILE_LIST)` and is tree-agnostic); (3) it is the named idiom's root form, at three lines of cost. The `##` grammar rides every recipe line (`target: ## Description` — dev.mk:76's form).
- **lint vs typecheck composition — BANKED: the hikari SPLIT (the divergence-3 answer).** `lint` = ruff alone; `typecheck` = pyright alone as a fourth floor target. Reasoning: (a) it is the named idiom's own shape — hikari keeps them as separate targets with separate path variables (lint.mk:188-198), and the banked floor names come from the same idiom; (b) the gate itself decomposes the legs — condition 4 names dev/test/lint, condition 3 holds the ruled checker separately (store/.junro/junro.json:189-190) — the floor mirroring the gate's own decomposition is the honest form; (c) the family hook treats pyright as its own check (input/.githooks/pre-commit:28-29); (d) orthogonal failure surfaces — a ruff finding and a pyright error each fail with their own clean signal. **How this satisfies both gate conditions honestly:** the route's recorded floor-green line (`make dev && make test && make lint`, junro.json:63) runs UNCHANGED and exits 0 on all three — condition 4's words hold exactly as recorded; the brief's dispatch extends the RUN with the additive `make typecheck` so condition 3's pyright leg is exercised through the floor too; kensho's condition-3 read-back reads the summary line (Mechanism 2). No route amendment needed — the recorded line remains literally true, and the fourth target is additive belt.

**jikko's dispatch must carry (Mechanism 4):** the exact bytes above; the floor-green run line for the collaborator's hand — `make dev && make test && make lint && make typecheck` (the route's recorded three + the additive fourth); the note that no `format`/`lock`/`uv-install` targets exist at floor scale (hikari's uv-lock target, dev.mk:79-80, is the precedent for the collaborator's bare `uv lock`; a format target births when ruled — the format config is already in pyproject).

---

## 6. Mechanism 5 — the hooks mechanics

**[CLAIM]** Foundations' step is the config pointer ONLY — `git config core.hooksPath .githooks`, set by the collaborator's hand; the pointer with no hook file yet is INERT and fail-open (git runs a hook only when the file is present at the path — the pointer alone never raises), so the gate's condition-5 read-back records the config key, not a hook execution; foundations-before-harness is load-bearing for three mechanical reasons, chief among them that the emitted hook's pyright check reads prioritree's own [tool.pyright] and would fail every .py-bearing commit if it fired before the tooling floor stood. [SOURCE store/.junro/junro.json:58,191,197 | T3 | 2026-11-19] [SOURCE plan/keikaku-composition.md:59 | T3] [SOURCE input/.githooks/pre-commit:5-7,28-29 | T1] [SOURCE tane/.git/config:8; prioritree/.git/config:1-13 | T1]

**The answer + reasoning:**

- **The pointer, banked:** `git config core.hooksPath .githooks` at the prioritree root, run by **the collaborator's hand** — the route's own words (junro.json:58: "the collaborator's hand sets git config core.hooksPath=.githooks (the no-seat-shelling rule; the .git/config read-back recorded)"); jikko writes files, never runs commands (Mechanism 1's hands-split). The config delta is ONE line inside the existing `[core]` block (`hooksPath = .githooks`, tane/.git/config:8's measured form — the config-read precedent). The before-state is measured: prioritree/.git/config is 13 lines with NO hooksPath (:1-7 the [core] block) — the read-back's delta is unambiguous.
- **What the pointer does when the file doesn't exist yet — BANKED honestly:** git resolves hooks from `core.hooksPath` at hook-invocation time and runs a hook only if the file is present and executable there; a hooksPath pointing at a directory with no `pre-commit` means **no hook runs, no error raised — commits proceed unchecked (inert, fail-open)**. [T4: git's hook-resolution mechanism] Consequence, banked for the gate's read-back: **G-FOUNDATIONS condition 5's hooksPath datum is the config key** ("git config core.hooksPath pointing at .githooks (the collaborator's hand — the .git/config read-back)", junro.json:191) — the gate records the pointer, NOT a hook execution; the window between foundations and the harness emission is a named, honest hookless window.
- **Why foundations-before-harness is load-bearing (the sequencing keikaku ruled — plan/keikaku-composition.md:59), three mechanisms:**
  1. **The emitted hook reads prioritree's own config.** The family template's Check 1 runs `uv run pyright` over staged .py files with "the strictness flags rid[ing] the tree's own pyproject" (input/.githooks/pre-commit:5-7) and greps the 0/0/0 line (:28-29) — if the hook fired before the tooling-floor's `[tool.pyright]` and the dev-group pyright stood, every commit staging a .py would die (pyright unresolvable → the grep fails → exit 1). Foundations' config is the hook's precondition.
  2. **The gate's own sequencing:** G-HARNESS condition 1 holds "G-FOUNDATIONS is closed green" FIRST — "the emission lands into a configured tree (the hook reads the tree's own configs; the .gitignore's derived-view entries precede the emission)", junro.json:197.
  3. **Pointer-first = activation-free emission:** because the pointer precedes the file, the harness unit's emitted `.githooks/pre-commit` is LIVE the moment it lands — no separate activation step, no install step, no drift between a copied hook and its version-controlled bytes. (The birth commits themselves run through the hookless window until the harness lands; the emitted hook's `PRIORITREE_HOOK_BYPASS` — the TargetSpec's name, junro.json:80 — exists for the bootstrap class the family template already anticipates, input/.githooks/pre-commit:15-18.)
- **The divergence, named:** hikari's copy-based install (`make hooks-install` → `cp` into `git rev-parse --git-path hooks`, hikari/make/hooks.mk:13-27) is NOT the banked form — tane's config pointer is (tane/.git/config:8), per the route's explicit words. Both mechanisms need one per-clone act (a fresh clone carries neither .git/config hooksPath nor .git/hooks copies); the pointer's advantages at birth: one command, zero copying, and the hook always runs the current working-tree bytes.

**jikko's dispatch must carry (Mechanism 5):** the hands-split line for the collaborator's command list — `git config core.hooksPath .githooks` at the tooling-floor step (after the Makefile/pyproject land, before floor-green); the read-back note for the gate: the datum is the `.git/config` line, honestly recorded as a pointer with the hook file NOT yet present (the harness unit emits it next); the explicit statement that jikko writes no hook file in this unit.

---

## 7. Mechanism 6 — the skeleton + smoke mechanics

**[CLAIM]** The package init is tane's 2-line form (input's empty form CANNOT pass the banked ALL tier — D104); the smoke test's exact minimal shape is a docstringed module with one `-> None` test asserting the import (born green under ALL+R1 and strict pyright at first run); tests/__init__.py is present-and-declared (the INP001 mechanism); no conftest and no pytest ini_options at birth. [SOURCE tane/src/tane/__init__.py:1-2; tane/tests/__init__.py:1-20; tane/tests/test_readme.py:1-16; tane/tests/test_marker.py:1-13 | T1 | 2026-11-19] [SOURCE input/src/kepric_input/__init__.py (0 lines); input/tests/__init__.py (0 lines) — measured | T1] [SOURCE tane/tests/conftest.py:21-39 | T1] [SOURCE store/.junro/junro.json:51,188 | T3]

**The answer — the three files, banked with exact shapes:**

**`src/prioritree/__init__.py` — BANKED: tane's 2-line form, not input's empty form.** Mechanism: under `select=["ALL"]`, D104 (undocumented-public-package) fires on an empty package `__init__.py` — input's empty form (measured, 0 lines) passes only because input's ruff selects defaults (input/pyproject.toml:44-46, no D rules); tane's copyright-comment + one-line docstring passes ALL live. tane's form also names the born tree — the docstring mirrors the pyproject description (tane/src/tane/__init__.py:2 mirrors tane/pyproject.toml:4, the family's cross-surface idiom). Banked form (the candidate line ≤120 chars, D400-compliant; togo composes the final bytes within these constraints):

```python
# Copyright (C) 2026 Mark A Losey. All rights reserved.
"""prioritree — superior orderings from pairwise comparison: votes stored, tallied into a ranked whole."""
```

(The em-dash and one-line grammar are proven-safe under ALL by tane's own passing init; D401 does not apply to package docstrings — tane's non-imperative line passes live. [T4]) No subpackages at birth — input's `adapters/api/cli/…` are its app plane, product-effort territory (census §3.6).

**`tests/__init__.py` — BANKED: present-and-declared.** The INP001 mechanism: the implicit-namespace-package finding fires on .py files under a directory lacking `__init__.py` — with the file present, `tests/test_smoke.py` stands inside a declared package and INP001 never opens; tane's own file documents the fix as *"never a noqa, the declaration the fix"* (tane/tests/__init__.py:8). Under ALL the file also needs its D104 docstring — one declaration, two mechanisms satisfied. Banked compact form (tane's 20-line act-statement is the maximal precedent; the compact declaration carries the rationale):

```python
# Copyright (C) 2026 Mark A Losey. All rights reserved.
"""Declare tests/ an explicit package — the INP001 fix (tane/tests/__init__.py the precedent): presence, never a noqa."""
```

**`tests/test_smoke.py` — BANKED: the exact minimal shape.** The smoke test is gate-derived, not sibling-copied (no sibling carries one — measured at both, census §3.6); its constraints: born green at first run (G-FOUNDATIONS conditions 2-3), imports src/prioritree (condition 2's literal words), passes ALL+R1 and strict pyright. Banked shape:

```python
# Copyright (C) 2026 Mark A Losey. All rights reserved.
"""The born tree's smoke test — the import answers, the namespace lives."""

import prioritree


def test_prioritree_imports() -> None:
    """Pin the import — src/prioritree resolves and answers its name."""
    assert prioritree.__name__ == "prioritree"
```

Every rule pre-checked: D100/D103/D400/D401-grammar (the "Pin the …" family grammar, test_readme.py:13,20), ANN201 (`-> None`), I001, E501, F401 (the import is used by the assert), S101+PLR2004 (R1-ruled — the literal "prioritree" IS the specification under test, R1's second limb verbatim), no INP001 (declared package), no TC/PT/FBT/TRY bites; pyright strict: one used first-party import, `__name__` is `str`, zero diagnostics — **0/0/0 born-green**. [T4, derived over the T1 grammar evidence]

**No conftest.py — BANKED absent.** tane's conftest exists to isolate one product organ (the index build's declared grounds — the single autouse fixture, tane/tests/conftest.py:21-39); input carries none despite 21 test files (measured absence); prioritree has no organ to isolate (census §3.6's reasoning, verified at source). **No `[tool.pytest.ini_options]` — BANKED: tane's bare form.** No async (no `asyncio_mode`), no markers, no framework settings, no `pythonpath` (the editable install resolves the import — Mechanism 1); bare pytest discovers `tests/` from the rootdir with dot-dirs skipped. Either minimal stanza would satisfy the gate; carrying options with no need violates the lean-floor stance the rulings set ("skeleton only", junro.json:51). [T3/T1]

**jikko's dispatch must carry (Mechanism 6):** the three files' exact bytes (§10); the no-conftest/no-ini/no-subpackages scope fence; the note that the smoke suite is the whole suite at birth (condition 2's "at least one" is exactly one).

---

## 8. Contradiction notes (evidence-disciplined, each changing or correcting a mechanism judgment)

1. **The census's zero-ignores lean is CORRECTED** (census §3.7: "select=['ALL'] over a two-file tree can pass 0/0 with no ignores"): TRUE only for the non-test skeleton files; FALSE for the gate-mandated asserting smoke test — S101+PLR2004 fire, and tane's R1 (tane/pyproject.toml:106-112) is the family's settled, reasoning-carrying ruling for exactly this class. The banked config: ALL + R1 inherited (one named ruling), zero convenience ignores. The zero-ignore LAW is unaffected — indeed better honored: the law is "an ignore is a ruling," and R1 IS one.
2. **The dispatch's example ruling-class, refined:** tane's per-file-ignores never ruled INP001 — the declaration closed it ("never a noqa, the declaration the fix", tane/tests/__init__.py:8). The bank keeps the declaration form for INP001 and the ignore-as-ruling form for S101/PLR2004 — two different mechanisms, both precedented at path:line.
3. **tane's grammar split is the D-rule/ANN evidence:** tane's OLD bare test files (test_marker.py:1-13 — no docstring, no `-> None`) stand in the sequenced "docstring sweep" backlog its own hook names (tane/.githooks/pre-commit:18-21 — "ruff zero-findings joins this hook when the docstring sweep completes"); tane's MATURE grammar (test_readme.py) is the compliant form. A born-green tree with a zero-findings gate cannot carry backlog — the mature grammar is the only bankable smoke-test form.
4. **A count-drift datum, not load-bearing:** tane's strictness comment says "the six NAMED RULINGS" (tane/pyproject.toml:90-95, the 2026-09-27 birth-time count) while the file now carries rulings through R14 (each dated in-line) — the discipline held, the count grew with the tree. No judgment changes; noted so the brief quotes the MECHANISM, not the stale count.

## 9. The open edges named for togo — ZERO

All six mechanisms are banked; the census's three brief-level edges are closed here: the pin spread (→ 3.13, four-surface agreement, §2), the lint/typecheck composition (→ the hikari split + additive typecheck, §5), the smoke shape (→ §7). What remains for togo is composition, not deliberation: the README's exact prose (content source banked by the census §3.5 — Q-purpose's ruled words, nothing invented), the .gitignore's template choice (census §3.4 banked: the input template + `.junro/`, the named precedent's lazy-true form; derived-view entries are harness-scope per G-HARNESS condition 1), and the final byte-polish of the docstring lines within the banked constraints (form + candidate lines given in §7). No open design question crosses into the brief.

## 10. The consolidated dispatch payload (jikko's brief carries this whole; the build needs no deliberation)

**Files jikko writes (9, exact bytes banked in §2-§7):** `pyproject.toml` (the [project] block + hatchling + ruff + pyright + dev group) · `.python-version` (`3.13`) · `.gitignore` (census §3.4's form) · `README.md` (census §3.5's content source) · `Makefile` (§5's bytes) · `src/prioritree/__init__.py` (§7) · `tests/__init__.py` (§7) · `tests/test_smoke.py` (§7). The ninth surface is the config act, not a file: `git config core.hooksPath .githooks`.

**The collaborator's hand (the hands-split, explicit):** `uv lock` (after project-floor lands, before floor-green; commit the lock at the root) → `git config core.hooksPath .githooks` (at tooling-floor) → the floor-green run `make dev && make test && make lint && make typecheck` → the prioritree-side commits through the collaborator's hand (the two-tree hands rule, plan/keikaku-composition.md:56). jikko's pack holds no shell — every command above is named for the hand, never for the seat.

**The verification read-backs (kensho's gate, keyed to the banked mechanisms):** condition 1 — uv sync green at 3.13 from the pin, the lock committed, zero errors AND zero warnings (§2); condition 2 — the smoke suite green, one passing test importing src/prioritree, zero-and-zero (§7); condition 3 — ruff zero findings over src/ and tests/ with the zero-ignore law standing (ALL + R1 only), and pyright at "0 errors, 0 warnings, 0 informations" — the summary line the read-back reads, the wrapper's version notice out-of-band (§3); condition 4 — make dev/test/lint exit 0 (the route's recorded line, unchanged), with `make typecheck` the additive belt (§5); condition 5 — the records read-back: .gitignore whole, README carrying Q-purpose's ruled description, and the hooksPath line in .git/config recorded as a pointer, the hook file honestly not yet present (§6).

**Boundary held to the end: read-only — no writes, no mutations, no filings. Every claim cited at source.**
