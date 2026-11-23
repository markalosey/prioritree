<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/readme

**Route:** prioritree-review (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T01:43:39Z |
| 2 | report | togo | 2026-11-23T01:45:39Z |
## Reported by togo — 2026-11-23T01:45:39Z

# THE README-DOCS UNIT BRIEF — togo's synthesis (prioritree-review, G-README-BRIEF, 2026-11-22)

Ground consumed: the review brief (reports/synthesize/review-brief.md — §1a the consistency breaks, §1c-1e the command honesty + hyoka's rank + moho's three fixes, §2 the ruled shape + the hybrid install story, §3 unit 1's fence + gate) + the census legs (tansa's doc-surface — the surfaces + the docstrings' claims; rikai's consistency — the stale numbers at their cited lines; keisan's commands — the honest fresh-clone sequence, the 12/3/1 inventory) + the design lane (suisen's install-story — the hybrid (e) + the README's outline; moho's blind-walk — the three fixes + the seven-point friction map; hyoka's adversarial — the ruff-pending truth, the ranked cures, every finding held) + Q-repo-review's four rulings (junro.json — R1 the scope, R2 the deliverable's discretion, R3 the governance, R4 THE FOUR CALLS: MIT landed, web+mcp in the wheel, the scrub deferred, PyPI deferred) + the landed LICENSE (the pairing to name) + the current three files at HEAD (README.md 24 lines, CONTINUATION.md 76, AGENTS.md 4) + the hygiene unit's brief (reports/synthesize/hygiene.md — the sibling dependency: the README names the LICENSE, named there, ruled here). The synthesis decides nothing; the collaborator rules at the gate.

## 1. THE SCOPE FENCE — three files, one door

**LANDS:**
1. **README.md WHOLE — the rewrite:** every section re-authored per §2's ruled shape; the current 24 lines the base, the product sentence + the Q-purpose blockquote + the measured citation kept verbatim where ruled; every stale number cured.
2. **CONTINUATION.md's refresh** — the eras current (the MCP era recorded, the review effort named) + the four drifts cured (§3).
3. **AGENTS.md's regen-line truth** — the honest annotation naming the hikari-side engine (§3).

**DOES NOT TOUCH:**
- **The Makefile** — the operator's doc stands (the nine targets self-document, every refusal ThreePart; the README cites, never rewrites).
- **pyproject.toml** — the hygiene unit landed license + authors; the packaging question (web/ + MCP into the wheel, ruling 4's call 2) rides the install-deliverable unit.
- **The src docstrings** — no code touched (service.py:44-45's fence-wording drift is the polish class, unowned here; named for the collaborator's later call).
- **The .opencode surfaces** — the 13 seat prompts + 12 tool wrappers: cycle-generated, hikari-side regeneration only (the standing law; the sibling action named at the review brief).
- **.githooks/pre-commit** — the hook's own header carries the same dead regen line (hyoka's fourth instance): cycle-generated, the hikari-side re-emit's surface — named for the sibling action; this unit's AGENTS.md annotation the in-tree precedent.
- **The .plans records** — the scrub deferred (ruling 4's call 3); the README's measured citation must keep resolving (the budget-curve record's tracked path stands).
- **The README's install-lane BYTES after this unit** — the install-deliverable unit owns the lane when the wheel grows web/ + MCP; this unit authors the lane per the CURRENT truth, the sibling dependency named, never re-ruled here.

## 2. THE README'S WHOLE SHAPE RULED — the sections in order, each's content pinned

**2.1 THE INTRO** — the product sentence (README:3's ruled language, byte-identical to pyproject:4 — stands); the measured citation (51 of 54 in-band cells, 94.4%, the record at .plans/ideation/2026-11-21-budget-curve/build/budget-curve-record.md — tracked, resolves at a fresh clone, KEPT); the comparator-class line (human AND LLM through the one vote interface); the Q-purpose blockquote verbatim (the ruled citation, KEPT); **THE LICENSE NAMED** — MIT, the file at the root (Copyright (c) 2026 Mark Losey; pyproject:7 license = "MIT") — the hygiene unit's pairing carried (the 33 header lines' "All rights reserved" answered by the grant).

**2.2 THE QUICKSTART (moho's fix 1 — install + a first comparison end-to-end):** the exact sequence per keisan's arithmetic — `git clone <repo>` → `cd prioritree` → `make dev` → `make test` → `git config core.hooksPath .githooks` → `make start` → open http://127.0.0.1:8000/ (the browser: the web tier the human's first-comparison surface — register a list, vote the pairs, read the tally) — **PLUS the CLI-only first-session alternative, the ten-line form:** `uv tool install .` → `prioritree register …` → `prioritree next …` → `prioritree vote …` → `prioritree tally …` (the five-op surface, state optional; per-project state by design). The exact transcript bytes authored against a live run at the spec lane. The floor's remaining legs (make lint, make typecheck) ride §2.7's full sequence — the Quickstart's job is the first comparison, the Install lanes' the whole honest path.

**2.3 THE ARCHITECTURE SECTION — the FIVE tiers current, every stale number cured:**
- **Library — src/prioritree** — the pure-logic core (items, the comparison operator, pair scheduling, votes, tally; the tally a pure function of the stored votes) — BUILT 2026-11-20.
- **CLI** — the five-op surface (register → next → vote → state → tally), the console script — BUILT 2026-11-21.
- **Service (FastAPI)** — **SIX routes** over HTTP (the five ops 1:1 + the manifest query), the lock seam, the ThreePart error surface 21/21 — LIVE 2026-11-21.
- **Web** — web.py (654 lines, nine routes, 14 authored templates + 2 statics), fronts the service over the in-process seam — **BUILT 2026-11-22** (never "banked" again).
- **MCP** — mcp_server.py (580 lines, the five OunceMCP tools: runs.register, runs.next, votes.cast, votes.census, runs.tally; store_lock.py's flock seam), two run forms — **LIVE 2026-11-22** (never "the ruled next effort" again).
Plus: the deps cured — **SIX** (fastapi, httpx2, jinja2, ouncemcp, python-multipart, uvicorn[standard]; pyproject:9 — never "fastapi + uvicorn[standard]" again); the **197-test** floor (keisan's live run: 197 passed, zero failures); the eras current.

**2.4 THE USAGE SECTION — tier-by-tier:**
- **CLI:** the invocation (`prioritree <op>` — the console script; five subcommands), the flags (--question/--quorum/--seed/--operator-id at register; --notes/--supersedes at vote; --home the store escape on all five; the id:label register token, first-colon split), the exit-code contract (0 success AND DONE; 1 the refusals; 2 argv+unexpected), an example per op.
- **Service:** the launch (`uvicorn prioritree.service:app` — or make start); the six routes with their HTTP verbs (POST register/cast, GET next/census/manifest, the tally route); PORT/HOST.
- **Web:** the make targets (start/stop/status/restart) + PORT/HOST overrides (PORT ?= 8000, HOST ?= 127.0.0.1; `make start PORT=8100`); the browser at http://127.0.0.1:8000/.
- **MCP:** the two run forms — `python -m prioritree.mcp_server` (stdio, per session, the MCP host's boot) / the --serve flag (streamable-HTTP) — **+ the port-collision note:** --serve hardcodes port 8000 = make start's default; one at a time, or `make start PORT=<other>`.

**2.5 THE INPUT/OUTPUT EXAMPLES (moho's fix 2 — a list going in, a vote, the tally emitted):** the exact CLI transcript — a register (the id:label tokens in), a next (the pair line out), a vote (the winner cast), the tally emitted (the marker-first, tab-separated report language: the rank/counts/coverage lines) — authored against a live run at the spec lane; the report language's markers named (pair/vote/ack/item/rank/counts/coverage).

**2.6 THE DISCIPLINE BLOCK:**
- **The CWD law:** the store (STORE_HOME = .prioritree/runs) + the web mounts (web/templates, web/static) resolve CWD-relative — run from the repo root or the data lands where you stood (silent mkdir on demand); --home the CLI's escape.
- **The hooksPath truth + the ruff-pending fact (hyoka's rank 2 — never claim the floor where only pyright rides):** .githooks/pre-commit is tracked but the pointer never clones — set it by hand (git config core.hooksPath .githooks); the hook enforces PYRIGHT ONLY (ruff is Phase 2, named, pending; PRIORITREE_HOOK_BYPASS=1 the tracked bypass).
- **The port collision** (per §2.4's note).
- **.prioritree/ mints at runtime** (the pid/log/runs home; gitignored — never in a clone).

**2.7 THE INSTALL LANES:**
- **The clone primary** — the ONLY whole-product path (web/templates + static ride the clone; the CWD-relative homes resolve at the root; all five tiers operable): the requirements (Python 3.13+, uv) + the FULL honest fresh-clone sequence per keisan — clone → cd prioritree → make dev → make test → make lint → make typecheck → git config core.hooksPath .githooks → make start → open http://127.0.0.1:8000/.
- **uv tool install . — the CLI-anywhere lane:** the prioritree console script + the six deps, usable anywhere; per-project state by design; **+ the web-absence truth for the tool lane:** the wheel carries src/prioritree only (the packages field) — no web templates, no web tier at an installed location today; the clone the web tier's only home (the install unit's packaging cure the named future — this line the lane's current truth, honest at its own landing).
- **The honest no-PyPI line:** prioritree is NOT on PyPI — `uv tool install prioritree` / `pip install prioritree` do not resolve; the publish DEFERRED (ruling 4's call 4: the preconditions — the LICENSE landed, the packaging + CI remaining; the trigger a later call). Never a promise until earned.

**2.8 THE STATUS SECTION — current:** born 2026-11-19; the core 2026-11-20; the CLI 2026-11-21; the claim measured 2026-11-21; the service 2026-11-21; the web 2026-11-22; the MCP tier live 2026-11-22 (the five OunceMCP tools); CI deferred (git hooks + local gates stand in); the 197-test floor. No next-effort promises — the status reports what IS.

**2.9 THE LICENSE SECTION:** MIT + the file — the LICENSE at the repo root (Copyright (c) 2026 Mark Losey), pyproject's license = "MIT"; the headers' rights claims paired by the grant.

## 3. CONTINUATION'S REFRESH + AGENTS' TRUTH — the ruled cures

**CONTINUATION.md (the record's entries are history — the cures are accuracy fixes at their cited lines, never rewrites):**
- **The eras current (:72-76 — "WHERE TO CONTINUE FROM" still names the MCP era NEXT):** the MCP era's state recorded (mcp_server.py + store_lock.py landed; mcp-server green at the first unit boundary; member-path + lifecycle-integration resting) + **the review effort named** (prioritree-review, born 2026-11-22 — the exhaustive review: the census whole, the four calls ruled — MIT landed, web+MCP in the wheel, the scrub deferred, PyPI deferred; the cure units composing).
- **The drift cures:** :53 "httpx2 dev the root cure" → httpx2 rides the MAIN deps table (pyproject:9; the dev group = pytest/pyright/ruff only — the service-era history named as history or re-worded to the current truth); :19 "the ten wrappers" → TWELVE (kumi_render.ts + lifecycle.ts the later arrivals); :65 "web.py at 655 lines" → 654.

**AGENTS.md (4 lines — the goal-line record):**
- **The regen line's truth (:1-2):** it cites scripts/generation/clarity_scaffold.py — the directory EMPTY in this repo; the engine lives at hikari. **THE CURE RULED: the honest annotation naming the hikari-side engine** — the regen command runs from the hikari tree (the cross-project form, the engine stays home); this repo's scripts/generation/ carries nothing. The ruled goal line (the Q-harness ruling verbatim) stands untouched.
- The same dead line rides .githooks/pre-commit's header + the 13 seat prompts — cycle-generated, the hikari-side re-emit's surfaces; named for the sibling action, out of this fence.

## 4. THE ACCEPTANCE MAPPING — G-README's three conditions (junro.json:296-302)

1. **The rewrite per the approved spec** → §2's whole shape; the spec lane (synthesize/readmespec, closing G-READMESPEC-BRIEF) pins the exact bytes — this brief the shape, the spec the bytes.
2. **CONTINUATION refreshed + AGENTS' truth + every stale number cured** → each correction checkable against the review brief's §1 at its cited line: deps 6, routes 6, tests 197, the five tiers, the eras current; CONTINUATION's four drifts + the era refresh; AGENTS' annotation. Moho's three fixes authored in (the Quickstart end-to-end; the input/output transcript; the per-tier launch lines).
3. **The floor + kensho** → the cures touch zero code bytes (three prose files): pyright 0/0/0, ruff zero findings, the suite green (197); **kensho's independent check at validate/readme** — every claim verified against the tree (the README's numbers match pyproject/service/the floor; every documented command runs as written).

## 5. THE HANDOFF — the spec lane's opens (synthesize/readmespec → G-READMESPEC-BRIEF)

- **THE README'S EXACT BYTES** — the biggest single-file fence: the whole file authored (the ruled sections in §2's order; the kept verbatim blocks pinned byte-precise; every command line verified runnable).
- **CONTINUATION's hunks** — the exact before/after at the four drift lines + the era section's refresh (byte-precise, the record otherwise untouched).
- **AGENTS' hunk** — the annotation's exact bytes.
- **The transcript bytes** — the Quickstart's and §2.5's exact CLI output authored against a live run (moho's bar: every line the spec promises must run).
- **The per-step plan — three files, the README first:** (1) README.md (the rewrite — the biggest single-file fence, its own dispatch); (2) CONTINUATION.md (the refresh); (3) AGENTS.md (the annotation) — each its own dispatch per R8's file-unit law, each step's completing act the report op (R6/R11), one commit per increment at the landing. The return forms: the bounded return per step; the dispatches cite this brief.

## 6. THE TRADE-OFF THE PLAN CARRIES

The README becomes a world-facing door on a tree whose vocabulary is internal: moho's friction map (the process jargon — Q-rulings, seat names, harness grammar — cold-lands in the world's only doc) rules the rewrite's VOICE, while the measured citation's tracked path (.plans/…budget-curve-record.md) must SURVIVE it — the one evidence link, kept resolving, never excised for cleanliness. And the lane's honest impermanence: the tool-lane line names the web-absence truth THIS unit lands, knowing the install unit's packaging cure (ruling 4's call 2) will re-rule that same line — a named moving surface, honest at each landing, never a promise ahead of its truth. And the split that reconciles the two walks: moho's under-ten-lines vs keisan's nine-step floor — the Quickstart carries the first comparison, the Install lanes the whole honest sequence; neither walk sacrificed to the other.

— togo, the synthesis leg, read-only by design; this report is the one write.
