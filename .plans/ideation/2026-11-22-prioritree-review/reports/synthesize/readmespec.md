<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/readmespec

**Route:** prioritree-review (executing) | **Events:** 4 | **Reports:** 3

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T01:51:05Z |
| 2 | report | togo | 2026-11-23T01:56:39Z |
| 3 | report | togo | 2026-11-23T01:56:46Z |
| 4 | report | togo | 2026-11-23T01:56:53Z |
## Reported by togo — 2026-11-23T01:56:39Z

# THE README-DOCS EXACT-TASK SPEC — togo (synthesize/readmespec, prioritree-review — the deliverable G-READMESPEC-BRIEF closes on, 2026-11-22). PART 1 of 3 (append-only pieces; the projection composes): §0 ground + §1 the README whole.

## 0. GROUND + FENCE

**Ground consumed (the read-back):** the unit brief (reports/synthesize/readme.md — G-README-BRIEF approved: the nine-section shape, the fence, the trade-offs) + the three files at HEAD (README.md 24 lines, CONTINUATION.md 76, AGENTS.md 4 — read whole) + the census's consistency map (reports/census/consistency.md — every break at its cited line) + the review brief §1 (reports/synthesize/review-brief.md — the checkable-cures map) + the tree's own bytes: cli.py whole (the argv grammar, the flag spellings, the exit-code mapping, the marker forms), service.py's six route decorators (:321 POST /runs, :350 GET next, :380 POST votes, :417 GET state, :451 GET tally, :490 GET manifest), mcp_server.py's run forms (:571-576 — bare stdio / --serve at hardcoded port 8000), the Makefile whole (nine targets, PORT ?= 8000, HOST ?= 127.0.0.1), pyproject.toml (:7 license = "MIT", :9 the six deps, :16 the console script, :19 the wheel's packages = src/prioritree), the landed LICENSE (MIT, Copyright (c) 2026 Mark Losey), scheduler.py's enumeration (:80-84 — the seed UNUSED, the id-sorted i-j queue), session.py's DONE bytes (:228-238, rendered at :92), votes.py's census maps (:517-518, :525-526 — both pair members counted per vote), tally.py's map orders (:198-202, :474-475) + TALLY_ALGORITHM (:47 "win-rate-v1"), registry.py's verdict triple (:20 prefer-a/prefer-b/tie), run_store.py's STORE_HOME (:53 .prioritree/runs), the MCP store on disk (.plans/ideation/2026-11-22-prioritree-mcp/ — build/mcp-server.md + validate/mcp-server.md landed; design/member-path.md resting). Every transcript byte in §1 is DERIVED from these constructions — no byte guessed.

**THE FENCE (the approved brief's, unchanged):** README.md + CONTINUATION.md + AGENTS.md — three prose files, ZERO code bytes. The Makefile, pyproject.toml, and the src docstrings untouched (the README cites, never rewrites). The .opencode surfaces + .githooks/pre-commit out (cycle-generated, hikari-side regeneration only). The .plans records out (the scrub deferred). The measured citation kept resolving. The install lane authored per the CURRENT truth (the install-deliverable unit re-rules it when the wheel grows web/ + MCP — the named moving surface).

## 1. THE README WHOLE — the complete post-build file (one dispatch; the fence IS the file's whole content, the current 24 lines fully replaced; the four kept blocks byte-identical to the current README's own)

````markdown
# Priori-tree

Priori-tree is a generalized prioritization system: for any list and comparison operator, run the pairwise permutations, store the votes, tally — the output list is in a superior order than sizing individual items, because discernment between two items is easy (for humans and LLMs) while absolute sizing is not.

Measured (2026-11-21): pairs + tally beats absolute sizing at equal budget in 51 of 54 in-band cells (94.4%; the 3 exceptions narrow and seed-local) — the record at `.plans/ideation/2026-11-21-budget-curve/build/budget-curve-record.md`.

The comparator class is both human AND LLM — both vote through the same vote interface; the tally is a pure function of the stored votes.

> Priori-tree is a generalized prioritization system based on the concept that LLM and Humans are great at discerning the difference between two items but not great at sizing an item. That is a simplification. Consider: a human is great at determining that a basketball is larger than a grapefruit. But not great as identifying the exact dimensions of a grapefruit or a basketball. By taking a list and running through the pairwise permutations for any given comparision operator. Storing the votes, then tallying. we get a list out that is in a superior order than trying to size individual items.
>
> — the collaborator's Q-purpose ruling, 2026-11-19 (verbatim)

License: MIT — the [LICENSE](LICENSE) file at the repo root (Copyright (c) 2026 Mark Losey).

## Quickstart

The first comparison, end-to-end, from a fresh clone. Run every command from the repo root (see [Discipline](#discipline)):

```console
$ git clone git@github.com:markalosey/prioritree.git
$ cd prioritree
$ make dev
$ make test
$ git config core.hooksPath .githooks
$ make start
$ open http://127.0.0.1:8000/
```

The browser is the human comparator's surface: register a list, vote the served pairs, read the ranked whole.

A first comparison at the command line instead (no server; from the repo root):

```console
$ uv tool install .
$ prioritree register aloe:Aloe basil:Basil cilantro:Cilantro --operator-id plant-size --question "Which is the bigger plant?"
RUN-0001
$ prioritree next RUN-0001
pair	aloe	basil	0
$ prioritree vote RUN-0001 aloe basil prefer-a mark human
vote	VOTE-0001	1
```

Then serve and vote the remaining pairs the same way; at quorum on every pair the tally emits the ranked whole — the full transcript: [Input/Output Examples](#inputoutput-examples).

## Architecture

Five tiers, one layered architecture, library-first:

- **Library — `src/prioritree` — built 2026-11-20.** The pure-logic core at the bottom of the stack: items, the comparison operator, pair scheduling, votes, tally — the tally a pure function of the stored votes. State is file-backed JSONL (no database).
- **CLI — built 2026-11-21.** Wraps the core: the five-op surface at the command line (register → next → vote → state → tally), the `prioritree` console script.
- **Service (FastAPI) — live 2026-11-21.** Serves the core over HTTP: six routes (the five ops 1:1 + the manifest query), one process-wide lock seam, every error body the three-part form (expected / found / next-action).
- **Web — built 2026-11-22.** Fronts the service: `src/prioritree/web.py` (654 lines, nine routes, 14 authored Jinja2 templates + 2 static files) over the in-process seam — the human comparator's vote surface at the browser.
- **MCP — live 2026-11-22.** The agent-callable tier: `src/prioritree/mcp_server.py` (580 lines, the five OunceMCP tools — `runs.register`, `runs.next`, `votes.cast`, `votes.census`, `runs.tally`; the `store_lock.py` flock seam), two run forms.

Runtime dependencies: six — `fastapi`, `httpx2`, `jinja2`, `ouncemcp`, `python-multipart`, `uvicorn[standard]` (`pyproject.toml`). The quality floor: 197 tests green, pyright clean, ruff clean.

## Usage

### CLI

The five ops, one console script. The report language is marker-first, tab-separated.

| op | invocation |
|---|---|
| register | `prioritree register <id:label>... --operator-id <id> --question <text> [--quorum <n>]` |
| next | `prioritree next <run_id> [--seed <n>]` |
| vote | `prioritree vote <run_id> <item_a> <item_b> <winner> <comparator_id> <comparator_class> [--notes <text>] [--supersedes <vote_id>]` |
| state | `prioritree state <run_id>` |
| tally | `prioritree tally <run_id>` |

- Item tokens are `id:label`, split on the FIRST colon — ids may not contain colons; labels may.
- The verdict set (the `winner` positional): `prefer-a`, `prefer-b`, `tie`.
- `--home <path>` rides all five ops — the store home (default `.prioritree/runs`, CWD-relative).
- Exit codes: `0` success AND DONE (the queue exhausted prints its three-field message on stdout); `1` refusals (the message on stderr); `2` argv errors and the unexpected (argparse's channel).

### Service (FastAPI)

```console
$ uv run uvicorn prioritree.service:app        # foreground
$ make start                                   # background, managed (make stop / status / restart)
```

Six routes over HTTP:

| route | op |
|---|---|
| `POST /runs` | register (201) |
| `GET /runs/{run_id}/next` | serve the next under-quorum pair |
| `POST /runs/{run_id}/votes` | cast one judgment |
| `GET /runs/{run_id}/state` | the census |
| `GET /runs/{run_id}/tally` | the ranked whole |
| `GET /runs/{run_id}/manifest` | the run's manifest |

### Web

The lifecycle targets — `make start`, `make stop`, `make status`, `make restart` (`PORT ?= 8000`, `HOST ?= 127.0.0.1`; override: `make start PORT=8100`). The browser at `http://127.0.0.1:8000/`: register a list, vote the served pairs, read the ranked whole.

### MCP

Two run forms:

```console
$ uv run python -m prioritree.mcp_server           # stdio, per session — the MCP host boots it
$ uv run python -m prioritree.mcp_server --serve    # streamable-HTTP at http://127.0.0.1:8000
```

Port note: `--serve` hardcodes port 8000 — the same default as `make start`; run one at a time, or start the web tier with `make start PORT=<other>`.

## Input/Output Examples

One run whole — a list in, three votes, the tally out (a fresh store; every byte as the tree emits it):

```console
$ prioritree register aloe:Aloe basil:Basil cilantro:Cilantro --operator-id plant-size --question "Which is the bigger plant?"
RUN-0001
$ prioritree next RUN-0001
pair	aloe	basil	0
$ prioritree vote RUN-0001 aloe basil prefer-a mark human
vote	VOTE-0001	1
$ prioritree next RUN-0001
pair	aloe	cilantro	0
$ prioritree vote RUN-0001 aloe cilantro prefer-b mark human
vote	VOTE-0002	2
$ prioritree next RUN-0001
pair	basil	cilantro	0
$ prioritree vote RUN-0001 basil cilantro prefer-b mark human
vote	VOTE-0003	3
$ prioritree next RUN-0001
exhausted — expected: all 3 scheduled pairs at quorum k=1 | found: the queue is exhausted — the walk fell through with no under-quorum pair (every pair at quorum on the census's AS-IS counts) | next: call tally_rank(run_id) — the tally path (R12's DONE; a standing correction can still SAFE HALT it — the census-vs-weighted seam, named and carried)
$ prioritree state RUN-0001
votes	3
item	aloe	2
item	basil	2
item	cilantro	2
$ prioritree tally RUN-0001
rank	cilantro
rank	aloe
rank	basil
counts	aloe	1	1	0
counts	basil	0	2	0
counts	cilantro	2	0	0
coverage	1	True
pairs	aloe	basil	1
pairs	aloe	cilantro	1
pairs	basil	cilantro	1
version	win-rate-v1
```

Reading the lines:

- `register` prints the bare run id — `RUN-0001`, the file stem of `.prioritree/runs/RUN-0001.jsonl`.
- `next` prints `pair`, the two ids, the votes already on the pair; the queue is the id-sorted pairwise schedule; at exhaustion it prints the DONE message instead (exit 0).
- `vote` prints `vote` (a new cast) or `ack` (a byte-identical re-cast — the dedup), the vote id, and the run's whole vote count.
- `state` prints `votes` (the total) then one `item` line per item — the votes the item appeared in.
- `tally` prints the ranked whole: one `rank` line per tie group, `counts` (wins, losses, ties) per item, `coverage` (the graph's components, done), a `cycle` line only when a Condorcet cycle exists, `pairs` (the weighted per-pair counts), and `version`.

## Discipline

- **The CWD law.** The store (`.prioritree/runs`) and the web mounts (`web/templates`, `web/static`) resolve CWD-relative — run from the repo root, or your data lands where you stood (the directories mint silently on demand). The CLI's `--home` is the per-invocation escape.
- **The git hook.** `.githooks/pre-commit` is tracked, but the pointer never clones — set it by hand: `git config core.hooksPath .githooks`. The hook enforces pyright only; ruff is named, pending — run `make lint` for the full floor. `PRIORITREE_HOOK_BYPASS=1` is the tracked bypass.
- **The port collision.** `make start` and `mcp_server --serve` both default to port 8000 — run one at a time, or override (`make start PORT=8100`).
- **`.prioritree/` mints at runtime** — the server pid and log, the runs store; gitignored, never present in a clone.

## Install

**The clone — the whole product.** The only path that operates all five tiers: the web tier's templates and static files ride the repo, and the CWD-relative homes resolve at the root. Requirements: Python 3.13+ and uv. The full honest sequence:

```console
$ git clone git@github.com:markalosey/prioritree.git
$ cd prioritree
$ make dev
$ make test
$ make lint
$ make typecheck
$ git config core.hooksPath .githooks
$ make start
$ open http://127.0.0.1:8000/
```

**`uv tool install .` — the CLI anywhere.** Installs the `prioritree` console script and its six dependencies, usable from any directory. State is per-project by design: the store mints at `.prioritree/runs` under your CWD; `--home` redirects. The web tier does not ride this lane today: the wheel carries `src/prioritree` only (no web templates) — the clone is the web tier's only home.

**Not on PyPI.** `uv tool install prioritree` and `pip install prioritree` do not resolve — Priori-tree is not published. The publish is deferred: the license has landed; packaging and CI remain.

## Status

Born 2026-11-19 (the setup). The core library built 2026-11-20; the CLI built 2026-11-21; the claim measured 2026-11-21 (pairs + tally beats absolute sizing at equal budget — 51 of 54 in-band cells); the service live 2026-11-21; the web app built 2026-11-22; the MCP tier live 2026-11-22 (the five OunceMCP tools). CI is deferred — the git hook and the local gates stand in. The quality floor: 197 tests green, pyright clean, ruff clean.

## License

MIT — the [LICENSE](LICENSE) file at the repo root (Copyright (c) 2026 Mark Losey); `pyproject.toml` carries `license = "MIT"`.
````

**The kept-verbatim proof:** the product sentence (== pyproject:4's description, byte-identical), the measured citation (the current README:5, byte-identical — the record's path still resolving), the comparator line (README:7), and the Q-purpose blockquote with its citation line (README:9-11) all appear byte-identical in the fence. **The transcript's derivation (every byte pinned, none guessed):** the pair order from scheduler.py:80-84 (ids sorted; the i-j queue (aloe,basil), (aloe,cilantro), (basil,cilantro); the seed UNUSED — the reserved seam); the DONE line from session.py:228-238's three fields rendered per session.py:92's grammar; the state's counts from votes.py:525-526 (both pair members counted per vote; the map's order the register payload order); the tally's counts/pairs orders from tally.py:200-202 + :474-475 (payload order / queue order); `coverage 1 True` = str(len(components)=1) + str(done: bool); `version win-rate-v1` from tally.py:47; the vote lines' counts = the run's census count (the whole-run count, per the cli-acceptance cure's own note); the register's stem RUN-0001 = the fresh store's first file mint. Kensho confirms the whole transcript at a live run (moho's bar: every line the spec promises must run).

— PART 1 ends. PART 2: CONTINUATION's hunks + AGENTS' hunk. PART 3: the no-break proofs + the three-step plan + the trade-off.
## Reported by togo — 2026-11-23T01:56:46Z

THE README-DOCS EXACT-TASK SPEC — PART 2 of 3 (append-only pieces; the projection composes): §2 CONTINUATION's hunks + §3 AGENTS' hunk.

## 2. CONTINUATION'S HUNKS — the four drifts + the era refresh (the record otherwise untouched; the entries are history — these are accuracy fixes at their cited lines, never rewrites)

**Hunk C1 — :19, the wrapper count (STALE, ten → twelve):**

```text
- ... the ten wrappers at `.opencode/tools/` (_run, calculate, curate, friction, git, junro, lint, patch, test, web); ...
+ ... the twelve wrappers at `.opencode/tools/` (_run, calculate, curate, friction, git, junro, kumi_render, lifecycle, lint, patch, test, web); ...
```

**Hunk C2 — :53, httpx2's home (WRONG as present state → the service-era history named + the current truth appended):**

```text
- ... the tree's FIRST runtime deps, httpx2 dev the root cure; Q-service-concurrency ...
+ ... the tree's FIRST runtime deps, httpx2 dev the root cure at the service era — since the web tier httpx2 rides the MAIN deps table (pyproject:9; the dev group is pytest/pyright/ruff only); Q-service-concurrency ...
```

**Hunk C3 — :65, web.py's line count (WRONG, one-line drift → 654):**

```text
- ... src/prioritree/web.py at 655 lines — the child app over the in-process seam ...
+ ... src/prioritree/web.py at 654 lines — the child app over the in-process seam ...
```

**Hunk C4 — :72-76, the tail's next-era section (STALE, one era behind → the MCP era recorded + the review effort named + the continuation point at its close). The whole section (the heading + its four bullets) is replaced by:**

```text
## WHERE TO CONTINUE FROM — the review effort (prioritree-review, BORN 2026-11-22)

- **THE MCP ERA ARRIVED AND WHOLE:** mcp_server.py + store_lock.py landed (the five OunceMCP tools — runs.register, runs.next, votes.cast, votes.census, runs.tally; the flock seam), mcp-server green at the first unit boundary (the store at `.plans/ideation/2026-11-22-prioritree-mcp/`); the member-path + lifecycle-integration widenings resting (banked, unruled). Q-setup-arch's stack whole at five tiers: the pure-logic library at the bottom, the CLI wraps it, the FastAPI service serves it, the web app fronts it, the MCP tier exposes it.
- **THE REVIEW EFFORT (prioritree-review, born 2026-11-22 — the exhaustive review):** the census whole (the doc surfaces, the hygiene sweep, the consistency map, the command honesty 12/3/1) + the design lane reconciled; THE FOUR CALLS ruled — MIT landed, web+MCP in the wheel, the scrub deferred, PyPI deferred; the cure units composing (readme-docs → hygiene → install-deliverable, one file per dispatch, each at its own gate).
- **CONTINUE FROM the review effort's close:** the three cure units' gates and closes — the readme-docs unit's three files (README whole, CONTINUATION refreshed, AGENTS' truth), the hygiene unit's ruled surfaces, the install lane's landing — then the done call at the collaborator's ruling when the cure set is whole.
```

## 3. AGENTS' HUNK — the regen-line truth (the honest annotation naming the hikari-side engine; the goal line :4 UNTOUCHED)

**The hunk (the file's two header lines):**

```text
- <!-- @generated by scripts/generation/clarity_scaffold.py — do not edit manually; the scaffold is the emission authority, the authored source is Q-harness's goal-line ruling (the collaborator, 2026-11-19) -->
- <!-- regen: uv run python scripts/generation/clarity_scaffold.py --target prioritree -->
+ <!-- @generated — do not edit manually; the emission engine (scripts/generation/clarity_scaffold.py) lives in the sibling hikari tree, not this one — this repo's scripts/generation/ is empty; the authored source is Q-harness's goal-line ruling (the collaborator, 2026-11-19) -->
+ <!-- regen: from the hikari tree — uv run python scripts/generation/clarity_scaffold.py --target prioritree -->
```

**The cycle note (the spec rules the honest form):** AGENTS.md is cycle-generated (the @generated header) — the hunk's bytes are written as the form the scaffold's hikari-side template CAN carry (nothing in them is repo-state-specific; the annotation names the engine's home, which the template knows). THE COLLABORATOR'S HIKARI-SIDE ACTION NAMED: edit the scaffold's AGENTS.md emission template at hikari to emit these bytes, then re-emit `--target prioritree` so `--check` stays green — the re-emit reconciles the cycle; the in-tree hunk lands first as the honest record (the precedent the re-emit must match). The same dead regen line rides `.githooks/pre-commit`'s header + the 13 seat prompts — the same hikari-side re-emit's surfaces, the sibling action named, out of this unit's fence.

— PART 2 ends. PART 3: the no-break proofs + the three-step plan (R8) + the trade-off.
## Reported by togo — 2026-11-23T01:56:53Z

THE README-DOCS EXACT-TASK SPEC — PART 3 of 3 (append-only pieces; the projection composes): §4 the no-break proofs + §5 the three-step plan (R8) + §6 the trade-off.

## 4. THE NO-BREAK PROOFS (each checkable at the gate)

1. **Every cure checkable against the review brief's §1 at its cited line:** deps 2→6 (§1a README:19; pyproject:9 verified — fastapi, httpx2, jinja2, ouncemcp, python-multipart, uvicorn[standard]); routes 5→6 (§1a README:19; service.py's six decorators verified at :321/:350/:380/:417/:451/:490); tests 131→197 (§1a README:24; keisan's live run); web "banked"→built 2026-11-22 (§1a README:20; web.py 654 lines, nine routes, 14 templates + 2 statics); MCP "the ruled next effort"→live 2026-11-22 (§1a README:24; mcp_server.py 580 lines, the five OunceMCP tools); four→five tiers (§1a README:15); the eras current (§1a CONTINUATION:72-76) + the four drifts (:53 httpx2 main-table, :19 twelve wrappers, :65 the 654 cure, the era refresh); AGENTS' dead regen line cured (§1a — the hikari-side engine named). The honest lines all landed in the README's fence: the no-PyPI form (§2), the web-absence truth for the tool lane (§1a the wheel), the ruff-pending fact (§1d hyoka rank 2 — never claim the floor where only pyright rides), the hooksPath pointer's command (§1a the fresh-clone gaps), the port-collision note (§1a), the CWD law (§1a), .prioritree/ mints at runtime (§1a).
2. **The floor untouched-green:** the three files are prose — zero Python bytes touched; 197 stands (keisan's live run the record; the gate's own re-run the proof); pyright 0/0/0 and ruff zero findings unchanged by construction.
3. **The measured citation's path still resolving:** `.plans/ideation/2026-11-21-budget-curve/build/budget-curve-record.md` — tracked; the fence's citation line byte-identical to the current README:5, never excised.
4. **The Makefile/pyproject/docstrings untouched:** the fence holds — the README cites, never rewrites; service.py:44-45's fence-wording drift named for the collaborator (the polish class, unowned here — the approved brief's own note).

## 5. THE THREE-STEP PLAN (R8 — one file per dispatch, each step's completing act the report op, one commit per increment at the landing)

1. **README.md — one dispatch (the biggest single-file fence):** replace the file's whole content with §1's fence (patch the one mutation verb; the kept blocks byte-identical); the bounded return per step; the report op (R6/R11); one commit.
2. **CONTINUATION.md — one dispatch:** apply §2's hunks C1-C4 at their cited lines (the record otherwise untouched); the report op; one commit.
3. **AGENTS.md — one dispatch:** apply §3's hunk (the two header lines; the goal line untouched); the report op; one commit.
4. **The gate:** the floor — `make test` (197), `make lint` (zero findings), `make typecheck` (0/0/0): zero Python bytes touched, the floor unchanged by construction, the run the proof — + kensho's independent verification at validate/readme: every claim against the tree (deps 6 at pyproject:9, routes 6 at service.py, the five tiers, tests 197, the transcript's bytes at a live run — moho's bar: every documented command runs as written).

## 6. THE TRADE-OFF THE PLAN CARRIES

The README becomes a world-facing door on a tree whose vocabulary is internal: the ruled blocks (the Q-purpose blockquote's citation line, the measured record's tracked path) must SURVIVE the world-facing voice — the one evidence link kept resolving, never excised for cleanliness. And the tool-lane line names the web-absence truth THIS unit lands, knowing the install unit's packaging cure (ruling 4's call 2) will re-rule that same line — a named moving surface, honest at each landing, never a promise ahead of its truth. And the split that reconciles the two walks: moho's under-ten-lines vs keisan's nine-step floor — the Quickstart carries the first comparison, the Install lanes the whole honest sequence; neither walk sacrificed to the other. The AGENTS annotation rides the same trade: an in-tree cure on a cycle-generated file — honest the moment it lands, reconciled to the cycle only at the hikari-side re-emit the collaborator convenes.

— togo, the synthesis leg, read-only by design; this report is the one write. The spec whole (parts 1-3) closes G-READMESPEC-BRIEF's deliverable at the collaborator's approval.
