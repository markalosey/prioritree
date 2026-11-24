<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — build/key-infrastructure

**Route:** prioritree-auth (executing) | **Events:** 18 | **Reports:** 9

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-24T14:04:08Z |
| 2 | dispatch | shinko | 2026-11-24T14:04:19Z |
| 3 | report | jikko | 2026-11-24T14:32:44Z |
| 4 | report | jikko | 2026-11-24T14:57:43Z |
| 5 | dispatch | shinko | 2026-11-24T14:59:34Z |
| 6 | dispatch | shinko | 2026-11-24T14:59:46Z |
| 7 | report | jikko | 2026-11-24T15:12:25Z |
| 8 | report | jikko | 2026-11-24T15:25:06Z |
| 9 | dispatch | shinko | 2026-11-24T15:26:25Z |
| 10 | dispatch | shinko | 2026-11-24T15:26:36Z |
| 11 | dispatch | shinko | 2026-11-24T15:26:46Z |
| 12 | report | jikko | 2026-11-24T15:46:35Z |
| 13 | report | jikko | 2026-11-24T15:58:17Z |
| 14 | report | jikko | 2026-11-24T16:02:24Z |
| 15 | dispatch | shinko | 2026-11-24T16:04:08Z |
| 16 | report | jikko | 2026-11-24T16:05:27Z |
| 17 | dispatch | shinko | 2026-11-24T16:07:54Z |
| 18 | report | jikko | 2026-11-24T16:09:03Z |
## Reported by jikko — 2026-11-24T14:32:44Z

STEP 2/8 — key_verify.py landed whole: 208 lines (the spec's §2 fence: 41 — the pseudocode's elisions unfurled: the two typed error classes, the five-field docstrings, the TYPE_CHECKING import law).
The contract whole: the stat ride before the lookup -> the sha256 -> the digest lookup -> the ONE compare (hmac.compare_digest at :192; the fence scan pre-fired: source count == 1) -> F5 audience (the SAME 401, never naming the record's audience) -> F8 (the record's class rides the record; no claim parameter) -> the scope check (KeyScopeError 403) -> the record. The ThreePart bodies typed data: 401 = the named header / absent-or-unknown / the mint teaching; 403 = the route's scope / the key's scopes / re-mint. Ruff-ALL green, zero rulings (§6 held).
CHOICES: the docstring's one compare mention reworded ("the constant-time compare") — the verbatim token would break the spec's own twice-ruled fence (count == 1); the 401 constructed once (_refuse_unknown_key) so the miss, the compare-fail, and the audience legs render the SAME 401; the compare's failure branch landed (the fence shows none) — an unverifiable digest refuses honestly.
GAPS NAMED: pyright red on 19 findings, all one seam — prioritree.key_store absent at landing (the parallel step 1, dispatched 11s before mine; resolves when it lands). SEAM FOR STEP 1: §2's step 7 calls store.reload_if_changed(home) — a surface §1's KeyStore fence does NOT name; step 1 must land it or pyright stays red past its landing. FOR STEP 7: the landed sha256 counts are hit = 1, miss = 2 (the F9 dummy is the miss's fingerprint; the spec's "hash count equals the hit's" gloss reconciles there).
## Reported by jikko — 2026-11-24T14:57:43Z

