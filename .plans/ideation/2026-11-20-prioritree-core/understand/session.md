# understand/session — THE SESSION UNIT'S MECHANISM (U5): the composition chain, the DONE signal, the seam's honesty

- Seat: rikai (理解, understand) — packet understand/session, route prioritree-core (U5), 2026-11-20. Read-only held; returned in-message (one transit truncation recovered by session resume same-turn); landed by shinko via patch, verbatim; read-back verified.
- Ground read whole: core junro.json (G-SESSION :297-305); birth junro.json (the scope rulings, R7/R8/R12); scope-synthesis.md (PART 2's U5 row, PART 3 §3.2, R8, R12); scheduler-brief.md §1 (seam (b), the DONE mint site, §3, §6's O(n²) pricing); votes-brief.md §4; tally-brief.md (§0, §4, §5 test 12, §6's trade-off); the landed siblings (all four read whole); understand/scheduler.md (the DONE-signal precedent); understand/tally.md (edge 12, the seam named for this brief).
- Labels: [STATED] ruled / on disk · [DERIVED] follows from stated premises · [OPEN] the brief pins.

## 1. THE COMPOSITION CHAIN, end-to-end

- **The construction**: the session wires Registry + VoteLedger (G-SESSION condition 2). ONE Registry instance must back both the session's register/read path and the ledger — the ledger's write-time ground-truth checks must read the same store register_run mints into; two instances would sever the ground-truth chain (FR-MEM-0001). The wiring's form [OPEN → the brief].
- **register_run (the manifest's ground)**: delegates to Registry.register_run — validate → mint RUN-{####} → copy-in freeze → append → return (run_id, manifest, count), the built-in read-back. The manifest is the ground every downstream consult cites: the id universe, the declared verdict set, and quorum — the DONE keying's own data (R8).
- **next_pair (the loop)**: per call — (1) read_manifest(run_id) → quorum + ids; (2) schedule_pairs(ids) → the queue (deterministic, byte-identical per id-set); (3) read_vote_state(run_id) → per_pair_counts (the map built over the full pair universe 0-included, +1 per record with NO supersession filter — the unweighted audit view, the AS-IS consult); (4) the walk: the FIRST pair whose census count < manifest.quorum returns WITH its count; (5) none remains → the DONE signal. The seed: derive_seed(run_id) exists for the default, dead under the ruled order; the composition form [OPEN]. Purity between casts: next_pair mutates nothing; the progression is cast_vote changing the store; the caller owns the loop; the session serves one consult per call.
- **cast_vote (the store's write)**: delegates to VoteLedger.cast_vote — the seven-stage chain; the session adds nothing; the refusals ride through as VotesRefusedError.
- **read_vote_state (the census)**: delegates to VoteLedger.read_vote_state — the unknown run only, NEVER on coverage; the zero-vote run a value.
- **tally_rank (the composed op)**: manifest = read_manifest(run_id); census = read_vote_state(run_id); return tally_votes(manifest, census.vote_log) — the frozen TallyResult whole, never re-computed. The session computes nothing of its own — no scores, no rankings, no coverage verdicts (condition 4); the DONE/SAFE-HALT binary rides U4 whole; the session renders neither, swallows neither.

## 2. THE DONE SIGNAL's mechanics

- **The class**: a dedicated signal class distinct from the refusal lineage, distinguishable from error by TYPE — mechanically an exception, semantically a terminal state (a sentinel priced out twice: it cannot carry evidence; the class of its OWN type so except-RefusedError never catches DONE). The exact name [OPEN → the brief].
- **The fields**: expected = the queue's full pair count at quorum; found = the exhausted state (every pair at quorum k); next_action = the tally path — R12's DONE. Raised, never returned. Exact bytes [OPEN].
- **The exact raise point**: the loop's fall-through — the single ordered scan (walk the queue in schedule_pairs' order, return the first under-quorum pair with its count, raise only at the scan's end — every pair ≥ quorum). The early return the hot path; the raise the terminal. No second pass: one walk, the count riding the pair it was found on.

## 3. THE SEAM'S HONESTY — the census-as-is consult vs U4's weighted gate

- **The two keyings off the same quorum (R8), each at its ruled datum**: U5's consult — the census's per_pair_counts AS-IS (+1 per record, no supersession filter — the unweighted audit view); U4's gate — the WEIGHTED counts (the exclusion set E; the tally builds its own). The divergence, constructed exactly: one pair at k=2 holding a superseded original + its correction — the census counts both (2); the weighting excludes the original (1). Then: next_pair — 2 ≥ 2 ⇒ DONE raised; tally_rank — leg 3 sees 1 < 2 ⇒ SAFE HALT raised, naming "(a, b) 1 of 2" and the shortfall vote.
- **Why this IS the design's shape**: each unit honors its own ruled datum — U3's census the audit view (counts as data, never a verdict); U4 owns the weighting alone (the Parnas fold's other half); U5 consults AS-IS by its own gate's letter. If U5 consulted U4's weighted view, it would put U4's keying behind the session's loop — the same leak the no-score fold forbids, and a third counting authority the composition layer is forbidden to own. Reconciliation is not merely declined; it is structurally out of grammar.
- **The agreement zone**: absent corrections, E is empty ⇒ census count == weighted count on every pair — the two keyings agree exactly. The divergence exists precisely when unresolved corrections stand in the log — the divergence IS a corrections-present detector.
- **The divergence as the data-quality signal**: DONE-at-next_pair + SAFE-HALT-at-tally_rank is the observable that a correction has displaced a live judgment below quorum; the caller learns it from the safe halt's own next_action. The session names it, never reconciles it.

## 4. THE SESSION'S STATE

- **Beyond the two stores: nothing** — the session holds only the wiring. No queue cache, no counts cache, no manifest cache, no scores (condition 4's letter holds by construction).
- **The queue: per-call derivation, not a cache** — the session CALLS schedule_pairs (the citation; never re-derived = never invents a second enumeration). The per-call cost O(n²), 4,950 pairs, trivial. A cache would be statefulness: a derived view the session owns, able to go stale, against the fresh-value-per-call discipline.
- **The counts: per-call consult** — read_vote_state per next_pair, a fresh census per call.
- **The manifest: read, never cached** — the freeze forecloses staleness at the data level; the discipline still chooses the read (ground truth at read time, FR-MEM-0001; the freeze makes the read cheap). Lean: no cache.

## 5. THE EDGES + THE TEST EDGES

1. **The end-to-end fixture**: register → next_pair (the returned pair + count asserted) → cast → … → DONE raised → tally_rank → the exact expected emission (hand-computable, every field asserted — the tally-brief test-2 precedent).
2. **The DONE path's fields**: the signal caught BY TYPE (an except clause that would not catch any RefusedError — the type-level distinction is the assert), the three fields verified, raised never returned.
3. **The seam-divergence fixture**: the correction at k=2 — in ONE test, next_pair raises DONE AND tally_rank raises TallyRefusedError naming the shortfall — the divergence named, never hidden.
4. **The swap/invariant edges**: register_run's refusals ride through unchanged; cast_vote's refusals ride through as VotesRefusedError verbatim; the swapped-citation and declared-set refusals unchanged.
5. **The unknown-run wrap's type at U5's surface [OPEN]**: the miss lands as RegistryRefusedError from next_pair/tally_rank's read_manifest but as VotesRefusedError from cast_vote/read_vote_state — two refusal types on one miss at the public face unless U5 wraps. Options: (a) wrap into VotesRefusedError per U3's precedent (the LEAN — the family's settled wrap form); (b) a session-level refusal class; (c) let RegistryRefusedError ride.
6. **Derived edges riding the gate's letter**: next_pair's purity-between-casts (the same pair returns between casts); the first-under-quorum order (the queue's first under-quorum pair, deterministic); the zero-vote run (the first pair at count 0 — a value); the k>1 partial (a pair at 1 of 2 returns with count 1).
7. **The floor**: pyright 0/0/0, ruff zero findings, zero ignores — named rulings only; kensho's independent re-run green.

*The [OPEN] list (each → the brief): (1) the construction form — U5 constructs the two stores vs. accepts them; (2) next_pair's return carrier — the op-2 triple vs. Pair + count; (3) the seed's composition at U5 — derive_seed(run_id) consumed for op 2's default or left dead; (4) the DONE signal's exact name and bytes; (5) the unknown-run wrap's type at U5's surface (lean (a)); (6) the manifest-cache question (lean: no cache); (7) the test list's exact names. Provenance: rikai (理解), packet understand/session, route prioritree-core (U5), 2026-11-20. Read-only held; the tree is the truth.*
