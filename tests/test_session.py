# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The session unit's edge tests — the nine named edges (session-brief §5)."""

import contextlib

import pytest

from prioritree.registry import OperatorDeclaration, Registry
from prioritree.scheduler import Pair
from prioritree.session import ExhaustedQueue, Session
from prioritree.tally import TALLY_ALGORITHM, TallyRefusedError, TallyResult
from prioritree.votes import VotesRefusedError

_AB_PAIR = Pair(item_a="a", item_b="b")
_AC_PAIR = Pair(item_a="a", item_b="c")
_BC_PAIR = Pair(item_a="b", item_b="c")
_SCRIPT: tuple[tuple[tuple[str, str], str], ...] = (
    (("a", "b"), "prefer-a"),
    (("a", "c"), "prefer-a"),
    (("b", "c"), "tie"),
)


def _declaration() -> OperatorDeclaration:
    """Build a well-formed operator declaration (the landed suites' own form)."""
    return OperatorDeclaration(id="op-1", question="Which matters more?")


def _session() -> Session:
    """Build a fresh session over a fresh registry — the one container, the stores private."""
    return Session(Registry())


def _registered(
    session: Session,
    items: list[tuple[str, str]],
    quorum: int = 1,
) -> str:
    """Register the payload through op 1 and return the run's handle."""
    run_id, _manifest, _count = session.register_run(items, operator=_declaration(), quorum=quorum)
    return run_id


def test_end_to_end_fixture_register_vote_done_tally() -> None:
    """The gate's fixture: register, schedule, cast three, DONE, and the exact hand-computed emission."""
    session = _session()
    run_id, manifest, count = session.register_run(
        [("a", "one"), ("b", "two"), ("c", "three")], operator=_declaration(), quorum=1,
    )
    assert count == 1
    assert [row.id for row in manifest.items] == ["a", "b", "c"]
    assert session.next_pair(run_id) == ("a", "b", 0)
    session.cast_vote(run_id, ("a", "b"), "prefer-a", comparator_id="x", comparator_class="human")
    session.cast_vote(run_id, ("a", "b"), "prefer-a", comparator_id="x", comparator_class="llm")
    assert session.next_pair(run_id) == ("a", "c", 0)
    session.cast_vote(run_id, ("a", "c"), "prefer-a", comparator_id="x", comparator_class="human")
    session.cast_vote(run_id, ("a", "c"), "prefer-a", comparator_id="x", comparator_class="llm")
    assert session.next_pair(run_id) == ("b", "c", 0)
    session.cast_vote(run_id, ("b", "c"), "tie", comparator_id="x", comparator_class="human")
    session.cast_vote(run_id, ("b", "c"), "tie", comparator_id="x", comparator_class="llm")
    with pytest.raises(ExhaustedQueue):
        session.next_pair(run_id)
    result = session.tally_rank(run_id)
    assert result.ranked_groups == (("a",), ("b", "c"))
    assert result.per_item_wins == {"a": 4, "b": 0, "c": 0}
    assert result.per_item_losses == {"a": 0, "b": 2, "c": 2}
    assert result.per_item_ties == {"a": 0, "b": 2, "c": 2}
    assert result.coverage.done is True
    assert result.coverage.components == (("a", "b", "c"),)
    assert result.coverage.cycle == ()
    assert result.coverage.pair_counts == {_AB_PAIR: 2, _AC_PAIR: 2, _BC_PAIR: 2}
    assert result.algorithm_version == TALLY_ALGORITHM
    assert result.algorithm_version == "win-rate-v1"


def test_done_signal_caught_by_type_three_fields() -> None:
    """The DONE signal is caught BY TYPE and carries the brief §2 field bytes verbatim."""
    session = _session()
    run_id = _registered(session, [("a", "one"), ("b", "two"), ("c", "three")])
    _cast_all(session, run_id)
    with pytest.raises(ExhaustedQueue) as exc_info:
        session.next_pair(run_id)
    assert exc_info.value.expected == "all 3 scheduled pairs at quorum k=1"
    assert exc_info.value.found.startswith("the queue is exhausted")
    assert exc_info.value.next_action.startswith("call tally_rank")
    assert not issubclass(ExhaustedQueue, VotesRefusedError)
    assert not issubclass(ExhaustedQueue, TallyRefusedError)


def test_seam_divergence_next_pair_done_tally_safe_halt() -> None:
    """A standing correction at k=2 exhausts the census-keyed queue yet SAFE HALTs the weighted gate."""
    session = _session()
    run_id = _registered(session, [("a", "one"), ("b", "two")], quorum=2)
    session.cast_vote(run_id, ("a", "b"), "prefer-a", comparator_id="x", comparator_class="human")
    session.cast_vote(
        run_id, ("a", "b"), "prefer-b", comparator_id="x", comparator_class="human", supersedes="VOTE-0001",
    )
    with pytest.raises(ExhaustedQueue):
        session.next_pair(run_id)
    with pytest.raises(TallyRefusedError) as exc_info:
        session.tally_rank(run_id)
    assert "(a, b) 1 of 2" in exc_info.value.found


