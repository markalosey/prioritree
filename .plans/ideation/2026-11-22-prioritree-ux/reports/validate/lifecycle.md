<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — validate/lifecycle

**Route:** prioritree-ux (executing) | **Events:** 5 | **Reports:** 2

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T19:06:59Z |
| 2 | report | kensho | 2026-11-22T19:09:28Z |
| 3 | result | shinko | 2026-11-22T19:09:48Z |
| 4 | dispatch | shinko | 2026-11-22T19:51:05Z |
| 5 | report | kensho | 2026-11-22T19:54:01Z |
## Reported by kensho — 2026-11-22T19:09:28Z

KENSHO'S INDEPENDENT VERIFICATION — validate/lifecycle (the lifecycle unit's build vs the approved spec, zero trust)
GROUND READ + CITED: lifecyclespec.md (§2's fence :24-95; §3 :117; §5 :133) · lifecycle.md (the brief) · junro.json (G-LIFECYCLE :323-330; R3 :653) · build/lifecycle.md (jikko's three steps) · HEAD = cf7cb1020f2694eef71e0f81c9df7fa54c01d124 (.git/refs/heads/main, my own read).
(a) THE FLOOR — my own runs, verbatim: test (all) "156 passed in 28.23s"; lint (check) "All checks passed!"; typecheck "0 errors, 0 warnings, 0 informations". All three match the expectations; zero findings outside them.
(b) THE EXACT-TASK LAW — GREEN: the landed Makefile = §2's fence, 70/70 lines byte-for-byte (my line-by-line read both sides + TAB greps: 46 TAB-led recipe lines, zero space-led, zero trailing whitespace); the .PHONY growth at :6 exact (`dev test lint typecheck help start stop status restart`); the standing five byte-untouched (:1, :8-18, :69-70); the handed constraints verbatim (HOST ?= 127.0.0.1 at :4; PORT ?= 8000 at :3; --workers never on the launch line; `env -u WEB_CONCURRENCY` at :30 — removal, never blanking; no cd in any recipe; the repo-root contract in all four help entries); the .gitignore :184 `.prioritree/` immediately after :183 `/.junro/`, the file whole at 184 l. Zero deviation found — nothing to rule.
(c) THE LIVE SEQUENCE — REFUSED AT MY PACK, the datum: kensho's acts carry no make verb (the no-shell law); the live sequence's holder is the operator's shell. On disk: .prioritree/ holds only runs/ — no server.pid, no server.log; no live run has happened on this tree. The recipes' mechanisms verified against the landed bytes: the guard's expected/found/next-action grammar (start :21-28); the one-line launch (:30 — nohup + the $$! capture share one line, the direct sibling binary .venv/bin/uvicorn, env -u, --host/--port alone); the drain-wait's ~5s bound (:44 — 5 sleeps); the read-backs' forms (:31 the 404-as-ready probe, -f never, || true; :52 the refusal arm; :61-65 the pid + the port both labeled; :67 restart = stop start, zero new mechanism). Static — necessary, never sufficient.
(d) G-LIFECYCLE'S THREE CONDITIONS (junro.json :323-330), each ruled:
1. GREEN — the lifecycle targets landed per the approved brief, byte-exact (probe b).
2. BLOCKED at kensho's hands — the live green unevidenced: the pack's refusal (probe c) + no on-disk live evidence; the live sequence is carried to the gate's hands, where the operator's shell runs make start/status/restart/stop and the read-backs rule.
3. GREEN — the floor green at my own hands, verbatim (probe a); the brief's live-sequence extension of the re-run rides condition 2's carrier.
GATE CARRIAGE: G-LIFECYCLE stands blocked on condition 2 alone; conditions 1 and 3 green with the evidence above.
## Reported by kensho — 2026-11-22T19:54:01Z

KENSHO'S EXTENSION VERIFICATION — validate/lifecycle, the second report (E4, the post-restart session; the lifecycle tool itself the instrument)
GROUND READ + CITED: synthesize/lifecyclespec.md §E2 (the wrapper's six ops) · §E3 (the grant map — kensho ALL SIX) · §E4 (the RUN-9999 probe cure, four byte-sites) · §E6 step 4 (the live sequence's order) · my prior report on this packet (19:09:28Z — conditions 1+3 green, condition 2 blocked at the no-verb seat, carried to the gate's hands).
THE INSTRUMENT: this post-restart session's pack carries the lifecycle act (§E1's delivery-at-the-launch, landed); the primary act ran the six ops THROUGH THE TOOL, zero trust in the build seat's claims — every output below the tool's own rendering, verbatim.
THE TRANSITIONS (each output the tool's own):
- start: "read-back: HTTP 404 on http://127.0.0.1:8000/ (404 = answering; 000 = still booting: make status)"
- status: "pid: 34904 (live)" / "port: 8000 answering (HTTP 404 on /runs/RUN-9999/next; the ready form)"
- restart: "SIGTERM -> pid 34904 (the graceful drain)" / "stopped: pid 34904 gone (the pidfile is removed)" / "read-back: refused on 8000 - the port is down" / "read-back: HTTP 404 on http://127.0.0.1:8000/ (404 = answering; 000 = still booting: make status)" — the refusal, then the answer
- stop: "SIGTERM -> pid 35121 (the graceful drain)" / "stopped: pid 35121 gone (the pidfile is removed)" / "read-back: refused on 8000 - the port is down"
THE READ VERBS:
- log: the bounded tail, "the last 7 of 7 lines" at .prioritree/server.log — the boot banner ("Started server process [34904]" / "Application startup complete." / "Uvicorn running on http://127.0.0.1:8000") + the request lines (two "GET /runs/RUN-9999/next" 404s — start's and status's probes)
- output: "output — http://127.0.0.1:8000/runs/RUN-9999/next answered HTTP 404 (the body verbatim):" then the ThreePart refusal whole: {"expected":"a run file in the store home (live: RUN-0001)","found":"no run file for 'RUN-9999' in .prioritree/runs","next_action":"register a run first, or cite a live RUN-{####} id — the home is the truth (the dir, never a hidden global)"}
THE PROBE CURE VERIFIED: every read-back probes RUN-9999 — the 404 expected and received at the REAL root (RUN-0001 lives live here; the pre-flip probe read HTTP 200, the "unexpected; not the ready form" mislabel); the healthy state now reads "the ready form" — the label gone from the healthy state.
THE VERDICT — G-LIFECYCLE's three conditions, whole:
1. GREEN (prior report — the targets landed byte-exact per the approved brief) — stands.
2. GREEN NOW — the live green evidenced by a member's own act: the six ops run through the lifecycle tool this session, every read-back true (answering / pid+port / refusal-then-answer / refusal); the blocked condition unblocked — R12's grant proven by use.
3. GREEN (prior floor runs + this run) — the floor green at my own hands; the independent re-run now self-sufficient — this run IS the re-run through the granted act.
THE GATE: unblocked — all three conditions green; the evidence above, the tool's own outputs.
