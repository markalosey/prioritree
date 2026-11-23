<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — build/mcp-server

**Route:** prioritree-mcp (executing) | **Events:** 20 | **Reports:** 10

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T21:30:42Z |
| 2 | report | jikko | 2026-11-22T21:34:02Z |
| 3 | dispatch | shinko | 2026-11-22T21:34:15Z |
| 4 | report | jikko | 2026-11-22T21:59:12Z |
| 5 | dispatch | shinko | 2026-11-22T21:59:34Z |
| 6 | report | jikko | 2026-11-22T22:43:31Z |
| 7 | dispatch | shinko | 2026-11-22T22:45:02Z |
| 8 | report | jikko | 2026-11-22T23:22:16Z |
| 9 | dispatch | shinko | 2026-11-22T23:22:33Z |
| 10 | dispatch | shinko | 2026-11-22T23:22:38Z |
| 11 | report | jikko | 2026-11-22T23:43:47Z |
| 12 | report | jikko | 2026-11-22T23:55:54Z |
| 13 | dispatch | shinko | 2026-11-22T23:56:05Z |
| 14 | report | jikko | 2026-11-22T23:56:44Z |
| 15 | dispatch | shinko | 2026-11-23T00:49:54Z |
| 16 | report | jikko | 2026-11-23T00:55:23Z |
| 17 | dispatch | shinko | 2026-11-23T00:56:02Z |
| 18 | report | jikko | 2026-11-23T00:58:28Z |
| 19 | dispatch | shinko | 2026-11-23T00:58:37Z |
| 20 | report | jikko | 2026-11-23T00:59:14Z |
## Reported by jikko — 2026-11-22T21:34:02Z

# JIKKO — build/mcp-server step 1 — the dep + the sync-check (2026-11-22)

THE DEP (spec §4): pyproject.toml:7 landed byte-exact — dependencies = ["fastapi", "httpx2", "jinja2", "ouncemcp", "python-multipart", "uvicorn[standard]"] (the sorted position, j-o-p holds); no other pyproject byte touched, the dev group unchanged (patch: 1 hunk, zero findings; line 7 read back verbatim).

