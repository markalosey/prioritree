<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/ciworkflowspec

**Route:** prioritree-ci (executing) | **Events:** 6 | **Reports:** 2

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T23:25:08Z |
| 2 | report | togo | 2026-11-23T23:30:16Z |
| 3 | result | shinko | 2026-11-23T23:31:39Z |
| 4 | gate | shinko | 2026-11-23T23:32:52Z |
| 5 | dispatch | shinko | 2026-11-24T01:01:14Z |
| 6 | report | togo | 2026-11-24T01:02:03Z |
## Reported by togo — 2026-11-23T23:30:16Z

TOGO — synthesize/ciworkflowspec — THE CI WORKFLOW EXACT-TASK SPEC (2026-11-23; the spec lane closing G-CIWORKFLOWSPEC-BRIEF at the collaborator's approval — every byte the builder writes, fenced; the brief's design whole carried, cited at every byte)

§0 THE GROUND, READ + CITED
- THE BRIEF (reports/synthesize/ci-design.md): §1 the shape (one file, two jobs, R4's triggers, MED-2's concurrency pick, the floor's five steps, the CodeQL steps, the trigger edges, the store-home clause); §2 the config (the positive form, the ruled-widening clause, HIGH-1's flip leg); §3 the ruff landing (the authored bytes, MED-3's hikari sequence, the emission-pending refusal); §4 the README (the three lines + the push story); §5 the one-unit ruling (the per-file order, one gate, one commit).
- THE CENSUS: reports/census/actions-free-forms.md §2 (the workflow grammar), §3 (setup-uv — python-version sets UV_PYTHON overriding .python-version, hence UNSET; enable-cache: auto; checkout before setup-uv), §4 (CodeQL — init@v4/analyze@v4, build-mode: none, the config-file form), §5 (make 4.3 on the runner image; steps run at the workspace root). reports/census/current-state.md §3 (the hook's :9-13 bytes, the 0/0/0 grep, the bypass), §4 (the Makefile targets :13-20, the 203-suite, the 200-drift at README:57), §5 (the hook never fires at the runner).
- THE TREE, READ AT THIS SEAT: Makefile (whole — test :13-14 "uv run pytest", lint :16-17 "uv run ruff check src/ tests/", typecheck :19-20 "uv run pyright"); .python-version (3.13); pyproject.toml (:6 requires-python ">=3.13", :43 ruff select=["ALL"], :162 pyright strict, :172 include ["src","tests"], :173 pythonVersion "3.13"); .githooks/pre-commit (whole — the current :9-13 note, :22 the ACM staging, :28 the pyright call, :29 the 0/0/0 grep, :18-20 the bypass); README.md (:57, :185, :189 read exact).

§1 THE WORKFLOW WHOLE — .github/workflows/ci.yml (fenced byte-exact; the builder writes these bytes and no others)

```yaml
name: CI

on:
  push:
    branches: [main]
  schedule:
    - cron: '0 3 * * 1'

concurrency:
  group: "${{ github.workflow }}-${{ github.ref }}"
  cancel-in-progress: true

jobs:
  floor:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - uses: astral-sh/setup-uv@v10.3.3
        with:
          enable-cache: auto
      - name: lint — ruff zero-findings
        run: make lint
      - name: test — pytest, the 203-suite
        run: make test
      - name: typecheck — pyright 0/0/0
        run: make typecheck

  codeql:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      security-events: write
    steps:
      - uses: actions/checkout@v6
      - uses: github/codeql-action/init@v4
        with:
          languages: python
          build-mode: none
          config-file: ./.github/codeql/codeql-config.yml
      - uses: github/codeql-action/analyze@v4
```

§1a THE BYTES' WHYS (each cited):
- name: CI — the name the README's line carries (the brief §1).
- THE TRIGGERS — THE NO-PR LAW (R4) held byte-whole: push: branches: [main] + schedule: cron '0 3 * * 1' (weekly, Monday 03:00 UTC) ALONE; zero pull_request forms anywhere in the file; no PR-gated jobs, no PR-required checks; the loop's lands ride direct pushes (the brief/spec/build/verify pipeline IS the review); any future PR surface a ruled trigger at the collaborator's hand, never a silent workflow addition.
- THE CONCURRENCY (MED-2's ruled pick): the workflow-level group "${{ github.workflow }}-${{ github.ref }}" + cancel-in-progress: true; NO schedule guard — the floor job carries no event filter, every run (push and cron alike) runs the whole floor. THE REASON (the brief §1): a cron cancelling a mid-push run itself carries the floor on the same ref (its checkout includes the pushed commits — the orphan dies), and the weekly cron runs ruff/pyright/pytest (drift blindness dies); the split-group alternative weighed and declined; the cost ~3 free min/wk — R1's arithmetic untouched.
- THE FLOOR JOB: runs-on: ubuntu-latest (R1's free class). The steps, in order: (1) actions/checkout@v6 — before setup-uv (the census §3); (2) astral-sh/setup-uv@v10.3.3 with ONLY enable-cache: auto in the with block — python-version UNSET (the configurability law: uv honors the tree's .python-version = 3.13 against requires-python ">=3.13"; the workflow re-declares nothing; the census §3 — python-version sets UV_PYTHON, overriding the tree's specs, the override refused by omission), version UNSET (the census's "" default), enable-cache: auto (on for hosted runners, keyed by the lock); (3) make lint; (4) make test; (5) make typecheck — the Makefile's targets the entrypoints, never re-declared commands (R2), each its own step naming the failing instrument (ruff — zero findings; pytest — the 203-suite; pyright — 0/0/0).
- THE CODEQL JOB: runs-on: ubuntu-latest; checkout@v6 -> init@v4 (with: languages: python, build-mode: none — buildless python, no autobuild; config-file: ./.github/codeql/codeql-config.yml) -> analyze@v4 — the census's current refs (v3 superseded — the brief §7.1).
- THE PERMISSIONS GRANT — the spec's ONE completion beyond the brief's enumerated steps, named never silent: the codeql job carries a job-scoped permissions block — contents: read (checkout's own grant), security-events: write (the SARIF upload — the analyze step's own act). THE REASON: the repo's default workflow-token is restricted (read-only — GitHub's standing default; the tree born 2026-11-19), and the analyze upload at a restricted token fails — the first live run would go red at the exact leg the unit's acceptance rides; the census's cited doc surface (§4, code-scanning customizing-advanced-setup) carries the advanced form WITH the grant. The floor job carries no permissions block (the restricted default's contents: read serves checkout). The collaborator strikes or keeps at the gate — a strike is a ruling (§7.1).
- THE TRIGGER EDGES (named once — the brief §1): tag pushes fire nothing (zero tags at HEAD; PyPI-era tags future ruled-trigger territory per R1's widening clause); forced pushes fire the push trigger (a push is a ref update); workflow_dispatch ABSENT (R4's letter closes the set — re-run serves the manual need); the landing push fires the first run.
- THE RUNNER-SIDE CLAUSES (the brief §1's named clause carried whole): the steps run at the workspace root (the Makefile at root — the census §5); uv auto-syncs on first run from the checkout's lock (the project installed editable — import prioritree resolves); STORE_HOME stays CWD-relative by its own law — NO workflow-side override (the configurability law); the suite never mints at the workspace anyway (every test takes tmp_path homes); .prioritree/ gitignored; CI never commits; the hook never fires at the runner (core.hooksPath is local config the clone never sets).

§2 THE CODEQL CONFIG WHOLE — .github/codeql/codeql-config.yml (fenced byte-exact)

```yaml
name: prioritree

# The positive form: only src/ and tests/ enter the scanner's world
# (mirroring pyright's include, pyproject.toml:172). The ruled-widening
# clause: future .py outside these paths enters the scanner's world only
# by a ruled widening (a config edit at a ruled hand, never a silent drift).
paths: [src/, tests/]
```

§2a THE NOTES: the positive form (the brief §2) — paths: [src/, tests/] mirrors pyright's include (pyproject:172); .plans excluded by construction (zero .py under .plans at HEAD — no ignore-list to rot); the ruled-widening clause rides as the comment in the brief's letter; the query suite stays CodeQL's default security suite (widening a ruled trigger per R1); the config is the tree's own triage form serving the alerts (FR-MEM-0033's lesson — R2).

§3 THE HOOK'S SOURCE BYTES — the hikari delivery-note (the collaborator's hand; the unit's opening act per MED-3; never a hand-edit of the emission — the generated-files law)

§3a THE AMENDMENT — the authored replacement bytes (the design brief §3's authored form, byte-exact; the phase-2 note's new text):

```
# PHASE 2 (landed at CI, 2026-11-23): ruff zero-findings is enforced by the CI workflow's lint step (make lint + make typecheck — the whole floor); this hook stays local-fast pyright — the standing division: the hook the commit backstop, CI the gate. The zero-ignore LAW stands: a new ignore is a ruling, never a convenience.
```

§3b THE EXPECTED LANDED EMISSION (.githooks/pre-commit:9-13 — the replacement occupies the same five lines; the current emission's own wrap style, ≤72 columns, comment-prefixed; the generator's exact wrap points confirm only at the landed emission — named honestly, this seat's reads stop at the tree's edge):

```
# PHASE 2 (landed at CI, 2026-11-23): ruff zero-findings is enforced by
# the CI workflow's lint step (make lint + make typecheck — the whole
# floor); this hook stays local-fast pyright — the standing division:
# the hook the commit backstop, CI the gate. The zero-ignore LAW stands:
# a new ignore is a ruling, never a convenience.
```

§3c THE SOURCE FILE (the amendment's home, cited by absolute path): /Users/marklosey/projects/kepric/hikari/scripts/generation/sources/prioritree-seats.yaml — the hook template's phase-2 note block within it (the authored source this tree's own generated headers name — AGENTS.md's header "from scripts/generation/sources/prioritree-seats.yaml"; the hikari-side read at the dispatch confirms the block's exact lines).

§3d THE REGEN COMMAND (run at hikari's root, /Users/marklosey/projects/kepric/hikari): uv run python scripts/generation/clarity_scaffold.py --target prioritree (the engine stays home; the emission lands at prioritree's .githooks/pre-commit).

§3e THE DELIVERY NOTE'S STEPS, IN ORDER:
1. THE SOURCE EDIT: the phase-2 note block at §3c's file replaced by §3a's bytes (hikari's own commit, cited by absolute path; never a hand-edit at this tree).
2. THE REGEN: §3d's command at hikari's root.
3. THE EMISSION LANDS HERE: the regen writes this tree's .githooks/pre-commit — the :9-13 block now §3b's expected form; the hook's mechanics byte-identical (the ACM staging :22, the pyright call :28, the 0/0/0 grep :29, the bypass :18-20 — untouched).
4. KENSHO VERIFIES THE LANDED BYTES: the landed :9-13 against §3a's authored form (content-identical; §3b's wrap the expected reading) — the emission-pending leg refused (the brief §3: the verification names landed bytes, never a promise).

§4 THE README'S LINES — one pass, the same file-touch (three edits, before/after fenced byte-exact; each edit swaps the fenced sentence(s) within the line, the lines' other bytes untouched)

§4a :57 — the drift folded (the suite at 203; current-state §4):

```
before: The quality floor: 200 tests green, pyright clean, ruff clean.
after:  The quality floor: 203 tests green, pyright clean, ruff clean.
```

§4b :185 — the precondition's remainder closed (CI landed; the publish itself still the outward lane's ruled act per R3's inward-first direction):

```
before: The publish is deferred: the license and the packaging have landed; CI remains.
after:  The publish is deferred: the license, the packaging, and CI have landed; the publish itself remains the outward lane's ruled act.
```

§4c :189 — the CI-live line naming the workflow + the direct-push story per the no-PR law (the PR form has no grammar here; moho's fix 3 re-shaped — the PR-story fix struck):

```
before: CI is deferred — the git hook and the local gates stand in.
after:  CI is live (2026-11-23): the CI workflow (.github/workflows/ci.yml) runs the quality floor — ruff, pytest, pyright — at every push to main and weekly, and CodeQL scans under the tree's own config (.github/codeql/codeql-config.yml); the loop's lands ride direct pushes to main and the workflow runs green at each push — the PR form has no grammar here; the git hook stays the local backstop.
```

(:189's line-tail "The quality floor: 203 tests green, pyright clean, ruff clean." already correct at HEAD — untouched.)

§5 THE NO-BREAK PROOFS (the landing breaks nothing)
1. THE FLOOR STANDING AT 203: the workflow adds zero Python — the two landed files are YAML (outside pyright's include pyproject:172, outside ruff's src/+tests/ scope); the README's edits are prose; the hook's amendment is a bash comment block; the suite unchanged at 203, ruff zero-findings, pyright 0/0/0 — the same floor the workflow then enforces (the floor's three instruments read the same world as before the landing).
2. THE MAKEFILE BYTE-UNTOUCHED: the workflow calls the targets (make lint / make test / make typecheck), never re-declares commands (R2); the Makefile is not in the unit's diff — byte-identical before and after.
3. THE HOOK'S LOCAL FORM UNTOUCHED BY THE TREE-SIDE LANDING: the tree-side commit never hand-edits .githooks/pre-commit (the generated-files law; the hook's own header "regenerated at will, never hand-maintained"); the note's amendment rides the source edit + the regen — the emission the delivery; the standing division lands as named: the hook the commit backstop, CI the gate.

§6 THE PER-STEP PLAN (R8, the file-unit; the brief §5's order — the references earn it; the whole unit lands as ONE commit)
- STEP 1 — .github/codeql/codeql-config.yml (§2's fence, byte-exact): first — the workflow references it; the referenced file exists before the referencing file.
- STEP 2 — .github/workflows/ci.yml (§1's fence, byte-exact): second — it references the config.
- STEP 3 — the hikari delivery-note (the collaborator's hand): §3e's four steps in order (the source edit -> the regen -> the emission lands here -> kensho verifies the landed bytes) — the unit's opening act (MED-3's member-path precedent).
- STEP 4 — the README's lines (§4's three edits, one pass, the same file-touch).
- STEP 5 — the floor: make lint + make test + make typecheck locally green (the 203-suite, zero findings, 0/0/0 — §5's proof read back at the tree before the push).
- STEP 6 — the first live run + the flip attestation + kensho's verification at the gate: the unit's one commit lands (one-commit-per-increment; piecemeal leaves in-between states — the workflow green while the note still says pending, the README still deferred); the landing push fires the workflow; the collaborator's read-back at GitHub's Actions surface (both jobs green); the flip attestation same-turn (HIGH-1's blocking leg — the default setup disabled at their GitHub hand at Code Security settings; the advanced config the owner; unnamed, the gate cannot go green — never the silent inheritance); kensho's independent verification at the build gate (every landed file byte-against-spec + the landed hook emission + the flip attestation recorded).

§7 THE OPEN QUESTIONS NAMED (the collaborator rules at the gate)
1. THE PERMISSIONS GRANT (§1a): the spec's one completion beyond the brief's enumerated steps — kept (the first-run green depends on it) or struck (a strike is a ruling; the first run then carries the named risk).
2. THE EMISSION'S WRAP POINTS (§3b): the generator's exact wrap confirms only at the landed emission (the hikari-side read at the dispatch confirms the source block's lines); the content-identity the verification's bar — a wrap variance named at the verification, never a silent pass.
3. THE BRIEF'S OWN TWO (carried, ruled at the brief's gate — not this spec's scope): the quickstart's lint/typecheck widening (the brief's open question 1); the public-form pricing confirmation (the brief's open question 2).
## Reported by togo — 2026-11-24T01:02:03Z

R6 fold — ci.yml least-privilege regions (findings verified 2026-11-24):
(a) workflow-level, INSERT after ci.yml:11 (concurrency end), before :13 (jobs:):
    + permissions:
    +   contents: read
    (after: concurrency → blank → permissions: contents: read → blank → jobs: — every job inherits unless overridden)
(b) codeql job ci.yml:30-32 — VERIFIED PRESENT, before = after (no change): the job-scoped block already carries BOTH contents: read + security-events: write (job-level replaces workflow-level whole).
