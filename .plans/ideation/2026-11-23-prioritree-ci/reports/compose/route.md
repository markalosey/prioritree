<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — compose/route

**Route:** prioritree-ci (composed) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T22:29:07Z |
| 2 | report | keikaku | 2026-11-23T22:31:35Z |
## Reported by keikaku — 2026-11-23T22:31:35Z

# THE COMPOSITION — prioritree-ci's opening route (keikaku, 2026-11-23)

The opening whole: 3 stages, 3 gates, 2 increments, 7 ungated placements. The census is placed FIRST; NONE of its findings is assumed by this composition (the census-first law — Q-ci-surface R3). The build units are named, not pinned — the unit map is ruled by the census and the design at their turn (do not pre-pin what the census could overturn; the mcp route's "named not pinned" form).

## THE STAGES

**pipeline** — THE PER-UNIT PIPELINE (the standing form, the ux/mcp precedents): THE CENSUS FIRST — ungated tansa/shindan/rikai/keisan packets over the CI ground (GitHub Actions' free forms, the current state, the mechanisms, the free-tier pricing); then THE DESIGN LANE — ungated suisen/hyoka/moho packets; then togo's gated synthesis closing G-CI-DESIGN-BRIEF; each build unit's ungated discovery legs + gated brief precede its build; THE ROUTE GROWS UNIT-BY-UNIT (the build-add auto-stamps the brief pair; the spec lane rides the unique suffix — the two-lane standing shape). ENTRY: G-COMPOSITION is green (the composition validated at the route's head); the census fires first, its findings assumed by none of this composition.

**build** — THE CI SURFACE'S BUILD: the units the census and design earn — the LIKELY SET, named not pinned: ci-workflow (the floor job in Actions riding the Makefile's targets as entrypoints — make test/lint/typecheck, R2; the CodeQL config owned by the tree — R2 + FR-MEM-0033; the hook's phase-2 note amended to name CI as the enforcement's home — R2, the amendment riding the hook's generator source, never a hand-edit) — the census/design RULE the unit map (one unit whole or split). One module per dispatch (R8, the file-unit), each landing per its approved brief (the exact-task law), kensho's independent verification per build gate, one-commit-per-increment; the FREE-TIER law held on every surface (R1 — nothing that bills). ENTRY: G-CI-DESIGN-BRIEF is green — the design is the spec; each unit's own G-<UNIT>-BRIEF green before its dispatch (the precedence law).

**close** — THE EFFORT'S BOOKEND (the standing form): hansei's retro (the friction ledger the intake), the effort's records (the CONTINUATION entry; the inward direction named next — auth first, the order-bias probe second, outward/PyPI after inward, R3 — banked, not composed), the done call at the collaborator's ruling. ENTRY: the route's build gates closed green and the collaborator has called the close.

## THE GATES

**G-COMPOSITION** (collaborator-ruling):
1. the composition lands at the store's reports home (reports/compose/route.md — keikaku's own report, the composition whole: stages, gates, increments, the ungated placements, the application order) — the opening whole, the census placed FIRST with none of its findings assumed, every seat placed (R3: no seat bypassed)
2. every choice cites its ruling: Q-ci-surface's three (R1 the free-tier law, R2 the configurability carry + the ruff phase-2 landing + the CodeQL ownership, R3 the governance form + the inward direction) + the standing laws carried (R6/R11 the seat-authored report, R8 the per-step file-unit dispatch, the two-lane form, the ThreePart, the census-first)
3. the collaborator validates the composition — the gate is the validation; the outcome records against compose/route; no route dispatch fires before it is green

**G-CI-DESIGN-BRIEF** (collaborator-ruling):
1. THE DESIGN BRIEF LANDED: togo's synthesis over the census (census/actions-free-forms, census/current-state, census/mechanism, census/pricing) + the design lane (design/workflow, design/adversarial, design/cold-clone-walk); a divergence that survives reconciliation blocks the brief, never rides silently (the pipeline-parallelism safeguard)
2. the brief carries the design-work whole the rulings leave open — never settled in the composition: the workflow's shape (the floor job's steps — checkout, uv's workflow-native setup, the make targets as entrypoints; the store home CWD-relative at the runner — R2), the CodeQL config's form (the free default setup's own configuration: the languages, the query suite, any path excludes — R2 + FR-MEM-0033's triage form), the ruff phase-2 landing (the lint step enforcing the whole floor — ruff + pyright; the hook's note naming CI as the enforcement's home — R2; the amendment riding the generator's source, the generated-files law), the UNIT MAP (one unit whole or split — the census/design's ruling), and the free-tier pricing's verdict (R1: nothing that bills — every surface priced within the free tier)
3. THE COLLABORATOR'S APPROVAL: the design judged ready-to-build; the build units' briefs cite it; their dispatches fire only after their own brief gates green

**G-CLOSE** (collaborator-ruling):
1. hansei's retro landed: the debrief over the effort whole, the friction ledger the intake, the lessons named
2. the effort's records landed: the CONTINUATION entry (the landing state named honestly); the inward direction named next (auth first — the write-exposure cure, Q-auth-widening's reframe; the order-bias probe second; outward/PyPI after inward — R3, banked not composed)
3. the collaborator rules the close — the done call recorded same-turn; the route's status set done at the ruling

