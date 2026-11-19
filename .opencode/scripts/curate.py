#!/usr/bin/env python3
"""curate.py — the curate composition's governed mutation engine (Q-CURATE-1).

Leg B of the curate composition (packet the-engine-fix/curate-b,
census-execution route, dispatched 2026-09-28, actor shinko —
research+implementation): leg A landed the manifest declaration
(.opencode/tools/manifest.yaml's curate entry — the four parameters,
the description_fields' boundary language); THIS engine lands against
that surface. The evidence the instrument exists to create:
FR-MEM-0030 — the patch guard refuses census.json while its own
refusal names "curate the census by ruling," a sanctioned route with
no instrument. This file is that instrument.

THE RULED SHAPE (Q-CURATE-1's ruling) — ONE OP (apply), a CQRS COMMAND:
  target   the protected file's path — the surface patch may never touch.
  ruling   the mandatory citation — question id + date + one-line
           summary, carried verbatim from the dispatch; provenance is
           mandatory (a curation without a ruling citation refuses).
  field    the JSON path within the target (a dotted path; field-level
           sets only — not a free-form editor).
  value    the JSON value to set (parsed strictly; must be valid JSON).

THE BOUNDARY INVERTS THE PATCH GUARD (scripts/patch.py::guard_surface):
patch refuses the protected surfaces; curate writes ONLY them — the
generated renders and the census. DERIVATION: the pattern list below
is transcribed from the guard's own taxonomy (PROTECTED_SUFFIXES /
PROTECTED_NAMES / PROTECTED_DIRS, scripts/patch.py lines 71-73, read
2026-09-28) — one source of truth, copied by hand. DRIFT RISK: the two
lists can diverge if the guard's taxonomy changes without this file
following; reconcile at each packet touching either file.

REFUSALS (the doctrine shape — REFUSED / Expected / Found / Next-action;
stdout stays byte-empty on every refusal):
  (a) an UNPROTECTED target refuses — "patch's lane, use patch".
  (b) an APPEND-ONLY LEDGER (chain.jsonl / packets.jsonl /
      friction-ledger.jsonl, or anything under .junro/) refuses —
      "the ledgers' own tools' lane" (the guard's own taxonomy
      verbatim: "a generated render, the census, or an append-only
      ledger" — the third class routes elsewhere).
  (c) a MISSING or EMPTY ruling citation refuses — Ruling 5's
      actor-refusal shape: "a curation without a ruling citation
      refuses, naming the requirement" (the citation rides the
      curation's own output record — the CQRS command character).
  (d) FIELD MINTING is legal (the anchor pin minted born_chain_head —
      the field did not exist before the ruling created it); the
      design choice rides the curation record ("minted" vs "existing").

ATOMICITY (the store-write idiom): tmp+rename with a JSON parse-back of
the tmp file — a failed parse-back refuses, the target byte-untouched.

OUTPUT: the curation record on stdout — target, field, the old value →
the new value, the ruling citation, the timestamp — the read-back the
verification reads.

THE CURATION RECORD'S HOME (the-engine-fix/curate-record, MEDIUM-1's
ruling, 2026-09-28): the record's mandatory ruling citation belongs to
a store, never a terminal — after the atomic write succeeds, the
record ALSO appends as one JSON line to <cwd-tree>/.junro/curations.jsonl,
the friction precedent (a command's provenance rides the tree's own
store). The .junro/ directory is created if absent — mkdir-on-first-
curation, the one legal directory creation (FR-MEM-0036's gap closed
by the instrument that needed it). The stdout record STAYS as the
immediate read-back (the wrapper renders it) — the append is
additional, not a replacement. APPEND-FAILURE SEMANTICS: an append
failure refuses doctrine-shaped AFTER the curation lands, naming that
the curation succeeded but its record did not — the store bytes stand,
the record is the gap (fail-loud, never a silent workaround).

THE ROOT DERIVATION (the-engine-fix/curate-root, 2026-09-28): _cmd_apply
derives the root from the CURRENT WORKING DIRECTORY (Path.cwd(),
resolved), not from __file__ — the wrapper invokes the engine with
cwd = the session's tree, and that tree is the tree the curation
belongs to. REASON (HIGH-1, hyoka's adversarial review): the
byte-faithful tane copy carried hikari's layout assumption —
__file__-derivation resolved to tane/.opencode inside tane's deeper
directory structure, refusing every target outside .opencode/,
including tane's census. LESSON (Q-INHERIT-1): byte-fidelity
requires the per-tree layout check for any path derived from the
invoking file.

Usage:
    uv run python scripts/curate.py apply --target=... --ruling=... \
        --field=... --value=...

Exit codes: 0 = the curation landed (the record on stdout); 1 = a named
refusal (fail-loud, on stderr — including the record-gap refusal: the
curation landed, its durable record did not); 2 = unusable invocation
(argparse).
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from collections.abc import Callable
from datetime import UTC, datetime
from pathlib import Path

# ---------------------------------------------------------------------------
# Protected surfaces — the boundary that INVERTS the patch guard.
# Derivation: transcribed from scripts/patch.py's guard_surface taxonomy
# (PROTECTED_SUFFIXES / PROTECTED_NAMES / PROTECTED_DIRS, lines 71-73,
# read 2026-09-28) — one source of truth, copied by hand. DRIFT RISK:
# these copies can diverge from the guard's taxonomy; reconcile on any
# packet touching either file. RECONCILED 2026-09-28 (packet
# the-engine-fix/guard-scoping): index.md left the flat set — it is
# curatable only under a "clarity-theorem" path component (the render
# home); this packet touched both files (scripts/patch.py and curate.py).
# ---------------------------------------------------------------------------

PROTECTED_SUFFIXES = (".pdf",)
PROTECTED_CURATABLE = {"census.json", "theorem.json"}
PROTECTED_LEDGERS = {"chain.jsonl", "packets.jsonl", "friction-ledger.jsonl"}
PROTECTED_LEDGER_DIRS = (".junro",)


class _FieldError(Exception):
    """The path crosses something a field-level set cannot cross."""


def _refuse(expected: str, found: str, next_action: str) -> int:
    """The doctrine-shaped refusal block on stderr; stdout stays empty."""
    sys.stderr.write(
        "REFUSED\n"
        f"Expected: {expected}\n"
        f"Found: {found}\n"
        f"Next-action: {next_action}\n"
    )
    return 1


def _guard_target(target: Path, root: Path) -> int | None:
    """The inverted guard — ONLY the curatable protected surfaces pass.

    Refusal (a): an unprotected target — patch's lane, use patch.
    Refusal (b): an append-only ledger — the ledgers' own tools' lane
    (the guard's own taxonomy verbatim: "a generated render, the census,
    or an append-only ledger" — the third class routes elsewhere).
    """
    resolved = target.resolve(strict=False)
    try:
        resolved.relative_to(root)
    except ValueError:
        return _refuse(
            expected=f"a target inside the root ({root})",
            found=f"{target} resolves outside it (realpath: {resolved})",
            next_action="confine the curation to the tree it runs in",
        )
    parts = resolved.parts[len(root.parts):]
    if any(part in PROTECTED_LEDGER_DIRS for part in parts):
        return _refuse(
            expected="a curatable protected surface (a render or the census)",
            found=(
                f"{target} sits inside the ledger store "
                f"({', '.join(PROTECTED_LEDGER_DIRS)}) — an append-only ledger"
            ),
            next_action=(
                "the ledgers' own tools' lane — append through the "
                "ledger's own tool, never curate"
            ),
        )
    if target.name in PROTECTED_LEDGERS:
        return _refuse(
            expected="a curatable protected surface (a render or the census)",
            found=(
                f"{target.name} is an append-only ledger — the guard's "
                'taxonomy verbatim: "a generated render, the census, or '
                'an append-only ledger" — the third class routes elsewhere'
            ),
            next_action=(
                "the ledgers' own tools' lane — append through the "
                "ledger's own tool, never curate"
            ),
        )
    if target.suffix in PROTECTED_SUFFIXES or target.name in PROTECTED_CURATABLE:
        return None
    # index.md is CURATABLE only when its path carries a "clarity-theorem"
    # component (the render home — it's a render, markdown not JSON, so the
    # JSON parse refuses anyway, but the admission vocabulary tells the
    # truth); everywhere else index.md is NOT a protected surface —
    # refusal (a): patch's lane. (packet the-engine-fix/guard-scoping,
    # 2026-09-28 — this packet touched both files.)
    if target.name == "index.md" and "clarity-theorem" in parts:
        return None
    return _refuse(
        expected="a protected surface (a generated render, the census)",
        found=f"{target.name} is not a protected surface — patch's lane",
        next_action="use patch — curate writes ONLY what patch may never touch",
    )


def _require_ruling(raw: str | None) -> int | None:
    """Refusal (c) — Ruling 5's actor-refusal shape, named."""
    if raw is None or not raw.strip():
        return _refuse(
            expected=(
                "a ruling citation — question id + date + one-line summary, "
                "carried verbatim from the dispatch"
            ),
            found="no ruling citation (missing or empty)",
            next_action=(
                "a curation without a ruling citation refuses, naming the "
                "requirement — pass --ruling with the citation verbatim"
            ),
        )
    return None


def _set_field(
    doc: dict[str, object],
    segments: list[str],
    value: object,
) -> tuple[dict[str, object], object, bool]:
    """The field-level set at the dotted path.

    MINTING IS LEGAL (the design choice): the anchor pin minted
    born_chain_head — the field did not exist before the ruling created
    it — so a missing leaf field is MINTED, not refused; a missing
    intermediate is minted as an object; an existing intermediate that
    is not an object refuses (the path crosses a scalar). The design
    choice rides the curation record ("minted" vs "existing").
    """
    node = doc
    for segment in segments[:-1]:
        child = node.get(segment)
        if child is None:
            child = {}
            node[segment] = child
        elif not isinstance(child, dict):
            raise _FieldError(f"the path crosses a non-object at '{segment}'")
        node = child
    leaf = segments[-1]
    minted = leaf not in node
    old = node.get(leaf)
    node[leaf] = value
    return doc, old, minted


def _write_atomic(target: Path, doc: object) -> int | None:
    """tmp+rename with a JSON parse-back — a failed parse-back refuses,
    the target byte-untouched (the store-write idiom)."""
    text = json.dumps(doc, indent=2, ensure_ascii=False) + "\n"
    tmp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", dir=target.parent, delete=False, suffix=".tmp"
        ) as handle:
            handle.write(text)
            tmp_path = Path(handle.name)
        reparsed = json.loads(tmp_path.read_text(encoding="utf-8"))
        if reparsed != doc:
            raise ValueError("the parse-back does not match the payload")
        os.replace(tmp_path, target)
        return None
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        if tmp_path is not None and tmp_path.exists():
            tmp_path.unlink()
        return _refuse(
            expected="an atomic write whose parse-back matches the payload",
            found=f"the parse-back failed: {exc} — the target is byte-untouched",
            next_action="retry the curation; if it persists, inspect the target",
        )


