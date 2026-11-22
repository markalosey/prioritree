# Copyright (C) 2026 Mark Losey. All rights reserved.
"""web_structure — the front end's content as data: the emission's only source.

The web unit's SOURCE STRUCTURE (web-brief §1.3, the ruled home: a sibling of
the generator — a Python module of data is IMPORT-shaped, the script-run's own
path root carries the sibling import, no importlib machinery). THE
CONTENT-IN-CONFIGURATION LAW AT THE WEB TIER (R1's ruled echo): the copy
lives in data, the generator renders — every human-facing word, the CDN pins,
the verdict triple, the route table with its service-call lanes, the form
declarations, the Shoelace inventory, the template bodies, the CSS, the
entire Web Components surface: ALL frontend things are generated from THIS
module (the projection law; hand-authored frontend artifacts are out of
grammar). The template bodies carry @KEY@ sentinels; web_scaffold substitutes
from COPY + PINS at emission ({slot} placeholders convert to Jinja2 slots)
— the emitted artifacts are byte-determined by this module alone.
"""

from __future__ import annotations

from typing import Final

__all__ = [
    "APP_JS",
    "COPY",
    "FRAGMENTS",
    "ITEM_ROWS",
    "PINS",
    "ROUTE_TABLE",
    "SCREENS",
    "SERVICE_LANES",
    "SHOELACE_INVENTORY",
    "STYLESHEET",
    "TEMPLATES",
    "VERDICT_BUTTONS",
    "VERDICTS",
]

# The CDN pins (web-brief §2.5: the exact version values spec-lane literals —
# zero shoelace/htmx bytes in-tree at HEAD; these are the pins the base
# template emits; the online-at-page-load assumption is the design §13's
# priced acceptance).
PINS: Final[dict[str, str]] = {
    "SHOELACE_THEME": "https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.20.1/cdn/themes/light.css",
    "SHOELACE_AUTOLOADER": (
        "https://cdn.jsdelivr.net/npm/@shoelace-style/shoelace@2.20.1/cdn/shoelace-autoloader.js"
    ),
    "HTMX": "https://cdn.jsdelivr.net/npm/htmx.org@2.0.7/dist/htmx.min.js",
}

# The verdict vocabulary (the ruled triple as data — R4's declared default).
VERDICTS: Final[tuple[str, ...]] = ("prefer-a", "prefer-b", "tie")

# The verdict buttons' labels — the markers named, the button<->card tie by
# construction (design §7a: the buttons name the MARKERS).
VERDICT_BUTTONS: Final[dict[str, str]] = {"prefer-a": "Prefer A", "prefer-b": "Prefer B", "tie": "Tie"}

# The route table — the nine routes, each with its kind + service-call lane
# (the web tier EXPERIENCES the service surface's own CQRS segregation, R2).
ROUTE_TABLE: Final[dict[str, tuple[str, str, str]]] = {
    "landing": ("GET", "/", "none — static"),
    "register": ("POST", "/ui/register", "POST /runs"),
    "sitting": ("GET", "/runs/{stem}", "GET /runs/{stem}/manifest + GET /runs/{stem}/next"),
    "pair": ("GET", "/ui/runs/{stem}/pair", "GET /runs/{stem}/next + GET /runs/{stem}/manifest"),
    "vote": ("POST", "/ui/runs/{stem}/vote", "POST /runs/{stem}/votes + GET /runs/{stem}/manifest"),
    "done": ("GET", "/runs/{stem}/done", "GET /runs/{stem}/next + GET /runs/{stem}/manifest"),
    "progress": ("GET", "/runs/{stem}/progress", "GET /runs/{stem}/state"),
    "state_strip": ("GET", "/ui/runs/{stem}/state", "GET /runs/{stem}/state"),
    "result": ("GET", "/runs/{stem}/result", "GET /runs/{stem}/tally + GET /runs/{stem}/manifest"),
}

