# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The acceptance unit's edge tests — the five named edges + the matrix iteration (acceptance-brief §6)."""

from fractions import Fraction

from prioritree.acceptance import (
    ACCEPTANCE_FLOOR,
    ACCEPTANCE_ITEM_COUNTS,
    ACCEPTANCE_NOISE_RATES,
    ACCEPTANCE_SEEDS,
    DEGRADATION_RATE,
    accept_run,
    floor_holds,
)
from prioritree.session import ExhaustedQueue
from prioritree.tally import TallyRefusedError


def test_recovery_at_floor_per_cell() -> None:
    """Every (n, p, seed) in the matrix clears the ruled integer floor — the per-cell taus recorded as data."""
    for item_count in ACCEPTANCE_ITEM_COUNTS:
        for noise_rate in ACCEPTANCE_NOISE_RATES:
            for seed in ACCEPTANCE_SEEDS:
                record = accept_run(item_count, noise_rate, seed)
                assert floor_holds(record.concordant, record.discordant, record.tied, record.item_count), (
                    item_count,
                    noise_rate,
                    seed,
                    record.concordant,
                    record.discordant,
                    record.tied,
                )


def test_determinism_same_seed_identical_replay() -> None:
    """The same (n, p, seed) run twice replays identical on the clock-free surface — the stamps never asserted."""
    first = accept_run(10, 0.15, 1109)
    second = accept_run(10, 0.15, 1109)
    assert first.latent_order == second.latent_order
    assert first.verdicts == second.verdicts
    assert first.result == second.result
    assert (first.concordant, first.discordant, first.tied) == (
        second.concordant,
        second.discordant,
        second.tied,
    )


def test_perfect_case_tau_one_exactly() -> None:
    """p=0 yields tau=1 exactly — P=n0, Q=T=0, the emission IS the latent order."""
    record = accept_run(10, 0.0, ACCEPTANCE_SEEDS[0])
    assert record.concordant == 45
    assert record.discordant == 0
    assert record.tied == 0
    assert record.result.ranked_groups == tuple((item_id,) for item_id in record.latent_order)


def test_degradation_observation_recorded_below_band() -> None:
    """The p=0.35 runs at n=20 fail the floor — the recorded drop is real, deterministic at fixed seeds."""
    for seed in ACCEPTANCE_SEEDS:
        record = accept_run(20, DEGRADATION_RATE, seed)
        assert not floor_holds(record.concordant, record.discordant, record.tied, record.item_count), (
            seed,
            record.concordant,
            record.discordant,
            record.tied,
        )


def test_done_caught_by_type() -> None:
    """The run completes only because the loop caught ExhaustedQueue by type — every pair voted by all three judges."""
    record = accept_run(10, 0.15, ACCEPTANCE_SEEDS[0])
    assert len(record.verdicts) == 135
    assert not issubclass(ExhaustedQueue, TallyRefusedError)
    assert Fraction(4, 5) == ACCEPTANCE_FLOOR
