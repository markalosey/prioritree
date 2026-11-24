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

from types import MappingProxyType
from typing import TYPE_CHECKING, Final

from prioritree.votes import COMPARATOR_CLASSES

if TYPE_CHECKING:
    from collections.abc import Mapping

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
    },
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
