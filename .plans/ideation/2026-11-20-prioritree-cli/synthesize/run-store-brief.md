# synthesize/run-store-brief — THE RUN-STORE UNIT'S BUILD BRIEF (the exact-task spec)

**Status: PROPOSAL.** Togo proposes; the collaborator rules at G-RUN-STORE-BRIEF. Every [PROPOSED] element is an offered default with its one-line reason. The brief IS the spec (the exact-task law): once approved, jikko executes exactly, kensho re-runs independently.

## §0 THE GROUND — the rulings cited

- Q-cli-persistence (ruled): FILE-BACKED — a flat JSON run store, NEW wrapper-tier surface; the core stays in-memory, zero-dep, untouched ("no DB" held — a file is not a database).
- Q-cli-granularity (ruled): THIS unit alone — the persistence seam; the command face (argv, exit codes, report shapes) is the NEXT unit — nothing of it here.
- Q-cli-shape (ruled): subcommands 1:1 on the five ops — each cast its own process: §2's write-path ground.
- The fence (session.py:114-116): "no files, no subprocess, no DB; SINGLE-PROCESS by contract" — the store composes the door ONLY (Registry(), Session(registry), register_run, cast_vote — public only, the stores private); NO persistence verb added to the five-op door.
- The honesty-pin precedent cited (acceptance.py:24-27): byte-reproducibility asserted over the field-selected clock-free surface only (the wall-clock stamps named and excluded by construction), never the impossible full-log byte-identity.
- The laws riding: the naming law (name = the first word of the act-statement); content-in-configuration; store-as-parameter containers (never module-level singletons — test isolation); the refusal family grammar (expected/found/next_action, the Error-suffix lineage); the JSONL precedent (the friction ledger: append-only, one flat self-describing object per line); five-field docstrings; zero findings, zero ignores; one-commit-per-increment.

## §1 THE MODULE — layout, public surface, naming

