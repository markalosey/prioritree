# synthesize/service-acceptance-brief — THE SERVICE-ACCEPTANCE UNIT'S BUILD BRIEF (the exact-task spec)

**Status: PROPOSAL.** Togo proposes; the collaborator rules at G-SERVICE-ACCEPTANCE-BRIEF. Every [PROPOSED] element is an offered default with its one-line reason. The brief IS the spec (the exact-task law): once approved, jikko executes exactly, kensho re-runs independently.

## §0 THE GROUND

- THE JOIN IS CLEAN — no divergence survives: both legs agree on the boot (the sibling binary, cwd=tmp_path — the import side-effect chain makes the Popen's cwd the ONE lever that reaches the module-level seam, zero product changes), the probe (404-as-ready), the isolation (per-test fresh homes), the counts (N=2 x M=2, aggregate-only), the fixture (function-scoped; the session form rejected structurally by both). rikai's recommendations ride as the [PROPOSED] defaults throughout. Two on-disk facts carried: pyproject.toml:127 (the dev group's "httpx2" vs the ruling's "httpx" — §7) and the S603/S607 per-file ruling (§7).
- THE RULINGS BINDING: Q-service-acceptance (the e2e through the real socket — the seven-request arc, the determinism replay, the refusal arcs, THE CONCURRENCY ARC); Q-service-lifecycle (the live socket at the acceptance unit ALONE; the fixed-argv subprocess per the no-shell law); Q-service-routes (the status mapping and the wire's body grammar — the frozen shapes §3 asserts); Q-service-concurrency (the lock — §6's subject); G-SERVICE-ACCEPTANCE's four conditions (the carriers table below); FR-MEM-0017 (§7's regions); the report-op discipline (the read-back the evidence, never the build's word).

## §1 THE MODULE + THE BOOT INSTRUMENT

- THE MODULE: tests/test_service_acceptance.py — the naming law: the act "Accept the service over the real socket" names every symbol [PROPOSED: the fixture `service` (yields the base URL), the helpers `boot_server`/`wait_ready`, the tests accept/replay/refuse/interleave — each the first word of its act-statement].
- THE DISCOVERY: _UVICORN = Path(sys.executable).parent / "uvicorn" — the CLI harness's _SHIM precedent re-carried 1:1 (uvicorn[standard] a [project] dep — the console script in the same venv's bin; [uv, run, ...] priced and rejected: the Popen handles uv not the server, terminate one hop removed, uv's lines polluting the streams).
- THE ARGV pinned byte-exact: [str(_UVICORN), "prioritree.service:app", "--host", "127.0.0.1", "--port", "0", "--no-access-log"] — a fixed-argv LIST, never a shell string (the no-shell law). Each flag priced: --host 127.0.0.1 the loopback pin (the S104-adjacent safety — never the wild interface); --port 0 the ephemeral form (the kernel assigns; the fixed-high-port alternative rejected — collision/CI flake); --no-access-log the pipe-fill silence (one line per request otherwise; --log-level NEVER lowered — it would erase the startup banner itself).
- cwd=tmp_path — THE HOME ISOLATION'S WHOLE MECHANISM: STORE_HOME is CWD-relative, never .resolve()d; every open under it resolves against the subprocess's CWD at call time; the Popen sets it once, before exec. The fragility named: omit cwd= and the store lands in the working tree — the oracle's direct read (§6) is load-bearing twice. The fixture pre-creates nothing (the register's own mkdir builds the home).
- THE FIXTURE, function-scoped [PROPOSED — the session form rejected STRUCTURALLY, not on cost: one boot shares ONE home — the stem sequence test-ORDER-coupled (the second register mints RUN-0002; every hard-coded RUN-0001 expectation breaks), the refusal arcs pollute the shared home, and the replay NEEDS two fresh homes by its own claim]. The sequence: Popen(ARGV, cwd=tmp_path, stderr=PIPE) => the readiness probe (§2) => yield the base URL f"http://127.0.0.1:{port}" => terminate() (SIGTERM, the graceful drain) => wait(timeout≈5s) => kill() ONLY on TimeoutExpired (the backstop) — pytest's finalization guarantees the teardown on assertion failure, no orphaned uvicorns.

