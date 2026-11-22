<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/lifecyclespec

**Route:** prioritree-ux (executing) | **Events:** 5 | **Reports:** 2

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T18:43:21Z |
| 2 | report | togo | 2026-11-22T18:58:39Z |
| 3 | gate | shinko | 2026-11-22T18:59:56Z |
| 4 | dispatch | shinko | 2026-11-22T19:17:21Z |
| 5 | report | togo | 2026-11-22T19:25:39Z |
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
## Reported by togo — 2026-11-22T19:25:39Z

# THE LIFECYCLE UNIT'S EXTENSION — THE MEMBER-CALLABLE SURFACE (synthesize/lifecyclespec, togo, 2026-11-22; the amended spec whole = this extension + the landed first spec, the chain composing both at this packet's projection)

## §E0 THE GROUND, READ + CITED
The ux store's junro.json whole — Q-ux-surface R12 (:635, the member-callable surface) + R13 (:643, the readable runtime), G-LIFECYCLESPEC-BRIEF :315-322, G-LIFECYCLE :323-330 · my landed spec (reports/synthesize/lifecyclespec.md — the 70-line fence, the tree at HEAD matching it byte-for-byte; the .gitignore's `.prioritree/` landed at :184) · the landed Makefile whole (70 l.) · .opencode/scripts/ read back: FIVE engines (calculate, curate, friction_ledger, patch, test_runner) — **the named ".opencode/scripts/lint.py" DOES NOT EXIST**: the lint tool has NO engine; it is the pure make shim (lint.ts:32/35 — runArgv(["make", "lint"])) — the closest fixed-argv act form is the wrapper itself, and that is this design's form · lint.ts whole (43 l. — the wrapper precedent) · _run.ts whole (the explicit-argv channel) · test_runner.py whole (the engine form where no make target exists) · kensho.md (the pack-routing table form, the regen header) · .opencode/tsconfig.json (the tsc scope + the family's Bun caveat) · the birth store's junro.json :595 (amendment 42's landed form) + the core store's :493 (the grant at HEAD, FR-MEM-0014's chain) · synthesize/tool-grants-brief.md §2 (the wrapper landing form: "tracked tree assets, NOT --check-covered; landed through the standing hands") · FR-MEM-0014/0024/0025 read whole via the friction ledger · the lifecycle unit brief (reports/synthesize/lifecycle.md — §2 the ruled target set, §3i/j the mechanisms, §4 the zero-test ruling) · packets.jsonl :183 (this dispatch). READ-ONLY held — nothing written beyond this report.