def _append_record(root: Path, record: dict[str, object]) -> int | None:
    """The record's durable home — one JSON line per curation, appended
    to <root>/.junro/curations.jsonl (MEDIUM-1's ruled home; the friction
    precedent: the friction ledger's own open-append shape).
    mkdir-on-first-curation — the one legal directory creation.
    Fail-loud AFTER the curation lands: an append failure refuses,
    naming that the curation succeeded but its record did not — the
    store bytes stand, the record is the gap."""
    store_dir = root / ".junro"
    line = json.dumps(record, ensure_ascii=False) + "\n"
    try:
        store_dir.mkdir(exist_ok=True)
        with (store_dir / "curations.jsonl").open("a", encoding="utf-8") as handle:
            handle.write(line)
        return None
    except OSError as exc:
        return _refuse(
            expected=(
                "the curation record appended to its durable home "
                f"({store_dir / 'curations.jsonl'})"
            ),
            found=(
                f"the append failed: {exc} — the curation itself SUCCEEDED "
                "(the target's new bytes stand) but its record did not land"
            ),
            next_action=(
                "the store bytes stand, the record is the gap — inspect the "
                "store directory, then re-record this curation by hand"
            ),
        )


def _cmd_apply(args: argparse.Namespace) -> int:
    # cwd = the session's tree (the wrapper invokes with cwd set there) —
    # the __file__-derivation was the layout assumption HIGH-1 broke;
    # see the docstring's THE ROOT DERIVATION paragraph.
    root = Path.cwd().resolve()
    target = Path(str(args.target))
    guard = _guard_target(target, root)
    if guard is not None:
        return guard
    ruling = str(args.ruling) if args.ruling is not None else ""
    ruling_refusal = _require_ruling(ruling)
    if ruling_refusal is not None:
        return ruling_refusal
    try:
        doc = json.loads(target.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return _refuse(
            expected="an existing protected target to curate",
            found=f"{target} does not exist",
            next_action="create the target through its own lifecycle first",
        )
    except json.JSONDecodeError as exc:
        return _refuse(
            expected="a JSON document at the target",
            found=f"{target} does not parse as JSON: {exc}",
            next_action="repair the target's JSON before curating it",
        )
    if not isinstance(doc, dict):
        return _refuse(
            expected="a JSON object at the target's root",
            found=f"{target}'s root is {type(doc).__name__}, not an object",
            next_action="field-level sets land in an object — repair the target",
        )
    try:
        value = json.loads(str(args.value))
    except json.JSONDecodeError:
        return _refuse(
            expected="value as a JSON value (quoted strings, real numbers)",
            found=f"value='{args.value}' — not parseable as JSON",
            next_action="pass the value the ruling names, as strict JSON",
        )
    segments = [s for s in str(args.field).split(".") if s]
    if not segments:
        return _refuse(
            expected="a non-empty dotted field path",
            found=f"field='{args.field}' — empty",
            next_action="pass the JSON path within the target (field-level sets only)",
        )
    try:
        doc, old, minted = _set_field(doc, segments, value)
    except _FieldError as exc:
        return _refuse(
            expected="a field path whose intermediates are JSON objects",
            found=str(exc),
            next_action=(
                "adjust the field path — field-level sets only, "
                "not a free-form editor"
            ),
        )
    write_refusal = _write_atomic(target, doc)
    if write_refusal is not None:
        return write_refusal
    record = {
        "op": "apply",
        "target": str(target),
        "field": str(args.field),
        "old": None if minted else old,
        "new": value,
        "field_status": "minted" if minted else "existing",
        "ruling": ruling,
        "timestamp": datetime.now(UTC).isoformat(timespec="seconds"),
    }
    append_refusal = _append_record(root, record)
    if append_refusal is not None:
        return append_refusal
    print(json.dumps(record, indent=2, ensure_ascii=False))
    return 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="curate.py",
        description=(
            "the governed mutation verb for protected surfaces (Q-CURATE-1) "
            "— one op (apply): a field-level set at a JSON path within a "
            "protected target, provenance mandatory"
        ),
    )
    subparsers = parser.add_subparsers(
        dest="subcommand", required=True, metavar="<subcommand>"
    )
    sub = subparsers.add_parser(
        "apply",
        help=(
            "execute exactly a ruling — set one field at a JSON path "
            "within a protected target, provenance mandatory"
        )
    )
    sub.add_argument("--target", required=True, help="the protected file's path")
    sub.add_argument(
        "--ruling",
        # NOT argparse-required: a missing citation must fire refusal (c),
        # the doctrine shape, not an exit-2 invocation error
        required=False,
        default=None,
        help="the mandatory citation — question id + date + one-line summary",
    )
    sub.add_argument("--field", required=True, help="the JSON path within the target (dotted)")
    sub.add_argument("--value", required=True, help="the JSON value to set (strict JSON)")
    sub.set_defaults(handler=_cmd_apply)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    handler: Callable[[argparse.Namespace], int] = args.handler
    return handler(args)


if __name__ == "__main__":
    sys.exit(main())
