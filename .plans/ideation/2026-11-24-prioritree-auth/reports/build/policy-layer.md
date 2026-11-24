<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — build/policy-layer

**Route:** prioritree-auth (executing) | **Events:** 22 | **Reports:** 11

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-24T18:35:43Z |
| 2 | report | jikko | 2026-11-24T18:40:52Z |
| 3 | dispatch | shinko | 2026-11-24T18:41:18Z |
| 4 | report | jikko | 2026-11-24T19:00:00Z |
| 5 | dispatch | shinko | 2026-11-24T19:02:03Z |
| 6 | report | jikko | 2026-11-24T19:03:47Z |
| 7 | dispatch | shinko | 2026-11-24T19:05:41Z |
| 8 | dispatch | shinko | 2026-11-24T19:05:57Z |
| 9 | report | jikko | 2026-11-24T19:09:01Z |
| 10 | report | jikko | 2026-11-24T19:17:10Z |
| 11 | dispatch | shinko | 2026-11-24T19:23:05Z |
| 12 | report | jikko | 2026-11-24T19:24:31Z |
| 13 | dispatch | shinko | 2026-11-24T19:24:50Z |
| 14 | report | jikko | 2026-11-24T19:27:43Z |
| 15 | dispatch | shinko | 2026-11-24T19:29:35Z |
| 16 | report | jikko | 2026-11-24T19:39:21Z |
| 17 | dispatch | shinko | 2026-11-24T19:39:52Z |
| 18 | report | jikko | 2026-11-24T19:56:52Z |
| 19 | dispatch | shinko | 2026-11-24T20:02:11Z |
| 20 | report | jikko | 2026-11-24T20:10:15Z |
| 21 | dispatch | shinko | 2026-11-24T20:16:45Z |
| 22 | report | jikko | 2026-11-24T20:43:49Z |
## Reported by jikko — 2026-11-24T18:40:52Z

# Step 1 landed — src/prioritree/policy.py per the spec §1's fence

The module WHOLE: ROLES the three-name vocabulary; ROLE_SCOPES as MappingProxyType over frozenset literals — operator {register, state, tally, manifest}, comparator {next, cast, manifest}, auditor {state, tally, manifest} (the six tokens re-declared as literals, the rows verbatim); granted_scopes (the unknown role -> the empty set, default-deny as data); missing_classes (the per-pair class counts -> COMPARATOR_CLASSES minus the count>=1 classes; the one runtime import votes.COMPARATOR_CLASSES, cited never re-declared). Five-field docstrings verbatim from the fence.

TWO FORCED DELTAS — the fence's exact bytes failed ruff ALL on first apply (TC003 + COM812); the zero-findings bar and the spec §4's own no-ignore ruling (pyproject UNTOUCHED) fixed them same-turn:
(1) TC003: `from collections.abc import Mapping` moved under `if TYPE_CHECKING:` — the tree's uniform idiom (tally.py :29-30 the precedent); +2 lines.
(2) COM812: the trailing comma at the grant map's dict close (line-neutral).

LANDED: 89 lines, NOT the fence's 87 — the +2 is the TYPE_CHECKING block; every other byte fence-verbatim (the docstrings, the comments, the two predicates, the § signs).

FORK-GUARD: zero key_store imports — the runtime import block cites votes alone; the import-form grep over policy.py returns 0. The bare grep's 2 hits are the fence's own PROSE (docstring :13, grant-map comment :36 — the spec's ruled bytes naming the vocabulary's home, documentation not import); the dispatch's "grep zero" read-back does not hold for the bare token as the fence itself carries the name.

Second apply: zero findings. Nothing else touched; no pyproject edit; no ignores added. The lint/type findings rode the patch's own apply — the coordinator's kensho is the verification.
## Reported by jikko — 2026-11-24T19:00:00Z

# STEP 2 LANDED — tally.py's five seam regions (policylayerspec §2's fences; 521 -> 570 lines)

