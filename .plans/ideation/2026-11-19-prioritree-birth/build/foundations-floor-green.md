# build/foundations-floor-green — the collaborator's floor-green run (the runtime evidence)

## 0. Provenance

- **The hand:** the collaborator's (marklosey@Mac, the prioritree root, 2026-11-19) — the no-seat-shelling rule; the two-tree hands rule (prioritree-side commands ride the collaborator's hand until the tree's own harness exists).
- **The capture:** the terminal output pasted verbatim in-session; the commands are the brief's §3 hands-split in the ruled order (uv lock → the hooksPath pointer → the floor-green run).
- **The instrument boundary:** no seat holds a prioritree-side shell (jikko/kensho packs carry file verbs + hikari's Docker-bound test tool only) — this captured run IS the runtime evidence; kensho's G-FOUNDATIONS verification reads it as such, never re-fabricating it. The seat-side read-backs (the files, the configs, the lock, .git/config) are kensho's own instruments.

## 1. The run, verbatim

```
marklosey@Mac prioritree % uv lock
Using CPython 3.13.9
Resolved 11 packages in 324ms
marklosey@Mac prioritree % git config core.hooksPath .githooks
marklosey@Mac prioritree % make dev && make test && make lint && make typecheck
uv sync
Using CPython 3.13.9
Creating virtual environment at: .venv
Resolved 11 packages in 11ms
      Built prioritree @ file:///Users/marklosey/projects/prioritree
Prepared 10 packages in 3.79s
Installed 10 packages in 86ms
 + iniconfig==2.3.1
 + nodeenv==1.12.0
 + packaging==26.3
 + pluggy==1.7.0
 + prioritree==0.1.0 (from file:///Users/marklosey/projects/prioritree)
 + pygments==2.21.0
 + pyright==1.1.414
 + pytest==9.2.0
 + ruff==0.17.6
 + typing-extensions==4.16.0
uv run pytest
==================================================== test session starts =====================================================
platform darwin -- Python 3.13.9, pytest-9.2.0, pluggy-1.7.0
rootdir: /Users/marklosey/projects/prioritree
configfile: pyproject.toml
collected 1 item

tests/test_smoke.py .                                                                                                  [100%]

===================================================== 1 passed in 0.01s ======================================================
uv run ruff check src/ tests/
warning: `incorrect-blank-line-before-class` (D203) and `blank-line-before-class` (D211) are incompatible. Ignoring `incorrect-blank-line-before-class`.
warning: `multi-line-summary-first-line` (D212) and `multi-line-summary-second-line` (D213) are incompatible. Ignoring `multi-line-summary-second-line`.
All checks passed!
uv run pyright
0 errors, 0 warnings, 0 informations
marklosey@Mac prioritree % 
```

## 2. The read of the capture (shinko's annotations, the data named)

- **uv lock:** green — CPython 3.13.9 (the pin resolved from `.python-version`), 11 packages resolved; the lock born small as banked (zero runtime deps + the dev group). On-disk read-back: `uv.lock` 141 lines, header `version = 1 / revision = 3 / requires-python = ">=3.13"`, `prioritree 0.1.0 source = { editable = "." }`, dev = pyright/pytest/ruff.
- **git config core.hooksPath .githooks:** no output = success; the on-disk read-back shows `hooksPath = .githooks` at `.git/config:8` — the pointer landed (inert until the harness unit emits the hook file: the hookless window, named honestly).
- **make dev (uv sync):** green — the venv created at 3.13.9, `Built prioritree` + `prioritree==0.1.0 (from file:///...)` in the install set — the editable install that resolves `import prioritree` (the jikko-time no-venv datum CLOSED here). Zero warnings in the output.
- **make test (uv run pytest):** **1 passed in 0.01s** — `tests/test_smoke.py` collected as the suite's one item, zero warnings (no warnings-summary in the output). Datum named: `configfile: pyproject.toml` — pytest 9.2 anchors rootdir at the bare pyproject (no `[tool.pytest.ini_options]` needed, the banked bare form).
- **make lint (uv run ruff check src/ tests/):** **All checks passed!** — zero findings, exit 0. TWO CONFIG META-WARNINGS ride the output (named as data; the gate's adjudication at the verification): ruff's ALL-select carries mutually exclusive docstring pairs (D203/D211, D212/D213) and auto-resolves each (ignoring D203 and D213) with a warning — NOT findings; the same class rides tane's own ALL select. A rider candidate for a future named ruling: pin the docstyle convention to silence the meta-warnings.
- **make typecheck (uv run pyright):** **"0 errors, 0 warnings, 0 informations"** — the verbatim summary line, the condition-3 read-back datum exactly as banked.
- **The && chain's completion through typecheck:** all four targets exited 0 (shell && semantics — any non-zero exit would have stopped the chain).

## 3. What this closes

- The jikko-time no-venv datum (pyright's unresolved-import at the build) — CLOSED by the editable install.
- The gate's runtime legs (conditions 1-4) — the evidence for kensho's G-FOUNDATIONS verification; the read-back legs (condition 5) are kensho's own instruments. The increment's commit lands at the gate's green (the one-commit-per-increment rhythm); `uv.lock` rides that commit.
