<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — walk/serving-tier-integration

**Route:** prioritree-auth (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-24T23:30:31Z |
| 2 | report | moho | 2026-11-24T23:36:20Z |
## Reported by moho — 2026-11-24T23:36:20Z

# moho's blind walk — unit 3's serving-tier integration (packet walk/serving-tier-integration)

Walked cold, 2026-11-24, at the repo root /Users/marklosey/projects/prioritree: the CLI's mint ceremony, the service's six doors, the web tier's browser lanes, the degrade, the live store home. No guides read, no builders asked — the code, the tests' own fixtures, and my seat's read-only instruments the only sources. The suite run green cold first: **299 passed in 32.02s** (the test tool's own emission).

## THE OPERATOR'S PATH (cli.py, key_store.py, service.py's construction)

- The ceremony: `prioritree key mint <comparator-id> --class <human|llm> --scopes <csv> --audience <service|mcp>` — stdout three lines, marker-first tab-separated: `key\t{plaintext}` (shown ONCE, never written — only the sha256 hexdigest rides the file), `digest\t{digest}`, `mode\t0600`. The line lands at `.prioritree/keys.jsonl` (CWD-relative), one complete sort_keys JSON line, chmod 0600 after the write (umask-proof), under one machine-wide file lock over the keys home's parent. The vocabulary gates refuse with the three fields at exit 1 (the class, the scopes — the six tokens named, the audience); argparse's own channel (exit 2) for the argv.
- The boot marker at the service's construction (service.py:209-213): AUTH read ONCE (resolve_auth_mode — a typo'd value refuses loudly at boot, the process dies honestly), the keys loaded once for the count, the marker rendered on uvicorn's boot channel. The three states, walked at key_store.render_boot_marker:
  - on+present: `auth: on | keys: {absolute} | count: {N}`
  - on+absent: `auth: on (failopen -- no key store) | keys: {absolute} | next-action: prioritree key mint`
  - off: `auth: off (operator's explicit degrade) | keys: {absolute} | count: {N}`
- LIVE: the store home `.prioritree/` carries runs/ and logs but NO keys.jsonl — the live state is on+absent. The standing server.log's last boot (pid 22906) predates the unit: no `auth:` line, no `web tier key:` line; both tiers down (no pidfiles). The marker's live evidence awaits the operator's reboot.

## THE COMPARATOR'S PATH (the six doors, the key carried — service.py, key_verify.py, the fixtures)

