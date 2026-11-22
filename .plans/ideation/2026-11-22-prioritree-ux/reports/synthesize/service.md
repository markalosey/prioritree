<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/service

**Route:** prioritree-ux (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T10:08:06Z |
| 2 | report | togo | 2026-11-22T10:12:09Z |
## Reported by togo — 2026-11-22T10:12:09Z

# THE SERVICE UNIT BRIEF (synthesize/service — the unit-level build spec; togo, 2026-11-22)

THE GROUND, READ + CITED: reports/discover/service.md (tansa — the touch inventory, the models verbatim, the test surface, the cure points, the insertion seams, the floor) · reports/understand/service.md (rikai — the sixth query's mechanism, the cures' mechanisms, the core boundary, the test seam's exact patterns) · reports/synthesize/ux-design.md (the approved design — §1's freeze consequence, §2 the sixth query, §10 the cure map, §12 the unit's handoffs) · the ux store's junro.json (G-SERVICE-BRIEF's three conditions; G-SERVICE's four conditions; Q-ux-surface R1-R6). READ-ONLY held — nothing written beyond this report.

THE UNIT IN ONE LINE: the service surface grows ONE query (GET /runs/{run_id}/manifest) and cures FIVE error bodies (×3 the 400 re-badge + ×2 the framework-default 404/405) — the five routes' success shapes FROZEN byte-stable, the core untouched.

## §0 THE TRADE-OFF THE PLAN CARRIES (named, per the seat's law)

The sixth query rides the FULL load: Persist has no manifest-line-only read — every public verb rides load's whole pre-pass (line 1's manifest validated, every vote line validated, the door rebuilt). A manifest read therefore prices the file's WHOLE integrity (a corrupt vote line refuses it as StoreRefusedError) and takes the lock even as a read (the read-locks-too law — a concurrent read never sees the mid-append tail; a bare read would fire the crash-tail refusal spuriously). THE ALTERNATIVE — a line-1-only read — would be cheaper and would skip both the integrity check and the consistency guarantee: REFUSED. The price is O(votes) per manifest read + the lock held across it — negligible at the single-operator local tool's file sizes, and IDENTICAL to what /next, /state, /tally already pay: the verb family stays consistent. SECOND PRICE, named: the 400 body flip breaks FastAPI's native "detail" grammar for any client parsing it — the census found none beyond the pinned tests (which flip in the same build); the web unit's client lands after, reading only the cured grammar. Both prices accepted.

## §1 THE SCOPE FENCE

LANDS (the whole of the unit's writes):
- src/prioritree/service.py: (a) THE SIXTH ROUTE — GET /runs/{run_id}/manifest, route + response-body construction (placement: the file tail after rank, l.393+; the path constant's home per the constants idiom — the l.85-88 block or the mid-file _TALLY_PATH precedent l.224 — §7 settles the exact home); (b) THE 400 RE-BADGE FLIP — the handler body at l.174-195 (ONE handler cures the ×3 family); (c) THE NEW app-level StarletteHTTPException handler — the ×2 cure, registered at the same app-level surface (the l.174/l.198 neighborhood).
- src/prioritree/service_store.py: Serialize.manifest — the new seam verb at the verb table's tail (after rank l.192-209): ONE `with self._lock` acquisition wrapping Persist.load(...).manifest() (the read-locks-too law, service_store.py:11-12's own rationale; routes never touch the lock).
- src/prioritree/run_store.py: Persist.manifest — the store-tier accessor at the verb tail (after rank l.852-866, alongside the run_id property l.868-882), returning the FRESH RunManifest load's reconstruction already mints (session.register_run, l.690 — discarded today as _manifest).
- tests/test_service_face.py + tests/test_service_acceptance.py: the new arcs + the assertion flips (§5).

DOES NOT TOUCH (the fence's other side):
- THE CORE — zero edits: registry.py / scheduler / votes / tally / session.py untouched. The core's read_manifest already exists (registry.py:371, U1's own op); session._read_manifest (session.py:140) stays private; the five-op interface (Q-solution-space's frozen ruling) stands; RegisterRunRequest UNCHANGED (the verdict-set field dropped — design §3).
- THE FIVE ROUTES' SHAPES — frozen byte-stable (the pinned success bodies untouched); the typed-refusal catch tables (404/422/409/500) stand; render_refusal (l.156-171) stands; DONE + the idempotent ack stay VALUES (R5's own carve-out, design §10).
- THE WEB TIER — no HTML, no templates, no HX-Request branch, no Jinja2, no mount line (the mount is the WEB unit's ONE service.py touch, landed by it); no dependencies added (jinja2/httpx ride the web unit's brief).
- THE LIFECYCLE — no Makefile service targets (the lifecycle unit's brief); no uvicorn policy in src (service.py:25/:147 held).
- THE CLI; the floor config (pyproject/Makefile) unchanged — the floor held: pyright strict, ruff ALL with the standing per-file rulings (service.py BLE001 l.105).

## §2 THE SIX LANES (the route table; 2 commands / 4 queries — design §9, R2 cited)

| # | Route | Lane | Op | Success form | Refusal forms |
|---|-------|------|----|--------------|---------------|
| 1 | POST /runs | COMMAND | register_run | 201 {"run_id"} | 422 typed (the door's own) · 400 CURED · 500 fold |
| 2 | POST /runs/{run_id}/votes | COMMAND | cast_vote | 200 {"vote_id","count","acknowledged"} | 404/422/409 typed · 400 CURED · 500 fold |
| 3 | GET /runs/{run_id}/next?seed= | QUERY | next_pair | 200 the bare pair / DONE 200 (a VALUE) | 404 typed · 400 CURED (the seed) · 500 fold |
| 4 | GET /runs/{run_id}/state | QUERY | read_vote_state | 200 {"total","items"} (never refuses on coverage) | 404 typed · 500 fold |
| 5 | GET /runs/{run_id}/tally | QUERY | tally_rank | 200 the asdict whole (pair_counts re-keyed "item_a|item_b") | 409 SAFE HALT typed · 404 typed · 500 fold |
| 6 | GET /runs/{run_id}/manifest | QUERY — THE SIXTH | the manifest read (store-tier; NOT one of the five ops — the interface untouched) | 200 the manifest body (below) | 404 the unknown stem · 500 fold · 422 NEVER |

THE SIXTH QUERY'S EXACT SPEC (G-SERVICE-BRIEF's condition 2, answered):
- THE 200 BODY: {"run_id": <the STEM echoed from the path param>, "question": <the stated question>, "verdicts": <the declared set as a sorted array>, "quorum": <the declared policy-as-data>, "items": [[id, label], ...] — payload order preserved}. FIVE keys. ELISIONS: operator.id + registered_at NEVER on the wire (the census's discipline — the query returns what the front end renders; the register ack holds the operator id from its own posted body).
- THE MECHANISM (per rikai, verified at HEAD): the route composes Serialize.manifest(run_id) → ONE lock acquisition wrapping Persist.load(home, run_id).manifest(). The load is the FULL pre-pass (line 1's manifest validated l.644-653, verdicts l.651; every vote line l.659-679; the door rebuilt by re-register + in-order re-casts l.684-706); the reconstruction mints a FRESH RunManifest at session.register_run (l.690, discarded today) → Persist.manifest returns it. The stem↔handle map held: load builds the file path FROM the stem (l.610); the in-file run_id never crosses back to the wire (l.706; l.536-539 the accepted oddity).
- THE ERROR PATHS: 404 the unknown stem (StoreRefusedError, both families — the honest label; the sibling reads' own catch table), 500 the fold. ZERO CORE EDITS (design §2's ruling; divergence ledger #1 answered).

## §3 THE THREEPART CURE MAP (R5 as-we-go; 21/21 after = 16 compliant + 5 cured — design §10)

THE LAW (R5): every 4xx/5xx body carries expected / found / next_action — never a bare status, never a stack leak, never a silent OK where a refusal belongs. THE STATUSES ARE FROZEN: the cure flips BODIES only — the codes (400/404/405) stay pinned (machine-dispatchable; the acceptance harness's 404-as-ready probe rides the status, untouched).

CURE 1 — the 400 re-badge family (×3: register body, serve's seed, cast body — all funnel to l.195's JSONResponse({DETAIL: exc.errors()}), the native grammar):
- THE MECHANISM (per rikai's verification): ONE app-level handler (l.174-195). At the handler, exc.errors() = a list of {loc, msg, type} dicts — loc names body|query + the field.
- THE FIELDS CONSTRUCTED: expected = the legal body form named from the route's schema (register: items/operator_id/question/quorum, l.113-116; serve: seed int|None, l.257; cast: pair/winner/comparator_id/comparator_class/notes/supersedes, l.138-143) · found = the violation detail AS CARRIED · next_action = the named cure. The in-code defense (l.183-184) is amended by this map.
- THE TOUCHED NEIGHBORHOOD (per tansa): the handler body l.183-195; the DETAIL body-key constant (the l.64-76 block) retires or repurposes — §7 settles.
- THE TEST FLIP: test_rebadge_malformed_body_400's native-grammar assertions ("detail" a non-empty list, l.204-206) flip to the family set + substring pins — the 400 now TEACHES.

CURE 2 — the framework-default 404/405 (×2: unmatched path → bare {"detail": "Not Found"}; disallowed method → bare {"detail": "Method Not Allowed"}):
- THE MECHANISM: ZERO StarletteHTTPException handlers in src today (tansa: exactly two handlers — l.174 RequestValidationError + l.198 Exception; zero grep hits). THE CURE: an app-level StarletteHTTPException handler at the same registration surface; it receives (request, exc) with exc.status_code + exc.detail.
- THE FIELDS CONSTRUCTED: expected = the route/method as addressed · found = the unmatched path / the disallowed method · next_action = the legal route/method set.
- THE TEST ARCS (new): the unmatched-path 404 + the disallowed-method 405 — the family set + the path/method named in found.
- NOTE: the typed refusals ride through BY TYPE untouched — the routes' catch tables stand; the app-level handler never sees them (the routes catch typed refusals first).

AFTER THE CURE: 21/21 error paths ThreePart (16 compliant, untouched + 5 cured). DONE and the idempotent ack stay VALUES.

## §4 THE RETURN FORMS (every body the unit serves after the build — success + refusal)

THE FROZEN FIVE (byte-stable; pinned at test_service_face.py l.64-139 + test_service_acceptance.py l.201-291):
1. POST /runs → 201 {"run_id": "<RUN-####>"} — one key alone (operator id, question, verdicts, quorum all elided from the ack).
2. GET .../next → 200 {"item_a": "<id>", "item_b": "<id>", "count": <int>} — ids, never labels; OR DONE → 200 {"done": true, "expected": ..., "found": ..., "next_action": ...} — a VALUE carrying the family-shaped fields (the pins: the done marker + three fields + "tally" in next_action).
3. POST .../votes → 200 {"vote_id": "<id>", "count": <int>, "acknowledged": <bool>} — the VoteRecord elided; acknowledged:false = the loud idempotent echo.
4. GET .../state → 200 {"total": <int>, "items": {"<id>": <int>, ...}} — per_pair_counts elided at the seam, never resurrected.
5. GET .../tally → 200 the asdict whole — pair_counts re-keyed "item_a|item_b" (l.387-393).

THE SIXTH (new):
6. GET .../manifest → 200 {"run_id": "<stem>", "question": "<the stated question>", "verdicts": ["prefer-a","prefer-b","tie"] (the declared set, sorted), "quorum": <int>, "items": [["<id>","<label>"], ...] (payload order preserved)} — FIVE keys; operator.id + registered_at NEVER present.

THE TYPED REFUSALS (frozen, the family grammar): 404 unknown run — {"expected","found","next_action"}, the run id named in found ("RUN-9999" pinned); 422 out-of-set verdict — the family set, the bogus winner in found; 409 SAFE HALT — the family set, "at quorum" in expected, the isolated items/components + exact closing pairs named; 500 the fold — {"expected": "<method> <path>", "found": "<Type>: <msg>", "next_action": ESCALATION}, never a Traceback.

THE CURED FAMILIES (bodies flipped; statuses pinned):
- 400 (×3) → {"expected": "<the legal body form named from the route's schema>", "found": "<the violation as carried>", "next_action": "<the named cure>"}.
- 404 (unmatched path) → {"expected": "<the route as addressed>", "found": "<the unmatched path>", "next_action": "<the legal route set>"}.
- 405 (disallowed method) → {"expected": "<the method as addressed>", "found": "<the disallowed method>", "next_action": "<the legal method set>"}.

## §5 THE TEST PLAN'S SHAPE (the patterns per the discovery)

FACE — tests/test_service_face.py (the fixture injects Serialize(tmp_path), app.state.seam overwritten per test l.44-61):
- test_manifest_200 (NEW): extends the exact-dict body-equality pattern (l.109, l.127-139) — the five keys asserted exact; verdicts the sorted triple; items payload-order-preserved; the elisions pinned by the key set (no operator/registered_at keys).
- test_refusal_manifest_unknown_run (NEW): extends the refusal pattern (l.149, l.153-159) — status first, set(body) == _REFUSAL_KEYS, the stem pinned in found.
- test_rebadge_malformed_body_400 (FLIPS, l.199): the native-grammar assertions flip to the family set + substring pins (§3's flip).
- test_rebadge_door_refusal_422 (STANDS, l.209): the two grammars still never conflated — 422 ≠ 400, now BOTH families (the separation claim strengthens).
- test_refusal_unmatched_path_404 (NEW): the family set + the path named in found — the framework default cured.
- test_refusal_method_not_allowed_405 (NEW): the family set + the method named in found.
- UNTOUCHED: the five pinned success tests (l.64-139), test_refusal_unknown_run / _out_of_set_verdict / _safe_halt, test_done_200, test_crash_envelope_500 — the freeze's pins.

ACCEPTANCE — tests/test_service_acceptance.py (the live boot: fixed-argv Popen [uvicorn, prioritree.service:app, --host 127.0.0.1, --port 0, --no-access-log] l.39-48, cwd=home — the Popen cwd IS the isolation, l.145-147; the 404-as-ready probe l.103-135; teardown terminate→wait(5)→kill l.165-171):
- THE NEW ARC: the seven-request arc (l.201) grows the manifest GET — the EIGHTH request, exact-literal body over the socket (the l.201-245 pattern); the manifest read rides the live seam (lock + full load under the real process). RECOMMENDATION: grow the arc (the same boot lifecycle; the manifest slots after register) — the exact name/literals §7 settles.
- test_refuse_the_four_arcs (l.299): the 404/400 arcs' BODY assertions flip to the family grammar through the socket; 422/409 untouched.
- THE READY PROBE: rides the 404 STATUS — the cure flipped its body, not its status; the probe untouched.
- UNTOUCHED: test_replay_byte_identical (l.248), test_interleave_the_concurrency_arc (l.348) + the Persist.load file oracle (l.407-416).

## §6 THE ACCEPTANCE MAPPING (G-SERVICE's four conditions → this brief's clauses)

1. "the service surface lands per its approved brief — the exact-task law" → §1 the fence + §7 the handoff: the probe lane's exact-task spec carries the bytes (FR-MEM-0011's doctrine — nothing to figure out at the execution seat); the build dispatches cite this brief + that spec; the build lands EXACTLY what they name, nothing more.
2. "the CQRS segregation green: commands segregated from queries at the service surface over the five ops (R2); the core's ruled refusals + the DONE signal carried at the API by type, in the family grammar" → §2 the six lanes (2 commands / 4 queries, R2 cited) + §3's typed-untouched clause (the catch tables stand; DONE a 200 VALUE) + §4's forms.
3. "the ThreePart compliance green on every touched surface (R5, as-we-go): every 4xx/5xx body carries expected/found/next-action — never a bare status, never a stack leak, never a silent OK; the census's error-shape map cured" → §3 the cure map (21/21 after: 16 + 5) + §4 (every 4xx/5xx body the family grammar after the build).
4. "pyright 0 errors 0 warnings + ruff zero findings, zero ignores; kensho's independent re-run green (validate/service)" → the floor whole held (tansa's §6: pyright strict, ruff ALL, the zero-findings bar; a lint/type ignore is a ruling, never a convenience) + kensho's INDEPENDENT verification leg at G-SERVICE — never the builder's own claim.

THE GATE THIS BRIEF CLOSES (G-SERVICE-BRIEF's own three conditions, answered): (1) the brief landed, carrying the CQRS lanes per the op-mapping + the touched surfaces' ThreePart plan (R5) + the scope fence + the return forms — §§1-4, over discover/service + understand/service + the approved design + the census; (2) the sixth query's exact spec (GET /runs/{run_id}/manifest via Serialize.manifest + Persist.manifest, zero core edits — the reconciliation's answer to the manifest gap, divergence ledger #1) — §2; (3) the ThreePart cure map (×3 the 400 re-badge → the schema-violation ThreePart form; ×2 the framework-default 404/405 → the app-level StarletteHTTPException handler — 21/21 after, per the approved design) — §3. THE COLLABORATOR'S APPROVAL IS THE GATE — the dispatches fire only after (the precedence law).

## §7 THE HANDOFF (what synthesize/probe → G-PROBE-BRIEF receives)

SETTLED HERE (the probe inherits, never re-opens): the six lanes + every return form (§§2, 4); the one-handler-per-family cure shape + the frozen statuses (§3); the full-load + one-lock mechanism; the stem echo + the elisions; the test arcs' names + patterns (§5); the zero-core-edits fence (§1).

THE OPEN QUESTIONS (the named bytes the probe must settle):
(a) THE 400 HANDLER'S EXACT CONSTRUCTION: one handler serves three sources — the exact expected strings per route (the legal body forms' phrasing from l.113-116 / l.257 / l.138-143); how the handler identifies the source (request.url.path branch vs loc-derived); found's exact rendering of exc.errors()' {loc, msg, type} dicts (as-carried — stringified? joined?); next_action's per-route cure wording.
(b) THE 404/405 HANDLER'S EXACT CONSTRUCTION: the handler receives ANY StarletteHTTPException — general ThreePart (fields from exc.status_code + exc.detail) vs 404/405-specific construction; next_action's legal-set wording (the route/method set enumerated or summarized); the registration order + position in service.py.
(c) THE ROUTE PLACEMENT + THE CONSTANTS' HOMES: the sixth route after rank (l.393+, the file tail — REST-parallel to /state l.323 and /tally l.357); the path constant's home (the l.85-88 block vs the mid-file _TALLY_PATH idiom l.224); the new body keys' constants vs literals (the l.64-76 idiom); the DETAIL constant's retirement.
(d) THE SIGNATURES: Serialize.manifest's exact signature (the verb table's own form, l.92-209); Persist.manifest's exact placement (the verb tail after rank l.852-866 vs alongside the run_id property l.868-882) + return type (the RunManifest whole — elision at the route — vs a projected form at the seam).
(e) THE TEST LITERALS: the exact expected/found/next_action substrings every new/flipped test pins; the manifest-200 fixture's literal body; the acceptance harness's eighth-request literal + the arc's final name; the final test names (the file's idiom held, the naming law checked).

THE BRIEF CLOSES: the unit's shape is whole — the fence, the lanes, the cures, the forms, the tests, the acceptance mapping, the handoff. Every open question is named for the probe lane; nothing rides silently. — togo, 2026-11-22