# The six service routes' lanes (the frozen wire's literals — the union's
# other half; web.py's _SERVICE_LANES mirrors these bytes).
SERVICE_LANES: Final[tuple[str, ...]] = (
    "POST /runs",
    "GET /runs/{run_id}/next",
    "POST /runs/{run_id}/votes",
    "GET /runs/{run_id}/state",
    "GET /runs/{run_id}/tally",
    "GET /runs/{run_id}/manifest",
)

# The form field declarations (design §5: the native affordances as MARKUP,
# never logic — the wire is the sole validator; the item-count rules are
# NEVER pre-checked client-side). Six item rows; required on operator_id,
# question, and the FIRST TWO item rows (the registry's <2-items refusal
# stated as the browser's own semantics); quorum a number input, min 1.
ITEM_ROWS: Final[int] = 6

# The Shoelace inventory (presentation.md's ruled set — Shoelace ships NO
# table component: the semantic table + generated CSS is the honest pick).
SHOELACE_INVENTORY: Final[tuple[str, ...]] = (
    "sl-card",
    "sl-badge",
    "sl-tag",
    "sl-tooltip",
    "sl-details",
)

# The screen + fragment inventories (the brief §1.3's whole list — the
# fragment inventory's refusal member is the ONE renderer, never its own
# route; the fold page carries §3b's page lane).
SCREENS: Final[tuple[str, ...]] = (
    "landing",
    "sitting",
    "done",
    "progress",
    "result",
    "halt",
    "unknown",
    "fold",
)
FRAGMENTS: Final[tuple[str, ...]] = ("ack", "pair", "vote-ack", "state-strip", "refuse")