## §2 THE PORT DISCOVERY + THE READINESS

- THE STDERR BANNER PARSE, both forms priced: (a) Popen(stderr=PIPE) with a bounded line loop, reading line-by-line to the banner — the pipe-fill hazard priced LOW at this volume (~10 lines the whole run under --no-access-log; the loop bounded by the deadline, the pipe closed after the port is taken); (b) stderr-to-a-tempfile — the fill hazard removed entirely, but the live-read becomes a file poll + a cleanup [PROPOSED (a) the PIPE with the bounded line loop — the simpler form; the fill priced negligible at this volume].
- THE REGEX: r"Uvicorn running on http://127\.0\.0\.1:(\d+)" — the resolved port (the banner rides STDERR — uvicorn's default logging config, never stdout; the wording-drift fragility guarded by uv.lock's pin — the lock IS the stability mechanism; the banner follows "Application startup complete." — itself the full-readiness signal).
- THE DEADLINE: ~15s — ~10x the boot's expected ~1-2s cold cost, CI variance absorbed.
- THE 404-AS-READY PROBE [PROPOSED]: the retry loop (~0.1s interval, ~0.5s per-call timeout — load-bearing: a connect landing mid-startup can stall in the accept backlog; short timeout + retry rides the gap), each call GET /runs/RUN-0001/next expecting 404 — the WHOLE CHAIN proven in one call (TCP accepted, HTTP parsed, route matched, the sync handler through the seam, the unknown-run refusal rendered, the store empty — the fresh home's live-set scan refusing RUN-0001). WHY 404 beats a raw connect poll: a connect proves only the listener accepts. The probe doubles as the file's first refusal-arc data point. Any other status => fail loudly. A TIMEOUT FAILS, NEVER SKIPS.

## §3 THE SEVEN-REQUEST ARC

- (1) register: POST /runs {"items": [["a","one"],["b","two"],["c","three"]], "operator_id": "op-1", "question": "Which matters more?"} (quorum omitted — the door's default 1) => 201 {"run_id": "RUN-0001"}.
- (2) next: GET /runs/RUN-0001/next => 200 {"item_a": "a", "item_b": "b", "count": 0}.
- (3-5) vote x3 (prefer-a, the three pairs (a,b)/(a,c)/(b,c)): POST /runs/RUN-0001/votes with CastVoteRequest's required four — {"pair": [...], "winner": "prefer-a", "comparator_id": <the face tests' own literal, carried 1:1>, "comparator_class": <the face tests' own literal, carried 1:1 — the door's legal class set, cited never invented>} (notes/supersedes the door's optional, omitted) => 200 {"vote_id": "VOTE-0001..0003", "count": 1..3, "acknowledged": false}.
- (6) next exhausted: GET /runs/RUN-0001/next => 200 the DONE body — {"done": true, + expected/found/next_action}, the three fields the signal's own, the /runs/RUN-0001/tally pointer riding in next_action (DONE a state, never an error).
- (7) tally: GET /runs/RUN-0001/tally => 200 the frozen whole — the census's exact literal: ranked_groups, per_item_wins/per_item_losses/per_item_ties, coverage {components: [["a","b","c"]], done: true, cycle: [], pair_counts {"a|b": 1, "a|c": 1, "b|c": 1}}, algorithm_version "win-rate-v1".
- EACH BODY ASSERTED — [PROPOSED .json() equality per step against the named-constant literals (content-in-configuration); the byte-level comparison is §4's own subject, not re-asserted per-step].

## §4 THE DETERMINISM REPLAY

- Two fresh homes (tmp_path/"one", tmp_path/"two") => two boots (the boot helper parameterized by the home) => the same seven-request arc against each => comparing [r.content for r in one] == [r.content for r in two] — THE BYTES, not parsed dicts; byte-identity IS the claim.
- The identity TOTAL by construction: no recorded_at crosses the wire anywhere (the register body the stem alone, the acks the id/count/acknowledged triple, the tally the frozen whole — the census elides the vote_log precisely because the stamps re-mint); the stems/vote-ids identical on fresh homes (the home-scan mint yields RUN-0001, the vote ids VOTE-0001..0003); the port never appears in any body. Priced: ~3-5s.

## §5 THE REFUSAL ARCS THROUGH THE SOCKET

- 404 — the unknown run: GET /runs/RUN-9999/next => 404 {"expected", "found", "next_action"}, the LIVE SET in found (the dedicated asserted call; the probe's own 404 the first sighting, not the assertion).
- 422 — the bogus winner: the vote cast with winner out-of-set => 422, the three fields verbatim.
- 409 — one vote then tally (a fresh run, one cast): GET .../tally => 409 with "at quorum" in expected — the SAFE HALT never swallowed, never a partial ranking dressed as whole.
- 400 — the malformed items: POST /runs with items the wrong shape => 400 {"detail": [loc/msg/type, ...]} — the native grammar re-badged, the client's own fix map (422 exclusively the door's value refusals).
- THE 500 ARC PRICED [PROPOSED OMITTED at this unit]: the monkeypatch cannot cross the process wall — the in-process face test carries the envelope's falsification (the fold handler's three-part body asserted there); the socket arc's subject the WIRE, not the crash. The re-priced alternative — a query-triggered fault — REJECTED: no product route carries a fault injection; the shape would be scaffolding in the product.

## §6 THE CONCURRENCY ARC

- N=2 threads x M=2 casts [PROPOSED — the gate's own letter "two clients"; N=4 x M=1 priced and passed over: thinner interleave density — each thread's second cast rides an ESTABLISHED connection, maximizing overlap].
- The release: threading.Barrier(2) — both first casts fire together; each thread its own httpx.Client (separate pools => two TCP connections => uvicorn's accept loop => FastAPI's threadpool runs the two sync handlers concurrently => the seam's one process-wide lock serializes each whole act).
- The distinctness key: comparator_id per thread — "c1"/"c2".
- THE PAIR PLAN: thread-1 casts (a,b), (a,c); thread-2 casts (b,c), (a,b) — the aggregate ORDER-INVARIANT: pair counts ab:2, ac:1, bc:1; per-item a:3, b:3, c:2; total 4.
- THE AGGREGATE-ONLY assertions: every cast 200; GET /runs/RUN-0001/state => {"total": 4, "items": {"a": 3, "b": 3, "c": 2}}; the vote-id SET unique {VOTE-0001..VOTE-0004} — the ORDER NEVER asserted (the per-ack counts are order-DEPENDENT — the lock serializes, arrival order decides; the interleaving nondeterministic by construction). No lost update (total<4), no doubled mint (a duplicate id).
- THE FILE'S DIRECT READ — the fresh Persist.load the oracle [PROPOSED the import]: the test process reads the subprocess's home directly (tmp_path/.prioritree/runs/RUN-0001.jsonl) — 4 records, the vote-id set, the per-pair counts exact; the load's own pre-pass the corruption check. THE ONE PRODUCT IMPORT priced honestly against the wire-alone alternative (the census + the ack id set — sufficient for the counts, but the file's direct read is the load-bearing half: the gate's own named form falsified against the FILE, and the read proves §1's cwd anchor aimed true — load-bearing twice; the import wins). The cross-process read safe: each request composes a fresh run-store inside the lock, the file closed between requests; after the census confirms 4, the file quiescent.

## §7 THE FLOOR

- pyright 0 errors 0 warnings 0 informations strict — httpx2's Client/Response typed surface (the transcription fact on disk carried for the floor's own verification: pyproject.toml:127's "httpx2" vs Q-service-deps' "httpx" wording — whether the lock serves the plain-httpx import is the floor's own check); the Popen/threading edges named (the pipe read-loop's str/bytes mode, Barrier, join/timeout members) — cast-typed per the registry school, never ignores.
- ruff zero findings: **THE S603/S607 PER-FILE ENTRY for the new harness — "tests/test_service_acceptance.py" = ["S603", "S607"]** — the re-scope the zero-findings bar requires: the ruling on disk is PER-FILE (scoped to tests/test_harness.py alone), and the acceptance harness's Popen fires the same pair until its own entry lands (the test_harness.py ruling's form re-carried; the entry IS the ruling, never a convenience).
- Five-field docstrings (the fixture, the helpers, each test); content-in-configuration (the payload literals named constants); the S101/PLR2004 tests ruling stands; FR-MEM-0017's regions named: the boot instrument / the arc / the replay / the refusals / the concurrency; one-commit-per-increment.
- The wall clock named: ~6 per-test boots ≈ 12s added (cold CI worst case toward 15-18s); the whole file ~20-25s — the honest price of total isolation.

