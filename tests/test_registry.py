# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The registry unit's example tests — the eleven named edges (registry-brief §4)."""

from typing import cast

import pytest

from prioritree.registry import (
    WEAK_ORDER_TRIPLE,
    ItemRow,
    OperatorDeclaration,
    Registry,
    RegistryRefusedError,
)


def _declaration(
    op_id: str = "op-1",
    question: str = "Which matters more?",
    verdicts: frozenset[str] | None = None,
) -> OperatorDeclaration:
    """Build a well-formed declaration, or a deliberately malformed one."""
    if verdicts is None:
        return OperatorDeclaration(id=op_id, question=question)
    return OperatorDeclaration(id=op_id, question=question, verdicts=verdicts)


def test_empty_list_refused() -> None:
    """The empty list refuses; found names 0; nothing lands."""
    registry = Registry()
    with pytest.raises(RegistryRefusedError) as exc_info:
        registry.register_run([], operator=_declaration())
    assert exc_info.value.expected == "at least 2 item rows (a comparison needs a pair)"
    assert exc_info.value.found == "0 item rows"
    assert registry.read_manifest_count() == 0


def test_single_item_refused() -> None:
    """The single item refuses; found names 1 — distinct from the empty list's 0."""
    registry = Registry()
    with pytest.raises(RegistryRefusedError) as exc_info:
        registry.register_run([("a", "one")], operator=_declaration())
    assert exc_info.value.found == "1 item row"
    assert exc_info.value.expected == "at least 2 item rows (a comparison needs a pair)"
    assert registry.read_manifest_count() == 0


def test_minimum_registration_mints_run_0001() -> None:
    """Exactly 2 items, distinct ids — the boundary success mints RUN-0001."""
    registry = Registry()
    run_id, manifest, count = registry.register_run([("a", "one"), ("b", "two")], operator=_declaration())
    assert run_id == "RUN-0001"
    assert count == 1
    assert manifest.run_id == "RUN-0001"
    assert manifest.quorum == 1
    assert manifest.items == (
        ItemRow(id="a", label="one"),
        ItemRow(id="b", label="two"),
    )
    assert registry.read_manifest_count() == 1


def test_duplicate_ids_refused() -> None:
    """Duplicate id refuses naming the id and its positions; the store unchanged."""
    registry = Registry()
    with pytest.raises(RegistryRefusedError) as exc_info:
        registry.register_run([("a", "one"), ("b", "two"), ("a", "again")], operator=_declaration())
    assert exc_info.value.expected == "all item ids unique within the payload"
    assert exc_info.value.found == "duplicate id 'a' at positions 0, 2"
    assert registry.read_manifest_count() == 0


def test_malformed_operator_declaration_refused() -> None:
    """Missing/empty id or question, and a non-triple verdict set, each refuse."""
    registry = Registry()
    with pytest.raises(RegistryRefusedError) as exc_info:
        registry.register_run([("a", "one"), ("b", "two")], operator=_declaration(op_id="  "))
    assert exc_info.value.found == "operator.id got '  '"
    with pytest.raises(RegistryRefusedError) as exc_info:
        registry.register_run([("a", "one"), ("b", "two")], operator=_declaration(question=""))
    assert exc_info.value.found == "operator.question got ''"
    bad_sets: tuple[frozenset[str], ...] = (
        frozenset({"prefer-a", "prefer-b"}),
        frozenset({"prefer-a", "prefer-b", "tie", "abstain"}),
        frozenset(),
    )
    for bad in bad_sets:
        with pytest.raises(RegistryRefusedError) as exc_info:
            registry.register_run([("a", "one"), ("b", "two")], operator=_declaration(verdicts=bad))
        assert exc_info.value.expected == (
            "the weak-order triple {prefer-a, prefer-b, tie} (the declared set's default)"
        )
    assert registry.read_manifest_count() == 0


