<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/hygiene

**Route:** prioritree-review (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T01:21:21Z |
| 2 | report | togo | 2026-11-23T01:22:55Z |
## Reported by togo — 2026-11-23T01:22:55Z

# THE HYGIENE UNIT BRIEF — togo's synthesis (prioritree-review, G-HYGIENE-BRIEF, 2026-11-22)

Ground consumed: the review brief (reports/synthesize/review-brief.md — §1b the hygiene map, §2 the classes ruled, §3 unit 2's fence + gate) + shindan's census (reports/census/hygiene.md — the five cures, the false-positive map) + Q-repo-review ruling 4 (junro.json:444 — THE COLLABORATOR'S FOUR CALLS: "License file: let's do it. MIT. --- ship web in the package and mcp --- defer the scrub. --- pypi deferred.") + the touched surfaces at HEAD (pyproject.toml:1-7, CONTINUATION.md:11, the src/test headers). The synthesis decides nothing; the collaborator rules at the gate.

## 1. THE SCOPE FENCE — the shrunk set (ruling 4's call 3)

**LANDS (three files, three cures):**
1. **LICENSE** at the repo root — the standard MIT text (call 1).
2. **pyproject.toml's [project] fields** — `license` + `authors` (call 1).
3. **CONTINUATION.md:11** — the absolute root path cured (the review brief's in-tree rewrite; line 11 is the file's ONLY /Users/ hit, verified at HEAD).

**DOES NOT TOUCH:**
- **The .plans records** — the scrub DEFERRED (call 3; the live-scrub ruling stands recorded, banked for a later trigger — this unit never edits a record).
- **The family-name comments** (service.py:250 + tests/__init__.py:2) — KEPT (call 3, per the recommendation: internal names, no paths, no personal data).
- **The .opencode paths** — the hikari-side operational note (cycle-generated, never hand-edited; out of this tree's hands — the sibling action named at the review brief, never this unit's work).
- **The src/tests copyright lines** — they STAND: every src file (the 14 modules + the package __init__ — 15 files at HEAD) and all 18 test files carry `Copyright (C) 2026 … All rights reserved.` at line 1; now PAIRED by the LICENSE (shindan's fence: no blanket rewrite).
- **The false-positive map** — noise, not work (the .gitignore template residue, the sweep's own prompt echo, the sk-/token/secret/API_KEY substring classes).
- **The wheel question** (call 2: ship web + mcp in the package) — rides the install-deliverable unit, never this one.
- **CONTINUATION's other drifts** (the MCP-era staleness, httpx2's table, the wrapper count, the 655/654 count) — the readme-docs unit's fence.

## 2. THE MECHANISMS RULED

**2a. The LICENSE's form:** the standard MIT template verbatim (the OSI canonical text). The copyright line: **"Copyright (c) 2026 Mark Losey"** — the year 2026 per every header; the holder per the dominant src-header form (14 of 15 src files carry "Mark Losey"; the three "Mark A Losey" files — src/prioritree/__init__.py:1, tests/__init__.py:1, tests/test_smoke.py:1 — stand unwritten: the same holder, the middle initial the only variance, the grant unambiguous). The template's own lowercase "(c)" rides the LICENSE (the headers' "(C)" is the file-comment form; the LICENSE carries the template's).

**2b. pyproject's fields** (the [project] table, pyproject:1-7 the region — currently name/version/description/readme/requires-python/dependencies; no license field, no authors field):
- `license = "MIT"` — the modern declarative SPDX-expression form (PEP 639; hatchling serves it; the LICENSE file at the root + the expression the standard pair — no license-file pointer needed).
- `authors = [{ name = "Mark Losey" }]` — the PEP 621 table form; NO email (the census: no personal email anywhere tracked — the email-less entry the honest form).
- **THE CLASSIFIER RULED:** the declarative field suffices — `License :: OSI Approved :: MIT License` is optional and OMITTED (legacy metadata beside the machine-readable SPDX truth; a later publish may add it additively).

**2c. CONTINUATION.md:11's cure:** `the third TargetSpec (root /Users/marklosey/projects/prioritree;` → `the third TargetSpec (root this repo;` — the meaning preserved (the record's claim stays true: the TargetSpec's root IS this repo's own root; the machine-specific path leaves the tracked surface). One phrase inside the line; the line's harness record whole otherwise.

## 3. THE ACCEPTANCE MAPPING (G-HYGIENE's three conditions, junro.json:273-279)

1. **The cures land per the approved spec** → §1's three cures in §2's forms; the spec lane (synthesize/hygienespec, closing G-HYGIENESPEC-BRIEF) pins the exact bytes — this brief the shape, the spec the bytes.
2. **The cured surfaces' marker greps clean** → post-cure: CONTINUATION.md carries zero /Users/ (the single hit removed); pyproject's license + authors fields present; the LICENSE at the root, the standard form.
3. **The floor green + kensho** → the cures touch zero code bytes (a new file, two metadata fields, one prose phrase): pyright 0 errors/0 warnings/0 informations, ruff zero findings, the suite green (197 at the last live run); **kensho's independent re-run at validate/hygiene** — his own hand, the greps + the three floor instruments re-run.

## 4. THE HANDOFF — the spec lane's open questions (synthesize/hygienespec → G-HYGIENESPEC-BRIEF)

- **The LICENSE text's exact bytes** — the template fenced verbatim in the spec (the copyright line settled per §2a; the body the canonical grant-paragraph + notice-paragraph + warranty form).
- **The pyproject regions** — the exact hunk: the fields' placement inside [project] (the spec pins the line positions against pyproject:1-7; the classifier's omission is the hunk's own shape).
- **The CONTINUATION hunk** — the exact before/after at line 11 (§2c's substitution, byte-precise).
- **The per-step plan** — three files, three steps per the file-unit law (R8): (1) the LICENSE create; (2) pyproject's two fields; (3) CONTINUATION:11's phrase — each its own dispatch, each step's completing act the report op (R6/R11), one commit per increment at the landing.

## 5. THE TRADE-OFF THE PLAN CARRIES

The pairing is the cure, never the rewrite: 33 header lines reading "All rights reserved" now stand one file away from the grant that answers them. Rewriting the headers would be the blanket rewrite shindan's fence rules out (theater + churn over a uniform, deliberate authorship mark); keeping them means the headers mark authorship while the LICENSE alone carries terms — honest, but the world must be ABLE to find the grant: the readme-docs unit's README should name the LICENSE (the sibling dependency named here, never re-ruled there). And the deferral named honestly: the .plans records' 100+ private paths remain tracked at this unit's close — the privacy class's records member waits on the banked scrub's later trigger; this unit cures the legal pairing + the one in-tree path, never the class whole. The gate remains the collaborator's: G-HYGIENE-BRIEF green, then the spec, then the build.

— togo, the synthesis leg, read-only by design; this report is the one write.
