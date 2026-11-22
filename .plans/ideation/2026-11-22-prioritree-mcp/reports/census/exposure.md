<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/exposure

**Route:** prioritree-mcp (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T20:24:17Z |
| 2 | report | shindan | 2026-11-22T20:27:16Z |
## Reported by shindan — 2026-11-22T20:27:16Z

SHINDAN — census/exposure — the exposure shape's diagnosis (2026-11-22)

STATE: three wrapping surfaces stand over one core, each already answering the four questions an MCP tool must answer; the tree's exposure problem is stable and fully precedented.

1. THE SURFACES. The core (session.py:161-318) speaks the five ops direct: register_run -> (run_id, manifest, count); next_pair -> (item_a, item_b, count) or ExhaustedQueue; cast_vote -> (vote_id, record, count, acknowledged); read_vote_state -> VoteCensus; tally_rank -> TallyResult whole. The CLI (cli.py:147-334) wraps through Persist: argv positionals/flags, marker-first tab-separated stdout — register prints the BARE STEM, next the pair triple, vote the vote/ack line (VoteRecord elided), state the votes/item summary (per_pair_counts, vote_log, run_id elided), tally the frozen whole. The service (service.py:321-528) wraps through the Serialize lock seam: six JSON routes carrying the same elisions, plus the sixth manifest query (operator id + registered_at elided) and one priced reconciliation — coverage.pair_counts re-keyed "item_a|item_b".

2. THE REFUSAL GRAMMAR. One grammar everywhere — expected/found/next_action — in three renderings. The core raises typed exceptions carrying the fields as ATTRIBUTES (RegistryRefusedError/VotesRefusedError/TallyRefusedError/StoreRefusedError; session wraps registry refusals into votes — ONE grammar downstream, session.py:140-159). The CLI renders str(e) verbatim to stderr, exit 1 (cli.py:376-378) — flat bytes, no fields. The service reads the fields as DATA at ONE render point (render_refusal, service.py:168-183) and dispatches by status: 404 the store's two families, 422 EXCLUSIVELY the door's value refusals, 409 the halt, 400 the re-badged schema violations (family grammar constructed), 405/404 the framework's routing refusals taught, 500 the crash envelope. An MCP tool over the core gets typed exceptions (structured, no reparse); over the wire, ThreePart bodies already; over the CLI, bytes that must pass through.

3. THE STAMPS. comparator_id + comparator_class are required and defaulted-nowhere at every tier: the core's cast_vote signature (session.py:240-248; the class gate {human, llm} at votes.py:33, 379-385), the CLI's vote POSITIONALS (cli.py:164-165, unvalidated pass-through), the service's CastVoteRequest fields (service.py:153-154). Both ride the dedup key and stamp every VoteRecord (votes.py:343-349, R5); both are durable in the file line and re-validated at load (run_store.py:417-435). Per the member-usable law (Q-mcp-tools ruling 2): the members' calls carry the SAME STAMPS the external agents carry — the MCP tools expose both as required parameters, minting no identity at the tool tier.

4. THE SIGNALS. DONE: the core raises ExhaustedQueue at next_pair's fall-through (session.py:228-238, the tally pointer in next_action); the CLI catches it BY TYPE -> stdout -> exit 0, DONE IS SUCCESS (cli.py:373-375); the service returns a 200 STATE {done: true, expected, found, next_action} (service.py:374-376). HALT: TallyRefusedError propagates verbatim from tally_rank; the CLI folds it into exit-1 stderr (indistinguishable from refusals except by bytes); the service holds it at 409 with the three-key body (service.py:479-480). An MCP tool must keep both strictly binary: a served pair vs a done state, a ranked whole vs a halted refusal — the type/status distinction IS the signal, never the message text.

CONDITION: honest — all three surfaces in-tree, consistent on one grammar, no drift found between the wrappers' elisions and their briefs; the MCP tier inherits a stable exposure shape with the ThreePart mandatory at its refusals already ruled.
