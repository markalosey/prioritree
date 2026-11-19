#!/usr/bin/env python3
"""friction_ledger.py — the member-facing friction ledger engine (packets CF-3 + CF-3b).

The system's sensory surface, mechanized: structured, self-reported friction —
at experience time, from the member's seat — processable for triage, response,
and FMEA analysis. The LEDGER is one global project-level JSONL file whose path
is an implementation detail INVISIBLE to members: every operation routes
through the tool from day one (the chmod-defense category eliminated BY
ABSTRACTION — there is no file surface to defend), and no delete op exists, so
append-only is a property of the op set, not of filesystem permissions.

STORAGE (packet CF-3b — the git-as-memory doctrine correction): the ledger is
the TEAM'S RECORD — CENTRAL, GIT-TRACKED, NEVER GITIGNORED. One store at the
MAIN clone's path (.plans/state/friction-ledger.jsonl — the live-state home,
CURRENT.md's family), derived via `git rev-parse --git-common-dir` (the cgc
_derive_context pattern); every session — main-clone or worktree — writes THE
ONE FILE (worktree sessions writing main's tracked file is BY DESIGN: the
record accrues; the landing/commit rhythm is the checkpoint mechanism — the
plan/subtask system's own shape). This is the fork defect's death: CF-3's
repo-relative default resolved against the engine's own tree, so the worktree
seat's copy froze at 3 entries while main's accrued 4 — two divergent stores
of one record, a duplicate-handle mint waiting to happen.

THE CF-3b ENTRY-FORMAT ADDITIONS (both cheap now, expensive to backfill;
minted on EVERY new write — friction, proposals, triage, voids, decisions —
and OPTIONAL-at-read: the fold tolerates their absence in pre-CF-3b entries):
  timestamp     the full write timestamp (ISO 8601 with time, UTC) — the
                merge-order key the future multi-source case needs.
  tree_origin   the WRITING session's tree ("main" for main-clone sessions,
                the worktree slug otherwise) — minted from the engine's own
                checkout facts (per-root derivation for PROVENANCE, common-dir
                derivation for STORAGE — both live in _context()).

The engine class (plain unmanaged, the cgc/symbol_lookup engine pattern): the
generated wrapper (.opencode/tools/friction.ts, emitted by
scripts/generation/generate_tools.py from the manifest row — the write-capable
internal-class render's first adopter) invokes THIS script's subcommands with
--flag=value argv; the wrapper forwards ops, never paths (the path lives ONLY
here — single-sourced; no wrapper change rode CF-3b). The engine owns the
schema validation, the id minting, the registry governance, and the refusals.
Fail-loud everywhere (named errors, the bad field named; never a silent drop)
— an empty result is distinguishable from an error by construction.
Deterministic (INV-H3: no LLM, no network, no git mutation); same input + same
ledger state -> same behavior; the ledger file is the only mutable state.

DATA MODEL (append-only JSONL; state is a FOLD over the file, never a rewrite):
  line kinds:
    friction            a reported friction entry — carries the FR-{NS}-{####}
                        handle, the two governed axes (friction_type = the
                        EXPERIENCE's class; failure_mode = the FAILURE's
                        mechanism), the verbatim attempted/happened/workaround
                        fields, and the member's cause EXPLICITLY labeled as a
                        hypothesis at render (the two-classes ruling: facts vs
                        hypotheses are labeled, never mixed).
    mode / namespace    registry entries: STAGED proposals (propose-mode /
                        propose-namespace — candidate vocabulary, NOT
                        ratified; the earning model applied to vocabulary).
    mode_decision /    triage's registry verdicts: ratified | rejected (a
    namespace_decision   staged proposal + a ratified decision -> ratified).
    triage              a status/disposition/retro_candidate event on a handle
                        (the effective entry state is the LAST event's values;
                        write-time state is "open" by construction).
    void                retires a handle permanently (GitHub semantics: gaps
                        visible, the number never reused — minting counts
                        every minted handle, voided or not; renumbering is the
                        citation-breaking class).
  the seed registries are ENGINE-DECLARED DATA (spec-ruled: "declared as data
  in the engine or a seed file") — the five ratified failure modes born at
  CF-3 (capability-loss/missing, data-gap, interface-cost, discoverability,
  ceremony-cost) and the member-reporting namespace MEM; extendable ONLY
  through the gate (propose -> triage ratify). Read ops never create the file;
  the seeds surface regardless of its existence.

IDS (rikai's research, adopted): one stored, tool-minted sequential handle per
entry — FR-{NS}-{####}, minted from that namespace's ledger content (max+1)
INSIDE the locked append; stored, never renumbered; NO UUID (a distributed-
regime solution bolted onto a single-serializer regime); 4-digit zero-pad
with natural overflow.

OPS (the system's verbs; find mirrors the find tool's grammar):
  read               entries by handle or filter — the known-key lookup.
  find               pattern discovery over entries AND registries (pattern =
                     regex, include = field filter, scope = entries|modes|
                     namespaces); results prefixed with the ledger root + count.
  write              report a friction (schema-validated, both axes governed,
                     id minted) — CREATE only; corrections are new entries
                     referencing the old handle.
  propose-mode /     staging-area writes (candidate vocabulary; land open for
  propose-namespace  coordinator ratification at triage).
  triage             status/disposition updates, mode/namespace RATIFICATION,
                     voiding — the governance half (coordinator-granted).
  NO delete op, by design.

GOVERNANCE (find-before-create, the G1 pattern — the refusal IS the catalog):
  write refuses an unknown friction_type (naming the six legal values), an
  unratified failure_mode (naming the ratified set), and an unregistered
  namespace (naming the registered set); the write NEVER invents vocabulary —
  find discovers the legal sets first, propose-mode/propose-namespace stage a
  candidate, and only triage ratifies it into the set.

Usage:
    uv run python scripts/friction_ledger.py <subcommand> [--flag=value ...]
    (the wrapper invokes exactly this; --ledger overrides the ledger path —
    MAIN-root-relative or absolute, the central-store anchor from every seat —
    for direct runs, probes, and future manifest re-pointing)

Exit codes: 0 = the op succeeded (output on stdout); 1 = a named refusal
(fail-loud, on stderr); 2 = unusable invocation (argparse).
"""

from __future__ import annotations