- [PROPOSED] `src/prioritree/run_store.py` — the tree's flat precedent (six core modules + `__init__.py`, on disk); a NEW file, ZERO edits to any core module (the fence's "untouched" held at the file level). Tests: `tests/test_run_store.py` (the flat `test_<module>` precedent).
- [PROPOSED] The class `Persist` — priced by the naming law from the act "Persist the run state across CLI invocations" (the Session precedent: the act's first word names the symbol); store-as-parameter container, never a module-level singleton.
- The public surface (each name priced by its own act-statement; five-field docstrings on every symbol):

| symbol | act-statement (the naming source) | form |
|---|---|---|
| `Persist(session, handle, run_file)` | the container's own act | parts injected; the factories compose |
| `Persist.register(store_home, items, operator, quorum=1)` | "Register the run at the door and write its manifest line" | classmethod factory → `Persist` |
| `Persist.load(store_home, run_id)` | "Load the run's file into a fresh single-run session, refusing the corrupt file whole" | classmethod factory → `Persist` |
| `.cast(pair, winner, comparator_id, comparator_class, notes=None, supersedes=None)` | "Cast the vote at the door and append its line at the cast's return" | → the door's (vote_id, VoteRecord, count, acknowledged) verbatim |
| `.serve(seed=None)` | "Serve the next under-quorum pair" | → (item_a, item_b, count); ExhaustedQueue rides through BY TYPE |
| `.census()` | "Census the run's vote state" | → VoteCensus, the door's read verbatim |
| `.rank()` | "Rank the run by its tallied votes" | → TallyResult; TallyRefusedError rides verbatim |
| `.run_id` | "Run id — the file's name, the cross-process identity" | property → the file's stem (the EXTERNAL id, §3) |

- The composition is public-only: fresh `Registry()` + `Session(registry)` at the factories; the reads delegate through the door; the store never touches a core store attribute — the fence held by construction.

## §2 THE STORE'S MECHANICS — home, format, write path, ids

- [PROPOSED] The home: `STORE_HOME: Final[Path] = Path(".prioritree/runs")` — the named module-level constant (content-in-configuration); every verb takes the home as a PARAMETER (the constant is the command face's default, never a hidden global — test isolation).
- [PROPOSED] The file: ONE JSONL file per run, `{STORE_HOME}/RUN-{n:04d}.jsonl` — the single-run store form (rikai §1, the acceptance unit's own shape): the manifest line FIRST, then one vote line per cast in mint order. REJECTED: the single JSON doc (cannot append per cast without whole-doc rewrite — the crash window becomes the whole file; the JSONL precedent is the in-tree append form).
- [PROPOSED] The line bytes: the door's returned value serialized WHOLE — one flat self-describing JSON object per line plus a `kind` tag ("manifest"/"vote"); `json.dumps(..., sort_keys=True)` for deterministic bytes. Manifest line: kind, run_id, items ([[id, label], …], payload order preserved), operator (id, question, verdicts — the frozenset as a SORTED array on the wire: deterministic bytes, `frozenset` restored type-exact at re-register), quorum, registered_at (carried as data, §3). Vote line: kind, vote_id, the seven cast fields in mint order (run_id; pair as [item_a, item_b], canonical; winner; comparator_id; comparator_class; recorded_at as data; notes; supersedes). Type-exactness by construction: the wire carries plain JSON; the door re-derives every frozen type at register_run/cast_vote (the signatures accept the wire's arrays directly); the store never constructs a frozen value itself.
- [PROPOSED] The write path: SAVE-AT-CAST — the capture point at cast_vote's OWN return: the door appends in memory, the store appends the line (open-append, one write of one complete line + "\n", flush, close — one synchronous act); the manifest line lands at register_run's return, the same discipline. REJECTED: save-at-exit — under the subcommand shape each cast IS its own process (no later exit to defer to). The crash window is thereby bounded ≤ 1 cast, named honestly: a crash between the door's return and the append loses that cast (the file is the truth at load; `next_pair` re-serves the pair deterministically).
- [PROPOSED] The ack rule: `acknowledged=True` (the byte-identical re-send) appends NOTHING — the line is already durable (the dedup IS the idempotence; a double line would be absorbed loudly at replay anyway, R9 — the cleaner file wins).
- [PROPOSED] The failed append REFUSES loudly (three fields: expected the line; found the OS error verbatim; next_action the repair path) — never swallowed; `found` names the divergence (the cast lives in memory, not on disk).
- [PROPOSED] Single-writer BY CONTRACT (documented): one process writes a run's file at a time (the subcommand shape is sequential; the core is single-process by contract — the store its kin); no lockfile machinery at this tier (zero-dep). A concurrent double-write surfaces at the NEXT load as the id-sequence refusal — loud, never silent.
- [PROPOSED] The id ruling: the FILE-NAME mint is the store's own — the store-home scan (max RUN-{n} + 1), continuing post-load (the dir is the truth); the door's fresh-session mint cannot continue across files — named, the single-run form's own consequence. The vote ids and the in-file run_id are the door's verbatim values.

## §3 THE ROUND-TRIP PROPERTY — the equality surface (the honesty pin cited)

- The property: a run registered + cast + saved, then loaded into a fresh container, reconstructs the identical state OVER THE FIELD-SELECTED CLOCK-FREE SURFACE:
  - EQUAL, byte-identical before/after: the census MAPS (per_pair_counts, per_item_counts); the vote IDS (line i re-mints VOTE-{i+1:04d} — the single-run in-order replay reproduces them exactly, so every supersedes link and the tally's exclusion set survive); the seven cast fields per record; the manifest's value fields (items' payload order, operator, quorum); the TallyResult WHOLE (tally_votes consumes no stamp); the external id (the file's stem, unchanged by construction).
  - NAMED AND EXCLUDED: registered_at (re-minted at re-register), recorded_at (re-minted at each re-cast) — therefore the census's vote_log is NOT byte-identical; the assertion never claims it.
- THE JOIN'S DIVERGENCES, RESOLVED (the accepted-cost clause): (1) the stamps' carriage — the file carries the door's returned values WHOLE (the faithful record); the reconstruction uses the crossing fields; the equality surface excludes the stamps (ACCEPTED COST: two inert fields ride the file, validated for type, never for value). (2) G-RUN-STORE's "census byte-identical" against the door's ceiling — no public verb restores a stamp or sets a run_id; full-log byte-identity is unrepresentable through the door; RESOLVED: the condition carried in the acceptance unit's own ruled form — byte-identity over the clock-free fields only, the stamps named and excluded by construction (ACCEPTED COST: the property's assertion is field-selected, stated never implied).
- The two id spaces named, never conflated: the in-file run_id is the door's ephemeral single-run handle (RUN-0001, stable within the form — the round-trip's representation base); the file's stem is the run's cross-process identity. The dedup index: rebuilt at load (the re-casts ARE the rebuild — the key's members are the seven fields, neither stamp nor id; the file never carries it).

## §4 THE REFUSAL PATHS — the corrupt file, refused whole

- [PROPOSED] The type: `StoreRefusedError(expected, found, next_action)` — a NEW family member (the three-field grammar verbatim, the Error-suffix lineage; the store's OWN refusal — the door did not refuse, the FILE did; a distinct type keeps the lineage honest). The door's refusals and ExhaustedQueue ride through VERBATIM — the store wraps nothing.
- [PROPOSED] The pre-pass: parse + validate the WHOLE file BEFORE the first re-cast — never a silent partial load. The pre-pass reads the manifest line's declared sets AS DATA (cited, never re-derived).
- The trigger set (each in the three-field grammar; `found` carries the line number + the parser's message verbatim; `next_action` names the repair path): (1) parse failure — a line not well-formed JSON; (2) truncation — the crash-tail: the last line without its newline / half-written; (3) missing fields — a line lacking a grammar field; (4) wrong types — a field of the wrong JSON type; plus the value-set triggers (winner outside the manifest's declared verdicts; comparator_class outside {human, llm}; the pair's ids outside the manifest's items — the pre-pass guarantees the re-casts cannot refuse mid-rebuild; the door's own checks re-fire identically at the re-casts, never bypassed); (5) the orphaned supersedes — a reference not resolving to an EARLIER line, same run, same pair (stage 5's ground truth and the tally's silent hazard both foreclosed); (6) the id-sequence violations — line i's vote_id ≠ VOTE-{i+1:04d} (gaps, duplicates, disorder); a vote line's run_id ≠ the manifest line's; the manifest line not first / duplicated.
- The missing FILE at load: `StoreRefusedError` (expected a run file in the store home; found the home's live set rendered; next_action register or cite a live id).

## §5 THE TESTS + THE LAWS + THE FLOOR

- The named edges (`tests/test_run_store.py`; every test passes tmp paths — never the real STORE_HOME): (1) THE ROUND-TRIP: register + k casts (mixed classes, one correction) → save → fresh load → the §3 surface asserted equal (the maps, the ids, the seven fields, the TallyResult whole); the stamps asserted EXCLUDED (the divergence named in the test, never hidden). (2) THE CORRUPT FILE: each §4 trigger → StoreRefusedError, all three fields rendered, the container never constructed (the partial load unrepresentable). (3) THE CRASH-TAIL: the truncated last line refused naming truncation; the clean file minus its tail loads whole — the census reflects the FILE (the loss invisible, bounded ≤ 1), `.serve` re-serves the same pair. (4) THE SUPERSEDE REPLAY: the correction rides the trip — the re-minted target live, the tally's exclusion set matching, the ranking byte-identical. (5) THE EMPTY-RUN LOAD: a manifest-only file → the all-zero maps + the empty log (a VALUE, never a refusal — register-then-exit is the mid-session crash's own form). (6) THE DOUBLE-WRITE ABSORPTION: a byte-identical line twice (the crash-retry form) → absorbed loudly at replay (acknowledged=True, the count unchanged, never double-counted — R9 at the file tier).
- [PROPOSED] The floor (a new ignore is a ruling HERE; none is proposed): pyright strict 0 errors 0 warnings; ruff ALL zero findings; zero ignores; ZERO runtime deps (json + pathlib, stdlib); five-field docstrings on every public symbol; one-commit-per-increment; floor-green = `make dev && make test && make lint && make typecheck`.

## THE CARRIERS TABLE (G-RUN-STORE's four → this spec's carriers)

| G-RUN-STORE condition | carried by |
|---|---|
| 1. lands per its approved brief (the exact-task law) | the whole brief — every choice [PROPOSED] with its reason; jikko executes byte-exact, nothing to figure out |
| 2. the round-trip property (manifest frozen once; the log append-only, the dedup rebuilt at load; the census byte-identical) | §2 (register writes the manifest line ONCE; the append-only save-at-cast log) + §3 (the field-selected equality surface) + tests 1, 3, 4, 6 |
| 3. the seam honest (CLI-tier; the core untouched, no persistence verb on the door; the corrupt file refuses three-field, never a silent partial load) | §0's fence + §1 (public-only composition; a NEW file, zero core edits) + §4 (the pre-pass, StoreRefusedError) + tests 2, 5 |
| 4. pyright 0/0/0, ruff zero findings, zero ignores; kensho's independent re-run green | §5's floor + the six tests — the read-back is the evidence |

## THE OPEN QUESTIONS carried to the gate (each [PROPOSED] — the collaborator rules)

1. The class's name: [PROPOSED] `Persist` — the dispatch act's first word ("Persist the run state across invocations"), the Session precedent's pricing form; alternative: `RunStore` (the unit's noun, the act re-worded). Reason: the law is mechanical; the given act prices Persist.
2. The store home's default: [PROPOSED] `.prioritree/runs`, CWD-relative (per-project state — the .git form: visible, gitignore-able, no hidden global); alternative: user-global `~/.prioritree/runs`. Reason: the CLI's use is per-project ranking; a global home hides the store from the project.
3. The in-file run_id's form: [PROPOSED] the door's verbatim handle (zero translation; the verbatim seven-field re-cast) — the accepted oddity named at §3 (file RUN-0007.jsonl's lines say RUN-0001); alternative: the external id translated on save. Reason: the equality surface is door-side; translation buys no stability, only file-local cosmetics.
4. Concurrency: [PROPOSED] single-writer BY CONTRACT, documented (violations surface as load refusals — the merged file's id-sequence violation — loud, never silent); alternative: a lockfile refusal (service-tier weight, priced out at this zero-dep tier). Reason: the subcommand shape is sequential by construction.

*Provenance: togo (統合, integrate), packet synthesize/run-store, route prioritree-cli, 2026-11-20 session. Read-only held — the brief returned in-message; landed by shinko via patch under the landing discipline. The tree is the truth.*
