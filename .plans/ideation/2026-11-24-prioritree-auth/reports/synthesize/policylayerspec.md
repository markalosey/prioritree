<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/policylayerspec

**Route:** prioritree-auth (executing) | **Events:** 14 | **Reports:** 8

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-24T18:08:48Z |
| 2 | report | togo | 2026-11-24T18:20:40Z |
| 3 | report | togo | 2026-11-24T18:21:01Z |
| 4 | report | togo | 2026-11-24T18:21:34Z |
| 5 | report | togo | 2026-11-24T18:22:02Z |
| 6 | report | togo | 2026-11-24T18:22:22Z |
| 7 | result | shinko | 2026-11-24T18:24:21Z |
| 8 | gate | shinko | 2026-11-24T18:35:22Z |
| 9 | dispatch | shinko | 2026-11-24T19:19:15Z |
| 10 | report | togo | 2026-11-24T19:22:47Z |
| 11 | dispatch | shinko | 2026-11-24T19:58:57Z |
| 12 | report | togo | 2026-11-24T20:01:54Z |
| 13 | dispatch | shinko | 2026-11-24T20:10:34Z |
| 14 | report | togo | 2026-11-24T20:15:57Z |
## Reported by togo — 2026-11-24T18:20:40Z

# THE POLICY-LAYER EXACT-TASK SPEC — togo (synthesize/policylayerspec, 2026-11-24)

## 0. THE GROUND READ WHOLE (the read-back, every file cited)

