<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/ground

**Route:** prioritree-ux (executing) | **Events:** 5 | **Reports:** 2

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T09:20:09Z |
| 2 | result | shinko | 2026-11-22T09:28:30Z |
| 3 | report | shinko | 2026-11-22T09:28:36Z |
| 4 | dispatch | shinko | 2026-11-22T09:36:12Z |
| 5 | report | tansa | 2026-11-22T09:37:27Z |
## Reported by shinko — 2026-11-22T09:28:36Z

tansa's completion report (packet census/ground, recorded by shinko):

THE GROUND CENSUS LANDED — six findings, exact paths, read-only held. THE EVIDENCE SET: .junro/evidence/Q-ux-surface/census-ground-a.md + census-ground-b.md (the return verbatim in two regions — the set-form, FR-MEM-0019's cure).

THE FINDINGS: (1) THE SERVER — src/prioritree/service.py, module-level app, five routes REST 1:1 over the five ops, exception handlers 400-re-badge + 500-fold, launch form `uvicorn prioritree.service:app` (no __main__, no make target, port unstated — the acceptance harness alone uses --port 0); (2) THE TECH NOTES — no standalone notes file exists; the collaborator's stack law lives in the stores' records (Q-frontend-stack's ruling at the birth store the closest carrier, cited with its line numbers); (3) THE WEB STATE — EMPTY: zero html/js/css/templates/static in the tree; the web tier exists as rulings only (README:20 names it banked); (4) THE MAKEFILE — dev/test/lint/typecheck/help only; NO lifecycle targets (R3's room is the current state); (5) .prioritree/ — the run store's home (STORE_HOME = Path(".prioritree/runs"), CWD-relative, run_store.py:53), carrying RUN-0001.jsonl registered 2026-11-22T05:22:15Z ("Who is prettier?"), untracked AND not gitignored — flagged for the lifecycle unit's brief; (6) THE DEPS — fastapi + uvicorn[standard] only; jinja2 ABSENT (the web tier's dep lands with it).

READ-BACK held (the files named in the evidence). The findings unassumed; the design lane takes them from here.
## Reported by tansa — 2026-11-22T09:37:27Z

# census/ground — tansa's completion report (the ground census, 2026-11-22)

WHAT I DID: the ground census over the repo — six asks, exact paths, read-only held (nothing written by the census itself).

1. THE FASTAPI SERVER: src/prioritree/service.py — module-level app = FastAPI() (line 152), the seam injected at construction (app.state.seam = Serialize(STORE_HOME), line 153). Five routes, REST 1:1 over the five ops: POST /runs → register (201 {run_id}); GET /runs/{run_id}/next → serve (optional seed query param; 200 the pair triple; DONE a 200 state body); POST /runs/{run_id}/votes → cast_vote (200 ack {vote_id, count, acknowledged}); GET /runs/{run_id}/state → census (200 {total, items}); GET /runs/{run_id}/tally → rank (200 the asdict whole, pair_counts keyed "item_a|item_b"). Two app-level handlers: rebadge (RequestValidationError → 400 {detail: errors}) and fold (Exception → 500 three-part crash envelope, the traceback to uvicorn's log channel). Status map: 404 StoreRefusedError, 422 VotesRefusedError, 409 TallyRefusedError, 400 the re-badge, 500 the crash. Launch form: uvicorn prioritree.service:app — ruled in the module docstring (lines 25/147: NO uvicorn.run in src, the boot the operator's command); NO __main__ in src, NO make target. The only exact invocation on disk is the acceptance harness's fixed argv (tests/test_service_acceptance.py:39-48): [<venv>/uvicorn, prioritree.service:app, --host 127.0.0.1, --port 0, --no-access-log]. No port stated in src — --port 0 (kernel-assigned) at the acceptance harness alone.

2. THE TECH NOTES: no standalone notes file exists — no docs/, no notes/; root *.md (README/AGENTS/CONTINUATION) carry zero hits on shoelace|htmx|cqrs|web component|frontend. The collaborator's notes live in the stores' records: Q-frontend-stack's ruling at the birth store (.plans/ideation/2026-11-19-prioritree-birth/.junro/junro.json lines 508/516/708/713 — HTMX UX-to-backend, Shoelace via CDN, Web Components separation-of-concerns, ALL frontend generated from Python, Jinja2 always, generated from structure); scope-synthesis.md lines 29/92 (the four-form layering, F8); prior-art.md lines 68/82 (CQRS: the tally a read model over the vote stream).

3. THE CURRENT WEB STATE: EMPTY — no templates/, no static/, no *.html/*.js/*.css anywhere in the tree. The web tier exists as rulings only (README.md:20 "banked").

4. THE MAKEFILE: five targets — dev (uv sync), test (uv run pytest), lint (ruff check src/ tests/), typecheck (pyright), help (the ## grep/awk). NO service/lifecycle targets exist.

5. .prioritree/ AT THE ROOT: runs/RUN-0001.jsonl — one manifest line, no vote lines: RUN-0001, items Tony/Mark + Jack/Eddie, operator "beauty"/"Who is prettier?", quorum 1, registered_at 2026-11-22T05:22:15Z. It IS the run store's home: STORE_HOME = Path(".prioritree/runs") (run_store.py:53) — a RELATIVE path written at the process cwd. Mechanical origin: a run registered ~3 minutes before this store minted (05:25), cwd at the repo root (CLI register or POST /runs — untracked because .gitignore carries no .prioritree entry).

6. pyproject.toml: dependencies = ["fastapi", "uvicorn[standard]"] — both present (the tree's first runtime deps); dev = pytest/pyright/ruff/httpx2. NO jinja2, NO web-tier deps of any kind.

LOAD-BEARING: the server exists whole (five routes, the lock seam, the crash envelope — 131 green at the service close); the front end is a greenfield (zero artifacts — R1's projection law starts from nothing); the lifecycle lane is a pure addition (no targets yet); ThreePart's ground is partial — refusals + the 500 envelope carry the three fields, the 400 re-badge carries FastAPI's native detail grammar instead (the error-shape ground shindan reads).

READ-BACK: the ux store's junro.json (R1-R5 cited); service.py whole; test_service_acceptance.py:30-99; Makefile; pyproject.toml; README.md; CONTINUATION.md; RUN-0001.jsonl; run_store.py (STORE_HOME grep); the birth store's junro.json (Q-frontend-stack); directory listings (root, .prioritree/, the ux store). Read-only held throughout.
