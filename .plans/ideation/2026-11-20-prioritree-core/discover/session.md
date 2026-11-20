# discover/session — THE SESSION UNIT'S DISCOVERY CENSUS (U5, the public face — the fifth unit)

- Seat: tansa (探査, discover), packet discover/session, route prioritree-core, 2026-11-20. Read-only held — returned in-message; landed by shinko via patch, verbatim; read-back verified.
- Ground read whole (fail-fast clean): the core route store (G-SESSION's five conditions :297-305; the stamped pair); the birth store (the Q-solution-space five-op ruling); scope-synthesis.md (PART 2's U5 row, PART 3 §3.2, PART 4); the three upstream briefs (scheduler/votes/tally — the seam rulings) + the four landed siblings (registry.py 405, scheduler.py 106, votes.py 532, tally.py 521 — all read whole). Measured: session.py and test_session.py unborn.
- Labels: [STATED] ruled / on disk · [OPEN] the brief must pin · [PROPOSED] an upstream brief's recorded default.

## 1. WHAT THE RULINGS FIX (cited)

- **The five ops' letters** [STATED — scope-synthesis §3.2 :130-134, adopted wholesale]: op 1 register_run (the immutable (items, operator) ground; the refusals; one side effect); op 2 next_pair (pure; the seed from run_id; the DONE signal distinct from error; no state no scores); op 3 cast_vote (the only stochastic entry; the loud dedup; the ground-truth checks; supersedes; never refuses on content); op 4 read_vote_state (the census; pure; unknown run only; never refuses on coverage); op 5 tally_rank (the pure projection; idempotent; write nothing; the SAFE HALT on the coverage gate).
- **The merge-refusals** [STATED — §3.2 :136]: ops 4+5 never merge (the audit read never refuses on coverage; the emission always refuses); ops 2+4 never merge (the comparator surface must not see state; the auditor must); op 1 never sheds the operator. Two append-only stores, zero edit/delete verbs.
- **The DONE mint site — U5 WHOLE** [STATED]: scheduler-brief §1's recorded proposal rides the minted gate (G-SESSION condition 2: "the DONE signal minted AT U5 WHOLE — the queue from U2, the counts from U3's census, the quorum from U1's manifest; a dedicated signal class distinct from the refusal lineage").
- **The census-as-is consult** [STATED — seam (b)'s letter]: U5's loop keys manifest.quorum against the census's per-pair counts AS-IS (G-SESSION condition 3) — unweighted, the divergence under corrections NAMED and carried, never hidden (tally-brief's trade-off).
- **The Parnas fence** [STATED — the U5 row :104]: CLI/service/web concerns, comparator elicitation UX MUST NOT KNOW. The act: "Session the chain into the library's public face — register → schedule → vote → tally composable at any coverage point, emitting the stable ranking serialization." The gate: the end-to-end fixture, the prefix-tally property, the public API frozen as the wrapper contract.
- **The one-name-one-arity reservation** [STATED — tally-brief §1/:43]: tally_rank is U5's composed op; U4's heart is tally_votes.
- **The composed-op letters** [STATED — G-SESSION condition 2]: register_run (U1's, exposed); next_pair (the count-consult + DONE at U5 whole); cast_vote (U3's, exposed); read_vote_state (U3's, exposed); tally_rank (read_manifest + the census's vote_log → tally_votes → the frozen TallyResult whole, never re-computed).

## 2. THE GAPS THE BRIEF MUST PIN

**(a) The session container's form** [OPEN]: a class holding the two stores ("Session" per the naming law from the act's first word). The constructor shape: (1) Session(registry: Registry) constructing VoteLedger(registry) internally — the mismatched-pair hazard foreclosed by construction; (2) Session(registry, ledger) both injected — the hazard representable, policing it dead weight; (3) Session() both internal — maximal convenience, the stores unreachable. Also: the stores public attributes or held privately behind the five ops (the fence leans private — the frozen wrapper contract is the five ops).

