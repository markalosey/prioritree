# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The service-store unit's edge tests — the six named edges (service-store-brief §4)."""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from threading import Event
from typing import TYPE_CHECKING

from prioritree.registry import OperatorDeclaration
from prioritree.run_store import Persist, StoreRefusedError
from prioritree.service_store import Serialize
from prioritree.session import ExhaustedQueue
from prioritree.tally import TallyRefusedError
from prioritree.votes import VotesRefusedError

if TYPE_CHECKING:
    from prioritree.votes import VoteRecord

# The payload every shared run carries — three items, the three-pair universe (the landed suite's own form).
ITEMS: tuple[tuple[str, str], ...] = (("a", "one"), ("b", "two"), ("c", "three"))


def _declaration() -> OperatorDeclaration:
    """Build a well-formed operator declaration (the landed suite's own form)."""
    return OperatorDeclaration(id="op-1", question="Which matters more?")


def _clock_free(record: VoteRecord) -> tuple[object, ...]:
    """Return the record's seven clock-free cast fields — the stamps' exclusion, by construction."""
    return (
        record.run_id,
        record.pair,
        record.winner,
        record.comparator_id,
        record.comparator_class,
        record.notes,
        record.supersedes,
    )


def test_interleaving_property_all_casts_land(tmp_path: Path) -> None:
    """Four threads x three distinct casts through the seam — every cast lands, ids unique, the load clean."""
    store_home = tmp_path / "runs"
    seam = Serialize(store_home)
    # The arithmetic walked: four items -> six pairs; the twelve distinct casts land two per pair — each
    # pair's second vote an over-quorum sample at k=1, LEGAL (the count grows past quorum as a new
    # sample). The property is the landing itself, never the per-pair counts.
    items: tuple[tuple[str, str], ...] = (
        ("a", "alpha"),
        ("b", "bravo"),
        ("c", "charlie"),
        ("d", "delta"),
    )
    pairs: tuple[tuple[str, str], ...] = (
        ("a", "b"),
        ("a", "c"),
        ("a", "d"),
        ("b", "c"),
        ("b", "d"),
        ("c", "d"),
    )
    stem = seam.register(items, operator=_declaration())

    def cast_batch(thread_index: int) -> list[bool]:
        """Cast this thread's three distinct votes — the comparator_id the distinctness key."""
        acks: list[bool] = []
        for slot in range(3):
            cast_index = thread_index * 3 + slot
            _vote_id, _record, _count, acknowledged = seam.cast(
                stem,
                pairs[cast_index % len(pairs)],
                "prefer-a" if cast_index % 2 == 0 else "prefer-b",
                comparator_id=f"comparator-{thread_index}-{slot}",
                comparator_class="human" if thread_index % 2 == 0 else "llm",
            )
            acks.append(acknowledged)
        return acks

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(cast_batch, thread_index) for thread_index in range(4)]
        acks = [acknowledged for future in futures for acknowledged in future.result()]
    # Every cast NEW — none rode the dedup ack; every cast landed.
    assert len(acks) == 12
    assert all(acknowledged is False for acknowledged in acks)
    # The fresh Persist.load IS the clean-file oracle — the unserialized doubled-mint refuses loudly here.
    census = Persist.load(store_home, stem).census()
    assert len(census.vote_log) == 12
    assert {record.vote_id for record in census.vote_log} == {f"VOTE-{number:04d}" for number in range(1, 13)}


def test_concurrent_registers_distinct_stems(tmp_path: Path) -> None:
    """Two concurrent registers through one seam — two distinct stems, both files clean (the TOCTOU closed)."""
    store_home = tmp_path / "runs"
    seam = Serialize(store_home)
    first_items: tuple[tuple[str, str], ...] = (("a", "alpha"), ("b", "bravo"))
    second_items: tuple[tuple[str, str], ...] = (("c", "charlie"), ("d", "delta"))
    with ThreadPoolExecutor(max_workers=2) as executor:
        first = executor.submit(seam.register, first_items, _declaration())
        second = executor.submit(seam.register, second_items, _declaration())
        stems = sorted((first.result(), second.result()))
    # Unserialized, both scans see the same max and mint one name — the duplicated manifest refusing at
    # the next load; through the lock, two distinct stems.
    assert stems == ["RUN-0001", "RUN-0002"]
    for stem in stems:
        census = Persist.load(store_home, stem).census()
        assert census.vote_log == ()
        assert set(census.per_pair_counts.values()) == {0}
        assert set(census.per_item_counts.values()) == {0}


def test_ack_under_the_lock(tmp_path: Path) -> None:
    """A byte-identical re-cast through the seam acks — the same id, the count unchanged, nothing appended."""
    store_home = tmp_path / "runs"
    seam = Serialize(store_home)
    stem = seam.register(ITEMS, operator=_declaration())
    first_id, first_record, first_count, first_ack = seam.cast(
        stem,
        ("a", "b"),
        "prefer-a",
        comparator_id="x",
        comparator_class="human",
    )
    second_id, second_record, second_count, second_ack = seam.cast(
        stem,
        ("a", "b"),
        "prefer-a",
        comparator_id="x",
        comparator_class="human",
    )
    # The dedup index fresh BY CONSTRUCTION — the re-cast's load inside the lock rebuilds the door.
    assert first_ack is False
    assert second_ack is True
    assert second_id == first_id
    assert second_record.vote_id == first_record.vote_id
    assert second_count == first_count
    # Nothing appended — the manifest plus the ONE vote line, the file read directly.
    run_file = store_home / f"{stem}.jsonl"
    assert len(run_file.read_text().splitlines()) == 2