import argparse
import fcntl
import json
import re
import subprocess
import sys
from collections.abc import Callable
from datetime import UTC, date, datetime
from functools import lru_cache
from pathlib import Path
from typing import Any, NoReturn

# The main-clone live-state home default (packet CF-3b's storage correction —
# the git-as-memory doctrine: the ledger is the TEAM'S record, central and
# git-tracked, never gitignored; .plans/state/ is the live-state family's
# root, CURRENT.md's home, at the MAIN-CLONE state level, not inside one
# research program). Configurable via --ledger (the manifest row's
# internal.fixed_args channel, unused today).
DEFAULT_LEDGER_REL = ".plans/state/friction-ledger.jsonl"


# ---------------------------------------------------------------------------
# The two derivations (packet CF-3b — the cgc _derive_context pattern,
# scripts/code_graph_context.py:211): one git call pair, two anchors.
#   STORAGE   — the common dir's parent (the MAIN clone root): every session,
#               main-clone or worktree, writes THE ONE FILE there (the fork
#               defect's death: a repo-relative default resolved against the
#               engine's own tree, so each checkout held its own "central"
#               store and the record forked — main accrued FR-MEM-0004 while
#               the worktree's copy froze at 0003).
#   PROVENANCE — the engine's own toplevel ("main" when it IS the main clone,
#               the worktree slug otherwise): minted per write as tree_origin.
# ---------------------------------------------------------------------------


def _run_git(args: list[str], cwd: Path) -> str:
    proc = subprocess.run(["git", *args], cwd=str(cwd), capture_output=True, text=True)
    if proc.returncode != 0:
        refuse(
            f"git {' '.join(args)} failed from {cwd} — the ledger derives its storage root "
            f"from the checkout facts and refuses to guess ({proc.stderr.strip()})"
        )
    return proc.stdout.strip()


@lru_cache(maxsize=1)
def _context() -> dict[str, Any]:
    """Derive the storage root + this engine's tree origin from its own
    checkout facts (cwd := the engine file's dir, the cgc pattern; the
    --git-common-dir output resolves against the CHILD cwd it was produced
    from — git prints it relative to the child cwd in the main repo
    ('.git' at the root, '../.git' from scripts/ — measured) and absolute
    from linked worktrees; a parent-cwd resolve forks the storage anchor by
    process cwd, the A2 probe's measured defect)."""
    cwd = Path(__file__).resolve().parent
    toplevel = Path(_run_git(["rev-parse", "--show-toplevel"], cwd=cwd)).resolve()
    common_dir_raw = _run_git(["rev-parse", "--git-common-dir"], cwd=cwd)
    common_dir = (cwd / common_dir_raw).resolve()
    main_root = common_dir.parent
    return {
        "toplevel": toplevel,
        "main_root": main_root,
        # "main" for main-clone sessions (the engine's own tree IS the main
        # clone); the worktree slug otherwise — minted as tree_origin.
        "tree": "main" if toplevel == main_root else toplevel.name,
    }


def _today() -> str:
    return date.today().isoformat()


def _now_iso() -> str:
    """The full write timestamp (ISO 8601 with time, UTC) — the merge-order
    key the future multi-source case needs; minted on every write."""
    return datetime.now(UTC).isoformat(timespec="microseconds")


# --- The governed axes (the schema's fixed vocabulary) ---
FRICTION_TYPES = ("tool-usage", "process-ceremony", "team-delegation", "documentation", "environment", "coordination")
SEVERITIES = ("low", "medium", "high")
DETECTABILITY = ("immediate", "eventual", "hidden")  # the FMEA detection axis
STATUSES = ("open", "triaged", "responded")  # open -> triaged -> responded; updated ONLY by triage

# --- The seed registries (ratified at birth; extendable only through the gate) ---
SEED_FAILURE_MODES = ("capability-loss/missing", "data-gap", "interface-cost", "discoverability", "ceremony-cost")
SEED_NAMESPACES: dict[str, str] = {
    "MEM": "member-reporting — the general namespace for tool/team/process friction (CF-3 seed)",
}

# --- Formats ---
HANDLE_RE = re.compile(r"^FR-([A-Z][A-Z0-9]*)-(\d{4,})$")
MODE_NAME_RE = re.compile(r"^[a-z][a-z0-9/-]*$")  # lowercase tokens (seed 'capability-loss/missing' carries a slash)
NAMESPACE_NAME_RE = re.compile(r"^[A-Z][A-Z0-9]{0,7}$")  # short uppercase tokens (MEM, CL, ...)
DISPOSITION_RE = re.compile(r"^(?:fixed-in-\S+|by-design|earned-later|superseded)$")
ISO_DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# The entry schema's searchable text fields (find's include filter validates
# against these; handle/date/member/session are exposed structurally by
# read/find, never pattern-matched by default).
ENTRY_FIELDS = (
    "friction_type",
    "surface",
    "attempted",
    "happened",
    "workaround",
    "failure_mode",
    "cause",
    "effect",
    "severity",
    "detectability",
)

# The required write fields (member, the two axes, the verbatim pair, the two
# FMEA axes); optional: session, namespace (default MEM), workaround, cause
# (hypothesis-labeled), effect.
WRITE_REQUIRED = (
    "member",
    "friction_type",
    "surface",
    "attempted",
    "happened",
    "failure_mode",
    "severity",
    "detectability",
)


class RefusedError(RuntimeError):
    """A named fail-loud refusal — exit 1, nothing written."""


def refuse(message: str) -> NoReturn:
    raise RefusedError(message)


# ---------------------------------------------------------------------------
# The ledger file (the only mutable state; append-only, locked appends)
# ---------------------------------------------------------------------------


def _ledger_path(cli_value: str | None) -> Path:
    """THE ONE FILE: the default (and any relative --ledger override) anchors
    to the MAIN clone root (the common-dir derivation), never the engine's
    own tree — a worktree session writes the same store a main-clone session
    writes (the fork-defect correction; absolute paths pass through as-is for
    direct/probe runs)."""
    anchor = _context()["main_root"]
    path = Path(cli_value) if cli_value else Path(DEFAULT_LEDGER_REL)
    if not path.is_absolute():
        path = anchor / path
    return path


