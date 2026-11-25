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

A fresh clone boots armed — the browser's first POST meets the key-path page until the operator mints a key AND wires it (`PRIORITYTREE_WEB_KEY` at the next boot, then `make restart`; both legs at [Auth](#auth)).

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
- **Web — built 2026-11-22.** Fronts the service: `src/prioritree/web.py` (820 lines, nine routes, 15 authored Jinja2 templates + 2 static files) over the in-process seam — the human comparator's vote surface at the browser.
- **MCP — live 2026-11-22.** The agent-callable tier: `src/prioritree/mcp_server.py` (645 lines, the five OunceMCP tools — `runs.register`, `runs.next`, `votes.cast`, `votes.census`, `runs.tally`; the `store_lock.py` flock seam), two run forms.

The auth doors live inside the service/web/mcp surfaces — not a sixth tier (see [Auth](#auth)).

Runtime dependencies: six — `fastapi`, `httpx2`, `jinja2`, `ouncemcp`, `python-multipart`, `uvicorn[standard]` (`pyproject.toml`). The quality floor: 336 tests green, pyright clean, ruff clean.

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

| route | op | scope |
|---|---|---|
| `POST /runs` | register (201) | `register` |
| `GET /runs/{run_id}/next` | serve the next under-quorum pair | `next` |
| `POST /runs/{run_id}/votes` | cast one judgment | `cast` |
| `GET /runs/{run_id}/state` | the census | `state` |
| `GET /runs/{run_id}/tally` | the ranked whole | `tally` |
| `GET /runs/{run_id}/manifest` | the run's manifest | `manifest` |

Every route reads the `X-Api-Key` header; the refusals are the three-part form (see [Auth](#auth)).

### Web

The lifecycle targets — `make start`, `make stop`, `make status`, `make restart` (`PORT ?= 8000`, `HOST ?= 127.0.0.1`; override: `make start PORT=8100`). The browser at `http://127.0.0.1:8000/`: register a list, vote the served pairs, read the ranked whole.

The browser is key-free by design (the tier's own server-side key — every judge one voice); the CSRF rides invisibly, a stale token's cure the reload (see [Auth](#auth)).

### MCP

Two run forms:

```console
$ uv run python -m prioritree.mcp_server           # stdio, per session — the MCP host boots it
$ uv run python -m prioritree.mcp_server --serve    # streamable-HTTP at http://127.0.0.1:8100
```

Port note: `--serve` defaults to port 8100 (`--host`/`--port` override); the web tier keeps 8000, so both servers co-run at their defaults — the collision is retired. The MCP's lifecycle targets: `make mcp-start`, `make mcp-stop`, `make mcp-status`, `make mcp-restart` (`MCP_PORT ?= 8100`, `MCP_HOST ?= 127.0.0.1`).

The two forms differ in trust: stdio is the local user's trust (the spawn IS the credential — the stamps self-claims); `--serve` is the bearer door. A tool absent from your list refuses as absent — check your key's scopes, not the server; the wrong-token 401's reconnect text is the substrate's own (the mint the only acquisition) (see [Auth](#auth)).

## Auth

A fresh clone boots armed: `AUTH ?= on` (Makefile:7) and no key store — every wire door answers 401, and the browser's first POST meets the key-path page. The first 401 is the design, not a bug. The boot marker lands in `.prioritree/server.log` (the service) and `.prioritree/mcp-server.log` (the mcp tier); the doors live inside the service/web/mcp surfaces, not a sixth tier.

### The doors

One mint ceremony, one store, two doors. The mint (the plaintext shown ONCE — only the sha256 hexdigest rides the file; mode 0600):

```console
$ prioritree key mint alice --class human --scopes register,state,tally,manifest --audience service
key	{the live mint's 43-char token_urlsafe(32) — shown once, never written}
digest	{the live mint's 64-hex sha256 — the only form at rest}
mode	0600
```

The store lands at `.prioritree/keys.jsonl`, CWD-relative — run the mint from the repo root, or pass `--home` matching the marker's absolute path (see [Discipline](#discipline)). The marker's three states (key_store.py:596-600), pasted from a live boot:

- armed + minted: `auth: on | keys: {home} | count: {N}`
- armed + no store: `auth: on (failopen -- no key store) | keys: {home} | next-action: prioritree key mint` — the LOAD fails open (the boot survives), the DOORS fail closed (every request 401s until a mint lands)
- the degrade: `auth: off (operator's explicit degrade) | keys: {home} | count: {N}` — the stamps fall back to the body's self-claims; the degrade is never a lockout

A typo'd AUTH refuses loudly at boot — expected `AUTH one of on|off (or unset)`, found the value verbatim, next-action the fix-and-reboot; the boot dies honestly (key_store.py:554-578).

The carry, three lanes: the service wire reads the `X-Api-Key` header (key_verify.py:32); the browser rides the env — `PRIORITYTREE_WEB_KEY` at the NEXT boot, then `make restart` (the mint alone cures nothing at the browser: the 401's next_action names the mint, never the wiring; the boot log's `web tier key: present|absent (a six-token grant)` line is the wiring's evidence, web.py:239-241); the mcp `--serve` door reads the bearer — `Authorization: Bearer {key}`; the X-Api-Key header never rides at that door (mcp_auth.py:37-39).

The audience pair {service, mcp} (key_store.py:53): one key form, two doors, one store — a key is dead at its non-audience, indistinguishably from unknown (the wrong-audience 401 is the SAME form; the identity oracle never fed). The mint validates scopes and audience separately, never the combination.

The web tier's own key — the skeleton key, named honestly: minted with the six-token grant (`--scopes register,next,cast,state,tally,manifest`); its leak is every human's writes — single-point, the design's named price.

The comparator's chain — the header at the doors, the class stamped from the KEY, never the body:

```console
$ curl -H "X-Api-Key: {key}" http://127.0.0.1:8000/runs/RUN-0001/next
{"item_a":"aloe","item_b":"basil","count":0}
```

Keyless — the 401's three-part body (the digest miss, the unknown key, and the wrong-audience key all render the SAME form):

```json
{"expected":"the key in the X-Api-Key header","found":"absent-or-unknown","next_action":"mint a key: prioritree key mint <comparator-id> --class <human|llm> --scopes <csv> --audience <tier>"}
```

Wrong scope — the 403's (the re-mint taught):

```json
{"expected":"the next scope","found":"the key's scopes ['manifest', 'register', 'state', 'tally']","next_action":"re-mint with the scope: prioritree key mint ... --scopes <csv>+next"}
```

The llm comparator rides the SAME ceremony — `prioritree key mint claude --class llm --scopes next,cast,manifest --audience service` — and the door stamps the key's class over any body's claim (an llm key over a body claiming human stamps llm; the corroboration floor needs exactly this). The grant map is data, default-deny (policy.py:41-47): the mints' `--scopes` arguments above ARE the map's rows; a scope absent from the mint is a door that 403s.

The corroboration floor, told up front (policy.py:69-89 — the standing policy every run declares by being a prioritree run; tally.py:534-548 — the gate): every pair needs >=1 human AND >=1 llm vote at the tally. Where it bites: the tally gate. Which voices count: the key's class. Where the second class rides: the operator's llm-class key at the service/MCP tier (the browser has no llm lane).

The browser's chain: `open http://127.0.0.1:8000/` — key-free by design (the tier key invisible by construction); the CSRF met only as the reload cure (`expected: the form's csrf_token field (minted into the served page) | found: absent-or-mismatched | next_action: reload the page and re-send — the re-render mints a fresh token`); the 401/403 lanes render the service's own three fields at the honest statuses, under the headings "The service asked for a key" / "The key lacks this act's scope" — never the crash page's clothes. Every browser judge is the web tier's ONE comparator: agreement between judges ACKs (the dedup), disagreement counts (a new record) — the other voices ride their own keys at the service/MCP tier.

The agent's chain: `uv run python -m prioritree.mcp_server --serve` + `Authorization: Bearer {key}`. The five-tool reach per the key's scopes (mcp_auth.py:86-94): `runs.register`→register, `runs.next`→next, `votes.cast`→cast, `votes.census`→state, `runs.tally`→tally — manifest has NO mcp tool (the service tier's sixth route alone; a manifest-only mcp key opens nothing). The wrong-token 401's body is the substrate's own canned OAuth text — "clear authentication tokens in your MCP client and reconnect. Your client should automatically re-register and obtain new tokens" — the reconnect mints nothing; the mint is the only acquisition. A tool absent from your list refuses as absent; check your key's scopes, not the server. Over stdio the spawn IS the credential — all five tools ungated, the stamps the body's self-claims (the local trust; `--serve` and the service wire are the verified forms).

The knobs, at their ?= forms (the configurability law — every name a knob from birth):

- `AUTH ?= on` (Makefile:7) — on|off|unset→on; a typo refuses loudly at boot
- `PRIORITYTREE_WEB_KEY ?=` (Makefile:8) — the browser lane's wiring, read once at boot (web.py:232-238); the boot log line `web tier key: present|absent (a six-token grant)`
- `PRIORITYTREE_KEYS_HOME` (key_store.py:45-48) — the store's home, resolved absolute at both doors; an empty override falls back to the default
- `PRIORITYTREE_WEB_CSRF_SECRET` (web.py:113-116) — unset means a boot-minted random; a restart invalidates outstanding tokens (the reload the cure); one secret across workers
- the header `X-Api-Key` at the service door (key_verify.py:32); the bearer grammar at the mcp door (mcp_auth.py:37-39); `--host`/`--port` at `--serve`

### Remains trust

> **THE AUTH CURES THE WIRE; THE DISK AND THE LOCAL MACHINE REMAIN TRUST**
>
> — the design's honest statement, carried verbatim (`.plans/ideation/2026-11-24-prioritree-auth/reports/synthesize/auth-design.md` §3)

- The cleartext store: hashed-at-rest guards the KEY, never the DATA — the runs' JSONL carries operator ids, questions, comparator ids, notes naked on disk.
- The local process's reach: the key fences the socket, not the filesystem — every local process owns every surface.
- The offline JSONL edit: the checks live at the wire; the seam lives on disk.
- The issuance's honesty: the operator mints honestly — the operational trust itself.
- The browser's unbound id: the form's self-claim behind the tier key — the door stamps the web key's id.
- The stdio self-claims: stdio is the local user's trust; `--serve` and the service wire are the verified forms.
- The hide's teaching loss: the unauthorized agent cannot tell broken-server from unauthorized-self.
- The quantities: the policy grants verbs, never quantities — owned by the tally-policy lane, never silent.

### Why the choices hold

The llm-class constraint, told plainly: the llm's key is the SAME mint ceremony (`--class llm`, one form for both classes), the vote scope granted (the comparator's row: next, cast, manifest), no human-approval gate anywhere — the llm is a first-class comparator, not an exception; the corroboration floor needs exactly this.

The alternatives were priced and refused — the prices cited to the record (auth-design.md §1), never re-derived here: JWT (9.1x-36.4x the wire, the second secret's custody, the downgrade class); the secret manager ($28.80/yr + the credential chain widening the exposure it guards); OAuth (the consent ceremony kills the llm ride). The file earned its place: one file (`.prioritree/keys.jsonl`), one machine's filesystem, one process's in-memory dict, the machine-wide flock.

When this stops being true — the threshold: past <=8 operators, past the single machine, into multi-tenancy, the file's earn ends and the banked machinery begins — JWT at the multi-machine wire, the secret manager at the fleet, OAuth at the external authority. The triggers named, the prices standing at the design's record (auth-design.md §3) — never silent, never copied here.

## Input/Output Examples

One run whole — a list in, three human votes, the corroboration halt, the llm's votes, the tally out (a fresh store; every byte as the tree emits it):

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
refused — expected: the coverage gate met: no zero-coverage item, the comparison graph connected, every pair at quorum k=1 AND corroborated (>=1 human AND >=1 llm per pair) | found: uncorroborated pairs: (aloe, basil) missing llm, (aloe, cilantro) missing llm, (basil, cilantro) missing llm | next: cast the corroborating votes: (aloe, basil) needs llm, (aloe, cilantro) needs llm, (basil, cilantro) needs llm — corroboration needs votes from BOTH CLASSES on existing pairs
$ prioritree vote RUN-0001 aloe basil prefer-a claude llm
vote	VOTE-0004	4
$ prioritree vote RUN-0001 aloe cilantro prefer-b claude llm
vote	VOTE-0005	5
$ prioritree vote RUN-0001 basil cilantro prefer-b claude llm
vote	VOTE-0006	6
$ prioritree state RUN-0001
votes	6
item	aloe	4
item	basil	4
item	cilantro	4
$ prioritree tally RUN-0001
rank	cilantro
rank	aloe
rank	basil
counts	aloe	2	2	0
counts	basil	0	4	0
counts	cilantro	4	0	0
coverage	1	True
pairs	aloe	basil	2
pairs	aloe	cilantro	2
pairs	basil	cilantro	2
version	win-rate-v1
```

Reading the lines:

- `register` prints the bare run id — `RUN-0001`, the file stem of `.prioritree/runs/RUN-0001.jsonl`.
- `next` prints `pair`, the two ids, the votes already on the pair; the queue is the id-sorted pairwise schedule; at exhaustion it prints the DONE message instead (exit 0).
- `vote` prints `vote` (a new cast) or `ack` (a byte-identical re-cast — the dedup), the vote id, and the run's whole vote count.
- `state` prints `votes` (the total) then one `item` line per item — the votes the item appeared in.
- `tally` prints the ranked whole — or refuses first: the corroboration floor (every pair >=1 human AND >=1 llm, the standing policy) SAFE HALTs the tally with the three-part form until both classes sit; the llm's votes land on the existing pairs (the queue's exhaustion never blocks a direct cast); the second `tally` prints the ranked whole: one `rank` line per tie group, `counts` (wins, losses, ties) per item, `coverage` (the graph's components, done), a `cycle` line only when a Condorcet cycle exists, `pairs` (the weighted per-pair counts), and `version`.

## Discipline

- **The CWD law.** The stores (`.prioritree/runs`, `.prioritree/keys.jsonl`) resolve CWD-relative — run from the repo root, or your data lands where you stood (the directories mint silently on demand); the CLI's `--home` is the per-invocation escape — the key mint included: a mint from another cwd lands in a store no door reads (the marker names the absolute home; pass `--home` matching it). The web homes resolve in order: the CWD's `web/templates` + `web/static` first (the repo's authored files — the clone's form), the installed package's copies the fallback — a wrong cwd in the clone folds honestly (the honest 500); an installed location always renders.
- **The git hook.** `.githooks/pre-commit` is tracked, but the pointer never clones — set it by hand: `git config core.hooksPath .githooks`. The hook enforces the whole floor locally — ruff + pyright on staged .py at the site the code is written; CI checks the same floor at the push. `PRIORITREE_HOOK_BYPASS=1` is the tracked bypass.
- **The port discipline.** The web tier (`make start`) defaults to port 8000; the MCP (`--serve`) defaults to 8100 — both servers co-run at their defaults, the collision retired (the MCP's lifecycle: `make mcp-start` / `make mcp-stop` / `make mcp-status` / `make mcp-restart`).
- **`.prioritree/` mints at runtime** — the server pid and log, the runs store, the keys store; gitignored, never present in a clone.

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

Born 2026-11-19 (the setup). The core library built 2026-11-20; the CLI built 2026-11-21; the claim measured 2026-11-21 (pairs + tally beats absolute sizing at equal budget — 51 of 54 in-band cells); the service live 2026-11-21; the web app built 2026-11-22; the MCP tier live 2026-11-22 (the five OunceMCP tools); the auth landed 2026-11-24 (the key store, the grant map, the six doors, the mcp bearer door, the corroboration floor — [Auth](#auth)). CI is live (2026-11-23): the CI workflow (.github/workflows/ci.yml) runs the quality floor — ruff, pytest, pyright — at every push to main and weekly, and CodeQL scans under the tree's own config (.github/codeql/codeql-config.yml); the loop's lands ride direct pushes to main and the workflow runs green at each push — the PR form has no grammar here; the git hook stays the local backstop. The quality floor: 336 tests green, pyright clean, ruff clean.

## License

MIT — the [LICENSE](LICENSE) file at the repo root (Copyright (c) 2026 Mark Losey); `pyproject.toml` carries `license = "MIT"`.
