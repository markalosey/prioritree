#!/usr/bin/env python3
"""patch.py — the mutation tool's engine: apply a unified diff, then check.

The seat's one mutation verb (the patch ruling, 2026-09-27: "by remove I mean
deny" — the packs deny edit/write; a targeted change applies as a unified
diff and the type-appropriate checks ride the SAME output — craftsmanship
as-you-go, the big-pile pattern's death).

STRICT SEMANTICS (Q1's first ruling, tane's store, 2026-09-28 — the lenient
matching cascade was PROPOSED and REVERSED): the patch matches the file
EXACTLY at the stated location or REFUSES. No window search, no global
fallback, no whitespace-normalized tier. Hunk counts are checksums
(malformed patches refuse as parse_error); line numbers are load-bearing,
never hints. already_applied is the sole idempotency path (a re-run of an
applied patch SUCCEEDS as a no-op — Idempotence.SAME_RESULT). Recovery from
a failed match is the CALLER's loop: the refusal carries expected/found/
next-action with the actual current lines as evidence. Errors ride the ruled
ThreePart shape. The name is `patch` (Q1's second ruling: the act-statement
"Patch the tree by verified diff — apply each hunk exactly at its stated
location, or refuse"; [a-z][a-z-]+; the strictness rides the act-statement).

NEW-FILE CREATION (Q-SEATS-1 ruling 12, 2026-09-30, packet
the-seats-migration/patch-tool-fix): the apply path creates ALL directories
in the patch path before write_text (mkdir parents, exist_ok) — a new file
lands through patch even into directories that do not yet exist
(FR-MEM-0097's defect — write_text without parent creation; FR-MEM-0036's
class — the hand-mkdir ceremony — dies at this write path). Hunk semantics
unchanged (FR-MEM-0114 stands): exact post-image counts, and a create
hunk's old side starts at 1 (@@ -1,0 +1,N @@; a -0,0 header refuses).

THE PROTECTED SURFACES (hyoka's surviving blocking conditions): generated
renders (the cycle's .md outputs, theorem.json, the pdf), the census (born
knowledge, collaborator-curated), the store (.junro/**), the append-only
ledgers (chain.jsonl, the friction ledger, packets.jsonl) — patch REFUSES
to mutate them, naming the class. index.md is protected ONLY in its render
home — a path carrying the "clarity-theorem" component (tane's cycle
render, src/tane/genome/clarity-theorem/index.md, beside its census); the
2026-09-28 exemption (the-engine-fix/adversarial's reconciliation ruling —
seven hand-maintained index.md files uneditable through any governed
instrument) lands hyoka's MEDIUM-3 scoping choice: hand-maintained
index.md files are patch's lane. The target's realpath must
resolve inside the root (symlink confinement). EOL mismatch is its own
typed refusal (eol_mismatch), never silently applied. CONCURRENCY: serialized
by the session loop (one mutation per turn); no lock until a real adopter
hits the race (earned abstraction).

THE CHECKS (ride every mutation's output — apply-then-report, never
refuse-on-red; the HARD gates stay at the commit hook and kensho):
  .py -> ruff + pyright | .json/.toml -> the parse check | .ts -> tsc
  .md -> none (the canon cycle governs — and the renders are protected anyway)

Exit codes: 0 = applied (or already_applied no-op), checks clean; 1 = a
refusal (named, nothing applied) or findings riding an applied edit; 2 =
unusable input. Deterministic; no LLM (INV-H3); fixed-argv subprocess only.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tomllib
from pathlib import Path
from typing import Any

_REFUSAL = "REFUSED"


def refuse(expected: str, found: str, next_action: str) -> None:
    """The ruled ThreePart refusal, printed and exited (exit 1)."""
    print(f"{_REFUSAL} — Expected: {expected}")
    print(f"         Found: {found}")
    print(f"         Next-action: {next_action}")
    sys.exit(1)


class PatchError(Exception):
    """Unusable input (parse_error class) — exit 2."""


# ---------------------------------------------------------------------------
# Protected surfaces (hyoka's surviving blocking conditions, as ruled)
# ---------------------------------------------------------------------------

PROTECTED_SUFFIXES = (".pdf",)
PROTECTED_NAMES = {"census.json", "theorem.json", "chain.jsonl", "packets.jsonl", "friction-ledger.jsonl"}
PROTECTED_DIRS = (".junro",)


def guard_surface(path: Path, root: Path) -> None:
    """Refuse mutations to the protected surfaces and outside the root."""
    resolved = path.resolve(strict=False)
    try:
        resolved.relative_to(root)
    except ValueError:
        refuse(
            f"a target inside the root ({root})",
            f"{path} resolves outside it (realpath: {resolved})",
            "fix the diff's paths — the tool confines to the tree it runs in",
        )
    parts = resolved.parts
    if any(part in PROTECTED_DIRS for part in parts[len(root.parts):]):
        refuse(
            "a mutable target (the store is born memory, never patch-mutated)",
            f"{path} sits inside the store",
            "route effort records through the junro tool — the store is protected",
        )
    if path.suffix in PROTECTED_SUFFIXES or path.name in PROTECTED_NAMES:
        refuse(
            "a mutable target",
            f"{path.name} is a protected surface (a generated render, the census, or an append-only ledger)",
            "regenerate renders through the cycle; curate the census by ruling; "
            "append to ledgers through their own tools",
        )
    # index.md is protected ONLY in the render home — the resolved path must
    # carry a "clarity-theorem" component (tane's cycle render lives at
    # src/tane/genome/clarity-theorem/index.md, beside its census; the only
    # index.md the cycle ever emits). Provenance: the 2026-09-28 exemption
    # (the-engine-fix/adversarial's reconciliation ruling — the seven hand-
    # maintained index.md docs uneditable through any governed instrument;
    # the scoping choice lands hyoka's MEDIUM-3). Hand-maintained index.md
    # files are patch's lane.
    if path.name == "index.md" and "clarity-theorem" in parts[len(root.parts):]:
        refuse(
            "a mutable target",
            f"{path.name} is a protected surface (the render-home index.md — "
            "the clarity-theorem component's cycle render)",
            "regenerate renders through the cycle",
        )


# ---------------------------------------------------------------------------
# Diff parsing (strict: counts are checksums; noise ignored)
# ---------------------------------------------------------------------------


def parse_diff(text: str) -> dict[str, Any]:
    """Parse a unified diff. Hunk header counts are VALIDATED as checksums
    (old_count == ' '+'-' lines; new_count == ' '+'+' lines) — a malformed
    patch refuses as parse_error, never a mis-located apply. Deletion lines
    whose content begins with '--- ', '+++ ', or '@@' are distinguished from
    file/hunk headers by hunk-count completeness: while the current hunk
    still requires body lines, such a line is deletion CONTENT, never a
    header (the markdown-list-item class, FR-MEM-0111)."""
    files: dict[str, Any] = {}
    current: dict[str, Any] | None = None
    def _hunk_incomplete(hunk: dict[str, Any]) -> bool:
        """True while the hunk still requires body lines per its declared
        counts — a header-prefixed line during that window is deletion
        CONTENT, never a file/hunk header (the unified-diff ambiguity:
        a deleted line whose file content begins with '--- ', '+++ ', or
        '@@' is otherwise indistinguishable from a header by prefix alone;
        the FR-MEM-0111 markdown-list-item class)."""
        pre_n = sum(1 for tag, _ in hunk["lines"] if tag in (" ", "-"))
        post_n = sum(1 for tag, _ in hunk["lines"] if tag in (" ", "+"))
        return pre_n < hunk["old_count"] or post_n < hunk["new_count"]

    for line in text.splitlines():
        in_hunk = current is not None and bool(current.get("hunks")) and _hunk_incomplete(current["hunks"][-1])
        if not in_hunk and line.startswith("--- "):
            current = {"old": line[4:].strip(), "hunks": []}
            continue
        if not in_hunk and line.startswith("+++ "):
            if current is None:
                raise PatchError(f"+++ header without --- : {line!r}")
            new_path = line[4:].strip()
            current["new"] = new_path
            current["is_new"] = current["old"] == "/dev/null"
            current["is_delete"] = new_path == "/dev/null"
            files[new_path] = current
            continue
        if line.startswith("@@"):
            if current is None:
                raise PatchError(f"hunk header before any file header: {line!r}")
            body = line[3:].split("@@")[0].strip()
            try:
                old_part, new_part = body.split()[:2]
                old_start = int(old_part.split(",")[0].lstrip("-") or "1")
                old_count = int(old_part.split(",")[1]) if "," in old_part else 1
                new_count = int(new_part.split(",")[1]) if "," in new_part else 1
            except (ValueError, IndexError) as exc:
                raise PatchError(f"unparseable hunk header: {line!r}") from exc
            current["hunks"].append(
                {"old_start": old_start, "old_count": old_count, "new_count": new_count, "lines": []}
            )
            continue
        if current is not None and current.get("hunks"):
            if line.startswith((" ", "+", "-")):
                current["hunks"][-1]["lines"].append((line[0], line[1:]))
            elif line == "":
                # a blank context line whose trailing space an editor stripped
                current["hunks"][-1]["lines"].append((" ", ""))
            elif line.startswith("\\"):
                continue  # no-newline marker: content-identical, implicit
            else:
                raise PatchError(f"unexpected diff line: {line!r}")
    if not files:
        raise PatchError("the diff carries no file sections")
    for entry in files.values():
        for hunk in entry["hunks"]:
            pre_n = sum(1 for tag, _ in hunk["lines"] if tag in (" ", "-"))
            post_n = sum(1 for tag, _ in hunk["lines"] if tag in (" ", "+"))
            if pre_n != hunk["old_count"] or post_n != hunk["new_count"]:
                raise PatchError(
                    f"hunk at line {hunk['old_start']} count checksum mismatch: "
                    f"header says -{hunk['old_count']},+{hunk['new_count']} "
                    f"but the body carries {pre_n} pre-image and {post_n} post-image lines"
                )
    return files


def _blocks_of(hunk: dict[str, Any]) -> tuple[list[str], list[str]]:
    """The pre-image (context+removed) and post-image (context+added) blocks."""
    pre = [t for tag, t in hunk["lines"] if tag in (" ", "-")]
    post = [t for tag, t in hunk["lines"] if tag in (" ", "+")]
    return pre, post


def _already_applied(hunk: dict[str, Any], original_lines: list[str], at: int) -> bool:
    """A no-op verdict requires PROOF the change is genuinely present in the
    file on disk — not merely that the post-image can be found at the anchor
    (the FR-MEM-0079/0080 trap: a deletion-only hunk's surviving context IS
    the file's own line, so a post-image slice matches trivially while the
    to-be-deleted content still exists). Per hunk shape:

    - replacement (lines removed AND added): the pre-image absent where the
      hunk acted (the anchor's window) AND the post-image present there.
    - pure insertion (nothing removed): the post-image (context+added)
      present at the stated location.
    - deletion shape (lines removed, none added): the removed lines ABSENT
      from the whole file (an existence search across the file's content,
      not the anchor's window) AND the post-image present at the stated
      location AND the pre-image span the header claims no longer standing
      as live content — a span still intact with non-matching content is a
      stale/drifted diff, which falls through to the strict refusal.
    """
    if at < 0:
        return False  # a garbage anchor is a broken diff — refuse, never no-op
    removed = [t for tag, t in hunk["lines"] if tag == "-"]
    added = [t for tag, t in hunk["lines"] if tag == "+"]
    pre, post = _blocks_of(hunk)
    if removed and added:
        return original_lines[at : at + len(post)] == post and original_lines[at : at + len(pre)] != pre
    if not removed:
        return bool(post) and original_lines[at : at + len(post)] == post
    if any(line in original_lines for line in removed):
        return False  # the to-be-deleted content still exists somewhere in the file
    if post and original_lines[at : at + len(post)] != post:
        return False
    return not (at + hunk["old_count"] <= len(original_lines))


def apply_file(path: Path, entry: dict[str, Any], root: Path) -> str:
    """Apply one file's hunks under STRICT semantics. Returns the verdict."""
    if entry["is_delete"]:
        if not path.is_file():
            refuse(
                "an existing file to delete",
                f"no file at {path}",
                "fix the diff — deletion of an absent file refuses",
            )
        guard_surface(path, root)
        path.unlink()
        return f"deleted: {path}"
    if entry["is_new"]:
        original_lines: list[str] = []
    else:
        if not path.is_file():
            refuse(
                f"an existing file at {path}",
                "no file there",
                "fix the diff's headers — or use the /dev/null create convention",
            )
        guard_surface(path, root)
        text = path.read_text(encoding="utf-8")
        if "\r\n" in text and "\r\n" not in "\n".join(t for h in entry["hunks"] for _, t in h["lines"]):
            refuse(
                "matching line endings (the file carries CRLF; the diff carries LF)",
                "eol_mismatch — the line endings disagree",
                "regenerate the diff against the file's actual line endings — never silently applied",
            )
        original_lines = text.splitlines()
    out: list[str] = []
    cursor = 0
    for hunk in entry["hunks"]:
        pre, post = _blocks_of(hunk)
        at = hunk["old_start"] - 1
        if pre:
            if 0 <= at <= len(original_lines) - len(pre) and original_lines[at : at + len(pre)] == pre:
                pass  # exact at the stated location — the strict match
            elif _already_applied(hunk, original_lines, at):
                return f"already applied: {path} (the change is genuinely present — SAME_RESULT, a no-op)"
            else:
                actual = original_lines[at : at + len(pre)] if 0 <= at < len(original_lines) else []
                refuse(
                    "the hunk's pre-image EXACTLY at line "
                    f"{hunk['old_start']} (strict semantics — line numbers are load-bearing)",
                    "the file has: "
                    f"{json.dumps([('...' + ln[:60] if len(ln) > 60 else ln) for ln in actual][:6])}",
                    "the file and the diff disagree — re-read the file and regenerate the diff (the caller's loop)",
                )
        else:
            if not (0 <= at <= len(original_lines)):
                refuse(
                    "an in-range insertion point",
                    f"hunk hint {hunk['old_start']} outside the file",
                    "fix the hunk header",
                )
        if at < cursor:
            refuse(
                "ordered hunks",
                f"a hunk's stated line {hunk['old_start']} falls behind the cursor at {cursor + 1}",
                "reorder the hunks — a patch applies in order",
            )
        out.extend(original_lines[cursor:at])
        out.extend(post)
        cursor = at + len(pre)
    out.extend(original_lines[cursor:])
    new_text = "\n".join(out) + ("\n" if out else "")
    if not entry["is_new"]:
        guard_surface(path, root)
        if new_text == path.read_text(encoding="utf-8"):
            return f"no change: {path} (the diff applies to nothing — refused as a no-op)"
    # Parent-dir creation (Q-SEATS-1 ruling 12, 2026-09-30): create ALL
    # directories in the patch path before write_text — new-file creation
    # happens via patch, including into directories that do not yet exist
    # (FR-MEM-0097's defect and FR-MEM-0036's hand-mkdir ceremony die here).
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(new_text, encoding="utf-8")
    return f"applied: {path} ({len(entry['hunks'])} hunk(s))"


# ---------------------------------------------------------------------------
# The checks (the registry; apply-then-report — findings ride the output)
# ---------------------------------------------------------------------------


def _run(cmd: list[str]) -> tuple[int, str]:
    """Fixed-argv subprocess (the no-shell law); returns (exit, output tail)."""
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    out = (proc.stdout + proc.stderr).strip()
    return proc.returncode, out[-2000:] if len(out) > 2000 else out


def _parse_check_json(text: str) -> str | None:
    try:
        json.loads(text)
    except json.JSONDecodeError as exc:
        return f"JSON parse error: {exc}"
    return None


def _parse_check_toml(text: str) -> str | None:
    try:
        tomllib.loads(text)
    except tomllib.TOMLDecodeError as exc:
        return f"TOML parse error: {exc}"
    return None


def check_file(path: Path) -> list[str]:
    """The type-appropriate checks on one mutated file (findings = the report)."""
    findings: list[str] = []
    suffix = path.suffix
    if suffix == ".py":
        code, out = _run(["uv", "run", "ruff", "check", str(path)])
        if code != 0:
            findings.append(f"ruff:\n{out}")
        code, out = _run(["uv", "run", "pyright", str(path)])
        if code != 0 and "0 errors, 0 warnings, 0 informations" not in out:
            findings.append(f"pyright:\n{out}")
    elif suffix == ".json":
        bad = _parse_check_json(path.read_text(encoding="utf-8"))
        if bad:
            findings.append(bad)
    elif suffix == ".toml":
        bad = _parse_check_toml(path.read_text(encoding="utf-8"))
        if bad:
            findings.append(bad)
    elif suffix == ".ts":
        code, out = _run(["uv", "run", "--no-sync", "bunx", "tsc", "--noEmit", str(path)])
        if code != 0:
            findings.append(f"tsc:\n{out}")
    return findings


def _reverse(snapshot: dict[Path, bytes | None], root: Path) -> None:
    """THE REVERSE (Q-SEATS-1 ruling 14): restore every touched file's exact
    pre-patch bytes from the snapshot — NOT git checkout, so pre-existing
    uncommitted edits to those files survive; files recorded absent are
    removed (created parent dirs stay — empty dirs are inert)."""
    for path, pre in snapshot.items():
        if pre is None:
            if path.is_file():
                path.unlink()
        else:
            path.write_bytes(pre)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "patch — the seat's one mutation verb: apply a unified diff under strict "
            "semantics (exact at the stated location or refuse), then the type-appropriate "
            "checks ride the same output (apply-then-report)."
        )
    )
    parser.add_argument("subcommand", choices=["apply"], help="the mutation act (apply is the verb)")
    parser.add_argument("diff_file", nargs="?", help="Path to the unified-diff file (or - for stdin)")
    parser.add_argument(
        "--diff", help="The unified-diff text verbatim (the wrapper's channel — multiline rides one arg)"
    )
    parser.add_argument("--root", default=".", help="The tree root the diff's paths resolve against")
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    try:
        if args.diff is not None:
            text = args.diff
        elif args.diff_file is not None:
            text = sys.stdin.read() if args.diff_file == "-" else Path(args.diff_file).read_text(encoding="utf-8")
        else:
            raise PatchError("no diff given — pass --diff (text) or a file path")
        files = parse_diff(text)
        # THE SNAPSHOT (Q-SEATS-1 ruling 14): every touched file's exact
        # pre-patch bytes in memory — absence recorded for new files. The
        # reverse restores THESE bytes, never git checkout.
        snapshot: dict[Path, bytes | None] = {}
        verdicts: list[str] = []
        mutated: list[Path] = []
        try:
            for path_str, entry in files.items():
                # THE DELETION TARGET (CA-7): parse_diff keys every file section
                # by its NEW path, so a deletion's dict key is the literal
                # /dev/null — never the target. Resolve ONCE per entry: a
                # deletion targets the --- header's path (entry["old"], the
                # a/ prefix stripped); creates and edits keep the key. The
                # ONE resolved path feeds the snapshot, the apply, and the
                # mutated append — no second resolution anywhere (the
                # coupling law: a second resolution is the failure mode).
                target_str = (
                    entry["old"].removeprefix("a/")
                    if entry["is_delete"]
                    else path_str.removeprefix("b/").removeprefix("a/")
                )
                path = root / target_str
                snapshot[path] = path.read_bytes() if path.is_file() else None
                verdict = apply_file(path, entry, root)
                verdicts.append(verdict)
                if verdict.startswith(("applied:", "deleted:")):
                    mutated.append(path)
        except SystemExit:
            # a mid-apply refusal in a multi-file diff is a torn state —
            # the transaction reverses before the refusal propagates
            _reverse(snapshot, root)
            print("REFUSED mid-apply — the transaction REVERSED; NO CHANGES LANDED")
            raise
        print(f"APPLIED — {len(mutated)} file(s)")
        for line in verdicts:
            print(f"  {line}")
        if not mutated:
            print("no-op — nothing mutated, nothing committed")
            return 0
        findings: list[str] = []
        for path in mutated:
            if not path.is_file():
                continue  # a deleted file has nothing left to check
            findings.extend(check_file(path))
        if findings:
            print("findings ride an applied edit (fix and re-apply):")
            for f in findings:
                print(f"  {f}")
            return 1
        return 0
    except PatchError as exc:
        print(f"Error (parse_error): {exc}", file=sys.stderr)
        return 2
    except OSError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
