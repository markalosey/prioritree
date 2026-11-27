<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — build/card

**Route:** prioritree-journey (executing) | **Events:** 7 | **Reports:** 6

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-27T22:09:50Z |
| 2 | report | jikko | 2026-11-27T22:23:31Z |
| 3 | report | jikko | 2026-11-27T22:25:16Z |
| 4 | report | jikko | 2026-11-27T22:26:17Z |
| 5 | report | jikko | 2026-11-27T22:33:49Z |
| 6 | report | jikko | 2026-11-27T22:39:42Z |
| 7 | report | jikko | 2026-11-27T23:25:47Z |
## Reported by jikko — 2026-11-27T22:23:31Z

STEP 1/6 DONE — src/prioritree/web.py alone, the four seams at the landed bytes (anchors re-verified first: the bridge moved lines — fragment route :1088 now, vote :1166 now):
(1) CITED RE-SERVE :1089/:1122-1163 — signature `async def pair(request: Request, stem: str, item_a: str = "", item_b: str = "", *, swap: bool = False) -> Response:`; carries read from the query :1122-1124 (the judge route's precedent); `cited = bool(item_a.strip() and item_b.strip())` :1125; /next consult + done-edge + refusals byte-standing inside `if not cited:` :1127-1133; presentation derived `PRESENTATION_SWAPPED if presented_a > presented_b else PRESENTATION_CANONICAL` :1141 (the fieldless swap never served); question threaded `"question": str(manifest_body["question"])` :1152; supersedes/deliberate/chain in the context :1159-1161; fresh mint :1150 byte-standing.
(2) SUPERSEDES READ :1243 — `"supersedes": str(form.get("supersedes", "")).strip() or None,` (absent/empty => None, votes.py:578's schema; parse order unchanged; POST :1245; separation :1246-1247 byte-standing).
(3) ACK CONTEXT :1271-1290 — four fields grown: `"vote_id": str(outcome.json()["vote_id"])` :1278, `"item_a": payload["pair"][0]`/`"item_b": payload["pair"][1]` :1280-1281, `"chain": chain,` :1285; acknowledged :1277 byte-standing; the bridge's standing `"identifying"` :1279 KEPT (the spec's before-fence predates it).
(4) BOTH DOCSTRINGS — fragment Purpose opens "TWO SERVE LANES. THE CITED RE-SERVE (the undo's lane, the cardspec):" :1092-1114 + Provenance tail "the journey design 1.1/1.4 + the cardspec (the cited re-serve, the question thread, the carries), G-CARDSPEC-BRIEF." :1118-1120; vote Purpose grows "THE SUPERSEDES READ (the undo's wire, the cardspec):" + "THE UNDO'S AFFORDANCE AT THE ACK (every arm):" :1195-1207 + Provenance tail "the journey design 1.4 + the cardspec (the supersedes read, the undo's context), G-CARDSPEC-BRIEF." :1217-1219.
DEVIATIONS (type-level necessities, the fences composed type-inconsistent at pyright strict; ZERO ignores): `payload: dict[str, Any] = {` :1237 — the None widened the dict's join, breaking the byte-standing chain arm `sorted(payload["pair"])` :1258; `served: dict[str, Any] = {}` pre-bound :1126 — pyright won't correlate `cited` across the join (possibly-unbound in the else lane); the fragment docstring's /next lead keeps "§7a's label law — the map its label-bearing companion", the redundant "/next the route's defining call" absorbed into the "(the defining call when no pair cited)" header.
NOT DONE: sitting.html / app.css / pair.html / vote-ack.html / test_web_face.py (steps 2-6); the suite + floor NOT run (the coordinator's instruments; step 6's own act). The patch's own findings fixed same-turn: 17 pyright (the payload join) + 6 (served unbound) -> clean at the landing.
## Reported by jikko — 2026-11-27T22:25:16Z

STEP 2/6 sitting.html DONE — cardspec §2 applied, one attribute: :17 before `  <div id="ack-region"></div>` -> after `  <div id="ack-region" aria-live="polite"></div>` (verified on disk, 23 lines, every other line byte-standing). Both lanes by construction — the judge route renders the same template. NOT DONE: web.py/pair.html/app.css/vote-ack.html/test_web_face.py (other seats' dispatches); no tests run here (kensho runs the instruments).
## Reported by jikko — 2026-11-27T22:26:17Z

STEP 3 REPORT — app.css's card-as-button forms (packet build/card, dispatch 3 of 6; web/static/app.css alone, 32 → 53 lines, one hunk).
THE RETIREMENT landed: `.pair-card { flex: 1; }` GONE (read-back grep-clean — no .pair-card in the file; the sl-cards dead, the flex:1 rides button.cast-card).
THE GROWTH landed at :12: `button.verdict { padding: 0.6rem 1.2rem; min-height: 24px; }` — the tie's subordinate floor MECHANICAL (WCAG 2.2 SC 2.5.8 AA's own byte).
THE NEW BLOCK landed :13-34 verbatim per §3's fence: `fieldset.pair-fieldset { border: none; margin: 0; padding: 0; }` + `fieldset.pair-fieldset legend { padding: 0; }`; `button.cast-card` carrying the UA reset (`appearance: none; color: inherit; font: inherit;`) + the cards' form (`flex: 1; min-height: 4.5rem; padding: var(--pt-gap);` — the 24px floor cleared whole at 72px); `.operator { align-self: center; color: #666; }` (display-only); `button.cast-card:focus-visible, button.verdict:focus-visible, button.undo:focus-visible { outline: 2px solid #1a1a1a; outline-offset: 2px; }` (the explicit ring).
BYTE-STANDING held: --pt-gap :2, .cards :9, .card-label :10, .verdicts :11 — the 12px adjacency untouched; the comment head + block order byte-matched the fence.
READ-BACK: the file re-read whole after the apply; nothing else touched — one file, the fence's blocks only. NOT DONE: nothing of this step's fence; instruments (tests/lint) not run — the coordinator runs them (steps 4-6 pending: pair.html, vote-ack.html, the test arcs).
## Reported by jikko — 2026-11-27T22:33:49Z

STEP 4/6 — web/templates/pair.html alone, cardspec §4's file-after fence landed (the dispatch's "§1" citation resolved: the spec's pair.html block — "THE FILE AFTER (25 lines — the fence is the file)"), 23 → 25 lines, two applies (the second same-turn: the read-back caught the two div wrappers + closers at the old 4-space indent, re-nested to the fieldset's 6 — the fence's bytes now exact).
THE RETIRED ROW named (before, whole — the marker-named verdict row + its labels dict, old :18-21): `<div class="verdicts">` / `{% set labels = {"prefer-a": "Prefer A", "prefer-b": "Prefer B", "tie": "Tie"} %}` / `{% for verdict in verdicts %}<button class="verdict" name="winner" value="{{ verdict }}">{{ labels.get(verdict, verdict) }}</button>{% endfor %}` / `</div>` — plus the display-only sl-cards block (old :14-17, the slot-badged pair-cards) retired whole; the AFTER: the loop-driven cards (cast-a/cast-b, name="winner", the declared values) + the subordinate row (id="cast-{{ verdict }}" — cast-tie at the triple, "Tie — both stand equal").
THE FILE AFTER (25 lines, verbatim on disk):
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
READ-BACK: the file re-read whole after each apply — the standing carries byte-identical (the ask :4-7, the five stamps :8-13), :3's hx-post untouched + hx-sync="this:drop", the hidden carries whole (CSRF, pair identity, presentation_order, chain/deliberate/supersedes conditional), the two cards type="submit" with name="winner" + the declared values, the badge+label phrasing content (the space join — the accessible names the full labels), the operator "vs" a display span never focusable, the tie at the bar's third DOM place. One file only; nothing else touched.
NOT DONE: vote-ack.html (step 5) + the test arcs (step 6) — other dispatches; the instruments (pytest/ruff/pyright) not run here — the coordinator/kensho runs them; the DOM-asserting arcs honestly RED at this workshop state per the spec's named window.
## Reported by jikko — 2026-11-27T22:39:42Z

Step 5 (R11) — vote-ack.html the fence whole landed, byte-for-byte vs cardspec §5 (7 lines: the comment re-pinned :1, id="vote-ack" :2 stable, :3/:4/:6/:7 byte-standing, the undo :5 at EVERY arm — button type="button", hx-get citing the pair as presented + supersedes={{ vote_id }} + the deliberate/chain carries, hx-target="#pair-region" hx-swap="outerHTML", the copy's both truths, never "erased"); the fence RETIRES the identifying conditional (the bridge's :5 — the undo the re-cast's own path now): test_identifying_ack_teaches_the_reload honestly RED at this landing (the workshop window; §6 does not name its re-pin — step 6's dispatch should); web.py :1279's identifying key now unread (step 1's keep, inert; ONE file, nothing else touched). The file after, verbatim:
<!-- vote-ack — the verdict restated in item-label terms + the embedded pair fetch + the undo's re-serve (web-brief §4 route 8; the journey design 1.4; the cardspec); the FOUR arms: the chain link / the done link + list-ended / the deliberate stay-put (the done-detour cure) / the fetch; the UNDO rides at EVERY arm — the pair re-served with the supersede carry, the affordance persisting at the ack (the region the swap's target, never its victim) -->
<div id="vote-ack">
  <p class="ack-line">{% if winner == 'prefer-a' %}You preferred {{ label_a }} (A) over {{ label_b }} (B).{% elif winner == 'prefer-b' %}You preferred {{ label_b }} (B) over {{ label_a }} (A).{% else %}Tie: {{ label_a }} (A) and {{ label_b }} (B) stand equal.{% endif %}</p>
  {% if acknowledged %}<p class="quiet">This pair was already recorded with the same answer — it stands once.</p>{% endif %}
  <p class="quiet">Clicked the wrong one? <button type="button" class="undo" hx-get="/ui/runs/{{ stem }}/pair?item_a={{ item_a }}&amp;item_b={{ item_b }}&amp;supersedes={{ vote_id }}{% if deliberate %}&amp;deliberate={{ deliberate }}{% endif %}{% if chain %}&amp;chain={{ chain }}{% endif %}" hx-target="#pair-region" hx-swap="outerHTML">undo this judgment</button> — your correction stands, the first is superseded; both records stay in the log.</p>
  {% if next_url %}<p><a class="next-pair" href="{{ next_url }}">next pair -></a></p>{% elif done_url %}<p class="quiet">That was the last pair on this card — the list has ended; every judgment is recorded.</p><p><a href="{{ done_url }}">the done page</a></p>{% elif deliberate %}<p>Recorded. Judge the next pair from the picker, or close out the sitting at the done page.</p><p><a href="/runs/{{ stem }}/pairs">the pair picker</a> <a href="/runs/{{ stem }}/done">the done page</a></p>{% else %}<div hx-get="/ui/runs/{{ stem }}/pair{% if swap %}?swap=true{% endif %}" hx-trigger="load" hx-target="#pair-region" hx-swap="outerHTML"></div>{% endif %}
