# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The votes unit's edge tests — the twelve named edges (votes-brief §5)."""

import dataclasses
from typing import cast

import pytest

import prioritree.votes as votes_module
from prioritree.registry import OperatorDeclaration, Registry
from prioritree.scheduler import Pair
from prioritree.votes import (
    COMPARATOR_CLASSES,
    VOTE_PREFIX,
    VoteCensus,
    VoteLedger,
    VoteRecord,
    VotesRefusedError,
)

_AB_PAIR = Pair(item_a="a", item_b="b")
_AC_PAIR = Pair(item_a="a", item_b="c")
_BC_PAIR = Pair(item_a="b", item_b="c")
_FULL_UNIVERSE = frozenset({_AB_PAIR, _AC_PAIR, _BC_PAIR})


def _declaration() -> OperatorDeclaration:
    """Build a well-formed operator declaration (the registry tests' own form)."""
    return OperatorDeclaration(id="op-1", question="Which matters more?")


def _registered_run(registry: Registry) -> str:
    """Mint a 3-item run (a, b, c) and return its handle."""
    run_id, _manifest, _count = registry.register_run(
        [("a", "one"), ("b", "two"), ("c", "three")],
        operator=_declaration(),
    )
    return run_id


def _ledger() -> tuple[Registry, VoteLedger, str]:
    """Build a registry + ledger holding one registered 3-item run."""
    registry = Registry()
    run_id = _registered_run(registry)
    return registry, VoteLedger(registry), run_id


def test_first_vote_mints_vote_0001() -> None:
    """The empty ledger's first cast mints VOTE-0001 with stamps and a counting census."""
    _registry, ledger, run_id = _ledger()
    handle, record, count, acknowledged = ledger.cast_vote(
        run_id,
        _AB_PAIR,
        "prefer-a",
        comparator_id="x",
        comparator_class="human",
    )
    assert handle == "VOTE-0001"
    assert count == 1
    assert acknowledged is False
    assert record.vote_id == "VOTE-0001"
    assert record.run_id == run_id
    assert record.pair == _AB_PAIR
    assert record.winner == "prefer-a"
    assert record.comparator_id == "x"
    assert record.comparator_class == "human"
    assert record.recorded_at.endswith("+00:00")
    assert record.notes is None
    assert record.supersedes is None
    census = ledger.read_vote_state(run_id)
    assert len(census.vote_log) == 1
    assert census.per_pair_counts == {_AB_PAIR: 1, _AC_PAIR: 0, _BC_PAIR: 0}
    assert sum(census.per_item_counts.values()) == 2
    assert census.per_item_counts == {"a": 1, "b": 1, "c": 0}


def test_changed_verdict_revote_is_a_new_record() -> None:
    """A changed verdict from the same comparator on the same pair is a new record — both count."""
    _registry, ledger, run_id = _ledger()
    ledger.cast_vote(run_id, _AB_PAIR, "prefer-a", comparator_id="x", comparator_class="human")
    handle, _record, count, acknowledged = ledger.cast_vote(
        run_id,
        _AB_PAIR,
        "prefer-b",
        comparator_id="x",
        comparator_class="human",
    )
    assert handle == "VOTE-0002"
    assert count == 2
    assert acknowledged is False
    census = ledger.read_vote_state(run_id)
    assert [record.vote_id for record in census.vote_log] == ["VOTE-0001", "VOTE-0002"]
    assert [record.winner for record in census.vote_log] == ["prefer-a", "prefer-b"]
    assert census.per_pair_counts[_AB_PAIR] == 2


def test_identical_resend_acks_the_original_handle() -> None:
    """A byte-identical re-send is the loud ack — the original handle, count, and log."""
    _registry, ledger, run_id = _ledger()
    _handle, original, count, _acknowledged = ledger.cast_vote(
        run_id,
        _AB_PAIR,
        "prefer-a",
        comparator_id="x",
        comparator_class="human",
    )
    handle, record, resent_count, acknowledged = ledger.cast_vote(
        run_id,
        _AB_PAIR,
        "prefer-a",
        comparator_id="x",
        comparator_class="human",
    )
    assert handle == "VOTE-0001"
    assert record == original
    assert resent_count == count
    assert acknowledged is True
    census = ledger.read_vote_state(run_id)
    assert len(census.vote_log) == 1
    assert census.per_pair_counts[_AB_PAIR] == 1


