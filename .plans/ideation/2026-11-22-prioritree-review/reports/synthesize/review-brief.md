<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/review-brief

**Route:** prioritree-review (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T01:13:08Z |
| 2 | report | togo | 2026-11-23T01:14:03Z |
## Reported by togo — 2026-11-23T01:14:03Z

# THE REVIEW BRIEF — togo's synthesis (prioritree-review, G-REVIEW-BRIEF, 2026-11-22)

Ground consumed: the seven seat-authored reports — census (tansa's doc-surface, shindan's hygiene, rikai's consistency, keisan's commands) + design (suisen's install-story, hyoka's adversarial, moho's blind-walk) — and Q-repo-review's three rulings (R1 the exhaustive scope, R2 the deliverable's discretion with the uv leaning carried, R3 the governance). The synthesis decides nothing; the collaborator rules at the gate.

## 1. THE FINDINGS WHOLE

### 1a. The consistency breaks

**README.md — wrong on every load-bearing number, and empty where it matters (BLOCKING, hyoka's rank 1):**
- :19 "first runtime deps: fastapi + uvicorn[standard]" → SIX at pyproject:7 (+ httpx2, jinja2, ouncemcp, python-multipart)
- :19 "the five routes" → SIX in service.py (the manifest query, :490)
- :20 web "banked" → web.py 654 lines, nine routes, 14 templates, mounted at the service tail — built 2026-11-22
- :24 "The MCP tier is the ruled next effort" → mcp_server.py live (five OunceMCP tools, 580 lines), the mcp store executing; the tier also MISSING from the architecture list (:15 "All four forms" — the tree has FIVE tiers)
- :24 "131 tests green at close" → keisan's LIVE run: 197 passed in 26.74s, zero failures
- ZERO commands anywhere in the file: no install, no usage, no launch — the product unoperable from the world's only door (moho: a silent dead end; the biggest gap)

**CONTINUATION.md — one era behind, four drifts (hyoka's polish class):** names the MCP era NEXT (:72-76) though it exists on disk; :53 "httpx2 dev the root cure" → httpx2 rides the MAIN table (wrong as present state); :19 "the ten wrappers" → twelve; :65 "web.py at 655 lines" → 654.

**AGENTS.md + the hook — the dead regen lines:** AGENTS.md's regen header cites scripts/generation/clarity_scaffold.py — the directory is EMPTY in this repo (the engine lives in hikari); the .githooks/pre-commit header carries the SAME dead line (hyoka's fourth instance of the class).

**The fresh-clone gaps:**
- **THE HOOK'S POINTER + ITS CONTENT:** .githooks/pre-commit is tracked but the hooksPath pointer lives in .git/config — never cloned; the floor is silently unenforced at a fresh clone. And the hook's own content: ruff is "PHASE 2 (named, pending)" in the hook's header — even with the pointer set, only pyright rides; the lint half of the floor is NOT enforced at commit (hyoka's addition — the gap is larger than censused). Also tracked: PRIORITREE_HOOK_BYPASS=1, the bypass env var.
- **THE WHEEL'S WEB-ABSENCE:** pyproject:16-17 packages=["src/prioritree"] — web/ sits outside it; every pip/uv install carries NO templates; web.py mounts CWD-relative web/templates + web/static → outside the repo every page folds to an honest 500 (TemplateNotFound), static 404s: the web tier is clone-only by construction. The flat deps table also drags all six packages behind a stdlib-only CLI (cli.py:19's "zero runtime dependencies" vs the packaged truth — the fence wording predates the web tier, service.py:44-45).
- **THE PORT COLLISION:** make start's PORT ?= 8000 (Makefile:3) vs mcp --serve's port=8000 hardcoded (mcp_server.py:574), no override flag — the two servers collide at boot with uvicorn's raw "address already in use".
- **THE CWD SILENT WRONG STORE:** STORE_HOME=.prioritree/runs (run_store.py:53) is CWD-relative everywhere; a server booted from another cwd silently uses a DIFFERENT store — data lands where you stood, mkdir on demand; the repo-root discipline lives in the Makefile help and the docstrings, absent from the README.

### 1b. The hygiene map

**ZERO SECRETS — CONFIRMED twice** (shindan's sweep; hyoka's independent greps): no credential has ever landed in a tracked file. The marker hits are false positives by construction — the sweep's own prompt echo (packets.jsonl:7, ruled noise for future sweeps), sk- 82x substrings ("task-/ask-/desk-"), token 100x grammar/budget/tiktoken uses, API_KEY 34x variable names (env reads + honest missing-key errors, no VALUES), secret 18x scope text. .env exists on disk but is gitignored by design (:133; .envrc tracked, "NO SECRETS LIVE HERE"). **uv.lock: zero private paths AND zero private sources** — httpx2/ouncemcp resolve publicly (no git+/gitea/file:/ssh:// in the lock); the fresh-clone arithmetic HOLDS (hyoka's unasked highest-stakes question, answered).

**The private-path surfaces:** shipped code (src/, tests/, web/) — ZERO /Users/, ZERO ~. The exposure rides: (a) .opencode configs (junro.ts's 18 invocation lines :101-:263, git.ts :53-:84, kumi_render.ts :49/:51, jikko.md:14 — all /Users/marklosey/projects/kepric/hikari/ absolute paths); (b) .plans records — 100+ /Users/ hits (tree-root maps, briefs' patch roots, every dispatch prompt, friction-ledger surfaces), the internal infra line gitea.kepric.io + LAN IP 192.168.1.22 (foundations.md:179), one real ~ expansion (friction-ledger.jsonl:9); (c) CONTINUATION.md:11 (the repo root in the harness record). Personal data: NO email anywhere; the uniform copyright lines (all 14 src modules + all 18 test files, "Mark A Losey" in two) — deliberate but UNPAIRED (no LICENSE file, no pyproject authors field); the internal family names at service.py:250 + tests/__init__.py:2. The false-positive map: .gitignore:1-176 is the standard Python template's residue — never applicable, not a leak.

**The five real cures (shindan's fence — everything else is noise, no blanket rewrite):** (i) .opencode paths → hikari-side regeneration; (ii) .plans → the ruled live scrub; (iii) CONTINUATION.md:11 → in-tree rewrite; (iv) the copyright/LICENSE pairing; (v) the family-name comments.

### 1c. The command honesty (keisan)

20 commands documented across the surfaces; 16 checked at this tree: **12 run / 3 need-context / 1 broken.** The one broken: bare `uv tool install prioritree` — unpublished, the resolver's own "no version found". The three needs-context: the uvicorn launch form (presumes repo-root CWD), the bare MCP stdio boot (the MCP host's, per session), the MCP --serve (the port-8000 collision). The 12 that run include the whole Makefile lifecycle — the one tier already honest (every refusal carries expected/found/next-action verbatim; the read-backs probe the guaranteed-404 form). **THE HONEST FRESH-CLONE SEQUENCE** (what the tree actually supports — NONE of it stated in README): clone → cd prioritree → make dev → make test → make lint → make typecheck → git config core.hooksPath .githooks → make start → open http://127.0.0.1:8000/.

### 1d. hyoka's rank (blocking a public ship first)

1. **BLOCKING — README rewrite:** wrong on every load-bearing number (deps 2→6, routes 5→6, web/MCP eras, tests 131→197), zero commands — the product unoperable from the world's only door.
2. **BLOCKING — the floor truth:** the hooksPath instruction must land in the README (the only world-facing place) + the ruff-pending fact named — never claim the floor where only pyright rides.
3. **BLOCKING — the privacy class, ONE cure-set:** .plans scrub (100+ /Users/, gitea + LAN IP) + .opencode path regeneration (hikari-side) + CONTINUATION:11 + the family-name comments — all tracked, all ship with the public clone.
4. **BLOCKING — LICENSE:** 32 files claim "All rights reserved" with no grant; the world cannot legally use a line of it.
5. **MUST-DECIDE — the wheel's web-absence:** ship web/ in the packages field or say the CLI-only truth.
6. **POLISH —** the port collision (a warning or a flag); CONTINUATION's staleness; the dead regen lines; service.py:44-45's fence wording drift.

### 1e. moho's three fixes (the user-pain order)

1. **The Quickstart** — install + a first comparison, end-to-end under ten lines.
2. **The input/output examples** — a list in, a vote, the tally out.
3. **The per-tier launch lines** — the CLI invocation and the uvicorn start.
Verdict: the README reports the build to the builders; the product is invisible to the user it was built for.

**Divergences: none survive reconciliation.** Hyoka attacked every load-bearing finding — every one HELD at its cited line (README's staleness read whole, the .git/config pointer read, the wheel read, the port read, the greps re-run). The one apparent census divergence (rikai "17 modules" vs keisan/shindan "18 files") is the same set under different nouns (17 test modules + __init__.py). The missed surfaces (the hook's content, the lock's sources, the templates' copy) ADD to the gap list and CONFIRM the arithmetic, never overturn. The census MEETS THE BAR as this synthesis's ground — the brief proceeds.

## 2. THE RECOMMENDATION CARRIED (R2's ruling form — the collaborator rules)

**THE HYBRID INSTALL STORY (suisen's (e), the leaning confirmed in its runnable form):** the repo clone as the README's primary Install (the ONLY whole-product path — web/templates + static ride the clone; the CWD-relative homes resolve at the root; all five tiers operable) **+ `uv tool install .` as the documented CLI-anywhere lane** (runs today: the prioritree console script + the six deps, usable anywhere; per-project state by design, --home the named escape; the NO-web-tier truth named honestly). **PyPI DEFERRED** — never a README promise until earned; the named preconditions: the LICENSE pairing, CI (deferred, no .github/), and the packaging ruling. `pip install prioritree` declined (the publish question minus uv.lock's pins — strictly weaker for a uv-first tree). Reasoning: the README may promise only what runs (moho's walk tests exactly this); the clone cures the census's biggest gap (0 commands); the path form IS "some sort of uv tool install" today — R2's leaning honored, refined, never mandated.

**THE README'S WHOLE SHAPE:** the Quickstart per moho (install + a first comparison, under ten lines) → Install (requirements: Python 3.13+, uv; the honest fresh-clone sequence per keisan; the CLI-anywhere lane; the NOT-promised line — no PyPI presence) → Usage tier-by-tier (the CLI's five ops register/next/vote/state/tally with launch lines + examples; the web lifecycle start/status/stop/restart with PORT/HOST; the service's six routes with the uvicorn launch; the MCP's two forms — stdio per session, --serve with the port-8000 collision named: one at a time, or make PORT=) → the discipline block (the repo-root CWD law — the store and templates mint where you stand; the hooksPath pointer never clones; .prioritree/ mints at runtime) → the honest no-PyPI line. The corrections ride the rewrite whole: six deps, six routes, the five tiers, the 197-test floor.

**THE HYGIENE CURES' CLASSES (the five, suisen's rulings carried):**
- **(i) .opencode paths — OPERATIONAL NOTE:** hikari-side regeneration only (cycle-generated, never hand-edited — the standing law); out of this tree's hands — named for the brief's sibling-action list.
- **(ii) .plans — RULED LIVE SCRUB, the collaborator's hand VIA TOOLING:** paths → relative forms, the gitea/LAN line removed; append-only honored — one ruled commit, NEVER a history rewrite (the commit hashes the records cite must keep resolving). Excision declined: it breaks the README's measured citation at a fresh clone.
- **(iii) CONTINUATION.md:11 — IN-TREE REWRITE** (the absolute root → "this repo"; jikko's hand, R8's file-unit).
- **(iv) copyright/LICENSE — THE COLLABORATOR'S CALL**, options named: (A) a LICENSE file + pyproject license + authors fields (publishable, the claim paired); (B) all-rights-reserved alone (private truth, publish off). **RECOMMENDED: (A), BEFORE any publish.**
- **(v) family-name comments — KEEP:** internal names, no paths, no personal data; rewriting them alone is theater; the real exposure is (i)+(ii). Escalation: if the family names are sensitive, the cure is (i)+(ii), never these two lines.

