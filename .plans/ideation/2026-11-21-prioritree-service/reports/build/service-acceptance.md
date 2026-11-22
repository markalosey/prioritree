<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — build/service-acceptance

**Route:** prioritree-service (composed) | **Events:** 5 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T03:16:18Z |
| 2 | result | shinko | 2026-11-22T03:16:33Z |
| 3 | gate | shinko | 2026-11-22T03:16:44Z |
| 4 | gate | shinko | 2026-11-22T03:16:52Z |
| 5 | report | kensho | 2026-11-22T03:54:54Z |
## Reported by kensho — 2026-11-22T03:54:54Z

kensho's independent re-run of build/service-acceptance (the G-SERVICE-ACCEPTANCE evidence leg), zero edits, fresh process — THE FINAL BUILD UNIT, the route's build whole.

THE RUNS (at my own hand): uv run pytest — "131 passed in 26.09s", zero warnings (jikko's floor reproduced FIRST RUN: 131 passed in 30.27s; the wall clock's boots ~12s the per-test isolation's honest price); uv run ruff — "All checks passed!"; uv run pyright — "0 errors, 0 warnings, 0 informations".

THE READ-BACK (a-e CONFIRMED, zero discrepancies): (a) THE BOOT INSTRUMENT — the sibling-binary discovery, the pinned fixed-argv list (never a shell string), the banner regex + the deadline (a timeout FAILS never skips), the 404-as-ready probe (the whole chain proven in one call), the function-scoped fixture (boot => probe => yield => terminate => wait => kill-backstop); (b) THE FOUR ARCS — the seven-request arc (each body asserted field-for-field, the DONE at 200 with the pointer, the tally's frozen whole); the replay (two fresh homes, byte-identical .content lists — THE BYTES); the four refusals (404/422/409/400, the two grammars tested apart); THE CONCURRENCY ARC (the Barrier release, the two threads with their own clients, the distinct comparator_ids, the aggregate-only assertions — the census total 4, the vote-id SET unique, the ORDER never asserted, the file's direct read via Persist.load the oracle: 4 records, the id set, the per-pair counts exact); (c) THE FENCE — the harness's product imports exactly one (Persist the oracle; the app NEVER imported: the subprocess the only channel); (d) ZERO in-code ignores; the pyproject entry exactly ["S603", "S607"] with the named-ruling comment; (e) THE DOCSTRINGS + CONSTANTS — the five fields at every public symbol, the named constants throughout.

Kensho's verdict (verbatim): "G-SERVICE-ACCEPTANCE's evidence leg: VERIFIED — the independent re-run green at my own hand (131 passed, zero warnings, 26.09s; ruff 'All checks passed!'; pyright '0 errors, 0 warnings, 0 informations'), every read-back a-e confirmed on disk; the unit works."

THE ROUTE'S BUILD WHOLE: three units green — service-store (the lock seam), service-face (the five routes, the crash envelope), service-acceptance (the live-socket arc + the concurrency proof); the close remains.
