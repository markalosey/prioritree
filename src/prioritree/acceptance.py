# Copyright (C) 2026 Mark Losey. All rights reserved.
"""acceptance — the superior-order claim made measurable: the harness, the measure, the floor.

The acceptance unit (U6): the seed-deterministic simulation harness that
exercises the chain exactly as a wrapper would — items with a latent total
order, votes sampled from a noisy comparator at stated noise rates, the
tally's emission measured against the truth by tau-b over the ranked groups
— and the floor, R13's ruled bar: recovery >= 4/5 at noise 0.10-0.20 for
n = 10-30, the floor binding the ruled band only (the degradation cell
recorded, never floored). THE FLOOR'S ASSESSMENT NATURE: the threshold is
the collaborator's BANKED RULING, revisitable at any later brief — carried
as the exact named constant ACCEPTANCE_FLOOR, never a discovered fact; the
machinery that measures it (the harness, the tally, the counts) is
deterministic — a revisit changes one constant, never code. THE
FIRST-TO-IMPORT-RANDOM NOTE: this is the tree's FIRST module to import
random — the randomness is the SIMULATION'S OWN, seed-pinned, instance-local
(one random.Random(seed) per run, never the process-global module); the
core's purity stands untouched (the measure exact integer arithmetic, the
only float the stochastic noise draw itself). The fence: ONLY the U5 public
API — Session's five ops compose the run (never the stores, never a core
surface); the first consumer standing in for the wrappers. The claim's
discipline: recovery-only evidence — the comparative-empirical framing
(pairs + tally beats absolute sizing at equal budget) rides as R13's banked
language, unmeasured by this harness; the honesty pin — byte-reproducibility
asserted over the field-selected clock-free surface only (the wall-clock
stamps named and excluded by construction), never the impossible full-log
byte-identity.
"""

from __future__ import annotations

import random
from dataclasses import dataclass
from fractions import Fraction
from typing import TYPE_CHECKING

from prioritree.registry import OperatorDeclaration, Registry
from prioritree.session import ExhaustedQueue, Session

# TallyResult rides TYPE_CHECKING (the annotation-only import — the record's field type).

if TYPE_CHECKING:
    from prioritree.tally import TallyResult

# THE FLOOR (the threshold's assessment nature: the collaborator's banked
# ruling at G-ACCEPTANCE-BRIEF, revisitable at any later brief — the exact
# data form of the ruled 0.8, never a float; the check's integers derive
# mechanically from it, so a revisit is a one-constant change, never code).
ACCEPTANCE_FLOOR: Fraction = Fraction(4, 5)

# The matrix (content-in-configuration): the same three named seeds across
# every cell — the lucky-seed objection priced; the ruled noise band; the
# ruled item counts; the degradation observation's rate, recorded never
# floored (the floor binds the ruled band only).
# THE SEED-SWAP FALSIFIED (2026-11-20): the (a)-cure (3371 -> 4423, ruled
# at the collaborator's "proceed with your recommendations") was falsified
# by its own first re-run — the RETAINED seed 1109 measured tau =
# 30/sqrt(1800) ~ 0.71 at (10, 0.15), sub-floor: the failures structural
# (the n=10 column at k=1), never unlucky draws. The ruled triple restored
# whole; every sub-floor observation recorded, never erased.
ACCEPTANCE_SEEDS: tuple[int, ...] = (1109, 2213, 3371)
ACCEPTANCE_NOISE_RATES: tuple[float, ...] = (0.10, 0.15, 0.20)
ACCEPTANCE_ITEM_COUNTS: tuple[int, ...] = (10, 20, 30)
# DEGRADATION_RATE's move (the pre-ruled contingency, executed
# 2026-11-20): at k=3 the 0.30 cell measured 0.6844/0.7268/0.8343 —
# seed 3371 CLEARED the floor (three judges tame 30% noise); the
# observation moved to 0.35 (all three seeds below-floor:
# 0.6121/0.6453/0.7336, separated from the band's min 0.8223) — the
# test's meaning stands; the 0.30 row recorded, never erased.
DEGRADATION_RATE: float = 0.35
# THE QUORUM (the k=1 -> k=3 revision, ruled 2026-11-20 at the
# collaborator's "proceed with your recommendations"): the k=1
# single-judgment table measured 8 of 27 in-band cells sub-floor (min tau
# 0.4714) — R13's band does not survive at one judgment per pair; THREE
# named comparators per pair (the tally's own aggregation, R8's quorum
# as data) carries it. The k=1 table recorded at
# synthesize/acceptance-bytes.md — the baseline, never erased.
ACCEPTANCE_QUORUM: int = 3

# The id template: zero-padded so lexicographic order = numeric order — the
# decoupling of truth from id sort made checkable by construction.
ACCEPTANCE_ID_TEMPLATE: str = "item-{index:02d}"

