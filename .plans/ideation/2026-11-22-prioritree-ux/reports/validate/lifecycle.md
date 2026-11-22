<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — validate/lifecycle

**Route:** prioritree-ux (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T19:06:59Z |
| 2 | report | kensho | 2026-11-22T19:09:28Z |
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
