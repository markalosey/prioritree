# Prior-art validation — B3 (noisy-sorting / active-ranking cluster)

- Packet: scope/prior-art-validate-b3
- Question: Q-problem-space
- Route: prioritree-birth
- Seat: tansa (探査, discover)
- Date: 2026-11-20
- Smoke test: GREEN (2026-11-20); re-fire gate passed
- Scope: web-validate claims B8–B11 of the prior-art return (packet scope/prior-art). Small surface honored — no new literature swept; no contradictions beyond the corrections named below.
- Landed: shinko via patch, 2026-11-20; read-back verified.

## Verdict summary

| Claim | Verdict | Correction |
|---|---|---|
| B8 Feige et al. 1994 | CORRECTED | Title: "Computing with Noisy Information" (not "Noisy Queries"); load-bearing claim CONFIRMED |
| B9 Braverman & Mossel "Noisy Sorting" | CORRECTED | Title: "Noisy Sorting Without Resampling"; venue: SODA 2008, pp. 268–276 (arXiv:0707.1051); load-bearing claim CONFIRMED |
| B10 Jamieson & Nowak 2011 | CORRECTED | Venue: NIPS 2011 (Adv. NeurIPS 24, pp. 2240–2248), not ICML 2011; claim recharacterized (full ranking under embedding assumption, not top-item) |
| B11 Yue et al. 2012 | CORRECTED | Journal: J. Comput. Syst. Sci. 78(5):1538–1556 (2012), not IEEE TPAMI 34(1):51–61; claim + ICML 2009 priority CONFIRMED |

## B8 — Feige, Raghavan, Peleg & Upfal (1994)

Citation fields verified against the published paper (ETH-hosted scan of the SIAM original): "COMPUTING WITH NOISY INFORMATION — URIEL FEIGE, PRABHAKAR RAGHAVAN, DAVID PELEG AND ELI UPFAL. SIAM J. COMPUT. Vol. 23, No. 5, pp. 1001-1018, October 1994." DOI: 10.1137/S0097539791195877. CORRECTION: the prior-art return's title "Computing with Noisy Queries" is wrong; the paper is "Computing with Noisy Information."

Load-bearing claim CONFIRMED from the paper text: "it is possible to repeat each comparison of the fault-free decision tree O(log(N/Q)) times and obtain, by majority voting, a guess for the true result of the comparison that is wrong with probability at most Q/N"; "any decision tree that has depth d in the absence of noise can be used to devise a noisy one of depth O(d log(d/Q))"; Theorem 3.2 (upper): noisy SORTING in O(N log(N/Q)) comparisons; Theorem 3.5 (lower): Ω(N log(N/Q)) — tight.

URLs: epubs.siam.org/doi/10.1137/S0097539791195877 · cadmo.ethz.ch/education/lectures/HS18/SAADS/papers/computing_noisy_information.pdf · weizmann.elsevierpure.com/en/publications/computing-with-noisy-information

## B9 — Braverman & Mossel, "Noisy Sorting" (venue resolved)

CORRECTION (title): full title is "Noisy Sorting Without Resampling" (arXiv:0707.1051, submitted July 2007). CORRECTION (venue/year): SODA 2008 — "Mark Braverman and Elchanan Mossel. Noisy sorting without resampling. In 19th ACM-SIAM Symposium on Discrete Algorithms (SODA), pages 268-276, 2008."

Load-bearing claim CONFIRMED in substance — model (per the MIT 6.854 report describing the paper): "every comparison has a probability of failure δ. The difference is that in this case by repeating a comparison we don't get a better comparator because the uncertainty comes from the input and therefore the comparisons are not independent" — persistent/recurrent errors, each pair compared at most once ("no resampling"). Result: O(n log n) comparisons w.h.p.; expected displacement O(1); Pr[d(a_i) ≥ c log n] ≤ Õ(n^−c) — every element within O(log n) of its true position w.h.p. ("up to a few misplaced items" is a fair informal gloss of this displacement guarantee; recovery is near-exact, not exact.)

