<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — evaluation/session-residuals

**Route:** prioritree-multi-user (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-26T17:26:02Z |
| 2 | report | shindan | 2026-11-26T17:43:49Z |
## Reported by shindan — 2026-11-26T17:43:49Z

# THE RESIDUAL DIAGNOSIS — the candidates' residual exposure, the honest statement drafted (shindan, packet evaluation/session-residuals, route prioritree-multi-user, 2026-11-26)

The ground read whole: togo's research brief (reports/synthesize/multi-user-research.md — the candidate field three, the divergences, the opens); this seat's own threat model (reports/research/session-threat-model.md — the classes, the seam question §2.4, the residuals §4); the legs' reports (tansa's census reports/census/identity-surfaces.md; moho's walk reports/research/identification-walk.md; keisan's arithmetic reports/research/session-arithmetic.md; rikai's mechanism maps reports/research/session-mechanisms.md); the auth precedent's honest statement (.plans/ideation/2026-11-24-prioritree-auth/reports/synthesize/auth-design.md §3 — the cures/carries/opens form). READ-ONLY held; this report the packet's only write. This seat diagnoses — never prescribes: the fixes and the rulings are the design gate's own acts; what follows states WHAT STATE IT IS IN, every row evidence-backed.

## 1. THE RESIDUAL MAPS — every candidate's residual state after the session lands (or does not)

### Candidate (i) — the signed-cookie session

| The residual's row | The honest state, priced at the evidence |
|---|---|
| REACHABLE: the local process class | NO NEW REACH at the loopback bind (threat model §1.3/§3.2): the cookie's thief class IS the class that can already vote directly through the wire and read the store home (a plain directory); the cookie adds a READABLE artifact, never a new capability; HttpOnly/SameSite priced at ZERO risk reduction at this bind (HOST ?= 127.0.0.1), born meaningful at the TLS/LAN rebind (HOST=0.0.0.0). |
| REACHABLE: the remote classes | the loopback keeps them dead; the drive-by cured by the standing CSRF guard (web.py:946, before _service — the write never lands) with SameSite as the second leg; the sitting's READ capability unchanged (anonymous GETs stay — the share-by-design form intact). |
| IDENTIFIABLE: the readable payload | the cookie carries the comparator name's bytes client-side — b64(json)+TimestampSigner.sign (sessions.py:70-71): readable by the holder and any local process reading the cookie store or the wire; tamper-CURED, never tamper-hidden; 72-92 B on the wire inside a 137-B Set-Cookie — noise. |
| IDENTIFIABLE: the persistent self-claim | the name now PERSISTENT (max_age default 14 days, sessions.py:22): the drift per sitting cured (the browser-pinned pseudonym), the persistence itself a new exposure axis — the typo remembered, the stolen cookie's long ride (the 14-day window). |
| FORGEABLE: the fabrication class UNCHANGED — THE HARDEST LINE | the name still a self-claimed STRING — no account, no secret; k fabricated voters still k identifications (each a name typed once, then carried); THE SESSION CURES THE UX COST, NEVER THE IDENTITY FABRICATION; the pseudonym binds the browser, never the human — multi-human-per-browser merges into one voter, multi-browser-per-human splits one human into k voters (visible in the id, never hidden). |
| FORGEABLE: the cookie itself | tamper-cured by the signature (any payload byte change breaks the HMAC); THE TAMPER-SILENCE residual: a forged cookie NEVER raises — `except BadSignature: scope["session"] = Session()` (sessions.py:56-57) — it silently becomes a fresh empty session, the visitor re-identifies, no alarm, no log line. |
| The logout bound | no per-session server kill without a store — a stolen signed cookie rides until the max-age (14 days by default) or the secret's rotation; the correction verb's mechanism prices accordingly (an earn the build set must rule). |
| The carried knobs' prices | the secret's env-or-boot-mint form (the CSRF precedent web.py:119-120: boot-mint = 88 keystrokes of re-identification per restart at the 8-browser fence; env = $0, 0); the concurrent-write race (last-write-wins on the identity map, NEVER a vote); the ~4KB cookie budget (identity bytes-trivial); the ±2-B base64 unpadding variance (UNVERIFIED at this tree — itsdangerous absent; verify at the build). |
| The dependency door | itsdangerous NOWHERE in uv.lock nor site-packages — the middleware UNIMPORTABLE at the current venv until the wheel joins [project] dependencies; one pure-Python wheel, no service, no infra — a build blocker, never an exposure residual. |
| What (i) cures whole | FR-MEM-0041's cost dead (78 identifications → 1); the render boundary crossed (both lanes at the one template seam — sitting.html's ask retires); the fixation surface BORN CURED (mint-at-identification; the pre-identify browser carries nothing to fixate); the entropy home (the CSRF token's per-session binding possible); the drift pinned; RESTART-PROOF by construction (no server state). |

### Candidate (ii) — the server-side memory store: (i)'s map plus its own two prices

| The residual's row | The honest state, priced at the evidence |
|---|---|
| (i)'s map carried | the same reachable/forgeable rows — the local class's no-new-reach; the fabrication class UNCHANGED (the name still a self-claim at the store's back door); the forged-id silence (an unknown opaque id falls to a fresh identification, no alarm); the carried knobs. |
| What (ii) NARROWS vs (i) | the READABLE PAYLOT leg cured (the cookie carries only an opaque random id — the name never client-side: read-side opacity, a privacy gain); the LOGOUT BOUND cured (the store is the oracle — a per-session server kill EXISTS; the correction verb's mechanism native). |
| THE RESTART-LOSS | the dict dies with the process — every visitor re-identifies at every boot: FR-MEM-0041's form AGAIN at a coarser cadence (the once-per-browser promise becomes once-per-process-lifetime); at the 8-browser fence every restart re-demands the identification the session was built to ask once; a persistence layer (a JSONL store, the run_store school) cures the loss at the price of a THIRD STORE HOME plus its lifecycle. |
| THE SINGLE-PROCESS BINDING | N workers fork the dict and diverge the identities — viable ONLY under the tree's single-process truth (Makefile:34 `env -u WEB_CONCURRENCY`; uvicorn's rule at config.py:358-359: unset ⇒ ONE worker); the env-unset law the only guard between the design and the divergence hazard; the signed-cookie form carries no such binding (stateless by construction). |
| The fixation surface's shape | an opaque id forgeable-by-capture, the store the oracle — a DIFFERENT animal, not a worse one (the brief's own words); the mint discipline unchanged (never a client-accepted id). |

### Candidate (iii) — the per-operation status quo: the non-completeable standing

| The residual's row | The honest state, priced at the record's own bytes |
|---|---|
| THE STANDING | refused at the record: 0 of 78 swapped judgments landed (RUN-0008.jsonl: 235 lines = 1 manifest + 234 votes; VOTE-0157..0234 = 78/78 at the sitting chain's carried form by the same human the same day the same run) — the abandonment preceded the first landed vote (the human met the first fresh form, priced the demand's repetition, refused the task ENTIRE); the run blocked at 234/312; the probe's datum deferred. |
| The measured cost | 390 identification acts vs 78 judgment clicks (5:1); 858 keystrokes at "Mark Losey" = 36.7% of the card's duration, 98.7% pure repetition; 156 context transitions; the collaborator's verbatim: "having to re-enter voter name each time basically makes the task non-completeable... too much work on the human." |
| The exposure rows, stated honestly | the fabrication class EQUALLY OPEN (self-claims at the wire — k fabrications still k identifications) PLUS the drift per sitting (the re-typed claim can vary — one human splits into many ids by typing variation, the duplication INVISIBLE); the identity's every carry dying at the render boundary (tansa's census: 12 per-operation identity surfaces, 0 carries surviving navigation, 0 cookie surfaces). |
| The one honest strength | every vote's identity explicit and confirmable at each act — no silent bleed (the shared machine), no typo permanence (each act fresh); the trade the session makes explicit, never hidden. |
| THE ROW'S VERDICT | the residual that matters is not exposure but REFUSAL — the work not done; the option's mechanism is the ABSENCE of a session, priced at the measured cost, not an estimate. |

