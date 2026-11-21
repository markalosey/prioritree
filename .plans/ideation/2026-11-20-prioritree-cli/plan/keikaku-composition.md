# plan/keikaku-composition — THE PRIORITREE-CLI ROUTE'S COMPOSITION (the proposal; the validation record rides §VI)

- Provenance: keikaku (計画, plan), packet compose/prioritree-cli-route, route prioritree-cli, 2026-11-20 — the ground read first (six reads: the birth store's route, the core store's route, CONTINUATION.md, session.py whole, pyproject.toml, the born junro.json); the composition returned in-message (one transit truncation recovered by session resume); nothing recorded via route ops before the validation — the validation gates the recording.

## I. THE GROUND, CONFIRMED

- **The frozen door** (session.py, read whole): Session(registry) — the registry injected, the ledger constructed internally; five ops only: register_run / next_pair (or ExhaustedQueue raised) / cast_vote / read_vote_state / tally_rank (or TallyRefusedError verbatim); ONE refusal grammar at the surface; ExhaustedQueue the DONE signal "caught BY TYPE by the wrappers" — the session's own docstring names the CLI as exactly this: the first wrapper. The core is SINGLE-PROCESS by contract, in-memory, no files, no DB — the persistence question lands wholly at this tier.
- **The floor** (pyproject.toml): dependencies = [] — argparse stdlib, never typer/click; ruff ALL + named rulings only; pyright strict 0/0/0; no [project.scripts] entry yet — the CLI wires it.
- **The core whole and green** (CONTINUATION.md): six units, 63 tests at close, the measured bar at k=3; Q-setup-arch's stack ruled — "the CLI wraps it"; the birth ruling priced: "pure logic at birth, no DB — persistence is a service-tier design ruling" (the tier that needs persistence owns its ruling — the CLI tier now stands here).
- **The engine's pairing model** (the core store, amendment 8): build gates minted manually with rich conditions BEFORE the build adds; each build-add auto-stamps its unit's pair (synthesize/<unit> + G-<UNIT>-BRIEF); this store is empty — the clean path, no amend flow, no voids.
- **The standing doctrines**: the exact-task law; single-goal dispatches; the naming law; the no-shell law; patch the one mutation verb; one-commit-per-increment through the tree's own git instrument.

## II. THE STAGES — pipeline, build, close (composed at the recording)

- **pipeline**: the per-unit pipeline law — discover → understand → synthesize before build; the precedence: no build dispatch until its brief gate is green.
- **build**: the CLI's build per the ruled unit decomposition — run-store, command-face, cli-acceptance; the exact-task law at each unit.
- **close**: the bookend — CONTINUATION.md's CLI entry, the next candidates staged, the done call at the collaborator's ruling.

## III. THE UNITS AND THE GATES

- **run-store** — the persistence seam (THE load-bearing unit): synthesize/run-store (togo, G-RUN-STORE-BRIEF) + build/run-store (jikko, G-RUN-STORE). Scope: the wrapper-tier file-backed persistence surface per Q-cli-persistence's ruling — the flat JSON run store (the manifest written once at register, the vote log appended per cast, the load path reconstructing the library state per invocation, the corrupt-file refusal); the core stays in-memory, zero-dep, untouched.
- **command-face** — the five subcommands over the frozen door: synthesize/command-face (togo, G-COMMAND-FACE-BRIEF) + build/command-face (jikko, G-COMMAND-FACE). Scope: the argparse subcommand tree mapping 1:1 onto the five ops (register/next/vote/state/tally), the console-script entry ([project.scripts] — the pyproject edit rides this unit), the I/O contract per Q-cli-io's ruling (exit codes 0/1/2, the report shapes).
- **cli-acceptance** — the e2e bar: synthesize/cli-acceptance (togo, G-CLI-ACCEPTANCE-BRIEF) + build/cli-acceptance (jikko, G-CLI-ACCEPTANCE). Scope: the deterministic end-to-end harness — fixed-argv subprocess invocations (the no-shell law), the full arc across process boundaries, the refusal arc at its exit code, the SAFE HALT whole.
- **close/cli-records** — owner shinko, gate G-CLI-RECORDS (collaborator-ruling): records-synthesis (togo) → records-landing (shinko) → done-call (shinko, the collaborator's ruling recorded same-turn).
- **The gates' full conditions**: recorded at the route's gates (G-RUN-STORE, G-COMMAND-FACE, G-CLI-ACCEPTANCE — deterministic-check, four conditions each; G-CLI-RECORDS — collaborator-ruling, three conditions).

## IV. THE PER-UNIT PIPELINE LAW — restated

+Each unit's discover → understand → synthesize BEFORE its build. Discover/understand ride ungated packets (tansa's census, rikai's mechanisms); the synthesis is the gated increment — togo's brief at G-<UNIT>-BRIEF, the collaborator's approval the gate, the fenced bytes at togo's hand. THE PRECEDENCE: no build unit's dispatch fires until its brief gate is green. Single-goal dispatches throughout; the four-leg floor rides every build unit.

## V. THE FIVE COMPOSITION QUESTIONS — the [PROPOSED] defaults and the rulings

+1. **Q-cli-shape** — [PROPOSED] subcommands only, 1:1 on the five ops (both comparator classes served mechanically; the interactive session banked for a later widening). **RULED at the validation (the collaborator's "proceed", 2026-11-20): the default whole.**
+2. **Q-cli-persistence** — [PROPOSED] file-backed, a flat JSON run store, NEW wrapper-tier surface (the subcommand shape demands state across exits; the core untouched — "no DB" held; the tier owns its store). **RULED: the default whole** — the zero-persistence alternative priced and rejected.
+3. **Q-cli-granularity** — [PROPOSED] three units + the close (three distinct falsification sets). **RULED: the default whole.**
+4. **Q-cli-acceptance** — [PROPOSED] yes, the e2e unit through the real argv surface. **RULED: the default whole.**
+5. **Q-cli-io** — [PROPOSED] argv in, stdout out; exit codes 0/1/2 (0 success AND DONE — the tally pointer; 1 the refusal lineage, the three-field rendering; 2 the unexpected). **RULED: the default whole.**

## VI. THE VALIDATION AND THE RECORDING (the record)

+The composition validated by the collaborator at the "proceed" ruling (2026-11-20) — the five defaults approved wholesale, each recorded as its question's ruling same-turn. The recording (shinko's hand at the junro, the core store's precedent): the five questions + rulings → the four manual gates (G-RUN-STORE, G-COMMAND-FACE, G-CLI-ACCEPTANCE, G-CLI-RECORDS) → the three stages (pipeline, build, close) → the close increment (close/cli-records) → run-store's build-add (auto-stamping synthesize/run-store + G-RUN-STORE-BRIEF — the pairing model held, the clean path). THE ROUTE'S FIRST MOVEMENT: run-store's pipeline (discover → understand → synthesize → G-RUN-STORE-BRIEF at the collaborator's approval); the build dispatch waits for the brief gate's green.

+*Provenance: keikaku (計画, plan), packet compose/prioritree-cli-route, route prioritree-cli, 2026-11-20 session. Read-only held — the composition returned in-message; archived by shinko via patch under the landing discipline. The tree is the truth.*
