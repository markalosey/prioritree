# Priori-tree

Priori-tree is a generalized prioritization system: for any list and comparison operator, run the pairwise permutations, store the votes, tally — the output list is in a superior order than sizing individual items, because discernment between two items is easy (for humans and LLMs) while absolute sizing is not.

Measured (2026-11-21): pairs + tally beats absolute sizing at equal budget in 51 of 54 in-band cells (94.4%; the 3 exceptions narrow and seed-local) — the record at `.plans/ideation/2026-11-21-budget-curve/build/budget-curve-record.md`.

The comparator class is both human AND LLM — both vote through the same vote interface; the tally is a pure function of the stored votes.

> Priori-tree is a generalized prioritization system based on the concept that LLM and Humans are great at discerning the difference between two items but not great at sizing an item. That is a simplification. Consider: a human is great at determining that a basketball is larger than a grapefruit. But not great as identifying the exact dimensions of a grapefruit or a basketball. By taking a list and running through the pairwise permutations for any given comparision operator. Storing the votes, then tallying. we get a list out that is in a superior order than trying to size individual items.
>
> — the collaborator's Q-purpose ruling, 2026-11-19 (verbatim)

License: MIT — the [LICENSE](LICENSE) file at the repo root (Copyright (c) 2026 Mark Losey).

[HUMAN.md](HUMAN.md) — the only human-written thing in this repository; everything else is generated.

## Quickstart

The first comparison, end-to-end, from a fresh clone. Requirements: Python 3.13+ and uv. Run every command from the repo root (see [Discipline](#discipline)):

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

Runtime dependencies: six — `fastapi`, `httpx2`, `jinja2`, `ouncemcp`, `python-multipart`, `uvicorn[standard]` (`pyproject.toml`). The quality floor: 203 tests green, pyright clean, ruff clean.

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

- Both lanes speak the table's ops: `uv run prioritree <op> ...` at the repo root (the clone lane — `make dev`'s editable install); the bare `prioritree` form is the tool lane's (`uv tool install .`).
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
$ uv run python -m prioritree.mcp_server --serve    # streamable-HTTP at http://127.0.0.1:8100
```

Port note: `--serve` defaults to port 8100 (`--host`/`--port` override); the web tier keeps 8000, so both servers co-run at their defaults — the collision is retired. The MCP's lifecycle targets: `make mcp-start`, `make mcp-stop`, `make mcp-status`, `make mcp-restart` (`MCP_PORT ?= 8100`, `MCP_HOST ?= 127.0.0.1`).

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

- **The CWD law.** The store (`.prioritree/runs`) resolves CWD-relative — run from the repo root, or your data lands where you stood (the directory mints silently on demand); the CLI's `--home` is the per-invocation escape. The web homes resolve in order: the CWD's `web/templates` + `web/static` first (the repo's authored files — the clone's form), the installed package's copies the fallback — a wrong cwd in the clone folds honestly (the honest 500); an installed location always renders.
- **The git hook.** `.githooks/pre-commit` is tracked, but the pointer never clones — set it by hand: `git config core.hooksPath .githooks`. The hook enforces the whole floor locally — ruff + pyright on staged .py at the site the code is written; CI checks the same floor at the push. `PRIORITREE_HOOK_BYPASS=1` is the tracked bypass.
- **The port discipline.** The web tier (`make start`) defaults to port 8000; the MCP (`--serve`) defaults to 8100 — both servers co-run at their defaults, the collision retired (the MCP's lifecycle: `make mcp-start` / `make mcp-stop` / `make mcp-status` / `make mcp-restart`).
- **`.prioritree/` mints at runtime** — the server pid and log, the runs store; gitignored, never present in a clone.

## Install

**The clone — the source and the floor.** The web tier's templates and static files ride the repo (`web/`), the homes resolve at the root, and the tool lane below serves the same pages from the installed package. Requirements: Python 3.13+ and uv. The full honest sequence:

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

**`uv tool install .` — the tool lane.** Installs the `prioritree` console script and its six dependencies — the five CLI ops run from any directory. State is per-project by design: the store mints at `.prioritree/runs` under your CWD; `--home` redirects. The web tier rides this lane too: the wheel ships the templates and static files as package data, and the web homes resolve them from the installed package. Serve the web with the tool env's uvicorn — `$(uv tool dir)/prioritree/bin/uvicorn prioritree.service:app` (any directory; the store mints where you stood). The MCP rides the same install: `$(uv tool dir)/prioritree/bin/python -m prioritree.mcp_server` for stdio, or the same command with `--serve` (port 8100 — co-runnable with the web's 8000).

**Not on PyPI.** `uv tool install prioritree` and `pip install prioritree` do not resolve — Priori-tree is not published. The publish is deferred: the license, the packaging, and CI have landed; the publish itself remains the outward lane's ruled act.

## Status

Born 2026-11-19 (the setup). The core library built 2026-11-20; the CLI built 2026-11-21; the claim measured 2026-11-21 (pairs + tally beats absolute sizing at equal budget — 51 of 54 in-band cells); the service live 2026-11-21; the web app built 2026-11-22; the MCP tier live 2026-11-22 (the five OunceMCP tools). CI is live (2026-11-23): the CI workflow (.github/workflows/ci.yml) runs the quality floor — ruff, pytest, pyright — at every push to main and weekly, and CodeQL scans under the tree's own config (.github/codeql/codeql-config.yml); the loop's lands ride direct pushes to main and the workflow runs green at each push — the PR form has no grammar here; the git hook stays the local backstop. The quality floor: 203 tests green, pyright clean, ruff clean.

## License

MIT — the [LICENSE](LICENSE) file at the repo root (Copyright (c) 2026 Mark Losey); `pyproject.toml` carries `license = "MIT"`.
