# understand/scheduler — the scheduler unit's mechanism analysis

**Seat:** rikai (理解) · **Packet:** understand/scheduler · **Route:** prioritree-core (U2) · **Date:** 2026-11-20. **Landing:** returned in-message at execution (the pack is read-only); landed by shinko via patch, verbatim; read-back verified.

**Ground read whole:** the core store's junro.json (G-SCHEDULER's five conditions), the birth store's junro.json (R7/R8/R12 ruled; the five-op interface), scope-synthesis.md (PART 2's U2 row, PART 3 §3.2 op 2 verbatim), registry.py (the frozen vocabulary U2 cites), friction_ledger.py (the family school). **Fail-fast check: no ground missing.** Tool-verified arithmetic rides the calculate runs.

**Absences stated as facts:** src/prioritree/scheduler.py does not exist; tests/test_scheduler.py does not exist; discover/scheduler.md landed in parallel (this packet rode the census leg's twin). G-SCHEDULER-BRIEF needs both.

## 1. THE ENUMERATION CHAIN — id-set in → canonical unordered pair list out

**Input** [STATED]: "given only the item-id set" (the U2 row). The ids arrive from the frozen manifest: Registry.read_manifest returns RunManifest.items, each ItemRow.id a non-empty stripped string.

**The algorithm** [DERIVED from R7 + the gate's own words]:
1. **Sort the ids lexicographically** — Python codepoint order on the exact stripped strings, no locale, no case-folding (the family's exact-string discipline). The sort is total: ids are distinct (the registry refuses duplicates before any byte lands), so no tie-break exists to invent. **The sort is the stability mechanism**: the gate keys stability off "the same id-set" — enumeration as a pure function of the SET (not the payload order; the manifest preserves payload order) forces sort-first; an unsorted-set iteration would be process-order-unstable.
2. **Enumerate the i<j pairs** — the double loop over the sorted list: for every position i, for every position j>i, emit (sorted[i], sorted[j]). Each pair is id-sorted within by construction.

**Determinism** [DERIVED]: every step is pure over the id-set — no time, no randomness, no environment reads. Same id-set → byte-identical queue. "Increment 1 ships complete round-robin" reads as the tournament COVERAGE property (each meets each once), realized as the flat deterministic queue — not a stateful rounds schedule [DERIVED].

**The count law** [DERIVED, tool-verified]: n(n−1)/2. Runs: 10×9=90→45; 100×99=9,900→4,950; 1,000×999=999,000→499,500; 2×1=2→1; 0→0. Matches the stated figures and the gate bar verbatim.

## 2. THE CANONICAL PAIR FORM — the frozen seam every vote cites

[STATED] R7: "canonical id-sorted presentation". [STATED] the seam's weight: "every pair canonically id-sorted — the form every vote cites… votes' records and U3's ground-truth checks ride it"; "scheduler's canonical pair form is the seam votes' brief cites" (amendment 22's schema-citation ordering — shinko's note: the sequencing record).

**The type** [DERIVED]: a frozen two-string value, (a, b) with a < b strict (uniqueness ⇒ no equal pair). Either tuple[str, str] or a @dataclass(frozen=True) — both hashable; the family's value-type precedent is ItemRow. **Hashability is load-bearing**: U3's dedup keys and the counts-map key off this form — a frozen dataclass gets __hash__ by construction; a tuple natively [DERIVED]. **Equality semantics**: exact string equality — two votes cite the same pair iff their canonical forms are equal, so the canonical form IS the pair's identity; the (a,b)/(b,a) ambiguity is killed by construction [DERIVED]. **Positional semantics** [DERIVED]: the verdict vocabulary {prefer-a, prefer-b, tie} (WEAK_ORDER_TRIPLE) is positional over the form — "a" means the lexicographically smaller id. This is WHY the seam pins at U2's brief, before votes exist.

## 3. THE OP-2 TENSION — next_pair's count consult vs the Parnas fence

**The tension, stated honestly** [STATED]: op 2's spec — next_pair(run_id, seed?) → (item_a, item_b, pair_vote_count); "Pure; default seed derived from run_id → replays byte-match. Refusals: unknown run; the exhausted state → the DONE signal". The fence: U2 "must NOT know: vote values, comparators, the operator's meaning". Three facts collide [DERIVED]: (i) pair_vote_count is a consult over the vote ledger — U3's store; (ii) the dependency graph makes U2 and U3 PARALLEL SIBLINGS — "no unit imports another's internals"; (iii) the build order is scheduler 2nd, votes 3rd — the ledger does not exist when U2 lands.

**Seam (a) — COUNTS AS DATA (store-as-parameter):** the scheduler takes a counts-map parameter (key: the canonical pair form; value: int), filters the queue for the next under-quorum pair, returns it with its count; DONE = no under-quorum pair remains (keyed off manifest.quorum). No U3 import — the map is data, the shape pinned at U2's brief. Price: the signature widens with a parameter the enumeration itself never needs; the "at-quorum?" predicate then lives in TWO consumers (U2's filter, U5's loop) — two sites to keep honest; the gate's own words ("the total-function form") go untested, since the tested surface becomes the consult-bearing filter.

**Seam (b) — PURE FULL ENUMERATION at U2; count-consult + DONE at the session tier:** U2 ships one total function — ids (+seed) in → the complete canonical queue out — plus the pair type. pair_vote_count and the exhausted state are NOT U2's return or refusal at all: the per-pair count consult already has a ruled home — read_vote_state returns "per-pair counts"; U5 (whose ruled act is "Session the chain into the library's public face — register → schedule → vote → tally composable at any coverage point") composes U2's queue × U3's counts × U1's quorum to serve the five-op next_pair and detect exhaustion. Price: op 2's five-op letter becomes U5's composition (the public face owns the name) — U2's brief specs the enumeration and mints the seam, not the whole op-2 surface; a per-call next-with-progress costs a queue re-derivation per call (pure, O(n²) — 4,950 pairs at the verified fence, trivial).

**PROPOSED: seam (b).** The load-bearing evidence: the gate's five conditions test ONLY the pure enumeration (count, dup/missing coverage, canonical form, order-stability, empty-queue edges) — no condition tests a count consult or an exhausted refusal; condition 4's own phrase is "the total-function form"; the dependency graph's letter places the composition edge at U5; and the count consult's duplication is avoided (read_vote_state already carries per-pair counts). The Parnas fence then holds absolutely — U2 knows nothing of votes, NOT EVEN COUNTS.

## 4. THE DONE SIGNAL — the exhausted state

[STATED] the exhausted state is "the DONE signal, named, distinct from error" and KEYED OFF QUORUM (R8: "the exhausted state and the coverage gate both key off it"). [DERIVED] there are two distinct quorum keyings: the LOOP'S exhausted state (the GROWING phase's terminal — "looping while under-quorum pairs remain") and the TALLY'S coverage gate (the PURE phase's emission refusal, R12). The scheduler's DONE is the first; the tally's safe halt is the second.

**Mechanism** [DERIVED → PROPOSED]: a named typed signal DISTINCT FROM the refusal family — not a sentinel value. A sentinel (None/empty) is priced out twice: the family's law "an empty result is distinguishable from an error by construction" and the standing law "silence is not"; a sentinel also cannot carry the evidence. The proposed form: a dedicated exception class OF ITS OWN TYPE (not the RegistryRefusedError/refusal lineage) so callers distinguish DONE from error BY TYPE, carrying the exhausted state's evidence in the family's three-field grammar — expected (the queue's full pair count), found (every pair at quorum k), next-action (the tally path — R12's DONE). Mechanically an exception, semantically a terminal state: the spec's "named, distinct from error" is satisfied in the type system [DERIVED].

**Where it lives under seam (b)** [DERIVED]: the raise site is U5'S LOOP (queue × counts × quorum → no under-quorum pair remains); U2's pure enumeration never signals DONE — it is total, always returning the whole queue. [OPEN] whether the signal's TYPE mints in U2's module (the spec-letter option: op 2's refusal set is the scheduler's) or in U5 (the strict seam-(b) option: the loop's terminal state, minted with the loop) — the brief/collaborator pins it; my proposal: U5 whole, keeping U2's surface to pair-type + enumeration + count law.

## 5. THE SEED — derived honestly

[STATED] R7: "deterministic enumeration, default seed derived from run_id"; op 2: "default seed derived from run_id → replays byte-match"; the ruled split names pair selection "deterministic (vote state + explicit seed)".

**The honest derivation** [DERIVED]: under R7's ruled form the enumeration is ALREADY fully deterministic — the canonical order is fixed by the sort; NOTHING STOCHASTIC REMAINS for the seed to do at birth. The seed is not for the ruled order; it is THE RESERVED PARAMETER OF THE HIDDEN SCHEDULER SEAM — "the scheduling policy hides here (increment 1 ships complete round-robin; adaptive selection is a later earned upgrade behind this seam)"; "adaptive scheduling is deferred behind the scheduler seam" (R6); "the hidden scheduler seam absorbs growth without changing shape". A future mode (presentation shuffle for the priced order-bias deferral, R7's named trade-off; or adaptive selection) needs a reproducible permutation — seed in, same permutation out. The signature carries seed NOW so the widening is additive, never rework (the fence doctrine).

**The derivation form** [DERIVED]: a STABLE function of run_id — the trap to name: Python's builtin hash() is process-randomized for strings (PYTHONHASHSEED) and would break byte-stable replays across processes; the derivation must be a content digest. [PROPOSED] a stdlib digest of the run_id's UTF-8 bytes (zero-dep — hashlib; e.g. int.from_bytes(blake2b(run_id.encode("utf-8")).digest()[:8], "big")), the algorithm a named constant frozen at the brief (content-in-configuration). [OPEN]: the exact algorithm is the brief's/collaborator's pin; the PROPERTIES are ruled now — same run_id → same seed, stable across processes (G-SCHEDULER condition 4 tests "the ruled seed derivation").

## 6. THE EDGES — the total function's bounds

- **Empty / 1-item → the empty queue** [STATED]: a legal VALUE, not a refusal — the total-function form; the count law agrees (0 pairs, tool-verified). The registry's <2 refusal (found names 0 and 1 distinctly) means "the ruled flow never hands the scheduler fewer than two" [STATED] — the empty-queue edges are unreachable via the ruled flow yet still defined, because "the core stays TOTAL — every function correct for any n, no artificial caps" (R6).
- **Duplicate ids impossible via the ruled flow** [DERIVED, named]: _check_duplicates refuses them BEFORE any byte lands, and the manifest is frozen. Therefore U2 needs NO duplicate check — the uniqueness invariant rides U1's upstream refusal, cited as a contract precondition (the schema-citation discipline), not re-policed as dead runtime weight. Named per the op-set idiom: the hazard is foreclosed by construction upstream, not refused downstream.
- **Beyond the fence** [STATED]: total for any n (R6), verified workload n ≤ 100 at full coverage — 4,950 pairs; 1,000 → 499,500 (tool-verified) is legal output beyond the verified bar.

## 7. THE TEST EDGES — the property set G-SCHEDULER will check

[STATED] the gate's bar + the floor (pyright 0/0, ruff zero, zero ignores; kensho's independent re-run). The landed test form is the precedent: one test per named edge, docstring naming the edge, direct asserts over the return shape. [DERIVED] the set:

