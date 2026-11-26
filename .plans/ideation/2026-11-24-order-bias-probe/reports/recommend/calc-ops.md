<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — recommend/calc-ops

**Route:** order-bias-probe (executing) | **Events:** 22 | **Reports:** 11

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-25T04:29:36Z |
| 2 | report | suisen | 2026-11-25T04:42:57Z |
| 3 | dispatch | shinko | 2026-11-25T04:44:18Z |
| 4 | result | shinko | 2026-11-25T04:44:18Z |
| 5 | report | jikko | 2026-11-25T04:46:35Z |
| 6 | report | tansa | 2026-11-26T00:40:02Z |
| 7 | dispatch | shinko | 2026-11-26T00:41:08Z |
| 8 | dispatch | shinko | 2026-11-26T00:41:08Z |
| 9 | report | jikko | 2026-11-26T00:42:03Z |
| 10 | report | jikko | 2026-11-26T01:03:11Z |
| 11 | dispatch | shinko | 2026-11-26T01:03:40Z |
| 12 | report | jikko | 2026-11-26T01:04:22Z |
| 13 | dispatch | shinko | 2026-11-26T01:11:40Z |
| 14 | report | jikko | 2026-11-26T01:18:30Z |
| 15 | dispatch | shinko | 2026-11-26T01:19:28Z |
| 16 | dispatch | shinko | 2026-11-26T01:19:28Z |
| 17 | report | keisan | 2026-11-26T01:21:24Z |
| 18 | report | jikko | 2026-11-26T01:30:22Z |
| 19 | dispatch | shinko | 2026-11-26T01:31:11Z |
| 20 | dispatch | shinko | 2026-11-26T01:31:11Z |
| 21 | report | moho | 2026-11-26T01:32:26Z |
| 22 | report | jikko | 2026-11-26T01:38:35Z |
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
## Reported by jikko — 2026-11-25T04:46:35Z

R11 (jikko, recommend/calc-ops step 2): the assessment's evidence copy landed.
File: .junro/evidence/Q-calc-expansion/suisen.md — NEW (107 lines), one patch created the evidence home; no findings.
Content: one provenance head line + the 106-line verbatim copy of the projection reports/recommend/calc-ops.md.
Head read-back: "<!-- provenance: packet recommend/calc-ops · actor suisen · question Q-calc-expansion · date 2026-11-25 · verbatim copy — the projection reports/recommend/calc-ops.md is the source -->" / "<!-- regen: uv run python scripts/generation/kumi_views.py -->".
Not done: nothing else — one file, one patch; no other surface touched.
## Reported by tansa — 2026-11-26T00:40:02Z

# tansa (探査) — THE CALCULATE EXPANSION'S DELIVERY CENSUS: the note refused at the boundary, the engine whole at 30 ops, the wrapper and the KAT unlanded — the smoke's ground named

Packet recommend/calc-ops · Route order-bias-probe · 2026-11-25. A CENSUS, NEVER A JUDGMENT — what exists, as it exists, line-pinned; the tree is the truth. Frame: the collaborator's notice (2026-11-25): "hikari complete. opencode restarted. delivery note from hikari: /Users/marklosey/projects/kepric/hikari/.plans/ideation/2026-11-24-calculate-expansion/build/delivery-note-prioritree.md".

## 1. THE DELIVERY NOTE — REFUSED AT THE BOUNDARY (the standing precedent, again)

