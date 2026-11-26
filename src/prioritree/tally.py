# Copyright (C) 2026 Mark Losey. All rights reserved.
"""tally — the pure projection: weight the votes, count, gate, rank, emit.

The tally unit (U4): the pure chain (weight → count → gate → score → rank)
over (manifest, vote_log) — R10 the win-rate/Copeland method (score =
(wins + 0.5·ties)/comparisons, deterministic id tie-break, NO score field in
the vote record), R11 the cycle policy (cycles structural, never an error,
never resolved by judgment — the fractional arithmetic dissolves them into
win fractions; the cycle named in the coverage data, never hidden), R12 the
strictly binary terminal states (DONE = the ranked whole; SAFE HALT = the
coverage-gate refusal naming the isolated items/components and the closing
pairs; never a partial ranking; re-runs byte-identical). The Parnas fold: the
win-rate family the ONE algorithm behind this module seam, replaceable
without touching any other unit — no score field crosses the vote interface.
The fence (the must-not-know, held by construction): no scheduling strategy
(the expected pair SET cited as data), no comparator identity (R5's stamps
never read into scoring; the CLASS stamp read at the coverage GATE alone --
F8's corroboration floor, the identity never read at all; the fence line's
own amendment), no storage medium (no store type anywhere); NO
datetime — purity's negative space (no time, no environment, no randomness).
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import TYPE_CHECKING

from prioritree.policy import missing_classes
from prioritree.scheduler import schedule_pairs
from prioritree.votes import COMPARATOR_CLASSES

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence

    from prioritree.registry import RunManifest
    from prioritree.scheduler import Pair
    from prioritree.votes import VoteRecord

# The counting pass's positional vocabulary (R4's triple, cited as a CONTRACT
# PRECONDITION from U3's write gate — the tally counts over the run's own
# declared set, never re-polices the record): content-in-configuration — the
# tokens are named module constants, never inline logic.
PREFER_A: str = "prefer-a"
PREFER_B: str = "prefer-b"
TIE: str = "tie"

# The version stamp (content-in-configuration: an auditability contract with
# U5/U6 — which algorithm produced the emission; the method + a version index
# for the later probabilistic swap, an index NEVER a date — purity).
TALLY_ALGORITHM: str = "win-rate-v1"

# Structural constants (named, per the zero-magic-value-in-src discipline):
# the score's exact-rational carrier — numerator 2·wins + 1·ties over
# denominator 2·comparisons (the cross-multiplied-integer comparison's form;
# R10's score with the 0.5·ties carried as the integer 2·w + t).
_WIN_WEIGHT = 2
_TIE_WEIGHT = 1


@dataclass(frozen=True)
class CoverageDatum:
    """CoverageDatum — the coverage block, R11's named home.

    Purpose: carry the coverage facts as data — the graph components (at
    DONE exactly one: the connected whole, the connectivity fact's positive
    form), the ONE named Condorcet cycle as its directed dominance edges
    (deterministically the first found in id-sorted DFS order; EMPTY when
    none), the WEIGHTED per-pair counts over the full expected universe
    (0 included — the gate's own datum, never the census's unweighted view),
    the WEIGHTED per-pair per-CLASS counted votes over the same full universe
    (every vocabulary class present, 0 included -- the corroboration named in
    the coverage data, never hidden; R11's discipline extended to F8's floor),
    and the verdict boolean.
    Refuses when: never at construction — a frozen value type; the gate
    raises before any partial emission exists.
    Re-run: idempotent — a value type; byte-identical under re-runs.
    Touches: nothing — a pure value; held by TallyResult, read by U5/U6.
    Provenance: R11 (the cycle named in the coverage data, never hidden),
    R12 (DONE's positive form), tally-brief §2 (CoverageDatum), §4 (the
    weighted datum), discover/tally and understand/tally (the legs riding
    the brief).
    """

    components: tuple[tuple[str, ...], ...]
    cycle: tuple[tuple[str, str], ...]
    pair_counts: Mapping[Pair, int]
    pair_class_counts: Mapping[str, Mapping[str, int]]
    done: bool


@dataclass(frozen=True)
class TallyResult:
    """TallyResult — the DONE emission, whole.

    Purpose: hold the ranked whole — the score-descending tie groups (maximal
    equal-score runs; ids sorted within each group), the three parallel
    per-item integer maps over EVERY manifest id (0 included; comparisons_i
    = wins + losses + ties, derivable in one sum at the consumer), the
    coverage block, and the version stamp.
    Refuses when: never at construction — a frozen value type; the gate
    raises before any partial ranking exists (never a partial ranking
    dressed as whole).
    Re-run: idempotent — a value type; byte-identical under re-runs (the
    purity property: same (manifest, votes) ⇒ same emission).
    Touches: nothing — a pure value; U5 serializes it, U6's tau harness
    reads the groups.
    Provenance: R10 (NO score field — recomputable from the counts, the
    ordering mechanism internal), R12 (the strictly binary terminal states),
    op 5, G-TALLY, tally-brief §2 (the emission, field-level), discover/tally
    and understand/tally (the legs riding the brief).
    """

    ranked_groups: tuple[tuple[str, ...], ...]
    per_item_wins: Mapping[str, int]
    per_item_losses: Mapping[str, int]
    per_item_ties: Mapping[str, int]
    coverage: CoverageDatum
    algorithm_version: str


class TallyRefusedError(Exception):
    """TallyRefusedError — the typed refusal: expected, found, next_action.

    Purpose: carry the SAFE HALT's refusal grammar (expected/found/
    next-action) as data the CLI/service wrappers catch and render; raised,
    never returned; the strictly binary distinction is the raise-or-return
    itself.
    Refuses when: never — it IS the refusal; the message renders all three
    fields so an uncaught traceback still names the legal form.
    Re-run: deterministic — the same violation raises the same three fields.
    Touches: nothing — a plain Exception subclass (zero runtime deps).
    Provenance: the RegistryRefusedError precedent (registry.py:89-115, the
    Error-suffix family form, N818), tally-brief §2 (the three-field typed
    refusal), §4 (the SAFE-HALT bytes); R12/op 5 (the safe halt).
    """

    def __init__(self, expected: str, found: str, next_action: str) -> None:
        """Initialize the refusal with its three named fields.

        Purpose: carry expected/found/next_action plus the rendered message.
        Refuses when: never.
        Re-run: idempotent.
        Touches: nothing.
        Provenance: tally-brief §2 (the typed exception, RefusedError precedent).
        """
        self.expected = expected
        self.found = found
        self.next_action = next_action
        super().__init__(f"refused — expected: {expected} | found: {found} | next: {next_action}")


@dataclass(frozen=True)
class _Counted:
    """_Counted — the counting pass's private accumulation state."""

    pair_counts: dict[Pair, int]
    pair_class_counts: dict[Pair, dict[str, int]]
    wins: dict[str, int]
    losses: dict[str, int]
    ties: dict[str, int]
    preference: dict[Pair, tuple[int, int]]