1. **Count law**: 10 ids → exactly 45; 100 → exactly 4,950 (tool-verified; the gate's own figures).
2. **Zero duplicates**: len(set(queue)) == len(queue) — rides the canonical form's hashability directly.
3. **Zero missing**: full coverage of the unordered pair set (R7) — the honest oracle is NOT the same idiom the implementation uses (that proves identity, not the property); the independent detectors [DERIVED]: the set-equality against a brute-force double loop, and the DEGREE LAW — each id appears in exactly n−1 pairs (sum of degrees = n(n−1) = 2·pair count), which localizes any missing pair.
4. **Byte-stable replays**: same id-set → equal queues across two calls (and across processes — the PYTHONHASHSEED trap); the seed derivation stable: same run_id → same derived seed.
5. **Set-keyed stability** [DERIVED, the strongest reading of the gate's words]: the same id-SET in different payload orders → the SAME queue — the direct test of sort-first.
6. **Canonical form**: every pair (a, b) satisfies a < b strict.
7. **The edges**: [] → []; one id → [] — the empty queue as value.
8. **The DONE path under seam (b)**: ABSENT at U2 — no DONE test exists in G-SCHEDULER's conditions (a fact, matching the gate); the signal's test rides U5's gate as the loop composition (queue × counts ≥ quorum → the exhausted signal).

## Constraints the brief inherits (named, not derived)

- The naming law: every new symbol's name is the first word of its act-statement (the scaffold's standing law; registry.py's symbols follow it).
- Five-field docstrings (Purpose/Refuses when/Re-run/Touches/Provenance) on every new symbol — the landed form is the precedent.
- Zero magic values (the named-constant precedent, the PLR2004 cure, amendment 16). Zero runtime deps, no subprocess.
- The floor: make dev && make test && make lint && make typecheck (the build-add's floor-green step).

## [OPEN] for the brief / G-SCHEDULER-BRIEF to pin

1. **The seed-derivation algorithm** (properties ruled; the digest choice is a [PROPOSED] default above).
2. **The pair form's concrete type** — tuple[str, str] vs frozen dataclass (hashability is the load-bearing either way) [PROPOSED: the frozen dataclass, the ItemRow precedent].
3. **The DONE signal's mint site** — U5 whole (my proposal) vs type-at-U2/raise-at-U5 (the spec-letter option).
4. **The queue's return type** (tuple vs list) and whether the enumeration function also carries the manifest-read convenience or stays ids-only (my derivation: ids-only; the run_id resolution is U5's composition — "given only the item-id set").
5. **Candidate names** [PROPOSED, the naming law's application]: Pair (the canonical form), schedule_pairs (the enumeration — act-statement "Schedule the full pairwise coverage queue…").

*Provenance: rikai (理解), packet understand/scheduler, route prioritree-core, 2026-11-20. Read-only held — no file written at execution; landed by shinko via patch (the landing discipline). Every figure tool-verified at execution (calculate: 90→45, 9,900→4,950, 999,000→499,500, 2→1, 0→0); the tree is the truth.*
