<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/readmepublicstoryspec

**Route:** prioritree-auth (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-25T02:23:56Z |
| 2 | report | togo | 2026-11-25T02:33:18Z |
## Reported by togo — 2026-11-25T02:33:18Z

# THE README-PUBLIC-STORY EXACT-TASK SPEC — togo's fenced bytes (synthesize/readmepublicstoryspec, 2026-11-25)

THE GROUND READ WHOLE (the read-back): the approved unit brief (reports/synthesize/readme-public-story.md — G-README-PUBLIC-STORY-BRIEF green: the placement + the four movements, the dedicated blockquote, the four chains, the 5-cured/6-named split, the threshold form, the halt-then-cure transcript, NO README-fence test); tansa's census (reports/discover/readme-public-story.md — the 193-line README pinned, the stale numbers, the commands' exact forms, the citation map §4); rikai's maps (reports/understand/readme-public-story.md — the claims, the chains, the CURED/NAMED split, the threshold, the drift options); the design's §3 verbatim (reports/synthesize/auth-design.md:56-65) + the alternatives' record (§1 :44); README.md whole (the standing voice); the landed surfaces verified AT MY HAND (cli.py:198-216/:401-441; key_store.py:45-62/:455-508/:554-600; key_verify.py:29-44/:116-208; policy.py:33-89; service.py:105-107/:200-260/:263-286/:410-427; web.py:108-117/:228-241; mcp_auth.py:25-125; tally.py:122-150/:348-428/:475-548; the Makefile:3-8/:24-35/:83; tests/test_cli.py:41-118; tests/test_tally.py:353-461); the walks' live records (walk/serving-tier-integration.md — the 401/403 bytes, the browser lanes' headings, F1-F8; walk/mcp-verified-token.md — the halt walked live :45, M1-M4, the stdio ride). THE LIVE SURFACE RUN AT MY HAND: the suite whole — **336 passed in 32.78s** (the test tool's emission, 2026-11-25) — the floor's standing number, the no-break proof's base, the halt's and the frozen whole's byte-pinning arcs green inside that run; web.py read at 820 lines, mcp_server.py read at 645 lines (the tails at :820/:645). The spec below fences every byte the build lands; the README is prose but these bytes are the exact-task law.

## 1. THE SECTION'S PLACEMENT + THE FOUR MOVEMENTS' EXACT BYTES

### 1.0 The placement (the exact insertion point — the before/after bytes)

The "## Auth" head lands between the Usage section's MCP close (the port-note line, :110 today) and "## Input/Output Examples" (:112 today). The seam is pinned by its ANCHOR LINES, never by the line numbers (the insertions shift the file):

BEFORE (the bytes standing today):
```markdown
Port note: `--serve` defaults to port 8100 (`--host`/`--port` override); the web tier keeps 8000, so both servers co-run at their defaults — the collision is retired. The MCP's lifecycle targets: `make mcp-start`, `make mcp-stop`, `make mcp-status`, `make mcp-restart` (`MCP_PORT ?= 8100`, `MCP_HOST ?= 127.0.0.1`).

## Input/Output Examples
```
AFTER: the same two lines with the §1.1 region WHOLE between them (one blank line each side).

### 1.1 The section whole (the four movements — the bytes the build lands, verbatim)

````markdown
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
````

THE MOVEMENTS' BOUNDS (the brief's triptych, each movement's load): the LEAD = the armed boot + the marker's homes + not-a-sixth-tier; THE DOORS = the mint, the marker's three states, the typo, the carry's three lanes, the audience pair, the skeleton key, the comparator's 401/403 + the llm's same ceremony + the class stamping, the floor told up front, the browser's chain, the agent's chain, the knobs; REMAINS TRUST = §3's headline VERBATIM as the blockquote + the residuals ONE home; WHY THE CHOICES HOLD = the llm-class constraint, the alternatives' prices CITED NOT COPIED, the threshold paragraph. The mint's key/digest lines and the marker's {home}/{N} are the LIVE emission's own bytes (the builder's re-run the byte source, never a hand-typed line); the `mode	0600` line, the three marker templates, and every refusal body are byte-exact above.

## 2. THE SEAMS' EXACT BYTES (eight sites, each pointer-shaped — one line + the section's anchor; never a second telling)

