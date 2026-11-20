# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The tally unit's edge tests — the twelve named edges (tally-brief §5).

The fixtures-alone bar (edge 10, the suite-wide discipline): every fixture is a
frozen RunManifest plus a tuple of frozen VoteRecords built directly — ZERO
store imports (no Registry, no VoteLedger, no VoteCensus anywhere); this file's
own import list is the evidence, verified at the read-back.
"""

import dataclasses
from collections.abc import Sequence

import pytest

from prioritree.registry import ItemRow, OperatorDeclaration, RunManifest
from prioritree.scheduler import Pair
from prioritree.tally import PREFER_A, PREFER_B, TALLY_ALGORITHM, TIE, TallyRefusedError, tally_votes
from prioritree.votes import VoteRecord

_RUN_ID = "RUN-0001"
_STAMP = "2026-11-20T00:00:00+00:00"
_AB_PAIR = Pair(item_a="a", item_b="b")
_AC_PAIR = Pair(item_a="a", item_b="c")
_AD_PAIR = Pair(item_a="a", item_b="d")
_BC_PAIR = Pair(item_a="b", item_b="c")
_BD_PAIR = Pair(item_a="b", item_b="d")
_CD_PAIR = Pair(item_a="c", item_b="d")


def _manifest(item_ids: Sequence[str], quorum: int = 1) -> RunManifest:
    """Build a frozen manifest over the ids — fixtures only, no store anywhere."""
    rows = tuple(ItemRow(id=item_id, label=f"label-{item_id}") for item_id in item_ids)
    return RunManifest(
        run_id=_RUN_ID,
        items=rows,
        operator=OperatorDeclaration(id="op-1", question="Which matters more?"),
        quorum=quorum,
        registered_at=_STAMP,
    )


def _vote(
    vote_id: str,
    pair: Pair,
    winner: str,
    *,
    notes: str | None = None,
    supersedes: str | None = None,
) -> VoteRecord:
    """Build one frozen vote record — fixtures only, no store anywhere."""
    return VoteRecord(
        vote_id=vote_id,
        run_id=_RUN_ID,
        pair=pair,
        winner=winner,
        comparator_id="x",
        comparator_class="human",
        recorded_at=_STAMP,
        notes=notes,
        supersedes=supersedes,
    )


def _perfect_order_votes() -> tuple[VoteRecord, ...]:
    """Build the hand-computed n=4 perfect order — a>b, a>c, a>d, b>c, b>d, c>d."""
    return (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _AC_PAIR, PREFER_A),
        _vote("VOTE-0003", _AD_PAIR, PREFER_A),
        _vote("VOTE-0004", _BC_PAIR, PREFER_A),
        _vote("VOTE-0005", _BD_PAIR, PREFER_A),
        _vote("VOTE-0006", _CD_PAIR, PREFER_A),
    )


def test_purity_permuted_multiset_byte_identical() -> None:
    """The same vote multiset in two cast orders tallies to equal TallyResult values."""
    manifest = _manifest(["a", "b", "c", "d"])
    forward = _perfect_order_votes()
    backward = tuple(reversed(forward))
    assert tally_votes(manifest, backward) == tally_votes(manifest, forward)


def test_hand_computed_known_answer_full_emission() -> None:
    """The n=4 perfect order emits the hand-computed whole — every field asserted."""
    result = tally_votes(_manifest(["a", "b", "c", "d"]), _perfect_order_votes())
    assert result.ranked_groups == (("a",), ("b",), ("c",), ("d",))
    assert result.per_item_wins == {"a": 3, "b": 2, "c": 1, "d": 0}
    assert result.per_item_losses == {"a": 0, "b": 1, "c": 2, "d": 3}
    assert result.per_item_ties == {"a": 0, "b": 0, "c": 0, "d": 0}
    assert result.coverage.done is True
    assert result.coverage.components == (("a", "b", "c", "d"),)
    assert result.coverage.cycle == ()
    assert result.coverage.pair_counts == {
        _AB_PAIR: 1,
        _AC_PAIR: 1,
        _AD_PAIR: 1,
        _BC_PAIR: 1,
        _BD_PAIR: 1,
        _CD_PAIR: 1,
    }
    assert result.algorithm_version == TALLY_ALGORITHM


def test_every_coverage_prefix_defined() -> None:
    """Every coverage prefix of the n=3 sequence is a defined outcome — never partial, never silent."""
    manifest = _manifest(["a", "b", "c"])
    script = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _AC_PAIR, PREFER_B),
        _vote("VOTE-0003", _BC_PAIR, PREFER_A),
    )
    with pytest.raises(TallyRefusedError) as prefix_0:
        tally_votes(manifest, script[:0])
    assert prefix_0.value.found == (
        "zero-coverage items: a, b, c; components: (a), (b), (c); "
        "under-quorum pairs: (a, b) 0 of 1, (a, c) 0 of 1, (b, c) 0 of 1"
    )
    with pytest.raises(TallyRefusedError) as prefix_1:
        tally_votes(manifest, script[:1])
    assert prefix_1.value.found == (
        "zero-coverage items: c; components: (a, b), (c); under-quorum pairs: (a, c) 0 of 1, (b, c) 0 of 1"
    )
    with pytest.raises(TallyRefusedError) as prefix_2:
        tally_votes(manifest, script[:2])
    assert prefix_2.value.found == "under-quorum pairs: (b, c) 0 of 1"
    assert isinstance(tally_votes(manifest, script[:3]).ranked_groups, tuple)


def test_cycle_structural_named_done() -> None:
    """The Condorcet triple is DONE — one shared group, the cycle named, never an error."""
    manifest = _manifest(["a", "b", "c"])
    votes = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_B),
        _vote("VOTE-0002", _BC_PAIR, PREFER_B),
        _vote("VOTE-0003", _AC_PAIR, PREFER_A),
    )
    result = tally_votes(manifest, votes)
    assert result.ranked_groups == (("a", "b", "c"),)
    assert result.per_item_wins == {"a": 1, "b": 1, "c": 1}
    assert result.per_item_losses == {"a": 1, "b": 1, "c": 1}
    assert result.per_item_ties == {"a": 0, "b": 0, "c": 0}
    assert result.coverage.done is True
    assert result.coverage.components == (("a", "b", "c"),)
    assert set(result.coverage.cycle) == {("a", "c"), ("b", "a"), ("c", "b")}
    assert result.coverage.pair_counts == {_AB_PAIR: 1, _AC_PAIR: 1, _BC_PAIR: 1}


def test_tie_break_exact_integer_grouping() -> None:
    """Equal exact scores share ONE group; distinct rationals stay separated — floats can collapse them."""
    manifest = _manifest(["a", "b", "c", "d"])
    tied_votes = (
        _vote("VOTE-0001", _AC_PAIR, PREFER_A),
        _vote("VOTE-0002", _AD_PAIR, PREFER_A),
        _vote("VOTE-0003", _BC_PAIR, PREFER_A),
        _vote("VOTE-0004", _BD_PAIR, PREFER_A),
        _vote("VOTE-0005", _AB_PAIR, TIE),
        _vote("VOTE-0006", _CD_PAIR, TIE),
    )
    result = tally_votes(manifest, tied_votes)
    assert result.ranked_groups == (("a", "b"), ("c", "d"))
    assert tally_votes(manifest, tied_votes) == result
    distinct_votes = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _AC_PAIR, PREFER_A),
        _vote("VOTE-0003", _BC_PAIR, PREFER_A),
        _vote("VOTE-0004", _BD_PAIR, PREFER_A),
        _vote("VOTE-0005", _CD_PAIR, PREFER_A),
        _vote("VOTE-0006", _AD_PAIR, PREFER_A),
    )
    distinct_result = tally_votes(manifest, distinct_votes)
    assert distinct_result.ranked_groups == (("a",), ("b",), ("c",), ("d",))


def test_quorum_leg_safe_halt_names_shortfall() -> None:
    """The k=2 shortfall is a SAFE HALT — found names the pair 1 of 2; next_action the missing vote."""
    manifest = _manifest(["a", "b", "c"], quorum=2)
    votes = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _AB_PAIR, PREFER_A),
        _vote("VOTE-0003", _AC_PAIR, PREFER_A),
        _vote("VOTE-0004", _BC_PAIR, PREFER_A),
    )
    with pytest.raises(TallyRefusedError) as exc_info:
        tally_votes(manifest, votes)
    assert "(b, c) 1 of 2" in exc_info.value.found
    assert "(b, c) needs 1 more" in exc_info.value.next_action
    assert "quorum needs MORE VOTES on existing pairs" in exc_info.value.next_action


def test_isolation_and_connectivity_legs_named() -> None:
    """Isolation names the isolated id, the components, and the bridging pair — every leg's finding."""
    single_manifest = _manifest(["a", "b", "c"])
    single_votes = (_vote("VOTE-0001", _AB_PAIR, PREFER_A),)
    with pytest.raises(TallyRefusedError) as single:
        tally_votes(single_manifest, single_votes)
    assert "zero-coverage items: c" in single.value.found
    assert "components: (a, b), (c)" in single.value.found
    assert "(a, c)" in single.value.next_action
    assert "connectivity needs NEW comparisons" in single.value.next_action
    two_manifest = _manifest(["a", "b", "c", "d"])
    two_votes = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _CD_PAIR, PREFER_A),
    )
    with pytest.raises(TallyRefusedError) as two:
        tally_votes(two_manifest, two_votes)
    assert "components: (a, b), (c, d)" in two.value.found
    assert "(a, c)" in two.value.next_action
    with pytest.raises(TallyRefusedError) as empty:
        tally_votes(_manifest(["a", "b", "c"]), ())
    assert empty.value.found == (
        "zero-coverage items: a, b, c; components: (a), (b), (c); "
        "under-quorum pairs: (a, b) 0 of 1, (a, c) 0 of 1, (b, c) 0 of 1"
    )


