# discover/cli-acceptance — the discovery census (tansa; the record; the pipeline's first leg)

- Provenance: tansa (探査, discover), packet discover/cli-acceptance, route prioritree-cli, 2026-11-21 — read-only held; the census returned in-message; landed by shinko via patch. Reads: cli.py whole (382), test_cli.py whole (220), pyproject.toml (100), the route's gates record, acceptance.py (280 — the harness precedent), command-face-bytes.md (kensho's act-4 gap — THIS unit closes it), the shim at .venv/bin/prioritree (10 lines) + three structural globs.

## (1) THE CENSUS — what exists

- **The landed CLI's exact surface**: the five subcommands 1:1 on the five ops — register (the id:label first-colon tokens, --operator-id/--question required, --quorum int default 1; the bare stem out), next (run_id + --seed; the pair line), vote (six positionals + --notes/--supersedes; the vote/ack lines), state (the census summary — map order, zeros included), tally (the frozen whole: rank/counts/coverage/cycle-if-non-empty/pairs/version). --home on the shared parent parser, the AFTER-subcommand placement, default STORE_HOME CWD-relative. **The exit-code mapping**: 0 success AND DONE (ExhaustedQueue BY TYPE → the full three-field message on stdout); 1 the three typed refusals str(e) verbatim on stderr; 2 the unexpected (traceback verbatim); argparse's SystemExit untouched. The report bytes are already unit-asserted in-process (test_cli.py's fixtures).
- **The console script's state**: declared prioritree = "prioritree.cli:command" (pyproject 13-14); the shim at .venv/bin/prioritree — the venv's python3 shebang, the import, sys.exit(command()) — the entry wired and live. **Kensho's act-4 gap (the live run unexecutable at the no-shell seat) closes at THIS unit by construction.**
- **The subprocess instrument's legal form**: fixed-argv lists, never shell strings — the gate's condition 2 verbatim; subprocess stdlib, dependencies = [] untouched.
- **The prior units' test precedent**: IN-PROCESS command(argv_list) + capsys + --home tmp homes, NO subprocess — the docstring itself names the e2e arc "cli-acceptance's unit, the NEXT one." **The e2e ADD**: exit codes AS OS returncodes, stdout/stderr as real pipes, the persistence seam proven in the arc.
- **The harness precedent** (acceptance.py): the in-process arc shape to mirror through argv — next → cast → ExhaustedQueue BY TYPE → tally. **Name collision confirmed**: acceptance.py AND tests/test_acceptance.py are both taken (the core's U6).

## (2) THE GAPS the brief must pin — as questions

1. **The module's name** — the naming law: acceptance.py/test_acceptance.py are taken. What act prices the harness's name, and does it land as tests/test_<name>.py or a src module?
2. **The invocation form** — priced: (a) the console script's full path derived Path(sys.executable).parent / "prioritree" — drives the REAL declared entry, closes kensho's gap, the full path dodges S607; (b) sys.executable -m — STRUCTURALLY UNAVAILABLE (no __main__.py, the command-face brief ruled against it); (c) uv run — prices an outer tool in the test bed; (d) the -c bootstrap — legal but bypasses the shim (the declared surface). Which rules?
3. **The working directory's role** — STORE_HOME's default is CWD-relative; the arcs pass --home tmp dirs (absolute) — does --home fully decouple the CWD?
4. **The arc's shape** — the gate's arc: register → next → vote × k → the exhausted turn (exit 0, the tally pointer) → tally. n items at the ruled k, EACH VOTE A SEPARATE INVOCATION (the seam is the test): n=3 at k=1 prices 7 process runs; what n and k? The loop's driving form (next re-serves the same under-quorum pair until count reaches k)?
5. **The determinism surface** — the same argv sequence yields byte-identical outputs across replays. The outputs are clock-free by construction (state elides vote_log — recorded_at re-mints at load; the FILE's stamps written once, never re-emitted). Does any output byte embed the --home path (the refusal bytes)? If yes, the replays must pin stable home paths.
6. **The refusal + SAFE HALT arcs at the process level** — the unknown run, the out-of-set verdict (exit 1, three fields), the SAFE HALT (tally under-covered → exit 1, U4's own message — never a partial ranking dressed as whole). Which ride the e2e?
7. **S603/S607** — the findings the harness WILL fire: S603 on every subprocess.run (the no-shell law's own form; the untrusted-input intent never rides a deterministic fixed-argv harness); S607 only on a partial-path executable (the full-shim form dodges it). The pyproject named-ruling question: extend tests/**'s R1 or a module ruling, in the prior rulings' form.

## (3) THE LAWS RIDING

- **The no-shell law** (fixed-argv lists ONLY — the standing law, condition 2 verbatim); **zero runtime deps** (subprocess stdlib); **the naming law** (both acceptance names taken); **content-in-configuration** (the arc's tokens and expected bytes as named constants); **five-field docstrings**; **the zero-findings bar, zero ignores** (the S603/S607 question rides here); **one-commit-per-increment**; **the tier fence** (the harness drives the REAL binary — NO in-process store/door imports; the imports subprocess/sys/pathlib/pytest only).

*The tree is the truth; the synthesis joins this census with understand/cli-acceptance.md at G-CLI-ACCEPTANCE-BRIEF.*
