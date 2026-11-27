<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/docstrings

**Route:** prioritree-polish (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-27T00:49:16Z |
| 2 | report | rikai | 2026-11-27T00:56:31Z |
## Reported by rikai — 2026-11-27T00:56:31Z

# THE DOCSTRINGS' MAPS — the honest-docs fold's ground itemized (rikai, census/docstrings, prioritree-polish, 2026-11-26)

The mechanism analysis: every public symbol's docstring read against its changed body, every count and pin re-verified at the tree's own bytes this pass (the claims lane — never copied from the banked records; kensho's fold record at the multi-user store reports/validate/voter-session.md §5 the intake, each pin re-read). The four confirmed at the bytes; the beyond-the-four sweep found ten more findings and one pin-drift class; the five-field audit: the session-era and probe-era symbols hold whole, the gaps named at four pre-session web.py symbols.

## 1. THE KNOWN FOUR, MAPPED (each at the tree's bytes this pass)

1. **web.py:2 + :8 — the module docstring's "eleven routes."** Stated: "the eleven routes (7 pages at honest statuses + 4 rendering fragments at 200". Lived: TWELVE — 7 pages (landing :599, sitting :623, done :710, picker :751, deliberate :792, progress :872, result :909) + 5 fragments (register :1001, pair :1059, vote :1106, state :1193, unremember :1217) — the un-remember lane the session era's twelfth. Honest rewrite: "the twelve routes (7 pages at honest statuses + 5 rendering fragments at 200 — register, pair, vote, state, unremember)" — two one-line cures (:2's head, :8's clause).

2. **web.py:287 — the lanes comment's "the nine web routes."** Stated: "the nine web routes (the child's own path constants above)" — the web-brief §3e citation true (the law's home; nine lived at that era), the count stale. Lived: _WEB_LANES :291-304 carries TWELVE entries. Rewrite: "the twelve web routes" — one word.

3. **web.py:527 — the refuse docstring's "the nine web routes + the six service routes."** The fourth instance, kensho's own find, CONFIRMED at my read: the docstring's next_action account vs UNION_LANES :313, which composes _WEB_LANES (twelve) + _SERVICE_LANES (six, :305-312 — the service six byte-true). Rewrite: "the twelve web routes + the six service routes" — one word.

4. **service.py:558-578 — the cast_vote route docstring's F8-ONLY account.** Stated: "comparator_id and comparator_class from the dependency's KeyRecord in place of the body's self-claims (F8: the self-claim dies at the cast door; under the degrade the body's claim stands — the boot marker names it)". Lived: the two-role seam :581-583 — `record.digest == _WEB_LANE_DIGEST` (the marker :136-149) rides the BODY's comparator_id (the sessioned name the web tier composed at web.py:1135-1147); every OTHER keyed caller's record id stands; the class ALWAYS the record's (when a digest exists). Site named honestly: the F8-only docstring lives at the service.py cast DOOR (the route handler); votes.py:475's seam docstring and session.py:298's delegation docstring carry NO F8-only claim (read whole — the seven-stage chain and the verbatim-delegation accounts are true). Rewrite: the docstring grows the web-lane sentence (kensho's ruled shape): "the web lane's callers alone (the digest match at _WEB_LANE_DIGEST, :136-149's marker) ride the body's comparator_id — the sessioned name the web tier composed; every other keyed caller's record id stands; the class always the record's."

## 2. THE BEYOND-THE-FOUR SWEEP — every module's docstrings vs the eras' changes

**The auth build's modules — HELD:** key_store.py, key_verify.py, policy.py, mcp_auth.py read whole — every claim true at its own door (F8's "no claim parameter exists" true at key_verify.py:141-207; the mcp adapter's F8 true at its own lane — the session never rides the mcp tier; the grant map's five + the manifest absence named). **service.py's status-mapping paragraph (:16-50) — VERIFIED: never amended at the fold** — it stands as the auth era wrote it, its own account TRUE (the session era added no status; 200/201/401/403/404/405/422/409/500 unchanged); the two-role seam's account lives at the :136-149 comment and the cast docstring's cure (finding 4) — the module docstring carries no web-lane account (an absence, stated as fact). **mcp_server's stamping delegation (:578-595) — the cast docstring (:567-577) TRUE at its door** (the token's claims at the authenticated door; the degrade's fallback; the session era never touched this lane); the :581 comment's pin drifts (below).

