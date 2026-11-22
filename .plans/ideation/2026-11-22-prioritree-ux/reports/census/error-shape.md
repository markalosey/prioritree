<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/error-shape

**Route:** prioritree-ux (executing) | **Events:** 5 | **Reports:** 2

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T09:20:18Z |
| 2 | result | shinko | 2026-11-22T09:28:39Z |
| 3 | report | shinko | 2026-11-22T09:28:46Z |
| 4 | dispatch | shinko | 2026-11-22T09:36:17Z |
| 5 | report | shindan | 2026-11-22T09:37:17Z |
## Reported by shinko — 2026-11-22T09:28:46Z

shindan's completion report (packet census/error-shape, recorded by shinko):

THE THREEPART GAP MAP LANDED — every route read whole, every refusal traced raise-to-wire. THE EVIDENCE SET: .junro/evidence/Q-ux-surface/census-error-shape-a.md + census-error-shape-b.md (the return verbatim in two regions).

THE HONEST CONDITION (the load-bearing finding): R5's premise and the tree DIVERGE — the service face already renders ThreePart on every path its own routes catch (the core effort's landed discipline: one render point, typed exceptions, never str(e) reparsed; the core's refusal grammar carried WHOLE across the seam). THE COUNT: 5 endpoints, 21 error paths, 16 ThreePart-compliant today. THE RESIDUE — exactly 5 gaps, all class string-detail: ×3 the 400 re-badge family (native {"detail": [...]} on register/serve-seed/cast_vote — deliberate per the in-code defense "fabricating expected/found/next_action for a schema violation would dress the wrong family" — R5's letter still breaches: every 4xx body is a ThreePart error now) + ×2 the framework-default 404/405 (no StarletteHTTPException handler registered — unmatched path, wrong method). No bare-status, no default-422 (re-badged away), no stack-leak, no silent-ok, no absent paths. DONE stays honest at 200 (a state, not an error); the byte-identical re-send's loud idempotent ack is a value, not a gap.

THE AS-WE-GO MAP rides the service unit's brief: the re-badge family's ThreePart form (the schema-violation family named honestly within the three fields) + the app-level StarletteHTTPException handler. No fixes proposed at this seat — the remediation rides the briefs (R5).
## Reported by shindan — 2026-11-22T09:37:17Z

shindan's completion report — census/error-shape (prioritree-ux): THE THREEPART GAP MAP.

THE LAW (cited): R5, Q-ux-surface ruling 5 (ux store) — every 4xx/5xx body carries expected/found/next-action, never a bare status, never a stack leak, never a silent OK where a refusal belongs; ground, the collaborator verbatim: "the api absolutely does not follow the errors teach methodology. So, we are going to have to fix that as we go." The core's own ruled grammar: Q-granularity R2 (named refusals naming the legal set), Q-problem-space R12's SAFE HALT (expected/found/next-action naming the isolated items/components and the exact closing pairs).

THE SERVER: exactly one — src/prioritree/service.py (the only fastapi import in the tree); five routes; zero HTTPException anywhere in src; two app-level exception handlers (the 400 re-badge; the 500 fold).

THE GAP MAP (21 error paths over 5 endpoints):
- POST /runs — 404 render_refusal (compliant) · 422 render_refusal (compliant) · malformed body => 400 {"detail": [...]} — string-detail · uncaught => 500 three-part fold (compliant).
- GET /runs/{run_id}/next — 404/422 render_refusal (compliant) · DONE => 200 {done: true, expected, found, next_action} — a ruled STATE, honest, not a silent-ok · ?seed=<non-int> => 400 detail family — string-detail · 500 fold (compliant).
- POST /runs/{run_id}/votes — 404/422 render_refusal (compliant) · malformed body => 400 detail family — string-detail · 500 fold (compliant) · byte-identical re-send => 200 loud ack (a value, not a gap).
- GET /runs/{run_id}/state — 404/422 render_refusal (compliant) · 500 fold (compliant) — no gaps on this route.
- GET /runs/{run_id}/tally — 404/422 render_refusal (compliant) · SAFE HALT => 409 render_refusal, R12's grammar at the wire (compliant) · 500 fold (compliant).
- SURFACE-WIDE — no handler for Starlette's default 404/405: {"detail": "Not Found"} / {"detail": "Method Not Allowed"} — string-detail, ×2.

THE SEAM: the core's refusal grammar is carried WHOLE. All four typed signals (StoreRefusedError, VotesRefusedError, ExhaustedQueue, TallyRefusedError) construct expected/found/next_action as data attributes; the seam rides them through BY TYPE, never wrapped, never conflated; one render point reads them as data, never str(e) reparsed; no ruled refusal type escapes the catch tables — anything else is a genuine crash into the three-part 500 fold. No flattening, no dropping, no swallowed excepts.

THE HONEST CONDITION: R5's premise and the tree diverge — the service face already renders ThreePart on every path its own routes catch (404/422/409/500 all carry the three fields; no stack leak; DONE honest at 200). The residue is exactly two families: the 400 re-badge's native detail grammar (fireable on register, serve's seed, cast) and the framework-default 404/405. No bare-status, no default-422, no stack-leak, no silent-ok, no absent path found. The premise matches the residue, not the whole — that is the state.

COUNT: endpoints: 5, error paths: 21 (incl. 2 framework-default surface paths), ThreePart-compliant today: 16 — the 5 gaps all string-detail: ×3 the 400 re-badge family, ×2 the framework-default 404/405.

READ-BACK (files actually read): src/prioritree/service.py (whole) · src/prioritree/service_store.py (whole) · run_store.py:55-124 · votes.py:95-164 · session.py:40-114 · tally.py:108-182 · registry.py _require_quorum:274-294 (via search) · tests/test_service_face.py (whole) · tests/test_service_acceptance.py (uvicorn arcs, via search) · the ux store's junro.json (R5 at :167/:275) · the birth store's junro.json (Q-granularity R2 at :555, Q-problem-space R12 at :547/:669, Q-solution-space at :466).

NO fixes proposed — the remediation rides the briefs (R5's as-we-go map), not this diagnosis.
