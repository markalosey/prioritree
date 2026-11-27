<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/state

**Route:** prioritree-polish (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-27T00:49:16Z |
| 2 | report | shindan | 2026-11-27T00:57:16Z |
## Reported by shindan — 2026-11-27T00:57:16Z

# THE STATE DIAGNOSIS — shindan (診断), packet census/state (prioritree-polish), 2026-11-27

The tree's stated-vs-lived condition, each gap at its bytes. The ground read whole: the store's heart (Q-polish, the convening ruling, the banked set); store_lock.py, service_store.py, service.py, mcp_server.py, mcp_auth.py, key_store.py, key_verify.py, session.py, policy.py, run_store.py, votes.py, tally.py, cli.py, web.py whole; the 17 templates + app.js/app.css; README.md whole; the Makefile whole; the .opencode wrappers + the engines' docstrings; the three efforts' records for the banked findings' era-truth. READ-ONLY held; this report the packet's only write. Every count re-read at the tree, never copied from the banked records (the claims lane); the tree is the truth.

## 1. THE TRUST STATEMENTS — the era-truth

**store_lock.py:10-12 (module docstring) + :45-46 (class docstring) — THE PRE-AUTH STATEMENT STILL STANDING [banked].** Stated: "CLOSED because all writers are local, none bypasses: the harness-launched session servers, the localhost service, the CLI; external agents speak THROUGH the shared HTTP server." The lived truth at the armed era: (a) the CLOSURE SURVIVES — "none bypasses" holds by composition: every writer tier composes the Lock (the CLI's five handler windows, the service's Serialize verbs, the mcp seam, the web tier through the service), no writer lane outside the seam; (b) the GROUNDING MOVED — "all writers are local" is the pre-auth trust; the armed era's writers include token-carrying REMOTE principals (external agents at the mcp --serve bearer door, browsers at the web lane) whose writes ride the local server processes under KEYS, not locality — the wire cured (the honest statement: "THE AUTH CURES THE WIRE; THE DISK AND THE LOCAL MACHINE REMAIN TRUST", README:188); (c) "the shared HTTP server" is now TWO armed doors (the service at 8000, X-Api-Key; the mcp --serve at 8100, bearer); (d) the local trust's own named residual is the stdio spawn (mcp_server.py:22-25: "the spawn IS the credential, the checks skipped at the transport") — the one lane where locality remains the whole trust. THE CURE-WORDING'S SHAPE: a one-line re-word naming the armed era — the closure by composition, the two armed doors, the honest statement's residual carried (the disk + the local machine; the stdio spawn the local lane's credential) — the mechanism unchanged, micro weight. The re-word must not claim more than the lock does: the auth era's own records (auth-threat-model.md) priced the flock "prevents torn files; it confers NO authorization" — the trust STATED, never enforced; the honest re-word names composition, never enforcement.

**service_store.py:19-21 (module) + :61-62 (class) — the same clause's in-source echoes.** "The multi-process widening held by the flock outermost: every standing writer local, none bypassing the seam" — the same era-gap (the locality grounding pre-auth), the same one-line re-word's shape; the banked gap's full extent.

**THE STDIO TRUST — CURRENT, AFFIRMED.** mcp_server.py:21-25 ("the stdio trust whole: the spawn IS the credential, the checks skipped at the transport"), mcp_auth.py:239-241 ("The stdio_policy kwarg NEVER rides (the substrate default 'trust' -- the spawn IS the credential, the enforce form priced and refused at the design)"), README:120/176/197 — the post-session era's truth stated whole: the local trust named as the residual, the verified forms named (--serve + the service wire). No gap.

**THE HONEST STATEMENT'S IN-SOURCE ECHOES — CURRENT, AFFIRMED.** service.py:136-149 (the web-lane marker's "THE HONEST RESIDUAL": the id-forgery price named, "the id PERSISTENT, NEVER VERIFIED — the record says what it knows and what it merely carries") — grown by the session build, true to the changed body at :581-583. key_verify.py's oracle clauses (the wrong-audience 401 the SAME form, :194-197) — true to the body. The multi-user statement's echoes (README:196/215-221) — current. The ONE standing pre-auth clause is store_lock's (+ its service_store echo).

## 2. THE STALE TOOL DESCRIPTION [banked] + THE SAME-CLASS DRIFT (the surprise)

**mcp_server.py:536-537 — runs.next's description [banked].** Stated: "Serve the sitting's next under-quorum pair -- the loop's read: call until done:true (every pair at quorum), then runs.tally." Lived (session.py:278-296, the corroboration-aware chain, amendment 22): a pair is SERVED while under-quorum OR uncorroborated (session.py:280: `count < manifest.quorum or missing_classes(...)`); done:true's own expected field reads "all N scheduled pairs at quorum k=K AND corroborated (>=1 human AND >=1 llm per pair)" (session.py:284-285). BOTH clauses stale: "next under-quorum pair" (an at-quorum-but-uncorroborated pair is served too) and "(every pair at quorum)" (the DONE condition grew the corroboration leg). The live tool's served description carries this stale text verbatim (corroborated at this session's own tool listing). CURE: one-line re-word, micro.

