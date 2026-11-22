<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — validate/probe

**Route:** prioritree-ux (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T15:09:00Z |
| 2 | report | kensho | 2026-11-22T15:12:10Z |
## Reported by kensho — 2026-11-22T15:12:10Z

# THE VERIFICATION REPORT — validate/probe (kensho, 2026-11-22)

THE GROUND, READ + CITED (my own reads, zero trust in the build seat's claims): reports/synthesize/probe.md (the approved exact-task spec, §§0-6) · reports/synthesize/service.md (the unit brief) · the ux store's junro.json (G-SERVICE's four conditions) · the five landed files at HEAD 76476cf (service.py, service_store.py, run_store.py, test_service_face.py, test_service_acceptance.py — read whole, every fenced region compared to the spec) · reports/build/probe.md (jikko's claims, re-verified) · pyproject.toml (the standing rulings) · the installed starlette's exceptions.py (deviation 2's ground, read directly).

THE FLOOR, MY OWN RUNS (verbatim): make test — "135 passed in 25.49s" (0 failed, 0 errors); make lint — "All checks passed!"; make typecheck — "0 errors, 0 warnings, 0 informations". The standing rulings only — nothing added for the new code; pyright's no-suppression twins (enableTypeIgnoreComments=false, reportUnnecessaryTypeIgnoreComment=error) hold.

THE SIXTH QUERY, LIVE (my own run — the acceptance harness's fixed-argv boot: uvicorn prioritree.service:app, 127.0.0.1, --port 0, --no-access-log, scratch cwd; teardown terminate+wait): tests/test_service_acceptance.py "4 passed in 2.12s" — register (POST /runs, the 3-item list) 201 {"run_id": "RUN-0001"}; GET /runs/RUN-0001/manifest 200 the five-key body byte-for-byte (run_id the stem echo, question, verdicts sorted, quorum, items payload-order-preserved; operator.id + registered_at ABSENT — the exact-dict equality pins the key set); GET /runs/RUN-9999/manifest 404 the ThreePart body, the stem in found; the replay: the manifest body byte-identical across two fresh homes.

THE CURES, LIVE: 400 the malformed items — the three fields (the family grammar, NOT {"detail": [...]}), "items" in expected, "body.items" in found — over the socket AND in-process (tests/test_service_face.py "16 passed in 0.21s"); 404 the unmatched path — expected "GET /no-such-path", found "no route matches the path /no-such-path", next_action the route table; 405 the disallowed method — expected "DELETE /runs", found "the method DELETE is not allowed at the path /runs". The five routes' success bodies byte-stable (the exact-dict pins + the replay's byte-identity).

THE FOUR CONDITIONS, EACH RULED:
(a) THE EXACT-TASK LAW — GREEN: every fenced region landed byte-matching on my read (run_store 1a-1h; service_store 2a-2b; service.py 3a-3g; face 4a-4f, 16 tests; acceptance 4g-4l, the eight-request arc); the citation drift (line numbers off by ≤6) is naming, not bytes. BOTH DEVIATIONS RULED LEGITIMATE-TREE-FORCED: (1) the RUF002 ASCII dodge ("x2" for "×2", one docstring line) — RUF002 rides the tree's ruff ALL select; the spec's own byte would fail the zero-findings floor the spec itself demands, and an ignore would breach both "NOTHING added to pyproject" and the zero-ignore law; (2) the starlette alias — the installed starlette/exceptions.py exports HTTPException only (read directly, verified myself); the alias is the canonical FastAPI idiom, every downstream authored byte verbatim.
(b) THE CQRS SEGREGATION — GREEN: 2 commands (POST /runs, POST /runs/{run_id}/votes) / 4 queries (GET next, state, tally, manifest), every command POST, every query GET, the lanes clean; the core's refusals carried at the API BY TYPE in the family grammar (404/422/409/500), DONE a 200 VALUE — live-verified.
(c) THE THREEPART 21/21 — GREEN: 16 compliant (the typed-refusal catch tables + the 500 fold, each live-asserted) + 5 cured (the 400 re-badge ×3, one handler, branch total; the 404/405 refuse handler, statuses FROZEN) — my own probe of each family; never a bare status, never a stack leak (the 500 body carries no Traceback), never a silent OK.
(d) THE FLOOR + MY INDEPENDENT RE-RUN — GREEN: the verbatim outcomes above; my own re-run green at every instrument.

THE VERDICT: G-SERVICE's four conditions GREEN at my seat's word — the runtime's word, my own runs, the build seat's claims never trusted, only re-derived. — kensho, 2026-11-22