**The session build's regions — the five-field form held** (§3). The mount (:347-361) and the assert-guard (:362-374) are module-level STATEMENTS carried by comments — the guard's refusal the ThreePart bytes in the raise (:369-373); the un-remember route (:1219-1238) five fields whole.

**The probe's tooling — THREE CLI findings + one mcp model finding + one mangled sentence:**

5. **web.py:1067-1070 — the pair fragment's docstring, the DONE sentence SPLIT by the probe-era insertion.** The swap sentence ("swap the query knob: the pair PRESENTED in the swapped order...") was inserted INSIDE "the HX-Redirect RESPONSE HEADER to the done / page (core HTMX's navigation verb — no extension, no JS)" — the DONE clause broken mid-sentence ("the done [swap sentence] page"). Both claims true; the prose mangled. Rewrite: the DONE sentence rejoined; the swap sentence its own.

6. **cli.py:145-147 — _build_parser's grammar unnamed flags.** Stated: "next: run_id + --seed type=int default None; vote: ... + --notes/--supersedes default None". Lived: next carries --swap (:187), vote carries --presentation-order (:197-201) — both probe-era instruments. Rewrite: the grammar's account grows the two flags.

7. **cli.py:269-286 — _command_next's swap unnamed.** Stated: "print pair\t{item_a}\t{item_b}\t{count} — the serve triple whole". Lived: :291-292 `if args.swap: item_a, item_b = item_b, item_a`. Rewrite: the Purpose grows the swap sentence.

8. **cli.py:297-313 — _command_vote's presentation_order unnamed + the "served canonical order" wording.** Stated: "the pair's two positionals in the served canonical order". Lived: the body passes args.presentation_order (:325); the served order can be swapped (both-orders experiment); the door maps presented→canonical (votes.py:499-505). Rewrite: the Purpose grows the presentation_order sentence; "served canonical order" → "served order (canonical or swapped)".

9. **mcp_server.py:169 — NextInput's docstring vs the swap field.** Stated: "the next tool's body: the run id and the optional seed". Lived: THREE fields — run_id, seed, swap (:171-173; the tool consumes body.swap at :554). Rewrite: "the run id, the optional seed, and the optional swap". (CastInput's summary :177 — milder: "the pair, the verdict, the stamps, the correction" leaves presentation_order unnamed in the enumeration, though the Field's own description TEXT_PRESENTATION :123 carries the teaching — a same-class candidate.)

**The banked mcp description — CONFIRMED at the bytes:**

10. **mcp_server.py:536-537 — the serve tool's description "(every pair at quorum)".** Stated: "call until done:true (every pair at quorum), then runs.tally". Lived: done:true fires at quorum AND CORROBORATION — session.py:284's expected field: "all {len(queue)} scheduled pairs at quorum k={manifest.quorum} AND corroborated (>=1 human AND >=1 llm per pair)" (amendment 22's extension; the corroboration named at session.py:61/:254-255, tally.py:528, web.py:716 — the serve tool's description ALONE stale). Rewrite: "(every pair at quorum AND corroborated)" — two words.