The per-unit gates mint at their turns (NONE pre-pinned here): the build-add auto-stamps G-<UNIT>-BRIEF + synthesize/<unit> (the unit-brief lane); the spec lane rides the unique suffix G-<UNITSPEC>-BRIEF (the exact-task bytes at synthesis — FR-MEM-0011's doctrine); the build gate G-<UNIT> (deterministic-check) carries the unit's floor-green + kensho's independent re-run (validate/<unit>) — the two-lane standing shape.

## THE INCREMENTS

- **synthesize/ci-design** · owner togo · gate G-CI-DESIGN-BRIEF — steps: [synthesize · semantic · togo · gate]
- **close/retro** · owner shinko · gate G-CLOSE — steps: [retro · semantic · hansei · assessment], [records-synthesis · semantic · togo · assessment], [records-landing · semantic · jikko · assessment], [done-call · semantic · shinko · assessment] (the mcp route's close form — the latest precedent)

The build increments mint at their build-adds, per the unit map the census/design rule.

## THE UNGATED PLACEMENTS (dispatched by shinko, ungated by design)

THE CENSUS FIRST (R3's discover/diagnose trio + the pricing ground):
- **census/actions-free-forms** — tansa: the inventory — GitHub Actions' free forms (the ubuntu-latest runner's free class, the workflow-native uv setup — astral-sh/setup-uv or the curl form — via the web tools if granted at the pack, or the tree's own pyproject/uv usage as the ground)
- **census/current-state** — shindan: the diagnosis — the current CI state (no .github/ at HEAD, glob-verified; the CodeQL default setup live per FR-MEM-0033, the first finding's triage form recorded; the hook's phase-2 state — .githooks/pre-commit: pyright only, ruff "PHASE 2 (named, pending)")
- **census/mechanism** — rikai: the understanding — the mechanics (the CodeQL default setup's engine composing with an owned config; the workflow/trigger/runner forms; the uv provisioning's mechanics at the runner)
- **census/pricing** — keisan: the free-tier arithmetic — the floor's ~26s runtime vs the free minutes (R1's "minutes-scale, never an issue" priced, not assumed), the CodeQL free form's limits, the suite's runtime at the runner

THE DESIGN LANE:
- **design/workflow** — suisen: the recommendation — the workflow's shape (the floor job's steps [checkout, uv, the make targets as entrypoints], the CodeQL job's config form, the ruff-phase-2 landing, the hook's note amendment)
- **design/adversarial** — hyoka: the adversarial pass over the design
- **design/cold-clone-walk** — moho: the cold repository's clone-to-CI experience — the fresh-clone story the workflow serves (R3's own placement)

## THE APPLICATION ORDER

G-COMPOSITION validates this composition (this report the evidence; the outcome recorded against compose/route) → the census fires (four packets, parallel, ungated) → the design lane (three packets, ungated, over the census's findings) → togo's synthesis closes G-CI-DESIGN-BRIEF (the design + the unit map ruled) → the build units' lanes mint at their turns (brief → spec → build; per-step, the file-unit; kensho independent per build gate) → the collaborator calls the close → hansei's retro, the records (the inward direction named), the done call.

## THE LOAD-BEARING DECISIONS (each citing its ruling)

1. The three-stage spine (pipeline/build/close) + the head G-COMPOSITION — the standing form (the ux/mcp precedents), R3's every-seat mandate realized.
2. The census FIRST, ungated, none of its findings assumed — the census-first law (R3; the precedents' pipeline entry-condition verbatim).
3. keisan's pricing placed in the CENSUS, not the design lane — the free-tier arithmetic is GROUND the design must fit (R1 the free-tier law), not a design output; the ux/mcp precedent's keisan-in-design-lane shape amended by this effort's own constraint.
4. rikai's census/mechanism placed — R3's discover/diagnose trio whole; no seat bypassed (every seat placed: keikaku composes, the census four, the design three, togo synthesizes, jikko builds, kensho verifies, hyoka attacks, moho walks, hansei debriefs, shinko dispatches).
5. moho's design/cold-clone-walk in the design lane — R3's verbatim placement (the cold repository's clone-to-CI experience, the fresh-clone story the workflow serves).
6. The build units named NOT pinned: ci-workflow the likely set; the unit map (one unit whole or split) ruled at G-CI-DESIGN-BRIEF — the composition composes only what the rulings pin; over-composition refused.
7. The two-lane form rides per unit (brief → spec → build), the gates minting at the unit's turn — R3's standing laws; the ux route's auto-stamp + unique-suffix precedent; NONE pre-pinned.
8. The hook's phase-2 note amendment rides the GENERATOR'S SOURCE (the hook is cycle-generated — its own header names hikari and the regen), never a hand-edit — R2's "the hook's note amended" + the generated-files standing law; the unit's scope names the regen as the act.
9. The workflow rides the Makefile's targets as entrypoints and the store home CWD-relative at the runner — R2 the configurability carry (a design-brief condition, never settled in the composition).
10. The close's records name the INWARD direction next (auth first, the order-bias probe second, outward/PyPI after inward) — R3; banked, not composed.
11. Two increments only pre-composed (synthesize/ci-design, close/retro) — the composition model: the build increments mint at their build-adds (the ux/mcp precedents' opening shape).

— keikaku (計画), the composition AS the report (R6/R11: the seat-authored report; the record never rides the return channel).
