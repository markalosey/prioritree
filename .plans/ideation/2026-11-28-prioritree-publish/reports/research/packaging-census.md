<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — research/packaging-census

**Route:** prioritree-publish (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-28T17:10:34Z |
| 2 | report | tansa | 2026-11-28T17:13:23Z |
## Reported by tansa — 2026-11-28T17:13:23Z

TANSA'S PACKAGING CENSUS — research/packaging-census (prioritree-publish), the research stage's first ungated leg. The premise law held throughout: every finding below is the bytes, line-pinned, nothing assumed.

THE GROUND (read whole): the store's heart (.plans/ideation/2026-11-28-prioritree-publish/.junro/junro.json, 318 lines) — Q-publish open with BOTH rulings on the record: THE CONVENING (the ruled act never silent; the free-tier law extended; the premise law turned on the publish itself; the verification from the index) and THE ACCOUNT + PROVENANCE RULING (the package under the collaborator's own PyPI account; the author fields carry the collaborator; the project URLs carry the repository; the README the record's public story; the verification deepened to the published page read cold as the collaborator's own). The account+provenance amendment and the context note (kepric's best-practice research, the channel open) also read.

(1) THE PYPROJECT'S ACTUAL PACKAGING FIELDS — /Users/marklosey/projects/prioritree/pyproject.toml (263 lines, read whole):
- name = "prioritree" (line 2) — PRESENT.
- version = "0.1.0" (line 3) — PRESENT, STATIC: no `dynamic` key anywhere in the [project] table; no __version__ symbol in any .py (grep tree-wide: zero matches). The pyproject's line 3 is the version's sole source of truth today.
- description (line 4) — PRESENT: the one-sentence claim ("Priori-tree is a generalized prioritization system: for any list and comparison operator, run the pairwise permutations, store the votes, tally — ...").
- readme = "README.md" (line 5) — PRESENT; the file exists at the root (346 lines).
- requires-python = ">=3.13" (line 6) — PRESENT.
- license = "MIT" (line 7) — PRESENT, the SPDX string form (not a file-table).
- authors = [{ name = "Mark Losey" }] (line 8) — PRESENT: name only, NO email.
- dependencies (line 9) — PRESENT, seven, all unpinned: fastapi, httpx2, itsdangerous, jinja2, ouncemcp, python-multipart, uvicorn[standard].
- urls — ABSENT: no [project.urls] table anywhere (no Homepage/Repository/Bugs).
- classifiers — ABSENT: no key.
- keywords — ABSENT.
- [project.scripts] (lines 15-16) — PRESENT: prioritree = "prioritree.cli:command".
- [build-system] (lines 11-13) — hatchling: requires = ["hatchling"], build-backend = "hatchling.build".
- [dependency-groups] dev = ["pytest", "pyright", "ruff"] (lines 262-263).
- BEYOND THE PYPROJECT: setup.py, setup.cfg, MANIFEST.in, hatch.toml — ALL ABSENT (glob ** across the tree: zero matches). The backend's own config rides the pyproject's [tool.hatch.*] sections alone; no other packaging surface exists.

(2) THE ARTIFACT'S REALITY — the build config's bytes (not the cure's memory):
- [tool.hatch.build.targets.wheel] packages = ["src/prioritree"] (lines 18-19): the wheel carries the package whole — 19 .py modules at src/prioritree (acceptance, budget_curve, cli, key_store, key_verify, mcp_auth, mcp_server, policy, registry, run_store, scheduler, service, service_store, session, store_lock, tally, votes, web, + __init__). THE MCP SERVER RIDES BY CONSTRUCTION: mcp_server.py among the nineteen modules the packages directive carries (the pyproject's own ruling comment, lines 21-28).
- [tool.hatch.build.targets.wheel.force-include] (lines 29-31): "web/templates" = "prioritree/templates", "web/static" = "prioritree/static" — THE PACKAGING CURE AT THE BYTES, flat dests (no prioritree/web/ directory shadowing web.py). The mapped sources verified present: web/templates = 17 files (ack, auth, base, done, fold, halt, landing, pair, pairs, picker, progress, refuse, result, sitting, state-strip, unknown, vote-ack .html), web/static = 2 files (app.css, app.js) — 19 web assets shipping as package data.
- THE SDIST: NO [tool.hatch.build.targets.sdist] section — the sdist's contents are NOT configured at the bytes; hatchling's defaults govern (the defaults' exact behavior is rikai's landscape question, not this census's claim).
- THE ENTRY POINTS: [project.scripts] prioritree = "prioritree.cli:command" — the CLI console script PRESENT; no other entry points (no gui-scripts, no plugin tables).

(3) THE CI WORKFLOW'S PUBLISH-READINESS — .github/workflows/ holds ONE file: ci.yml (43 lines, read whole):
- Triggers: push to branches [main] (lines 4-5) + schedule cron '0 3 * * 1' (weekly Monday 03:00, lines 6-7). NO tag triggers, NO release triggers, NO workflow_dispatch.
- permissions: contents: read (lines 13-14) — NO id-token: write anywhere: the trusted-publishing permission ABSENT.
- job "floor" (lines 17-29): ubuntu-latest; actions/checkout@v6; astral-sh/setup-uv@v10.3.3 (enable-cache: auto); make lint (ruff zero-findings); make test (step named "test — pytest, the 203-suite" — a byte-level divergence named, never averaged: the workflow's step name carries "the 203-suite" while README:342 carries "490 tests green"; the census reports both forms as they stand); make typecheck (pyright 0/0/0).
- job "codeql" (lines 31-43): ubuntu-latest; contents: read + security-events: write; github/codeql-action/init@v4 (languages: python, build-mode: none, config-file: ./.github/codeql/codeql-config.yml) + analyze@v4.
- PYTHON VERSIONS: no matrix — the floor rides uv; .python-version at the root = "3.13" (the file's whole content).
- THE PUBLISH JOB: ABSENT — the expected absence confirmed at the bytes: no build job, no pypa/gh-action-pypi-publish, no twine, no PyPI credential or trusted-publisher reference anywhere. The channel unit's ground is open field.
- THE TAG FORMS THE WORKFLOW KNOWS: NONE — the on: grammar is push-to-main + cron only; no tag/release form exists to know.
- THE REPO'S TAGS TODAY: NONE — .git/refs/tags is empty (0 entries) and .git/packed-refs carries only refs/remotes/origin/main (c4db0f9): no release tag has ever been minted.

(4) THE AUTHORSHIP FIELDS TODAY — the provenance ruling's ground:
- pyproject authors: [{ name = "Mark Losey" }] (line 8) — the collaborator PRESENT as author, no email: the ruling's "author fields carry the collaborator" half-met at the bytes; the email's form the design rules.
- LICENSE (9 lines, whole): "MIT License" / "Copyright (c) 2026 Mark Losey" (line 3) — year 2026, holder Mark Losey.
- README's provenance claims: the author named at two surfaces — line 13 (License: MIT ... Copyright (c) 2026 Mark Losey) and line 346 (the License section, same + "pyproject.toml carries license = \"MIT\""); the repository's URL told in the clone commands — git clone git@github.com:markalosey/prioritree.git (lines 22, 325), the SSH form; HUMAN.md cited at line 15 ("the only human-written thing in this repository; everything else is generated") — the self-evolving record's own story told; the collaborator's Q-purpose ruling quoted verbatim at lines 9-11.
- THE INSTALL STORY'S CLAIMS (the index-verification surface): line 336 — "uv tool install ." the tool lane (the console script + seven dependencies; the wheel ships the templates/static as package data; the web and the MCP ride the same install); line 338 — "**Not on PyPI.** uv tool install prioritree and pip install prioritree do not resolve — Priori-tree is not published. The publish is deferred..." — the README's own honest gap, TRUE today and FALSE the moment the publish lands: the install story MUST be re-authored at the build (the honest-docs law priced).
- THE GIT IDENTITY: .git/config (14 lines, read whole) carries NO [user] section — no local user.name/user.email; the identity falls to the global config, which sits OUTSIDE this seat's permitted read surface (the read refused at the external-directory permission — the refusal named, the local bytes reported as they stand). The local bytes carry: remote origin url = git@github.com:markalosey/prioritree.git (line 10); branch main tracks origin/main; hooksPath = .githooks (line 8). The collaborator's name-forms at the tree's own surfaces: "Mark Losey" (authors/LICENSE/README) and "markalosey" (the GitHub handle at the remote and the clone commands).

(5) THE HONEST TABLE — every packaging field, the premise law at every row:
| field | today (the bytes) | the publish's need |
|---|---|---|
| name | "prioritree" (pyproject:2) | the PyPI claim itself; the name's availability + squat window are the channel's questions |
| version | "0.1.0" STATIC (pyproject:3; no dynamic, no __version__) | the first release's number + source of truth — the design's ruling; the immutable version's law priced |
| description | present (pyproject:4) | the index Summary — carried |
| readme | "README.md" (pyproject:5) | the index's served page; its "Not on PyPI" claim (README:338) must flip at the build |
| requires-python | ">=3.13" (pyproject:6) | carried |
| license | "MIT" SPDX string (pyproject:7) | carried; the LICENSE file's shipping form the design confirms |
| authors | [{ name = "Mark Losey" }], NO email (pyproject:8) | the provenance ruling's carrier — the email's form the design rules |
| urls | ABSENT | the ruling requires the repository carried — Home/Repository/Issues the build mints |
| classifiers | ABSENT | the identity told at the metadata — the set the design rules |
| keywords | ABSENT | optional — the design rules |
| dependencies | 7, all unpinned (pyproject:9) | the pinning question the design rules |
| scripts | prioritree = "prioritree.cli:command" (pyproject:15-16) | carried — the CLI's door |
| build-system | hatchling (pyproject:11-13) | carried |
| wheel contents | src/prioritree (19 modules) + force-include web/templates->prioritree/templates (17 files) + web/static->prioritree/static (2 files) (pyproject:18-31) | the packaging cure VERIFIED at the bytes — carried |
| sdist config | ABSENT (no targets.sdist section) | the artifact unit's question — configure or accept the backend's defaults |
| CI publish job | ABSENT (ci.yml: push-to-main + cron only; no tags, no id-token) | the channel unit's whole ground — the trusted-publishing form or the manual publish |
| git tags | NONE (refs empty; packed-refs: main only) | the release unit's ground — the first tag's form unclaimed |
| git identity | no local [user] (.git/config whole); global fallback outside this seat's read surface | the collaborator's account carries the publish per the ruling; the exact identity forms confirmed at the collaborator's hands |

CENSUS PROVENANCE (the reads, all this turn, read-only): pyproject.toml (263 lines, whole); .github/workflows/ (dir: one file) + ci.yml (43 lines, whole); LICENSE (9 lines, whole); README.md (346 lines — header, install/status/license sections read; provenance grep across the whole file); src/prioritree (20 entries); web/templates (17) + web/static (2); .git/config (14 lines, whole); .git/refs/tags (empty) + .git/packed-refs (main only); .python-version ("3.13"); the store's heart .junro/junro.json (318 lines, whole). Absences verified: setup.py/setup.cfg/MANIFEST.in/hatch.toml — zero glob matches tree-wide; __version__ — zero grep matches in .py. One surface refused: the global git config (external-directory permission) — named above, never silently dropped. No file touched; no store record written but this report.
