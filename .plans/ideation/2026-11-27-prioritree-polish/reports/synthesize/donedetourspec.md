<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/donedetourspec

**Route:** prioritree-polish (executing) | **Events:** 5 | **Reports:** 2

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-27T01:34:06Z |
| 2 | report | togo | 2026-11-27T01:41:28Z |
| 3 | result | shinko | 2026-11-27T02:09:03Z |
| 4 | dispatch | shinko | 2026-11-27T02:18:24Z |
| 5 | report | togo | 2026-11-27T02:20:38Z |
## Reported by togo — 2026-11-27T01:41:28Z

# THE EXACT-TASK SPEC — the done-detour's build bytes (togo, 統合, packet synthesize/donedetourspec, route prioritree-polish, 2026-11-27)

THE GROUND, PINNED THIS PASS (every byte re-read at the tree, never copied): the approved unit brief (reports/synthesize/done-detour.md — G-DONE-DETOUR-BRIEF green); web.py's judge route :792-869 (the chain pass-through :847, the context :867), the fragment's done edge :1078-1103 (the redirect :1082-1083), the vote POST :1106-1190 (the chain read :1163, the chain region :1164-1176, the ack context :1177-1190); pair.html whole (:1's comment, :12's chain carry); vote-ack.html whole (:1's comment, :3's ack-line, :4's echo, :5's arms); picker.html:6-7 (the bare links — UNTOUCHED); sitting.html:16/:21 (the include + the picker); test_web_face.py (the header's map :2-38, the constants :60-96, the scrapers, the two-step arc :424-438, the HX-Redirect arc :471-481, the deliberate arcs :714-782); the suite re-run at the tree this pass: 475 PASSED (the floor's live proof, the claims lane — never copied); the no-chain-arcs record: NO `next-pair`/`next_url`/`name="chain"`/`&chain=` match anywhere in test_web_face.py (grep this pass — the chain arms carry NO arcs today; the lane-separation proof lands them whole). G-DONEDETOURSPEC-BRIEF's three conditions (the store's junro.json) — the bytes whole (§1-§4), the four constraints fenced (§5), the per-step plan (§6). READ-ONLY held — this report the packet's only write; the synthesis rules, never decides: the approval the collaborator's.

## 1. THE HANDLER'S BEFORE/AFTER (web.py's vote POST :1106-1190)

**(a) THE LANE DATUM'S READ — the POST's read order: chain -> datum -> fetch.**

BEFORE (:1163):
    chain = str(form.get("chain", "")).strip()

AFTER (the datum read inserted directly beside :1163 — BEFORE the arms, so the composed order reads chain first, datum second):
    chain = str(form.get("chain", "")).strip()
    deliberate = str(form.get("deliberate", "")).strip()

The fetch arm's condition remains the composition's ELSE — the bare fall-through when neither field is present (the sitting lane). NO new fetch-side code; NO call to /next; the fragment route NEVER called at the deliberate lane — the bounce's root dead (the done edge :1082-1083 unreachable from this arm).

**(b) THE BARE-LANE BRANCH — the stay-put arm, inserted after the chain block (:1176), before the context build.**

BEFORE (:1164-1176, BYTE-STANDING — untouched):
    next_url = ""
    done_url = ""
    if chain:
        schedule = _scheduled_pairs(manifest.json())
        voted_a, voted_b = sorted(payload["pair"])
        just_token = f"P{schedule.index((voted_a, voted_b)) + 1:02d}"
        rest = [token for token in (part.strip() for part in chain.split(",")) if token and token != just_token]
        if rest:
            head = schedule[int(rest[0][1:]) - 1]
            swap_form = "&swap=true" if presentation == PRESENTATION_SWAPPED else ""
            next_url = f"/runs/{stem}/pair?item_a={head[0]}&item_b={head[1]}{swap_form}&chain={','.join(rest)}"
        else:
            done_url = f"/runs/{stem}/done"

AFTER (the chain block's `done_url = f"/runs/{stem}/done"` grows an `elif deliberate:` beside the same indent — the datum NEVER reaching the chain arms; the arm renders NOTHING computed — no fetch, no redirect, both links composed from the stem at the TEMPLATE, never the handler):
        else:
            done_url = f"/runs/{stem}/done"
    elif deliberate:
        pass  # the stay-put arm: the bare deliberate lane — the ack template renders the confirmation + both links (queue-blind, static from the stem); no fetch, no redirect

**(c) THE CONTEXT'S ARM MARKER (:1177-1190) — the arm's key added beside next_url/done_url.**

BEFORE (:1180-1189):
            "swap": presentation == PRESENTATION_SWAPPED,
            "next_url": next_url,
            "done_url": done_url,

AFTER:
            "swap": presentation == PRESENTATION_SWAPPED,
            "next_url": next_url,
            "done_url": done_url,
            "deliberate": deliberate,

**(d) THE SITTING + CHAIN LANES BYTE-STANDING.** The fetch's condition (the template's else arm) untouched; the chain's carry (the read :1163, the block :1164-1176, the judge route's :847/:867 pass-through) untouched — the datum read AFTER the chain in order, so a chain form carrying both fields takes the chain arms (the datum read and discarded at that lane); the sitting lane (both fields absent) falls to the fetch exactly as today. The vote docstring (:1108-1133) GROWS the deliberate arm's account (the datum's read, the stay-put form, both links, queue-blind, no fetch at the bare lane — composed beside the standing chain-form sentence at :117-124).

