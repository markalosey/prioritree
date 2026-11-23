<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — design/install-story

**Route:** prioritree-review (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T01:10:35Z |
| 2 | report | suisen | 2026-11-23T01:12:05Z |
## Reported by suisen — 2026-11-23T01:12:05Z

SUISEN — design/install-story — R2's deliverable form: the recommendation (2026-11-22). Ground consumed: the four census reports (keisan's honesty classes, rikai's fresh-clone mechanism, tansa's claims map, shindan's cure fence) + pyproject.toml whole + R2's ruling (the uv leaning carried, never mandated).

THE CANDIDATES PRICED:
(a) `uv tool install prioritree` [PyPI] — BROKEN today: unpublished, the resolver's own refusal (keisan's broken class). A 0.1.0 publish earns preconditions: the LICENSE pairing (hygiene iv — "all rights reserved" with no license grants nobody anything), CI (deferred, no .github/), and the packaging ruling (the wheel's packages=["src/prioritree"] ships NO web tier — ship web/ or publish the CLI-only truth). Not a README promise until earned.
(b) `uv tool install .` [path] — runs today: the prioritree console script + the six deps, usable anywhere; per-project state by design (--home the named escape). Price: the wheel carries NO web tier; the flat deps table drags six packages behind a stdlib-only CLI.
(c) the repo-clone form (make dev at the repo root) — the ONLY whole-product truth: web/templates + static ride the clone; the CWD-relative homes resolve at the root; all five tiers operable. Price: no global tool — the story is "clone, not pip".
(d) `pip install prioritree` — (a)'s publish question, minus uv.lock's pins — strictly weaker for a uv-first tree. Declined.
(e) the hybrid — (c) primary + (b) as the CLI-anywhere lane, named as ONE install story.

THE RECOMMENDATION: (e) — the clone as the README's primary Install, `uv tool install .` as the documented CLI-anywhere lane; PyPI (a)/(d) DEFERRED with the named preconditions. Reasoning: the README may promise only what runs (moho's walk will test exactly this); (c) is the only whole-product path and cures the census's biggest gap (README 0 commands); (b) is R2's leaning confirmed in its runnable form — "some sort of uv tool install" IS the path form today. The leaning honored, refined, never mandated.

THE README'S SHAPE — Install: requirements (Python 3.13+, uv); the fresh-clone sequence per keisan's arithmetic (clone → cd prioritree → make dev → make test → make lint → make typecheck → git config core.hooksPath .githooks → make start → open http://127.0.0.1:8000/); the CLI-anywhere lane (uv tool install . — five ops, per-project state, --home, NO web tier named honestly); the NOT-promised line (no PyPI presence). Usage tier-by-tier: the CLI's five ops; the web lifecycle (start/status/stop/restart, PORT/HOST); the service's six routes; the MCP's two forms (stdio per session; --serve — the port-8000 collision with make start named: one at a time, or make PORT=). The discipline block: the repo-root CWD law (the store + templates mint where you stand — the silent wrong-path gap), the hooksPath pointer (never clones), .prioritree/ mints at runtime.

THE HYGIENE CLASSES RULED (shindan's five, R1's map consumed):
(i) .opencode paths — OPERATIONAL NOTE: hikari-side regeneration only (cycle-generated, never hand-edited); out of this tree's hands, named for the brief's sibling-action list.
(ii) .plans redaction — RULED LIVE SCRUB, the collaborator's hand, VIA TOOLING: paths → relative forms, the gitea/LAN line removed; append-only honored — one ruled commit, NEVER a history rewrite (the commit hashes the records cite must keep resolving). Excision declined: it breaks the README's measured citation at a fresh clone.
(iii) CONTINUATION.md:11 — IN-TREE REWRITE (the hygiene cure unit, jikko's hand, R8's file-unit): the absolute root → "this repo".
(iv) copyright/LICENSE — COLLABORATOR'S CALL, options named: (A) a LICENSE file + pyproject license + authors fields (publishable, the claim paired); (B) all-rights-reserved alone (private truth, publish off). Recommended: (A), BEFORE any publish.
(v) family-name comments (service.py:250, tests/__init__.py:2) — KEEP: internal family names, no paths, no personal data; the exposure is the .opencode/.plans sets, not the two lines — rewriting them alone is theater. Escalation: if the family names are sensitive, the cure is (i)+(ii), never these lines alone.
