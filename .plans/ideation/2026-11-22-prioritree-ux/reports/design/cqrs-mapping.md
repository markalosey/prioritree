<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — design/cqrs-mapping

**Route:** prioritree-ux (executing) | **Events:** 3 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T09:29:10Z |
| 2 | dispatch | shinko | 2026-11-22T09:36:29Z |
| 3 | report | keisan | 2026-11-22T09:37:22Z |
## Reported by keisan — 2026-11-22T09:37:22Z

# keisan (計算) — packet design/cqrs-mapping — THE CQRS OP-MAPPING — READ-ONLY

Ground cited: R2 the CQRS agenda + R5 the ThreePart mandatory (Q-ux-surface rulings, ux store) · census-mechanism-a.md + census-mechanism-b.md + census-error-shape-a.md + census-error-shape-b.md (.junro/evidence/Q-ux-surface/).

## 1. The op lanes — 2 commands / 3 queries
- COMMAND register_run — mutates: mints the run's file (the manifest line; reconstructed at load).
- QUERY next_pair — pure scheduler read (deterministic enumeration + seed); appends nothing; the bare pair, no scores.
- COMMAND cast_vote — the wire's one durable act (save-at-cast, one line + flush per write).
- QUERY read_vote_state — pure read; never refuses on coverage.
- QUERY tally_rank — the write-target-NOTHING law: rank appends nothing — a locked read; the SAFE HALT refuses to emit, never writes.
The segregation lives at the SERVICE SURFACE (verb/path/response/error contract per lane), not the store: one JSONL store + per-request reconstruction serves both lanes; one render point (render_refusal) serves both lanes' refusals.

## 2. The service surface — current routes 1:1 — CONFIRMED, no amendment
Commands on POST: register_run → POST /runs (:227); cast_vote → POST /runs/{run_id}/votes (:286).
Queries on GET: next_pair → GET /runs/{run_id}/next?seed= (:256); read_vote_state → GET /runs/{run_id}/state (:323); tally_rank → GET /runs/{run_id}/tally (:357).
HTMX wire: hx-post on the commands, hx-get on the queries. HTMX swaps nothing on non-2xx by default — the error-swap rule composes in the web unit's brief, not this mapping.

## 3. The response forms — the census's elisions, ruled
- register: 201 {"run_id": stem} ALONE — sufficient: the front end holds what it just posted, the count arrives on the first next_pair; manifest + count stay elided.
- next: 200 the bare pair {"item_a","item_b","count"} — exactly what the comparison surface renders.
- cast: 200 {"vote_id","count","acknowledged"} — VoteRecord stays elided (durable only in the file); byte-identical re-send → acknowledged:false, the ruled loud idempotent ack — a value, not a refusal.
- state: 200 {"total","items"} — the query returns what the front end renders; vote_log ("rendering lies") + per_pair_counts stay elided.
- tally: 200 asdict-whole with pair_counts re-keyed "item_a|item_b" — the one priced reconciliation (JSON keys must be strings), confirmed.
- THE DONE SIGNAL — query lane (GET /next): 200 {"done": true, + expected/found/next_action} — a VALUE, a state, never an error; the front end swaps to the completion view off it.
- THE SAFE HALT — query lane (GET /tally): 409 {expected, found, next_action} — R12's grammar verbatim ("at quorum" in expected; found names the isolated items/components; next-action names the exact closing pairs).

## 4. The ThreePart error contract + the cure map (R5 as-we-go — the service unit's brief; 16/21 compliant today)
- ×3 the 400 re-badge family (register body, serve's seed, cast body): {"detail":[…]}, no three fields → CURE: the ThreePart schema-violation form — expected = the legal body form named from the route's schema; found = the violation detail as carried; next-action = the named cure. Fields CONSTRUCTED from schema + violation, not fabricated — the violation detail IS the found (the honest answer to the in-code defense).
- ×2 the framework-default 404/405 (no StarletteHTTPException handler registered) → CURE: the app-level StarletteHTTPException handler — expected = the route/method as addressed; found = the unmatched path / disallowed method; next-action = the legal route/method set.
- After cure: 21/21 error paths ThreePart (16 compliant + 5 cured). DONE and the idempotent ack stay values, untouched by R5.

## 5. The two id spaces — the ruling
The WIRE carries the FILE STEM — confirmed as the mapping's law: every {run_id} path parameter is the stem; clients address runs by stem; no new id minted, no convergence attempted. The IN-FILE HANDLE: status NAMED, never crossing — the file-internal provenance stamp (RUN-0007.jsonl's lines may say RUN-0001); the built-in read-back never crosses the wire; the front end never sees, mints, or renders it.

## Read-back (files actually read)
.plans/ideation/2026-11-22-prioritree-ux/.junro/junro.json (query status; Q-ux-surface rulings R1-R5) · census-mechanism-a.md (whole, 25 l.) · census-mechanism-b.md (whole, 18 l.) · census-error-shape-a.md (whole, 26 l.) · census-error-shape-b.md (whole, 27 l.) — all under .junro/evidence/Q-ux-surface/. READ-ONLY — nothing written to disk beyond this report.
