# discover/budget-curve — the discovery census (tansa; the record; the pipeline's first leg)

- Provenance: tansa (探査, discover), packet discover/budget-curve, route budget-curve, 2026-11-21 — read-only held (7 reads: the composition, acceptance.py whole, the acceptance-brief §5, the k=1 baseline table, the route's gates record, tests/test_acceptance.py, the verification-record precedent); the census returned in-message; landed by shinko via patch.

## (1) THE CENSUS — what exists

- **The amendment's site**: accept_run's signature (acceptance.py:199) `def accept_run(item_count: int, noise_rate: float, seed: int) -> AcceptanceRecord:` — the ruled amendment adds `quorum: int = ACCEPTANCE_QUORUM` here, the default pinned at 3; the quorum threading's site: the register_run call's `quorum=ACCEPTANCE_QUORUM` literal (line 249) becomes `quorum=quorum` — the ONE expression.
- **The reuse target — accept_measure** (acceptance.py:156-196): consumes (ranked_groups, latent_order); the contract — over the n0 pairs of the flattened groups, same group => T, different => P/Q by the latent-earlier item's group order; reads groups ALONE, never scores; REFUSES when P+Q+T != n0; deterministic. The sizer's requirements: emit the groups covering every id exactly once, the group order carrying the ranking's direction.
- **The matrix constants**: ACCEPTANCE_FLOOR = Fraction(4,5); ACCEPTANCE_SEEDS = (1109, 2213, 3371); ACCEPTANCE_NOISE_RATES = (0.10, 0.15, 0.20); ACCEPTANCE_ITEM_COUNTS = (10, 20, 30); DEGRADATION_RATE = 0.35; ACCEPTANCE_QUORUM = 3; ACCEPTANCE_ID_TEMPLATE; HARNESS_COMPARATOR_ID/CLASS; the derived floor integers 25/16. The RNG discipline: ONE random.Random(seed) per run, the permutation FIRST, per-judgment draws after; the honesty guard.
- **The k=1 baseline — the opening evidence**: 8 of 27 in-band cells sub-floor; min tau 0.4714 at (10, 0.20, 3371); the structural pattern (the n=10 column failing at every rate, the p=0.20 column at every n); 3 of the 8 cells' coordinates NOT named on disk (the probe deleted within its session; the bytes record the data's only home). k=3: ALL 27 hold, min 0.8223, max 0.9775.
- **The re-verification surface** (tests/test_acceptance.py, 5 tests): every accept_run call positional (n, p, seed) — zero keyword quorum anywhere; the 135-verdicts pin asserts the k=3 default's behavior — the amendment leaves the suite byte-identical. The record-form precedents: the *-verification.md form (the title, the Seat line, the runs block, the read-back, the verdict, the closure).

## (2) THE GAPS the brief must pin — as questions

1. **The threshold schedule's domain** — is m the PER-ITEM counter (each item's stream cycles thresholds independently) or the GLOBAL judgment counter? The round-robin's coverage pattern differs.
2. **The per-item budget split** — the walked arithmetic at every ruled (n, k): floor = B // n, r = B mod n, the first r items in id order the ceiling (5x14+5x13 at n=10/k=3; 10x29+10x28; 15x44+15x43; the k=1 splits 5x5+5x4, 10x10+10x9, 15x15+15x14); the odd-n integral edge named (ruled n all even — non-integral by construction).
3. **The score's Fraction form + polarity** — yes-count / B_i; which direction is "above threshold j"; the perfect case the polarity's only end-to-end proof.
4. **The tie-group emission form** — score-descending groups, within-group by id (the tally's deterministic mirror); fully pinned for byte-identical replays.
5. **SizerRecord's fields** — the ruled list (coordinates, latent_order, per-item judgments, scores, ranked_groups, the (P,Q,T)); the open: exact names/types; does B_i ride; the per-item judgments' form ((threshold, answer) pairs or yes-counts only).
6. **compare_run's return shape** — a paired frozen record (a new named type) or a tuple of the two records; derived taus or only the integer counts.
7. **The amendment's exact patch form** — the signature line + the threading; the docstring's step-(4) wording update; the re-verification (63 green, the default byte-identical) inside this unit's gate; the amendment riding the same commit as the module.
8. **The record's shape** — build/budget-curve-record.md: the per-cell table's columns (n, p, seed, k, both taus, a delta?); both budget points; the tau representation (4dp); the reading's honest form (supported/falsified/mixed, never pre-written).
9. **The tests' named edges (~6-8)** — the ruled falsification set's seven: the budget law exact; the pairing law; the determinism replays; the model's mechanics; the measure invariants (accept_measure REUSED); the perfect case (tau = 1 exactly, both arms); the record's completeness.
10. **THE NOISE-STREAMS QUESTION** — the ruled pairing law (fresh instances at the SAME seed) means the latents match AND the judgment u-sequences COINCIDE position-by-position (the SAME noise realization — maximal coupling) unless the sizer's stream derives differently. Identical vs independent: rikai's leg prices it; the brief rules it.

## (3) THE LAWS RIDING

- **The naming law** (budget_curve.py + size_run/compare_run/SizerRecord ruled); **content-in-configuration** (the threshold grammar, the remainder rule, the budget points, the record's shape); **five-field docstrings** (Provenance citing R13, §5, the composition, the brief); **the zero-findings bar + the S311 ruling's extension** (the pyproject per-file entry extends to budget_curve.py; ARG001 likewise if needed); **zero new runtime deps** (random stdlib); **the no-shell law**; **one-commit-per-increment** (the module + tests + the ONE amendment together); **NO ordering assertion anywhere in the unit** — the graduation ruled at the close over the measured data.

*The tree is the truth; the synthesis joins this census with understand/budget-curve.md at G-BUDGET-CURVE-BRIEF.*
