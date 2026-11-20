# synthesize/acceptance-brief — THE ACCEPTANCE UNIT'S BUILD BRIEF (the exact-task spec)

**Status: PROPOSAL.** Togo proposes; the collaborator rules at G-ACCEPTANCE-BRIEF. Every [PROPOSED] element is an offered default with its one-line reason. The brief IS the spec (the exact-task law): once approved, jikko executes exactly, kensho re-runs independently.

## §0 GROUND — the rulings the brief cites

- **R13 whole**: the seed-deterministic simulation harness — items with a latent total order, votes sampled from noisy comparators at stated noise rates, Kendall-tau >= the ruled floor; seeds fixed for byte-reproducibility. THE OPENING NUMBERS: noise 10-20% / tau >= 0.8 at n = 10-30, revisitable at the acceptance brief; the defensible claim comparative-empirical (pairwise + tally beats absolute sizing at equal budget), never "the output order is correct."
- **The U6 row**: the act ("Accept the product at the ruled bar…"); the gate (seeds fixed, byte-reproducible, the threshold itself the collaborator's ruling banked at the brief — the one genuine assessment axis); the fence (any private surface: ONLY the U5 public API, the first consumer standing in for the wrappers).
- **The citation contract (U4/U5 → U6)**: TallyResult (ranked_groups — the tie-group form tau consumes), CoverageDatum, TallyRefusedError, TALLY_ALGORITHM; Session the only door — the five ops, never the stores; the wrapper contract frozen at U5's surface.
- **The legs + the convergence (amendment 25's join point)**: discover/acceptance and understand/acceptance, both read from disk. THE CONVERGENCE, named: (1) the per-pair binary flip model — one draw per judgment, u < p ⇒ the flipped verdict, else the true positional, ties never sampled; (2) the tau-b integer floor 25·(P−Q)² >= 16·(P+Q)·n₀ — exact, no floats; (3) the random.Random(seed) instance school — never the process-global module; (4) the clock-stamp honesty pin — full-log byte-identity impossible (recorded_at, registered_at), the equality surface field-selected; (5) the baseline-not-in-the-gate reading — the gate binds recovery; the comparative claim rides as R13's banked framing. No divergence survives; the one synthesis-surfaced addition (the P+Q definedness guard, §3) named as the brief's own per amendment 25's accepted-cost clause.
- **G-ACCEPTANCE's five conditions**: (1) the exact-task law; (2) the harness green — the ruled band, U5's public API ONLY, by-type catches; (3) the measure green — tau over the groups, the floor banked here; (4) the determinism green — same seed ⇒ same items, votes, tally, tau; (5) the floor + kensho's independent re-run.

## §1 THE MODULE — the layout ruling

**[PROPOSED]: src/prioritree/acceptance.py + tests/test_acceptance.py.** The family precedent; the route's ruled vocabulary.

**What U6 ships — the harness, the measure, the matrix constants, and NOTHING ELSE:** no new core surface (zero additions to the five landed modules — the fence: U5's public API the only door); no wrapper logic. **The first-to-import-random note:** acceptance.py is the tree's FIRST module to import random — the randomness is the simulation's own, seed-pinned, instance-local; the core's purity stands untouched.

**The public surface:** accept_run (function — one (item_count, noise_rate, seed) simulation through Session's five ops → the frozen AcceptanceRecord); accept_measure (function — (ranked_groups, latent_order) → (P, Q, T), the integer counts); AcceptanceRecord (frozen dataclass — the run's clock-free evidence whole: latent_order, verdicts, result (TallyResult), concordant, discordant, tied, + the run's own (item_count, noise_rate, seed)); the ACCEPTANCE_* constants (the matrix, the seeds, the rates, the floor — content-in-configuration). **The naming law:** the act "Accept the product at the ruled bar…" — accept_run, accept_measure; AcceptanceRecord the family's noun form.

## §2 THE HARNESS — the simulation's exact mechanics

1. **The RNG**: ONE random.Random(seed) instance per run — private state, stdlib-reproducible, never the process-global module. The chain's stochastic acts: the permutation draw (first) and the per-judgment vote draws (after) — the draw order pinned by construction.
2. **The seeded latent order**: n ids from the id template [PROPOSED: "item-{i:02d}" — zero-padded so lexicographic = numeric, making the decoupling checkable]; the truth = a seeded permutation drawn from the SAME instance as its first act [PROPOSED: one RNG for everything — the fewest moving parts]. **THE DECOUPLING IS LOAD-BEARING:** were the truth implicit in id sort, the tally's deterministic id tie-break would correlate with truth and inflate tau on every noise-induced score tie — the harness asserts the drawn permutation ≠ the id-sorted order [PROPOSED: the one-line honesty guard; a sorted-order draw revisits the seed at the gate]. The truth is harness-local data, NEVER registered — the manifest carries the items as opaque rows.
3. **The noisy comparator**: per judgment ONE draw u = rng.random(); u < p ⇒ the FLIPPED verdict, else the TRUE positional verdict — "prefer-a" if item_a precedes item_b in the latent order, else "prefer-b". NEVER a tie sampled — the declared set stays the full triple; the binary flip the minimal honest model (the three-way model the later widening path).
4. **The run through Session's five ops ONLY**: Session(Registry()) fresh per run → register_run(items, operator) at the default k=1 → the loop: next_pair(run_id) [the default seed resolution — the harness rides the public surface exactly as a wrapper would] → the draw → cast_vote → repeat → except ExhaustedQueue BY TYPE (never a bare except) → tally_rank → TallyResult; except TallyRefusedError BY TYPE as discipline — unreachable by construction in a healthy run (voting until DONE ⇒ every pair at quorum ⇒ all three coverage legs met), the catch the wrapper contract's standing proof. Ops composed: 1, 2, 3, 5 — op 4 the audit surface kensho's evidence leg cites; the fence is "the five ops ONLY" (no store access), not "all five."
5. **The comparator stamp**: two named constants [PROPOSED: comparator_id "acceptance-noisy-comparator", comparator_class "synthetic" — arbitrary-but-fixed bytes; the stamp is data (R5), zero tally effect].
6. **The verdict sequence**: the harness records (pair, winner) per cast, in queue order — harness-local data, the replay's equality surface.
## §3 THE MEASURE — tau-b over the ranked groups, exact

- **The input**: TallyResult.ranked_groups (the tie-group form tau consumes) + the harness's latent_order; the measure reads the groups alone, never scores.
- **The counts**: over the n₀ = n(n−1)/2 unordered pairs — same emission group ⇒ T (T = Σ|g|(|g|−1)/2); different groups ⇒ P if the latent-earlier item's group precedes, else Q. P+Q+T = n₀ (asserted as the measure's invariant); the truth strict — the standard tau-b with the truth untied: **tau = (P−Q)/√((P+Q)·n₀)**; within-group id order irrelevant (only co-membership and group order).
- **THE FLOOR AS THE INTEGER INEQUALITY**: tau ≥ 4/5 ⟺ **P ≥ Q AND 25·(P−Q)² ≥ 16·(P+Q)·n₀** — every term an integer, the radical never taken, no floats anywhere in the comparison (the Fraction precedent; the noise draw unavoidably float — the stochastic act; the MEASURE exact by construction). [PROPOSED: the definedness guard P+Q ≥ 1 joins the assertion — the guard is free honesty; the brief's own addition, surfaced at the join.]
- **The check derives from the floor constant**: ACCEPTANCE_FLOOR = Fraction(4, 5) — the exact data form of the banked 0.8 (no float); the check's integers derive mechanically, so a revisited floor is a one-constant change, never a code change.
- **THE FLOOR 0.8 = THE COLLABORATOR'S BANKED RULING** — the one genuine assessment axis: the threshold is ruled data, revisitable at any later brief; the module NAMES the threshold's assessment nature in its own docstring — the floor a banked ruling carried as a named exact constant, never a discovered fact; the machinery that measures it deterministic; a revisit changes one constant, never code.

## §4 THE MATRIX — the concrete cells, the seeds, the reproducibility pin

**The grid [PROPOSED: n ∈ {10, 20, 30} × p ∈ {0.10, 0.15, 0.20} — R13's ruled band exactly]: 9 cells, 27 runs.**

**The seeds [PROPOSED: three named seeds per cell — the lucky-seed objection priced]: ACCEPTANCE_SEEDS = (1109, 2213, 3371)** — one named constant tuple, the SAME three seeds across every cell. Each (n, p, seed) tuple is one full run: 6,030 in-band judgments (tool-verified).

**The degradation observation [PROPOSED: p = 0.30 at n = 20, the same three seeds — recorded, never floored]**: 570 more judgments; the observation makes the bar's meaning visible as data without widening the gate — the floor binds ONLY the ruled band. [PROPOSED: the tests assert the recorded degradation taus fall below the floor — the observation is evidence only if the drop is real, and the fixed seeds make it deterministic.]

**The perfect case [PROPOSED: p = 0 at n = 10, one seed — 45 judgments]: tau = 1 exactly.** Every vote true ⇒ every score distinct ⇒ the emission IS the latent order; P = n₀, Q = T = 0 — the one edge that proves the measure's polarity end-to-end.

**Total: 6,645 judgments — seconds-scale in-memory** (6,030 + 570 + 45, tool-verified).

**THE REPRODUCIBILITY PIN: the equality surface is FIELD-SELECTED, the clock-free whole** — across replays of the same (n, p, seed): the latent order, the verdict sequence ((pair, winner) in queue order), the TallyResult WHOLE (every field clock-free), and tau are IDENTICAL. **The clock stamps — VoteRecord.recorded_at, RunManifest.registered_at — are named and excluded by construction**: wall-clock provenance the tally never reads; full-log byte-identity is impossible and never claimed; the surface is named, never silently narrowed.

## §5 THE BUDGET QUESTION — the baseline ruled honestly

**THE BASELINE NOT IN THE GATE [PROPOSED: the claim-discipline default]**: none of G-ACCEPTANCE's five conditions names a baseline; the gate binds recovery. The harness measures the pairwise side's recovery at the ruled floor; R13's comparative-empirical claim rides as the BANKED FRAMING in the close's language, unmeasured by the minted gate. The deferral's price named honestly: the harness demonstrates recovery ≥ 0.8 at the stated noise; it does NOT empirically demonstrate "beats absolute sizing," though the product's purpose sentence rests on that comparison.

**THE IN-HARNESS BASELINE PRICED AS THE COLLABORATOR'S OPTION**: if ruled in at this gate, the mechanism is priced whole — each item sized by the same noisy comparator at the same p (the sizings repeated to equal budget — n₀ judgments total, matching the pairwise side's spend), the sizes sorted into the sizer's own ranking, tau computed identically, the two taus compared per cell. The earning condition: the baseline arm must itself ride the discipline — seeds fixed, runs deterministic, the per-cell comparison recorded as data. The price: the matrix doubles (~6,030 more judgments), the module grows a second harness arm, the close's claim graduates from language to measurement. The option is the collaborator's ruling at the gate; absent the ruling, the default stands as proposed.

## §6 THE TESTS + THE LAWS + THE GATE'S EVIDENCE

**The named edges (tests/test_acceptance.py):**

1. **test_recovery_at_floor_per_cell** — every in-band (n, p, seed) run asserts the INTEGER floor (P ≥ Q AND 25·(P−Q)² ≥ 16·(P+Q)·n₀); the per-cell taus recorded as the run's data.
2. **test_determinism_same_seed_identical_replay** — the same (n, p, seed) run twice (fresh Session/Registry per run): the clock-free surface identical — latent order, verdict sequence, TallyResult equal field-for-field, tau equal; the stamps named and excluded (never asserted equal).
3. **test_perfect_case_tau_one_exactly** — p = 0: P = n₀, Q = T = 0; the emission IS the latent order.
4. **test_degradation_observation_recorded_below_band** — the p = 0.30 runs recorded with their floor inequalities failing; the floor never binds them (the bar's meaning as data).
5. **test_done_caught_by_type** — the loop exits on ExhaustedQueue caught BY TYPE (never a bare except), tally_rank returns the whole; TallyRefusedError caught BY TYPE as discipline though the healthy run never raises it.

(The decoupling guard rides accept_run itself — every test exercises it; a sorted-order seed draw fails loudly at the run, never at the measure.)

**The floor:** pyright strict 0/0/0; ruff (select ALL, line-length 120, the named tests ruling S101/PLR2004) zero findings; ZERO ignores; zero runtime dependencies (random is stdlib — the named import). **Kensho's independent re-run:** the same suite, fresh process, kensho's own instruments — the fixed seeds replay the identical items, votes, tally, tau; the read-back is the evidence.

**The laws riding:** five-field docstrings (Provenance citing R13, the U6 row, G-ACCEPTANCE, both legs, this brief); the naming law (accept_run, accept_measure from the act's first word); zero runtime deps (the simulation's randomness stdlib, named in the module docstring as the simulation's own — the tree's first random import, never the core's); content-in-configuration (the cells, the seed list, the rates, the floor, the id template, the stamps — named constants); **the threshold's assessment nature NAMED in the module** — the floor the collaborator's banked ruling, revisitable; the machinery that measures it deterministic; the no-shell law; the exact-task law.

**The carriers table:**

| G-ACCEPTANCE condition | The spec's carrier |
|---|---|
| 1. The acceptance module lands per the brief | §1 the module + surface; §2 the harness mechanics; §3 the measure — signatures and constants pinned |
| 2. The harness green (the ruled band, U5's public API ONLY, by-type catches) | §2 items 1-7 the chain whole; §4 the cells + seeds; §6 test 5 |
| 3. The measure green (tau-b over the groups; the floor banked here) | §3 the integer inequality + the floor constant; §6 tests 1, 3, 4 |
| 4. The determinism green (same seed ⇒ same items, votes, tally, tau) | §4 the reproducibility pin; §6 test 2 |
| 5. Pyright 0/0/0 + ruff zero + kensho's independent re-run | §6 the floor + the independence leg |

**The trade-off the plan must carry:** the honesty pin narrows the claim — byte-reproducibility asserted ONLY over the field-selected clock-free surface, the strongest true claim, never the impossible one; the stamps are provenance, never content. The rest priced and named: the binary flip (minimal honesty; the three-way model the later widening path), the one-RNG chain (truth and votes coupled in draw order — the seed pins the whole chain as one artifact), the baseline deferral (recovery-only evidence; the comparative claim rides as language), the degradation at one n (the bar's meaning visible without widening the gate). The earned-later menu rides forward: test-retest, cross-class, order-swap, cycle rate, the budget curve — the baseline leg's first cousin.

**Open questions carried to the gate (each [PROPOSED]): the id template (§2), the one-RNG permutation (§2), the decoupling guard (§2), the default-seed resolution at next_pair (§2), the comparator stamps (§2), the P+Q guard (§3), the matrix cells + seed count (§4), the degradation cell and its below-floor assertion (§4), the perfect-case size (§4), the baseline option (§5).** Every one resolves the legs' [OPEN] items; the brief carries nothing unruled past the gate.

*Provenance: togo (統合, integrate), packet synthesize/acceptance, route prioritree-core, 2026-11-20 session. Read-only held — the content returned in-message (one transit truncation recovered by session resume); landed by shinko via patch under the landing discipline. The tree is the truth.*
7. **The runtime**: n₀ judgments per run (45/190/435); the whole matrix seconds-scale in-memory (§4: 6,645 judgments total).