def test_verdict_set_default_lands_as_data() -> None:
    """A declaration with no verdict set carries the triple (the default as data)."""
    registry = Registry()
    _run_id, manifest, _count = registry.register_run([("a", "one"), ("b", "two")], operator=_declaration())
    assert manifest.operator.verdicts == WEAK_ORDER_TRIPLE


def test_quorum_as_data() -> None:
    """Omitted → 1; k=2 stored verbatim; illegal forms refuse; a large k accepts."""
    registry = Registry()
    _run_id, manifest, _count = registry.register_run([("a", "one"), ("b", "two")], operator=_declaration())
    assert manifest.quorum == 1
    _run_id, manifest, _count = registry.register_run([("a", "one"), ("b", "two")], operator=_declaration(), quorum=2)
    assert manifest.quorum == 2
    for bad in (0, -1, "2", 2.5, None):
        with pytest.raises(RegistryRefusedError) as exc_info:
            registry.register_run([("a", "one"), ("b", "two")], operator=_declaration(), quorum=cast("int", bad))
        assert exc_info.value.expected == "an integer >= 1 (default 1)"
    _run_id, manifest, _count = registry.register_run(
        [("a", "one"), ("b", "two")], operator=_declaration(), quorum=1_000_000,
    )
    assert manifest.quorum == 1_000_000


def test_read_back_round_trip() -> None:
    """Payload in → return out → read_manifest equal to both; stable across calls."""
    registry = Registry()
    sent = [("a", "one"), ("b", "two")]
    run_id, manifest, count = registry.register_run(sent, operator=_declaration(), quorum=3)
    assert count == 1
    read_back = registry.read_manifest(run_id)
    assert read_back == manifest
    assert read_back == registry.read_manifest(run_id)
    assert [row.id for row in read_back.items] == ["a", "b"]
    assert [row.label for row in read_back.items] == ["one", "two"]
    assert read_back.quorum == 3
    assert read_back.run_id == run_id


def test_aliasing_edge() -> None:
    """Mutating the caller's list after registration leaves the manifest unchanged."""
    registry = Registry()
    payload: list[tuple[str, str]] = [("a", "one"), ("b", "two")]
    run_id, manifest, _count = registry.register_run(payload, operator=_declaration())
    payload.append(("c", "three"))
    payload[0] = ("a", "MUTATED")
    assert registry.read_manifest(run_id) == manifest
    assert [row.id for row in registry.read_manifest(run_id).items] == ["a", "b"]
    assert [row.label for row in registry.read_manifest(run_id).items] == ["one", "two"]


def test_mint_sequence() -> None:
    """Three registrations mint RUN-0001/0002/0003 monotonely; no dedup."""
    registry = Registry()
    payload = [("a", "one"), ("b", "two")]
    handles = [registry.register_run(payload, operator=_declaration())[0] for _ in range(3)]
    assert handles == ["RUN-0001", "RUN-0002", "RUN-0003"]
    assert registry.read_manifest_count() == 3


def test_two_registries_mint_independently() -> None:
    """Two containers in one process each mint RUN-0001 (store-as-data)."""
    first = Registry()
    second = Registry()
    payload = [("a", "one"), ("b", "two")]
    assert first.register_run(payload, operator=_declaration())[0] == "RUN-0001"
    assert second.register_run(payload, operator=_declaration())[0] == "RUN-0001"
    assert first.read_manifest_count() == 1
    assert second.read_manifest_count() == 1


def test_opacity() -> None:
    """Labels of any content and the stated question store verbatim — no content check."""
    registry = Registry()
    long_label = "z" * 10_000
    payload = [
        ("a", ""),
        ("b", "héllo — 日本語 🌍, tabs\tand\nnewlines"),
        ("c", long_label),
    ]
    _run_id, manifest, _count = registry.register_run(payload, operator=_declaration(question="¿Cuál importa?"))
    assert [row.label for row in manifest.items] == ["", "héllo — 日本語 🌍, tabs\tand\nnewlines", long_label]
    assert manifest.operator.question == "¿Cuál importa?"