def _counted_records(manifest: RunManifest, vote_log: Sequence[VoteRecord]) -> tuple[VoteRecord, ...]:
    """Return the run's weighted records — the correction counted, the superseded excluded.

    Purpose: apply the run filter (records with run_id != manifest.run_id
    dropped — the census's own discipline, cited), then the exclusion set
    E = {r.supersedes for r in the run's log if not None} — set semantics,
    no chain walk (every chain's interior is E, its uncited tip counted;
    the fork's two corrections citing one original: the original excluded
    ONCE, both corrections counted — one judgment, one unit of weight).
    Refuses when: never — the pure weighting pass.
    Re-run: deterministic — order-independent over the multiset.
    Touches: nothing — pure over its arguments.
    Provenance: tally-brief §3.1 (the weighting pass, the fork ratified),
    R9 (corrections ride supersedes), U3's same-run check (cross-run
    citations unrepresentable).
    """
    in_run = [record for record in vote_log if record.run_id == manifest.run_id]
    excluded = {record.supersedes for record in in_run if record.supersedes is not None}
    return tuple(record for record in in_run if record.vote_id not in excluded)


def _count_votes(
    ids: Sequence[str],
    expected_pairs: Sequence[Pair],
    counted: tuple[VoteRecord, ...],
) -> _Counted:
    """Accumulate the weighted counts — the positional mapping over the canonical pair.

    Purpose: build the weighted per-pair counts (0 included over the full
    expected universe), the per-item integer wins/losses/ties (winner ==
    PREFER_A ⇒ item_a win/item_b loss; == PREFER_B ⇒ item_b win/item_a loss;
    == TIE ⇒ both +1 tie — a tie still compares), and the per-pair
    prefer-a/prefer-b tallies (the dominance graph's input), and the per-pair
    per-CLASS counts (the corroboration floor's rollup -- every vocabulary
    class 0 included, the CLASS STAMP accumulated in this same one pass, the
    identity never read).
    Refuses when: never — pair legality and verdict membership are CITED
    PRECONDITIONS (U3's write gate the authority, never re-policed — U2's
    precedent; the mapping total over the only legal declared set).
    Re-run: deterministic — integer accumulation, exact, commutative,
    associative (the purity ground).
    Touches: nothing — pure over its arguments.
    Provenance: tally-brief §3.2 (the counting pass), R10 (integer counts
    only), the FR-MEM-0001 lesson (the expected set cited, never re-derived).
    """
    pair_counts: dict[Pair, int] = dict.fromkeys(expected_pairs, 0)
    pair_class_counts: dict[Pair, dict[str, int]] = {
        pair: dict.fromkeys(sorted(COMPARATOR_CLASSES), 0) for pair in expected_pairs
    }
    preference: dict[Pair, tuple[int, int]] = dict.fromkeys(expected_pairs, (0, 0))
    wins: dict[str, int] = dict.fromkeys(ids, 0)
    losses: dict[str, int] = dict.fromkeys(ids, 0)
    ties: dict[str, int] = dict.fromkeys(ids, 0)
    for record in counted:
        pair_counts[record.pair] += 1
        pair_class_counts[record.pair][record.comparator_class] += 1
        item_a, item_b = record.pair.item_a, record.pair.item_b
        if record.winner == PREFER_A:
            wins[item_a] += 1
            losses[item_b] += 1
            preference[record.pair] = (preference[record.pair][0] + 1, preference[record.pair][1])
        elif record.winner == PREFER_B:
            wins[item_b] += 1
            losses[item_a] += 1
            preference[record.pair] = (preference[record.pair][0], preference[record.pair][1] + 1)
        else:
            ties[item_a] += 1
            ties[item_b] += 1
    return _Counted(
        pair_counts=pair_counts,
        pair_class_counts=pair_class_counts,
        wins=wins,
        losses=losses,
        ties=ties,
        preference=preference,
    )


