<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — design/cold-clone-walk

**Route:** prioritree-ci (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T23:08:10Z |
| 2 | report | moho | 2026-11-23T23:09:41Z |
## Reported by moho — 2026-11-23T23:09:41Z

The cold-clone walk, CI-era — what breaks when nobody helps.

(1) THE CLONE holds: every README-named make target exists (dev/test/lint/typecheck/start/stop/status/restart/mcp-*); the hooksPath command is valid (.githooks/pre-commit tracked in-tree); the launch forms are real (service.py, mcp_server.py, web/'s 14 templates + 2 static — the README's own counts). One drift: "200 tests green" (Architecture) vs "203 tests green" (Status) — the floor disagrees with itself.

(2) THE CI STORY: "CI is deferred — the git hook and the local gates stand in" (Status); "CI remains" (Install). Honest but empty: no .github/ in-tree at all — no workflows, no PR template, no CODEOWNERS. Nothing tells the contributor what runs at a push: nothing does.

(3) THE HOOK: pyright-only on staged .py (ACM filter); ruff is "PHASE 2 (named, pending)". At the visitor's own commits, ruff violations commit cleanly — the local stand-in for CI enforces half the floor it names. Seam: the hook strict-pyrights staged files outside make typecheck's include set (scripts/*.py) — the commit gate and the typecheck target disagree on scope.

(4) THE PUSH: nothing runs at the fork (no workflows in-tree; the fork's Actions page is empty); nothing in-tree checks the PR at the base; whether upstream's CodeQL default-setup scans the PR is the maintainer's hand — unknowable from the clone. "Will my push be green?" is unanswerable: no check exists to be green.

(5) THE FRICTION: no runner to be green; the local gate is half the floor; the 200/203 drift; the quickstart omits lint/typecheck (the honest sequence carries them) so a quickstart-only visitor never runs ruff anywhere; no CONTRIBUTING — the contribution story ends at "deferred" with no path to the CI's shape.

TOP THREE FIXES (by contributor-pain):
1. Land the minimal CI workflow in-tree (Actions: make dev, lint, typecheck, test — on push and PR): the fork and the PR both run it, the question becomes answerable, and Status flips from "deferred" to the workflow's name.
2. Complete the local gate — land the ruff half of the pre-commit hook (the named Phase 2), so the local stand-in enforces the same floor the CI would.
3. Fix the README's push story for the cold visitor — a "Pushing and PRs" line naming exactly what runs today (nothing in-tree; the local gates; upstream's CodeQL at the maintainer's hand), the 200/203 reconciliation, and lint/typecheck into the quickstart.
