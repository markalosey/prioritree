<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — discover/lifecycle

**Route:** prioritree-ux (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T18:27:11Z |
| 2 | report | tansa | 2026-11-22T18:31:24Z |
## Reported by tansa — 2026-11-22T18:31:24Z

# THE LIFECYCLE UNIT'S BUILD-SURFACE CENSUS (discover/lifecycle, tansa) — verified at HEAD 2026-11-22

1. THE MAKEFILE — 18 lines whole, five targets, re-verified: .DEFAULT_GOAL := help (:1); .PHONY: dev test lint typecheck help (:3); dev :5-6 (uv sync); test :8-9 (uv run pytest); lint :11-12 (uv run ruff check src/ tests/); typecheck :14-15 (uv run pyright); help :17-18 (the grep|sort|awk pipeline). ZERO service/lifecycle targets — the unit's surface is greenfield.

2. THE LAUNCH GROUND TRUTH — the tree's only exact invocation on disk: the acceptance harness's fixed argv, tests/test_service_acceptance.py:39-54 (_UVICORN the sibling binary :41; _ARGV :42-50 = [<venv>/uvicorn, prioritree.service:app, --host 127.0.0.1, --port 0, --no-access-log]; the banner regex :54), fired Popen(_ARGV, cwd=home, stderr=PIPE) :81. The src-side ruled form: service.py:33-34 — "the launch form uvicorn prioritree.service:app; NO uvicorn.run in src". THE CWD STAKE: three CWD-relative homes ride the launch cwd — STORE_HOME (run_store.py:53, Path(".prioritree/runs")) + web/templates + web/static (web.py:76-77; the mount :119 check_dir=False; Jinja2Templates :120) — the repo-root launch resolves all three and serves the pages; at a scratch cwd the page tier is dead (webspec.md:3653).

3. THE HANDED CONSTRAINTS, each cited: (a) design brief §12 (ux-design.md:143): start/stop/status; 127.0.0.1 + a NAMED default port as a make variable (overridable), the policy in the TARGETS never in src; single-worker — --workers NEVER passed (uvicorn default 1; the seam's process-wide lock the single-writer contract, service_store.py:56's banked note); the cwd discipline — the targets launch from the repo root; the pidfile discipline (start writes, stop/status read) + the log channel (also §13:147 item 7; §14:164 item 14 — Low 7 HANDED). (b) hyoka's Low 7 (adversarial.md:32): "the lifecycle unit's constraints (port/host policy — 'Port: NOT stated in src', census-ground-a; single-worker launch) are never handed forward; the brief should carry them." (c) R3 (junro.json:653): "room for service targets later" (the birth ruling's own clause) is now. (d) THE RETHINK (webspec.md): the cwd discipline held (:2114 the homes resolve CWD-relative, the SAME law STORE_HOME rides; :2146 the home STANDS, CWD-relative per the launch discipline; :2165 the repo-root launch — the lifecycle targets — serves the files), the port policy in the targets never in src (:479/:3033), the Makefile untouched (:2120/:3236); the four-part set "127.0.0.1, the named port, single-worker, the cwd discipline" pinned verbatim at G-LIFECYCLESPEC-BRIEF's condition (junro.json:319).

4. THE PROCESS-MANAGEMENT SURFACE — NOTHING exists in-tree: no src module, no target, no script manages a background process; zero nohup/daemonize/setsid/launchd/launchctl hits anywhere (whole-tree greps). The pidfile/log idioms appear ONLY as .gitignore template residue (:61 "*.log" under "# Django stuff"; :127 "celerybeat.pid" under "# Celery stuff") — ignore rules, never idioms in use. The only subprocess surfaces: test_harness.py:62-64 (subprocess.run, foreground CLI runs) and the acceptance harness's Popen. darwin launchd: zero precedents — the absence IS the finding.

5. THE READ-BACK FORMS — (a) the stderr-banner parse: the port read back from "Uvicorn running on http://127.0.0.1:(\d+)" (:54; the bounded loop :86-94). (b) the 404-as-ready probe _wait_ready :105-137 AT HEAD (the dispatch's :103-135 is the pre-manifest-leg numbering — the file grew 417→437): GET /runs/RUN-0001/next, timeout 0.5; 404 => ready (the whole chain proven); ConnectError/ConnectTimeout => sleep(0.1) + retry (:127-129 — the connection-refused form: refused = not-up-yet); any other status fails loudly (:132-134); the 15s deadline fails (:135-137) — a timeout FAILS, never skips. (c) the teardown terminate→wait(5)→kill (:167-173). G-LIFECYCLE's own read-back conditions (junro.json:327): start = the port answers; stop = the refusal.

6. THE TEST SURFACE — 15 test files + __init__ at HEAD; ZERO lifecycle tests exist (no test_lifecycle*, no make-target/process test; greps over tests/ find no lifecycle surface). The acceptance harness's boot/teardown (:67-102 _boot; :140-173 the fixture) is the tree's ONLY live-process precedent.

READ-BACK: Makefile whole · test_service_acceptance.py whole · service.py :1-40 · web.py :1-139 · run_store.py :50-57 · service_store.py :50-61 · .gitignore :55-66/:121-130 · ux-design.md whole · adversarial.md whole · adversarial-web/webspec/web.md targeted greps · the ux store's junro.json :639-668 + greps · tests/ + web/ globs. READ-ONLY held — nothing written beyond this report.
