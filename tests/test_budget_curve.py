# Copyright (C) 2026 Mark Losey. All rights reserved.
"""test_budget_curve — the budget-curve unit's mechanical invariants, asserted.

The ~7 named edges per budget-curve-brief §6: the budget law exact, the
pairing law, the determinism, the model's mechanics, the measure invariants
(accept_measure REUSED, never re-implemented), the perfect case both arms,
and the record's completeness matrix. THE ASSERTION LAW (Q-curve-assertion):
NO ordering claim anywhere — the tests assert the MECHANICAL invariants
only; the per-cell taus are COLLECTED as data for the record, never judged
here. The amendment's re-verification (the acceptance suite green at the
default) rides the floor, not this suite.
"""

from fractions import Fraction

from prioritree.acceptance import (
    ACCEPTANCE_ID_TEMPLATE,
    ACCEPTANCE_ITEM_COUNTS,
    ACCEPTANCE_NOISE_RATES,
    ACCEPTANCE_SEEDS,
    accept_measure,
)
from prioritree.budget_curve import compare_run, size_run

FIXTURE_SEED = 1109


def _expected_ids(item_count: int) -> tuple[str, ...]:
    """Return the zero-padded id tuple for a run's item count.

    Purpose: the id set every record's groups must cover exactly — the ids
    derived from ACCEPTANCE_ID_TEMPLATE, never a hardcode per count.
    Refuses when: never — pure template formatting.
    Re-run: deterministic — the template is a constant.
    Touches: nothing — pure over its argument.
    Provenance: acceptance.py's ACCEPTANCE_ID_TEMPLATE (the shared id law).
    """
    return tuple(ACCEPTANCE_ID_TEMPLATE.format(index=index) for index in range(item_count))


def test_budget_law_exact() -> None:
    """Assert the equal-budget law at both quorum points — sums exact, split even.

    At (n=10, k=3): B = 45 * 3 = 135, q = 13, r = 5 — the first 5 ids in id
    order carry 14, the rest 13. At (n=20, k=1): B = 190, q = 9, r = 10.
    Both runs assert sum(budgets) == n0 * quorum and the even split
    (max - min <= 1); no ordering asserted anywhere.
    """
    ten = size_run(10, 0.15, FIXTURE_SEED, 3)
    assert ten.quorum == 3
    assert sum(ten.budgets) == 45 * 3
    assert max(ten.budgets) - min(ten.budgets) <= 1
    assert ten.budgets == (14, 14, 14, 14, 14, 13, 13, 13, 13, 13)
    twenty = size_run(20, 0.15, FIXTURE_SEED, 1)
    assert twenty.quorum == 1
    assert sum(twenty.budgets) == 190 * 1
    assert max(twenty.budgets) - min(twenty.budgets) <= 1
    assert twenty.budgets == (10,) * 10 + (9,) * 10


def test_pairing_law_latent_identical() -> None:
    """Assert both arms' latent orders identical per seed — the truth paired.

    compare_run at (n=10, p=0.15, seed=1109, k=3): the acceptance arm's and
    the sizer arm's latent_order byte-equal — the paired-cell design's own
    law, asserted, never assumed.
    """
    record = compare_run(10, 0.15, FIXTURE_SEED, 3)
    assert record.acceptance.latent_order == record.sizer.latent_order
    assert tuple(sorted(record.acceptance.latent_order)) == _expected_ids(10)


def test_determinism_byte_identical_replays() -> None:
    """Assert the same coordinates replay to field-for-field equal records.

    size_run(10, 0.15, 1109, 3) twice: the two frozen SizerRecords equal
    under == (the clock-free surface, the wall-clock never a field);
    compare_run at the same coordinates likewise equal whole.
    """
    first = size_run(10, 0.15, FIXTURE_SEED, 3)
    second = size_run(10, 0.15, FIXTURE_SEED, 3)
    assert first == second
    assert first.latent_order == second.latent_order
    assert first.judgment_counts == second.judgment_counts
    assert first.ranked_groups == second.ranked_groups


