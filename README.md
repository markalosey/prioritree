# Priori-tree

Priori-tree is a generalized prioritization system: for any list and comparison operator, run the pairwise permutations, store the votes, tally — the output list is in a superior order than sizing individual items, because discernment between two items is easy (for humans and LLMs) while absolute sizing is not.

Measured (2026-11-21): pairs + tally beats absolute sizing at equal budget in 51 of 54 in-band cells (94.4%; the 3 exceptions narrow and seed-local) — the record at `.plans/ideation/2026-11-21-budget-curve/build/budget-curve-record.md`.

The comparator class is both human AND LLM — both vote through the same vote interface; the tally is a pure function of the stored votes.

> Priori-tree is a generalized prioritization system based on the concept that LLM and Humans are great at discerning the difference between two items but not great at sizing an item. That is a simplification. Consider: a human is great at determining that a basketball is larger than a grapefruit. But not great as identifying the exact dimensions of a grapefruit or a basketball. By taking a list and running through the pairwise permutations for any given comparision operator. Storing the votes, then tallying. we get a list out that is in a superior order than trying to size individual items.
>
> — the collaborator's Q-purpose ruling, 2026-11-19 (verbatim)

## Architecture

All four forms, one layered architecture, library-first (the collaborator's Q-setup-arch ruling, 2026-11-19):

- **Library — `src/prioritree` — BUILT (2026-11-20, the prioritree-core effort):** the pure-logic core (items, comparison operator, pair scheduling, votes, tally) at the bottom of the stack. Data plane = pure logic: stateless scoring/ranking core, votes are data in/out, no DB at birth.
- **CLI — BUILT (2026-11-21, the prioritree-cli effort):** wraps the core — the five-op surface at the command line (register → next → vote → state → tally).
- **API service (FastAPI) — LIVE (2026-11-21, the prioritree-service effort):** serves the core — the five routes over HTTP (the lock seam beneath, the 500 crash envelope, the live-socket acceptance arc proven; the tree's first runtime deps: fastapi + uvicorn[standard]).
- **Web app — banked (the stack's fourth layer):** fronts the service (the human comparator's vote surface).

## Status

Born 2026-11-19 (the setup: the skeleton, the kumi harness, the tool grants). The core library built 2026-11-20 (six units, all gates green); the CLI built 2026-11-21 (three units); the claim measured 2026-11-21 (pairs + tally beats absolute sizing at equal budget — 51 of 54 in-band cells); the API service live 2026-11-21 (three units, the live-socket acceptance proven, 131 tests green at close). The MCP tier is the ruled next effort (OunceMCP lands the five ops as its tools — Q-mcp-surface's banked ruling, the condition fired at the service era's arrival). CI is deferred — git hooks and local gates stand in.
