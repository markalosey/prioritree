<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/ouncemcp

**Route:** prioritree-mcp (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T20:24:07Z |
| 2 | report | tansa | 2026-11-22T20:27:18Z |
## Reported by tansa — 2026-11-22T20:27:18Z

# OunceMCP census — the framework's actual surface (tansa, 2026-11-22)

1. TOOL FORM: `@server.tool(name="noun.verb", effect=Effect.READ|WRITE|DESTRUCTIVE)` on a Python function. Pydantic input (`Field(description=...)`, bounds ge/le/max_length) and a Pydantic return model are REQUIRED — the server refuses to start otherwise ("must be annotated to return a Pydantic model"). The docstring is the tool's description; errors are values (`raise NotFound(msg, hint=...)`). `ouncemcp context server.py <tool>` prints the exact JSON a client receives.

2. BUDGETS: three — startup context (warn at 4,000 tokens by default), per-tool definition (target 250 / warn 500 / fail 1,000), result (default 2,000). `ouncemcp check server.py` counts name+description+inputSchema+outputSchema, lints, and exits non-zero over the fail budget (CI gate). Forms: `Budget(result_tokens=..., startup_tokens=...)` on OunceServer; per-tool `result_tokens=` + `budget_reason=` (lint budget-override-without-reason). Tokenizer `o200k_base` default, pluggable (`tokenizer=`, `--tokenizer`). Over-budget results are SHAPED: lists trimmed first, then long strings, then optional fields — always valid against the output schema; paged lists rewrite `next_cursor` so nothing is skipped; else `result_too_large`. Every result self-reports in `_meta.ouncemcp`.

3. WRITES: `idempotency=True` keys the write by caller+tenant+arguments — a repeat replays the first result, never re-runs (store: `MemoryStore`, `RedisStore` for replicas; client key via `_meta`). `approval="required"` (or a function) + `preview=` (read-only text for the person) gate every change: MCP `input_required` with a signed single-use receipt, elicitation for older clients, server-side `OunceServer(approver=...)` hook otherwise; the model cannot approve its own write (`approval`/`approved` reserved). Handles: `OunceServer(handles=True)`; `ctx.issue_state`/`ctx.verify_state` bind tokens to caller, request, expiry (`consume=True` single-use); signed cursors bind to tool+caller+query.

4. SUBSTRATE: Python framework ON FastMCP 4.1.6 + the official MCP Python SDK, targeting MCP spec 2026-07-28. `OunceServer` wraps a FastMCP server; `OunceServer.wrap(existing)` adopts one; `from_config(name, "ouncemcp.toml")` loads settings. Run forms: stdio (`python server.py`, host-launched) AND streamable HTTP (`server.run("http", host=, port=, allowed_hosts=, allowed_origins=)`; `ouncemcp dev` hot-reloads on http://127.0.0.1:8000/mcp; `server.http_app()` for ASGI). Install: `pip install ouncemcp` (pipx/uv tool), release 1.0.0rc3, Python >= 3.11, Apache-2.0, status pre-1.0 with the API frozen.

5. PROOF: task suites — `ouncemcp eval suite.yaml` (replay model by default; `--model openrouter:...` with `--repeats`/`--max-cost`; `--compare baseline.json --fail-on-regression`; `--html report.html`). Benchmark harness — `ouncemcp bench` compares servers across models (published M3: two pilots vs plain FastMCP, 4 models, 21 tasks). Traces — `OunceServer(trace=JsonlSink("calls.jsonl")|MemorySink()|LoggingSink()|CallbackSink(fn)|OTelSink())`, redacted by default; `ouncemcp trace calls.jsonl` views. Plus `ouncemcp audit <url|file|-- cmd>` for any server, `ouncemcp.eval.run_security_suite(server, cases)`, `ouncemcp.testing.as_caller(...)`, `await server.measure_recall(cases)`.

6. CLIENT: `ouncemcp.client.Broker` — one catalog over many servers: `await broker.host_tools()` → (mode, definitions); `await broker.call("shelf.books.search", {...})`; `await broker.handle(name, arguments)` answers the search_tools/describe_tool/call_tool meta-tools; `result.for_model()`; OAuth via `OunceOAuth`. Any MCP host works over stdio or HTTP (verified: Claude Desktop, Cursor, MCP SDK stdio client, official conformance suite). The docs name the Broker as the client surface; FastMCP's own Client API is the layer beneath, not re-documented here.

Sources: subbusainath.github.io/ouncemcp — landing, quickstart, book ch02/ch03/ch04/ch06/ch13/ch15, concepts/security, concepts/traces, guides/safe-writes, guides/evaluating, guides/client-broker, compatibility; github.com/subbusainath/ouncemcp README; pypi.org/project/ouncemcp (1.0.0rc3, Python >= 3.11).