def test_serial_equivalence_seam_transparent(tmp_path: Path) -> None:
    """The same acts through the seam and through raw Persist — census maps and the TallyResult identical."""
    acts: tuple[tuple[tuple[str, str], str, str, str], ...] = (
        (("a", "b"), "prefer-a", "x", "human"),
        (("a", "c"), "prefer-a", "y", "llm"),
        (("b", "c"), "prefer-a", "z", "human"),
    )
    # Home A — the same acts THROUGH the seam; home B — the same acts through raw Persist, the CLI's own
    # composition. The same acts -> the same census and tally, trivially deterministic; the seam proven
    # transparent — adds nothing, changes nothing.
    seam = Serialize(tmp_path / "runs-seam")
    stem = seam.register(ITEMS, operator=_declaration())
    for pair, winner, comparator_id, comparator_class in acts:
        seam.cast(stem, pair, winner, comparator_id=comparator_id, comparator_class=comparator_class)
    seam_census = seam.census(stem)
    seam_rank = seam.rank(stem)
    raw = Persist.register(tmp_path / "runs-raw", ITEMS, operator=_declaration())
    for pair, winner, comparator_id, comparator_class in acts:
        raw.cast(pair, winner, comparator_id=comparator_id, comparator_class=comparator_class)
    raw_census = raw.census()
    raw_rank = raw.rank()
    assert stem == raw.run_id
    assert seam_census.per_pair_counts == raw_census.per_pair_counts
    assert seam_census.per_item_counts == raw_census.per_item_counts
    seam_ids = [record.vote_id for record in seam_census.vote_log]
    raw_ids = [record.vote_id for record in raw_census.vote_log]
    assert seam_ids == raw_ids
    for seam_record, raw_record in zip(seam_census.vote_log, raw_census.vote_log, strict=True):
        assert _clock_free(seam_record) == _clock_free(raw_record)
        # THE HONESTY PIN — recorded_at named and excluded (minted per arm): a string on both sides,
        # never compared.
        assert isinstance(seam_record.recorded_at, str)
        assert isinstance(raw_record.recorded_at, str)
    assert seam_rank == raw_rank


def test_false_tail_absent_racing_reads(tmp_path: Path) -> None:
    """Racing readers loop census/serve/rank against a casting writer — zero refusals, the final load clean."""
    store_home = tmp_path / "runs"
    seam = Serialize(store_home)
    stem = seam.register(ITEMS, operator=_declaration())
    pairs: tuple[tuple[str, str], ...] = (("a", "b"), ("a", "c"), ("b", "c"))
    writer_done = Event()

    def cast_all() -> None:
        """Cast the coverage votes then the over-quorum samples — every append racing the readers."""
        try:
            for slot, pair in enumerate(pairs):
                seam.cast(
                    stem,
                    pair,
                    "prefer-a",
                    comparator_id=f"cover-{slot}",
                    comparator_class="human",
                )
            for slot in range(9):
                winner = "prefer-a" if slot % 2 == 0 else "prefer-b"
                seam.cast(
                    stem,
                    pairs[slot % len(pairs)],
                    winner,
                    comparator_id=f"sample-{slot}",
                    comparator_class="llm",
                )
        finally:
            writer_done.set()

    def race_reads() -> list[Exception]:
        """Loop census/serve/rank until the writer is done — collect the seam's whole typed refusal surface."""
        collected: list[Exception] = []
        while not writer_done.is_set():
            try:
                seam.census(stem)
                seam.serve(stem)
                seam.rank(stem)
            except (StoreRefusedError, VotesRefusedError, TallyRefusedError, ExhaustedQueue) as error:
                collected.append(error)
        return collected

    with ThreadPoolExecutor(max_workers=4) as executor:
        writer_future = executor.submit(cast_all)
        reader_futures = [executor.submit(race_reads) for _ in range(3)]
        writer_future.result()
        collected = [error for future in reader_futures for error in future.result()]
    # The door's DONE signal (ExhaustedQueue — the queue drained) and SAFE HALT (TallyRefusedError,
    # pre-coverage) are racing-window VALUES, never the hunted refusal — serve and rank cannot both be
    # legal in one state, so both signals are expected here. Every other raised exception — the
    # spurious crash-tail StoreRefusedError above all — is the failure; anything outside the typed
    # quartet crashes its reader and fails the join loudly.
    refusals = [error for error in collected if not isinstance(error, (ExhaustedQueue, TallyRefusedError))]
    assert refusals == []
    census = Persist.load(store_home, stem).census()
    assert len(census.vote_log) == 12


def test_fence_no_threading_in_run_store() -> None:
    """The fence — run_store.py's bytes carry no threading token: the store never threaded, the seam owns it."""
    module_path = Path(__file__).resolve().parents[1] / "src" / "prioritree" / "run_store.py"
    source = module_path.read_text(encoding="utf-8")
    assert "threading" not in source