**SEAM 1 — Quickstart (the load-bearing seam; the anchor: the browser line).** BEFORE: `The browser is the human comparator's surface: register a list, vote the served pairs, read the ranked whole.` then a blank line then `A first comparison at the command line instead (no server; from the repo root):`. AFTER (one line inserted between): `A fresh clone boots armed — the browser's first POST meets the key-path page until the operator mints a key AND wires it (`PRIORITYTREE_WEB_KEY` at the next boot, then `make restart`; both legs at [Auth](#auth)).`

**SEAM 2 — Architecture.** (a) the stale cures at the Web bullet and the MCP bullet (§3.1's fences); (b) one line after the five-tier list (after the MCP bullet, before `Runtime dependencies:`): `The auth doors live inside the service/web/mcp surfaces — not a sixth tier (see [Auth](#auth)).` BEFORE: `..., two run forms.` blank `Runtime dependencies: six — ...`. AFTER: `..., two run forms.` blank `The auth doors live inside the service/web/mcp surfaces — not a sixth tier (see [Auth](#auth)).` blank `Runtime dependencies: six — ...`.

**SEAM 3 — Usage-Service.** The route table gains the scope column; one line after the table. BEFORE: `| route | op |` / `|---|---|` / `| `POST /runs` | register (201) |` / `| `GET /runs/{run_id}/next` | serve the next under-quorum pair |` / `| `POST /runs/{run_id}/votes` | cast one judgment |` / `| `GET /runs/{run_id}/state` | the census |` / `| `GET /runs/{run_id}/tally` | the ranked whole |` / `| `GET /runs/{run_id}/manifest` | the run's manifest |`. AFTER: `| route | op | scope |` / `|---|---|---|` / `| `POST /runs` | register (201) | `register` |` / `| `GET /runs/{run_id}/next` | serve the next under-quorum pair | `next` |` / `| `POST /runs/{run_id}/votes` | cast one judgment | `cast` |` / `| `GET /runs/{run_id}/state` | the census | `state` |` / `| `GET /runs/{run_id}/tally` | the ranked whole | `tally` |` / `| `GET /runs/{run_id}/manifest` | the run's manifest | `manifest` |` then blank then `Every route reads the `X-Api-Key` header; the refusals are the three-part form (see [Auth](#auth)).`

**SEAM 4 — Usage-Web.** One line appended after the lifecycle line. BEFORE: `The lifecycle targets — `make start`, `make stop`, `make status`, `make restart` (`PORT ?= 8000`, `HOST ?= 127.0.0.1`; override: `make start PORT=8100`). The browser at `http://127.0.0.1:8000/`: register a list, vote the served pairs, read the ranked whole.` AFTER: the same line, then `The browser is key-free by design (the tier's own server-side key — every judge one voice); the CSRF rides invisibly, a stale token's cure the reload (see [Auth](#auth)).`

**SEAM 5 — Usage-MCP.** One line appended after the port note. BEFORE: `Port note: ... (`MCP_PORT ?= 8100`, `MCP_HOST ?= 127.0.0.1`).` AFTER: the same line, then `The two forms differ in trust: stdio is the local user's trust (the spawn IS the credential — the stamps self-claims); `--serve` is the bearer door. A tool absent from your list refuses as absent — check your key's scopes, not the server; the wrong-token 401's reconnect text is the substrate's own (the mint the only acquisition) (see [Auth](#auth)).`

**SEAM 6 — Input/Output Examples.** (a) the intro line amended; (b) the transcript re-emitted (§3.2); (c) the `tally` bullet amended. BEFORE (intro): `One run whole — a list in, three votes, the tally out (a fresh store; every byte as the tree emits it):` AFTER: `One run whole — a list in, three human votes, the corroboration halt, the llm's votes, the tally out (a fresh store; every byte as the tree emits it):`. BEFORE (the tally bullet): `- `tally` prints the ranked whole: one `rank` line per tie group, `counts` (wins, losses, ties) per item, `coverage` (the graph's components, done), a `cycle` line only when a Condorcet cycle exists, `pairs` (the weighted per-pair counts), and `version`.` AFTER: `- `tally` prints the ranked whole — or refuses first: the corroboration floor (every pair >=1 human AND >=1 llm, the standing policy) SAFE HALTs the tally with the three-part form until both classes sit; the llm's votes land on the existing pairs (the queue's exhaustion never blocks a direct cast); the second `tally` prints the ranked whole: one `rank` line per tie group, `counts` (wins, losses, ties) per item, `coverage` (the graph's components, done), a `cycle` line only when a Condorcet cycle exists, `pairs` (the weighted per-pair counts), and `version`.`

**SEAM 7 — Discipline.** (a) the CWD law amended; (b) the `.prioritree/` line amended. BEFORE (a): `- **The CWD law.** The store (`.prioritree/runs`) resolves CWD-relative — run from the repo root, or your data lands where you stood (the directory mints silently on demand); the CLI's `--home` is the per-invocation escape.` AFTER: `- **The CWD law.** The stores (`.prioritree/runs`, `.prioritree/keys.jsonl`) resolve CWD-relative — run from the repo root, or your data lands where you stood (the directories mint silently on demand); the CLI's `--home` is the per-invocation escape — the key mint included: a mint from another cwd lands in a store no door reads (the marker names the absolute home; pass `--home` matching it).` BEFORE (b): `- **`.prioritree/` mints at runtime** — the server pid and log, the runs store; gitignored, never present in a clone.` AFTER: `- **`.prioritree/` mints at runtime** — the server pid and log, the runs store, the keys store; gitignored, never present in a clone.`

**SEAM 8 — Status.** (a) the stale 203→336 cure (§3.1); (b) the dated land line. BEFORE: `... the MCP tier live 2026-11-22 (the five OunceMCP tools). CI is live (2026-11-23): ...` AFTER: `... the MCP tier live 2026-11-22 (the five OunceMCP tools); the auth landed 2026-11-24 (the key store, the grant map, the six doors, the mcp bearer door, the corroboration floor — [Auth](#auth)). CI is live (2026-11-23): ...`

## 3. THE STALE CURES' EXACT BYTES + THE TRANSCRIPT RE-EMITTED LIVE

### 3.1 The three numbers, four sites (each before/after)

- web.py's count — BEFORE: `` `src/prioritree/web.py` (654 lines, nine routes, `` AFTER: `` `src/prioritree/web.py` (820 lines, nine routes, `` (the Architecture Web bullet).
- mcp_server.py's count — BEFORE: `` `src/prioritree/mcp_server.py` (580 lines, `` AFTER: `` `src/prioritree/mcp_server.py` (645 lines, `` (the Architecture MCP bullet).
- the floor, site 1 — BEFORE: `The quality floor: 203 tests green, pyright clean, ruff clean.` AFTER: `The quality floor: 336 tests green, pyright clean, ruff clean.` (the Architecture close).
- the floor, site 2 — BEFORE: `The quality floor: 203 tests green, pyright clean, ruff clean.` AFTER: `The quality floor: 336 tests green, pyright clean, ruff clean.` (the Status close).

### 3.2 The Examples transcript re-emitted live (the halt-then-cure form — byte-exact)

The transcript whole (the console block replaces the standing block; every line the tree's own emission — the register/vote/state lines unchanged from the standing form, the exhausted line unchanged, the halt and the cure the new bytes):

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

THE HALT'S LINE, derived and pinned: the message form `refused — expected: {expected} | found: {found} | next: {next_action}` (tally.py:150); expected = tally.py:535-538 at k=1; found = tally.py:379-384 (the three scheduled pairs in order, each missing llm — policy.py:89's predicate over {human:1}); next = tally.py:421-427. The sections' bytes are pinned by the arcs (tests/test_tally.py:355-359, :386-391, :502) and the halt's expected/found walked LIVE (walk/mcp-verified-token.md:45); the suite green at my hand today carries every arc. THE CURED TALLY'S BYTES: the llm's three votes corroborate the human's judgments (prefer-a, prefer-b, prefer-b — the ranking unchanged: cilantro, aloe, basil; each pair's weighted count 2; the census at 6/4/4/4). The builder's verify-back (§6) re-emits the whole LIVE — the halt AND the green byte-exact (the CLI in-process per the tests' own school: a tmp home, `command([...])` the entry).