- The six doors: POST /runs (register), GET /runs/{id}/next, POST /runs/{id}/votes (cast), GET /runs/{id}/state (census), GET /runs/{id}/tally, GET /runs/{id}/manifest — each gated `require_key(<scope>)`, the six scope tokens 1:1 the doors. The fence pinned twice in the fixtures: the route-table walk (every APIRoute carries the factory marker; the web child's tail Mount exempt by type; no seventh route) and the source scan (six door tokens).
- The 401 at the missing/unknown/wrong-audience key: the SAME three fields at every leg — `expected: the key in the X-Api-Key header`, `found: absent-or-unknown`, `next_action: mint a key: prioritree key mint <comparator-id> --class <human|llm> --scopes <csv> --audience <tier>` — the identity oracle never fed (the F9 dummy compute equalizes the miss path's work; the ONE compare constant-time; the wrong audience renders identically, `mcp` never named). The dedicated handler lane: 401 stays 401, the mint taught, never the fold's ESCALATION.
- The 403 at the scope denial: `expected: the {scope} scope`, `found: the key's scopes [...]`, `next_action: re-mint with the scope: prioritree key mint ... --scopes <csv>+{scope}` — the authorization half's own refusal, taught.
- The cast's stamps: the door's record overrides the body — comparator_id and comparator_class from the KeyRecord (`record.comparator_id if record.digest else body.comparator_id`) — the self-claim dies at the door; an llm-class key (minted by the SAME ceremony, only --class llm) stamps llm over a body claiming human. The supersedes 403: found ELIDES the author — `{VOTE-####} — another author's vote (the author never named)`; the target vote untouched.
- The tally's halt forms teaching BOTH cures — live-confirmed at the member tier by my keyless probe on RUN-0001 (zero votes): expected names the full conjunction (`the coverage gate met: ... every pair at quorum k=1 AND corroborated (>=1 human AND >=1 llm per pair)`); found carries the sections (`zero-coverage items: ...; components: ...; under-quorum pairs: (a, b) 0 of 1; uncorroborated pairs: (a, b) missing human, llm`); next_action teaches the cures distinctly — `cast the missing votes: (a, b) needs 1 more — quorum needs MORE VOTES on existing pairs` AND `cast the corroborating votes: (a, b) needs llm — corroboration needs votes from BOTH CLASSES on existing pairs`. The manifest door: the five-key body (stem echoed, question, verdicts sorted, quorum, items), the operator id and stamp elided.
- The mid-flight mint lands live through the door (the stat ride re-loads on mtime — a second container's mint seen at the next request).

## THE BROWSER'S PATH (web.py, the templates, the fixtures)

- The register form: the CSRF rides invisibly — `<input type="hidden" name="csrf_token">` minted per-path (the landing bound to /ui/register; the sitting page and the pair fragment bound to /ui/runs/{stem}/vote; the per-path binding asserted — the landing's and sitting's tokens differ).
- The vote post: the token carried in the pair form's hidden field; the comparator entry rides hx-include from the sitting page.
- The result page: the ranked whole at the render gate (done:false NEVER renders — the gated branch withholds); the shareable URL preserved — the register-ack renders it from the REQUEST's own base URL (`{request.base_url}runs/{run_id}`), never a configured port, with the click-to-copy affordance.
- The drive-by's death: the tokenless POST refused BEFORE the service call — the write never lands (the resume 404s); the refusal fragment at 200: `expected: the form's csrf_token field (minted into the served page)`, `found: absent-or-mismatched`, `next_action: reload the page and re-send — the re-render mints a fresh token` — never the fold's clothes. The stale-secret arc teaches the restart price with the same re-render cure; the mismatched-token arc the compare's mismatch leg.
- The 401/403 lanes at the browser: the PAGE lanes render auth.html — the service's own three fields verbatim, the heading naming the half (`The service asked for a key` / `The key lacks this act's scope`), at the honest 401/403 statuses, never the crash page's clothes; the FRAGMENT lanes render the refusal fragment (the fields verbatim at 200 — the fragment tier holds no 4xx).
- The tier key invisible at the browser: the child holds ONE key at boot (PRIORITYTREE_WEB_KEY riding the in-process client's default header); the browser never sees it — the key absent from every rendered body (the ack and the sitting page both asserted key-free).

## THE DEGRADE'S PATH (auth off)

The doors return the anonymous record (digest="" the fallback marker); the six routes' bodies byte-identical to the pre-auth surface, no key anywhere; the cast's stamps fall back to the body's claims (the degrade's price, named in the code); the marker's honest line names the operator's explicit degrade. The web tier rides bare: the register fragment's ack and the sitting page 200 with NO key store at all — the standing fixtures ride the degrade.

## THE FINDINGS — every stumble named, each with its surface and cure-path (each a retro candidate for the friction ledger at the coordinator's call)

**F1 — the web tier's 401 cure-loop is under-taught (the mint taught, the wiring never named).**
Surface: the default boot — Makefile `AUTH ?= on`, `PRIORITYTREE_WEB_KEY ?=` EMPTY — the browser's register POST meets the service's 401 (no web key), and the taught cure is `mint a key: prioritree key mint ...` — but the minted key cures NOTHING at the browser until `PRIORITYTREE_WEB_KEY=<key>` rides the next boot. The operator who follows the refusal's next_action verbatim stays refused, looped back to the same 401. Cure-path: the web lane's 401 teaching (auth.html + the fragment) names the tier's own second step — set PRIORITYTREE_WEB_KEY and reboot — or the boot marker names both legs (the mint AND the wiring). The web boot log's `web tier key: absent` is the half-teaching the operator must find on their own.

**F2 — the shareable URL's multiplicity collapses under auth-on (all browser judges one voice).**
Surface: the cast door stamps the KEY's comparator_id over the form's entry (F8); the child holds ONE key; so every judge on the shared URL is the same comparator — agreement between judges ACKS (the dedup key identical, the count unchanged, "it stands once") while disagreement counts (a different winner is a new record). ack.html's quorum>1 teaching — "share this sitting URL with your other judges" — promises a multiplicity the door cannot deliver under auth-on. Cure-path: rule the web tier's per-judge claim trusted at the child (a sub-stamp the door carries), or teach the truth at the ack (browser judges are the web tier's one voice; the other voices ride their own keys at the service tier).

**F3 — the corroboration floor is invisible until the tally, and the halt's affordances predate it.**
Surface: the register form teaches quorum only ("1 means just you"); the done page says "The run is complete — each pair has its judgments"; the floor (>=1 human AND >=1 llm per pair) first appears at the result page's 409. halt.html's affordance list carries TWO `<li>`s (bridging pairs, shortfall pairs) — the corroboration leg's cure rides only in the three fields, and the browser has NO lane to cast an llm voice at all (the form hardcodes human; under auth-on the door stamps the key's class): "Resume the sitting" cannot cure the uncorroborated leg. Cure-path: the halt grows the third `<li>` naming where the second class rides (the operator's llm-class key at the service/MCP tier); the register form and the done page name the floor's price at registration.

**F4 — the sitting page's judge-entry copy lies under auth-on.**
Surface: sitting.html — "Your name for yourself as a judge — it stamps your votes" — true only at auth-off; under auth-on the door stamps the web key's id and the entry is dead weight (the child sends it; the door overrides it). Cure-path: the copy names the mode's truth, or the entry renders only at the degrade.

**F5 — the mcp audience is mintable but doorless; the member tier answers keyless (live-confirmed).**
Surface: the mint accepts `--audience mcp`; verify's ONLY caller passes "service"; mcp_server.py carries no door at all — the AUTH env rides `make mcp-start` but nothing reads it. My keyless census and tally probes LANDED live on the member tier (RUN-0001 answered total 0; the halt's full conjunction taught). An mcp-audience key opens nothing; worse, an operator following the 401's teaching (`--audience <tier>`) who mints mcp gets the SAME 401 at the service — the oracle discipline cannot tell them which leg fired. Cure-path: the mcp tier's door (its own unit), or the mint's teaching names the audience's present reach (service is the only consuming tier today); the wrong-audience holder's cure is re-minting with the default.

**F6 — the marker's "failopen" names the boot, not the doors (the on+absent surface is fail-CLOSED).**
Surface: at on+absent the marker reads `auth: on (failopen -- no key store)` — the LOAD fails open (the boot survives, the empty dict) but the DOORS fail closed: no key can verify against an empty store; every request 401s until a mint lands (the stat ride then makes it live). A first-time reader of "failopen" may expect the doors open. Cure-path: the absent-state line names the doors' truth too ("no key can verify — every door refuses until a mint lands"); the mint next-action already rides it.

**F7 — the live log channels carry no marker (the marker's evidence absent until a reboot).**
Surface: `.prioritree/server.log`'s last boot predates the unit — no `auth:` line, no `web tier key:` line; both tiers down; no keys.jsonl in the live home. The marker's honesty is untestable at the live surface until the operator reboots. Cure-path: `make restart` + `make mcp-restart` — the marker then lands on uvicorn's boot channel (server.log); the residual (a daemon's unread marker) is named in the code's own docstring.

**F8 — minor: the mint's CWD-relative home.**
Surface: the CLI's `--home` default is CWD-relative (.prioritree/keys.jsonl); the service resolves its own home ABSOLUTE at boot — a mint run from another cwd lands in a different store and the failopen persists. Cure-path (already present, named for the ledger): the marker names the absolute path; run the mint from the repo root, or pass `--home` matching the marker's named path.

## THE VERDICT

The built surface holds: 299/299 green cold; the six doors gated (the fence pinned twice) and teaching in the family grammar at every refusal — the 401's oracle discipline byte-exact at every leg, the 403's re-mint, the supersedes elision, the tally's halt teaching BOTH cures (live-confirmed); the browser's drive-by dies with the write never landing, the tier key never rendered, the shareable URL preserved from the request's own base URL; the degrade rides whole with the marker's honest line. The stumbles are TEACHING-grade, not behavior-grade — the sharpest sit at the seam where the door's verified truth meets the browser's promise (F1's cure-loop, F2's collapsed multiplicity, F3's invisible floor), plus one open door by omission (F5's keyless member tier). The gate's evidence: this report; each finding a retro candidate for the friction ledger at the coordinator's call.
