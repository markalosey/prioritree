# synthesize/registry-bytes-v2 — THE REGISTRY UNIT'S CURED BYTES (amendment 16 applied; supersedes registry-bytes.md Deliverables 1-2)

- Provenance: togo (統合, integrate), packets synthesize/registry-bytes-v2-py + the test-file cure (same authoring session), route prioritree-core, 2026-11-20. Amendment 16's cures applied to the v1 bytes: the N818 rename (RegistryRefused → RegistryRefusedError), the C901 validator split (object-typed private validators — also curing the four reportUnnecessaryIsInstance findings), the PLR2004 _PAIR_LENGTH constant, the five explicit-concatenation cures, the tests' I001/COM812 cures with ItemRow joining the import block, and the __import__ wart replaced with direct ItemRow use.
- The v1 addendum (synthesize/registry-bytes.md) stands as the authoring record; THIS file supersedes its Deliverables 1-2 as the landing source. The code paths already carry the v1 bytes — the landing steps are REPLACE, not create.
- The landing discipline held through authoring: the test-file return's transit truncation was recovered by session resume same-turn; the excursion session (FR-MEM-0012) stayed cancelled — the simplified single-goal prompts (the verification clause deleted; the floor is its own dispatch) returned both files clean.
- Landed by shinko via patch, 2026-11-20; read-back verified.

## Deliverable 1 — src/prioritree/registry.py (byte-exact; land as the replacement)

