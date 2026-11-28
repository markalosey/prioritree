<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — research/cold-install-walk

**Route:** prioritree-publish (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-28T17:10:34Z |
| 2 | report | moho | 2026-11-28T17:16:41Z |
## Reported by moho — 2026-11-28T17:16:41Z

# THE COLD INSTALL WALK — research/cold-install-walk (moho, prioritree-publish, 2026-11-28)

The blind walk's answer: **what breaks when nobody helps** — the stranger's install lived at the walk's own hands, every finding at the bytes, every boundary named, nothing papered.

## 0. THE WALK'S OWN HANDS (the unaided condition, named first)

The moho seat carries NO SHELL — the pack routes read/glob/grep/calculate/test/junro/prioritree/friction, no subprocess surface — and the harness's permission wall refuses reads outside the tree (the probe of /Users/marklosey/Library/Caches/pip, the host's index memory, came back REFUSED: the external_directory rule). So every told path that needs a shell — pip install, uv build, uv tool install, make dev, the fresh venv at tmp — is UNLIVABLE at these hands. The walk lived what its hands allow: the bytes read whole, the tree's own venv's installed form, the artifact home, the tree's test surface. The tree's own .prioritree store was NEVER touched (no read, no write — only its name at the root listing).

## 1. THE TOLD STORY READ (README.md whole — the Install section at the bytes, README:320-338)

Three told paths:

(a) THE CLONE LANE (README:322-334): `git clone git@github.com:markalosey/prioritree.git` → `cd prioritree` → `make dev` → `make test` → `make lint` → `make typecheck` → `git config core.hooksPath .githooks` → `make start` → `open http://127.0.0.1:8000/` — "Requirements: Python 3.13+ and uv" (README:322). The Makefile read whole: dev = `uv sync`, test = `uv run pytest`, lint = `uv run ruff check src/ tests/`, typecheck = `uv run pyright` (Makefile:12-22). NO build target exists in the Makefile (13 targets, none builds) — the build verb is uv's own (`uv build`), never the tree's.

(b) THE TOOL LANE (README:336): "`uv tool install .` — the tool lane. Installs the `prioritree` console script and its seven dependencies — the five CLI ops run from any directory... The web tier rides this lane too: the wheel ships the templates and static files as package data, and the web homes resolve them from the installed package." The serve forms: `$(uv tool dir)/prioritree/bin/uvicorn prioritree.service:app`; the MCP: `$(uv tool dir)/prioritree/bin/python -m prioritree.mcp_server` (+ `--serve`, port 8100).

(c) THE INDEX LANE — TOLD ABSENT (README:338, verbatim): "**Not on PyPI.** `uv tool install prioritree` and `pip install prioritree` do not resolve — Priori-tree is not published. The publish is deferred: the license, the packaging, and CI have landed; the publish itself remains the outward lane's ruled act."

THE TOLD STORY IS HONEST: the README never tells a stranger `pip install prioritree` as a path — it names that command only to say it does not resolve. No install-story lie at today's bytes. The stranger is told: clone, or local tool-install.

## 2. THE TOLD PATHS LIVED, AS FAR AS THE HANDS ALLOW