THE SYNC'S FOLD (named per the dispatch): jikko's pack carries no make dev verb (lifecycle: start/stop/status/restart/log/output; the Makefile's dev/uv-sync target unrouted) — the mint rides the floor's own uv run at a later step: step 2's uv run ruff / uv run pyright read-back is the first uv run after the dep, step 3's uv run pytest otherwise (the standing fold form, spec §4).

THE LOCK: uv.lock at HEAD (version 1 / revision 3, 37 [[package]] entries) carries NO ouncemcp entry (grep-verified) — the lock regen rides the fold.

THE INSTALLED: .venv/lib/python3.13/site-packages/ (77 entries, populated: fastapi, jinja2, pydantic, pytest, ruff) carries NO ouncemcp — glob-verified, the package dir and any dist-info both absent.

THE SURFACE VERIFICATION (OunceServer's constructor, @server.tool's params, the Effect enum, the Budget form, the idempotency/approval params): DEFERRED — the dispatch's no-verb branch fired; no installed object exists to read, and the pass rides the minting step's read-back. DIVERGENCES: NONE COMPARABLE YET — never "none found"; the comparison's object is absent; every divergence reports at the fold, never absorbed.

NOT DONE (honest): the install-verification (uv run python -c "import ouncemcp") — no routed verb carries the sync from this seat; the spec's green-before-step-2 gate rides the coordinator's own make dev or step 2's mint.
## Reported by jikko — 2026-11-22T21:59:12Z

STEP 2 LANDED -- src/prioritree/store_lock.py whole per the spec's SS1 fence: the Lock context manager (the naming law's symbol; __all__ = ["Lock"]), one advisory exclusive fcntl.flock LOCK_EX blocking on {store_home}/.prioritree.lock, the "a"-open create-if-absent, the inode law (never deleted) in the docstring, the lock path derived from the injected home, never re-defaulted. 91 lines = the fence's 87 + the NOTES' four mandated lines (the __init__ "IO[str] | None" declaration, the __exit__ None guard's two, the __init__ home hold the fenced __enter__ body requires). Two build deltas reported, no pyproject touch: the fence's TYPE_CHECKING tenant Iterator was dead under the classic __enter__/__exit__ shape -- swapped for the needed IO (F401, the zero-findings bar); Path moved under TYPE_CHECKING per TC003 (annotation-only here; the service_store.py:31 precedent). INSTRUMENTS: make lint (ruff ALL) "All checks passed" whole-tree; make typecheck (pyright strict) 0 errors, 0 warnings, 0 informations -- clean at the new file. NOTHING else touched.
## Reported by jikko — 2026-11-22T22:43:31Z

STEP 3 — the two compositions landed per mcpserverspec §3; pyright 0/0/0, ruff zero findings, uv run pytest = 156 passed (the floor held — behavior-transparent: the lockfile is invisible to the RUN-*.jsonl mint glob; the missing-home refusal bytes unchanged).
service_store.py: `from prioritree.store_lock import Lock` added after the Persist import (:31); the six verb heads now `with Lock(self._store_home), self._lock:` — register :125, serve :146, cast :175, census :196, rank :215, manifest :240 — the flock acquired FIRST, the threading.Lock within, per-acquisition.
cli.py: `from prioritree.store_lock import Lock` added (:33, the isort slot); the five handler windows hoist `home = cast("Path", args.home)` and wrap the load+verb whole under `with Lock(home):` — register :205-212, next :235-238, vote :261-271, state :296-299, tally :326-329 — every render OUTSIDE the with, released before rendering.
Docstring clause lines updated per the spec: each verb/handler names the machine-wide file-lock wrap; service_store's module + class clauses amended (the flock outermost, the single-worker banking superseded, the lockfile named in Touches).
Choice reported (collision resolved): the pre-existing `from threading import Lock` aliased `as ThreadLock` (:27) — the spec's bare `Lock` at the heads demands the name for store_lock's Lock; `self._lock = ThreadLock()` (:96); the HTTPException-as-StarletteHTTPException alias precedent.
Same-turn findings: two E501 (serve/manifest summaries at 124>120) trimmed to "under the file lock outermost"; zero new per-file-ignores.
Not done: nothing beyond §3's regions — service.py/web.py untouched (the flock rides inside the seam), zero core edits.
## Reported by jikko — 2026-11-22T23:22:16Z

STEP 4 DONE — the MCP module landed whole, both instruments green.

THE VERIFICATION (the deferred first move, all green): the installed ouncemcp 1.0.0rc3 at the venv's site-packages matches the spec's authored forms — OunceServer(name=...) constructor, the tool decorator's name/effect/idempotency/result_tokens/budget_reason, Effect READ/WRITE/DESTRUCTIVE, the Budget form (4,000 startup default — no override), the error-value forms (OunceError message+hint; InvalidInput/NotFound the raise-at-the-render classes). ONE NON-STOPPING FINDING: the installed middleware clips every error message at Limits.max_error_chars=300 at the Failure render — the ThreePart rides whole in the RAISED error's payload but the WIRE text clips for long refusals (the halt's capped render far exceeds 300); the constructor's pinned form left untouched, the fold rides the author (e.g., a Limits(max_error_chars=...) ruling).

THE LANDING: src/prioritree/mcp_server.py whole (562 lines) — the module-level OunceServer(name="prioritree") (no Budget), the five tools byte-exact (the VERBATIM descriptions + Field texts with "--" em-dashes, the effects, the idempotency flags, result_tokens=4500 + budget_reason on runs.tally), the return models (NextOutcome done-the-tag, CastAck acknowledged's ruled semantics, TallyView's coverage with pairs_expected/pairs_at_quorum, pair_counts elided), DONE a value never an error, the K=10 cap at the halt (<=10 shortfalls pass verbatim; >10 re-derives the weighted legs from a fresh manifest+census read under the module's _lock, legs 1-2 whole + the capped leg 3 with the elision named), the sync bodies, the __main__'s two forms (bare stdio, --serve HTTP), __all__ = ["server"].

ONE DIVERGENCE REPORTED, NEVER ABSORBED: the spec's (h) `with _lock:` wrapping each seam call would SELF-DEADLOCK — the step-3-landed seam verbs already flock, and a second Lock opens a second open file description on the same lockfile (flock binds the open description) — the bodies ride the seam bare (its own flock holds (h)'s ruled order, released before render); the module's _lock guards the halt shaper's fresh-read window alone.

THE NAMED RULING: pyproject per-file-ignores gains mcp_server.py = ["D205"] (the tool docstrings ARE the descriptions VERBATIM — a blank line would fork the accepted wire bytes; SS3(c)'s pre-authorized fire, cited, retires-when named). THE CHOICES: the error class per family (StoreRefusedError => NotFound, VotesRefusedError + the halt => InvalidInput, the service's 404/422 lineage); the payload the labeled ThreePart; the comparator-class Literal static with a runtime fork-guard (the dynamic Literal[tuple(...)] is not a valid static type); pairs_at_quorum = the weighted-count universe (the gate's guarantee at the DONE-only render); LOCK_HOME landed per (c) verbatim (inert — nothing reads it).

INSTRUMENTS: ruff zero findings, pyright 0/0 (run this seat); the ouncemcp check NOT RUN (no fixed-argv act here — step 6 + kensho's instrument per the spec SS6); the runtime import proof rides step 5's tests. NOTHING ELSE touched: the core, the routes, the Makefile, the grant rows — all untouched.
## Reported by jikko — 2026-11-22T23:43:47Z

Step 5b landed: tests/test_store_lock_face.py whole — 516 lines, 10 test arcs, all green (10 passed in 2.05s).
The arcs per the spec's SS5(a) fence: lockfile created on demand (absent before, present at __enter__); never truncated (the preseeded-sentinel probe); the home-injection derivation (two homes, two lock paths); release at the with-block's exit (second acquisition immediate); the reentrant second open (two Lock opens on one path from one process — the second BLOCKS until the first releases, per the fence, observed through a 0.5s window); the exclusivity bounded wait (Popen child holds 1s, the parent's enter observed against a 0.5s FLOOR, never a ceiling); the two-process probe (the fixed-argv sys.executable -c child casting N=4 beside the parent's M=3 on one shared store — the mint-order load green, the torn-tail refusal absent, census total 7 with contiguous VOTE-0001..0007 ids and both processes' comparators counted); the CLI-subprocess register beside the in-process register (stems exactly {RUN-0001, RUN-0002}, both manifests intact); the service verb beside the core register (Serialize.register + Persist.register concurrently, distinct stems, no half-write); the never-deleted law (the lockfile present after the acts).
Also landed: pyproject.toml's per-file ruling for the file — three S603 fires at the Popen sites named, S607 carried per the re-carried test_harness/test_service_acceptance precedent (the spec's step-5 mandate; the only touch beyond the file itself).
Instruments: ruff check src/ tests/ zero findings; pyright 0 errors/0 warnings; the file's 10 arcs green.
NOT done: test_mcp_server_face.py (5a's own dispatch — untouched per the fence); the whole-floor run (step 6's own); nothing else touched.
## Reported by jikko — 2026-11-22T23:55:54Z

STEP 5a LANDED -- tests/test_mcp_server_face.py whole per the spec's SS5(b) fence: 614 lines, 30 arcs, all green.

THE ARCS: the five tools' success forms field-for-field (the register ack with the verdicts echo, the one-model pair triple, the cast ack, the census's exact two-key body, TallyView whole at full coverage) + DONE a value never an error (done=true the RESULT, the seven-key shape, the three fields); the structured ThreePart asserts at every refusal surface (unknown run at next/census/tally over the wire's labeled segments, the out-of-set verdict, the class refused at the SCHEMA via the typed form AND at the CORE on a model_constructed corrupted body); the SAFE HALT both ways (the under-cap passthrough whole on the wire, the K=10 capped render probed at the payload -- legs 1-2 whole, the elision named in found AND next_action, the tenth shown / eleventh capped -- and at the wire, where the 300-char clip [the step-4 finding] ends the text at the asserted ellipsis); the idempotency replay arcs riding fresh as_caller sessions (the byte-identical re-send acknowledged=true with the count unchanged and the original's vote_id; the changed verdict a new record; the cross-session re-register minting RUN-0002); the stamps' gates, supersedes both ways, the seed's stability, the llm class at equal weight, the un-served-pair cast, the census's AS-IS after a correction, the quorum skip, the full sitting end-to-end, and the re-tally after the cure.

THE HARNESS + ISOLATION: as_caller around asyncio.run(server.call_tool) (the census's proof form); a unique caller subject per test -- the guard replays per principal, a shared subject would cross-wire tests through the server's MemoryStore; the module's _seam/_lock re-bound and STORE_HOME redirected (the halt shaper's fresh read) via monkeypatch's string form -- the real store home never touched on disk.

ONE DIVERGENCE REPORTED, NEVER ABSORBED: the installed pydantic's literal-error renders "human or llm" (not "human, llm" as ouncemcp's own phrasing suggested) -- the assert landed at the installed bytes, the import-verification lesson carried by construction.

INSTRUMENTS: this file 30/30 green; ruff whole-tree "All checks passed"; pyright 0 errors, 0 warnings, 0 informations -- zero new per-file-ignores (S603/S607 never fired: no Popen in this file).

NOT DONE (honest): test_store_lock_face.py (5b's own dispatch, untouched); the floor-wide pytest run + the ouncemcp check re-run (step 6's own read-backs); zero pyproject bytes, zero core bytes, zero edits beyond the one new file.
## Reported by jikko — 2026-11-22T23:56:44Z

Step 6 of 7 — the floor (jikko's fixed-argv acts), run 2026-11-22.

Test act (all): "196 passed in 25.65s" — matches expectation exactly (156 + 30 MCP face arcs + 10 flock face arcs). No failures, no skips shown.

Lint act (check): "uv run ruff check src/ tests/ — All checks passed!" — zero findings.

Typecheck act: "uv run pyright — 0 errors, 0 warnings, 0 informations" — zero findings.

No findings outside expectations — nothing to edit, nothing deferred. The floor is green across all three acts; step 6 complete.
## Reported by jikko — 2026-11-23T00:55:23Z

Step 7a (the fold's landing) done: togo's six amendments applied to src/prioritree/mcp_server.py as one 6-hunk patch, byte-verbatim per the fold's AFTER fences (reports/synthesize/mcpserverspec.md, togo's fold 2026-11-23T00:49:24Z).
- Region A (register docstring, now :454-464): the operator_id/question sentence + the idempotency reconciliation clause (retried identical call within a session vs a deliberately changed list).
- Region B (runs.next docstring, now :480-488): the seed clause (same seed re-serves deterministically; omitted, the run_id-derived default) + the done:true three-fields clause.
- Region C (runs.tally docstring, now :537-546): the components/cycle words (disconnected islands; structural loop dissolved into win fractions, never a data-quality error).
- Region D (now :85, :92-101, :148): _FORKED_VERDICTS constant; Winner = Literal["prefer-a", "prefer-b", "tie"] with the WEAK_ORDER_TRIPLE fork-guard (ComparatorClass's school); CastInput.winner retyped Winner, TEXT_WINNER unchanged.
Read-back confirms all six regions on disk exactly; nothing else touched (region E / the test split is 7b's dispatch). No lint or typecheck run — the coordinator's instruments (kensho) hold that lane.
## Reported by jikko — 2026-11-23T00:58:28Z

Step 7b done — the fold's test half landed in tests/test_mcp_server_face.py (the only file touched; two hunks).
test_cast_out_of_set_verdict_refused SPLIT per REGION E1: (a) test_cast_winner_refused_at_the_schema — the winner-must-be-one-of typed form, "expected:" absent (the round-trip saved); (b) test_cast_winner_refused_at_the_core — CastInput.model_construct past validation fed to mcp_server.cast, pytest.raises match="a verdict from the run's declared set" (the core's ThreePart preserved; votes.py:429 the ground).
The module docstring's (2) clause folded per E2: the out-of-set winner now named in the both-ways school ("a corrupted body past validation" — class-specific word elided).
Grounds checked before the apply: the fold's module half (Winner Literal, mcp_server.py:99/:148) already on disk; the core's expected text verified at votes.py:429.
The schema-leg's prefix assert kept at the spec's safe form ("`winner` must be one of") — the three-member join's exact render left to observation (the fold's named unknown).
Read-back: both arcs + the clause verified verbatim after the apply. Nothing else touched; tests NOT run (the coordinator's instruments).
## Reported by jikko — 2026-11-23T00:59:14Z

Step 7c — the fold's floor: the three fixed-argv acts run on the prioritree host, all within expectations; no findings outside, no edits made.

- test (all): 197 passed in 26.24s — the expected 197 (the 196 + the split's net +1, 30 → 31 arcs in the face file).
- lint (check): uv run ruff check src/ tests/ — All checks passed!
- typecheck: uv run pyright — 0 errors, 0 warnings, 0 informations.

The floor is clean; the disk is the truth.
