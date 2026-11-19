# plan/keikaku-composition.md — the prioritree-birth route, composed

**Packet:** compose/prioritree-birth-route · **Actor:** keikaku · **Date:** 2026-11-19
**Store:** `/Users/marklosey/projects/prioritree/.plans/ideation/2026-11-19-prioritree-birth` (status: **composed**, amendments 6 → 17)

## 1. The route's shape

```
STAGE build  (entry: the three birth rulings stand — Q-purpose, Q-setup-arch, Q-harness, ruled
              2026-11-19 — the composition is validated by the collaborator, and the first
              unit's dispatch fires; NO build dispatch until its unit's brief gate is green)
│
├─ build/foundations — owner jikko @ G-FOUNDATIONS (deterministic-check, 5 conditions)
│    steps: project-floor (pyproject + .python-version + uv.lock + .gitignore + README —
│    Q-purpose's ruled description) → src-skeleton (the src/prioritree namespace, skeleton
│    only, NO product logic — the core library is the PRODUCT effort's first increment) →
│    tooling-floor (ruff + the ruled type-check config + pytest floor + Makefile floor
│    dev/test/lint; the collaborator's hand sets core.hooksPath=.githooks) → floor-green
│    (deterministic: make dev && make test && make lint)
│    PIPELINE (engine-stamped): discover/foundations → understand/foundations →
│    synthesize/foundations (togo) @ G-FOUNDATIONS-BRIEF
│
└─ build/harness — owner jikko @ G-HARNESS (deterministic-check, 5 conditions)
     steps: targetspec-adapter (the third TargetSpec + prioritree-seats.yaml adapter land
     in HIKARI's scripts/generation/ — the hikari-side landing rides hikari's shinko-git
     choreography) → sibling-contracts (deterministic: the clarity + input --check
     byte-compares — the siblings' bytes are the falsifier) → emission-run (deterministic:
     --target prioritree from hikari's root, the collaborator's regen hand) → emission-check
     (deterministic: --target prioritree --check exits 0) → friction-store-birth (the
     friction store born at prioritree's store home + the LIVE proof: a verbatim fixed-five
     tool call answering at a prioritree seat)
     PIPELINE (engine-stamped): discover/harness → understand/harness →
     synthesize/harness (togo) @ G-HARNESS-BRIEF

STAGE close  (entry: G-FOUNDATIONS and G-HARNESS closed green + the collaborator calls the close)
│
└─ close/birth-records — owner shinko @ G-BIRTH-RECORDS (collaborator-ruling, 4 conditions)
     steps: records-synthesis (togo — prioritree's first CONTINUATION.md entry: the birth
     record; hikari's family-growth line: the FIVE-TREES record; the next effort named) →
     records-landing (shinko — prioritree's records through the collaborator's hand;
     hikari's through hikari's shinko-git choreography; the product effort's store birth
     recorded) → done-call (the route's status set done at the collaborator's ruling)

STAGE pipeline  (engine-stamped by construction — amendment 19's law, verified live:
                 PIPELINE_STAGE_ID = "build" at junro.py:180, the FR-MEM-0184 trap avoided)
│
├─ synthesize/foundations — togo @ G-FOUNDATIONS-BRIEF (collaborator-ruling, the engine's
│                          two-condition template: the brief landed + the collaborator approves)
└─ synthesize/harness    — togo @ G-HARNESS-BRIEF (the same shape)
```

**The gate teeth:** G-FOUNDATIONS holds the zero-errors-AND-zero-warnings bar on every leg (uv sync, the smoke suite, ruff, the ruled type checker, make dev/test/lint, the records read-back including the `.git/config` hooksPath). G-HARNESS holds the falsifiers: the sibling byte-compares (`--target clarity/input --check` exit 0 — the shared core must serve three targets without moving the existing two), the prioritree `--check` exit 0, the inventory read-back whole (13 seat blocks, builtins disabled, shinko primary, the closed-world deny, the goal line verbatim, the fixed five, the 13 prompts, the executable hook), the LIVE registration proof, the friction store born, and the two-tree hands honored in the landing record. G-BIRTH-RECORDS is the collaborator's own gate.

## 2. The composition factors judged

