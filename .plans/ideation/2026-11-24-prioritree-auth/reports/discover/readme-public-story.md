<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — discover/readme-public-story

**Route:** prioritree-auth (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-25T02:13:11Z |
| 2 | report | tansa | 2026-11-25T02:17:34Z |
## Reported by tansa — 2026-11-25T02:17:34Z

# tansa's discovery census — the public story's inputs whole (discover/readme-public-story, 2026-11-24)

Read-only at the repo root /Users/marklosey/projects/prioritree. Every finding a pointer: the path, the line, the byte. The suite run green at my own hand before anything was reported: **336 passed in 35.18s** (the test tool's emission). Nothing edited, nothing only in memory.

## 0. THE GROUND (read whole)

- The approved design: `.plans/ideation/2026-11-24-prioritree-auth/reports/synthesize/auth-design.md` (79 lines) — §3 THE HONEST STATEMENT verbatim (:56-65); §4 THE BUILD SET (:67-73), item 5: "THE README'S PUBLIC STORY — cured / remains-trust / why the choices hold (the public telling's own artifact)" (:73).
- The walks: `reports/walk/serving-tier-integration.md` (77 lines — the eight stumbles F1-F8 at :51-73, each with cure-path; 299 green at :16); `reports/walk/mcp-verified-token.md` (63 lines — the four stumbles M1-M4 at :49-55; F5 CHECKED CURED at :59; the stdio trust walked LIVE at :41-45; 336 green at :16).
- The blocking rulings F1-F10 whole: `reports/eval/adversarial.md` (:20-38) — F1 the failopen made loud (HIGH, blocking; F10 folded into it), F2 the drive-by cured at the tier (HIGH), F3 the store's integrity (HIGH), F4 the supersedes door check (HIGH), F5 the audience field (MED-HIGH), F6 the coverage invariant (MED), F7 the quantities (MED), F8 the llm-insider (MED), F9 the timing residual (LOW-MED), F10 the cwd resolution (LOW).

## 1. THE README WHOLE (README.md, 193 lines)

**Section order**: title + intro (:1-15) → Quickstart (:17-45) → Architecture (:47-57) → Usage — CLI (:61-77), Service (:79-95), Web (:97-99), MCP (:101-110) → Input/Output Examples (:112-158) → Discipline (:160-165) → Install (:167-185) → Status (:187-189) → License (:191-193).

**The MCP section (:101-110), its current claims**: two run forms — stdio `uv run python -m prioritree.mcp_server` (:106) and `--serve` at http://127.0.0.1:8100 (:107); the port note (:110 — defaults, `--host`/`--port` override, the web keeps 8000, "the collision is retired", the lifecycle targets `make mcp-start/mcp-stop/mcp-status/mcp-restart`, `MCP_PORT ?= 8100`, `MCP_HOST ?= 127.0.0.1`). The five OunceMCP tools named at :55 (`runs.register`, `runs.next`, `votes.cast`, `votes.census`, `runs.tally`). ZERO auth content in the section — the mcp tier told ungated.

**The auth story's ABSENCE, pinned**: the file-scoped grep over auth|AUTH|[Kk]ey|secret|scope|CSRF|audience|corroborat|401|403 returns exactly TWO matches, both the incidental word "authored" (:54 "14 authored Jinja2 templates"; :162 "the repo's authored files"). The auth vocabulary — AUTH, key, mint, scope, CSRF, audience, corroboration, 401, 403, PRIORITYTREE_* — appears NOWHERE. The README's told posture is anonymous end-to-end: `make start` opens the browser with no key (:27-28), the MCP boots bare (:106), the six service routes are taught ungated (:86-95). Near-matches, named so the story's rewrite doesn't confuse them: "Item tokens" (:74, the id:label grammar) and "`.prioritree/` mints at runtime" (:165, the store directory).

**The commands it teaches, pinned per command**: `git clone` (:22); `make dev` (:24); `make test` (:25); `git config core.hooksPath .githooks` (:26); `make start` (:27); `open http://127.0.0.1:8000/` (:28); the tool lane `uv tool install .` (:36) + `prioritree register/next/vote` (:37-43); the service `uv run uvicorn prioritree.service:app` (:82), `make start/stop/status/restart` (:83); the web overrides `make start PORT=8100` (:99); the mcp forms (:106-107) + `make mcp-start/mcp-stop/mcp-status/mcp-restart` (:110); `PRIORITREE_HOOK_BYPASS=1` (:163); the install sequence `make dev/test/lint/typecheck` (:174-177); the tool lane's `$(uv tool dir)/prioritree/bin/uvicorn prioritree.service:app` and `$(uv tool dir)/prioritree/bin/python -m prioritree.mcp_server` (:183).

**The voice**: noun section heads; two-column tables for the op/route maps (:65-71, :88-95); verbatim console blocks ("every byte as the tree emits it", :114); the parenthetical-citation style carrying each claim's reason inline ("the collision is retired", :110); one-claim-per-line length discipline; dates pinned per land ("Born 2026-11-19... the MCP tier live 2026-11-22", :189); the honest-sequence idiom (:169 "The full honest sequence").

**The stale numbers (drift the story's rewrite corrects)**: "203 tests green" (:57 and :189 — the floor is now 336); `web.py` "654 lines" (:54 — now 820); `mcp_server.py` "580 lines" (:55 — now 645).

## 2. THE HONEST STATEMENT'S SOURCES

**The design's §3 verbatim (auth-design.md:56-65)** — "THE AUTH CURES THE WIRE; THE DISK AND THE LOCAL MACHINE REMAIN TRUST" — the residuals, each the story's remains-trust section: (1) the cleartext store (:59 — hashed-at-rest guards the KEY, never the DATA; the JSONL's ids, questions, notes naked on disk); (2) the local process's reach (:60 — the key fences the socket, not the filesystem); (3) the offline JSONL edit (:61 — the check lives at the wire; the seam on disk); (4) the issuance's honesty (:62 — the operator mints honestly, the operational trust itself); (5) the web tier's id-binding (:63 — the form's self-claim behind the tier key); (6) the MCP hiding's teaching loss; F7's quantities owned by the tally-policy lane, never silent; the /docs + route-table recon ruled with F6 (:64); (7) THE SCALE FENCE BANKED (:65 — past <=8 operators, past the single machine, into multi-tenancy: the file's earn ends; JWT 9.1x-36.4x + the second secret; the secret manager $28.80/yr + the credential chain; OAuth the consent ceremony — the triggers named, the prices standing).

**The walk findings' story-relevant set (each with its cure-path)**:
- The 401's misdirection (walk/mcp-verified-token.md M1 :49) — the wrong-token 401's canned OAuth text ("clear authentication tokens in your MCP client and reconnect...") actively misdirects; the reconnect mints nothing. Cure-path: the operator's boot marker + unit 5's README (the mcp tier's key story).
- The hide's dead-end (M2 :51) — the guessed-name hint ("List the tools again...") is a cure-path the hidden tool can never honor; the unauthorized agent cannot tell broken-server from unauthorized-self. Cure-path: the README names the hide's law — a tool absent from your list refuses as absent; check your key's scopes, not the server.
- The marker's evidence (M3 :53; serving walk F7 :70) — no `auth:` line in the live logs until the operator reboots. Cure-path: `make restart` / `make mcp-restart`.
- The manifest-only mint (M4 :55) — `--audience mcp --scopes manifest` mints cleanly yet opens NO door anywhere (manifest rides the service tier alone); a legitimately-keyed caller's tools/list renders empty. Cure-path: the README names the mcp tier's five-tool reach.
- The web tier's single-voice price (serving walk F2 :54-55; the design §1 :40) — every browser judge is the web tier's one comparator; agreement ACKs while disagreement counts; the sitting URL's promised multiplicity collapses under auth-on. Cure-path: teach the truth at the ack.
- The browser's unbound id (design §3 :63; serving walk F4 :60-61) — the judge-entry copy ("it stamps your votes") lies under auth-on; the door stamps the web key's id. Cure-path: the copy names the mode's truth.
- The CSRF restart (serving walk :41; web.py:108-116) — the secret unset => a boot-minted random; outstanding tokens die at restart; the stale-secret arc teaches the re-render cure. The knob: PRIORITYTREE_WEB_CSRF_SECRET for one secret across workers.
- The skeleton key (design §1 :40, §2 :48) — the tier key's leak = every human's writes; single-point, named.
- The wiring loop (serving walk F1 :51-52) — the 401's taught mint cures NOTHING at the browser until PRIORITYTREE_WEB_KEY rides the next boot. Cure-path: the story teaches the wiring leg (the mint AND the env).
- The failopen naming (serving walk F6 :66-67) — the marker's "failopen" names the BOOT, not the doors: on+absent the doors fail CLOSED (every request 401s until a mint lands). Cure-path: the story's honest naming.
- The corroboration floor's visibility (serving walk F3 :57-58) — the floor (>=1 human AND >=1 llm) first appears at the tally's halt; the browser has no llm lane. Cure-path: name where the second class rides (the operator's llm-class key at the service/MCP tier).

## 3. THE LANDED SURFACES' PUBLIC FACTS (verified at the source)

**The mint's exact CLI form**: `prioritree key mint <comparator-id> --class <human|llm> --scopes <csv> --audience <service|mcp>` — the parser at src/prioritree/cli.py:198-216 (`--class` default human :212; `--scopes` required :215; `--audience` default service :216; its own `--home` parent defaulting KEYS_HOME :200-206). Output three lines, marker-first tab-separated: `key\t{plaintext}` / `digest\t{digest}` / `mode\t0600` (:438-440). The plaintext shown ONCE, never written — only the sha256 hexdigest rides the file (key_store.py:484-485); chmod 0600 after the write, umask-proof (:507); the record one self-describing JSONL line {digest, comparator_id, comparator_class, scopes, audience, created_at} (:120-125); the store `.prioritree/keys.jsonl` (KEYS_HOME :45). The vocabulary gates refuse with the three fields at exit 1 (class :462-467, scopes :468-474, audience :475-479); the six scope tokens (:52) = {register, next, cast, state, tally, manifest}; the audience pair (:53) = {service, mcp}. Exit codes 0/1/2 (cli.py:84-86; KeyStoreRefusedError rides the exit-1 tuple clause :488-490).

**The boot markers' exact bytes** — render_boot_marker (key_store.py:581-600), three states:
- on+present: `auth: on | keys: {home} | count: {N}` (:600)
- on+absent: `auth: on (failopen -- no key store) | keys: {home} | next-action: prioritree key mint` (:599)
- off: `auth: off (operator's explicit degrade) | keys: {home} | count: {N}` (:597)
The service's render site (service.py:209-213): AUTH read ONCE at construction (:209), the keys home resolved ABSOLUTE (:210), the marker on uvicorn's "uvicorn.error" channel (:211-213). The mcp's render site (mcp_auth.py:121-125): the same read at the import, the marker on "fastmcp.prioritree.mcp_auth" (:110, :123-125). A typo'd AUTH refuses LOUDLY at the resolve (key_store.py:554-578: expected `AUTH one of on|off (or unset)`, found the value verbatim, the fix-and-reboot next-action) — the boot dies honestly.

**The knobs' exact forms**: `AUTH ?= on` (Makefile:7) — carried by `make start` (:34, with `env -u WEB_CONCURRENCY AUTH=$(AUTH) PRIORITYTREE_WEB_KEY=$(PRIORITYTREE_WEB_KEY)`) and `make mcp-start` (:83, AUTH=$(AUTH)); `PRIORITYTREE_WEB_KEY ?=` empty default (Makefile:8) — read at web.py:232-233, riding the in-process client's default header (:237 `headers={AUTH_HEADER_DEFAULT: _web_key} if _web_key else None`), with the boot log line `web tier key: present|absent (a six-token grant)` (:239-241); `PRIORITYTREE_KEYS_HOME` (key_store.py:48, resolved once at boot :144-161 — an empty/absent override falls back to KEYS_HOME); `PRIORITYTREE_WEB_CSRF_SECRET` (web.py:113-116 — unset => a boot-minted random secret, the restart-invalidation price carried :110-112); the header default `X-Api-Key` (key_verify.py:32) — at the service door and the web child; the mcp door rides the transport's bearer grammar instead (mcp_auth.py:37-38 — the X-Api-Key knob does NOT ride at this door).

**The grant map's rows** (policy.py:33-47, default-deny — absence IS the denial):
- operator: {register, state, tally, manifest} (:43)
- comparator: {next, cast, manifest} (:44)
- auditor: {state, tally, manifest} (:45)
The mcp lift TOOL_SCOPES (mcp_auth.py:86-94): runs.register→register, runs.next→next, votes.cast→cast, votes.census→state, runs.tally→tally — five of the six tokens; manifest rides the service tier's sixth route alone (the named gap :33-36, no mcp tool carries it).

**The corroboration floor (the tally's fourth leg)**: tally.py:479-483 names the four legs (zero-coverage, connectivity, per-pair quorum, per-pair corroboration — F8's floor ">=1 human AND >=1 llm", the policy predicate the law's one home); the gate's conjunction at :534-548, expected verbatim: `the coverage gate met: no zero-coverage item, the comparison graph connected, every pair at quorum k={quorum} AND corroborated (>=1 human AND >=1 llm per pair)`; the pure predicate missing_classes (policy.py:69-89); the two gap kinds taught distinctly (tally.py:493-494 — "quorum needs MORE VOTES; corroboration needs votes from BOTH CLASSES").

**The audience doors (the cross-tier replay dead)**: F5 fires inside verify — the service door (key_verify.py:194-197, tier_audience "service" passed at service.py:251) and the mcp door (mcp_auth.py:175, `verify(_keys, token, "mcp", None)`, KeyVerifyError → None at :176-177) — the wrong-audience key the SAME 401/None as the digest miss, the audience never named (the oracle never fed). Verified both directions by the walk (walk/mcp-verified-token.md :32-33, :59: F5 CHECKED CURED).

**The 401/403 ThreePart, exact bytes**: 401 (key_verify.py:132-138) — expected `the key in the X-Api-Key header`, found `absent-or-unknown`, next_action `mint a key: prioritree key mint <comparator-id> --class <human|llm> --scopes <csv> --audience <tier>`; 403 (:203-207) — expected `the {scope} scope`, found `the key's scopes [...]`, next_action `re-mint with the scope: prioritree key mint ... --scopes <csv>+{scope}`. The dedicated handlers at service.py:410-417 (401) and :420-427 (403); the supersedes 403's found ELIDES the target's author; the web tier's 401/403 lanes render auth.html at the honest statuses (never the crash page); the mcp 401 the transport's own (empty body + `WWW-Authenticate: Bearer`). The recon surfaces stripped: service.py:195 and web.py:224 both `FastAPI(docs_url=None, redoc_url=None, openapi_url=None)`.

**The stdio trust, the story's remains-trust leg**: the spawn IS the credential (auth-design.md:42-43; walk/mcp-verified-token.md :41-45 LIVE — all five tools ridden ungated, the halt's corroboration teaching proving the self-claim stamps; opencode.json:583-593 the bare spawn pinned).

## 4. THE PUBLIC RECORD'S CITATIONS (the claims-citable map — every README claim rides an evidence home on disk)

| the public fact | the evidence home |
|---|---|
| the mint's form + bytes | cli.py:198-216/:401-441; build/key-infrastructure.md; validate/key-infrastructure.md (245 green :20) |
| the marker's three states | key_store.py:581-600; walk serving F6 :66-67 / F7 :70; walk mcp M3 :53 |
| the grant map's rows | policy.py:33-47; validate/policy-layer.md (rows byte-exact, 268 green :16/:20) |
| the floor's fourth leg | tally.py:479-483/:534-548; validate/policy-layer.md :16; the design §1 :34 + §2 :54 |
| the audience door dead both ways | key_verify.py:194-197; mcp_auth.py:158-188; walk mcp :59 (F5 checked cured); the design F5 :32 |
| the honest statement | auth-design.md:56-65 (§3 verbatim — the public record's own carrier) |
| the build set's unit 5 | auth-design.md:67-73 (§4 item 5) |
| the F1-F10 rulings whole | eval/adversarial.md:20-38 |
| the web tier's prices | auth-design.md:40 (§1) + :48 (§2); walk serving F1-F8 :51-73 |
| the MCP teaching losses | walk mcp M1-M4 :49-55 |
| the stdio trust | auth-design.md:42-43; walk mcp :41-45; opencode.json:583-593 |
| the 336 | my run (336 passed in 35.18s, 2026-11-24); walk mcp :16; validate/mcp-verified-token.md :16 |
| the spec fences | synthesize/keyinfrastructurespec.md, policylayerspec.md, servingtierintegrationspec.md, mcpverifiedtokenspec.md (the four exact-task specs at the auth store's synthesize home); the unit briefs synthesize/{key-infrastructure, policy-layer, serving-tier-integration, mcp-verified-token}.md |

All paths relative to the repo root /Users/marklosey/projects/prioritree; the reports under .plans/ideation/2026-11-24-prioritree-auth/reports/.

## 5. THE TESTS' UNTOUCHED TRUTH

**The floor: 336 passed in 35.18s** — my own run, 2026-11-24 (the test tool's emission; zero skips, zero failures). The increment trail on disk: 245 (validate/key-infrastructure.md :20) → 268 (validate/policy-layer.md :20) → 299 (walk serving :16, validate serving :92) → 336 (walk mcp :16 — "299 + 37 = 336, the door's own file solo 37 passed in 1.83s"; confirmed at validate/mcp-verified-token.md :16). The instruments (the story's verify-it-yourself commands, Makefile:15-22): `make test` (uv run pytest), `make lint` (uv run ruff check src/ tests/), `make typecheck` (uv run pyright). The README's stale "203 tests green" (:57, :189) is the number the story's rewrite corrects to 336.

## THE HEADLINE (for togo's brief)

The README today tells an anonymous tree: 193 lines, zero auth vocabulary (two incidental "authored" the only matches), the MCP section (:101-110) teaching two ungated run forms, three stale numbers (203 tests / 654 web lines / 580 mcp lines) against the landed 336 / 820 / 645. The story's inputs are whole on disk: the honest statement verbatim (auth-design.md §3, eight residuals), the eleven story-relevant walk findings each with its cure-path, the mint's exact form and markers' exact bytes, the five knobs (AUTH, PRIORITYTREE_WEB_KEY, PRIORITYTREE_KEYS_HOME, PRIORITYTREE_WEB_CSRF_SECRET, X-Api-Key), the grant map's three rows + the mcp five-tool lift, the four-legged coverage gate, the audience doors dead both directions, the citation map (design § / walk finding / spec fence / validate report per claim), and the floor's 336 verified live at this census's own hand. Nothing missing for the brief; nothing here decided — the choices are togo's and the build's.
