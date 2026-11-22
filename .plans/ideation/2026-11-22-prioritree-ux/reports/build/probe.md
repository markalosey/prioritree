<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — build/probe

**Route:** prioritree-ux (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T14:56:13Z |
| 2 | report | jikko | 2026-11-22T15:08:13Z |
## Reported by jikko — 2026-11-22T15:08:13Z

# THE BUILD REPORT — build/probe (jikko, 2026-11-22)

THE EDITS, LANDED PER FILE (the spec's §5 order; fenced bytes at every point):
1. run_store.py (1a-1h): ItemRow, RunManifest import; reads-clause amended; __init__ fourth param + self._manifest; register's cls(session, run_id, run_file, manifest); load docstring + un-underscored discard + four-part return; the manifest accessor between rank and run_id (l.876-898). All §5 read-back anchors confirmed.
2. service_store.py (2a-2b): TYPE_CHECKING import + Serialize.manifest at the tail (with self._lock: / Persist.load(...).manifest()).
3. service.py (3a-3g): docstring head (sixth query + ThreePart cures named); starlette import; QUESTION/VERDICTS/QUORUM after ITEMS, DETAIL retired; _MANIFEST_PATH after _STATE_PATH; the rebadge cure (param un-underscored); _NOT_FOUND/_METHOD_NOT_ALLOWED + refuse + _ROUTE_TABLE between fold and register; the describe route at the tail.
4. test_service_face.py (4a-4f): docstring; test_manifest_200 + test_refusal_manifest_unknown_run inserted; the 400 flip (family set + three substring pins); test_refusal_unmatched_path_404 + test_refusal_method_not_allowed_405 inserted; the five success tests + door-refusal-422 byte-untouched. 16 test functions.
5. test_service_acceptance.py (4g-4l): docstring head; _drive_arc's manifest GET second; test_accept_the_eight_request_arc (literals re-indexed, bodies[1] the five-key manifest); replay docstring says eight; the four-arcs 400 clause + section flipped to the family grammar.

THE FLOOR (once after all five; rerun after the two tree-forced fixes):
- make test: "135 passed in 24.74s" — 0 failed, 0 errors; the spec's byte-named nodes among them (test_manifest_200, test_refusal_manifest_unknown_run, test_refusal_unmatched_path_404, test_refusal_method_not_allowed_405, the flipped test_rebadge_malformed_body_400, the renamed test_accept_the_eight_request_arc, test_replay_byte_identical, test_refuse_the_four_arcs, test_interleave_the_concurrency_arc). NOTE: the spec names 115 test FUNCTIONS (111+4); pytest's 135 counts ITEMS — the spec's own "parametrized expansions aside" clause covers the difference.
- make lint: "All checks passed!"
- make typecheck: "0 errors, 0 warnings, 0 informations"
- make dev: NOT RUN — no act in this seat's pack carries it; pyproject byte-untouched (uv sync a no-op by the spec's own note).

THE COMMIT: NOT DONE — the dispatch names "the git tool (land op)" but this seat's pack routing carries no git act. The five files stand on disk, floor green; the commit (the spec's message: "prioritree-ux: the probe increment lands — G-SERVICE green, the sixth query live, the error surface 21/21 ThreePart") awaits the coordinator's hand.

THE DEVIATIONS (two, both tree-forced, both one line, every other authored byte verbatim):
1. service.py refuse docstring: the spec's `×` (MULTIPLICATION SIGN) refused by the tree's standing RUF002 at apply time; landed ASCII `x` ("R5's census cure x2") — the spec's own zero-findings floor demanded it.
2. service.py l.59: the spec's `from starlette.exceptions import StarletteHTTPException` is ImportError in this tree (the installed starlette.exceptions exports HTTPException only — verified); landed as `from starlette.exceptions import HTTPException as StarletteHTTPException` (the FastAPI-canonical alias idiom) — every downstream authored byte (decorator, signature, docstring, handler) rides verbatim.

CITATION DRIFT, noted (the fences ruled; every fence matched the tree uniquely): 1b named l.475-478, the bytes sat at l.474-477; 4a named l.2-17, the docstring closes at l.18; 4g/4j named ranges off by ~2. The _ROUTE_TABLE fence carries a leading blank its own note denies ("no blank line before the comment (one constants region)"); landed per the note — the comment directly after _TALLY_PATH.