```python
# Copyright (C) 2026 Mark Losey. All rights reserved.
"""registry — the run-manifest store: register a comparison session's ground, read it back.

The registry unit (U1): opaque (id, label) rows, one operator declaration, quorum
as data — frozen at registration into a RUN-{####} manifest the downstream units
cite. Zero runtime dependencies; hand-rolled fail-loud validation; no subprocess;
labels and questions stored verbatim (opacity — validation touches structure only).
"""

from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field
from datetime import UTC, datetime

# The declared default verdict set (R4): the weak-order triple — a module-level
# frozenset constant (content-in-configuration: the vocabulary is data, never
# inline logic).
WEAK_ORDER_TRIPLE: frozenset[str] = frozenset({"prefer-a", "prefer-b", "tie"})

# Structural constants (named, per the zero-magic-value-in-src discipline).
_MIN_ITEM_ROWS = 2
_PAIR_LENGTH = 2
_RUN_PREFIX = "RUN-"


@dataclass(frozen=True)
class ItemRow:
    """ItemRow — one opaque row of the list under comparison.

    Purpose: carry one item's addressable identity (id) and its content (label)
    as the frozen row every vote cites.
    Refuses when: never at construction — validation happens at register_run;
    ids are non-empty stripped strings there; labels are any string, verbatim.
    Re-run: idempotent — a value type; constructing the same (id, label) twice
    yields equal rows.
    Touches: nothing — a pure value; read by RunManifest and every downstream unit.
    Provenance: R2 (the opaque (id, label) rows the core never interprets),
    scope-synthesis PART 3 §3.2 op 1, registry-brief §2.
    """

    id: str
    label: str


@dataclass(frozen=True)
class OperatorDeclaration:
    """OperatorDeclaration — the session's single comparison operator, declared.

    Purpose: bind one operator (id + stated question + declared verdict set) to
    the run; the declared verdict set is the single source of legal vote values.
    Refuses when: never at construction — the form is validated at register_run
    (non-empty id/question; the verdict set the weak-order triple, default when
    omitted).
    Re-run: idempotent — a value type.
    Touches: nothing — a pure value; frozen into RunManifest at registration.
    Provenance: R3 (ONE operator declaration per run), R4 (the weak-order triple
    as the declared set's default), registry-brief §2.
    """

    id: str
    question: str
    verdicts: frozenset[str] = field(default_factory=lambda: frozenset(WEAK_ORDER_TRIPLE))


@dataclass(frozen=True)
class RunManifest:
    """RunManifest — the frozen ground of one registered run.

    Purpose: hold the run's handle, its frozen rows (payload order preserved),
    the operator declaration, the quorum, and the registration stamp — the
    immutable record downstream units cite by run_id.
    Refuses when: never at construction — register_run validates the payload
    and mints the manifest; there is no edit or delete verb for it.
    Re-run: idempotent — a value type; reading is stable across calls.
    Touches: nothing — a pure value; the Registry container holds these.
    Provenance: R1 (the run is FROZEN at registration), R8 (quorum as data),
    registry-brief §2; the registered_at stamp per the CF-3b cheap-now doctrine.
    """

    run_id: str
    items: tuple[ItemRow, ...]
    operator: OperatorDeclaration
    quorum: int
    registered_at: str


class RegistryRefusedError(Exception):
    """RegistryRefusedError — the typed refusal: expected, found, next_action.

    Purpose: carry the refusal grammar (expected/found/next-action) as data the
    CLI/service wrappers catch and render; raised, never returned.
    Refuses when: never — it IS the refusal; the message renders all three
    fields so an uncaught traceback still names the legal form.
    Re-run: deterministic — the same violation raises the same three fields.
    Touches: nothing — a plain Exception subclass (zero runtime deps).
    Provenance: the RefusedError precedent (friction_ledger.py:241-246),
    registry-brief §2; the expected/found/next-action grammar (R2, scope-synthesis
    PART 3 §3.2 op 1).
    """

    def __init__(self, expected: str, found: str, next_action: str) -> None:
        """Initialize the refusal with its three named fields.

        Purpose: carry expected/found/next_action plus the rendered message.
        Refuses when: never.
        Re-run: idempotent.
        Touches: nothing.
        Provenance: registry-brief §2 (the typed exception, RefusedError precedent).
        """
        self.expected = expected
        self.found = found
        self.next_action = next_action
        super().__init__(f"refused — expected: {expected} | found: {found} | next: {next_action}")


def _require_text(value: object, field_name: str) -> str:
    """Return the stripped non-empty string or refuse (the _req_text precedent).

    Purpose: enforce the non-empty-string discipline on structural fields.
    Refuses when: the value is not a string or is empty/whitespace-only.
    Re-run: deterministic.
    Touches: nothing (raises before any store write).
    Provenance: friction_ledger.py:406-413 (_req_text), registry-brief §2.
    """
    if not isinstance(value, str) or not value.strip():
        raise RegistryRefusedError(
            expected="a non-empty string",
            found=f"{field_name} got {value!r}",
            next_action="the schema is the module's public types (ItemRow)",
        )
    return value.strip()


def _mint_run_id(count: int) -> str:
    """Mint the RUN-{####} handle — 4-digit zero-pad, natural overflow.

    Purpose: name the run per the per-store max+1 mint (count is the live size).
    Refuses when: never — the count is the container's own live state.
    Re-run: deterministic for a given store state.
    Touches: nothing — pure over its argument.
    Provenance: the FR-{NS}-{####} precedent (friction_ledger.py:74-78, 389-398),
    registry-brief §3 (the mint).
    """
    return f"{_RUN_PREFIX}{count + 1:04d}"


def _coerce_rows(items: object) -> tuple[tuple[str, str], ...]:
    """Shape-check the payload into (id, label) string pairs.

    Purpose: validate each item as an ItemRow or a 2-length sequence; ids via
    _require_text, labels any string; return the validated pairs.
    Refuses when: an item is neither ItemRow nor 2-length sequence, an id is not
    a non-empty string, or a label is not a string.
    Re-run: deterministic.
    Touches: nothing (raises before any store write).
    Provenance: registry-brief §3 validation step 1 (shape), the _req_text precedent.
    """
    if not isinstance(items, Sequence) or isinstance(items, str):
        raise RegistryRefusedError(
            expected="rows of (string id, string label)",
            found=f"items got {items!r}",
            next_action="the schema is the module's public types (ItemRow)",
        )
    rows: list[tuple[str, str]] = []
    for position, item in enumerate(items):
        if isinstance(item, ItemRow):
            item_id = _require_text(item.id, f"items[{position}].id")
            if not isinstance(item.label, str):
                raise RegistryRefusedError(
                    expected="rows of (string id, string label)",
                    found=f"items[{position}].label got {item.label!r}",
                    next_action="the schema is the module's public types (ItemRow)",
                )
            rows.append((item_id, item.label))
        elif isinstance(item, Sequence) and not isinstance(item, str) and len(item) == _PAIR_LENGTH:
            pair = tuple(item)
            item_id = _require_text(pair[0], f"items[{position}].id")
            if not isinstance(pair[1], str):
                raise RegistryRefusedError(
                    expected="rows of (string id, string label)",
                    found=f"items[{position}].label got {pair[1]!r}",
                    next_action="the schema is the module's public types (ItemRow)",
                )
            rows.append((item_id, pair[1]))
        else:
            raise RegistryRefusedError(
                expected="rows of (string id, string label)",
                found=f"items[{position}] got {item!r}",
                next_action="the schema is the module's public types (ItemRow)",
            )
    return tuple(rows)


def _check_cardinality(rows: tuple[tuple[str, str], ...]) -> None:
    """Refuse fewer than two rows — the empty list AND the single item are named refusals.

    Purpose: enforce the comparison-needs-a-pair floor (R2).
    Refuses when: len(rows) < 2 — found names 0 and 1 distinctly.
    Re-run: deterministic.
    Touches: nothing (raises before any store write).
    Provenance: R2, registry-brief §3 validation step 2 (cardinality).
    """
    if len(rows) < _MIN_ITEM_ROWS:
        raise RegistryRefusedError(
            expected="at least 2 item rows (a comparison needs a pair)",
            found=f"{len(rows)} item row" + ("s" if len(rows) != 1 else ""),
            next_action=(
                "register at least two rows — the empty list and the single item are named "
                + "refusals, not special rankings"
            ),
        )


def _check_duplicates(rows: tuple[tuple[str, str], ...]) -> None:
    """Refuse duplicate ids within the payload (exact string equality).

    Purpose: enforce intra-payload uniqueness — the registry's payload-internal
    find-before-create analog.
    Refuses when: an id repeats — naming the id and both positions.
    Re-run: deterministic.
    Touches: nothing (raises before any store write).
    Provenance: R2, scope-synthesis §3.4:153 ("even trusted-source payloads are
    untrusted bytes"), registry-brief §3 validation step 3.
    """
    seen: dict[str, int] = {}
    for position, (item_id, _label) in enumerate(rows):
        first = seen.get(item_id)
        if first is not None:
            raise RegistryRefusedError(
                expected="all item ids unique within the payload",
                found=f"duplicate id '{item_id}' at positions {first}, {position}",
                next_action=(
                    "disambiguate — one id per row; even trusted-source payloads are "
                    + "untrusted bytes"
                ),
            )
        seen[item_id] = position


def _check_operator(operator: object) -> tuple[str, str, frozenset[str]]:
    """Validate the operator declaration; return its validated (id, question, verdicts).

    Purpose: enforce the declaration's form — id/question non-empty stripped
    strings, the verdict set the weak-order triple (the declared default).
    Refuses when: the operator is not an OperatorDeclaration, id/question are
    not non-empty strings, or the verdict set is not the triple.
    Re-run: deterministic.
    Touches: nothing (raises before any store write).
    Provenance: R3/R4, registry-brief §3 validation step 4 (declaration form).
    """
    if not isinstance(operator, OperatorDeclaration):
        raise RegistryRefusedError(
            expected="an OperatorDeclaration (id, question, verdicts)",
            found=f"operator got {operator!r}",
            next_action="the schema is the module's public types (OperatorDeclaration)",
        )
    op_id = _require_text(operator.id, "operator.id")
    op_question = _require_text(operator.question, "operator.question")
    if operator.verdicts != WEAK_ORDER_TRIPLE:
        raise RegistryRefusedError(
            expected="the weak-order triple {prefer-a, prefer-b, tie} (the declared set's default)",
            found=f"{operator.verdicts!r}",
            next_action=(
                "omit the set for the default, or declare the triple — custom sets are "
                + "the F2 deferral's widening path"
            ),
        )
    return op_id, op_question, operator.verdicts


def _require_quorum(quorum: object) -> int:
    """Validate quorum — an integer >= 1 (bool refused), no upper bound.

    Purpose: enforce the quorum-as-data form (R8's default 1; R6's no artificial
    cap — an unreachable quorum is tally's coverage-gate territory).
    Refuses when: quorum is not an int, is a bool, or is < 1.
    Re-run: deterministic.
    Touches: nothing (raises before any store write).
    Provenance: R8/R6, registry-brief §3 validation step 5 (quorum form).
    """
    if isinstance(quorum, bool) or not isinstance(quorum, int) or quorum < 1:
        raise RegistryRefusedError(
            expected="an integer >= 1 (default 1)",
            found=f"{quorum!r}",
            next_action=(
                "pass a positive integer or omit for the default; no upper bound — an "
                + "unreachable quorum is tally's coverage-gate territory, not registration's"
            ),
        )
    return quorum


class Registry:
    """Registry — hold the run manifests; the in-memory manifest store.

    Purpose: hold the run manifests one process mints via register_run, and read
    them back by handle (read_manifest, read_manifest_count).
    Refuses when: register_run refuses (fewer than two rows, duplicate ids,
    malformed rows or declaration, illegal verdict set, illegal quorum) —
    raising RegistryRefusedError BEFORE any manifest lands; read_manifest refuses an
    unknown run_id naming the live handles.
    Re-run: the read ops are pure over the store; register_run is append-only —
    the mint is per-store max+1 in the same synchronous act as the append (the
    atomic-mint window the service tier later wraps in a lock).
    Touches: only its own in-memory manifests — no files, no subprocess, no DB;
    SINGLE-PROCESS by contract (the service tier later owns serialization).
    Provenance: R1/R2/R3/R4/R8, the five-op interface, scope-synthesis PART 3
    §3.2 op 1, registry-brief §3 (Option A — the store-as-parameter container).
    """

    def __init__(self) -> None:
        """Initialize an empty manifest store.

        Purpose: construct the container the caller holds (store-as-parameter;
        never a module-level singleton — test isolation).
        Refuses when: never.
        Re-run: idempotent — a fresh empty store.
        Touches: only its own state.
        Provenance: registry-brief §3 (the container class).
        """
        self._manifests: dict[str, RunManifest] = {}

    def register_run(
        self,
        items: Sequence[Sequence[str] | ItemRow],
        operator: OperatorDeclaration,
        quorum: int = 1,
    ) -> tuple[str, RunManifest, int]:
        """Register the run: validate the payload, mint RUN-{####}, freeze it.

        Purpose: one list, one operator, one sitting (R1) — validate shape →
        cardinality → duplicate ids → declaration form → quorum, mint the handle
        per-store max+1, deep-copy the validated rows into a frozen manifest, and
        return (run_id, manifest, count) — the built-in read-back.
        Refuses when: fewer than two rows; a row is not a 2-tuple or ItemRow; a
        row's id is not a non-empty string or a label is not a string; duplicate
        ids within the payload; the operator's id/question not non-empty strings;
        the verdict set not the weak-order triple; quorum not an integer >= 1 —
        every refusal raises RegistryRefusedError before any byte is stored.
        Re-run: deterministic given the same store state; an identical
        re-registration mints a NEW run (no dedup at the library tier — request
        idempotency is a service-tier concern).
        Touches: only the store's own manifests (the single mutating op).
        Provenance: R1/R2/R3/R4/R8, scope-synthesis PART 3 §3.2 op 1,
        registry-brief §3 (the seven refusal texts verbatim, the mint, the
        copy-in freeze).
        """

        # The deterministic validation order — every refusal raises BEFORE any byte lands.
        rows = _coerce_rows(items)
        _check_cardinality(rows)
        _check_duplicates(rows)
        op_id, op_question, op_verdicts = _check_operator(operator)
        quorum_value = _require_quorum(quorum)
        # The mint + the copy-in freeze, in one synchronous act.
        run_id = _mint_run_id(len(self._manifests))
        frozen_rows = tuple(ItemRow(id=item_id, label=label) for item_id, label in rows)
        manifest = RunManifest(
            run_id=run_id,
            items=frozen_rows,
            operator=OperatorDeclaration(id=op_id, question=op_question, verdicts=frozenset(op_verdicts)),
            quorum=quorum_value,
            registered_at=datetime.now(UTC).isoformat(timespec="microseconds"),
        )
        self._manifests[run_id] = manifest
        return run_id, manifest, len(self._manifests)

    def read_manifest(self, run_id: str) -> RunManifest:
        """Read the manifest by run_id — a pure lookup over the store.

        Purpose: return the frozen manifest a handle names (the surface the
        ground-truth checks and the audit op ride).
        Refuses when: the run_id is not a live handle — naming the live set.
        Re-run: pure — re-reading is stable across calls (the freeze).
        Touches: nothing — a read.
        Provenance: registry-brief §3 (the manifest read op), the five-op
        interface (op 4's read shape), scope-synthesis PART 3 §3.2.
        """
        manifest = self._manifests.get(run_id)
        if manifest is None:
            live = ", ".join(sorted(self._manifests)) if self._manifests else "(none minted yet)"
            raise RegistryRefusedError(
                expected=f"a live RUN-{{####}} handle ({live})",
                found=f"{run_id!r}",
                next_action=(
                    "handles are minted only by register_run; read an existing run or "
                    + "register the payload first"
                ),
            )
        return manifest

    def read_manifest_count(self) -> int:
        """Read the store's manifest count — the mint's read-back.

        Purpose: return how many manifests the store holds.
        Refuses when: never — a count over the store.
        Re-run: pure — stable between registrations.
        Touches: nothing — a read.
        Provenance: registry-brief §3 (the manifest count accessor).
        """
        return len(self._manifests)
```

## Deliverable 2 — tests/test_registry.py (byte-exact; land as the replacement)

```python
# Copyright (C) 2026 Mark Losey. All rights reserved.
"""The registry unit's example tests — the eleven named edges (registry-brief §4)."""

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
    for bad in (
        frozenset({"prefer-a", "prefer-b"}),
        frozenset({"prefer-a", "prefer-b", "tie", "abstain"}),
        frozenset(),
        {"prefer-a", "prefer-b", "tie"},
    ):
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
            registry.register_run([("a", "one"), ("b", "two")], operator=_declaration(), quorum=bad)
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
```

## Deliverable 3 — the replacement steps (each its own single-goal dispatch)

1. Replace src/prioritree/registry.py: patch-delete the landed v1 file (full pre-image as it sits on disk), then patch-create with Deliverable 1's block (count exactly). Expected: byte-identical to the block.
2. Replace tests/test_registry.py: same form with Deliverable 2's block.
3. make dev → uv sync exit 0; dependencies stays [].
4. make test → 13 passed, zero warnings.
5. make lint → All checks passed!
6. make typecheck → 0 errors, 0 warnings, 0 informations.
7. The read-back: both files against this addendum; deltas reported (expected: none).
