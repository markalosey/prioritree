<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — design/blind-walk

**Route:** prioritree-ux (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T09:39:25Z |
| 2 | report | moho | 2026-11-22T09:42:34Z |
## Reported by moho — 2026-11-22T09:42:34Z

# design/blind-walk — moho's completion report — what breaks when nobody helps

READ-BACK (files read): this ux store's reports/design/flows.md (the walked flows 1–5) + reports/design/presentation.md (the terminal screens) + two blind probes: glob src/prioritree/** (the API tier exists — service.py, five ops) and glob **/*.html (ZERO templates — no live web surface; the walked glass is the design as written).

THE WALK, COLD, PER STEP (screen serves → what I need → where it breaks):
1. LANDING "/": a form serves operator id, stated question, verdict set, quorum, item rows, a resume field. Breaks: nothing says what this site IS or what happens after submit; "operator id" unexplained (chosen? minted? does it matter?); "verdict set — the weak-order triple" is jargon I cannot act on; quorum (default 1) never explained — I can set 2 and quietly doom the run; item-id rules unknown until refused; the RESUME field wants a run_id with no shape, no example, no where-to-find — and no runs-list exists, so a lost token is lost forever.
2. REGISTER ACK: run_id shown + "a changed list is a new run". Breaks: NO link from ack to the sitting is stated anywhere — my only stated path to judging is retyping the token I just received into the resume field; no "save this"/copy affordance named; the warning names a future I cannot reach (no edit op exists); for quorum>1 no share/invite affordance — recruiting the second judge is unaddressed on every screen.
3. THE SITTING: question + two label-only cards + verdict buttons from the declared set + comparator id entry. Breaks: WHY a comparator id — I registered as operator, nobody says these are the same person; the button↔card mapping is UNSPECIFIED — the two docs never tie a button to a card, and cards carry labels only (ids hidden, id-sorted invisible), so if buttons read a/b-flavored I must GUESS which backs which card; a consistent wrong guess silently reverses the whole ranking and no signal ever disconfirms it.
4. VOTE ACK → NEXT: the ack strip (vote_id + acknowledged) auto-loads the next pair. Breaks: the ack never restates WHAT I chose (no "you preferred X over Y") — mis-clicks and mis-mappings are undetectable at the only moment they are checkable; counts hidden by design leaves no horizon (10 pairs? 10,000?); the operator's progress screen exists but no stated link reaches it.
5. 422 MID-SITTING: the pair stays, refusal renders verbatim three-key. Serves OK (pair intact, same-pair retry). Breaks: no pre-check on the comparator id — my first refusal teaches me the field I never understood; the wire's machine grammar renders verbatim by ruling — readable to the seats, alien to me.
6. DONE "every pair judged": Breaks: "judged" means MY queue, not the run's coverage — with quorum>1 my done is the run's not-done; the "ranked whole" link can land me on a 409 I cannot act on ("I did my job — why refused?").
7. RANKED WHOLE + SAFE HALT: the table reads (competition ranks, tie groups, W/L/T). Breaks: "graph connected (1 component)" and the components badges are graph theory with no plain gloss (the cycle earns a one-liner; components earn none); the cycle one-liner cites "win fractions" — a number the table deliberately hides; the halt's "resume the sitting" presumes I know more judges exist — WHO provides the "NEW comparisons"/"MORE VOTES" is never said, and a solo operator's cure is unstated (re-sit under a new comparator id?); the seats disagree on the halt's affordances (flows.md: cure links resume+progress; presentation.md: "one button").
8. RESUME (a day later): token → landing resume field → sitting re-serves. Breaks: depends entirely on a once-shown opaque token being preserved; no "where you left off" — the returning me cannot tell a fresh pair from one already judged, and a quorum-echo pair (idempotent ack) is indistinguishable from new work; the returning user who wants the RESULT funnels through the sitting — no direct result address on the landing.

THE WALK'S VERDICT: the design serves the domain flawlessly (honest refusals, unanchored pairs, legal halts) and the user barely — the wire's grammar is projected into the glass verbatim, and the cold user inherits the engineers' nouns (components, quorum, weak-order, comparator) with no bridge. The three breaks that lose users: the button↔card guess (silent vote corruption), the ack→sitting gap (the fresh registrant's dead end), done-vs-coverage (the completed user refused).