ATTEMPTED: read /Users/marklosey/projects/kepric/hikari/.plans/ideation/2026-11-24-calculate-expansion/build/delivery-note-prioritree.md
HAPPENED (verbatim, the boundary's verdict): "The user has specified a rule which prevents you from using this specific tool call. Some of the relevant rules [{"permission":"*","action":"allow","pattern":"*"},{"permission":"external_directory","pattern":"*","action":"ask"},{"permission":"external_directory","pattern":"/Users/marklosey/.local/share/opencode/tool-output/*","action":"allow"},{"permission":"external_directory","pattern":"/var/folders/mb/3b37nw4140j4yk2xf34n5mqc0000gn/T/opencode/*","action":"allow"},{"permission":"*","action":"deny","pattern":"*"},{"permission":"external_directory","pattern":"/Users/marklosey/.local/share/opencode/tool-output/*","action":"allow"}]"
The external_directory boundary refused the read — tansa's reads stopped at the tree's edge, the standing precedent holding. The note's content (the delivered ops, the KAT surface, the regen state, any integration instructions) is NOT censusable from this seat; the tree's own landed surface is the truth this census reports.

## 2. THE LANDED EXPANSION IN THIS TREE

### 2a. THE ENGINE — .opencode/scripts/calculate.py WHOLE (1228 lines), EXPANDED TO 30 OPS

The docstring names the ruled shape (lines 13-27): "30 deterministic ops (Q-CALC-1's six arithmetic and counting + Q-CALC-EXPANSION's 24: statistics, combinatorics, distribution, seeded permutation)", output "THE TRACE LINE, and only the trace line, on stdout — {"op","args","result"} compact JSON... NO timestamp — the same inputs yield the same trace bytes". Imports stdlib-only (72-80: argparse, hashlib, json, math, random, re, statistics, sys).

TIER 1'S 14 — ALL PRESENT, line-pinned (handler / parser):
- sqrt — _cmd_sqrt 351-374 / 1108-1110 — math.sqrt; REFUSES a<0 (366-373, the complex-result type contract named)
- power — _cmd_power 377-412 / 1112-1115 — the ** operator; REFUSES 0^b at b≤0 (397-402, 0^0 indeterminate), negative base at non-integer b (403-411); hyoka A6 carried in provenance (388-391)
- factorial — _cmd_factorial 415-437 / 1117-1119 — math.factorial exact int; REFUSES n<0 (431-436); THE 171! BOUNDARY NAMED (418-420: "float64 overflows at 171!... the boundary rides any downstream float conversion, never this op")
- combination — _cmd_combination 440-474 / 1121-1124 — math.comb; REFUSES n<0/k<0 (459-464), k>n (465-473 — the stdlib's silent 0 refused instead, keisan's priced addition)
- proportion — _cmd_proportion 477-509 / 1126-1129 — part/whole; REFUSES whole=0 (498-508)
- mean — _cmd_mean 512-526 / 1131-1133 — statistics.fmean
- variance — _cmd_variance 529-560 / 1135-1138 — pvariance/variance at --form=population|sample; sample n<2 REFUSED (551-559, the zero-denominator class)
- stddev — _cmd_stddev 563-593 / 1140-1143 — pstdev/stdev, same refusals (584-592)
- max — _cmd_max 596-610 / 1145-1147 — builtin max
- min — _cmd_min 613-627 / 1149-1151 — builtin min
- median — _cmd_median 630-645 / 1153-1155 — statistics.median
- quantile — _cmd_quantile 648-683 / 1157-1160 — FIXED (n-1)-based linear interpolation, ENGINE-OWNED (no stdlib backing, as specified); REFUSES p outside [0,1] (671-676)
- wilson — _cmd_wilson 686-720 / 1162-1166 — the composite WITH the (1+z²/n) divisor present (717-719: d = 1 + z*z/n — suisen §0's dropped normalizer corrected by construction); RESULT the pair [lo, hi]; REFUSES k<0, n≤0, k>n, z≤0 (710-715)
- binom-test — _cmd_binom_test 723-777 / 1168-1173 — exact int tails at p=0.5 (760-765, Σ C(n,j)/2^n), float terms at general p (766-777), --sided=two|one; REFUSES the k/n/p domain (754-759), the general-p float overflow naming the log-space lane (768-773)

TIER 2'S 10 — ALSO LANDED (the engine docstring 58-61: "the 24 statistical ops LANDED band by band (the staged sub-ask law, complete at this final band)"): normal-cdf 798-813/1174-1176, normal-ppf 816-839/1178-1180 (q strictly inside (0,1), 833-838), log 842-863/1182-1184, exp 866-889/1186-1188 (the e^710 overflow refused, 881-888), log-factorial 892-913/1190-1192, log-combination 916-940/1194-1197, log-beta 943-969/1199-1202, chisquare 972-1008/1204-1207 (pair [statistic, df]; the p-limit honesty docstring-carried 978-980), shuffle 1011-1056/1209-1212 (seed REQUIRED — 1040-1053, the refusal teaches the derive-seed route; NO RNG-without-seed op, docstring 1027-1029), derive-seed 1059-1074/1214-1216 (blake2b first 8 bytes big-endian, the scheduler.py form).

THE PROVENANCE SCHEMA — LANDED, STRUCTURAL: _emit 112-131 (one JSON object per run {"op","args","result"}; the raw flag values as sent; integral float coerced to int at result; NO timestamp — same inputs, same trace bytes); _emit_pair 134-158 (wilson's [lo,hi], chisquare's [statistic,df]); _emit_list 780-795 (shuffle's structural permutation, no coercion). The ThreePart shape at _refuse 86-89 (REFUSED/Expected/Found/Next-action, stderr, stdout byte-empty, exit 1). Five-field docstrings (Purpose/Refuses when/Re-run/Touches/Provenance) on EVERY new handler — verified in the reads.

### 2b. THE WRAPPER — .opencode/tools/calculate.ts, NOT EXTENDED (78 lines, the six-op form)

The enum (lines 24-27) carries ONLY ["add","subtract","multiply","divide","sum","count"]; the description (line 22) and the help text (line 73) still say "six ops"; every case's argv form UNCHANGED (the --flag=value eargs over runArgv, lines 38-71 — the Q-CALC-1 form held). The header (line 1): "prioritree-owned (2026-11-19, G-HARNESS-BRIEF)... hand-maintained in prioritree's tree". The engine's own docstring scopes the wrapper OUT of the delivery leg (29-36: "the generated wrapper (.opencode/tools/calculate.ts, emitted at regen by scripts/generation/generate_tools.py — the collaborator's hand, never this leg's)"). THE LIVE PROOF: this restarted session's own calculate tool grant carries the six ops only (its description verbatim = calculate.ts line 22) — the 24 new ops are engine-side (uv run python .opencode/scripts/calculate.py <op>) but NOT seat-callable through the calculate tool.

### 2c. THE KAT SURFACE — NOT LANDED IN THIS TREE (fixture count: 0)

grep "calculate" over tests/ → NO match (15 test files, none touching calculate). grep "binom-test" / "646646" / "known-answer" repo-wide → hits ONLY in the engine, the 12 regenerated seat prompts, and the store's report/evidence/packets copies. NO test_calculate*.py, NO KAT fixture, NO pinned trace bytes anywhere in prioritree. The manifest's first KAT rows (§5.6: binom-test 12/22→≈0.831811; wilson 12/22 z=1.96→[≈0.3466,≈0.7308]; power 0.825^8→≈0.2146; proportion 12/22→≈0.545455; combination C(22,12)→646646) have NO ground in this tree. (The KAT may ride the hikari tree — the boundary refused that read; THIS tree's floor is what the census pins.)

### 2d. THE REGEN STATE — THE SEAT PROMPTS REGENERATED; THE WRAPPER DID NOT

- .opencode/prompts/seats/keisan.md line 26: the calculate row carries ALL 30 ops — verified across all 12 seat prompts (keisan, hansei, hyoka, jikko, keikaku, kensho, moho, rikai, shindan, suisan, tansa, togo) — the regen DID change the prompts' calculate rows.
- opencode.json's keisan row (181-222): description UPDATED (line 182: "arithmetic, counting, statistics, combinatorics, distribution, and seeded permutation on the calculate surface"); "calculate": "allow" UNCHANGED (line 188). tansa's row likewise calculate: allow (line 500), git: deny (line 507).
- calculate.ts: UNCHANGED (2b above) — the regen's calculate row reached the prompts, not the hand-maintained wrapper.
- scripts/ does NOT exist in prioritree (glob "scripts/**" → nothing) — the scaffold's emission authority rides the hikari tree (external; the boundary refused).

### 2e. GIT'S VIEW — NOT CENSUSABLE FROM THIS SEAT

No shell or git act is granted to tansa (opencode.json line 507: "git": "deny"; no bash tool in the pack). git status's new/modified list cannot be read from here — the boundary named, honestly; the file-level truth above IS the tree's truth at this census's hand.

## 3. THE DELIVERY'S HONESTY CHECK — suisen's manifest vs the landed ops

EVERY TIER-1 OP LANDED AS SPECIFIED — name, signature, semantics, stdlib backing (2a's line pins): no op renamed, no op re-shaped, no op declined. THE PROVENANCE SCHEMA LANDED (the one-line JSON trace, 2a). THE BOUNDARY HELD: pyproject.toml dependencies (line 9: fastapi, httpx2, jinja2, ouncemcp, python-multipart, uvicorn[standard]) — NO scipy/numpy/mpmath; the engine's imports stdlib-only; NO RNG-without-seed op exists (shuffle's seed required=True at 1211, the refusal at 1040-1053).

THE DEVIATIONS, NAMED:
1. THE WRAPPER GAP — the manifest §4 ruled "the wrapper extends .opencode/tools/calculate.ts in place"; it did NOT (the six-op form stands, 2b). The delivery scopes it to "the collaborator's hand" (engine docstring 29-36) — a known sequencing gap, never a silent decline — but the consequence is hard: the smoke's gate 3 cannot fire for the 24 new ops at the live seat.
2. THE KAT GAP — the manifest §2b's gates 1-2 (the KAT fixture as data; the fixed-argv pytest rider) landed NOWHERE in prioritree (2c). The tree's floor carries no engine-whole check.
3. THE S311 PER-FILE ENTRY — the manifest §4 foresaw "the per-file entry NAMES the ruling" at the shuffle op; pyproject.toml carries NO entry for calculate.py. Scope fact: ruff's src=["src"] and pyright's include=["src","tests"] never covered .opencode/scripts — the ruling lives in the shuffle's own docstring instead (1011-1029). Named, never silent.
4. THE STAGING FACT (an exceeding, not a fault) — the recommendation staged tier 1 first, tier 2 before G-PROBE-DESIGN closes; the delivery landed BOTH tiers' 24 ops in one landing ("band by band... complete at this final band"). Every op is as specified; only the staging differs.

## 4. THE SMOKE PROTOCOL'S READINESS — THE THREE GATES' GROUND

1. THE KAT FIXTURES: DO NOT EXIST in prioritree — count 0. GATE NOT READY.
2. THE TREE'S PYTEST: the fixed-argv form exists (tests/test_harness.py, the S603 ruling at pyproject 94-104) but carries NO calculate KAT — grep "calculate" over tests/ is empty. GATE NOT READY.
3. THE SEAT'S LIVE PER-OP RUN: the calculate row at opencode.json is unchanged (allow) and the session is restarted — but the restarted registry serves the SIX-OP wrapper (this census's own calculate grant is the proof). keisan's live smoke for the 24 new ops is NOT dispatchable until calculate.ts extends and the registry reloads. GATE HALF-READY (grant live, registry stale).

THE FINDING THIS CENSUS CARRIES (a finding, never a ruling): the smoke is NOT green-able on this ground — the KAT and its pytest rider must land in prioritree, and the wrapper must extend (the collaborator's hand), before the three-gate order (KAT green → pytest green → seat smoke green) can begin. The design stage's hold does not lift on this census.
## Reported by jikko — 2026-11-26T00:42:03Z

R11 — the KAT copy attempt (step 4b, recommend/calc-ops, order-bias-probe): the boundary refused; nothing landed.
Attempted read: /Users/marklosey/projects/kepric/hikari/tests/test_calculate_expansion_kat.py — REFUSED: "The user has specified a rule which prevents you from using this specific tool call. Some of the relevant rules [{"permission":"*","action":"allow","pattern":"*"},{"permission":"external_directory","pattern":"*","action":"ask"},{"permission":"external_directory","pattern":"/Users/marklosey/.local/share/opencode/tool-output/*","action":"allow"},{"permission":"external_directory","pattern":"/var/folders/mb/3b37nw4140j4yk2xf34n5mqc0000gn/T/opencode/*","action":"allow"},{"permission":"*","action":"deny","pattern":"*"},{"permission":"external_directory","pattern":"/Users/marklosey/.local/share/opencode/tool-output/*","action":"allow"}]"
Nothing landed — glob confirms no tests/test_calculate_expansion_kat.py in this tree; no engine-path pinning performed; patch never fired; the 87 pinned rows never reached this seat's hands.
Precedent consistent — the third read stopped at the tree's edge (tansa's reads refused twice before); the refusal is the evidence.
Fallback: the collaborator's cp carries the battery across; the wrapper lane (step 4a) unaffected.
## Reported by jikko — 2026-11-26T01:03:11Z

R11 — step 4a LANDED (the wrapper lane + the S3 entry, one patch, two files; recommend/calc-ops, 2026-11-26).
1) .opencode/tools/calculate.ts (78→241 lines): the enum at the 30 ops in the ruled order + .or("help"); 31 cases (30 ops + help) mirroring the standing runArgv form, every flag per the engine's argparse (--k/--n/--z at wilson, --k/--n/--p/--sided at binom-test, --observed/--expected at chisquare, --values/--seed at shuffle, --text at derive-seed — no renames); the zod block's 17 params, ONE description per name; the help text re-composed from the engine's declarations (30 entries + the shared "To list every make target" closing).
2) pyproject.toml: ".opencode/scripts/calculate.py" = ["S311"] at per-file-ignores' tail, the ruling comment naming the seeded seam (the acceptance.py/budget_curve.py precedent; never an in-engine noqa).
READ-BACKS — enum verbatim: .enum(["add","subtract","multiply","divide","sum","count","sqrt","power","factorial","combination","proportion","mean","variance","stddev","max","min","median","quantile","wilson","binom-test","normal-cdf","normal-ppf","log","exp","log-factorial","log-combination","log-beta","chisquare","shuffle","derive-seed"]).
wilson's case verbatim: case "wilson": { — const eargs = ["wilson"] — if (args.k !== undefined) eargs.push(`--k=${args.k}`) — if (args.n !== undefined) eargs.push(`--n=${args.n}`) — if (args.z !== undefined) eargs.push(`--z=${args.z}`) — return formatOutput(await runArgv(["uv", "run", "python", ".opencode/scripts/calculate.py", ...eargs], { cwd: context.directory })) — }.
zod p description verbatim: "the quantile position in [0, 1] (a number, as a string) (quantile); the null probability in [0, 1] (a number, as a string) (binom-test)". pyproject row verbatim: ".opencode/scripts/calculate.py" = ["S311"].
CHOICES, reported: (a) the merged-description law read literally — "identical descriptions never merge" → per-op entries (each op's engine help tagged with its op; a/b/n/k/values/form all per-op), never grouped; p byte-verbatim per the note's example — regroupable if the coordinator reads "with its ops" as the grouped form. (b) the tool description re-authored for the 30-op truth (the six-op text falsified: the op count, "returns a number" [wilson/chisquare return pairs, shuffle an array], "arithmetic and counting only") — composed from the engine's own argparse description + the trace-line law + the regenerated seat prompts' ruled domain wording. (c) the help text's per-op content = the engine's subparser + argparse helps verbatim (the standing "(deterministic)" summary decoration dropped — declaration-sourced, per-op correct by construction).
NOT DONE, named: the patch's tsc findings are PRE-EXISTING environment gaps (missing @types/node/@types/bun — the plugin's own shell.d.ts, the untouched _run.ts, and calculate.ts line 8's standing `stderr: Buffer | string`, byte-untouched by the hunk); my added lines carry zero type errors; no cure attempted (outside the two-file fence — the coordinator rules). No lint/type/test runs (the coordinator's instruments; kensho the second eyes). Nothing else touched.
## Reported by jikko — 2026-11-26T01:04:22Z

R11 — jikko, the three fixed-argv acts, outcomes verbatim (step 4c, packet recommend/calc-ops):
1. TEST: "336 passed in 29.62s" — the expected 336, count unchanged (the KAT absent at the boundary's refusal).
2. LINT: "uv run ruff check src/ tests/ / All checks passed!" — zero findings, the pyproject's new S311 entry parsing clean.
3. TYPECHECK: "uv run pyright / 0 errors, 0 warnings, 0 informations".
The wrapper is TypeScript (not the suite's scope); the changeset (calculate.ts + pyproject.toml) broke nothing.
## Reported by jikko — 2026-11-26T01:18:30Z

R11 — step 5 diagnosis (jikko, packet recommend/calc-ops; NO fixes applied). Disk truth: tests/test_calculate_expansion_kat.py = 419 lines / 87 rows (delivery note said 351 — delta noted); headline row intact at line 162 (binom-test 12 22 0.5 two -> 0.8318119049072266).
(1) LINT — make lint (uv run ruff check src/ tests/): "Found 13 errors. [*] 5 fixable with `--fix`"; zero in src/, all 13 in tests/test_calculate_expansion_kat.py, verbatim:
CPY001 1:1 "Missing copyright notice at top of file" | D401 61:5 "First line of docstring should be in imperative mood: \"The S603 fixed-argv fire — [sys.executable, the engine path, the op, the flags].\"" | D401 66:5 "First line of docstring should be in imperative mood: \"The positive row — stdout is the trace line, byte-asserted.\"" | D401 79:5 "First line of docstring should be in imperative mood: \"The refusal row — exit 1, stdout byte-empty, the ThreePart block, never a traceback.\"" | S603 62:12 + 398:14 + 406:13 "`subprocess` call: check for execution of untrusted input" | D403 283:5 "First word of the docstring should be capitalized: `wilson` -> `Wilson`" | D403 348:5 "First word of the docstring should be capitalized: `chisquare` -> `Chisquare`" | D403 357:5 "First word of the docstring should be capitalized: `shuffle` -> `Shuffle`" | D403 380:5 "First word of the docstring should be capitalized: `exp` -> `Exp`" | S311 359:5 "Standard pseudo-random generators are not suitable for cryptographic purposes" | COM812 361:103 "Trailing comma missing".
ENGINE .opencode/scripts/calculate.py sits OUTSIDE make lint's surface (src/ tests/) — no other finding nameable from this seat's instruments (honest bound); its standing state = the landed S311 row; the refusal surface = .githooks/pre-commit:42 "uv run ruff check $STAGED_PY" (core.hooksPath=.githooks; bypass PRIORITREE_HOOK_BYPASS=1) — the refusal's findings are the KAT's 13 (the KAT's own floor-row ruff fire printed the same 13 verbatim after its E902 path error).
pyproject per-file-ignores standing map (lines 45-200): "tests/**"=[S101,PLR2004]; src/prioritree/: scheduler=[ARG001], votes=[PLR0913,PLR0917], session=[N818,PLR0913,PLR0917], acceptance=[S311,ARG001], run_store=[PLR0913,PLR0917], cli=[T201,BLE001], budget_curve=[S311,ARG001], service_store=[PLR0913,PLR0917], service=[BLE001,E402,PLC0415,ARG001], web=[BLE001,S105,PLR0911,C901], mcp_server=[D205]; tests/: test_harness=[PLR0913,S603,S607], test_service_acceptance=[S603,S607], test_store_lock_face=[S603,S607], test_tally=[PLR0913], test_mcp_server_face=[PLR0913,PLR0917]; the S311 row's exact landed form (line 200): ".opencode/scripts/calculate.py" = ["S311"].
(2) PATH — the KAT's engine-path lines verbatim (56-57): "ROOT = Path(__file__).resolve().parents[1]" / "ENGINE = ROOT / \"scripts\" / \"calculate.py\"" — scripts/calculate.py ABSENT here (read: File not found); the engine lives at .opencode/scripts/calculate.py (1228 lines, confirmed by direct read). The adjustment IS forced, NOT APPLIED:
- ENGINE = ROOT / "scripts" / "calculate.py"
+ ENGINE = ROOT / ".opencode" / "scripts" / "calculate.py"
SECOND hikari-path reference beyond the one-line frame — line 407 (the floor row's pyright fire): [pyright, "--outputjson", "scripts/calculate.py", "tests/test_calculate_expansion_kat.py"] — the same unresolved path; both ride to the ruling (the 87 pinned rows' expected bytes untouched either way).
(3) KAT RUN — pytest tests/test_calculate_expansion_kat.py: "87 failed in 1.51s"; every row the same datum: "can't open file '/Users/marklosey/projects/prioritree/scripts/calculate.py': [Errno 2] No such file or directory" (assert 2 == 0); the floor row's variant: "E902 No such file or directory (os error 2) --> scripts/calculate.py:1:1". Full output: /Users/marklosey/.local/share/opencode/tool-output/tool_2156bdfb3001dZKn5a8viyKJn1 (2717 lines).
(4) FLOOR — the full suite: "87 failed, 336 passed in 30.67s" (423 collected = 336 + 87; the 336 pre-existing all pass; all 87 failures are the KAT's path failure).
NOT DONE (per the dispatch): no edits, no path cure, no per-file-ignores rows — every finding rides to the ruling first.
## Reported by keisan — 2026-11-26T01:21:24Z

keisan seat smoke — calculate's 30-op registry proven live, one fire per op (recommend/calc-ops step 7, order-bias-probe; FR-MEM-0037 gate 3: function proven by per-op runs, never by the map)
1. {"op": "add", "args": {"a": "2", "b": "3"}, "result": 5}
2. {"op": "subtract", "args": {"a": "10", "b": "4"}, "result": 6}
3. {"op": "multiply", "args": {"a": "6", "b": "7"}, "result": 42}
4. {"op": "divide", "args": {"a": "20", "b": "5"}, "result": 4}
5. {"op": "sum", "args": {"values": "[1, 2, 3, 4]"}, "result": 10}
6. {"op": "count", "args": {"values": "[\"a\", \"b\", \"c\"]"}, "result": 3}
7. {"op": "sqrt", "args": {"a": "16"}, "result": 4}
8. {"op": "power", "args": {"a": "2", "b": "10"}, "result": 1024}
9. {"op": "factorial", "args": {"n": "5"}, "result": 120}
10. {"op": "combination", "args": {"n": "22", "k": "12"}, "result": 646646}
11. {"op": "proportion", "args": {"part": "12", "whole": "22"}, "result": 0.5454545454545454}
12. {"op": "mean", "args": {"values": "[1, 2, 3, 4]"}, "result": 2.5}
13. {"op": "variance", "args": {"values": "[2, 4, 4, 4, 5, 5, 7, 9]", "form": "population"}, "result": 4}
14. {"op": "stddev", "args": {"values": "[2, 4, 4, 4, 5, 5, 7, 9]", "form": "sample"}, "result": 2.138089935299395}
15. {"op": "max", "args": {"values": "[1, 5, 3]"}, "result": 5}
16. {"op": "min", "args": {"values": "[1, 5, 3]"}, "result": 1}
17. {"op": "median", "args": {"values": "[1, 2, 3, 4]"}, "result": 2.5}
18. {"op": "quantile", "args": {"values": "[1, 2, 3, 4]", "p": "0.5"}, "result": 2.5}
19. {"op": "wilson", "args": {"k": "12", "n": "22", "z": "1.96"}, "result": [0.34659473289041554, 0.7307998556799515]}
20. {"op": "binom-test", "args": {"k": "12", "n": "22", "p": "0.5", "sided": "two"}, "result": 0.8318119049072266}
21. {"op": "normal-cdf", "args": {"x": "1.96"}, "result": 0.9750021048517796}
22. {"op": "normal-ppf", "args": {"q": "0.975"}, "result": 1.9599639845400534}
23. {"op": "log", "args": {"a": "2.718281828459045"}, "result": 1}
24. {"op": "exp", "args": {"a": "1"}, "result": 2.718281828459045}
25. {"op": "log-factorial", "args": {"n": "5"}, "result": 4.787491742782047}
26. {"op": "log-combination", "args": {"n": "22", "k": "12"}, "result": 13.379554283097821}
27. {"op": "log-beta", "args": {"a": "1", "b": "1"}, "result": 0}
28. {"op": "chisquare", "args": {"observed": "[5, 7]", "expected": "[6, 6]"}, "result": [0.3333333333333333, 1]}
29. {"op": "shuffle", "args": {"values": "[\"a\", \"b\", \"c\", \"d\"]", "seed": "42"}, "result": ["c", "b", "d", "a"]}
30. {"op": "derive-seed", "args": {"text": "smoke"}, "result": 11652036751135693796}
R1 domain refusal (factorial n='-1') REFUSED — Expected: a non-negative integer n (no negative factorial exists) / Found: n='-1' — the factorial of a negative count is undefined / Next-action: pass n >= 0
R2 taught seed refusal (shuffle seed='smoke') REFUSED in two blocks — block 1 (int contract): Expected: seed as an integer (as a string) — the int contract / Found: seed='smoke' — a non-integer string (whole counts only, never fractions) / Next-action: pass seed as an integer — whole counts only
R2 block 2 (the taught routing): Expected: seed as an integer (as a string) — the seed is REQUIRED: determinism demands the operand (the one place entropy could creep, foreclosed by construction; the same seed always yields the same permutation) / Found: seed='smoke' — not an integer / Next-action: pass an explicit integer seed — or derive one from any handle (a run_id, a sitting's name) via derive-seed, then pass it here
(side probe: the seedless shuffle refuses at argparse — "calculate.py shuffle: error: the following arguments are required: --seed" — the seed contract foreclosed at the CLI surface)
VERDICT: 30/30 live — the registry serves all 30 ops, every trace line the {"op","args","result"} one-liner quoted above, arithmetic spot-checked (sum=10, population variance=4, C(22,12)=646646); both refusals taught their ThreePart bodies, the taught seed refusal routing to derive-seed exactly as the delivery note said. No unexpected refusals, no missing ops.
## Reported by jikko — 2026-11-26T01:30:22Z

R11 — step 6 (the KAT's cures + the re-run; jikko, recommend/calc-ops, order-bias-probe, 2026-11-26). R1+R2+R3 landed in ONE patch (the KAT 9 hunks + pyproject 1 hunk; no findings at apply); the 87 pinned rows' answers byte-untouched (the file 419->420 lines).
READ-BACKS — :1 "# Copyright (C) 2026 Mark Losey. All rights reserved."; :58 "ENGINE = ROOT / \".opencode\" / \"scripts\" / \"calculate.py\""; :408 "[pyright, \"--outputjson\", \".opencode/scripts/calculate.py\", \"tests/test_calculate_expansion_kat.py\"],"; pyproject :211 "\"tests/test_calculate_expansion_kat.py\" = [\"S603\", \"S311\"]" (the comment :202-210 names both — S603 the tests/test_harness.py fixed-argv precedent, S311 the acceptance.py/budget_curve.py seeded seam); the docstring cures: D401 x3 "Fire the S603 fixed-argv subprocess…" / "Assert the positive row…" / "Assert the refusal row…", D403 x4 Wilson/Chisquare/Shuffle/Exp, COM812's trailing comma at the shuffle row — all outside the rows.
ACT 1 LINT: "uv run ruff check src/ tests/ / All checks passed!" — zero findings, the KAT's 13 cured.
ACT 2 KAT: "1 failed, 86 passed in 2.66s" — the headline row PASSED live (binom-test 12 22 0.5 two -> 0.8318119049072266, among the 86); the ONE failure is the floor row's ruff fire at the ENGINE: ".opencode/scripts/calculate.py ... Found 38 errors. [*] 21 fixable" — CPY001 1:1, EXE001 1:1, TC003 80:29, PYI041 105+112, D401 106+162+293+306+441, T201 130+157+794, D403 x17 (sqrt 352/power 378/factorial 416/combination 441/proportion 478/mean 513/variance 530/stddev 564/max 597/min 614/median 631/quantile 649/wilson 687/log 843/exp 867/chisquare 973/shuffle 1012), PLR2004 551+584+760, PLR0911 723, PIE808 764+776, PLR0915 1077, D103 1220 — the battery itself ZERO findings; the engine's bytes fork-free-untouched; the floor row's pyright leg unreached (the ruff assert fires first).
ACT 3 FLOOR: "1 failed, 422 passed in 32.66s" — 423 collected (336 + 87), the 336 pre-existing all pass; the one failure the same floor row.
THE GAP TO THE RULING: the ENGINE under this tree's select=ALL is NOT covered by its landed [\"S311\"] row — 38 findings live at the floor row's fire; the cure is the engine's per-file-ignores extension (the coordinator's ruling, never the bytes — the fork-free law held). NOT DONE: the typecheck act (not among this dispatch's three acts); no engine edit; nothing beyond R1+R2+R3.
## Reported by moho — 2026-11-26T01:32:26Z

# moho's confirmation walk — the calculate wrapper's 30-op surface, cold (step 9, recommend/calc-ops)

PATHS: repo /Users/marklosey/projects/prioritree; store .plans/ideation/2026-11-24-order-bias-probe; surface = calculate (help + 5 cold fires: wilson, binom-test, combination, factorial refusal, factorial cure).

(1) THE HELP SURFACE COLD — fired operation="help": it teaches ALL 30 ops, each with ITS OWN per-op param block (name, semantics, constraint, example call) — the per-op correctness the delivery note promised IS there.
Cold-learned: the n meanings per op — wilson n = "the trial count (an integer >= 1)", binom-test n = "the trial count (an integer >= 0)", combination n = "the population count" — the zod-block's cross-op n collision is dissolved per-op; binom-test's sided = "the sidedness: two or one"; variance/stddev form = "population or sample".
Stays opaque: factorial's n taught only as "the count (an integer, as a string)" — no non-negative bound (log-factorial's parallel param DOES say "non-negative"); and the help's closing line is domain-foreign noise: "To list every make target, use the `help` tool or run `make help`."

(2) THREE COLD USES — all three landed the right form FIRST TRY; zero retries:
- wilson (the collision case): {"op": "wilson", "args": {"k": "7", "n": "10", "z": "1.96"}, "result": [0.39677321997956516, 0.892210712513788]} — the cold form taught the RIGHT n straight from wilson's own block; no stumble.
- binom-test: {"op": "binom-test", "args": {"k": "7", "n": "10", "p": "0.5", "sided": "two"}, "result": 0.34375} — the sided enum was discoverable; no stumble.
- combination: {"op": "combination", "args": {"n": "5", "k": "2"}, "result": 10} — no stumble.

(3) THE COLD REFUSAL — factorial n="-3" (a negative n; the help's "an integer" gave no bound, so the trip was untelegraphed):
"REFUSED
Expected: a non-negative integer n (no negative factorial exists)
Found: n='-3' — the factorial of a negative count is undefined
Next-action: pass n >= 0"
ThreePart teaching present, quoted verbatim; the next-action cured the cold seat's error in ONE step: {"op": "factorial", "args": {"n": "3"}, "result": 6}.

(4) THE VERDICT: the surface is walkable without help.
- Zero retries across the three cold uses: the n-collision taught per-op (wilson landed cold), the sided enum discoverable, no form guessing.
- The refusal teaches RIGHT — ThreePart grammar, and the next-action cures in one step.
- Named blemishes, neither FR-MEM-0515-class: (a) factorial's non-negative bound lives only in the refusal, not the help — the cold seat learns it by tripping, not by reading; (b) the help's make-target closing line is domain-foreign noise.
- FR-MEM-0515's question — "can a cold seat use the surface without help?" — answered YES on this walk's evidence.
## Reported by jikko — 2026-11-26T01:38:35Z

R11 — step 8 (the engine's per-file rulings; jikko, recommend/calc-ops, order-bias-probe, 2026-11-26). R4 LANDED at pyproject.toml:209 — ".opencode/scripts/calculate.py" = ["CPY001", "EXE001", "D401", "D403", "D103", "T201", "PYI041", "PLR2004", "PLR0911", "PLR0915", "PIE808", "TC003", "S311"] — the standing S311-only row replaced, the comment (:192-208) naming every code with its reason (the fork-free cargo: the header [CPY001], the shebang [EXE001], hikari's docstring conventions [D401/D403/D103], hikari's annotation style [PYI041/TC003/PIE808], the numeric constants [PLR2004]; the trace-line output IS prints [T201]; the 30-case argparse dispatch [PLR0911/PLR0915]; the seeded seam [S311, standing]) — never blanket, no code unnamed.
SET CONFIRMED at the step-6 report's verbatim fire: the 38 findings (1+1+1+2+5+3+17+3+1+2+1+1 = 38) map exactly to the row's 12 firing codes + S311 standing — no code unfired, none missing (no shell act at this seat: the report the census, the floor row the live re-fire).
ACT 1 — THE KAT'S RE-RUN: "87 passed in 3.31s" — 87/87 (the floor row's ruff fire now passing over the ruled engine).
ACT 2 — THE FLOOR: "423 passed in 33.52s" — the full suite, all passing.
ACT 3 — THE LINT ACT: ruff check .opencode/scripts/calculate.py tests/test_calculate_expansion_kat.py — ZERO findings, proven at the floor row fired alone ("1 passed in 0.48s" — the battery's own lane, the no-shell law: the row's subprocess IS the exact explicit argv, returncode 0 asserted; the row's pyright leg green with it).
NOT DONE: no engine byte touched (the fork-free law held); no make-lint/typecheck acts (not among the dispatch's three).
