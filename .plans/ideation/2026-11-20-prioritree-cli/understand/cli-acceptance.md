# understand/cli-acceptance — the mechanism analysis (rikai; the record; the pipeline's second leg)

- Provenance: rikai (理解, understand), packet understand/cli-acceptance, route prioritree-cli, 2026-11-21 — read-only held; the analysis returned in-message; landed by shinko via patch. Reads: cli.py whole, test_cli.py whole, pyproject.toml, the shim at .venv/bin/prioritree, acceptance.py, run_store.py + the __main__.py glob (zero matches — the absence the finding).

## (1) THE PROCESS BOUNDARY — the falsification set, step by step

- **Exit code as OS exit code.** In-process, command(argv) returns an int and argparse's channel is seen only as pytest.raises(SystemExit) — the int never crosses a boundary. Only a subprocess proves the shim's conversion: sys.exit(command()) turns the int into the OS status; subprocess.run(...).returncode is the OS receipt. SystemExit is BaseException, deliberately uncaught by the except Exception — argparse's exit 2 propagates through the shim to a REAL OS exit 2, a thing pytest.raises intercepts in-process and can never prove.
- **stdout/stderr as real pipes.** Every stdout byte rides _report → print; every refusal byte rides _report_error → print(file=sys.stderr). capsys intercepts at the Python layer; only the child's fd 1/fd 2, captured as subprocess bytes, proves the channels are real, separate OS pipes.
- **The shim at a fresh interpreter.** The shebang pins the venv's python3; the import resolved by the child at run time through the editable mapping. An in-process test proves nothing about the installed artifact — only the child's import chain proves the mapping live.
- **The persistence seam.** THE MECHANISM NAMED: each invocation loads from disk; the in-memory store dies with each process. Every read verb opens with Persist.load → run_file.read_text → a FRESH Session(Registry()) reconstructed by re-register + in-order re-casts. A vote cast in process N is visible to N+1 because and only because cast appends one complete JSONL line at cast_vote's return — save-at-cast — and the file is the sole carrier. One process cannot prove this; two OS processes can, and nothing less.

## (2) THE INVOCATION FORMS, PRICED — AND THE INSTRUMENT

- **(a) The console script directly** — Path(sys.executable).parent / "prioritree". Under uv run pytest the venv IS the active interpreter, so the discovered path is the same bin/ the editable install minted the script into; the absolute argv form needs NO PATH. The shebang pins the child interpreter regardless of caller env. **(b) sys.executable -m prioritree — FAILS structurally**: no __main__.py anywhere (the command-face brief's ruling held; -m an unruled widening, banked). **(c) uv run — the wrapper's wrapper**: pays uv's per-invocation resolution, adds env variance, proves nothing beyond (a). **(d) the -c bootstrap — WORKS mechanically** (sys.argv[0] is "-c", the real argv rides sys.argv[1:], command(None) reads exactly those) but bypasses the shim — it re-implements the shim's two lines inline; proves the module surface, not the installed entry point. **RECOMMENDATION: (a)** — alone it exercises the full falsification set: the entry spec, the shim's own sys.exit, the fresh-interpreter import. **Environment**: the arcs pass --home {tmp_path} (absolute), so the CWD is irrelevant; the flag rides AFTER the subcommand token.

## (3) THE DETERMINISM SURFACE — field by field

- **Rides stdout, clock-free by construction**: the bare stem RUN-0001; the pair line; the vote/ack lines (VOTE-{i+1:04d} mint order, load-enforced); the census summary; the tally frozen whole. **No stamp ever emits to stdout** — state elides vote_log precisely because rendering re-minted stamps lies; tally consumes no stamp.
- **Re-stamps per process**: registered_at/recorded_at written ONCE to the file, then loaded, validated for TYPE only, and re-minted in memory at every Persist.load — unobservable at the CLI surface (the acceptance honesty-pin precedent).
- **The replay**: fresh tmp home per replay → both arcs mint RUN-0001 and VOTE-0001... → two full arc replays yield byte-identical stdout sequences (the field-selection discipline).

## (4) THE ARC'S SHAPE — 3 items at k=1 (the general form: 1 + 1 + n(n-1)/2·k + 1 + 1 invocations)

- (1) register 3 items → RUN-0001\n, 0; (2) next → pair\ta\tb\t0\n, 0; (3-5) vote × 3 (a:b, a:c, b:c — the served canonical order each) → vote\tVOTE-000{1,2,3}\t1\n, 0; (6) next → the exhausted line on stdout, exit 0 — **DONE-at-0 proven at the process level**; (7) tally → the frozen whole, byte-identical, 0. **Total: 7 invocations, seconds-scale.** Refusal arcs: the unknown run → exit 1, the three-field render on stderr (StoreRefusedError); the out-of-set winner → exit 1 (VotesRefusedError rides through BY TYPE); **the SAFE HALT** — tally at undercoverage → exit 1, U4's message verbatim on stderr, never a partial ranking.

## (5) THE FENCE — confirmed, with one named limit

- The harness composes argv lists only: imports subprocess/pathlib/pytest — NO prioritree import at all. Helpers build fixed-argv lists and assert over (returncode, stdout, stderr); every state transition rides the child's own stdout and the file — the harness never calls command()/Persist/Session in-process. Nothing the arc needs is missing from the grammar (the five subcommands with --home on all five, --seed, --notes/--supersedes, state mid-arc). **THE ONE NAMED LIMIT**: the monkeypatched unexpected channel (the in-process unit's arc 4) is an in-process injection only — a real exit-2-with-traceback needs a real bug, not an arc; the e2e covers exit 2 only through argparse's own channel (the unknown subcommand at the process level).

*The tree is the truth; the synthesis joins this analysis with discover/cli-acceptance.md at G-CLI-ACCEPTANCE-BRIEF.*
