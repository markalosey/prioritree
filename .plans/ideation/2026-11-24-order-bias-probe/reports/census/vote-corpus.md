<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/vote-corpus

**Route:** order-bias-probe (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-25T03:42:43Z |
| 2 | report | tansa | 2026-11-25T03:46:09Z |
## Reported by tansa — 2026-11-25T03:46:09Z

# THE VOTE CORPUS'S CENSUS — tansa (census/vote-corpus, order-bias-probe, 2026-11-24)

Read-only at the repo root /Users/marklosey/projects/prioritree; every number cited to its file; the sums verified at the calculate instrument (22, 11, 11, 14, 8, 25). Nothing edited.

## 0. THE GROUND (read whole)
- THE STORE'S HEART (.plans/ideation/2026-11-24-order-bias-probe/.junro/junro.json): Q-order-bias open; THE CONVENING ruling (2026-11-25): the measurement first, the cure earned by the datum, the null a finding; the census stage first, its findings assumed by none of the composition.
- THE BIRTH STORE'S R7 (.plans/ideation/2026-11-19-prioritree-birth/.junro/junro.json:547, :725): unordered-pairs-once — the schedule is the n(n−1)/2 unordered pairs, CANONICAL ID-SORTED presentation, deterministic enumeration, default seed derived from run_id; the both-directions order-bias probe (Wang et al.'s flips-on-swap) a PRICED DEFERRAL behind the schema's stamps. Wang et al. VERIFIED at the birth store (.junro/evidence/Q-problem-space/prior-art-validation-b1.md:15, :34-36 — B3 CONFIRMED, "easily hacked by simply altering their order of appearance").
- THE AUTH CLOSE'S GROUND (.plans/ideation/2026-11-24-prioritree-auth/.junro/junro.json:813, :842 — the done call 2026-11-25, floor 336): the verified stamps — the class on the key record (F8), the id from the key, the self-claim dead at every authenticated door (service.py:527-528); the corroboration floor ENFORCED at the tally's coverage gate (policy.py:69-89, missing_classes — >=1 human AND >=1 llm per pair); the stdio tier trusts self-claims by named ruling.

