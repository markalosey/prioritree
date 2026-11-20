# Prior-art validation B1 — LLM-as-judge claims (web verification)

- Packet: scope/prior-art-validate-b1 · Question: Q-problem-space · Route: prioritree-birth
- Seat: tansa (探査, discover) · Date: 2026-11-19
- Status: web tools functional; keyed smoke test GREEN (2026-11-20); re-fire gate passed
- Method: web search + web extract of the four arXiv abstract pages, full-text arXiv HTML of 2306.05685 (v4) and 2403.04132 (v1), the NeurIPS 2023 D&B virtual-event page, and PMLR v235 (ICML 2024). The 2403.04132v1 extract exceeded the response window; the tool's saved full output was grepped to recover the methods text. No literature beyond the four claims was opened; one adjacent surfaced result touching a claimed wording is reported in-line under B2 without broadening.
- Landed: shinko via patch, 2026-11-20; read-back verified.

## Verdict table

| # | Claim | Verdict | Named correction |
|---|---|---|---|
| B1 | Zheng et al. 2023, arXiv:2306.05685 (NeurIPS 2023 D&B): GPT-4 judge ~80%+ agreement, comparable-to-exceeding inter-human (~66%); pairwise substantially beats single-answer grading | CORRECTED | Citation fields all hold (incl. NeurIPS 2023 D&B). (i) Inter-human agreement like-for-like is 81% (non-tie; GPT-4 85%, "even higher than the agreement among humans") — "~66%" is the with-ties setup (human–human 63–67%), under which GPT-4 also scores ~66%; do not mix setups. (ii) Pairwise is equal-to-slightly-better, not "substantially beats" (85 vs 85 non-tie turn 1; 66 vs 60/59 with-ties; 87 vs 85 Arena); paper: single-answer "matches... very well" and is "more scalable." |
| B2 | Chiang et al. 2024, arXiv:2403.04132 (ICML 2024): millions of pairwise votes → BT/Elo → live widely trusted leaderboard | CORRECTED | Citation fields hold (PMLR v235, pp. 8359–8388). BT/Elo confirmed ("Bradley & Terry (1952)... Elo score (Elo, 1967)"). "Widely trusted" confirmed (paper: "one of the most referenced LLM leaderboards, widely cited by leading LLM developers and companies"). Correction: paper snapshot = 240K+ votes (~90K users, Jan 2024), not millions; millions = platform's current state (ICML 2025: "millions of crowdsourced votes," "around 1.7 million historical votes"). |
| B3 | Wang et al. 2023, arXiv:2305.17926: position bias — verdicts flip on order swap | CONFIRMED | Abstract: ranking "easily hacked by simply altering their order of appearance"; "Vicuna-13B could beat ChatGPT on 66 over 80 tested queries with ChatGPT as an evaluator." |
| B4 | Dubois et al. 2024, arXiv:2404.04475: verbosity bias; length-controlled win rates as the cure | CONFIRMED | Abstract: "AlpacaEval is known to favor models that generate longer outputs"; length-controlled AlpacaEval; Arena Spearman 0.94 → 0.98. |

## B1 — Zheng et al. (2023), arXiv:2306.05685 (NeurIPS 2023 Datasets & Benchmarks)

Citation fields verified: title, first author Lianmin Zheng, arXiv v1 2023-06-09 / v4 2023-12-24, NeurIPS 2023 D&B track (poster session Dec 12, 2023).

Load-bearing claims: (1) "~80%+ agreement with human preference" — CONFIRMED: abstract "strong LLM judges like GPT-4 can match both controlled and crowdsourced human preferences well, achieving over 80% agreement, the same level of agreement between humans"; §4.2 "agreement under setup S2 (w/o tie) between GPT-4 and humans reaches 85%, which is even higher than the agreement among humans (81%)"; Arena sample (Table 7, S2): GPT-4 pairwise vs crowd humans 87%. (2) The ~66% figure — CORRECTED: like-for-like inter-human is 81% (S2 non-tie); the 63–67% range is the S1 with-ties setup, under which GPT-4 also scores ~66%. The claim's juxtaposition mixes setups. (3) "Pairwise substantially beats single-answer" — CORRECTED as overstated: 85 vs 85 (S2 turn 1); 85 vs 84 (S2 turn 2); 66 vs 60/59 (S1); 87 vs 85 (Arena S2); paper's words: single-answer grading "matches both pairwise GPT-4 and human preferences very well... a more scalable method"; §3.1 notes pairwise "may lack scalability when the number of players increases, given that the number of possible pairs grows quadratically."

URLs: arxiv.org/abs/2306.05685 · arxiv.org/html/2306.05685v4 · neurips.cc/virtual/2023/events/datasets-benchmarks-2023

## B2 — Chiang et al. (2024), arXiv:2403.04132 (ICML 2024)

Citation fields verified: PMLR v235 (ICML 2024), pp. 8359–8388, ching24b; first author Wei-Lin Chiang.

Load-bearing claims: votes-in → ranked-whole-out CONFIRMED ("We employ a suite of powerful statistical techniques, ranging from the statistical model of Bradley & Terry (1952) to the E-values of Vovk & Wang (2021)"; "previous evolutions of our online interface have reported different ranking scores, such as the Elo score (Elo, 1967) instead of the BT coefficients"). "Widely trusted" CONFIRMED from the paper's own words. "Millions" CORRECTED: the paper's snapshot is "over 240K votes from about 90K users... as of Jan 2024"; millions is the platform's current state (ICML 2025 vote-rigging paper: "millions of crowdsourced votes... around 1.7 million historical votes" — adjacent caveat, reported without broadening: Arena rankings can be shifted by a few hundred rigged votes).

URLs: arxiv.org/abs/2403.04132 · arxiv.org/html/2403.04132v1 · proceedings.mlr.press/v235/chiang24b.html · icml.cc/virtual/2025/poster/46419

## B3 — Wang et al. (2023), arXiv:2305.17926 — CONFIRMED

Citation fields verified (first author Peiyi Wang; v1 2023-05-29). Abstract: "the quality ranking of candidate responses can be easily hacked by simply altering their order of appearance in the context... Vicuna-13B could beat ChatGPT on 66 over 80 tested queries with ChatGPT as an evaluator." The paper's Balanced Position Calibration (aggregating across orders) presupposes exactly the flip-on-swap behavior. URL: arxiv.org/abs/2305.17926

## B4 — Dubois et al. (2024), arXiv:2404.04475 — CONFIRMED

Citation fields verified (first author Yann Dubois; v1 2024-04-06). Abstract: "AlpacaEval is known to favor models that generate longer outputs. We introduce a length-controlled AlpacaEval... improves the robustness of the metric to manipulations in model verbosity, but... increases the Spearman correlation with LMSYS Chatbot Arena from 0.94 to 0.98." URL: arxiv.org/abs/2404.04475

## Bottom line

SAFE TO LAND WITH NAMED CORRECTIONS. All four citations are real and correctly attributed, and the cluster's load-bearing direction — strong-LLM judges at human-level agreement, pairwise-votes-in → statistically-ranked-whole-out as a live production precedent, order/position bias, verbosity bias with a length-controlled cure — survives web verification. Fold in three corrections: (1) B1 inter-human agreement ~81% like-for-like (the ~66% is the with-ties setup, where GPT-4 also scores ~66%); (2) B1 pairwise vs single-answer grading is equal-to-slightly-better, not "substantially beats"; (3) B2 the paper reports 240K+ votes (Jan 2024) — "millions" describes the platform today.