## 2. THE SEAM QUESTION RESOLVED-READY — the three forms' residual states (the design's own act; this diagnosis the ground)

The door today (service.py:564-565): `comparator_id = record.comparator_id if record.digest else body.comparator_id` — F8: the verified record's stamps REPLACE the body's claims at the armed door; the web tier's in-process client carries ONE key (web.py:239-245), so under auth-on EVERY browser's vote lands as the web key's one named comparator, the typed names discarded; under the auth-off degrade the body's self-claim stands. The three priced forms, each residual stated precisely:

| The form | The record's state | The residual, precise |
|---|---|---|
| (A) THE SESSION ID CROSSES (the door gains a seam) | the sessioned id rides onto the record as the vote's comparator_id — THE VOTES RECORD THE BROWSER'S SELF-CLAIM; the key's class verification UNCHANGED (the class still the key record's verified stamp — F8 held at the class axis; the llm-class constraint mechanical: the browser never claims a class) | the id-binding residual at its NARROWEST: the record's identity a persistent, browser-pinned, self-claimed pseudonym — drift cured, the duplication visible in the id (two browsers, two ids) — yet UNCHANGED IN KIND: never verified, the fabrication class untouched; the key's own identity silent at the record (the vote line does not name which tier-key authenticated the vote — the crossing's plain substitution leaves the provenance unwritten) |
| (B) THE KEY'S ID STAYS (the session stays web-tier-only) | the door's law unchanged; the session pure UX at the web tier (the once-per-browser ask, the pre-fill); under auth-on every vote stamps the web key's one comparator_id | the multi-user truth INVISIBLE in the data — the vote log cannot distinguish N humans from one; the two-browser duplication UNCOUNTABLE (the per-browser signal absent: the duplication indistinguishable from one identity's re-votes); the id-binding residual at its widest-for-humans form (one collapsed identity for every browser — moho's collapse: multi-user impossible by construction at the record; the session's whole purpose refused at the seam) |
| (C) THE TWO-ROLE COMPOSITION (moho's composed form) | the id from the session, the class from the key — EACH ROLE NAMED: the record's semantics carry both layers' truth distinctly (WHO: the sessioned per-browser self-claim; WHAT CLASS: the door's key-verified stamp — the two roles the walked code already separates, composed at the record, never silently merged) | the id axis form (A)'s self-claim (never verified, the fabrication class unchanged); the class axis verified (the constraint held mechanically); the record's semantics the honest carrier — the provenance NAMED in the data (the self-claim visible as self-claimed, the verified class visible as verified); the most legible residual of the three: the record says exactly what it knows and what it merely carries |

