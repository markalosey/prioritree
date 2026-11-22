# CENSUS/ERROR-SHAPE — part b (the state/tally routes; the surface-wide paths; the seam; the honest condition; the count; the read-back)

**GET /runs/{run_id}/state — census (l.323-347)**
- 404 (l.343), 422 (l.345) → render_refusal — compliant
- no validatable params (`run_id: str` — any string passes the door; the unknown run refuses at 404) — no 400 path fireable
- uncaught → 500 fold — compliant; **gaps on this route: none**

**GET /runs/{run_id}/tally — rank (l.357-393)**
- 404 (l.382), 422 (l.384) → render_refusal — compliant
- SAFE HALT: `except TallyRefusedError … return JSONResponse(status_code=409, content=render_refusal(refusal))` (l.385-386) — R12's grammar at the wire, verbatim fields ("at quorum" asserted in expected, test:196) — compliant
- uncaught → 500 fold — compliant

**SURFACE-WIDE — no route matches.** No `StarletteHTTPException` handler is registered (only `RequestValidationError` l.174 and `Exception` l.198), so the framework defaults ride bare:
- unmatched path → FastAPI default 404 body `{"detail": "Not Found"}` — **string-detail**
- wrong method on a matched path → 405 `{"detail": "Method Not Allowed"}` — **string-detail**

**THE SEAM (ask 4) — the core's refusal grammar: carried WHOLE**
All four typed signals construct the three fields as data attributes: `StoreRefusedError` (run_store.py:79-91), `VotesRefusedError` (votes.py:122-134), `ExhaustedQueue` (session.py:78-92, "exhausted —" prefix), `TallyRefusedError` (tally.py:130-142). The seam rides them "verbatim BY TYPE, never wrapped, never conflated" (service_store.py:57-59); the registry's own refusals wrap into `VotesRefusedError` at the session surface with the fields carried (session.py:105-107). At the routes, ONE render point reads attributes as data — `return {EXPECTED: refusal.expected, FOUND: refusal.found, NEXT_ACTION: refusal.next_action}` (service.py:171) — never `str(e)` reparsed. **Carried whole: no flattening, no dropping, no swallowed excepts; no ruled refusal type escapes the catch tables** (anything else is a genuine crash → the 500 fold, itself ThreePart).

**THE HONEST CONDITION**
R5's premise and the tree diverge: the service face (landed in the core effort — its provenance cites Q-service-routes/Q-error-teaching, service.py:2-39) **already renders ThreePart on every path its own routes catch** — 404/422/409/500 all carry the three fields, no stack leak, DONE honest at 200. The non-ThreePart residue on the wire is exactly two families: (a) the 400 re-badge's native detail grammar — `{"detail": [...]}`, no three fields — fireable on register, serve's seed, cast_vote; (b) the unhandled framework-default 404/405 — `{"detail": "Not Found"}`. No bare-status, no default-422 (re-badged away), no stack-leak, no silent-ok, no absent path found. The premise matches the residue, not the whole — that is the state.

**count: endpoints: 5, error paths: 21 (incl. 2 framework-default surface paths), ThreePart-compliant today: 16 — the 5 gaps all class string-detail: ×3 the 400 re-badge family, ×2 the framework-default 404/405.**

**READ-BACK (files actually read):** src/prioritree/service.py (whole, 393 l.) · src/prioritree/service_store.py (whole, 209 l.) · src/prioritree/run_store.py (l.55-124) · src/prioritree/votes.py (l.95-164) · src/prioritree/session.py (l.40-114) · src/prioritree/tally.py (l.108-182) · src/prioritree/registry.py `_require_quorum` (l.274-294, via search) · tests/test_service_face.py (whole, 265 l.) · tests/test_service_acceptance.py (uvicorn arcs, via search) · .plans/ideation/2026-11-22-prioritree-ux/.junro/junro.json (R5:167/:275) · .plans/ideation/2026-11-19-prioritree-birth/.junro/junro.json (Q-granularity R2:555, Q-problem-space R12:547/:669, Q-solution-space ground:466).

No fixes proposed — the remediation rides the briefs (R5's as-we-go map), not this diagnosis.
