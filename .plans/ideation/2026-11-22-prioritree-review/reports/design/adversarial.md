<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — design/adversarial

**Route:** prioritree-review (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T01:10:44Z |
| 2 | report | hyoka | 2026-11-23T01:12:21Z |
## Reported by hyoka — 2026-11-23T01:12:21Z

# HYOKA — design/adversarial — the census attacked (2026-11-22)

## SPOT-VERIFICATIONS — every load-bearing finding attacked, every one HELD
- README staleness: CONFIRMED whole-read (24 lines). :19 "first runtime deps: fastapi + uvicorn[standard]" vs SIX at pyproject:7 (fastapi, httpx2, jinja2, ouncemcp, python-multipart, uvicorn[standard] — read myself); :19 "the five routes" vs SIX @app decorators (service.py:321/:350/:380/:417/:451/:490 — the manifest exactly where rikai cited); :20 web "banked" vs web.py built; :24 "the MCP tier is the ruled next effort" vs mcp_server.py:571-580 live; :24 "131 tests green" vs keisan's LIVE 197; ZERO commands in the file — confirmed.
- hooksPath: CONFIRMED — .git/config:8 `hooksPath = .githooks` (local-only, read myself); pre-commit tracked, the pointer never cloned.
- Wheel: CONFIRMED — pyproject:16-17 packages=["src/prioritree"] only; web/ outside it; no license field, no authors field.
- Port collision: CONFIRMED — Makefile:3 `PORT ?= 8000` vs mcp_server.py:574 port=8000 hardcoded; main() read whole, no override flag.
- Zero secrets: CONFIRMED under my OWN greps — src/, tests/, web/ zero hits on every marker + sk-[20+]; uv.lock zero private paths AND zero private sources. Hygiene's provenance cites held: service.py:250 (tane/kepric), tests/__init__.py:2, 18/18 test copyright lines, "Mark A Losey" in exactly the two named files.
- Census internal consistency: rikai "17 modules" vs keisan/hygiene "18 files" = the same set (my glob: 18 files = 17 test modules + __init__.py) — different nouns, no contradiction.

## MISSED SURFACES (named honestly)
1. .githooks/pre-commit's OWN CONTENT — neither commands nor consistency read past its existence. Three material facts: (a) ruff is "PHASE 2 (named, pending)" in the hook's own header — the hook enforces pyright ONLY: even with the pointer set, the lint half of the floor is NOT enforced at commit (the "floor believed enforced" gap is larger than censused); (b) PRIORITREE_HOOK_BYPASS=1 — a tracked bypass env var; (c) the hook's header carries the SAME dead regen line as AGENTS.md (generator absent in this repo) — a fourth instance of that class.
2. uv.lock's DEPENDENCY SOURCES — the unasked highest-stakes question: httpx2/ouncemcp are nonstandard deps; had they resolved from private git (gitea.kepric.io is .plans-named internal infra), the whole fresh-clone arithmetic collapses. Checked myself: zero git+/gitea/file:/ssh:// in the lock — public resolution; the arithmetic HOLDS.
3. web/templates rendered copy — doc-surface named it "not censused"; my spot-read of landing.html: current, accurate, clean world-facing prose, zero private paths in web/. Low yield, but the 14-template sweep belongs in the synthesis if the web tier ships.

## THE CURE SET RANKED (blocking a public ship first)
1. BLOCKING — README rewrite: wrong on every load-bearing number (deps 2→6, routes 5→6, web/MCP eras, tests 131→197), zero commands — the product is unoperable from the world's only door.
2. BLOCKING — the floor truth: the hooksPath instruction must land in the README (the only world-facing place) + the ruff-pending fact named — never claim the floor where only pyright rides.
3. BLOCKING (privacy class, one cure-set): .plans scrub ruling (100+ /Users/, gitea.kepric.io + LAN IP at foundations.md:179) + .opencode path regeneration (hikari-side) + CONTINUATION.md:11 + the family-name comments (service.py:250, tests/__init__.py:2) — all tracked, all ship with the public clone.
4. BLOCKING — LICENSE: 32 files claim "All rights reserved" with no grant; the world cannot legally use a line of it.
5. MUST-DECIDE — the wheel's web-absence: ship web/ in the packages field or say CLI-only truth.
6. POLISH — the port collision (a warning or a flag); CONTINUATION.md staleness; the dead regen lines; service.py:44-45's fence wording drift.

## VERDICT
The census MEETS THE BAR as the synthesis's ground: every attacked finding held at its cited line, the zero-secrets verdict survived independent greps, and no missed surface overturns a census finding — the hook's content ADDS to the gap list, the lock's sources CONFIRM the arithmetic. The synthesis may proceed on this ground; fold the hook-content facts and this ranking in.