# The comparator stamp (R5: the stamp is data, zero tally effect) — the id
# arbitrary-but-fixed bytes; the class rides R5's ruled set (the schema's
# legal vocabulary): the machine judge for the generated judgments.
HARNESS_COMPARATOR_ID: str = "acceptance-noisy-comparator"
HARNESS_COMPARATOR_CLASS: str = "llm"

# The floor check's derived integers (tau >= 4/5 with the truth strict:
# (P-Q)/sqrt((P+Q)·n0) >= 4/5 ⟺ P >= Q AND 25·(P-Q)^2 >= 16·(P+Q)·n0 —
# cross-multiplied, exact, the radical never taken): the squared floor's
# numerator and denominator, derived mechanically from ACCEPTANCE_FLOOR.
_FLOOR_NUMERATOR: int = ACCEPTANCE_FLOOR.numerator**2
_FLOOR_DENOMINATOR: int = ACCEPTANCE_FLOOR.denominator**2


@dataclass(frozen=True)
class AcceptanceRecord:
    """AcceptanceRecord — one simulation run's clock-free evidence whole.

    Purpose: carry the run's reproducibility surface as data — the run's own
    coordinates (item_count, noise_rate, seed), the latent truth, the
    (pair, winner) verdict sequence in queue order, the tally's frozen
    emission, and the measure's integer counts; the replay's equality
    surface, field-selected (the wall-clock stamps — VoteRecord.recorded_at,
    RunManifest.registered_at — excluded by construction: they never ride
    this record).
    Refuses when: never at construction — a frozen value type; the guard
    fires inside accept_run before any byte of this record exists.
    Re-run: idempotent — a value type; the same (item_count, noise_rate,
    seed) run twice constructs equal records, clock-free field for field.
    Touches: nothing — a pure value; read by the tests' assertions.
    Provenance: R13 (the seed-deterministic harness), the U6 row (the gate,
    the clock-free surface), G-ACCEPTANCE (the five conditions),
    acceptance-brief §1 (the record's fields), §4 (the reproducibility pin);
    discover/acceptance and understand/acceptance (the legs riding the
    brief).
    """

    item_count: int
    noise_rate: float
    seed: int
    latent_order: tuple[str, ...]
    verdicts: tuple[tuple[tuple[str, str], str], ...]
    result: TallyResult
    concordant: int
    discordant: int
    tied: int


def floor_holds(concordant: int, discordant: int, tied: int, item_count: int) -> bool:
    """Return whether the integer floor inequality holds — the tests' shared assertion.

    Purpose: the exact integer form of tau >= ACCEPTANCE_FLOOR with the
    truth strict — P >= Q AND 25*(P-Q)^2 >= 16*(P+Q)*n0 AND the
    definedness guard P+Q >= 1; every term an integer, the radical never
    taken, no floats anywhere in the comparison; the coefficients derived
    from ACCEPTANCE_FLOOR at import time — a revisited floor changes one
    constant, never this code.
    Refuses when: never — a pure boolean over its integer arguments.
    Re-run: deterministic — exact integer arithmetic.
    Touches: nothing — pure over its arguments.
    Provenance: acceptance-brief §3 (the integer inequality, the P+Q
    definedness guard), §4 (the floor binding the ruled band only), R13
    (the ruled bar), the Fraction precedent (exact arithmetic).
    """
    total_pairs = item_count * (item_count - 1) // 2
    concordant_minus_discordant = concordant - discordant
    scored = concordant + discordant
    if concordant < discordant or scored < 1:
        return False
    return _FLOOR_DENOMINATOR * concordant_minus_discordant**2 >= _FLOOR_NUMERATOR * scored * total_pairs


def accept_measure(
    ranked_groups: tuple[tuple[str, ...], ...],
    latent_order: tuple[str, ...],
) -> tuple[int, int, int]:
    """Measure the emission against the truth — tau-b's integer counts (P, Q, T).

    Purpose: over the n0 = n(n-1)/2 unordered pairs of the flattened groups
    — same emission group => T; different groups => P if the latent-earlier
    item's group precedes, else Q; the truth strict (the standard tau-b with
    the truth untied); within-group id order irrelevant (only co-membership
    and group order); the measure reads the groups ALONE, never scores.
    Refuses when: the invariant breaks — P + Q + T != n0, ValueError
    raised naming the invariant; the core's write gate the authority for
    id uniqueness, never re-policed.
    Re-run: deterministic — same inputs => same counts, byte-identical.
    Touches: nothing — pure over its arguments.
    Provenance: R13, acceptance-brief §3, the U4/U5 citation contract
    (ranked_groups — the tie-group form tau consumes); both legs.
    """
    latent_position = {item_id: position for position, item_id in enumerate(latent_order)}
    group_index: dict[str, int] = {}
    for index, group in enumerate(ranked_groups):
        for item_id in group:
            group_index[item_id] = index
    members = [item_id for group in ranked_groups for item_id in group]
    concordant = 0
    discordant = 0
    tied = 0
    for i, item_a in enumerate(members):
        for item_b in members[i + 1 :]:
            if group_index[item_a] == group_index[item_b]:
                tied += 1
            elif latent_position[item_a] < latent_position[item_b]:
                concordant += 1
            else:
                discordant += 1
    total_pairs = len(members) * (len(members) - 1) // 2
    if concordant + discordant + tied != total_pairs:
        guard_head = "the measure's invariant broke: P + Q + T != n0"
        raise ValueError(guard_head)
    return (concordant, discordant, tied)


