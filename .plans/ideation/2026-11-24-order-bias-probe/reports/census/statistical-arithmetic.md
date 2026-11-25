<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/statistical-arithmetic

**Route:** order-bias-probe (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-25T03:42:43Z |
| 2 | report | keisan | 2026-11-25T03:54:20Z |
## Reported by keisan — 2026-11-25T03:54:20Z

# keisan (計算) — STATISTICAL ARITHMETIC: the order-bias probe's numbers

Seat: keisan · Packet: census/statistical-arithmetic · Route: order-bias-probe · Date: 2026-11-24. Every number below shows its work; the calculate tool verified every sum, product, and quotient (cited inline); the square roots verified by their squares (the tool's six ops carry no sqrt — 0.115128² = 0.013254 ✓).

## 0. THE CORPUS'S REAL N (grep-verified at my own read — the arithmetic's ground)

The runs on disk (.prioritree/runs/): 7 runs, 5 voting. RUN-0002: 10 votes (human, "Mark Losey"); RUN-0003: 3 (human, "mark"); RUN-0005: 6 (llm, "moho"); RUN-0006: 1 (llm, "moho"); RUN-0007: 2 (llm "moho" + human "the-stranger"). RUN-0001/0004: manifests only.

- TOTAL: 22 votes — prefer-a 12, prefer-b 10, tie 0 (grep counts: 12 + 10 = 22 ✓). All supersedes null (no corrections).
- CLASSES: human 14 (7 prefer-a, 7 prefer-b); llm 8 (5 prefer-a, 3 prefer-b). All 8 llm votes from ONE seat (moho), 2 of them self-authored R4 probes (RUN-0006/0007) — a diagnosis-seat confound, named not smoothed.
- PRESENTATION: all 22 stored pairs id-sorted (verified pair by pair) = the schedule's canonical form = the presented order at birth → prefer-a IS the first-position win. The presentation-position variable has ZERO variation in the corpus (22/22 id-first presentations): position capture and id-order merit are PERFECTLY CONFOUNDED, and NO pair exists at both orders — Wang's flips-on-swap datum is retrospectively ABSENT, not merely underpowered.

## 1. THE RETROSPECTIVE DATUM'S FORMS (the descriptive statistics + the exact test at the real N)

1.1 The position-preference rate (prefer-a's share among non-tie votes): 12/22 = 0.5455 (54.5%). Human slice: 7/14 = 0.5000. LLM slice: 5/8 = 0.6250.

1.2 The exact binomial test at N=22 (H0: first-position share w = 0.5), observed 12: one-sided tail P(X≥12) = [Σ C(22,k), k=12..22]/2^22 = 1744436/4194304 = 0.41591 → two-sided p = 2 × 0.41591 = 0.8318. THE DATUM SITS AT THE NULL'S HEART (12 is one vote above the mean 11).

1.3 The test's rejection bar at α=0.05 (exact two-sided): X=16 → p = 2 × 110056/4194304 = 0.05248 (misses); X=17 → p = 2 × 35443/4194304 = 0.01690 (rejects). The corpus rejects ONLY at ≥17/22 = 77.3% first-position share (or ≤5/22).

1.4 The 95% Wilson CI at 12/22: inner term 0.5455×0.4545/22 + 1.96²/(4×22²) = 0.011270 + 0.001984 = 0.013254; √ = 0.115128 (verified by its square); half-width = 1.96×0.115128/1.174618 = 0.192112; center = (0.54545+0.087309)/1.174618 = 0.538721 → CI = [0.3466, 0.7308]. WIDTH ±19.2 points (38.4 whole).

1.5 THE POWER LADDER at N=22 (P(reject | w), exact test, terms summed and verified): w=0.60 → 0.072 (7%); w=0.65 → 0.163 (16%); w=0.70 → 0.314 (31%); w=0.75 → 0.517 (52%); w=0.80 → 0.733 (73%); w=0.825 → 0.826 (83%). MDE at 80% power ≈ w = 0.82: the corpus is 80%-powered ONLY for a ≥32-point position capture.

1.6 THE PER-CLASS SLICES' OWN POWER: human N=14 (bar 12/14 = 85.7%): power at w=0.75 = 0.281, at w=0.825 = 0.546, MDE₈₀ ≈ 0.88. LLM N=8 (bar 8/8 = 100% — nothing less rejects): power at 0.75 = 0.75⁸ = 0.100, at 0.825 = 0.825⁸ = 0.215 (verified 0.463251² = 0.21460), MDE₈₀ = 0.8^(1/8) ≈ 0.97. NO SLICE ALONE CAN CATCH EVEN THE GROSS CLASS; only the pooled N=22 does.

1.7 THE TIE RATE'S SEPARATE DATUM (its own weight): 0/22 = 0.000; the 95% upper bound (the rule of three) = 3/22 = 0.136 (13.6%). No tie evidence exists; ties excluded from the position test exclude nothing here (the non-tie N IS 22).

1.8 THE HONEST STATEMENT OF THE RETROSPECTIVE NULL: the corpus's datum 54.5% [34.7%, 73.1%] EXCLUDES (at 95%) any first-position share above 0.731 — the ONE bound it carries: if the tree's judges captured position at the verified literature-gross rate (0.825), the corpus would likely have shown it (power 83%). But the band [0.500, 0.731] — up to a 23-point position preference — is UNMEASURED, and the id-sort confound means the share is position capture + id-order merit JOINTLY. The retrospective form is a screen over the gross class, never a causal claim.

## 2. THE PROSPECTIVE EXPERIMENT'S PRICE (the both-orders causal form)

2.1 WANG ET AL. VERIFIED (the birth store's claims lane, prior-art-validation-b1.md B3 — CONFIRMED): "the quality ranking of candidate responses can be easily hacked by simply altering their order of appearance... Vicuna-13B could beat ChatGPT on 66 over 80 tested queries with ChatGPT as an evaluator" → THE VERIFIED GROSS EFFECT: a first-position win rate of 66/80 = 0.825 by order manipulation alone; the paper's own cure: Balanced Position Calibration — aggregating across both orders (= both-orders averaging). Fresh sources: no web tool rides this seat's pack — the design stage's claims lane owns any fresh verdict; this arithmetic prices the LADDER.

2.2 THE DESIGN: each experimental pair presented BOTH orders (within-pair flips); at the corroboration floor (≥1 human AND ≥1 llm per pair) × 2 orders = 4 votes per pair minimum. The per-pair datum: consistent / first-capture / second-capture; the flip rate φ, and among flips the first-capture share θ. Position-override model: w = φθ + (1−φ)/2 — the both-orders design cancels content by construction (the marginal prefer-first share is independent of true preferences).

2.3 THE DEMANDED SAMPLE (two-sided sign test among flips, α=0.05, 80% power; constant (1.96+0.8416)² = 7.849; m = 7.849·θ(1−θ)/(θ−0.5)²):
- GROSS (Wang's verified class: φ=0.65, θ=1.0 → w=0.825): ≥6 one-way discordants (exact p = 2·0.5⁶ = 0.031); P(Bin(n,0.65)≥6) ≥ 0.80 at n ≈ 11 PAIRS → 44 VOTES at the floor (11×4 = 44 ✓).
- HALF (φ=0.5, θ=0.75 → w=0.625): m = 7.849×3 = 23.55 → 24 discordants → ~54 pairs → 216 VOTES (54×4 = 216 ✓).
- MODEST (φ=0.4, θ=0.65 → w=0.59): m = 7.849×10.111 = 79.4 → 80 → ~214 pairs → 856 VOTES (214×4 = 856 ✓).
- NULL-ISH (φ=0.25, θ=0.55): m = 7.849×99 = 777.0 → 778 → ~3,150 pairs → 12,600 VOTES (3150×4 = 12,600 ✓) — beyond any bench.

2.4 THE HONEST-NULL EQUIVALENCE BOUND: to assert |θ−0.5| < 0.10 (the null carrying a ±10-point bound) at 95%: m = 1.96²×0.25/0.01 = 3.8416×0.25/0.01 = 96.04 → 97 discordants → ~242 pairs at φ=0.4 to ~388 at φ=0.25 → ~970-1,552 VOTES.

2.5 THE RUNS IT WOULD TAKE: the quorum structure (quorum=1 per the manifests) × the floor's both-class demand × both orders = 4 votes per pair; each class accumulates its own flip units on the SAME pairs — the floor's structure gives the per-class slices for free (no extra votes for slicing; the pooled test carries 2× the units).

2.6 THE BENCH'S OWN HANDS (the free-tier law, $0): the tree's roster ≈ 13 llm seats (parallel voters; observed pace RUN-0005: 6 votes in 47.1 s ≈ 7.9 s/vote) + the human hand (observed pace RUN-0002: 10 votes in 17.7 s ≈ 1.77 s/vote; the prior-art's conservative 10 s/judgment). THE HUMAN LANE IS THE BOTTLENECK: gross = 22 human votes (about a minute); half = 108 (one sitting); modest = 428 (2-4 sittings — beyond comfort); null-ish = 6,300 human votes (impossible at $0). REALISTIC BENCH CEILING: ~50-100 pairs per sitting → the gross and half classes are REACHABLE at $0; the modest and null-ish classes are NOT.

2.7 ITEMS: 11 pairs ← 6 items (6×5/2 = 15 max); 54 ← 11 items (55); 214 ← 21 items (210) — all far inside the >100-item fence; the experiment never widens the ruled scope.

## 3. THE THRESHOLD'S RULING INPUTS (the design gate rules it; this prices the options)

3.1 THE SIGNIFICANCE CONSTANTS (80% power, two-sided): α=0.05 → (1.96+0.8416)² = 7.849 (the baseline above); α=0.01 → (2.5758+0.8416)² = 11.679 → +48.8% N at every effect; Bonferroni across 3 tests (pooled + 2 class slices) → (2.394+0.8416)² = 10.469 → +33.4% N per test.

3.2 THE BAYES-FACTOR FORM (uniform prior on θ; BF₁₀ = Beta(k+1, m−k+1)·2^m): at the α=0.05 design's 80%-power point (m=24, k=18): BF₁₀ = [720/2422728000]/2⁻²⁴ = 2.9719e-7/5.96046e-8 = 4.99 — MODERATE only; the same design at k=19: BF₁₀ = [120/127512000]/5.96046e-8 = 15.79 — strong. THE STRONG-BF DISCIPLINE PRICES ≈ +50% N over α=0.05 at the same effect.

3.3 THE MULTIPLE-COMPARISONS HONEST FORM: 3 confirmatory tests demand Bonferroni (+33.4% each); the cheaper honest form — ONE pre-registered primary (the pooled flip asymmetry at α=0.05) + the class slices EXPLORATORY (at the corpus's own N the slices are powerless anyway: §1.6).

3.4 THE NULL'S WEIGHT AT THIS POWER: a null at N=22 bounds NOTHING below 0.731 (§1.8). A null at the bench-feasible designs bounds |θ−0.5| only within ~±0.25 (gross design, m≈6-8 discordants) to ~±0.20 (half design, m≈24: half-width ≈ 1.96·√(0.25/24) = 0.20). The equivalence form (±0.10) costs ~97 discordants — 4× the half design. THE DESIGN GATE MUST RULE WHICH BOUND THE NULL CARRIES: "no gross hack-class bias" (cheap) vs "the flip asymmetry is under ±10 points" (~1,000-1,550 votes).

## 4. THE CURE'S PRICES (named not pinned — the datum rules; each priced at $0 and at the cost the datum would justify)

4.1 BOTH-ORDERS AVERAGING (Wang's own cure — "Balanced Position Calibration"): THE STRUCTURAL FACT — the CURRENT tally already averages implicitly: a flip pair nets one win to each item (a 0.5-0.5), a consistent pair nets 2-0 — the win-rate count IS the both-orders average; NO tally change (the purity and R12's byte-identity untouched). THE REAL PRICE: (a) the write path's presented→canonical mapping (votes.py's cast_vote seam: the vote surface gains the presented pair or a presentation flag, mapped onto the canonical Pair at write) + (b) THE SCHEMA'S PRESENTATION DATUM (a presentation_order field on the vote record — non-optional per the prior-art's own field schema; the corpus's records carry none — the datum must be carried to be measurable) + (c) THE VOLUME: 2× at every sitting (RUN-0002's 10-vote sitting becomes 20; at n=100 the full both-orders both-class sweep = 100×99×2 = 19,800 votes). At $0 the bench's hands absorb it at small n; the cost the datum justifies: a measured asymmetric flip datum (φ>0, θ>0.5 — Wang's verified class justifies the double outright; a null at the honest bound does NOT — the deferral stands).

4.2 THE SHUFFLE MODE (the scheduler's seed already carried): the seam EXISTS — schedule_pairs(ids, seed=None) (scheduler.py:52, the reserved parameter) + derive_seed(run_id) (blake2b, :87). THE ADDITION'S PRICE: a seeded per-pair presentation draw (the seed consumed — the widening additive, never rework) + the same write-path mapping and schema field as 4.1. THE VOLUME PRICE: $0 — NO extra votes. THE HONEST LIMIT: the shuffle debiases IN EXPECTATION (E[first-position capture] = 0.5 by symmetry) — it converts systematic bias into run-level noise; it does NOT cancel per-pair (a small run's realized orders are unbalanced with probability 1). The purity held: the manifest carries the seed, the schedule stays a pure function of (ids, seed) — byte-identical replays preserved. Justified by: ANY measured position sensitivity — the cheapest cure (no volume, one seam, one field).

4.3 THE EARLY-STOP RULES (the adaptive form — the >100-item fence held): the price: a scheduler-side STOP CONSUMER over the tally's coverage datum (pair_counts / the running flip count — the stop is never a tally input; the tally's purity preserved) + THE SEQUENTIAL DISCIPLINE: repeated looks inflate α — the honest forms a pre-registered boundary (Pocock / O'Brien-Fleming) or the SPRT; the >100-item fence held (the stop rule operates WITHIN the ruled small-n scope, never widening it). THE VALUE: at gross effects the sequential form stops at ~6-10 discordants vs the fixed design's 24 — a 30-50% vote saving; at the null it confirms the bound cheaper. Justified by: any measured φ (the boundary's information form) or the budget-curve precedent's own efficiency demand.

## 5. THE HEADLINE FOR THE DESIGN GATE (the arithmetic whole)

- THE RETROSPECTIVE: the corpus's first-position share 12/22 = 54.5% [34.7, 73.1], exact p = 0.832 — null-ish; 80%-powered ONLY at w ≥ 0.82; the class slices (N=14, N=8) are powerless even at the gross class (55%/21%); the ONE bound carried: the verified Wang-gross rate (0.825) is excluded in the corpus's own content; the 23-point band below it is blind; the id-sort confound and the ZERO both-order units mean the retrospective form can never support the causal claim.
- THE PROSPECTIVE: the both-orders causal design at the corroboration floor (4 votes/pair) prices at 44 votes (Wang-gross), 216 (half), 856 (modest), 12,600 (null-ish); the honest ±10-point null costs ~97 discordants (~970-1,552 votes); the bench's own hands (≈13 llm seats + 1 human, $0) afford the gross and half classes, NOT the modest/null.
- THE THRESHOLD: 0.05 = 7.849; 0.01 = +48.8%; Bonferroni-3 = +33.4%; strong-BF ≈ +50%; the honest pre-registration: one primary + exploratory slices; the null's weight must be ruled as a BOUND (which bound the design can afford).
- THE CURES: both-orders averaging = write-path mapping + presentation field + 2× volume (the tally untouched — the count already averages); the shuffle = the carried seed seam + the same field, $0 volume, expectation-level debiasing; the early-stop = a scheduler stop consumer + a pre-registered sequential boundary, the fence held.