def test_supersede_chain() -> None:
    """A correction rides supersedes; chains linearly; invalid targets refuse — nothing lands."""
    _registry, ledger, run_id = _ledger()
    original, _orig_record, _orig_count, _orig_ack = ledger.cast_vote(
        run_id,
        _AB_PAIR,
        "prefer-a",
        comparator_id="x",
        comparator_class="human",
    )
    correction, corr_record, corr_count, _corr_ack = ledger.cast_vote(
        run_id,
        _AB_PAIR,
        "prefer-b",
        comparator_id="x",
        comparator_class="human",
        notes="clerical fix",
        supersedes=original,
    )
    assert correction == "VOTE-0002"
    assert corr_record.supersedes == original
    assert corr_count == 2
    chained, _chain_record, _chain_count, _chain_ack = ledger.cast_vote(
        run_id,
        _AB_PAIR,
        "tie",
        comparator_id="x",
        comparator_class="human",
        notes="fixing the fix",
        supersedes=correction,
    )
    assert chained == "VOTE-0003"
    census = ledger.read_vote_state(run_id)
    assert [record.supersedes for record in census.vote_log] == [None, original, correction]
    with pytest.raises(VotesRefusedError) as exc_info:
        ledger.cast_vote(
            run_id,
            _AB_PAIR,
            "tie",
            comparator_id="x",
            comparator_class="human",
            supersedes="VOTE-9999",
        )
    assert exc_info.value.expected == (
        "a live VOTE-{####} handle in the same run, on the same pair (a correction corrects the same judgment)"
    )
    assert exc_info.value.found == "'VOTE-9999'"
    second_run, _second_manifest, _second_count = _registry.register_run(
        [("a", "one-2"), ("b", "two-2"), ("c", "three-2")],
        operator=_declaration(),
    )
    with pytest.raises(VotesRefusedError) as exc_info:
        ledger.cast_vote(
            second_run,
            _AB_PAIR,
            "tie",
            comparator_id="y",
            comparator_class="llm",
            supersedes=original,
        )
    assert "same run" in exc_info.value.expected
    with pytest.raises(VotesRefusedError) as exc_info:
        ledger.cast_vote(
            run_id,
            _BC_PAIR,
            "tie",
            comparator_id="z",
            comparator_class="human",
            supersedes=correction,
        )
    assert "same pair" in exc_info.value.expected
    final_census = ledger.read_vote_state(run_id)
    assert len(final_census.vote_log) == 3


def test_two_comparators_on_one_pair() -> None:
    """A human and an llm both land on the same pair — both classes through the one interface."""
    _registry, ledger, run_id = _ledger()
    _h_handle, h_record, _h_count, _h_ack = ledger.cast_vote(
        run_id,
        _AB_PAIR,
        "prefer-a",
        comparator_id="x",
        comparator_class="human",
    )
    _l_handle, l_record, _l_count, _l_ack = ledger.cast_vote(
        run_id,
        _AB_PAIR,
        "prefer-a",
        comparator_id="y",
        comparator_class="llm",
    )
    assert h_record.comparator_class == "human"
    assert l_record.comparator_class == "llm"
    assert h_record != l_record
    census = ledger.read_vote_state(run_id)
    assert len(census.vote_log) == 2
    assert census.per_pair_counts[_AB_PAIR] == 2


def test_unknown_pair_refused_including_swapped_citation() -> None:
    """An id outside the manifest and a swapped citation each refuse before any byte lands."""
    _registry, ledger, run_id = _ledger()
    with pytest.raises(VotesRefusedError) as exc_info:
        ledger.cast_vote(run_id, Pair(item_a="a", item_b="zz"), "prefer-a", comparator_id="x", comparator_class="human")
    assert exc_info.value.expected == (
        "a canonical pair from schedule_pairs over the run's 3 manifest ids (the legal set's source)"
    )
    assert exc_info.value.found == repr(Pair(item_a="a", item_b="zz"))
    with pytest.raises(VotesRefusedError) as exc_info:
        ledger.cast_vote(run_id, Pair(item_a="b", item_b="a"), "prefer-a", comparator_id="x", comparator_class="human")
    assert exc_info.value.expected == (
        f"a canonical pair (item_a < item_b) — the canonical form of these ids is {_AB_PAIR!r}"
    )
    assert "never silently re-ordered" in exc_info.value.next_action
    census = ledger.read_vote_state(run_id)
    assert census.vote_log == ()
    assert sum(census.per_pair_counts.values()) == 0


def test_wrong_verdict_refused() -> None:
    """A winner outside the run's declared set refuses naming the declared set; nothing lands."""
    _registry, ledger, run_id = _ledger()
    with pytest.raises(VotesRefusedError) as exc_info:
        ledger.cast_vote(run_id, _AB_PAIR, "abstain", comparator_id="x", comparator_class="human")
    assert exc_info.value.expected == ("a verdict from the run's declared set ['prefer-a', 'prefer-b', 'tie']")
    assert exc_info.value.found == "'abstain'"
    assert exc_info.value.next_action == "cast a verdict from the declared set"
    assert ledger.read_vote_state(run_id).vote_log == ()


