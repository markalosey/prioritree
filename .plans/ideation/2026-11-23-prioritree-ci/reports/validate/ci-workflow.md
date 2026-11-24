<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — validate/ci-workflow

**Route:** prioritree-ci (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-24T00:56:27Z |
| 2 | report | kensho | 2026-11-24T00:59:33Z |
## Reported by kensho — 2026-11-24T00:59:33Z

KENSHO — validate/ci-workflow — the independent verification of the CI unit's build whole (2026-11-23; zero trust: my own reads, my own runs; the fence cited at reports/synthesize/ciworkflowspec.md).
§1 THE SURFACES, READ AT MY OWN HANDS, BYTE-AGAINST-SPEC:
- .github/workflows/ci.yml (40 lines) — byte-identical to spec §1's fence: floor job checkout@v6 → setup-uv@v10.3.3 (enable-cache: auto alone) → make lint / make test / make typecheck (the Makefile's targets the entrypoints); codeql job checkout@v6 → init@v4 (languages: python, build-mode: none, config-file: ./.github/codeql/codeql-config.yml) → analyze@v4, job-scoped permissions contents: read + security-events: write; triggers push[main] + the weekly cron ALONE (my grep "pull_request" over the file: ZERO matches — the no-PR law); workflow-level concurrency, cancel-in-progress: true, the schedule guard dropped.
- .github/codeql/codeql-config.yml (7 lines) — byte-identical to §2's fence: paths: [src/, tests/] + the ruled-widening comment.
- README — :57 "The quality floor: 203 tests green, pyright clean, ruff clean." (the drift folded); :185 "The publish is deferred: the license, the packaging, and CI have landed; the publish itself remains the outward lane's ruled act." (the remainder closed); :189 the CI-live line byte-matching §4c's after-form (the workflow named, the direct-push story, the no-PR grammar) + the 203 tail.
- The hook's landed emission — .githooks/pre-commit:9-15 names PHASE 2 landed, "both carrying the whole floor locally" (the multiple-locations law's re-authored form; the refused "hook stays pyright" framing absent; the wrap variance vs spec §3b named — §3b superseded by the 2026-11-24 correction); :41-51 the ruff block mirrors the pyright form ($STAGED_PY, `uv run ruff check`, exit 1 on any finding); the bypass :17-22 covers both checks; the sibling emissions' generated markers unchanged (jikko.md:1, opencode.json:1-15) — the regen rode the generator, never a hand-edit.
§2 THE LIVE LEG, NAMED HONESTLY:
The scratch form (uv run ruff check <scratch.py> over a deliberate finding) is OUTSIDE this seat — no file-creation act, no shell (the no-shell law; kensho's routing carries no patch/write). The live form I ran: `uv run ruff check src/ tests/` (the lint act — the hook's own invocation verb and instrument, under the tree's [tool.ruff] select=["ALL"]) — exit 0, "All checks passed!" (the zero-findings side live at my hands). The NON-ZERO refusal leg: verified by my own read of the landed bytes (:42 `|| RUFF_EXIT=$?` → :43-51 the refusal block → exit 1), NOT by live reproduction — named, never faked; the live reproduction belongs to a mutation-carrying hand.
§3 THE FLOOR, RUN AT MY OWN HANDS (VERBATIM):
- make test → "203 passed in 26.50s"
- make lint → "uv run ruff check src/ tests/" / "All checks passed!"
- make typecheck → "uv run pyright" / "0 errors, 0 warnings, 0 informations"
- the zero-ignore census at my own grep: zero noqa directives within the floor's scope (src/ + tests/); the tree's one real noqa (.opencode/scripts/test_runner.py:41, S603/S607) sits outside the instruments' scope, ruling-commented — named, not a finding against the bar.
§4 THE VERDICT — G-CI-WORKFLOW's four conditions, one-line evidence each:
1 GREEN — the surfaces byte-against-spec: the workflow, the config, the README's three lines (§1 above).
2 GREEN — the ruff-phase-2 landing whole at the emission this seat reads: the ruff check joined the hook mirroring pyright, the note names the completion (the multiple-locations law realized); the hikari source edit the collaborator's hand — the landed emission + the unchanged sibling markers the tree-side evidence.
3 BLOCKED — THE FLIP LEG: the collaborator's pending leg — the GitHub-side default-setup flip attested at their hand (the settings surface; never verifiable at the seats).
4 SPLIT — the first live run: the collaborator's pending leg (the read-back at GitHub's Actions surface; never verifiable at the seats); kensho's independent verification GREEN — this report + the floor above.
A RESIDUAL NAMED (no gate condition carries it; never a silent pass): README:163 still reads "The hook enforces pyright only; ruff is named, pending" — stale against the landed hook (ruff rides it now); outside the spec's three-line fence, a candidate for the next ruled edit.
THE GATE: blocked pending the collaborator's two legs (the flip attestation; the first-live-run read-back) — every seat-verifiable leg green at this seat's own hands.
