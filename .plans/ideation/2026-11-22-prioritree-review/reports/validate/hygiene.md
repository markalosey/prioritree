<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — validate/hygiene

**Route:** prioritree-review (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T01:40:06Z |
| 2 | report | kensho | 2026-11-23T01:42:32Z |
## Reported by kensho — 2026-11-23T01:42:32Z

Kensho — validate/hygiene: the hygiene unit independently verified against the approved spec (reports/synthesize/hygienespec.md), zero trust — my own reads, my own greps, my own runs.

THE CURES (my own eyes): LICENSE at the root — the canonical MIT template whole: the "MIT License" title, "Copyright (c) 2026 Mark Losey" (the template's lowercase "(c)", year + holder per the headers' dominant form), the three paragraphs complete (permission notice, inclusion condition, "AS IS" warranty disclaimer), pure ASCII.
pyproject.toml :7 `license = "MIT"` (PEP 639 declarative SPDX form), :8 `authors = [{ name = "Mark Losey" }]` (PEP 621, email-less) — the file 166 lines, the two-line insert alone.
CONTINUATION.md:11 carries "root this repo" — the harness record whole otherwise; the file 76 lines.

ONE DIVERGENCE, named and adjudicated: SS1's fence priced the LICENSE at 7 lines / 1055 bytes with "no title line"; the landed file carries the template's title (9 lines). SS1's own normative sentence — "the standard MIT template verbatim (the canonical opensource.org/MIT text)" — carries the title; the fence's omission contradicts the spec's own provenance. The landed form IS the canonical template with the ruled copyright line; jikko's step-1 read-back named the 9-line form plainly. Adjudicated LEGITIMATE: the grant's substance exact (the three paragraphs, the ruled copyright line), the condition's own letter ("the standard MIT text") held by the landed bytes.

THE NO-BREAK PROOFS: zero Python touched — the three landed files are doc/metadata only (a new file, two TOML metadata lines, one Markdown phrase). The 33 copyright lines stand untouched at my own greps (15 src + 18 tests); three headers read myself: session.py:1 "Mark Losey" (the pairing form), __init__.py:1 and test_smoke.py:1 "Mark A Losey" — the pairing, never the rewrite.
The shrunk scope honored: the .plans records untouched (100+ /Users/ hits remain at my own grep — the scrub deferral standing); the family-name comments kept (service.py:250 "tane/kepric", tests/__init__.py:2 — read myself).

THE FLOOR at my own hands, verbatim: test (all) — "197 passed in 26.27s"; lint (check) — "All checks passed!"; typecheck — "0 errors, 0 warnings, 0 informations".

THE VERDICT — G-HYGIENE's three conditions:
1. THE CURES PER THE APPROVED SPEC — GREEN: the LICENSE (the standard MIT text; the title divergence named and adjudicated above), pyproject's :7/:8 exact, CONTINUATION:11 rewritten with no absolute path.
2. THE MARKER GREPS CLEAN — GREEN: grep /Users/ over CONTINUATION.md → ZERO hits; the pyproject license + authors fields present at :7/:8; the LICENSE at the root, the standard form.
3. THE FLOOR + MY RE-RUN — GREEN: the three instruments green at my own hands — 197 passed (the expected 197), pyright 0/0/0, ruff zero findings.
