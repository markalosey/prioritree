# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The run-store unit's edge tests — the six named edges (run-store-brief §5)."""

from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any

import pytest

from prioritree.registry import OperatorDeclaration
from prioritree.run_store import Persist, StoreRefusedError

if TYPE_CHECKING:
    from pathlib import Path

    from prioritree.votes import VoteRecord

# The payload every run shares — three items, the three-pair universe (content-in-configuration).
ITEMS: tuple[tuple[str, str], ...] = (("a", "one"), ("b", "two"), ("c", "three"))


def _declaration() -> OperatorDeclaration:
    """Build a well-formed operator declaration (the landed suites' own form)."""
    return OperatorDeclaration(id="op-1", question="Which matters more?")


def _register(store_home: Path) -> Persist:
    """Register the three-item run at a tmp home — the manifest line, no votes yet."""
    return Persist.register(store_home, ITEMS, operator=_declaration())


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


def test_round_trip_clock_free_surface_equal(tmp_path: Path) -> None:
    """Register + four casts (mixed classes, one correction) → fresh load → the §3 surface equal, stamps excluded."""
    store_home = tmp_path / "runs"
    store = _register(store_home)
    store.cast(("a", "b"), "prefer-a", comparator_id="x", comparator_class="human")
    store.cast(("a", "c"), "prefer-b", comparator_id="y", comparator_class="llm")
    store.cast(("b", "c"), "tie", comparator_id="z", comparator_class="human")
    store.cast(("a", "b"), "prefer-b", comparator_id="x", comparator_class="human", supersedes="VOTE-0001")
    before = store.census()
    before_rank = store.rank()
    reloaded = Persist.load(store_home, store.run_id)
    after = reloaded.census()
    # The census MAPS byte-equal (the manifest's value fields ride the universe's pair keys and the tally below).
    assert after.per_pair_counts == before.per_pair_counts
    assert after.per_item_counts == before.per_item_counts
    # The vote IDS re-mint exactly — every supersedes link and the tally's exclusion set survive the trip.
    assert [record.vote_id for record in after.vote_log] == [record.vote_id for record in before.vote_log]
    # The seven cast fields per record, clock-free by construction.
    for pre, post in zip(before.vote_log, after.vote_log, strict=True):
        assert _clock_free(post) == _clock_free(pre)
        # THE HONESTY PIN — recorded_at is the named divergence (re-minted at each re-cast): a string
        # on both sides, never asserted equal; registered_at likewise carried, never compared.
        assert isinstance(pre.recorded_at, str)
        assert isinstance(post.recorded_at, str)
    # The TallyResult WHOLE — ranked_groups and every clock-free field (tally_votes consumes no stamp).
    assert reloaded.rank() == before_rank
    # The external id — the file's stem, unchanged by construction.
    assert reloaded.run_id == store.run_id

def _corrupt_entries(entries: list[dict[str, Any]], case: str) -> None:
    """Mutate the parsed entries per the corruption case — the record-level triggers."""
    if case == "missing_field":
        del entries[1]["comparator_id"]
    elif case == "quorum_string":
        entries[0]["quorum"] = "1"
    elif case == "winner_outside":
        entries[1]["winner"] = "abstain"
    elif case == "class_outside":
        entries[1]["comparator_class"] = "robot"
    elif case == "pair_outside":
        entries[1]["pair"] = ["a", "zz"]
    elif case == "orphan_supersedes":
        entries[1]["supersedes"] = "VOTE-0009"
    elif case == "id_sequence":
        entries[2]["vote_id"] = "VOTE-0003"
    elif case == "duplicate_manifest":
        entries.append(dict(entries[0]))



def _corrupt_run_file(run_file: Path, raw: str, case: str) -> None:
    """Mutate the run file per the corruption case — the §4 trigger's bytes."""
    if case == "garbage_line":
        text_lines = raw.splitlines()
        text_lines[1] = "{ this is not json"
        run_file.write_text("\n".join(text_lines) + "\n")
    elif case == "truncated_tail":
        run_file.write_text(raw[:-1])
    else:
        entries: list[dict[str, Any]] = [json.loads(line) for line in raw.splitlines()]
        _corrupt_entries(entries, case)
        run_file.write_text("".join(json.dumps(entry, sort_keys=True) + "\n" for entry in entries))



@pytest.mark.parametrize(
    "case",
    [
        "garbage_line",
        "truncated_tail",
        "missing_field",
        "quorum_string",
        "winner_outside",
        "class_outside",
        "pair_outside",
        "orphan_supersedes",
        "id_sequence",
        "duplicate_manifest",
        "missing_file",
    ],
)
def test_corrupt_file_refused_whole(tmp_path: Path, case: str) -> None:
    """Each §4 trigger refuses at load — three fields rendered, the container never constructed."""
    store_home = tmp_path / "runs"
    store = _register(store_home)
    store.cast(("a", "b"), "prefer-a", comparator_id="x", comparator_class="human")
    store.cast(("a", "c"), "prefer-b", comparator_id="y", comparator_class="llm")
    if case == "missing_file":
        # The missing FILE — an unknown id: the home's live set rendered.
        with pytest.raises(StoreRefusedError) as info:
            Persist.load(store_home, "RUN-9999")
        message = str(info.value)
        assert "expected:" in message
        assert "found:" in message
        assert "next:" in message
        assert store.run_id in message
        return
    run_file = store_home / f"{store.run_id}.jsonl"
    raw = run_file.read_text()
    _corrupt_run_file(run_file, raw, case)
    # The refusal fires at load, before any re-cast — the partial load unrepresentable.
    with pytest.raises(StoreRefusedError) as info:
        Persist.load(store_home, store.run_id)
    message = str(info.value)
    assert "expected:" in message
    assert "found:" in message