(a) `pip install prioritree` at a fresh venv — NOT LIVABLE at these hands: no shell to mint a venv, no network surface to reach the index, the outside-tree wall refusing even the host's pip cache. The index's live answer (absent? squatter?) could not be HEARD at the walk's hands. The index's absence stands on the tree's own claim alone (README:338) + the store's ground (the publish convenes BECAUSE the package is unpublished — the heart's convening ruling). A stranger who followed the README today would not try the index: they are told it does not resolve. The squat question belongs to legs with sources (rikai's landscape, shindan's risk), not these hands.

(b) THE CLONE FORM'S FIRST STUMBLE, at the bytes: the told clone is the SSH form — `git clone git@github.com:markalosey/prioritree.git` (README:22, 325). The COLD stranger without a GitHub SSH key is refused at the first told command; the public https form is never told. The told story's first byte assumes the keyed insider, not the stranger. (Unlivable at these hands too — the stumble named at the bytes.)

(c) `uv tool install .` — unlivable at these hands (no shell). Its told claims lived at the tree's own venv instead (§3c) — the editable form, the same pyproject the source.

## 3. THE LOCAL INSTALL LIVED (the artifact's reality at the walk's hands)

(a) THE ARTIFACT HOME: dist/ EXISTS and carries BOTH artifacts — `prioritree-0.1.0-py3-none-any.whl` + `prioritree-0.1.0.tar.gz` (read at the directory; the glob tool is gitignore-filtered and returns nothing for dist/ — the read tool carries the truth). The artifacts are LOCAL and UNTRACKED: .gitignore:14 ignores dist/, dist/.gitignore = `*` — a fresh clone carries NO dist/. The walk did NOT build them (no shell); they stood at the walk's arrival — a prior hands' build (which hands, the walk cannot know: no mtimes at these hands). The version at the artifact names: 0.1.0 (pyproject:3 the source).

(b) THE WHEEL'S INTERIOR — DARK at these hands: the read tool refuses binary ("Cannot read binary file: .../prioritree-0.1.0-py3-none-any.whl" — the verbatim refusal); no shell to unzip or install. The cure's carried form could not be verified at the WHEEL's own bytes. What the walk found at the bytes it can read:
- THE PROMISE: pyproject.toml:29-31 — [tool.hatch.build.targets.wheel.force-include]: "web/templates" = "prioritree/templates", "web/static" = "prioritree/static" (the file's own comment: "the wheel SHIPS the web tier's authored homes as package data", install-brief §2, G-INSTALL-BRIEF 2026-11-22).
- THE SOURCES EXIST: web/templates = 17 files, web/static = 2 files (app.css, app.js) — matching README:56's "17 authored Jinja2 templates + 2 static files".
- THE CARRIED FORM MATERIALIZED AT THE INSTALLED LOCATION: .venv/lib/python3.13/site-packages/prioritree/ carries templates/ (all 17, the names read) + static/ (app.css, app.js) — the force-include mapping LIVED at the installed form; the loader seam's fallback copies stand.
- THE MODULES: src/prioritree = 19 .py files (globbed) — the library whole.
- THE GENERATOR: the dist-info's WHEEL file: "Generator: hatchling 1.33.0", "Tag: py3-none-any" — matching the wheel's filename tag.

(c) THE INSTALLED FORM LIVED (the tree's venv — the editable install; direct_url.json verbatim: {"url":"file:///Users/marklosey/projects/prioritree","dir_info":{"editable":true}}):
- THE ENTRY POINT PRESENT: .venv/bin/prioritree (read at the bin listing) + entry_points.txt verbatim: "[console_scripts] prioritree = prioritree.cli:command" (pyproject:16 the source).
- THE CLI GREEN AT THE INSTALLED FORM — THE WALK'S LIVE ACT: tests/test_harness.py run through the tree's test_runner — **"6 passed in 1.84s"** (verbatim). The harness drives the REAL console script (test_harness.py:27: the shim = the interpreter's sibling "prioritree") via fixed-argv subprocess: the ten-invocation success arc (register → next → 6 votes → next → tally, every stdout byte asserted), the determinism replay (two fresh homes, byte-identical), the refusal arcs R1-R3 (rc 1, "refused —" on stderr), argparse's channel R4 (rc 2). EVERY invocation carries --home pinned to the tmp home (the argv composed at test_harness.py:71-94) — the tree's .prioritree store untouched by the run, the discipline read at the bytes BEFORE the run.
- THE DIFFERENCE NAMED: the venv's form is the EDITABLE install (the clone lane's), not a fresh venv with the wheel — the wheel-at-a-fresh-venv story remains UNLIVED at these hands. The CLI's green at the installed form is lived at the editable form; the wheel's install story belongs to the publish's verification (the ruling's law: FROM THE INDEX, at hands that can install).

## 4. THE PROVENANCE'S COLD READ (the metadata at the installed form)

METADATA at .venv/lib/python3.13/site-packages/prioritree-0.1.0.dist-info/METADATA, head verbatim: Metadata-Version: 2.5 | Name: prioritree | Version: 0.1.0 | Summary: "Priori-tree is a generalized prioritization system: for any list and comparison operator, run the pairwise permutations, store the votes, tally — the output list is in a superior order than sizing individual items, because discernment between two items is easy (for humans and LLMs) while absolute sizing is not." | Author: Mark Losey | License-Expression: MIT | License-File: LICENSE | Requires-Python: >=3.13 | Requires-Dist: fastapi, httpx2, itsdangerous, jinja2, ouncemcp, python-multipart, uvicorn[standard] | Description-Content-Type: text/markdown — then the FULL README rides as the long description (the index page's served body; the ruling's README limb MET at the bytes).

WHAT A STRANGER WOULD LEARN at today's artifact:
- WHO: **Author: Mark Losey** — the collaborator IS named; the tool does NOT arrive nameless (the packet's premise "the author fields absent today?" answered NO at the bytes). NO email rides (pyproject:8: `authors = [{ name = "Mark Losey" }]` — name only).
- WHERE: **NO Project-URL fields anywhere** — no homepage, no repository, no issues (pyproject carries NO [project.urls] table at all). The provenance ruling's URL limb ("the project URLs carry the repository") is UNMET at today's bytes: the stranger learns WHO, never WHERE.
- NO classifiers, NO keywords ride the metadata (read whole — absent). The ruling's classifier/Description limbs: unruled today, absent at the bytes.
- The identity's tiny drift: the code's copyright line says "Mark A Losey" (src/prioritree/__init__.py:1) while the metadata says "Mark Losey" — the middle initial rides the code, not the artifact's identity.
- **THE STALE BODY (unexpected finding)**: the README embedded in the venv's metadata is an OLDER generation — it says "web.py (1256 lines, ...)" and "The quality floor: 480 tests green" (METADATA:73, 78) where the tree's current README says "1341 lines" (README:56) and "490 tests green" (README:61). The editable install's metadata was baked at the earlier floor and never re-baked (editable installs do not refresh on source change). A fresh build at today's tree would carry the current README — the artifact's served story is baked AT THE BUILD.

## 5. THE FINDINGS (every stumble named — the publish map's lived ground)

1. **THE STORY THAT FLIPS AT THE PUBLISH**: README:338's "**Not on PyPI.** ... `pip install prioritree` do not resolve" is TRUE today and FALSE the moment the publish lands. The index serves the README as the long description — published as-is, the index page would tell every stranger that the package they are installing does not exist. The paragraph's re-rule must ride the publish's own act — a named unit for the map.
2. **THE SSH-ONLY TOLD CLONE**: `git@github.com:markalosey/prioritree.git` (README:22, 325) — the cold stranger without a GitHub key is refused at the first told command; the https form is never told. The told story assumes the keyed insider.
3. **THE INDEX UNREACHABLE AT THE WALK'S HANDS**: no shell, no network, the outside-tree wall — the index's live answer unheard here; the absence stands on the tree's own claim + the effort's ground. The squat question: legs with sources.
4. **THE WHEEL STANDS BUT IS DARK AT THESE HANDS**: both artifacts exist at dist/ (0.1.0); the interior unverifiable without a shell. The cure is PROMISED (pyproject:29-31), SOURCED (web/: 17+2 files), MATERIALIZED at the editable form's installed location (site-packages/prioritree/{templates,static} — 17+2 read) — the WHEEL's own interior remains the publish's verification.
5. **THE METADATA'S PROVENANCE GAP**: Author present (no email), Project-URLs ABSENT, classifiers ABSENT, keywords ABSENT — the identity carries WHO, never WHERE. The account/provenance ruling's URL limb unmet at today's bytes — named for the metadata unit.
6. **THE STALE SERVED STORY** at the venv's metadata (480/1256 vs the tree's 490/1341) — the build bakes the README at build time; the publish must build at the current truth, and the README's own flip (finding 1) must land BEFORE the build that bakes it.
7. **THE ARTIFACTS ARE UNTRACKED**: dist/ gitignored — a fresh clone's dist/ is empty; the publish's artifact must be BUILT at the publish's moment (the immutable version's law's ground — the standing artifacts are a prior hands', unattributable at these hands).
8. **THE TOOL ITSELF IS GREEN**: the walk's one live act — 6/6 harness tests green in 1.84s at the installed form: the entry point, the five ops, the persistence seam, the refusals, the DONE channel. The gap is NOT the tool: it is the CHANNEL (nothing at the index) and the METADATA (no WHERE) — the publish's map written in exactly these gaps.

## THE WALK'S ONE-LINE TRUTH

The tool installs green and arrives NAMED (Author: Mark Losey) — what breaks when nobody helps is the stranger's ROAD to it: no index presence (told honestly, lived as absence), an SSH-only told clone, a wheel dark to unaided hands, and a metadata that names WHO but never WHERE.