## 2. THE PAIR CONTEXT'S BEFORE/AFTER (the judge route :792-869 + pair.html)

**(a) THE ROUTE'S CONTEXT :847/:867 — the datum passed beside "chain".**

BEFORE (:847 + :867):
    chain = request.query_params.get("chain", "").strip()
    ...
            "chain": chain,

AFTER:
    chain = request.query_params.get("chain", "").strip()
    ...
            "chain": chain,
            "deliberate": "true",

The datum is the ROUTE's own knowledge — the constant `"true"` passed at every judge-page render (BOTH the bare form and the chain form ride it; the chain is the sequence over the lane, read at the POST after the chain). NEVER a query param: the picker's links (:6-7) BYTE-UNTOUCHED — no link drift, no new teaching at the picker. The sitting page and the fragment-served region (no datum in their contexts) render byte-identical to today — the field's template guard renders nothing at absent/empty. The judge docstring (:801-830) GROWS the datum's pass-through sentence (beside the chain param's own :816-820).

**(b) THE TEMPLATE'S CONDITIONAL CARRY (pair.html :12's pattern, the identical form).**

BEFORE (:12):
    {% if chain %}<input type="hidden" name="chain" value="{{ chain }}">{% endif %}

AFTER (inserted directly below :12):
    {% if chain %}<input type="hidden" name="chain" value="{{ chain }}">{% endif %}
    {% if deliberate %}<input type="hidden" name="deliberate" value="{{ deliberate }}">{% endif %}

