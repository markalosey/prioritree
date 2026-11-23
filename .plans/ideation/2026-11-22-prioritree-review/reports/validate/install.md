<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — validate/install

**Route:** prioritree-review (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T02:54:43Z |
| 2 | report | kensho | 2026-11-23T02:57:10Z |
## Reported by kensho — 2026-11-23T02:57:10Z

R6 — kensho, validate/install — the live install verification, zero trust. MY PACK'S FOLDS NAMED UP FRONT: no build verb, no install/exec verb — never faked; inspected via the gate's named instruments.

THE CARRIAGE (a): pyproject:18-19 packages=["src/prioritree"] — the 15 modules ride by construction (mcp_server.py among them, the MCP confirmed riding); pyproject:29-31 force-include web/templates→prioritree/templates + web/static→prioritree/static (the ruled mechanism, flat dests, no prioritree/web/ shadow of web.py's portion); pyproject:15-16 prioritree=prioritree.cli:command (the CLI entry). The tree reads: src/prioritree = 15 modules; web/templates = 14 authored; web/static = 2 files. web.py:126-147 resolve(): the CWD's copy WINS, files("prioritree") the fallback — the CWD question answered honestly (README:159; the clone byte-preserved at the CWD branch).

THE INSTALL LANE (b): uv build + uv tool install . NOT RUNNABLE at my pack — the fold named for the gate's hands (MOHO'S RE-WALK walks/installs). What I ran: the clone's serve lane LIVE — make start answered (404 read-back = the Makefile:31 probe's ready form); the RUN-9999 probe's body verbatim: {"expected":"a run file in the store home (live: RUN-0001, RUN-0002)","found":"no run file for 'RUN-9999' in .prioritree/runs","next_action":"register a run first, or cite a live RUN-{####} id — the home is the truth (the dir, never a hidden global)"}; make stop drained clean (pid gone, port refused).

THE FLOOR (c), verbatim at my own hands: test = "200 passed in 27.26s" | lint = "All checks passed!" | typecheck = "0 errors, 0 warnings, 0 informations".

SPOT-CHECKS: the CWD branch first — verified (web.py:145-147); the CLI home — run_store.py:53 STORE_HOME=Path(".prioritree/runs") CWD-relative, cli.py:57 --home the escape. FINDING (honest, for the gate): README:55/:186 say "197 tests green" — the suite is 200 (the install unit's own growth left the README's number stale; a one-line cure).

THE VERDICT — G-INSTALL's four: (1) the wheel per the spec — GREEN at my instruments (force-include + packages + scripts + resolve() + the suite); the wheel's own bytes = the named fold. (2) the lanes — the clone lane GREEN live; the uv tool lane NOT verified at my hands, named to MOHO'S RE-WALK, never faked. (3) MOHO'S RE-WALK — NOT verified here (the parallel packet); named for the gate. (4) the floor + my re-run — GREEN: 200 / ruff clean / pyright 0-0-0.
