# Copyright (C) 2026 Mark Losey. All rights reserved.
"""session — the chain's public face: register → schedule → vote → tally, composed.

The session unit (U5): the composition layer the wrappers cite — ONE Registry
behind both stores by construction (the session constructs VoteLedger(registry)
internally; the mismatched-pair hazard unrepresentable), the five ops of the
frozen interface (register_run, next_pair, cast_vote, read_vote_state,
tally_rank), and the DONE signal minted here whole — ExhaustedQueue, the
typed terminal state raised when the first-under-quorum walk falls through
(the queue from U2, the counts from U3's census, the quorum from U1's
manifest; distinguishable from error BY TYPE, hence suffix-free — the
StopIteration kin). The fence held by construction: no scores, no rankings,
no coverage verdicts (U4's alone — tally_votes called, its frozen TallyResult
returned whole); the pair set CITED never re-derived (schedule_pairs called);
the census consulted AS-IS, never re-weighted (the census-vs-weighted seam
NAMED and carried, never reconciled); no cache beyond the two store
references; no CLI/service/web concerns, no comparator-elicitation UX.
Zero runtime dependencies; no subprocess; NO datetime — nothing at U5 stamps
time.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence

from prioritree.registry import (
    ItemRow,
    OperatorDeclaration,
    Registry,
    RegistryRefusedError,
    RunManifest,
)
from prioritree.scheduler import Pair, derive_seed, schedule_pairs
from prioritree.tally import TallyRefusedError, TallyResult, tally_votes
from prioritree.votes import (
    PRESENTATION_CANONICAL,
    VoteCensus,
    VoteLedger,
    VoteRecord,
    VotesRefusedError,
)

__all__ = [
    "ExhaustedQueue",
    "Session",
    "TallyRefusedError",
]


class ExhaustedQueue(Exception):
    """ExhaustedQueue — the DONE signal: the queue is exhausted, every pair at quorum.

    Purpose: carry the walk's terminal state as data — expected (the full
    scheduled queue at its quorum), found (the fall-through, the census's
    AS-IS counts named), next_action (the tally path, the seam named and
    carried) — raised, never returned, at next_pair's fall-through; caught
    BY TYPE by the wrappers (the type distinction IS the hierarchy: never a
    subclass of any RefusedError, so an except-RefusedError clause never
    catches DONE; the suffix-free name per the StopIteration precedent —
    the Error suffix in this family marks the refusal lineage).
    Refuses when: never — it IS the terminal signal, not a refusal; the
    message renders all three fields so an uncaught traceback still names
    the state and the path ("exhausted —", never "refused —").
    Re-run: deterministic — the same exhausted state raises the same three
    fields; a later cast below quorum makes next_pair return a pair again
    (the signal is a state read, not a latch).
    Touches: nothing — a plain Exception subclass (zero runtime deps).
    Provenance: the DONE mint site — U5 WHOLE (scheduler-brief §1 riding
    G-SESSION condition 2), the naming law ("the queue is exhausted" — the
    act-statement's own words), G-SESSION condition 3, session-brief §2
    (the suffix ruling, the fields' bytes); the census-as-is consult
    (G-SESSION condition 3, session-brief §4 — the divergence under
    corrections named, never hidden).
    """

    def __init__(self, expected: str, found: str, next_action: str) -> None:
        """Initialize the signal with its three named fields.

        Purpose: carry expected/found/next_action plus the rendered message
        (the signal's own prefix — "exhausted —", never "refused —").
        Refuses when: never.
        Re-run: idempotent.
        Touches: nothing.
        Provenance: session-brief §2 (the family grammar's render form, the
        signal's own prefix clause).
        """
        self.expected = expected
        self.found = found
        self.next_action = next_action
        super().__init__(f"exhausted — expected: {expected} | found: {found} | next: {next_action}")


class Session:
    """Session — the chain's public face: the five ops composed over the two stores.

    Purpose: Session the chain into the library's public face — register →
    schedule → vote → tally composable at any coverage point, emitting the
    stable ranking serialization; ONE Registry instance backs both the
    session's read path and the ledger's write-time ground-truth checks by
    construction (VoteLedger(registry) constructed internally — the
    one-registry discipline; the mismatched-pair hazard unrepresentable);
    the stores PRIVATE behind the five ops (the frozen wrapper contract).
    Refuses when: the ops refuse — every RegistryRefusedError crossing this
    surface is wrapped into VotesRefusedError (ONE refusal grammar, the U3
    wrap form verbatim); the ledger's own refusals ride through verbatim;
    ExhaustedQueue at next_pair's fall-through; TallyRefusedError through
    tally_rank (the SAFE HALT, U4's own signal — never swallowed, never
    wrapped).
    Re-run: next_pair and tally_rank re-derive per call (the queue from the
    manifest's ids, the census a fresh read — no cache beyond the two store
    references); the stores themselves are append-only.
    Touches: only the two injected-internally stores — no files, no
    subprocess, no DB; SINGLE-PROCESS by contract; nothing of its own is
    computed, nothing the units own is re-owned.
    Provenance: G-SESSION (the five conditions), the U5 row's act ("Session
    the chain into the library's public face…"), the five-op interface,
    session-brief §1 (the container, the one-registry discipline, the
    private stores); discover/session and understand/session (the legs
    riding the brief).
    """

    def __init__(self, registry: Registry) -> None:
        """Initialize the session over the injected registry.

        Purpose: construct the container the caller holds — the registry
        injected by the caller, the ledger constructed internally over that
        SAME registry (ONE Registry instance behind both stores by
        construction; never a module-level singleton — test isolation).
        Refuses when: never.
        Re-run: idempotent — a fresh session over the given registry.
        Touches: only its own two store references.
        Provenance: G-SESSION, session-brief §1 (the container's
        constructor + the private stores ruling; the U5 row's act).
        """
        self._registry = registry
        self._ledger = VoteLedger(registry)

    def _read_manifest(self, run_id: str) -> RunManifest:
        """Resolve the manifest via the registry, wrapping its refusal.

        Purpose: the wrap — catch RegistryRefusedError, re-raise
        VotesRefusedError carrying the same expected/found/next_action
        verbatim, from refusal (the session's surface speaks ONE refusal
        grammar; the registry's rendered live-set rides through unchanged).
        Refuses when: the run_id is not a live registry handle — naming the
        live set (the registry's own rendering).
        Re-run: deterministic.
        Touches: nothing — a read through the registry.
        Provenance: session-brief §3 (the unknown-run wrap, lean (a)), the
        U3 form verbatim (votes.py:298-318).
        """
        try:
            return self._registry.read_manifest(run_id)
        except RegistryRefusedError as refusal:
            raise VotesRefusedError(
                expected=refusal.expected,
                found=refusal.found,
                next_action=refusal.next_action,
            ) from refusal

    def register_run(
        self,
        items: Sequence[Sequence[str] | ItemRow],
        operator: OperatorDeclaration,
        quorum: int = 1,
    ) -> tuple[str, RunManifest, int]:
        """Register the run — verbatim delegation to the registry, wrapped.

        Purpose: the immutable (items, operator, quorum) ground — delegate
        inside the wrap clause, return the (run_id, manifest, count) triple
        verbatim (the built-in read-back); the session adds nothing (the
        manifest's ground is U1's).
        Refuses when: the registry refuses (fewer than two rows, duplicate
        ids, malformed rows or declaration, illegal verdict set, illegal
        quorum) — landed here as VotesRefusedError, the registry's three
        fields verbatim, raised before any byte lands.
        Re-run: deterministic given the same store state; an identical
        re-registration mints a NEW run (no dedup at the library tier).
        Touches: only the registry's own store (the single mutating op on
        that store).
        Provenance: op 1, session-brief §3.1 (the wrap, the verbatim
        delegation), the five-op interface.
        """
        try:
            return self._registry.register_run(items, operator, quorum)
        except RegistryRefusedError as refusal:
            raise VotesRefusedError(
                expected=refusal.expected,
                found=refusal.found,
                next_action=refusal.next_action,
            ) from refusal

    def next_pair(self, run_id: str, seed: int | None = None) -> tuple[str, str, int]:
        """Next under-quorum pair — the composed loop: manifest, queue, census.

        Purpose: per call, pure between calls — (1) read the manifest (the
        miss wrapped); (2) resolve the seed: derive_seed(run_id) when None,
        else the caller's seed, and derive the queue from the manifest's ids
        via schedule_pairs (the queue per-call, CITED never re-derived);
        (3) read the census (the fresh per-call consult, the counts AS-IS);
        (4) walk the queue in order — the FIRST pair whose census count <
        quorum returns (item_a, item_b, count), the count riding the pair it
        was found on; (5) the fall-through: raise ExhaustedQueue (§2's bytes)
        — the single ordered scan, the raise only at the scan's end, no
        second pass.
        Refuses when: the run is unknown (the wrap); the queue exhausted —
        ExhaustedQueue, the DONE signal, raised never returned (NOT a
        refusal: a value-returning op whose terminal state is a typed
        signal; no state mutated, no scores computed).
        Re-run: pure between calls — the same store state yields the same
        pair; a re-call between casts returns the same pair; a fresh run
        returns the first scheduled pair with count 0 (a value, never a
        refusal).
        Touches: nothing — the reads ride the registry and the ledger; no
        state of its own.
        Provenance: op 2, session-brief §3.2 (the loop's five steps, the
        op-2 triple carrier, the seed's consumption — derive_seed
        consumed as op 2's default), G-SESSION condition 3 (the DONE minted
        at U5 whole); the census-as-is keying (session-brief §4 — the
        census-vs-weighted seam named and carried, never reconciled).
        """
        manifest = self._read_manifest(run_id)
        resolved = derive_seed(run_id) if seed is None else seed
        queue = schedule_pairs([row.id for row in manifest.items], seed=resolved)
        census = self._ledger.read_vote_state(run_id)
        for pair in queue:
            count = census.per_pair_counts[pair]
            if count < manifest.quorum:
                return (pair.item_a, pair.item_b, count)
        raise ExhaustedQueue(
            expected=f"all {len(queue)} scheduled pairs at quorum k={manifest.quorum}",
            found=(
                "the queue is exhausted — the walk fell through with no under-quorum pair "
                "(every pair at quorum on the census's AS-IS counts)"
            ),
            next_action=(
                "call tally_rank(run_id) — the tally path (R12's DONE; a standing correction "
                "can still SAFE HALT it — the census-vs-weighted seam, named and carried)"
            ),
        )

    def cast_vote(
        self,
        run_id: str,
        pair: Pair | Sequence[str],
        winner: str,
        comparator_id: str,
        comparator_class: str,
        notes: str | None = None,
        supersedes: str | None = None,
        presentation_order: str = PRESENTATION_CANONICAL,
    ) -> tuple[str, VoteRecord, int, bool]:
        """Cast one judgment — verbatim delegation to the ledger.

        Purpose: the seven-stage chain is U3's, the session adds nothing —
        return the ledger's (vote_id, record, count, acknowledged) quadruple
        verbatim (the loud dedup ack included; the presentation_order the
        order-bias probe's instrument riding last, additive);
        VotesRefusedError rides through verbatim (the ledger already speaks
        the grammar — no wrap needed here).
        Refuses when: the ledger refuses (malformed payload; unknown run;
        pair outside the legal set, the swapped citation named; winner
        outside the declared set; invalid supersede target) — every refusal
        raises VotesRefusedError before any byte lands; NEVER refuses on
        content plausibility.
        Re-run: deterministic given the same store state; the re-vote
        semantics (R9) are the ledger's, riding through unchanged.
        Touches: only the ledger's own store and dedup index.
        Provenance: op 3, session-brief §3.3 (the verbatim delegation, the
        eight arguments ARE op 3's ruled signature — the probe's instrument
        additive), the five-op interface.
        """
        return self._ledger.cast_vote(
            run_id,
            pair,
            winner,
            comparator_id,
            comparator_class,
            notes,
            supersedes,
            presentation_order,
        )

    def read_vote_state(self, run_id: str) -> VoteCensus:
        """Read the run's vote state — verbatim delegation to the ledger.

        Purpose: the census — a fresh frozen value per call (the counts as
        data over the full pair universe, the full vote log in mint order);
        the audit surface every gate's evidence leg rides.
        Refuses when: the ledger refuses the unknown run ONLY — never on
        coverage (the zero-vote run reads back all-zero maps + the empty
        log: a VALUE, never a refusal).
        Re-run: pure — re-reading is stable between casts.
        Touches: nothing — a read.
        Provenance: op 4, session-brief §3.4 (the verbatim delegation),
        the five-op interface.
        """
        return self._ledger.read_vote_state(run_id)

    def tally_rank(self, run_id: str) -> TallyResult:
        """Tally the run's votes — the pure projection composed: manifest, census, tally.

        Purpose: read the manifest (the miss wrapped), read the census, and
        return tally_votes(manifest, census.vote_log) — the frozen TallyResult
        whole, never re-computed, never re-derived; the "stable ranking
        serialization" realized by the frozen value itself; the session
        computes nothing of its own (scores, rankings, coverage verdicts —
        U4's alone).
        Refuses when: the run is unknown (the wrap); the coverage gate
        fails — TallyRefusedError (the SAFE HALT) propagates VERBATIM,
        never swallowed, never wrapped (U4's own signal; the wrappers render
        it); a cycle never blocks (structural, R11).
        Re-run: pure — same store state ⇒ byte-identical emission
        (tally_votes' purity rides through); well-defined at EVERY
        coverage prefix (a refusal IS a defined outcome).
        Touches: nothing — the reads ride the registry and the ledger; the
        projection is pure.
        Provenance: op 5, session-brief §3.5 (the composition, one name one
        arity — tally_rank U5's composed op, tally_votes U4's heart), R12
        (the strictly binary terminal states), the five-op interface.
        """
        manifest = self._read_manifest(run_id)
        census = self._ledger.read_vote_state(run_id)
        return tally_votes(manifest, census.vote_log)