def _components(ids: Sequence[str], counted_pairs: Sequence[Pair]) -> tuple[tuple[str, ...], ...]:
    """Union-find the comparison graph — the components, ids-sorted within, smallest-id-ordered.

    Purpose: partition the manifest ids over the ≥1-counted pairs (the graph
    of comparisons made; quorum shortfalls ride leg 3 — the legs stay
    orthogonal); return each component ids-sorted, the components ordered
    by smallest id.
    Refuses when: never — a pure traversal (deterministic, near-linear).
    Re-run: deterministic — same (ids, edges) ⇒ same partition.
    Touches: nothing — pure over its arguments.
    Provenance: tally-brief §4 leg 2 (union-find, the component partition
    as data), R12 (the isolated items/components named).
    """
    parent: dict[str, str] = {item_id: item_id for item_id in ids}

    def find(node: str) -> str:
        """Compress the path; return the root."""
        root = node
        while parent[root] != root:
            root = parent[root]
        while parent[node] != root:
            parent[node], node = root, parent[node]
        return root

    for pair in counted_pairs:
        root_a, root_b = find(pair.item_a), find(pair.item_b)
        if root_a != root_b:
            parent[root_b] = root_a
    members: dict[str, list[str]] = {}
    for item_id in ids:
        members.setdefault(find(item_id), []).append(item_id)
    return tuple(tuple(sorted(group)) for _, group in sorted(members.items(), key=lambda entry: entry[1][0]))


def _dominance_adjacency(ids: Sequence[str], preference: Mapping[Pair, tuple[int, int]]) -> dict[str, list[str]]:
    """Build the dominance graph's id-sorted adjacency (prefer-a majority: a to b; prefer-b: b to a).

    Purpose: the cycle finder's graph input — per pair, the weighted verdict
    counts give one dominance direction; ties/equality give none; neighbors
    id-sorted.
    Refuses when: never — pure over its arguments.
    Re-run: deterministic.
    Touches: nothing.
    Provenance: tally-brief §4 (the dominance graph), R11 (the cycle's input).
    """
    adjacency: dict[str, list[str]] = {item_id: [] for item_id in ids}
    for pair, (prefer_a_count, prefer_b_count) in preference.items():
        if prefer_a_count > prefer_b_count:
            adjacency[pair.item_a].append(pair.item_b)
        elif prefer_b_count > prefer_a_count:
            adjacency[pair.item_b].append(pair.item_a)
    for neighbors in adjacency.values():
        neighbors.sort()
    return adjacency


