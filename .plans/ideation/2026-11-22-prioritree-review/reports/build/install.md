<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — build/install

**Route:** prioritree-review (executing) | **Events:** 20 | **Reports:** 9

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T02:29:02Z |
| 2 | dispatch | shinko | 2026-11-23T02:29:08Z |
| 3 | report | jikko | 2026-11-23T02:30:02Z |
| 4 | report | jikko | 2026-11-23T02:42:45Z |
| 5 | dispatch | shinko | 2026-11-23T02:43:01Z |
| 6 | dispatch | shinko | 2026-11-23T02:43:08Z |
| 7 | report | jikko | 2026-11-23T02:45:34Z |
| 8 | report | jikko | 2026-11-23T02:47:36Z |
| 9 | dispatch | shinko | 2026-11-23T02:50:41Z |
| 10 | report | jikko | 2026-11-23T02:53:36Z |
| 11 | dispatch | shinko | 2026-11-23T02:53:48Z |
| 12 | report | jikko | 2026-11-23T02:54:31Z |
| 13 | dispatch | shinko | 2026-11-23T02:58:46Z |
| 14 | report | jikko | 2026-11-23T03:05:09Z |
| 15 | dispatch | shinko | 2026-11-23T03:06:02Z |
| 16 | report | jikko | 2026-11-23T03:07:16Z |
| 17 | gate | shinko | 2026-11-23T03:22:16Z |
| 18 | result | shinko | 2026-11-23T03:22:28Z |
| 19 | dispatch | shinko | 2026-11-23T03:24:18Z |
| 20 | report | jikko | 2026-11-23T03:24:48Z |
## Reported by jikko — 2026-11-23T02:30:02Z

# Step 1 — pyproject.toml's wheel region (build/install)

§1's fence landed whole: the ruled comment (install-brief §2 + Q-repo-review ruling 4, G-INSTALL-BRIEF approved 2026-11-22) at :21-28, the force-include sub-table at :29-31 — "web/templates" = "prioritree/templates", "web/static" = "prioritree/static" — placed directly under the wheel target, before [tool.ruff]. The packages line (:19) byte-unchanged; read-back verified the region verbatim against the fence. NOTHING else touched — one hunk, one file; uv.lock untouched (no dep change). Read-only beyond the landing and this report; not verified (kensho's instruments pending at the gate).
## Reported by jikko — 2026-11-23T02:42:45Z

Step 2 landed: web.py's loader seam per installspec §2, five hunks, NOTHING else touched.

- _resolve(home, tail) at :126-147 — the CWD branch returns the home byte-verbatim when the directory exists; the fallback str(files(_PACKAGE).joinpath(tail)); the five-field docstring whole; the naming law's first-word form.
- Constants :84-90 — _PACKAGE + _TEMPLATES_TAIL/_STATIC_TAIL inserted after the byte-unchanged homes (_TEMPLATES_HOME/_STATIC_HOME).
- Mounts :157-158 — both rewired to _resolve's results (StaticFiles + Jinja2Templates); check_dir=False STAYS; the child-app comment :150-155 byte-unchanged.
- Imports :50-54 — from importlib.resources import files; from pathlib import Path; the alphabetical order held (isort law).
- Module docstring :23-32 — the resolution clause re-ruled (IN ORDER: the CWD copy FIRST, the shipped package the FALLBACK, the wrong-cwd fold named); the loader/render seam's law :13-17 byte-unchanged.
- LANDED web.py = 692 lines, measured at the read-back (the honest number for README :52 — never predicted).

En route: two patch refusals (hunk-count checksums; then a one-line-off leading anchor) — both refused with nothing landed (the transaction reversed); re-derived, third apply clean.
NOT done (outside this step's fence): the test arcs (step 3), README (step 4), the floor + the gate's live legs (steps 5-6); no instruments run — the coordinator's eyes.
## Reported by jikko — 2026-11-23T02:45:34Z

Step 4 landed: README.md's four re-ruled lines applied per installspec §4's fences — nothing else touched. :159 the CWD law re-ruled: the store alone CWD-relative, the web homes' ordered resolution named (CWD-first, the installed package's copies the fallback; the wrong-cwd fold honest, an installed location always renders). :166 the clone paragraph re-titled "the source and the floor" — the tool lane below named as serving the same pages from the installed package. :180 the web-absence truth cured: the tool lane carries the web tier, both installed serve forms at the spec's exact bytes ($(uv tool dir)/prioritree/bin/uvicorn prioritree.service:app; $(uv tool dir)/prioritree/bin/python -m prioritree.mcp_server [--serve]). :182 the PyPI precondition shrunk: the license and the packaging have landed; CI remains. Read-back: the four lines byte-match the fences; the neighborhoods (## Discipline, ## Install, the clone console block, ## Status) intact. NOT done — the two count lines the spec names beyond the four (:52's web.py line count, :55's floor 197→200): outside this dispatch's letter ("NOTHING else touched"); left for the gate's collaborator ruling. File touched: README.md only.
## Reported by jikko — 2026-11-23T02:47:36Z

