<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — measure/probe

**Route:** order-bias-probe (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-26T02:26:32Z |
| 2 | report | jikko | 2026-11-26T03:08:57Z |
## Reported by jikko — 2026-11-26T03:08:57Z

# THE INSTRUMENT STEP — jikko (実行), packet measure/probe, route order-bias-probe, 2026-11-26

THE FIELD (seven sites, additive): (1) votes.py `presentation_order: str = PRESENTATION_CANONICAL` on VoteRecord + `PRESENTATION_ORDERS = frozenset({PRESENTATION_CANONICAL, PRESENTATION_SWAPPED})` + cast_vote's eighth argument; (2) run_store.py the line `"presentation_order": presentation_order` (the pair/winner the WIRE's bytes) + the pre-pass `_read_presentation_order_field` (absent → canonical, the legacy honest read; unknown token refused); (3) service.py CastVoteRequest `presentation_order: str = PRESENTATION_CANONICAL`; (4) mcp_server.py CastInput `presentation_order: PresentationOrder = Field(default="canonical", description=TEXT_PRESENTATION)` (the Literal + the PRESENTATION_ORDERS drift guard); (5) cli.py next `--swap` + vote `--presentation-order`; (6) web.py + pair.html the hidden `<input type="hidden" name="presentation_order" value="{{ presentation_order }}">`; (7) the door composed: `_resolve_cited_pair` (the fieldless swapped citation still refused naming the canonical form + teaching the field; the contradicting field refused; the fielded swap mapped).
THE MAPPING (votes.py:605-614, verbatim): stage 4b `if presentation_order == PRESENTATION_SWAPPED: winner = _POSITIONAL_SWAP.get(winner, winner)` — prefer-a@swapped = the canonical item_b's win (record winner prefer-b); the record canonical pair + mapped winner + token; the dedup key 8-wide (two orders two distinct judgments); THE TALLY NEVER TOUCHED (R12's fence: tally.py zero bytes edited).
THE SWAP'S SERVE FORM (service.py:528-536, verbatim): `?swap=true` → `content={ITEM_A: item_b, ITEM_B: item_a, COUNT: count, PRESENTATION_ORDER: PRESENTATION_SWAPPED}` — the same knob at the MCP's NextInput.swap, the CLI's `next --swap`, the web's sitting/fragment `?swap` (the vote-ack chain carrying it); the served body's item_a/item_b the PRESENTED pair, presentation_order naming the form.
THE FLOOR (the three outcomes verbatim): lint — "All checks passed!"; pyright — "0 errors, 0 warnings, 0 informations"; tests — "442 passed in 33.21s". THE EXACT COUNT: 442 (423 standing + 19 new arcs: test_votes 3 [the recorded order, the composed refusals, the two-orders dedup], test_run_store 4 [the swapped round trip, the legacy honest read, the swapped-line-without-field refusal, the contradictions + the form check], test_tally 1 [the R12 byte-identity over both presentation forms], test_session 1, test_service_face 3, test_mcp_server_face 3, test_web_face 2, test_cli 2); two exact-body pins amended (the serve body + the done key set) across the face/auth/acceptance files.
NOT DONE (honest): the run's own steps — the sweep's driving, the item universe, the roster, the counterbalance assignment (the instrument enables, the run's step drives); the seed's shuffle mode stays a CURE, un-built per the synthesis.
