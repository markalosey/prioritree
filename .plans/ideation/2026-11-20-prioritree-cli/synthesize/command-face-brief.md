# synthesize/command-face-brief — THE COMMAND-FACE UNIT'S BUILD BRIEF (the exact-task spec)

**Status: PROPOSAL.** Togo proposes; the collaborator rules at G-COMMAND-FACE-BRIEF. Every [PROPOSED] element is an offered default with its one-line reason. The brief IS the spec (the exact-task law): once approved, jikko executes exactly, kensho re-runs independently.

## §0 THE GROUND — the join, the bindings, the convergence

- THE SUBSTRATE (both legs agree; no divergence): the CLI's ONLY callee is run_store — STORE_HOME (".prioritree/runs", CWD-relative, the named constant), Persist.register/load, .cast/.serve/.census/.rank, .run_id (the file STEM — the cross-process id; the in-file handle never crosses the CLI). The catch set: ExhaustedQueue (DONE, NOT a RefusedError subclass, prefix "exhausted —", next_action already names the tally pointer) + the three refusals StoreRefusedError/VotesRefusedError/TallyRefusedError (each renders "refused — expected: … | found: … | next: …" in __str__). RegistryRefusedError never reaches the CLI (door-wrapped).
- THE BINDINGS: Q-cli-shape (subcommands only, 1:1 on register/next/vote/state/tally); Q-cli-io (argv in, stdout out; 0/1/2 — DONE at 0, refusals at 1, the unexpected at 2); G-COMMAND-FACE's four (quoted at the carriers table); the tier fence (the CLI composes run_store ONLY; value-type imports legal; no op added, no op re-derived).
- THE CONVERGENCE — two divergences named, resolved per the accepted-cost clause: (1) the dispatch's floated light ranking (groups+version+cycle) vs the gate's binding "TallyResult's frozen whole rendered faithfully, tie groups and coverage counts included" — THE GATE WINS: the whole renders (§3); the light form priced as the rejected alternative (its cost: a binding condition unmet). (2) the floated space-form report lines vs opaque ids (an id may legally contain spaces) — RESOLVED: the marker+tab language (§3; collision-free, first-token parseable); the floats priced.

## §1 THE MODULE + THE SURFACE

