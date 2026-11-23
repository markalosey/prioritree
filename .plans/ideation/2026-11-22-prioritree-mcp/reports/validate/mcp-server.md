<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — validate/mcp-server

**Route:** prioritree-mcp (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T23:57:12Z |
| 2 | report | kensho | 2026-11-23T00:00:22Z |
## Reported by kensho — 2026-11-23T00:00:22Z

# KENSHO — validate/mcp-server — the independent verification (my own runs, my own reads)

THE FLOOR (verbatim, my runs): pytest = 196 passed in 25.74s; ruff check src/ tests/ = All checks passed!; pyright = 0 errors, 0 warnings, 0 informations. My pointed probe re-run: tests/test_store_lock_face.py = 10 passed in 1.66s.

READ-BACK (the files my ruling rides): the spec reports/synthesize/mcpserverspec.md; src/prioritree/store_lock.py, mcp_server.py, service_store.py, cli.py, run_store.py:581-895; pyproject.toml; tests/test_store_lock_face.py, tests/test_mcp_server_face.py; .junro/junro.json.

THE EXACT-TASK LAW — every named deviation RULED:
- THE DEADLOCK DEVIATION: RULED legitimate-tree-forced, the cure SOUND. The spec's SS2(h) wrapped each tool body in `with _lock:` while SS3(a) carried the flock in the seam's own heads — composed, the body's Lock (open fd, LOCK_EX) would await the seam head's SECOND open on the same lockfile: flock binds per open file description, so the process deadlocks against itself. Verified myself: the reentrant arc (two opens, one path, one process) blocks until release — green under my run. The landed cure: the bodies ride the seam bare (all three tiers still compose — the seam IS the composition point); `_lock` guards the halt shaper's fresh read alone (mcp_server.py:420-421, a direct Persist.load — no seam call inside, no nesting; census()/manifest() are in-memory over the loaded door, run_store.py:842-895).
- store_lock deltas: RULED legitimate — `_store_home` set at __init__ (the spec's own __enter__ cited it unset, its bytes unrunnable); the IO tenant per the spec's NOTES verbatim (`IO[str] | None`, the None-guarded exit); Path under TYPE_CHECKING (annotations lazy, behavior-neutral).
- D205: RULED legitimate — pyproject:124-131, the named per-fire ruling (the tool docstrings ARE the wire descriptions verbatim; a summary blank line would fork the accepted bytes) — the spec SS3(c)'s own prediction.
- ThreadLock rename: RULED legitimate — service_store.py:27, the alias disambiguating threading.Lock from store_lock.Lock in one namespace; behavior-neutral.
- THE 300-CHAR CLIP: RULED non-stopping — the ouncemcp Failure render clips error text at Limits.max_error_chars=300 (the step-4 finding, named + asserted in test_mcp_server_face.py:363-380): the framework's own token-budget wire discipline; the structured ThreePart rides the payload whole, the K=10 cap already bounds the mass, the under-cap refusals fit whole. Not a fork of R5.

THE FOUR G-MCPSERVER CONDITIONS:
1. GREEN — the five tools per the spec: the definitions verbatim (all five docstrings + Field texts byte-checked); the ThreePart at ONE render point as data (attributes read, never str(e)); DONE a value never an error (done=true a RESULT); the K=10 cap honest (the elision named in found AND next_action, legs 1-2 whole — payload + wire both asserted).
2. GREEN — the flock seam composed by ALL three writer tiers: the service's six heads (:125/:146/:175/:196/:215/:240), the CLI's five windows (:206/:236/:262/:297/:327, render outside), the server's door (the seam's heads + the halt shaper's window); my own two-process probe green (child N casts beside parent M on one store, the mint-order load clean, ids contiguous, the lockfile never deleted).
3. GREEN — the floor: pyright 0/0, ruff zero findings, ouncemcp the landed dep (pyproject:7, the sorted position); my re-run green — the three acts + the pointed probe my own.
4. GREEN as the parallel leg — moho's implementation walk rides the gate as the packet walk/mcp-server (dispatched 2026-11-22T23:57:20Z); the ease-of-use findings are the gate's evidence, moho's to land — named, not verified here.

THE VERDICT: four-for-four green at my seat; the named deviations all legitimate-tree-forced or non-stopping; the exact-task law held against the approved spec.
