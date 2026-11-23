<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/doc-surface

**Route:** prioritree-review (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T01:05:19Z |
| 2 | report | tansa | 2026-11-23T01:09:02Z |
## Reported by tansa — 2026-11-23T01:09:02Z

census/doc-surface — the documentation-surface inventory (tansa, prioritree-review, 2026-11-22). Read-only census; every finding a pointer, nothing decided.

THE SURFACES (path — audience — size):
- /README.md — the world — 24 lines. The repo's only world-facing prose.
- /pyproject.toml — the world (metadata) + the team (the rulings block) — 164 lines. Public claims: prioritree 0.1.0; the ruled Q-purpose description verbatim; requires-python >=3.13; SIX runtime deps (fastapi, httpx2, jinja2, ouncemcp, python-multipart, uvicorn[standard]); console script prioritree. No license field.
- /Makefile — the operator — 70 lines. `make help` self-documents 9 targets (dev/test/lint/typecheck/start/stop/status/restart/help); the lifecycle four are the freshest operator doc (2026-11-22), PORT/HOST overridable.
- /.gitignore — the operator — 184 lines. The github Python template's comments + two home-grown hunks (.opencode derived views :177-181; /.junro/ + .prioritree/ :183-184).
- /AGENTS.md — the team — 4 lines.
- /CONTINUATION.md — the team — 76 lines (very long lines).
- /.opencode/prompts/seats/*.md — the team — 13 files, 60-68 lines each, 806 total; each opens @generated + a regen line naming scripts/generation/clarity_scaffold.py.
- /.opencode/tools/*.ts — the team — 12 wrappers, 1364 lines (web 335, junro 271, friction 188, lifecycle 93, git 89, calculate 78, _run 58, kumi_render 58, curate 54, test 49, patch 48, lint 43); each header a provenance record.
- /opencode.json — the team — 522 lines (13 seat blocks, four builtins disabled, the closed-world deny).
- ABSENT everywhere: LICENSE (no file, no pyproject license field), CHANGELOG, docs/, .github/ (CI — matching README's "CI is deferred").
- Adjacent tracked sets, named not censused: /web/templates/ (14 html — the human's rendered surface, not docs); /.plans/ideation/ (8 effort stores — the record home); /scripts/generation/ EMPTY in this repo.

README.md WHOLE — headings verbatim: H1 "Priori-tree"; "## Architecture" (:13); "## Status" (:22). NOTHING else: no install, no usage, no commands, no license section; zero command examples anywhere in the file.
Claims: the product sentence (:3); the measured 51-of-54 in-band cells, 94.4%, 2026-11-21, cited to the budget-curve record (:5); human AND LLM through the one vote interface (:7); the Q-purpose ruling blockquote (:9-11); the four-form stack (:17-20 — library BUILT / CLI BUILT / service LIVE / web "banked"); the status dates, "The MCP tier is the ruled next effort", "CI is deferred" (:24).
Freshness vs what exists: service covered and accurate (LIVE 2026-11-21 — though it doesn't know the sixth query or the 156-test floor); web tier STALE — "banked" (:20) but built 2026-11-22 (web.py 654 lines, 14 templates, mounted at the service tail); MCP STALE — "ruled next effort" (:24) but mcp_server.py (580 lines) + store_lock.py (91) + the store /.plans/ideation/2026-11-22-prioritree-mcp/ all exist; lifecycle targets ABSENT from README (live in the Makefile since 2026-11-22); CI-deferred accurate.

AGENTS.md + CONTINUATION.md: AGENTS.md = the goal-line sentence (the Q-harness ruling verbatim) under @generated/regen headers naming an engine path that does NOT exist in this repo (/scripts/generation/ is empty; the engine lives at hikari) — the regen instruction unrunnable here. CONTINUATION.md = the tree's whole history: six effort records (birth, core, cli, budget-curve, service, ux) + "WHERE TO CONTINUE FROM"; team vocabulary throughout (seat names, FR-MEM handles, commit hashes, collaborator rulings, store paths); its last section still names the MCP era as NEXT — one effort stale (the MCP effort exists on disk). Both are internal-team records facing a world-facing repo; whether they belong in a public repo is the reviewer's design call — the census names their audience honestly: the team, not the world.

THE DOCSTRINGS' PUBLIC CLAIMS — every module opens "Copyright (C) 2026 Mark Losey. All rights reserved." (:1), a rights claim with no LICENSE file backing it:
- /src/prioritree/cli.py (402): "the wrapper-tier command face" — five subcommands 1:1 on the five ops; argv in, stdout out, exit 0/1/2 (0 = success AND DONE); argparse stdlib only, zero runtime deps at this tier.
- /src/prioritree/service.py (540): "the wire face" — five routes REST 1:1 + the sixth query; the BOOT INSTRUCTION embedded in the docstring: "uvicorn prioritree.service:app"; the ruled status map (200, 201, the 400 re-badge, 404, 405, 409, the 500 crash envelope).
- /src/prioritree/web.py (654): "the web fronts" — the child app over the service's wire, nine routes; template files authored at web/templates/, loaded, rendered — "the web tier is the human's surface, not an API".
- /src/prioritree/mcp_server.py (580): "the member tier" — the five ops as OunceMCP tools (runs.register, runs.next, votes.cast, votes.census, runs.tally); the BOOT INSTRUCTION embedded: python -m prioritree.mcp_server (stdio per session) / the --serve flag (streamable-HTTP).
- /src/prioritree/store_lock.py (91): "the machine-wide lock seam" — the advisory exclusive flock on {store_home}/.prioritree.lock, never deleted; closed because all writers are local.
- /src/prioritree/session.py (318): "the chain's public face" — register → schedule → vote → tally composed; ExhaustedQueue the DONE signal; zero runtime deps, no datetime.

Files read: the 7 root surfaces (README.md, AGENTS.md, CONTINUATION.md, pyproject.toml, Makefile, .gitignore, opencode.json); heads of the 6 shipped modules; heads of all 12 .opencode/tools/*.ts; heads of all 13 .opencode/prompts/seats/*.md; directory listings (root, .opencode + prompts/seats + tools, .plans/ideation, scripts, scripts/generation, web, web/templates).
