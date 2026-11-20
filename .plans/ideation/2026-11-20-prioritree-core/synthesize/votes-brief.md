# synthesize/votes-brief — THE VOTES UNIT'S BUILD BRIEF (the exact-task spec)

**Status: PROPOSAL.** Togo proposes; the collaborator rules at G-VOTES-BRIEF. Every [PROPOSED] element is an offered default with its one-line reason. The brief IS the spec (the exact-task law): once approved, the bytes addendum (the fenced file contents, togo's hand) composes as its own dispatches; jikko executes byte-exact, kensho re-runs independently.

## §0 GROUND — the rulings the brief cites

**The R-rulings (adopted wholesale at the birth store's Q-solution-space resolution; scope-synthesis PART 4):**

- **R4 — vote vocabulary** (scope-synthesis:171): the weak-order triple {prefer-a, prefer-b, tie} as the declared verdict set's default (binary at birth, tie per the operator's declaration); abstention needs no record — a comparator who cannot judge does not cast, and the pair stays under-quorum. A vote's legal winner set is the RUN'S OWN declared set — RunManifest.operator.verdicts (registry.py:64), one source of truth; never the module constant directly.
- **R5 — comparator scope** (:172): equal weight at birth (one vote, one tally unit); stamped provenance — comparator_id + class ∈ {human, llm} on every vote; identity recorded, not anonymous; weighting is a later tally parameter, retro-fittable from the stamps with zero record migration. The stamps are data U3 carries and never interprets.
- **R9 — re-vote semantics** (:176): append-and-accumulate — a byte-identical re-send is a loud idempotent ack naming the original handle (never a silent dup); a changed verdict from the same (comparator, pair) is a NEW record (a revote is a new sample — changed minds are information; both count); clerical corrections ride supersedes (the old stands in the log, excluded by the tally's weighting); no edit op, no delete op — the FR-MEM-0143/0001 fold-ins (lock-file discipline, ground-truth check at write time, handle + post-append count, single-process contract) ride this brief as design requirements.

**Op 3, verbatim** (scope-synthesis:132): "cast_vote(run_id, pair, winner, comparator_id, comparator_class, notes?) → VOTE-{####} + post-append ledger count — the only stochastic-side entry point, and the only op that mutates the vote ledger. Gates: strict schema; winner ∈ the pair's declared verdict set; both item ids ground-truth-checked against the run manifest AT WRITE TIME (FR-MEM-0001's discipline); comparator_class ∈ {human, llm}; provenance stamp on every line. Idempotency: a byte-identical re-send is a LOUD idempotent ack naming the original handle (never silent — FR-MEM-0143's lesson); a changed verdict from the same (comparator, pair) is a new record (a revote is a new sample — changed minds are information); clerical corrections ride supersedes: VOTE-{####}. Refusals: unknown run/item ids; winner not in pair; malformed payload — naming the legal set. Never refuses on content plausibility (the system has no opinion about votes — noise is data). Ingestion is independent of the scheduler: a vote is valid on any registered pair (the scheduler suggests; it does not confer permission — keeping them decoupled preserves the Parnas seam and serves both comparator classes). Side effects: exactly one — the append. Hidden seams/forecloses: any notion of score (nothing to leak through); the return carries the post-append count — a built-in self-verification leg; vote edit/delete unrepresentable (append-only); vote-time ranking access foreclosed. Abstention needs no record."

**Op 4, verbatim** (:133): "read_vote_state(run_id) → manifest, per-pair counts, per-item comparison counts, coverage/connectivity verdict, the full vote log — the census read-back instrument. Pure. Refuses: unknown run ONLY. Never refuses on coverage — the audit surface must read back even a broken state, especially a broken state; that is its job (the op that catches FR-MEM-0143-class silent loss and FR-MEM-0001-class gaps; every gate's evidence leg rides it). Side effects: zero."

**The family form, citation CORRECTED (the census's discipline):** the clause's true home is the APPROVED REGISTRY BRIEF (registry-brief.md:151, Option A's load-bearing decision): "U1's ruling sets the family form — the vote ledger (U3) inherits the store-as-data discipline with its own lock-file layer per R9" — not the birth store's ruling (that carries R9's design-requirement set the clause cites). The landed precedent: the store-as-parameter container (registry.py:297-313); the per-store max+1 mint in the same synchronous act as the append (registry.py:358-368); the built-in read-back's return form (registry.py:369); the unknown-handle refusal naming the live set (registry.py:371-394).

**The legs riding this brief + the convergence statement (amendment 25's join point):** discover/votes (tansa's census — the seven ruled items, the gaps (a)-(h), the citation contract) and understand/votes (rikai's mechanism — the seven-stage chain, the re-vote classes, the refusal table, the invariants, the read shape, the ten edges). RECONCILED: the legs CONVERGED — the mechanism's chain matches the census's gap list item for item, with identical leans on every open (per-store mint, constructor-injected registry, the explicit ack marker, notes/supersedes keying). Two near-misses reconciled, neither a divergence of fact: (1) the lock's concrete carrier — resolved by G-VOTES condition 3's own letter (the synchronous act IS the window at the single-process tier; §3 pins it); (2) the family-form citation — corrected to registry-brief.md:151 per the census, content unchanged. No residual divergence survived reconciliation — nothing blocks the brief.

**G-VOTES's five conditions** (the route store, gates :197-202) — the deterministic gate this spec feeds; the carriers table at §6.

## §1 THE MODULE — the layout ruling

**[PROPOSED]: single module `src/prioritree/votes.py` + `tests/test_votes.py`** — the route's ruled vocabulary names them (G-VOTES, build/votes); measured: both unborn. Reason: the naming law is honored at the symbol level; the module name follows the route's ruled vocabulary (the registry/scheduler flat-module precedent).

**The public surface (the citation contract — the frozen list):**

| Symbol | Kind | Consumers |
|---|---|---|
| `VoteRecord` | frozen dataclass (9 fields, NO score) | U4 (the tally's entire input), U5 |
| `VoteCensus` | frozen dataclass snapshot | U5 (the quorum consult), every gate's evidence leg |
| `VoteLedger` | the container class (store-as-parameter, registry-injected) | U5 (wires Registry + VoteLedger), the tests |
| `cast_vote` (method) | the ONE mutating op | U5, the wrappers (op 3) |
| `read_vote_state` (method) | the census read | U5, the audit surface (op 4) |
| `VotesRefusedError` | the typed refusal | every downstream unit's refusal grammar |
| `COMPARATOR_CLASSES` | frozenset[str] = {"human", "llm"} | the wrappers, U4 (R5's stamps) |
| `VOTE_PREFIX` | str = "VOTE-" | the handle grammar's citers |

Everything else (coercion helpers, the dedup index, the mint) is internal. No bare count accessor — the count rides every cast's return and the census's log; an uncited seam is refused. **What U3 does NOT ship:** the DONE signal (U5's — next_pair's exhausted state); any score field (the Parnas fold); any quorum or count check at cast (R8 keys U5/U4 — an over-quorum vote lands as a legal new sample; "refusing the second sample would discard the psychometric remedy"); no abstention verb (R4); no edit/delete verb (append-only); no scheduling policy — "the scheduler suggests; it does not confer permission."

**The import split (the siblings law; absolute form — the landed tests' own precedent):** `from prioritree.registry import Registry, RegistryRefusedError` and `from prioritree.scheduler import Pair, schedule_pairs` (the legal pair set's ONE source of truth); registry's read surface via the container's public `read_manifest`; never the private helpers (votes hand-rolls its own per the family school); never the reverse — U3 is a leaf consumer and knows nothing of ranking or enumeration order (the U3 fence).

## §2 THE SCHEMAS — field-level

All frozen dataclasses; zero runtime deps (validation hand-rolled per the family precedent).

**`VoteRecord`** [PROPOSED: frozen dataclass, the family school — the ItemRow/RunManifest precedent]:
- `vote_id: str` — the VOTE-{####} handle (4-digit zero-pad, natural overflow; stored, never renumbered).
- `run_id: str` — the record's run (read_vote_state and per-run grouping key it; both legs derive it must ride).
- `pair: Pair` — U2's canonical type, the seam ("the type U3's vote records and ground-truth checks cite", scheduler.py:32).
- `winner: str` — the declared set's token; positional over the canonical form (prefer-a ⇒ item_a, prefer-b ⇒ item_b, tie — named by the triple itself); stored verbatim.
- `comparator_id: str` — non-empty stripped at cast (R5's identity stamp).
- `comparator_class: str` — a COMPARATOR_CLASSES token, validated at cast (R5).
- `recorded_at: str` — the UTC microsecond ISO stamp (the registered_at precedent, registry.py:366).
- `notes: str | None = None` — any string, stored verbatim (opacity).
- `supersedes: str | None = None` — the clerical correction's reference (R9: "supersedes: VOTE-{####}").
- **NO score field — ruled** (the Parnas fold: "there is no field to leak through").

**[PROPOSED] the definition order:** vote_id, run_id, pair, winner, comparator_id, comparator_class, recorded_at, notes, supersedes — `recorded_at` before the two optionals: Python's dataclass law refuses a non-default field after a defaulted one (a mechanical constraint, not a design choice; the field enumeration above is the SET, the definition order rides the constraint).

**The constants (content-in-configuration — the WEAK_ORDER_TRIPLE/_RUN_PREFIX precedents):** `COMPARATOR_CLASSES: frozenset[str] = frozenset({"human", "llm"})` (R5's class set as data, never inline logic); `VOTE_PREFIX: str = "VOTE-"` (the handle grammar on the public surface — the citation contract).

**`VotesRefusedError`** [PROPOSED: the Error-suffix family form — the RegistryRefusedError precedent (N818, the amendment-16 rename ruling)]: fields `expected: str`, `found: str`, `next_action: str` plus the rendered message — the registry-brief §2 carrier verbatim; raised, never returned.

## §3 CAST_VOTE — the exact signature and semantics

**The container [PROPOSED: `VoteLedger(registry: Registry)` — the constructor-injected reference, census option (1)]:** the manifest resolved per write via `read_manifest(run_id)` — never cached (FR-MEM-0001: validate against the store's own truth at write time; a stale manifest copy is the payload-provenance trap). Reason: a never-voted run's unknown-run refusal needs the registry anyway; the container-to-container form keeps the ruled five-op signature pure. Internal store [PROPOSED]: `self._votes: dict[str, VoteRecord]` (flat, handle-keyed; insertion order = mint order — the U1 dict precedent) + `self._dedup: dict[tuple[...], str]` (the canonical-content key → the original vote_id; Pair's hashability banked for exactly this). Reason: one store, one namespace; the per-run views (the census, the supersede check) are read-time derivations — no third structure to keep consistent.

**The signature (the single mutating op):**

```python
def cast_vote(
    self,
    run_id: str,                        # non-empty, stripped
    pair: Pair | Sequence[str],         # [PROPOSED] the dual form (the _coerce_rows precedent)
    winner: str,                        # a declared-set token, verbatim
    comparator_id: str,                 # non-empty, stripped
    comparator_class: str,              # ∈ COMPARATOR_CLASSES
    notes: str | None = None,
    supersedes: str | None = None,      # [PROPOSED] the name matches the record's field (R9's own word)
) -> tuple[str, VoteRecord, int, bool]  # (handle, the landed record, the post-append count, acknowledged)
```

[PROPOSED] the dual-form pair: a Pair instance (members checked strings) or a 2-length sequence of strings — carried AS SENT, never re-ordered; the swapped citation is refused at stage 3 naming the canonical form. Reason: the registry's ergonomic precedent; the store always holds the canonical Pair. [PROPOSED] the return: the registry read-back triple (handle, value, count — registry.py:369) plus the explicit ack boolean — `acknowledged=False` on a fresh append; `True` on the idempotent ack (the ORIGINAL handle + the ORIGINAL record + the UNCHANGED count). Reason: the "never silent" bar — the caller distinguishes ack from append by construction, never by count-delta inference (a silent dup is unrepresentable at the surface).

**The seven-stage chain (deterministic; fail-fast; every refusal raises BEFORE any byte lands — the registry precedent):**

1. **Schema** — run_id a non-empty stripped string; pair a Pair or 2-length sequence of strings; winner a string; comparator_id non-empty stripped; comparator_class ∈ COMPARATOR_CLASSES; notes a string or None; supersedes a string or None. Malformed → refusal 4.
2. **Run live** — `read_manifest(run_id)` via the injected registry. [PROPOSED: the WRAP — catch RegistryRefusedError, re-raise `VotesRefusedError` carrying the same expected/found/next_action verbatim, `from refusal`.] Reason: the votes surface speaks ONE refusal grammar (one except clause downstream); the registry's rendered live-set rides through unchanged — the live handles named are the REGISTRY's manifests (a never-voted run is legal ground; the ledger has no run-domain authority — census gap (b)(iv) resolved).
3. **Pair ∈ legal set** — enumerate `schedule_pairs` over the manifest's ids; membership-test the cited pair (Pair hashable). Outside → refusal 2; the swapped citation ("b","a") is refused naming the canonical form, NEVER silently re-ordered (the verdict vocabulary is positional over the form).
4. **Winner ∈ declared set** — `manifest.operator.verdicts`, the run's OWN frozen set. Outside → refusal 3.
5. **The dedup key** — (a) the supersede ground truth, when supersedes is set: the cited handle live in the same run's ledger AND its pair equals the cited pair [PROPOSED: ratifying the mechanism's derivation — a correction corrects the same judgment; a cross-run/cross-pair "correction" is a new vote, not a correction]; (b) the key = **(run_id, canonical pair, winner, comparator_id stripped, comparator_class, notes, supersedes)** — every caller-authored field in canonical form, the store-minted fields (vote_id, recorded_at) excluded [PROPOSED: the "byte-identical" letter — a re-send differing in ANY authored field is a fresh record; the priced verdict-only key would ack non-byte-identical sends]. Index hit → **the LOUD ACK**: return (the original handle, the original record, the unchanged count, acknowledged=True) — nothing appended.
6. **The mint** — `VOTE-{####}` per-STORE max+1 (len+1 — append-only keeps len == max; 4-digit zero-pad, natural overflow; two ledgers mint independently) [PROPOSED: the RUN-{####} precedent — one ledger, one namespace; per-run numbering collides in any cross-run view]; `recorded_at` = the UTC microsecond ISO stamp.
7. **The append + verify — ONE synchronous act (the atomic window)** — insert into the store + the dedup index; return (vote_id, record, len(store), acknowledged=False); the count reads the store post-append, never a local counter. [PROPOSED: the synchronous method body IS the window — "the lock's birth form at the single-process tier" (G-VOTES condition 3's own letter); NO threading primitive at birth; the single-process contract documented in the class docstring (the Registry precedent); the LOUD concurrent-write refusal ("expected: free ledger; found: lock held; next: retry sequentially") rides the service tier's lock-file layer per R9's design requirements.]

**The re-vote semantics (R9's three outcome classes):** changed verdict, same (comparator, pair) → different key → a NEW record, both count (equal weight, R5); byte-identical re-send → same key → the loud ack (zero weight pollution — a silent dup would double-count); clerical correction → different key + supersedes set → a NEW record citing the old; both stand in the log — U4's weighting walks the link (named here, never implemented here). A correction-of-a-correction chains linearly — nothing forbids it; U4 walks the chain.

**The refusal texts, verbatim (the expected/found/next-action grammar):**

1. **Unknown run (the wrap):** expected=`a live RUN-{####} handle ({live})` (the registry's own rendering — the live handles NAMED), found=`{run_id!r}`, next_action=`handles are minted only by register_run; read an existing run or register the payload first`.
2. **Pair ∉ legal set:** expected=`a canonical pair from schedule_pairs over the run's {n} manifest ids (the legal set's source)`, found=`{pair!r}`, next_action=`cite a canonical scheduled pair — the scheduler suggests; it does not confer permission, but a vote cites the canonical form`; the SWAPPED citation (both ids live, order non-canonical): expected=`a canonical pair (item_a < item_b) — the canonical form of these ids is {canonical!r}`, next_action=`re-send the pair id-sorted — the verdict vocabulary is positional over the canonical form; a swap is never silently re-ordered`.
3. **Winner ∉ declared set:** expected=`a verdict from the run's declared set {sorted(manifest.operator.verdicts)}`, found=`{winner!r}`, next_action=`cast a verdict from the declared set`.
4. **Malformed payload:** expected=`the schema's public types (run_id a non-empty string; pair a Pair or 2-length sequence of strings; winner a string; comparator_id a non-empty string; comparator_class from {sorted(COMPARATOR_CLASSES)}; notes a string or None; supersedes a string or None)`, found=`{field} got {value!r}`, next_action=`re-send per the schema — the module's public types (VoteRecord's fields)`.
5. **Supersede target invalid:** expected=`a live VOTE-{####} handle in the same run, on the same pair (a correction corrects the same judgment)`, found=`{supersedes!r}` (plus ` — a record on pair {target.pair!r}` when live but cross-pair), next_action=`cite the record being corrected`.

**NEVER refuses on content plausibility** (op 3: "the system has no opinion about votes — noise is data"); no quorum/count check at cast — the exhausted state and the coverage gate key off quorum at U5/U4 (R8), never here.

## §4 READ_VOTE_STATE — the census

**[PROPOSED: the frozen dataclass snapshot — `VoteCensus`]** (the family's frozen-value school; pure — a fresh value per call): `def read_vote_state(self, run_id: str) -> VoteCensus`

- `run_id: str` — the census's key.
- `per_pair_counts: Mapping[Pair, int]` — the full pair universe from `schedule_pairs(manifest ids)`, 0 included; +1 per record on the pair. The scheduler seam-(b) input — U5's loop keys it against manifest.quorum; the Pair-keyed form is U5's schema citation.
- `per_item_counts: Mapping[str, int]` — every manifest id at 0; each record increments BOTH pair members (a tie still compares) — sum(per_item_counts) = 2 × total votes (tool-verified: two votes on one pair → {a:2, b:2, c:0}).
- `vote_log: tuple[VoteRecord, ...]` — the run's records in mint order; a frozen tuple of frozen records.

Field names per the naming law — op 4's own vocabulary ("per-pair counts, per-item comparison counts, the full vote log") governs. The maps are plain dicts built fresh per call, typed Mapping [PROPOSED: the fresh-per-call build IS the snapshot — later casts never mutate a returned census; proxy-type hardening is the service tier's, not birth's]. **Pure; refuses the unknown run ONLY (the same wrap, naming the live handles); NEVER refuses on coverage** — the zero-vote run reads back all-zero maps over the full universe + the empty log: a VALUE, never a refusal (the audit surface reads back broken states, especially broken states). Side effects: zero.

**[PROPOSED] the reconciliation — the gate's three vs op-4's five, resolved with the reason:** the gate's three (per-pair, per-item, the log) ride the census as named fields; op-4's other two resolve OUT. (1) **The manifest is NOT a census field** — the census's 0-keyed universes ARE the manifest's content as data (the ids, the pairs — the ground reflected in the key sets); the value itself is U1's own read-back (`read_manifest(run_id)`, one call); each unit reads back its own store — U3 duplicating the frozen manifest doubles the read surface for zero new information. (2) **The coverage/connectivity verdict does NOT compute at U3** — it keys off quorum (R8) and R12's binary: the DONE signal is U5's, the coverage gate is U4's tally refusal — computing the verdict here would put U5's keying behind U3's interface (the same leak the no-score fold forbids). **The census carries the counts as data** — zero-coverage items and untouched pairs are VISIBLE 0s; the verdicts compute where the quorum lives.

## §5 THE TESTS — tests/test_votes.py (twelve named edges, one test per edge, the docstring naming the edge)

1. **`test_first_vote_mints_vote_0001`** — the empty ledger's first cast → ("VOTE-0001", record, 1, acknowledged=False); the record's stamps verified (run_id, pair, winner, comparator stamps, recorded_at a UTC microsecond ISO string); the census: one record, per_pair_counts {P: 1}, sum(per_item_counts) == 2.
2. **`test_changed_verdict_revote_is_a_new_record`** — same (comparator, pair), different winner → a NEW handle, count 2, acknowledged=False, BOTH records in the log, per-pair count 2 (both count — R9).
3. **`test_identical_resend_acks_the_original_handle`** — the same authored content re-sent → the ORIGINAL handle, the original record, count UNCHANGED, acknowledged=True, the log unchanged — distinguishable from a fresh mint by construction.
4. **`test_supersede_chain`** — a correction citing the original handle lands as a new record (supersedes set); the log carries both; the correction-of-correction chains linearly; the invalid targets (unknown handle; cross-run; cross-pair) refused naming the constraint — nothing lands.
5. **`test_two_comparators_on_one_pair`** — X (class "human") and Y (class "llm") vote the same pair → two records (different keys), both land, per-pair count 2 — the design case; both classes through the one interface.
6. **`test_unknown_pair_refused_including_swapped_citation`** — a pair with an id outside the manifest refused naming the source; the swapped citation refused naming the canonical form; the count UNCHANGED — refusal-before-append proven.
7. **`test_wrong_verdict_refused`** — winner ∉ the declared set → refused naming the declared set; nothing lands.
8. **`test_census_on_empty_ledger_never_refuses`** — a registered run, zero votes → all-zero per-pair over the full pair universe, all-zero per-item over every manifest id, the empty log (a value, never a refusal); AND the unknown run → VotesRefusedError naming the live handles (the wrap's type and text).
9. **`test_idempotency_key_stable_across_intervening_votes`** — A votes P (VOTE-0001); B votes P (VOTE-0002 — intervening); A re-sends identically → the ack still names VOTE-0001 (acknowledged=True, the count UNCHANGED, the log unchanged) — the key is content, not position.
10. **`test_malformed_payload_refusals`** — empty comparator_id; comparator_class ∉ {human, llm}; a bad pair shape (a 3-length sequence; a non-string member; a bare string); winner not a string; empty run_id; notes neither string nor None; supersedes neither string nor None — each refused naming the schema's public types; the count UNCHANGED across the whole batch (every refusal raised before any byte lands).
11. **`test_append_only_invariant_at_module_surface`** — no edit/delete verb exists: VoteLedger's public method set is exactly {cast_vote, read_vote_state}; no name carrying edit/delete/remove/update semantics exists anywhere in the module's public vocabulary; corrections are new entries referencing the old (test 4's chain is the behavioral proof — this edge pins the structural one).
12. **`test_no_score_field`** — "score" is not among VoteRecord's field names (nor VoteCensus's): the Parnas fold asserted structurally — there is no field to leak through; the tally's choice cannot cross the vote interface.

**The floor:** make dev && make test && make lint && make typecheck at the prioritree root — pyright strict 0 errors, 0 warnings, 0 informations; ruff (select ALL, line-length 120) zero findings; ZERO ignores anywhere — a new per-file exemption ONLY as a NAMED RULING at pyproject's per-file-ignores, citing the approving ruling (the R1/ARG001 standing form; votes expects NONE). **Kensho's independent re-run:** the same suite, fresh process, on kensho's own instruments — the read-back is the evidence, not the build's word (the FR-MEM-0013/0014 stale-session class rides the next opencode restart's re-dispatch).

## §6 THE LAWS RIDING + THE GATE'S EVIDENCE

**The laws:** Five-field docstrings (Purpose / Refuses when / Re-run / Touches / Provenance) on EVERY public symbol — VoteRecord, VoteCensus, VoteLedger, cast_vote, read_vote_state, VotesRefusedError, COMPARATOR_CLASSES, VOTE_PREFIX — Provenance citing R4/R5/R9, the five-op interface, scope-synthesis PART 3 §3.2 ops 3-4, G-VOTES's conditions, this brief. The naming law: cast_vote/read_vote_state pre-named by the ruled interface; VoteRecord/VoteLedger/VoteCensus ruled here from the family school; VotesRefusedError [PROPOSED] the Error-suffix family form (N818 — the amendment-16 rename precedent, cheapest now, before U4-U6 cite the name). Zero-deps: dependencies = [] stands; datetime (UTC microsecond ISO) stdlib-legal for recorded_at; threading NOT imported — the synchronous act IS the window; the lock-file layer is the service tier's per R9's design requirements. Content-in-configuration: COMPARATOR_CLASSES + VOTE_PREFIX as named module constants (the WEAK_ORDER_TRIPLE precedent); the dedup key built in exactly one place; zero magic values (the PLR2004 cure). The no-shell law: zero subprocess (pure logic). The exact-task law + the bytes addendum: the brief pins signatures, field names, refusal texts, test names; the exact file contents (the fenced blocks) compose at togo's hand as the bytes addendum — its own single-goal dispatches per the execution-decomposition doctrine — AFTER G-VOTES-BRIEF greens; jikko lands them byte-exact, the floor runs, kensho re-runs independently.

**The G-VOTES conditions → the spec's carriers:**

| G-VOTES condition | The spec's carrier |
|---|---|
| 1. The votes module lands per its approved brief — the exact-task law | §1 the module + the import split, §2 the schemas, §3 the op, §4 the census — signatures, field names, refusal texts, test names pinned |
| 2. The append-only invariant: cast_vote the single mutating op; no edit/delete verb; corrections ride supersedes; NO score field | §1 the frozen surface, §2 the record (no score), §3 stage 5(a) + the re-vote classes, §5 tests 11 + 12 |
| 3. The write discipline green: schema + ground-truth at write time; the loud idempotent dedup; the atomic window; provenance stamps | §3 the seven-stage chain — stages 1-4 (schema + ground truth), stage 5 (the dedup + the ack), stages 6-7 (the mint + append + verify, one synchronous act); the stamps at §2 — §5 tests 1-9 |
| 4. The census read-back green: per-pair counts, per-item counts, the full vote log; NEVER refusing on coverage; the unknown-run refusal naming the live handles | §4 the VoteCensus + the wrap; the zero-vote run a value — §5 tests 8 (+ tests 1, 5's counts) |
| 5. Pyright 0/0/0 + ruff zero findings, the named rulings standing; kensho's independent re-run green | §5 the floor + the independent re-run leg |

**The trade-offs the plan carries, named:** (i) the wrap — one refusal grammar at the votes surface, at the price of a translation layer whose texts ride the registry's rendering verbatim; (ii) the dual-form pair — the ergonomic minimum, at the price of a coercion stage and the swapped-citation refusal (the vocabulary is positional; a swap is never silently re-ordered); (iii) the canonical-content key — the "byte-identical" letter honored, at the price that a re-send differing in ANY authored field (notes included) is a fresh record, never an ack; (iv) the ack boolean — the self-describing return, at the price of a four-tuple (op 3's ruled two elements ride as the first and third); (v) the synchronous act as the window — zero birth machinery, at the price of the single-process contract (the loud concurrent-write refusal rides the service tier's lock); (vi) the census without manifest/verdict — the counts as data, at the price of U4/U5 computing their own verdicts where the quorum lives (the no-score fold not re-created through the back door).

**Open questions carried to the gate (each [PROPOSED] above):** the module layout (§1); the record's field set, optionals, and definition order (§2); VotesRefusedError's name (§2); the container's injected registry + flat store + dedup index (§3); the dual-form pair + the return's four-tuple with the ack boolean (§3); the wrap's re-raise form (§3); the seven-stage order + the dedup key's participation + the supersede ground truth (§3); the per-store mint + the synchronous act with no threading primitive (§3); the census's frozen shape + the manifest/verdict resolution (§4); the twelve-edge test set (§5). Every one resolves discover's gaps (a)-(h) and understand's [OPEN] list; the brief carries nothing unruled past the gate.

*Provenance: togo (統合, integrate), packet synthesize/votes, route prioritree-core, 2026-11-20 session. Read-only held — no file written at execution; the brief returned in-message (with one transit truncation recovered by session resume same-turn); landed by shinko via patch under the landing discipline (read → patch → re-read). The tree is the truth; every citation carries its file:line.*

