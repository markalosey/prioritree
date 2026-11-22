<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/mechanism

**Route:** prioritree-ux (executing) | **Events:** 5 | **Reports:** 2

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T09:20:23Z |
| 2 | result | shinko | 2026-11-22T09:28:50Z |
| 3 | report | shinko | 2026-11-22T09:28:55Z |
| 4 | dispatch | shinko | 2026-11-22T09:36:20Z |
| 5 | report | rikai | 2026-11-22T09:37:08Z |
## Reported by shinko — 2026-11-22T09:28:55Z

rikai's completion report (packet census/mechanism, recorded by shinko):

THE MECHANISM MAP LANDED — the chain, the route table, the shapes pinned. THE EVIDENCE SET: .junro/evidence/Q-ux-surface/census-mechanism-a.md + census-mechanism-b.md (the return verbatim in two regions).

THE MAP: (1) THE FIVE OPS' PUBLIC FACE — Session's signatures + return forms pinned (register_run → (run_id, manifest, count); next_pair → the bare triple, raises ExhaustedQueue as the DONE signal; cast_vote → the ack quadruple; read_vote_state → VoteCensus, NEVER refuses on coverage; tally_rank → TallyResult (ranked_groups tie-tuples, per_item wins/losses/ties, coverage datum, algorithm_version), ALWAYS refuses on coverage — the SAFE HALT). (2) THE WIRING — ALL FIVE OPS exposed 1:1 (POST /runs, GET /runs/{id}/next, POST /runs/{id}/votes, GET /runs/{id}/state, GET /runs/{id}/tally; status map 404/422/409/200-DONE/400-rebadge/500-fold; one render point). (3) THE STATE MECHANISM — module-level seam singleton per process; per-request full reconstruction (lock + Persist.load + fresh Session/Registry, re-register + in-order re-casts); the append-only JSONL files on disk are the ONLY cross-request state. (4) THE SEAMS — six named: register drops manifest+count (and the wire carries the FILE STEM id, the in-file handle never crossing — two id spaces); cast elides VoteRecord; state elides vote_log + per_pair_counts; tally re-keys pair_counts (the one priced reconciliation); DONE becomes a 200 value body; the 400 re-badge carries the native grammar. Ruled properties CONFIRMED holding at the wire: no-anchoring (next_pair bare), the audit/emission refusal asymmetry, tally's write-target-nothing.

The design lane's ground is whole: the CQRS mapping composes over this table.
## Reported by rikai — 2026-11-22T09:37:08Z

rikai — packet census/mechanism (prioritree-ux): the mechanism map — how the existing FastAPI server fronts the core's five-op interface today. READ-ONLY; no other act performed.

THE CORE'S PUBLIC FACE (src/prioritree/session.py, class Session — the composition layer the wrappers cite):
- register_run(items, operator, quorum=1) → (run_id, RunManifest, count); RegistryRefusedError wrapped into VotesRefusedError.
- next_pair(run_id, seed=None) → the bare (item_a, item_b, count) triple — no state, no scores; fall-through RAISES ExhaustedQueue, the DONE signal (three fields: expected/found/next_action).
- cast_vote(run_id, pair, winner, comparator_id, comparator_class, notes=None, supersedes=None) → the ack quadruple (vote_id, VoteRecord, count, acknowledged).
- read_vote_state(run_id) → VoteCensus (per_pair_counts over the full universe, per_item_counts, the full vote_log) — NEVER refuses on coverage.
- tally_rank(run_id) → frozen TallyResult (ranked_groups, per-item wins/losses/ties, CoverageDatum, algorithm_version); TallyRefusedError = the SAFE HALT — the emission ALWAYS refuses on coverage; write target NOTHING.

THE SERVER'S WIRING (src/prioritree/service.py — the ONLY server module; app = FastAPI() :152, launch uvicorn prioritree.service:app): all five ops exposed REST 1:1, none missing — POST /runs → register (201 {run_id: stem}); GET /runs/{run_id}/next?seed= → serve (200 the pair object; DONE → 200 {done: true + three fields}); POST /runs/{run_id}/votes → cast_vote (200 {vote_id, count, acknowledged}); GET /runs/{run_id}/state → census (200 {total, items}); GET /runs/{run_id}/tally → rank (200 asdict(TallyResult), 409 SAFE HALT). Status map: StoreRefusedError→404 (both families), VotesRefusedError→422, TallyRefusedError→409, ExhaustedQueue→200-DONE, RequestValidationError re-badged→400, uncaught→500 crash envelope. Refusals caught BY TYPE, rendered at one point (render_refusal).

THE STATE MECHANISM (the chain, named): (1) module-level per-process seam — app.state.seam = Serialize(STORE_HOME) at import; STORE_HOME = Path(".prioritree/runs"), CWD-relative (run_store.py:53). (2) per-request reconstruction under ONE process-wide threading.Lock — each Serialize verb acquires once around Persist.load + the act whole (service_store.py:118-208); load pre-pass-validates the JSONL file and rebuilds a FRESH in-memory door (Session(Registry()), re-register, in-order re-casts — run_store.py:684-705), so the dedup index is fresh by construction. (3) lifetime: lock/seam = process; in-memory core = one request; the append-only JSONL run files on disk are the only cross-request state (save-at-cast, one line + flush per write). Multi-process banked under single-worker.

THE SEAMS (envelope vs the core's ruled return forms): (1) register — the (run_id, manifest, count) triple collapses to {run_id: stem} alone, and the wire's id is the FILE STEM, not the core's in-file handle (two id spaces, run_store.py:536-539); (2) cast — VoteRecord ELIDED from the ack (durable in the file only); (3) state — vote_log and per_pair_counts elided ({"total","items"} only; "the stamps re-mint at load — rendering lies"); (4) tally — coverage.pair_counts re-keyed Pair→"item_a|item_b" strings (JSON keys; the one priced reconciliation); (5) DONE — the core's RAISED signal becomes a 200 VALUE body; (6) the 400 re-badge carries FastAPI's native {detail: [...]} grammar, NOT the three-field form; the 500 fabricates a three-part envelope with no core counterpart. Ruled properties holding at the wire: the state read never refuses on coverage; the tally always refuses on it (409); rank appends nothing.

READ-BACK (files actually read): .plans/ideation/2026-11-19-prioritree-birth/.junro/junro.json (whole — Q-solution-space's five-op ruling); src/prioritree/__init__.py, session.py, service.py, service_store.py, run_store.py (whole); votes.py :43-105, tally.py :40-154, registry.py :29-110, scheduler.py :28-42; greps: the fastapi sweep (service.py the sole server), the @app. route census, the value-type sweep. Zero redesign proposed (the design lane's seat).
