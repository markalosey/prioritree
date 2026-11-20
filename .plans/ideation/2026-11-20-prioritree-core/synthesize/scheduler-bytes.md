# synthesize/scheduler-bytes — THE SCHEDULER UNIT'S EXACT BYTES (G-SCHEDULER-BRIEF approved; the landing source)

- Provenance: togo (統合, integrate), packet synthesize/scheduler-bytes, route prioritree-core, 2026-11-20 — two single-goal authoring acts (amendment 15), both returned clean. Landed by shinko via patch; read-back verified.
- Ground: the approved brief (synthesize/scheduler-brief.md — G-SCHEDULER-BRIEF green, the defaults law); the style precedent registry.py / test_registry.py.

## Deliverable 1 — src/prioritree/scheduler.py (byte-exact; land as the create)

```python
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
from collections.abc import Iterable
from dataclasses import dataclass

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
        for inner in sorted_ids[i + 1 :]:
            queue.append(Pair(item_a=outer, item_b=inner))
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
```

## Deliverable 2 — tests/test_scheduler.py (byte-exact; land as the create)

```python
# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The scheduler unit's property tests — the thirteen named edges (scheduler-brief §4)."""

from prioritree.scheduler import SEED_ALGORITHM, SEED_BYTES, Pair, derive_seed, schedule_pairs


def test_exact_count_10_items_45_pairs() -> None:
    """10 distinct ids schedule exactly 45 pairs — the count law n(n-1)/2."""
    ids = [f"id-{index:02d}" for index in range(10)]
    assert len(schedule_pairs(ids)) == 45


def test_exact_count_100_items_4950_pairs() -> None:
    """100 distinct ids schedule exactly 4,950 pairs — the verified fence's figure."""
    ids = [f"id-{index:03d}" for index in range(100)]
    assert len(schedule_pairs(ids)) == 4950


def test_zero_duplicates() -> None:
    """The queue holds no duplicate pair — Pair's hashability rides the set idiom."""
    ids = [f"id-{index:02d}" for index in range(10)]
    queue = schedule_pairs(ids)
    assert len(set(queue)) == len(queue)


def test_zero_missing_full_coverage() -> None:
    """The queue equals an independently authored brute-force double loop — full coverage."""
    ids = [f"id-{index:02d}" for index in range(10)]
    ordered = sorted(ids)
    expected: list[Pair] = []
    for i in range(len(ordered)):
        for j in range(i + 1, len(ordered)):
            expected.append(Pair(item_a=ordered[i], item_b=ordered[j]))
    assert set(schedule_pairs(ids)) == set(expected)


def test_degree_law_each_id_in_n_minus_1_pairs() -> None:
    """Each id appears in exactly n-1 pairs — the degree sum localizes any missing pair."""
    ids = [f"id-{index:02d}" for index in range(10)]
    queue = schedule_pairs(ids)
    for id_ in ids:
        count = sum(1 for pair in queue if pair.item_a == id_ or pair.item_b == id_)
        assert count == 9


def test_replays_byte_identical() -> None:
    """Two calls on the same ids produce equal queues — the deterministic enumeration."""
    ids = [f"id-{index:02d}" for index in range(10)]
    assert schedule_pairs(ids) == schedule_pairs(ids)


def test_seed_derivation_stable() -> None:
    """Same run_id derives the same seed across calls — the blake2b digest forecloses the PYTHONHASHSEED trap."""
    assert derive_seed("RUN-0001") == derive_seed("RUN-0001")
    assert derive_seed("RUN-0001") != derive_seed("RUN-0002")
    assert SEED_ALGORITHM == "blake2b"
    assert SEED_BYTES == 8


def test_set_keyed_stability() -> None:
    """The same id-set in different payload orders yields the same queue — sort-first keyed on the set."""
    assert schedule_pairs(["b", "a", "c"]) == schedule_pairs(["c", "a", "b"])


def test_canonical_form_id_sorted() -> None:
    """Every pair satisfies item_a < item_b strict — the canonical form every vote cites."""
    ids = [f"id-{index:02d}" for index in range(10)]
    for pair in schedule_pairs(ids):
        assert pair.item_a < pair.item_b


def test_minimum_two_ids_one_pair() -> None:
    """Two distinct ids schedule exactly one canonical pair — the ruled flow's minimum."""
    assert schedule_pairs(["b", "a"]) == (Pair(item_a="a", item_b="b"),)


def test_empty_ids_yield_empty_queue() -> None:
    """An empty id list yields the empty queue — the count law's 0, a legal value not a refusal."""
    assert schedule_pairs([]) == ()


def test_single_id_yields_empty_queue() -> None:
    """A single id yields the empty queue — the count law's 0 at n=1."""
    assert schedule_pairs(["only"]) == ()


def test_reserved_seed_parameter_unused_by_ruled_order() -> None:
    """An explicit seed changes nothing under the ruled order — the reservation held, not a promise."""
    ids = [f"id-{index:02d}" for index in range(10)]
    assert schedule_pairs(ids, seed=12345) == schedule_pairs(ids)
```

## Deliverable 3 — the landing steps (each its own single-goal dispatch)

1. Create src/prioritree/scheduler.py — patch-create with Deliverable 1's block (104 lines; the create hunk @@ -1,0 +1,104 @@). Expected: byte-identical to the block.
2. Create tests/test_scheduler.py — patch-create with Deliverable 2's block (90 lines; @@ -1,0 +1,90 @@). Expected: byte-identical.
3. The floor: make test (expected 26 passed — the 13 scheduler property tests + the 13 prior: 12 registry + 1 smoke), make lint (All checks passed!), make typecheck (0 errors, 0 warnings, 0 informations).
4. The read-back: both files against this addendum; deltas reported (expected: none).
