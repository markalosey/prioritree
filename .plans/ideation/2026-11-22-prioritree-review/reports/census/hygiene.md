<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/hygiene

**Route:** prioritree-review (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T01:05:28Z |
| 2 | report | shindan | 2026-11-23T01:09:19Z |
## Reported by shindan — 2026-11-23T01:09:19Z

# SHINDAN — census/hygiene — the hygiene sweep's diagnosis (2026-11-22)

## 1. SECRETS — ZERO real leaks in the tracked set
The seven marker greps (password, passwd, BEGIN.*PRIVATE KEY, aws_, AKIA, ghp_, xox) each return exactly ONE hit — my own dispatch prompt (.plans/ideation/2026-11-22-prioritree-review/.junro/packets.jsonl:7), the grep list itself: false positive by construction. sk-: 82 hits, all "task-/ask-/desk-" substrings (.plans records; .opencode/tools/junro.ts:81) — ZERO in *.py. api_key/API_KEY: 34 hits, ALL variable names — TAVILY_API_KEY/CONTEXT7_API_KEY env reads + honest missing-key errors (web.ts:92-93/:132-133/:177-178/:204-205) and template-literal `Bearer ${apiKey}` (:105/:148/:183) — no key VALUES anywhere tracked.
token: 100+ hits — grammar/budget tokens (cli.py, mcp_server.py:77/:535) + the tiktoken dependency (uv.lock:1626+): generic. secret: 18 hits — the sweep's own scope text + discover/foundations.md:173 (the INPUT sibling's infisicalsdk dep line — another tree's inventory, no key). .env residue: .env EXISTS on disk but is GITIGNORED (.gitignore:133 — properly excluded by design); .envrc (tracked, read whole): comments + `dotenv`, its own header "NO SECRETS LIVE HERE". No .pem, no credential emails. VERDICT: no credential has ever landed in a tracked file.

## 2. PRIVATE PATHS — two real surfaces + the records bulk
- SHIPPED CODE: src/, tests/, web/ — ZERO /Users/, ZERO ~. The product surfaces are clean.
- .opencode CONFIGS (tracked, cycle-generated): junro.ts 18 invocation lines (:101-:263) + help (:266); git.ts (:53/:58/:68/:74/:81 + help :84); kumi_render.ts (:49/:51); prompts/seats/jikko.md:14 — all /Users/marklosey/projects/kepric/hikari/... (jikko.md the repo root). REMEDIATION: never hand-edit — the cure is hikari-side regeneration (env/relative resolution); the exclusion question rides the design.
- .plans RECORDS (R1: no exemption): 100+ /Users/ hits (the grep cap; class uniform) — tree-root maps (discover/harness.md:10-14, foundations.md:10-14), briefs' patch roots (harness-brief.md:87), build/verification records (harness-verification.md:24/:37/:49/:54/:68), EVERY dispatch prompt naming the repo root (all five stores' packets.jsonl), friction-ledger surfaces (:1, :35). ONE real ~ expansion: friction-ledger.jsonl:9. Internal infra: discover/foundations.md:179 — gitea.kepric.io + LAN IP 192.168.1.22. REMEDIATION: the design rules it (append-only history — a ruled scrub, never hand edits).
- DOCS: CONTINUATION.md:11 (the repo root in the harness record) — rewrite candidate. README/AGENTS/Makefile/pyproject/uv.lock/opencode.json/.githooks/.envrc: ZERO private paths.

## 3. PERSONAL DATA
- `Copyright (C) 2026 Mark Losey. All rights reserved.` — line 1 of ALL 14 shipped src modules + ALL 18 test files ("Mark A Losey" in src/prioritree/__init__.py, tests/__init__.py, tests/test_smoke.py). Deliberate, uniform — but unpaired (NO LICENSE file, NO pyproject authors field). NO personal email anywhere (personal-domain grep: zero; the generic regex's 4 hits = the git remote + plugin@version specs).
- markalosey: CONTINUATION.md:15/:21 + discover/foundations.md:179 — mirrors the repo's own public origin (benign, mapped).
- The internal family names (kepric/hikari/tane) ride tracked surfaces beyond paths: shipped-code provenance comments — service.py:250, tests/__init__.py:2 — and .opencode/scripts engines (patch.py:36-37/:117-118, curate.py:74-77, friction_ledger.py:1048, test_runner.py:4).
- .plans references the collaborator by ROLE ("the collaborator") throughout — the name only via the copyright lines; no other identifier.

## 4. THE FALSE-POSITIVE MAP
- .gitignore:1-176 — the standard Python template's residue (Django/Flask/Scrapy/SageMath): never applicable, not a leak; :177-184 the tree's own.
- The dispatch-prompt echo: packets.jsonl:7 carries every swept marker once — THIS sweep's own artifact; future sweeps re-hit it: ruled noise here.
- sk- 82x substring noise; token 100x grammar/budget/dependency uses; secret 18x scope text; API_KEY 34x variable names; ~/ 4x generic convention docs (.envrc:14, discover/harness.md:29, empty-return-detector.ts:67, run-store-brief.md:76 — plus the 1 real at friction-ledger.jsonl:9).
- THE CURE FENCE: exactly five real cures — the .opencode path regeneration (hikari-side), the .plans redaction ruling, CONTINUATION.md:11's rewrite, the copyright/LICENSE pairing question, the service.py:250 + tests/__init__.py:2 family-name comments. Everything else is noise — no blanket rewrite.
