# synthesize/budget-curve-brief — THE BUDGET-CURVE UNIT'S BUILD BRIEF (the exact-task spec)

**Status: PROPOSAL.** Togo proposes; the collaborator rules at G-BUDGET-CURVE-BRIEF. Every [PROPOSED] element is an offered default with its one-line reason. The brief IS the spec (the exact-task law): once approved, jikko executes exactly, kensho re-runs independently.

## §0 THE GROUND

- The legs: tansa's census (the amendment's site, accept_measure's contract, the ten gaps) and rikai's analysis (the sizer's chain stepped with the walked budget table, the pairing question priced with the recommendation, the equal-budget law proven, the blast radius minimal). The rulings: the seven composition questions ruled 2026-11-21; G-BUDGET-CURVE's five conditions verbatim at the store's junro. No divergence survives the join; the one live question — the noise-streams ruling — resolved per the accepted-cost clause with rikai's recommendation as the [PROPOSED] default, the alternative priced.

## §1 THE MODULE + SURFACE

- src/prioritree/budget_curve.py + tests/test_budget_curve.py (Q-curve-name).
- size_run(item_count: int, noise_rate: float, seed: int, quorum: int) -> SizerRecord — the act "Size the run's items at equal budget."
- compare_run(item_count: int, noise_rate: float, seed: int, quorum: int) -> CurveRecord — the act "Compare the two arms at equal budget"; one call, both arms.
- SizerRecord (frozen, clock-free), fields PINNED: item_count, noise_rate, seed, quorum (the coordinates); latent_order: tuple[str, ...]; the per-item judgments [PROPOSED: judgment_counts: tuple[int, ...] (the yes-count per item) + budgets: tuple[int, ...] (the B_i allocation) — the minimal replay-equality surface; the (threshold, answer) pairs rejected: 48k tuples of detail the replay never reads, the replay fully determined by (seed, quorum, B_i) by construction]; scores: tuple[Fraction, ...] (exact); ranked_groups: tuple[tuple[str, ...], ...]; concordant, discordant, tied: int (the (P, Q, T)).
- compare_run's return [PROPOSED: a frozen CurveRecord — fields acceptance: AcceptanceRecord, sizer: SizerRecord — over the tuple: the naming law would otherwise be unanswered by an anonymous pair, and a frozen record carries the replay-equality surface mechanically].

## §2 THE SIZER'S MECHANICS (the binary-threshold model whole)

- The latent: rng = random.Random(seed), ids from ACCEPTANCE_ID_TEMPLATE, latent = tuple(rng.sample(list(ids), item_count)) as the instance's FIRST act — the honesty guard rides (the same idiom as accept_run).
- THE NOISE-STREAMS RULING [PROPOSED: the derived instance random.Random(f"{seed}-sizer") for the sizer's flip draws — the truth paired (both arms' latents byte-identical per seed), the noise independent; §5's "the same noisy comparator at the same p" names the noise MODEL, not the realization, and the paired-cell design needs only the truth paired. ALTERNATIVE priced: identical streams (maximal coupling) — variance-free and luck-correlated, it would make the comparison conditional on one noise realization and arguably understate the sizer's independent error structure].
- The thresholds: j in {1..n-1}, integer midpoints, zero floats; the true answer deterministic: position(i) > j => yes.
- The noise: ONE draw per judgment, u < p => the FLIPPED answer (the acceptance flip grammar verbatim in form).
- The threshold schedule's domain [PROPOSED: the PER-ITEM counter — judgment m (1-indexed per item) uses threshold ((m-1) mod (n-1)) + 1; each item exhausts its own B_i budget against its own cycling stream, the exhaustive-coverage analog].
- The budget split PINNED: B = n0 x quorum (n0 = n(n-1)/2); q = B // n, r = B mod n; the first r items in id order get q+1, the rest q. r = n/2 at every ruled cell (n all even); the odd-n integral edge named: at odd n and k=1 the split is integral (n=11: 55/11 = 5, r=0) — ruled n never hits it.
- The score: Fraction(yes_count, B_i) per item — never a float.
- The emission: score-descending; equal Fractions tied in one group; within-group by id — the tally's deterministic mirror; every id exactly once; group order carries the ranking's direction (accept_measure's contract).

## §3 COMPARE_RUN — one call, both arms

- The pairwise arm: accept_run(item_count, noise_rate, seed, quorum) — FRESH, the amended signature, never cited.
- The sizer arm: size_run(item_count, noise_rate, seed, quorum) at the same coordinates — the equal-budget derivation's single home: B derives from the SAME (n, quorum), no independent parameter.
- The return: CurveRecord(acceptance=..., sizer=...) — the paired comparison per cell.

## §4 THE ONE AMENDMENT (additive; same commit as the module)

- accept_run(item_count: int, noise_rate: float, seed: int, quorum: int = ACCEPTANCE_QUORUM) -> AcceptanceRecord (acceptance.py:199).
- The ONE call site: quorum=ACCEPTANCE_QUORUM at line 249 becomes quorum=quorum.
- The docstring's step-(4) wording names the parameter (the ruled quorum at the call, not the hardwired literal).
- The re-verification inside this unit's gate: the 63-test acceptance suite green, the default behavior byte-identical (the 135-verdicts pin survives) — it rides the floor, not a new test.
- ACCEPTANCE_QUORUM appears at exactly two sites (:78, :249) — no other hardcode; the amendment is the smallest honest enabler of the fresh paired k=1 runs (Q-curve-matrix).

## §5 THE RECORD

- build/budget-curve-record.md at the store's build home (Q-curve-home; the acceptance-verification precedent's block form).
- The per-cell table's columns [PROPOSED: n, p, seed, k, tau-pairwise, tau-sizer, delta (the taus at 4dp each)].
- Both budget points [PROPOSED: ONE k-columned table — 54 rows, the k column the curve's own axis, both points readable in one scan; two tables rejected — they split one axis across two blocks the reader must re-join].
- The perfect case's row (p=0, n=10, seed 1109, k=3: both taus = 1.0000) — stated as data.
- The reading: supported/falsified/mixed over the measured data, never pre-written; the aggregate stated (the cells' count per direction). The ordering claim asserted NOWHERE the data has not ruled it (Q-curve-assertion).

## §6 THE TESTS (~7 named edges; NO ordering assertion anywhere)

1. The budget law exact: sum B_i = n0 x quorum, asserted per run (at both k points). 2. The pairing law: both arms' latent_order identical per seed, asserted. 3. The determinism: the same (n, p, seed, quorum) => byte-identical SizerRecord across replays. 4. The model's mechanics: the round-robin schedule's coverage (each item's thresholds cycle 1..n-1), the flip grammar at p, the exact-Fraction scores. 5. The measure invariants: accept_measure on the sizer's groups: P+Q+T = n0 (REUSED, never re-implemented). 6. The perfect case: p=0, n=10, seed 1109, k=3: BOTH arms tau = 1 exactly. 7. The record's completeness: the curve's table — every cell, both arms, both points — the record's data asserted present. The amendment's re-verification (the acceptance suite green at the default) rides the floor, not a new test.

## §7 THE FLOOR

- The standard form: pyright strict 0/0/0; ruff (ALL, line-length 120) zero findings; zero convenience ignores. The pyproject per-file entry [PROPOSED: "src/prioritree/budget_curve.py" = ["S311", "ARG001"] — the acceptance entry's kin, the same approved-brief citation; S311 the seeded simulation's random import, ruled at Q-curve-floor; ARG001 priced honestly: if the call forms keep every argument live (all four ride the CurveRecord and the runs), ARG001 never fires and the entry lists S311 alone — the brief names it, the build's ruff run decides]. Zero new runtime deps (random stdlib); the no-shell law (pure in-memory, zero subprocess); five-field docstrings (Provenance citing R13, acceptance-brief §5, the composition, the brief).

## §8 THE CARRIERS TABLE (G-BUDGET-CURVE's five → the spec's carriers)

| The condition | The carrier |
|---|---|
| (1) the module per the brief; the ONE additive amendment, the suite green, the default byte-identical | §1, §4; the gate's floor-green run |
| (2) the sizer green in the ruled model: the binary-threshold form, the budget law exact, the Fraction scores, the pairing law, the perfect case | §2, §6 tests 1, 2, 4, 6 |
| (3) the determinism byte-identical; the measure invariants, accept_measure REUSED | §1 (the clock-free record), §6 tests 3, 5 |
| (4) the record at the store's build home, the table whole, the reading honest, no ordering asserted | §5, §6 test 7 |
| (5) pyright 0/0, ruff zero, the S311-class ruling extended, zero new deps, kensho's independent re-run | §7; the read-back the evidence |

## §9 THE OPEN QUESTIONS carried to the gate (each [PROPOSED] + alternative + reason)

1. **THE NOISE-STREAMS RULING (load-bearing)**: the derived instance random.Random(f"{seed}-sizer") — the truth paired, the noise independent; §5 names the model not the realization. ALTERNATIVE: identical streams (maximal coupling) — variance-free, luck-correlated, arguably understating the sizer's independent error. 2. **The per-item judgments' record form**: yes-counts + B_i (the minimal replay surface) vs the (threshold, answer) pairs — the pairs add detail the replay never reads. 3. **compare_run's return shape**: the frozen CurveRecord (named, replay-checkable) vs the tuple (anonymous; the naming law unanswered). 4. **The record's table form**: one k-columned table (the axis in one scan) vs two tables. 5. **ARG001's necessity**: the call forms decide; the entry named either way, the ignore IS the ruling.

*Provenance: togo (統合, integrate), packet synthesize/budget-curve, route budget-curve, 2026-11-21 session. Read-only held — the brief returned in-message; landed by shinko via patch under the landing discipline. The tree is the truth.*