def _find_cycle(ids: Sequence[str], preference: Mapping[Pair, tuple[int, int]]) -> tuple[tuple[str, str], ...]:
    """Name ONE Condorcet cycle — the first found in id-sorted DFS order over the dominance graph.

    Purpose: build the dominance graph (per pair: prefer-a majority ⇒
    (item_a, item_b) edge; prefer-b ⇒ (item_b, item_a); tie/equality ⇒
    none), then DFS with a visited set and an on-path stack — iterate
    nodes id-sorted, neighbors id-sorted — extracting the first back-edge's
    path as the cycle's directed edges (EMPTY when none).
    Refuses when: never — a cycle is STRUCTURAL, never an error (R11).
    Re-run: deterministic — the same graph yields the same named cycle.
    Touches: nothing — pure over its arguments.
    Provenance: R11 (the cycle named in the coverage data, never hidden),
    tally-brief §2 (the explicit directed-edge datum), §2/§4 (ONE cycle,
    deterministically the first in id-sorted DFS order).
    """
    adjacency = _dominance_adjacency(ids, preference)
    visited: set[str] = set()
    path: list[str] = []
    on_path: set[str] = set()

    def dfs(node: str) -> list[str]:
        """Walk id-sorted neighbors; return the cycle nodes at the first back-edge, else empty."""
        visited.add(node)
        path.append(node)
        on_path.add(node)
        for neighbor in adjacency[node]:
            if neighbor in on_path:
                return path[path.index(neighbor) :]
            if neighbor not in visited:
                cycle = dfs(neighbor)
                if cycle:
                    return cycle
        path.pop()
        on_path.discard(node)
        return []

    for start in sorted(ids):
        if start in visited:
            continue
        cycle = dfs(start)
        if cycle:
            return tuple((cycle[i], cycle[(i + 1) % len(cycle)]) for i in range(len(cycle)))
    return ()


def _found_sections(
    zero_coverage: Sequence[str],
    components: tuple[tuple[str, ...], ...],
    shortfalls: Sequence[tuple[Pair, int]],
    missing_class_pairs: Sequence[tuple[Pair, tuple[str, ...]]],
    quorum: int,
) -> str:
    """Render the SAFE HALT's found — each failing leg's section, '; '-joined.

    Purpose: the audit-honest report of ALL failing legs — leg 1's
    zero-coverage ids (sorted), leg 2's components, leg 3's under-quorum
    pairs (canonical id-sorted order, each with its weighted count), leg 4's
    uncorroborated pairs (each with its missing class names, sorted); each
    section present only when its leg fails.
    Refuses when: never — a pure rendering.
    Re-run: deterministic.
    Touches: nothing.
    Provenance: tally-brief §4 (the found bytes verbatim), the deepest-leg
    naming (the nesting made visible by the AND-reporting).
    """
    sections: list[str] = []
    if zero_coverage:
        sections.append(f"zero-coverage items: {', '.join(zero_coverage)}")
    if len(components) > 1:
        rendered = ", ".join(f"({', '.join(component)})" for component in components)
        sections.append(f"components: {rendered}")
    if shortfalls:
        rendered = ", ".join(f"({pair.item_a}, {pair.item_b}) {count} of {quorum}" for pair, count in shortfalls)
        sections.append(f"under-quorum pairs: {rendered}")
    if missing_class_pairs:
        rendered = ", ".join(
            f"({pair.item_a}, {pair.item_b}) missing {', '.join(classes)}" for pair, classes in missing_class_pairs
        )
        sections.append(f"uncorroborated pairs: {rendered}")
    return "; ".join(sections)