(a) fence line :17-19 (the CLASS stamp read at the coverage GATE alone; the untouched em dash stands) + imports :29-31 (policy.missing_classes; votes.COMPARATOR_CLASSES; isort order).
(b) CoverageDatum :88 `pair_class_counts: Mapping[Pair, Mapping[str, int]]` after pair_counts; the Purpose clause grown :71-73.
(c) counting pass: _Counted :158; the rollup initialized over the full universe :211-213 (every vocabulary class 0); the CLASS STAMP accumulated in the SAME pass :220 (riding the weighted set, superseded excluded); the return's second argument :235.
(d) gate: missing_class_pairs from the policy predicate :529-533; THE FOURTH CONJUNCT :534; the expected's FULL conjunction :536-538; the renderers' grown calls :542-547; the emission's field :566; tally_votes' docstrings grown :481-484 + :492-495.
(e) renderers: signatures gained the leg-4 parameter (:352, :391); the uncorroborated section :379-384; the floor's cure :421-427 (floor_head, the ONE em dash — R6).
SIGNATURE byte-standing: `def tally_votes(...)` at tally.py:471 byte-identical; session.py:294 `def tally_rank` untouched; zero caller edits; mcp_server's local mirror untouched (the spec's named drift).
DEVIATION (named): the fence's (d) multi-line renderer calls carried no trailing commas — ruff COM812 flagged both in the patch findings; commas added (:543, :546) per the zero-findings bar — zero rendered-byte effect.
NOT done: the floor-green instruments (step 15 + kensho's verification). OBSERVED: _next_action_sections' docstring still names the old section set (the spec ruled no growth for it) — left untouched per the fence, named here.
## Reported by jikko — 2026-11-24T19:03:47Z

Step 3 of 15 (build/policy-layer, R8 file-unit) landed: acceptance.py's harness builder per §3c's R5 fence — the two regions plus the fence-mandated imports, nothing else.
- The stamp block: HARNESS_COMPARATOR_CLASS ("llm") retired; HARNESS_JUDGE_CLASSES: Final[tuple[str, ...]] = tuple(sorted(COMPARATOR_CLASSES)) stands — the votes import grown at the runtime block, Final joining typing (the tree's convention, store_lock/policy form); the comment rewritten to the parity-over-the-ruled-set meaning, R5's now-false "zero tally effect" clause replaced with the identity framing (the block honest under F8).
- The cast: comparator_class=HARNESS_JUDGE_CLASSES[pair_count % len(HARNESS_JUDGE_CLASSES)] — judge 1 human, judge 2 llm, judge 3 human at k=3; the class derives from the deterministic census count, zero RNG draws consumed, the replay byte-identical.
- Verified before the apply: the retired constant's only two code references were the two fenced regions (grep tree-wide); every accept_run call in test_acceptance.py rides the default k=3 (no quorum overrides) — the byte-unchanged file corroborates under the parity.
- Not done (not this step's fence): test_acceptance.py, the tally/policy seams (steps 1-2 already on disk), the floor-green make (step 15); the package's lint/typecheck rides the coordinator's instruments.
## Reported by jikko — 2026-11-24T19:09:01Z

Step 4 (R8 file-unit) landed: tests/test_policy.py NEW, whole per synthesize/policylayerspec §3a's fence — 10 arcs; nothing else touched.
The 10 arcs at the spec's names: test_grant_map_rows_exact, test_granted_tokens_pin_scope_tokens, test_roles_vocabulary_exactly_three, test_grant_map_frozen_data_form, test_default_deny_absence_is_the_denial, test_unknown_role_denied_whole, test_comparator_manifest_hole_closed, test_missing_classes_both_present_empty, test_missing_classes_names_the_absent_class, test_missing_classes_zero_count_not_present.
The fork-guard's assertion quoted: `assert granted <= SCOPE_TOKENS` (granted = the union of ROLE_SCOPES' rows) — the map's granted vocabulary pinned against key_store's, policy.py importing nothing from key_store, the independence deliberate.
Three instrument-forced deltas from the fence's literal bytes, all semantic-neutral, fixed in-turn to zero findings: the policy import ordered ROLE_SCOPES, ROLES (ruff I001); the fork-guard's accumulator typed set[str]() (pyright strict's reportUnknownVariableType); the roles-vocabulary assert's sides swapped (ruff SIM300). No new ignores; pyproject.toml untouched.
Not done (other steps' units): policy.py edits, test_tally.py's 13 new arcs, the tally seam regions, the faces' fixture growth. No self-verification run — the coordinator runs the instruments.
## Reported by jikko — 2026-11-24T19:17:10Z

Step 5 (tests/test_tally.py): LANDED — the _vote helper grown per the §3b fence (keyword-only comparator_class, default "human"; the docstring byte the fence's "--"), the 13 arcs appended at the spec's names and order (:291-462, 9 floor + 4 grammar), byte-verbatim from the fence; the standing arcs byte-identical (:77-:275), the class-mix fixture growth NOT this step's, nothing else touched.
One in-scope cure: arc 13's next_action tuple element parenthesized — the fence's bytes fire ISC004 + pyright's concat-in-collection; the parenthesized continuation is the tree's ruled idiom (R8, tally.py :535-538's class), the asserted string value unchanged.
FINDING 1 (ruling needed; pyproject untouched per §4 + the step's scope): PLR0913 fires on _vote's ruled 6-parameter signature (6 > 5). The only legal cure is the named per-file-ignores entry — "tests/test_tally.py" = ["PLR0913"] citing the policylayerspec §3b fence (the votes.py/run_store.py precedent form) — ready for the coordinator's ruling; the tree's zero-in-code-ignores law bars a noqa.
FINDING 2 (the fence's own contradiction, landed verbatim, ruling needed): test_halt_next_action_two_cures_distinct's third assert (startswith "cast the bridging pairs") cannot hold under its fenced fixture — votes on (a,b)+(a,c) union-find to ONE component (tally.py :524-525, :408), so no bridging section; that next_action starts "cast the missing votes". One-line candidates: the §2(e) worked whole's one-vote fixture (the spec's own rendered example), or the needle change. The other 12 arcs derive green against the landed tally; the coordinator's instruments decide.
## Reported by jikko — 2026-11-24T19:24:31Z

# Step 5b — the fold's two fixes landed (jikko, build/policy-layer)

1. pyproject.toml: the PLR0913 entry `"tests/test_tally.py" = ["PLR0913"]` landed at :163, in the per-file-ignores region after the test_store_lock_face.py block (:156), before [tool.ruff.format] (:165) — the fold's RULING comment verbatim (:158-162), the existing entries' shape followed.
2. tests/test_tally.py: test_halt_next_action_two_cures_distinct cured — the ab+ac mis-copy deleted; the votes tuple is now the single VOTE-0001 on _AB_PAIR at :451 (`votes = (_vote("VOTE-0001", _AB_PAIR, PREFER_A),)` per the fold's bytes); the manifest ["a","b","c"] (:450) and the arc's THREE asserts (:454-456) byte-verbatim unchanged. The arc now renders the two components {a,b} + {c} with the bridge (a,c) — the §2(e) worked whole's own shape.
3. NOTHING else touched — both hunks applied clean (2 files, no findings); the read-backs confirm the landed bytes. Not done here: lint/type/test runs (the coordinator's instruments, kensho the second eyes).

## Reported by jikko — 2026-11-24T19:27:43Z

Steps 6-7 of 15 (R8 file-unit, two dispatches) landed: the DONE-reaching fixtures' class-mix growth per policylayerspec §3c's fence — two patches, zero findings, nothing else touched.
- test_session.py, 3 arcs grown: (1) test_end_to_end (:44-73) — each of the three casts gains its llm corroborator (same winner, id "x") -> 6 casts; emission asserts doubled (wins {"a": 4,...}, losses/ties {"a": 0, "b": 2, "c": 2}, pair_counts 2 each); ranked_groups/components unchanged. (2) test_prefix_tally (:105-116) — the loop casts each pair's human then llm vote (same winner) before the suppressed tally; the final assertion stands. (3) test_five_ops (:119-136) — the corroborating cast (the fence's exact byte, ("a","b") prefer-a id "x" class llm) lands after the read_vote_state assertions, before tally_rank; ranked_groups (("a",), ("b",)) stands.
- test_run_store.py, 2 arcs grown: test_round_trip (:46-76) and test_supersede_replay (:183-203) — the fence's three corroborating casts appended (ids VOTE-0005..0007, y-llm/z-human/w-llm) after the correction / after VOTE-0004; every before/after equality stands, log[1] still the correction.
- Non-DONE arcs byte-unchanged (verified by read-back): the seam-divergence halt's "(a, b) 1 of 2" needle, _cast_all + done-signal census arcs, the refusal/unknown-run/zero-vote/quorum-two arcs; run_store's corruption parametrize, crash-tail, empty-run, dedup arcs.
- OBSERVATION (fence-silent, left untouched, named for the coordinator): the grown arcs' docstrings stay byte-verbatim per the fence — test_session :45 "cast three" and test_run_store :47 "four casts" now under-count the grown fixtures (6 and 7 casts); the spec's §3c rules docstring edits nowhere in these two files.
- Not done (other steps' units): the remaining faces' growth (cli/service/mcp/harness/web/acceptance), the floor-green instruments, kensho's verification.
## Reported by jikko — 2026-11-24T19:39:21Z

# Steps 8-11 landed (jikko, build/policy-layer; R8 file-unit — four dispatches, one report)
Step 8 (test_acceptance.py): ZERO-DIFF per §3c's own ruling ("BYTE-UNCHANGED — every arc rides accept_run; the class stamps never asserted"); the measured arcs' vote chains carry the mix via the harness already on disk (acceptance.py :90 HARNESS_JUDGE_CLASSES, :268 the parity cast — step 3); read back whole, no edit owed.
Step 9 (test_cli.py): _LLM joins after _HUMAN (:32); _cast gains comparator_class (default _HUMAN — standing single-class calls byte-identical); _drive_abc_to_coverage 6 casts human+llm per pair (:71-76); _TALLY_ABC grown — a 4/0/0, b 2/2/0, c 0/4/0, pairs 2 each; rank/coverage/version lines byte-identical (:41-53).
Step 10 (test_service_store.py): the equivalence arc's acts 3→6 (:146-151 — each original act joined by its twin, the fence's order: ab human+llm, ac llm+human, bc human+llm); both arms replay the same 6; every seam-vs-raw equality stands (in-process TallyResults, no wire).
Step 11 (test_service_face.py): the tally arc nests the class pair → 6 posts (:120-129, the human body + the same body with comparator_class llm); the body grown — wins {a:4,b:2,c:0}, losses {a:0,b:2,c:4}, pair_counts 2 each; ranked_groups/done/cycle/components unchanged (:133-144); the 409 arc's "at quorum" needle + every non-DONE arc untouched across all three files.
FINDING (ruling needed; fence landed, the step-5 precedent): the service tier's 200-tally render crashes under the grown datum — service.py's ONE priced reconciliation (:513-514, replace(..., pair_counts={}) + asdict) strips pair_counts alone; pair_class_counts (tally.py :88/:566) is ALSO Pair-keyed and rides asdict — the tree's own recorded crash class (service-face-bytes.md: "crashing on the unhashable dict keys inside _asdict_inner").
The grown test_tally_success — the first corroborated wire tally — surfaces it at step 15; the spec §4's own intent ("the new datum field rides UNSERIALIZED") names the cure's shape (the replace-strip's second field, service.py's tier — fenced off here per §4's "zero tier edits"); the web tier rides the same wire downstream (web.py :517-519); the CLI/store/acceptance arcs are asdict-free, unaffected.
OBSERVATION: fence-silent docstrings stay byte-verbatim (cli _drive's "voted at k=1", store's "the same acts", face's "full coverage") — the steps 6-7 precedent.
Not done: steps 12-14 (the other faces), step 15 (the floor-green make); no self-verification — the coordinator's instruments + kensho decide.
## Reported by jikko — 2026-11-24T19:56:52Z

# Steps 12-15 landed (jikko, build/policy-layer; R8 file-unit — four patches, one per file; §3c's fixture-growth fence, the DONE-reaching arcs grown, the non-DONE arcs byte-unchanged)
- Step 12 tests/test_service_acceptance.py: _drive_arc's loop posts each pair's _VOTE_BODY form then its llm twin {**_VOTE_BODY, "comparator_class": "llm"} -> ELEVEN requests; test_accept_the_eleven_request_arc (renamed per the fence) — len 11, statuses [201 + ten 200s], acks bodies[3..8] VOTE-0001..0006 counts 1..6 acknowledged False, done bodies[9], the tally body bodies[10] grown (wins {a:4,b:2,c:0}, losses {a:0,b:2,c:4}, ties 0, pair_counts 2 each; ranked_groups/components unchanged); the four docstring tokens "eight-request" -> "eleven-request" (the fence's ruled swap, module :6, _drive_arc :177, the test :217, the replay :281); test_refuse_the_four_arcs' "at quorum" needle + the concurrency census arc untouched.
- Step 13 tests/test_web_face.py: test_result_ranks_the_whole's loop posts each pair twice (the _VOTE form then {**_VOTE, "comparator_class": "llm"}) -> 6 posts; every assertion ("one", "three", "win-rate-v1", "<table") stands; the done-redirect/done-page/fragment arcs + test_result_safe_halt_409's needle untouched.
- Step 14 tests/test_mcp_server_face.py: _cast gains comparator_class (default "human", before supersedes; "comparator_class": comparator_class in the arguments; the docstring's class clause updated — the head grown to the six-argument form, the sentence's own count); test_tally_view_at_full_coverage's each pair cast twice (human then llm) -> body wins 4/2/0 losses 0/2/4, pairs_expected/at_quorum/done unchanged; test_the_sitting_end_to_end's corroborating cast _cast(caller, ["a","b"], "prefer-a", "x", "llm") after the first cast, census -> {total: 2, items {a: 2, b: 2}}, the tally asserts stand; test_re_tally_after_cure's cure cast grown its class byte (..., "y", "llm") — the halt's "(a, b) needs 1 more" + the cured body (wins 2/0) stand; every census/ack/idempotency/seed/cross-session/refusal arc untouched.
- Step 15 tests/test_harness.py: _LLM joins after _HUMAN; the ack constants _VOTE_FOUR/SIX_OUT grow; _TALLY_ABC grown (counts a 4/0/0, b 2/2/0, c 0/4/0; pairs 2 each; rank/coverage/version lines unchanged); _vote_argv gains comparator_class (default _HUMAN); _arc_argv_sequence -> 10 argvs (each pair human then llm); test_arc_ten_invocations_green (renamed) — 10 rc zeros, the per-step stdout asserts against _VOTE_ONE..SIX_OUT, tally == _TALLY_ABC; FORCED DELTA named: the replay's two rc lists grown 7->10 zeros — the fence's "ride UNCHANGED" read as the form (the grown sequence fails the 7-zero lists by construction; §3c's head: the counts' bytes grow); R1-R4 + the unknown-run/out-of-set arcs untouched.
- FINDING (ruling needed; the step-5 precedent; pyproject untouched — outside this dispatch's four files): the fence's _cast 6-parameter signature fires PLR0913 AND PLR0917 (6 > 5, no keyword-only marker; the arcs pass the class positionally per the fence's own call bytes). The ready cure: "tests/test_mcp_server_face.py" = ["PLR0913", "PLR0917"] (the votes.py/session.py/run_store.py/service_store.py ruled-signature precedent form). The zero-in-code-ignores law bars a noqa.
- THE NAMED CRASH SURFACED (the steps 8-11 finding; rides to the integration unit's fence, NEVER fixed here): the grown step-12 tally body and the step-13 result page both ride service.py :513-514's tally route — the Pair-keyed pair_class_counts rides asdict past the replace-strip (the unhashable-dict-keys class) -> the wire 500s -> both arcs fail at the floor-green until the integration unit's cure (the replace-strip's second field, service.py's tier, §4's "rides UNSERIALIZED" naming the shape). The MCP/CLI arcs name their fields — asdict-free, unaffected.
- OBSERVATIONS (fence-silent docstrings byte-verbatim, the steps 6-7 precedent): test_harness's "7 invocations" tokens (module :8, _arc_argv_sequence :82 "seven processes", the renamed test's :103) under-count the 10-invocation arc; service_acceptance's "vote x3"/"three votes 1..3" clauses under-count the 6-vote arc — the fence rules docstring edits nowhere in these two files (only the eight->eleven token swap, landed).
- Same-turn instrument cure: my _vote_argv hunk landed one typo (item_a: str_b) — the patch's own findings named it; the file re-read, one-line fix applied, the re-apply ZERO findings.
- Not done: the floor-green make + kensho's verification (the coordinator's instruments); no self-verification run.
## Reported by jikko — 2026-11-24T20:10:15Z

# Step 14b + 15 landed — the fold's three fixes + the floor (jikko, build/policy-layer)
(a1) tally.py :88 `pair_class_counts: Mapping[str, Mapping[str, int]]`; :566 re-keyed AT THE DATUM'S BIRTH (the fold's exact comprehension, service.py:516's form); signature :471 byte-standing; gate :529-533/renderers/accumulation untouched. service.py untouched.
(a2)+(a3) pyproject: "tests/test_mcp_server_face.py" = ["PLR0913","PLR0917"] placed after test_tally's entry + "tests/test_harness.py" grown to ["PLR0913","S603","S607"] at the existing :99 — both RULING comments per the fold's Rulings B/C (the prophylactic character named).
RULED CONSEQUENCES landed same-turn (Ruling A's own, each named): test_tally :402 the datum pin re-keyed {"a|b": …}; the two wire-body pins grown (test_service_face :137-146, test_service_acceptance :267-276 — the field rides asdict SERIALIZED, the arcs' expected dicts follow); sorted(COMPARATOR_CLASSES) at the init :212 — the frozenset's per-process iteration order vs the byte-replay's own bar ("no order-dependent byte escaping into a body"), the step-2 deviation precedent; zero counted-value change.
THE FLOOR (the three acts, verbatim): test — "14 failed, 254 passed in 16.47s" (268 collected: the spec's 268 estimate holds as the COLLECTION count); lint — "All checks passed!"; typecheck — "0 errors, 0 warnings, 0 informations".
THE 14 FAILURES — three pre-existing classes, NONE the fold's (the crash class CURED and green: the step-12 tally body, the step-13 result page, the datum pin, the byte-replay): (i) 10 = test_tally.py's STANDING arcs (step 5's named deviation — the §3b existing-arcs' class-mix growth never landed, never re-dispatched); (ii) 3 = the mcp halt arcs (the spec §4 R10's "needles hold" is FALSE on the wire — the grown found's uncorroborated section pushes the needles past the 300-char clip: halt_refusal_under_the_cap, halt_capped_render_wire, re_tally_after_cure); (iii) 1 = the matrix's k=1 leg (the R5 parity at pair_count=0 casts human-only — every k=1 cell halts, single-class by the fence's own derivation).
Findings ride to the fold; NOT fixed here (outside this step's fence). Nothing else touched.
## Reported by jikko — 2026-11-24T20:43:49Z

STEP 15b — the fold's three cures landed whole (tests/test_tally.py, tests/test_mcp_server_face.py, src/prioritree/acceptance.py + src/prioritree/budget_curve.py + tests/test_budget_curve.py); the floor-green re-run follows.
(a) RULING 1, the TEN standing arcs in tests/test_tally.py: every DONE-reaching fixture gained its llm twin per pair (same pair, same winner, class "llm") — _perfect_order_votes 12 votes; hand-computed wins/losses doubled plus the pair_class_counts datum (string keys per Ruling A); prefix arc the interleaved human-then-llm 6-vote script, each prefix's found grown to the rendered bytes, [:6] DONE; cycle + tie-break counts doubled with groups/cycle byte-unchanged; no-score ties doubled; supersession: correction + chain arms' counted-judgment llm twins with doubled asserts, the fork arm's VOTE-0005 recast comparator_class="llm" with asserts byte-identical, the quorum-2 halt arm keeping its own un-twinned 2-vote fixture ("1 of 2" unchanged); isolation arc's empty needle grown; seam arc's quorum-1 arm re-pinned to the corroboration halt (found "uncorroborated pairs: (a, b) missing llm", next the corroborating byte form), quorum-2 arm byte-unchanged.
(b) RULING 2, the halt arcs in tests/test_mcp_server_face.py: under-cap asserts "next_action: cast the missing votes: (a, b) needs" plus the visible "uncorroborated pairs: (a, b) missing llm" plus the clip's ellipsis; capped wire asserts "under-quorum pairs: 15" (the total's head); re-tally asserts "cast the missing votes: (a, b) needs" at the halt (the llm cure-cast + re-tally DONE asserts byte-unchanged); the docstrings grown honest naming the two-cap reality (the found's 10-cap, the wire's 300-clip) — the file-level (3) clause's now-false "(unclipped)" claim grown too; the payload arc byte-unchanged (its asserts hold unclipped).
(c) RULING 3, the parity: src/prioritree/acceptance.py's accept_run registers at quorum=max(quorum, len(HARNESS_JUDGE_CLASSES)) (the docstring's clause (4) grown honest); src/prioritree/budget_curve.py's size_run total_budget at the same max form with the docstrings' B-form clauses grown; tests/test_budget_curve.py's matrix budget assert grown to the max form plus the k=1 mechanical consequences (budget-law B = 190 * 2 = 380, budgets (19,)*20; mechanics budgets (3, 3, 3, 3), thresholds (1, 2, 3), four singleton groups at p=0).
DEVIATION REPORTED (resolved conservatively per the fold, the latest event): the dispatch named "tests/test_acceptance.py's matrix assert" — the matrix's budget asserts live in tests/test_budget_curve.py (the only matrix carrying the k=1 cells); tests/test_acceptance.py rides the default k=3 (max(3, 2) = 3) and stayed byte-unchanged per the fold's own cure.
THE FLOOR (verbatim): test all: "268 passed in 29.12s" | lint check: "All checks passed!" | typecheck: "0 errors, 0 warnings, 0 informations" — the exact count 268, zero new ignores, pyproject.toml untouched.