- [PROPOSED] module `cli.py` — modules price by surface (the seven-module precedent); docstring lead "cli — the wrapper-tier command face: command the run at the command line". Entry `command(argv: Sequence[str] | None = None) -> int` — the act "Command the run at the command line" (the naming law's first word); None → sys.argv[1:]; the RETURN is the exit code (the console-script wrapper sys.exit()s it — the standard generated form).
- THE 1:1 MAP (the frozen door cited, no op added, no op re-derived): register → Persist.register; next → Persist.load + .serve(seed); vote → Persist.load + .cast; state → Persist.load + .census; tally → Persist.load + .rank.
- THE IMPORTS (value types from their homes — citations, never door compositions): from run_store: Persist, StoreRefusedError, STORE_HOME (the default home — cited, never re-defined); from registry: OperatorDeclaration (the register path's value type — its verdicts field defaults to WEAK_ORDER_TRIPLE, so the CLI constructs it id+question only); from votes: VotesRefusedError; from tally: TallyRefusedError; from session: ExhaustedQueue (its home).
- THE FENCE, HELD: no Registry()/Session() at the CLI tier; no argparse choices= for door-validated values (winner, comparator_class, pair ids — their refusals ride exit 1, never argparse's 2); no validation re-derived — the CLI polices only ITS OWN argv syntax (the colon's presence; argparse's token forms); the door polices values (empty ids, cardinality, verdict membership, class membership).

## §2 THE ARGV GRAMMAR (per subcommand whole; every token a named constant — content-in-configuration)

```
prioritree register ITEM... --operator-id ID --question TEXT [--quorum N]
prioritree next RUN-ID [--seed N]
prioritree vote RUN-ID ITEM-A ITEM-B WINNER COMPARATOR-ID COMPARATOR-CLASS [--notes TEXT] [--supersedes VOTE-ID]
prioritree state RUN-ID
prioritree tally RUN-ID
```

- [PROPOSED] register's items: id:label single tokens, nargs="+", split on the FIRST colon (labels may contain colons; ids may not — the accepted cost, named: a colon-free id is trivially choosable). Alternatives priced: two-token positionals (the odd-count error class + interleaved confusion), a JSON file / stdin (a round-trip per register — friction both composer classes pay). The CLI validates only the colon's PRESENCE (a token without it → parser.error → exit 2); the empty id (":label") passes to the door's own refusal (exit 1) — no re-derivation.
- The operator: --operator-id + --question (required flags — positionals after a variadic positional are argparse-ambiguous); --quorum type=int default 1. The division named: a non-integer token → argparse's 2 (token FORM); --quorum 0 → the door's refusal 1 (token VALUE).
- [PROPOSED] the verdicts NOT exposed — no flag: the door's own law (the registry refuses any set ≠ WEAK_ORDER_TRIPLE; the dataclass default carries the triple) — a --verdicts flag would be a no-op surface whose only legal value is the default.
- RUN-ID = the file STEM ("RUN-0001") — the two-id-spaces law: load builds {stem}.jsonl; the in-file handle never crosses.
- vote's pair: two positionals in the served canonical order (the swapped-citation check is the door's); winner / comparator-class pass through unvalidated (the door's exit-1 refusals); --notes/--supersedes default None → .cast verbatim.
- [PROPOSED] --home PATH: ONE definition on a shared PARENT parser attached to all five subparsers — placement AFTER the subcommand (prioritree next RUN-0001 --home X); default STORE_HOME. Alternative: global-before (rejected: argparse hands off at the subcommand token — a global flag dies after it; the footgun named). --seed type=int default None → .serve(seed) verbatim (the door derives when None — no re-derivation).

## §3 THE EXIT-CODE MAPPING + THE REPORT SHAPES (the exact bytes)

- HAPPY → 0: the handler renders, returns 0.
- DONE (ExhaustedQueue, caught BY TYPE, before the generic clause): print(str(done)) to STDOUT → 0. [PROPOSED] the FULL three-field message verbatim — one rendering path (the pass-through discipline), the expected/found fields tell the operator WHY, the pointer rides next_action. Alternatives: the pointer-only line (rejected: field extraction is a second rendering path + context loss); stderr (rejected: DONE is success — scripts read stdout).
- REFUSALS → 1: except (StoreRefusedError, VotesRefusedError, TallyRefusedError) — ALL THREE, BY TYPE, one tuple clause (the brief closes Q-cli-io's gap: its text named the two door refusals; the store's tier joins them); print(str(refusal), file=sys.stderr) → 1 — the str(e) PASS-THROUGH (the grammar already rendered; re-rendering from fields yields identical bytes).
- UNEXPECTED → 2: except Exception: traceback.print_exc() to stderr → return 2. [PROPOSED] the traceback rides verbatim — the unexpected is unanticipated by definition; the traceback is the only honest rendering.
- ARGPARSE'S CHANNEL, UNTOUCHED: parse_args' usage errors raise SystemExit(2) + usage to stderr BY CONSTRUCTION; SystemExit is BaseException — the except Exception clause never swallows it; it propagates → exit 2. The CLI's OWN argv-semantic violations route parser.error(...) — the SAME channel. The honest ruling: exit 2 is the argv+unexpected channel; the rendering distinguishes them (usage text vs traceback); no SystemExit wrapper (conflation + bytes for nothing).
- THE REPORT LANGUAGE: [PROPOSED] marker-first, tab-separated fields ({marker}\t{field}...) — collision-free against opaque ids (spaces ride intact), first-token parseable; the pass-through lines (DONE to stdout, refusals to stderr) ride the tiers' OWN bytes, never re-wrapped. Alternative priced: the floated space forms ("a vs b", "a b count") — collision-prone with opaque ids.
- register: the BARE STEM, one line — RUN-0001 (the id IS the whole report).
- next: pair\t{item_a}\t{item_b}\t{count} — the serve triple whole.
- vote: vote\t{vote_id}\t{count} (a new cast); ack\t{vote_id}\t{count} (acknowledged=True — the marker IS the loud dedup ack).
- state (the census SUMMARY — Q-cli-io's own word): votes\t{total} (total = len(census.vote_log) — the log IS the votes), then item\t{id}\t{count} per item — the map's own iteration order (deterministic by the door's construction; the CLI adds no sort), zeros INCLUDED (0-included is the census's own law; an elided zero is indistinguishable from an absent item). [PROPOSED] elided: per_pair_counts (the log's granularity; the WEIGHTED view renders at tally), vote_log (the honesty edge: recorded_at RE-MINTS at load — rendering re-minted stamps as original lies), census.run_id (the in-file HANDLE — never crosses the CLI).
- tally (the frozen WHOLE — every field renders, §0's resolved divergence): rank\t{id}\t{id}... one line per group (the door's score order; the line boundary IS the tie-group boundary — the only place tie-ness lives); counts\t{id}\t{wins}\t{losses}\t{ties} per item (map order, zeros included); coverage\t{len(components)}\t{done}; cycle\t{a>b}\t{b>c}... ONLY when non-empty (named-never-error); pairs\t{a}\t{b}\t{n} per pair (the map's order — the WEIGHTED counts, "coverage counts included" satisfied); version\t{algorithm_version}.

## §4 THE CONSOLE-SCRIPT + THE PYPROJECT EDIT

- The NEW table, appended at the end of pyproject.toml (zero existing lines touched — the pure append):

```toml
[project.scripts]
prioritree = "prioritree.cli:command"
```

- Under hatchling, uv's editable install maps the entry to live src/prioritree — make dev makes prioritree answer, no reinstall. NO __main__.py (the console script is the ruled entry; python -m an unruled widening — banked, never forced).

## §5 THE TESTS + THE FLOOR

- tests/test_cli.py (flat; the module's name), the unit form: command(argv_list) called IN-PROCESS with --home tmp_path homes ONLY (the default home never touched); NO subprocess (the e2e fixed-argv arc is cli-acceptance's unit); per-test docstrings; module-level payload constants; parametrized refusal matrices. The arcs: (1) each subcommand's success (5 tests): return 0 + the exact stdout bytes (the id line / pair line / vote line / summary / the whole ranking against a driven-to-coverage fixture); (2) DONE: a 2-item run exhausted → return 0; stdout == the "exhausted —" three-field bytes (the pointer in next); (3) the refusals (parametrized, ALL THREE): StoreRefusedError (the unknown run at load), VotesRefusedError (the out-of-set winner at vote), TallyRefusedError (the SAFE HALT at an undercovered tally — e.g. 3 items, 1 vote) → return 1; stderr == str(e) bytes; (4) the unexpected: a monkeypatched verb raising RuntimeError → return 2; the traceback's name on stderr; (5) argparse's channel: the missing positional, the unknown subcommand, the non-integer --seed, the colon-less item token → SystemExit code 2 + the usage/error bytes on stderr; (6) --home: register under A; A serves; B (empty) refuses → 1; the after-subcommand placement exercised; (7) --seed: the same seed twice → byte-identical pair lines (the pass-through); (8) the ack: a byte-identical re-cast → the ack line, return 0 (the loud dedup).
- THE FLOOR: pyright strict 0 errors 0 warnings; ruff zero findings; ZERO ignores (this brief rules NONE — a new ignore is a new ruling at a new gate); argparse stdlib ONLY (dependencies stays [] — never typer/click); five-field docstrings on every public symbol; the naming law; content-in-configuration (the five subcommand names, the flag spellings, the separators ":"/"\t", the markers, the ack token — every grammar token a named constant); the no-shell law (in-process; zero subprocess in the module).

## THE CARRIERS TABLE (G-COMMAND-FACE's four → the spec's carriers)

| the gate's condition | the carrier |
|---|---|
| 1. "the command face lands per its approved brief — the exact-task law" | the whole brief §0-§5 — jikko executes byte-exact, nothing to figure out |
| 2. "the five subcommands map 1:1 onto the five ops — the frozen door cited, no op added, no op re-derived; the console-script entry live; argparse stdlib only" | §1 (the map + the fence), §2 (the grammar), §4 (the hunk), §5's floor |
| 3. "the I/O contract green per the brief: the exit codes ruled (0 success AND DONE; 1 the refusal lineage, three fields; 2 the unexpected); the report shapes ruled (the pair line, the census, the ranking — the frozen whole, tie groups and coverage counts included)" | §3 (the mapping + the exact bytes) + §5's arcs 1-5 (the bytes asserted) |
| 4. "pyright 0 errors 0 warnings and ruff zero findings; kensho's independent re-run green" | §5's floor; the tests the re-run's evidence |

## THE OPEN QUESTIONS carried to the gate (each [PROPOSED] + alternative + reason)

1. The names: cli.py + command() [PROPOSED] — modules price by surface (the seven-module precedent), the entry by the act's first word; alternative command.py/main — the unit-id form / the conventional unpriced name.
2. The items form: id:label first-colon [PROPOSED] — flat argv, no file round-trip, the cost named (colon-ids unrepresentable); alternatives: two-token pairs (the odd-count class), file/stdin (the round-trip friction).
3. The report language: marker+tab [PROPOSED] — collision-free over opaque ids; alternative: the floated space forms — prettier, collision-prone.
4. The ranking: the frozen WHOLE [PROPOSED — §0's named divergence; the gate's binding text wins]; alternative: the light form — its cost: "the frozen whole… coverage counts included" unmet.
5. DONE's bytes: the full str(e) to stdout [PROPOSED]; alternative: the pointer-only line — a second rendering path, context loss.
6. The census: the summary (votes + items) [PROPOSED — Q-cli-io's "census summary"]; alternative: + per-pair lines — noise at the state surface (the weighted view lives at tally).
7. --home's placement: per-subcommand parent parser [PROPOSED]; alternative: global-before — argparse's handoff makes it a footgun.
8. The ack form: the ack marker [PROPOSED]; alternative: a third token on the vote line — the marker is louder (the "loud dedup ack").
9. The unexpected: the traceback verbatim [PROPOSED]; alternative: a named line — diagnosis loss at the moment it is most needed.
10. The verdicts: no flag [PROPOSED — the door's own law]; alternative: --verdicts — a no-op surface.
11. The OperatorDeclaration citation: import-from-home [PROPOSED]; alternative: a run_store re-export — new store surface after its gate closed.

*Provenance: togo (統合, integrate), packet synthesize/command-face, route prioritree-cli, 2026-11-21 session. Read-only held — the brief returned in-message; landed by shinko via patch under the landing discipline. The tree is the truth.*
