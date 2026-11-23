<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/hygienespec

**Route:** prioritree-review (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T01:24:22Z |
| 2 | report | togo | 2026-11-23T01:27:08Z |
## Reported by togo — 2026-11-23T01:27:08Z

# THE HYGIENE EXACT-TASK SPEC — togo (prioritree-review, G-HYGIENESPEC-BRIEF, 2026-11-22)

Ground consumed (the read-back): the approved unit brief (reports/synthesize/hygiene.md — the fence, §2's mechanisms, §4's four opens) + pyproject.toml:1-7 at HEAD (the [project] table: name/version/description/readme/requires-python/dependencies — no license field, no authors field; no LICENSE at the root, glob-verified) + CONTINUATION.md:9-13 at HEAD (:11 the file's ONLY /Users/ hit, grep-verified) + the pairing form at src/prioritree/session.py:1 (`# Copyright (C) 2026 Mark Losey. All rights reserved.` — the 33-line census re-verified: 15 src + 18 tests; "Mark A Losey" at exactly src/prioritree/__init__.py:1, tests/__init__.py:1, tests/test_smoke.py:1) + Q-repo-review ruling 4 (junro.json:444 — the four calls: LICENSE MIT; wheel web+mcp the sibling unit; scrub deferred; pypi deferred) + G-HYGIENE's three conditions (junro.json:468) + G-HYGIENESPEC-BRIEF's three (junro.json:452). The spec decides nothing; the collaborator rules at the gate.

## SS1. THE LICENSE WHOLE — the new file at the repo root, byte-exact

The standard MIT template verbatim (the canonical opensource.org/MIT text — the license text is standard, its provenance the template itself). The complete file, fenced as its exact bytes: 7 lines, pure ASCII, LF endings, one trailing newline — `wc -l` = 7, `wc -c` = 1055:

```
Copyright (c) 2026 Mark Losey

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

The copyright line `Copyright (c) 2026 Mark Losey`: the template's own lowercase "(c)" (the headers' "(C)" is the file-comment form; the LICENSE carries the template's), year 2026 per every header, holder per the dominant src-header form (30 of 33 lines "Mark Losey"; the three "Mark A Losey" files stand unwritten — same holder, grant unambiguous). Nothing else: no title line, no added notice — the three paragraphs whole (permission notice, inclusion condition, "AS IS" warranty disclaimer).

## SS2. PYPROJECT'S REGIONS — the two-line insert in [project]

BEFORE (HEAD, pyproject.toml:1-9):
```toml
[project]
name = "prioritree"
version = "0.1.0"
description = "Priori-tree is a generalized prioritization system: for any list and comparison operator, run the pairwise permutations, store the votes, tally — the output list is in a superior order than sizing individual items, because discernment between two items is easy (for humans and LLMs) while absolute sizing is not."
readme = "README.md"
requires-python = ">=3.13"
dependencies = ["fastapi", "httpx2", "jinja2", "ouncemcp", "python-multipart", "uvicorn[standard]"]

[build-system]
```

AFTER (the insert at :7-:8; the file grows 164 → 166 lines, every old line ≥7 shifts +2, nothing else moves):
```toml
[project]
name = "prioritree"
version = "0.1.0"
description = "Priori-tree is a generalized prioritization system: for any list and comparison operator, run the pairwise permutations, store the votes, tally — the output list is in a superior order than sizing individual items, because discernment between two items is easy (for humans and LLMs) while absolute sizing is not."
readme = "README.md"
requires-python = ">=3.13"
license = "MIT"
authors = [{ name = "Mark Losey" }]
dependencies = ["fastapi", "httpx2", "jinja2", "ouncemcp", "python-multipart", "uvicorn[standard]"]

[build-system]
```

`license = "MIT"` at :7 — PEP 639's declarative SPDX-expression form (hatchling serves it; the root LICENSE + the expression the standard pair, no license-file pointer needed). `authors = [{ name = "Mark Losey" }]` at :8 — the PEP 621 table form, EMAIL-LESS (the census: no personal email anywhere tracked). The classifier `License :: OSI Approved :: MIT License` OMITTED per the brief §2b's ruling (legacy metadata beside the machine-readable SPDX truth; a later publish may add it additively). uv.lock untouched (the lock carries deps + requires-python, never license/authors metadata).

## SS3. CONTINUATION:11'S HUNK — the one phrase cured

The substitution inside line 11 (the harness bullet), the line's harness record whole otherwise:
- BEFORE: `HIKARI-SIDE: the third TargetSpec (root /Users/marklosey/projects/prioritree; the prioritree-seats.yaml adapter`
- AFTER: `HIKARI-SIDE: the third TargetSpec (root this repo; the prioritree-seats.yaml adapter`

The contiguous byte range: `root /Users/marklosey/projects/prioritree;` (42 bytes) → `root this repo;` (15 bytes) — line 11 shrinks by 27 bytes; no other byte of :11 moves; the neighborhood intact (:10 the foundations bullet, :12 the tool-grants bullet, :13 the Store bullet); the file stays 76 lines. The meaning preserved: the record's claim stays true (the TargetSpec's root IS this repo's own root); the machine-specific path leaves the tracked surface.

## SS4. THE NO-BREAK PROOFS

1. THE FLOOR UNTOUCHED-GREEN: the three cures touch ZERO Python bytes (a new file, two TOML metadata lines, one Markdown phrase) — pyright 0 errors/0 warnings/0 informations, ruff zero findings, the suite green (197 passed — the last live run stands).
2. THE MARKER GREPS' POST-BUILD EXPECTATIONS (G-HYGIENE condition 2): `grep -n /Users/ CONTINUATION.md` → ZERO hits (:11's single hit cured, the file's only one); the LICENSE at the repo root (1055 bytes, the standard form); `grep -n '^license' pyproject.toml` → `7:license = "MIT"`; `grep -n '^authors' pyproject.toml` → `8:authors = [{ name = "Mark Losey" }]`.
3. THE 33 COPYRIGHT LINES UNTOUCHED: 15 src + 18 test files, every line 1 `# Copyright (C) 2026 … All rights reserved.` — zero edits; the LICENSE PAIRS them (the pairing, never the rewrite — shindan's fence).
4. THE SHRUNK SCOPE HONORED: three files, no more — the .plans records untouched (scrub deferred per ruling 4's call 3), the family-name comments kept (service.py:250 + tests/__init__.py:2), the .opencode paths out of this tree's hands, the 33 headers standing.

## SS5. THE THREE-STEP PLAN (R8 — one file per dispatch)

- STEP 1 — build/hygiene-license (jikko): create the root LICENSE with SS1's exact bytes (patch, the one mutation verb — the file add whole). Verify: `wc -c` 1055, `wc -l` 7, the fence read back byte-exact. The report op completes the step (R6/R11); one commit at the landing.
- STEP 2 — build/hygiene-pyproject (jikko): SS2's two-line insert. Verify: the two field greps at :7/:8; the 166-line file; the lock untouched. Report op; one commit.
- STEP 3 — build/hygiene-continuation (jikko): SS3's phrase cure. Verify: the /Users/ grep → zero hits; the line read back whole. Report op; one commit.
- THE GATE: the floor run to prove it untouched-green (make test / lint / typecheck) + KENSHO'S validate/hygiene — his independent hand: the marker greps + the three floor instruments re-run + the landed bytes against these fences (G-HYGIENE condition 3). This spec closes G-HYGIENESPEC-BRIEF at the collaborator's approval — the build fires only after.

The trade-off the plan carries (the brief's, unchanged): the pairing is the cure — 33 "All rights reserved" lines now stand one file away from the grant that answers them; the readme-docs unit's README should name the LICENSE (the sibling dependency named, never re-ruled here); the scrub deferral stands honest — the .plans records' 100+ private paths remain tracked at this unit's close.