## §E1 THE LANDING FORM RULED — (b) THE MID-ROUTE GRANT PRECEDENT, LANDING NOW (the design's first ruling; R12's named question)
**RULED: (b) — amendment 42's own form, landing NOW, composed per the tree's two-surface discipline.** The two surfaces have two different homes, and the ruling names each:
- **THE WRAPPER (.opencode/tools/lifecycle.ts): DIRECT, THIS TREE, THE STANDING HANDS — now.** The wrappers are NOT emission-covered: the harness's own record rules them "tracked tree assets, NOT --check-covered; landed through the standing hands" (tool-grants brief §2), and lint.ts:1 + _run.ts:1 carry the standing header "hand-maintained in prioritree's tree". The scaffold's 24 artifacts never included a wrapper; option (a)'s "the wrapper rides the scaffold's own cycle" has ZERO precedent — it invents an emission capability mid-route. The wrapper lands via patch (jikko's step), tracked, prioritree-owned.
- **THE GRANT (opencode.json's permission rows + the seat prompts' Pack Routing rows): THE MID-ROUTE SOURCE-EDIT + REGEN — amendment 42's literal landed form (birth store :595: "the adapter edit + the re-emit lands the allow in the permission map and the row in kensho.md's pack table"), NEVER a hand-edit of the derived rows.** The derived surfaces carry the regen header ("do not edit manually"); the standing law is explicit ("never hand-edit cycle-generated files — the fix is a re-run"), and the tree's own record prices the hand-edit form: the amendment-28 togo stopgap — a hand-allow at a derived surface, CLOBBERED by the next ruled re-emit. So: the hikari-side adapter edit (prioritree-seats.yaml's pack rows + the universe entry) + the regen (--target prioritree) fired mid-route at the collaborator's hand — the same machinery amendment 42 fired, now rather than at a scheduled cycle. THE SYNC IS NOT BANKED — the source edit IS the sync, and it rides the same window as the landing: a banked sync leaves the clobber window open (the drift the never-hand-edit law exists to prevent).
**WHY (b) OVER (a):** R12's own diagnosis — G-LIFECYCLE condition 2 is BLOCKED at kensho's hands NOW (no make verb; the live read-backs ran at the collaborator's shell — FR-MEM-0025's own record); the unit's close waits on the live sequence being a member's own act. (a) routes the whole landing through the hikari-side cycle — out of this tree's reach, the unit blocked meanwhile, and it still pays the same universe cost (below). (b) lands the capability in the unit's own window, through forms the tree has already used (the tool-grants unit's wrapper landing + amendment 42's grant), with every drift price named.
**THE UNIVERSE COST — PAID EITHER WAY, NAMED:** a new tool id (lifecycle) grows the closed-world universe 26 → 27; the deny-lines re-derive at every seat in every tree — clarity's and input's opencode.json re-byte (the sibling-impact law, tool-grants brief §2's derivation), their --check legs re-run. This is the universe's price, not the landing form's — (a) pays it identically.
**THE OPERATIONAL NOTE (FR-MEM-0014, THE DRIFT LESSON PRICED):** a landed grant is ABSENT from every live session's callable set — opencode registers .opencode/tools/*.ts and derives the seat's pack AT LAUNCH. The grant lands at the tree; the DELIVERY lands at the launch: after the regen, the collaborator RESTARTS opencode, and only post-restart sessions carry the lifecycle act. A live session's "no verb exists" refusal after the landing is the NAMED EXPECTED STATE (the stale-session class, FR-MEM-0007/0008's family), never a defect report; the verification step (§E6 step 4) dispatches into a post-restart session by construction.

