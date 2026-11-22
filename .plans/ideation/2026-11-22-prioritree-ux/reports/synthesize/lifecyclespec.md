<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/lifecyclespec

**Route:** prioritree-ux (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T18:43:21Z |
| 2 | report | togo | 2026-11-22T18:58:39Z |
## Reported by togo — 2026-11-22T18:58:39Z

# THE LIFECYCLE UNIT'S EXACT-TASK SPEC (synthesize/lifecyclespec — togo, 2026-11-22)

## §0 THE GROUND, READ + CITED
reports/synthesize/lifecycle.md — my own unit brief (G-LIFECYCLE-BRIEF approved; every mechanism cited per clause below) · reports/discover/lifecycle.md (tansa: the census — the Makefile greenfield at 18 l., the harness's launch/read-back forms, the .gitignore residue, the standing flag) · reports/understand/lifecycle.md (rikai: the mechanisms — the one-shell line, the pid chain, the port conflict, the two worker channels, the cwd chain, the refusal form) · Makefile at HEAD (whole, 18 l.) · .gitignore at HEAD (whole, 183 l.) · the ux store's junro.json (G-LIFECYCLESPEC-BRIEF :315-322 — the three conditions; G-LIFECYCLE :323-330; R3 :653). READ-ONLY held — nothing written beyond this report.

## §1 THE LAW (the exact-task law)
THE FENCE IS THE FILE: §2's fenced bytes are the Makefile's COMPLETE post-build content — 70 lines. The build lands them WHOLE (one whole-file patch), never a re-composition; where the tree at build time disagrees with this spec, the build STOPS and reports the disagreement (never improvises). Every recipe line begins with the single TAB byte (0x09); continuation indents inside multi-line recipes are 0x09 0x09. The growth is ASCII-clean (the standing file's own discipline; make/grep/awk/sort all byte-safe). THE HANDED CONSTRAINTS, VERBATIM (the gate's condition 2): HOST ?= 127.0.0.1 (the local-first single-operator bind) · PORT ?= 8000 (the named default port as a make variable, overridable) · single-worker — BOTH channels held (--workers NEVER on the line; WEB_CONCURRENCY removed, never blanked) · the cwd discipline (no cd in any recipe; the repo-root contract named in all four help entries).

## §2 THE MAKEFILE WHOLE-AFTER — THE COMPLETE POST-BUILD BYTES (70 lines)

```make
.DEFAULT_GOAL := help

PORT ?= 8000
HOST ?= 127.0.0.1

.PHONY: dev test lint typecheck help start stop status restart

dev:       ## Sync the environment (project + dev group, from the lock)
	uv sync

test:      ## Run the test suite
	uv run pytest

lint:      ## Ruff over src/ and tests/
	uv run ruff check src/ tests/

typecheck: ## Pyright over the tree's [tool.pyright] include set
	uv run pyright

start:     ## Start the server in the background (run from the repo root; pid -> .prioritree/server.pid; override: make start PORT=8100)
	@if [ -f .prioritree/server.pid ] && kill -0 $$(cat .prioritree/server.pid) 2>/dev/null; then \
		echo "start refused: expected no live pid, found pid $$(cat .prioritree/server.pid) live (the server is running); next-action: make status, or make stop"; \
		exit 1; \
	fi
	@if [ ! -x .venv/bin/uvicorn ]; then \
		echo "start refused: expected .venv/bin/uvicorn, found it absent (no venv yet); next-action: make dev (uv sync) first"; \
		exit 1; \
	fi
	@mkdir -p .prioritree
	@nohup env -u WEB_CONCURRENCY .venv/bin/uvicorn prioritree.service:app --host $(HOST) --port $(PORT) > .prioritree/server.log 2>&1 & echo $$! > .prioritree/server.pid
	@sleep 1; curl -s -o /dev/null -w 'read-back: HTTP %{http_code} on http://127.0.0.1:$(PORT)/ (404 = answering; 000 = still booting: make status)\n' http://127.0.0.1:$(PORT)/runs/RUN-0001/next || true

stop:      ## Stop the server: SIGTERM + the bounded drain (pid read from .prioritree/server.pid; run from the repo root)
	@if [ ! -f .prioritree/server.pid ]; then echo "stop: no pidfile; nothing managed (already down)"; exit 0; fi
	@pid=$$(cat .prioritree/server.pid); \
	if ! kill -0 $$pid 2>/dev/null; then \
		echo "stop refused: expected a live pid, found pid $$pid dead (stale pidfile); next-action: the stale pidfile is removed; make start launches fresh"; \
		rm -f .prioritree/server.pid; \
		exit 1; \
	fi; \
	echo "SIGTERM -> pid $$pid (the graceful drain)"; \
	kill $$pid; \
	i=0; \
	while kill -0 $$pid 2>/dev/null && [ $$i -lt 5 ]; do sleep 1; i=$$((i + 1)); done; \
	rm -f .prioritree/server.pid; \
	if kill -0 $$pid 2>/dev/null; then \
		echo "stop incomplete: expected the pid gone by the 5s bound, found pid $$pid still live; next-action: make status, or kill -9 $$pid"; \
		exit 1; \
	else \
		echo "stopped: pid $$pid gone (the pidfile is removed)"; \
	fi
	@curl -s -o /dev/null http://127.0.0.1:$(PORT)/runs/RUN-0001/next && echo "read-back: STILL ANSWERING on $(PORT); another (unmanaged) server holds the port" || echo "read-back: refused on $(PORT) - the port is down"

status:    ## Report the pid and the port, both labeled, read-only (run from the repo root)
	@if [ -f .prioritree/server.pid ]; then \
		pid=$$(cat .prioritree/server.pid); \
		if kill -0 $$pid 2>/dev/null; then echo "pid: $$pid (live)"; else echo "pid: $$pid (dead; stale pidfile; next-action: make stop cures it)"; fi; \
	else \
		echo "pid: none (no pidfile; not managed)"; \
	fi
	@code=$$(curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:$(PORT)/runs/RUN-0001/next); \
	if [ "$$code" = "404" ]; then echo "port: $(PORT) answering (HTTP 404 on /runs/RUN-0001/next; the ready form)"; \
	elif [ "$$code" = "000" ]; then echo "port: $(PORT) refused (down)"; \
	else echo "port: $(PORT) answered HTTP $$code (unexpected; not the ready form)"; \
	fi

restart: stop start ## Stop then start: the operator's rebind (run from the repo root; the read-backs ride both prerequisites)

help: ## Show this help
	@grep -hE '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
```

### §2a THE GROWTH'S ANATOMY (each region at its brief clause; every read-back named)
- :3-4 THE VARIABLES — `PORT ?= 8000` (brief §3d: the ?= overridable form, env or CLI `make start PORT=8100`; 8000 = uvicorn's own default, config.py:199-200 — the ruled default names what the launch already does) + `HOST ?= 127.0.0.1` (§3e: the local-first single-operator bind).
- :6 THE .PHONY GROWTH — the four names join the standing line (§6 item 5): `dev test lint typecheck help start stop status restart`.
- :20-31 START — :21-24 the kill -0 refuse-if-running guard FIRST (§3f: a live pid refuses with the expected/found/next-action grammar; a dead pid passes and the launch overwrites — the second-start-overwrites-the-pidfile defect cured, the live pid never lost to a doomed EADDRINUSE child) · :25-28 the binary guard (§3f: the direct binary's absence — no make dev yet — refuses with the ThreePart-spirit message) · :29 `mkdir -p .prioritree` (the spec's ruling, §2b-1) · :30 THE ONE-LINE LAUNCH (§3f/g): nohup + the $$! capture share the single recipe line (one make line = one /bin/sh, rikai §1); `env -u WEB_CONCURRENCY` (§3g: removal, never blanking — a blank string still reaches the child and int("") crashes the boot; the unset cannot lie; the second worker channel at config.py:358-359); the DIRECT SIBLING BINARY `.venv/bin/uvicorn prioritree.service:app` (the harness's own form, test_service_acceptance.py:41 — never `uv run`, whose wrapper pid would sit between the operator's kill and uvicorn's HANDLED_SIGNALS); `--host $(HOST) --port $(PORT)` ALONE (no --workers — config.py:274 `workers or 1`; no --no-access-log — the harness's test choice, never the operator surface); `> .prioritree/server.log 2>&1` (§3b: the default logger rides stderr, config.py:101) · :31 the read-back: `sleep 1` + ONE `curl -w '%{http_code}'` probe + `|| true` (the spec's ruling, §2b-5) — never a loop, never blocking; 000 = still booting with the next-action named. START'S READ-BACK (the gate's form, §3j): the port answers — the 404-AS-READY probe; `-f` NEVER (exit 22 fails the 404; the status is DATA).
- :33-52 STOP — :34 the absent-pidfile case: exit 0 (the spec's ruling, §2b-3) · :35-40 the stale case (§3h: kill -0 red → the honest refusal + the stale file removed) · :41-42 SIGTERM via `kill` — kill's default, NAMED in the message (§3h; uvicorn's HANDLED_SIGNALS, server.py:45-48 → the graceful drain → exit 0, main.py:639-640) · :43-44 the BOUNDED kill -0 drain-wait: 5 x sleep 1 = the ~5s bound (§3h; the harness's wait(5) precedent, test_service_acceptance.py:169-173) · :45 `rm -f .prioritree/server.pid` (§3h's sequence: kill -> wait -> rm -> report) · :46-51 the report: stopped, or the timeout reported honestly (ThreePart) · :52 the refusal read-back. STOP'S READ-BACK (§3j): the refusal — curl exit 7 / code 000, true at stop's return by the drain-wait; the unexpected arm named (a foreign holder).
- :54-65 STATUS — read-only, never acts (§3i): :55-60 the pid verdict (absent / dead-stale / live — kill -0 the probe); :61-65 the port verdict (`curl -w '%{http_code}'` on /runs/RUN-0001/next: 404 = answering, the ready form; 000 = refused; anything else = unexpected) — BOTH, labeled (either alone lies: a live pid + a refused port = draining or wedged; a dead pid + an answering port = an unmanaged hand-start). STATUS'S READ-BACK: the pid + the port both reported.
- :67 RESTART — the prerequisite composition (§2: stop + start, ZERO new mechanism, sequential by make's own nature; NO recipe; the `-j` race fails safe — start's guard meets the draining pid and honestly refuses, §3j).
- The probe path's exact bytes: `/runs/RUN-0001/next` (§6 item 6 — the honest-404 form, tansa §5b).

### §2b THE SPEC'S BYTE-LEVEL RULINGS (the open cases the brief's §6 handed this lane — each with its reason)
1. `mkdir -p .prioritree` at :29 — the log's redirect opens the file at SHELL time, before the child boots; on a fresh tree the home is absent and the launch would die on the redirect. Idempotent, minimal.
2. The binary guard at :25-28 — the brief's own word: the direct binary's "absence (no make dev yet) refuses with the ThreePart-spirit message" (§3f). It names make dev.
3. The absent-pidfile stop case -> exit 0 at :34 — the brief ruled the STALE case a refusal (a pidfile that lies); the ABSENT case is the satisfied state (the server is already down, the refusal read-back already true), and make's prerequisite semantics demand it: a refusing stop would kill restart's chain on a fresh tree, breaking the ruled composition. Idempotent stop, never a failure.
4. The probe's byte completion: `curl -s -o /dev/null -w '%{http_code}'` — the brief's ruled -w form + the body-suppressing pair (the code as data, the report clean); `-f` NEVER.
5. The one-shot settle at :31: `sleep 1` + one probe + `|| true` — a cold boot binds in well under 1s on a warm FS; a zero-settle probe would print 000 by construction. NEVER a loop, never a retry, never a failure (the read-back reports, never judges; the bounded retry is the gate's/kensho's machinery, §3f/j).
6. The drain-wait's form at :43-44: `while kill -0 ... && [ $$i -lt 5 ]; do sleep 1; i=$$((i + 1)); done` — the bound is 5 sleeps = ~5s, the harness's wait(5) precedent.
7. The messages' grammar: expected/found/next-action (ThreePart-spirit) at every refusal point — the tree's own refusal grammar at the operator surface.
8. The ASCII discipline: the growth carries no multibyte — the standing 18 lines are ASCII; the growth matches the file's own bytes.

## §3 THE .GITIGNORE'S ONE LINE (the curing line)
PLACEMENT: the file's END — appended at :184, immediately after `/.junro/` (:183, the store's heart): the two tool-homes adjacent, each in its ruled form. BYTES: `.prioritree/` (12 bytes) + the newline. ONE line, no comment, NO duplicate log entry (brief §3c: `*.log` at .gitignore:61 already matches any .log at any depth — one line, one meaning). THE CURE (§3c): the pidfile AND the census's standing flag — the live store content `.prioritree/runs/`, untracked-not-ignored at HEAD (tansa §4) — both ignored by the home-level entry; the tool-home is runtime artifacts by definition, never tracked. The brief's ruled form carried verbatim: `.prioritree/`.

## §4 THE NO-BREAK PROOFS
(a) THE FIVE STANDING TARGETS BYTE-UNTOUCHED: :1 (`.DEFAULT_GOAL := help`), :8-9 (dev), :11-12 (test), :14-15 (lint), :17-18 (typecheck), :69-70 (help + the pipeline) — byte-identical to HEAD's :1, :5-6, :8-9, :11-12, :14-15, :17-18. The ONLY standing-line edit: :6 (the .PHONY growth — the ruled growth, never a target's byte). The diff adds, never touches.
(b) THE FLOOR'S FOUR ACTS GREEN — THE GROWTH ADDS NO PYTHON: the unit touches ZERO files under src/ or tests/ (the brief §1's fence — the policy in the TARGETS, never in src) -> make dev (uv sync) a no-op (the lock untouched) · make test green (156 passed — the web unit's close state stands) · make lint green (All checks passed!) · make typecheck green (0 errors, 0 warnings). The floor rides unchanged and green (G-LIFECYCLE condition 3's first half).
(c) THE RECIPES' SHELL FORMS vs THE DISCOVERY'S MECHANISMS, each verified: `$$` the escaping — make's `$$` -> the shell's `$` (the help pipeline's own precedent, HEAD :18): `$$!`, `$$(cat ...)`, `$$pid`, `$$((i + 1))` all render; ONE make line = ONE /bin/sh (rikai §1) — the launch at :30 is ONE line, the $$! capture the line's own · the nohup/env exec chain — nohup execs env execs uvicorn: $$! IS uvicorn's pid, no wrapper between the operator's kill and HANDLED_SIGNALS (the brief §3f's ruling against `uv run`) · the kill -0 forms (rikai §1, the liveness probe): start's guard :21, stop's stale guard :36 + drain-wait :44/:46, status's verdict :57 · SIGTERM = kill's default, NAMED at :41 (rikai §1: HANDLED_SIGNALS -> the graceful drain -> exit 0) · curl -w '%{http_code}' the status as DATA (tansa §5b, rikai §4: -f NEVER; 404 = ready; 000/exit 7 = the refusal; curl is a darwin base-system binary — no new dependency) · `env -u WEB_CONCURRENCY` (rikai §3: the second worker channel at config.py:358-359 — removal, never blanking) · the direct sibling binary `.venv/bin/uvicorn` (tansa §2: the harness's own form, test_service_acceptance.py:41) · no cd in any recipe; the repo-root contract in all four help entries (§3k: STORE_HOME + web/templates + web/static all resolve CWD-relative at the root — a non-root launch means a scratch store and dead pages) · the help entries' shape identical to the standing form (`target: [prereqs] ## description`) — whatever the pipeline parses at HEAD, the growth parses the same way; `make help` renders NINE entries.

## §5 THE COMMAND SEQUENCE PER-STEP (R8) — THE DISPATCH PLAN
Three step-dispatches (one step per dispatch), the executor jikko (the build seat — the route's own precedent), each step's report riding the packet (R11), the commit banked at the coordinator's hand. NOTHING beyond the named act in any step.

STEP 1/3 — THE MAKEFILE'S EDIT: land §2's fence WHOLE (the 70 lines, byte-exact, the TAB-led recipes) via one whole-file patch. THE READ-BACK: the file re-read whole — the diff vs HEAD shows ONLY the growth (:3-4 the variables; :6 the .PHONY growth; :20-31 start; :33-52 stop; :54-65 status; :67 restart); the standing bytes identical (:1, :8-18, :69-70). FILE THE STEP REPORT (R11). THE RETURN (<=10 lines).

STEP 2/3 — THE .GITIGNORE'S LINE: append ONE line at :184: `.prioritree/` (immediately after `/.junro/`). NOTHING else. THE READ-BACK: the tail re-read verbatim (:183-:184 — `/.junro/` then `.prioritree/`); the file whole at 184 lines. FILE THE STEP REPORT (R11). THE RETURN (<=8 lines).

STEP 3/3 — THE FLOOR (the pack's own fixed-argv acts): the test act (all) -> 156 passed; the lint act (check) -> All checks passed!; the typecheck act -> 0 errors, 0 warnings. dev = uv sync is a no-op (the lock untouched — nothing to sync). A finding outside these expectations is a report item, never an edit. FILE THE STEP REPORT (R11 — the outcomes verbatim). THE RETURN (<=12 lines).

THE LIVE SEQUENCE — G-LIFECYCLE condition 2's own letter, NOT a build-seat dispatch (the make verb rides the coordinator's hand; kensho's pack re-runs it independently at validate/lifecycle — condition 3): make start -> the read-back: the port answers (curl -w: 404 on /runs/RUN-0001/next) · make status -> the pid + the port, both labeled · make restart -> the refusal then the answer · make stop -> the refusal (000/exit 7), true at return by the drain-wait.

THE COMMIT — at the coordinator's hand (shinko), ONE commit at the unit's close (the gate's green held), covering both files (the Makefile + the .gitignore — the unit's whole); proposed message: `Makefile: the lifecycle targets start/stop/status/restart; .gitignore: the .prioritree/ runtime home`.

## §6 THE GATE'S MAPPING + THE TRADE-OFF CARRIED
G-LIFECYCLESPEC-BRIEF's conditions -> this spec: (1) "every target's exact recipe bytes, every read-back named, the per-step dispatch plan whole" -> §2's fence + §2a (each target's read-back named at its recipe) + §5 (R8 whole). (2) "the ruled target set (start, stop, + the etc. the design/census pin — R3) with the handed constraints verbatim" -> the four-target set (R3's "etc." = restart, the brief §2's pin): start/stop/status/restart; 127.0.0.1; the named port; single-worker (both channels); the cwd discipline — all verbatim at §1 and in the bytes. (3) "the collaborator approves the spec — the build dispatches fire only after" -> the gate's own act: §5's three steps fire only at the approval.
THE TRADE-OFF CARRIED (the brief §7, standing): the recipes are hand-authored shell — make IS the operator's shell (the no-shell law binds the seats' Python, never the operator's recipes); the pidfile discipline's known limits (a recycled PID makes kill -0 lie — the single-operator local tool's price) — carried knowingly; process-management machinery (launchd/launchctl) ruled out — zero precedents, the absence IS the finding.
