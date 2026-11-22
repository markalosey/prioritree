<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — design/blind-walk

**Route:** prioritree-mcp (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T20:39:56Z |
| 2 | report | moho | 2026-11-22T20:43:26Z |
## Reported by moho — 2026-11-22T20:43:26Z

MOHO — design/blind-walk — what breaks when nobody helps: the cold agent's walk through the five designed tools (2026-11-22)

Ground read: reports/design/tools.md (the five definitions), reports/design/budgets.md, reports/census/ouncemcp.md (the teaching idiom). Walked against the designed SHAPES — no verbatim definitions exist on disk (no server.py; no description text anywhere — glob/grep evidence). First finding: the shapes are settled, the teaching layer is a blank; every "does the agent know" below lands on text still unauthored.

1. ARRIVAL — runs.register / runs.next / votes.cast / votes.census / runs.tally: two noun groups, five ordinary verbs — the agent half-guesses "register, get next, cast votes, audit, tally." But the PRODUCT's mechanic (items judged PAIRWISE, votes tallied into a rank) appears in no name; "pairwise" stays invisible until runs.next returns item_a/item_b. Nothing confirms the sequence. Headroom exists (1,005 of 4,000 startup tokens) to teach the arc — none authored.

2. REGISTER — items (min 2, non-empty strings): plain strings, guessable, fine. quorum (ge 1): the word hints votes-per-pair, but its semantics — per pair? gates the tally? — are taught nowhere; the agent sets a number it cannot price, and that number later IS the halt. The ack's run_id is inferable as the handle (weak but workable); "verdicts" is a mystery field — one of "the two defaulted run-facts," never explained. Refusals carry {expected, found, next_action} — self-correcting IF the core's text instructs; the static bounds sit in the schema, so most refusals never fire. Credit.

3. NEXT — one model, done: bool tag — a clean channel, credit. done=false carries item_a/item_b/count — the field names rhyme with cast's pair param, so the loop wires itself; "count" of WHAT is untaught (cosmetic). done=true carries next_action verbatim from ExhaustedQueue — whether it says "call runs.tally" is quoted nowhere: the done→tally handoff, the journey's load-bearing turn, rests entirely on unauthored text.

4. CAST — pair [item_a, item_b] from next's echo: wired by rhyme, credit; whether order matters is unrecorded — a swapped pair's legality is learned only by refusal, or accepted mirrored. comparator_class is pattern-constrained (self-teaching, credit) but comparator_id is a free REQUIRED string, minted-nowhere, convention taught nowhere — the agent invents an identity while the R9 judgment-keyed dedup may make that guess load-bearing (split ids = split voice? unrecorded). acknowledged: True fires on fresh votes AND on dedup-caught replays — constant on success, so what it MARKS (and whether False ever occurs) is opaque; the agent cannot tell counted-fresh from replayed.

5. THE HALT — runs.tally refuses under quorum, naming the isolated items and closing pairs — but at that moment runs.next returns done=true: the two tools DISAGREE about "finished," and the taught loop (next→cast) offers no move. The only exit — casting the closing pairs directly, without a serve — is taught nowhere. Whether the halt is self-curable (can one voice raise a pair to quorum, or does judgment-keyed dedup collapse repeats?) is unanswerable from the record — the agent cannot know if the cure is its own casts or the sitting's other voters. The stuck-state is total unless the refusal's next_action names the verb; budgets' own hazard confirms the render is open (found can name 4,950 pairs ≈ 69,300 tokens through the error channel — the cap/summarize "must" unlanded).

6. THE WHOLE — ranked_groups: the name says groups, not ties — reading [[A],[B,C],[D]] as "B ties C" is a guess from shape. The three per-item maps are never named in the record — the agent decodes unnamed fields at runtime. coverage (pairs_expected vs pairs_at_quorum) is self-teaching arithmetic — credit. algorithm_version stamps the rule without naming it: the agent presents a rank it cannot explain.

THE TOP THREE FIXES (description-level, the census's own idiom — "Use books.search to find ids"):
1. THE HALT'S EXIT, AUTHORED: tally's next_action names the verb and the branch — "cast the closing pairs via votes.cast (a legal pair needs no serve); pairs beyond your one voice mean: resume the sitting" — with the capped found (shortfall count + first pairs) landed as budgets ruled.
2. THE ARRIVAL ARC IN register'S DOCSTRING: "Register items for a pairwise-comparison sitting; loop runs.next → votes.cast until done:true; runs.tally emits the ranked whole; votes.census audits." One breath teaches product and sequence — the widest gap closed cheapest.
3. THE STAMPS + THE MARKER ON cast'S FIELDS: comparator_id — "your stable identity for this sitting; the same id keeps re-sent judgments one voice"; acknowledged — "true = recorded; a repeat acks the original, never double-counts" — and rule what False means, if anything, so the marker carries information.

Also on disk: the name fork — tools.md's runs.*/votes.* vs budgets.md's run.register/pair.serve/vote.cast/state.census/tally.rank priced two minutes earlier; the result_tokens=4,500 ruling is keyed to names since renamed. A cold agent sees one set; the budget ruling must be re-keyed at the synthesis.
