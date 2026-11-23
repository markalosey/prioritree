<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — design/blind-walk

**Route:** prioritree-review (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T01:10:53Z |
| 2 | report | moho | 2026-11-23T01:11:39Z |
## Reported by moho — 2026-11-23T01:11:39Z

MOHO (盲歩) — THE README WALK, 2026-11-22. Surface: README.md alone (24 lines) — the cold visitor's only doc.

ARRIVAL: strong pitch — pairwise votes, tallied, beat absolute sizing (94.4% measured); four tiers named: library (src/prioritree), CLI, FastAPI service, web (banked).

INSTALL ATTEMPT: DEAD END — the README teaches zero runnable commands. No install section, no setup step, no package name. The cold user's every move (pip? uv sync? make?) is an unlicensed guess.

USAGE STORY: CLI — five ops NAMED (register → next → vote → state → tally); binary + invocation MISSING. API — five routes NAMED over HTTP; start command, host, port, route paths MISSING. Library — path named; import surface MISSING.

FIRST SESSION: IMPOSSIBLE from the README — no list format shown, no vote example, no tally output. The op sequence is inferable; every keystroke is a guess.

FRICTION MAP: 1) install — no path; 2) CLI — no binary; 3) API — no launch line; 4) input format — unknown; 5) output shape — never shown; 6) process jargon cold-lands (kumi harness, OunceMCP, Q-rulings, .plans paths); 7) no license stated.

TOP THREE FIXES (user-pain order): 1) Quickstart — install + a first comparison, end-to-end under ten lines; 2) input/output examples — a list in, a vote, the tally out; 3) per-tier launch lines — the CLI invocation and the uvicorn start.

VERDICT: the README reports the build to the builders; the product is invisible to the user it was built for.