def test_census_on_empty_ledger_never_refuses() -> None:
    """A zero-vote run reads back all-zero maps and the empty log; the unknown run wraps."""
    _registry, ledger, run_id = _ledger()
    census = ledger.read_vote_state(run_id)
    assert isinstance(census, VoteCensus)
    assert census.run_id == run_id
    assert set(census.per_pair_counts) == _FULL_UNIVERSE
    assert set(census.per_pair_counts.values()) == {0}
    assert set(census.per_item_counts) == {"a", "b", "c"}
    assert set(census.per_item_counts.values()) == {0}
    assert census.vote_log == ()
    with pytest.raises(VotesRefusedError) as exc_info:
        ledger.read_vote_state("RUN-9999")
    assert exc_info.value.expected == f"a live RUN-{{####}} handle ({run_id})"
    assert exc_info.value.found == "'RUN-9999'"


def test_idempotency_key_stable_across_intervening_votes() -> None:
    """A's re-send still acks VOTE-0001 after B's intervening vote — the key is content, not position."""
    _registry, ledger, run_id = _ledger()
    first, _record, _count, _ack = ledger.cast_vote(
        run_id,
        _AB_PAIR,
        "prefer-a",
        comparator_id="x",
        comparator_class="human",
    )
    assert first == "VOTE-0001"
    intervening, _int_record, _int_count, _int_ack = ledger.cast_vote(
        run_id,
        _AB_PAIR,
        "prefer-b",
        comparator_id="y",
        comparator_class="llm",
    )
    assert intervening == "VOTE-0002"
    handle, _record, count, acknowledged = ledger.cast_vote(
        run_id,
        _AB_PAIR,
        "prefer-a",
        comparator_id="x",
        comparator_class="human",
    )
    assert handle == "VOTE-0001"
    assert acknowledged is True
    assert count == 2
    census = ledger.read_vote_state(run_id)
    assert len(census.vote_log) == 2
    assert [entry.comparator_id for entry in census.vote_log] == ["x", "y"]


def test_malformed_payload_refusals() -> None:
    """Every malformed payload refuses naming the schema's public types; nothing lands."""
    _registry, ledger, run_id = _ledger()
    bad_batches: list[tuple[object, ...]] = [
        ("", _AB_PAIR, "prefer-a", "", "human", None, None),
        (run_id, _AB_PAIR, "prefer-a", "x", "robot", None, None),
        (run_id, ["a", "b", "c"], "prefer-a", "x", "human", None, None),
        (run_id, ["a", 2], "prefer-a", "x", "human", None, None),
        (run_id, "ab", "prefer-a", "x", "human", None, None),
        (run_id, _AB_PAIR, 1, "x", "human", None, None),
        ("", _AB_PAIR, "prefer-a", "x", "human", None, None),
        (run_id, _AB_PAIR, "prefer-a", "x", "human", 123, None),
        (run_id, _AB_PAIR, "prefer-a", "x", "human", None, 456),
    ]
    for batch in bad_batches:
        run_arg, pair_arg, winner_arg, comp_id, comp_class, notes_arg, supersede_arg = batch
        with pytest.raises(VotesRefusedError) as exc_info:
            ledger.cast_vote(
                cast("str", run_arg),
                cast("Pair", pair_arg),
                cast("str", winner_arg),
                comparator_id=cast("str", comp_id),
                comparator_class=cast("str", comp_class),
                notes=cast("str | None", notes_arg),
                supersedes=cast("str | None", supersede_arg),
            )
        assert exc_info.value.expected.startswith("the schema's public types (")
        assert " got " in exc_info.value.found
        assert exc_info.value.next_action == (
            "re-send per the schema — the module's public types (VoteRecord's fields)"
        )
    assert ledger.read_vote_state(run_id).vote_log == ()


def test_append_only_invariant_at_module_surface() -> None:
    """The public method set is exactly the two ruled ops; no edit/delete word exists publicly."""
    public_methods = sorted(
        name for name in dir(VoteLedger) if not name.startswith("_") and callable(getattr(VoteLedger, name))
    )
    assert public_methods == ["cast_vote", "read_vote_state"]
    forbidden_words = ("edit", "delete", "remove", "update")
    forbidden = [name for name in dir(votes_module) if any(word in name.lower() for word in forbidden_words)]
    assert forbidden == []


def test_no_score_field() -> None:
    """No 'score' field exists on VoteRecord or VoteCensus — the Parnas fold, structurally."""
    record_fields = {field.name for field in dataclasses.fields(VoteRecord)}
    assert "score" not in record_fields
    census_fields = {field.name for field in dataclasses.fields(VoteCensus)}
    assert "score" not in census_fields
    assert VOTE_PREFIX == "VOTE-"
    assert frozenset({"human", "llm"}) == COMPARATOR_CLASSES
