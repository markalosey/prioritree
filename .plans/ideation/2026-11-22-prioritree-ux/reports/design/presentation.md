<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — design/presentation

**Route:** prioritree-ux (executing) | **Events:** 3 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T09:29:16Z |
| 2 | dispatch | shinko | 2026-11-22T09:36:33Z |
| 3 | report | suisen | 2026-11-22T09:37:19Z |
## Reported by suisen — 2026-11-22T09:37:19Z

suisen's completion report (packet design/presentation, prioritree-ux) — the tally presentation recommendation:

THE RECOMMENDATION, WHOLE: one route (GET /runs/{run_id}/tally), one generated screen family with TWO exclusive renderings — the RANKED WHOLE (200, done: true) and the SAFE HALT (409) — branched at the wire's outcome, rendered from a Python view model, Shoelace chrome via CDN, Jinja2 the renderer, zero client-side derivation, one fetch (never a second endpoint summoned to decorate either state). The binary IS the domain's (R12 strictly binary); the presentation mirrors it — never a partial ranking dressed as whole, never a halt dressed as failure.

THE RANKED WHOLE SCREEN: a semantic table, one rowspan'd rank cell per tie group — competition ranking (1, 2, 2, 4; dense lies about position), members in the frozen id-order verbatim (never re-sorted). Per-item stats: W/L/T integers verbatim plus comparisons (W+L+T — the one derivation the frozen contract sanctions); NO win-fraction column — the score is the tally's internal mechanism (R10); the projection law forbids the presentation re-deriving what the tally rules. The coverage line: one muted strip (pairs-at-quorum, "graph connected (1 component)", cycle named) with the full datum in sl-details; the named cycle rendered as a NEUTRAL tag with its directed edges + the R11 one-liner (structural, dissolved into win fractions — data quality, never an error, never danger-red); pair_counts matrix under sl-details, keys re-split on "|" (the wire's re-keyed form). The version stamp: footer badge, algorithm_version VERBATIM ("win-rate-v1") — the auditability contract.

THE SAFE HALT SCREEN: the refusal IS the screen — three labeled regions (Expected / Found / Next-action) rendering the 409 body's fields VERBATIM (R5: the same grammar on wire and screen; the body is the source, never re-computed). Found structured from the domain's own deterministic section grammar: zero-coverage items, components, under-quorum pairs as badges. Next-action = the cure, two kinds never conflated: bridging pairs ("connectivity needs NEW comparisons") vs shortfall pairs ("quorum needs MORE VOTES") — sl-tags grouped by kind. One button: resume the sitting → the compare flow (the scheduler serves exactly the under-quorum pairs; no pair-picker — comparator pair-gaming foreclosed by construction). NO ranking content — not grayed, not collapsed, not "provisional" (R12, absolute).

THE DONE-vs-HALTED DISTINCTION: branch at the wire (200 done:true → the whole; 409 → the halt) — the generator never re-derives the coverage gate's ruling; a render gate mirrors the domain gate (a body with groups but done:false REFUSES to render); distinct chrome: DONE = success badge, HALT = warning never danger (a legal terminal state, an honest refusal, not a crash); two exclusive templates, zero shared rank content, one route.

THE SHOELACE INVENTORY (CDN form): sl-card ×3 (region containers); semantic <table> + generated CSS (Shoelace ships NO table component — the honest pick; the tie group's unit-ness IS the content); sl-badge (success DONE / warning HALT / neutral ranks — the binary made visible); sl-tag (the named cycle, the closing pairs); sl-tooltip (the R11 one-liner); sl-details (the coverage datum, the pair matrix — O(n²) content collapsed). NO progress bar on either terminal screen: terminal states are binary (R12) and the 409 body carries exactly three fields — "how far along" is the mid-run STATE screen's question (the audit view that never refuses on coverage).

THE OPERATOR-vs-COMPARATOR LINE: mid-run the comparator sees the BARE pair only — the tally screen is not linked from the compare surface, no tally content embeds there (the no-anchoring law held at the presentation layer); mid-run the tally view is the OPERATOR's diagnostic (the honest refusal + the named cure); after DONE the comparator MAY see the whole — the compare flow's DONE body links to the tally (the queue exhausted, the sitting over; both comparator classes human|llm inherit the same screen contract; the later MCP tier inherits it too).

READ-BACK (files actually read): .plans/ideation/2026-11-22-prioritree-ux/.junro/evidence/Q-ux-surface/census-mechanism-a.md + census-mechanism-b.md (TallyResult's frozen shape; the tally wire — 200 asdict with pair_counts re-keyed, 409 ThreePart, the one render point); src/prioritree/tally.py (whole — CoverageDatum, TallyResult, TallyRefusedError's exact three-field bytes, win-rate-v1); .plans/ideation/2026-11-19-prioritree-birth/.junro/junro.json (R11/R12; the comparator stamps) + its evidence/Q-solution-space/suisen.md (the bare-pair law, pair-gaming foreclosed); .plans/ideation/2026-11-22-prioritree-ux/.junro/junro.json (R1 the stack + the projection law; R5 ThreePart); .junro/packets.jsonl (this dispatch). READ-ONLY held — nothing written to disk beyond this report act.
