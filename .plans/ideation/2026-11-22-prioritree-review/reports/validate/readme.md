<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — validate/readme

**Route:** prioritree-review (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T02:07:23Z |
| 2 | report | kensho | 2026-11-23T02:09:45Z |
## Reported by kensho — 2026-11-23T02:09:45Z

# KENSHO'S INDEPENDENT VERIFICATION — validate/readme (G-README's third condition, 2026-11-22)

Zero trust held: every README number and command re-derived at my own reads and my own floor run.

**THE CLAIMS — all verified against the tree:** deps 6 (pyproject:9); routes 6 (service.py's route decorators :321/:350/:380/:417/:451/:490 — the exception handlers are not routes); tests 197 at MY OWN RUN (below); the five tiers on disk (core modules, cli.py, service.py, web.py 654 lines / nine routes / 14 templates + 2 statics counted, mcp_server.py 580 lines / five named tools); the CLI transcript byte-checked against cli.py's own forms — register's bare stem (:213), next's pair triple (:239), vote/ack (:272-273), state's votes/item (:300-302), tally's rank/counts/coverage/pairs/version (:330-353), the DONE message byte-matches session.py:92 rendering :228-238 ("all 3 scheduled pairs at quorum k=1" — 3 items ⇒ 3 pairs, derived); the ranking (cilantro > aloe > basil) re-derived from the three votes — the counts lines agree; the Makefile's named targets all exist (PORT ?= 8000, HOST ?= 127.0.0.1); the LICENSE section = the landed file (MIT, Copyright (c) 2026 Mark Losey; pyproject:7 license = "MIT"); the clone URL = .git/config's origin; the Q-purpose blockquote byte-matches the birth store's ruling (the "comparision" typo preserved); the measured citation resolves (budget-curve-record.md:65 — 51 of 54, 94.4% verbatim).

**THE HONEST LINES — each true:** no-PyPI (no .github/, no CI, no publish lane; R4 defers the publish); the tool lane's web-absence (pyproject:19 wheel packages = ["src/prioritree"] — web/ lives at the root, outside the wheel); ruff-pending (.githooks/pre-commit:9-13 names PHASE 2 pending; the hook runs pyright only; PRIORITREE_HOOK_BYPASS=1 tracked); the hooksPath command (git never clones hooks; the pointer live at .git/config:8 here); the port note (mcp_server.py:574 hardcodes 8000 = the Makefile's PORT default — the collision real); the CWD law (STORE_HOME = Path(".prioritree/runs") relative, run_store.py:53; web.py:76-77 plain relative template/static homes); .prioritree/ gitignored (.gitignore:184), minted at runtime.

**THE TWO HUNKS — cured:** CONTINUATION's four drifts: "twelve wrappers" at :19 (the :12 "TEN wrappers" is the dated tool-grants era record, historically accurate, out of the drift scope); "655" absent from the file, 654 at :65; :53's httpx2 era-annotated to the main table; the WHERE-TO-CONTINUE tail (:72-76) current — the MCP era "ARRIVED AND WHOLE" (:74) + the review effort named (:75-76). AGENTS.md: :1-:2 name the hikari-side engine; :4 the goal line byte-intact.

**THE FLOOR at my own hands — verbatim:** test: "197 passed in 26.09s"; lint: "All checks passed!"; typecheck: "0 errors, 0 warnings, 0 informations".

**THE VERDICT — G-README's three conditions (junro.json:500), each ruled:** 1 the rewrite per the approved spec — GREEN (Quickstart end-to-end, every stale number cured, tier-by-tier usage, discipline block, no-PyPI + uv-tool lanes — all landed, all true); 2 the fixes + every stale number cured — GREEN (the four drifts cured, eras current, AGENTS' regen truth honest); 3 the floor + my re-run — GREEN (197/lint/pyright at my own hand; this check green at every claim).
