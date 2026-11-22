<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — design/member-path

**Route:** prioritree-mcp (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T20:32:18Z |
| 2 | report | suisen | 2026-11-22T20:36:35Z |
## Reported by suisen — 2026-11-22T20:36:35Z

# SUISEN — design/member-path — the member-usable path ruled (2026-11-22)

## 1. THE FORM RULED — harness-native: the server wired into opencode's mcp config, stdio, launch-delivered
RECOMMENDED: the harness-native form — prioritree's own MCP server wired into opencode's mcp config block (the opencode.json:514-521 form), the five tools riding into the granted seats' packs AS harness tools. Reasons: (1) THE LAW'S OWN NAMED FORM — "the MCP server's own callable surface exposed to the seats" (Q-mcp-tools ruling 2, junro.json:243); the seats call THE MCP TOOLS directly, opencode an MCP host (any-host works — ouncemcp census §6's verified claim). (2) MINIMUM CEREMONY — zero new wrapper/engine surface in prioritree's tree: the wrapper→client-CLI form adds JSON-parsing wrapper weight (precedented once, shinko-only) for what the harness already provides; the wrapper→HTTP form is heavier than any standing member-facing wrapper (the census's own price); the in-process engine pays the per-call interpreter boot AND the MemoryStore reset (idempotent replay dying per call). (3) THE GRANT MAP DELIVERS through the standing two layers — per-seat permission rows for MCP tools are proven IN opencode.json itself (the sequential-thinking_sequentialthinking row: the {server}_{tool} form) + the @generated Pack Routing rows; and the per-tool enforcement is STRONGER than the wrapper's op-routing (the write tools not even callable at the read seats). (4) THE RESTART LAW rides by construction (the config read at launch). The lifecycle precedent extended is its GRANT MAP's form (full/read/deny), not its argv-shim form — the harness IS the client; no shim needed. The tier's machinery ridden whole: budgets shape the members' results (_meta.ouncemcp self-reports), idempotency keys their retries, the schema+gate verify their stamps.

## 2. THE MCP GRANT MAP (the lifecycle map's form extended to the five tools)
- FULL — register_run, next_pair, cast_vote, read_vote_state, tally_rank: jikko, kensho, shinko (the working seats: build exercises the server, verify calls the surface, dispatch coordinates).
- READ — next_pair, read_vote_state, tally_rank: rikai, shindan (the analysis seats: diagnosis reads the run's state, the pair served, the tally; never writes).
- DENY — rows absent + permission deny: keikaku, tansa, suisen, keisan, hyoka, moho, togo, hansei. Minimum grant held; a dispatched live exercise (a blind-walk of the running surface, an adversarial probe) earns its own grant AT that dispatch — the map is a floor, never a ceiling.

## 3. THE STAMPS — VERIFIED AT THE SURFACE, NEVER MERELY CARRIED
The members' calls carry comparator_id + comparator_class as the tools' REQUIRED arguments: the Pydantic input (ouncemcp §1 — required fields, bounds; the server refuses to start without them) rejects a stampless call at the SCHEMA; the core's gate (the Session class the server rides) rejects the semantic violations — unknown class, unregistered comparator, the duplicate vote (R9 at the core). The harness-native path CANNOT bypass: the members' calls ARE the server's tool calls — no path past the surface exists. The direct-core ruling's lesson is the counterfactual priced: that path was ruled out BECAUSE it carried-without-verifying; this path verifies by construction — the members meet the SAME verification the external agents meet. Caller-binding rides OunceMCP's caller-keyed idempotency (§3); per-seat identity pinning is NOT added — the law asks the same stamps and the same verification, and minimum ceremony holds.

## 4. THE OPERATIONAL NOTES
- LAUNCH DELIVERY (the restart law, FR-MEM-0014): the grant lands at the tree, the delivery at the launch — a live session never sees it; the build unit's report carries the restart note verbatim (the lifecycle grants' own delivery form).
- THE RUN FORM: stdio, harness-launched per session — opencode owns the process (launch at session start, teardown at end); NO member-facing lifecycle ceremony (no ports, no make targets for the member path). The semantic state is disk-backed at the core (registry+ledger injected — session.py:124-138) — per-session servers share the store; only OunceMCP's MemoryStore (transport-level replay) resets per session, and the core's own dedup holds across sessions. NAMED RISK handed to the mcp-server unit: concurrent writers (the seats' session servers + the service + external agents) on the one store — the server's store discipline resolves it.
- THE SERVER'S OWN LIFECYCLE: the lifecycle-integration unit serves the SHARED HTTP form (the external agents' long-lived server — mcp-start/stop/status riding the make-target form); the member path needs none of it. One server implementation, two run forms (§4: stdio AND HTTP).
- THE GRANT'S EDIT HOME: BOTH layers are scaffold-generated (opencode.json + the 13 prompts — the source out-of-tree at hikari); the rows land at the scaffold source, the regen emits, never hand-edited — zero prioritree-tree files beyond the server itself.
