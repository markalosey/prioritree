<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/done-detour

**Route:** prioritree-polish (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-27T01:21:42Z |
| 2 | report | togo | 2026-11-27T01:25:03Z |
## Reported by togo — 2026-11-27T01:25:03Z

# THE DETOUR'S UNIT BRIEF — the material cure's lane (togo, 統合, packet synthesize/done-detour, route prioritree-polish, 2026-11-27)

THE GROUND, PINNED THIS PASS (every load-bearing byte re-read, never copied): the vote POST whole (web.py:1106-1189 — the chain region :1163-1176, the arms' context :1180-1189); the judge route whole (:792-869 — the chain pass-through :847/:867); the fragment's done edge (:1078-1103, the redirect :1082-1083); pair.html (the form :3-21, the conditional carry :12); vote-ack.html (the ack-line :3, the echo :4, the three arms :5); picker.html:6-7 (the bare links); sitting.html:16/:21 (the include + the picker); test_web_face.py's deliberate arcs (:714-769) + the header's map (:2-38); the synthesis §3 + 1c-8/1c-9; moho's walk §1; hyoka's four fences; G-DONE-DETOUR's three conditions (the store's heart). READ-ONLY held — this report the packet's only write; the synthesis rules, never decides: the approval the collaborator's.

## 1. THE SCOPE FENCE — what the cure lands

**(a) THE LANE DATUM `deliberate`.** Three lanes feed the ONE vote POST (/ui/runs/{stem}/vote); today only two are distinguishable — the chain field's presence/absence — so the bare deliberate vote (the picker's links, picker.html:6-7) and the sitting's vote SHARE the fetch arm, and that sharing IS the detour (the fetch → the fragment's /next consult → HX-Redirect /done at the exhausted queue; the pair-swap override at the live queue — moho's two lived forms). THE CURE AT THE BYTES: the judge route (/runs/{stem}/pair — the picker's link target; BOTH the bare form and the chain form ride it) passes the lane datum into the pair context — `"deliberate": "true"` beside `"chain": chain` (web.py:867); pair.html grows the conditional hidden field beside the chain's own (:12's pattern, the identical form): `{% if deliberate %}<input type="hidden" name="deliberate" value="{{ deliberate }}">{% endif %}`. THE COMPOSITION RULED (the absence/presence of the two fields, read in order at the POST): chain present (whatever the datum) → the CHAIN ARMS (the sequence-carry wins — the chain form's ack byte-standing); chain absent + datum present → the STAY-PUT ARM (the bare deliberate lane); both absent → the FETCH ARM (the sitting lane, byte-standing). The datum is the ROUTE's own knowledge — NEVER a new query param (the picker's links byte-untouched, no link drift, no new teaching at the picker); the datum rides ALL judge pages (the lane is deliberate; the chain is the sequence over that lane); absent/empty renders no field, so the sitting page and the fragment-served region (no datum in their contexts) render byte-identical to today. THE FIELD'S NAME per the naming law: `deliberate` (the synthesis §3's ruling).

**(b) THE STAY-PUT ARM.** The POST reads the datum — `deliberate = str(form.get("deliberate", "")).strip()` beside the chain read (:1163) — the arm's rule above. THE ARM'S RENDER: the confirmation standing — the ack-line (:3, the verdict restated in item-label terms) + the acknowledged echo (:4) sit ABOVE the branch, byte-standing at every arm — plus BOTH LINKS taught: the picker's return link `/runs/{stem}/pairs` (the live queue's next move — the judge picks the next pair) + the done link `/runs/{stem}/done` (the exhausted queue's end — the chain form's own empty-rest link shape). NO fetch (no hx-trigger="load" div at this arm), NO redirect (the fragment route never called at this lane — the done edge :1082-1083 unreachable from the deliberate lane; the bounce dead at its root, the live-queue pair-swap override dead with it).

**(c) THE LANES UNTOUCHED.** The SITTING lane's fetch chain byte-standing (the ack's else arm IS the sitting's two-step next-pair mechanism — fence 1); the CHAIN form's carry byte-standing (the judge route's :847/:867 pass-through, pair.html:12, the POST's chain arms :1166-1176 — the chain lane's ack renders next_url/done_url exactly as today; the datum riding the chain page's form is read AFTER the chain, never reaching its arms); the FRAGMENT's done edge untouched (:1082-1083 — the sitting's natural end, fence 3).

**(d) THE ARCS.** The lane-separation set — the three lanes' separation proven at the suite (§3).

## 2. THE MECHANISMS RULED

**THE ACK'S COMPOSITION.** The handler's lane read: the composed order above (chain → datum → fetch). The context grows the arm's marker (`"deliberate"` beside next_url/done_url, :1180-1189); the template's arm order after the cure: `next_url / done_url / deliberate / the fetch` (§3's ruling) — the deliberate branch inserted between the done_url arm and the else at :5, rendering the teaching line + both links composed from `{{ stem }}` (STATIC — no handler URL computation at this arm).

**THE QUEUE-BLIND RULING (the no-anchoring law held — fence 2 + the synthesis 1c-9).** The arm is QUEUE-BLIND: the POST never consults /next, never reads the queue's state, renders NO counts (the vote docstring's "the count UNREAD, never rendered" standing). BOTH LINKS RENDERED STATIC from the stem; the open-vs-exhausted conditions live with the judge (who knows the queue from the pages walked), never the POST. The state-carrier chain (the picker's GET marking the links per the queue's read) REFUSED — the state stales between the read and the POST; the lane's own law coverage-blind ("a vote legal on any registered pair at any coverage point", web.py:811-813); the stale-teaching seed refused.

**THE HONEST-DOCS RIDES (the law at the landing).** The vote docstring (:1108-1133) GROWS the deliberate arm's account (the datum's read, the stay-put form, both links, queue-blind, no fetch at the bare lane — composed with the standing chain-form sentence); the judge docstring (:801-830) GROWS the datum's pass-through sentence (beside the chain param's own :816-820); the two template comments (vote-ack.html:1 + pair.html:1 — the detour's own touched surfaces, 1c-8's sequencing: ONE true landing, never the double-edit drift) name the post-cure forms: vote-ack's the FOUR arms (the chain link / the done link + list-ended / the deliberate stay-put / the fetch); pair's BOTH conditional carries (the chain + the deliberate).