**THE SAME CLASS BEYOND THE BANKED TEXT — the drift pattern:** the core's own docstring was updated at amendment 22 (session.py's next_pair names the corroboration rollup whole, :243-252), but EVERY citing surface still states the pre-amendment condition:
- mcp_server.py:634 — runs.tally's description: "Under quorum the tally SAFE-HALTs" — the halt also fires AT quorum when corroboration is missing; the README's own worked example (:259) is exactly this case (three human votes at k=1, the tally halts on the corroboration leg alone).
- service.py:516 (the serve route's docstring), service_store.py:129 (the serve verb's docstring), run_store.py:901-902 (Persist.serve's docstring) — "the next under-quorum pair", three wrapper tiers of the same stale clause.
- cli.py:184 (the next subcommand's help — user-facing) + cli.py:270-275 (_command_next's docstring) — the same clause.
- cli.py:183 (--quorum's help): "votes per pair before coverage (default: 1)" — stated: quorum => coverage; lived: the coverage gate is two-legged (quorum AND corroboration, tally's gate; the README's example halts at quorum k=1).
- README.md:47: "at quorum on every pair the tally emits the ranked whole" — contradicted by the README's own I/O transcript at :259; README.md:95 (the service route table): "serve the next under-quorum pair".
ALL one-line re-words, micro; the honest-docs law at each.

## 3. THE STALE COUNTS (the honest-docs fold — banked + one beyond)

- web.py:2 — "the eleven routes" — lived: TWELVE (7 pages + 5 fragments; the unremember fragment the session build added). [banked]
- web.py:8-9 — "the eleven routes (7 pages at honest statuses + 4 rendering fragments at 200" — lived: 12 = 7 + 5. [banked]
- web.py:287-288 — "the nine web routes" — lived: the _WEB_LANES tuple holds TWELVE lanes (the comment two eras stale: the pre-deliberate-lane nine). [banked]
- web.py:527-528 — the refuse docstring: "the nine web routes + the six service routes" — the fourth instance, the same lived twelve. [banked]
- run_store.py:441-444 — BEYOND the banked set: "extract the nine grammar fields (the seven cast fields + the two stamps carried as data + the presentation_order token" — the docstring's own parenthetical enumerates TEN (7+2+1) while the count word says nine; the body extracts ten fields at the bytes (:465-474: vote_id, run_id, pair, winner, comparator_id, comparator_class, recorded_at, notes, supersedes, presentation_order) — the probe's presentation_order grew the count, the word left at the pre-probe nine. The sentence contradicts its own enumeration.
ALL one-line re-counts, micro.

## 4. THE STATED-VS-LIVED DOCSTRING [banked]

**service.py:563-569 — cast_vote's F8-only docstring [banked].** Stated: "the DOOR RECORD'S verified stamps -- comparator_id and comparator_class from the dependency's KeyRecord in place of the body's self-claims (F8: the self-claim dies at the cast door; under the degrade the body's claim stands -- the boot marker names it)". Lived (:581-583): the two-role seam's web-lane exception — under the web key's digest the BODY's comparator_id (the sessioned name) crosses while the KEY's class alone stamps (`_web_lane = bool(record.digest) and record.digest == _WEB_LANE_DIGEST`); the blanket F8 form is no longer the whole truth. CURE: the docstring grown to name the web-lane crossing — a few lines, still micro (the honest-docs law; the mechanism unchanged).

## 5. THE TEMPLATE COMMENTS (the flow-fix's leftovers [banked])

- vote-ack.html:1 — "the verdict restated in item-label terms + the embedded pair fetch" — lived (:5): THREE forms (the chain's next-pair link; the done-page link + the list-has-ended teaching; the embedded fetch at the sitting lane alone). The comment names only the pre-flow-fix form. CURE: one-line re-word.
- pair.html:1 — "the shared pair region: the sitting includes it, the fragment route serves it (web-brief §4 routes 2+7; the design §7a; the voter-session spec §3b)" — lived (:12): the region also carries the flow-fix's hidden chain field (`{% if chain %}<input type="hidden" name="chain" ...>`); the citations predate the flow fix, the carry unnamed. CURE: one-line re-word.
- THE "THIS PAGE" COPY — already cured at the session build: sitting.html:13 and pair.html:5 both read "from this device" (moho's finding 8's widening landed); the banked set's named copy-leftover is NOT live at the templates — the live leftovers are the two COMMENTS above. Named honestly, never assumed.

## 6. THE CLI'S HELP TEXTS (the mint's, the key region's — the post-session truth)

- cli.py:216 (the mint's comparator_id help): "the operator id the key names" — HONEST at the bytes (the record's own field), THIN post-session: at the web lane the key's id is NOT the stamped id (the sessioned name crosses, service.py:581-582; taught at README:149/196, untaught at the flag). No stated-vs-lived gap; the thinness named for the synthesis's ruling.
- cli.py:221 (--class: "the comparator's class (default: human)"), :224 (--audience: "the key's audience tier (default: service)"), :206 (the key group), :215 (the mint's action help) — checked honest at the bytes; the store's refusals teach the legal sets (key_store.py:466-479).
- The CLI's stale helps are the corroboration-class pair at §2 (cli.py:183/184) — the key region clean.

## 7. THE PROBE'S TOOLING (the generated wrappers — the family forms carried from hikari; @generated files: the cure a scaffold re-run at the source, never a hand edit — the standing law)

- test.ts:22 + :44 — STATED: "run all tests or a single test file via Docker" / "[make test-one-docker]" / "inside Docker"; LIVED: the wrapper's own execute runs .opencode/scripts/test_runner.py (:36/:41), whose engine runs `uv run pytest` directly (test_runner.py:14-15); the Makefile has no Docker and no test-one-docker target (its test: `uv run pytest`, Makefile:15-16). The family form carried whole from a tree whose test lane rides Docker. BEYOND-BANKED.
- The closing line "To list every make target, use the `help` tool or run `make help`." — rides calculate.ts:236 [banked: "the calculate help's make-target closing line"] AND patch.ts:43, curate.ts:49, test.ts:44 — LIVED: no `help` tool exists in this tree's wrapper set (13 tools, none named help). The banked instance + three beyond of the same line.
- The helps' usage lines citing "uv run python scripts/<engine>.py" (calculate.ts:236 every op header; the engine's own docstring calculate.py:64; friction.ts:183; curate.ts:49; patch.ts:43; junro.ts:264) — LIVED: the invocation is ".opencode/scripts/<engine>.py" (the wrappers' own runArgv — calculate.ts:70 et al. — the help text and the execute disagree; vote_query.py:67 cites the correct path, the one engine already cured). BEYOND-BANKED.
- calculate.py:418 + :1117 vs :433-434 — "factorial's bound living only in the refusal" [banked]: the non-negative domain is taught only at the refusal (:433-434 "a non-negative integer n (no negative factorial exists)"), the docstring saying "any n" (:418) and the subparser help "n! in exact, arbitrary-precision int" (:1117); the schema's n-describe carries no bound. CURE: the describe line grown at the generation source.

## 8. THE STANDING STATES NAMED (the other legs' grounds confirmed at the bytes)

- THE DONE-PAGE DETOUR [banked, material — moho's leg]: web.py:1082-1083 — the pair fragment's DONE edge still bounces `HX-Redirect: /runs/{stem}/done`, the ack replaced (the confirmation killed — the seven-times-lived finding); the flow-fix's chain lane (vote-ack.html:5) avoids it only when the chain rides. Standing, confirmed at the bytes.
- web.py:389-392 — the boot log line "web tier key: %s (a six-token grant)": the parenthetical is a CONSTANT rendered at both states ("absent (a six-token grant)" at the unwired boot) and the wired key's actual scope count is never read — the claim stated, never derived. BEYOND-BANKED; the micro cure a re-word ("expected: the six-token grant") — the honest statement's "the issuance's honesty" clause adjacent. (The tier cannot read the scopes at boot without the key store — the re-word the honest form, not a scope count.)
- app.js:1-24 — the comment matches the body (pt-copy + the data-pt-path submit delegation); no post-session drift at the bytes; the behavior question rides hyoka's leg. Current.
- The mcp_server prose carries two "F8"s of two eras (the mcp-design's K=10 cap fold at :19; the auth design's corroboration floor at :585-588) — each internally consistent with its era's fold numbering; the collision named, no false statement.
- The corroboration floor's in-source statements (policy.py:69-89, tally.py's fence line :15-19, session.py's rollup) — current, affirmed.
- The README's own trust sections (Auth §"Remains trust" :186-199; Multi-user :209-231) — current, the era-truth told; the README's two stale lines are §2's (:47, :95).

## 9. THE HONEST TABLE (every gap — the file, the line, the stated, the lived, the cure's shape + weight)

| # | file:line | stated | lived | cure (weight) |
|---|---|---|---|---|
| 1 | store_lock.py:10-12 | "CLOSED because all writers are local, none bypasses... external agents speak THROUGH the shared HTTP server" | closure holds by composition; the grounding moved — the armed doors + tokens, TWO HTTP doors; the residual the honest statement's (disk + local machine; the stdio spawn) | one-line re-word (micro) [banked] |
| 2 | store_lock.py:45-46 | "closed because every writer is local and none bypasses the seam" | same era-gap | one-line re-word (micro) |
| 3 | service_store.py:19-21, :61-62 | "every standing writer local, none bypassing the seam" | same | one-line re-word (micro) |
| 4 | mcp_server.py:536-537 | runs.next: "next under-quorum pair... done:true (every pair at quorum)" | served: under-quorum OR uncorroborated; done: quorum AND corroborated | one-line re-word (micro) [banked] |
| 5 | mcp_server.py:634 | runs.tally: "Under quorum the tally SAFE-HALTs" | halts on either leg (the corroboration halt AT quorum is the README's own example) | one-line re-word (micro) |
| 6 | service.py:516 | "Serve the next under-quorum pair" | same class | one-line re-word (micro) |
| 7 | service_store.py:129 | "Serve the next under-quorum pair" | same | one-line re-word (micro) |
| 8 | run_store.py:901-902 | "Serve the next under-quorum pair." | same | one-line re-word (micro) |
| 9 | cli.py:184, :270-275 | "serve the next under-quorum pair" (help + docstring) | same | one-line re-word (micro) |
| 10 | cli.py:183 | --quorum: "votes per pair before coverage" | coverage = quorum AND corroboration | one-line re-word (micro) |
| 11 | README.md:47 | "at quorum on every pair the tally emits the ranked whole" | the corroboration halt first (README's own :259) | one-line re-word (micro) |
| 12 | README.md:95 | "serve the next under-quorum pair" (the route table) | same class | one-line re-word (micro) |
| 13 | web.py:2, :8-9 | "the eleven routes" (7 pages + 4 fragments) | twelve (7 + 5 — the unremember fragment) | one-line re-count (micro) [banked] |
| 14 | web.py:287-288 | "the nine web routes" | twelve lanes in _WEB_LANES | one-line re-count (micro) [banked] |
| 15 | web.py:527-528 | "the nine web routes + the six service routes" | twelve + six | one-line re-count (micro) [banked — the fourth instance] |
| 16 | run_store.py:441-444 | "the nine grammar fields (the seven cast fields + the two stamps + the presentation_order token" | TEN fields extracted; the parenthetical itself sums 7+2+1=10 | one-line re-count (micro) [beyond-banked] |
| 17 | service.py:563-569 | cast_vote: F8-only ("the self-claim dies at the cast door") | the web lane's sessioned id crosses; the key's class alone stamps (:581-583) | docstring grown, a few lines (micro) [banked] |
| 18 | vote-ack.html:1 | "the verdict restated... + the embedded pair fetch" | three forms (the chain link / the done link + teaching / the fetch) | one-line re-word (micro) [banked] |
| 19 | pair.html:1 | the shared pair region (citations pre-flow-fix) | + the hidden chain carry (:12) | one-line re-word (micro) [banked] |
| 20 | test.ts:22, :44 | "via Docker" / "[make test-one-docker]" | uv run pytest direct; no such target, no Docker in the Makefile | generation-source re-run [beyond-banked] |
| 21 | calculate.ts:236 (+ patch.ts:43, curate.ts:49, test.ts:44) | "use the `help` tool or run `make help`" | no help tool in this tree's wrapper set | generation-source re-run [banked at calculate + 3 beyond] |
| 22 | calculate.ts:236 (all op headers) + calculate.py:64 + friction.ts:183 + curate.ts:49 + patch.ts:43 + junro.ts:264 | "uv run python scripts/<engine>.py" | the lived path ".opencode/scripts/<engine>.py" (the wrappers' own runArgv) | generation-source re-run [beyond-banked] |
| 23 | calculate.py:418, :1117 vs :433-434 | factorial "any n" | the non-negative bound taught only at the refusal | describe line grown at the source [banked] |
| 24 | web.py:389-392 | "web tier key: present|absent (a six-token grant)" | the parenthetical a constant at BOTH states; the wired key's scopes never read | one-line re-word (micro) [beyond-banked] |
| 25 | web.py:1082-1083 | the fragment DONE edge: HX-Redirect to /done | the ack replaced, the confirmation killed (seven-times-lived) | the material cure — the synthesis's judgment [banked] |

**THE HEADLINE COUNT: 25 rows.** The banked set confirmed WHOLE — every named item found at its bytes (the store_lock gap, the mcp description, the four web.py counts, cast_vote's docstring, the template comments, the calculate blemishes, the detour). Fourteen rows BEYOND the banked set, the largest class the corroboration-aware drift (rows 5-12: nine surfaces still stating the pre-amendment-22 condition while the core's own docstring tells the new truth — one root, ten citing surfaces with the banked description), then run_store's self-contradicting count (16), the tooling family's carried forms (20-22), and the boot-log constant (24).

**THE WEIGHT:** 23 micro cures (one-line re-words and re-counts + cast_vote's few-line docstring growth) + 2 non-micro: the done-page detour (the material UX cure — moho's leg, the synthesis's judgment) and the generated-wrappers class (rows 20-22 — the cure a scaffold re-run at the generation source, never a hand edit, the @generated law).

**THE SURPRISES:** (1) the drift is TIER-WIDE — amendment 22 updated the core's docstring and left every citing tier stating the old condition, the honest-docs law held at the changed file and missed at the citing files; (2) run_store.py:441's count word contradicts its own parenthetical in the same sentence (nine vs 7+2+1); (3) the web boot log claims "(a six-token grant)" even at "absent"; (4) the test wrapper teaches a Docker lane this tree never had — the hikari family form carried whole; (5) the banked "THIS PAGE" copy is already cured — the live template leftovers are the two COMMENTS.

Provenance: shindan (診断), packet census/state, route prioritree-polish, 2026-11-27. READ-ONLY held — this report the packet's only write. Every line pinned at the tree's bytes this session; the era-truth cited to the records only where the record IS the finding's provenance (the auth era's stated-vs-walked verdict). The tree is the truth.