The comment at :1 GROWS to name BOTH conditional carries (the chain + the deliberate) — the 1c-8 cure, ONE true landing, never the double-edit drift:
<!-- pair — the shared pair region: the sitting includes it, the fragment route serves it (web-brief §4 routes 2+7; the design §7a; the voter-session spec §3b); the page's TWO conditional carries: the chain (the ack-carry's remaining list) + the deliberate (the lane's own datum — the done-detour cure) -->

## 3. THE ACK TEMPLATE'S BEFORE/AFTER (vote-ack.html whole)

**(a) THE CONFIRMATION STANDING — the ack-line (:3) + the echo (:4) sit ABOVE the branch, BYTE-STANDING at every arm (grown never — the fence 4 proof lives at these bytes; nothing below touches them).**

**(b) THE BARE-LANE BRANCH (:5) — inserted BETWEEN the done_url arm and the else; the fetch line confined to its arm, BYTE-UNCHANGED.**

BEFORE (:5):
  {% if next_url %}<p><a class="next-pair" href="{{ next_url }}">next pair -></a></p>{% elif done_url %}<p class="quiet">That was the last pair on this card — the list has ended; every judgment is recorded.</p><p><a href="{{ done_url }}">the done page</a></p>{% else %}<div hx-get="/ui/runs/{{ stem }}/pair{% if swap %}?swap=true{% endif %}" hx-trigger="load" hx-target="#pair-region" hx-swap="outerHTML"></div>{% endif %}

AFTER (the arm order: next_url / done_url / deliberate / the fetch — §3's ruling):
  {% if next_url %}<p><a class="next-pair" href="{{ next_url }}">next pair -></a></p>{% elif done_url %}<p class="quiet">That was the last pair on this card — the list has ended; every judgment is recorded.</p><p><a href="{{ done_url }}">the done page</a></p>{% elif deliberate %}<p>Recorded. Judge the next pair from the picker, or close out the sitting at the done page.</p><p><a href="/runs/{{ stem }}/pairs">the pair picker</a> <a href="/runs/{{ stem }}/done">the done page</a></p>{% else %}<div hx-get="/ui/runs/{{ stem }}/pair{% if swap %}?swap=true{% endif %}" hx-trigger="load" hx-target="#pair-region" hx-swap="outerHTML"></div>{% endif %}

BOTH LINKS STATIC from `{{ stem }}` (NO handler URL computation at this arm; NO counts rendered — the no-anchoring law held; the open-vs-exhausted conditions live with the judge, never the POST). The comment at :1 GROWS to name the FOUR arms:
<!-- vote-ack — the verdict restated in item-label terms + the embedded pair fetch (web-brief §4 route 8; the design §7a); the FOUR arms: the chain link / the done link + list-ended / the deliberate stay-put (the done-detour cure) / the fetch -->

## 4. THE ARCS (test_web_face.py — the lane-separation set, five arcs, each fenced by name)

**ARC 1 — THE SITTING LANE'S SEPARATION ARC** (the byte-standing proof; today's two-step arc :424-438 ALREADY asserts the sitting lane's fetch — the lane-separation set lands the sibling arcs beside it, the sitting arc itself byte-standing as the existing test_vote_then_pair_chain). No new sitting arc: the existing arc IS the lane's proof; the set's siblings are new.

**ARC 2 — THE CHAIN LANE'S SEPARATION ARC (next_url)**: `test_vote_chain_carry_next_pair` — a chain vote (the datum also carried — the chain form's own field order) -> the ack renders `next-pair` at the head's judge URL (the P-token dropped, the swap knob carried when the page's mode is swapped, the shrunken chain riding the URL); NO fetch div rendered. [NO chain arcs exist today — the record held at this pass's grep; the arcs land whole.]

**ARC 3 — THE CHAIN LANE'S SEPARATION ARC (empty-rest done_url)**: `test_vote_chain_carry_done_link` — the chain's empty rest -> `done_url` + the list-ended teaching ("the list has ended"); NO fetch div.

**ARC 4 — THE BARE DELIBERATE ARC**: `test_deliberate_vote_stays_put` — the picker-sourced vote (the datum carried via the judge page's hidden field — scraped from the judge page's form; the chain absent) -> the stay-put arm: the confirmation rendered (the ack-line's restatement "You preferred one (A) over two (B)." + NO hx-get div + NO HX-Redirect) + BOTH links in their exact forms (`href="/runs/{stem}/pairs"` + `href="/runs/{stem}/done"`); the idempotent re-cast renders the acknowledged echo ("already recorded with the same answer") at the same stay-put form.

**ARC 5 — THE EXHAUSTED-QUEUE DELIBERATE ARC**: `test_deliberate_vote_stays_put_at_the_done_queue` — the same stay-put form at the exhausted queue (every pair at quorum AND corroborated — the two-class corroboration composed exactly as the existing HX-Redirect arc :471-481 sets its state: the human + the llm votes) -> the same confirmation + both links; the bounce dead — `"hx-redirect" not in response.headers` ASSERTED (the POST's own response never carries the redirect; the fragment never called).

THE COUNT EXACT (re-derived at the tree this pass): the floor 475 -> the grown count 480 (475 + the four new arcs [arcs 2-5]; arc 1 byte-standing as the existing sitting test — never re-counted). The header's map (:2-38) GROWS the lane-separation naming (the honest-docs law: the fragment arcs' line re-worded to carry "the two-step chain, the chain-carry links, the deliberate stay-put at both queues, the HX-Redirect").

## 5. THE NO-BREAK PROOFS — the four fences held (each asserted at the spec's own bytes)

- FENCE 1 — THE SITTING LANE'S TWO-STEP CHAIN UNTOUCHED: the fetch's condition (§3b's else arm, byte-unchanged) + the existing sitting arc (:424-438) byte-standing + ARC 1's proof — the sitting-sourced vote renders the fetch div exactly as today.
- FENCE 2 — THE NO-ANCHORING LAW: the stay-put arm renders NO counts (§3b's exact bytes — two links, one teaching line, never a number); the arm's handler branch computes NOTHING (§1b's `pass` — the links composed at the template from the stem); the existing no-anchoring pins (byte-level) stand.
- FENCE 3 — THE FRAGMENT'S SITTING-SERVING DONE EDGE UNTOUCHED: :1082-1083 never edited (§1a — the fragment route NEVER called at the deliberate lane; the edge stays the sitting lane's own); ARC 5's `hx-redirect` absence asserted at the POST's own bytes.
- FENCE 4 — THE CONFIRMATION STANDING AT THE DELIBERATE LANE: :3/:4 byte-standing (§3a — grown never); ARC 4/5 assert the restatement + the echo at the stay-put form.
- THE PICKER'S LINKS UNTOUCHED: picker.html:6-7 never edited (§2a — the datum the ROUTE's own knowledge, never a query param); the existing picker arcs (:714-735) byte-standing.
- THE CHAIN LANE BYTE-STANDING: :1164-1176 (§1b), :847/:867's chain pass-through, pair.html:12 — untouched; ARCS 2-3 land the carry's first-ever proof.

## 6. THE PER-STEP PLAN (R8, the file-units — FOUR dispatches, each its own)

1. **web.py** — §1a/b/c/d (the POST's datum read, the elif arm, the context marker, the docstrings' grows) + §2a (the judge route's context + docstring). Read-backs: the four edits' rendered diffs at the packet's result; ruff + pyright green at the unit.
2. **pair.html** — §2b (the conditional field + the :1 comment's cure). Read-back: the rendered judge page carrying BOTH conditional carries at the chain form.
3. **vote-ack.html** — §3 (the deliberate branch + the :1 comment's cure). Read-back: the four arms' rendered order; the fetch line byte-unchanged.
4. **test_web_face.py** — §4 (the four new arcs + the header's map grown). Read-back: the suite whole green at 480.
THEN FLOOR-GREEN (the three acts verbatim): `uv run pytest` (480 passed), `uv run ruff check src/ tests/` (zero findings), `uv run pyright` (0 errors, 0 warnings). THE CEREMONY AFTER: kensho's independent verify (validate/done-detour); MOHO'S R4 WALK at the gate (the bare deliberate vote at the completed run — the confirmation standing, both links served, no bounce); the four fences held at the build's own bytes.

— togo (統合), the spec whole; every byte fenced at the tree's own reads, the floor's number derived at the suite's live re-run (475 -> 480), the four fences composed never violated; the disk the truth; READ-ONLY held, this report the packet's only write.
## Reported by togo — 2026-11-27T02:20:38Z

# THE MICRO SET'S VERIFICATION FOLD (togo, 統合; packet synthesize/donedetourspec, route prioritree-polish, 2026-11-27) — kensho's four findings ruled one each at the bytes; jikko's overclaim named, never hidden

R1 — UNIT 10 (the spec's own conflict resolved): the fork-free law STANDING and unambiguous — pyproject:196-213 RULING R4: "the calculate engine (.opencode/scripts/calculate.py) is hikari's VERBATIM CARGO — its bytes never edited at prioritree (the delivery note's law)"; §2's unit 10 conflicted with §4's own refusal class, and the refusal class WINS — the ENGINE-side cures REFUSED, the blemish (:64 Usage, :418 Purpose, :1118 factorial help, :1122/:1123 + :1195/:1196 combination helps — all confirmed absent at my reads) named hikari's regen-lane residual (the SRI's class), carried in the record. The WRAPPER'S cure IN SCOPE: .opencode/tools/calculate.ts hand-maintained (the wrapper lane — no tree script emits it), the zod descriptions CAN carry the bound teachings under the merged-description law (one description per param NAME, collisions listing each meaning with its ops — the FR-MEM-0515 cure; each meaning free to carry its own bound); the exact bytes:
  calculate.ts:35 (n) BEFORE: "the count (an integer, as a string) (factorial); the population count (an integer, as a string) (combination, log-combination); the trial count (an integer >= 1, as a string) (wilson); the trial count (an integer >= 0, as a string) (binom-test); the count (a non-negative integer, as a string) (log-factorial)"
  calculate.ts:35 (n) AFTER: "the count (a non-negative integer, as a string) (factorial); the population count (a non-negative integer, as a string) (combination, log-combination); the trial count (an integer >= 1, as a string) (wilson); the trial count (an integer >= 0, as a string) (binom-test); the count (a non-negative integer, as a string) (log-factorial)"
  calculate.ts:37 (k) BEFORE: "the selection count (an integer, as a string) (combination, log-combination); the success count (an integer, as a string) (wilson, binom-test)" → AFTER: "the selection count (an integer <= n, as a string) (combination, log-combination); the success count (an integer, as a string) (wilson, binom-test)" — the (c) k<=n bound at its home; the KAT untouched (its rows pin op+args+result, never the helps)
R2 — THE PINS: mcp_server.py:267 "(the service.py:168-183 precedent re-carried)" → "(the service.py:291 precedent re-carried)" (render_refusal at :291, the one render point); mcp_server.py:130 "service.py:158-165" → "service.py:217-218" (same-width token swap, the wrap untouched — the objects: app = FastAPI :217, app.state.seam :218; :158-165 is RegisterRunRequest's docstring, never the precedent).
R3 — THE README'S FLOOR: README:61 + :322 "The quality floor: 475 tests green, pyright clean, ruff clean." → "The quality floor: 476 tests green, pyright clean, ruff clean." — both sites, the claims lane at the lived floor (kensho's run: 476 passed; jikko's arc the +1).
R4 — THE ENUMERATION: key_store.py:17-18 "Stdlib only (hashlib, json, os, re, secrets, datetime, pathlib)." → "Stdlib only (hashlib, json, os, re, secrets, dataclasses, datetime, pathlib, typing)." — nine roots, the told list matching the lived imports (:24-32), the tree's own docstring school.
THE OVERCLAIM NAMED: jikko's report-vs-tree divergence carried whole — item 8 claimed the engine's four cures landed (NONE at the tree); item 3 claimed the :267 pin cured (the tree still ":168-183") — the record's integrity finding, never hidden.
