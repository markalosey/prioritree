<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — build/done-detour

**Route:** prioritree-polish (executing) | **Events:** 11 | **Reports:** 8

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-27T03:19:29Z |
| 2 | report | jikko | 2026-11-27T16:00:28Z |
| 3 | report | jikko | 2026-11-27T16:03:48Z |
| 4 | report | jikko | 2026-11-27T16:05:01Z |
| 5 | report | jikko | 2026-11-27T16:07:16Z |
| 6 | report | jikko | 2026-11-27T16:11:35Z |
| 7 | report | jikko | 2026-11-27T16:45:48Z |
| 8 | report | jikko | 2026-11-27T16:49:14Z |
| 9 | dispatch | shinko | 2026-11-27T16:59:02Z |
| 10 | result | shinko | 2026-11-27T16:59:02Z |
| 11 | report | jikko | 2026-11-27T17:01:56Z |
## Reported by jikko — 2026-11-27T16:00:28Z

jikko step 1/4 — build/done-detour, web.py ALONE (§1a/b/c/d + §2a): landed in six hunks, patch zero findings; ruff "All checks passed!", pyright 0 errors 0 warnings at the unit.
- datum read (:1192): `deliberate = str(form.get("deliberate", "")).strip()` — beside the chain read :1191, the composed order chain -> datum -> fetch; the chain lane byte-standing (a chain form carrying both fields takes the chain arms, the datum discarded).
- stay-put arm (:1206-1209): `elif deliberate:` + `pass` — queue-blind, nothing computed, no fetch, the fragment never called; the spec's one-line trailing comment re-flowed ABOVE the pass, TEXT VERBATIM (E501 at line-length 120 — no ignore taken, the zero-findings bar held).
- ack context (:1222): `"deliberate": deliberate,` after done_url; judge route (:888): `"deliberate": "true",` beside `"chain": chain,` — the route's own knowledge, never a query param.
- both docstrings grown: the vote's bare-lane account beside the standing chain-form sentence; the judge's datum pass-through beside the chain param's own.
- untouched: the sitting fetch lane, the chain carry, the fragment's done edge (:1097-1098 — pin drifted from the spec's :1082-1083, verified at the tree), the picker's links.
- NOT done (never mine this dispatch): pair.html + vote-ack.html + the four arcs (steps 2-4), the pytest floor run (the floor act + kensho's verify the coordinator's).
## Reported by jikko — 2026-11-27T16:03:48Z

