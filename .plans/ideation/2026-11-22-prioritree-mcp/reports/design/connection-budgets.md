<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — design/connection-budgets

**Route:** prioritree-mcp (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T05:56:24Z |
| 2 | report | keisan | 2026-11-23T06:01:21Z |
## Reported by keisan — 2026-11-23T06:01:21Z

KEISAN — design/connection-budgets — the connection form's costs, the honest numbers (2026-11-23).

READ-BACK (cited): junro.json Q-mcp-tools R6 · mcp_server.py:110-113 (the seam/server minted at import), :452-535 (five tools, idempotency=True on register+cast), :571-576 (the two run forms, port 8000 hardcoded) · opencode.json:514-521 (the mcp block) · Makefile:3,20-67 (PORT ?= 8000; sleep 1 + read-back; the 5s drain bound) · README.md:110,164 (the port note) · mcp-design.md F1/F5/F6 + §4 (the flock; the register asymmetry + the ack's run_id guard; the launch keys; the 1,005-token startup) · design/member-path.md §2 (the grant map: 5 granted seats) · store_lock.py:77-91 (blocking LOCK_EX) · run_store.py (save-at-cast: one line + flush; the load re-validates every line) · ouncemcp/core/server.py:23 (`from fastmcp import FastMCP`) + site-packages fastmcp-4.2.4, mcp-2.3.0, fastapi-0.165.0, pydantic-2.14.4, jsonschema-4.26.0, tiktoken-0.14.0. Estimates marked as estimates — this seat holds no timer (the no-shell law).

1. STDIO PER SESSION — the spawn ≈ 1.7s wall-clock per session per seat. Derivation (an estimate from the imports' weight, summed): interpreter 40ms + pydantic 200 + fastapi/starlette 300 + fastmcp 200 + the mcp SDK 300 + jsonschema 150 + tiktoken + the o200k table 250 + ouncemcp's own 100 + prioritree's core 20 + the OunceServer construction + five registrations (schema building, budget measuring) 100 + the seam mint (Serialize + Lock — construction only, no I/O) 1 = 1,661ms; the ouncemcp→fastmcp→mcp/fastapi chain is ~90% of it. Overlapped with the harness's own session boot — the seat feels it at the first tool call. Plus 1,005 tokens of definitions in context every session (§4's budget; both forms pay it — not a differentiator).

2. THE MEMORYSTORE RESET — what dies: the transport-level replay alone (a retried identical call WITHIN a session). Priced honestly: cast is cross-session SAFE (R9 durable in the file — the dedup index rebuilt and re-validated at load, acknowledged=True, the count unchanged); register re-RUNS on the fresh store → the scan-mint mints RUN-{max+1} — the PHANTOM DUPLICATE: ~1 dead run file (a manifest row, ~1-3KB), the sitting fragments (the retry's ack carries the new run_id; a tally on the phantom halts "zero-coverage"), and the guard is the ack's own run_id (F5's teaching, authored into the description). The failure mode exposed: a harness-tier retry of register across a session death — nothing else.

3. N-SERVERS — 5 granted seats (jikko/kensho/shinko full five; rikai/shindan read three) = up to 5 concurrent server processes + the service + the CLI on ONE store; the machine-wide flock (blocking LOCK_EX; every op loads) serializes every act. The wait is bounded by the act: typical act ~3ms (a <10KB run file: load-parse + append + flush) → worst wait 4 queued writers × ~3ms ≈ 12ms (imperceptible); the n=100/k=1 ceiling (4,950 vote rows ≈ 1.14MB, parse ~50ms + I/O) ≈ ~100ms/act → worst wait ~400ms — reads pay it too (all five ops load). Five seats' wave ≈ 8.3s of machine work, run in parallel — ~1.7s wall-clock each.

4. SHARED-HTTP — the boot once ≈ 1.7s, amortized to ~0 per session (a ~1-2ms connect); the MemoryStore persists → the register replay SURVIVES sessions (the phantom duplicate CURED — the one durable asymmetry between the forms); the writers drop 5→1 (+ the service + CLI): the flock's worst wait halves (~200ms at the ceiling). The port: 8000 HARDCODED (mcp_server.py:574, no override flag) = make start's default (Makefile:3) — the collision's price: uvicorn's raw EADDRINUSE at boot (NOT a ThreePart) unless the web moves (make start PORT=8100 — the README's own documented alternative, :110/:164).

5. THE LIFECYCLE CEREMONY — enabled:true + a DOWN server: the connect fails AT LAUNCH, and the restart law hides it from live sessions (F6's own clause; FR-MEM-0014's shape) — the cold-tree seat finds the tools ABSENT, silently: the failure rides the harness's launch channel, never a ThreePart at the seat. The ceremony's numbers: start ≈ 3s (sleep 1 + boot + the read-back probe), stop ≤ 5s (the bounded drain), restart ≤ 8s — paid per cold start, by hand or through the lifecycle tool's grant.

6. THE SWITCH — enabled is read at launch: every flip costs a harness restart (the seat's session context dies with it). The fragment: ~6 lines / ~200 bytes (the mcp block: command/args/enabled — F6's keys) vs the yaml's 21 grant rows (15 full + 6 read) — the sync burden: TWO places to keep true (the carried fragment's bytes + the yaml's rows) vs ONE (the yaml's structured data, the regen emitting both layers from the single source); a drift surfaces only at the next launch — hidden from live sessions, the same law.

7. THE TABLE (the total-cost comparison — the recommendation's ground):

| axis | stdio per-session | shared-HTTP (tool-starts-it) |
|---|---|---|
| session-start latency | ~1.7s/session/seat | ~0 marginal (boot once ~1.7s) |
| register cross-session retry | phantom duplicate (guarded: the ack's run_id) | replays — cured |
| cast cross-session retry | safe (R9 durable) | safe (R9 durable) |
| flock worst wait typical/ceiling | ~12ms / ~400ms | ~6ms / ~200ms |
| port | none (stdio) | 8000 collision — the web moves |
| cold tree | tools spawn on demand | tools ABSENT silently; ~3s start ceremony |
| flip cost | a restart per flip | the state IS the switch; enabled still launch-read |
| maintenance | fragment ~200B + yaml rows | the same fragment (url form) |

THE GROUND LAID: the stdio form's two real prices are ~1.7s/session (hidden, overlapped, amortized) and the register phantom (visible at the ack, guarded by F5's teaching, cheap: one dead file + a fragmented sitting); the shared-HTTP form's real prices are the SILENT absent-tools at a cold tree (no guard, no ThreePart — the seat's worst experience), the port collision (the web displaced or a raw EADDRINUSE), and the ceremony (~3s per cold start). The collaborator's leaning ("maybe the tool starts it and runs it?") cures the phantom and halves the contention — but its worst failure is the unguarded one; if the leaning is taken, the cure must carry its own guard (the start ceremony's read-back serving as the honest up/down signal, the spec's paste-able block teaching the seats the status probe). The phantom is cheap and guarded; the silence is neither. The recommendation is suisen's to rule — the numbers favor whichever form guards its own worst failure.
