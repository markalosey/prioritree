<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — validate/done-detour

**Route:** prioritree-polish (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-27T16:49:35Z |
| 2 | report | kensho | 2026-11-27T16:57:07Z |
## Reported by kensho — 2026-11-27T16:57:07Z

# THE DONE-DETOUR'S INDEPENDENT VERIFICATION (kensho, 検証; packet validate/done-detour, route prioritree-polish, 2026-11-27)

THE INSTRUMENTS RE-RUN (my own runs this pass — never the build's word):
1. THE FULL SUITE: "480 passed in 43.81s" — the floor 480 CONFIRMED (the build named 480 at 42.15s; the count exact at my own run, the tree's own way).
2. THE LINT ACT: "All checks passed!" (ruff over src/ + tests/) — zero findings, the zero-ignore bar held.
3. THE TYPECHECK ACT: "0 errors, 0 warnings, 0 informations" (pyright) — the zero-errors AND zero-warnings bar held.

THE SPEC'S CLAUSES AT THE BYTES (each read at the tree this pass, never copied):
- THE LANE DATUM: web.py:1191-1192 — chain read at :1191, `deliberate = str(form.get("deliberate", "")).strip()` at :1192, the composed order chain -> datum -> fetch (the fetch the template's bare else when neither field rides); the judge route's `"deliberate": "true",` at :888 beside `"chain": chain,` (:887) — the constant the ROUTE's own knowledge at every judge-page render, NEVER a query param (the route's only query read is `chain` at :867); the picker's links byte-untouched (picker.html:6-7 — the bare `/runs/{{ stem }}/pair?item_a=...&item_b=...` + the `&swap=true` form, NO datum param).
- THE STAY-PUT ARM: web.py:1206-1209 — `elif deliberate:` + the spec's comment TEXT VERBATIM (re-flowed to two lines above the pass at the 120-char limit, E501 held, no ignore taken) + `pass` — queue-blind, nothing computed, no /next call, the fragment route never reached from this arm.
- THE CONTEXT MARKER: web.py:1222 — `"deliberate": deliberate,` after `"done_url": done_url,` (:1221).
- PAIR.HTML'S CARRIES: :12 the chain carry byte-unchanged; :13 `{% if deliberate %}<input type="hidden" name="deliberate" value="{{ deliberate }}">{% endif %}` — the field carried at the POST so the arm fires; the :1 comment grown naming BOTH conditional carries (the 2B landing verbatim at the tree); the file 23 lines.
- VOTE-ACK.HTML'S FOUR-ARM BRANCH: :5 — next_url / done_url / deliberate / the fetch; the deliberate arm BETWEEN done_url and the fetch; BOTH LINKS STATIC from the stem (`href="/runs/{{ stem }}/pairs"` + `href="/runs/{{ stem }}/done"`); the fetch line BYTE-UNCHANGED inside its else arm; the ack-line :3 + the echo :4 byte-standing above the branch; the :1 comment names the FOUR arms (the 3B landing verbatim); the file 6 lines.
- THE FOUR ARCS AT THEIR NAMES (test_web_face.py, the set comment :454-457 citing donedetourspec §4): test_vote_chain_carry_next_pair (:460 — BOTH conditional fields asserted at the card :465-466, the head's judge URL :475 autoescaped, the P02 dropped + the swap carried at the second hop :500, no fetch div :477/:501, the picker link absent :478); test_vote_chain_carry_done_link (:504 — "the list has ended" :515 + the done link :516, no fetch div :517, next-pair absent :518); test_deliberate_vote_stays_put (:522 — the datum's field asserted :527, `name="chain"` ABSENT :528, the confirmation :535 + the stay-put teaching :536 + BOTH links exact :537-538, no fetch div :539, the idempotent re-cast's echo :550 at the SAME stay-put form); test_deliberate_vote_stays_put_at_the_done_queue (:557 — the human+llm corroborated queue :561-565, the confirmation :572 + the echo :573 + the teaching :574 + both links :575-576, the fetch div dead :577). THE HX-REDIRECT-ABSENT ASSERTIONS verified at :540, :554, and :578 — the bounce dead at both queues.

THE FOUR FENCES (each at the bytes):
1. THE SITTING'S TWO-STEP CHAIN BYTE-STANDING: the fetch div's bytes identical to the spec's BEFORE inside its else arm; the existing arc test_vote_then_pair_chain byte-standing at :437-451 (the fetch div's three attrs :445-447, the served fragment :449-451) — the sitting lane's proof never re-counted, never touched.
2. THE NO-ANCHORING LAW: the deliberate arm renders NO counts (one teaching line + two static links, never a number); the handler's arm computes NOTHING (the pass at :1209 — no queue reads at the arm; the manifest read at :1187 the pre-existing labels need at every lane); the sitting arc's "count" not in at :448 standing.
3. THE FRAGMENT'S DONE EDGE UNTOUCHED: web.py:1103-1104 — `if body.get("done"): return Response(status_code=_OK, headers={"HX-Redirect": f"/runs/{stem}/done"})` — byte-standing, unreachable from the deliberate lane (the arcs' absent-redirect assertions the proof).
4. THE PICKER'S LINKS UNTOUCHED: picker.html:6-7 — the bare links, no datum, no drift; the picker arcs standing and green in my 480 run (test_sitting_lists_the_pair_picker :854, test_picker_page_lists_the_pairs :867, test_deliberate_pair_card_either_presentation :878).

THE SEVEN-DISPATCH CHAIN'S HONEST RECORDS (every read-back vs the tree):
- STEP 1 (web.py): :1192 / :1206-1209 / :1222 / :888 ALL EXACT at my reads; both docstrings grown (the vote's deliberate account :1145-1151 beside the standing chain-form sentence; the judge's datum pass-through :836-840 beside the chain param's :831-835); ruff + pyright green (my whole-tree runs the standing proof).
- STEPS 2/2B (pair.html): :12/:13 + the :1 comment — all verbatim at the tree; 23 lines (22 -> 23 as claimed).
- STEPS 3/3B (vote-ack.html): :5's branch + the :1 comment — all verbatim; 6 lines.
- STEP 4a (test_web_face.py): the four arcs :460-578, the header map :22 grown ("the chain-carry links, the deliberate stay-put at both queues" inserted into the fragment-arcs line), the file 1247 lines (1119 -> 1247 as claimed).
- STEP 4b (the floor): the three acts — my re-run matches all three verbatim (480 / All checks passed! / 0 errors, 0 warnings, 0 informations).
- THE HONEST NOT-DONES: steps 2 and 3's deferred :1 comments cured by 2B/3B — the chain honest, the tree whole.
- TWO STALE LINE-PINS NAMED (never hidden): (a) step 1's done-edge pin ":1097-1098" vs the tree's :1103-1104 — stale by step 1's OWN +6 judge-route growth above the edge (the docstring +5, the context +1); the edge's BYTES untouched, the substance true. (b) step 4a's and FR-MEM-0045's ":97" for the file's cycle-naming comment vs the tree's :98 (`_IMPORT_PROBE = "import prioritree.service"  # service-first — the standing import cycle resolves this order alone`) — stale by the patch's own +1 header-line growth; the FR's trace pins (test_web_face.py:56, web.py:74, service.py:729) ALL EXACT, the substance true. Both blemishes the reporters' own edits shifting the lines after the pinning — the bytes true at every claim.

FR-MEM-0045'S CLAIM VERIFIED: the file-only cycle PRE-EXISTING at web.py:74-75 (`from prioritree.service import ESCALATION` :74 + `from prioritree.service import app as service_app` :75) <-> service.py:729 (`from prioritree.web import web_app`), NOT the patch's (the done-detour touched no import lines — web.py's edits the handler/docstring/context bytes; test_web_face.py's the header map + arcs; the templates carry no imports); the single-file refusal honest (the full battery warms the cycle at collection — my 480-green run the proof); the entry stands open, correctly filed (tool-usage / interface-cost, medium / immediate).

TWO OBSERVATIONS FOR THE COORDINATOR (out of this packet's fence, named never hidden):
- THE README'S FLOOR CLAIMS NOW TRAIL THE LIVED FLOOR: README:61 + :322 both read "The quality floor: 476 tests green, pyright clean, ruff clean." — the done-detour's +4 lifts the lived floor to 480; the claims lane (the honest-docs law) now stale — the cure outside this packet's four-step fence, the coordinator's call.
- THE SPEC'S COUNT-DERIVATION BLEMISH: §4's "the floor 475 -> the grown count 480 (475 + the four new arcs)" — 475+4=479; the derivation carried the pre-micro-set floor. The lived floor at build time was 476 (the R3 README cure's own account), and the build's honest accounting (476 standing + the four new arcs = 480) EXACT — the landed count 480 confirmed at my run either way.

THE VERDICT: GREEN — the cure works at the runtime's word. The floor 480 confirmed at my own run; ruff and pyright at zero findings; every spec clause verified at the bytes; the four fences held; the seven-dispatch chain's records honest (two stale line-pins named, the bytes true at every claim); FR-MEM-0045's core claim verified. The done-detour's bounce is dead at both queues, the sitting lane's two-step chain byte-standing, the picker untouched.

— kensho (検証), the verification whole; the instruments my own runs, every clause at the tree's bytes; this report the packet's only write.