def test_supersession_weighting_chain_and_fork() -> None:
    """The exclusion set E counts the correction, excludes the cited — the chain's tip, the fork's both."""
    correction_manifest = _manifest(["a", "b"])
    correction_votes = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _AB_PAIR, PREFER_B, notes="clerical fix", supersedes="VOTE-0001"),
    )
    result = tally_votes(correction_manifest, correction_votes)
    assert result.per_item_wins == {"a": 0, "b": 1}
    assert result.per_item_losses == {"a": 1, "b": 0}
    assert result.coverage.pair_counts == {_AB_PAIR: 1}
    chain_manifest = _manifest(["a", "b"], quorum=1)
    chain_votes = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _AB_PAIR, PREFER_B, supersedes="VOTE-0001"),
        _vote("VOTE-0003", _AB_PAIR, TIE, supersedes="VOTE-0002"),
    )
    chain_result = tally_votes(chain_manifest, chain_votes)
    assert chain_result.per_item_ties == {"a": 1, "b": 1}
    assert chain_result.per_item_wins == {"a": 0, "b": 0}
    fork_manifest = _manifest(["a", "b"], quorum=2)
    fork_votes = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0004", _AB_PAIR, PREFER_A, supersedes="VOTE-0001"),
        _vote("VOTE-0005", _AB_PAIR, PREFER_B, supersedes="VOTE-0001"),
    )
    fork_result = tally_votes(fork_manifest, fork_votes)
    assert fork_result.per_item_wins == {"a": 1, "b": 1}
    assert fork_result.per_item_losses == {"a": 1, "b": 1}
    assert fork_result.coverage.pair_counts == {_AB_PAIR: 2}
    quorum_manifest = _manifest(["a", "b"], quorum=2)
    with pytest.raises(TallyRefusedError) as exc_info:
        tally_votes(quorum_manifest, correction_votes)
    assert "(a, b) 1 of 2" in exc_info.value.found