def test_crash_tail_truncated_refused_clean_minus_tail_loads(tmp_path: Path) -> None:
    """The truncated tail refuses naming truncation; the clean file minus its tail loads whole and re-serves."""
    # The truncated last line — the crash mid-append, refused naming truncation.
    crashed_home = tmp_path / "runs"
    crashed = _register(crashed_home)
    crashed.cast(("a", "b"), "prefer-a", comparator_id="x", comparator_class="human")
    crashed_file = crashed_home / f"{crashed.run_id}.jsonl"
    crashed_file.write_text(crashed_file.read_text()[:-1])
    with pytest.raises(StoreRefusedError) as info:
        Persist.load(crashed_home, crashed.run_id)
    assert "truncat" in str(info.value).lower()
    # The clean file minus its tail — the legit between-casts crash: the complete lines kept, the last
    # complete line REMOVED (the cast that never appended).
    clean_home = tmp_path / "runs-again"
    clean = _register(clean_home)
    clean.cast(("a", "b"), "prefer-a", comparator_id="x", comparator_class="human")
    clean.cast(("a", "c"), "prefer-b", comparator_id="y", comparator_class="llm")
    clean.cast(("b", "c"), "tie", comparator_id="z", comparator_class="human")
    clean_file = clean_home / f"{clean.run_id}.jsonl"
    clean_file.write_text("".join(clean_file.read_text().splitlines(keepends=True)[:-1]))
    reloaded = Persist.load(clean_home, clean.run_id)
    census = reloaded.census()
    assert len(census.vote_log) == 2  # the census reflects the FILE — the loss invisible, bounded at one cast
    assert reloaded.serve() == ("b", "c", 0)  # .serve re-serves the same pair as before the removal


def test_supersede_replay_correction_rides_the_trip(tmp_path: Path) -> None:
    """The correction rides the round-trip — re-minted target live, exclusion set matching, ranking equal."""
    store_home = tmp_path / "runs"
    store = _register(store_home)
    store.cast(("a", "b"), "prefer-a", comparator_id="x", comparator_class="human")
    store.cast(("a", "b"), "prefer-b", comparator_id="x", comparator_class="human", supersedes="VOTE-0001")
    store.cast(("a", "c"), "prefer-b", comparator_id="y", comparator_class="llm")
    store.cast(("b", "c"), "prefer-a", comparator_id="z", comparator_class="human")
    before_rank = store.rank()
    reloaded = Persist.load(store_home, store.run_id)
    log = reloaded.census().vote_log
    # The pre-pass validated the EARLIER-line reference; the re-minted target live at the replayed re-cast.
    assert log[1].vote_id == "VOTE-0002"
    assert log[1].supersedes == "VOTE-0001"
    assert log[1].supersedes == log[0].vote_id
    # The tally's exclusion set matching — the original excluded, the correction counted — the ranking
    # byte-identical pre/post round-trip.
    assert reloaded.rank() == before_rank


def test_empty_run_load_is_a_value_never_a_refusal(tmp_path: Path) -> None:
    """A manifest-only file (register then exit) loads to the all-zero maps + the empty log; serve serves."""
    store_home = tmp_path / "runs"
    store = _register(store_home)
    reloaded = Persist.load(store_home, store.run_id)
    census = reloaded.census()
    assert census.vote_log == ()
    assert set(census.per_pair_counts.values()) == {0}
    assert set(census.per_item_counts.values()) == {0}
    assert reloaded.serve() == ("a", "b", 0)  # the first scheduled pair, count 0


def test_double_cast_absorbed_count_unchanged(tmp_path: Path) -> None:
    """A byte-identical re-cast (the crash-retry form) acks loudly and appends NOTHING — never double-counted."""
    store_home = tmp_path / "runs"
    store = _register(store_home)
    first_id, first_record, first_count, first_ack = store.cast(
        ("a", "b"), "prefer-a", comparator_id="x", comparator_class="human",
    )
    second_id, second_record, second_count, second_ack = store.cast(
        ("a", "b"), "prefer-a", comparator_id="x", comparator_class="human",
    )
    # The door's loud ack — the dedup IS the idempotence; the store appends NOTHING on the ack (R9 at
    # the file tier; the crash-retry re-casts THROUGH the store, never hand-writes the file — a
    # hand-written double line is the id-sequence corruption, refused at the pre-pass per §4 trigger 6).
    assert first_ack is False
    assert second_ack is True
    assert second_id == first_id
    assert second_record.vote_id == first_record.vote_id
    assert second_count == first_count
    run_file = store_home / f"{store.run_id}.jsonl"
    # ONE vote line in the file — the cleaner file wins.
    assert len(run_file.read_text().splitlines()) == 2
    reloaded = Persist.load(store_home, store.run_id)
    census = reloaded.census()
    assert len(census.vote_log) == 1
    assert census.per_pair_counts == store.census().per_pair_counts
    assert census.per_item_counts == store.census().per_item_counts
