# CENSUS/GROUND — the existing UX ground (prioritree-ux) — tansa — part a of the set (b: census-ground-b.md)

**1. THE FASTAPI SERVER**
- The server: `src/prioritree/service.py` (the only src module importing fastapi; grep -l -i "fastapi" over `*.py` → also `tests/test_service_face.py` [TestClient] and `tests/test_service_acceptance.py` [live boot]). The seam beneath: `src/prioritree/service_store.py` (`Serialize`, the lock seam).
- App entry point: module-level `app = FastAPI()` (service.py:152); `app.state.seam = Serialize(STORE_HOME)` (:153); `__all__ = ["app"]` (:59).
- Routes — five, REST 1:1 over the five ops (service.py:85-88, :224):
  - `POST /runs` → `register` (:227) — 201 `{"run_id": stem}`
  - `GET /runs/{run_id}/next` → `serve` (:256) — optional query param `seed`; 200 `{"item_a","item_b","count"}`; DONE a 200 state body (`done: true` + three fields)
  - `POST /runs/{run_id}/votes` → `cast_vote` (:286) — 200 ack `{"vote_id","count","acknowledged"}`
  - `GET /runs/{run_id}/state` → `census` (:323) — 200 `{"total","items"}`
  - `GET /runs/{run_id}/tally` → `rank` (:357) — 200 asdict(TallyResult), `pair_counts` keyed `"item_a|item_b"`
- Exception handlers: `RequestValidationError` → `rebadge` → 400 `{detail: errors}` (:174-195); `Exception` → `fold` → 500 three-part crash envelope (:198-223).
- Status mapping: 404 StoreRefusedError, 422 VotesRefusedError, 409 TallyRefusedError (SAFE HALT), 400 the re-badge, 500 the crash envelope.
- Meant to run: `uvicorn prioritree.service:app` — the ruled launch form, stated in the module docstring (service.py:25, :147: "NO uvicorn.run in src — the boot the operator's command"). No `__main__` in src/tests (the tree's only `__main__` blocks are `.opencode/scripts/*` harness engines). No make target for the service. The only exact invocation on disk — the acceptance harness's fixed argv (tests/test_service_acceptance.py:39-48): `[<venv>/uvicorn, "prioritree.service:app", "--host", "127.0.0.1", "--port", "0", "--no-access-log"]`.
- Port: NOT stated in src. The acceptance harness alone uses `--port 0` (kernel-assigned, parsed from the banner; Q-service-lifecycle: the live socket at the acceptance unit alone).

**2. THE TECH NOTES**
- No standalone notes file exists — no `docs/`, no `notes/` directory; root `*.md` (README.md, AGENTS.md, CONTINUATION.md) carry zero hits on shoelace/htmx/cqrs/web component/frontend. The collaborator's notes live in the stores' records; the grep sweep's carriers:
  - `.plans/ideation/2026-11-19-prioritree-birth/.junro/junro.json` — **Q-frontend-stack's ruling** (:508, :516, :708, :713): "FRONTEND STACK (collaborator ruling 2026-11-19, the development ground rules, stated twice for emphasis): HTMX carries UX-to-backend; Shoelace via CDN supplies the UX component chrome; Web Components with separation-of-concerns architecture; ALL frontend things are generated from Python — including the entire Web Components surface; Jinja2 templating always; generated from structure." The closest thing to the named "notes for the tech."
  - `.plans/ideation/2026-11-19-prioritree-birth/synthesize/scope-synthesis.md` — the ruled layering (:29: "CLI wraps, FastAPI serves, web fronts"; :92: F8 LAYERING).
  - `.plans/ideation/2026-11-19-prioritree-birth/.junro/evidence/Q-problem-space/prior-art.md` — CQRS/event-sourcing prior art (:68, :82: the tally a CQRS read model projected from the vote stream).
  - This effort's own composition records also carry the stack (`.plans/ideation/2026-11-22-prioritree-ux/.junro/evidence/Q-ux-surface/route-composition*.md`, `reports/compose/route.md`) — this route's own, not the collaborator's notes.

**3. THE CURRENT WEB STATE**
- **EMPTY — the finding.** No `templates/`, no `static/`, no `*.html`, no `*.js`, no `*.css` anywhere in the tree (glob `**/*.{html,js,css}` → no files; `templates/**` and `static/**` → no files). The web tier exists as rulings only (README.md:20: "Web app — banked (the stack's fourth layer): fronts the service").

**4. THE MAKEFILE** (verbatim target list — 5 targets; `.DEFAULT_GOAL := help`; `.PHONY: dev test lint typecheck help`)
- `dev:` → `uv sync` — sync the environment (project + dev group, from the lock)
- `test:` → `uv run pytest` — run the test suite
- `lint:` → `uv run ruff check src/ tests/` — ruff over src/ and tests/
- `typecheck:` → `uv run pyright` — pyright over the tree's `[tool.pyright]` include set
- `help:` → grep/awk over the `##` comments — show this help
- NO service/lifecycle targets exist (no start/stop) — R3's "room for service targets later" is the current state.
