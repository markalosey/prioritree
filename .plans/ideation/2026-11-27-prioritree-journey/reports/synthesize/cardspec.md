<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/cardspec

**Route:** prioritree-journey (executing) | **Events:** 3 | **Reports:** 2

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-27T20:55:43Z |
| 2 | report | togo | 2026-11-27T21:21:44Z |
| 3 | report | togo | 2026-11-27T21:23:05Z |
## Reported by togo — 2026-11-27T21:21:44Z

# THE CARD UNIT'S EXACT-TASK SPEC — PIECE 1 OF 2 (togo, packet synthesize/cardspec, route prioritree-journey, 2026-11-27)

The exact-task spec for the unit **build/card**, closing G-CARDSPEC-BRIEF at the collaborator's approval: every edit fenced at its exact bytes, every byte the R5/ASCII/ruff-ALL discipline at authoring time (the three acts: ruff zero findings, pyright 0/0, the suite green at the named count). The build dispatches cite THIS spec; this spec cites the approved unit brief (reports/synthesize/card.md — G-CARD-BRIEF green) + the design brief (reports/synthesize/journey-design.md — G-JOURNEY-DESIGN green) + the cycle's records whole (hyoka's attack — F1 the form wrapper, F2 the undo's ack home, F4 the rides binding, F5 the tie's bounds, F8 the package's binding; moho's walks — the copy's both-truths law, RUN-0009's first supersede, the flag's live seam; keisan's pricing — the floor 480 exact, the arcs +7-10; shindan's residuals — the discoverability wall, the tie's 0/319). READ-ONLY held; this report the packet's only write. Nothing decided here that is the collaborator's to decide.

## 0. THE GROUND (read whole this pass; every pin re-verified at the tree's CURRENT bytes — the regen-drift lesson held)

THE FLOOR VERIFIED AT THE ENGINE THIS PASS: 480 passed — keisan's baseline confirmed exact, no drift; the count's fence at 6 prices against THIS number. THE SIX FILES' CURRENT BYTES: pair.html 23 lines (the form :3, the conditional ask :4-7, the five stamps :8-13, the display-only sl-cards :14-17, the marker-named verdict row + the labels dict :18-21); sitting.html 23 (the h1 question :5, the include :16, the PLAIN ack-region div :17); vote-ack.html 6 (the label-first restatement :3, the acknowledged echo :4, the four arms :5); app.css 32 (--pt-gap :2, .wrap 40rem :4, .cards :9, .pair-card :10, .card-label :11, .verdicts :12, button.verdict :13); web.py 1290 (the guard's ONE read lane :276-291, the sitting render :638-722 with question :711, the judge route :807-890 with question :877 + deliberate "true" :888, the fragment route :1080-1124 — the /next consult :1099, the context :1110-1123 carrying NO question and NO carries, the fresh mint :1115, the vote route :1127-1224 — the parse :1162-1176, the payload :1177-1183, the service POST :1184, the refusal-to-ack-region separation :1185-1186, the chain/deliberate arms :1191-1209, the ack context :1210-1224 with acknowledged :1216); test_web_face.py 1247 lines / 68 arcs (the client fixture :102-113, _scrape_csrf :116-131, _FORM_VOTE :71). THE WIRE'S LAWS RE-PINNED: votes.py :578 the supersedes optional-text (absent/empty => None), :597-603 the run's OWN declared set, :613-614 the positional swap, :617-652 the supersede door (same run, SAME PAIR, the author's own hand — SupersedeRefusedError before any byte lands), :653-662 the dedup key (carries supersedes), :663-667 the LOUD ack (the original handle, the unchanged count, acknowledged=True); tally.py :165-183 the weighting walk (E = {r.supersedes}, the superseded excluded, the correction counted — the cell's weight unchanged); service.py :180-207 CastVoteRequest already carries supersedes (str | None) + :597 the door passes body.supersedes + :606 the ack object {vote_id, count, acknowledged} — THE WEB LANE'S READ RIDES AT $0 WIRE BYTES; registry.py :259 the register REFUSES any declared set beyond the constant triple — the two-verdict loop truth's school the template's own render (fenced at 6). THE STANDING RULINGS (pyproject.toml): line-length 120; select ALL; web.py = BLE001/S105/PLR0911/C901 (byte-standing, NO new entry — the card unit carries NO new ruling); tests/** = S101/PLR2004; test_web_face.py = S603/S607; tests/conftest.py = F401 (the BRIDGE's ruling, never here); the implicit-concat precedent web.py:148-152 (the multi-line parenthesized f-string form the tree's own green school); the ASCII law's form (the lifecyclespec precedent): the growth matches each FILE'S OWN bytes — the em-dash the tree's own copy byte (pair.html:5, vote-ack.html:4, web.py's docstrings), NO new multibyte class any file does not already own. base.html: the Shoelace autoloader + htmx 2.0.7 (the fragment lane htmx-required by construction — the undo's no-JS state the tier's own truth).

## 1. src/prioritree/web.py — THE FOUR SEAMS (dispatch 1; all additive, the suite green at the landing)

### 1a. THE PAIR FRAGMENT ROUTE — the cited re-serve branch + the question thread

before (:1080-1081, the signature):
```python
@web_app.get(_PAIR)
async def pair(request: Request, stem: str, *, swap: bool = False) -> Response:
```
after (the signature grows the citation params — the judge route's own form :811-812; FIVE arguments, the PLR0913 bar held; the carries read from the request's query — the judge route's chain precedent :867):
```python
@web_app.get(_PAIR)
async def pair(request: Request, stem: str, item_a: str = "", item_b: str = "", *, swap: bool = False) -> Response:
```
the route's body after (the whole region :1099-1124 replaced; the /next lane's consult order + the done-edge + the refusal order BYTE-STANDING — the cited branch only SKIPS the /next block):
```python
    supersedes = request.query_params.get("supersedes", "").strip()
    deliberate = request.query_params.get("deliberate", "").strip()
    chain = request.query_params.get("chain", "").strip()
    cited = bool(item_a.strip() and item_b.strip())
    if not cited:
        nxt = await _service("GET", f"/runs/{stem}/next?swap=true" if swap else f"/runs/{stem}/next")
        if nxt.status_code != _OK:
            return _refuse_fragment(request, _fields(nxt.json()), fold=nxt.status_code == _CRASH)
        served = nxt.json()
        if served.get("done"):
            return Response(status_code=_OK, headers={"HX-Redirect": f"/runs/{stem}/done"})
    manifest = await _service("GET", f"/runs/{stem}/manifest")
    if manifest.status_code != _OK:
        return _refuse_fragment(request, _fields(manifest.json()), fold=manifest.status_code == _CRASH)
    manifest_body = manifest.json()
    labels = _labels(manifest_body)
    if cited:
        presented_a, presented_b = item_a.strip(), item_b.strip()
        presentation = PRESENTATION_SWAPPED if presented_a > presented_b else PRESENTATION_CANONICAL
    else:
        presented_a, presented_b = str(served["item_a"]), str(served["item_b"])
        presentation = str(served["presentation_order"])
    return templates.TemplateResponse(
        request,
        "pair.html",
        {
            "stem": stem,
            "csrf_token": _mint_bound(f"/ui/runs/{stem}/vote", request),
            "remembered_name": _remembered(request),
            "question": str(manifest_body["question"]),
            "item_a": presented_a,
            "item_b": presented_b,
            "label_a": labels.get(presented_a, presented_a),
            "label_b": labels.get(presented_b, presented_b),
            "presentation_order": presentation,
            "verdicts": list(manifest_body["verdicts"]),
            "supersedes": supersedes,
            "deliberate": deliberate,
            "chain": chain,
        },
    )
```
THE CITED BRANCH'S LAWS: the pair AS CITED per the judge route's citation law (:841-843 — a mangled citation renders honestly, the vote's legality the wire's act); NO next consult (the no-anchoring law held — the pair as cited whatever the coverage); the presentation DERIVED from the cited order (the reversed citation the explicit swapped presentation — the fieldless swap never served; the derivation composes legal at the wire by the canonical-sorted law the chain arm itself rides at :1197); the question threaded at EVERY serve (the legend's context — the fragment's own h1 absent); the fresh token minted (:1115's law byte-standing). The route's docstring re-derived (the honest-docs law) — the Purpose grows, inserted before the standing /next sentences: "TWO SERVE LANES. THE CITED RE-SERVE (the undo's lane, the cardspec): item_a/item_b both present => the CITED pair rendered per the judge route's citation law (the wire the sole validator: a mangled citation renders honestly, the vote's legality the wire's act) — NO next consult (the pair as cited, whatever the coverage; the no-anchoring law held), the presentation DERIVED from the cited order (the reversed citation the explicit swapped presentation — the fieldless swap never served); the supersedes/deliberate/chain query carries ride the re-served form's hidden fields (the undo's supersede carry + the lane's own datum, read from the request's query — the judge route's chain precedent); the fresh token minted, the question threaded (the legend's context — the fieldset binding the pair's question at EVERY serve). THE /NEXT SERVE (the defining call when no pair cited): consume next (+ the manifest's label map) ..."; the Provenance's tail grows: "... the journey design 1.1/1.4 + the cardspec (the cited re-serve, the question thread, the carries), G-CARDSPEC-BRIEF."

### 1b. THE VOTE ROUTE'S SUPERSEDES READ (the payload's one field — the absent=>None form)

before (:1177-1183):
```python
    payload = {
        "pair": [str(form.get("item_a", "")), str(form.get("item_b", ""))],
        "winner": str(form.get("winner", "")),
        "comparator_id": name,
        "comparator_class": str(form.get("comparator_class", "human")),
        "presentation_order": presentation,
    }
```
after (the field at the optional-text form — absent/empty/whitespace => None, the wire's own schema votes.py:578; the parse order unchanged — the sessioned name :1163-1175, the presentation :1176, the payload, the service POST :1184):
```python
    payload = {
        "pair": [str(form.get("item_a", "")), str(form.get("item_b", ""))],
        "winner": str(form.get("winner", "")),
        "comparator_id": name,
        "comparator_class": str(form.get("comparator_class", "human")),
        "presentation_order": presentation,
        "supersedes": str(form.get("supersedes", "")).strip() or None,
    }
```

### 1c. THE ACK CONTEXT — the vote_id + the undo's citation fields (the acknowledged seam's both states)

before (:1210-1224):
```python
    return templates.TemplateResponse(
        request,
        "vote-ack.html",
        {
            "stem": stem,
            "winner": payload["winner"],
            "acknowledged": bool(outcome.json()["acknowledged"]),
            "label_a": labels.get(payload["pair"][0], payload["pair"][0]),
            "label_b": labels.get(payload["pair"][1], payload["pair"][1]),
            "swap": presentation == PRESENTATION_SWAPPED,
            "next_url": next_url,
            "done_url": done_url,
            "deliberate": deliberate,
        },
    )
```
after (four fields grown — vote_id the cast outcome's OWN handle (the ORIGINAL at the idempotent arm, votes.py:667 — the undo target honest at both flag states); item_a/item_b the pair AS PRESENTED (the mirror's order — the undo cites what the human saw); chain the raw carry (the chain arm's re-serve); the acknowledged line byte-standing — the flag's both states' copy the template's own conditionals, 5's fence):
```python
    return templates.TemplateResponse(
        request,
        "vote-ack.html",
        {
            "stem": stem,
            "winner": payload["winner"],
            "acknowledged": bool(outcome.json()["acknowledged"]),
            "vote_id": str(outcome.json()["vote_id"]),
            "item_a": payload["pair"][0],
            "item_b": payload["pair"][1],
            "label_a": labels.get(payload["pair"][0], payload["pair"][0]),
            "label_b": labels.get(payload["pair"][1], payload["pair"][1]),
            "swap": presentation == PRESENTATION_SWAPPED,
            "chain": chain,
            "next_url": next_url,
            "done_url": done_url,
            "deliberate": deliberate,
        },
    )
```
The vote route's docstring re-derived — the Purpose grows (after the deliberate arm's sentences): "THE SUPERSEDES READ (the undo's wire, the cardspec): the payload gains the field at the optional-text form (absent/empty => None — the wire's own schema, votes.py:578); the corrected click rides the correction's citation (a NEW record citing the old, both standing — R9; the tally's weighting walks the link, the cell's weight unchanged). THE UNDO'S AFFORDANCE AT THE ACK (every arm): the context carries the cast's own vote_id (the original handle at the idempotent arm) + the pair as presented + the lane's carries — the template composes the re-serve's citation (5's fence); the re-serve targets #pair-region at the ack region's persistence (the region the swap's target, never its victim — the affordance survives the fetch, self-healing at the second click; the sub-second race the named residual, no new machinery)."; the Provenance's tail grows: "... the journey design 1.4 + the cardspec (the supersedes read, the undo's context), G-CARDSPEC-BRIEF."

### 1d. THE STANDING SEAMS' PINS (no bytes — the read-back's own)

The sitting render :703-722 and the judge route :869-890 ALREADY carry the question (:711/:877) — the legend's thread whole at both page lanes by construction; the guard's ONE read lane :276-291 byte-standing; the refusal-to-ack-region separation :1185-1186 byte-standing; the class default "human" :1181 byte-standing; the two-step law :643-645 unridden (the re-serve a GET fragment, never the POST's response).

## 2. web/templates/sitting.html — THE ACK REGION'S ANNOUNCEMENT (dispatch 2; one attribute, both lanes)

before (:17):
```html
  <div id="ack-region"></div>
```
after:
```html
  <div id="ack-region" aria-live="polite"></div>
```
ONE attribute; BOTH lanes by construction (the judge route renders sitting.html, :869-871); every other line byte-standing (the h1's question, the identity line, the quorum line, the include, the picker).

## 3. web/static/app.css — THE CARD-AS-BUTTON FORMS (dispatch 3; one retirement + one growth + the new block)

THE RETIREMENT — before (:10): `.pair-card { flex: 1; }` — RETIRED whole (the sl-cards dead; the flex:1 rides button.cast-card below). :9 .cards, :11 .card-label, :12 .verdicts BYTE-STANDING (the 12px adjacency --pt-gap held — the operator rides the same flex row's gaps; the rival's distance honestly widened by the operator's display width: the priced carry NAMED, never hidden).
THE GROWTH — before (:13): `button.verdict { padding: 0.6rem 1.2rem; }` — after: `button.verdict { padding: 0.6rem 1.2rem; min-height: 24px; }` (the subordinate's 24px floor MECHANICAL — WCAG 2.2 SC 2.5.8 AA's own byte).
THE NEW BLOCK (inserted after :13, before table.ranked :14):
```css
/* the card-as-button forms (the cardspec; the journey design 1.1/1.5 — the submit-styled-as-card, the 24px floor, the operator display-only, the focus ring) */
fieldset.pair-fieldset { border: none; margin: 0; padding: 0; }
fieldset.pair-fieldset legend { padding: 0; }
button.cast-card {
  appearance: none;
  background: white;
  border: 1px solid #ddd;
  border-radius: 0.5rem;
  color: inherit;
  cursor: pointer;
  display: flex;
  flex: 1;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.25rem;
  font: inherit;
  min-height: 4.5rem;
  padding: var(--pt-gap);
  text-align: left;
}
.operator { align-self: center; color: #666; }
button.cast-card:focus-visible, button.verdict:focus-visible, button.undo:focus-visible { outline: 2px solid #1a1a1a; outline-offset: 2px; }
```
THE BARS: the UA button reset (the submit styled as the card); the cards the pattern space's largest (flex:1 halves of the 40rem wrap + min-height 4.5rem — the 24px floor cleared whole); the operator display-only (a span, centered, never focusable); the focus states' visibility (the explicit ring at the cast cards, the tie, the undo).

## 4. web/templates/pair.html — THE CARD PAIR'S TEMPLATE WHOLE (dispatch 4; the DOM-asserting arcs honestly RED here — the workshop state, never the tree's history)

THE FILE AFTER (25 lines — the fence is the file; the standing carries byte-identical: the ask :4-7, the five stamps; the marker-named verdict row + its labels dict RETIRED whole — the translation's own bytes gone):
```html
<!-- pair — the shared pair region: the sitting includes it, the fragment route serves it (web-brief §4 routes 2+7; the journey design 1.1-1.5; the cardspec); the page's conditional carries: the chain (the ack-carry's remaining list) + the deliberate (the lane's own datum — the done-detour cure) + the supersedes (the undo's re-serve — the correction's carry) -->
<div id="pair-region">
  <form hx-post="/ui/runs/{{ stem }}/vote" hx-target="#ack-region" hx-swap="innerHTML" hx-sync="this:drop">
    {% if not remembered_name %}
    <label for="comparator-id">Your name for yourself as a judge — it stamps your votes. Asked once; remembered for every judgment from this device.</label>
    <input id="comparator-id" name="comparator_id" required minlength="1">
    {% endif %}
    <input type="hidden" name="item_a" value="{{ item_a }}">
    <input type="hidden" name="item_b" value="{{ item_b }}">
    <input type="hidden" name="csrf_token" value="{{ csrf_token }}">
    <input type="hidden" name="presentation_order" value="{{ presentation_order }}">
    {% if chain %}<input type="hidden" name="chain" value="{{ chain }}">{% endif %}
    {% if deliberate %}<input type="hidden" name="deliberate" value="{{ deliberate }}">{% endif %}
    {% if supersedes %}<input type="hidden" name="supersedes" value="{{ supersedes }}">{% endif %}
    <fieldset class="pair-fieldset">
      <legend>{{ question }}</legend>
      <div class="cards">
        {% for verdict in verdicts %}{% if verdict == 'prefer-a' %}<button type="submit" class="cast-card" id="cast-a" name="winner" value="{{ verdict }}"><sl-badge>A</sl-badge> <span class="card-label">{{ label_a }}</span></button>{% elif verdict == 'prefer-b' %}<span class="operator">vs</span><button type="submit" class="cast-card" id="cast-b" name="winner" value="{{ verdict }}"><sl-badge>B</sl-badge> <span class="card-label">{{ label_b }}</span></button>{% endif %}{% endfor %}
      </div>
      <div class="verdicts">
        {% for verdict in verdicts %}{% if verdict != 'prefer-a' and verdict != 'prefer-b' %}<button type="submit" class="verdict" id="cast-{{ verdict }}" name="winner" value="{{ verdict }}">{% if verdict == 'tie' %}Tie — both stand equal{% else %}{{ verdict }}{% endif %}</button>{% endif %}{% endfor %}
      </div>
    </fieldset>
  </form>
</div>
```
THE REGION'S LAWS: the form's head grows hx-sync="this:drop" — the form's native shared sync context, the DROP strategy (the different-verdict in-flight double-click DROPPED before it lands; the same-verdict residual safe at the wire's dedup); the conditional supersedes carry the :12-13 carries' sibling pattern; the fieldset/legend wrapping the pair + the tie inside the form, the legend binding THE QUESTION (the reader hears the group, never bare buttons — threaded at every serve by 1a); the two option cards type="submit" buttons — type EXPLICIT (the default never leaned on), name="winner", value="{{ verdict }}" from the declared set's loop, id="cast-a"/"cast-b" PAIR-STABLE (htmx's restoration keys on the id — the focus survives the two swaps at zero JS); the badge + the label the button's phrasing content (the content model legal; the badge's slot attribute RETIRED — it pointed at the sl-card's header, meaningless and unrendered inside a button; the space between them the accessible name's join — the names the FULL LABELS, "Prefer A" alone dead); the operator the word "vs" display-only between (a span, never focusable, never a target — picker.html:5's own precedent); the tie the declared set's loop member styled subordinate, named honestly "Tie — both stand equal" (the brief's ruled bytes), its own stable id (id="cast-tie" at the declared set's third member — loop-driven, a two-verdict run renders no subordinate control), the tab order's third place (DOM order = visual order); the remaining declared verdicts the subordinate row, the custom verdict's own id the honest fallback ({{ verdict }}); the loop survives — the prefer-* verdicts the equal cards, the remaining declared verdicts the subordinate row.

[PIECE 2 FOLLOWS: §5 vote-ack.html (the undo riding the ack), §6 the test arcs (the re-pins + the eight classes' ten arcs, the count exact), §7 the no-break proofs, §8 the per-step plan R8 + the order's divergence named + FLOOR-GREEN, the bottom line.]
## Reported by togo — 2026-11-27T21:23:05Z

# THE CARD UNIT'S EXACT-TASK SPEC — PIECE 2 OF 2 (§5 the undo riding the ack, §6 the test arcs, §7 the no-break proofs, §8 the per-step plan, the bottom line) — continuing packet synthesize/cardspec, route prioritree-journey, 2026-11-27

## 5. web/templates/vote-ack.html — THE UNDO RIDING THE ACK (dispatch 5; the stay-put region's growth — the affordance at every arm)

THE FILE AFTER (7 lines — the fence is the file; the restatement :3, the acknowledged echo :4, the four arms :6 byte-standing; the comment head re-pinned):
```html
<!-- vote-ack — the verdict restated in item-label terms + the embedded pair fetch + the undo's re-serve (web-brief §4 route 8; the journey design 1.4; the cardspec); the FOUR arms: the chain link / the done link + list-ended / the deliberate stay-put (the done-detour cure) / the fetch; the UNDO rides at EVERY arm — the pair re-served with the supersede carry, the affordance persisting at the ack (the region the swap's target, never its victim) -->
<div id="vote-ack">
  <p class="ack-line">{% if winner == 'prefer-a' %}You preferred {{ label_a }} (A) over {{ label_b }} (B).{% elif winner == 'prefer-b' %}You preferred {{ label_b }} (B) over {{ label_a }} (A).{% else %}Tie: {{ label_a }} (A) and {{ label_b }} (B) stand equal.{% endif %}</p>
  {% if acknowledged %}<p class="quiet">This pair was already recorded with the same answer — it stands once.</p>{% endif %}
  <p class="quiet">Clicked the wrong one? <button type="button" class="undo" hx-get="/ui/runs/{{ stem }}/pair?item_a={{ item_a }}&amp;item_b={{ item_b }}&amp;supersedes={{ vote_id }}{% if deliberate %}&amp;deliberate={{ deliberate }}{% endif %}{% if chain %}&amp;chain={{ chain }}{% endif %}" hx-target="#pair-region" hx-swap="outerHTML">undo this judgment</button> — your correction stands, the first is superseded; both records stay in the log.</p>
  {% if next_url %}<p><a class="next-pair" href="{{ next_url }}">next pair -></a></p>{% elif done_url %}<p class="quiet">That was the last pair on this card — the list has ended; every judgment is recorded.</p><p><a href="{{ done_url }}">the done page</a></p>{% elif deliberate %}<p>Recorded. Judge the next pair from the picker, or close out the sitting at the done page.</p><p><a href="/runs/{{ stem }}/pairs">the pair picker</a> <a href="/runs/{{ stem }}/done">the done page</a></p>{% else %}<div hx-get="/ui/runs/{{ stem }}/pair{% if swap %}?swap=true{% endif %}" hx-trigger="load" hx-target="#pair-region" hx-swap="outerHTML"></div>{% endif %}
</div>
```
THE REGION'S LAWS: the last vote's id carried ({{ vote_id }} — 1c's context field; the ORIGINAL handle at the idempotent arm — the undo target honest at both flag states); the "undo this judgment" re-serve link — a BUTTON type="button" (the explicit type; an action, never a navigation; natively focusable + keyboard-activatable; the no-JS state the tier's own htmx-required truth), hx-get to the pair fragment carrying the pair AS PRESENTED (the mirror's order — the correction's mirror: the same cards at the same positions) + supersedes={{ vote_id }} + the lane's own carries riding ({% if deliberate %} the deliberate datum at the stay-put arm; {% if chain %} the chain token at the chain arm — the raw incoming chain, the corrected click's chain arithmetic IDEMPOTENT at the re-computation: the just-voted token dropped again, the same next_url; the done arm's rest empty => the done arm again), targeting #pair-region at hx-swap="outerHTML" (the fetch arm's own form) — the affordance PERSISTS at the ack (the region the swap's target, never its victim: the second undo click re-serves, self-healing at the persistence; the sub-second race against the pending fetch the named residual, no new machinery); the copy teaching at the mistake's mirror — the label-first restatement :3 the trigger, then "Clicked the wrong one?" (moho's walk's teaching), the affordance named "undo this judgment" (the brief's ruled phrase), then BOTH TRUTHS: "your correction stands, the first is superseded" (the brief's ruled bytes verbatim — the tally's weighting meaning) + "both records stay in the log" (the record's keeping — append-only, no delete verb exists; NEVER "erased": the word never teaches, the negation never needed — the two truths carried plainly); the acknowledged flag's both states' copy — the standing :4 echo at the idempotent arm, the plain restatement at the normal arm (the undo line rides at BOTH, outside the arms' conditional); the ids' stability — id="vote-ack" byte-standing (:2); the bare re-click at the stay-put card REFUSED as the teaching's subject (the copy teaches the AFFORDANCE, never the bare re-click — R9's new-sample law, the double-count trap).

## 6. tests/test_web_face.py — THE ARCS (dispatch 6; the re-pins + the eight classes' ten new arcs; the count exact)

THE SCHOOL byte-standing: the client fixture :102-113, _scrape_csrf, the literal copies asserted as served (the autoescaped bytes the school's own law), two TestClients = two browsers. THE FLOOR: 480 (verified at 0) -> **490** at the unit's gate (+10 exact — keisan's +7-10 reconciled at the ceiling; the eight classes' whole, none padded: the card's form/operator/tie/loop + the rides + the sync + the lanes = seven, the undo's three; the ~491 whole-set mid carried by the bridge's landed arcs inside the 480 + this unit's ten).

### 6a. THE RE-PINS (the DOM-asserting arcs re-pinned at the card's landing — five arcs, seven assert sites)

1. test_sitting_serves_first_pair_server_side :262 — before: `assert 'slot="header">A<' in response.text` — after (the card-button's new bytes; :263 'value="prefer-a"' and every other assert byte-standing):
```python
    assert 'id="cast-a"' in response.text
    assert '<sl-badge>A</sl-badge> <span class="card-label">one</span>' in response.text
```
2. The "no fetch" byte-patterns — the undo's hx-get now legal at every arm; the pin moves to the AUTO-fetch's own byte (hx-trigger="load" — the load-triggered div dead, the deliberate re-serve link legal): test_vote_chain_carry_next_pair :477 + :501, test_vote_chain_carry_done_link :517, test_deliberate_vote_stays_put :539 + :553, test_deliberate_vote_stays_put_at_the_done_queue :577 — each `assert 'hx-get="/ui/runs' not in X.text` becomes `assert 'hx-trigger="load"' not in X.text` with the comment re-pinned (the chain lane never AUTO-fetches — the undo's deliberate re-serve legal at the arm). test_vote_then_pair_chain :445-447 byte-standing (the fetch div's own closing-quote byte distinct from the undo's query-carrying URL); test_vote_swapped_hidden_field_resends :841 byte-standing (the fetch's ?swap=true byte); every wire-level arc STANDS (the POST body unchanged).

### 6b. THE TEN NEW ARCS (fenced by name; the eight classes)

1. `test_card_click_casts_the_clicked_option` [class 1 — the casting] — the sitting renders the two option cards as submit buttons (id="cast-a"/id="cast-b", name="winner", value="prefer-a"/value="prefer-b", the labels the buttons' content), the fieldset + the legend binding the question; the B card's click (the POST winner=prefer-b, the scraped token, the hidden stamps) lands the ack "You preferred two (B) over one (A)." — the submitter's name/value the wire's only carrier, the body byte-identical (_FORM_VOTE's shape).
2. `test_operator_vs_between_the_cards_never_focusable` [class 2 — the operator's render] — the served pair carries the operator's exact byte `<span class="operator">vs</span>` BETWEEN the two card-buttons (the served text's index order cast-a < operator < cast-b); the operator a display span — no button/input/a/tabindex/hx- attribute inside it (never focusable, never a target).
3. `test_tie_control_subordinate_at_the_bar` [class 3 — the tie's control] — the served pair carries the tie's subordinate control: id="cast-tie", value="tie", the copy "Tie — both stand equal" (the em-dash byte asserted as served), the DOM order's THIRD place (cast-a < cast-b < cast-tie — the tab order = the visual order); the served CSS carries the 24px floor's byte (min-height: 24px at /static/app.css); the tie's click (winner=tie) lands the ack "Tie: one (A) and two (B) stand equal."
4. `test_two_verdict_run_renders_no_subordinate_control` [class 3 — the loop-driven truth] — the register REFUSES any declared set beyond the constant triple (registry.py:259 — the two-verdict school the template's own render): web.templates.env.get_template("pair.html") rendered with verdicts ["prefer-a", "prefer-b"] carries NO subordinate control (no cast-tie, no "Tie") and both cards — the declared set renders whole from the loop, never a hardcoded third button.
5. `test_undo_different_verdict_supersedes_both_stand` [class 4 — the landing + the copy] — the ack carries the undo affordance: the button's hx-get citing the pair as presented + supersedes=VOTE-0001 (the autoescaped bytes as served), hx-target="#pair-region"; the copy's both-truths pinned ("your correction stands, the first is superseded" + "both records stay in the log"; "erased" NEVER in the ack's bytes); the re-serve GET renders the pair with the hidden supersedes carry (name="supersedes" value="VOTE-0001") + the fresh token (the scrape passes); the corrected click (winner=prefer-b + supersedes) lands a NEW record citing the old — the log: len 2, the link pinned, BOTH standing; the tally's weighting walked: the llm corroborating vote cast, the tally's pair_class_counts == {"a|b": {"human": 1, "llm": 1}} — the superseded EXCLUDED, the correction counted, the cell's weight unchanged; a cross-pair carry (the supersedes citing VOTE-0001 at ANOTHER pair's POST) refused at the wire — the refusal fragment rendered (the pair region untouched), the log unchanged (the door's same-pair law, votes.py:628-636).
6. `test_undo_same_verdict_stands_once` [class 4 — the idempotent arm] — the re-serve + the SAME-verdict click (winner=prefer-a + supersedes=VOTE-0001): a NEW record citing the old (the log: len 2, both prefer-a, the link pinned — the dedup key carries supersedes, no dedup hit); the verdict stands ONCE at the same weight (the llm vote + the tally's pair_class_counts == {"a|b": {"human": 1, "llm": 1}} — the link walked, the weight unchanged); the repeated re-send (the byte-identical POST again): the LOUD dedup — the echo rendered, the log UNCHANGED (len 2).
7. `test_acknowledged_flag_true_through_the_web_route` [class 7 — the seam's pins] — the fresh cast: no echo, the undo's supersedes citing VOTE-0001; the byte-identical re-send THROUGH THE WEB ROUTE: the echo rendered (the flag's truth through the route's own read :1216), the undo link citing the ORIGINAL handle (VOTE-0001 — the id's honesty at the idempotent arm), the census unchanged (the write never landed twice). RUN-0009's live divergence the NAMED RESIDUAL — never leaned on, never diagnosed here (the cause a hypothesis: the connected server's build vs the tree's bytes; the live-lane diagnosis the outward lane's own or earned-later).
8. `test_ack_region_aria_live_and_ids_stable` [class 5 — the rides] — the sitting carries `<div id="ack-region" aria-live="polite">` (the swap's content announced — the ack, the undo affordance, the refusal); the fragment GET carries the SAME stable ids (id="cast-a"/id="cast-b"/id="cast-tie") + the legend's question threaded at the fragment (the group semantics at the chain's swap — the reader hears the group) — the ids' stability the focus restoration's key (htmx's built-in restoration, the same-named control after the fetch's outerHTML swap, ZERO JS).
9. `test_form_carries_hx_sync_drop` [class 6 — the sync] — the served form carries hx-sync="this:drop" (the form's native shared sync context, the DROP strategy — the different-verdict in-flight double-click DROPPED before it lands; the byte-level pin, the strategy's own bytes).
10. `test_deliberate_lane_same_card_and_composes_reclick` [class 8 — the lanes' consistency] — the judge page serves the SAME card form (the shared include: cast-a/cast-b, the operator, cast-tie, the fieldset/legend — the consistency by construction pinned); the deliberate vote's ack carries the undo with the deliberate carry riding (&amp;deliberate=true in the served bytes); the re-serve GET renders the deliberate hidden carry (name="deliberate" value="true"); the corrected click (supersedes + deliberate) lands the ack STAYING PUT (no load-triggered div, the confirmation + both links rendered) — the lane's law held at the correction.

## 7. THE NO-BREAK PROOFS (the unit's fence)

- **THE POST BYTE-IDENTICAL:** the wire body _FORM_VOTE :71 byte-standing; the submitter's name/value rides (the HTML standard — RUN-0008's 319 browser-cast votes the live proof); the CSRF field + the five stamps untouched; the supersedes field ABSENT at the normal click (the conditional renders nothing); the guard's ONE read lane :276-291 untouched; the class default "human" :1181 untouched; the parse order unchanged; the corroboration floor untouched by construction (the tally's weighting the wire's own law, $0 bytes).
- **THE CLI/TOOLS LANES UNTOUCHED:** cli.py + mcp_server.py byte-standing (zero bytes — the llm-class at its own UX weight; the one-click journey the browser lane's story, the wire's law the only sameness); the service's door already reads supersedes (service.py:207/:597) — the web lane gains the READ alone.
- **THE REGISTER/PICKER UNTOUCHED:** landing.html + picker.html + pairs.html byte-standing; the register's door refuses any declared set beyond the triple (registry.py:259).
- **THE WIRE'S BYTES UNTOUCHED:** votes.py/tally.py/run_store.py/service_store.py/service.py/session.py/registry.py byte-standing — the supersedes verb already owned (the CLI :347 + the MCP :607 carry it), the tally's weighting already walks the link (verified at :165-183 this pass).
- **THE LANDED SURFACES RIDDEN:** the identify-once ask riding the form unchanged; the ack target's separation held; the two-step law held (the re-serve a GET fragment, never the POST's response); the refusal's same-pair law riding the undo's seam; the fragment chain's fresh-token law held.
- **THE FLOOR:** 480 -> 490 (6's exact count); ruff zero findings; pyright 0/0; ZERO new ignores — the card unit carries NO new per-file ruling (the standing pyproject entries byte-standing; the conftest F401 the bridge's, never here; the five-argument signatures at the PLR0913 bar — the judge route's own precedent).

## 8. THE PER-STEP PLAN (R8 — one file per dispatch, the read-backs named) + THE ORDER'S DIVERGENCE NAMED + FLOOR-GREEN

**THE ORDER'S DIVERGENCE, NAMED (never averaged away):** the dispatch's stated sequence (pair.html -> sitting.html -> app.css -> vote-ack.html -> web.py -> test_web_face.py) is the brief's FILE-LIST order (keisan's union, the brief §1) — NOT the brief's ruled DISPATCH order (§5.4). THE READINGS: the brief's §5.4 — "(1) web.py ... all additive, the suite green at the landing" — the additive bytes first (web.py's seams, the aria-live, the CSS rules), the RED window concentrated at the two template reworks (pair.html "the DOM-asserting arcs honestly RED here, the workshop state, never the tree's history"), the tests re-pinning last; the dispatch's sequence — the file-list order read as the dispatch order. THE RESOLUTION: THIS SPEC FENCES THE BRIEF'S §5.4 ORDER — the suite green at each of the first three additive landings (the read-backs clean), the honest-RED workshop window bounded to the two template reworks, the tests closing at FLOOR-GREEN; the dispatch's sequence would open the RED window at step 1 (pair.html before the fragment's question/supersedes context exists — the legend empty, the undo's re-serve dead between its steps 4 and 5). THE REASONING: the same bytes land either way (ONE COMMIT the unit — the intermediate states never the tree's history); the brief is the approved gated record and the dispatch cites it as its own authority; the collaborator's approval at G-CARDSPEC-BRIEF rules the divergence — either order lands this spec's bytes.

**THE SIX DISPATCHES (each its own; the read-backs named):**
1. **web.py:** 1a-1c — the fragment route's cited re-serve branch + the question thread + the carries, the vote route's supersedes read, the ack context's four fields, both docstrings re-derived. Read-back: the four seams vs this spec's fence; the register lane's mint path-bound; the suite GREEN at the landing (the seams additive — no standing arc touches them).
2. **sitting.html:** 2 — the aria-live attribute. Read-back: the attribute present at BOTH lanes' renders (the sitting GET + the judge GET — the same template).
3. **app.css:** 3 — the .pair-card retirement, the :13 growth, the new block. Read-back: the rules vs this spec's fence; the retired rule gone; --pt-gap byte-standing.
4. **pair.html:** 4 — the card region reworked whole + the hx-sync + the supersedes carry. Read-back: the file vs this spec's 25-line fence — the DOM-asserting arcs honestly RED here (the workshop state, never the tree's history).
5. **vote-ack.html:** 5 — the undo region + the copy. Read-back: the file vs this spec's 7-line fence — the undo at every arm, the acknowledged both states, the re-pinned comment head.
6. **test_web_face.py:** 6 — the re-pins + the ten arcs. Read-back: the arcs' names + the count vs this spec (68 -> 78 in the file; the suite at 490).

**FLOOR-GREEN (the increment's closing step, the three acts verbatim):** `uv run pytest` (the suite green at 490 passed — the count named) -> `uv run ruff check .` (zero findings) -> `uv run pyright` (0 errors, 0 warnings). THEN the gate's own lanes (cited, never performed here): kensho's independent verification (validate/card-unit) + MOHO'S IMPLEMENTATION WALK at G-CARD (R4 — the card lived cold: the translation dead, the undo discovered at the mirror, the tie found at the bar, the operator teaching) — the findings riding the gate as evidence. **ONE COMMIT the natural unit** (the six dispatches inside; the intermediate states never the tree's history).

## THE BOTTOM LINE

THE SPEC — six files, every byte fenced: web.py's four seams (the cited re-serve branch deriving the presentation, the supersedes read at the absent=>None form, the ack context's vote_id + the mirror's pair + the chain carry, the docstrings re-derived); sitting.html's one attribute (both lanes by construction); app.css's card-as-button forms (the UA reset, the 24px floor mechanical, the operator display-only, the focus ring); pair.html's card pair whole (the two option cards the submit buttons inside the standing form, the wire byte-identical, the fieldset/legend binding the question, the word "vs" between never focusable, the tie named small at the bar, the marker-named row retired, the hx-sync closing the in-flight race); vote-ack.html's undo riding the ack at every arm (the re-serve with the supersede carry + the lane carries, the copy carrying both truths never "erased", the acknowledged both states); test_web_face.py's re-pins + ten arcs at 480 -> 490. THE TRADE-OFF THE PLAN CARRIES, unchanged from the brief: the bigger targets sharpen the adjacency (the rival a card-width away, the operator between — the scroll-tap and fat-thumb classes the priced carry, NAMED); the correction's window same-sitting-only (the cross-sitting path the tools lanes' own); RUN-0009's acknowledged-flag divergence the named residual (the cause a hypothesis, the live-lane diagnosis the outward lane's own); the tie's 0/319 rarity the walk's only school. THE APPROVAL is the collaborator's act at G-CARDSPEC-BRIEF — no build dispatch before the green; this spec the build's whole ground. [THE SPEC WHOLE ENDS — pieces 1+2 the report.]
