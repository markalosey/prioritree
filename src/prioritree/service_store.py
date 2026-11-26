# Copyright (C) 2026 Mark Losey. All rights reserved.
"""service_store — the lock seam: the CLI's process boundary become a lock boundary at the request tier.

The service-store unit (Q-service-concurrency's ruling: the single-writer contract held
AT THE REQUEST TIER — the machine-wide file lock OUTERMOST (the mcp-server unit's
flock seam, store_lock.Lock — the lock that spans processes), the process-wide
threading.Lock within, wrapping each request's whole act;
the CLI's one-act-per-process shape translated to many-requests-per-process BY
CONSTRUCTION, not by convention). Each verb is ONE acquisition around the load + the
act whole: the lock serializes ACTS (each act spans thousands of bytecodes plus file I/O
— the load→rebuild window the GIL cannot close); the GIL serializes bytecodes and is
NEVER load-bearing (the file I/O releases the GIL around the syscalls; the contract
rests on the LOCK alone). The reads lock too — a read concurrent with a write would
catch the mid-append tail and fire the crash-tail refusal spuriously on a healthy run.
The FENCE: zero edits to run_store.py or any core module — the seam composes Persist's
public surface only (register/load, the verbs delegated; the privates never touched);
load never exposed (each verb loads INSIDE the lock — per-request composition, the
dedup index fresh by construction). The door's values returned verbatim; the door's and
store's refusals ride through BY TYPE, never wrapped. The multi-process widening held
by the flock outermost: every standing writer local, none bypassing the seam (the
single-worker banking superseded). Five-field docstrings on every public symbol;
stdlib only (threading; the flock seam store_lock, itself stdlib-only).
"""

from __future__ import annotations

from threading import Lock as ThreadLock
from typing import TYPE_CHECKING

from prioritree.run_store import Persist
from prioritree.store_lock import Lock

if TYPE_CHECKING:
    from collections.abc import Sequence
    from pathlib import Path

    from prioritree.registry import ItemRow, OperatorDeclaration, RunManifest
    from prioritree.scheduler import Pair
    from prioritree.tally import TallyResult
    from prioritree.votes import VoteCensus, VoteRecord

__all__ = [
    "Serialize",
]


