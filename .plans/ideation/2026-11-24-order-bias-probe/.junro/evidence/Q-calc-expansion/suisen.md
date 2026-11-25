<!-- provenance: packet recommend/calc-ops · actor suisen · question Q-calc-expansion · date 2026-11-25 · verbatim copy — the projection reports/recommend/calc-ops.md is the source -->
<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — recommend/calc-ops

**Route:** order-bias-probe (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-25T04:29:36Z |
| 2 | report | suisen | 2026-11-25T04:42:57Z |
## Reported by suisen — 2026-11-25T04:42:57Z

# suisen (推薦) — THE CALCULATE EXPANSION ASSESSED FOR HIKARI: the op manifest, the provenance schema, the numerics policy, the priorities

Packet recommend/calc-ops · Route order-bias-probe · Q-calc-expansion · 2026-11-24. A RECOMMENDATION, NEVER A COMPUTATION — no number below is my product; every form cites the ground on disk (the convening ruling at the store's junro.json; the engine .opencode/scripts/calculate.py whole; the wrapper .opencode/tools/calculate.ts whole; the pin pyproject.toml >=3.13; reports/census/statistical-arithmetic.md and honest-conditions.md; FR-MEM-0036/0037; src/prioritree/scheduler.py:87-106 the derive_seed precedent). Every proposal pairs its recommendation with the reasoning.

## 0. THE LIVE EVIDENCE FOR THE PROVENANCE LAW, NAMED FIRST (it shapes the whole manifest)

My own recomputation (a recommendation's check, named as such — the instrument owes the settlement): the two census legs' Wilson-95 bounds at the SAME 12/22 DISAGREE — keisan §1.4: [0.3466, 0.7308]; shindan §2: [31.3%, 76.4%]. The disagreement is a DROPPED NORMALIZER: shindan's half-width omits the (1+z²/n) divisor (center 0.5387 ± 0.2257 unnormalized = [0.3131, 0.7644]; the correct 0.5387 ± 0.1921 = [0.3466, 0.7308]). Two legs, one quantity, two answers — and the record as it stands cannot settle which: neither leg carries an instrument trace to appeal to. That is FR-MEM-0036's fault made concrete: the trace must be INSEPARABLE from the number (§2), and the arithmetic must run at the instrument (§5's re-fire). The manifest below is built so this class of error cannot recur silently.

## 1. THE OP MANIFEST, TIERED

Each op: name / signature / semantics / stdlib backing / refusal domain (the ThreePart triggers) / consumers. EVERY op is stdlib-carried (the free-tier law: pyproject's dependencies untouched — math, statistics, random, hashlib only; the 3.13 pin carries math.comb/lgamma/sqrt/log/exp, statistics.NormalDist/median/fmean/pstdev/stdev/pvariance/variance, all from 3.8 or earlier). All-op grammar: fixed-argv --flag=value; EVERY operand explicit and required (a hidden default is an untraceable operand — no defaults anywhere in the new surface).

### TIER 1 — THE PROBE-UNBLOCKING ATOMS (first to land; the held verification's demands)

1. **sqrt** — `sqrt --a` — √a — math.sqrt — REFUSES a<0 (negative radicand: no real root; complex is outside the type contract) — consumers: the Wilson radical (§1.4), the half-width atoms (§3.4's 1.96·√(0.25/24)), the df=1 χ² p chain. The op keisan's census lacked — "the square roots verified by their squares (the tool's six ops carry no sqrt)": the detour this op kills.
2. **power** — `power --a --b` — a^b, b real (a², 0.825⁸, 2^24, 0.8^(1/8): one op; int bases keep exact int) — the ** operator (int exact / float64) — REFUSES 0^b for b≤0 (0^0 indeterminate; 0^negative is 1/0), unrepresentable results (the inf-guard) — consumers: the threshold constants (1.96+0.8416)²=7.849, (2.5758+0.8416)²=11.679, (2.394+0.8416)²=10.469 (§3.1); Wilson's z²; the ladder's 0.75⁸/0.825⁸ (§1.6); the MDE 0.8^(1/8); the BF's 2^m; the equivalence m = 1.96²×0.25/0.01.
3. **factorial** — `factorial --n` — n! EXACT INT, arbitrary precision — math.factorial — REFUSES non-integer n, n<0 — consumers: the binomial exact chains, the BF's Beta(k+1, m−k+1) = k!(m−k)!/(m+1)! form. THE NAMED BOUNDARY (docstring-carried): float64 overflows at 171! (170!≈7.26e306 fits; 171!>1.80e308) — the ENGINE's int is unbounded; the boundary rides any downstream float CONVERSION, never the op.
4. **combination** — `combination --n --k` — C(n,k) exact int — math.comb — REFUSES non-integers, n<0, k<0, k>n — consumers: the exact binomial's Σ C(22,k) (§1.2/§1.3), every sign-test tail, the BF chain.
5. **proportion** — `proportion --part --whole` — part/whole (the share form; percentage = proportion × 100 stepwise via the existing multiply — the composition's two citable traces beat one sugar op) — divide beneath — REFUSES whole=0 (division by zero), non-numeric — consumers: the position-share 12/22, the class shares 14/22 and 8/22, the slices 7/14 and 5/8, the rule-of-three 3/22 (§1.7), votes-per-pair 22/21.
6. **mean** — `mean --values` — the arithmetic mean — statistics.fmean — REFUSES empty array, non-numeric elements — consumers: the pace atoms (7.9 s/vote, 1.77 s/vote), votes-per-pair.
7. **variance** — `variance --values --form=population|sample` — statistics.pvariance / statistics.variance — REFUSES empty; the sample form at n<2 (the zero-denominator class) — consumers: the dispersion atoms behind the CI half-widths.
8. **stddev** — `stddev --values --form=population|sample` — statistics.pstdev / statistics.stdev — same refusals — consumers: the ±-point half-widths; derivable from variance+sqrt but carried directly (the cited quantity, one trace).
9. **max** / 10. **min** — `max --values` / `min --values` — REFUSES empty (no extremum of nothing) — consumers: the ladder's bounds, the pace extremes.
11. **median** — `median --values` — statistics.median — REFUSES empty, non-numeric — consumers: the sittings' central pace, robust centers.
12. **quantile** — `quantile --values --p` — the p-quantile by FIXED (n−1)-based linear interpolation (the method NAMED in the docstring — determinism demands one method, never a flag) — sorted-array arithmetic — REFUSES empty, p outside [0,1] — consumers: the quartile atoms, the datum's tails.
13. **wilson** — `wilson --k --n --z` — the Wilson score interval: p̂=k/n; d=1+z²/n; center=(p̂+z²/(2n))/d; half=z·√(p̂(1−p̂)/n + z²/(4n²))/d; RESULT the pair [lo, hi] — math.sqrt — REFUSES non-integer k, k<0, n≤0, k>n, z≤0 — consumers: §1.4's 12/22 → [0.3466, 0.7308]; the class slices (7/14, 5/8); the prospective datum's bounds (honest-conditions §4's 2-flip [0.3%, 30.0%]); §0's discrepancy settled by construction (the instrument computes, the seat quotes). The z-explicit form ruled over --confidence sugar: every constant appears in the trace, nothing resolved invisibly.
14. **binom-test** — `binom-test --k --n --p --sided=two|one` — the EXACT binomial p: at p=0.5 in arbitrary-precision INTS (Σ C(n,j)/2^n, the final division the only float — keisan's 1744436/4194304 form preserved exactly); at general p in float terms (each ≤1, the sum ≤1 — no overflow; tail underflow contributes 0); two-sided = 2·min(tail) capped at 1 — math.comb + int arithmetic — REFUSES non-integer k/n, k<0, n<0, k>n, p outside [0,1] — consumers: THE SIGN TEST (§1.2: 12/22 two-sided ≈0.8318; §1.3's bar: 17/22 rejects, 16/22 misses); THE POWER LADDER (§1.5: power at w = the one-sided tail at the bar — P(X≥17|0.75) is this op at p=0.75); the per-class bars (§1.6); the prospective sign test among flips (§2.3: 2·0.5⁶=0.03125). The COMPOSITE ruled in (not just atoms) because its interior — the tail sum, the min, the cap, the ×2 — is exactly where seat-side transcription errors enter (§0 is the proof).

### TIER 2 — THE MEASUREMENT CLASS'S STEADY DIET (lands with/before the design gate's threshold ruling)

15. **normal-cdf** — `normal-cdf --x` — Φ(x) — statistics.NormalDist().cdf — total (no domain refusals; non-numeric only) — consumers: the df=1 χ² p chain (p = 2(1−Φ(√χ²))), the tail atoms.
16. **normal-ppf** — `normal-ppf --q` — Φ⁻¹(q) — statistics.NormalDist().inv_cdf — REFUSES q outside (0,1) (q∈{0,1} → ±∞: the range refusal) — consumers: THE THRESHOLD TABLE'S Z CONSTANTS — 1.96=ppf(0.975), 0.8416=ppf(0.80), 2.5758=ppf(0.995), the Bonferroni-3 2.394=ppf(1−0.05/6) (§3.1); every power/sample arithmetic's z² atoms. A mistyped 2.394 is a silent wrong threshold; an envelope-carried operand is quotable.
17. **log** — `log --a` — ln(a) (any base stepwise: log(a)/log(b)) — math.log — REFUSES a≤0 (the log domain) — consumers: the BF chain's m·ln2, the log-space front door.
18. **exp** — `exp --a` — e^a — math.exp — REFUSES unrepresentable (e^710 overflows float64: the inf-guard) — consumers: the log-space chains' return step.
19. **log-factorial** — `log-factorial --n` — ln(n!) = math.lgamma(n+1) — REFUSES non-integer, n<0 — consumers: the large-m chains past the 171! float boundary.
20. **log-combination** — `log-combination --n --k` — ln C(n,k) = lgamma(n+1)−lgamma(k+1)−lgamma(n−k+1) — REFUSES the combination domain — consumers: the far-ladder general-p chains (the null-ish class), if ever run.
21. **log-beta** — `log-beta --a --b` — ln B(a,b) = lgamma(a)+lgamma(b)−lgamma(a+b) — REFUSES a≤0, b≤0 — consumers: THE BF FORM (§3.2: log BF₁₀ = log-beta(k+1, m−k+1) + m·ln 2, then exp) — the threshold table's strong-BF option priced honestly at the design gate.
22. **chisquare** — `chisquare --observed --expected` (equal-length JSON arrays) — the goodness-of-fit statistic χ² = Σ(O−E)²/E and its df (len−1); RESULT the pair [χ², df] — the sum/power/divide atoms — REFUSES length mismatch, empty, any E≤0 cell, non-numeric — consumers: the class-balance questions (the 14/8 mix). THE HONEST LIMIT (docstring-carried): the χ² p-VALUE at df>1 is NOT stdlib-carried (incomplete-gamma machinery) — the op emits the statistic; the df=1 p composes stepwise (√ → normal-cdf → complement → ×2, all citable); df>1 rides the ruled critical-value table, NEVER a silent approximation.
23. **shuffle** — `shuffle --values --seed` — the deterministic permutation under the EXPLICIT integer seed — random.Random(seed).shuffle — the S311 ruled seam precedent (acceptance.py, budget_curve.py: the seeded simulation, stdlib-reproducible) — REFUSES an absent or non-integer seed (DETERMINISM DEMANDS THE OPERAND — the one place entropy could creep, foreclosed by construction), empty array — consumers: the prospective experiment's presentation-draw design (the cure §4.2 priced at the design gate). THE PURITY RULING, ASSESSED HONESTLY: COMPATIBLE — the pure-query law demands same-inputs→same-output, and the seed IS an input; random.Random(seed) is process- and PYTHONHASHSEED-independent (Mersenne Twister, never the builtin hash — the derive_seed docstring's own named trap, scheduler.py:98); cross-version stability is foreclosed by the pin (>=3.13) + the KAT's byte-exact pin. NO RNG-without-seed op exists anywhere in the manifest — this op is the seed's only legal carrier.
24. **derive-seed** — `derive-seed --text` — the stable blake2b digest → int (scheduler.py's own derive_seed form: blake2b, first 8 bytes big-endian) — total (a pure function of its argument) — consumers: the seed's own provenance tool-carried (run_id → seed, the manifest's replay story citable as a trace). Recommended so the shuffle's seed never enters a report as a bare prose constant.

### TIER 3 — THE HONEST BOUNDARY (named, never silent — carried in every op's help text)

- NO SIMULATION/MCMC: any RNG without an explicit seed operand refuses by construction (the shuffle law generalizes); no sampled p-values, no bootstrap, no Monte Carlo — inference is EXACT (integer binomial) or NORMAL-DERIVED (the df=1 chain), never sampled.
- NO REGRESSION SUITES: no OLS/logistic/fitting — the moment the tool fits models it is a statistics library, not a calculator; the probe never demands it.
- NO SCIPY/NUMPY/MPMATH: priced and REFUSED where the stdlib carries the need (every op above is stdlib) — the named refused list: the general χ²/F/t CDFs, kernel densities, optimization, non-central power. A future need wanting them is a PRICED DEPENDENCY RULING at the collaborator — never a silent add.
- NO DATASET INGESTION: flags and JSON arrays only — the tool never reads files, never queries stores.
- NO PROSE OPS: the type contract stands.
- NO MUTATION, EVER; NOT a substitute for kensho's verification — the anti_scenario carried verbatim.
- THE MANIFEST ITSELF IS GOVERNED: the op set grows ONLY at a demonstrated friction entry + the collaborator's ruling — never by forecast.

## 2. THE PROVENANCE LAW MADE STRUCTURAL (FR-MEM-0036/0037)

### 2a. THE RESULT SCHEMA — the trace inseparable from the number

RECOMMENDED: the engine's stdout becomes THE TRACE LINE — one JSON object per run: {"op": "binom-test", "args": {"k": 12, "n": 22, "p": 0.5, "sided": "two"}, "result": 0.8318108367919922}. The op, the operands, the result, in ONE quotable byte-string. Reasoning: FR-MEM-0036's fault was "the reports carry no instrument traces — the provenance unauditable from the record"; a bare number on stdout REPRODUCES that fault (the seat re-assembles the citation from memory — §0 shows the cost). With the trace line, a report quoting the tool CANNOT cite a number without its provenance. Multi-valued results (wilson's [lo,hi], chisquare's [χ²,df]) carry the array in "result". NO TIMESTAMP in the trace — determinism demands the same inputs yield the same TRACE BYTES (the re-run check is the smoke's own instrument); the call's time lives in the seat's transcript. COMPATIBILITY NAMED HONESTLY: this EXTENDS Q-CALC-1's output law ("the number, and only the number") to "the result object, and only the result object" — a real shape change for the six existing ops, ruled at the collaborator's hand; the alternative (bare number, the call transcript as the trace) is DECLINED — the transcript lives at the session, not on the report's page; a naked number on the page is unauditable from the page.

### 2b. THE SMOKE PROTOCOL — grant never function (FR-MEM-0037)

THREE GATES, IN ORDER:
1. THE KAT (known-answer test) AS DATA: a fixture mapping every op → one canonical input → the EXACT expected trace line, byte-pinned (determinism is the claim; a tolerance would blur it). Content-in-configuration: the table is data; the check renders it.
2. THE TREE CHECK: the KAT rides as a fixed-argv pytest (subprocess.run over the script's argv — the tests/test_harness.py S603 ruled form), so the floor (make) carries the engine whole at every future build gate's floor-green.
3. THE SEAT SMOKE — THE LIVE PROOF: the arithmetic seat (keisan at the re-fire) invokes EVERY op once at its own live seat via the calculate tool, quoting each trace line verbatim into the report's smoke section. The map's allow proves nothing; the seat's own hands at the seat's own runtime are the only function-proof accepted. THE ORDER IS THE LAW: hikari lands → tree KAT green → seat smoke green → the verification re-fires. No report trusts the tool before its own seat's smoke lines are on the page.

## 3. THE NUMERICS POLICY, RULED

- INT FOR COUNTS, EXACT: every counting chain (combination, factorial, the p=0.5 binomial sums) in Python's arbitrary-precision ints — keisan's exact 1744436/4194304 is the ENGINE's native form, not an approximation; the final division is the only float.
- FLOAT64 FOR CONTINUOUS: IEEE-754 double for rates, p-values, bounds — two orders past the reports' honest 3-4-digit weight. DECIMAL PRICED AND DECLINED: nothing cited wants 28-digit decimals; the exact-int chains already carry the precision that matters.
- LOG-SPACE AT THE NAMED BOUNDARIES: float64 overflows at 171! and underflows below ~1e-308 — the boundaries NAMED IN THE DOCSTRINGS. Inside the band: direct float. Past it: the lgamma-backed forms (19-21) with exp as the return step. The probe's real Ns (22, 24, ~778) never leave the exact-int band; log-space is far-ladder insurance, not the daily diet.
- NO INTERNAL ROUNDING: the engine renders full precision (Python's shortest-roundtrip repr); the report's 3-4-digit weight is the SEAT's rendering at the quote — a truncated engine number is a laundered number.
- OVERFLOW GUARDS: the existing inf-guard at emit carries to every op; the int→float conversion at the final division refuses on OverflowError (naming the range); every domain guard fires BEFORE arithmetic.

## 4. THE DESIGN LAWS CARRIED WHOLE

- PURE QUERY: stateless, actorless, deterministic — every op; the shuffle's explicit-seed law is the one entropy seam, foreclosed by the required operand.
- FIXED ARGV, NO SHELL: the wrapper's per-op case composes --flag=value eargs; runArgv; no interpolation; values as JSON-array flags.
- THREEPART AT EVERY REFUSAL: REFUSED/Expected/Found/Next-action on stderr, stdout byte-empty, exit 1; never a traceback; argparse exit 2 for unusable invocations.
- FIVE-FIELD DOCSTRINGS: Purpose/Refuses when/Re-run/Touches/Provenance on every handler — the scheduler.py precedent; the boundary notes (171!, the χ² p limit, the shuffle's pin) live where the next reader meets them.
- ZERO-IGNORE: select=ALL + pyright strict — the expansion lands at the tree's bar; the ONE foreseen exception is S311 at the shuffle op (random.Random the ruled reproducibility seam — the acceptance.py/budget_curve.py precedent re-cited; the per-file entry NAMES the ruling, never a convenience).
- THE NAMING LAW: each op's name is its act-statement's first word (binom-test tests the exact binomial; wilson scores the interval).
- ONE ENGINE, ONE WRAPPER, BOTH TREES NAMED: the engine extends .opencode/scripts/calculate.py IN PLACE (one script, one rail — forking the invocation surface declined); the wrapper extends .opencode/tools/calculate.ts in place (its header's hand-maintained ruling, G-HARNESS-BRIEF); the hikari seat-yaml's tool description must MATCH the in-tree registry — amendment 16's drift question settles at this expansion (the scaffold's --check the catcher).
- ADDITIVE, NEVER REWORK: the six ops' semantics, the refusal shape, the parse contracts — untouched; the new ops are ADDITIONS under the same laws. The expansion EXTENDS the engine's own grammar, never rewrites it.

## 5. THE PRIORITIZED RECOMMENDATION

1. LAND TIER 1 FIRST — ALL 14 OPS, ONE ENGINE LEG, the trace-line schema riding the same landing. The probe's design stage is HELD on it (the amendment: "the design stage's every leg REMAINS HELD until the expanded tool is live, the arithmetic verification re-fired, and the census's numbers instrument-verified"). Tier 1 IS the held verification's demand: the recount (count/sum — have), the position-share (proportion), the exact p at N=22 (binom-test), the bounds (wilson), the ladder's atoms (power, sqrt, combination), the descriptives (mean/variance/stddev/max/min/median/quantile).
2. THE EXACT RE-FIRE, NAMED: the moment tier 1 is verified live at the seat (the three-gate smoke green: hikari landed → tree KAT green → keisan's seat smoke quoted), the census/statistical-arithmetic VERIFICATION chain re-dispatches to keisan — the recount at the tool, the one-vote discrepancy (6/14 vs 7/14, 11/11 vs 12/10) settled vote-by-vote, EVERY headline number tool-carried or stepwise-derived with the tool checking each supported step, every trace line quoted. On that report landing, the design stage's hold lifts (suisen's measurement design, hyoka's adversarial pass, moho's datum story, togo's gated synthesis at G-PROBE-DESIGN).
3. TIER 2 SECOND, BEFORE G-PROBE-DESIGN CLOSES: the gate rules .05/.01/Bonferroni-3/strong-BF — the z constants (normal-ppf), the BF chain (log-beta/log/exp), the χ² statistic (class balance), and shuffle/derive-seed (the cure's presentation-draw priced at the gate) all want to be citable AT the ruling, not after it.
4. TIER 3 STANDS AS WRITTEN — the boundary never lands; revisited ONLY at a demonstrated friction entry + the collaborator's ruling.
5. THE COMPOSITES DECLINED, THE ATOMS RULED: the power/sample-size mega-composites are DECLINED — the stepwise atom chains compose every demonstrated form in ≤5 citable traces (the census's own workaround already names the stepwise form legitimate; every constant stays quotable; a composite hides the formula). binom-test and wilson are the ruled-in exceptions (long, error-prone interiors — §0 the proof). A new composite earns its place only at a demonstrated friction entry, never a forecast.
6. THE FIRST KAT ROWS, PINNED FROM THE CENSUS'S OWN HEADLINES (the smoke's first quarry — the discrepancies settle at the instrument, in public): binom-test k=12 n=22 p=0.5 sided=two → ≈0.831811; wilson k=12 n=22 z=1.96 → [≈0.3466, ≈0.7308]; power a=0.825 b=8 → ≈0.2146 (keisan's own square-verified 0.463251²); proportion part=12 whole=22 → ≈0.545455; combination n=22 k=12 → 646646. The KAT's exact bytes pin at implementation.

THE ONE-LINE HEADLINE: 24 new stdlib-backed ops in three tiers (14 unblocking the held verification, 10 the measurement diet, the boundary refused by name), the trace-line result schema making FR-MEM-0036 structural, the three-gate smoke making FR-MEM-0037 structural — and the arithmetic verification re-fires to keisan the moment the seat smoke is green.
