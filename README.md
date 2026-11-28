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

The browser is the human comparator's surface: register a list, vote the served pairs (identifying once at the first judgment — the browser remembers the name), read the ranked whole (see [Multi-user](#multi-user)).

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

Then serve and vote the remaining pairs the same way; at quorum AND corroboration on every pair the tally emits the ranked whole — the full transcript: [Input/Output Examples](#inputoutput-examples).

## Architecture

Five tiers, one layered architecture, library-first:

- **Library — `src/prioritree` — built 2026-11-20.** The pure-logic core at the bottom of the stack: items, the comparison operator, pair scheduling, votes, tally — the tally a pure function of the stored votes. State is file-backed JSONL (no database).
- **CLI — built 2026-11-21.** Wraps the core: the five-op surface at the command line (register → next → vote → state → tally), the `prioritree` console script.
- **Service (FastAPI) — live 2026-11-21.** Serves the core over HTTP: six routes (the five ops 1:1 + the manifest query), one process-wide lock seam, every error body the three-part form (expected / found / next-action).
- **Web — built 2026-11-22.** Fronts the service: `src/prioritree/web.py` (1341 lines, twelve lanes, 17 authored Jinja2 templates + 2 static files) over the in-process seam — the human comparator's vote surface at the browser.
- **MCP — live 2026-11-22.** The agent-callable tier: `src/prioritree/mcp_server.py` (685 lines, the five OunceMCP tools — `runs.register`, `runs.next`, `votes.cast`, `votes.census`, `runs.tally`; the `store_lock.py` flock seam), two run forms.

The auth doors live inside the service/web/mcp surfaces — not a sixth tier (see [Auth](#auth)).

Runtime dependencies: seven — `fastapi`, `httpx2`, `itsdangerous`, `jinja2`, `ouncemcp`, `python-multipart`, `uvicorn[standard]` (`pyproject.toml`). The quality floor: 490 tests green, pyright clean, ruff clean.

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
| `GET /runs/{run_id}/next` | serve the next open pair (under-quorum or uncorroborated) | `next` |
| `POST /runs/{run_id}/votes` | cast one judgment | `cast` |
| `GET /runs/{run_id}/state` | the census | `state` |
| `GET /runs/{run_id}/tally` | the ranked whole | `tally` |
| `GET /runs/{run_id}/manifest` | the run's manifest | `manifest` |

Every route reads the `X-Api-Key` header; the refusals are the three-part form (see [Auth](#auth)).

### Web

The lifecycle targets — `make start`, `make stop`, `make status`, `make restart` (`PORT ?= 8000`, `HOST ?= 127.0.0.1`; override: `make start PORT=8100`). The browser at `http://127.0.0.1:8000/`: register a list, vote the served pairs, read the ranked whole.

The browser is key-free by design (the tier's own server-side key — each browser its own voter, the name asked once and remembered); the CSRF rides invisibly, a stale token's cure the reload, a lapsed identification's cure the same reload — the page re-asks the name (see [Auth](#auth), [Multi-user](#multi-user)).

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

The store lands at `.prioritree/keys.jsonl`, CWD-relative — run the mint from the repo root, or pass `--home` matching the marker's absolute path (see [Discipline](#discipline)). The marker's three states (key_store.py:601-605), pasted from a live boot:

- armed + minted: `auth: on | keys: {home} | count: {N}`
- armed + no store: `auth: on (load fail-open; doors fail-closed) | keys: {home} | next-action: prioritree key mint` — the LOAD fails open (the boot survives), the DOORS fail closed (every request 401s until a mint lands)
- the degrade: `auth: off (operator's explicit degrade) | keys: {home} | count: {N}` — the stamps fall back to the body's self-claims; the degrade is never a lockout

A typo'd AUTH refuses loudly at boot — expected `AUTH one of on|off (or unset)`, found the value verbatim, next-action the fix-and-reboot; the boot dies honestly (key_store.py:557-581).

The carry, three lanes: the service wire reads the `X-Api-Key` header (key_verify.py:32); the browser rides the env — `PRIORITYTREE_WEB_KEY` at the NEXT boot, then `make restart` (the mint alone cures nothing at the browser: the 401's next_action names the mint, never the wiring; the boot log's `web tier key: present|absent (expected: the six-token grant)` line is the wiring's evidence — the absent arm names the wiring at the next boot, web.py:396-400); the mcp `--serve` door reads the bearer — `Authorization: Bearer {key}`; the X-Api-Key header never rides at that door (mcp_auth.py:37-39).

The audience pair {service, mcp} (key_store.py:53): one key form, two doors, one store — a key is dead at its non-audience, indistinguishably from unknown (the wrong-audience 401 is the SAME form; the identity oracle never fed). The mint validates scopes and audience separately, never the combination.

The web tier's own key — the skeleton key, named honestly: minted with the six-token grant (`--scopes register,next,cast,state,tally,manifest`); its leak is every human's writes — single-point, the design's named price, grown one notch by the session's seam: the key's holder can vote as any remembered name at the web lane alone (id forgery at that lane — priced at the loopback's no-new-reach: the class that holds the key can already vote directly; the key's custody the guard).

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

The corroboration floor, told up front (policy.py:69-89 — the standing policy every run declares by being a prioritree run; tally.py:512-546 — the gate): every pair needs >=1 human AND >=1 llm vote at the tally. Where it bites: the tally gate. Which voices count: the key's class. Where the second class rides: the operator's llm-class key at the service/MCP tier (the browser has no llm lane).

The browser's chain: `open http://127.0.0.1:8000/` — key-free by design (the tier key invisible by construction); the CSRF met as the two taught cures (`expected: the form's csrf_token field (minted into the served page) | found: absent-or-mismatched | next_action: reload the page and re-send — the re-render mints a fresh token` — the live-session copy, web.py:284; the lapsed identification teaches `your identification lapsed — reload, the page re-asks your name`, web.py:286); the 401/403 lanes render the service's own three fields at the honest statuses, under the headings "The service asked for a key" / "The key lacks this act's scope" — never the crash page's clothes. Each browser is its own voter at the web tier: the same browser's re-send ACKs (the dedup), two browsers land two ids (two records — the duplication visible, the depth inflation named honestly); the other voices ride their own keys at the service/MCP tier.

The agent's chain: `uv run python -m prioritree.mcp_server --serve` + `Authorization: Bearer {key}`. The five-tool reach per the key's scopes (mcp_auth.py:86-94): `runs.register`→register, `runs.next`→next, `votes.cast`→cast, `votes.census`→state, `runs.tally`→tally — manifest has NO mcp tool (the service tier's sixth route alone; a manifest-only mcp key opens nothing). The wrong-token 401's body is the substrate's own canned OAuth text — "clear authentication tokens in your MCP client and reconnect. Your client should automatically re-register and obtain new tokens" — the reconnect mints nothing; the mint is the only acquisition. A tool absent from your list refuses as absent; check your key's scopes, not the server. Over stdio the spawn IS the credential — all five tools ungated, the stamps the body's self-claims (the local trust; `--serve` and the service wire are the verified forms).

The knobs, at their ?= forms (the configurability law — every name a knob from birth):

- `AUTH ?= on` (Makefile:7) — on|off|unset→on; a typo refuses loudly at boot
- `PRIORITYTREE_WEB_KEY ?=` (Makefile:8) — the browser lane's wiring, read once at boot (web.py:389); the boot log line `web tier key: present|absent (expected: the six-token grant)` — the absent arm names the wiring at the next boot
- `PRIORITYTREE_KEYS_HOME` (key_store.py:45-48) — the store's home, resolved absolute at both doors; an empty override falls back to the default
- `PRIORITYTREE_WEB_CSRF_SECRET` / `PRIORITYTREE_WEB_REMEMBER_SECRET` (web.py:126-127) — unset means a boot-minted 256-bit secret; a restart invalidates outstanding tokens and sessions (the reload and the re-ask the cures); one secret each across workers; an under-floor env secret refuses at import in the three-part form
- the header `X-Api-Key` at the service door (key_verify.py:32); the bearer grammar at the mcp door (mcp_auth.py:37-39); `--host`/`--port` at `--serve`

### Remains trust

> **THE AUTH CURES THE WIRE; THE DISK AND THE LOCAL MACHINE REMAIN TRUST**
>
> — the design's honest statement, carried verbatim (`.plans/ideation/2026-11-24-prioritree-auth/reports/synthesize/auth-design.md` §3)

- The cleartext store: hashed-at-rest guards the KEY, never the DATA — the runs' JSONL carries operator ids, questions, comparator ids, notes naked on disk.
- The local process's reach: the key fences the socket, not the filesystem — every local process owns every surface.
- The offline JSONL edit: the checks live at the wire; the seam lives on disk.
- The issuance's honesty: the operator mints honestly — the operational trust itself.
- The browser's remembered id: narrowed, never erased — the session's self-claim carried across the tier key's door from the web lane alone (service.py:586-587), persistent never verified; the class still the key's, stamped over any body's claim.
- The stdio self-claims: stdio is the local user's trust; `--serve` and the service wire are the verified forms.
- The hide's teaching loss: the unauthorized agent cannot tell broken-server from unauthorized-self.
- The quantities: the policy grants verbs, never quantities — owned by the tally-policy lane, never silent.

### Why the choices hold

The llm-class constraint, told plainly: the llm's key is the SAME mint ceremony (`--class llm`, one form for both classes), the vote scope granted (the comparator's row: next, cast, manifest), no human-approval gate anywhere — the llm is a first-class comparator, not an exception; the corroboration floor needs exactly this.

The alternatives were priced and refused — the prices cited to the record (auth-design.md §1), never re-derived here: JWT (9.1x-36.4x the wire, the second secret's custody, the downgrade class); the secret manager ($28.80/yr + the credential chain widening the exposure it guards); OAuth (the consent ceremony kills the llm ride). The file earned its place: one file (`.prioritree/keys.jsonl`), one machine's filesystem, one process's in-memory dict, the machine-wide flock.

When this stops being true — the threshold: past <=8 operators, past the single machine, into multi-tenancy, the file's earn ends and the banked machinery begins — JWT at the multi-machine wire, the secret manager at the fleet, OAuth at the external authority. The triggers named, the prices standing at the design's record (auth-design.md §3) — never silent, never copied here.

## Multi-user

The browser remembers the judge — `Your name is asked once — the site remembers your entry for every judgment you cast from this device.` The ask lives inside the vote form at the first judgment, never a separate gate; the cookie named `remember` carries the name across every page load (itsdangerous-signed, 14 days by default). Every render shows `voting as: <name>` — one visible line closes three stumbles: the cookie-swap is seen at the next render, the typo is seen and not just remembered, the shared machine's bleed is seen.

Each browser is its own voter. A fresh browser asks again — the expiry taught in the human's words, `your identification lapsed — reload the page, it re-asks your name`, never the schema's. Two browsers land two voters, the ids distinct at the record, the duplication visible never hidden; two humans on one browser merge into one voter. The tally counts votes, never minds. The register's operator field arrives pre-filled from the remembered name — a visible editable value; the claim always rides the body. The shareable URL stays shareable: anonymous reads unchanged, each judge identifies once at their own browser.

Two roles, named honestly. WHO — the name is yours: a self-claim, persistent, never verified (no account, no secret; k fabrications are still k identifications). WHAT CLASS — the key's verified stamp, never the browser's to claim at any door: the session is the humans' lane, the llm votes ride unchanged at the stdio/tools tier on the mcp audience's keys. The id-binding is narrowed, never erased — the remembered self-claim crosses the verified door from the web lane alone (service.py:586-587), persistent never verified; the record says what it knows and what it merely carries.

> **THE SESSION CURES THE UX COST, NEVER THE IDENTITY FABRICATION**
>
> — the design's honest statement, carried verbatim (`.plans/ideation/2026-11-26-prioritree-multi-user/reports/synthesize/multi-user-design.md` §3)

The statement's whole, compact: the record's identity is a browser's self-claim, persistent and pinned, never verified; the corroboration story's strength lives at the class axis (the key's verified stamp), never at the id axis (the self-claim). The browser binding — each browser its own voter: multi-browser-per-human splits one human into k voters, multi-human-per-browser merges many into one. The readable payload — the name's bytes client-side in the cookie, tamper-cured, readable by the holder. The verdict at this bind: UX-first, security-second — the loopback keeps the remote classes dead and the local class already owns the machine; the session's security value prices in at the LAN rebind era. The auth precedent's parallel: the auth cures the wire — the session cures the ceremony; the identity's honesty remains the human's own.

The correction verbs, one affordance (`not you? change your name or un-remember this device`, sitting.html:10). Change — the re-identification rotates the CSRF epoch; the old tabs' tokens die, the reload the cure (`reload the page and re-send — the re-render mints a fresh token`). Un-remember — the engine's deletion cookie (`remember=null; expires=Thu, 01 Jan 1970`, no max-age, web.py:1317-1341): it clears this browser's cookie, never a server kill — a stolen cookie elsewhere rides to the max-age or the secret's rotation.

The knobs, at their env forms (the configurability law — every knob from birth):

- `PRIORITYTREE_WEB_REMEMBER_SECRET` / `PRIORITYTREE_WEB_CSRF_SECRET` (web.py:126-127) — unset means a boot-minted 256-bit secret; a restart invalidates outstanding sessions and tokens (the re-ask and the reload the cures); an under-floor env secret refuses at import in the three-part form — a weak secret weakens every artifact it signs.
- The 14-day `max_age` — the 780-s card covered 1550×; the price a 14-day stolen-cookie window. `SameSite=lax` — the shareable URL's top-level entry preserved; `HttpOnly` hardcoded at the engine, never a knob.

The era order, told compact: this session was born mid-probe — the order-bias probe's completion card met the per-operation identification and was abandoned at the first sitting (0 of 78; the datum deferred at 241 of 312); the collaborator's governance overrule convened the full-team cycle (research → evaluation → recommendation → the design), the session landed at the floor 475 — and the datum was served: RUN-0008 completed at 319 votes, the null standing at its realized bound |θ−0.5| ≲ ±0.192, never "no bias". The records resolve to the two stores: the datum at `.plans/ideation/2026-11-24-order-bias-probe/` (reports/measure/probe.md; reports/close/records.md), this effort's whole at `.plans/ideation/2026-11-26-prioritree-multi-user/`.

## Journey

The journey's story opens with the record's own honesty, never an error: the convening remembered the form as "two choices, click a button to choose, click a submit button to send the decision" — the tree's real form had the verdict buttons as the submits all along, one click casting since 2026-11-22 (RUN-0008's 319 votes the live proof — 163 cast at the browser's one-click form, 156 at the tools lane). The claims lane caught the mismatch; the effort's ground was amended to the tree's real form, never the remembered one. The simplification's true product is the semantics: the option card itself the click target, the marker translation ("Prefer A" -> the left card -> river) dead.

The card: two option cards, each a submit button inside the standing form (`pair.html`) — the badge and the full label the button's own content, the click the cast, the wire unchanged (the same POST, the same stamps, the corroboration floor untouched). The comparison operator `vs` rides between the options — display-only, never focusable, the tab flow skipping it (the picker's own precedent). The tie rides subordinate under the two cards — "Tie — both stand equal" — the declared set's own loop member at the 24px minimum target; a run declaring two verdicts renders none.

The undo rides the ack. "Clicked the wrong one?" — the correction taught at the mistake's own mirror, the ack line restating the pair and the verdict in label terms first. The undo re-serves the just-judged pair as presented, carrying the supersede; the corrected click lands a new record citing the old — both records stay in the log, never erased (append-only; no delete verb exists), the tally walking the link: the superseded excluded, the correction counted (RUN-0010: 7 records, 6 counted). The bound named honestly: the window is same-sitting — it ends when the card leaves, the done page carrying no undo; the durable cross-sitting correction is the tools lanes' own.

The accessibility rides, told plainly: the ack region carries `aria-live="polite"` — the swap's content announced at both lanes by construction; the option ids are pair-stable (`cast-a`, `cast-b`, `cast-tie`) at every serve, htmx's focus restoration keying on the ids — the focus survives the two swaps at zero JavaScript; the fieldset/legend binds the question at every serve, the reader hearing the group, never bare buttons; the accessible names the full labels; the touch targets at the 24px floor, the 12px adjacency the named price.

The llm-class divergence, named honestly: the one-click journey is the browser lane's story. The CLI and the tools lanes keep their own UX weight — zero bytes changed at `cli.py`/`mcp_server.py`, the tools' ack bare (the vote id and the count). The wire's law is the only sameness: the same vote, the same stamps, the same supersedes — the CLI's `--supersedes` the cross-sitting correction's home.

The acknowledged residual, named never hidden: the flag's live divergence is twice-observed (RUN-0009 and RUN-0010 — a dedup-proven re-send read `acknowledged: false` at the live tools lane, while the tree's bytes thread `True` at every layer, test-pinned through the web route). The cause is a hypothesis — the connected server's build versus the tree's bytes — the outward lane's own diagnosis.

> **THE JOURNEY SIMPLIFICATION CURES THE CHOICE'S SEMANTICS; THE ASKS, THE LANES, AND THE CORRECTION'S WINDOW KEEP THEIR OWN WEIGHT**
>
> — the design's honest statement, carried verbatim (`.plans/ideation/2026-11-27-prioritree-journey/reports/synthesize/journey-design.md` §3)

At the landed truth — CURES: the translation dead (the card is the choice); the operator present between the options; the correction live at the browser lane; the true 302 at the re-opened done edge (the plain browser arrives whole); the undo's re-serve the correction's path (one click, never a reload); the quorum label's 16 words; the aria-live and the focus at the ack; the conftest (the single-module test runs green). CARRIES: the deliberate lane's 3 clicks per judgment; the register's asks whole (the merge banked, never landed); the picker's wall (the link banked, never landed); the append-only law. OPENS: the same-sitting bound; the lanes' UX divergence; the tie's rarity (0 of 319 at the live record — the walk its only school); the acknowledged seam.

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

**`uv tool install .` — the tool lane.** Installs the `prioritree` console script and its seven dependencies — the five CLI ops run from any directory. State is per-project by design: the store mints at `.prioritree/runs` under your CWD; `--home` redirects. The web tier rides this lane too: the wheel ships the templates and static files as package data, and the web homes resolve them from the installed package. Serve the web with the tool env's uvicorn — `$(uv tool dir)/prioritree/bin/uvicorn prioritree.service:app` (any directory; the store mints where you stood). The MCP rides the same install: `$(uv tool dir)/prioritree/bin/python -m prioritree.mcp_server` for stdio, or the same command with `--serve` (port 8100 — co-runnable with the web's 8000).

**Not on PyPI.** `uv tool install prioritree` and `pip install prioritree` do not resolve — Priori-tree is not published. The publish is deferred: the license, the packaging, and CI have landed; the publish itself remains the outward lane's ruled act.

## Status

Born 2026-11-19 (the setup). The core library built 2026-11-20; the CLI built 2026-11-21; the claim measured 2026-11-21 (pairs + tally beats absolute sizing at equal budget — 51 of 54 in-band cells); the service live 2026-11-21; the web app built 2026-11-22; the MCP tier live 2026-11-22 (the five OunceMCP tools); the auth landed 2026-11-24 (the key store, the grant map, the six doors, the mcp bearer door, the corroboration floor — [Auth](#auth)); the order-bias question measured 2026-11-26 (the presented order's bias over the tree's own stamped votes: the flips real — 26 of 155 classifiable cells flipped on the swap; the direction's asymmetry unestablished at the realized m — THE NULL AT ITS BOUND |θ−0.5| ≲ ±0.192, never "no bias"; the record at `.plans/ideation/2026-11-24-order-bias-probe/`); the voter session landed 2026-11-26 (identify once per browser — each browser its own voter, the class still the key's; born mid-probe at the measured refusal, RUN-0008's datum served at 319 — [Multi-user](#multi-user)); the journey landed 2026-11-27 (the one-click card — the option itself the choice, the operator `vs` between, the tie subordinate; the undo at the ack, both records in the log; the bridge's cures — the done-page 302, the re-cast copy (the reload teaching retired by the undo's re-serve), the conftest, the quorum's 16 words — [Journey](#journey)). CI is live (2026-11-23): the CI workflow (.github/workflows/ci.yml) runs the quality floor — ruff, pytest, pyright — at every push to main and weekly, and CodeQL scans under the tree's own config (.github/codeql/codeql-config.yml); the loop's lands ride direct pushes to main and the workflow runs green at each push — the PR form has no grammar here; the git hook stays the local backstop. The quality floor: 490 tests green, pyright clean, ruff clean.

## License

MIT — the [LICENSE](LICENSE) file at the repo root (Copyright (c) 2026 Mark Losey); `pyproject.toml` carries `license = "MIT"`.
