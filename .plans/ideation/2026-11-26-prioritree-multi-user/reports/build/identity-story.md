<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — build/identity-story

**Route:** prioritree-multi-user (executing) | **Events:** 4 | **Reports:** 2

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-26T23:53:31Z |
| 2 | report | jikko | 2026-11-26T23:58:47Z |
| 3 | dispatch | shinko | 2026-11-27T00:04:25Z |
| 4 | report | jikko | 2026-11-27T00:04:54Z |
## Reported by jikko — 2026-11-26T23:58:47Z

# R11 — the identity-story landing (build/identity-story, jikko, 2026-11-26)

LANDED: README.md alone (303→326 lines; one patch, 11 hunks, no findings) — the "## Multi-user" section WHOLE per the spec's fence at the verified placement + the twelve stale cures + the Status era entries; NOTHING else (zero source bytes, zero test bytes).
READ-BACK (a) the section's head verbatim: "## Multi-user" at :209, between the auth's :207 close and "## Input/Output Examples" :232 — the era order held.
READ-BACK (b) the honest-statement blockquote verbatim: "> **THE SESSION CURES THE UX COST, NEVER THE IDENTITY FABRICATION** > > — the design's honest statement, carried verbatim (`.plans/ideation/2026-11-26-prioritree-multi-user/reports/synthesize/multi-user-design.md` §3)" — byte-true against the design brief §3's hardest line, the citation's absolute path resolved.
READ-BACK (c) the stale cures' lines verbatim — the floor-475 site (:61): "Runtime dependencies: seven — `fastapi`, `httpx2`, `itsdangerous`, `jinja2`, `ouncemcp`, `python-multipart`, `uvicorn[standard]` (`pyproject.toml`). The quality floor: 475 tests green, pyright clean, ruff clean."; the counts site (:56): "`src/prioritree/web.py` (1241 lines, twelve lanes, 17 authored Jinja2 templates + 2 static files)"; one seam (:107): "each browser its own voter, the name asked once and remembered"; every cured count re-read at its source (475 at the suite's own run; seven at pyproject.toml:9; twelve at web.py:291-304; seventeen at web/templates; 1241 at web.py's tail; the pins at web.py:389-392/:382/:124-125, service.py:581-582); the told copies pasted byte-exact (sitting.html:7/:10/:13; web.py:277/:279/:1144/:1225-1226); the citations resolved (the two stores; the design brief §3).
FLOOR 1 — the suite: "475 passed in 41.68s" (475 expected, unbroken).
FLOOR 2 — the lint act (ruff): "All checks passed!" (zero findings).
FLOOR 3 — the typecheck act (pyright): "0 errors, 0 warnings, 0 informations".
## Reported by jikko — 2026-11-27T00:04:54Z

R11 (step 1b, jikko): count-cure applied — README.md:57 "645" → "681" (mcp_server.py's true length); one line, one patch hunk, applied clean.
Read-back (verbatim): - **MCP — live 2026-11-22.** The agent-callable tier: `src/prioritree/mcp_server.py` (681 lines, the five OunceMCP tools — `runs.register`, `runs.next`, `votes.cast`, `votes.census`, `runs.tally`; the `store_lock.py` flock seam), two run forms.
Files touched: README.md line 57 only — nothing else, no gaps found.
Not done: no verification (the coordinator runs the instruments); no other README edits.
