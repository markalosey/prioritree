# Copyright (C) 2026 Mark Losey. All rights reserved.
"""scheduler — the pure pairwise enumeration: schedule the full coverage queue.

The scheduler unit (U2): the n(n-1)/2 unordered pairs over the registered ids,
each id-sorted within by construction, the queue a pure function of the id-set
(R7); the seed a reserved seam parameter dead at birth — the hidden scheduler
seam's widening is additive, never rework (R6, the Parnas fence: no vote
values, no comparators, not even counts). Zero runtime dependencies; no
subprocess; ids are opaque structure (codepoint sort, no interpretation).
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Iterable

# The seed derivation's data (content-in-configuration): the digest algorithm
# and byte-width are module-level constants, never magic literals.
SEED_ALGORITHM = "blake2b"
SEED_BYTES = 8


@dataclass(frozen=True)
class Pair:
    """Pair — the canonical form every vote cites (the seam pinned here).

    Purpose: carry one unordered pair as its id-sorted frozen form — the type
    U3's vote records and ground-truth checks cite and U5 composes.
    Refuses when: never at construction — the registry school keeps value types
    bare; the minting op (schedule_pairs) owns correctness by construction.
    Re-run: idempotent — a value type; constructing the same (item_a, item_b)
    twice yields equal pairs; hashable (load-bearing for U3's dedup and the
    counts-map keys).
    Touches: nothing — a pure value.
    Provenance: R7 (unordered-pairs-once, canonical id-sorted), the op-2 spec,
    G-SCHEDULER condition 3, scheduler-brief §2; discover/scheduler and
    understand/scheduler (the legs riding the brief).

    Canonical invariant: item_a < item_b STRICT (ids distinct per U1's
    precondition — _check_duplicates refuses before any byte lands, so no
    duplicate check exists here; no equal pair can arise).
    """

    item_a: str
    item_b: str


def schedule_pairs(ids: Iterable[str], seed: int | None = None) -> tuple[Pair, ...]:
    """Schedule the full pairwise coverage queue (the pure enumeration).

    Purpose: enumerate the complete unordered-pair set — sort the ids
    lexicographically (Python codepoint order, no locale, no case-folding;
    the sort IS the stability mechanism, making enumeration a pure function
    of the SET), then the i<j double loop in lexicographic order emits
    Pair(sorted[i], sorted[j]) — each pair id-sorted within by construction —
    returning the complete queue as one flat tuple; the count law n(n-1)/2
    (10 → 45, 100 → 4,950); the empty/1-item edges yield the empty queue ()
    (legal values, not refusals; the core stays TOTAL).
    Refuses when: never — the total function; duplicate ids and <2 cardinality
    are U1's upstream refusals (landed at registration, cited as a CONTRACT
    PRECONDITION here, never re-policed as dead runtime weight).
    Re-run: deterministic — same id-set → byte-identical queue; set-keyed
    stability (payload order irrelevant — sort-first); replays byte-match
    across processes (no time, no randomness, no environment reads, no set
    iteration).
    Touches: nothing — pure over its argument; no votes, no counts, no
    registry imports (the Parnas fence holds by construction).
    Provenance: R7, the op-2 spec, G-SCHEDULER condition 4, scheduler-brief
    §3; discover/scheduler and understand/scheduler (the legs).

    The seed: the reserved seam parameter (op 2's own "seed?" optional form) —
    UNUSED by the ruled order (nothing stochastic remains at birth); carried
    so the hidden scheduler seam's widening (a future reproducible permutation:
    seed in, same permutation out) is additive, never rework.
    """
    sorted_ids = sorted(ids)
    queue: list[Pair] = []
    for i, outer in enumerate(sorted_ids):
        queue.extend(Pair(item_a=outer, item_b=inner) for inner in sorted_ids[i + 1 :])
    return tuple(queue)


def derive_seed(run_id: str) -> int:
    """Derive the default seed from run_id — the stable digest.

    Purpose: turn a run_id into its stable integer seed — blake2b over the
    run_id's UTF-8 bytes, the first SEED_BYTES big-endian — the reproducible
    key the hidden scheduler seam later consumes; U5 composes this when the
    five-op surface needs op 2's default.
    Refuses when: never — a pure function of its argument.
    Re-run: same run_id → same seed, stable across calls and processes; the
    PYTHONHASHSEED trap named and foreclosed — Python's builtin hash() is
    process-salted for strings and would break byte-stable replays; a content
    digest cannot drift.
    Touches: nothing — pure over its argument (hashlib is stdlib; zero runtime
    dependencies).
    Provenance: R7 (default seed derived from run_id), the op-2 spec, G-SCHEDULER
    condition 4, scheduler-brief §3; discover/scheduler and understand/scheduler
    (the legs).
    """
    digest = hashlib.new(SEED_ALGORITHM, run_id.encode("utf-8")).digest()[:SEED_BYTES]
    return int.from_bytes(digest, "big")