class Serialize:
    """Serialize — the requests' store acts under the file lock outermost, the process-wide lock within.

    Purpose: serialize the requests' store acts under the machine-wide file lock
    OUTERMOST and the process-wide threading.Lock within — each verb
    is a single acquisition wrapping the load + the act whole (register's mkdir-scan-
    mint-write inside one acquire: the TOCTOU closed by construction; every other verb
    loads the run file INSIDE the lock, acts, returns — a read never sees a half-state,
    the crash-tail window priced out at this tier). The CLI's process boundary BECOME a
    lock boundary: the single-writer contract held by construction, not convention. The
    seam composes Persist's PUBLIC surface only (the fence: zero edits to run_store.py
    or any core module); load never exposed — each verb loads inside the lock. The GIL
    never load-bearing: the lock serializes acts, the GIL bytecodes — the contract rests
    on the lock alone. The multi-process widening held by the flock outermost (every
    standing writer local, none bypassing the seam).
    Refuses when: never its own refusal — the door's refusals (VotesRefusedError,
    TallyRefusedError, ExhaustedQueue) and the store's own (StoreRefusedError) ride
    through verbatim BY TYPE, never wrapped, never conflated (the face unit maps them
    to the statuses; this seam never holds the lock across rendering).
    Re-run: deterministic given the store state — the lock never changes values, only
    interleavings (the door's re-run semantics ride through unchanged).
    Touches: the run files through Persist, and the lockfile at the home (the flock
    seam's own — created on demand, never truncated, never deleted); the seam adds
    no state of its own — the threading lock and the injected home are its whole holdings.
    Provenance: Q-service-concurrency (per-request composition under one process-wide
    lock), Q-service-store (the run-store per request, store-as-parameter), the
    composition (service-store §0-§5), G-SERVICE-STORE (the four conditions), the
    naming law ("Serialize the requests' store acts under one process-wide lock" — the
    act's first word).
    """

    def __init__(self, store_home: Path) -> None:
        """Initialize the seam: mint the lock, hold the store home as the parameter.

        Purpose: mint the process-wide lock AT CONSTRUCTION (one lock, all runs, all
        verbs — the single critical section) and hold the store home as the injected
        parameter (store-as-parameter: never a module-level singleton; STORE_HOME stays
        the face unit's own default, never re-defaulted here — the hidden-global drift
        refused). The routes never touch the lock — acquire/release lives inside the
        verbs alone.
        Refuses when: never — construction mints and holds, nothing else.
        Re-run: idempotent — a fresh seam over the given home (the lock never held
        across constructions; test isolation by injection).
        Touches: only its own references (the lock object, the injected path).
        Provenance: service-store-brief §1 (the constructor, the home required — open
        question 5 ruled), §2 (the lock minted at construction, container-held),
        Q-service-store (store-as-parameter), G-SERVICE-STORE.
        """
        self._lock = ThreadLock()
        self._store_home = store_home

    def register(
        self,
        items: Sequence[Sequence[str] | ItemRow],
        operator: OperatorDeclaration,
        quorum: int = 1,
    ) -> str:
        """Register the run under the file lock outermost — the whole mkdir-scan-mint-write in one acquire.

        Purpose: serialize the register act — ONE acquisition wrapping Persist.register
        WHOLE (the door's register_run, the store home's mkdir, the scan, the mint, the
        manifest write — the TOCTOU closed by construction: no register's scan ever sees
        another's half-write), returning the STEM alone (persist.run_id — the file's
        name, the cross-process identity; the in-file handle never crosses the seam).
        The face unit's 201 carries the stem; the manifest is durable in the file.
        Refuses when: never its own refusal — the door's registration refusals
        (VotesRefusedError) and the store's own (StoreRefusedError, the failed append)
        ride through verbatim BY TYPE, before any byte lands.
        Re-run: deterministic given the store home's state — the lock never changes
        values, only interleavings (the file-name mint continues the home's max; the
        dir is the truth).
        Touches: the store home (created if absent) and the new run file — through
        Persist only.
        Provenance: service-store-brief §2-§3 (the critical section's boundary, the
        stem-alone ruling — open question 4 ruled), Q-service-concurrency,
        G-SERVICE-STORE.
        """
        with Lock(self._store_home), self._lock:
            return Persist.register(self._store_home, items, operator, quorum).run_id

    def serve(self, run_id: str, seed: int | None = None) -> tuple[str, str, int]:
        """Serve the next under-quorum pair under the file lock outermost — the load and the read in one acquire.

        Purpose: serialize the serve act — load the run file INSIDE the lock (the fresh
        door rebuilt from the file; load never exposed), delegate to the door's
        next_pair, return the door's triple VERBATIM. The read locks too: a serve
        concurrent with a cast would catch the mid-append tail and fire the crash-tail
        refusal spuriously on a healthy run — inside the lock the read never sees a
        half-state.
        Refuses when: never its own refusal — the store's own (StoreRefusedError) and
        the door's (VotesRefusedError) ride through verbatim BY TYPE; the queue
        exhausted — ExhaustedQueue rides through BY TYPE (the DONE signal, never
        swallowed).
        Re-run: deterministic given the store state (pure between casts; the door's
        semantics verbatim).
        Touches: only the run file (a read) — through Persist only.
        Provenance: service-store-brief §2-§3, Q-service-concurrency, G-SERVICE-STORE.
        """
        with Lock(self._store_home), self._lock:
            return Persist.load(self._store_home, run_id).serve(seed)

    def cast(
        self,
        run_id: str,
        pair: Pair | Sequence[str],
        winner: str,
        comparator_id: str,
        comparator_class: str,
        notes: str | None = None,
        supersedes: str | None = None,
    ) -> tuple[str, VoteRecord, int, bool]:
        """Cast the vote under the file lock outermost — the load, the cast, and the append in one acquire.

        Purpose: serialize the cast act — load the run file INSIDE the lock (the dedup
        index fresh BY CONSTRUCTION: the re-cast's load rebuilds the door from the file,
        so the ack under the lock is honest), delegate to the door's cast_vote, return
        the ack quadruple VERBATIM. The seven-argument form mirrors Persist.cast 1:1
        (PLR0913/PLR0917 firing — the pyproject's named ruling rides, the run_store.py
        precedent re-cited).
        Refuses when: never its own refusal — the store's own (StoreRefusedError) and
        the door's (VotesRefusedError) ride through verbatim BY TYPE, never wrapped.
        Re-run: deterministic given the store state — the lock never changes values,
        only interleavings (a byte-identical re-send is the door's loud ack; the count
        unchanged, never double-counted).
        Touches: the run file (append) and the door's own stores — through Persist only.
        Provenance: service-store-brief §2-§3, Q-service-concurrency, G-SERVICE-STORE.
        """
        with Lock(self._store_home), self._lock:
            return Persist.load(self._store_home, run_id).cast(
                pair,
                winner,
                comparator_id,
                comparator_class,
                notes,
                supersedes,
            )

    def census(self, run_id: str) -> VoteCensus:
        """Census the run under the file lock outermost — the load and the read in one acquire.

        Purpose: serialize the census act — load the run file INSIDE the lock, delegate
        to the door's read_vote_state, return the frozen snapshot VERBATIM (the counts
        as data, the full vote log in mint order). The read locks too: a census
        concurrent with a cast would catch the mid-append tail and fire the crash-tail
        refusal spuriously on a healthy run — inside the lock the read never sees a
        half-state.
        Refuses when: never its own refusal — the store's own (StoreRefusedError) and
        the door's (VotesRefusedError) ride through verbatim BY TYPE; never on coverage
        (the manifest-only file loads to the all-zero maps + the empty log — a value).
        Re-run: deterministic given the store state (pure between casts).
        Touches: only the run file (a read) — through Persist only.
        Provenance: service-store-brief §2-§3, Q-service-concurrency, G-SERVICE-STORE.
        """
        with Lock(self._store_home), self._lock:
            return Persist.load(self._store_home, run_id).census()

    def rank(self, run_id: str) -> TallyResult:
        """Rank the run under the file lock outermost — the load and the tally in one acquire.

        Purpose: serialize the rank act — load the run file INSIDE the lock, delegate
        to the door's tally_rank, return the frozen TallyResult WHOLE VERBATIM. The
        read locks too: a rank concurrent with a cast would catch the mid-append tail
        and fire the crash-tail refusal spuriously on a healthy run — inside the lock
        the read never sees a half-state.
        Refuses when: never its own refusal — the store's own (StoreRefusedError), the
        door's (VotesRefusedError), and the coverage gate's (TallyRefusedError — the
        SAFE HALT) ride through verbatim BY TYPE, never swallowed, never wrapped.
        Re-run: deterministic given the store state (same store state yields the
        byte-identical emission).
        Touches: only the run file (a read) — through Persist only.
        Provenance: service-store-brief §2-§3, Q-service-concurrency, G-SERVICE-STORE.
        """
        with Lock(self._store_home), self._lock:
            return Persist.load(self._store_home, run_id).rank()

    def manifest(self, run_id: str) -> RunManifest:
        """Manifest the run's frozen ground under the file lock outermost — the load and the read in one acquire.

        Purpose: serialize the manifest act — load the run file INSIDE the
        lock, delegate to the container's manifest accessor, return the frozen
        RunManifest WHOLE VERBATIM. The read locks too: a manifest read
        concurrent with a cast would catch the mid-append tail and fire the
        crash-tail refusal spuriously on a healthy run — inside the lock the
        read never sees a half-state. The load is the FULL pre-pass (every
        public verb rides it — a manifest read prices the file's WHOLE
        integrity: a corrupt vote line refuses it as StoreRefusedError).
        Refuses when: never its own refusal — the store's own
        (StoreRefusedError) rides through verbatim BY TYPE; no value refusal
        exists at this read (the manifest line already validated at load's
        pre-pass).
        Re-run: deterministic given the store state (the clock-free surface
        re-derives identically at every load).
        Touches: only the run file (a read) — through Persist only.
        Provenance: the service unit brief §1-§2 (the sixth query's seam
        verb — ONE lock acquisition), the ux design §2 (the mechanism named),
        Q-service-concurrency (the read-locks-too law), G-SERVICE-STORE.
        """
        with Lock(self._store_home), self._lock:
            return Persist.load(self._store_home, run_id).manifest()