# The copy strings — every human-facing word (design §7's plain-words bridges
# whole; moho's breaks closed). {slot} placeholders convert to Jinja2 slots
# at emission ({quorum} -> {{ quorum }}, {label_a} -> {{ label_a }}, ...).
COPY: Final[dict[str, str]] = {
    "SITE_TITLE": "Priori-tree",
    "SITE_EXPLANATION": (
        "Priori-tree turns easy pairwise judgments into a reliable ranking. "
        + "You register a list, then judge the items two at a time — the site "
        + "tallies your judgments into a superior order."
    ),
    "VOCABULARY": (
        "Each pair is judged with three answers: prefer the first, prefer the "
        + "second, or a tie."
    ),
    "OPERATOR_ID_BRIDGE": "Your name for yourself on this run.",
    "QUESTION_LABEL": "The question to answer.",
    "QUORUM_BRIDGE": (
        "How many judgments each pair needs — 1 means just you; 2 or more "
        + "means you need other judges, and a pair stays open until it has them."
    ),
    "ITEMS_LEGEND": (
        "The items — an id and a label for each. The first two rows are "
        + "required; the list is locked once registered."
    ),
    "REGISTER_BUTTON": "Register the run",
    "RESUME_LABEL": "Have a run id? Resume its sitting.",
    "RUN_ID_BRIDGE": (
        "The run id looks like RUN-0001 — it was shown when the run was "
        + "registered."
    ),
    "RESULT_LABEL": "Have a run id? See its result.",
    "COMPARATOR_BRIDGE": (
        "Your name for yourself as a judge — it stamps your votes. The same "
        + "entry rides every judgment you cast on this page."
    ),
    "QUORUM_ECHO": (
        "Each pair needs {quorum} judgments — you may see pairs you already "
        + "judged until every pair has {quorum} judgments."
    ),
    "ACK_HEADING": "Run registered.",
    "ACK_BEGIN": "BEGIN THE SITTING",
    "ACK_COPY_RUN_ID": "Copy run id",
    "ACK_COPY_URL": "Copy sitting URL",
    "ACK_SHARE": (
        "Each pair needs {quorum} judgments — share this sitting URL with "
        + "your other judges."
    ),
    "ACK_FROZEN": (
        "The list is locked once registered — a changed list is a new run."
    ),
    "ACK_PREFER_A": "You preferred {label_a} (A) over {label_b} (B).",
    "ACK_PREFER_B": "You preferred {label_b} (B) over {label_a} (A).",
    "ACK_TIE": "Tie: {label_a} (A) and {label_b} (B) stand equal.",
    "ACK_ECHO": (
        "This pair was already recorded with the same answer — it stands once."
    ),
    "DONE_HEADING": "The sitting is complete.",
    "DONE_RESTATED": "The run is complete — each pair has its judgments.",
    "DONE_LINK": "See the result",
    "HALT_HEADING": "The ranking is not ready.",
    "HALT_CURE_BRIDGE": (
        "Bridging pairs — connectivity needs NEW comparisons: a comparator "
        + "provides them — sit again (the resume link serves exactly the named "
        + "closing pairs); the solo operator re-sits under a NEW comparator id "
        + "(a new id's judgments are new samples — a changed verdict is a new "
        + "sample)."
    ),
    "HALT_CURE_SHORTFALL": (
        "Shortfall pairs — quorum needs MORE VOTES: more judgments from any "
        + "comparator — existing judges (a changed verdict is a new sample) "
        + "or new ones (share the sitting URL)."
    ),
    "HALT_RESUME": "Resume the sitting",
    "HALT_PROGRESS": "See the run's progress",
    "WITHHOLD_HEADING": "The ranking is not complete.",
    "WITHHOLD_COPY": (
        "The ranking will not be shown until every pair has its judgments — "
        + "never a partial ranking dressed as whole."
    ),
    "WITHHOLD_RESUME": "Resume the sitting",
    "WITHHOLD_PROGRESS": "See the run's progress",
    "UNKNOWN_HEADING": "Unknown run.",
    "UNKNOWN_COPY": "No run answers this address — the wire's own report:",
    "PROGRESS_HEADING": "The run's progress.",
    "PROGRESS_TOTAL": "Judgments recorded:",
    "STATE_POLL_QUIET": "This strip refreshes every 5 seconds.",
    "FOLD_HEADING": "The request failed.",
    "REFUSAL_HEADING": "The request was refused — the wire's own three fields:",
    "FOLD_HEADING_FRAGMENT": "Something broke — the fold's three fields:",
    "EXPECTED_LABEL": "Expected",
    "FOUND_LABEL": "Found",
    "NEXT_ACTION_LABEL": "Next action",
    "RESULT_HEADING": "The ranked whole.",
    "RESULT_COVERAGE_STRIP": (
        "Every scheduled pair at quorum — the comparison graph is connected "
        + "({components | length} component)."
    ),
    "RESULT_CYCLE_TAG": "A cycle is named in the coverage data: {edges}",
    "RESULT_CYCLE_ONE_LINER": (
        "This cycle is structural, never an error, never resolved by "
        + "judgment — the wins, losses, and ties in the table are the honest "
        + "numbers behind each item's position."
    ),
    "RESULT_PAIR_MATRIX": "The pair matrix — judgments per pair:",
    "RESULT_VERSION": "Ranked by {algorithm_version}",
    "TABLE_RANK": "Rank",
    "TABLE_ITEM": "Item",
    "TABLE_WINS": "W",
    "TABLE_LOSSES": "L",
    "TABLE_TIES": "T",
    "TABLE_COMPARISONS": "Comparisons",
    "BUTTON_COPY_DONE": "Copied",
}