**Same-class candidates (the synthesis's ruling):**

11. **mcp_server.py:634 — the tally tool's "Under quorum the tally SAFE-HALTs".** The halt's condition: ANY coverage leg fails (zero-coverage, connectivity, quorum, corroboration — tally.py:472-477, AND-composed); "Under quorum" names one leg as the trigger, the runtime refusal teaching all legs (the two gap kinds taught distinctly, tally.py:485-487). Weaker than #10 — the refusal's own render carries the truth.

12. **service_store.py:63-66 + :169-170 — the ride-through enumerations omit SupersedeRefusedError.** Stated: "the door's refusals (VotesRefusedError, TallyRefusedError, ExhaustedQueue) and the store's own (StoreRefusedError) ride through verbatim BY TYPE" (the seam's class docstring); the cast verb's Refuses-when names "the door's (VotesRefusedError)" alone. Lived: the cast verb passes supersedes (:157/:184); the door raises SupersedeRefusedError (votes.py:175, the serving-tier era's addition — the verb's own eight-argument form WAS named in the same docstring, the enumeration never widened); the seam passes it through unwrapped (caught at service.py:599-600 → 403, at mcp_server.py:609-612 → PermissionDenied; at the CLI uncaught → exit 2, the unexpected channel — the CLI's own claim true as written, below). Rewrite: both enumerations grow SupersedeRefusedError.

**THE PIN-DRIFT CLASS — docstrings citing other files' line-ranges the eras moved (each pin re-read at the current bytes):**

13. The auth era pushed render_refusal: **mcp_server.py:15** cites "service.py:168-183" — render_refusal now at service.py:291 (:168-183 today is CastVoteRequest's docstring region). The session era pushed the stamps' school: **mcp_server.py:581** cites "service.py:527-528's school" — the two-role seam now at :581-583 (:527-528 today is the serve docstring's refusal lines). The corroboration era pushed the tally render members: **mcp_server.py:344** "tally.py:226-259" → _components now :243; **:378** "tally.py:331-360" → _found_sections now :344; **:414** "tally.py:363-395" → _next_action_sections now :381. The probe era (run_store's presentation_order field helpers, :293-369) pushed the run_store internals the auth-era docstrings cite: **key_store.py:76-77** + **key_verify.py:54/:69/:91-92/:107** "run_store.py:62-93"/"79-93" (StoreRefusedError) → now :77; **key_store.py:137** "96-109" (_repair_path) → now :111; **key_store.py:173/:241** "146-171" (_require_str_field) → now :161; **key_store.py:204** "322-351" (_require_verdicts_field) → now :372; **key_store.py:324** "470-504" (Persist) → now :523; **:342** "506-525" (__init__) → now :536; **:367** "580-714" (load) → now :634; **:453-454** "716-744" (_append_line) → now :776; **web.py:27** "STORE_HOME run_store.py:53" → now :67; **store_lock.py:63-64** "run_store.py:48-53" → now :67, "service_store.py:77-80" → now :84-85; **store_lock.py:9-10/:13-14** "service_store.py:59-60" → the clause now :66, ":19" → :15 (soft — same docstring, off by lines). Cure shape: each pin re-derived at the current bytes (micro-cures, one line each) — or the class ruled at the synthesis (the pins' school).

**HELD (named to fence the sweep):** votes.py, session.py, tally.py, run_store.py, registry.py, scheduler.py, service_store.py's verbs, acceptance.py, budget_curve.py, __init__.py — the probe-era and corroboration-era additives named whole in their docstrings (votes.py:19-29 the presentation_order datum; run_store.py:22-25; service_store.cast :167-168; session.cast_vote :313-314; service.serve :519-523; CastVoteRequest :184-188; tally's four-leg gate :472-477); the CLI's four-refusals claim TRUE at the bytes (cli.py:12 + command() :462-463 match the catch :499 exactly — StoreRefusedError, VotesRefusedError, TallyRefusedError, KeyStoreRefusedError; the session era added no CLI-typed refusal; the door's fifth, SupersedeRefusedError, rides the exit-2 unexpected channel — the claim true as written, the mechanism stated); store_lock.py's own docstring consistent with its body (the stated-vs-armed trust comment shindan's charge, not a docstring).

## 3. THE FIVE-FIELD AUDIT — the new public symbols

**The session era's — HELD WHOLE:** _boot_secret (web.py:129-142), _remembered (:172-183), _remember (:186-201), _mint_bound (:229-245), the un-remember route (:1219-1238) — all five fields (Purpose / Refuses when / Re-run / Touches / Provenance); the mount and the assert-guard module-level statements carried by comments (the law binds symbols). **The probe era's — HELD WHOLE:** VoteRecord (votes.py:78-99), CoverageDatum (tally.py:63-80), the seam verbs' five-field docstrings whole. **THE GAPS (all pre-session symbols, named):** **web.py:585-592 refuse_csrf** — the drive-by's own handler, ONE field (Provenance; Purpose/Refuses when/Re-run/Touches absent) — the ONLY exception handler off the form (refuse :519-536 and fold :552-568 both carry five); **web.py:204-214 CsrfRefusedError** — the public class, TWO fields (Purpose/Provenance; its typed-refusal peers — KeyVerifyError, KeyScopeError, KeyStoreRefusedError, VotesRefusedError, SupersedeRefusedError — all carry five), its __init__ :217 a one-liner; **web.py:250-268 _csrf_guard** — private, THREE of five (Re-run/Touches absent); **web.py:224-226 _mint_csrf** and **:479-485 _auth_page** — private, the form abbreviated (the law's scope named: it binds PUBLIC symbols). The mcp models' one-line docstrings (mcp_server.py:148-254) — the unit's ruled spec form; NextInput's summary gap at finding 9.

## 4. THE HONEST TABLE — every docstring finding, the one-line cure or the field-grown form

| # | Symbol / site | Line | Stated form | Lived form | Honest rewrite's shape |
|---|---|---|---|---|---|
| 1 | web.py module docstring | :2, :8 | "the eleven routes (7 pages + 4 fragments)" | 12 routes (7 pages + 5 fragments: register, pair, vote, state, unremember) | "the twelve routes (7 pages + 5 rendering fragments)" — one word, two lines |
| 2 | web.py lanes comment | :287 | "the nine web routes" | _WEB_LANES :291-304 = 12 | "the twelve web routes" — one word |
| 3 | web.py refuse docstring | :527 | "the nine web routes + the six service routes" | UNION_LANES :313 = 12 + 6 | "the twelve web routes + the six service routes" — one word |
| 4 | service.py cast_vote docstring | :558-578 | F8-only: "the stamps from the KeyRecord in place of the body's self-claims" | the two-role seam :581-583 — the web lane's body id rides; every other keyed caller's record id stands; the class always the record's | the docstring GROWS the web-lane sentence (kensho's ruled shape) |
| 5 | web.py pair docstring | :1067-1070 | the DONE sentence split by the swap insertion ("to the done [swap] page") | both claims true, the prose mangled | the DONE sentence rejoined; the swap its own sentence |
| 6 | cli.py _build_parser | :145-147 | the grammar without --swap/--presentation-order | :187 + :197-201 carry both | the grammar's account grows the two flags |
| 7 | cli.py _command_next | :269-286 | the serve triple, the swap unnamed | :291-292 swaps the presented pair | the Purpose grows the swap sentence |
| 8 | cli.py _command_vote | :297-313 | "the served canonical order"; presentation_order unnamed | :325 passes presentation_order; the served order can be swapped | the Purpose grows the presentation_order sentence; the wording to "served order (canonical or swapped)" |
| 9 | mcp_server.py NextInput | :169 | "the run id and the optional seed" | three fields (:171-173: run_id, seed, swap) | "the run id, the optional seed, and the optional swap" |
| 10 | mcp_server.py serve tool | :536-537 | "done:true (every pair at quorum)" [the banked finding] | quorum AND corroborated (session.py:284) | "(every pair at quorum AND corroborated)" — two words |
| 11 | mcp_server.py tally tool | :634 | "Under quorum the tally SAFE-HALTs" | any coverage leg fails (tally.py:472-477) | a same-class candidate — the synthesis's ruling |
| 12 | service_store.py class + cast | :63-66, :169-170 | the ride-through enumerations without SupersedeRefusedError | the door raises it (votes.py:175); the seam passes it through | both enumerations grow SupersedeRefusedError |
| 13 | the pin-drift class | mcp_server :15/:344/:378/:414/:581; key_store :76/:137/:173/:204/:241/:324/:342/:367/:453; key_verify :54/:69/:91/:107; web :27; store_lock :9/:13/:63 | the line-ranges as written | the cited members moved (the probe/auth/corroboration/session eras) | each pin re-derived at the current bytes — micro-cures, or the class ruled |
| 14 | web.py refuse_csrf | :585-592 | one field (Provenance) | the handler renders the fragment at 200 | the four fields grown to the peers' form (refuse/fold's school) |
| 15 | web.py CsrfRefusedError | :204-214 | two fields (Purpose/Provenance) | the typed refusal carries three fields | Refuses when/Re-run/Touches grown — the typed-refusal family's form |

None of the fifteen blocks the floor — doc-drift, never behavior (the suite/lint/typecheck green at kensho's and moho's runs, the record's). The four banked instances confirmed at the bytes; the fold's charge itemized whole for the synthesis's ranking.

— rikai (理解), the mechanism whole; the disk the truth, every read at the cited bytes this pass; READ-ONLY held, this report the packet's only write.
