# understand/votes — the votes unit's mechanism analysis

**Seat:** rikai (理解) · **Packet:** understand/votes · **Route:** prioritree-core (U3) · **Date:** 2026-11-20. **Landing:** returned in-message at execution (the pack is read-only); landed by shinko via patch, verbatim; read-back verified.

**Ground read whole:** the core store's junro.json (G-VOTES's five conditions :195-203; the build/votes increment :130-147), the birth store's junro.json (the solution-space ruling — R4/R5/R9 :563-568; the resolution :587, :695-700), scope-synthesis.md (§3.2 ops 3-4 verbatim :132-133; §3.4 the hazard fold-ins :150-156; PART 4 :171-176), registry.py (RunManifest, read_manifest, RegistryRefusedError, the container form, the mint precedent), scheduler.py (Pair, schedule_pairs — the legal pair set), understand/scheduler.md (seam (b) — the counts-map consult). Tool-verified arithmetic rides the calculate runs.

**Absences stated as facts:** src/prioritree/votes.py does not exist; tests/test_votes.py does not exist; discover/votes.md landed in parallel (amendment 25's co-derivation form); G-VOTES-BRIEF unlanded.

## 1. THE CAST_VOTE CHAIN — payload in → handle + count out

**The payload** [STATED, scope-synthesis.md:132]: cast_vote(run_id, pair, winner, comparator_id, comparator_class, notes?) → VOTE-{####} + post-append ledger count. The only stochastic-side entry point and the only op that mutates the vote ledger; ingestion is independent of the scheduler — a vote is valid on any registered pair ("the scheduler suggests; it does not confer permission").

**Seven stages, every refusal before any byte lands (the registry precedent):** (1) Schema validation [DERIVED, the registry school]: run_id a non-empty stripped string (the _require_text precedent); pair a Pair instance or a 2-length sequence of strings (the dual-form _coerce_rows precedent); winner a string; comparator_id non-empty stripped; comparator_class ∈ {human, llm} — a module-level frozenset constant (content-in-configuration); notes any string, stored verbatim (opacity); the optional supersede reference a string handle. Malformed → expected/found/next-action naming the schema's public types. (2) Ground-truth: run live [STATED]: read the manifest via read_manifest(run_id) — unknown run raises naming the live handles; the lookup happens INSIDE the write path (FR-MEM-0001: validate against the store's own truth, never the payload's provenance). (3) Ground-truth: pair ∈ the legal pair set [STATED]: enumerate schedule_pairs over the manifest's item ids, membership-test the cited pair by canonical-form equality (Pair is hashable by construction). A pair outside the set is refused naming the legal set's source; a SWAPPED citation ("b","a") is not in the canonical set and is refused naming the canonical form — never silently re-ordered: the verdict vocabulary is positional over the form ("a" = the lexicographically smaller id), so a swap + "prefer-a" is semantically ambiguous — refusal maps the gap. (4) Ground-truth: winner ∈ the declared verdict set [STATED]: the check reads manifest.operator.verdicts — the run's own frozen frozenset, never the module constant directly; at birth always the weak-order triple. Refusal names the declared set. (5) Idempotent dedup — the canonical-content key [DERIVED]: the key = every field the caller authors, in validated canonical form — (run_id, canonical pair, winner, comparator_id stripped, comparator_class, notes verbatim, supersede reference); excluded = every field the store mints (the VOTE handle, the recorded_at stamp). WHY: the key is the transport-retry detector — stable across retries (authored content identical → the original record found → the LOUD ack names its handle), unstable across distinct judgments (any authored-field difference → a new record). The key is content, not position: no ledger index, no count, no timestamp rides it — a re-send after intervening votes still matches the original. (6) The mint + the append — THE ATOMIC WINDOW [STATED]: mint VOTE-{####} per-ledger max+1 — 4-digit zero-pad, natural overflow (the U1 precedent verbatim) — then append, then verify, inside one synchronous method body. The verify leg: the post-append count re-read from the store. The single-process tier's "lock" IS the synchronous act (no interleave within one sequential call); the module contract documents the boundary honestly — the file-lock form is named as the service tier's (.junro/.junro.json.lock the on-disk precedent), not implemented at birth. A concurrent write at the service tier REFUSES LOUDLY; the caller-side law: sequential writes over one run's ledger, always. (7) The return [STATED]: (handle, post-append ledger count) — "the write returns what landed, not what was sent" — the built-in read-back.

## 2. THE RE-VOTE SEMANTICS — the key's three outcome classes [STATED R9; DERIVED the mechanics]

| Send | Key relation | Mechanism | Tally consequence |
|---|---|---|---|
| Changed verdict, same (comparator, pair) | different key (winner differs) | NEW record — both count ("a revote is a new sample; changed minds are information") | equal weight, both counted (R5) |
| Byte-identical re-send | same key | the LOUD idempotent ack: the ORIGINAL handle named, nothing appended, count unchanged | zero — no weight pollution (a silent dup would double-count: FR-MEM-0143's lesson) |
| Clerical correction | different key + supersede reference set | a NEW record citing the old handle; the old stands in the log, excluded by the tally's weighting — U4's concern, named not implemented here | U4's weighting policy walks the supersede link |

The ack is loud BY CONSTRUCTION: it names the original handle (not a fresh mint) — the caller distinguishes ack from append without inference; a silent dup is unrepresentable at the surface. The supersede rides cast_vote as an optional parameter (the notes? precedent — the five-op interface is five ops, no sixth; [OPEN] its exact name); its ground-truth checks [DERIVED, for the brief to ratify]: the cited handle is live in the same run's ledger (unknown → malformed refusal), and the superseded record's pair equals the new record's pair (a correction corrects the same judgment). A correction-of-a-correction chains linearly — nothing forbids it; U4 walks the chain.

## 3. THE REFUSAL PATHS — expected/found/next-action, every one before any byte lands

| Refusal | Expected | Found | Next-action |
|---|---|---|---|
| Unknown run [STATED] | a live RUN-{####} handle (the live handles NAMED) | the run_id sent | read an existing run or register the payload first |
| Pair ∉ legal set [STATED] | a canonical pair from schedule_pairs over the manifest's ids (the legal set's SOURCE named; the swapped citation's canonical form named) | the cited pair | cite a canonical scheduled pair |
| Winner ∉ declared set [STATED] | the run's declared verdict set (the manifest's own frozen set; the weak-order triple at birth) | the winner sent | cast a verdict from the declared set |
| Malformed payload [STATED] | the schema's public types (a Pair or 2-string sequence; a string winner; a non-empty comparator_id; class ∈ {human, llm}) | the offending value/field | re-send per the schema |
| Supersede target invalid [DERIVED] | a live VOTE handle in the same run, same pair | the cited handle | cite the record being corrected |

**NEVER refuses on content plausibility** [STATED — "the system has no opinion about votes — noise is data"]: no check exists on whether the verdict is sensible; the gate asks well-formed?, never correct?. Corollary [DERIVED]: no quorum/count check at cast time — an over-quorum vote lands as a legal new sample ("any well-formed vote, any count — refusing the second sample would discard the psychometric remedy"); the exhausted state and the coverage gate key off quorum at U5/U4 (R8), never here.

## 4. THE INVARIANTS

1. **Append-only** [STATED]: no edit verb, no delete verb exists at the module surface; corrections are new entries referencing the old. The public surface: the value types, the container, the one cast op, the census read.
2. **NO score field** [STATED — the Parnas fold]: the vote record carries no score; ingestion computes nothing; "the tally's choice cannot leak through the vote interface" — swapping win-rate → BT later touches exactly one module, zero record migration.
3. **Provenance stamps on every record** [STATED; R5]: run_id, comparator_id, comparator_class ∈ {human, llm}, recorded_at (the registered_at precedent — UTC microsecond ISO) — identity recorded not anonymous; weighting retro-fittable from the stamps with zero record migration.
4. **The single mutating op** [STATED]: cast_vote is the vote ledger's ONE mutation — the choke point; register_run owns the manifests, cast_vote owns the votes; the write path is where the design spends its strictness.

**The VoteRecord** [DERIVED, the family precedent frozen dataclass]: (vote_id, run_id, pair as U2's Pair — "the type U3's vote records and ground-truth checks cite", comparator stamped, winner, notes, supersede reference optional, recorded_at) — frozen; NO score field.

## 5. THE READ_VOTE_STATE SHAPE — the census over the ledger

[STATED op 4; G-VOTES]: read_vote_state(run_id) → the run's per-pair counts, per-item comparison counts, and the full vote log. Pure; refuses the unknown run ONLY (naming the live handles); side effects: zero. NEVER refuses on coverage — it is the op that catches FR-MEM-0143-class silent loss and FR-MEM-0001-class gaps — every gate's evidence leg rides it.

- **The manifest link** [STATED/DERIVED]: the census reads the manifest via run_id (read_manifest); the run's frozen ids ARE the census's universe — per-item counts keyed over every manifest.items id (0 included), per-pair counts keyed over schedule_pairs(manifest ids) (0 included). Zero-coverage items and untouched pairs read back as 0s — the coverage gap is VISIBLE data, never an error.
- **The counts-map's downstream role** [DERIVED, load-bearing]: the per-pair counts map is the scheduler seam-(b) input — U5's loop consumes it as data. Pinning its shape here is U5's schema citation.
- **Per-item counts** [DERIVED]: each record increments BOTH pair members (a tie still compares); sum(per-item) = 2 × total votes (tool-verified: two votes on one pair → {a:2, b:2, c:0}, sum 4 = 2×2).
- **The full log** [DERIVED]: every record, append (mint) order — the ledger's own sequence; a frozen tuple of frozen records.
- **The return's form** [DERIVED, the frozen-value precedent]: a frozen dataclass snapshot (pure — stable across calls between mutations). [OPEN] the exact field set: G-VOTES's three vs op-4's letter (which adds the manifest and a coverage/connectivity verdict) — the brief reconciles; the ruled properties hold either way (pure, never-refusing-on-coverage, manifest-keyed).
- **The census on an empty ledger** [DERIVED, test edge 8]: all-zero maps over the full id/pair universe + the empty log — a VALUE, never a refusal.

## 6. THE EDGES + THE TEST EDGES — the set G-VOTES will check

[STATED] the floor + the landed test precedent (one test per named edge, docstring naming the edge). The set [DERIVED]:

1. **The first vote**: empty ledger → (VOTE-0001, 1); the census carries one record, per-pair {P:1}.
2. **The re-vote (changed verdict)**: same (comparator, pair), different winner → a NEW handle, count +1, BOTH records in the log, per-pair count 2.
3. **The identical resend's loud ack**: the same authored content re-sent → the ORIGINAL handle named, count UNCHANGED, the log unchanged — distinguishable from a fresh mint by construction.
4. **The supersede chain**: a correction citing the original handle → a new record referencing the old; the log carries both; the correction-of-correction chains.
5. **Two comparators on one pair** (the multi-actor stream): X and Y vote the same pair → two records (different keys), both land, per-pair count 2 — the DESIGN case, not the edge.
6. **The unknown-pair refusal** (including the swapped citation): refused naming the legal set's source and the canonical form; the count UNCHANGED — refusal-before-append proven.
7. **The wrong-verdict refusal**: winner ∉ the declared set → refused naming the declared set; nothing lands.
8. **The census on an empty ledger**: all-zeros + empty log (never a refusal); the unknown-run refusal names the live handles.
9. **The idempotency key's stability**: A votes P (VOTE-0001); B votes P (VOTE-0002 — intervening); A re-sends identically → the ack still names VOTE-0001 — the key is content, not position.
10. **The malformed-payload refusals**: empty comparator_id; class ∉ {human, llm}; bad pair shape — each naming the legal form.

## [OPEN] for the brief / G-VOTES-BRIEF to pin

- The refusal class's exact name (the Error-suffix family grammar — N818's precedent; the naming law: first word of the act-statement).
- The mint's ledger scope: per-store container (my derivation — the direct U1 precedent; the FR per-namespace-sequential semantics: one ledger, one namespace) vs. per-run (priced: cross-run handle collisions in logs); the container form (store-as-parameter, constructor-injected registry reference for write-time lookups, the registry precedent).
- The ack's return encoding: (handle, count) with the original handle named suffices for the ruled letter; an explicit ack marker makes it self-describing without caller-side inference — the "never silent" bar favors the marker; the brief pins.
- The dedup key's ratification (notes and supersede participate — the "byte-identical" letter; the priced alternative, a verdict-only key, would ack non-byte-identical sends).
- The census return's exact shape (the gate's three vs op-4's five; whether the coverage/connectivity verdict computes at U3 as pure census facts or rides U4/U5 — R8/R12 key both off quorum).
- The supersede parameter's name + the same-pair constraint's ratification.

## Constraints the brief inherits (named, not derived)

- The naming law; five-field docstrings (Purpose/Refuses when/Re-run/Touches/Provenance) on every new symbol; zero magic values (named constants — the PLR2004 cure); zero runtime dependencies; no subprocess; single-process by contract, documented.
- The floor: make dev && make test && make lint && make typecheck at the prioritree root; zero-ignore strictness — a lint/type ignore is a ruling, never a convenience.

*Provenance: rikai (理解), packet understand/votes, route prioritree-core (U3), 2026-11-20. Read-only held — no file written at execution; returned in-message; landed by shinko via patch under the landing discipline (read → patch → re-read). The tree is the truth; every mechanism claim carries its file:line.*