# The template bodies — the artifacts' content (the emitted files carry the
# regen header + these bodies with @KEY@ sentinels substituted). Fragments
# do NOT extend the base (HTMX swaps them into the live page).
TEMPLATES: Final[dict[str, str]] = {
    "base.html": (
        "<!DOCTYPE html>\n"
        + '<html lang="en">\n'
        + "<head>\n"
        + '  <meta charset="utf-8">\n'
        + '  <meta name="viewport" content="width=device-width, initial-scale=1">\n'
        + "  <title>{% block title %}@SITE_TITLE@{% endblock %}</title>\n"
        + '  <link rel="stylesheet" href="@SHOELACE_THEME@">\n'
        + '  <script type="module" src="@SHOELACE_AUTOLOADER@"></script>\n'
        + '  <script src="@HTMX@"></script>\n'
        + '  <link rel="stylesheet" href="/static/app.css">\n'
        + '  <script type="module" src="/static/app.js"></script>\n'
        + "</head>\n"
        + "<body>\n"
        + '<main class="wrap">\n'
        + "{% block content %}{% endblock %}\n"
        + "</main>\n"
        + "</body>\n"
        + "</html>\n"
    ),
    "landing.html": (
        '{% extends "base.html" %}\n'
        + "{% block title %}@SITE_TITLE@ — begin{% endblock %}\n"
        + "{% block content %}\n"
        + '<section class="card">\n'
        + "  <h1>@SITE_TITLE@</h1>\n"
        + "  <p>@SITE_EXPLANATION@</p>\n"
        + "  <p>@VOCABULARY@</p>\n"
        + "</section>\n"
        + '<section class="card">\n'
        + "  <h2>Register a run</h2>\n"
        + '  <form hx-post="/ui/register" hx-target="#register-result" hx-swap="innerHTML">\n'
        + "    <label>@OPERATOR_ID_BRIDGE@ <input name=\"operator_id\" required minlength=\"1\"></label>\n"
        + "    <label>@QUESTION_LABEL@ <input name=\"question\" required minlength=\"1\"></label>\n"
        + '    <label>@QUORUM_BRIDGE@ <input type="number" name="quorum" value="1" min="1"></label>\n'
        + "    <fieldset>\n"
        + "      <legend>@ITEMS_LEGEND@</legend>\n"
        + '      <div class="item-row"><input name="item-id" required minlength="1" placeholder="id">'
        + ' <input name="item-label" required minlength="1" placeholder="label"></div>\n'
        + '      <div class="item-row"><input name="item-id" required minlength="1" placeholder="id">'
        + ' <input name="item-label" required minlength="1" placeholder="label"></div>\n'
        + '      <div class="item-row"><input name="item-id" placeholder="id">'
        + ' <input name="item-label" placeholder="label"></div>\n'
        + '      <div class="item-row"><input name="item-id" placeholder="id">'
        + ' <input name="item-label" placeholder="label"></div>\n'
        + '      <div class="item-row"><input name="item-id" placeholder="id">'
        + ' <input name="item-label" placeholder="label"></div>\n'
        + '      <div class="item-row"><input name="item-id" placeholder="id">'
        + ' <input name="item-label" placeholder="label"></div>\n'
        + "    </fieldset>\n"
        + '    <button type="submit">@REGISTER_BUTTON@</button>\n'
        + "  </form>\n"
        + '  <div id="register-result"></div>\n'
        + "</section>\n"
        + '<section class="card">\n'
        + "  <h2>Resume</h2>\n"
        + '  <form method="get" action="/" data-pt-path="/runs/{stem}">\n'
        + "    <label>@RESUME_LABEL@ <input name=\"stem\" placeholder=\"RUN-0001\"></label>\n"
        + '    <button type="submit">Resume the sitting</button>\n'
        + "  </form>\n"
        + '  <p class="quiet">@RUN_ID_BRIDGE@</p>\n'
        + '  <form method="get" action="/" data-pt-path="/runs/{stem}/result">\n'
        + "    <label>@RESULT_LABEL@ <input name=\"stem\" placeholder=\"RUN-0001\"></label>\n"
        + '    <button type="submit">See the result</button>\n'
        + "  </form>\n"
        + "</section>\n"
        + "{% endblock %}\n"
    ),
    "sitting.html": (
        '{% extends "base.html" %}\n'
        + "{% block title %}@SITE_TITLE@ — the sitting{% endblock %}\n"
        + "{% block content %}\n"
        + '<section class="card">\n'
        + "  <h1>{{ question }}</h1>\n"
        + '  <label for="comparator-id">@COMPARATOR_BRIDGE@</label>\n'
        + '  <input id="comparator-id" name="comparator_id" required minlength="1">\n'
        + '  {% if quorum > 1 %}<p class="quiet">@QUORUM_ECHO@</p>{% endif %}\n'
        + '  {% include "pair.html" %}\n'
        + '  <div id="ack-region"></div>\n'
        + "</section>\n"
        + "{% endblock %}\n"
    ),
    "pair.html": (
        '<div id="pair-region">\n'
        + '  <form hx-post="/ui/runs/{{ stem }}/vote" hx-target="#ack-region" hx-swap="innerHTML"'
        + ' hx-include="[name=\'comparator_id\']">\n'
        + '    <input type="hidden" name="item_a" value="{{ item_a }}">\n'
        + '    <input type="hidden" name="item_b" value="{{ item_b }}">\n'
        + '    <div class="cards">\n'
        + '      <sl-card class="pair-card">'
        + '<sl-badge slot="header">A</sl-badge><span class="card-label">{{ label_a }}</span></sl-card>\n'
        + '      <sl-card class="pair-card">'
        + '<sl-badge slot="header">B</sl-badge><span class="card-label">{{ label_b }}</span></sl-card>\n'
        + "    </div>\n"
        + '    <div class="verdicts">\n'
        + "      {% set labels = @VERDICT_BUTTONS@ %}\n"
        + '      {% for verdict in verdicts %}<button class="verdict" name="winner" value="{{ verdict }}">'
        + "{{ labels.get(verdict, verdict) }}</button>{% endfor %}\n"
        + "    </div>\n"
        + "  </form>\n"
        + "</div>\n"
    ),
    "vote-ack.html": (
        '<div id="vote-ack">\n'
        + '  <p class="ack-line">'
        + "{% if winner == 'prefer-a' %}@ACK_PREFER_A@"
        + "{% elif winner == 'prefer-b' %}@ACK_PREFER_B@"
        + "{% else %}@ACK_TIE@{% endif %}</p>\n"
        + '  {% if not acknowledged %}<p class="quiet">@ACK_ECHO@</p>{% endif %}\n'
        + '  <div hx-get="/ui/runs/{{ stem }}/pair" hx-trigger="load" hx-target="#pair-region"'
        + ' hx-swap="outerHTML"></div>\n'
        + "</div>\n"
    ),
    "ack.html": (
        '<div id="register-ack">\n'
        + "  <p><strong>@ACK_HEADING@</strong></p>\n"
        + '  <p>The run id: <strong>{{ run_id }}</strong>'
        + ' <pt-copy value="{{ run_id }}" label="@ACK_COPY_RUN_ID@"></pt-copy></p>\n'
        + '  <p>The sitting URL: <code>{{ sitting_url }}</code>'
        + ' <pt-copy value="{{ sitting_url }}" label="@ACK_COPY_URL@"></pt-copy></p>\n'
        + '  {% if quorum > 1 %}<p class="share">@ACK_SHARE@</p>{% endif %}\n'
        + '  <p class="quiet">@ACK_FROZEN@</p>\n'
        + '  <sl-button variant="primary" href="/runs/{{ run_id }}">@ACK_BEGIN@</sl-button>\n'
        + "</div>\n"
    ),
    "state-strip.html": (
        '<div id="state-strip" hx-get="/ui/runs/{{ stem }}/state" hx-trigger="every 5s"'
        + ' hx-swap="outerHTML">\n'
        + "  <p>@PROGRESS_TOTAL@ <strong>{{ total }}</strong></p>\n"
        + '  <ul class="involvement">\n'
        + "    {% for item_id, involvement in items.items() %}"
        + "<li>{{ item_id }}: {{ involvement }}</li>{% endfor %}\n"
        + "  </ul>\n"
        + '  <p class="quiet">@STATE_POLL_QUIET@</p>\n'
        + "</div>\n"
    ),
    "refuse.html": (
        '<div class="refusal">\n'
        + '  <p><strong>{% if fold %}@FOLD_HEADING_FRAGMENT@{% else %}@REFUSAL_HEADING@{% endif %}'
        + "</strong></p>\n"
        + '  <dl class="three-part">\n'
        + "    <dt>@EXPECTED_LABEL@</dt><dd>{{ fields.expected }}</dd>\n"
        + "    <dt>@FOUND_LABEL@</dt><dd>{{ fields.found }}</dd>\n"
        + "    <dt>@NEXT_ACTION_LABEL@</dt><dd>{{ fields.next_action }}</dd>\n"
        + "  </dl>\n"
        + "</div>\n"
    ),
    "done.html": (
        '{% extends "base.html" %}\n'
        + "{% block title %}@SITE_TITLE@ — done{% endblock %}\n"
        + "{% block content %}\n"
        + '<section class="card">\n'
        + "  <h1>@DONE_HEADING@</h1>\n"
        + '  <sl-badge variant="success">done</sl-badge>\n'
        + '  <p class="coverage">{{ fields.expected }}</p>\n'
        + "  <p>@DONE_RESTATED@</p>\n"
        + '  <sl-button variant="primary" href="/runs/{{ stem }}/result">@DONE_LINK@</sl-button>\n'
        + "</section>\n"
        + "{% endblock %}\n"
    ),
    "progress.html": (
        '{% extends "base.html" %}\n'
        + "{% block title %}@SITE_TITLE@ — progress{% endblock %}\n"
        + "{% block content %}\n"
        + '<section class="card">\n'
        + "  <h1>@PROGRESS_HEADING@</h1>\n"
        + '  {% include "state-strip.html" %}\n'
        + "</section>\n"
        + "{% endblock %}\n"
    ),
    "result.html": (
        '{% extends "base.html" %}\n'
        + "{% block title %}@SITE_TITLE@ — the result{% endblock %}\n"
        + "{% block content %}\n"
        + '<section class="card">\n'
        + "  <h1>@RESULT_HEADING@</h1>\n"
        + '  <sl-badge variant="success">done</sl-badge>\n'
        + '  <table class="ranked">\n'
        + "    <thead><tr><th>@TABLE_RANK@</th><th>@TABLE_ITEM@</th><th>@TABLE_WINS@</th>"
        + "<th>@TABLE_LOSSES@</th><th>@TABLE_TIES@</th><th>@TABLE_COMPARISONS@</th></tr></thead>\n"
        + "    <tbody>\n"
        + "      {% for rank, group in ranked %}{% set outer = loop %}{% for item in group %}\n"
        + "      <tr>\n"
        + '        {% if outer.first %}<td rowspan="{{ group | length }}">{{ rank }}</td>{% endif %}\n'
        + '        <td>{{ rows[item].label }} <sl-badge>{{ item }}</sl-badge></td>\n'
        + "        <td>{{ rows[item].wins }}</td>\n"
        + "        <td>{{ rows[item].losses }}</td>\n"
        + "        <td>{{ rows[item].ties }}</td>\n"
        + "        <td>{{ rows[item].wins + rows[item].losses + rows[item].ties }}</td>\n"
        + "      </tr>\n"
        + "      {% endfor %}{% endfor %}\n"
        + "    </tbody>\n"
        + "  </table>\n"
        + '  <p class="coverage-strip">@RESULT_COVERAGE_STRIP@</p>\n'
        + "  {% if cycle %}\n"
        + '  <sl-tooltip content="@RESULT_CYCLE_ONE_LINER@">\n'
        + '    <sl-tag variant="neutral">@RESULT_CYCLE_TAG@\n'
        + "  {% for edge in cycle %}{{ edge[0] }} &gt; {{ edge[1] }}{% if not loop.last %}, {% endif %}{% endfor %}\n"
        + "  </sl-tag></sl-tooltip>\n"
        + "  {% endif %}\n"
        + '  <sl-details summary="The coverage datum">\n'
        + "    <p>@RESULT_COVERAGE_STRIP@</p>\n"
        + "    <p>@RESULT_PAIR_MATRIX@</p>\n"
        + "    <ul>\n"
        + "      {% for key, count in pair_counts.items() %}<li>{{ key }}: {{ count }}</li>{% endfor %}\n"
        + "    </ul>\n"
        + "  </sl-details>\n"
        + "  <footer><sl-badge>{{ algorithm_version }}</sl-badge> — @RESULT_VERSION@</footer>\n"
        + "</section>\n"
        + "{% endblock %}\n"
    ),
    "halt.html": (
        '{% extends "base.html" %}\n'
        + "{% block title %}@SITE_TITLE@ — not ready{% endblock %}\n"
        + "{% block content %}\n"
        + '<section class="card">\n'
        + "  <h1>{% if gated %}@WITHHOLD_HEADING@{% else %}@HALT_HEADING@{% endif %}</h1>\n"
        + '  {% if gated %}<sl-badge variant="neutral">withheld</sl-badge>'
        + '<p>@WITHHOLD_COPY@</p>{% else %}<sl-badge variant="warning">safe halt</sl-badge>\n'
        + '  <dl class="three-part">\n'
        + "    <dt>@EXPECTED_LABEL@</dt><dd>{{ fields.expected }}</dd>\n"
        + "    <dt>@FOUND_LABEL@</dt><dd>{{ fields.found }}</dd>\n"
        + "    <dt>@NEXT_ACTION_LABEL@</dt><dd>{{ fields.next_action }}</dd>\n"
        + "  </dl>\n"
        + '  <ul>\n'
        + "    <li>@HALT_CURE_BRIDGE@</li>\n"
        + "    <li>@HALT_CURE_SHORTFALL@</li>\n"
        + "  </ul>{% endif %}\n"
        + '  <sl-button variant="primary" href="/runs/{{ stem }}">'
        + "{% if gated %}@WITHHOLD_RESUME@{% else %}@HALT_RESUME@{% endif %}</sl-button>\n"
        + '  <a href="/runs/{{ stem }}/progress">'
        + "{% if gated %}@WITHHOLD_PROGRESS@{% else %}@HALT_PROGRESS@{% endif %}</a>\n"
        + "</section>\n"
        + "{% endblock %}\n"
    ),
    "unknown.html": (
        '{% extends "base.html" %}\n'
        + "{% block title %}@SITE_TITLE@ — unknown run{% endblock %}\n"
        + "{% block content %}\n"
        + '<section class="card">\n'
        + "  <h1>@UNKNOWN_HEADING@</h1>\n"
        + "  <p>@UNKNOWN_COPY@</p>\n"
        + '  <p class="wire-found">{{ fields.found }}</p>\n'
        + '  <form method="get" action="/" data-pt-path="/runs/{stem}">\n'
        + "    <label>@RESUME_LABEL@ <input name=\"stem\" placeholder=\"RUN-0001\"></label>\n"
        + '    <button type="submit">Resume the sitting</button>\n'
        + "  </form>\n"
        + '  <p class="quiet">@RUN_ID_BRIDGE@</p>\n'
        + "</section>\n"
        + "{% endblock %}\n"
    ),
    "fold.html": (
        '{% extends "base.html" %}\n'
        + "{% block title %}@SITE_TITLE@ — the fold{% endblock %}\n"
        + "{% block content %}\n"
        + '<section class="card">\n'
        + "  <h1>@FOLD_HEADING@</h1>\n"
        + '  <dl class="three-part">\n'
        + "    <dt>@EXPECTED_LABEL@</dt><dd>{{ fields.expected }}</dd>\n"
        + "    <dt>@FOUND_LABEL@</dt><dd>{{ fields.found }}</dd>\n"
        + "    <dt>@NEXT_ACTION_LABEL@</dt><dd>{{ fields.next_action }}</dd>\n"
        + "  </dl>\n"
        + "</section>\n"
        + "{% endblock %}\n"
    ),
}

