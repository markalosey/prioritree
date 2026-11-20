# synthesize/scheduler-brief — THE SCHEDULER UNIT'S BUILD BRIEF (the exact-task spec)

**Status: PROPOSAL.** Togo proposes; the collaborator rules at G-SCHEDULER-BRIEF. Every [PROPOSED] element is an offered default with its one-line reason — the legs' convergent proposals are the defaults. The brief IS the spec (the exact-task law): once approved, the bytes addendum follows (togo authors the fenced contents; jikko lands byte-exact per single-goal dispatches), then build/scheduler fires against G-SCHEDULER.

## §0 GROUND — the rulings cited (compact)

- **R7** (birth store): unordered-pairs-once — the schedule is the n(n−1)/2 unordered pairs; canonical id-sorted presentation; deterministic enumeration; default seed derived from run_id.
- **R8**: quorum keys the exhausted state — policy-as-data declared at registration (k=1 default, landed: RunManifest.quorum); the DONE signal's keying is ruled upstream of this brief.
- **The Parnas fence** (U2's must-not-know): vote values, comparators, the operator's meaning; the hidden scheduler seam — "increment 1 ships complete round-robin; adaptive selection is a later earned upgrade behind this seam" (R6: the seam absorbs growth without changing shape).
- **The op-2 spec verbatim** (the five-op interface): next_pair(run_id, seed?) → (item_a, item_b, pair_vote_count); "Pure; default seed derived from run_id → replays byte-match. Refusals: unknown run; the exhausted state → the DONE signal" — the count tension §1's seam ruling resolves.
- **The composition model**: U1 → {U2, U3} → U4 → U5 → U6 — U2 and U3 are PARALLEL SIBLINGS (no unit imports another's internals), and the build order is scheduler 2nd, votes 3rd — the vote ledger does not exist when U2 lands.
- **The legs riding this brief:** discover/scheduler (tansa's census — the ruled ground, the gaps (a)–(h), the citation contract) + understand/scheduler (rikai's mechanism — the enumeration chain, the op-2 tension priced, the edges, the test edges). Every [OPEN] item resolves below.

## §1 THE MODULE — the layout and seam rulings

**[PROPOSED]: single module `src/prioritree/scheduler.py`; tests at `tests/test_scheduler.py`.** Reason: the route's ruled vocabulary names it (build/scheduler, G-SCHEDULER) and the U1 precedent sets the flat-module form; measured at discovery, both unborn.

**THE SEAM RULING — seam (b)** [PROPOSED — both legs converge]: **the pure full enumeration at U2; the count consult and the DONE signal compose at U5 (the session tier).** U2 ships ONE total function — ids (+ the reserved seed) in → the complete canonical queue out — plus the pair type and the seed derivation. `pair_vote_count` and the exhausted state are NOT U2's return or refusal at all: the count consult's ruled home is U3's read_vote_state; U5 — whose act is "Session the chain into the library's public face: register → schedule → vote → tally composable at any coverage point" — composes queue × counts × quorum to serve the five-op next_pair and detect exhaustion. Reasons (one line): the gate's five conditions test ONLY the pure enumeration; the dependency graph's letter places the composition edge at U5; the count consult's duplication is avoided; the Parnas fence then holds absolutely — **U2 knows nothing of votes, NOT EVEN COUNTS**.

**What U2 does NOT ship (named as U5's composition):** `next_pair` (the five-op surface — the public face owns the name); the DONE signal (the exhausted state is the loop's terminal — **[PROPOSED]: it mints at U5 whole**, type and raise site with the loop, keeping U2's surface to pair-type + enumeration + seed derivation); any count consult. The signal's concrete carrier is U5's brief's own pin (recorded proposal: a dedicated signal class distinct from the refusal lineage, carrying expected/found/next-action — semantically a terminal state, distinguishable from error by type).

**The registry-import split [PROPOSED]: pure-ids — the module imports nothing.** Reason: the U2 row's act runs "given only the item-id set"; the run_id → id-set resolution (read_manifest) is U5's composition — the module stays vote-ignorant and registry-unimported, the siblings law holding by construction.

**The public surface (the frozen list — the citation contract):**

| Symbol | Kind | Consumers |
|---|---|---|
| `Pair` | frozen dataclass | U3 (vote records, ground-truth checks), U5 |
| `schedule_pairs` | the enumeration | U3 (the legal pair set), U4 (the coverage gate's expected side), U5 |
| `derive_seed` | the seed derivation | U5 (op 2's default) |
| `SEED_ALGORITHM` / `SEED_BYTES` | named constants | the derivation's data |

U3 and U4 cite `Pair` + the pair-set derivation over ids — `schedule_pairs` is the unordered-pair set's ONE source of truth (U3's unknown-pair and winner-not-in-pair refusals check against it; U4's coverage gate cites the same expected set, never re-derived — FR-MEM-0001's lesson); NEITHER imports the queue's order. Everything else is internal.

## §2 THE SCHEMAS — field-level

**`Pair`** — the frozen dataclass, the canonical form every vote cites [PROPOSED: the registry's school verbatim — the ItemRow precedent; typed, named, hashable (load-bearing for U3's dedup and the counts-map keys), five-field-docstringed, importable as the seam — a nameless tuple cannot serve as "the form every vote cites"]:

- `item_a: str` — the lexicographically smaller id; `item_b: str` — the larger.
- **Canonical invariant: item_a < item_b strict** (ids distinct per the U1 precondition ⇒ no equal pair). Minted canonical BY CONSTRUCTION in schedule_pairs (sort-first); documented in the docstring; no constructor validation — the registry school keeps value types bare, the minting op owns correctness (U3's ground-truth check refuses non-canonical citations against the legal set).

**The queue's return type** — `tuple[Pair, ...]` [PROPOSED: the immutable whole-queue value — the total-function form; the family's frozen-value discipline (a mutable list as a pure function's return is surface no one asked for)].

**The seed parameter** — `int | None`, default `None`, on schedule_pairs [PROPOSED: the reserved seam parameter — op 2's own "seed?" optional form; an int is the future mode's reproducible permutation key, unused by the ruled order, carried now so the hidden seam's widening is additive, never rework — the fence doctrine].

**The derivation's named constants** [PROPOSED — content-in-configuration]: `SEED_ALGORITHM = "blake2b"`, `SEED_BYTES = 8` — the digest algorithm and byte-width as module-level data, never magic literals.

## §3 THE ENUMERATION — schedule_pairs' exact signature and semantics

```python
def schedule_pairs(ids: Iterable[str], seed: int | None = None) -> tuple[Pair, ...]
```

**The order [PROPOSED — resolving the enumeration-order gap]: sorted combinations** — id-sorted outer, id-sorted inner; the natural reading of R7's three-part phrase (unordered-pairs-once, canonical id-sorted, deterministic enumeration); the seed carried as the reserved seam parameter, dead at birth, additive later.

**The algorithm (the enumeration chain):**
1. **Sort the ids lexicographically** — Python codepoint order on the exact strings, no locale, no case-folding (the family's exact-string discipline). The sort is total (ids distinct — no tie-break exists to invent) and **the sort IS the stability mechanism**: enumeration as a pure function of the SET forces sort-first; an unsorted iteration would be process-order-unstable.
2. **Enumerate the i<j pairs in lexicographic order** — the double loop over the sorted list: for every position i, for every j>i, emit `Pair(sorted[i], sorted[j])`. Each pair id-sorted within by construction.
3. **Return the complete queue** — the flat deterministic tuple; the tournament COVERAGE property (each meets each once) realized as the whole-queue value, not a stateful rounds schedule.

**The count law:** n(n−1)/2 — 10 items → 45; 100 → 4,950 (re-verified at composition: 10×9=90→45; 100×99=9,900→4,950; the degree identity 2·pairs = n(n−1): 90=90, 9,900=9,900). Total for any n (R6): 1,000 → 499,500 is legal output beyond the verified bar.

**NO duplicate check** [PROPOSED — both legs derive it]: the uniqueness invariant rides U1's upstream refusal (_check_duplicates refuses before any byte lands; the manifest is frozen) — cited as a CONTRACT PRECONDITION in the docstring, never re-policed as dead runtime weight. The <2 cardinality refusal is likewise U1's, landed at registration (_check_cardinality, naming 0 and 1 distinctly) — the scheduler itself stays TOTAL; it refuses nothing.

**The empty/1-item edges → the empty queue** — `schedule_pairs([])` → `()`; one id → `()`. Legal VALUES, not refusals (the total-function form; the count law agrees: 0 pairs). The ruled flow never hands the scheduler fewer than two; the edges are still defined because "the core stays TOTAL — every function correct for any n, no artificial caps" (R6).

**The seed derivation** [PROPOSED — both legs converge: the stable digest]:

```python
def derive_seed(run_id: str) -> int
```

`int.from_bytes(hashlib.new(SEED_ALGORITHM, run_id.encode("utf-8")).digest()[:SEED_BYTES], "big")` — blake2b over the run_id's UTF-8 bytes, the first 8 bytes big-endian. Reason (one line): stdlib (zero-deps legal) and stable bytes→integer across processes — **the PYTHONHASHSEED trap named and foreclosed**: Python's builtin `hash()` is process-salted for strings and would break byte-stable replays; a content digest cannot drift. Properties ruled now: same run_id → same seed, stable across calls and processes. The seed is NOT for the ruled order — nothing stochastic remains at birth; it is the reserved parameter of the hidden scheduler seam (a future mode needs a reproducible permutation: seed in, same permutation out), and U5 composes `derive_seed(run_id)` when the five-op surface needs op 2's default.

**Determinism (the gate's condition 4):** same id-set → byte-identical queue; **set-keyed stability** — payload order is irrelevant (sort-first); replays byte-match across processes (no time, no randomness, no environment reads; no set iteration anywhere).

## §4 THE TESTS — the thirteen named edges (tests/test_scheduler.py)

Property tests as the gate names them — one test per named edge, each name from its edge (the naming law); direct asserts over the return shape (the registry precedent's landed form):

1. **`test_exact_count_10_items_45_pairs`** — 10 distinct ids → exactly 45 pairs (the gate's own figure).
2. **`test_exact_count_100_items_4950_pairs`** — 100 distinct ids → exactly 4,950 (the gate's own figure).
3. **`test_zero_duplicates`** — `len(set(queue)) == len(queue)`; the set idiom rides Pair's hashability directly.
4. **`test_zero_missing_full_coverage`** — set-equality against an independently authored brute-force double loop — the oracle is NOT the implementation's idiom (identity proves nothing).
5. **`test_degree_law_each_id_in_n_minus_1_pairs`** — each id appears in exactly n−1 pairs; the degree sum n(n−1) = 2·pair count localizes any missing pair.
6. **`test_replays_byte_identical`** — two calls on the same ids → equal queues.
7. **`test_seed_derivation_stable`** — same run_id → the same derived seed across calls (the PYTHONHASHSEED trap named in the docstring — the blake2b digest forecloses it).
8. **`test_set_keyed_stability`** — the same id-set in different payload orders → the SAME queue (the direct test of sort-first).
9. **`test_canonical_form_id_sorted`** — every pair satisfies `item_a < item_b` strict.
10. **`test_minimum_two_ids_one_pair`** — the ruled flow's minimum: 2 distinct ids → exactly one canonical pair.
11. **`test_empty_ids_yield_empty_queue`** — `schedule_pairs([])` → `()` (the count law's 0).
12. **`test_single_id_yields_empty_queue`** — one id → `()`.
13. **`test_reserved_seed_parameter_unused_by_ruled_order`** — an explicit seed changes nothing under the ruled order: `schedule_pairs(ids, seed=x) == schedule_pairs(ids)` — the reservation documented by a property, not a promise.

**The DONE path is ABSENT at U2** — no DONE test exists in G-SCHEDULER's conditions (a fact, matching the gate); the signal's test rides U5's gate as the loop composition (queue × counts ≥ quorum → the exhausted signal).

**The floor:** pyright strict 0 errors 0 warnings 0 informations; ruff (select ALL, line-length 120) zero findings; zero ignores anywhere (an ignore is a ruling, never a convenience); the tests' one named exemption class per the registry precedent (S101 + PLR2004 in tests — the birth store's named pyproject ruling, never an inline ignore). **Kensho's independent re-run:** the same suite, fresh process, kensho's own instruments — the read-back is the evidence, not the build's word. The floor-green step rides the build increment: `make dev && make test && make lint && make typecheck`.

## §5 THE LAWS RIDING THE MODULE

- **Five-field docstrings** (Purpose / Refuses when / Re-run / Touches / Provenance) on EVERY public symbol — Pair, schedule_pairs, derive_seed, SEED_ALGORITHM, SEED_BYTES — Provenance citing R7, the op-2 spec, G-SCHEDULER's conditions, the two legs.
- **The naming law at the symbol level:** `schedule_pairs` from "Schedule the full pairwise coverage queue" (the U2 row's own act); `derive_seed` from "default seed derived from run_id" (op 2's own words); `Pair` — the canonical form's name, the seam every vote cites.
- **Zero runtime dependencies:** hashlib is stdlib — legal; pyproject dependencies = [] stands.
- **Zero magic values:** the digest algorithm and byte-width are named constants (content-in-configuration); the PLR2004 cure in tests rides the named tests ruling.
- **No content interpretation:** ids are opaque structure — the sort is codepoint order on exact strings; no label, no vote value, no comparator ever enters the module.
- **The no-shell law:** zero subprocess (pure logic).
- **The exact-task law:** this brief is the spec; once the collaborator approves at G-SCHEDULER-BRIEF, the bytes addendum follows (togo authors the exact file contents as fenced blocks — amendment 14's doctrine; single-goal dispatches — amendment 15), jikko lands byte-exact, kensho re-runs independently; G-SCHEDULER closes on the evidence.

## §6 THE GATE'S EVIDENCE — G-SCHEDULER's five conditions mapped to this spec

| G-SCHEDULER condition | The spec's carrier |
|---|---|
| 1. The scheduler module lands per its approved brief — the exact-task law, jikko byte-exact, nothing to figure out | §1 the module + seam ruling, §2 the schemas, §3 the enumeration — signatures, field names, the derivation formula, test names pinned; the bytes addendum lands the exact contents |
| 2. Property tests green: the exact pair count (10→45, 100→4,950), zero duplicates, zero missing — full coverage (R7) | §4 tests 1–5 — the two count figures, the set idiom, the brute-force oracle, the degree law |
| 3. The canonical pair form: every pair id-sorted — the form every vote cites (the seam pinned at this unit's brief) | §2 Pair (item_a < item_b strict, minted by construction) + §4 test 9 — the seam U3's brief cites |
| 4. Order-stable: the same id-set (and the ruled seed derivation) → the byte-identical enumeration; the empty/1-item edges → the empty queue | §3's determinism clause + §4 tests 6, 7, 8 (replays, the derivation's stability, set-keyed stability) and tests 11, 12 (the edges) |
| 5. Pyright 0/0/0 + ruff zero findings, zero ignores; kensho's independent re-run green | §4 the floor + §5's zero-ignore law — the read-back as evidence, not the build's word |

**The trade-off the plan must carry (seam (b)'s price, named):** op 2's five-op letter becomes U5's composition — this brief specs the enumeration and mints the seam, not the whole op-2 surface; a per-call next-with-progress costs a queue re-derivation per call (pure, O(n²) — 4,950 pairs at the verified fence, trivial); and the seed rides as a reserved parameter dead at birth — carried so the seam's widening is additive, never rework.

**Open questions carried to the gate (each [PROPOSED] above):** the seam ruling (§1), the DONE mint site — U5 whole (§1), the module layout + registry-import split (§1), the frozen Pair + its bare constructor (§2), the queue's tuple return (§2), the seed's reserved-parameter form (§2), the digest derivation + its constants (§2, §3), the enumeration order (§3 — sorted combinations), the test list (§4). Every one resolves discover's gaps (a)–(h) and understand's five [OPEN] items; the brief carries nothing unruled past the gate.

*Provenance: togo (統合, integrate), packet synthesize/scheduler, route prioritree-core, 2026-11-20. Read-only held — the content returned in-message at execution; landed by shinko via patch under the landing discipline. Every figure re-verified at composition (calculate: 90→45, 9,900→4,950; the degree sums 90=2×45, 9,900=2×4,950); the tree is the truth.*
