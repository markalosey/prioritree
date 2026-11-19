# discover/foundations — the foundations unit's discovery census (raw-first)

## 0. Census provenance

- **Seat:** tansa (探査, discover) — packet `discover/foundations`, route `prioritree-birth`, unit `build/foundations`
- **Date:** 2026-11-19
- **Method:** direct read-only file reads at four trees + the store; every claim cited at `path:line` against the measured file; counts via the pack's own calculate instrument
- **Boundary held:** reads and citations only — no writes anywhere, no store mutations, no friction filings. Read-only by design, held.
- **Tree roots (citations are tree-relative to these):**
  - `store/` = `/Users/marklosey/projects/prioritree/.plans/ideation/2026-11-19-prioritree-birth`
  - `input/` = `/Users/marklosey/projects/kepric/kepric-input` (the named precedent sibling — store/.junro/junro.json:14)
  - `tane/` = `/Users/marklosey/projects/kepric/tane`
  - `hikari/` = `/Users/marklosey/projects/kepric/hikari`
  - `prioritree/` = `/Users/marklosey/projects/prioritree`
- **Session binding set (session-start law, recorded):** visible surface enumerated verbatim at dispatch start; reconciled against the pin — the `hikari-local` evaluation binding is **absent** this session (only `hikari-prod` present, unused: this is a file-tree census, not an API census); unearned per pin and confirmed absent: `code-graph-context`, `edit`, `etl`, `junro`, `reflect`, `script`, `symbol-lookup`, `write`.

## 1. What the census answers to (the store's ground truth)

