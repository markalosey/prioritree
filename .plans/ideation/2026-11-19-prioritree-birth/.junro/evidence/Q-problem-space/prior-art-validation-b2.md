# Prior-art validation, leg B2 (web) — rating-model cluster B5–B7

- Packet: scope/prior-art-validate-b2 · Question: Q-problem-space · Route: prioritree-birth
- Seat: tansa (探査), read-only — content returned in-packet; landed by shinko via patch, 2026-11-20
- Date: 2026-11-19 · Status: web tools functional (keyed smoke test GREEN 2026-11-20; this packet's searches/extracts live-fired)
- Predecessor: packet scope/prior-art — the rating-model claims were labeled "corpus-knowledge, not web-verified"; this leg web-validates them
- Scope discipline: the three claims below only. No literature expansion; no contradicting results surfaced.
- Tally: 3 CONFIRMED / 0 CORRECTED / 0 UNVERIFIABLE / 3 precision riders recorded

## Verdict table

| Claim | Verdict | Anchor URLs |
|---|---|---|
| B5 — Elo (1978), Arco: incremental update R' = R + K(S−E), order-dependent | CONFIRMED | gwern book scan; archive.org/details/ratingofchesspla00unse; en.wikipedia.org/wiki/Elo_rating_system; arxiv.org/html/2104.05422v1 |
| B6 — Glickman (1999), JRSS-C 48(3):377–394: Glicko adds per-player rating deviation | CONFIRMED | glicko.net/research/glicko.pdf; glicko.net/glicko/glicko.pdf; papers.neurips.cc/paper/3079 |
| B7 — Herbrich/Minka/Graepel (2006), NIPS 19: Bayesian factor-graph; converges on far fewer games than Elo | CONFIRMED | proceedings.neurips.cc/paper/2006/hash/f44ee263952e65b3610b8ba51229d1f9-Abstract.html; papers.neurips.cc/paper/3079-trueskilltm-a-bayesian-skill-rating-system.pdf |

## B5 — Elo (1978): incremental update, order-dependent — CONFIRMED

Citation fields verified against the book scan (gwern, scan of the 1986 second edition of the 1978 first): "ARCO PUBLISHING. INC. New York … Copyright © 1978 by Arpad E. Elo. First published 1978." §1.6 "The Current Rating Formula": "Rn = Ro + K(W − We)" — the claim's S/E notation is the standard modern rendering of the same equation (rider, not correction).

Order-dependence verified: (a) mechanically — the expectancy E is computed from the player's current rating, so consecutive updates do not commute; corroborated at arxiv.org/html/2104.05422v1 ("the issue of deciding which order to compute the rating updates in"); (b) numerically, in-pack via the calculate tool (7 calls): the same two games (beat 1200, lose to 1800; R0=1500, K=40, logistic expectancy) in two orders yield finals 1499.81984 vs 1500.18016 — a difference of 0.36032 rating points on the identical multiset.

Granularity rider (sharpens the purity ruling's batch-vs-sequential contrast; not a correction): per-game application is fully order-dependent (demonstrated); administrative practice batches games per rating period with pre-period expectancies, making a within-period reorder a no-op — but period-batched Elo is still not a function of the whole-history multiset (the periodization matters), and the incremental formula itself is the sequential mechanism the claim names.

## B6 — Glickman (1999): Glicko's per-player rating deviation — CONFIRMED

Citation fields verified from the paper's own running header: "Appl. Statist. (1999) 48, Part 3, pp. 377–394", © 1999 Royal Statistical Society (Applied Statistics = JRSS-C) — glicko.net/research/glicko.pdf; glicko.net/research.html ("This paper describes the technical details of the 'Glicko' rating system").

Load-bearing claim verified: "The Glicko system therefore extends the Elo system by computing not only a rating … but also a 'ratings deviation' (RD) … which measures the uncertainty in a rating (high RD's correspond to unreliable ratings)" — glicko.net/glicko/glicko.pdf. TrueSkill corroborates: Glicko "introduces the idea of modeling the belief about a player's skill as a Gaussian belief distribution characterized by a mean μ and a variance σ²" — papers.neurips.cc/paper/3079.

Provenance rider (not a correction): Glickman dates the system's creation to 1995; the 1999 JRSS-C paper is the peer-reviewed technical account, and citing it for Glicko is author-sanctioned.

## B7 — Herbrich/Minka/Graepel (2006): TrueSkill — CONFIRMED

Citation fields verified: NeurIPS proceedings page — "TrueSkill™: A Bayesian Skill Rating System — Ralf Herbrich, Tom Minka, Thore Graepel — Advances in Neural Information Processing Systems 19 (NIPS 2006)"; Wikipedia: MIT Press, pp. 569–576.

Load-bearing claims verified: (a) Bayesian factor-graph — abstract: "Inference is performed by approximate message passing on a factor graph representation of the model"; §2 "Factor Graphs for Ranking"; conclusion: "TrueSkill is a globally deployed Bayesian skill rating algorithm based on approximate message passing in factor graphs." (b) convergence — abstract: "experimental evidence on the increased accuracy and convergence speed of the system compared to Elo"; §4.1: "Elo only slowly converges to the target skill… the observed convergence for these two players is ≈10 games" (near the ≈5-game information-theoretic limit). Wording rider: "far fewer games" is a fair strong paraphrase of the paper's convergence wording.

## Contradiction sweep

No web result directly contradicting any of the three claims surfaced. One adjacent third-party inaccuracy observed in-scope (uscfsales.com claims the book appeared in 1960 — 1960 is the USCF adoption of the system; the book is 1978); noted only because it surfaced.

## Bottom line

SAFE TO LAND AS-IS — all three verdicts CONFIRMED; every citation field checks against primary or author-controlled sources and every load-bearing claim holds (B5's order-dependence demonstrated numerically in-pack). The three riders sharpen the record; none overturns a verdict.

Tool friction encountered and filed: the grep tool could not search the saved web-extract of the Elo book scan (records exceed ripgrep's 65536-byte cap; one invocation returned matches from other files instead of refusing) — filed as FR-MEM-0009 by tansa (tool-usage / interface-cost, medium, open); nothing from the misleading grep output entered this record.