## 4. THE STUMBLES' BYTES (the eleven findings — the 5-cured/6-named split held)

CURED-IN-PROSE (5 — the wire cannot teach them; the README the only remaining channel; each's prose form fenced at §1.1):
- **M1** (the 401's misdirection) → the agent chain's line: the canned OAuth text named as the substrate's own, the reconnect mints nothing, the mint the only acquisition.
- **M3** (the marker's evidence) → the operator chain teaches where the marker lands (server.log's uvicorn boot channel; mcp-server.log's fastmcp channel) + the three states' bytes; `make restart`/`make mcp-restart` the verification ride. The residual named: a daemon's unread marker is still silent.
- **M4** (the no-door mint) → the agent chain's line: manifest has NO mcp tool — a manifest-only mcp key opens nothing; + the audience-pair line's "validates scopes and audience separately, never the combination".
- **F1** (the unwired web 401) → the operator chain's carry line + the Quickstart seam: BOTH legs named (the mint AND the env, then the reboot).
- **F3** (the invisible floor) → the floor told up front at the doors' movement + the transcript's halt teaching it in the genre (seam 6).

NAMED-ONLY (6 — the honest price, never hidden; each's line fenced):
- **M2** (the hide's dead-end) → "A tool absent from your list refuses as absent; check your key's scopes, not the server." (the agent chain + the MCP seam).
- **F2** (the single voice) → "Every browser judge is the web tier's ONE comparator: agreement between judges ACKs (the dedup), disagreement counts (a new record) — the other voices ride their own keys at the service/MCP tier." (the browser chain + the Web seam).
- **the stdio self-claims** → "Over stdio the spawn IS the credential — all five tools ungated, the stamps the body's self-claims (the local trust; `--serve` and the service wire are the verified forms)." (the agent chain + the MCP seam).
- **F6** (the failopen word) → the marker's on+absent line: "the LOAD fails open (the boot survives), the DOORS fail closed (every request 401s until a mint lands)".
- **F8** (the CWD mint) → the mint block's tie-down line + the Discipline seam's amendment (§2 seam 7).
- **F4** (the dead entry) → the residuals' line: "The browser's unbound id: the form's self-claim behind the tier key — the door stamps the web key's id." The template's own copy is the template's lane — UNTOUCHED (the no-source-bytes law).

## 5. THE THRESHOLD PARAGRAPH'S BYTES (the "when this stops being true" form)

Fenced at §1.1's WHY-HOLDS close: the three triggers (the operator count past <=8; the machine count past one; multi-tenancy) + the machinery each trigger earns (JWT at the multi-machine wire; the secret manager at the fleet; OAuth at the external authority) + the prices CITED to auth-design.md §1/§3, never copied — the full pricing stays banked at the store's record (the README's genre kept; the fork refused). The fence's posts named at the surface: one file (`.prioritree/keys.jsonl`), one machine's filesystem, one process's in-memory dict, the machine-wide flock.

## 6. THE NO-BREAK PROOFS

- **ZERO source bytes**: src/ whole untouched — the templates included (F4's template copy stands); the story is prose, the tree the truth it tells.
- **ZERO test bytes**: no new arcs; NO README-fence test (the drift question ruled — the F6 precedent's boundary held: the fence pins MECHANISM, never prose; the guards instead: (i) the transcript genre's paste-verification, (ii) the citation discipline (§8), (iii) moho's cold walk at the build gate (R4), (iv) the Status ledger's per-land line — the README's own standing cure for count-drift).
- **THE FLOOR AT 336**: my run today — 336 passed in 32.78s; the gate's floor-green step: `make test` (336 passed), `make lint` (zero findings), `make typecheck` (0 errors, 0 warnings) — the README edit touches no importable byte; the run proves the unbroken.
- **THE VERIFY-BACK READS** (the read-backs at the build gate, named): (1) the three stale cures confirmed at the source — the suite's own emission (336), `wc -l src/prioritree/web.py` (820), `wc -l src/prioritree/mcp_server.py` (645); (2) the Examples transcript's LIVE re-emission at the builder's hand — the halt AND the green both reproduced byte-exact (§3.2); (3) the marker's three states pasted from a live boot (`make restart` / `make mcp-restart`; the boot log lines read back); (4) the mint's three output lines pasted from a live mint; (5) the 401/403 bodies pasted from a live probe; (6) every cited path resolved (the store-relative paths git-tracked — the standing law; the code paths at their lines).

## 7. THE PER-STEP PLAN (R8 — the README ONE dispatch)

**ONE DISPATCH, one file, one edit** (the build increment build/readme-public-story, step 1 semantic at jikko's hand): the section (§1.1) + the eight seams (§2) + the stale cures (§3.1) + the transcript's re-emission (§3.2) — a single coherent landing. THE READ-BACKS NAMED (the dispatch's own text carries them): the section's head read back (the "## Auth" between the MCP close and "## Input/Output Examples"); the transcripts' byte-verification (the live re-emission compared byte-exact against §3.2's block; the mint's and the marker's lines pasted from the live run); the stale cures' sites confirmed (the four fences at §3.1, each read back at the source). **THEN FLOOR-GREEN** (step 2, deterministic — the make step): `make test` / `make lint` / `make typecheck` — the instruments' no-break proof (§6). The build dispatch cites THIS approved spec (the exact-task law). No dispatch fires before its gate is green (the precedence: this spec closes G-READMEPUBLICSTORYSPEC-BRIEF at the collaborator's approval → the build at G-README-PUBLIC-STORY).

## 8. THE CLAIMS' CITATIONS (each public claim → its evidence home, riding inline in the prose)

- the armed boot → Makefile:7; key_store.py:569-570; service.py:209; web.py:232-238; rikai map 1a
- the mint's ceremony + bytes → cli.py:198-216/:401-441; key_store.py:484-508; the census §3
- the marker's three states + channels → key_store.py:596-600; service.py:209-213; mcp_auth.py:110-125; walk/mcp-verified-token.md:22-27
- the typo refusal → key_store.py:554-578
- the carry's three lanes → key_verify.py:32; Makefile:8; web.py:232-241; mcp_auth.py:37-39
- the skeleton key → policy.py:41-47 (the six tokens); auth-design.md §1 :40
- the 401/403 ThreeParts → key_verify.py:116-138/:203-207; service.py:410-427; walk/serving-tier-integration.md:30-31
- the class stamped from the key → service.py:527-528; mcp_server.py:554-560; auth-design.md F8 :34
- the grant map + the mcp lift → policy.py:41-47; mcp_auth.py:86-94 (the standalone table REFUSED — a row-copy forks the data with no ImportError; the mints' arguments paste-verifiable)
- the corroboration floor + the halt → policy.py:69-89; tally.py:479-483/:534-548; tests/test_tally.py:353-359/:386-391; walk/mcp-verified-token.md:45
- the browser's lanes + the one voice → web.py:108-117/:228-241; walk/serving-tier-integration.md:38-43, F2 :54-55
- the agent's chain + the hide + the canned text → mcp_auth.py:33-44/:86-94/:196-226; walk/mcp-verified-token.md:29-35, M1 :49, M2 :51
- the honest statement → auth-design.md:56-65 (§3 verbatim — the blockquote's source)
- the stdio trust → auth-design.md:42-43; walk/mcp-verified-token.md:41-45; opencode.json:583-593
- the threshold + the alternatives' prices → auth-design.md:44/:65 (cited, never copied)
- the 336 / 820 / 645 → the suite's own emission; the two files' line counts (the census :36/:103; my reads today)
- the dated land line → the Status ledger's own form (the README's standing drift cure)

## 9. THE ACCEPTANCE MAPPING — G-READMEPUBLICSTORYSPEC-BRIEF's three conditions answered

1. **"the exact-task spec landed (the bytes whole, every line fenced): the README's regions — the story's structure, the honest statement verbatim, the commands exact, the claims' citations, the per-step plan"** → §1 (the placement's before/after + the section whole fenced); §1.1's Remains-trust blockquote (§3's headline VERBATIM + the residuals one home); the commands byte-exact at §1.1 (the mint's flags, the marker's three states, the AUTH states, the knobs at their ?= forms) and §3.2 (the halt-then-cure transcript); §8 (each claim → home); §7 (the one-dispatch plan, the read-backs named).
2. **"the llm-class constraint held at every line; the configurability law told at every knob the story names"** → the llm's key the SAME ceremony + the class stamped from the key + the floor needing exactly this (the comparator chain + the WHY-HOLDS movement — told honestly, never footnoted); every knob at its ?= form with its Makefile/source site (AUTH :7, PRIORITYTREE_WEB_KEY :8, PRIORITYTREE_KEYS_HOME key_store.py:45-48, PRIORITYTREE_WEB_CSRF_SECRET web.py:113-116, the header key_verify.py:32, the bearer mcp_auth.py:37-39).
3. **"the collaborator's approval — the build dispatch cites the approved spec"** → §7's close: the precedence named; the build dispatch fires only after this gate's green, citing this spec whole.

**THE TRADE-OFF THE PLAN MUST CARRY**: the prose's unfenced drift (NO machine fence — the four guards at §6; the numbers WILL drift again — the Status ledger's per-land line the standing cure, the exposure named); the one-voice truth told publicly (the sitting URL's promised multiplicity honestly narrowed); the hide's opacity owned in prose (the unauthorized agent's confusion the substrate's own law); the Examples transcript's growth (the halt taught in the genre — the length priced and accepted); the seams' eight-site maintenance (each a pointer, never a second telling — the story's ONE home the section); the armed boot's first-experience wall (the Quickstart seam carries it at the first command — the cost of a secure default, told, never apologized for). Every price named, never silent.
