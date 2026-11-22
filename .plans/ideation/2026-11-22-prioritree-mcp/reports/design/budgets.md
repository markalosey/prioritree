<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — design/budgets

**Route:** prioritree-mcp (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T20:32:28Z |
| 2 | report | keisan | 2026-11-22T20:35:56Z |
## Reported by keisan — 2026-11-22T20:35:56Z

# design/budgets — the token budgets calculated (keisan, 2026-11-22)

GROUND READ: reports/census/ouncemcp.md (startup 4,000 default; definition 250/500/1,000; result 2,000; o200k_base; per-tool result_tokens + budget_reason; lists-first schema-safe shaping); birth R6 (n ≤ 100 verified at full coverage); tally.py (TallyResult); votes.py (VoteCensus); service.py (the elisions: vote_log dropped at census, pair_counts re-keyed at tally).

ASSUMPTIONS STATED: ids the RUNITEM_A form ≈ 4 tokens; a JSON map entry ≈ 8; a pair_counts entry "A|B": N ≈ 12; arithmetic on the calculate surface.

1. STARTUP — the five definitions vs 4,000: run.register 170, pair.serve 155, vote.cast 265, state.census 120, tally.rank 295. Sum = 1,005 = 25% of the default. RULE: no startup_tokens override — the default rides.

2. DEFINITIONS — 250/500/1,000: all five under the 500 warn, none near the 1,000 fail. vote.cast (265) and tally.rank (295) sit over the 250 target — the cure is authorial (tight descriptions); a definition-budget override does not exist (budget_reason pairs with result_tokens only).

3. RESULTS vs the 2,000 default:
- register ack {run_id} ≈ 15 — default.
- pair.serve {item_a, item_b, count} ≈ 30 — default.
- vote.cast ack {vote_id, count, acknowledged} ≈ 25 — default.
- state.census {total, items} at n=100: 100×8+10 = 810 — default; the service's own elision precedent holds (per_pair_counts and vote_log never cross the wire).
- tally.rank at n=100, the honest whole: pair_counts 4,950×12 = 59,400 + three per-item maps 300×8 = 2,400 + ranked_groups 700 + components 700 + ~40 = 63,240 → 31.6× the default. NO override can honestly cover that.

THE LOAD-BEARING RULING: pair_counts is 94% of the mass — the O(n²) term. A result_tokens override is the wrong instrument; the DESIGN DECISION rides the elision precedent — the MCP return model ELIDES coverage.pair_counts, the coverage block carrying the summary totals (pairs_expected = 4,950, pairs_at_quorum). The elided whole: 63,240 − 59,400 + 20 = 3,860 → 1.93× the default → tally.rank takes result_tokens = 4,500, budget_reason: "the frozen whole at n=100 minus the elided pair mass — 100 ids in ranked groups + components + the three per-item maps ≈ 3,860; 4,500 holds the verified ceiling with 640 tokens (~16%) headroom."

4. SHAPING'S FIT: with pair_counts designed out, every result fits at the verified ceiling — the lists-first trims never fire in the honest envelope. Past n=100 (R6's far side, earned-later) the first pressure is the ranked_groups/components lists (trimmed + next_cursor-paged, schema-safe); the per-item maps are objects, unlisted — pressure there is a later earn. HAZARD NAMED: the SAFE HALT's found can name all 4,950 under-quorum pairs ≈ 4,950×14 ≈ 69,300 — the refusal render must cap/summarize (the shortfall count + the first pairs), the same O(n²) mass arriving through the error-value channel.