URLs: arxiv.org/abs/0707.1051 · drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SEA.2023.8 · courses.csail.mit.edu/6.854/20/sample-projects/A/noisy%20sorting.pdf

## B10 — Jamieson & Nowak (2011), "Active Ranking using Pairwise Comparisons"

CORRECTION (venue): published at NIPS 2011 (Advances in Neural Information Processing Systems 24, pp. 2240–2248), NOT ICML 2011 — confirmed by the official NeurIPS proceedings page, Jamieson's own publications page, and independent citations.

Load-bearing claim CORRECTED in characterization; the quantitative contrast holds: under the assumption that objects embed in R^d with rankings reflecting distances from a common reference point, "an algorithm that can identify a randomly selected ranking using just slightly more than d log n adaptively selected pairwise comparisons, on average. If instead the comparisons are chosen at random, then almost all pairwise comparisons must be made in order to identify any ranking." Adaptive O(d log n) vs ~n(n−1)/2 random/round-robin — "exponentially fewer" confirmed. But the paper's CORE result is full-ranking identification under the embedding assumption — not "the top item"; no top-item-only guarantee appears in this paper.

URLs: papers.nips.cc/paper/4427-active-ranking-using-pairwise-comparisons · homes.cs.washington.edu/~jamieson/publications.html · proceedings.mlr.press/v28/wauthier13.pdf

## B11 — Yue, Broder, Kleinberg & Joachims, "The K-armed Dueling Bandits Problem"

CORRECTION (journal/volume/pages): "IEEE TPAMI 34(1):51–61" is wrong in every field. The journal version is Journal of Computer and System Sciences, 78(5):1538–1556, 2012, doi:10.1016/j.jcss.2011.12.028 (per Wikipedia's multi-armed bandit bibliography; identically in Komiyama et al. ICML 2015 references and the paper PDF itself). Conference version: COLT 2009.

Load-bearing claim substantively CONFIRMED, with one nuance: the paper introduces the K-armed dueling bandits problem — sequential, adaptive scheduling of noisy pairwise comparisons ("duels") among K alternatives to converge on the best arm (Interleave Filtering and RUCB; regret defined relative to the Condorcet winner) — the foundational theory behind pair scheduling. Nuance: the formal objective is cumulative dueling-regret minimization over a time horizon (the horizon acts as the implicit budget), not pure budget-constrained best-arm identification; explicit budgeted BAI formulations appear in later work (e.g., Yue & Joachims, "Beat the Mean Bandit," ICML 2011).

ICML 2009 priority CONFIRMED: Yue, Y. & Joachims, T., "Interactively Optimizing Information Retrieval Systems as a Dueling Bandits Problem," Proceedings of the 26th ICML (Montreal), 2009, pp. 151–159 — listed on the official ICML 2009 abstracts page (paper ID 346); the COLT 2009 K-armed paper cites it as simultaneous priority work: "Yue and Joachims [YJ09] simultaneously studied a continuous version of the Dueling Bandits Problem."

URLs: en.wikipedia.org/wiki/Multi-armed_bandit · josephcclin.github.io/paper/duelingBandits.pdf · proceedings.mlr.press/v40/Komiyama15.pdf · cs.cornell.edu/~tj/publications/yue_etal_09a.pdf · cs.cornell.edu/~tj/publications/yue_joachims_09a.pdf · icml.cc/Conferences/2009/abstracts.html · proceedings.mlr.press/v32/ailon14.pdf

## Bottom line

SAFE TO LAND WITH NAMED CORRECTIONS — not as-is. Every load-bearing technical claim in this cluster is web-verified and sound in substance. The corrections are citation-field fixes (B8 title; B9 title + venue; B10 venue) plus one claim-characterization fix (B10: full-ranking identification under the embedding assumption, not top-item identification) and one nuance (B11: regret-minimization framing vs. explicit budgeted BAI). No load-bearing claim fails; no contradicting literature surfaced.

Provenance: 6 web search calls + 4 extract calls (2026-11-20), executed by tansa; primary-source scans (Feige et al. full text; NeurIPS proceedings page; Cornell paper PDFs) used wherever fetchable. Landed by shinko via patch, 2026-11-20.