## 3. THE CURE SET PINNED (the units the findings earn)

Three units, one file per dispatch (R8's file-unit law), each landing per its approved spec (the exact-task law), kensho's independent verification per build gate, one commit per increment:

1. **readme-docs — the rewrite whole:** the Quickstart (moho fix 1); the corrections (deps 2→6, routes 5→6, the five tiers, the 197-test floor); the tier-by-tier usage with launch lines + input/output examples (moho fixes 2+3); the discipline block (the CWD law, the hooksPath pointer + ruff-pending truth, .prioritree/ at runtime); the honest no-PyPI line. Plus CONTINUATION's refresh (the MCP era current; httpx2 main-table; twelve wrappers; 654) and AGENTS.md's regen-line truth (the hikari-side engine named or the line made honest — the same class in the hook's header). **FENCE:** README.md + CONTINUATION.md + AGENTS.md, per-file dispatches — the world's door only; no code touched. **GATE:** G-README-DOCS-BRIEF green before dispatch; the build gate = kensho's verification per file + every correction checkable against this brief's §1.
2. **hygiene — the ruled surfaces only:** CONTINUATION:11 (in-tree); the .plans scrub's ruled form (via tooling, append-only honored, the gitea/LAN line removed, paths → relative); the LICENSE file + pyproject license + authors fields per the collaborator's ruling (recommended (A)). **FENCE:** the ruled surfaces only — shindan's fence stands; the false-positive map is noise, not work; no blanket rewrite; .opencode named for the hikari-side sibling action, out of this unit's hands. **GATE:** G-HYGIENE-BRIEF green before dispatch; the build gate = the marker greps return clean on the cured surfaces + the records' citations still resolve (the README's measured citation intact).
3. **install-deliverable — the CLI-anywhere lane landed:** the `uv tool install .` documentation + any packaging ruling the collaborator makes (the wheel's web-absence MUST-DECIDE: ship web/ in packages, or the CLI-only truth named). **FENCE:** the install story's documented forms run as written — nothing promised that does not run. **GATE:** G-INSTALL-DELIVERABLE-BRIEF green before dispatch; the build gate = kensho's verification + **MOHO'S RE-WALK** (the post-cure README walk, R4's precedent — the cold user's path tested against the landed README, at this gate).

**The open questions named for the collaborator:** (1) the LICENSE choice — (A) or (B), recommended (A) before any publish; (2) the wheel's web-absence — ship web/ or the CLI-only truth; (3) the .plans scrub's exact tooling form (the collaborator's hand via tooling); (4) the PyPI deferral's trigger (the preconditions named: LICENSE, CI, packaging — no date). Each unit's brief cites this gate; their dispatches fire only after it is green.

## 4. THE ACCEPTANCE MAPPING — G-REVIEW-BRIEF's three conditions answered

1. **THE REVIEW BRIEF LANDED:** this synthesis over the four census legs (doc-surface, hygiene, consistency, commands) + the design lane (install-story, adversarial, the blind walk). Divergence check: none survive reconciliation — hyoka's attack held every load-bearing finding; the missed surfaces add, never overturn; the census meets the bar. This report IS the landed brief.
2. **The findings whole + the recommendation + the cure set pinned:** §1 the findings whole (the consistency breaks, the hygiene map with the remediation classes RULED, the commands' honesty 12/3/1, hyoka's rank, moho's fixes); §2 the recommendation carried in R2's ruling form (the hybrid story, the README's shape, the hygiene classes); §3 the cure set pinned (three units, fences + gates named, the open questions named).
3. **THE COLLABORATOR'S APPROVAL — the gate's own act:** the findings judged, the recommendation ruled (the deliverable's form chosen), the cure units' briefs cite this gate; their dispatches fire only after it is green.

— togo, the synthesis leg, read-only by design; this report is the one write.