**(b) The five ops' exact signatures at U5** [OPEN]: register_run exposed — the same signature → (run_id, RunManifest, count) or op 1's letter → RUN-{####}?; which refusal crosses (RegistryRefusedError verbatim or a session form?). next_pair composed — the loop: read_manifest → quorum + ids; read_vote_state → per_pair_counts; walk schedule_pairs' queue in order; THE FIRST under-quorum pair returns with its count (the natural composition — the brief pins); none → the DONE signal. The seed: derive_seed(run_id) the default, dead at birth under the ruled order. The return carrier: the op-2 triple (str, str, int) vs. (Pair, int) — Pair the seam into cast_vote. The DONE signal's exact class name + fields (a dedicated class distinct from the refusal lineage; N818 tension: a suffix-free name trips the family lint — a named ruling or the form priced). cast_vote/read_vote_state exposed — verbatim delegation (the four-tuple; the VoteCensus)? VotesRefusedError verbatim? tally_rank — read_manifest + read_vote_state().vote_log → tally_votes → the frozen TallyResult; TallyRefusedError verbatim propagation (never swallowed).

**(c) The DONE signal's raise semantics** [STATED keying / OPEN bytes]: the exhausted state — no under-quorum pair remains, keyed off manifest.quorum against the census's per-pair counts AS-IS; the loop: census[pair] < quorum over the cited queue; the divergence named — a corrected pair at k=2 → next_pair DONE while tally_rank SAFE-HALTs (the seam carried, never reconciled).

**(d) The session's state** [OPEN, strongly priced]: beyond the two store references — NOTHING. The queue per-call (O(n²), 4,950 pairs, trivial per the brief's own pricing); a cache a third structure to keep consistent + state the composition layer must not own; the manifest never cached (FR-MEM-0001's discipline; the freeze makes the read cheap anyway).

**(e) The module layout** [PROPOSED → the brief rules]: src/prioritree/session.py + tests/test_session.py — the route's ruled vocabulary; measured unborn.

**(f) The test surface** [STATED in names / OPEN in count]: (i) the end-to-end fixture — a scripted sequence through the public face → the exact expected ranking; (ii) the prefix-tally property — tally_rank well-defined at every prefix; (iii) the DONE path — caught BY TYPE, the fields verified; (iv) the seam-divergence test — the correction at k=2: next_pair DONE + tally_rank SAFE HALT, the divergence named; (v) the five ops present and wired; (vi) the seam's honesty asserted (no scores, no rankings, no pair-set re-derivation at U5). The floor: pyright 0/0/0 + ruff zero + zero ignores; kensho's re-run.

**(g) The laws riding** [STATED]: five-field docstrings; the naming law (the class from the act's first word; the five ops pre-named); zero-deps; zero-findings/zero-ignores — THE ARG001 RETIREMENT CLAUSE RIDES THIS UNIT ("it retires when U5's next_pair consumes the seed" — the pyproject ruling's own words); the no-shell law; content-in-configuration; the exact-task law (the bytes after G-SESSION-BRIEF greens; single-goal dispatches); THE WRAPPERS' CONTRACT FROZEN — U6 and the future CLI/FastAPI/web cite THIS surface (the U5 row; the MCP tier's tools are these five ops — Q-mcp-surface).

## 3. THE CITATION CONTRACT — what U6 and the wrappers import from U5

- **Session (the class, the two stores wired)**: U6's only door — "any private surface — ONLY the U5 public API (the first consumer, standing in for the wrappers)"; the CLI wraps it, FastAPI serves it, the web fronts it; OunceMCP lands the five ops as its tools (Q-mcp-surface).
- **register_run (exposed)**: the run's birth — the frozen manifest's handle crosses.
- **next_pair (composed)**: the elicitation loop's feed — the bare pair, no state; the wrappers' "ask the comparator" step.
- **the DONE signal (U5-minted)**: the loop's terminal — U6 and the wrappers catch it BY TYPE to know the queue is exhausted (distinguishable from error).
- **cast_vote (exposed)**: the one mutating entry — the wrappers' write path.
- **read_vote_state (exposed)**: the audit read — every gate's evidence leg.
- **tally_rank (composed, one name one arity)**: the emission — returning U4's frozen TallyResult whole, never re-computed; U6's tau harness reads ranked_groups.
- **TallyRefusedError (propagated, never swallowed)**: U6 handles it; the wrappers render the SAFE HALT.
- **the refusal grammar mapping (which typed refusal crosses which op)**: the wrappers' catch-and-render table — frozen here.

*The frozen inputs U5 composes: Registry/RunManifest/RegistryRefusedError; Pair/schedule_pairs/derive_seed; VoteRecord/VoteCensus/VoteLedger/cast_vote/read_vote_state/VotesRefusedError; tally_votes/TallyResult/CoverageDatum/TallyRefusedError/TALLY_ALGORITHM. U5 imports ONLY sibling public types; the census a carrier, never a re-derivation. Provenance: tansa (探査), packet discover/session, route prioritree-core, 2026-11-20. The tree is the truth.*
