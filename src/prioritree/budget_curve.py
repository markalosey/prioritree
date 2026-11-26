# Copyright (C) 2026 Mark Losey. All rights reserved.
"""budget_curve — the comparative-empirical claim made measurable: the two arms at equal budget.

THE CLAIM, PRICED: acceptance.py carried R13's comparative-empirical framing — pairwise
comparison plus the tally beats absolute sizing at equal budget — as BANKED LANGUAGE,
unmeasured by that harness (its own named discipline); this unit graduates the claim from
ruled language to MEASUREMENT, pricing the option acceptance-brief §5 named: the sizer arm,
a binary-threshold absolute sizer per Q-curve-sizer — each item judged alone against the
integer thresholds j cycling 1..n-1, ONE flip draw per judgment at the noise rate, the score
the exact Fraction of yes over budget — sized at the SAME budget the pairwise arm spends
(B = n0 x the floored quorum, max(quorum, len(HARNESS_JUDGE_CLASSES)) — the pairwise arm's
own registration form, the corroboration floor's minimum; n0 = n(n-1)/2), both arms composed
as one paired cell by compare_run: one
call, both arms, the equal-budget law by construction (B derives from the SAME (n, quorum) —
no independent parameter, no cross-check).
THE NOISE-STREAMS RULING (the brief's §2, ruled at G-BUDGET-CURVE 2026-11-21): the truth
PAIRED — both arms draw their latent from random.Random(seed), the instance's FIRST act,
the same seed naming the same latent in both arms — and the noise INDEPENDENT: the sizer's
flip draws ride the derived instance seeded by SIZER_SEED_TEMPLATE.format(seed=seed), never
the latent stream's own; the priced language — "the same noisy comparator at the same p" —
names the noise MODEL, never the realization; the alternative (identical streams, maximal
coupling: variance-free but luck-correlated, arguably understating the sizer's independent
error structure) priced and declined.
THE POLARITY (load-bearing): the threshold judgment asks "is item i among the top j?" — the
1-indexed latent position answers YES when position <= j — so the latent-FIRST item answers
yes to EVERY threshold and the latent-last to none: at zero noise the scores descend exactly
by latent position, the perfect case (p=0) tau = 1 exactly; the inverted ask ("is position
> j") would crown the latent-LAST item and fail the perfect case by construction.
The laws riding: the naming law (every new symbol named by its act's first word — the brief's
§1 acts "Size the run's items at equal budget" / "Compare the two arms at equal budget"),
content-in-configuration (the seed-derivation template the named constant SIZER_SEED_TEMPLATE,
never an inline literal), zero runtime deps (random the stdlib's — the simulation's own,
instance-local, seed-pinned, never the process-global module; pure in-memory, the no-shell
law held).
THE READING, STATED HONESTLY AT THE CLOSE: this module MEASURES, it never asserts — the
ordering claim is stated NOWHERE here (Q-curve-assertion); the reading — supported,
falsified, or mixed over the measured cells, the aggregate stated — lands in the record at
the store's build home, written from the data, never pre-written.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from fractions import Fraction
from typing import TYPE_CHECKING, Final

from prioritree.acceptance import ACCEPTANCE_ID_TEMPLATE, HARNESS_JUDGE_CLASSES, accept_measure, accept_run

# AcceptanceRecord rides TYPE_CHECKING (the annotation-only import — the curve record's field
# type; the dataclass's field annotations stay strings under future-annotations, never resolved).

if TYPE_CHECKING:
    from prioritree.acceptance import AcceptanceRecord

# The public surface: the two records and the two acts (the brief's §1 — the module's whole).
__all__ = ["CurveRecord", "SizerRecord", "compare_run", "size_run"]

# The sizer seed template (content-in-configuration: the derivation lives as named data,
# never an inline literal): the derived instance's form — the truth PAIRED (the same seed
# names the same latent in both arms), the noise INDEPENDENT (the derived stream never
# touches the latent stream's draws; the identical-streams alternative priced and declined).
# A string seed derives deterministically in the stdlib's version-2 seeding (sha512-based —
# stable across replays and platforms, never the hash()-randomized path).


@dataclass(frozen=True)
class SizerRecord:
    """SizerRecord — one sizer-arm run's clock-free evidence whole.

    Purpose: carry the sizing run's replay-equality surface as data — the run's coordinates
    (item_count, noise_rate, seed, quorum), the latent truth (paired with the pairwise arm's by
    the shared seed), the per-item yes-counts and budget allocation (judgment_counts + budgets:
    the minimal replay surface, ruled over the (threshold, answer) pairs — the pairs add detail
    the replay never reads, the replay fully determined by (seed, quorum, B_i) by construction),
    the exact Fraction scores, the emission's ranked groups (the tie-group form the measure
    consumes), and the measure's integer counts.
    Refuses when: never at construction — a frozen value type; the honesty guard fires inside
    size_run before any byte of this record exists.
    Re-run: idempotent — a value type; the same (item_count, noise_rate, seed, quorum) run twice
    constructs equal records, byte-identical across replays BY CONSTRUCTION — clock-free fields
    only, NO stamps anywhere (no wall-clock, no process state: nothing time-touched ever rides
    this record).
    Touches: nothing — a pure value; read by the tests' assertions and the record's per-cell table.
    Provenance: R13 (the claim priced), acceptance-brief §5 (the priced option), the composition
    (the seven questions ruled 2026-11-21 — the record form ruled), the brief §1 (the fields
    pinned), G-BUDGET-CURVE (the five conditions).
    """

    item_count: int
    noise_rate: float
    seed: int
    quorum: int
    latent_order: tuple[str, ...]
    judgment_counts: tuple[int, ...]
    budgets: tuple[int, ...]
    scores: tuple[Fraction, ...]
    ranked_groups: tuple[tuple[str, ...], ...]
    concordant: int
    discordant: int
    tied: int


@dataclass(frozen=True)
class CurveRecord:
    """CurveRecord — one cell's paired evidence: both arms at equal budget, whole.

    Purpose: carry the paired comparison as data — the pairwise arm's AcceptanceRecord (fresh,
    the amended signature, never cited for a second arm) and the sizer arm's SizerRecord at the
    same coordinates; a NAMED frozen record over an anonymous pair (the naming law answered
    mechanically; the replay-equality surface carried whole — both fields clock-free,
    byte-identical across replays by construction).
    Refuses when: never at construction — a frozen value type; both arms' own guards fire inside
    their runs before any byte of this record exists.
    Re-run: idempotent — a value type; the same coordinates run twice construct equal records,
    clock-free field for field.
    Touches: nothing — a pure value; read by the tests' assertions and the record's per-cell table.
    Provenance: R13, acceptance-brief §5 (the priced option), the composition (the return shape
    ruled), the brief §1 (the return named), §3 (one call, both arms), G-BUDGET-CURVE (the five
    conditions).
    """

    acceptance: AcceptanceRecord
    sizer: SizerRecord


def size_run(item_count: int, noise_rate: float, seed: int, quorum: int) -> SizerRecord:
    """Size the run's items at equal budget — the binary-threshold arm whole.

    Purpose: (1) ONE random.Random(seed) instance for the truth — private state,
    stdlib-reproducible, never the process-global module; the ids from ACCEPTANCE_ID_TEMPLATE,
    the latent = rng.sample as the instance's FIRST act, the HONESTY GUARD raising when the drawn
    permutation equals the id-sorted order (the same idiom as accept_run: were the truth implicit
    in the id sort, the within-group id tie-break would correlate with truth and inflate the
    sizer's tau on every noise-induced score tie — the decoupling load-bearing); (2) the noise
    instance DERIVED — random.Random(SIZER_SEED_TEMPLATE.format(seed=seed)) — the truth paired
    (the same seed names the same latent in both arms), the noise independent (the derived stream
    never touches the latent stream's draws; the identical-streams alternative priced and
    declined); (3) the budget split: B = n0 x max(quorum, len(HARNESS_JUDGE_CLASSES)) (n0 =
    n(n-1)/2, the pairwise arm's own registration form — the floored quorum, the corroboration
    floor's minimum, both arms at the floored budget; the k=1 leg sized at the floored form,
    the single-judgment baseline retired to the recorded table), q = B // n, r = B mod n —
    the first r items in id order allotted q+1 judgments, the rest q: the equal-budget law
    exact, sum(B_i) = B, never a float's rounding;
    (4) the per-item judgment loop, items in id order: judgment m (0-indexed, m < B_i) asks
    "is item i among the top j?" — the polarity load-bearing — against the threshold
    j = (m mod (n-1)) + 1 (the per-item counter cycling 1..n-1, each item exhausting its own
    B_i against its own stream); the 1-indexed latent position answers YES when position <= j —
    the latent-first item to every threshold, the latent-last to none — the true answer
    deterministic, then ONE flip draw per judgment: u < noise_rate => the FLIPPED answer (the
    acceptance flip grammar verbatim in form — a draw, never a tie), the yes-count accumulating;
    (5) the scores exact — Fraction(yes_count, B_i) per item, never a float; (6) the emission:
    score-descending groups, equal Fractions tied in one group, within-group by id, every id
    exactly once — the tally's deterministic mirror in the form accept_measure consumes; (7) the
    measure REUSED — accept_measure over the groups against the latent, never re-implemented
    here; (8) the SizerRecord returned whole.
    Refuses when: the honesty guard fails — the drawn latent order equals the id-sorted order —
    raising ValueError naming the seed (the degenerate coordinates n < 2 refuse here too: their
    only permutation IS the id-sorted order); no other refusal is ruled — the matrix's cells
    (n in {10, 20, 30}, k in {1, 3}) never produce a vanishing budget, and the core is never
    touched.
    Re-run: seed-deterministic — the same (item_count, noise_rate, seed, quorum) yields a
    byte-identical SizerRecord across replays: the latent by the seed's stream, the flips by the
    derived stream, the arithmetic exact — no clock, no stamps, no platform surface.
    Touches: nothing — pure in-memory, the stdlib random the simulation's own (instance-local,
    seed-pinned); zero subprocess (the no-shell law), zero stores, zero clock.
    Provenance: R13 (the claim priced), acceptance-brief §5 (the priced option), Q-curve-sizer
    (the binary-threshold model), the composition (the seven questions ruled 2026-11-21), the
    brief §2 (the mechanics whole — the noise-streams ruling, the budget split pinned), §1 (the
    pinned fields), G-BUDGET-CURVE (the five conditions).
    """
    rng = random.Random(seed)
    ids = tuple(ACCEPTANCE_ID_TEMPLATE.format(index=index) for index in range(item_count))
    latent = tuple(rng.sample(list(ids), item_count))
    if latent == tuple(sorted(ids)):
        guard_head = f"sizer honesty guard: the seeded latent order equals the id-sorted order at seed {seed}"
        raise ValueError(guard_head + " — the truth would be implicit in the id sort; revisit the seed at the gate")
    noise_rng = random.Random(SIZER_SEED_TEMPLATE.format(seed=seed))
    total_pairs = item_count * (item_count - 1) // 2
    total_budget = total_pairs * max(quorum, len(HARNESS_JUDGE_CLASSES))
    base_budget, remainder = divmod(total_budget, item_count)
    budgets = tuple(base_budget + 1 if index < remainder else base_budget for index in range(item_count))
    judgment_counts: list[int] = []
    for item_id, item_budget in zip(ids, budgets, strict=True):
        position = latent.index(item_id) + 1
        yes_count = 0
        for judgment_index in range(item_budget):
            threshold = (judgment_index % (item_count - 1)) + 1
            true_answer = position <= threshold
            answer = not true_answer if noise_rng.random() < noise_rate else true_answer
            if answer:
                yes_count += 1
        judgment_counts.append(yes_count)
    scores = tuple(Fraction(yes, budget) for yes, budget in zip(judgment_counts, budgets, strict=True))
    groups_by_score: dict[Fraction, list[str]] = {}
    for item_id, score in zip(ids, scores, strict=True):
        groups_by_score.setdefault(score, []).append(item_id)
    ranked_groups = tuple(tuple(sorted(groups_by_score[score])) for score in sorted(groups_by_score, reverse=True))
    concordant, discordant, tied = accept_measure(ranked_groups, latent)
    return SizerRecord(
        item_count=item_count,
        noise_rate=noise_rate,
        seed=seed,
        quorum=quorum,
        latent_order=latent,
        judgment_counts=tuple(judgment_counts),
        budgets=budgets,
        scores=scores,
        ranked_groups=ranked_groups,
        concordant=concordant,
        discordant=discordant,
        tied=tied,
    )


def compare_run(item_count: int, noise_rate: float, seed: int, quorum: int) -> CurveRecord:
    """Compare the two arms at equal budget — one call, both arms, one paired cell.

    Purpose: (1) the pairwise arm accept_run(item_count, noise_rate, seed, quorum) FRESH — the
    amended four-argument signature (§4's one additive amendment: the quorum a parameter, the
    default ACCEPTANCE_QUORUM held — every existing caller's behavior byte-identical), never a
    cited or replayed arm; (2) the sizer arm size_run(item_count, noise_rate, seed, quorum) at
    the SAME coordinates — the equal-budget derivation's single home: B derives from the same
    (item_count, quorum) at the floored max form, no independent parameter, the equal-budget
    law by construction (both arms at the floored budget);
    (3) the CurveRecord returned whole — both arms' records paired per cell, the latent PAIRED
    (the same seed names the same latent in both arms) and the noise INDEPENDENT (each arm its
    own stream, the derived instance's form), the pairing the comparison's own control.
    Refuses when: never its own refusal — both arms' guards ride through by type, never
    swallowed, never wrapped: the honesty guard (the shared idiom) fires inside its arm before
    any byte of this record exists.
    Re-run: seed-deterministic — the same (item_count, noise_rate, seed, quorum) yields a
    byte-identical CurveRecord across replays: both fields clock-free, NO stamps anywhere, the
    latent by the seed's stream in both arms, the flips by their own.
    Touches: nothing — in-memory ONLY (both runs pure); the U5 public API composed inside
    accept_run, zero subprocess (the no-shell law), zero stores, zero clock.
    Provenance: R13, acceptance-brief §5 (the priced option), the composition (the seven
    questions ruled 2026-11-21), the brief §3 (one call, both arms), §1 (the CurveRecord named),
    G-BUDGET-CURVE (the five conditions).
    """
    acceptance = accept_run(item_count, noise_rate, seed, quorum)
    sizer = size_run(item_count, noise_rate, seed, quorum)
    return CurveRecord(acceptance=acceptance, sizer=sizer)


SIZER_SEED_TEMPLATE: Final[str] = "{seed}-sizer"