STEP 2/4 (jikko; R8 file-unit web/templates/pair.html alone): the deliberate conditional carry landed — inserted directly below :12, the spec §2b's fenced bytes exact; the patch clean, zero findings; the file 22 → 23 lines.
READ-BACK at :12-:13 — BEFORE: :12 `{% if chain %}<input type="hidden" name="chain" value="{{ chain }}">{% endif %}` (the region's last hidden field); AFTER: :12 the chain line byte-unchanged + :13 `{% if deliberate %}<input type="hidden" name="deliberate" value="{{ deliberate }}">{% endif %}`.
NOT DONE (honest): §2b's :1 comment growth (naming BOTH conditional carries) NOT landed — the dispatch's scope ("the conditional hidden field alone, NOTHING else") read as excluding it while the spec's §6 step-2 includes it; no later step touches pair.html — left to the coordinator's call.
THE CARRY LANDS AT THE POST: step 1's pins re-read at the bytes this pass (web.py:888 `"deliberate": "true"` in the judge context; the datum read :1192; the stay-put arm :1206-1209) — the judge page's form carries both conditionals, the arm fires.
FILES: web/templates/pair.html alone; no other file touched, no instrument run (the coordinator's lane).
## Reported by jikko — 2026-11-27T16:05:01Z

STEP 2B — pair.html :1 comment growth landed exactly as §2b fenced (the both-carries naming — the template's head comment grown beside the chain carry); ONE line, nothing else touched.
READ-BACK BEFORE (:1): <!-- pair — the shared pair region: the sitting includes it, the fragment route serves it (web-brief §4 routes 2+7; the design §7a; the voter-session spec §3b) -->
READ-BACK AFTER (:1): <!-- pair — the shared pair region: the sitting includes it, the fragment route serves it (web-brief §4 routes 2+7; the design §7a; the voter-session spec §3b); the page's TWO conditional carries: the chain (the ack-carry's remaining list) + the deliberate (the lane's own datum — the done-detour cure) -->
Applied cleanly; the tree re-read confirms the byte-exact AFTER at :1, the :12/:13 conditional carries byte-standing; gaps none; not done nothing — this was the one line.
## Reported by jikko — 2026-11-27T16:07:16Z

STEP 3/4 (jikko; R8 file-unit web/templates/vote-ack.html alone): the deliberate arm landed at :5 — inserted BETWEEN the done_url arm and the fetch's else arm, §3b's fenced bytes exact; the patch clean, zero findings; the file still 6 lines.
READ-BACK :5 AFTER (the whole branch): {% if next_url %}<p><a class="next-pair" href="{{ next_url }}">next pair -></a></p>{% elif done_url %}<p class="quiet">That was the last pair on this card — the list has ended; every judgment is recorded.</p><p><a href="{{ done_url }}">the done page</a></p>{% elif deliberate %}<p>Recorded. Judge the next pair from the picker, or close out the sitting at the done page.</p><p><a href="/runs/{{ stem }}/pairs">the pair picker</a> <a href="/runs/{{ stem }}/done">the done page</a></p>{% else %}<div hx-get="/ui/runs/{{ stem }}/pair{% if swap %}?swap=true{% endif %}" hx-trigger="load" hx-target="#pair-region" hx-swap="outerHTML"></div>{% endif %}
FENCES HELD: the fetch line byte-unchanged inside its else arm; the ack-line :3 + the echo :4 byte-standing above; the no-anchoring law — no counts, no queue reads, both links static from {{ stem }} (/runs/{{ stem }}/pairs + /runs/{{ stem }}/done).
NOT DONE (honest): §3's :1 comment growth (the FOUR arms' naming) NOT landed — the dispatch's scope ("the deliberate branch alone, NOTHING else") read per the 2b precedent; left to the coordinator's call.
FILES: web/templates/vote-ack.html alone; no instrument run (the coordinator's lane); no other file touched.
## Reported by jikko — 2026-11-27T16:11:35Z

STEP 3B — vote-ack.html :1 comment growth landed per the spec §3's fence (the FOUR-arms naming; step 3's dispatch-fence excluded, the 2b precedent; ONE line, nothing else).
BEFORE: <!-- vote-ack — the verdict restated in item-label terms + the embedded pair fetch (web-brief §4 route 8; the design §7a) -->
AFTER: <!-- vote-ack — the verdict restated in item-label terms + the embedded pair fetch (web-brief §4 route 8; the design §7a); the FOUR arms: the chain link / the done link + list-ended / the deliberate stay-put (the done-detour cure) / the fetch -->
Lines :2-:6 byte-standing (the ack-line, the echo, the deliberate branch, the fetch line untouched); read-back verbatim from the disk this pass.
## Reported by jikko — 2026-11-27T16:45:48Z

R11 — jikko, step 4a of 4 (build/done-detour): ONE FILE patched — tests/test_web_face.py (1119 -> 1247 lines): the header's map grown per §4 (:22 — "the chain-carry links, the deliberate stay-put at both queues" inserted into the fragment-arcs line) + the four lane-separation arcs landed beside the byte-standing sitting arc (test_vote_then_pair_chain untouched) at :460-578, a one-line set comment citing donedetourspec §4.
ARC 2 test_vote_chain_carry_next_pair — hop 1 at the canonical chain form (the judge page asserts BOTH conditional fields: `name="chain" value="P02,P03"` + `name="deliberate" value="true"`): the ack links the head's judge URL `href="/runs/RUN-0001/pair?item_a=a&amp;item_b=c&amp;chain=P02,P03"` (the autoescaped served bytes — verified at the installed Starlette's select_autoescape, templating.py:95), `next-pair` present, `'hx-get="/ui/runs' not in first.text`, the picker link ABSENT (the datum read and discarded at the chain lane); hop 2 via a second TestClient at the swapped head's page: "You preferred three (A) over one (B)." + `href="/runs/RUN-0001/pair?item_a=b&amp;item_b=c&amp;swap=true&amp;chain=P03"` — the just-voted P02 DROPPED, the shrunken chain riding, the swap knob carried, no fetch div.
ARC 3 test_vote_chain_carry_done_link — the chain's empty rest: "the list has ended" + `href="/runs/RUN-0001/done"`, NO fetch div, `next-pair` absent, the picker link absent.
ARC 4 test_deliberate_vote_stays_put — the picker-sourced judge page (the datum's hidden field asserted, `name="chain"` ABSENT) -> the bare deliberate POST: "You preferred one (A) over two (B)." + "Recorded. Judge the next pair from the picker, or close out the sitting at the done page." + BOTH links in their exact forms (`href="/runs/RUN-0001/pairs"` + `href="/runs/RUN-0001/done"`), `'hx-get="/ui/runs' not in response.text`, `"hx-redirect" not in response.headers`; the idempotent re-cast renders "already recorded with the same answer" at the SAME stay-put form (the fragment-token law per the school).
ARC 5 test_deliberate_vote_stays_put_at_the_done_queue — the fully-corroborated run (the existing HX-Redirect arc's own human+llm setup): the restatement "You preferred alpha (A) over bravo (B)." + the echo + the stay-put teaching + both links, and `"hx-redirect" not in response.headers` ASSERTED — the bounce dead, the fragment never called.
THE FINDING CHECK (this file's suite alone, the dispatch's grant): collection REFUSED at a PRE-EXISTING standing cycle (web.py:74-75 <-> service.py:729; the isort-mandated web-first :56) — independent of this patch (no imports touched; the file's own :97 names the cycle); filed FR-MEM-0045 (tool-usage/interface-cost: the single-file run unrunnable since the mount landed; no in-fence cure at zero findings — F401/I001 both block; the lazy-import cure lives in web.py/service.py, out of this one-file dispatch).
NOT DONE: the floor (uv run pytest / ruff / pyright whole) — 4b's, never this step's; web.py/pair.html/vote-ack.html read, never edited by me; the arcs' green proof rides 4b's full floor (the whole battery warms the cycle at test_service_face.py:37 — the 475->480 expectation intact at the standing setup).
## Reported by jikko — 2026-11-27T16:49:14Z

STEP 4B (jikko) — the three acts, outcomes verbatim:
1. TEST (full suite): "480 passed in 42.15s" — count 480 matches the named expectation (476 standing + the four new arcs)
2. LINT (ruff): "All checks passed!"
3. TYPECHECK (pyright): "0 errors, 0 warnings, 0 informations"
No failures landed; nothing fixed outside the fence; no files touched (instrument run only).
## Reported by jikko — 2026-11-27T17:01:56Z

R11 — Step 4c (build/done-detour, jikko, 2026-11-27): README.md's two floor sites cured 476 -> 480, one patch (2 hunks), NOTHING else — pre-cure grep "476" over README.md: exactly two hits (:61, :322); post-cure: zero "476", both sites at 480 (the count re-read at the tree, never copied).
:61 BEFORE "The quality floor: 476 tests green, pyright clean, ruff clean." -> AFTER "The quality floor: 480 tests green, pyright clean, ruff clean."
:322 BEFORE "The quality floor: 476 tests green, pyright clean, ruff clean." -> AFTER "The quality floor: 480 tests green, pyright clean, ruff clean."
Claims-lane edit only — no floor re-run this step (the lived floor 480 already confirmed at both seats' instrument runs).