## §E2 THE WRAPPER'S DESIGN — THE FIXED-ARGV ACT FORM (R12)
**THE NAME (the naming law):** the act-statement — "the lifecycle surface: the members call the service's lifecycle verbs directly" — first word: **lifecycle** → `.opencode/tools/lifecycle.ts` (the filename IS the tool id, Q-tool-registration).
**THE DRY QUESTION RULED: THE WRAPPER SUBPROCESSES MAKE — ONE IMPLEMENTATION.** The recipes live ONCE in the Makefile (R3's ruled surface, G-LIFECYCLE's exact-task bytes, already landed and live-proven); the wrapper is the argv shim over them — lint.ts's own form (ops → runArgv(["make", "<target>"]), ZERO mechanism of its own; the "engine at .opencode/scripts/lint.py" does not exist precisely because the lint tool owns nothing). Re-implementing the verbs (the pid chain, the kill -0 guards, the drain-wait, the probe forms) would fork the mechanism: two truths to keep true, every cure (RUN-9999 itself) landing twice, the G-LIFECYCLE exact-task bytes re-authored — the divergence class the tree's whole discipline refuses. The wrapper NEVER owns a transition.
**THE READ VERBS (R13) — TWO PURE READS, RULED:** the Makefile's set stays FOUR (the brief §2's ruling untouched — no log/output targets; the operator's surface and the members' surface are two surfaces, the transitions shared, the reads member-only):
- **log** — the SERVER LOG's bounded tail (.prioritree/server.log — the boot banner, the request channel, the errors, the drain lines), default the last 100 lines, `tail` overridable; an in-wrapper read (node:fs — no subprocess, no shell, no engine: web.ts's zero-engine in-wrapper precedent). EARNED: the read tool reads from the HEAD (2000-line default) — a growing log's meaning lives at the TAIL, a moving target offset cannot express; R13's bounded-tail discipline is the form no standing instrument carries.
- **output** — THE SERVICE'S LIVE ANSWER, VERBATIM: the RUN-9999 probe's response BODY whole (an in-wrapper fetch — web.ts's fetch precedent; status reports the CODE, output reports the BODY — the honest ThreePart refusal's own words, FR-MEM-0025's cure read at the surface it was built for; R13's "the port's answers" among the runtime's readable evidence). RULED REJECTED, priced: (i) the log-twin form (output = a second log read — an ungrounded duplicate verb); (ii) the tee form (the wrapper appending each transition's output to a second log home — a new write channel + a new artifact for a need the live body serves without mutation; R13: "the read verbs are read-only — never a mutation"). THE OPEN QUESTION NAMED for the gate: R13's "the output verbatim" read HERE as the live-answer body; the transitions' own outputs already ride verbatim by the wrapper's rendering law (formatOutput — stdout/stderr whole, exit codes passed through), so no verb is minted for them.
**THE VERBS' ARGV + READ-BACKS (each):** start → `["make","start", +PORT=/HOST= overrides]` — the read-back: the recipe's own line (the port answers; 000 = still booting) · stop → `["make","stop"]` — the drain report / the refusal read-back · status → `["make","status"]` — the pid + the port, both labeled · restart → `["make","restart", +overrides]` — the refusal then the answer (both prerequisites' read-backs) · log → the tail verbatim, the window labeled (the last N of M lines — the budget named) · output → the body verbatim, the HTTP status named · help → the usage. The PORT/HOST overrides render the Makefile's own `?=` grammar as make variable assignments — the operator's override surface, never re-implemented. Exit codes: make's own, passed through (the recipes' ThreePart refusals ride exit 1; formatOutput renders them whole).
**THE EXACT BYTES — THE COMPLETE NEW FILE (FR-MEM-0011's bytes-at-synthesis doctrine; lint.ts's form grown to six ops; node builtins + fetch only — no Bun global in THIS file, the _run import the one channel):**

```ts
// prioritree-owned (2026-11-22, G-LIFECYCLESPEC-BRIEF's extension — Q-ux-surface R12/R13): the member-callable lifecycle surface; hand-maintained in prioritree's tree (lint.ts's standing form)
//
// Purpose: the lifecycle act — the members call the service's runtime directly (R12): the transitions (start/stop/status/restart) subprocess make through the _run.ts explicit-argv channel (the Makefile's recipes the ONE implementation; this wrapper the argv shim); the READ verbs are pure reads (R13): log — the server log's bounded tail (.prioritree/server.log, default the last 100 lines); output — the service's live answer, the RUN-9999 probe's response body rendered verbatim. Every op's output renders verbatim, never summarized.
// Refuses when: log finds .prioritree/server.log absent (the honest never-started report); output finds the port refused (the honest down report); the transitions refuse per the recipes' own guards — the exit codes pass through, never swallowed. NOT a shell, NOT a server manager beyond the ruled verbs: the four transitions + the two reads only.
// Re-run: the reads are pure (idempotent); the transitions idempotent per the recipes' own guards (start refuses on a live pid; stop exits 0 on the absent pidfile); the wrapper's verification is kensho's live run through the wrapper itself (validate/lifecycle — the registration + the verbs' read-backs; no pytest arc).
// Touches: nothing of its own — the recipes' writes (.prioritree/) are the only mutations; the read verbs never mutate (R13: the log is evidence, not state).
// Provenance: Q-ux-surface R12/R13 (2026-11-22, the collaborator's two rulings); the lifecyclespec extension (togo, packet synthesize/lifecyclespec); FR-MEM-0025 (the RUN-9999 context-free probe); lint.ts the wrapper precedent; _run.ts the explicit-argv channel.
import { tool } from "@opencode-ai/plugin"
import { readFileSync } from "node:fs"
import { join } from "node:path"
import { runArgv } from "./_run"

function formatOutput(result: {
  exitCode: number
  text(): string
  stderr: Buffer | string
}): string {
  const stdout = result.text()
  const stderr = result.stderr.toString()
  if (result.exitCode === 0) {
    return stdout.trim() || "Done."
  }
  if (stderr.trim()) {
    return `${stdout}${stdout.trim() ? "\n" : ""}stderr:\n${stderr}`.trim()
  }
  return stdout.trim() || `Exited with code ${result.exitCode} (no output captured).`
}

export default tool({
  description: "Lifecycle — the member-callable service-management surface: the transitions (start/stop/status/restart) over the host Makefile's targets via the explicit-argv runArgv channel (one implementation: the recipes; this wrapper the argv shim), plus the READ verbs (log — the server log's bounded tail, default 100; output — the service's live answer, the RUN-9999 probe's body verbatim). The reads are read-only; every op's output renders verbatim, never summarized. Host-only (no Docker, no worktrees); no shell.",
  args: {
    operation: tool.schema
      .enum(["start", "stop", "status", "restart", "log", "output"])
      .or(tool.schema.literal("help"))
      .describe("Operation to perform (use \"help\" to print this tool's usage)"),
    port: tool.schema.string().optional().describe("The service's port — appended as the make override PORT=<n> on the transitions (default 8000, the Makefile's own ?=); the probe's target on output"),
    host: tool.schema.string().optional().describe("The service's bind host — appended as the make override HOST=<h> on the transitions (default 127.0.0.1, the Makefile's own ?=); the probe's target on output"),
    tail: tool.schema.string().optional().describe("The log tail's line count (the log op only; default 100 — R13's bounded-tail discipline)"),
  },
  async execute(args, context) {
    const makeTarget = (target: string): string[] => {
      const argv = ["make", target]
      if (args.port) argv.push(`PORT=${args.port}`)
      if (args.host) argv.push(`HOST=${args.host}`)
      return argv
    }
    switch (args.operation) {
      case "start": {
        return formatOutput(await runArgv(makeTarget("start"), { cwd: context.directory }))
      }
      case "stop": {
        return formatOutput(await runArgv(makeTarget("stop"), { cwd: context.directory }))
      }
      case "status": {
        return formatOutput(await runArgv(makeTarget("status"), { cwd: context.directory }))
      }
      case "restart": {
        return formatOutput(await runArgv(makeTarget("restart"), { cwd: context.directory }))
      }
      case "log": {
        const path = join(context.directory, ".prioritree", "server.log")
        let text: string
        try {
          text = readFileSync(path, "utf8")
        } catch {
          return "log refused — Expected: .prioritree/server.log (the server's log, present after a start)\nFound: the file absent (the server has never been started)\nNext-action: lifecycle start first, or read the runtime state with lifecycle status"
        }
        const lines = text.split("\n")
        const parsed = args.tail ? Number.parseInt(args.tail, 10) : 100
        const n = Number.isFinite(parsed) && parsed > 0 ? parsed : 100
        const shown = lines.slice(-n).join("\n")
        return `log — ${path} (the last ${Math.min(n, lines.length)} of ${lines.length} lines; the bounded tail is the discipline — a full-file read is a budget question)\n${shown}`
      }
      case "output": {
        const host = args.host ?? "127.0.0.1"
        const port = args.port ?? "8000"
        const url = `http://${host}:${port}/runs/RUN-9999/next`
        try {
          const res = await fetch(url, { signal: AbortSignal.timeout(5000) })
          const body = await res.text()
          return `output — ${url} answered HTTP ${res.status} (the body verbatim):\n${body}`
        } catch (error) {
          const message = error instanceof Error ? error.message : String(error)
          return `output refused — Expected: the service answering on ${url} (the RUN-9999 probe — the honest ThreePart refusal proving the chain)\nFound: the connection refused (${message} — the server is down)\nNext-action: lifecycle start, or read the runtime state with lifecycle status`
        }
      }
      case "help": {
        return "lifecycle — the member-callable service-management surface (the transitions subprocess make — the recipes the one implementation; the reads pure).\n\nOperations:\n  start  [make start (+ PORT=/HOST= overrides)]\n    Start the server in the background; the read-back: the port answers (the RUN-9999 honest 404; 000 = still booting)\n  stop  [make stop]\n    SIGTERM + the bounded drain; the read-back: the refusal (the port down)\n  status  [make status]\n    The pid + the port, both labeled, read-only\n  restart  [make restart (+ PORT=/HOST= overrides)]\n    Stop then start: the refusal then the answer\n  log  [read .prioritree/server.log]\n    The server log's bounded tail (default the last 100 lines; tail=<n> overrides)\n  output  [probe http://127.0.0.1:8000/runs/RUN-9999/next]\n    The service's live answer — the response body verbatim"
      }
    }
    return `Unknown operation: ${args.operation}`
  },
})
```

## §E3 THE GRANT MAP RULED (R12's three + R13's candidates; the minimum-grant principle — every grant carries its citation, no cited need no grant)
| Seat | Verbs granted | The reason (the citation) |
|---|---|---|
| jikko | ALL SIX (start/stop/status/restart/log/output) | THE BUILD FLOOR (R12's named grant): the lifecycle unit's own executor — the floor's live read-backs (G-LIFECYCLE condition 2, the targets-green step), the boot-diagnosis reads when a start fails; FR-MEM-0024's cure-class — the execution seat's needed acts all routed, never discovered at execution time |
| kensho | ALL SIX | THE VERIFICATION (R12's named grant): G-LIFECYCLE conditions 2+3 — the independent re-run SELF-SUFFICIENT, the live evidence a member's own act; the reads are the evidence channels (the artifact contract: outputs verbatim — the log + the answer body are the runtime's word) |
| shinko | ALL SIX | THE COORDINATION (R12's named grant): the convenor's live-sequence hand (the first spec's own form — "the make verb rides the coordinator's hand", now the wrapper's act) + the position reads at dispatch time |
| shindan | READ THREE (status/log/output) — NEVER the transitions | THE DIAGNOSTIC EYE (R13's candidate, GRANTED read-only): the state + the history + the chain's own words; status is read-only by construction (brief §3i); an analysis seat never mutates the runtime — the competency boundary |
| rikai | READ THREE (status/log/output) — NEVER the transitions | THE MECHANISM'S TRACE (R13's candidate, GRANTED read-only): the log IS the mechanism's own record (the request channel, the drain lines), the body IS the refusal mechanism's text; same boundary |
| ALL OTHERS (tansa, suisen, keisan, hyoka, moho, togo, keikaku, hansei) | DENIED — the closed-world deny lines | No ruled need on the record (the minimum-grant principle); the static surfaces already serve the read/grep instruments; togo read-only by design and never acts on what it synthesizes |
THE LANDING FORM (per §E1): the adapter rows at hikari's prioritree-seats.yaml (the five seats' pack rows — the full-six row at jikko/kensho/shinko, the read-three row at shindan/rikai) + the universe entry (lifecycle, 26→27); the regen lands opencode.json's five allow-rows + eight deny-lines + the five seat prompts' Pack Routing rows (kensho.md:31's own form: `| lifecycle | start, stop, status, restart, log, output |` / the read-three row); the siblings re-byte + their --check legs.

## §E4 FR-MEM-0025'S CURE — THE RUN-9999 PROBE FLIP (the context-free 404-as-ready; four byte-sites, one token each: RUN-0001 → RUN-9999, same length, a clean swap)
- **:31 (start's read-back probe):** `...http://127.0.0.1:$(PORT)/runs/RUN-0001/next || true` → `RUN-9999` — start's read-back now reads the honest 404 at ANY root, ANY store state (the real root's RUN-0001 serves its REAL pair at 200 — the mislabeled-healthy defect dead).
- **:52 (stop's refusal read-back — the stop/restart probes' form-consistency):** `@curl -s -o /dev/null http://127.0.0.1:$(PORT)/runs/RUN-0001/next && echo ...` → `RUN-9999` (restart rides stop+start's own probes — no fifth site).
- **:61 (status's port verdict):** `@code=$$(curl -s -o /dev/null -w '%{http_code}' http://127.0.0.1:$(PORT)/runs/RUN-0001/next); \` → `RUN-9999`.
- **:62 (status's message path string):** `echo "port: $(PORT) answering (HTTP 404 on /runs/RUN-0001/next; the ready form)"` → `RUN-9999`.
**THE WRAPPER'S OWN VERIFICATION FORMS: NONE — the DRY ruling's dividend.** The wrapper carries zero probe forms of its own (the read-backs ride the recipes; the wrapper's output = the recipe's own read-back, verbatim); its `output` verb probes RUN-9999 BY DESIGN — the context-free form born into the member surface. The flip lands ONCE, in the Makefile, and every surface (the operator's shell, the members' wrapper, kensho's verification) reads it through the one implementation.

## §E5 THE TEST QUESTION RULED — NO PYTEST ARC; THE WRAPPER'S TEST IS KENSHO'S LIVE RUN THROUGH THE WRAPPER ITSELF
The brief §4's zero-test ruling EXTENDS to the wrapper, the four reasons carrying over: (1) the acceptance harness (tests/test_service_acceptance.py) already proves the boot mechanism live (Popen, the sibling uvicorn, the scratch cwd, wait(5) — the tree's live-boot precedent, untouched and green); (2) the wrapper adds ZERO mechanism — the argv shim over the ruled recipes + two pure reads; (3) a pytest arc over the wrapper would be a test-of-the-shim — brittle to the TS bytes, needing bun/opencode runtime inside pytest, proving nothing the live run does not prove more honestly (the run IS the evidence — the verification seat's own contract); (4) the floor rides untouched (zero Python touched — the floor re-run a no-op formality at step 4). THE STATIC CHECK: the per-file tsc lane (the wrappers' own recorded discipline, _run.ts:5), executed at the collaborator's hand — `bunx tsc --noEmit --strict --target ES2022 --module ESNext --moduleResolution bundler --skipLibCheck --allowImportingTsExtensions --types node .opencode/tools/lifecycle.ts` (the flags mirrored from .opencode/tsconfig.json:19-29; no seat carries a tsc act — the instrument gap named honestly, FR-MEM-0024's form); the tsconfig's own comment names the family caveat (tools/ references Bun globals via _run — the lane's Bun-family errors there are the known class, which is why the file at hand carries node builtins + fetch only). THE AUTHORITATIVE VERDICT: the LIVE REGISTRATION — opencode auto-discovers and loads .opencode/tools/*.ts at session start; a wrapper that fails to parse fails the registration loudly — and kensho's step-4 run through the wrapper IS the test (the proof by use — the tool-grants unit's own form: "the live proof rides the first gate, where kensho fires the tool in verification").

## §E6 THE PER-STEP DISPATCH PLAN (R8) — ONE STEP, ONE DISPATCH, ONE BOUNDED RETURN
**STEP 1/4 — THE PROBE FLIP (jikko; one patch).** The Makefile's four byte-sites (:31, :52, :61, :62), RUN-0001 → RUN-9999 each; NOTHING else. READ-BACK: the four lines re-read verbatim; `grep -c RUN-0001 Makefile` = 0, `grep -c RUN-9999 Makefile` = 4. FILE THE STEP REPORT (R11). RETURN ≤8 lines.
**STEP 2/4 — THE WRAPPER'S LANDING (jikko; one patch create).** §E2's fence WHOLE — the complete file at .opencode/tools/lifecycle.ts, byte-exact. READ-BACK: the file re-read whole vs the fence; the tsc lane at the collaborator's hand (§E5's command — named in the step's dispatch as the collaborator's check, no seat act). FILE THE STEP REPORT (R11). RETURN ≤8 lines.
**STEP 3/4 — THE GRANT'S LANDING (one step, two hands, named).** THE SEAT'S PART (jikko through hikari's shinko-git choreography — the tool-grants unit's own precedent, patch's root override): the adapter rows at hikari's prioritree-seats.yaml (§E3's five rows) + the universe entry (lifecycle, 26→27). THE COLLABORATOR'S PART (the human shell — the regen and the restart are the operator's acts): `uv run python scripts/generation/clarity_scaffold.py --target prioritree` (+ the clarity/input re-emits, the sibling re-byte) → the --check legs PASS; then THE RESTART (§E1's operational note). READ-BACK: opencode.json's five allow-rows + eight deny-lines; the five seat prompts' pack rows; the --check legs. FILE THE STEP REPORT (R11). RETURN ≤10 lines.
**STEP 4/4 — THE VERIFICATION (kensho; FROM A POST-RESTART SESSION; the packet validate/lifecycle — G-LIFECYCLE condition 3's independent leg, now SELF-SUFFICIENT).** The live sequence THROUGH THE WRAPPER: lifecycle start → the read-back (the port answers — the RUN-9999 honest 404 at the REAL root, the context-free form proven where FR-MEM-0025 broke) · lifecycle status → the pid + the port · lifecycle log → the tail (the boot banner, the request channel) · lifecycle output → the body verbatim (the ThreePart refusal's own words) · lifecycle restart → the refusal then the answer · lifecycle stop → the refusal. Each output VERBATIM in the report (the artifact contract). Plus the floor (the test + lint acts: 156 passed, All checks passed!, 0/0). FILE THE STEP REPORT (R11). RETURN ≤15 lines.
**THE COMMIT — the coordinator's hand (shinko's git land, the tree's own instrument):** ONE commit at the unit's close covering the extension's files (the Makefile flip + lifecycle.ts + the regen's grant artifacts); proposed message: `the lifecycle extension: the member-callable surface (lifecycle.ts + the grants); the RUN-9999 probe flip`.

## §E7 THE GATE'S MAPPING + THE TRADE-OFF CARRIED
**G-LIFECYCLESPEC-BRIEF (re-presented; this extension + the landed first spec = the amended whole):** (1) "every target's exact recipe bytes, every read-back named, the per-step dispatch plan (R8) whole" → the first spec's fence STANDS (landed, live-proven); the extension carries the amended bytes (§E2's fence, §E4's four sites) + the read-backs (§E2's verb table) + §E6's plan whole. (2) "the ruled target set with the handed constraints verbatim" → UNTOUCHED (the four-target set + 127.0.0.1/the port/single-worker/the cwd discipline all stand; the extension ADDS the member surface per R12/R13, never re-opens the ruled set). (3) "the collaborator approves — the build dispatches fire only after" → this re-presentation IS the ask; §E6's steps fire at the approval.
**G-LIFECYCLE (the unit's close, the extension inside it):** condition 2 ("the targets green live") → the live sequence now rides the wrapper AT KENSHO'S HAND (step 4 — R12's cure: the blocked condition unblocked, the evidence a member's own act; the collaborator's-shell run stands as the pre-grant record); condition 3 ("the floor green; kensho's independent re-run") → step 4's floor + the wrapper-borne sequence; condition 1 (the exact-task law) → the flip + the wrapper land per THIS spec's bytes.
**THE TRADE-OFF THE PLAN CARRIES (named):** (1) the grant's landing depends on the cross-tree hand (the hikari adapter + the regen + the siblings' re-byte + the restart) — the unit's close is hostage to a non-seat window; the wrapper may sit on disk UNROUTED until the regen fires (harmless by the closed-world deny: discoverable, never callable — the drift window named, never hidden); (2) FR-MEM-0014's delivery-at-the-launch: post-landing live sessions stay grant-blind until the restart — the named expected state; (3) the `output` verb's ruling (the live-answer body reading of R13's "the output verbatim") carries interpretive risk — the alternatives priced at §E2, the gate's approval the settle; (4) the universe growth 26→27 re-bytes the sibling trees — the closed world's price, paid under either landing form.