Step 1 landed: src/prioritree/key_store.py WHOLE per the §1 fence — 600 lines (the fence's 132-line sketch expanded by the five-field docstring law).
Surfaces: KeyRecord (frozen, six fields); KeyStoreRefusedError (the run_store three-field grammar); KEYS_HOME + PRIORITYTREE_KEYS_HOME at resolve_keys_home; the mint ceremony (token_urlsafe(32) -> sha256 -> sort_keys one-line append -> chmod 0600 AFTER the write); the load (stat check first, pre-pass whole, dup-digest, crash-tail; absent = empty dict, never a refusal); mtime + reload_if_changed (the landed key_verify.py's store.reload_if_changed(home) call form honored); resolve_auth_mode (on/off, typo refuses loudly); render_boot_marker (off-degrade / absent-failopen / present-count).
Choices reported: (1) the home rides the constructor — the fence's 6-param mint breaks PLR0913's 5-arg bar and §6 expects zero rulings; (2) "--" dashes kept verbatim per the fence + the landed key_verify.py sibling; (3) __all__ re-sorted per RUF022's isort order (same six names); (4) Path.chmod per PTH101 (the fence's module-docstring prose byte kept).
Not done: the REPL mint round-trip — no shell at this seat (kensho's read-back covers).
Read-backs: ruff ALL and pyright strict both green over the tree (key_verify.py's KeyStore imports type-check against the landed surface).

## Reported by jikko — 2026-11-24T15:12:25Z

The AUTH knob landed per the spec's §5 fence; nothing else touched.
Makefile: `AUTH ?= on` at :7 (beside the standing variables, the ?= precedent); both launch lines widened to `env -u WEB_CONCURRENCY AUTH=$(AUTH) ...` — start :33, mcp-start :82 (environment carriage only; mcp_server never imports service, its surface untouched).
service.py: the ONE construction line `app.state.auth = resolve_auth_mode(os.environ.get("AUTH"))` at :193 after the seam injection — the thin carrier over key_store's own resolution (a typo'd AUTH refuses loudly at boot, the process dies honestly).
The boot marker: the key store loaded once at boot (:194, KeyStore over resolve_keys_home().absolute()), the count true, the three states the store module's own render_boot_marker, emitted at INFO on the uvicorn.error boot channel (_BOOT_LOG_CHANNEL — the channel server.log captures; under pytest the channel is unconfigured, the render silent by design).
Choices reported: the load fires at boot regardless of mode (the off marker's count is the TRUE count — a corrupt store kills even an off boot, the honest compose); the loaded store is NOT held on app.state (beyond the fence — the next unit's seam).
Read-back, the three states at render_boot_marker's rendered form: on+present `auth: on | keys: {abs} | count: {n}`; on+absent `auth: on (failopen -- no key store) | keys: {home} | next-action: prioritree key mint`; off `auth: off (operator's explicit degrade) | keys: {abs} | count: {n}`.
Not done: routes/web/mcp untouched; no instrument runs (the coordinator's instruments); the live-boot probes (make start AUTH=off / AUTH=bogus) left to the gate. One in-turn fix: COM812 trailing comma on the marker emit (the patch's finding, fixed same turn).
## Reported by jikko — 2026-11-24T15:25:06Z

Step 3 (R8 file-unit, R11 report) — cli.py's key region landed per §3's fence: the nested "key" group (dest="action", required) carrying "mint" — comparator_id positional; --class/--scopes/--audience door-validated at the store (NO choices=; --scopes required, the CLI splits on ","), the mint's own --home parent defaulting KEYS_HOME (never conflated with the runs' STORE_HOME).
_command_key_mint composes KeyStore(home).mint (the CLI never re-implements the ceremony) under a machine-wide flock, then reports key\t{key} / digest\t{digest} / mode\t0600 marker-first via _report; KeyStoreRefusedError joined the exit-1 tuple clause; the five HANDLERS byte-untouched (defs :218/:259/:285/:319/:348, the five dispatch lines identical, KEY inserted at :479).
Choices made (fence-letter vs landed seams, reported): Lock(home.parent) — store_lock derives its lockfile INSIDE a directory home and KEYS_HOME is a file; the literal "Lock(keys_home)" would mkdir keys.jsonl as a directory and break every first mint. dest="comparator_class" on --class (args.class is a keyword). MODE_LANDED="0600" + SCOPES_SEPARATOR="," named constants.
Docstring deltas: _build_parser's summary/Purpose and command()'s refusal enumeration/Re-run/Touches/Provenance updated to stay true to the widened surfaces (honest docs on changed bodies).
Read-back: the region verbatim (constants :86-100, parser :196-215, handler :399-439, tuple :486); ruff check + pyright ZERO findings; tests/test_cli.py 17 passed (the five standing subcommands re-run green).
Not done / flagged: the module docstring left byte-untouched per the fence — its "three typed refusals" + tier-fence import enumeration now undercount (a follow-up for the coordinator); `prioritree key mint --help` bytes not captured (no shell at this seat — the parser's construction proven by lint/typecheck/the green suite); the PRIORITYTREE_KEYS_HOME env knob stays the service's boot resolve (resolve_keys_home), not the CLI's --home default, per §1/§3 — noted for step 8's "env override home" arc.
## Reported by jikko — 2026-11-24T15:46:35Z

Landed tests/test_key_mint.py WHOLE (the spec's named home; the dispatch's test_cli_key.py alias resolved to it per the fence) — the 8 arcs per §4, the test_cli.py school (command() in-process, --home tmp_path homes only, no subprocess): (1) the success stdout — the key\tdigest\tmode triple, exit 0, the digest the key's own sha256; (2) THE PLAINTEXT'S ONCE — stdout carries the key exactly once, the file's bytes plaintext-ABSENT; (3) the record on disk — the digest present, the mode 0600; (4) the vocabulary refusals at exit 1 (3-id parametrize: the bad class / bad scope / bad audience — the store's typed door, never argparse choices=, no file written); (5) argparse at 2 (the missing comparator_id); (6) the --home placement AFTER the subcommand (two homes routed, the digests never conflated); (7) the env override home — PRIORITYTREE_KEYS_HOME inert at the CLI (the service's boot knob per step 3's note; the --home flag the CLI's only override — the env path never created); (8) the second mint appends (two lines, two digests, the mint order held).
Read-back: pytest on the file green — 8 arcs / 10 runtime items (the parametrize's 3); ruff check green (zero findings, no new rulings — the standing S101/PLR2004 ruling covers); pyright strict 0 errors.
Gap found: the key family's refusal prefix renders "refused -- expected:" (key_store.py:95, double hyphen) where the cited StoreRefusedError precedent renders "refused — expected:" (run_store.py:93, em dash) — the arc-4 assertion pins the LANDED bytes; flagged for the coordinator (a harmonization would re-touch that one prefix line).
Nothing else touched — one file per the fence.
## Reported by jikko — 2026-11-24T15:58:17Z

tests/test_key_store.py landed whole (311 lines) — the spec §4's 13 arcs, NOTHING else touched.
Arcs: the mint's record bytes (six fields, sort_keys, hashed-at-rest asserted via key-not-in-file + sha256 round-trip); the 0600 mode (S_IMODE == 0o600); the second mint's append; the mint's and the load's world-writable refusals (chmod 0o666 first, ThreePart named, the never-widened line-count pinned); the corrupt-line parametrizes (7 ids, each refusing with the form named from the cited SCOPE_TOKENS/AUDIENCES/COMPARATOR_CLASSES); the absent-store-empty-dict (mtime None, never a refusal); the mtime reload (mid-flight mint by a second container live at the next read); the mid-flight chmod refused at re-load (last-good state stands); the marker's three renders byte-exact (on+present, on+absent failopen, off degrade); the AUTH knob's three parametrized (default on, off, typo 'onX' refused loudly); the mint's vocabulary refusals (typed three-field data, nothing written — gates fire before the mkdir); the scopes sorted-deduped on the wire.
Fixtures per the tree's precedent: tmp_path homes only, the corruption mutations per the test_run_store _corrupt school; no monkeypatch needed (the knob/env surfaces take injected values — the env-override home arc is test_key_mint.py's, not this file's).
Read-back: 13 test functions, the names matching the spec's arc list; parametrizes 7+3+3 = 23 runtime items total.
Two ruff findings on the first apply (COM812 trailing comma, RUF005 list concat) — both fixed in the same turn; the re-apply reported zero findings. pytest/pyright runs are the coordinator's instruments (not run here — never verify your own work).
## Reported by jikko — 2026-11-24T16:02:24Z

Step 4b (R8 file-unit, R11 report) — tests/test_key_verify.py landed WHOLE per §4's fence: the 9 arcs at the spec's count, names and order matching (right key → the identity whole; wrong key → the 401 byte-exact; the dummy compute; the one-compare-site fence; audience; class; scope's two; reload-through-verify; absent header). 186 lines; nothing else touched.
The fixture forms per the tree's precedent (the just-landed test_key_mint.py sibling's school): tmp_path keys homes, the _minted_store fixture minting through the landed store, underscore payload constants, the 401 trio pinned once in _assert_same_401 — the SAME bytes at the digest miss, the wrong tier, and the absent header (the oracle never fed; F5's "mcp never named" asserted over the rendered refusal).
The F9 reconciliation (step 2's deferred seam) landed in the counter arc: hit = 1 (the presented key hashed once on BOTH paths — the spec's "count equals the hit's" gloss holds on the shared leg), miss = 2 (the dummy the miss's added fingerprint, its sentinel bytes pinned) — never less hash work than the hit's, the short-circuit killed.
The fence per the test_service_store.py:238 school: source.count("compare_digest") == 1 (pre-verified: exactly one in the landed module). The class arc pins F8 both ways: the record's class returned whole (llm + human legs) and "claim" absent from verify's signature (no claim parameter exists).
Read-backs: the file's suite 9 passed (0.06s); ruff check over src/+tests/ ALL PASSED (zero new rulings — the standing S101/PLR2004 covers); pyright 0 errors / 0 warnings / 0 informations.
Not done: nothing else touched — kensho's second eyes pending.
## Reported by jikko — 2026-11-24T16:05:27Z

The floor, jikko, 2026-11-24 — the pack's three fixed-argv acts:
test (all): 245 collected — 244 passed, 1 failed in 26.53s. The exact count: 245 (above the ~241 estimate).
lint (check): "All checks passed!" — ruff over src/ and tests/, zero findings.
typecheck: "0 errors, 0 warnings, 0 informations" — pyright clean.
Finding, outside expectations, report-only — no edit made:
FAILED tests/test_key_store.py::test_corrupt_line_refused_form_named[crash-tail] — FileExistsError
[Errno 17] at tests/test_key_store.py:198: the crash-tail case calls home.parent.mkdir(parents=True)
on tmp_path itself, which pytest pre-creates, without exist_ok=True — the setup crashes before
the corrupt-tail load-refusal under test is exercised.
## Reported by jikko — 2026-11-24T16:09:03Z

# jikko — build/key-infrastructure, step 8b (the fold's landing + the floor re-run)

THE FIX (the fold, synthesize/keyinfrastructurespec's before/after): tests/test_key_store.py:198 — `home.parent.mkdir(parents=True)` → `home.parent.mkdir(parents=True, exist_ok=True)`; the arc's assertion :202-205 untouched; the store module untouched (its mint already correct). Nothing else touched.

THE FLOOR RE-RUN (verbatim):
1. test all: `245 passed in 27.44s` (the expected 245, all passing)
2. lint check: `All checks passed!`
3. typecheck: `0 errors, 0 warnings, 0 informations`
