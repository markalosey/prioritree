<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — design/workflow

**Route:** prioritree-ci (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T23:07:51Z |
| 2 | report | suisen | 2026-11-23T23:12:27Z |
## Reported by suisen — 2026-11-23T23:12:27Z

SUISEN'S CI WORKFLOW RECOMMENDATION (design/workflow, prioritree-ci, 2026-11-23)
1. SHAPE — ONE file (.github/workflows/ci.yml), TWO jobs in parallel lanes (the floor ~3 min beside
   CodeQL ~8 min — pricing). Triggers: push[main] + pull_request[main] + the weekly cron '0 3 * * 1';
   the floor job carries `if: github.event_name != 'schedule'` (push/PR only), CodeQL rides all
   three (actions-free-forms §4's form). Concurrency, workflow level: group
   "${{ github.workflow }}-${{ github.ref }}", cancel-in-progress: true — per-ref, superseded
   same-branch runs die early (mechanism §4; ~30-50% burst saving, pricing).
2. THE FLOOR JOB — runs-on: ubuntu-latest (R1's free class); steps: actions/checkout@v6 ->
   astral-sh/setup-uv@v10.3.3 -> make lint / make test / make typecheck, three steps (R2: the
   Makefile's targets the entrypoints, never re-declared commands; ruff ~8s fail-fast before
   pytest ~26s; make ships on the image — actions-free-forms §5). Ruff AND pyright both gate the
   job — R2's whole floor; separate steps name the failing instrument.
3. THE CODEQL JOB — checkout -> init@v4 (languages: python, build-mode: none, config-file:
   ./.github/codeql/codeql-config.yml) -> analyze@v4 — the docs' current ref, the census's v4
   over the map's v3; buildless python, no autobuild (mechanism §3).
4. THE SETUP-UV FORM — v10.3.3 TAG-pinned (the census's own pinned form, readable; a SHA move a
   future ruled hardening, never silent); python-version UNSET (uv honors .python-version = 3.13 —
   R2's configurability law, mechanism §1); enable-cache: auto (the census's form; ~110s cached
   vs ~165s cold — pricing).
5. THE CODEQL CONFIG — name + paths: [src/, tests/], the positive form mirroring pyright's include
   (pyproject:172). .PLANS RULED: EXCLUDED BY CONSTRUCTION — zero .py under .plans at HEAD,
   near-zero price either way (mechanism §3); provenance untouched by both (scanning reads, never
   writes); the positive form answers structurally — no ignore-list to rot; future .py under
   .plans a ruled widening. Query suite: CodeQL's default security suite (the priced form;
   widening a ruled trigger per R1).
6. THE OWNERSHIP TRANSITION (operational note, the collaborator's hand): landing the workflow does
   NOT disable the default setup — flip it manually at Code Security settings or duplicate results
   ride (mechanism §3; R2: never inherited silently).
7. THE RUFF-PHASE-2 LANDING — make lint + make typecheck gate the job (R2; ruff already zero on
   every recorded run — current-state §3). The hook's note amended at the HIKARI SOURCE (regen,
   never a hand-edit); exact bytes: "PHASE 2 (landed at CI, 2026-11-23): ruff zero-findings is
   enforced by the CI workflow's lint step (make lint + make typecheck — the whole floor); this
   hook stays local-fast pyright — the standing division: the hook the commit backstop, CI the
   gate. The zero-ignore LAW stands — a new ignore is a ruling, never a convenience." Hook
   mechanics unchanged; the regen lands it byte-identical.
8. THE README — one pass, three lines: :57 "200"->"203" (the census-named drift, FOLDED here — a
   two-character fix riding the same file-touch; a separate unit pure ceremony); :185 "CI remains"
   -> the landed form; :189 "CI is deferred" -> "CI is live" naming the workflow.
9. THE ONE-UNIT RULING — YES, one build-add whole: per-file dispatches within (R8's file-unit held:
   the config -> the workflow -> the hikari source + regen -> the README, the build order the
   references earn), the two-lane form within (discovery leg + brief, then the build), one gate, one
   commit. The surface is one design whole — the workflow references the config, the README and the
   hook's note name the landing; piecemeal leaves in-between states, every diff minutes-scale;
   kensho verifies the whole at the one gate.
