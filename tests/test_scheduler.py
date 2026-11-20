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
        expected.extend(Pair(item_a=ordered[i], item_b=ordered[j]) for j in range(i + 1, len(ordered)))
    assert set(schedule_pairs(ids)) == set(expected)


def test_degree_law_each_id_in_n_minus_1_pairs() -> None:
    """Each id appears in exactly n-1 pairs — the degree sum localizes any missing pair."""
    ids = [f"id-{index:02d}" for index in range(10)]
    queue = schedule_pairs(ids)
    for id_ in ids:
        count = sum(1 for pair in queue if id_ in (pair.item_a, pair.item_b))
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