def test_prefix_tally_well_defined_every_coverage_point() -> None:
    """tally_rank at every coverage prefix is a defined outcome — a TallyResult or a TallyRefusedError, never else."""
    session = _session()
    run_id = _registered(session, [("a", "one"), ("b", "two"), ("c", "three")])
    with contextlib.suppress(TallyRefusedError):
        session.tally_rank(run_id)
    for pair, winner in _SCRIPT:
        session.cast_vote(run_id, pair, winner, comparator_id="x", comparator_class="human")
        session.cast_vote(run_id, pair, winner, comparator_id="x", comparator_class="llm")
        with contextlib.suppress(TallyRefusedError):
            session.tally_rank(run_id)
    assert session.tally_rank(run_id).ranked_groups == (("a",), ("b", "c"))


def test_five_ops_present_and_wired() -> None:
    """The five ruled ops exist on Session and the flow proves each wiring end to end."""
    session = _session()
    for op_name in ("register_run", "next_pair", "cast_vote", "read_vote_state", "tally_rank"):
        assert callable(getattr(session, op_name))
    run_id, _manifest, _count = session.register_run([("a", "one"), ("b", "two")], operator=_declaration())
    census = session.read_vote_state(run_id)
    assert census.run_id == run_id
    assert census.vote_log == ()
    assert session.next_pair(run_id) == ("a", "b", 0)
    session.cast_vote(run_id, ("a", "b"), "prefer-a", comparator_id="x", comparator_class="human")
    landed = session.read_vote_state(run_id)
    assert len(landed.vote_log) == 1
    assert landed.per_pair_counts[_AB_PAIR] == 1
    session.cast_vote(run_id, ("a", "b"), "prefer-a", comparator_id="x", comparator_class="llm")
    result = session.tally_rank(run_id)
    assert isinstance(result, TallyResult)
    assert result.ranked_groups == (("a",), ("b",))


def test_register_refusals_wrapped_one_grammar() -> None:
    """Duplicate ids and the single item land as VotesRefusedError carrying the registry's fields."""
    # The store unchanged: the miss never lands.
    session = _session()
    run_id = _registered(session, [("a", "one"), ("b", "two")])
    with pytest.raises(VotesRefusedError) as duplicate:
        session.register_run([("a", "one"), ("a", "again")], operator=_declaration())
    assert duplicate.value.expected == "all item ids unique within the payload"
    assert duplicate.value.found == "duplicate id 'a' at positions 0, 1"
    assert duplicate.value.next_action == (
        "disambiguate — one id per row; even trusted-source payloads are untrusted bytes"
    )
    with pytest.raises(VotesRefusedError) as single:
        session.register_run([("a", "one")], operator=_declaration())
    assert single.value.expected == "at least 2 item rows (a comparison needs a pair)"
    assert single.value.found == "1 item row"
    assert single.value.next_action.startswith("register at least two rows")
    assert session.read_vote_state(run_id).vote_log == ()


def test_unknown_run_miss_one_refusal_type() -> None:
    """Every op on the unknown run speaks VotesRefusedError — one refusal type at the public face."""
    session = _session()
    with pytest.raises(VotesRefusedError) as scheduled:
        session.next_pair("RUN-9999")
    assert scheduled.value.found == "'RUN-9999'"
    with pytest.raises(VotesRefusedError):
        session.tally_rank("RUN-9999")
    with pytest.raises(VotesRefusedError):
        session.cast_vote("RUN-9999", ("a", "b"), "tie", comparator_id="x", comparator_class="human")
    with pytest.raises(VotesRefusedError):
        session.read_vote_state("RUN-9999")


def test_zero_vote_run_first_pair_count_zero() -> None:
    """The fresh run's next_pair returns the first scheduled pair with count 0 — a value, pure across re-calls."""
    session = _session()
    run_id = _registered(session, [("a", "one"), ("b", "two"), ("c", "three")])
    assert session.next_pair(run_id) == ("a", "b", 0)
    session.cast_vote(run_id, ("b", "c"), "tie", comparator_id="x", comparator_class="human")
    assert session.next_pair(run_id) == ("a", "b", 0)


def test_quorum_two_partial_returns_count_one() -> None:
    """At k=2 one vote keeps the pair first — next_pair returns it with its census count 1."""
    session = _session()
    run_id = _registered(session, [("a", "one"), ("b", "two")], quorum=2)
    session.cast_vote(run_id, ("a", "b"), "prefer-a", comparator_id="x", comparator_class="human")
    assert session.next_pair(run_id) == ("a", "b", 1)


def _cast_all(session: Session, run_id: str) -> None:
    """Cast the three-pair script through op 3 (one tie among the verdicts)."""
    for pair, winner in _SCRIPT:
        session.cast_vote(run_id, pair, winner, comparator_id="x", comparator_class="human")