def test_model_mechanics() -> None:
    """Assert the binary-threshold model's mechanics — properties, never a magic latent.

    The honest fixture form (the dispatch's ruling): the expected groups and
    scores derive from the record's OWN latent_order, hand-computable at the
    small counts. At (n=4, k=1, p=0): B = 6, q = 1, r = 2 — budgets
    (2, 2, 1, 1) in id order; the per-item thresholds cycle ((m-1) mod 3)+1
    = (1, 2); the true answer yes iff latent position <= threshold — the
    counts by latent position, the exact Fractions, the groups by score.
    The flip grammar at the extreme rate: at p=1.0 every answer flipped —
    the counts invert exactly. The k=2 coverage: budgets (3, 3, 3, 3),
    thresholds (1, 2, 1) — the round-robin cycle reached.
    """
    quiet = size_run(4, 0.0, FIXTURE_SEED, 1)
    assert quiet.budgets == (2, 2, 1, 1)
    latent = quiet.latent_order
    position = {item_id: index for index, item_id in enumerate(latent, start=1)}
    expected_counts = tuple(
        sum(position[item_id] <= ((m % 3) + 1) for m in range(budget))
        for item_id, budget in zip(_expected_ids(4), (2, 2, 1, 1), strict=True)
    )
    assert quiet.judgment_counts == expected_counts
    assert quiet.scores == tuple(
        Fraction(count, budget) for count, budget in zip(quiet.judgment_counts, quiet.budgets, strict=True)
    )
    assert quiet.ranked_groups == ((latent[0],), (latent[1],), tuple(sorted(latent[2:])))
    flipped = size_run(4, 1.0, FIXTURE_SEED, 1)
    assert flipped.budgets == quiet.budgets
    assert flipped.judgment_counts == tuple(
        budget - count for budget, count in zip(flipped.budgets, quiet.judgment_counts, strict=True)
    )
    covered = size_run(4, 0.0, FIXTURE_SEED, 2)
    assert covered.budgets == (3, 3, 3, 3)
    assert covered.judgment_counts == tuple(
        sum(position[item_id] <= ((m % 3) + 1) for m in range(budget))
        for item_id, budget in zip(_expected_ids(4), (3, 3, 3, 3), strict=True)
    )


def test_measure_invariants_reused() -> None:
    """Assert the sizer's counts recomputed by accept_measure — REUSED, never re-implemented.

    accept_measure(sizer.ranked_groups, sizer.latent_order) — the U6
    measure's own surface — recomputes the record's (concordant, discordant,
    tied) exactly; P + Q + T == n0 the pairwise total.
    """
    sizer = size_run(10, 0.15, FIXTURE_SEED, 3)
    assert accept_measure(sizer.ranked_groups, sizer.latent_order) == (
        sizer.concordant,
        sizer.discordant,
        sizer.tied,
    )
    assert sizer.concordant + sizer.discordant + sizer.tied == 45


def test_perfect_case_both_arms_tau_one() -> None:
    """Assert the perfect case at p=0 — both arms' counts the pairwise perfect.

    compare_run(10, 0.0, 1109, 3): the acceptance arm (45, 0, 0) and the
    sizer arm (45, 0, 0) — n0 = 45 all concordant, tau = 1 exactly on both
    arms, stated as counts, never an ordering claim beyond the perfect
    cell's own data.
    """
    record = compare_run(10, 0.0, FIXTURE_SEED, 3)
    assert (record.acceptance.concordant, record.acceptance.discordant, record.acceptance.tied) == (45, 0, 0)
    assert (record.sizer.concordant, record.sizer.discordant, record.sizer.tied) == (45, 0, 0)


def test_record_completeness_matrix() -> None:
    """Assert the whole 54-cell matrix complete — both arms, both k points, green.

    Every (n, p, seed, k) cell driven through compare_run: the budgets sum
    to n0 * quorum with the even split, the latents paired across arms, the
    groups covering every id exactly once, P + Q + T == n0 on BOTH arms.
    The per-cell tau-squared values collected as exact Fractions — the data
    for the record's table; NOTHING about any ordering asserted (the
    Q-curve-assertion ruling), the collection's completeness its own
    guarantee.
    """
    collected: list[Fraction] = []
    for item_count in ACCEPTANCE_ITEM_COUNTS:
        total_pairs = item_count * (item_count - 1) // 2
        ids = _expected_ids(item_count)
        for noise_rate in ACCEPTANCE_NOISE_RATES:
            for seed in ACCEPTANCE_SEEDS:
                for quorum in (1, 3):
                    record = compare_run(item_count, noise_rate, seed, quorum)
                    acceptance, sizer = record.acceptance, record.sizer
                    assert sum(sizer.budgets) == total_pairs * quorum
                    assert max(sizer.budgets) - min(sizer.budgets) <= 1
                    assert acceptance.latent_order == sizer.latent_order
                    assert tuple(sorted(item_id for group in sizer.ranked_groups for item_id in group)) == ids
                    acceptance_ids = tuple(
                        sorted(item_id for group in acceptance.result.ranked_groups for item_id in group),
                    )
                    assert acceptance_ids == ids
                    assert acceptance.concordant + acceptance.discordant + acceptance.tied == total_pairs
                    assert sizer.concordant + sizer.discordant + sizer.tied == total_pairs
                    squared_denominator = (sizer.concordant + sizer.discordant) * total_pairs
                    assert squared_denominator >= 1
                    difference = sizer.concordant - sizer.discordant
                    collected.append(Fraction(difference * difference, squared_denominator))
    assert len(collected) == 54
    assert compare_run(10, 0.15, FIXTURE_SEED, 3) == compare_run(10, 0.15, FIXTURE_SEED, 3)
