<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — build/lifecycleintegration

**Route:** prioritree-mcp (executing) | **Events:** 10 | **Reports:** 5

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T18:50:17Z |
| 2 | dispatch | shinko | 2026-11-23T18:50:28Z |
| 3 | report | jikko | 2026-11-23T18:52:00Z |
| 4 | report | jikko | 2026-11-23T18:58:22Z |
| 5 | dispatch | shinko | 2026-11-23T18:58:36Z |
| 6 | dispatch | shinko | 2026-11-23T18:58:46Z |
| 7 | report | jikko | 2026-11-23T19:04:37Z |
| 8 | report | jikko | 2026-11-23T19:05:44Z |
| 9 | dispatch | shinko | 2026-11-23T19:05:58Z |
| 10 | report | jikko | 2026-11-23T19:06:54Z |
## Reported by jikko — 2026-11-23T18:52:00Z

Step 2 of 6 (the src region) DONE — src/prioritree/mcp_server.py, two hunks, the spec §2's fenced bytes applied verbatim.

1. The import swap :27 — `import sys` → `import argparse` (sys grep-verified at :27/:573 only before the swap; no dead import left).
2. main() widened :571-584 — argparse parser (prog="prioritree.mcp_server"), --serve store_true, --host default "127.0.0.1", --port type=int default 8100; the docstring widened to name the defaults.
3. The bare form BYTE-HELD — `server.run("stdio")` at :584 byte-identical to HEAD's line; the module docstring, the __main__ form, the server construction (:113), the five tools, the seam all untouched (the diff shows only the two hunks).
4. The --serve flow — parsed values flow to server.run (:582: host=args.host, port=args.port); the host JOINED to allowed_hosts when non-loopback (:579-581); allowed_origins [] unchanged.
5. Read-back done: region verbatim matches the spec's AFTER fence; one patch header checksum fixed mid-apply (parse refusal, file untouched at the refusal — recount, re-apply, clean).
NOT done (other steps' lanes): Makefile (step 1), the test arc (step 3), README (step 4), the floor + lint/typecheck + live legs (steps 5-6, the coordinator's instruments — this seat never verifies its own work).
## Reported by jikko — 2026-11-23T18:58:22Z

Step 1 of 6 (file-unit 1, the Makefile's regions) — landed.

- Head block: MCP_PORT ?= 8100 / MCP_HOST ?= 127.0.0.1 inserted beside the byte-untouched PORT/HOST (Makefile:3-6); the .PHONY row extended with the four mcp names (Makefile:8, the one touched line).
- The four targets inserted between restart (:69) and help (:123), the spec's fence bytes verbatim, recipe lines TAB-indented: mcp-start (:71-82 — the live-pid guard against .prioritree/mcp-server.pid, the .venv/bin/python binary guard, mkdir, the env -u WEB_CONCURRENCY module-form launch, the sleep-1 /mcp probe read-back with the || true form); mcp-stop (:84-106 — absent-pidfile no-op, the stale cure, SIGTERM + the 5s drain, the rm, the code-form refusal read-back); mcp-status (:108-119 — the pid and the port both labeled, read-only); mcp-restart (:121 — the prerequisite composition, no recipe).
- The web's four recipes byte-untouched: the applied diff's only changed lines are the two variable adds, the .PHONY row, and the insertions; the read-back confirms start/stop/status/restart at :22-69 identical to HEAD's bytes (the four standing names grepped — the help forms unchanged).
- Not done: steps 2-6 (the src widening, the test arc, the README's lines, the floor, the live legs) — later steps' lanes; no live fire this step (the ready code names at step 6 per the spec's clause).
## Reported by jikko — 2026-11-23T19:04:37Z

Step 3 (of 6) — the test arc, landed. tests/test_mcp_server_face.py:638-694: test_parse_argv_derives_the_run_call appended at the spec's §3 insertion neighborhood (the tail, after test_re_tally_after_cure, two-blank separation), the three parametrized forms byte-held: bare-stdio (server.run("stdio"), no kwargs, no HTTP call), serve-defaults (127.0.0.1:8100, the loopback pair), serve-overrides (host/port flowed, the host JOINED to allowed_hosts). Three floor-forced cures over the spec's literal bytes, each reported: (1) the empty-dict expected wrapped cast("dict[str, object]", {}) + cast added to the typing import — pyright strict's partially-unknown refusal, the tree's quoted-cast form (run_store.py:142 precedent); (2) the override host 0.0.0.0 -> 192.0.2.10 — S104's bind-all heuristic on the literal, the zero-in-code-ignores law forbidding a noqa and the pyproject ruling outside this file-unit; the asserted behavior (a non-loopback host joining allowed_hosts) preserved whole; (3) the signature's trailing comma — COM812, test_cli.py:137's precedent form. The apply's findings cured same-turn; the final apply rides zero ruff/pyright findings. NOT done: the floor run and the live legs (steps 5-6, the coordinator's instruments).
## Reported by jikko — 2026-11-23T19:05:44Z

README step 4 landed (the four re-ruled lines + the named open at :189), nothing else touched — patch applied 3 hunks, zero findings.

- :107 — the --serve console line now reads `# streamable-HTTP at http://127.0.0.1:8100` (was 8000).
- :110 — the Port note rewritten: 8100 the default (`--host`/`--port` override), the web keeps 8000, both co-run at defaults, collision retired; the four mcp-* targets named (`MCP_PORT ?= 8100`, `MCP_HOST ?= 127.0.0.1`).
- :164 — the collision bullet now **The port discipline**: web 8000 / MCP 8100, co-run at defaults, the mcp-start/mcp-stop/mcp-status/mcp-restart lifecycle named.
- :183 — the tool-lane tail: `--serve` (port 8100 — co-runnable with the web's 8000).
- :189 — the floor line: 200 -> 203 (the arc's three parametrized forms, the dispatch's named number; step 5's floor run measures it).

Read-back verbatim at all five lines; neighborhoods byte-intact (file 193 lines). The named targets + defaults verified present: Makefile carries MCP_PORT ?= 8100 and the four targets; mcp_server.py carries the 8100 default. No gaps found; nothing left undone in this step.
## Reported by jikko — 2026-11-23T19:06:54Z

The floor, all three acts executed, no edits:

1. Test act (all): the full suite — "203 passed in 25.99s" — matches the expectation exactly (203: the 200 + the argv arc's three parametrized forms).
2. Lint act (check): "uv run ruff check src/ tests/ — All checks passed!"
3. Typecheck act: "uv run pyright — 0 errors, 0 warnings, 0 informations"

No findings outside the expectations; nothing edited, nothing skipped.
