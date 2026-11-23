<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/mechanism

**Route:** prioritree-ci (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T23:02:33Z |
| 2 | report | rikai | 2026-11-23T23:05:47Z |
## Reported by rikai — 2026-11-23T23:05:47Z

# THE CI MECHANISM MAP (rikai, census/mechanism, 2026-11-23)

## 1. THE RUNNER'S ENVIRONMENT
- ubuntu-latest preinstalls a Python range that carries 3.13 (the runner-images' toolset) — but the workflow need not touch it: setup-uv installs uv (the workflow-native form — PATH/cache/versioned; the curl|sh form installs the same binary outside Actions' forms).
- uv resolves Python itself: with no python-version input, uv run/sync read the project's .python-version = 3.13 against requires-python ">=3.13" (pyproject.toml:6), preferring uv's managed interpreter (downloaded when absent). The tree's form is the source; the workflow re-declares nothing (the configurability law).
- actions/checkout@v4 clones into $GITHUB_WORKSPACE (ubuntu: /home/runner/work/<repo>/<repo>), shallow (fetch-depth 1) by default; every run: step executes with the workspace root as CWD — the workspace IS the cwd, the same law as the clone.
- STORE_HOME is CWD-relative by law (run_store.py:48-53; cli.py:144-145; service.py:165; mcp_server.py:110-112); the suite never mints at the workspace — every test takes tmp_path homes (test_cli.py:57; the subprocess boot mints under tmp_path/.prioritree/runs — test_service_acceptance.py:380,428). .gitignore:184 ignores .prioritree/ besides; CI never commits. The hook never fires at the runner: core.hooksPath is local config the runner's clone never sets (README.md:26) — enforcement must ride the workflow itself.

## 2. THE MAKE TARGETS AT THE RUNNER
- make is preinstalled on the ubuntu image (the runner-images' toolset: GNU make). make test = `uv run pytest` (Makefile:14): needs uv (setup-uv) + the lock (the checkout's uv.lock at root) + a 3.13 (uv resolves) + a venv.
- `uv run` auto-syncs on first run: .venv mints at the workspace from the lock, the project installed EDITABLE (uv sync's default; hatchling's src-layout, pyproject.toml:18-19) — `import prioritree` and the console script (pyproject.toml:15-16) resolve inside .venv; NO PYTHONPATH needed.
- The price: the first uv run per job pays the whole sync on a fresh runner (download + install: the six runtime deps + the dev trio + the project); setup-uv's enable-cache (auto on hosted runners, keyed by the lock) persists uv's cache between runs. make dev (Makefile:11) is the explicit same price; the floor's ruff/pyright configs ride pyproject.toml (ruff 33-36; pyright 161-175) — discovered at the workspace, never re-declared.

## 3. THE CODEQL MECHANISM
- Advanced chain: init@v3 with languages: python, then analyze@v3; python is interpreted — no build required (the docs' starter carries autobuild, which only attempts dependency installs; the buildless form omits it). Tree ownership: init's config-file: ./codeql-config.yml — the file's form: name/paths/paths-ignore/queries(+packs).
- The scan set at HEAD: src/ (15 modules) + tests/ — the tree's only .py; scripts/generation/ is EMPTY at HEAD; .plans/ carries zero .py (grep *.py: no files) — provenance records (md/json/jsonl), no Python.
- Default-setup overlap: both CAN run at once (duplicate results per the docs); landing the advanced workflow does NOT disable default setup — the ownership transition is a manual settings change (disable default at Code Security settings); the config-file form is exactly what default setup cannot carry (FR-MEM-0033's lesson).
- The .plans candidates' mechanics, honestly: python extraction reads only .py — .plans yields zero findings at near-zero price either way; paths-ignore [".plans"] is a guard against future noise, not a price cut; scanning READS, never writes — the provenance law's letter (preserved, never scrubbed) untouched by both candidates. The ruling is the design lane's.

## 4. THE TRIGGER MECHANICS
- `on: push: branches: [main]` + `on: pull_request: branches: [main]`: the pull_request filter matches the PR's BASE branch; push fires on main commits, pull_request on opened/synchronize/reopened into main.
- Fork PRs: public repos' hosted minutes are free — fork-PR workflows run in the base repo's context and bill the base nothing (the docs' public form); private repos: the free allocation bills the base, external-fork workflows require approval. The repo's visibility is not recorded in the tree — an honest absence (R1 names both forms).
- `concurrency: {group, cancel-in-progress: true}`: a newly queued run in the group cancels the in-progress one — at the burst rate, superseded runs die early; the minutes converge toward the latest run only.