def _next_action_sections(
    components: tuple[tuple[str, ...], ...],
    shortfalls: Sequence[tuple[Pair, int]],
    missing_class_pairs: Sequence[tuple[Pair, tuple[str, ...]]],
    quorum: int,
) -> str:
    """Render the SAFE HALT's next_action — the two gap kinds named distinctly, '; '-joined.

    Purpose: the connectivity section when legs 1-2 fail — the spanning-tree
    bridges across components ordered by smallest id ((min C1, min C2),
    then (min of C1 and C2, min C3), …), "connectivity needs NEW comparisons"; the
    quorum section when leg 3 fails — each shortfall's missing count,
    "quorum needs MORE VOTES on existing pairs"; never conflated.
    Refuses when: never — a pure rendering.
    Re-run: deterministic.
    Touches: nothing.
    Provenance: tally-brief §4 (the closing-pairs spanning-tree rule, the
    census (f) noise-refusal), R12 (the refusal naming the closing pairs).
    """
    sections: list[str] = []
    if len(components) > 1:
        merged = set(components[0])
        bridges: list[tuple[str, str]] = []
        for component in components[1:]:
            bridges.append((min(merged), min(component)))
            merged.update(component)
        rendered = ", ".join(f"({item_a}, {item_b})" for item_a, item_b in bridges)
        sections.append(f"cast the bridging pairs: {rendered} — connectivity needs NEW comparisons")
    if shortfalls:
        rendered = ", ".join(
            f"({pair.item_a}, {pair.item_b}) needs {quorum - count} more" for pair, count in shortfalls
        )
        sections.append(f"cast the missing votes: {rendered} — quorum needs MORE VOTES on existing pairs")
    if missing_class_pairs:
        rendered = ", ".join(
            f"({pair.item_a}, {pair.item_b}) needs {', '.join(classes)}" for pair, classes in missing_class_pairs
        )
        floor_head = f"cast the corroborating votes: {rendered}"
        sections.append(f"{floor_head} — corroboration needs votes from BOTH CLASSES on existing pairs")
    return "; ".join(sections)


def _rank_groups(
    ids: Sequence[str],
    wins: Mapping[str, int],
    losses: Mapping[str, int],
    ties: Mapping[str, int],
) -> tuple[tuple[str, ...], ...]:
    """Rank by the exact-rational key — the maximal equal-score runs, ids sorted within.

    Purpose: the sort key (-Fraction(2·wins + ties, 2·comparisons), id) —
    cross-multiplied integers via stdlib Fraction, never floats (correctly-
    rounded floats can collapse mathematically-distinct rationals into a
    spurious shared group — the fragility named, foreclosed by
    construction); equal scores ⇒ ONE shared group; the (-score, id) key
    sorts ids within each group by itself.
    Refuses when: never — the gate fires before this pass (division safety:
    every scored item has comparisons ≥ 1).
    Re-run: deterministic — byte-identical groups under re-runs.
    Touches: nothing — pure over its arguments.
    Provenance: R10 (win-rate, the deterministic id tie-break), tally-brief
    §3.3-§3.4 (the score, the ruled exact comparison, the Fraction carrier),
    the census (c) ruling (cross-multiplied integers, never floats).
    """

    def score(item_id: str) -> Fraction:
        """Return the exact win fraction — (2·wins + ties)/(2·comparisons)."""
        comparisons = wins[item_id] + losses[item_id] + ties[item_id]
        numerator = _WIN_WEIGHT * wins[item_id] + _TIE_WEIGHT * ties[item_id]
        return Fraction(numerator, _WIN_WEIGHT * comparisons)

    ordered = sorted(ids, key=lambda item_id: (-score(item_id), item_id))
    groups: list[tuple[str, ...]] = []
    current: list[str] = []
    for item_id in ordered:
        if current and score(item_id) != score(current[0]):
            groups.append(tuple(current))
            current = []
        current.append(item_id)
    groups.append(tuple(current))
    return tuple(groups)


