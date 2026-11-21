# understand/budget-curve — the mechanism analysis (rikai; the record; the pipeline's second leg)

- Provenance: rikai (理解, understand), packet understand/budget-curve, route budget-curve, 2026-11-21 — read-only held (4 reads: the composition, acceptance.py whole, the acceptance-brief §5, the k=1 baseline table); the analysis returned in-message; landed by shinko via patch.

## (1) THE SIZER'S CHAIN (the binary-threshold model, stepped)

- (1) The latent order — n ids from the template, the truth = rng.sample as the instance's FIRST act; the honesty guard rides. (2) The thresholds — j in {1..n-1}, the integer midpoints; the judgment asks "is item i's latent position > j?" — zero floats. (3) The true answer — deterministic from the truth: position(i) > j => yes; never sampled. (4) The noise — ONE flip draw per judgment: u = rng.random(); u < p => the flipped answer, else the true (the acceptance grammar reused verbatim in form). (5) The round-robin schedule — judgment m (1-indexed, per item) uses threshold ((m-1) mod (n-1)) + 1 — the exhaustive-coverage analog of the pairwise re-serving loop. (6) THE PER-ITEM BUDGET SPLIT — total B = n0 x k; per-item base q = B // n, remainder r = B mod n; the first r items (by id) get q+1, the rest q — THE WALKED TABLE: n=10/k=1 => 5x5+5x4=45; n=10/k=3 => 5x14+5x13=135; n=20/k=1 => 10x10+10x9=190; n=20/k=3 => 10x29+10x28=570; n=30/k=1 => 15x15+15x14=435; n=30/k=3 => 15x44+15x43=1305 — r = n/2 at every ruled cell (the ruled n ALL EVEN => n-1 odd => non-integral at k=1 AND k=3); THE ODD-N EDGE named: at odd n and k=1 the split is INTEGRAL (n=11: 55/11 = 5, r=0 — the flat split; ruled n never hits it; the brief names it). (7) The score — the exact Fraction(yes_count, B_i) per item — never a float. (8) The ranking — score-descending; equal Fractions tied in one group; within-group order by id — mirroring the tally's emission form. (9) THE MEASURE REUSE — accept_measure reads only co-membership and group order over the flattened members; the sizer's groups carry every id exactly once, groups ordered by score — the contract fits exactly; P+Q+T = n0 holds by construction; no surface mismatch.

## (2) THE PAIRING LAW — priced (the brief rules)

- **(a) IDENTICAL STREAMS** (both arms random.Random(seed)): the latent matches by construction, but every subsequent draw mirrors position-for-position — the arms face the SAME noise realization. Strictest pairing; isolates aggregation from noise luck — but the noise is one realization, not two samples of the model; variance-free and luck-correlated.
- **(b) INDEPENDENT STREAMS**: the same seed for the latent's draw (the pairing law — the same truth), then the sizer's noise from a derived instance, e.g. random.Random(f"{seed}-sizer"). Same truth, independent noise; one new named derivation rule.
- **RECOMMENDATION: (b), the derived-instance form.** §5's own words — "the same noisy comparator at the same p" — name the noise MODEL, not the realization; the paired-cell design needs only the TRUTH paired (the latent byte-identical per seed), not the noise mirrored. Mirrored noise would make the comparison conditional on one luck draw and arguably understate the sizer's independent error structure. The derivation is one named constant-free line; the brief rules.

## (3) THE AMENDMENT'S BLAST RADIUS — minimal, verified

- accept_run gains quorum: int = ACCEPTANCE_QUORUM; the ONE call site (the register_run call, line 249) threads quorum=quorum. ACCEPTANCE_QUORUM appears at exactly two sites in acceptance.py (the constant at :78, the call at :249) — NO other hardcode; the docstring's step-(4) wording already parameter-shaped. Default unchanged => the landed 63-test suite byte-identical in behavior.

## (4) THE EQUAL-BUDGET LAW — proven

- The sizer total = r x (q+1) + (n-r) x q = n x q + r = B = n0 x k EXACTLY at every ruled cell (the walked table). The pairwise total = n0 x k — each of the n0 pairs served quorum times through next_pair's re-serving loop (the count-suffixed judge id tracking the census). Equal at both budget points, exactly, by construction.

## (5) THE RECORD'S DETERMINISM

- The SizerRecord's surface is clock-free whole: the coordinates (n, p, seed, k), the latent order, the per-item judgments and exact-Fraction scores, the ranked groups, the counts (P, Q, T). NO stamps anywhere — the record never touches VoteRecord/RunManifest (the sizer's groups are data, measured by the pure accept_measure). Same seed => the same stream => the same bytes across replays — byte-identical by construction, STRONGER than the pairwise arm's field-selected surface (whose stamps are named-and-excluded).

- Absences stated as facts: budget_curve.py absent (this packet precedes the build); no existing quorum-parameter surface beyond the one call site; the odd-n integral-split edge unruled (the brief's to rule).

*The tree is the truth; the synthesis joins this analysis with discover/budget-curve.md at G-BUDGET-CURVE-BRIEF.*
