# Copyright (C) 2026 Mark Losey. All rights reserved.
"""key_store -- the key persistence seam: mint and load the api keys.

The key-infrastructure unit (the approved design + unit brief, the
exact-task spec synthesize/keyinfrastructurespec): the JSONL key store
per the run_store school -- one flat self-describing line per key,
{digest, comparator_id, comparator_class, scopes, audience, created_at},
sort_keys deterministic bytes, one complete line + newline + flush per
write. HASHED-AT-REST: only the sha256 hexdigest rides the file; the
plaintext is shown ONCE at the mint and never written. The 0600 mode at
the mint (os.chmod after the write, umask-proof); the load's stat check
(F3: a world-writable store refuses loudly); the corrupt file refused
WHOLE (the pre-pass validates every line before the first use); the
absent store NEVER a refusal (the failopen's data shape: the empty
state, made loud by the boot marker at the service, not here). The home
resolved-and-rendered once at boot (F10 folded into F1) -- the resolved
ABSOLUTE path, the cwd-split boot killed. Stdlib only (json, hashlib,
os, pathlib, secrets, time). Five-field docstrings on every public
symbol; every vocabulary a named constant (content-in-configuration).
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import secrets
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import TYPE_CHECKING, Final, cast

from prioritree.votes import COMPARATOR_CLASSES

if TYPE_CHECKING:
    from collections.abc import Mapping, Sequence

__all__ = ["KEYS_HOME", "KeyRecord", "KeyStore", "KeyStoreRefusedError", "render_boot_marker", "resolve_auth_mode"]

# The store home's default (unit brief §2a, the STORE_HOME school): CWD-relative,
# per-project state; a named module constant; every verb takes the home as a
# PARAMETER (test isolation). The env override PRIORITYTREE_KEYS_HOME resolves
# at resolve_keys_home -- the knob's ?= form read ONCE at boot, never per-request.
KEYS_HOME: Final[Path] = Path(".prioritree/keys.jsonl")

# The env override's name (the knob read once at boot).
_KEYS_HOME_ENV: Final[str] = "PRIORITYTREE_KEYS_HOME"

# The vocabulary constants (content-in-configuration): the six scope tokens
# (the design's grant-map nouns), the audience pair (F5), the digest form.
SCOPE_TOKENS: Final[frozenset[str]] = frozenset({"register", "next", "cast", "state", "tally", "manifest"})
AUDIENCES: Final[frozenset[str]] = frozenset({"service", "mcp"})
_DIGEST_HEX_LENGTH: Final[int] = 64
_DIGEST_PATTERN: Final[re.Pattern[str]] = re.compile(r"[0-9a-f]{64}")
_KEY_ENTROPY_BYTES: Final[int] = 32
_KEY_MODE: Final[int] = 0o600
_WORLD_WRITE_MASK: Final[int] = 0o002

# The AUTH knob's legal pair (F1's vocabulary): on | off -- named constants.
_AUTH_MODE_ON: Final[str] = "on"
_AUTH_MODE_OFF: Final[str] = "off"


class KeyStoreRefusedError(Exception):
    """KeyStoreRefusedError -- the typed refusal: expected, found, next_action.

    Purpose: carry the key store's OWN refusal grammar (expected/found/
    next-action) as data the CLI/service wrappers catch and render; raised,
    never returned -- the store's refusal is the FILE's and the VOCABULARY's
    (the door's refusals never wrapped, never conflated).
    Refuses when: never -- it IS the refusal; the message renders all three
    fields so an uncaught traceback still names the legal form.
    Re-run: deterministic -- the same violation raises the same three fields.
    Touches: nothing -- a plain Exception subclass (zero runtime deps).
    Provenance: the StoreRefusedError precedent (run_store.py:62-93, the
    Error-suffix family form, N818); the exact-task spec
    synthesize/keyinfrastructurespec §1 (KeyStoreRefusedError).
    """

    def __init__(self, expected: str, found: str, next_action: str) -> None:
        """Initialize the refusal with its three named fields.

        Purpose: carry expected/found/next_action plus the rendered message.
        Refuses when: never.
        Re-run: idempotent.
        Touches: nothing.
        Provenance: registry-brief §2 (the typed exception, RefusedError
        precedent); the exact-task spec synthesize/keyinfrastructurespec §1.
        """
        self.expected = expected
        self.found = found
        self.next_action = next_action
        _prefix = "refused"
        super().__init__(f"{_prefix} — expected: {expected} | found: {found} | next: {next_action}")


@dataclass(frozen=True)
class KeyRecord:
    """KeyRecord -- one frozen key line, provenance stamped.

    Purpose: carry one key's persisted identity as data -- the sha256
    hexdigest (hashed-at-rest; the plaintext never rides the file), the
    comparator id and class (the provenance stamps), the granted scopes
    (the route-table vocabulary), the audience (F5: the tier the key
    opens), and the created_at stamp (carried as data, validated for
    type never value -- the clock-free discipline).
    Refuses when: never at construction -- validation happens at the
    load's pre-pass (_parse_line) and the mint's argument gates; every
    refusal raises KeyStoreRefusedError before any byte lands there.
    Re-run: idempotent -- a frozen value type; the same line parses to
    the same record at every load.
    Touches: nothing -- a pure value; held by KeyStore.records and read
    back by the verify seam.
    Provenance: the VoteRecord precedent (votes.py:42-60); the exact-task
    spec synthesize/keyinfrastructurespec §1 (the record {digest,
    comparator_id, comparator_class, scopes, audience, created_at}).
    """

    digest: str
    comparator_id: str
    comparator_class: str
    scopes: frozenset[str]
    audience: str
    created_at: str


def _repair_path(keys_home: Path) -> str:
    """Return the shared next_action for a corrupt-store refusal.

    Purpose: render the repair path once -- every pre-pass refusal
    names it (the load refuses the corrupt file whole, never a silent
    partial load).
    Refuses when: never.
    Re-run: deterministic.
    Touches: nothing.
    Provenance: the run_store._repair_path precedent (run_store.py:96-109);
    the exact-task spec synthesize/keyinfrastructurespec §1 (_repair_path).
    """
    _head = "repair the key store -- the load refuses the corrupt file whole, never a silent"
    return f"{_head} partial load ({keys_home}); re-mint with prioritree key mint after fixing"


def resolve_keys_home(env: Mapping[str, str] | None = None) -> Path:
    """Resolve the keys home ONCE at boot (F10): the env override PRIORITYTREE_KEYS_HOME if set, else KEYS_HOME.

    Purpose: the knob's ?= form -- the env override read ONCE at boot,
    never per-request; the caller renders the ABSOLUTE resolved path
    (Path.absolute()) -- the cwd-split boot killed.
    Refuses when: never -- an empty/absent override falls back to
    KEYS_HOME (the default is a value, never a refusal).
    Re-run: deterministic given the environment mapping.
    Touches: nothing -- a read of the injected env mapping (the process
    environment when env is None; the mapping injected for test
    isolation).
    Provenance: the exact-task spec synthesize/keyinfrastructurespec §1
    (resolve_keys_home, the STORE_HOME ?= school); the F10 fold.
    """
    source = os.environ if env is None else env
    override = source.get(_KEYS_HOME_ENV)
    return Path(override) if override else KEYS_HOME


def _require_str_field(line: Mapping[str, object], field: str, position: int, keys_home: Path) -> str:
    """Return the line's string field, refusing the missing or mistyped.

    Purpose: enforce the field's presence and JSON string type (the
    run_store field-helper school, verbatim form).
    Refuses when: the field is missing or not a string (found carries
    the line number + the raw value).
    Re-run: deterministic.
    Touches: nothing -- a read of the bytes already in hand.
    Provenance: the _require_str_field precedent (run_store.py:146-171);
    the exact-task spec synthesize/keyinfrastructurespec §1 (_parse_line's
    field-helper school).
    """
    if field not in line:
        raise KeyStoreRefusedError(
            expected=f"a '{field}' field on line {position}",
            found=f"line {position}: the field is missing",
            next_action=_repair_path(keys_home),
        )
    value = line[field]
    if not isinstance(value, str):
        raise KeyStoreRefusedError(
            expected=f"the '{field}' field a JSON string",
            found=f"line {position}: {value!r}",
            next_action=_repair_path(keys_home),
        )
    return value


def _require_scopes_field(line: Mapping[str, object], position: int, keys_home: Path) -> frozenset[str]:
    """Return the line's scopes as a validated frozenset, refusing the malformed.

    Purpose: enforce the scopes' wire form -- a JSON array of strings,
    each token from SCOPE_TOKENS; restored type-exact as a frozenset
    (the store never constructs the frozen value itself).
    Refuses when: the field is missing, not an array, or a token falls
    outside the vocabulary (found carries the line number + the raw
    value).
    Re-run: deterministic.
    Touches: nothing -- a pure validation over its arguments.
    Provenance: the _require_verdicts_field precedent
    (run_store.py:322-351); the exact-task spec
    synthesize/keyinfrastructurespec §1 (_parse_line's scopes check).
    """
    if "scopes" not in line:
        raise KeyStoreRefusedError(
            expected=f"a 'scopes' field on line {position}",
            found=f"line {position}: the field is missing",
            next_action=_repair_path(keys_home),
        )
    value = line["scopes"]
    if not isinstance(value, list) or any(
        not isinstance(member, str) or member not in SCOPE_TOKENS for member in cast("list[object]", value)
    ):
        raise KeyStoreRefusedError(
            expected=f"the 'scopes' field a JSON array of tokens from {sorted(SCOPE_TOKENS)}",
            found=f"line {position}: {value!r}",
            next_action=_repair_path(keys_home),
        )
    return frozenset(cast("list[str]", value))


def _parse_line(line: Mapping[str, object], position: int, keys_home: Path) -> KeyRecord:
    """Validate one key line's six fields, refusing the ill-formed.

    Purpose: the pre-pass's per-line core (the run_store field-helper
    school): the six fields required; digest a 64-char lowercase hex
    (re.fullmatch); comparator_id a non-empty str; comparator_class
    from COMPARATOR_CLASSES (CITED, never re-declared -- the
    mcp_server.py:97 fork-guard school); scopes a list of str each in
    SCOPE_TOKENS; audience in AUDIENCES; created_at a str. Every
    refusal names the line number + the raw value.
    Refuses when: any field is missing or mistyped, or any value falls
    outside its vocabulary (KeyStoreRefusedError, found carrying the
    line number + the raw value verbatim).
    Re-run: deterministic -- the same line raises the same refusal.
    Touches: nothing -- a pure validation over its arguments.
    Provenance: the run_store field helpers (run_store.py:146-171); the
    exact-task spec synthesize/keyinfrastructurespec §1 (_parse_line).
    """
    digest = _require_str_field(line, "digest", position, keys_home)
    if _DIGEST_PATTERN.fullmatch(digest) is None:
        raise KeyStoreRefusedError(
            expected=f"the 'digest' field a {_DIGEST_HEX_LENGTH}-char lowercase hex string",
            found=f"line {position}: digest got {digest!r}",
            next_action=_repair_path(keys_home),
        )
    comparator_id = _require_str_field(line, "comparator_id", position, keys_home)
    if not comparator_id:
        raise KeyStoreRefusedError(
            expected="the 'comparator_id' field a non-empty JSON string",
            found=f"line {position}: comparator_id got {comparator_id!r}",
            next_action=_repair_path(keys_home),
        )
    comparator_class = _require_str_field(line, "comparator_class", position, keys_home)
    if comparator_class not in COMPARATOR_CLASSES:
        raise KeyStoreRefusedError(
            expected=f"a comparator_class from {sorted(COMPARATOR_CLASSES)}",
            found=f"line {position}: comparator_class got {comparator_class!r}",
            next_action=_repair_path(keys_home),
        )
    scopes = _require_scopes_field(line, position, keys_home)
    audience = _require_str_field(line, "audience", position, keys_home)
    if audience not in AUDIENCES:
        raise KeyStoreRefusedError(
            expected=f"an audience from {sorted(AUDIENCES)}",
            found=f"line {position}: audience got {audience!r}",
            next_action=_repair_path(keys_home),
        )
    created_at = _require_str_field(line, "created_at", position, keys_home)
    return KeyRecord(
        digest=digest,
        comparator_id=comparator_id,
        comparator_class=comparator_class,
        scopes=scopes,
        audience=audience,
        created_at=created_at,
    )


def _stat_check(keys_file: Path) -> None:
    """Refuse a world-writable key store (F3) -- the mode check before any read or append.

    Purpose: stat().st_mode & 0o002 -> KeyStoreRefusedError -- the
    world-writable store refuses loudly, never silently widened; the
    0600+stat floor is a FLOOR, never a cure (the trade-off carried).
    Refuses when: the file's mode has ANY world-write bit set.
    Re-run: deterministic given the file's mode.
    Touches: nothing -- a stat read only.
    Provenance: the design's F3 ruling; the exact-task spec
    synthesize/keyinfrastructurespec §1 (_stat_check).
    """
    mode = keys_file.stat().st_mode
    if mode & _WORLD_WRITE_MASK:
        raise KeyStoreRefusedError(
            expected=f"the key store mode {_KEY_MODE:04o}",
            found=f"mode {oct(mode & 0o777)} world-writable",
            next_action=f"chmod 600 {keys_file}",
        )


class KeyStore:
    """KeyStore -- the load-at-boot container with the mtime re-read.

    Purpose: hold the keys file's path (.home, injected at construction
    -- the store-as-parameter discipline, test isolation) and the
    loaded records (.records, keyed by digest); the CONSTRUCTION is the
    boot's compose (the load fires here: the absent store the empty
    dict, never a refusal; the world-writable or corrupt store refuses
    loudly at the boot); the mtime re-read keeps a mid-flight mint live.
    Refuses when: KeyStoreRefusedError -- the store's own refusals
    (F3's world-writable mode, the corrupt line, the crash-tail, the
    duplicated digest, the mint's vocabulary gates); the ABSENT store
    is never a refusal (the empty dict).
    Re-run: load is deterministic given the file's bytes; mint is
    random by design (secrets) but byte-disciplined in form
    (sort_keys); the mtime re-read is a pure comparison.
    Touches: only its own key file (a read at the load; append + chmod
    at the mint) and the parent directory's creation at the mint --
    nothing of the core's.
    Provenance: the Persist precedent (run_store.py:470-504); the
    exact-task spec synthesize/keyinfrastructurespec §1 (KeyStore,
    load_keys, mint, mtime -- the container's surfaces).
    """

    def __init__(self, home: Path) -> None:
        """Initialize the container over the injected key home -- the load-at-boot composed.

        Purpose: hold the keys file's path and compose the load (the
        absent store the empty dict, never a refusal; the
        world-writable or corrupt store refuses HERE -- the boot dies
        honestly); the loaded mtime captured (the re-read's ground).
        Refuses when: the load refuses (KeyStoreRefusedError riding
        through, BY TYPE); never on the absent store.
        Re-run: idempotent in effect -- a fresh container over the same
        home loads the same bytes to the same records.
        Touches: only its own attributes and a read of the key file.
        Provenance: the exact-task spec synthesize/keyinfrastructurespec
        §1 (the load-at-boot container); the Persist.__init__ precedent
        (run_store.py:506-525).
        """
        self.home = home
        self.records: dict[str, KeyRecord] = {}
        self._loaded_mtime: float | None = None
        self.load_keys()

    def load_keys(self, home: Path | None = None) -> dict[str, KeyRecord]:
        """Load the key file's records whole, keyed by digest -- the absent store the empty dict, never a refusal.

        Purpose: the pre-pass -- the absent file returns the EMPTY dict
        (NEVER a refusal; the absence is made loud by the boot marker at
        the service, not here); present -> the stat check first (F3),
        then the whole file parsed and validated (every line before the
        first use), the records returned keyed by digest; a duplicate
        digest refuses (found names the two line numbers); the loaded
        mtime captured (the re-read's comparison surface); the passed
        home re-binds the container (the container's own the default).
        Refuses when: the store is world-writable (F3); any line is
        corrupt (the _parse_line trigger set); the crash-tail (the last
        line without its newline); a duplicate digest.
        Re-run: deterministic given the file's bytes.
        Touches: only the key file (a read) and the container's own
        state (records, home, the mtime stamp).
        Provenance: the Persist.load precedent (run_store.py:580-714); the
        exact-task spec synthesize/keyinfrastructurespec §1 (load_keys).
        """
        target = self.home if home is None else home
        if not target.is_file():
            self.home = target
            self.records = {}
            self._loaded_mtime = None
            return self.records
        _stat_check(target)
        raw = target.read_text(encoding="utf-8")
        if raw and not raw.endswith("\n"):
            tail_lines = raw.splitlines()
            _tail = tail_lines[-1] if tail_lines else raw
            raise KeyStoreRefusedError(
                expected="the file's last line complete with its newline (one write of one complete line per append)",
                found=f"line {len(tail_lines)}: the crash-tail is truncated -- {_tail!r}",
                next_action=_repair_path(target),
            )
        records: dict[str, KeyRecord] = {}
        positions: dict[str, int] = {}
        for position, raw_line in enumerate(raw.splitlines(), start=1):
            try:
                value = json.loads(raw_line)
            except json.JSONDecodeError as parse_error:
                raise KeyStoreRefusedError(
                    expected=f"line {position} well-formed JSON (one flat self-describing object)",
                    found=f"line {position}: {parse_error.msg} -- {raw_line!r}",
                    next_action=_repair_path(target),
                ) from parse_error
            if not isinstance(value, dict):
                raise KeyStoreRefusedError(
                    expected=f"line {position} a flat JSON object",
                    found=f"line {position}: a {type(value).__name__} -- {raw_line!r}",
                    next_action=_repair_path(target),
                )
            record = _parse_line(cast("dict[str, object]", value), position, target)
            if record.digest in records:
                raise KeyStoreRefusedError(
                    expected="one record per digest (no duplicated digests)",
                    found=f"digest {record.digest!r} at both line {positions[record.digest]} and line {position}",
                    next_action=_repair_path(target),
                )
            records[record.digest] = record
            positions[record.digest] = position
        self.home = target
        self.records = records
        self._loaded_mtime = self.mtime(target)
        return self.records

    def mint(
        self,
        comparator_id: str,
        comparator_class: str,
        scopes: Sequence[str],
        audience: str,
        created_at: str | None = None,
    ) -> tuple[str, str]:
        """Mint one key -- the ceremony: validate the arguments, append the one line, chmod 0600, return (key, digest).

        Purpose: THE MINT CEREMONY: (1) validate the arguments at the
        store (comparator_id non-empty; comparator_class in
        COMPARATOR_CLASSES; every scope in SCOPE_TOKENS, empty list
        refused; audience in AUDIENCES) -> typed refusal, exit 1 at
        the CLI, NEVER argparse choices=; (2) home.parent.mkdir(
        parents=True, exist_ok=True); (3) IF the file exists: the stat
        check (a world-writable store never widened) + the load's
        pre-pass (the mint appends only to a validated whole --
        load_keys); (4) key = secrets.token_urlsafe(32) (the 256-bit
        norm, 43 chars); digest = the sha256 hexdigest; (5) one write
        of one complete line + newline + flush (json.dumps sort_keys --
        deterministic bytes, the _append_line school); (6) chmod 0600
        AFTER the write (Path.chmod -- the create-and-append both land
        0600, umask-proof); (7) return (key, digest) -- the key shown ONCE
        by the caller, never on disk. The home rides the container's
        own (self.home).
        Refuses when: any argument outside its vocabulary (the typed
        three fields); the existing store is world-writable (F3) or
        corrupt (the pre-pass); the write or flush raises (the OS
        error verbatim, never swallowed).
        Re-run: the line's FORM is deterministic (sort_keys) but the
        key is random by design (secrets) -- a re-mint is a NEW key,
        never a replay.
        Touches: the parent directory (created if absent) and the key
        file (append + chmod) -- nothing else.
        Provenance: the exact-task spec synthesize/keyinfrastructurespec
        §1 (mint, the ceremony's seven steps); the Persist._append_line
        precedent (run_store.py:716-744).
        """
        if not comparator_id:
            raise KeyStoreRefusedError(
                expected="a non-empty comparator_id",
                found=f"comparator_id got {comparator_id!r}",
                next_action="pass the comparator id (the operator id the key names)",
            )
        if comparator_class not in COMPARATOR_CLASSES:
            raise KeyStoreRefusedError(
                expected=f"a comparator_class from {sorted(COMPARATOR_CLASSES)}",
                found=f"comparator_class got {comparator_class!r}",
                next_action="re-run the mint with --class human or --class llm",
            )
        scope_list = list(scopes)
        if not scope_list or any(scope not in SCOPE_TOKENS for scope in scope_list):
            raise KeyStoreRefusedError(
                expected=f"a non-empty --scopes list of tokens from {sorted(SCOPE_TOKENS)}",
                found=f"scopes got {scope_list!r}",
                next_action=f"re-run the mint with --scopes a comma list over {sorted(SCOPE_TOKENS)}",
            )
        if audience not in AUDIENCES:
            raise KeyStoreRefusedError(
                expected=f"an --audience from {sorted(AUDIENCES)}",
                found=f"audience got {audience!r}",
                next_action="re-run the mint with --audience service or --audience mcp",
            )
        self.home.parent.mkdir(parents=True, exist_ok=True)
        if self.home.is_file():
            self.load_keys()
        key = secrets.token_urlsafe(_KEY_ENTROPY_BYTES)
        digest = hashlib.sha256(key.encode("utf-8")).hexdigest()
        payload = (
            json.dumps(
                {
                    "digest": digest,
                    "comparator_id": comparator_id,
                    "comparator_class": comparator_class,
                    "scopes": sorted(set(scope_list)),
                    "audience": audience,
                    "created_at": created_at or datetime.now(UTC).isoformat(),
                },
                sort_keys=True,
            )
            + "\n"
        )
        try:
            with self.home.open("a", encoding="utf-8") as handle:
                handle.write(payload)
                handle.flush()
        except OSError as write_error:
            raise KeyStoreRefusedError(
                expected="the key line durable on disk at the mint's return (one complete line, flushed)",
                found=f"{write_error!r} -- the key lives in memory, not on disk",
                next_action=_repair_path(self.home),
            ) from write_error
        self.home.chmod(_KEY_MODE)
        return key, digest

    def mtime(self, home: Path | None = None) -> float | None:
        """Return the key file's st_mtime, or None when the file is absent.

        Purpose: the re-read's comparison surface (the mid-flight mint
        seen live); None is a VALUE (the absent store's data shape),
        never a refusal; the passed home the target (the container's
        own the default).
        Refuses when: never -- the absent file is None by design.
        Re-run: deterministic given the file's state.
        Touches: nothing -- a stat read only.
        Provenance: the exact-task spec synthesize/keyinfrastructurespec
        §1 (mtime -- the re-read's comparison surface).
        """
        target = self.home if home is None else home
        return target.stat().st_mtime if target.is_file() else None

    def reload_if_changed(self, home: Path | None = None) -> bool:
        """Reload the key file when its mtime moved past the loaded stamp -- the mid-flight mint seen live.

        Purpose: THE RELOAD -- the mtime check: compare the file's
        current mtime against the loaded stamp; changed -> the full
        re-load (the validation re-firing whole: the stat check, the
        pre-pass); unchanged -> no reload, False returned; the passed
        home the target (the container's own the default), re-bound on
        the successful re-load. The verify seam calls this before
        every lookup -- a mid-flight mint lands live.
        Refuses when: never its own -- a changed file's own refusal
        fires at load_keys and rides through BY TYPE, never wrapped
        (the last-good records stand).
        Re-run: deterministic given the file's state.
        Touches: only the container's own state -- a stat read, and the
        key file's read at the re-load.
        Provenance: the exact-task spec synthesize/keyinfrastructurespec
        §1 (the mtime re-read) + §2 (the stat ride:
        store.reload_if_changed(home)).
        """
        target = self.home if home is None else home
        current = self.mtime(target)
        if current == self._loaded_mtime:
            return False
        self.load_keys(target)
        return True


def resolve_auth_mode(raw: str | None) -> str:
    """Resolve the AUTH knob (F1): None or 'on' -> 'on'; 'off' -> 'off'; anything else refuses loudly.

    Purpose: the typo refusal -- AUTH=on/off the legal pair; ANY OTHER
    VALUE refuses loudly at boot (a typo'd knob NEVER silently means
    either -- the process dies honestly); the resolved mode rides the
    service's app.state.auth for the routes.
    Refuses when: raw is any value other than None, 'on', or 'off'
    (KeyStoreRefusedError, found the value verbatim).
    Re-run: deterministic given the value.
    Touches: nothing -- a pure resolution over its argument.
    Provenance: the design's F1 ruling; the exact-task spec
    synthesize/keyinfrastructurespec §1 (resolve_auth_mode) + §5 (the
    knob's exact form).
    """
    if raw is None or raw == _AUTH_MODE_ON:
        return _AUTH_MODE_ON
    if raw == _AUTH_MODE_OFF:
        return _AUTH_MODE_OFF
    _fix_head = "fix the AUTH value in the environment or Makefile and reboot"
    raise KeyStoreRefusedError(
        expected="AUTH one of on|off (or unset)",
        found=f"AUTH got {raw!r}",
        next_action=f"{_fix_head} -- a typo'd knob never silently means either",
    )


def render_boot_marker(home: Path, mode: str, count: int) -> str:
    """Render the boot marker's exact bytes (the boot form, the log channel).

    Purpose: the marker at each state -- off: the operator's explicit
    degrade named; on + absent store: the absence LOUD (the failopen
    named, the next-action cited -- never silent, F1); on + present:
    the home + the mode + the count. The home arrives already resolved
    (the caller's Path.absolute() render -- the cwd-split boot killed).
    Refuses when: never -- a pure render over its arguments.
    Re-run: deterministic -- the same inputs render the same bytes.
    Touches: nothing -- a read of the injected path's file-presence
    only (the present/absent branch).
    Provenance: the exact-task spec synthesize/keyinfrastructurespec §1
    (render_boot_marker) + §5 (the marker's three states); the F10 fold.
    """
    if mode == _AUTH_MODE_OFF:
        return f"auth: {mode} (operator's explicit degrade) | keys: {home} | count: {count}"
    if not home.is_file():
        return f"auth: {mode} (failopen -- no key store) | keys: {home} | next-action: prioritree key mint"
    return f"auth: {mode} | keys: {home} | count: {count}"