tests/test_web_face.py landed per installspec §3 whole: the two docstring re-rules (the CWD-fixture extension named; the resolver-arcs sentence inserted after the static pair), the imports replaced (Path to runtime, the dead TYPE_CHECKING block + its typing import deleted, `from prioritree.web import _resolve` added), the N=3 arcs inserted after test_static_pair_serves — nothing else touched.
The arcs (:72-92): test_resolve_prefers_the_cwd_home (the CWD-present case — the home returned byte-verbatim), test_resolve_falls_back_to_the_package (the installed form — the absolute package path, the tail named), test_resolve_keeps_the_fold_at_a_wrong_cwd (both branches miss, never raises).
The fixture form: monkeypatch.chdir(tmp_path) in all three; the client fixture byte-unchanged; no client on the resolver arcs.
The arc count: the file's total 24 (21+3); the suite's pin 197 → 200.
FINDINGS fixed in the same turn: (a) ruff I001 — the blank line between pytest and fastapi.testclient merged (the isort law held over the fence's blank); (b) ruff ARG001 ×2 — the spec's fence for arc 2 omitted §3(c)'s ruled `monkeypatch.chdir(tmp_path)` body line; without it the arc self-falsifies (at the repo root web/templates exists, so the fallback assertion fails) and both fixtures sit unused — restored 1:1 with arcs 1 and 3. Ruff now zero findings on the file.
NOT FIXED, NAMED — the one remaining finding: pyright strict's reportPrivateUsage fires on the spec's own fenced import (`from prioritree.web import _resolve`, :32:28).
Its cures all live outside this step's one-file fence: a pyright per-file override (a named ruling in pyproject.toml — step 1's file, the tree's ruff per-file-ignores precedent's shape) or a public rename in web.py (step 2's file); a suppression comment is a convenience, barred by the zero-ignore law.
The coordinator rules the cure; the floor (step 5) and kensho will see the finding named here.
## Reported by jikko — 2026-11-23T02:53:36Z

Step 4b landed: the public-resolver rename per R6 (b), togo's micro-fold — the underscore dropped at every cited site, nothing else touched.
- src/prioritree/web.py: def resolve at :126 (the docstring's first line already carried "Resolve..." — the naming law held); both mounts at :157/:158; __all__ grown at :66.
- tests/test_web_face.py: the import at :32 + the three arcs' calls at :76/:82/:91; the ruled test names (test_resolve_...) byte-unchanged.
- ONE DELTA, reported: __all__ landed SORTED — ["resolve", "web_app"], not the ruling's literal ["web_app", "resolve"] — ruff RUF022 fired on the apply; the zero-findings standing law (installspec §5.2's own floor: ruff zero findings, zero new ignores) forced the sorted form; the export contract (the two symbols) is the ruling's content whole.
- The read-back: the symbol \b_resolve\b zero hits over both files (the plain-substring residue in tests is the test names' own "test_resolve_...", the ruled names, not the symbol); resolve present at every cited site.
- pyright strict 0 errors/0 warnings/0 informations — the typecheck act run: the reportPrivateUsage remainder GONE, retired by this fold.
## Reported by jikko — 2026-11-23T02:54:31Z

The floor for packet build/install (prioritree-review, step 5 of 6) — three fixed-argv acts, all within expectation, no edits made.

1. Test act (all): the full suite passed — "200 passed in 27.92s", matching the expected 200 (the 197 plus the 3 new resolver arcs).
2. Lint act (check): "All checks passed!" — zero findings.
3. Typecheck act: "0 errors, 0 warnings, 0 informations" — zero findings.

No findings outside the expectations; nothing to edit; no deltas to report. The disk stands as the coordinator left it.
## Reported by jikko — 2026-11-23T03:05:09Z

Step 6a (the residue landing) landed — README.md's three cures per the fold's fences (installspec's 2026-11-23T02:58:27Z event), nothing else touched:
(1) the count: "197 tests green" → "200 tests green" at BOTH sites (:55 the Runtime-dependencies floor, :187 the Status floor), phrasing otherwise byte-identical.
(2) the Usage/CLI list's new bullet at :71 — the list's FIRST, right after the five-op table (:63-69): the fold names the list but not the intra-list position; first = adjacent to the table it speaks of (the one choice made, reported here).
(3) :17's Quickstart head gained "Requirements: Python 3.13+ and uv." between "from a fresh clone." and "Run every command..." — before the first make command.
Read-back: the three sites verified verbatim post-apply (README.md 190 → 191 lines, the bullet the +1); grep "197" over README.md returns ZERO hits.
Files touched: README.md only (one patch, four hunks — exactly the three cures). Not done: nothing — the fold's three cures are the whole step; no floor run (step 5's lane, not mine).
## Reported by jikko — 2026-11-23T03:07:16Z

Step 6b done. README.md: the HUMAND.md line landed at the intro's end — line 15, its own paragraph, immediately before `## Quickstart` — verbatim per Q-repo-review ruling 5: `[HUMAND.md](HUMAND.md) — the only human-written thing in this repository; everything else is generated.`

Read-back: grep HUMAND over README.md = exactly one hit (line 15). HUMAND.md itself NOT created — the collaborator's own hand, per the ruling. Nothing else touched; one hunk, one file.
## Reported by jikko — 2026-11-23T03:24:48Z

The link cure landed: README.md:15 now reads [HUMAN.md](HUMAN.md) — the only human-written thing in this repository; everything else is generated. Both link text and target cured from HUMAND.md to HUMAN.md; phrasing byte-identical otherwise; line stays at :15, own paragraph before ## Quickstart. Read-back green: "HUMAND" zero hits over README.md; "HUMAN.md" exactly one hit (line 15); HUMAN.md exists at the repo root, so the link resolves. HUMAN.md itself untouched; nothing else touched. One patch refusal en route (hunk count checksum mismatch), fixed in-turn with a context-carrying hunk.