THE RECOMMENDATION'S GROUND (stated, never prescribed): forms (A) and (C) carry the multi-user truth into the data — the duplication visible, the corroboration countable per browser, the id-binding residual at its narrowest and (at C) named per role; form (B) cures the UX but leaves the record blind to the humans — the effort's own purpose (multi-user BUILT-IN) refused at the seam. EITHER WAY the class verification stands (F8) and the llm-class constraint holds (the session the HUMANS' lane; the llm votes ride the stdio/tools keys, never the browser).

## 3. THE HONEST STATEMENT DRAFTED (per the auth precedent's cures/carries/opens form — the README's future unit will carry it; drafted now at the record)

**THE SESSION CURES:**
- the lived cost — FR-MEM-0041 dead: 78 identifications → 1; the 0/78 predicted 78/78 at the same hands; RUN-0008's completion unblocked (234/312 → 312/312); the register's quorum>1 promise ("share this sitting URL with your other judges") finally served by the form instead of refused by it.
- the render boundary — the identity carried across every page load (the DOM carry's page-lifetime limit crossed by the cookie); both lanes cured at the one template seam (sitting.html's ask retires; the deliberate lane's per-visit cost dead with it).
- the entropy home — the CSRF token's per-session binding possible (a scraped token useless in another browser, a leaked token dead at the session's death; today a leaked token a permanent forgery primitive for that path until the boot's secret changes).
- the fixation surface — born cured at the mint-at-identification (the pre-identify browser carries nothing to fixate); the identity drift per sitting pinned (the browser-bound pseudonym).
- THE HONEST VERDICT AT THIS BIND: UX-FIRST, SECURITY-SECOND — the loopback keeps the remote classes dead, the local class already owns the machine; the session's security value prices in at the LAN rebind era.

**THE SESSION CARRIES:**
- the self-claimed pseudonym — persistent, NEVER verified: no account, no secret; the fabrication class untouched (k fabrications still k identifications); the trust narrows to the typing human's honesty — the free-tier spirit's own shape, carried openly.
- the browser binding — the pseudonym binds the browser, never the human: multi-human-per-browser merges into one voter (the shared machine's silent bleed — the second human's votes ride the first's name); multi-browser-per-human splits one human into k voters (visible in the id, never hidden); the tally counts VOTES, never minds.
- the readable payload — the name's bytes client-side in the cookie (tamper-cured, readable by the holder and the local class); the register's operator a PRE-FILL at most, never a silent substitute (web.py:885 — two identities, two surfaces, one browser).
- the local trust — the cookie a readable artifact beside the sitting URL, adding NO new reach at the loopback (the class that can read it can already vote directly and read the store); the mitigations aim at the classes the bind keeps out (the LAN after a rebind, the drive-by over the wire).
- the knobs' prices — the secret (env-or-boot-mint: the restart-invalidation carried honestly; env $0), max_age 14 days (the sitting covered 1550×; a 14-day stolen-cookie window), SameSite=Lax (the shareable URL's top-level entry preserved), the tamper-silence (the forged cookie re-identifies, no alarm), the logout bound at [i] (no per-session server kill without a store).

**THE SESSION OPENS:**
- the second capability artifact — the cookie beside the sitting URL: a stolen cookie rides until the max-age or the secret's rotation; the fixation discipline's standing duty (never a client-accepted id — one design slip reopens the class).
- the persistence of mistakes — the typo remembered (a "makr" rides every vote until noticed; NO correction surface walked — the logout/correction surface an EARN the build set must rule); the expiry untaught (the mid-sitting death's bare re-ask — the teaching an earn); the shared machine's silent bleed (the per-operation form's explicitness traded for flow).
- the naming hazard — the tree already owns "session" (session.py the library's U5 chain composition); the new symbol minted per the naming law from its act-statement.
- the seam question itself — the record's identity composition RULED at the design gate, never assumed (§2's three forms the ruling's ground).

**THE HARDEST LINE (the statement's own):** the session cures the UX cost, NEVER the identity fabrication — the record's identity a browser's self-claim, persistent and pinned, never verified; the corroboration story's strength lives at the CLASS axis (the key's verified stamp), never at the ID axis (the self-claim). The auth precedent's parallel carried: "the auth cures the wire; the disk and the local machine remain trust" — the session cures the ceremony; the identity's honesty remains the human's own.

## 4. THE CONCURRENT-HUMANS STATE — the multi-user truth's honest face under each candidate

| The row | The honest state |
|---|---|
| THE STANDING SEMANTICS | the tally counts VOTES, never distinct authors (zero dedup anywhere in the tree — the auth precedent's standing statement); the corroboration floor counts CLASSES (the human/llm pair rollup over policy.missing_classes), never identities — TRUE UNDER EVERY CANDIDATE; the session neither cures nor worsens the count semantics. |
| Under (iii) | the duplication already possible and INVISIBLE (two browsers, two fresh self-claims — the drift compounding: one human splits into many ids by typing variation); the multi-user promise refused by the form itself; the corroboration floor one human's 13 min. |
| Under (i) | the duplication VISIBLE in the id (two votes, one comparator_id where one independent human sits — the datum count inflated 2×; 26 min of duplicated human time where 13 min of judgment lives); the second browser's ceremony priced DOWN (one identification per browser — the convenience real); whether the quorum counts votes or distinct voters the DESIGN's own act (a per-voter floor over distinct sessioned ids a possible composition, never prescribed here). |
| Under (ii) | (i)'s rows plus the restart-loss's multi-user face: a mid-sitting boot kills EVERY judge's session at once — all re-identify (the coarser cadence's concurrent cost); the single-process binding the fence the whole sitting rides on. |
| THE CORROBORATION STORY'S STRENGTHENING | the floor splits 78/N (2 humans → 39 pairs each; 5 → 15.6; 8 → 9.75 ≈ 1.6 min each where one human carries 13 min) — the floor never inflates with headcount, it parallelizes; the story (>=1 human per pair) unchanged, the burden divisible. THE RESIDUAL'S HONEST FACE: the corroboration depth counts votes per class, never independent MINDS — two browsers' votes from one human deepen the depth without adding an independent observer; the class axis verified (the key), the independence axis unverified (the self-claim); the multi-user truth strengthens in burden-sharing and visible multiplicity, never in verified independence. |

## 5. THE VERDICT — the residuals ranked (the honest condition ordered; the recommendation suisen's act, the ruling the design gate's)

- **(iii) ranked LAST**: the residual is the refusal itself — the non-completeable standing measured at the record's own bytes (0/78 against 78/78 at the same hands); no exposure refinement buys back a task the human will not do.
- **(ii) ranked MIDDLE**: it narrows (i)'s readable payload and cures (i)'s logout bound, but buys them at the RESTART-LOSS (FR-MEM-0041's form again at a coarser cadence — the very cost the effort exists to kill, returning at every boot) and the single-process binding (the whole sitting fenced on the env-unset law); the persistence cure prices as a third store home plus its lifecycle.
- **(i) ranked FIRST on the residual axis**: the smallest exposure set against the effort's own purpose — restart-proof by construction (the once-per-browser promise held across boots), the statelessness matching the tree's single-process truth with no new binding, the residuals all priced and none blocking: the readable payload, the tamper-silence, the logout bound, the carried knobs — each named, each priced.
- **THE FABRICATION CLASS UNCHANGED UNDER EVERY CANDIDATE** — the hardest line, the statement's own: (iii) carries it open at the wire with drift compounding; (i)/(ii) carry it persistent and browser-pinned; no candidate verifies the human — the id-binding residual is narrowed, never erased.
- **The seam's ranking (the ground, never the prescription)**: the crossing forms (A)/(C) carry the multi-user truth into the data with the id-binding residual at its narrowest and (at C) named per role; the non-crossing form (B) cures the UX and refuses the story at the record — the collapse's residual (the multi-user truth invisible, the duplication uncountable) the heaviest the seam can carry.
- **THE DESIGN GATE'S GROUND WHOLE**: every candidate's residual mapped (§1); the seam's three forms priced precisely (§2); the honest statement drafted in the auth precedent's form for the README's future unit (§3); the concurrent-humans truth stated without flattery (§4); the residuals ranked (§5). The id-binding residual rides every form — narrowed, never erased; the record's honesty names that price publicly. The ruling is the design gate's own act; this diagnosis its whole ground.

— shindan (診断), the diagnosis whole; every row cited to the legs' evidence and the tree's own bytes; the honest condition stated, nothing prescribed.