The banked file set (store/plan/keikaku-composition.md:13-19): project-floor (`pyproject` + `.python-version` + `uv.lock` + `.gitignore` + `README`) → src-skeleton (skeleton only, NO product logic) → tooling-floor (ruff + the ruled type-check config + pytest floor + Makefile floor dev/test/lint; `core.hooksPath=.githooks` by the collaborator's hand) → floor-green (`make dev && make test && make lint`).

The three birth rulings, all 2026-11-19:

- **Q-purpose** (store/.junro/junro.json:379-389) — the README's content source. Verbatim ruling at :384; the resolution line at :389: *"Priori-tree is a generalized prioritization system: for any list and comparison operator, run the pairwise permutations, store the votes, tally — the output list is in a superior order than sizing individual items, because discernment between two items is easy (for humans and LLMs) while absolute sizing is not."*
- **Q-setup-arch** (store/.junro/junro.json:391-402) — all four forms layered library-first (`src/prioritree` pure-logic core at the bottom); **pure logic at birth, no DB**; Makefile floor dev/test/lint ("the hikari idiom"); **GitHub project, CI deferred — git hooks and local gates stand in at birth** (:397).
- **Q-typecheck-alignment → PYRIGHT** — the ruling is recorded as **amendment 17, the dated supersede** (store/.junro/junro.json:368-371): the collaborator *"validated the composition … and ruled Q-typecheck-alignment PYRIGHT in the same pass … build/foundations' tooling-floor step carries pyright from the start."* Measured discrepancy named honestly: the `open_questions` array still carries the question as `status: "open"` (store/.junro/junro.json:423-426) — the amendment is the operative, dated record (its own words: "this amendment the dated supersede"); the dispatch and the amendment agree: **pyright is in from the start**.

The gate teeth that shape the floor (G-FOUNDATIONS, store/.junro/junro.json:184-192): uv sync zero-errors-AND-zero-warnings with the pinned Python from `.python-version` (:187); the smoke suite green with **at least one passing test importing src/prioritree** (:188); ruff zero findings over `src/` and `tests/` **and** the ruled type checker at zero errors AND zero warnings, the zero-ignore law standing (:189); `make dev && make test && make lint` all exit 0 (:190); the records read-back — `.gitignore` (the Python set + `.junro/` + the derived-view entries the harness discovery confirms), README carrying Q-purpose's ruled description, and `core.hooksPath` pointing at `.githooks` (:191).

## 2. The measured trees

### 2.1 kepric-input — the most recent scaffolded sibling (the named precedent)

Root census (measured listing, 25 entries): `.cursor/ .dockerignore .env .env.example .env.prod.example .git/ .githooks/ .gitignore .junro/ .opencode/ .python-version .venv/ AGENTS.md alembic.ini alembic/ docker-compose.yml Dockerfile docs/ LICENSE opencode.json pyproject.toml README.md src/ tests/ uv.lock`. **No Makefile. No CI directory (no `.github/`, no `.gitea/`).**

- `pyproject.toml` (61 lines): `[project]` name/version/description/readme/`requires-python = ">=3.13"` (input/pyproject.toml:1-6); 25 runtime dependencies — the full app plane (aiofiles, alembic, asyncpg, fastapi, fastmcp, grpcio, httpx, infisicalsdk, jinja2, opentelemetry ×6, prometheus, pydantic-settings, python-multipart, sqlalchemy, structlog, typer, uvicorn) (input/pyproject.toml:7-32); `[project.scripts] kepric-input = "kepric_input.cli.main:app"` (:34-35); hatchling + `[tool.hatch.build.targets.wheel] packages = ["src/kepric_input"]` (:37-42); `[tool.ruff] extend-exclude = ["*_pb2.py", "*_pb2_grpc.py"]` — ruff defaults otherwise (:44-46); `[tool.pytest.ini_options] asyncio_mode = "auto"` + two markers (:48-54); `[dependency-groups] dev = ["pytest>=9.1.1", "pytest-asyncio>=1.4.0", "ruff>=0.15.20"]` (:56-61). **Measured NO-typechecker state: no `[tool.pyright]`, no mypy, no type checker in dev** (the whole 61-line file read) — matching the store's datum (store/.junro/junro.json:424).
- `.python-version`: `3.13` (input/.python-version:1).
- `uv.lock`: 2197 lines; header `version = 1`, `revision = 3`, `requires-python = ">=3.13"` (input/uv.lock:1-3) — committed at the root (listing).
- `.gitignore` (181 lines): the github Python template whole — `.env`/`.venv` at :132-133, `.pytest_cache/` at :52, `.mypy_cache/` at :151, `.ruff_cache/` at :172, and **`.junro/` at :181** (the sibling's only family-specific entry). **No `.opencode/` entries** (measured over :1-181) — confirming the store's datum (store/plan/keikaku-composition.md:68).
- `README.md` (272 lines): title + one-paragraph description (input/README.md:1-8), status blockquote (:10-26), Goal section (:28-46), What it is / is not table (:48-56), Quick start (:69-101), Technology stack (:166-180), Project structure (:196-213), License (:270-272).
- `src/` layout: `src/kepric_input/` with `__init__.py` (measured: **0 lines, empty**), `main.py`, and subpackages `adapters/ api/ cli/ core/ models/ proto/ services/ static/ templates/` (listing) — the `src/<pkg>` convention bound by the hatch wheel stanza (input/pyproject.toml:41-42).
- `tests/` layout: `__init__.py` (measured: **0 lines, empty**) + `fixtures/` + **21 `test_*.py` files** (23 listing entries − `__init__.py` − `fixtures/`, count via calculate). **No `conftest.py` anywhere** (glob `tests/**/conftest.py`: no hits; root listing: none) — the async/marker floor rides pyproject alone (input/pyproject.toml:48-54).
- `.githooks/`: **only `pre-commit`** (listing, 1 entry) — the family template, census at §3.11.

### 2.2 tane — the leaner sibling

Root census (measured listing, 32 entries): `entry.py` **at the root** (the CLI precedent), `pyproject.toml`, `src/`, `tests/`, `.githooks/` (1 entry: `pre-commit`), `.gitignore`, `uv.lock`, **`.gitea/`** (the CI-carrying sibling), `.env`/`.env.example`, `.tane/`, `vendor/`, `dist/`, `scripts/`. **No Makefile. No `.python-version`** (measured absence in the listing; `requires-python = ">=3.12"` rides pyproject alone, tane/pyproject.toml:5).

- `pyproject.toml` (226 lines): 4 runtime deps with the separation-law comments (tane/pyproject.toml:6-28); addon extras `pdf`/`knowledge` — never the base install (:30-55); `[project.scripts] tane = "tane.console:main"` (:57-58); hatchling + wheel `packages = ["src/tane"]` (:60-65); `[tool.ruff]` target py312, line-length 120, `src = ["src"]` (:67-87); **`[tool.ruff.lint] select = ["ALL"]`** — "THE SEED'S OWN STRICTNESS — every rule on; the ONLY exceptions are the six NAMED RULINGS … Nothing else is ignored, ever" (:89-96); per-file-ignores as named rulings (:105-197); `[tool.ruff.format] quote-style = "double"` (:199-200); **`[tool.pyright] typeCheckingMode = "strict"`** + the no-suppression extras (:202-215); `[dependency-groups] dev = ["pytest", "pyright", "pyinstaller", "ruff"]` (:217-218). **No `[tool.pytest.ini_options]`** (measured absence over the full 226 lines).
- `entry.py` (14 lines): the PyInstaller console entry — `from tane.console import main` / `raise SystemExit(main())` (tane/entry.py:11-14), docstring at :2-9. Root-level, outside `src/`.
- `src/tane/__init__.py`: copyright + one-line module docstring (tane/src/tane/__init__.py:1-2).
- `tests/`: `__init__.py` as a **declared package** — the INP001 fix, documented in the file itself (tane/tests/__init__.py:2-19); `conftest.py` at the tests root — one autouse isolation fixture (tane/tests/conftest.py:21-39); `data/`; **121 `test_*.py` files** (125 listing entries − `__init__.py` − `__pycache__/` − `conftest.py` − `data/`, count via calculate).
- `.gitignore` (76 lines): hand-rolled lean — `.env` (:2), `__pycache__/` (:5), `.venv/` (:13), `.pytest_cache/`/`.mypy_cache/`/`.ruff_cache/` (:17-19), **`.opencode/node_modules/` + `.opencode/.venv/`** (:46-47, the derived-view entries), tane-specific derived-state blocks (:49-76).

### 2.3 hikari — the floor idioms

- **The Makefile idiom:** root `Makefile` with `.DEFAULT_GOAL := help` (hikari/Makefile:1), the include chain `include make/dev.mk … make/mcp.mk` over 17 `make/*.mk` files (hikari/Makefile:29-45; listing), and the self-documenting help target greping `$(MAKEFILE_LIST)` for `##` comments (hikari/Makefile:47-49).
- **The floor targets' actual recipes:**
  - dev-env: `uv-install: uv sync --extra dev` (hikari/make/dev.mk:76-77) — hikari's env target is **named `uv-install`**, not `dev`.
  - test: `test: $(COMPOSE) exec hikari pytest tests/` (hikari/make/test.mk:5-6) — **Docker-first** (`COMPOSE := docker compose …` at test.mk:1).
  - lint: `lint: $(RUFF) check $(LINT_PATHS)` with `LINT_PATHS ?= src/ tests/` (hikari/make/lint.mk:188, 191-192) — Docker default (`WHERE ?= docker`, lint.mk:6); the **local channel** is `uv run --active --no-sync ruff` (lint.mk:20-28). Ruff and the type checker are **separate targets**: `typecheck: $(PYRIGHT) $(TYPECHECK_PATHS)` with `TYPECHECK_PATHS ?= src/` (lint.mk:189, 197-198); pyright's channel is host-local by ruling (`PYRIGHT_WHERE ?= local`, lint.mk:17).
- **`.githooks/` family:** five hooks — `commit-msg`, `post-commit`, `post-commit-lfs`, `pre-commit`, `prepare-commit-msg` (listing). `pre-commit` (234 lines) runs six hikari-specific checks behind `HIKARI_HOOK_BYPASS` (hikari/.githooks/pre-commit:24-26, checks at :43-232) — **not the family template**; hikari installs hooks by **copy** (`make hooks-install` → `cp` into `git rev-parse --git-path hooks`, hikari/make/hooks.mk:13-27), not by hooksPath.
- **pyproject:** `[tool.ruff]` target py312, line-length 120, `src = ["src"]`, `[tool.ruff.lint] select = ["E","F","I","N","UP","B","SIM","RUF"]` (hikari/pyproject.toml:150-156); **`[tool.pyright]` minimal — `pythonVersion = "3.12"`, `venvPath = "."`, `venv = ".venv"`, NO typeCheckingMode** (:199-202); pyright in dev extras (`pyright>=1.1`, :76); `[tool.pytest.ini_options]` with `pythonpath = ["src"]` + `asyncio_mode = "auto"` (:204-207).
- `.python-version`: `3.12` (hikari/.python-version:1).
- `.gitignore` (227 lines): the github template + a hikari tail — `.venv` at :140, `.ruff_cache/` at :179, `.pytest_cache/` at :59, `.worktrees/` at :186, `.opencode/node_modules/` + lock files at :198-199, `.scratch/` at :211. **No `.junro/` entry** (measured absence) — hikari tracks its effort records under `.plans/` paths.

### 2.4 prioritree — the greenfield baseline

Root census (measured listing, 3 entries): `.git/`, `.plans/`, `README.md`. **That is everything.** No pyproject, no `.python-version`, no `uv.lock`, no `.gitignore` beyond none, no src/, no tests/, no Makefile, no `.githooks/`, no `.opencode/`, no CI directory. Current README is 2 lines: `# prioritree` / `Prioritization framework` (prioritree/README.md:1-2).

## 3. Per banked file — precedent / measured shape / recommended form

### 3.1 pyproject.toml

- **Precedent:** kepric-input (the named precedent tree, store/.junro/junro.json:14) — `input/pyproject.toml`; tane's leaner shape as the secondary datum.
- **Measured shape (verbatim key lines):** `[project] name/version/description/readme = "README.md"/requires-python = ">=3.13"` (input/pyproject.toml:1-6); hatchling + `packages = ["src/kepric_input"]` (:37-42); `[dependency-groups] dev = ["pytest>=9.1.1", "pytest-asyncio>=1.4.0", "ruff>=0.15.20"]` (:56-61). tane: `requires-python = ">=3.12"` (tane/pyproject.toml:5), wheel `packages = ["src/tane"]` (:64-65), `dev = ["pytest", "pyright", "pyinstaller", "ruff"]` (:217-218).
- **Recommended form for prioritree:** `[project]` with `name = "prioritree"`, `version = "0.1.0"` (hikari's measured birth version, hikari/pyproject.toml:3), `description` = Q-purpose's resolution line (store/.junro/junro.json:389), `readme = "README.md"`, `requires-python = ">=3.13"` **per the named precedent tree** (input/pyproject.toml:6; see §6.1 for the pin spread). Build system: hatchling + `[tool.hatch.build.targets.wheel] packages = ["src/prioritree"]` (both siblings' form). **Divergence:** `dependencies = []` — zero runtime deps at birth (pure logic, Q-setup-arch, store/.junro/junro.json:397); no `[project.scripts]` at birth (the CLI is the product effort's layer, junro.json:51 — input's scripts stanza at :34-35 is its v0.1+ maturity, not the skeleton). `[dependency-groups] dev = ["pytest", "ruff", "pyright"]` — tane's set (tane/pyproject.toml:218) minus `pyinstaller` (tane's binary-delivery need, not prioritree's), minus `pytest-asyncio` (no async at birth). Ruff/pyright/pytest stanzas per §3.7-3.9.

### 3.2 .python-version

- **Precedent:** kepric-input (named precedent) + hikari.
- **Measured shape:** `3.13` (input/.python-version:1); `3.12` (hikari/.python-version:1); **tane carries no `.python-version` at all** (listing) — the family is split, and the gate requires the file (G-FOUNDATIONS condition 1, "the pinned Python resolved from `.python-version`", store/.junro/junro.json:187).
- **Recommended form:** the file, one line, `3.13` — following the named precedent tree (input/.python-version:1). The pin spread is named at §6.1 for the brief.

### 3.3 uv.lock

- **Precedent:** kepric-input (named precedent); carried at all three siblings (input listing; tane listing; hikari glob hit `hikari/uv.lock`).
- **Measured shape:** `version = 1`, `revision = 3`, `requires-python = ">=3.13"` — mirroring the pyproject floor (input/uv.lock:1-3); 2197 lines at the mature tree.
- **Recommended form:** not hand-written — **generated** (`uv lock` at the build, committed at the root per the family habit). The lock is the reproducibility leg of G-FOUNDATIONS condition 1 ("the environment reproducible from the lockfile", store/.junro/junro.json:187). At birth it will be small (empty runtime deps + the dev group); its shape will match the measured header.

### 3.4 .gitignore

- **Precedent:** kepric-input (named precedent — the github-template form); tane (the hand-rolled leaner form).
- **Measured shape (coverage datum):** input carries `.env`/`.venv` (:132-133), `.pytest_cache/` (:52), `.mypy_cache/` (:151), `.ruff_cache/` (:172), and **`.junro/` at :181 — the only family-specific entry**; **no `.opencode/` entries** (measured). tane carries the lean set: `.env` (:2), `.venv/` (:13), `.pytest_cache/`/`.mypy_cache/`/`.ruff_cache/` (:17-19), plus the derived-view `.opencode/node_modules/` + `.opencode/.venv/` (:46-47). hikari: `.venv` (:140), `.ruff_cache/` (:179), plus its own tail (:184-227).
- **Recommended form:** the gate's words rule the scope — "the Python set + `.junro/` + the derived-view entries the harness discovery confirms" (store/.junro/junro.json:191). Either sibling form satisfies the gate; the input template (named precedent) whole-plus-`.junro/` is the lazy-true form, tane's 76-line hand-rolled form is the pure-logic-tree form (it drops the Django/Flask/Scrapy/Celery noise input's template carries at :59-135). **Divergence named:** the derived-view entries (`.opencode/node_modules/` etc., tane/.gitignore:46-47) are **harness-scope** — G-HARNESS condition 1 holds "the `.gitignore`'s derived-view entries precede the emission" (store/.junro/junro.json:197); foundations lands the Python set + `.junro/` (the kepric-input precedent, input/.gitignore:181 — note the pattern matches `.junro/` at any depth, covering the store's record home at `.plans/ideation/*/.junro/`), and the harness unit adds the derived views.

### 3.5 README.md

- **Precedent:** kepric-input's README (input/README.md:1-272) — title + one-paragraph description + goal, the scaffold README shape; the current 2-line state is measured at prioritree/README.md:1-2.
- **Measured shape (the content source is ruled, not copied):** Q-purpose's verbatim ruling (store/.junro/junro.json:384) — the basketball/grapefruit discernment passage — and its resolution (:389). G-FOUNDATIONS condition 5: "README content carrying Q-purpose's ruled description" (store/.junro/junro.json:191).
- **Recommended form:** title (`# Priori-tree`), the ruled description carried (the verbatim passage and/or the resolution line, cited to the ruling), and the four-form library-first architecture named per Q-setup-arch (store/.junro/junro.json:397) — skeleton-honest: no quick-start that doesn't exist yet, no stack table the tree doesn't carry. The exact composition is the brief's; the census binds the content source: the ruling's own words, nothing invented.

### 3.6 src/prioritree skeleton + the smoke test

- **Precedent:** the `src/<pkg>` convention at both siblings — bound by the hatch wheel stanzas (input/pyproject.toml:41-42; tane/pyproject.toml:64-65); the package-init forms: input's `src/kepric_input/__init__.py` is **empty** (measured, 0 lines); tane's `src/tane/__init__.py` is **copyright + one-line docstring** (tane/src/tane/__init__.py:1-2).
- **Measured shape:** the skeleton ruling — "skeleton only, NO product logic: the core library is the product effort's first increment" (store/.junro/junro.json:51); the smoke requirement — "at least one passing test importing src/prioritree" (G-FOUNDATIONS condition 2, store/.junro/junro.json:188).
- **Recommended form:** `src/prioritree/__init__.py` (either measured init form satisfies the gate — tane's 2-line docstring form names the born tree; input's empty form is the named precedent; the brief picks). **The smoke test has no sibling copy** — measured: neither sibling carries a named smoke test (input/tests: 21 product tests, tane/tests: 121 product tests) — it is **gate-derived** (junro.json:188): one `tests/test_smoke.py` importing `prioritree` and asserting one trivial truth, born green so the zero-and-zero bar passes at first run. `tests/__init__.py` present per both siblings (input: empty; tane: the INP001 declaration, tane/tests/__init__.py:2-19). **Divergence:** no subpackages at birth (input's `adapters/api/cli/...` are its app plane, prioritree/README.md:199-209 — product-effort territory); no conftest.py at birth (input precedent: none measured; tane's conftest exists to isolate its index organ, tane/tests/conftest.py:21-39 — prioritree has no organ to isolate yet).

### 3.7 ruff config

- **Precedent:** three measured strictness tiers. input: `[tool.ruff] extend-exclude` only — defaults otherwise (input/pyproject.toml:44-46). hikari: `target-version = "py312"`, `line-length = 120`, `src = ["src"]`, `select = ["E","F","I","N","UP","B","SIM","RUF"]` + per-file-ignores reserved for verbatim-emitted files (hikari/pyproject.toml:150-168). tane: `select = ["ALL"]` — "the ONLY exceptions are the six NAMED RULINGS … Nothing else is ignored, ever" (tane/pyproject.toml:89-96), with every per-file-ignore a cited ruling (:105-197) and `[tool.ruff.format] quote-style = "double"` (:199-200).
- **Recommended form:** the zero-ignore law binds either tier (G-FOUNDATIONS condition 3, store/.junro/junro.json:189: "an ignore is a ruling, never a convenience"). For a **born-green skeleton with zero backlog**, tane's seed stance is the natural fit — `select = ["ALL"]` over a two-file tree can pass 0/0 with no ignores, and every future ignore is forced into the named-ruling discipline from day one. `target-version` matches the pin (§6.1), `line-length = 120` (both elder siblings agree, tane/pyproject.toml:69, hikari/pyproject.toml:152), `src = ["src"]`. The brief rules the tier; the census binds the law (zero-ignore) and the two measured precedents.

### 3.8 pyright config (the ruled checker)

- **Precedent:** tane — the strictness precedent the family template itself cites. The family hook's own header: "The strictness flags ride the tree's own pyproject (the tane precedent's shape)" (input/.githooks/pre-commit:5-7).
- **Measured shape (verbatim, tane/pyproject.toml:202-215):**
  ```toml
  [tool.pyright]
  typeCheckingMode = "strict"
  enableTypeIgnoreComments = false
  reportImplicitStringConcatenation = "error"
  reportUnnecessaryTypeIgnoreComment = "error"
  reportCallInDefaultInitializer = "error"
  reportUninitializedInstanceVariable = "error"
  reportMatchNotExhaustive = "error"
  reportDeprecated = "error"
  include = ["src", "tests", "scripts/junro"]
  ```
  (with the no-suppression-law comment at :206-210: "dead type-ignore comments are reported lies, not tolerated text"). hikari's block is minimal — `pythonVersion`/`venvPath`/`venv` only, no mode (hikari/pyproject.toml:199-202). input carries **neither** (§2.1). Both checker-carrying trees put pyright in dev deps (tane/pyproject.toml:218; hikari/pyproject.toml:76).
- **Recommended form:** the PYRIGHT ruling is measured (store/.junro/junro.json:368-371) — pyright is the tree's checker from the tooling-floor step, not a harness-unit retrofit. `[tool.pyright]` in prioritree's pyproject, tane's shape adapted: `typeCheckingMode = "strict"` + the no-suppression extras, `include = ["src", "tests"]` (no frozen engine to include), `pythonVersion = "3.13"` per the pin (or omitted — tane omits it; hikari sets it; the brief picks). `pyright` in the dev group (§3.1). **Divergence named:** input — the named precedent tree — has no type checker at all; prioritree diverges from the named precedent per the ruling, following tane's config instead. This is exactly the resolved tension the amendment records (junro.json:368: "build/foundations' tooling-floor step carries pyright from the start").

### 3.9 pytest floor

- **Precedent:** three measured forms. input: `[tool.pytest.ini_options] asyncio_mode = "auto"` + markers (input/pyproject.toml:48-54), no conftest (§2.1). hikari: `DJANGO_SETTINGS_MODULE` + `pythonpath = ["src"]` + `asyncio_mode = "auto"` (hikari/pyproject.toml:204-207). tane: **no ini_options at all** (measured absence) + `tests/conftest.py` + `tests/__init__.py`.
- **Recommended form:** minimal — pure logic at birth means no async (`asyncio_mode` unneeded — input's is there for its async DB plane), no Django settings (hikari's is its framework), no markers. Either tane's bare form or a minimal `[tool.pytest.ini_options]` with `testpaths = ["tests"]` satisfies the gate; the zero-and-zero bar (G-FOUNDATIONS condition 2, store/.junro/junro.json:188) is the binding constraint. The smoke suite (§3.6) is the suite.

### 3.10 Makefile floor (dev/test/lint)

- **Precedent:** hikari — **the only Makefile in the family** (measured: input listing — no Makefile; tane listing — no Makefile; hikari/Makefile + 17 `make/*.mk`). The banked floor names are the hikari idiom's (Q-setup-arch, store/.junro/junro.json:397; G-FOUNDATIONS condition 4, :190).
- **Measured shape:** root Makefile with `.DEFAULT_GOAL := help` + the include chain + the `##`-comment help target (hikari/Makefile:1, 29-49). Target recipes: env-sync `uv-install: uv sync --extra dev` (hikari/make/dev.mk:76-77); `test: $(COMPOSE) exec hikari pytest tests/` (hikari/make/test.mk:5-6); `lint: $(RUFF) check $(LINT_PATHS)`, `LINT_PATHS ?= src/ tests/` (hikari/make/lint.mk:188-192); `typecheck: $(PYRIGHT) $(TYPECHECK_PATHS)`, `TYPECHECK_PATHS ?= src/` (hikari/make/lint.mk:189, 197-198); the **no-docker local channel** is `uv run --active --no-sync ruff` (hikari/make/lint.mk:20-28).
- **Recommended form:** a single root `Makefile` (no `make/` directory needed at floor scale — hikari's include chain is its 17-file maturity). **Divergences, named:**
  1. **No Docker.** hikari's `test`/`lint` recipes are compose-exec (test.mk:1, lint.mk:1, 27) — prioritree's run host-side via bare `uv run` (the measured no-docker channel form, lint.mk:20-28, is the recipe precedent).
  2. **The env target is named `dev`, not `uv-install`** (the banked floor names dev/test/lint — store/plan/keikaku-composition.md:18-19; floor-green runs `make dev && make test && make lint`, :19). Recipe `uv sync` — hikari's `--extra dev` is its optional-dependencies form (hikari/pyproject.toml:70-71); the siblings use `[dependency-groups]` (input/pyproject.toml:56; tane/pyproject.toml:217), which `uv sync` installs by default.
  3. **pyright's target.** hikari splits `lint` (ruff) from `typecheck` (pyright) (lint.mk:191-198). The gate names only dev/test/lint at floor-green (store/.junro/junro.json:190) while condition 3 separately holds the ruled checker at zero (:189) — so the brief either composes pyright into `lint` or banks a fourth `typecheck` target invoked at the gate run. Both precedents measured; the hikari split is the named idiom's shape.
- Sketch (the brief rules the exact bytes):
  ```make
  .PHONY: dev test lint
  dev:      ## Sync the environment (dev group included)
  	uv sync
  test:     ## Run the test suite
  	uv run pytest
  lint:     ## Ruff over src/ and tests/
  	uv run ruff check src/ tests/
  ```

### 3.11 .githooks/pre-commit + the hooksPath step

- **Precedent:** the **family template** — kepric-input's and tane's hooks are the scaffold-emitted pair; hikari's pre-commit is hikari-specific (six checks, hikari/.githooks/pre-commit:43-232) and NOT the family form.
- **Measured shape (verbatim key lines, input/.githooks/pre-commit):** header — "GENERATED by scripts/generation/clarity_scaffold.py from hikari; regenerated at will, never hand-maintained" (:2-3); Check 1 — "staged .py files must pass pyright — the 0/0/0 bar (a warning is an error waiting to happen). The strictness flags ride the tree's own pyproject" (:5-7); the bypass — `INPUT_HOOK_BYPASS=1` (:15-18); the mechanism — `STAGED_PY=$(git diff --cached --name-only --diff-filter=ACM | grep '\.py$' || true)` (:22), `PYRIGHT_OUT=$(uv run pyright $STAGED_PY 2>&1)` and the bar grep `"0 errors, 0 warnings, 0 informations"` (:28-29), exit 1 otherwise (:30-37); PHASE 2 named-pending — "ruff zero-findings joins this hook when the tree's ruff backlog is sequenced to zero" (:9-13). tane's is the same template plus its ledger-chain Check 1 (tane/.githooks/pre-commit:30-50) behind `TANE_HOOK_BYPASS` (:26-28) — same pyright check at :58-59.
- **Recommended form + sequencing (the store rules the split):** foundations' step is the **config pointer, not the hook file** — "the collaborator's hand sets git config core.hooksPath=.githooks (the no-seat-shelling rule; the .git/config read-back recorded)" (store/.junro/junro.json:58); the hook **file** is emitted by the harness unit (Q-harness ruling, store/.junro/junro.json:410; the sequencing is load-bearing: "the emission lands `.githooks/pre-commit` whose strictness flags ride the tree's own pyproject" — store/plan/keikaku-composition.md:59 — which is why foundations' pyproject precedes it, and why G-HARNESS condition 1 holds "G-FOUNDATIONS is closed green" first, junro.json:197). The emitted form will be the family template with `PRIORITREE_HOOK_BYPASS` (the TargetSpec names it, junro.json:80) and the pyright check reading **prioritree's own** `[tool.pyright]` (§3.8). Setting hooksPath before the file exists is inert (git runs a hooksPath hook only if the file is present) — the read-back at G-FOUNDATIONS condition 5 (junro.json:191) is the config pointer, honestly. **Divergence named:** hikari's copy-based install (hooks.mk:13-27) is NOT the banked form — tane's measured config is (§5).

## 4. WHAT-DOES-NOT-CARRY (the divergence set — sibling evidence for every exclusion)

Prioritree is pure logic at birth (Q-setup-arch, store/.junro/junro.json:397); no CI at birth (same ruling; store/plan/keikaku-composition.md:61). Named with the sibling evidence:

| Not carried | Sibling evidence (measured) |
|---|---|
| `alembic/` + `alembic.ini` | input listing; `alembic>=1.18.5` (input/pyproject.toml:9) |
| `docker-compose.yml`, `Dockerfile`, `.dockerignore` | input listing (3 entries) |
| `.env` machinery (`.env`, `.env.example`, `.env.prod.example`) | input listing; `.env` ignored at input/.gitignore:132; tane carries `.env`+`.env.example` (listing, tane/.gitignore:2) |
| DB drivers (asyncpg, sqlalchemy) | input/pyproject.toml:10, :28 |
| The app plane (fastapi, uvicorn, typer, fastmcp, httpx, jinja2, python-multipart, pydantic-settings) | input/pyproject.toml:11, :16, :18, :26, :27, :30, :31, :12 — the four-form stack's upper layers are product-effort increments (store/.junro/junro.json:51) |
| Observability (opentelemetry ×6, prometheus, structlog) + secrets (infisicalsdk) | input/pyproject.toml:17, :19-25, :29 |
| gRPC/proto stubs (grpcio, grpcio-tools) | input/pyproject.toml:14-15; ruff's pb2 exclude (input/pyproject.toml:46) exists only for these |
| CI config | tane carries `.gitea/` (listing); hikari references `.gitea/workflows/allowlist-freshness.yml` (hikari/.githooks/pre-commit:10-12); **input carries none** (listing) — the named precedent is already CI-free; prioritree: deferred per the ruling, with the measured GitHub remote (§5) |

## 5. The git-state datum

- **prioritree hooksPath today: UNSET.** `prioritree/.git/config` is 13 lines, `[core]` block at :1-7 with **no `hooksPath`** — the greenfield datum. Remote: `git@github.com:markalosey/prioritree.git` (prioritree/.git/config:9) — **the only GitHub-hosted tree in the family** (measured remotes: input → `gitea.kepric.io` at input/.git/config:9; tane → `gitea.kepric.io` at tane/.git/config:10; hikari → `192.168.1.22` gitea at hikari/.git/config:9). The Q-setup-arch ruling "prioritree is a GitHub project" (store/.junro/junro.json:397) is mirrored in the measured wire.
- **The sibling activation precedents (measured):** tane holds its hooks via config — **`hooksPath = .githooks` at tane/.git/config:8** — this is the config-read precedent for the banked form. kepric-input's config carries **no hooksPath** (input/.git/config:1-14) despite carrying `.githooks/pre-commit` (listing) — the file exists but the config doesn't point at it; the activation question at the named precedent tree is an **open datum** that belongs to the harness unit's discover leg (adjacent to Q-tool-registration, store/.junro/junro.json:418-421). hikari uses neither: copy-based install (hikari/make/hooks.mk:13-27), no hooksPath (hikari/.git/config:1-62).
- **`.gitignore` coverage of the derived dirs at the siblings (measured):** `.venv` — input :133, tane :13, hikari :140; `.ruff_cache/` — input :172, tane :19, hikari :179; `.pytest_cache/` — input :52, tane :17, hikari :59; `.junro/` — **input :181 only** (tane and hikari: absent); `.opencode/` derived views — tane :46-47, hikari :198-199, **input: none** (confirming store/plan/keikaku-composition.md:68 verbatim).

## 6. Edges named for the brief (measured, not ruled here)

1. **The Python pin spread.** input 3.13 (.python-version:1 + requires-python :6) vs hikari 3.12 (.python-version:1, pyright :200) vs tane unpinned (no file; pyproject :5). The named precedent tree says 3.13; the floor-idiom tree says 3.12. The census recommends 3.13 (the named precedent); the brief rules the pin, and `.python-version`, `requires-python`, and any `pythonVersion` in `[tool.pyright]` must agree.
2. **lint vs typecheck target composition** (§3.10 divergence 3) — floor-green names dev/test/lint only; the pyright bar is a separate gate condition. Brief's call.
3. **The smoke test is gate-derived, not sibling-copied** (§3.6) — no sibling carries one; its shape is the brief's.
4. **Out of this packet's scope, named so the brief doesn't re-dispatch:** Q-tool-registration (open, store/.junro/junro.json:418-421), the derived-view gitignore entries (harness-scope, G-HARNESS condition 1, junro.json:197), the friction store's home/birth mechanism (store/plan/keikaku-composition.md:68), the `.opencode/` fixed-five engine inventory (Q-harness ruling, junro.json:410), and kepric-input's hook-activation gap (§5) — all ride build/harness's discover leg per the composition (store/plan/keikaku-composition.md:58, :65-68).

**Census closed. Boundary held: read-only, no writes, no mutations, no filings. Every claim above is cited at source.**
