<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — build/ci-workflow

**Route:** prioritree-ci (executing) | **Events:** 13 | **Reports:** 6

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T23:33:21Z |
| 2 | dispatch | shinko | 2026-11-23T23:33:42Z |
| 3 | report | jikko | 2026-11-23T23:34:16Z |
| 4 | report | jikko | 2026-11-23T23:34:24Z |
| 5 | dispatch | shinko | 2026-11-23T23:34:40Z |
| 6 | report | jikko | 2026-11-23T23:35:40Z |
| 7 | dispatch | shinko | 2026-11-23T23:35:55Z |
| 8 | report | jikko | 2026-11-23T23:36:42Z |
| 9 | result | shinko | 2026-11-24T01:00:09Z |
| 10 | dispatch | shinko | 2026-11-24T01:02:30Z |
| 11 | report | jikko | 2026-11-24T01:02:57Z |
| 12 | dispatch | shinko | 2026-11-24T01:13:33Z |
| 13 | report | jikko | 2026-11-24T01:14:03Z |
## Reported by jikko — 2026-11-23T23:34:16Z

Step 1 of 6 done: landed .github/codeql/codeql-config.yml via patch create (parent dirs made — .github/codeql/ born by the apply). The fence's seven lines whole: name: prioritree, the four-line ruled-widening comment (the positive form mirroring pyright's include at pyproject:172), paths: [src/, tests/]. Read-back byte-against-fence: identical, 7 lines, trailing newline. Nothing else touched — no other file read-written, .github/ was empty before (glob-confirmed), the workflow and README legs untouched. Gap: none at this step; steps 2-6 remain.
## Reported by jikko — 2026-11-23T23:34:24Z

STEP 2 LANDED — .github/workflows/ci.yml created whole (40 lines, the spec §1's fence byte-exact, nothing else touched).
The triggers: push branches [main] + schedule cron '0 3 * * 1'] — grep "pull_request" over the file: ZERO hits (R4's no-PR law held).
The concurrency: group "${{ github.workflow }}-${{ github.ref }}" + cancel-in-progress: true, no schedule guard.
The floor job: ubuntu-latest; checkout@v6 -> setup-uv@v10.3.3 (python-version UNSET, enable-cache: auto) -> make lint -> make test -> make typecheck, each its own step naming its instrument.
The codeql job: job-scoped permissions (contents: read, security-events: write); checkout@v6 -> init@v4 (languages: python, build-mode: none, config-file: ./.github/codeql/codeql-config.yml) -> analyze@v4.
Read-back: the file read verbatim post-apply — matches the fence; note: .github/codeql/codeql-config.yml does not exist at this step's landing (step 1's file; my unit was the workflow alone).
## Reported by jikko — 2026-11-23T23:35:40Z

STEP 4 (the README's lines) done — one pass, one file-touch, three sentence-swaps per the spec's §4 fences, nothing else touched.
- README:57 — "200 tests green" -> "203 tests green" (the census-named drift folded); the line's other bytes untouched.
- README:185 — "the license and the packaging have landed; CI remains" -> "the license, the packaging, and CI have landed; the publish itself remains the outward lane's ruled act" — the precondition's remainder closed.
- README:189 — "CI is deferred — the git hook and the local gates stand in" -> the CI-live line naming the workflow (.github/workflows/ci.yml), the floor (ruff, pytest, pyright) at every push to main and weekly, the tree's own CodeQL config (.github/codeql/codeql-config.yml), the direct-push story per the no-PR law, and the hook as the local backstop; the line-tail "203 tests green" untouched (already correct at HEAD).
Read-back done at :55-59 and :184-190 — the three lines verbatim byte-against-fence, neighborhoods intact; file at 193 lines, same length. No gaps; nothing else in the unit touched (the other steps are other hands).
## Reported by jikko — 2026-11-23T23:36:42Z

The floor (step 5 of 6) — the pack's three fixed-argv acts, all within expectations, zero findings, nothing edited:

1. Test act (all): the full suite green — 203 passed in 27.09s (the expected 203; this unit touched zero Python — the workflow, the config, and the README only).
2. Lint act (check): ruff over src/ and tests/ — "All checks passed!"
3. Typecheck act: pyright over the tree — "0 errors, 0 warnings, 0 informations".

Every outcome matched the stated expectations; no report items beyond the outcomes themselves.
## Reported by jikko — 2026-11-24T01:02:57Z

Step 7 landed — the R6 fold's workflow-level permissions block inserted into .github/workflows/ci.yml: `permissions:` + `contents: read` at :13-14, after :11 (cancel-in-progress: true), before `jobs:` (now :16), with the file's own blank-line spacing (concurrency → blank → block → blank → jobs). One hunk, three added lines; nothing else touched. The codeql job's job-scoped block (:33-35, was :30-32) read back byte-unchanged: contents: read + security-events: write. File grew 40 → 43 lines, all at the insertion point. Not done: no other edits, no commit (the fold's one-commit lands at step 8), no verification of my own work.
## Reported by jikko — 2026-11-24T01:14:03Z

Step 8 (the residual fold) done: README.md:163's stale clause cured.

Verified the exact current bytes first — kensho's finding held: "The hook enforces pyright only; ruff is named, pending — run `make lint` for the full floor."

Verified the landed truth against the disk (.githooks/pre-commit): the hook now runs both checks on staged .py — pyright at 0/0/0 and ruff at zero findings.

Replaced the stale clause with the multiple-locations law's words: "The hook enforces the whole floor locally — ruff + pyright on staged .py at the site the code is written; CI checks the same floor at the push."

Read-back confirms the line verbatim; the surrounding bullets (CWD law, port discipline, .prioritree/ runtime) untouched — one hunk, one file, nothing else.
