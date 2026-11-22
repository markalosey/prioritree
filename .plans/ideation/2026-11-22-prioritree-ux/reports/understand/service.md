<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — understand/service

**Route:** prioritree-ux (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T10:03:58Z |
| 2 | report | rikai | 2026-11-22T10:06:39Z |
## Reported by rikai — 2026-11-22T10:06:39Z

# THE SERVICE UNIT'S MECHANISM MAP (understand/service — the seams the unit's mechanisms ride)

READ-BACK (the whole ground): reports/synthesize/ux-design.md §§1-14 · evidence Q-ux-surface: census-mechanism-a.md/-b.md + census-error-shape-a.md/-b.md · src: service_store.py, run_store.py, service.py (whole), registry.py, session.py (cited) · tests: test_service_face.py, test_service_acceptance.py (whole).

## 1. THE SIXTH QUERY
- THE MANIFEST'S JOURNEY: register's session.register_run RETURNS it (run_store.py:552) → the line (kind, run_id, items, operator{id,question,verdicts sorted}, quorum, registered_at — :556-567) written ONCE (:568-571) → at load, line 1 validated field-by-field (:644-653, verdicts :651) → reconstruction mints a FRESH RunManifest at session.register_run (:690 — today DISCARDED as _manifest), frozen into the fresh Registry (registry.py:368) — the object lives in the door's store, readable by the core's OWN read_manifest (registry.py:371, a pure lookup).
- FULL LOAD REQUIRED: Persist has NO manifest-line-only read — every public verb rides load's whole pre-pass (all vote lines validated :659-679; the door rebuilt by re-register + in-order re-casts :684-706). The design wraps the FULL load: the data sits on line 1, but the verb rides the load — a manifest read prices the file's integrity (a corrupt vote line refuses it as StoreRefusedError).
- THE LOCK DISCIPLINE (a read): ONE `with self._lock` acquisition wrapping load + act — the read-locks-too law (service_store.py:11-12; a concurrent read would catch the mid-append tail and fire the crash-tail refusal spuriously, run_store.py:626-634); the lock minted at Serialize.__init__ (:89); routes never touch it (:79-80). The new verb's shape: with lock: return Persist.load(home, run_id).manifest().
- THE RESPONSE SEAM: the route (service.py) builds the body from the seam's return — run_id = the STEM echoed from the path param (the wire's id law); question / verdicts-sorted / quorum / items from the manifest (payload order preserved); operator.id + registered_at ELIDED. The stem↔handle map: load builds the file path FROM the stem (:610); the container carries the IN-FILE run_id as the door's handle (:706, the accepted oddity :536-539); the handle never crosses back to the wire.

## 2. THE THREEPART CURES
- THE 400 FAMILY (×3 — register body, serve's seed, cast body): ONE app-level handler (service.py:174-195). At the handler: exc.errors() = a list of {loc, msg, type} dicts — loc names body|query + the field. The cure constructs: expected = the legal body form named from the route's schema (register: items/operator_id/question/quorum :113-116; serve: seed int|None :257; cast: pair/winner/comparator_id/comparator_class/notes/supersedes :138-143), found = the violation detail AS CARRIED, next_action = the named cure. The in-code defense (:183-184) is amended by R5's cure map.
- THE 404/405 DEFAULTS: no StarletteHTTPException handler registered today (only :174 RequestValidationError + :198 Exception) — the framework defaults ride bare: unmatched path → {"detail": "Not Found"}, disallowed method → {"detail": "Method Not Allowed"}. The cure: a StarletteHTTPException handler at the same app-level registration surface; it receives (request, exc) with exc.status_code + exc.detail — expected = the route/method as addressed, found = the unmatched path / disallowed method, next_action = the legal route/method set.

## 3. THE CORE BOUNDARY (zero core edits — held)
- The sixth query rides STORE tier (the Persist.manifest accessor, run_store.py) + LOCK SEAM (the Serialize.manifest verb, service_store.py) + FACE (the GET route + body construction, service.py). The core (registry/scheduler/votes/tally/session) untouched — read_manifest already exists (registry.py:371); the five-op interface stands; session._read_manifest (:140) stays private.
- The cures ride the FACE alone: the two handler bodies in service.py. The typed refusals ride through BY TYPE untouched — the routes' catch tables and render_refusal (:156-171) stand; DONE and the idempotent ack stay values.

## 4. THE TEST SEAM
- FACE (test_service_face.py): the fixture injects Serialize(tmp_path) — app.state.seam overwritten per test (:44-61). The refusal pattern: status first, then set(body) == _REFUSAL_KEYS = {"expected","found","next_action"} (:149), then a substring pin ("RUN-9999" in found :159; "at quorum" in expected :196). Success = exact-dict body equality (:109, :127-139). The sixth query's tests extend: the exact 200 body + the 404 unknown-stem arc. The cured-400 test flips from the native grammar (:204-206 — "detail" a non-empty list) to the family set; the cured 404/405 extend the set + substring pattern (the path/method named in found).
- ACCEPTANCE (test_service_acceptance.py): Popen of the fixed argv [uvicorn, prioritree.service:app, --host 127.0.0.1, --port 0, --no-access-log] (:39-48), cwd=home (STORE_HOME CWD-relative — the Popen cwd IS the isolation, :145-147), the banner regex parses the kernel port (:52, :65-100), the 404 probe = ready (:103-135), teardown terminate→wait(5)→kill (:165-171); assertions: exact-literal bodies (:201-245), the replay's byte-identical .content lists (:248-291), the refusals' family grammar through the socket (:299-345), the file's direct read (Persist.load) as the oracle (:407-416).