def _parse_line(line: str, line_no: int, path: Path) -> dict[str, Any]:
    try:
        entry = json.loads(line)
    except json.JSONDecodeError as exc:
        raise RefusedError(
            f"the ledger file {path} carries an unparsable line {line_no} — the ledger is machine-written JSONL; "
            f"refusing to guess over corrupt state ({exc.msg})"
        ) from exc
    if not isinstance(entry, dict) or not isinstance(entry.get("kind"), str):
        raise RefusedError(
            f"the ledger file {path} carries a malformed entry at line {line_no} (no 'kind' string) — "
            "the ledger is machine-written JSONL; refusing to guess over corrupt state"
        )
    return entry


def _parse_all(content: str, path: Path) -> list[dict[str, Any]]:
    return [_parse_line(line, idx, path) for idx, line in enumerate(content.splitlines(), start=1) if line.strip()]


def _read_entries(path: Path) -> list[dict[str, Any]]:
    """Read the ledger under a SHARED lock (a concurrent append never yields a
    torn last line). A missing ledger is an EMPTY ledger (zero entries) — read
    ops never create the file; the seed registries are engine-declared data and
    surface regardless."""
    if not path.is_file():
        return []
    with path.open("r", encoding="utf-8") as fh:
        fcntl.flock(fh.fileno(), fcntl.LOCK_SH)
        try:
            content = fh.read()
        finally:
            fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
    return _parse_all(content, path)