def accept_run(item_count: int, noise_rate: float, seed: int) -> AcceptanceRecord:
    """Run one simulation — the seed-deterministic harness through Session's five ops.

    Purpose: (1) ONE random.Random(seed) instance per run — private state,
    stdlib-reproducible, never the process-global module; the draw order
    pinned by construction (the permutation first, the per-judgment draws
    after); (2) the seeded latent order: n ids from the zero-padded
    template, the truth = rng.sample as the instance's FIRST act — the
    HONESTY GUARD asserts the drawn permutation differs from the id-sorted
    order (were the truth implicit in id sort, the tally's deterministic
    id tie-break would correlate with truth and inflate tau on every
    noise-induced score tie — the decoupling is load-bearing); (3) the
    items as opaque (id, label) rows — the truth harness-local data,
    NEVER registered as such; (4) register_run at the ruled quorum
    k=ACCEPTANCE_QUORUM — 3, THREE named comparators per pair (the k=1
    single-judgment baseline measured 8 of 27 in-band cells sub-floor,
    min tau 0.4714; the quorum the tally's own aggregation implies; the
    k=1 table recorded, never erased); (5) the loop: next_pair (the pair
    re-served until its census count reaches quorum) -> ONE draw per
    serving -> the TRUE positional verdict,
    FLIPPED when u < noise_rate (a tie NEVER sampled) -> cast_vote under
    the count-suffixed judge id, the (pair, winner) recorded in queue
    order -> repeat; ExhaustedQueue (the
    DONE signal) caught BY TYPE — never a bare except; (6) tally_rank —
    TallyRefusedError propagates verbatim — never swallowed, never
    wrapped; (7) the measure over the frozen emission, the record
    returned whole.
    Refuses when: the honesty guard fails — the drawn latent order equals
    the id-sorted order — raising ValueError naming the seed; the core's
    own refusals ride through by type, never swallowed.
    Re-run: seed-deterministic — the same (item_count, noise_rate, seed)
    yields byte-identical latent order, verdict sequence, TallyResult and
    counts across replays (the clock-free surface; the wall-clock stamps
    named and excluded by construction).
    Touches: nothing — one fresh Session(Registry()) per run, in-memory,
    the U5 public API ONLY; random the simulation's own, seed-pinned.
    Provenance: R13, the U6 row, G-ACCEPTANCE, acceptance-brief §2-§4;
    both legs riding the brief.
    """
    rng = random.Random(seed)
    ids = tuple(ACCEPTANCE_ID_TEMPLATE.format(index=index) for index in range(item_count))
    latent = tuple(rng.sample(list(ids), item_count))
    if latent == tuple(sorted(ids)):
        guard_head = f"harness honesty guard: the seeded latent order equals the id-sorted order at seed {seed}"
        raise ValueError(guard_head + " — the truth would be implicit in the id sort; revisit the seed at the gate")
    items: list[tuple[str, str]] = [(item_id, f"label-{item_id}") for item_id in ids]
    session = Session(Registry())
    run_id, _manifest, _count = session.register_run(
        items,
        operator=OperatorDeclaration(id="acceptance-op", question="Which is more important?"),
        quorum=ACCEPTANCE_QUORUM,
    )
    verdicts: list[tuple[tuple[str, str], str]] = []
    while True:
        try:
            item_a, item_b, pair_count = session.next_pair(run_id)
        except ExhaustedQueue:
            break
        true_verdict = "prefer-a" if latent.index(item_a) < latent.index(item_b) else "prefer-b"
        flipped_verdict = "prefer-b" if true_verdict == "prefer-a" else "prefer-a"
        verdict = flipped_verdict if rng.random() < noise_rate else true_verdict
        session.cast_vote(
            run_id,
            (item_a, item_b),
            verdict,
            comparator_id=f"{HARNESS_COMPARATOR_ID}-{pair_count + 1}",
            comparator_class=HARNESS_COMPARATOR_CLASS,
        )
        verdicts.append(((item_a, item_b), verdict))
    result = session.tally_rank(run_id)
    concordant, discordant, tied = accept_measure(result.ranked_groups, latent)
    return AcceptanceRecord(
        item_count=item_count,
        noise_rate=noise_rate,
        seed=seed,
        latent_order=latent,
        verdicts=tuple(verdicts),
        result=result,
        concordant=concordant,
        discordant=discordant,
        tied=tied,
    )