## THE CARRIERS TABLE (G-SERVICE-ACCEPTANCE's four → the spec's carriers)

| the gate's condition | the carrier |
|---|---|
| the acceptance harness lands per its approved brief — the exact-task law | this brief whole (§1-§7) — jikko executes byte-exact, nothing to figure out |
| the e2e arc green THROUGH THE REAL SOCKET (fixed-argv subprocess, httpx the client): register → next → vote × k → the exhausted turn → tally | §1 the boot + the fixture; §2 the port + the readiness; §3 the arc (k=3, the three pairs); the seam + the lock proven in the arc itself |
| the determinism replay + the refusal arcs (404/422/409/400) + THE CONCURRENCY ARC (every cast landed, the counts exact, no lost update) | §4 the byte-identical replay; §5 the four refusals; §6 the aggregate-only assertions + the file's direct read |
| pyright 0/0 and ruff zero findings; kensho's independent re-run green | §7 the floor; the read-back the evidence (the report-op discipline) |

## THE OPEN QUESTIONS (each [PROPOSED] + alternative + reason)

1. THE 500 ARC'S FATE — [PROPOSED OMITTED at this unit]: the monkeypatch cannot cross the wall; the in-process face test carries the envelope's falsification. Alternative: a query-triggered fault — rejected (no product route for it; scaffolding in the product). Reason: the socket arc's subject the wire, not the crash.
2. THE ORACLE IMPORT — [PROPOSED the fresh Persist.load, the file's direct read]. Alternative: the wire alone (the census + the ack id set). Reason: the gate's own named form ("no lost update — the counts exact") is best falsified against the FILE, and the read proves the cwd anchor aimed true.
3. THE STDERR FORM — [PROPOSED the PIPE with the bounded line loop]. Alternative: stderr-to-a-tempfile (the fill hazard removed entirely; the file + cleanup + the live-read poll the cost). Reason: at ~10 lines the whole run the fill is negligible — the simpler form wins.
4. THE THREAD/CAST COUNTS — [PROPOSED N=2 x M=2]: the gate's own letter "two clients"; the second cast per thread rides an established connection (denser interleave). Alternative: N=4 x M=1 — priced, thinner overlap. Reason: the gate's letter + the density.
5. THE WALL CLOCK — the per-test boots' ~12s named (~2s x ~6; cold CI toward 15-18s worst case). Alternative: the session-scoped form — rejected structurally (§1: the home shared, the stems order-coupled, the replay broken). Reason: the isolation is total and the replay structural; 12s the honest price.
6. THE comparator_class LITERAL — [PROPOSED carried 1:1 from the face tests' own literal]: the field set is byte-exact per CastVoteRequest, but the census does not spell the class VALUE. Alternative: invented here — refused (no claim without evidence on disk). Reason: the face tests' literal is the on-disk truth; the brief cites, never invents.

*The tree is the truth; the gate G-SERVICE-ACCEPTANCE-BRIEF awaits the collaborator's approval; the build dispatch fires only after (the precedence law).*