The unit brief (reports/synthesize/policy-layer.md — G-POLICY-LAYER-BRIEF approved: the five surfaces, §2's ruled semantics [the conjunction; the unconditional floor; the purity dividend], §3's arcs, §5's opens); the approved design (reports/synthesize/auth-design.md — F8 ruled in whole, §1 the grant map, §4 the build set's unit 2); tally.py WHOLE (the :1-19 fence line, :57-81 CoverageDatum, :114-142 TallyRefusedError, :145-174 the weighting pass, :177-223 the counting pass, :331-395 the renderers, :438-521 the gate + emission); key_store.py :50-58 (SCOPE_TOKENS the six tokens {register, next, cast, state, tally, manifest}; AUDIENCES; the KeyRecord :98-125); votes.py :30-72 (COMPARATOR_CLASSES :33; the VoteRecord's comparator_class stamp :69); tests/test_tally.py WHOLE (the fixtures-alone bar, the _vote helper :42-61 hardcoding "human", the twelve edges); the seven named faces read (test_session.py, test_run_store.py, test_acceptance.py, test_cli.py, test_service_acceptance.py, test_web_face.py, test_mcp_server_face.py) PLUS the read-back's own census findings — test_service_face.py :116-143, test_harness.py :47-107, test_service_store.py :143-176: three DONE-reaching arcs the brief's seven-file list MISSED (§4's ruling R9, the evidence per line); the verified-clean surfaces (test_store_lock_face.py — census/lock only, the tally never called; test_votes.py — cast-level; budget_curve.py — the pure mirror, "the core is never touched"; test_budget_curve.py — zero tally references; test_registry.py/test_scheduler.py — pre-tally); acceptance.py :84-88 + :239-281 (HARNESS_COMPARATOR_CLASS = "llm" — the harness's single-class casts, the load-bearing fact for the fixture growth); the wire's serializers (service.py :479-516, web.py :517-519, mcp_server.py :558-565, cli.py :386-393 — every coverage render NAMES its fields: the new datum field rides unserialized, additive); pyproject.toml :33-176 (ruff ALL, line-length 120, the per-file-ignores ledger, pyright strict, reportImplicitStringConcatenation = "error", enableTypeIgnoreComments = false); the floor's landed count (reports/validate/key-infrastructure.md :20 — "245 passed in 26.48s"; lint clean; pyright clean).

## 1. THE POLICY MODULE WHOLE — src/prioritree/policy.py (NEW, fenced whole)

THE IMPORT FORM RULED (the ask's own question): the map's rows are LITERALS in policy.py, the vocabulary's match pinned by test_policy.py's fork-guard arc (importing SCOPE_TOKENS there) — policy.py imports NOTHING from key_store. THE REASON: (1) the purity law — key_store pulls re/hashlib/hmac/secrets/Path (the store's machinery); the policy data layer couples to none of it; (2) the map's rows ARE data (content-in-configuration — the literals are the grant map's own content, the SCOPE_TOKENS school); (3) the drift class (a token granted but absent from SCOPE_TOKENS, or the reverse) is caught by the arc at the suite — the same guarantee an import-time check would give, without the coupling. The ONE runtime import: votes.COMPARATOR_CLASSES (the floor's required set — cited, never re-declared).

```python
# Copyright (C) 2026 Mark Losey. All rights reserved.
"""policy -- the grant map as data and the corroboration floor as data + predicate.

The policy layer (unit 2 of the auth build set): the role->scope table as
DATA (default-deny -- absence IS the denial, no explicit deny rows, the
opencode.json per-seat school) and F8's per-class quorum floor as DATA +
PREDICATE (>=1 human AND >=1 llm per pair -- the corroboration the
product's public story names, ENFORCED at the tally's coverage gate, never
marketed; the floor the product's standing policy, every run declaring it
by being a prioritree run). The Parnas fold: the two laws in ONE home,
replaceable behind their seams -- the tally the floor's consumer, the
doors the map's. The module's purity: zero runtime deps beyond the cited
vocabulary (votes.COMPARATOR_CLASSES); the scope tokens ride key_store's
SCOPE_TOKENS vocabulary as LITERALS, the match pinned by the test arc
(tests/test_policy.py -- the fork-guard), never by an import coupling
this data layer to the key store's machinery.
"""

from __future__ import annotations

from collections.abc import Mapping
from types import MappingProxyType
from typing import Final

from prioritree.votes import COMPARATOR_CLASSES

__all__ = ["ROLES", "ROLE_SCOPES", "granted_scopes", "missing_classes"]

# The roles' vocabulary (content-in-configuration): the three seats the
# grant map names -- a named module constant, never inline logic.
ROLES: Final[frozenset[str]] = frozenset({"operator", "comparator", "auditor"})

# THE GRANT MAP AS DATA (the design's three rows over the six scope tokens):
# each role's granted tokens -- literals riding key_store's SCOPE_TOKENS
# vocabulary (the match pinned by the fork-guard arc); frozenset values, the
# mapping a frozen proxy (reads only); DEFAULT-DENY: no explicit deny rows --
# a token absent from a role's row is denied that role; moho's hole closed
# (the comparator carries manifest + next -- the sitting page's consume).
ROLE_SCOPES: Final[Mapping[str, frozenset[str]]] = MappingProxyType(
    {
        "operator": frozenset({"register", "state", "tally", "manifest"}),
        "comparator": frozenset({"next", "cast", "manifest"}),
        "auditor": frozenset({"state", "tally", "manifest"}),
    }
)


def granted_scopes(role: str) -> frozenset[str]:
    """Granted scopes -- the role's scope set; the unknown role the empty set.

    Purpose: the pure lookup over the grant map -- the known role returns
    its frozen scope set; the unknown role returns the EMPTY SET
    (default-deny's datum: absence IS the denial, the empty set denies
    every token by construction, the door's check `token in
    granted_scopes(role)` total and exception-free at every route).
    Refuses when: never -- the denial is DATA, never a raised grammar; the
    door's own 403 lane carries the teaching ThreePart at the tier.
    Re-run: deterministic -- a pure read over frozen data.
    Touches: nothing -- pure over its argument.
    Provenance: the auth design brief §1 (the grant map as data), the
    policy-layer unit brief §1.1 (the default-deny discipline), the
    exact-task spec synthesize/policylayerspec §1 (this fence).
    """
    return ROLE_SCOPES.get(role, frozenset())


def missing_classes(class_counts: Mapping[str, int]) -> frozenset[str]:
    """Missing classes -- the required classes a pair's counted rollup lacks.

    Purpose: F8's per-class quorum floor as a pure predicate -- the
    corroboration law (>=1 human AND >=1 llm) over one pair's per-class
    counted-vote rollup (the weighted set's own accumulation: the run
    filter and the exclusion set E already applied upstream -- a
    superseded vote's class never corroborates); the missing set = the
    vocabulary minus the classes with count >= 1; EMPTY when the pair
    corroborates (the gate's pass form).
    Refuses when: never -- a pure predicate; the HALT is the tally gate's
    own act (TallyRefusedError there, never a second grammar here); class
    vocabulary membership a CITED PRECONDITION (cast_vote's write gate the
    authority, never re-policed).
    Re-run: deterministic -- a pure set difference over frozen data.
    Touches: nothing -- pure over its argument.
    Provenance: the auth design brief §1 (F8 ruled in), the policy-layer
    unit brief §1.1 (the law in ONE home) and §2a (the conjunction), the
    exact-task spec synthesize/policylayerspec §1 (this fence).
    """
    return COMPARATOR_CLASSES - {cls for cls, count in class_counts.items() if count >= 1}
```

THE FOUR COMPONENTS RULED: (1) THE GRANT MAP AS DATA — the three rows verbatim above (operator {register, state, tally, manifest}; comparator {next, cast, manifest}; auditor {state, tally, manifest}); default-deny (absence IS the denial, no deny rows); frozen form (frozenset values, MappingProxyType — reads only, the write raises TypeError). (2) THE SCOPE LOOKUP — granted_scopes: the known role -> its set; THE UNKNOWN ROLE -> THE EMPTY SET (the ask's own bytes; the brief's N818 typed-refusal proposal SUPERSEDED — §4's ruling R1). (3) THE FLOOR'S CHECKER — missing_classes over the per-pair class COUNTS (the rollup), never the records: the one-pass ruling (the brief §1.2 — "one pass, no second traversal"); the >=1 law lives IN the predicate, not the caller; the required set CITED from votes.COMPARATOR_CLASSES (imported and iterated — never re-declared). (4) THE FLOOR'S REFUSAL DATA — the missing-class pairs as `list[tuple[Pair, tuple[str, ...]]]` at the GATE (the datum's own school: the shortfalls' list-comprehension idiom at :488-490, expected-pairs order, the class names sorted within — sorted(COMPARATOR_CLASSES) renders "human, llm"); the aggregation the gate's own (like shortfalls), the law the module's.

[the spec's continuation — piece 2: §2 the tally's seam regions]
## Reported by togo — 2026-11-24T18:21:01Z

[the spec's continuation — piece 2: §2 the tally's seam regions]

## 2. THE TALLY'S SEAM REGIONS — the five regions, exact before/after

THE SIGNATURE UNCHANGED (:438): `tally_votes(manifest: RunManifest, vote_log: Sequence[VoteRecord]) -> TallyResult` — byte-standing (the purity dividend, §4).

### (a) THE FENCE LINE (:15-19 + the import block :27)

BEFORE (:15-19, the docstring's fence paragraph + the closing quotes):
```python
The fence (the must-not-know, held by construction): no scheduling strategy
(the expected pair SET cited as data), no comparator identity (R5's stamps
never read into scoring), no storage medium (no store type anywhere); NO
datetime — purity's negative space (no time, no environment, no randomness).
"""
```
AFTER (the fence paragraph grown — the brief §2f's amendment; the new bytes parenthesized, never dashed; the untouched em dash stands):
```python
The fence (the must-not-know, held by construction): no scheduling strategy
(the expected pair SET cited as data), no comparator identity (R5's stamps
never read into scoring; the CLASS stamp read at the coverage GATE alone --
F8's corroboration floor, the identity never read at all; the fence line's
own amendment), no storage medium (no store type anywhere); NO
datetime — purity's negative space (no time, no environment, no randomness).
"""
```
AND the runtime imports (:27 grown — isort order; COMPARATOR_CLASSES rides RUNTIME for the counting pass's initialization; VoteRecord stays TYPE_CHECKING; no cycle — votes imports neither policy nor tally):
```python
from prioritree.policy import missing_classes
from prioritree.scheduler import schedule_pairs
from prioritree.votes import COMPARATOR_CLASSES
```

### (b) THE DATUM (:57-81)

BEFORE (:78-81):
```python
    components: tuple[tuple[str, ...], ...]
    cycle: tuple[tuple[str, str], ...]
    pair_counts: Mapping[Pair, int]
    done: bool
```
AFTER (the new field after pair_counts — the per-pair {human, llm} counts, the inner mapping keyed by class name):
```python
    components: tuple[tuple[str, ...], ...]
    cycle: tuple[tuple[str, str], ...]
    pair_counts: Mapping[Pair, int]
    pair_class_counts: Mapping[Pair, Mapping[str, int]]
    done: bool
```
AND the docstring's Purpose grown (after the weighted-counts clause): "the WEIGHTED per-pair per-CLASS counted votes over the same full universe (every vocabulary class present, 0 included -- the corroboration named in the coverage data, never hidden; R11's discipline extended to F8's floor)".

### (c) THE COUNTING PASS (:145-223)

BEFORE (:145-153, the accumulator):
```python
@dataclass(frozen=True)
class _Counted:
    """_Counted — the counting pass's private accumulation state."""

    pair_counts: dict[Pair, int]
    wins: dict[str, int]
    losses: dict[str, int]
    ties: dict[str, int]
    preference: dict[Pair, tuple[int, int]]
```
AFTER (the field second):
```python
@dataclass(frozen=True)
class _Counted:
    """_Counted — the counting pass's private accumulation state."""

    pair_counts: dict[Pair, int]
    pair_class_counts: dict[Pair, dict[str, int]]
    wins: dict[str, int]
    losses: dict[str, int]
    ties: dict[str, int]
    preference: dict[Pair, tuple[int, int]]
```
BEFORE (:198-204, the init + the loop's head):
```python
    pair_counts: dict[Pair, int] = dict.fromkeys(expected_pairs, 0)
    preference: dict[Pair, tuple[int, int]] = dict.fromkeys(expected_pairs, (0, 0))
    wins: dict[str, int] = dict.fromkeys(ids, 0)
    losses: dict[str, int] = dict.fromkeys(ids, 0)
    ties: dict[str, int] = dict.fromkeys(ids, 0)
    for record in counted:
        pair_counts[record.pair] += 1
```
AFTER (the class accumulation in the SAME pass — the record already in hand, one pass, no second traversal; the direct index safe under the cited precondition — the class vocabulary-checked at cast_vote :379-389):
```python
    pair_counts: dict[Pair, int] = dict.fromkeys(expected_pairs, 0)
    pair_class_counts: dict[Pair, dict[str, int]] = {
        pair: dict.fromkeys(COMPARATOR_CLASSES, 0) for pair in expected_pairs
    }
    preference: dict[Pair, tuple[int, int]] = dict.fromkeys(expected_pairs, (0, 0))
    wins: dict[str, int] = dict.fromkeys(ids, 0)
    losses: dict[str, int] = dict.fromkeys(ids, 0)
    ties: dict[str, int] = dict.fromkeys(ids, 0)
    for record in counted:
        pair_counts[record.pair] += 1
        pair_class_counts[record.pair][record.comparator_class] += 1
```
AND the return (:217-223) gains `pair_class_counts=pair_class_counts,` (second argument); AND the docstring's Purpose grows (after the dominance-graph clause): "and the per-pair per-CLASS counts (the corroboration floor's rollup -- every vocabulary class 0 included, the CLASS STAMP accumulated in this same one pass, the identity never read)".

### (d) THE GATE (:481-500) + tally_votes' docstring (:438-472) + the emission (:514-519)

BEFORE (:488-500):
```python
    shortfalls = [
        (pair, state.pair_counts[pair]) for pair in expected_pairs if state.pair_counts[pair] < manifest.quorum
    ]
    if zero_coverage or len(components) > 1 or shortfalls:
        expected = (
            f"the coverage gate met: no zero-coverage item, the comparison graph connected, "
            f"every pair at quorum k={manifest.quorum}"
        )
        raise TallyRefusedError(
            expected=expected,
            found=_found_sections(zero_coverage, components, shortfalls, manifest.quorum),
            next_action=_next_action_sections(components, shortfalls, manifest.quorum),
        )
```
AFTER (the fourth conjunct — the missing-class pairs from the policy predicate, the conjunction's condition line, the expected's FULL conjunction, the renderers' grown signatures):
```python
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
                zero_coverage, components, shortfalls, missing_class_pairs, manifest.quorum
            ),
            next_action=_next_action_sections(
                components, shortfalls, missing_class_pairs, manifest.quorum
            ),
        )
```
(The double call of the pure predicate in the comprehension: the shortfalls' parallel form — the set difference over at most two classes, the cost zero. The expected's multi-line paren f-string: the file's own :492-495 idiom — §4's ruling R8.)
AND tally_votes' docstring grows: the Purpose's (3) after "leg 3 per-pair quorum against the cited expected set" -> ", leg 4 per-pair corroboration (F8's floor: >=1 human AND >=1 llm among the pair's counted votes, the policy predicate the law's one home)"; the Refuses-when after "the under-quorum pairs with their shortfalls" -> ", the uncorroborated pairs with their missing classes (the two gap kinds taught distinctly: quorum needs MORE VOTES; corroboration needs votes from BOTH CLASSES)". AND the emission (:514-519): the CoverageDatum construction gains `pair_class_counts=state.pair_class_counts,` after pair_counts.

### (e) THE RENDERERS (:331-395)

_found_sections — BEFORE (:331-336 + :355-360):
```python
def _found_sections(
    zero_coverage: Sequence[str],
    components: tuple[tuple[str, ...], ...],
    shortfalls: Sequence[tuple[Pair, int]],
    quorum: int,
) -> str:
```
```python
    if shortfalls:
        rendered = ", ".join(
            f"({pair.item_a}, {pair.item_b}) {count} of {quorum}" for pair, count in shortfalls
        )
        sections.append(f"under-quorum pairs: {rendered}")
    return "; ".join(sections)
```
AFTER (the signature gains the leg-4 parameter; the section after leg 3 — the legs' order; the docstring's Purpose grows "leg 4's uncorroborated pairs (each with its missing class names, sorted)"):
```python
def _found_sections(
    zero_coverage: Sequence[str],
    components: tuple[tuple[str, ...], ...],
    shortfalls: Sequence[tuple[Pair, int]],
    missing_class_pairs: Sequence[tuple[Pair, tuple[str, ...]]],
    quorum: int,
) -> str:
```
```python
    if shortfalls:
        rendered = ", ".join(
            f"({pair.item_a}, {pair.item_b}) {count} of {quorum}" for pair, count in shortfalls
        )
        sections.append(f"under-quorum pairs: {rendered}")
    if missing_class_pairs:
        rendered = ", ".join(
            f"({pair.item_a}, {pair.item_b}) missing {', '.join(classes)}"
            for pair, classes in missing_class_pairs
        )
        sections.append(f"uncorroborated pairs: {rendered}")
    return "; ".join(sections)
```
_next_action_sections — BEFORE (:363-367 + :390-395):
```python
def _next_action_sections(
    components: tuple[tuple[str, ...], ...],
    shortfalls: Sequence[tuple[Pair, int]],
    quorum: int,
) -> str:
```
```python
    if shortfalls:
        rendered = ", ".join(
            f"({pair.item_a}, {pair.item_b}) needs {quorum - count} more" for pair, count in shortfalls
        )
        sections.append(f"cast the missing votes: {rendered} — quorum needs MORE VOTES on existing pairs")
    return "; ".join(sections)
```
AFTER (the floor's cure — the two gap kinds DISTINCT, never conflated; the ONE em dash matches the field's own grammar at :389/:394 — §4's ruling R6):
```python
def _next_action_sections(
    components: tuple[tuple[str, ...], ...],
    shortfalls: Sequence[tuple[Pair, int]],
    missing_class_pairs: Sequence[tuple[Pair, tuple[str, ...]]],
    quorum: int,
) -> str:
```
```python
    if shortfalls:
        rendered = ", ".join(
            f"({pair.item_a}, {pair.item_b}) needs {quorum - count} more" for pair, count in shortfalls
        )
        sections.append(f"cast the missing votes: {rendered} — quorum needs MORE VOTES on existing pairs")
    if missing_class_pairs:
        rendered = ", ".join(
            f"({pair.item_a}, {pair.item_b}) needs {', '.join(classes)}"
            for pair, classes in missing_class_pairs
        )
        floor_head = f"cast the corroborating votes: {rendered}"
        sections.append(f"{floor_head} — corroboration needs votes from BOTH CLASSES on existing pairs")
    return "; ".join(sections)
```
THE RENDERED BYTES, one worked whole (a k=1 3-item run, one human vote on (a,b)): found = "zero-coverage items: c; components: (a, b), (c); under-quorum pairs: (a, c) 0 of 1, (b, c) 0 of 1; uncorroborated pairs: (a, b) missing llm, (a, c) missing human, llm, (b, c) missing human, llm" — a pair failing both legs carries in BOTH sections (each leg's own truth, the brief §2d). next_action = "cast the bridging pairs: (a, c) — connectivity needs NEW comparisons; cast the missing votes: (a, c) needs 1 more, (b, c) needs 1 more — quorum needs MORE VOTES on existing pairs; cast the corroborating votes: (a, b) needs llm, (a, c) needs human, llm, (b, c) needs human, llm — corroboration needs votes from BOTH CLASSES on existing pairs". THE TIERS RIDE THE BYTES VERBATIM (service.py :511-512 render_refusal; web.py's honest 409; cli.py :486 the exit-1 render; mcp_server's halt shaper within the K=10 cap) — the fence's dividend, zero tier edits.

[the spec's continuation — piece 3: §3 the test files]
## Reported by togo — 2026-11-24T18:21:34Z

[the spec's continuation — piece 3: §3a + §3b the core test files]

## 3. THE TEST FILES

### 3a. tests/test_policy.py (NEW — fenced whole, 10 arcs; the fixtures-alone bar, zero store imports beyond the fork-guard's SCOPE_TOKENS pin)

```python
# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The policy unit's edge tests -- the grant map's arcs + the floor predicate's arcs.

The fixtures-alone bar (the suite-wide discipline): every arc asserts over
the module's own constants and predicates directly. The ONE import beyond
the module under test is key_store's SCOPE_TOKENS -- the fork-guard arc's
own pin (the map's rows are literals; the suite catches the drift).
"""

from typing import cast

import pytest

from prioritree.key_store import SCOPE_TOKENS
from prioritree.policy import ROLES, ROLE_SCOPES, granted_scopes, missing_classes
from prioritree.votes import COMPARATOR_CLASSES


def test_grant_map_rows_exact() -> None:
    """The three rows byte-exact -- the design's grant map, default-deny's named allows."""
    assert ROLE_SCOPES["operator"] == frozenset({"register", "state", "tally", "manifest"})
    assert ROLE_SCOPES["comparator"] == frozenset({"next", "cast", "manifest"})
    assert ROLE_SCOPES["auditor"] == frozenset({"state", "tally", "manifest"})


def test_granted_tokens_pin_scope_tokens() -> None:
    """The fork-guard: every granted token rides key_store's SCOPE_TOKENS -- the drift caught here."""
    granted = set().union(*ROLE_SCOPES.values())
    assert granted <= SCOPE_TOKENS


def test_roles_vocabulary_exactly_three() -> None:
    """The roles' vocabulary: three names, no fourth -- the map's keys exactly the vocabulary."""
    assert ROLES == frozenset({"operator", "comparator", "auditor"})
    assert set(ROLE_SCOPES) == ROLES


def test_grant_map_frozen_data_form() -> None:
    """The frozen-data form: frozenset values, the read-only mapping -- the write refused at runtime."""
    assert all(isinstance(scopes, frozenset) for scopes in ROLE_SCOPES.values())
    with pytest.raises(TypeError):
        cast("dict[str, frozenset[str]]", ROLE_SCOPES)["operator"] = frozenset()


def test_default_deny_absence_is_the_denial() -> None:
    """Absence IS the denial: the auditor's absent cast, the comparator's absent register and tally."""
    assert "cast" not in granted_scopes("auditor")
    assert "register" not in granted_scopes("comparator")
    assert "tally" not in granted_scopes("comparator")


def test_unknown_role_denied_whole() -> None:
    """The unknown role returns the empty set -- default-deny's datum, every token denied by construction."""
    assert granted_scopes("robot") == frozenset()
    assert granted_scopes("") == frozenset()
    assert not (SCOPE_TOKENS & granted_scopes("robot"))


def test_comparator_manifest_hole_closed() -> None:
    """Moho's hole closed: the comparator carries manifest AND next -- the sitting page's consume."""
    assert "manifest" in granted_scopes("comparator")
    assert "next" in granted_scopes("comparator")


def test_missing_classes_both_present_empty() -> None:
    """Both classes counted -> nothing missing: the floor's pass form."""
    assert missing_classes({"human": 1, "llm": 1}) == frozenset()
    assert missing_classes({"human": 3, "llm": 2}) == frozenset()


def test_missing_classes_names_the_absent_class() -> None:
    """The single-class rollup names its absent class; the empty rollup names the whole vocabulary."""
    assert missing_classes({"human": 2}) == frozenset({"llm"})
    assert missing_classes({"llm": 1}) == frozenset({"human"})
    assert missing_classes({}) == COMPARATOR_CLASSES


def test_missing_classes_zero_count_not_present() -> None:
    """The >=1 law: a zero count does not corroborate -- the class named despite the key present."""
    assert missing_classes({"human": 0, "llm": 3}) == frozenset({"human"})
```

### 3b. tests/test_tally.py (GROWN — the _vote helper, 13 new arcs, the existing arcs' exact updates)

THE _vote HELPER AFTER (:42-61 — the class parameter keyword-only, DEFAULT "human": every existing arc byte-unchanged):
```python
def _vote(
    vote_id: str,
    pair: Pair,
    winner: str,
    *,
    comparator_class: str = "human",
    notes: str | None = None,
    supersedes: str | None = None,
) -> VoteRecord:
    """Build one frozen vote record -- fixtures only, no store anywhere."""
    return VoteRecord(
        vote_id=vote_id,
        run_id=_RUN_ID,
        pair=pair,
        winner=winner,
        comparator_id="x",
        comparator_class=comparator_class,
        recorded_at=_STAMP,
        notes=notes,
        supersedes=supersedes,
    )
```
THE NEW ARCS (13 — 9 floor + 4 grammar; the import line :17 unchanged, the `dataclasses` import already at :10 rides the stamp arc):
```python
def test_floor_both_classes_pass_done() -> None:
    """k=1 with one human AND one llm per pair -> DONE: the corroboration floor's pass form."""
    manifest = _manifest(["a", "b", "c"])
    votes = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _AB_PAIR, PREFER_A, comparator_class="llm"),
        _vote("VOTE-0003", _AC_PAIR, PREFER_A),
        _vote("VOTE-0004", _AC_PAIR, PREFER_A, comparator_class="llm"),
        _vote("VOTE-0005", _BC_PAIR, PREFER_A),
        _vote("VOTE-0006", _BC_PAIR, PREFER_A, comparator_class="llm"),
    )
    result = tally_votes(manifest, votes)
    assert result.coverage.done is True
    assert result.ranked_groups == (("a",), ("b",), ("c",))
    assert result.per_item_wins == {"a": 4, "b": 2, "c": 0}
    assert result.coverage.pair_counts == {_AB_PAIR: 2, _AC_PAIR: 2, _BC_PAIR: 2}


def test_floor_human_only_halt_names_missing_llm() -> None:
    """Quorum met, all human -> the halt's found names the missing llm; the quorum section absent."""
    manifest = _manifest(["a", "b"])
    votes = (_vote("VOTE-0001", _AB_PAIR, PREFER_A),)
    with pytest.raises(TallyRefusedError) as exc_info:
        tally_votes(manifest, votes)
    assert exc_info.value.found == "uncorroborated pairs: (a, b) missing llm"
    assert "under-quorum" not in exc_info.value.found
    assert exc_info.value.next_action == (
        "cast the corroborating votes: (a, b) needs llm"
        " — corroboration needs votes from BOTH CLASSES on existing pairs"
    )


def test_floor_llm_only_halt_names_missing_human() -> None:
    """The mirror: quorum met, all llm -> the found names the missing human."""
    manifest = _manifest(["a", "b"])
    votes = (_vote("VOTE-0001", _AB_PAIR, PREFER_A, comparator_class="llm"),)
    with pytest.raises(TallyRefusedError) as exc_info:
        tally_votes(manifest, votes)
    assert exc_info.value.found == "uncorroborated pairs: (a, b) missing human"


def test_floor_conjunction_k2_two_human_zero_llm() -> None:
    """k=2 with 2 human 0 llm on the pair: the quorum leg passes, the floor fails -- never an OR."""
    manifest = _manifest(["a", "b", "c"], quorum=2)
    votes = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _AB_PAIR, PREFER_A),
        _vote("VOTE-0003", _AC_PAIR, PREFER_A, comparator_class="llm"),
        _vote("VOTE-0004", _AC_PAIR, PREFER_A),
        _vote("VOTE-0005", _BC_PAIR, PREFER_A, comparator_class="llm"),
        _vote("VOTE-0006", _BC_PAIR, PREFER_A),
    )
    with pytest.raises(TallyRefusedError) as exc_info:
        tally_votes(manifest, votes)
    assert exc_info.value.found == "uncorroborated pairs: (a, b) missing llm"
    assert "under-quorum" not in exc_info.value.found


def test_floor_superseded_class_does_not_corroborate() -> None:
    """A SUPERSEDED human vote's class does not corroborate: the floor rides the weighted set."""
    manifest = _manifest(["a", "b"])
    votes = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _AB_PAIR, PREFER_B, comparator_class="llm", supersedes="VOTE-0001"),
    )
    with pytest.raises(TallyRefusedError) as exc_info:
        tally_votes(manifest, votes)
    assert exc_info.value.found == "uncorroborated pairs: (a, b) missing human"


def test_floor_stamp_not_identity() -> None:
    """The class from the STAMPS, never the identity: one id both classes passes; two ids one class halts."""
    manifest = _manifest(["a", "b"])
    one_id = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _AB_PAIR, PREFER_A, comparator_class="llm"),
    )
    assert tally_votes(manifest, one_id).coverage.done is True
    two_ids = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        dataclasses.replace(_vote("VOTE-0002", _AB_PAIR, PREFER_A), comparator_id="y"),
    )
    with pytest.raises(TallyRefusedError) as exc_info:
        tally_votes(manifest, two_ids)
    assert exc_info.value.found == "uncorroborated pairs: (a, b) missing llm"


def test_floor_zero_vote_pair_names_both_classes() -> None:
    """The 0-vote pair: both classes named -- the empty counts' truth, in the legs' own sections."""
    manifest = _manifest(["a", "b", "c"])
    votes = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _AB_PAIR, PREFER_A, comparator_class="llm"),
    )
    with pytest.raises(TallyRefusedError) as exc_info:
        tally_votes(manifest, votes)
    assert "under-quorum pairs: (a, c) 0 of 1, (b, c) 0 of 1" in exc_info.value.found
    assert (
        "uncorroborated pairs: (a, c) missing human, llm, (b, c) missing human, llm"
        in exc_info.value.found
    )


def test_datum_pair_class_counts_named_at_done() -> None:
    """The datum's pair_class_counts: the corroboration named in the coverage data, never hidden."""
    manifest = _manifest(["a", "b"])
    votes = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _AB_PAIR, PREFER_A, comparator_class="llm"),
    )
    result = tally_votes(manifest, votes)
    assert result.coverage.pair_class_counts == {_AB_PAIR: {"human": 1, "llm": 1}}


def test_floor_purity_permuted_multiset_with_class_mix() -> None:
    """The same class-mixed multiset in two cast orders tallies byte-identical -- the purity holds."""
    manifest = _manifest(["a", "b", "c"])
    forward = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _AB_PAIR, PREFER_B, comparator_class="llm"),
        _vote("VOTE-0003", _AC_PAIR, TIE),
        _vote("VOTE-0004", _AC_PAIR, TIE, comparator_class="llm"),
        _vote("VOTE-0005", _BC_PAIR, PREFER_A),
        _vote("VOTE-0006", _BC_PAIR, PREFER_B, comparator_class="llm"),
    )
    backward = tuple(reversed(forward))
    assert tally_votes(manifest, backward) == tally_votes(manifest, forward)


def test_halt_found_names_both_cures() -> None:
    """One run, both gap kinds: an at-quorum-human-only pair AND an under-quorum pair -> both sections."""
    manifest = _manifest(["a", "b", "c"])
    votes = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _AC_PAIR, PREFER_A),
    )
    with pytest.raises(TallyRefusedError) as exc_info:
        tally_votes(manifest, votes)
    assert "under-quorum pairs: (b, c) 0 of 1" in exc_info.value.found
    assert (
        "uncorroborated pairs: (a, b) missing llm, (a, c) missing llm, (b, c) missing human, llm"
        in exc_info.value.found
    )


def test_halt_expected_names_full_conjunction() -> None:
    """The expected names the FULL conjunction: quorum AND corroboration -- the gate's one meaning."""
    manifest = _manifest(["a", "b"])
    votes = (_vote("VOTE-0001", _AB_PAIR, PREFER_A),)
    with pytest.raises(TallyRefusedError) as exc_info:
        tally_votes(manifest, votes)
    assert exc_info.value.expected == (
        "the coverage gate met: no zero-coverage item, the comparison graph connected, "
        "every pair at quorum k=1 AND corroborated (>=1 human AND >=1 llm per pair)"
    )


def test_halt_next_action_two_cures_distinct() -> None:
    """The two gap kinds taught distinctly: MORE VOTES vs BOTH CLASSES -- never conflated."""
    manifest = _manifest(["a", "b", "c"])
    votes = (
        _vote("VOTE-0001", _AB_PAIR, PREFER_A),
        _vote("VOTE-0002", _AC_PAIR, PREFER_A),
    )
    with pytest.raises(TallyRefusedError) as exc_info:
        tally_votes(manifest, votes)
    assert "quorum needs MORE VOTES on existing pairs" in exc_info.value.next_action
    assert "corroboration needs votes from BOTH CLASSES on existing pairs" in exc_info.value.next_action
    assert exc_info.value.next_action.startswith("cast the bridging pairs")


def test_refusal_three_fields_same_type() -> None:
    """ONE refusal type at the halt: TallyRefusedError's three fields together, no new exception."""
    manifest = _manifest(["a", "b"])
    votes = (_vote("VOTE-0001", _AB_PAIR, PREFER_A),)
    with pytest.raises(TallyRefusedError) as exc_info:
        tally_votes(manifest, votes)
    refusal = exc_info.value
    assert (refusal.found, refusal.next_action) == (
        "uncorroborated pairs: (a, b) missing llm",
        "cast the corroborating votes: (a, b) needs llm"
        " — corroboration needs votes from BOTH CLASSES on existing pairs",
    )
    assert refusal.expected.startswith("the coverage gate met")
```
THE EXISTING ARCS' EXACT UPDATES (the floor's honest cost in this file): (1) `_perfect_order_votes` grows to 12 votes (each pair's human vote + its llm twin, prefer-a throughout, VOTE-0001..0012); `test_hand_computed_known_answer_full_emission` asserts wins {"a": 6, "b": 4, "c": 2, "d": 0}, losses {"a": 0, "b": 2, "c": 4, "d": 6}, ties all 0, pair_counts each pair 2, PLUS `result.coverage.pair_class_counts == {_AB_PAIR: {"human": 1, "llm": 1}, ...}` for all six pairs — ranked_groups (("a",), ("b",), ("c",), ("d",)) UNCHANGED. (2) `test_every_coverage_prefix_defined` — the script grows to 6 votes (each pair human then llm, same verdicts as _SCRIPT); the found bytes re-derive per prefix: [:0] found = "zero-coverage items: a, b, c; components: (a), (b), (c); under-quorum pairs: (a, b) 0 of 1, (a, c) 0 of 1, (b, c) 0 of 1; uncorroborated pairs: (a, b) missing human, llm, (a, c) missing human, llm, (b, c) missing human, llm"; [:1] found = "zero-coverage items: c; components: (a, b), (c); under-quorum pairs: (a, c) 0 of 1, (b, c) 0 of 1; uncorroborated pairs: (a, b) missing llm, (a, c) missing human, llm, (b, c) missing human, llm"; [:2] found = "zero-coverage items: c; components: (a, b), (c); under-quorum pairs: (a, c) 0 of 1, (b, c) 0 of 1; uncorroborated pairs: (a, c) missing human, llm, (b, c) missing human, llm"; [:3] found = "under-quorum pairs: (b, c) 0 of 1; uncorroborated pairs: (a, c) missing llm, (b, c) missing human, llm"; [:4] found = "under-quorum pairs: (b, c) 0 of 1; uncorroborated pairs: (b, c) missing human, llm"; [:5] found = "uncorroborated pairs: (b, c) missing llm"; [:6] DONE (isinstance tuple). (3) `test_cycle_structural_named_done` — the three votes each grow their llm twin (same verdicts): wins/losses {"a": 2, "b": 2, "c": 2}, ties 0, pair_counts each 2; the cycle set UNCHANGED. (4) `test_tie_break_exact_integer_grouping` — each of the six votes grows its llm twin (same verdicts): the groups UNCHANGED (("a", "b"), ("c", "d") / the singles). (5) `test_no_score_field_consumption` — the single tie vote grows its llm twin: per_item_ties {"a": 2, "b": 2}. (6) `test_supersession_weighting_chain_and_fork` — the correction case grows a third vote `_vote("VOTE-0003", _AB_PAIR, PREFER_B)` (human, plain) so the counted set corroborates (asserts wins {"a": 0, "b": 2}, losses {"a": 2, "b": 0}, pair_counts {_AB_PAIR: 2}); the chain case grows a fourth plain vote `_vote("VOTE-0004", _AB_PAIR, TIE, comparator_class="llm")` (asserts ties {"a": 2, "b": 2}, wins all 0); the fork case: VOTE-0005's class byte human -> llm (the second correction's own stamp) — the asserted wins/losses {"a": 1, "b": 1} and pair_counts {_AB_PAIR: 2} STAND; the k=2 halt case STANDS (its "(a, b) 1 of 2" substring intact). (7) `test_isolation_and_connectivity_legs_named` — the empty-run exact found grows the trailing section: "; uncorroborated pairs: (a, b) missing human, llm, (a, c) missing human, llm, (b, c) missing human, llm"; the other substring assertions STAND. (8) `test_quorum_leg_safe_halt_names_shortfall` and `test_weighted_vs_census_seam` — UNCHANGED (their substring needles hold under the grown found; the halt's intent — the quorum leg named — intact). (9) `test_purity_permuted_multiset_byte_identical` and `test_version_stamp_constant_and_byte_identical_rerun` — ride the grown _perfect_order_votes, UNCHANGED.

[the spec's continuation — piece 4: §3c the DONE-reaching fixtures' class-mix growth]
## Reported by togo — 2026-11-24T18:22:02Z

[the spec's continuation — piece 4: §3c the DONE-reaching fixtures' class-mix growth]

### 3c. THE DONE-REACHING FIXTURES' CLASS-MIX GROWTH (per file, the exact grows; every DONE-reaching arc still DONE; the asserted outcomes stand — the counts' bytes grow where the mix doubles them)

**tests/test_session.py** — 3 arcs grow: (1) `test_end_to_end_fixture_register_vote_done_tally` (:44-70): each of the three casts grows its corroborating vote (the same winner, class llm, comparator_id "x") -> 6 casts; the emission asserts UPDATE: per_item_wins {"a": 4, "b": 0, "c": 0}, per_item_losses {"a": 0, "b": 2, "c": 2}, per_item_ties {"a": 0, "b": 2, "c": 2}, pair_counts {_AB_PAIR: 2, _AC_PAIR: 2, _BC_PAIR: 2}; ranked_groups (("a",), ("b", "c")) and components UNCHANGED. (2) `test_prefix_tally_well_defined_every_coverage_point` (:102-112): the loop's body grows -- each iteration casts the pair's human vote then its llm vote (same winner) before the suppressed tally; the final assertion stands. (3) `test_five_ops_present_and_wired` (:115-131): after the read_vote_state assertions, BEFORE tally_rank, the corroborating cast lands: `session.cast_vote(run_id, ("a", "b"), "prefer-a", comparator_id="x", comparator_class="llm")`; the ranked_groups (("a",), ("b",)) STANDS. UNCHANGED (verified): `test_seam_divergence_next_pair_done_tally_safe_halt` (the halt's "(a, b) 1 of 2" needle intact), `_cast_all` + `test_done_signal_caught_by_type_three_fields` (the queue census-keyed, no tally claim), the register-refusal/unknown-run/zero-vote/quorum-two arcs.

**tests/test_run_store.py** — 2 arcs grow: (1) `test_round_trip_clock_free_surface_equal` (:46-73): three corroborating casts appended AFTER the correction (ids VOTE-0005..0007): `store.cast(("a", "b"), "prefer-a", comparator_id="y", comparator_class="llm")`, `store.cast(("a", "c"), "prefer-b", comparator_id="z", comparator_class="human")`, `store.cast(("b", "c"), "tie", comparator_id="w", comparator_class="llm")` -> the weighted set corroborates on all three pairs; every assertion is a before/after EQUALITY -> STANDS. (2) `test_supersede_replay_correction_rides_the_trip` (:180-197): the same three corroborating casts appended after VOTE-0004 (ids VOTE-0005..0007); log[1] remains the correction (VOTE-0002) -> every assertion STANDS.

**src/prioritree/acceptance.py** (test_acceptance.py's builder — THE HARNESS GROW, §4's ruling R5) — 2 regions: (1) the stamp block :84-88: `HARNESS_COMPARATOR_CLASS: str = "llm"` RETIRED, replaced by `HARNESS_JUDGE_CLASSES: Final[tuple[str, ...]] = tuple(sorted(COMPARATOR_CLASSES))` with the import `from prioritree.votes import COMPARATOR_CLASSES` grown at the runtime import block; the block's comment rewritten: the judge's class the parity over the ruled set (the corroboration floor's mix at the harness — the floor's honest cost grown here, the seeds' determinism unchanged). (2) the cast :261-267: `comparator_class=HARNESS_COMPARATOR_CLASS,` -> `comparator_class=HARNESS_JUDGE_CLASSES[pair_count % len(HARNESS_JUDGE_CLASSES)],` (judge 1 human, judge 2 llm, judge 3 human at k=3 -> every pair corroborated; the class derives from the deterministic census count — NO RNG draw consumed, the replay byte-identical). test_acceptance.py BYTE-UNCHANGED (every arc rides accept_run; the class stamps never asserted).

**tests/test_cli.py** — the `_cast` helper (:61-64) gains the class parameter: `def _cast(tmp_path: Path, item_a: str, item_b: str, winner: str, comparator_class: str = _HUMAN) -> None:` with the argv's `_HUMAN` -> `comparator_class`; a `_LLM = "llm"` constant joins the block; `_drive_abc_to_coverage` (:67-72) grows: each pair cast twice (`_cast(tmp_path, "a", "b", _PREFER_A)` then `_cast(tmp_path, "a", "b", _PREFER_A, _LLM)` — likewise a-c and b-c) -> 6 casts; `_TALLY_ABC` (:40-52) UPDATES: "counts\ta\t4\t0\t0", "counts\tb\t2\t2\t0", "counts\tc\t0\t4\t0", "coverage\t1\tTrue", "pairs\ta\tb\t2", "pairs\ta\tc\t2", "pairs\tb\tc\t2", the rank and version lines UNCHANGED. UNCHANGED (verified): `test_done_exhausted_line_at_zero` (the queue census-keyed), the refusal parametrize's "tally-undercovered" needle "at quorum" (intact in the grown expected), `test_ack_loud_dedup_count_unchanged`, the argparse/seed/home arcs.

**tests/test_service_store.py** — THE TENTH FACE (the brief's miss, §4's R9): `test_serial_equivalence_seam_transparent` (:143-176): the `acts` tuple (:145-149) grows to 6 acts — each pair's human act joined by its llm twin: `(("a", "b"), "prefer-a", "x", "human")` + `(("a", "b"), "prefer-a", "x", "llm")`, `(("a", "c"), "prefer-a", "y", "llm")` + `(("a", "c"), "prefer-a", "y", "human")`, `(("b", "c"), "prefer-a", "z", "human")` + `(("b", "c"), "prefer-a", "z", "llm")` — both arms replay the same 6 acts; every assertion is a seam-vs-raw EQUALITY -> STANDS. UNCHANGED (verified): `test_false_tail_absent_racing_reads` (the racing readers' TallyRefusedError catch already typed; the floor's halts ride the same quartet; the final census 12 intact).

**tests/test_service_face.py** — THE EIGHTH FACE (the brief's miss, §4's R9): `test_tally_success` (:116-143): the three-vote loop grows — each pair posted twice (the human body + the same body with "comparator_class": "llm") -> 6 posts; the body asserts UPDATE: per_item_wins {"a": 4, "b": 2, "c": 0}, per_item_losses {"a": 0, "b": 2, "c": 4}, per_item_ties all 0, pair_counts {"a|b": 2, "a|c": 2, "b|c": 2}; ranked_groups [["a"], ["b"], ["c"]] UNCHANGED. UNCHANGED (verified): `test_refusal_safe_halt` (the "at quorum" needle intact), `test_done_200` (census-keyed), every register/manifest/state/422/400/404/405/500 arc.

**tests/test_service_acceptance.py** — `_drive_arc` (:176-205) grows: the vote loop posts each pair TWICE — the `_VOTE_BODY` form then its llm variant `{**_VOTE_BODY, "comparator_class": "llm"}` -> the arc is ELEVEN requests (1 register + 1 manifest + 1 next + 6 votes + 1 done + 1 tally); `test_accept_the_eight_request_arc` RENAMES to `test_accept_the_eleven_request_arc` (the naming law — the arc's own count) with: len == 11; the statuses [201, 200, 200] + six 200s + [200, 200]; the acks bodies[3..8] == {"vote_id": "VOTE-0001".."VOTE-0006", "count": 1..6, "acknowledged": False}; the done body (bodies[9]) STANDS; the tally body (bodies[10]) UPDATES: per_item_wins {"a": 4, "b": 2, "c": 0}, per_item_losses {"a": 0, "b": 2, "c": 4}, per_item_ties all 0, pair_counts {"a|b": 2, "a|c": 2, "b|c": 2}; the docstrings' "eight-request" -> "eleven-request". `test_replay_byte_identical` rides _drive_arc UNCHANGED. UNCHANGED (verified): `test_refuse_the_four_arcs` (the 409 arc's "at quorum" needle intact; the concurrency arc census-only).

**tests/test_web_face.py** — `test_result_ranks_the_whole` (:158-168): the loop grows — each pair posted twice: the `_VOTE` form then `{**_VOTE, "comparator_class": "llm"}` -> 6 posts; every assertion ("one", "three", "win-rate-v1", "<table") STANDS. UNCHANGED (verified): the done-redirect/done-page/fragment arcs (census-keyed), `test_result_safe_halt_409` (the "at quorum" needle intact).

**tests/test_mcp_server_face.py** — the `_cast` helper (:94-116) gains the class parameter: `def _cast(caller: str, pair: list[str], winner: str, comparator_id: str, comparator_class: str = "human", supersedes: str | None = None) -> ToolResult:` with `"comparator_class": comparator_class` in the arguments (the docstring's "the class human" clause updated). 3 arcs grow: (1) `test_tally_view_at_full_coverage` (:190-210): each pair cast twice (human then llm) -> the TallyView body UPDATES: per_item_wins {"a": 4, "b": 2, "c": 0}, per_item_losses {"a": 0, "b": 2, "c": 4}, per_item_ties all 0; pairs_expected 3, pairs_at_quorum 3, done True UNCHANGED. (2) `test_the_sitting_end_to_end` (:575-598): after the first cast, the corroborating cast `_cast(caller, ["a", "b"], "prefer-a", "x", "llm")` lands; the census assert UPDATES to {"total": 2, "items": {"a": 2, "b": 2}}; the tally asserts (ranked_groups [["a"], ["b"]], coverage done) STAND. (3) `test_re_tally_after_cure` (:601-635): the cure cast (:619) grows its class byte: `_cast(caller, ["a", "b"], "prefer-a", "y", "llm")` — the halt after the first cast still carries "(a, b) needs 1 more" (the quorum section), the cured tally's body (wins {"a": 2, "b": 0}) STANDS. UNCHANGED (verified): the census/ack/idempotency/seed/cross-session arcs and every refusal arc.

**tests/test_harness.py** — THE NINTH FACE (the brief's miss, §4's R9): the arc grows from 7 to 10 invocations: `_vote_argv` (:72-74) gains the class parameter `comparator_class: str = _HUMAN`; `_arc_argv_sequence` (:77-87) grows — each pair voted twice (`_vote_argv(home, "a", "b")` then `_vote_argv(home, "a", "b", _LLM)` with the `_LLM = "llm"` constant; likewise a-c and b-c) -> 10 argvs; the ack constants grow (`_VOTE_FOUR_OUT`..`_VOTE_SIX_OUT` = b"vote\tVOTE-0004\t4\n" .. b"vote\tVOTE-0006\t6\n"); `_TALLY_ABC` (:47-59) UPDATES: b"counts\ta\t4\t0\t0", b"counts\tb\t2\t2\t0", b"counts\tc\t0\t4\t0", b"coverage\t1\tTrue", b"pairs\ta\tb\t2", b"pairs\ta\tc\t2", b"pairs\tb\tc\t2", the rank/version lines UNCHANGED; `test_arc_seven_invocations_green` RENAMES to `test_arc_ten_invocations_green` (the rc list 10 zeros, the per-step stdout asserts, the tally stdout == _TALLY_ABC); `_drive_arc`/`test_determinism_replay_byte_identical` ride UNCHANGED. UNCHANGED (verified): `test_safe_halt_exit_one_no_partial_ranking` (the "at quorum" needle intact), the unknown-run/out-of-set arcs.

THE STANDING HALT ARCS ACROSS THE FACES (test_cli's parametrize, test_service_face's 409, test_service_acceptance's 409, test_web's 409, test_harness's R3, test_session's seam-divergence, test_tally's quorum/seam arcs): every one asserts SUBSTRING needles that hold under the grown found/expected — UNCHANGED, named here so the build never "fixes" what stands.

[the spec's continuation — piece 5: §4 the proofs + §5 the plan]
## Reported by togo — 2026-11-24T18:22:22Z

[the spec's continuation — piece 5, the closing: §4 the proofs + §5 the plan]

## 4. THE NO-BREAK PROOFS + THE NAMED RULINGS

**THE PURITY DIVIDEND — THE SIGNATURE BYTE-STANDING**: `tally_votes(manifest, vote_log)` unchanged at :438; ZERO caller changes: service.py, session.py, mcp_server.py, web.py, cli.py, run_store.py, service_store.py, key_store.py, key_verify.py, scheduler.py, registry.py, votes.py — byte-standing (no signature, no manifest field, no knob, no caller edit — the brief §2c's unconditional ruling). THE ONE SOURCE GROW: acceptance.py's two builder regions (§3c — the harness's judge classes; the signature of accept_run unchanged, the RNG stream untouched). THE WIRE BYTE-STANDING: every coverage serializer names its fields (service.py :513-516, web.py :517-519, mcp_server.py :558-565, cli.py :386-393) — the new datum field rides UNSERIALIZED, additive (the integration unit's lift if ever earned).

**THE FLOOR'S GROWTH**: 245 (validate/key-infrastructure.md :20, the landed count) -> **268** — 23 new test functions, zero parametrize: test_policy.py 10 (rows-exact, fork-guard, roles-vocabulary, frozen-form, default-deny, unknown-role, manifest-hole, both-present, names-the-absent, zero-count) + test_tally.py 13 (both-classes-pass, human-only, llm-only, k2-conjunction, superseded, stamp-not-identity, zero-vote-both, datum-at-done, purity-mix, both-cures, full-conjunction, two-cures-distinct, three-fields). The faces' fixture growth changes NO function count (the two renames — eight->eleven, seven->ten — are renames, not additions). The build's floor-green step names the landed count; any drift ruled at the gate.

**THE ZERO-IGNORE BAR**: zero new per-file-ignores expected (policy.py and test_policy.py need none — the module is pure data + two predicates, the file's asserts ride the tests/** S101/PLR2004 ruling); pyproject.toml UNTOUCHED. Every existing ignore stands as its named ruling.

**THE NAMED RULINGS (each with the reason — the ask's own demand)**:
- **R1 THE UNKNOWN ROLE -> THE EMPTY SET** (the ask's bytes): the brief's N818 typed-refusal proposal superseded — the denial as DATA (the door's check `token in granted_scopes(role)` one total expression, no try/except machinery at the six doors; the empty set denies every token by construction); the teaching ThreePart rides the door's own 403 lane (the integration unit's arc), never a second grammar inside the pure module — the Parnas fold's own law. The brief's "unknown-role refusal" arc becomes the empty-set arc (test_unknown_role_denied_whole).
- **R2 THE TOKENS' HOME**: the map's rows literals + the test-arc pin; policy.py imports nothing from key_store (§1's reasons).
- **R3 THE CHECKER'S INPUT**: the per-pair class COUNTS, never the records — the one-pass ruling; the >=1 law in the predicate.
- **R4 THE REFUSAL DATA'S FORM**: list[tuple[Pair, tuple[str, ...]]] — the shortfalls' own school.
- **R5 THE ACCEPTANCE HARNESS GROW**: the brief's §3 honest cost over its §1 NOT-touch letter — the letter's reason (the signature dividend) holds whole (accept_run's signature unchanged, no RNG draw consumed, the seeds' replay identical); the builder's class mix is the floor's tree-wide semantic cost, grown in THIS unit's floor-green, never a follow-up.
- **R6 THE ONE EM DASH**: the next_action floor section's separator matches the renderer field's own grammar (:389/:394) — the field-level no-fork law (a "--" beside "—" inside one next_action string is the byte-fork class); every other authored byte ASCII (the new files whole; the seam lines' new prose parenthesized, never dashed); the test assertions QUOTE the rendered byte where exactness demands.
- **R7 THE § SIGN**: the provenance-citation school the sibling unit landed (key_store.py :78, ruled green at validate/key-infrastructure.md) — carried for the citation grammar's uniformity; the ASCII discipline governs every other byte.
- **R8 THE IMPLICIT-CONCAT DISCIPLINE**: "no implicit concat" = the same-line adjacency class (pyright's error form; ISC001's class); the multi-line paren continuation is the tree's ruled idiom (tally.py :492-495, key_store.py :135 — green at both gates today), kept where a long f-string demands it (the gate's expected, the exact-byte test assertions); no `+`-concat of literals anywhere (ISC003).
- **R9 THE CENSUS'S THREE ADDITIONS**: test_service_face.py :116-143, test_harness.py :47-107, test_service_store.py :143-176 — DONE-reaching arcs the brief's seven-file list missed; the read-back's own findings (the census function the brief itself mandates), grown in this unit's floor-green, the evidence cited per line, never silent.
- **R10 THE HALT ARCS STAND**: the existing halt arcs' substring needles hold under the grown found/expected — unchanged, named so the build never "fixes" what stands.

**THE NAMED DRIFT (the integration unit's opens, never silent)**: mcp_server.py's _capped_halt re-derivation (:402-449 over the mirrored renderers :331-398) knows legs 1-3 only — OVER the K=10 cap its local re-render would drop the floor's section; WITHIN the cap the refusal rides verbatim. The integration unit grows the mirror's leg 4; this unit's fence holds the tiers untouched.

**THE TRADE-OFF THE PLAN MUST CARRY** (the brief §2c, standing): the single-class sitting can never DONE — the solo comparator, the llm-only run, the web-only sitting halt honestly unless corroborated; at k=1 the effective minimum becomes TWO votes per pair (one per class — a vote carries one class, the conjunction never degrades).

## 5. THE PER-STEP PLAN (R8, the file-unit — one file per dispatch, the read-backs named)

1. **src/prioritree/policy.py** (NEW) — read-back: pyright resolves the module (no cycle: votes imports neither policy nor tally); the three rows vs the design's bytes verbatim; the vocabulary citation (COMPARATOR_CLASSES imported, SCOPE_TOKENS never).
2. **src/prioritree/tally.py** (the five seam regions + tally_votes' docstring + the emission's field) — read-back: the signature byte-standing (grep `tally_votes(` — the callers' call sites untouched); the gate's four conjuncts in the condition line; the renderers' sections in the legs' order; the counted rollup initialized over the full universe.
3. **src/prioritree/acceptance.py** (the harness builder's two regions) — read-back: the judge-class derivation deterministic (the parity over sorted(COMPARATOR_CLASSES), no RNG draw); the docstring's stamp block honest.
4. **tests/test_policy.py** (NEW) — read-back: the fork-guard arc green (the literals pinned to SCOPE_TOKENS); the ten arcs green; zero store imports beyond the pin.
5. **tests/test_tally.py** (GROWN) — read-back: the 13 new arcs green; the existing arcs' updated bytes exact (the re-derived prefix founds, the doubled emissions); the helper's default keeping the halt arcs byte-identical.
6. **tests/test_session.py** — read-back: the end-to-end emission's doubled counts exact; the standing arcs untouched.
7. **tests/test_run_store.py** — read-back: the two replay arcs' rank equality at the mix; log[1] still the correction.
8. **tests/test_cli.py** — read-back: _TALLY_ABC's grown bytes; the standing needles intact.
9. **tests/test_service_store.py** — read-back: the equivalence arc's 6-act mix, both arms equal.
10. **tests/test_service_face.py** — read-back: the tally body's doubled counts; the 409 arc's needle intact.
11. **tests/test_service_acceptance.py** — read-back: the eleven-request arc whole (the statuses, the six acks, the done body, the grown tally body); the replay byte-identical.
12. **tests/test_web_face.py** — read-back: the result page's 200 at the mix; the 409 arc's needle intact.
13. **tests/test_mcp_server_face.py** — read-back: the helper's class parameter; the three arcs' updated bodies; the cure arc's class byte.
14. **tests/test_harness.py** — read-back: the ten-invocation arc's rcs and per-step stdout; _TALLY_ABC's grown bytes; the replay byte-identical.
15. **THE FLOOR-GREEN (make)** — the landed count named in the build's report (the plan's 268); ruff ALL clean + pyright strict clean at the SAME make (the zero-findings bar; zero new ignores); kensho's validate/policy-layer the independent verification per the route's build stage.

THE SPEC LANDED WHOLE — five report pieces composing one document (the 65,536-byte bound honored, append-only); the projection at reports/synthesize/policylayerspec.md; the collaborator rules on this record at G-POLICYLAYERSPEC-BRIEF.
## Reported by togo — 2026-11-24T19:22:47Z

R6 — THE TWO RULINGS (jikko step-5's findings folded; the read-back: _vote's fence-verbatim 6-param signature tests/test_tally.py:42-50 [spec §3b :456-476]; the bridging render condition tally.py:408 `len(components) > 1` [components :525, union-find :243-276]; the arc's fence policylayerspec :637-648; the §2(e) worked whole :358).
RULING 1 (PLR0913 — the pyproject entry per the named-ruling family form, placed alphabetically LAST among the tests entries: after pyproject.toml:156's tests/test_store_lock_face.py block, before [tool.ruff.format] :158):
# RULING (policylayerspec §3b, G-POLICYLAYERSPEC-BRIEF approved 2026-11-24): _vote's six parameters ARE the fence's ruled
# builder signature — the helper mirrors VoteRecord's own fields (vote_id, pair, winner, comparator_class, notes, supersedes —
# the votes' own signature carried at the fixture tier; the votes.py/session.py/run_store.py/service_store.py PLR0913 rulings
# re-cited). The arg count is the domain's, not the test's choice; the ignore IS the ruling, named. It retires only if the
# record's own signature is re-ruled.
"tests/test_tally.py" = ["PLR0913"]
RULING 2 (the bridging assert's cure — the spec's own worked whole): the three asserted needles were authored from §2(e)'s rendered next_action (policylayerspec :358, each verbatim in it); the fence's ab+ac fixture was the mis-copy (the sibling arc's shape — unions to ONE component, tally.py :524-525, so the bridging section never renders and the assert can never pass). THE FIX, exact bytes: `manifest = _manifest(["a", "b", "c"])` UNCHANGED; `votes = (_vote("VOTE-0001", _AB_PAIR, PREFER_A),)` — the `_vote("VOTE-0002", _AC_PAIR, PREFER_A),` line deleted (tests/test_tally.py:453); the three asserts stand byte-verbatim; the arc then renders the §2(e) bytes exact — components ({a,b}, {c}), bridge (a, c): "cast the bridging pairs: (a, c) — connectivity needs NEW comparisons; cast the missing votes: (a, c) needs 1 more, (b, c) needs 1 more — quorum needs MORE VOTES on existing pairs; cast the corroborating votes: (a, b) needs llm, (a, c) needs human, llm, (b, c) needs human, llm — corroboration needs votes from BOTH CLASSES on existing pairs".
TRADE-OFF NAMED: the four-item alternative (manifest ["a","b","c","d"], votes ab+ac — components {a,b,c}+{d}, rendered bridge (a, d)) also satisfies the three asserts but carries no spec byte-provenance; the §2(e)-backed form rules — the arc becomes the spec's own worked whole's acceptance.
## Reported by togo — 2026-11-24T20:01:54Z

R6 — the pre-floor fold: the three rulings (build/policy-layer's findings, jikko's steps 12-15 report).

RULING A — the crash's fix, THE DATUM RE-KEYS AT CONSTRUCTION (candidate (i); the service's strip extension REFUSED — the integration's fence breached by this unit): tally.py:88's field becomes `pair_class_counts: Mapping[str, Mapping[str, int]]` — the "a|b" string keys, the same re-key form service.py:516 already renders for pair_counts; the construction line (:566) re-keys at the datum's birth — `{f"{pair.item_a}|{pair.item_b}": class_map for pair, class_map in state.pair_class_counts.items()}` — while the internal accumulation stays Pair-keyed: the gate (:529-533), the renderers (:542-547), and tally_votes' signature (:471) untouched, byte-standing. service.py UNTOUCHED: the :513 strip suffices, asdict serializes, the tally body + the result page 500s die. THE NAMED COST: the datum's form asymmetry — pair_counts stays Pair-keyed (:87), pair_class_counts string-keyed from birth.

RULING B — the PLR0913+PLR0917 entry: `"tests/test_mcp_server_face.py" = ["PLR0913", "PLR0917"]`, landing after the test_tally.py entry (:163), the RULING comment per the existing form: _cast's six parameters (:94-101 — caller, pair, winner, comparator_id, comparator_class, supersedes) mirror the tool's own cast parameters — the domain's, not the test's choice; it retires only if the tool's own signature is re-ruled.

RULING C — the PLR0913 entry: `"tests/test_harness.py" = ["PLR0913", "S603", "S607"]` — PLR0913 joins the existing :99 entry (TOML bars duplicate keys; the S603/S607 ruling re-carried), the RULING comment citing _vote_argv's CLI-argv mirror. THE READ-BACK'S OPEN QUESTION, named: _vote_argv carries FOUR parameters (test_harness.py:76 — home, item_a, item_b, comparator_class); PLR0913's bar under select=["ALL"] with no max-args override is six arguments, and jikko's own re-apply read ZERO findings on the file — the finding does not reproduce on disk; the entry is prophylactic (dead until the signature grows past five); the floor instruments decide.
## Reported by togo — 2026-11-24T20:15:57Z

# The fold — the three floor classes ruled (togo; the bytes read at the instruments — pytest run, every error read)

RULING 1 — the ten test_tally standing arcs. DIAGNOSIS (the bytes): F8's leg-4 conjunction halts every single-class fixture — the six DONE-reaching arcs (purity, hand-computed, cycle, tie-break, no-score, version-stamp) raise "uncorroborated pairs: … missing llm" (tally.py:540) where DONE/rankings are asserted; the prefix/isolation arcs' exact found needles lack the appended "; uncorroborated pairs: …" section; supersession's arms halt at weighted 1-2 human-only; the seam's quorum-1 arm halts at weighted 1. Step 5's R10 "unchanged" was the wrong ruling — the DONE intent requires the mix under the floor.
CURE 1 (the §3c growth, the other faces' form): each DONE-reaching fixture joins per pair its llm twin, same winner — the counted maps double mechanically (pair_counts 1→2, wins/losses ×2; ranked_groups/cycle byte-unchanged); supersession's DONE arms append the counted judgment's llm twin (the fork arm's minimal byte: VOTE-0005 recast comparator_class="llm", its asserts standing byte-identical) while the quorum-2 halt arm keeps the un-tupled 2-vote fixture; the prefix arc's script becomes the interleaved human-then-llm 6-vote sequence (each prefix's found needle grown to the rendered bytes, [:6] DONE), the isolation arc's empty needle appends "; uncorroborated pairs: (a, b) missing human, llm, (a, c) missing human, llm, (b, c) missing human, llm"; the seam arc's quorum-1 DONE arm is STRUCTURALLY unreachable (one counted vote = one class) — re-pin it to the corroboration halt (found "uncorroborated pairs: (a, b) missing llm", next "cast the corroborating votes: (a, b) needs llm"), the quorum-2 arm byte-unchanged — the weighted-vs-raw seam still pinned by "1 of 2".

RULING 2 — the three mcp halt arcs. DIAGNOSIS (the bytes): the halt's grown render — the expected's " AND corroborated (>=1 human AND >=1 llm per pair)" plus found's uncorroborated section — pushes the needles past the wire's 300-char clip (ouncemcp's max_error_chars): the under-cap text ends "(a, b) needs…" (the "needs 1 more" needle clipped), the capped text ends "…15 under-quorum pairs tota…" (the "total; first 10 shown" elision clipped), the re-tally halt needle clips the same way. R10's "needles hold" is false under the grown render; the wire's budget is external (not growable), the grown bytes are the floor's honesty (not shrinkable).
CURE 2 (needle re-placement to the visible head): under-cap asserts "next_action: cast the missing votes: (a, b) needs" and may add the visible "uncorroborated pairs: (a, b) missing llm" (the found's two sections both on the wire); capped asserts "under-quorum pairs: 15" (the total's head; the found's internal 10-cap elision rides past the wire clip); re-tally asserts "cast the missing votes: (a, b) needs" at the halt (the llm cure-cast and the re-tally DONE asserts byte-unchanged); the three docstrings' "no clip"/"elision visible" claims grow honest — the two-cap reality named (the found's 10-cap, the wire's 300-clip).

RULING 3 — the matrix k=1 leg. DIAGNOSIS (the bytes): at the (n=10, k=1) cell all 45 pairs report "missing llm" — next_pair drains each pair at census 1 and the single cast lands at pair_count=0 → HARNESS_JUDGE_CLASSES[0]="human" for every pair; one vote cannot carry both classes, so NO derivation fix exists (the hypothesis's pair_count-form is closed by the bytes); the k=3 cells pass (human, llm, human); the sizer arm rides no gate (budget_curve's own mirror) — the single halt site is accept_run's tally_rank.
CURE 3 (the floor's honest cost at the harness — the parity comment's own words, acceptance.py:85-88): accept_run registers at max(quorum, len(HARNESS_JUDGE_CLASSES)) — the k=1 cells register at 2 and the parity then serves human+llm per pair (both legs green; the k=3 cells and every default-k accept_run call byte-unchanged).
TRADE-OFF 3 (named, the plan's carry): the equal-budget law (B = n0×quorum, both arms — the curve's banked thesis) — growing the acceptance arm alone breaks it at k=1 (n0×2 vs n0×1); the recommended whole grows size_run's total_budget and the matrix's budget assert to the same max form — both arms at the floored budget, the law preserved, the k=1 leg measuring the floored form (the single-judgment baseline retired to the recorded table, the docstring's own "recorded, never erased").

LANDING: the three cures ride one dispatch (tests/test_tally.py, tests/test_mcp_server_face.py, src/prioritree/acceptance.py + budget_curve.py + the matrix's budget assert); the floor-green make re-runs after; the grown arcs' under-counting docstrings stay byte-verbatim per the steps 6-7 precedent unless the coordinator rules their growth.