# The generated stylesheet (the semantic table's CSS — Shoelace ships NO
# table component, the honest pick carries its own styling).
STYLESHEET: Final[str] = (
    ":root { --pt-gap: 0.75rem; }\n"
    + "body { margin: 0; font-family: system-ui, sans-serif; background: #fafafa; color: #1a1a1a; }\n"
    + ".wrap { max-width: 40rem; margin: 0 auto; padding: var(--pt-gap); }\n"
    + ".card { background: white; border-radius: 0.5rem; padding: var(--pt-gap); margin-bottom: var(--pt-gap); }\n"
    + "label { display: block; margin: 0.5rem 0; }\n"
    + "input { display: block; width: 100%; box-sizing: border-box; padding: 0.4rem; margin-top: 0.2rem; }\n"
    + ".item-row input { display: inline-block; width: calc(50% - 0.25rem); }\n"
    + ".cards { display: flex; gap: var(--pt-gap); margin: var(--pt-gap) 0; }\n"
    + ".pair-card { flex: 1; }\n"
    + ".card-label { font-size: 1.1rem; }\n"
    + ".verdicts { display: flex; gap: var(--pt-gap); flex-wrap: wrap; }\n"
    + "button.verdict { padding: 0.6rem 1.2rem; }\n"
    + "table.ranked { border-collapse: collapse; width: 100%; margin: var(--pt-gap) 0; }\n"
    + "table.ranked th, table.ranked td { border: 1px solid #ddd; padding: 0.4rem; text-align: left; }\n"
    + "table.ranked th { background: #f0f0f0; }\n"
    + ".coverage-strip { color: #666; }\n"
    + ".three-part dt { font-weight: bold; margin-top: 0.5rem; }\n"
    + ".three-part dd { margin: 0; }\n"
    + ".wire-found { font-family: monospace; background: #f4f4f4; padding: 0.5rem; border-radius: 0.3rem; }\n"
    + ".quiet { color: #666; }\n"
    + ".share { background: #eef6ff; padding: 0.5rem; border-radius: 0.3rem; }\n"
    + ".refusal { background: #fff7f0; border-left: 3px solid #e67e22; padding: var(--pt-gap); }\n"
    + "#state-strip { background: #f4f4f4; padding: var(--pt-gap); border-radius: 0.3rem; }\n"
    + ".involvement { columns: 2; margin: 0.5rem 0; }\n"
    + ".ack-line { font-size: 1.1rem; }\n"
    + "footer { color: #666; margin-top: var(--pt-gap); }\n"
)