## 3. THE TEST PLAN'S SHAPE — the arcs (test_web_face.py, the deliberate lane's arcs' home)

THE FLOOR 475 STANDING (the no-break proof) + the lane-separation set landed — the floor grown by the arcs' count (derived at the build, the claims lane; every arc green):
1. THE SITTING LANE'S SEPARATION ARC — the sitting-sourced vote (no chain, no datum) → the fetch arm (the hx-get div rendered): the lane untouched, proven.
2. THE CHAIN LANE'S SEPARATION ARCS — the chain vote → next_url (the P-token dropped, the swap knob carried); the chain's empty rest → done_url + the list-ended teaching: the carry byte-standing, proven. [AT THE RECORD: the chain arms carry NO arcs in the tree today — the flow fix landed the mechanism without its tests (verified this pass: no chain-form assertion anywhere in tests/); the lane-separation proof lands them whole.]
3. THE BARE DELIBERATE ARC — the picker-sourced vote (the datum, no chain) → the stay-put arm: the confirmation rendered (the ack-line's restatement; the acknowledged echo at the idempotent re-cast), NO hx-get div, NO HX-Redirect, BOTH links in their exact forms (`href="/runs/{stem}/pairs"` + `href="/runs/{stem}/done"`).
4. THE EXHAUSTED-QUEUE DELIBERATE ARC — the same stay-put form at the done queue (every pair at quorum AND corroborated — RUN-0008's own state; the two-class corroboration composed as the existing deliberate arc does): the bounce dead — the seven-times-lived cost's proof.
THE ARCS COUNTED: the lane-separation's three (the sitting / the chain [two arcs] / the bare) + the confirmation's render + the links' forms (the deliberate arcs' own assertions). The header's map GROWS the lane-separation naming (any told count re-derived at the cure — the honest-docs law).

## 4. THE ACCEPTANCE MAPPING — G-DONE-DETOUR's three conditions

1. "the detour lands per the approved spec (the exact-task law): the ack stays at BOTH forms … the sitting/chain lanes and the fragment's done edge byte-untouched, the lane-separation arcs landed" → §1(a)-(d) + §5: the datum + the stay-put arm land the bare lane's ack (the confirmation rendered, both links taught, no fetch, no redirect; the done link taught at the exhausted queue); the three untouched surfaces fenced at §1(c); the arcs at §3.
2. "the floor 475 standing (the lanes' separation proven by the arcs); ruff zero, pyright 0/0; kensho's independent verification green (validate/done-detour); MOHO'S WALK at the gate" → §3's set + the standing bar; the walk's shape: the bare deliberate vote at the completed run — the confirmation standing, both links served, no bounce (the picker's link at the live queue, the done link at the exhausted — the seven-times-lived cost dead).
3. "the four constraints held (hyoka's fences)" → fence 1 the sitting's two-step chain untouched (§1c); fence 2 the no-anchoring law (§2); fence 3 the fragment's sitting-serving done edge untouched (§1c); fence 4 the confirmation standing at the deliberate lane (§1b); the lane-separation proven (§1d/§3).
THE SPEC GATE'S OWN CONDITIONS (G-DONEDETOURSPEC-BRIEF at the store's registry — the dispatch's G-DONE-DETOUR-BRIEF its shorthand) served by this brief: the bytes whole, every edit fenced (§5); the four constraints fenced — never violated by the spec's own bytes (§1c/§2); the collaborator's approval — the build dispatches cite the approved spec (the exact-task law).

## 5. THE HANDOFF — the spec lane's opens (the per-step plan R8, the file-units)

FOUR units (the ask's three + pair.html named honestly — the field's home + the 1c-8 comment cure, the synthesis's own sequencing):
1. **web.py** — (a) the judge route's context: `"deliberate": "true"` beside `"chain": chain` (:867); (b) the POST: the deliberate read beside :1163, the `elif deliberate:` arm after the chain block (:1176), the context's arm marker (:1180-1189); (c) the two docstrings' grows (:1108-1133, :801-830). Every edit's before/after fenced at the spec's derivation (the exact bytes the build cites).
2. **pair.html** — the conditional field beside :12 (the chain-carry's own pattern); the comment's cure (:1).
3. **vote-ack.html** — the deliberate branch between the done_url arm and the else (:5); the comment's cure (:1, the four arms named).
4. **test_web_face.py** — the lane-separation arcs (§3) + the header's map grown.
THE CEREMONY: the build (jikko) lands the four units per the approved spec; the floor-green step (make); kensho's independent verify (validate/done-detour — the arcs green, the floor standing, the three lanes' separation confirmed at the tree); MOHO'S R4 WALK at the gate; the bar at every unit: ruff zero, pyright 0/0, zero ignores (any ruling named per-file), the F6 boundary (mechanism fenced, prose paste-verified), the claims lane at every count.

— togo (統合), the brief whole; the synthesis §3 carried at the bytes, every fence composed, never violated; the disk the truth; READ-ONLY held, this report the packet's only write.