def _locked_append(
    path: Path,
    entries: list[dict[str, Any]],
    validate: Callable[[list[dict[str, Any]]], None],
) -> None:
    """The mutating ops' ONE atomicity primitive: open (create-if-absent)
    under an EXCLUSIVE lock, re-read the current state, run validate(state)
    (a refusal raises BEFORE any byte is written), append the json lines,
    flush, unlock. The mint's max+1 and every find-before-create check run
    over the state read INSIDE this window — validation and append are atomic
    (the single-serializer regime's whole point)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a+", encoding="utf-8") as fh:
        fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
        try:
            fh.seek(0)
            state = _parse_all(fh.read(), path)
            validate(state)
            fh.seek(0, 2)  # end
            for entry in entries:
                fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
            fh.flush()
        finally:
            fcntl.flock(fh.fileno(), fcntl.LOCK_UN)


# ---------------------------------------------------------------------------
# The folds (effective state is computed, never stored twice)
# ---------------------------------------------------------------------------


def _registry_state(
    entries: list[dict[str, Any]],
    kind: str,
    seeds: dict[str, str] | tuple[str, ...],
) -> dict[str, dict[str, Any]]:
    """The effective registry: engine seeds (ratified at birth) + the file's
    staged proposals + the triage decisions (a staged proposal with a decision
    entry moves to that decision; the LAST decision wins; a name without a
    decision keeps its entry status)."""
    names: dict[str, dict[str, Any]] = {}
    if isinstance(seeds, dict):
        for name, purpose in seeds.items():
            names[name] = {"status": "ratified", "seed": True, "purpose": purpose}
    else:
        for name in seeds:
            names[name] = {"status": "ratified", "seed": True}
    for e in entries:
        if e.get("kind") == kind:
            names[str(e.get("name", ""))] = {**e, "status": str(e.get("status", "staged")), "seed": False}
    for e in entries:
        if e.get("kind") == f"{kind}_decision":
            name = str(e.get("name", ""))
            target = names.get(name)
            if target is None:
                # A decision naming an unknown member is corrupt state — fail loud.
                raise RefusedError(
                    f"a {kind}_decision entry names registry member '{name}' that no entry or seed declares — "
                    "refusing to fold corrupt ledger state"
                )
            target["status"] = str(e.get("decision", ""))
    return names


def _triage_folds(entries: list[dict[str, Any]]) -> tuple[dict[str, dict[str, Any]], set[str]]:
    """The per-handle folds: the LAST triage event's status/disposition/
    retro_candidate win (write-time state is open by construction), and the
    void set retires handles permanently."""
    triage: dict[str, dict[str, Any]] = {}
    voided: set[str] = set()
    for e in entries:
        kind = e.get("kind")
        if kind == "triage":
            current = triage.setdefault(str(e.get("handle", "")), {})
            for field in ("status", "disposition", "retro_candidate"):
                if field in e:
                    current[field] = e[field]
        elif kind == "void":
            voided.add(str(e.get("handle", "")))
    return triage, voided


def _friction_entries(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [e for e in entries if e.get("kind") == "friction"]


def _next_handle(entries: list[dict[str, Any]], namespace: str) -> str:
    """Per-namespace max+1 over every minted handle (VOIDED INCLUDED — a
    voided handle's number retires with it, GitHub semantics; the mint never
    reuses a number). 4-digit zero-pad, natural overflow."""
    max_num = 0
    for e in _friction_entries(entries):
        m = HANDLE_RE.match(str(e.get("handle", "")))
        if m and m.group(1) == namespace:
            max_num = max(max_num, int(m.group(2)))
    return f"FR-{namespace}-{max_num + 1:04d}"


# ---------------------------------------------------------------------------
# Validation (fail-loud; the bad field named; the legal sets named)
# ---------------------------------------------------------------------------


def _req_text(args: argparse.Namespace, field: str) -> str:
    value = getattr(args, field, None)
    if not isinstance(value, str) or not value.strip():
        refuse(
            f"field '{field}' is required and must be a non-empty string (got {value!r}) — the report is malformed; "
            "the schema is the op's help text (operation: help)"
        )
    return value.strip()


def _opt_text(args: argparse.Namespace, field: str) -> str | None:
    value = getattr(args, field, None)
    if value is None:
        return None
    if not isinstance(value, str) or not value.strip():
        refuse(f"field '{field}' is optional but, when given, must be a non-empty string (got {value!r})")
    return value.strip()


def _validate_enum(value: str, legal: tuple[str, ...], field: str, what: str) -> str:
    if value not in legal:
        refuse(
            f"field '{field}': unknown {what} '{value}' — the legal set is: {', '.join(legal)} "
            "(find-before-create: discover the legal set with find, never invent vocabulary)"
        )
    return value


def _validate_date(value: str, field: str) -> str:
    if not ISO_DATE_RE.fullmatch(value):
        refuse(f"field '{field}': '{value}' is not an ISO date (YYYY-MM-DD)")
    return value


def _validate_handle(handle: str) -> str:
    if HANDLE_RE.fullmatch(handle) is None:
        refuse(
            f"field 'handle': '{handle}' is not a friction handle — the format is FR-{{NAMESPACE}}-{{####}} "
            "(e.g. FR-MEM-0001); discover handles with read/find"
        )
    return handle


def _validate_failure_mode(mode: str, modes: dict[str, dict[str, Any]]) -> str:
    info = modes.get(mode)
    if info is None:
        ratified = [n for n, i in modes.items() if i["status"] == "ratified"]
        refuse(
            f"field 'failure_mode': '{mode}' is NOT in the ratified set — the ratified failure modes are: "
            f"{', '.join(ratified)} (find-before-create, the G1 pattern: this refusal IS the catalog; a new mode "
            "starts as a STAGED proposal via propose-mode and enters the set only when triage ratifies it)"
        )
    status = str(info["status"])
    if status == "staged":
        refuse(
            f"field 'failure_mode': '{mode}' is STAGED (a proposal awaiting triage ratification), not ratified — "
            "write accepts only ratified modes; discover the ratified set with find (scope=modes)"
        )
    if status == "rejected":
        refuse(
            f"field 'failure_mode': '{mode}' was REJECTED at triage — it is not in the ratified set; "
            "the coordinator owns re-opening rejected vocabulary"
        )
    if status != "ratified":  # defensive: the fold produces exactly the four states
        refuse(f"field 'failure_mode': '{mode}' carries unknown registry status '{status}'")
    return mode


def _validate_namespace(namespace: str, namespaces: dict[str, dict[str, Any]]) -> str:
    info = namespaces.get(namespace)
    if info is None:
        registered = sorted(n for n, i in namespaces.items() if i["status"] == "ratified")
        refuse(
            f"field 'namespace': '{namespace}' is NOT registered — the registered namespaces are: "
            f"{', '.join(registered)} (a new namespace starts as a STAGED proposal via propose-namespace "
            "and enters the registry only when triage ratifies it)"
        )
    status = str(info["status"])
    if status != "ratified":
        refuse(
            f"field 'namespace': '{namespace}' is {status.upper()} (a proposal), not registered — "
            "write records only into registered namespaces"
        )
    return namespace


# ---------------------------------------------------------------------------
# Rendering (read/find output; the ledger root prefix — the find visibility
# precedent: a wrong-file answer is visible, never silent)
# ---------------------------------------------------------------------------


def _entry_summary(e: dict[str, Any], status: str) -> str:
    return f"[{status}] {e.get('friction_type')}/{e.get('failure_mode')} — {e.get('surface')}"


def _render_entry(handle: str, e: dict[str, Any], voided: bool) -> list[str]:
    status = str(e.get("status", "open"))
    lines = [
        f"{handle} — {status}{' (VOIDED — the number is retired, never reused)' if voided else ''}",
        f"  date: {e.get('date')}   member: {e.get('member')}   session: {e.get('session', '')}",
    ]
    # The CF-3b provenance pair: shown when present; pre-CF-3b entries (the
    # fields are optional-at-read) render the honest absence marker.
    if e.get("timestamp") is not None or e.get("tree_origin") is not None:
        lines.append(
            f"  written: {e.get('timestamp', '(not minted — pre-CF-3b entry)')}   "
            f"tree_origin: {e.get('tree_origin', '(not minted — pre-CF-3b entry)')}"
        )
    lines.extend(
        [
            f"  friction_type: {e.get('friction_type')}   failure_mode: {e.get('failure_mode')}",
            f"  surface: {e.get('surface')}",
            f"  attempted: {e.get('attempted')}",
            f"  happened: {e.get('happened')}",
        ]
    )
    if e.get("workaround"):
        lines.append(f"  workaround: {e['workaround']}")
    lines.append(f"  cause (hypothesis): {e.get('cause', '(none offered)')}")
    if e.get("effect"):
        lines.append(f"  effect: {e['effect']}")
    lines.append(f"  severity: {e.get('severity')}   detectability: {e.get('detectability')}")
    lines.append(f"  status: {status}   disposition: {e.get('disposition', '(unset — set at triage)')}")
    retro = e.get("retro_candidate")
    lines.append(f"  retro_candidate: {retro if retro is not None else '(unset — set at triage)'}")
    return lines


def _render_registry(
    names: dict[str, dict[str, Any]],
    label: str,
    pattern: re.Pattern[str] | None,
    extra_text: dict[str, str] | None = None,
) -> tuple[list[str], int]:
    """Render one registry (modes or namespaces) — every member listed when no
    pattern is active (the catalog is the discovery surface); matching members
    only when one is. extra_text: name -> additional searchable text (rationale/
    purpose)."""
    extra_text = extra_text or {}
    counts = {s: sum(1 for i in names.values() if i["status"] == s) for s in ("ratified", "staged", "rejected")}
    lines = [f"{label}: {counts['ratified']} ratified, {counts['staged']} staged, {counts['rejected']} rejected"]
    matches = 0
    for name in sorted(names):
        info = names[name]
        if pattern is not None and pattern.search(name + " " + extra_text.get(name, "")) is None:
            continue
        matches += 1
        marker = "  <- match" if pattern is not None else ""
        if info.get("seed"):
            lines.append(f"  {name} — {info['status']} (seed, ratified at birth){marker}")
        else:
            detail = extra_text.get(name, "")
            lines.append(f"  {name} — {info['status']}{f' — {detail}' if detail else ''}{marker}")
    if pattern is not None and matches == 0:
        lines.append("  (no matches)")
    return lines, matches


def _findable_body(e: dict[str, Any], include: list[str] | None) -> str:
    """The entry text find's pattern runs over: the include fields when given
    (validated against the schema), else every searchable field."""
    fields = include if include is not None else list(ENTRY_FIELDS)
    return " ".join(str(e.get(f, "")) for f in fields)


def _effective(e: dict[str, Any], triage: dict[str, dict[str, Any]]) -> dict[str, Any]:
    """The rendered entry = the stored entry folded with its triage events."""
    merged = dict(e)
    t = triage.get(str(e.get("handle", "")), {})
    merged["status"] = t.get("status", "open")
    if "disposition" in t:
        merged["disposition"] = t["disposition"]
    if "retro_candidate" in t:
        merged["retro_candidate"] = t["retro_candidate"]
    return merged


# ---------------------------------------------------------------------------
# Ops
# ---------------------------------------------------------------------------


def op_read(args: argparse.Namespace) -> str:
    path = _ledger_path(args.ledger)
    entries = _read_entries(path)
    triage, voided = _triage_folds(entries)
    frictions = [_effective(e, triage) for e in _friction_entries(entries)]

    if args.handle:
        _validate_handle(args.handle)
        found = [e for e in frictions if e.get("handle") == args.handle]
        if not found:
            refuse(
                f"no entry '{args.handle}' in the ledger ({len(frictions)} entries total) — a handle is minted only "
                "by write; discover handles with find (a pattern over entry text) or read (filters)"
            )
        e = found[0]
        lines = [f"ledger root: {path}", f"read '{args.handle}' — 1 entry"]
        lines.extend(_render_entry(args.handle, e, args.handle in voided))
        return "\n".join(lines)

    # Filters (each validated against its legal set; the status filter matches
    # the FOLD's effective status, never a stored one).
    flt: list[tuple[str, str]] = []
    if args.friction_type:
        flt.append(
            ("friction_type", _validate_enum(args.friction_type, FRICTION_TYPES, "friction_type", "friction_type"))
        )
    if args.failure_mode:
        flt.append(("failure_mode", args.failure_mode))
    if args.severity:
        flt.append(("severity", _validate_enum(args.severity, SEVERITIES, "severity", "severity")))
    if args.status:
        flt.append(("status", _validate_enum(args.status, STATUSES, "status", "status")))
    if args.member:
        flt.append(("member", args.member))
    if args.date_from:
        flt.append(("date>=", _validate_date(args.date_from, "date_from")))
    if args.date_to:
        flt.append(("date<=", _validate_date(args.date_to, "date_to")))

    matched: list[tuple[str, dict[str, Any]]] = []
    for e in frictions:
        ok = True
        for field, value in flt:
            if field == "date>=" and str(e.get("date", "")) < value:
                ok = False
                break
            if field == "date<=" and str(e.get("date", "")) > value:
                ok = False
                break
            if field in ("friction_type", "failure_mode", "severity", "status", "member") and e.get(field) != value:
                ok = False
                break
        if ok:
            matched.append((str(e.get("handle", "")), e))

    lines = [f"ledger root: {path}", f"read — {len(matched)} of {len(frictions)} entries match the filters"]
    if not matched and flt:
        lines.append(
            "  (no entries match; an empty result is NOT an error — loosen a filter, or find (pattern) to discover)"
        )
    for handle, e in matched:
        lines.append("")
        lines.extend(_render_entry(handle, e, handle in voided))
    return "\n".join(lines)


def op_find(args: argparse.Namespace) -> str:
    path = _ledger_path(args.ledger)
    try:
        pattern = re.compile(args.pattern)
    except re.error as exc:
        refuse(f"field 'pattern': '{args.pattern}' is not a valid regex — {exc}")

    scope = args.scope
    include: list[str] | None = None
    if args.include:
        if scope not in (None, "entries"):
            refuse(
                f"field 'include': the field filter applies to the ENTRIES scope only (scope is '{scope}') — "
                "include names entry fields (e.g. 'surface,attempted')"
            )
        include = []
        for field in args.include.split(","):
            field = field.strip()
            if field not in ENTRY_FIELDS:
                refuse(
                    f"field 'include': '{field}' is not a searchable entry field — the searchable fields are: "
                    f"{', '.join(ENTRY_FIELDS)}"
                )
            include.append(field)

    entries = _read_entries(path)
    triage, voided = _triage_folds(entries)
    frictions = [_effective(e, triage) for e in _friction_entries(entries)]
    modes = _registry_state(entries, "mode", SEED_FAILURE_MODES)
    namespaces = _registry_state(entries, "namespace", SEED_NAMESPACES)

    mode_extra = {str(e["name"]): str(e.get("rationale", "")) for e in entries if e.get("kind") == "mode"}
    ns_extra = {str(e["name"]): str(e.get("purpose", "")) for e in entries if e.get("kind") == "namespace"}

    lines = [f"ledger root: {path}"]
    total = 0

    if scope in (None, "entries"):
        hits = [
            (str(e.get("handle", "")), e) for e in frictions if pattern.search(_findable_body(e, include)) is not None
        ]
        total += len(hits)
        lines.append(
            f"entries: {len(hits)} match '{args.pattern}'" + (f" (fields: {', '.join(include)})" if include else "")
        )
        for handle, e in hits:
            void_mark = " VOIDED" if handle in voided else ""
            lines.append(f"  {handle} {_entry_summary(e, str(e['status']))}{void_mark}")
        if not hits:
            lines.append("  (no matches)")

    if scope in (None, "modes"):
        reg_lines, matches = _render_registry(modes, "modes", pattern, mode_extra)
        total += matches
        lines.extend(reg_lines)

    if scope in (None, "namespaces"):
        reg_lines, matches = _render_registry(namespaces, "namespaces", pattern, ns_extra)
        total += matches
        lines.extend(reg_lines)

    lines.insert(1, f"find '{args.pattern}' — {total} match(es) total")
    if total == 0:
        lines.append("No matches.")
    return "\n".join(lines)


def op_write(args: argparse.Namespace) -> str:
    path = _ledger_path(args.ledger)
    fields: dict[str, Any] = {}
    for field in WRITE_REQUIRED:
        fields[field] = _req_text(args, field)
    for field in ("session", "workaround", "cause", "effect"):
        value = _opt_text(args, field)
        if value is not None:
            fields[field] = value
    fields["friction_type"] = _validate_enum(fields["friction_type"], FRICTION_TYPES, "friction_type", "friction_type")
    fields["severity"] = _validate_enum(fields["severity"], SEVERITIES, "severity", "severity")
    fields["detectability"] = _validate_enum(fields["detectability"], DETECTABILITY, "detectability", "detectability")
    namespace = (args.namespace or "MEM").strip()
    fields["namespace"] = namespace

    tree = _context()["tree"]
    entry: dict[str, Any] = {
        "kind": "friction",
        "date": _today(),
        **fields,
        # CF-3b provenance pair: ALWAYS minted on new writes (optional-at-read
        # — the fold tolerates their absence in pre-CF-3b entries).
        "tree_origin": tree,
        "timestamp": _now_iso(),
    }
    minted: dict[str, str] = {}

    def _validate_and_mint(state: list[dict[str, Any]]) -> None:
        """Runs INSIDE the locked append's window: both governed axes against
        the fresh registry fold, then the mint — atomic with the write."""
        modes = _registry_state(state, "mode", SEED_FAILURE_MODES)
        namespaces = _registry_state(state, "namespace", SEED_NAMESPACES)
        _validate_failure_mode(str(entry["failure_mode"]), modes)
        _validate_namespace(str(entry["namespace"]), namespaces)
        entry["handle"] = _next_handle(state, str(entry["namespace"]))
        minted["handle"] = str(entry["handle"])

    _locked_append(path, [entry], _validate_and_mint)

    handle = minted["handle"]
    return (
        f"recorded {handle} (status open)\n"
        f"  reported by {entry['member']} on {entry['date']} from tree {tree} at {entry['timestamp']} — "
        f"{entry['friction_type']} / {entry['failure_mode']} "
        f"(severity {entry['severity']}, detectability {entry['detectability']})\n"
        f"  read it back: read handle={handle} — corrections are NEW entries referencing {handle} (no edit, no delete)"
    )


def _propose(
    args: argparse.Namespace,
    kind: str,
    name_re: re.Pattern[str],
    extra_field: str,
    what: str,
) -> str:
    path = _ledger_path(args.ledger)
    name = _req_text(args, "mode" if kind == "mode" else "namespace")
    extra = _req_text(args, extra_field)
    member = _opt_text(args, "member") or "(unattributed)"
    name_hint = (
        "lowercase tokens (hyphens/slashes allowed, e.g. data-gap)"
        if kind == "mode"
        else "a short UPPERCASE token (e.g. MEM, CL)"
    )
    if not name_re.fullmatch(name):
        refuse(
            f"field '{'mode' if kind == 'mode' else 'namespace'}': '{name}' is not a well-formed "
            f"{what} name ({name_hint})"
        )

    entry: dict[str, Any] = {
        "kind": kind,
        "name": name,
        "status": "staged",
        extra_field: extra,
        "proposed_by": member,
        "date": _today(),
        # CF-3b provenance pair (minted on every write, like the friction kind).
        "tree_origin": _context()["tree"],
        "timestamp": _now_iso(),
    }

    def _validate_find_before_create(state: list[dict[str, Any]]) -> None:
        names = _registry_state(state, kind, SEED_FAILURE_MODES if kind == "mode" else SEED_NAMESPACES)
        info = names.get(name)
        if info is None:
            return  # not present in any state — the proposal is new
        status = str(info["status"])
        if status == "ratified":
            where = " (a seed, ratified at birth)" if info.get("seed") else ""
            refuse(
                f"{what} '{name}' is ALREADY RATIFIED{where} — find-before-create: it is in the legal set; use it "
                f"directly (this refusal IS the catalog; find scope={'modes' if kind == 'mode' else 'namespaces'} "
                "lists it)"
            )
        if status == "staged":
            refuse(
                f"{what} '{name}' is ALREADY STAGED (proposed {info.get('date', '?')}, awaiting triage ratification) "
                "— a duplicate proposal is not a second vote"
            )
        if status == "rejected":
            refuse(
                f"{what} '{name}' was REJECTED at triage — re-opening rejected vocabulary is the coordinator's "
                "(a fresh rationale rides a coordinator ruling, not a re-proposal)"
            )

    _locked_append(path, [entry], _validate_find_before_create)

    return (
        f"staged {what} proposal '{name}' — it is NOT in the ratified set (write still refuses it) until triage "
        f"ratifies it\n  {extra_field}: {extra}\n  proposed by {member} on {entry['date']}; awaiting coordinator "
        f"ratification (triage {'ratify_mode' if kind == 'mode' else 'ratify_namespace'}={name})"
    )


def op_propose_mode(args: argparse.Namespace) -> str:
    return _propose(args, "mode", MODE_NAME_RE, "rationale", "failure mode")


def op_propose_namespace(args: argparse.Namespace) -> str:
    return _propose(args, "namespace", NAMESPACE_NAME_RE, "purpose", "namespace")


def op_triage(args: argparse.Namespace) -> str:
    path = _ledger_path(args.ledger)
    handle_actions: list[tuple[str, Any]] = [
        ("status", args.status),
        ("disposition", args.disposition),
        ("retro_candidate", args.retro_candidate),
        ("void_reason", args.void_reason),
    ]
    registry_actions: list[tuple[str, str, str]] = [
        ("ratify_mode", args.ratify_mode, "mode"),
        ("reject_mode", args.reject_mode, "mode"),
        ("ratify_namespace", args.ratify_namespace, "namespace"),
        ("reject_namespace", args.reject_namespace, "namespace"),
    ]
    any_handle_action = any(v is not None for _, v in handle_actions)
    any_registry_action = any(v is not None for _name, v, _kind in registry_actions)
    if not any_handle_action and not any_registry_action:
        refuse(
            "triage requires an action: status / disposition / retro_candidate / void_reason (handle-scoped) or "
            "ratify_mode / reject_mode / ratify_namespace / reject_namespace (registry verdicts)"
        )

    status = disposition = None
    retro: bool | None = None
    if args.status is not None:
        status = _validate_enum(args.status, STATUSES, "status", "status")
    if args.disposition is not None:
        disposition = args.disposition.strip()
        if not DISPOSITION_RE.fullmatch(disposition):
            refuse(
                f"field 'disposition': '{disposition}' is not a legal disposition — the classes are: "
                "fixed-in-<packet> | by-design | earned-later | superseded"
            )
    if args.retro_candidate is not None:
        if args.retro_candidate not in ("true", "false"):
            refuse("field 'retro_candidate': must be 'true' or 'false'")
        retro = args.retro_candidate == "true"

    if any_handle_action and not args.handle:
        refuse(
            "handle-scoped triage actions (status / disposition / retro_candidate / void_reason) require "
            "the target handle"
        )
    if args.handle:
        _validate_handle(args.handle)
    if args.ratify_mode and args.reject_mode:
        refuse("ratify_mode and reject_mode are mutually exclusive — one verdict per call")
    if args.ratify_namespace and args.reject_namespace:
        refuse("ratify_namespace and reject_namespace are mutually exclusive — one verdict per call")

    pre_state = _read_entries(path)

    def _registry(name: str, kind: str) -> dict[str, dict[str, Any]]:
        return _registry_state(pre_state, kind, SEED_FAILURE_MODES if kind == "mode" else SEED_NAMESPACES)

    def _validate_registry_verdict(name: str, kind: str, decision: str, what: str) -> None:
        names = _registry(name, kind)
        info = names.get(name)
        if info is None:
            refuse(
                f"{what} '{name}' has NO staged proposal to {decision} — proposals come from propose-{kind} "
                "(find-before-create cuts both ways)"
            )
        status = str(info["status"])
        if status == "ratified":
            refuse(
                f"{what} '{name}' is ALREADY RATIFIED{' (a seed)' if info.get('seed') else ''} — nothing to {decision}"
            )
        if status == "rejected":
            refuse(f"{what} '{name}' is already REJECTED — a second verdict is a no-op; re-opening is a fresh ruling")
        if status != "staged":
            refuse(f"{what} '{name}' carries unknown registry status '{status}'")

    if args.ratify_mode:
        _validate_registry_verdict(args.ratify_mode, "mode", "ratify", "failure mode")
    if args.reject_mode:
        _validate_registry_verdict(args.reject_mode, "mode", "reject", "failure mode")
    if args.ratify_namespace:
        _validate_registry_verdict(args.ratify_namespace, "namespace", "ratify", "namespace")
    if args.reject_namespace:
        _validate_registry_verdict(args.reject_namespace, "namespace", "reject", "namespace")

    if any_handle_action:
        frictions = {str(e.get("handle", "")) for e in _friction_entries(pre_state)}
        _, pre_voided = _triage_folds(pre_state)
        if args.handle not in frictions:
            refuse(
                f"field 'handle': '{args.handle}' is not a friction entry in the ledger ({len(frictions)} entries) — "
                "triage acts on minted handles only"
            )
        if args.handle in pre_voided and args.void_reason is not None:
            refuse(
                f"handle '{args.handle}' is ALREADY VOIDED (retired permanently) — a second void is a no-op by "
                "design; the number never comes back"
            )

    # Assemble the append lines + the in-window validation closure.
    to_append: list[dict[str, Any]] = []
    confirmations: list[str] = []

    if any_handle_action:
        if args.void_reason is not None:
            if status is not None or disposition is not None or retro is not None:
                refuse(
                    "void_reason is mutually exclusive with status/disposition/retro_candidate — "
                    "one verdict class per call (the void retires the entry; the other actions "
                    "would be silently dropped)"
                )
            reason = args.void_reason.strip()
            if not reason:
                refuse("field 'void_reason': voiding requires a non-empty reason (the retirement is permanent)")
            to_append.append(
                {
                    "kind": "void",
                    "handle": args.handle,
                    "reason": reason,
                    "date": _today(),
                    "tree_origin": _context()["tree"],
                    "timestamp": _now_iso(),
                }
            )
            confirmations.append(f"VOIDED {args.handle} (retired permanently — the number is never reused): {reason}")
        else:
            triage_entry: dict[str, Any] = {"kind": "triage", "handle": args.handle, "date": _today()}
            parts: list[str] = []
            if status is not None:
                triage_entry["status"] = status
                parts.append(f"status -> {status}")
            if disposition is not None:
                triage_entry["disposition"] = disposition
                parts.append(f"disposition -> {disposition}")
            if retro is not None:
                triage_entry["retro_candidate"] = retro
                parts.append(f"retro_candidate -> {retro}")
            triage_entry["tree_origin"] = _context()["tree"]
            triage_entry["timestamp"] = _now_iso()
            to_append.append(triage_entry)
            confirmations.append(f"TRIAGED {args.handle}: {'; '.join(parts)}")

    if any_registry_action:
        verdicts: list[tuple[str, str, str]] = []  # (name, kind, decision)
        if args.ratify_mode:
            verdicts.append((args.ratify_mode, "mode", "ratified"))
        if args.reject_mode:
            verdicts.append((args.reject_mode, "mode", "rejected"))
        if args.ratify_namespace:
            verdicts.append((args.ratify_namespace, "namespace", "ratified"))
        if args.reject_namespace:
            verdicts.append((args.reject_namespace, "namespace", "rejected"))
        for name, kind, decision in verdicts:
            to_append.append(
                {
                    "kind": f"{kind}_decision",
                    "name": name,
                    "decision": decision,
                    "date": _today(),
                    "tree_origin": _context()["tree"],
                    "timestamp": _now_iso(),
                }
            )
            confirmations.append(
                f"{decision.upper()} {kind} '{name}' — "
                + (
                    "it is NOW in the ratified set (write accepts it)"
                    if decision == "ratified"
                    else "it stays out of the ratified set (write keeps refusing it)"
                )
            )

    def _validate_window(state: list[dict[str, Any]]) -> None:
        """Re-validate against the state read INSIDE the lock (the pre-state
        check was the fast fail; this is the atomic one)."""
        fresh_voided = _triage_folds(state)[1]
        if any_handle_action:
            if args.handle not in {str(e.get("handle", "")) for e in _friction_entries(state)}:
                refuse(
                    f"the ledger moved under this triage (handle '{args.handle}' no longer resolves) — re-run; "
                    "refusing to act on stale state"
                )
            if args.void_reason is not None and args.handle in fresh_voided:
                refuse(f"handle '{args.handle}' was voided concurrently — a second void is a no-op by design")

    _locked_append(path, to_append, _validate_window)

    lines = [f"ledger root: {path}"]
    lines.extend(f"  {c}" for c in confirmations)
    lines.append(f"triage complete — {len(confirmations)} action(s) appended (append-only; the fold is the truth)")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def _add_ledger_arg(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--ledger",
        "--store",
        dest="ledger",
        default=None,
        help="Friction store path override (MAIN-root-relative or absolute — the central "
        "store is anchored to the main clone from every seat; the tane target's team "
        "writes its own store, read from the coordinator's tree through this flag); "
        "default: " + DEFAULT_LEDGER_REL,
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="The member-facing friction ledger engine (packet CF-3)")
    sub = parser.add_subparsers(dest="op", required=True)

    p = sub.add_parser("read", help="Entries by handle or filter (member, type, mode, severity, status, date range)")
    _add_ledger_arg(p)
    p.add_argument("--handle", help="Exact handle lookup (FR-{NS}-{####})")
    p.add_argument("--member", help="Filter: the reporting member")
    p.add_argument("--friction_type", help="Filter: the friction_type axis")
    p.add_argument("--failure_mode", help="Filter: the failure_mode axis")
    p.add_argument("--severity", help="Filter: severity")
    p.add_argument("--status", help="Filter: effective status (open|triaged|responded)")
    p.add_argument("--date_from", help="Filter: entry date >= (YYYY-MM-DD)")
    p.add_argument("--date_to", help="Filter: entry date <= (YYYY-MM-DD)")
    p.set_defaults(func=op_read)

    p = sub.add_parser("find", help="Pattern discovery over entries AND registries (the find tool's grammar)")
    _add_ledger_arg(p)
    p.add_argument("--pattern", required=True, help="Regex over entry text / mode names")
    p.add_argument(
        "--include", help="Comma-separated entry FIELD filter (e.g. 'surface,attempted') — entries scope only"
    )
    p.add_argument("--scope", choices=["entries", "modes", "namespaces"], help="Restrict discovery; omit for all")
    p.set_defaults(func=op_find)

    p = sub.add_parser("write", help="Report a friction (schema-validated; both axes governed; id minted)")
    _add_ledger_arg(p)
    p.add_argument("--member", help="The reporting member's name")
    p.add_argument("--session", help="The reporting member's session id")
    p.add_argument("--namespace", help="The ledger namespace (default MEM; must be registered)")
    p.add_argument("--friction_type", help="The EXPERIENCE's class (the governed type axis)")
    p.add_argument("--surface", help="The specific surface it touched (tool+op, process name, doc path)")
    p.add_argument("--attempted", help="Verbatim — what the member tried")
    p.add_argument("--happened", help="Verbatim — what occurred (the envelope/output, quoted)")
    p.add_argument("--workaround", help="Verbatim — the detour, if any (a workaround is DATA)")
    p.add_argument("--failure_mode", help="The FAILURE's mechanism (the governed mode axis; find-before-create)")
    p.add_argument("--cause", help="The member's HYPOTHESIS, explicitly (labeled at render)")
    p.add_argument("--effect", help="What it cost")
    p.add_argument("--severity", help="low | medium | high")
    p.add_argument("--detectability", help="immediate | eventual | hidden (the FMEA detection axis)")
    p.set_defaults(func=op_write)

    p = sub.add_parser("propose-mode", help="Stage a candidate failure mode (NOT ratified; triage ratifies)")
    _add_ledger_arg(p)
    p.add_argument("--mode", help="The candidate mode name (lowercase tokens)")
    p.add_argument("--rationale", help="Why this mode earns a place in the taxonomy")
    p.add_argument("--member", help="The proposing member's name")
    p.set_defaults(func=op_propose_mode)

    p = sub.add_parser("propose-namespace", help="Stage a candidate namespace (NOT registered; triage ratifies)")
    _add_ledger_arg(p)
    p.add_argument("--namespace", help="The candidate namespace id (short UPPERCASE, e.g. CL)")
    p.add_argument("--purpose", help="What the namespace scopes")
    p.add_argument("--member", help="The proposing member's name")
    p.set_defaults(func=op_propose_namespace)

    p = sub.add_parser("triage", help="Coordinator-granted: status/disposition, ratification, voiding")
    _add_ledger_arg(p)
    p.add_argument("--handle", help="The target handle (handle-scoped actions)")
    p.add_argument("--status", help="New effective status (open|triaged|responded)")
    p.add_argument("--disposition", help="fixed-in-<packet> | by-design | earned-later | superseded")
    p.add_argument("--retro_candidate", help="true | false (the retro bridge — hansei reads the ledger as intake)")
    p.add_argument("--ratify_mode", help="Ratify a staged failure mode into the set")
    p.add_argument("--reject_mode", help="Reject a staged failure mode")
    p.add_argument("--ratify_namespace", help="Ratify a staged namespace into the registry")
    p.add_argument("--reject_namespace", help="Reject a staged namespace")
    p.add_argument("--void_reason", help="Void the handle (retires its number permanently); the required reason")
    p.set_defaults(func=op_triage)

    p = sub.add_parser("union", help="Union the forked friction ledgers (main x the worktree)")
    p.add_argument("--write", help="Apply the union to BOTH trees ('true'; default: dry-run)")
    p.add_argument("--allow_collisions", help="Keep both entries on collisions ('true'; default: refuse, exit 3)")
    p.add_argument("--main_ledger", help="Path override: main's ledger copy")
    p.add_argument("--worktree_ledger", help="Path override: the worktree's ledger copy")
    p.add_argument("--backup_dir", help="The backup directory (default /tmp)")
    p.set_defaults(func=op_union)

    return parser

def op_union(args):
    """Union the forked friction ledgers — delegates to scripts/friction_ledger_union.py.

    The close choreography's governed form (the union-op lane, 2026-11-03): the identical
    prefix kept, the forked suffixes merged timestamp-ordered, handle collisions BOTH-KEPT
    (append-only), containment proven, backups first, both trees written byte-identical.
    The instrument's exit codes ride up (0 ok | 2 corrupt | 3 collisions | 4 containment)
    — SystemExit propagates with them.
    """
    import friction_ledger_union as _flu  # the sibling script (scripts/ on sys.path)

    union_argv: list[str] = []
    if str(args.write or "").strip().lower() in {"1", "true", "yes"}:
        union_argv.append("--write")
    if str(args.allow_collisions or "").strip().lower() in {"1", "true", "yes"}:
        union_argv.append("--allow-collisions")
    if args.main_ledger:
        union_argv += ["--main-ledger", args.main_ledger]
    if args.worktree_ledger:
        union_argv += ["--worktree-ledger", args.worktree_ledger]
    if args.backup_dir:
        union_argv += ["--backup-dir", args.backup_dir]
    _flu.main(union_argv)  # prints the plan + legend; SystemExit carries 0/2/3/4 up
    return ""  # defensive: _flu.main always exits

def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        print(args.func(args))
        return 0
    except RefusedError as exc:
        print(f"friction-ledger: REFUSED — {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