def tally_votes(manifest: RunManifest, vote_log: Sequence[VoteRecord]) -> TallyResult:
    """Tally the stored votes — the pure projection: weight → count → gate → score → rank → emit.

    Purpose: one pure function over frozen values — (1) the weighting pass
    (the run filter; the exclusion set E over cited handles, set semantics,
    no chain walk; the fork's both corrections counted, the original excluded
    once); (2) the counting pass (the weighted per-pair counts over the full
    expected universe, 0 included; the positional per-item integer
    wins/losses/ties); (3) the coverage gate BEFORE the score (leg 1
    zero-coverage, leg 2 connectivity via union-find over the ≥1-counted
    pairs, leg 3 per-pair quorum against the cited expected set, leg 4
    per-pair corroboration (F8's floor: >=1 human AND >=1 llm among the
    pair's counted votes, the policy predicate the law's one home) — the legs
    AND-composed, the refusal reporting ALL failing legs); (4) the
    exact-rational score and the maximal equal-score groups; (5) the ONE
    deterministic Condorcet cycle named in the coverage data; (6) the frozen
    TallyResult emission (the groups, the three maps, CoverageDatum with
    done=True, the version stamp).
    Refuses when: any coverage leg fails — raising TallyRefusedError (the
    SAFE HALT) with the expected/found/next_action bytes of §4, naming the
    zero-coverage items, the components with their spanning-tree bridges,
    and the under-quorum pairs with their shortfalls, the uncorroborated
    pairs with their missing classes (the two gap kinds taught distinctly:
    quorum needs MORE VOTES; corroboration needs votes from BOTH CLASSES);
    a cycle NEVER blocks
    (a Condorcet triple at full coverage is DONE with the cycle named);
    never a partial ranking dressed as whole; pair legality and verdict
    membership are CITED preconditions, never re-policed.
    Re-run: pure — same (manifest, vote_log) ⇒ byte-identical emission
    (order-independent over the multiset; no time, no environment, no
    randomness); well-defined at EVERY coverage prefix (a refusal IS a
    defined outcome).
    Touches: nothing — no store, no files, no subprocess; storage-medium-
    blind in the absolute form (no store type anywhere in the signature).
    Provenance: R10 (the tally method), R11 (the cycle policy), R12 (the
    terminal states), op 5's spec (the pure projection), G-TALLY (the five
    conditions), tally-brief §1 (the signature ruling, Option A), §3 (the
    chain, §3.5's order), §4 (the gate, the SAFE-HALT bytes); discover/tally
    and understand/tally (the legs riding the brief).
    """
    # (1) THE WEIGHTING PASS — the run filter, then the exclusion set E.
    ids = tuple(row.id for row in manifest.items)
    expected_pairs = schedule_pairs(ids)
    counted = _counted_records(manifest, vote_log)

    # (2) THE COUNTING PASS — the weighted counts, the positional mapping.
    state = _count_votes(ids, expected_pairs, counted)

    # (3) THE COVERAGE GATE — before the score (division safety).
    comparisons = {item_id: state.wins[item_id] + state.losses[item_id] + state.ties[item_id] for item_id in ids}
    zero_coverage = sorted(item_id for item_id in ids if comparisons[item_id] == 0)
    counted_pairs = [pair for pair in expected_pairs if state.pair_counts[pair] >= 1]
    components = _components(ids, counted_pairs)
    shortfalls = [
        (pair, state.pair_counts[pair]) for pair in expected_pairs if state.pair_counts[pair] < manifest.quorum
    ]
    missing_class_pairs = [
        (pair, tuple(sorted(missing_classes(state.pair_class_counts[pair]))))
        for pair in expected_pairs
        if missing_classes(state.pair_class_counts[pair])
    ]
    if zero_coverage or len(components) > 1 or shortfalls or missing_class_pairs:
        expected = (
            f"the coverage gate met: no zero-coverage item, the comparison graph connected, "
            f"every pair at quorum k={manifest.quorum} AND corroborated "
            f"(>=1 human AND >=1 llm per pair)"
        )
        raise TallyRefusedError(
            expected=expected,
            found=_found_sections(
                zero_coverage,
                components,
                shortfalls,
                missing_class_pairs,
                manifest.quorum,
            ),
            next_action=_next_action_sections(
                components,
                shortfalls,
                missing_class_pairs,
                manifest.quorum,
            ),
        )

    # (4) THE SCORE + THE RANKING — exact rationals, maximal equal-score runs.
    ranked_groups = _rank_groups(ids, state.wins, state.losses, state.ties)

    # (5) THE CYCLE — one deterministic naming, structural, never an error.
    cycle = _find_cycle(ids, state.preference)

    # (6) THE EMISSION — whole, frozen, version-stamped.
    return TallyResult(
        ranked_groups=ranked_groups,
        per_item_wins=state.wins,
        per_item_losses=state.losses,
        per_item_ties=state.ties,
        coverage=CoverageDatum(
            components=components,
            cycle=cycle,
            pair_counts=state.pair_counts,
            pair_class_counts={
                f"{pair.item_a}|{pair.item_b}": class_map for pair, class_map in state.pair_class_counts.items()
            },
            done=True,
        ),
        algorithm_version=TALLY_ALGORITHM,
    )
