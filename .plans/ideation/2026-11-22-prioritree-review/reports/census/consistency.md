<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/consistency

**Route:** prioritree-review (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T01:05:38Z |
| 2 | report | rikai | 2026-11-23T01:09:20Z |
## Reported by rikai — 2026-11-23T01:09:20Z

CONSISTENCY MAP — the doc surfaces vs the tree (rikai). Classes: stale | missing | wrong.

[1] README.md vs the tree
- "Web app — banked" (README:20) → web.py 654 lines, nine routes, mounted at service.py:540; 14 templates + 2 statics; four lifecycle targets; the ux effort closed 2026-11-22 → STALE.
- "The MCP tier is the ruled next effort" (README:24) → mcp_server.py's five OunceMCP tools (452-535), ouncemcp at pyproject:7, the mcp store EXECUTING → STALE; the tier also MISSING from the architecture list ("All four forms" README:15 — the tree has five tiers).
- "first runtime deps: fastapi + uvicorn[standard]" (README:19) → six at pyproject:7 (+ httpx2, jinja2, ouncemcp, python-multipart) → STALE.
- "the five routes over HTTP" (README:19) → six in service.py (the manifest query, :490) → STALE.
- "131 tests green at close" (README:24) → the service-era number; the ux close recorded 156; tests/ now 17 modules → STALE.
- Zero commands documented (no install, no usage, no make, no CLI form) → MISSING: the product is unoperable from the README alone.
- HOLD: the purpose sentence byte-identical to pyproject:4; the measured citation resolves (the 54-cell record, the 3 seed-1109 negatives match); "Born 2026-11-19"; the five CLI ops (cli.py:44-48); "no DB" (file-backed JSONL); {human, llm} (votes.py:33).

[2] AGENTS.md / CONTINUATION.md vs the tree
- AGENTS.md's regen header cites scripts/generation/clarity_scaffold.py → the directory exists EMPTY (0 entries); the generator lives in the sibling hikari tree → MISSING at the cited path.
- The goal line == CONTINUATION:8's verbatim ruling → HOLDS.
- "the next effort: the MCP-surface era... composes next" (CONTINUATION:72-76) → the store born and executing, mcp_server landed → STALE (one era behind the tree).
- "httpx2 dev the root cure" (CONTINUATION:53) → httpx2 rides the MAIN table (pyproject:7, the web tier's runtime import web.py:50); the dev group is pytest/pyright/ruff only → WRONG as present state (stale as service-era history).
- "the ten wrappers" (CONTINUATION:19) → twelve at .opencode/tools/ (+ kumi_render.ts, lifecycle.ts, both the doc's own later arrivals) → STALE.
- "web.py at 655 lines" (CONTINUATION:65) → 654 → WRONG (one-line drift).
- Verified: the friction store (.plans/state/friction-ledger.jsonl) exists; 13 seats in opencode.json; the lifecycle grant map matches (allow at jikko/kensho/rikai/shindan/shinko).

[3] Internal consistency
- README:3 == pyproject:4 byte-identical. The Makefile's four transitions == the lifecycle tool's four; log/output the tool's reads (no Make target — no contradiction); the Makefile's launch form == service.py:33's documented uvicorn form; the RUN-9999 probe == the 404-as-ready form.
- Tier fences hold at the import level (cli stdlib-only; run_store json+pathlib; service composes Serialize only); service.py:44-45's "first runtime deps live at THIS tier alone" now shared with web.py's fastapi/httpx2 imports — the fence's wording predates the web tier.
- The deeper fact: the fences are import-level; pyproject's table is FLAT (no per-tier extras) — the packaged CLI drags all six deps despite cli.py:19's "zero runtime dependencies".
- The route teachings agree (service.py:309-318's six == web.py:102-109's six); the vocabulary guards (mcp_server.py:97-101) enforce the no-fork claim by construction.

[4] The fresh-clone mechanism
- Tracked: web/templates (14) + web/static (2) ride the CLONE; .plans rides → the README's citation resolves at a fresh clone. Absent: .prioritree/, .venv/, /build/, /.junro/.
- The wheel carries ONLY src/prioritree (pyproject:16-17) — web/ sits outside it → pip/uv install carries NO templates; web.py:119-120 mounts CWD-relative web/static (check_dir=False, the absent-dir cure) + web/templates → outside the repo every page folds to an honest 500 (TemplateNotFound), static 404s: the web tier is clone-only by construction.
- STORE_HOME = Path(".prioritree/runs") (run_store.py:53), CWD-relative everywhere: the CLI's --home redirects per invocation; the service hardwires it at construction (service.py:165, the env knob BANKED); the MCP tier likewise (mcp_server.py:110-112) → a server booted from another cwd silently uses a DIFFERENT store; the repo-root discipline is named in the Makefile help and the docstrings, absent from the README.
- The boot chain: no .venv → make start refuses naming "make dev first" (Makefile:25-28) → uv sync resolves all six from uv.lock at 3.13 → make start mkdirs .prioritree (pid + log + the RUN-9999 read-back).
- The pre-commit hook is DEAD at a fresh clone: .githooks/pre-commit is tracked, but the hooksPath POINTER lives in .git/config — never cloned; "git hooks stand in" is silently false until the pointer is set by hand.
- Port 8000 is the shared default of BOTH make start (PORT ?= 8000) and mcp --serve (mcp_server.py:574) — the two servers collide on the same port.