</div>
## Reported by jikko — 2026-11-27T23:25:47Z

STEP 6/6 DONE — tests/test_web_face.py alone; the 5 re-pins + the ten new arcs + the owed re-pin landed; THE FLOOR GREEN at the exact count.
RE-PINS (§6a): the badge byte at test_sitting_serves_first_pair_server_side (slot= -> id="cast-a" + '<sl-badge>A</sl-badge> <span class="card-label">one</span>'); the six no-fetch sites -> assert 'hx-trigger="load"' not in (test_vote_chain_carry_next_pair x2, test_vote_chain_carry_done_link, test_deliberate_vote_stays_put x2, test_deliberate_vote_stays_put_at_the_done_queue), the comments re-pinned per-lane ("never AUTO-fetches", the undo's re-serve legal).
TEN NEW ARCS (§6b, in the spec's order): test_card_click_casts_the_clicked_option, test_operator_vs_between_the_cards_never_focusable, test_tie_control_subordinate_at_the_bar, test_two_verdict_run_renders_no_subordinate_control, test_undo_different_verdict_supersedes_both_stand, test_undo_same_verdict_stands_once, test_acknowledged_flag_true_through_the_web_route, test_ack_region_aria_live_and_ids_stable, test_form_carries_hx_sync_drop, test_deliberate_lane_same_card_and_composes_reclick.
THE OWED RE-PIN: test_identifying_ack_teaches_the_reload RETIRED — the honest landing read at the dispatch's own arithmetic (the suite "490 expected: 481 + the ten new arcs, the re-pins' count reconciled": 481 - 1 + 10 = 490 exact; the file 69 - 1 + 10 = 78 = the spec's read-back "68 -> 78"); the intent — the identifying ack's re-cast affordance — re-derived whole at the undo arcs' bytes (the different-verdict arc pins the identifying arm's undo citation + the both-truths copy; the acknowledged arc pins the identifying ack + the LOUD echo + the undo citing the ORIGINAL handle); if the dispatch's "re-pin" meant keep-and-reassert, the re-add is one arc from this report's shape + the correction path (the suite would read 491).
DEVIATIONS (fence-internal, reported): the same-verdict arc's final pin at len == 3 (the spec's "(len 2)" a slip against its own flow — the llm corroborating vote's own record makes 3 at the re-send; the intent "the log UNCHANGED" held, first run failed 3 == 2, fixed same-turn); the tally pin at the (a|b) CELL (the spec's whole-dict form assumed the one-pair universe; the cross-pair same-pair law needs the three-pair one — votes.py:628-636 cited in the arc); three docstrings trimmed at the 120 bar (E501 findings fixed same-turn).
NOT DONE: the inert identifying key (web.py :1279) — the fence's letter names no arc for it, no act here (web.py another dispatch; also web.py's vote-route docstring still carries the retired reload-teaching sentence — its owner's concern); the module docstring not grown (the fence names no growth); nothing else touched in the file.
THE FLOOR (the three acts verbatim): the suite "490 passed in 40.08s" (the baseline before the landing: 475 passed + the 6 named RED at the workshop state) | ruff "All checks passed!" | pyright "0 errors, 0 warnings, 0 informations".