## 1. THE RUNS ON DISK (the .prioritree/ home whole)
The home .prioritree/ carries: runs/ (SEVEN run files + .prioritree.lock, 0 bytes), mcp-server.log, server.log. Every run file read whole; items are [id, label] rows (run_store.py:565); ids listed below in manifest order (the sort is the scheduler's act):

- RUN-0001.jsonl — in-file run_id RUN-0001; registered 2026-11-22T05:22:15Z; 2 items (ids Tony, Jack); operator id "beauty"; question "Who is prettier?"; quorum 1; verdicts [prefer-a, prefer-b, tie]; VOTES: 0.
- RUN-0002.jsonl — in-file run_id RUN-0001; registered 2026-11-22T20:15:27Z; 5 items (ids blue, red, green, yellow, orange); operator id "Mark Losey"; question "What color is more beautiful?"; quorum 1; VOTES: 10.
- RUN-0003.jsonl — in-file run_id RUN-0001; registered 2026-11-23T03:20:36Z; 3 items (ids 1, 2, 3; labels blue, yellow, orange); operator id "Mark A Losey"; question "Which"; quorum 1; VOTES: 3.
- RUN-0004.jsonl — in-file run_id RUN-0001; registered 2026-11-23T16:21:48Z; 3 items (ids live-check-alpha, live-check-bravo, live-check-charlie); operator id "shinko"; question "The member-path live check: which of these three?"; quorum 1; VOTES: 0.
- RUN-0005.jsonl — in-file run_id RUN-0001; registered 2026-11-23T17:27:26Z; 4 items (ids nuts, chocolate, banana, jerky); operator id "moho"; question "Which snack best fuels a long blind walk?"; quorum 1; VOTES: 6.
- RUN-0006.jsonl — in-file run_id RUN-0001; registered 2026-11-25T02:09:16Z; 2 items (ids the-hide-teaching-loss, the-401-misdirection); operator id "moho"; question "moho's R4 blind-walk probe at the stdio tier: which finding cuts deeper at the mcp door?"; quorum 1; VOTES: 1.
- RUN-0007.jsonl — in-file run_id RUN-0001; registered 2026-11-25T02:54:07Z; 2 items (ids the-told, the-lived); operator id "moho"; question "R4's cold-walk live probe: does the README's told surface match the lived?"; quorum 1; VOTES: 2.

THE TWO ID SPACES (the accepted oddity, named at the source): every file's manifest AND vote lines carry the DOOR's verbatim run_id "RUN-0001"; the FILE STEM (RUN-0001..RUN-0007) is the cross-process identity, minted per the store-home scan (max RUN-{n}+1, run_store.py:540-545 — "the accepted oddity named: file RUN-0007.jsonl's lines may say RUN-0001"; :901-912 the two id spaces never conflated). A census keyed on the in-file run_id collapses all seven runs into one; the stem is the truth. Vote ids are per-run sequential VOTE-{####}, restarting in each file (run_store.py:593).

## 2. THE VOTES' STAMPS (per run, every vote read whole; pair → winner)
- RUN-0002 (VOTE-0001..0010; comparator_id "Mark Losey", class HUMAN, supersedes null, notes null; recorded_at 2026-11-22T20:16:02 → 20:16:20): (blue,green)→prefer-a; (blue,orange)→prefer-b; (blue,red)→prefer-b; (blue,yellow)→prefer-b; (green,orange)→prefer-a; (green,red)→prefer-b; (green,yellow)→prefer-b; (orange,red)→prefer-b; (orange,yellow)→prefer-a; (red,yellow)→prefer-a — 3 prefer-a, 7 prefer-b.
- RUN-0003 (VOTE-0001..0003; "mark", HUMAN, null supersedes; 2026-11-23T03:20:54 → 03:21:03): (1,2)→prefer-a; (1,3)→prefer-a; (2,3)→prefer-b.
- RUN-0005 (VOTE-0001..0006; "moho", LLM, prose notes on every vote, null supersedes; 2026-11-23T17:27:33 → 17:28:20): (banana,chocolate)→prefer-a; (banana,jerky)→prefer-a; (banana,nuts)→prefer-b; (chocolate,jerky)→prefer-a; (chocolate,nuts)→prefer-b; (jerky,nuts)→prefer-b — 3 prefer-a, 3 prefer-b.
- RUN-0006 (VOTE-0001; "moho", LLM, noted; 2026-11-25T02:09:23): (the-401-misdirection, the-hide-teaching-loss)→prefer-a.
- RUN-0007 (VOTE-0001 "moho" LLM 02:54:16 + VOTE-0002 "the-stranger" HUMAN 02:55:23; both noted, both null supersedes): both on the SAME pair (the-lived, the-told)→prefer-a, prefer-a.
- THE STAMPS' ERA: all 22 votes were cast BEFORE the auth close (the done call 2026-11-25; the last vote 02:55:23Z precedes the auth route's final gate G-README-PUBLIC-STORY, green 02:59:54Z) — the corpus's comparator_id/comparator_class fields are the SELF-CLAIM form (pre-auth wire doors; RUN-0006/0007 cast at the stdio tier, which trusts self-claims by the named ruling). The verified-stamp doors (service.py:527-528 — the KeyRecord's id/class in place of the body's claims; the mcp door's stamping delegation) govern the probe's FUTURE minted runs; this corpus's stamps are citable AS RECORDED.
- THE CORROBORATION FLOOR'S HOLD PER PAIR (>=1 human AND >=1 llm — policy.py:69-89): of the 21 voted pairs, EXACTLY ONE holds — RUN-0007's (the-lived, the-told): 1 llm + 1 human. The other 20 voted pairs are single-class: 13 human-only (RUN-0002's 10 + RUN-0003's 3), 7 llm-only (RUN-0005's 6 + RUN-0006's 1). Under the standing floor every one of those 20 pairs halts missing one class.
- THE SUPERSEDES RECORDS: 22 of 22 votes carry "supersedes": null — ZERO corrections in the corpus; the supersedes door check (the auth effort's F4) never exercised by this data.

## 3. THE PRESENTATION ORDER (the schedule's canonical form, read at the source)
- src/prioritree/scheduler.py:80-84 (schedule_pairs): sorted(ids) — Python codepoint order, no locale, no case-folding — then the i<j double loop in lexicographic order emits Pair(item_a=outer, item_b=inner): every pair ID-SORTED WITHIN by construction; the queue a pure function of the id-SET; the count law n(n−1)/2; deterministic, no randomness, no time.
- THE SEED'S CARRIED FORM: schedule_pairs(ids, seed: int | None = None) — the seed parameter UNUSED at birth ("nothing stochastic remains at birth", scheduler.py:75-79); derive_seed(run_id) (:87-106) — blake2b over the run_id's UTF-8 bytes, first 8 bytes big-endian (SEED_ALGORITHM :23, SEED_BYTES :24) — the reproducible key the hidden scheduler seam later consumes (the widening additive, never rework).
- AT EVERY VOTE: the recorded pair IS the canonical id-sorted form — verified per pair across all 22 votes: RUN-0002's 10 pairs all (earlier, later) per codepoint sort blue<green<orange<red<yellow; RUN-0003's (1,2),(1,3),(2,3); RUN-0005's 6 per banana<chocolate<jerky<nuts; RUN-0006's (the-401-misdirection, the-hide-teaching-loss) ("4"<"h"); RUN-0007's (the-lived, the-told) ("l"<"t"). The vote order within each file follows the scheduler's queue order (sequential casting). prefer-a therefore means "the lexicographically-first id won" at every vote in this corpus.

## 4. THE CORPUS'S MEASUREMENT SHAPE
- THE PAIRS' UNIVERSE: 25 pairs scheduled across the 7 runs (1+10+3+3+6+1+1); 21 carry votes (10+3+6+1+1); 4 unvoted (RUN-0001's (Jack,Tony); RUN-0004's 3).
- THE BOTH-DIRECTIONS QUESTION'S RAW MATERIAL: ZERO. No pair was EVER presented in both orders — every one of the 21 voted pairs appears in exactly ONE direction (the canonical id-sorted), and no presentation-order stamp exists besides the canonical form (the schedule emits one direction per pair; the seed dead at birth). THE FLIPS-ON-SWAP DATUM (Wang et al.'s class) IS NOT COMPUTABLE OVER THIS CORPUS AS-IS: the retrospective corpus supports only single-order descriptive statistics (the prefer-a share at the fixed canonical order, sliced per class and per run), never a within-pair swap comparison. The both-orders experiment must be PROSPECTIVE — a minted run presenting the same pair in both orders; the corpus's own shape is that experiment's ground.
- WHAT THE CORPUS SUPPORTS AS-IS (the descriptive raw material; interpretation to shindan/keisan): the canonical-order prefer-a rate 11/22 = 50.0% of all votes (per class: human 6/14, llm 5/8); zero ties; per-run prefer-a shares: RUN-0002 3/10, RUN-0003 2/3, RUN-0005 3/6, RUN-0006 1/1, RUN-0007 2/2. The caveat the corpus itself carries: the canonical order correlates with id sort (codepoint), never with any quality dimension.
- THE CLASSES' BALANCE PER PAIR: 20 pairs single-class single-vote; 1 pair both classes (RUN-0007's). Whole corpus: 14 human votes / 8 llm votes. R7's "LLM-dominant birth session" revisit trigger: NOT met at the whole-corpus count (human 14 > llm 8) — the per-run picture varies (RUN-0005/0006 llm-only; RUN-0002/0003 human-only).
- THE RUNS' DONE/HALT STATES: NO state field exists in any run file — DONE/halt is DERIVED at the tally (the coverage gate over the votes), never stored in the JSONL. Derived coverage at quorum 1: RUN-0002 10/10 pairs voted → coverage complete; RUN-0003 3/3; RUN-0005 6/6; RUN-0006 1/1; RUN-0007 1/1 (2 votes, quorum met at the first); RUN-0001 0/1 and RUN-0004 0/3 — zero votes, halt-shaped (the closing pairs unjudged). UNDER THE STANDING CORROBORATION FLOOR the derived picture narrows to ONE passing pair: RUN-0007's (both classes); every other voted pair halts missing one class; RUN-0001/RUN-0004 halt on zero coverage besides.

