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
from prioritree.policy import ROLE_SCOPES, ROLES, granted_scopes, missing_classes
from prioritree.votes import COMPARATOR_CLASSES


def test_grant_map_rows_exact() -> None:
    """The three rows byte-exact -- the design's grant map, default-deny's named allows."""
    assert ROLE_SCOPES["operator"] == frozenset({"register", "state", "tally", "manifest"})
    assert ROLE_SCOPES["comparator"] == frozenset({"next", "cast", "manifest"})
    assert ROLE_SCOPES["auditor"] == frozenset({"state", "tally", "manifest"})


def test_granted_tokens_pin_scope_tokens() -> None:
    """The fork-guard: every granted token rides key_store's SCOPE_TOKENS -- the drift caught here."""
    granted = set[str]().union(*ROLE_SCOPES.values())
    assert granted <= SCOPE_TOKENS


def test_roles_vocabulary_exactly_three() -> None:
    """The roles' vocabulary: three names, no fourth -- the map's keys exactly the vocabulary."""
    assert frozenset({"operator", "comparator", "auditor"}) == ROLES
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