# The entire Web Components surface (R1: ALL frontend things generated from
# Python — the JS itself is structure data). pt-copy: the click-to-copy
# affordance (the clipboard call is the component's own generated JS — in
# grammar). The pt-path delegation: the landing's resume + direct-result
# fields NAVIGATE (the page routes) without a query-string landing — a
# delegated submit listener reads the form's data-pt-path, substitutes the
# stem, and assigns the location (navigation JS, never validation JS: the
# wire stays the sole validator, the design §5's dropped-pre-checks ruling
# held).
APP_JS: Final[str] = (
    "class PtCopy extends HTMLElement {\n"
    + "  connectedCallback() {\n"
    + '    const value = this.getAttribute("value") ?? "";\n'
    + '    const label = this.getAttribute("label") ?? "Copy";\n'
    + '    const button = document.createElement("sl-button");\n'
    + "    button.textContent = label;\n"
    + '    button.addEventListener("click", () => {\n'
    + "      navigator.clipboard.writeText(value);\n"
    + '      button.textContent = "Copied";\n'
    + "      window.setTimeout(() => { button.textContent = label; }, 2000);\n"
    + "    });\n"
    + "    this.replaceChildren(button);\n"
    + "  }\n"
    + "}\n"
    + 'customElements.define("pt-copy", PtCopy);\n'
    + "document.addEventListener(\"submit\", (event) => {\n"
    + "  const form = event.target;\n"
    + '  const path = form.getAttribute("data-pt-path");\n'
    + "  if (path === null) { return; }\n"
    + "  event.preventDefault();\n"
    + '  const stem = form.querySelector("input[name=\'stem\']").value.trim();\n'
    + "  if (stem) { window.location.assign(path.replace(\"{stem}\", encodeURIComponent(stem))); }\n"
    + "});\n"
)