## 5. THE HONEST COUNTS (every number cited; the sums verified at the calculate instrument)
- Runs: 7 total; 5 with votes; 2 manifest-only (RUN-0001.jsonl:1, RUN-0004.jsonl:1).
- Votes: 22 total (RUN-0002 10 + RUN-0003 3 + RUN-0005 6 + RUN-0006 1 + RUN-0007 2 = 22).
- Winners: prefer-a 11, prefer-b 11, tie 0 — the ties' share 0/22 = 0% (every manifest declares "tie" in its verdicts vocabulary; no vote ever used it).
- Per-pair counts: 20 pairs × 1 vote; 1 pair × 2 votes (RUN-0007's (the-lived, the-told)).
- Classes: HUMAN 14 ("Mark Losey" 10 [RUN-0002], "mark" 3 [RUN-0003], "the-stranger" 1 [RUN-0007]); LLM 8 ("moho" 8: 6 [RUN-0005] + 1 [RUN-0006] + 1 [RUN-0007]).
- Quorum: 1 declared on all 7 runs — the quorum-1 shape everywhere; the quorum-2 shape ABSENT from the corpus. RUN-0007's pair is the only beyond-quorum vote set (2 votes on a quorum-1 pair — the corpus's only corroboration).
- Supersedes: 0 correction records (22× null). Vote notes: null on 13 votes (RUN-0002/0003's); prose on 9 (RUN-0005's 6, RUN-0006's 1, RUN-0007's 2).
- The recorded_at span: 2026-11-22T20:16:02Z (RUN-0002 VOTE-0001) → 2026-11-25T02:55:23Z (RUN-0007 VOTE-0002).

THE CENSUS'S HEADLINE FOR THE DESIGN LANE: the corpus is small (22 votes, 21 voted pairs, 7 runs), single-order (ZERO both-directions raw material — every pair ever judged in exactly one, canonical, direction), single-vote per pair (quorum 1, one corroborating exception), class-skewed per pair (one both-class pair in the whole corpus), zero ties, zero corrections, all stamps the pre-auth self-claim form. The flips-on-swap datum demands the prospective both-orders experiment; the retrospective corpus can carry only the fixed-order descriptive datum at its own weight.