def test_no_score_field_consumption() -> None:
    """The consumed records are VoteRecords with NO score field — the Parnas fold, by construction."""
    record_fields = {field.name for field in dataclasses.fields(VoteRecord)}
    assert "score" not in record_fields
    manifest = _manifest(["a", "b"])
    votes = (_vote("VOTE-0001", _AB_PAIR, TIE),)
    result = tally_votes(manifest, votes)
    assert result.per_item_ties == {"a": 1, "b": 1}


def test_version_stamp_constant_and_byte_identical_rerun() -> None:
    """The emission's algorithm_version is exactly TALLY_ALGORITHM; re-runs byte-identical."""
    manifest = _manifest(["a", "b", "c", "d"])
    votes = _perfect_order_votes()
    first = tally_votes(manifest, votes)
    assert first.algorithm_version == "win-rate-v1"
    assert first.algorithm_version == TALLY_ALGORITHM
    assert tally_votes(manifest, votes) == first


def test_weighted_vs_census_seam() -> None:
    """The raw pair count is 2 but the weighted count is 1 — the gate rides the weighted, the seam pinned."""
    manifest = _manifest(["a", "b"], quorum=2)
    votes = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _AB_PAIR, PREFER_B, notes="clerical fix", supersedes="VOTE-0001"),
    )
    assert len(votes) == 2
    with pytest.raises(TallyRefusedError) as exc_info:
        tally_votes(manifest, votes)
    assert "(a, b) 1 of 2" in exc_info.value.found
    assert "(a, b) needs 1 more" in exc_info.value.next_action
    quorum_one_result = tally_votes(_manifest(["a", "b"]), votes)
    assert quorum_one_result.coverage.pair_counts == {_AB_PAIR: 1}
