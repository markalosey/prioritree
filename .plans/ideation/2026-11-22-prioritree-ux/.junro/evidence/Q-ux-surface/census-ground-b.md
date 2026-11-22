# CENSUS/GROUND — part b of the set (a: census-ground-a.md) — the run store home, the dependencies, the read-back

**5. `.prioritree/` AT THE REPO ROOT**
- Contents: one file — `runs/RUN-0001.jsonl` (1 line, the manifest; no vote lines): items `[["Tony","Mark"],["Jack","Eddie"]]`, operator id `"beauty"`, question `"Who is prettier?"`, verdicts `prefer-a/prefer-b/tie`, quorum 1, run_id `RUN-0001`, registered_at `2026-11-22T05:22:15.763491+00:00`.
- What it is: the file-backed run store's home — `STORE_HOME: Final[Path] = Path(".prioritree/runs")` at `src/prioritree/run_store.py:53`, a RELATIVE path (written at the process cwd; `app.state.seam = Serialize(STORE_HOME)` at service.py:153 uses the same constant).
- Origin (mechanical): a run registered 2026-11-22T05:22:15Z through the run-store seam (CLI register or `POST /runs`) with cwd at the repo root — ~3 minutes before this effort's store minting (05:25). Untracked because `.gitignore` carries no `.prioritree` entry (grep of .gitignore: no match) — untracked-and-not-ignored.

**6. pyproject.toml — THE DEPENDENCY LIST**
- `dependencies = ["fastapi", "uvicorn[standard]"]` (:7) — fastapi: YES; uvicorn: YES (the `[standard]` extra). The tree's first and only runtime deps.
- `[dependency-groups] dev = ["pytest", "pyright", "ruff", "httpx2"]` (:134).
- jinja2: **NO.** No web-tier deps of any kind (no htmx, no shoelace, nothing beyond the service pair).
- Context: requires-python `>=3.13`; `[project.scripts] prioritree = "prioritree.cli:command"`; hatchling build, packages `["src/prioritree"]`.

**READ-BACK (files actually read):** `.plans/ideation/2026-11-22-prioritree-ux/.junro/junro.json` (the ground rules — R1/R2/R3/R5 confirmed); `src/prioritree/service.py` (whole, 393 lines); `tests/test_service_acceptance.py` (:30-99); `Makefile` (whole); `pyproject.toml` (whole); `README.md`; `CONTINUATION.md`; `.prioritree/runs/RUN-0001.jsonl` (:1); directory listings of repo root, `.prioritree/`, `.prioritree/runs/`, `.plans/ideation/2026-11-22-prioritree-ux/`; greps: `*.py` for fastapi/uvicorn/`__main__`/STORE_HOME, `run_store.py` for STORE_HOME, `*.md` and all-files for shoelace|htmx, `.gitignore`, birth-store `junro.json` for Q-frontend-stack. Nothing written to disk — read-only held.

The ask-ceiling held: one primary act (this census) + read-back + this report. The findings are delivered unassumed — no interpretation, no recommendations; the design lane's seats take it from here.
