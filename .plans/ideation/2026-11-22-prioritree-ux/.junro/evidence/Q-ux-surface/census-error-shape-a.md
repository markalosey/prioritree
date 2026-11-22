# CENSUS/ERROR-SHAPE — THE THREEPART GAP MAP (prioritree-ux) — shindan — part a (b: census-error-shape-b.md)

**THE LAW, cited.** R5, ux store (.plans/ideation/2026-11-22-prioritree-ux/.junro/junro.json:167, :275): "THE THREEPART IS MANDATORY IN THIS CODEBASE NOW: every 4xx/5xx response body is a ThreePart error — expected / found / next-action … never a bare status code, never a stack leak, never a silent OK where a refusal belongs" — ground, the collaborator verbatim: "the api absolutely does not follow the errors teach methodology. So, we are going to have to fix that as we go." The core's ruled grammar: Q-granularity R2 (birth store :555) "<2 items REFUSED — the empty list and the single item are named refusals, not special rankings"; the SAFE HALT at Q-problem-space R12 (:547/:669): "the coverage-gate refusal carrying expected/found/next-action naming the isolated items/components and the exact closing pairs."

**THE SERVER.** Exactly one: `src/prioritree/service.py` (the only fastapi import in the tree) — module-level `app` (l.152), five routes, two app-level exception handlers. Zero `HTTPException` raised anywhere in src (grep: no hits) — every refusal is a typed core exception caught BY TYPE and rendered at one point.

## THE GAP MAP — per endpoint, every error path

**POST /runs — register (l.227-253)**
- store refusal → `JSONResponse(status_code=404, content=render_refusal(refusal))` (l.250) — body `{expected, found, next_action}` — compliant
- door's value refusal (<2 items, duplicate ids, quorum<1 — registry.py `_require_quorum` l.285) → `status_code=422, content=render_refusal(refusal)` (l.252) — compliant
- malformed body (items not a list of [id,label] pairs, missing/mistyped operator_id/question/quorum) → the app-level re-badge: `JSONResponse(status_code=400, content={DETAIL: exc.errors()})` (l.195) — body `{"detail": [{loc, msg, type}, …]}`, **no expected/found/next_action** — **string-detail** (R5's letter breached on a 4xx; the in-code defense, l.183-184: "fabricating expected/found/next_action for a schema violation would dress the wrong family")
- any other exception → the 500 fold: `{EXPECTED: "POST /runs", FOUND: "Type: msg", NEXT_ACTION: ESCALATION}` (l.219-223) — compliant; the traceback rides uvicorn's log channel, never the body (tested: test_service_face.py:265 `assert "Traceback" not in response.text`)

**GET /runs/{run_id}/next — serve (l.256-283)**
- unknown run → 404 render_refusal (l.277) — compliant
- door refusal → 422 render_refusal (l.279) — compliant
- DONE: `except ExhaustedQueue as done:` → 200 `{DONE: True, EXPECTED…, FOUND…, NEXT_ACTION…}` (l.280-282) — ruled a STATE, never an error (l.12-13); carries the three fields plus the done marker — honest, not a silent-ok
- `?seed=<non-int>` → the 400 re-badge detail family — **string-detail**
- uncaught → 500 fold — compliant

**POST /runs/{run_id}/votes — cast_vote (l.286-320)**
- 404 (l.316), 422 out-of-set verdict / unknown pair ids (l.318) → render_refusal — compliant
- malformed body (pair not a two-array of strings, missing fields) → 400 re-badge — **string-detail**
- uncaught → 500 fold — compliant
- note: byte-identical re-send → 200 ack `{"vote_id", "count", "acknowledged": False}` (l.319-320) — the ruled loud idempotent ack, a value not a refusal — not a gap