- **Complexity: two small units, one real coordination axis.** The work itself is thin (a skeleton; a parameterized emission — the family's own record: "the fifth tree is config not code: a store seed, an adapter, a goal-line ruling, two commands"). The sizing signal went to the **two-tree split**: the TargetSpec + adapter are HIKARI-side edits (hikari's instruments, hikari's landing choreography); the foundations + the emission's output + the friction store are PRIORITREE-side (the collaborator's hand — no own landing rule exists at birth). Every hand is named inside the increments and gates.
- **The pipeline law carried by construction, not by discipline.** The build stage is named `build` deliberately so the engine stamps each unit's discover → understand → synthesize @ its brief gate (confirmed live: the OK lines carry `pipeline stamped: G-FOUNDATIONS-BRIEF + synthesize/foundations`). The michigan route's silent forfeit (FR-MEM-0184) is the avoided trap. The close unit correctly takes NO pipeline stamp — a records bookend is not a build unit.
- **Discovery-before-build, as ruled.** Q-harness's ruling names ONE discovery question; it is carried as the store's open question Q-tool-registration and rides build/harness's discover leg — G-HARNESS condition 4 holds the live proof (a verbatim tool call) and refuses the emission firing before the answer.
- **Sequencing by gate, not by stage count.** Foundations before harness is load-bearing: the emission lands `.githooks/pre-commit` whose strictness flags ride the tree's own pyproject, and the `.gitignore`'s derived-view entries must precede the emission. The dependency rides G-HARNESS condition 1 (G-FOUNDATIONS closed green).
- **The product boundary held.** Q-setup-arch: the setup builds the SKELETON only; the core library (items, comparison operator, pair scheduling, votes, tally) is the PRODUCT effort's first increment — composed nowhere in this route, named only at the close.
- **No CI increment** (deferred per the ruling — git hooks and the local gates stand in); **no DB** (pure logic at birth).

## 3. The open questions held for the collaborator

1. **Q-tool-registration** (open; the ruled carry from Q-harness): what mechanism makes `.opencode/scripts/*.py` callable as the `calculate/curate/patch/friction/test` tool ids at the sibling (no `tools/` wrappers visible), and what must the prioritree emission carry so the fixed five actually register? Resolves at build/harness's discover/understand legs; G-HARNESS holds the live proof.
2. **Q-typecheck-alignment** (open; surfaced by this composition — a real tension between two ruled/banked shapes): the foundations' `ruff + mypy` config vs the family pre-commit template's `uv run pyright` 0/0/0 check. Measured datum: kepric-input's own pyproject carries NEITHER (ruff + pytest only) — the family has no resolved precedent at the derived trees. Options banked in the question: (a) adopt pyright, (b) carry both, (c) parameterize the hook per-target in the TargetSpec. **The ruling must land before the emission fires** — G-HARNESS-BRIEF is the natural checkpoint.

Two further datums ride the harness discover leg as census scope (not questions — sibling-state facts to confirm, not rule): the derived-view gitignore shape at the siblings (kepric-input's root `.gitignore` carries `.junro/` but no `.opencode/` entries; kepric-clarity has no root `.gitignore` at all), and the friction store's home + birth mechanism (kepric-input carries NO `.junro/friction-ledger.jsonl` — the ledger apparently births at first write).

## 4. What fires first

The collaborator validates this composition → **tansa's census for the foundations unit** (packet discover/foundations — thin: the sibling skeleton precedents, the banked file set) → rikai's mechanisms → togo's brief → **G-FOUNDATIONS-BRIEF green at the collaborator's approval** → the foundations dispatches (jikko, the exact-task law, the brief cited) → kensho's G-FOUNDATES… G-FOUNDATIONS verification. The harness unit's discover leg carries the two questions' resolution; its brief gate is where Q-typecheck-alignment lands. The close fires last, at the collaborator's call. All landings: hikari-side through hikari's shinko-git choreography; prioritree-side through the collaborator's hand until prioritree's own harness + landing rule exist.

## 5. The ops executed, with the store's OK confirmations verbatim

All ops actor=keikaku, `--store /Users/marklosey/projects/prioritree/.plans/ideation/2026-11-19-prioritree-birth`:

```
OK add-question 'Q-tool-registration' -> open (store: ...)
OK add-question 'Q-typecheck-alignment' -> open (store: ...)
OK add-gate 'G-FOUNDATIONS' (deterministic-check; conditions: 5; store: ...)
OK add-gate 'G-HARNESS' (deterministic-check; conditions: 5; store: ...)
OK add-gate 'G-BIRTH-RECORDS' (collaborator-ruling; conditions: 4; store: ...)
OK compose-stage 'build' (stages in the route: 1; store: ...)
OK compose-stage 'close' (stages in the route: 2; store: ...)
OK add-increment 'foundations' in stage 'build'; pipeline stamped: G-FOUNDATIONS-BRIEF + synthesize/foundations (store: ...)
OK add-increment 'harness' in stage 'build'; pipeline stamped: G-HARNESS-BRIEF + synthesize/harness (store: ...)
OK add-increment 'birth-records' in stage 'close' (store: ...)
OK set-route-status: composed -> composed (store: ...)
```

One refusal on the path, named as data: the first add-increment fired the step-schema refusal (my steps carried seat ids as `executor` and prose as `verification`); the refusal taught Part 1's actual schema (`executor: deterministic|semantic`, `tool` on deterministic, `member` on semantic, `verification: gate|assessment` — confirmed at grammar.py:191-229), and every step re-fired in the legal form. The store's record — 17 amendments, every op provenance-stamped — is the composition's evidence; no files were written outside the store.

**The route is composed and awaits the collaborator's validation.**
