<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/lifecycleintegration-spec

**Route:** prioritree-mcp (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T18:02:37Z |
| 2 | report | togo | 2026-11-23T18:25:22Z |
## Reported by togo — 2026-11-23T18:25:22Z

# TOGO — synthesize/lifecycleintegration-spec — THE EXACT-TASK SPEC (2026-11-23; the lifecycle-integration unit's build bytes, closing G-LIFECYCLEINTEGSPEC-BRIEF at the collaborator's approval)

## §0 THE GROUND, READ + CITED (every fact traces to disk)
- THE APPROVED BRIEF: reports/synthesize/lifecycleintegration.md (G-LIFECYCLEINTEGRATION-BRIEF approved) — the five surfaces (§1(a)-(f)); the ruled mechanisms (§2.1 the 8100 default; §2.2 the recipes + the direct-sibling invocation form; §2.3 env -u WEB_CONCURRENCY + the flock truth; §2.4 the /mcp probe RULED [-m 2 bound; the /healthz candidate refuted at the census; the ready code named at the first live fire]; §2.5 the ceremony's numbers); the test ruling (§3: ZERO arcs the targets, ONE arc the src region); the handoff's opens (§5); the trade-off + the four opens (§6).
- THE STANDING MAKEFILE WHOLE (Makefile:1-70, THE MIRROR'S SOURCE): PORT ?= 8000 (:3), HOST ?= 127.0.0.1 (:4), the .PHONY row (:6); start (:20-31 — the live-pid guard :21-24, the binary guard :25-28, mkdir :29, the nohup + pid capture :30, the sleep-1 read-back :31); stop (:33-52 — the absent-pidfile exit-0 :34, the stale cure :35-40, SIGTERM + the 5s drain :41-45, the still-live refusal :46-49, the read-back :52); status (:54-65 — pid :55-60, port :61-65); restart (:67, composed stop start); help (:69-70, the grep + awk — the ## form auto-lists).
- THE SRC REGION (src/prioritree/mcp_server.py): :27 `import sys` — grep-verified the module's ONLY sys use is :573 (the widening retires it; the zero-findings bar: the import swaps to argparse, never left dead); :571-576 main() (:572 the docstring line; :573-574 the hardcoded forms — host="127.0.0.1", port=8000, allowed_hosts=["127.0.0.1", "localhost"], allowed_origins=[]; :575-576 the bare stdio branch); :19-22 the module docstring (untouched — it names no port); :580 the __main__ form (untouched).
- THE TEST HOME (tests/test_mcp_server_face.py:1-635): the fixture forms (:139-142 — monkeypatch.setattr, the object + string-name family); the string-form precedent (tests/test_cli.py:165); the parametrize form (tests/test_cli.py:128-135 — the tuple-names + pytest.param id form); the tail (:601-635 — test_re_tally_after_cure the last function, the file ends :635 — the arc's insertion neighborhood); the tests' ruled ignores (pyproject.toml:50 — S101/PLR2004).
- THE README (README.md): :107 (the serve URL's port), :110 (the port note), :164 (the collision bullet), :183 (the tool lane's parenthetical) — the four re-ruled lines.
- THE FLOORS + THE GATES: ruff line-length 120, select ALL (pyproject.toml:33-43), the mcp_server.py D205 ruling (:145), pyright strict (:161-175); G-LIFECYCLEINTEGSPEC-BRIEF (junro.json:300-307) + G-LIFECYCLEINTEGRATION (:308-315) read at the store; .gitignore:184 `.prioritree/` — the new pid/log homes ride the ignored tool-home (no ignore line needed).

## §1 THE MAKEFILE'S REGION (file-unit 1) — the diff ADDITIONS ONLY over the web bytes (the one touched line: the .PHONY row, extended)

THE HEAD BLOCK — :3-4 stand byte-untouched; MCP_PORT/MCP_HOST INSERTED beside PORT/HOST; the .PHONY row's four names appended (the one touched line):

```make
PORT ?= 8000
HOST ?= 127.0.0.1
MCP_PORT ?= 8100
MCP_HOST ?= 127.0.0.1

.PHONY: dev test lint typecheck help start stop status restart mcp-start mcp-stop mcp-status mcp-restart
```

THE FOUR TARGETS — the block INSERTED between :67 (restart) and :69 (help); every recipe line TAB-indented (make's law — the fence's leading whitespace IS the byte); the recipes mirror the standing forms whole (the messages in the tree's refusal grammar: "refused: expected X, found Y; next-action: Z"):

```make
mcp-start: ## Start the MCP server in the background (run from the repo root; pid -> .prioritree/mcp-server.pid; override: make mcp-start MCP_PORT=<other>)
	@if [ -f .prioritree/mcp-server.pid ] && kill -0 $$(cat .prioritree/mcp-server.pid) 2>/dev/null; then \
		echo "mcp-start refused: expected no live pid, found pid $$(cat .prioritree/mcp-server.pid) live (the MCP server is running); next-action: make mcp-status, or make mcp-stop"; \
		exit 1; \
	fi
	@if [ ! -x .venv/bin/python ]; then \
		echo "mcp-start refused: expected .venv/bin/python, found it absent (no venv yet); next-action: make dev (uv sync) first"; \
		exit 1; \
	fi
	@mkdir -p .prioritree
	@nohup env -u WEB_CONCURRENCY .venv/bin/python -m prioritree.mcp_server --serve --host $(MCP_HOST) --port $(MCP_PORT) > .prioritree/mcp-server.log 2>&1 & echo $$! > .prioritree/mcp-server.pid
	@sleep 1; code=$$(curl -s -o /dev/null -w '%{http_code}' -m 2 http://127.0.0.1:$(MCP_PORT)/mcp || true); echo "read-back: HTTP $$code on http://127.0.0.1:$(MCP_PORT)/mcp (200 or 405 = answering, the ready code byte-named at the first live fire; 000 = still booting: make mcp-status)"

mcp-stop:  ## Stop the MCP server: SIGTERM + the bounded drain (pid read from .prioritree/mcp-server.pid; run from the repo root)
	@if [ ! -f .prioritree/mcp-server.pid ]; then echo "mcp-stop: no pidfile; nothing managed (already down)"; exit 0; fi
	@pid=$$(cat .prioritree/mcp-server.pid); \
	if ! kill -0 $$pid 2>/dev/null; then \
		echo "mcp-stop refused: expected a live pid, found pid $$pid dead (stale pidfile); next-action: the stale pidfile is removed; make mcp-start launches fresh"; \
		rm -f .prioritree/mcp-server.pid; \
		exit 1; \
	fi; \
	echo "SIGTERM -> pid $$pid (the graceful drain)"; \
	kill $$pid; \
	i=0; \
	while kill -0 $$pid 2>/dev/null && [ $$i -lt 5 ]; do sleep 1; i=$$((i + 1)); done; \
	rm -f .prioritree/mcp-server.pid; \
	if kill -0 $$pid 2>/dev/null; then \
		echo "mcp-stop incomplete: expected the pid gone by the 5s bound, found pid $$pid still live; next-action: make mcp-status, or kill -9 $$pid"; \
		exit 1; \
	else \
		echo "stopped: pid $$pid gone (the pidfile is removed)"; \
	fi
	@code=$$(curl -s -o /dev/null -w '%{http_code}' -m 2 http://127.0.0.1:$(MCP_PORT)/mcp); \
	if [ "$$code" = "000" ]; then echo "read-back: refused on $(MCP_PORT) - the port is down"; \
	else echo "read-back: STILL ANSWERING on $(MCP_PORT) (HTTP $$code); another (unmanaged) server holds the port"; \
	fi

mcp-status: ## Report the MCP server's pid and port, both labeled, read-only (run from the repo root)
	@if [ -f .prioritree/mcp-server.pid ]; then \
		pid=$$(cat .prioritree/mcp-server.pid); \
		if kill -0 $$pid 2>/dev/null; then echo "pid: $$pid (live)"; else echo "pid: $$pid (dead; stale pidfile; next-action: make mcp-stop cures it)"; fi; \
	else \
		echo "pid: none (no pidfile; not managed)"; \
	fi
	@code=$$(curl -s -o /dev/null -w '%{http_code}' -m 2 http://127.0.0.1:$(MCP_PORT)/mcp); \
	if [ "$$code" = "200" ] || [ "$$code" = "405" ]; then echo "port: $(MCP_PORT) answering (HTTP $$code on /mcp; the ready form)"; \
	elif [ "$$code" = "000" ]; then echo "port: $(MCP_PORT) refused (down)"; \
	else echo "port: $(MCP_PORT) answered HTTP $$code (unexpected; not the ready form)"; \
	fi

mcp-restart: mcp-stop mcp-start ## Stop then start: the operator's rebind (run from the repo root; the read-backs ride both prerequisites)
```

THE MECHANISMS, NAMED (the brief §2 mirrored): the live-pid guard against .prioritree/mcp-server.pid — DISTINCT from the web's server.pid (the collision cured at the file level); the binary guard .venv/bin/python (the recipe's own binary, the module form's launcher, the dev-first message); mkdir -p .prioritree (the ignored home, idempotent); THE LAUNCH LINE (the ruled bytes: env -u WEB_CONCURRENCY [the single-worker discipline carried — FastMCP's http runner rides uvicorn beneath; the unset conservative: inert if unheeded], the direct sibling binary [never `uv run`'s wrapper pid between the kill and the drain], the module form, the log home .prioritree/mcp-server.log, the pid capture); THE SLEEP-1 READ-BACK (the /mcp probe: `curl -s -o /dev/null -w '%{http_code}' -m 2 http://127.0.0.1:$(MCP_PORT)/mcp` — the -m 2 bound RULED [the streamable endpoint may hold a GET stream open; the recipe never hangs on a healthy server]; the || true form [the read-back informational — the target stays green at 000]; the ready code named as the first-live-fire's datum); MCP-STOP'S GRAMMAR (the absent-pidfile exit-0; the stale-pidfile cure; SIGTERM + the 5s drain bound + the pidfile rm; the still-live refusal with the kill -9 next-action; the refusal read-back in the CODE form — 000 = the port down, any HTTP code = still answering, an unmanaged holder [curl's exit status is unreliable under -m 2 on a streaming endpoint; the code is the truth — the brief §2.2's own 000-form]); MCP-STATUS (the pid labeled live/dead/no-pidfile + the port labeled answering/refused/unexpected — the standing three-way grammar, read-only); MCP-RESTART (composed mcp-stop mcp-start, zero new mechanism).

THE FIRST-LIVE-FIRE CLAUSE (the brief §2.4; the RUN-9999 lesson, FR-MEM-0025): the ready code's exact value — 200 the stream / 405 the method refusal, the brief's own candidate pair, either proving the chain — is BYTE-NAMED at the build's FIRST LIVE FIRE (plan step 6): the observed code byte-matches into mcp-start's read-back message and mcp-status's ready-case (the candidate pair collapsing to the observed truth); the unexpected-code verdict labeled honestly at mcp-status. A probe's premise verified live, never assumed.

## §2 THE SRC REGION (file-unit 2) — main()'s widening; the ONE region touched

THE IMPORT SWAP (:27) — grep-verified sys's only use is :573; the parse retires it; an unused import fails ruff F401 (the zero-findings bar). BEFORE (:25-28):

```python
from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Final, Literal, get_args
```

AFTER:

```python
from __future__ import annotations

import argparse
from typing import TYPE_CHECKING, Final, Literal, get_args
```

main() BEFORE (:571-576, the file's current bytes):

```python
def main() -> None:
    """Run the server -- bare stdio, --serve the shared HTTP form."""
    if "--serve" in sys.argv[1:]:
        server.run("http", host="127.0.0.1", port=8000, allowed_hosts=["127.0.0.1", "localhost"], allowed_origins=[])
    else:
        server.run("stdio")
```

main() AFTER (the widened bytes; the docstring line widened to name the defaults — the module docstring untouched, it names no port):

```python
def main() -> None:
    """Run the server -- bare stdio, --serve the shared HTTP form (defaults: --host 127.0.0.1, --port 8100)."""
    parser = argparse.ArgumentParser(prog="prioritree.mcp_server")
    parser.add_argument("--serve", action="store_true", help="the shared streamable-HTTP form (default: stdio)")
    parser.add_argument("--host", default="127.0.0.1", help="the HTTP bind host (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=8100, help="the HTTP bind port (default: 8100)")
    args = parser.parse_args()
    if args.serve:
        allowed_hosts = ["127.0.0.1", "localhost"]
        if args.host not in allowed_hosts:
            allowed_hosts = [*allowed_hosts, args.host]
        server.run("http", host=args.host, port=args.port, allowed_hosts=allowed_hosts, allowed_origins=[])
    else:
        server.run("stdio")
```

THE BEHAVIORS, NAMED: (1) THE BARE FORM BYTE-HELD — argv [] parses to serve=False; the flow reaches the BYTE-IDENTICAL `server.run("stdio")` line (the diff shows the line untouched); no flags consumed, no HTTP-form call (the dispatch's bracket — stdio, no flags, no server.run — read: the http-form run call never reached bare; the member path byte-preserved per the brief §1(e)). (2) THE --SERVE FLOW — the current hardcoded forms replaced by the parsed values: host=args.host, port=args.port; the 8100 default the widening; the flags teach at --help (the brief's reason 3; the make variable → the flag, ONE mapping). (3) THE ALLOWED DERIVATION — allowed_hosts the loopback pair at the default; the --host value JOINS the list when it differs (a non-loopback bind whose own host is unallowed is a silent Host-header 400 — the widening honest at the seam it opens); allowed_origins [] unchanged (no browser form this era). (4) ARGPARSE'S STRICTNESS, NAMED NEVER SILENT — unknown flags now refuse at the parser (argparse's usage + exit 2, cli.py's own channel), never a silent stdio fall-through; the member path (the MCP host's bare spawn, zero flags) unaffected by construction. (5) The __main__ form (:579-580) untouched.

## §3 THE TEST ARC (file-unit 3) — the ONE ruled Python arc (the brief §3); the targets themselves carry ZERO arcs (the ux era's lifecycle precedent — the recipes are shell, the suite has no seam on them; the verification the gate's live read-backs)

THE INSERTION NEIGHBORHOOD: the file's TAIL, after test_re_tally_after_cure (the last function, ending :635), the file's two-blank-line separation. NO import changes — the arc is self-contained (sys.argv via monkeypatch's string form, the tree's own precedent at tests/test_cli.py:165). The arc's whole bytes:

```python
@pytest.mark.parametrize(
    ("argv", "expected"),
    [
        pytest.param([], (("stdio",), {}), id="bare-stdio"),
        pytest.param(
            ["--serve"],
            (
                ("http",),
                {
                    "host": "127.0.0.1",
                    "port": 8100,
                    "allowed_hosts": ["127.0.0.1", "localhost"],
                    "allowed_origins": [],
                },
            ),
            id="serve-defaults",
        ),
        pytest.param(
            ["--serve", "--host", "0.0.0.0", "--port", "9000"],
            (
                ("http",),
                {
                    "host": "0.0.0.0",
                    "port": 9000,
                    "allowed_hosts": ["127.0.0.1", "localhost", "0.0.0.0"],
                    "allowed_origins": [],
                },
            ),
            id="serve-overrides",
        ),
    ],
)
def test_parse_argv_derives_the_run_call(
    argv: list[str], expected: tuple[tuple[str, ...], dict[str, object]], monkeypatch: pytest.MonkeyPatch
) -> None:
    """Parse main()'s argv form => the derived server.run call whole, the three forms parametrized.

    The lifecycle-integration arc (the brief §3, the one ruled Python arc):
    the argv widening is new branch logic with a changed default -- the bare
    form the member path byte-held (server.run("stdio"), no HTTP-form call,
    no kwargs); --serve alone the defaults (127.0.0.1:8100, the loopback
    pair); the overrides flowed and the host JOINED to allowed_hosts (a
    non-loopback bind unallowed is a silent Host-header 400). The run call
    captured per the file's fixture forms (monkeypatch's setattr; sys.argv
    via the string form, the tree's own precedent); the store never touched
    -- the parse is pure.
    """
    calls: list[tuple[tuple[str, ...], dict[str, object]]] = []

    def record(*args: str, **kwargs: object) -> None:
        """Record the derived run call's whole argument shape -- the assertion's ground."""
        calls.append((args, kwargs))

    monkeypatch.setattr("sys.argv", ["prioritree.mcp_server", *argv])
    monkeypatch.setattr(mcp_server.server, "run", record)
    mcp_server.main()
    assert calls == [expected]
```

THE ARC'S ASSERTIONS (the three forms): bare [] → the captured call (("stdio",), {}) — the stdio flow, NO HTTP-form call, no kwargs (the member path byte-held at the arc's own level); ["--serve"] → ("http",) + the defaults (host 127.0.0.1, port 8100, allowed_hosts the loopback pair, allowed_origins []); ["--serve", "--host", "0.0.0.0", "--port", "9000"] → the overrides flowed (host 0.0.0.0, port 9000) and the host JOINED (["127.0.0.1", "localhost", "0.0.0.0"]). The capture per the file's fixture forms (monkeypatch.setattr; server.run mocked — the store never touched, the parse pure).

THE FLOOR: the suite grown by the arc's three parametrized forms — 200 + 3 = 203 PREDICTED here, MEASURED at the build's floor run (never asserted as fact here; the grown number rides the build's report; kensho's re-run reads it back fresh-process).

## §4 THE README'S LINES (file-unit 4) — the four re-ruled lines, before/after

:107 — BEFORE: `# streamable-HTTP at http://127.0.0.1:8000` rides the --serve console line; AFTER (the line's whole form):

```console
$ uv run python -m prioritree.mcp_server --serve    # streamable-HTTP at http://127.0.0.1:8100
```

:110 — BEFORE: "Port note: `--serve` hardcodes port 8000 — the same default as `make start`; run one at a time, or start the web tier with `make start PORT=<other>`."; AFTER:

```markdown
Port note: `--serve` defaults to port 8100 (`--host`/`--port` override); the web tier keeps 8000, so both servers co-run at their defaults — the collision is retired. The MCP's lifecycle targets: `make mcp-start`, `make mcp-stop`, `make mcp-status`, `make mcp-restart` (`MCP_PORT ?= 8100`, `MCP_HOST ?= 127.0.0.1`).
```

:164 — BEFORE: "- **The port collision.** `make start` and `mcp_server --serve` both default to port 8000 — run one at a time, or override (`make start PORT=8100`)."; AFTER:

```markdown
- **The port discipline.** The web tier (`make start`) defaults to port 8000; the MCP (`--serve`) defaults to 8100 — both servers co-run at their defaults, the collision retired (the MCP's lifecycle: `make mcp-start` / `make mcp-stop` / `make mcp-status` / `make mcp-restart`).
```

:183 — BEFORE (the sentence's tail): "... or the same command with `--serve` (port 8000 — one at a time with the web)."; AFTER (the sentence's whole form):

```markdown
The MCP rides the same install: `$(uv tool dir)/prioritree/bin/python -m prioritree.mcp_server` for stdio, or the same command with `--serve` (port 8100 — co-runnable with the web's 8000).
```

## §5 THE NO-BREAK PROOFS (the gate's condition 1's own evidence)
1. THE WEB TARGETS BYTE-UNTOUCHED: start (:20-31), stop (:33-52), status (:54-65), restart (:67), PORT/HOST (:3-4), help (:69-70) — the four standing recipes identical; the diff over the Makefile: the two variable lines + the targets block ADDED, the .PHONY row EXTENDED (the one touched line, the four names appended); provable at the build's git-diff read-back (zero changed lines in the web region).
2. THE BARE FORM BYTE-PRESERVED: the diff over mcp_server.py shows the import swap (:27) + main()'s widening — the `server.run("stdio")` line byte-identical, the module docstring untouched, the __main__ form untouched; the member path (stdio per session) byte-held; the diff shows only the --serve flow's widening.
3. THE FLOOR GROWN: 203 predicted (200 + 3), MEASURED at the build's floor run; kensho's independent re-run green (validate/lifecycleintegration).
4. THE FLOCK SEAM'S GUARANTEE: both servers are writers on ONE store (the web's Serialize verbs + the MCP's _seam, one STORE_HOME, CWD-relative) — the machine-wide flock (store_lock.Lock, composed by every writer tier, G-MCPSERVER's own green) serializes every whole store act across BOTH processes: the co-runnability's store-side guarantee held by construction, not convention (the brief §2.3, F1's seam).

## §6 THE PER-STEP PLAN (R8, the file-unit law — one file per step, each with its own read-back; the whole rides build/lifecycleintegration's steps: build jikjo + targets-green make)
1. THE MAKEFILE (§1) — read-back: `make help` lists the four (the grep auto-lists); `make mcp-status` labels both fields read-only; the git diff shows the web recipes byte-identical.
2. THE SRC REGION (§2) — read-back: `.venv/bin/python -m prioritree.mcp_server --help` teaches the three flags with the defaults; `make lint` + `make typecheck` clean (the zero-findings bar).
3. THE TEST ARC (§3) — read-back: `uv run pytest tests/test_mcp_server_face.py` green, the three forms.
4. THE README'S LINES (§4) — read-back: the four lines read current (the 8100 default, the four targets, the co-run, the collision retired).
5. THE FLOOR — `uv run pytest` whole: the grown count measured (203 predicted); `make lint` + `make typecheck` clean.
6. THE LIVE LEGS — kensho's validate/lifecycleintegration (the zero-trust re-run) + the targets' own runs: `make mcp-start` (the read-back answering — THE FIRST LIVE FIRE, the ready code byte-matched per §1's clause); `make mcp-status` (the pid + the port labeled); `make mcp-stop` (the refusal read-back: the port down); BOTH servers co-live at their defaults (`make start` + `make mcp-start`: the web at 8000 answering, the MCP at 8100 answering — the collision check); the teardown (`make mcp-stop`, `make stop`).

## §7 THE OPENS (every one named; the collaborator rules)
1. THE READY CODE — "200 or 405" is the brief's own candidate pair; the exact value byte-named at the build's first live fire (§1's clause; the RUN-9999 lesson, FR-MEM-0025).
2. THE README'S FLOOR LINE (:189 — "The quality floor: 200 tests green, pyright clean, ruff clean.") goes stale at the grown floor: the build's README step (file-unit 4) carries the one-line update to the MEASURED count — named here; this spec's approval the ruling.
3. THE GATE'S CONDITION 2 (the targets green live) — this lane is READ-ONLY (the seat's law): the live evidence rides the build's step 6 + kensho's validate/lifecycleintegration, the brief §5's own clause ("the read-backs' evidence rides the gate — the spec's verification or the build's"); the collaborator rules the satisfaction.
4. THE TRADE-OFF CARRIED (the brief §6): a SECOND lifecycle surface — eight recipes at one Makefile, two pid/log pairs, the mirroring duplication the named maintenance cost (the shared-recipe alternative priced and declined: the web's byte-untouched law + the tiers' failure modes never coupled). The plan carries this cost, named.

THE RECOMMENDATION, WHOLE: approve this spec — the bytes whole over the approved brief (the four targets mirroring the standing form; the 8100 default at both sides [src + MCP_PORT]; the argparse widening with the bare form byte-held; the one arc's three forms; the README's four lines); build/lifecycleintegration fires per §6; G-LIFECYCLEINTEGRATION closes on the live read-backs + the grown floor + kensho's re-run. The collaborator rules.
