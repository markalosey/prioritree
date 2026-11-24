<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/keyinfrastructurespec

**Route:** prioritree-auth (executing) | **Events:** 6 | **Reports:** 2

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-24T09:28:08Z |
| 2 | report | togo | 2026-11-24T09:39:50Z |
| 3 | result | shinko | 2026-11-24T09:41:40Z |
| 4 | gate | shinko | 2026-11-24T14:03:49Z |
| 5 | dispatch | shinko | 2026-11-24T16:05:48Z |
| 6 | report | togo | 2026-11-24T16:07:38Z |
## Reported by togo — 2026-11-24T09:39:50Z

# THE KEY-INFRASTRUCTURE EXACT-TASK SPEC — togo's bytes (synthesize/keyinfrastructurespec, 2026-11-24)

## 0. THE GROUND READ WHOLE (every file cited)

key-infrastructure.md (the approved unit brief — §1 the five landings, §2 the mechanisms a-h, §3 the arcs, §5 the handoff's opens); auth-design.md (the blocking rulings F1/F3/F5/F8/F9 carried, F10 folded into F1); run_store.py whole (STORE_HOME :53 the ?= school, StoreRefusedError :62-93 the three-field grammar, _parse_lines :111-143 the pre-pass, _append_line :716-744 one-write-one-line-flush sort_keys); cli.py whole (the five-subcommand grammar :44-48, the AFTER-subcommand --home :140-146, NO choices= anywhere, the exit mapping :393-401, _report :86-98); service.py whole (the constants school :73-92, render_refusal :168-183, the construction :164-165); Makefile whole (:3-6 the ?= form, :22-33 the start target's env carrier); votes.py:33 COMPARATOR_CLASSES; mcp_server.py:96-98 the Literal drift guard precedent; pyproject.toml (ruff ALL, named rulings only, tests S101/PLR2004 :50); tests/test_cli.py, tests/test_run_store.py, tests/test_service_store.py:238 the fence precedent, whole.

## 1. src/prioritree/key_store.py — THE STORE WHOLE (fenced bytes)

```python
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
import time
from pathlib import Path
from typing import Final, cast

from prioritree.votes import COMPARATOR_CLASSES

__all__ = ["KEYS_HOME", "KeyRecord", "KeyStoreRefusedError", "KeyStore", "resolve_auth_mode", "render_boot_marker"]

# The store home's default (unit brief §2a, the STORE_HOME school): CWD-relative,
# per-project state; a named module constant; every verb takes the home as a
# PARAMETER (test isolation). The env override PRIORITYTREE_KEYS_HOME resolves
# at resolve_keys_home -- the knob's ?= form read ONCE at boot, never per-request.
KEYS_HOME: Final[Path] = Path(".prioritree/keys.jsonl")

# The vocabulary constants (content-in-configuration): the six scope tokens
# (the design's grant-map nouns), the audience pair (F5), the digest form.
SCOPE_TOKENS: Final[frozenset[str]] = frozenset({"register", "next", "cast", "state", "tally", "manifest"})
AUDIENCES: Final[frozenset[str]] = frozenset({"service", "mcp"})
_DIGEST_HEX_LENGTH: Final[int] = 64
_DIGEST_PATTERN: Final[re.Pattern[str]] = re.compile(r"[0-9a-f]{64}")
_KEY_ENTROPY_BYTES: Final[int] = 32
_KEY_MODE: Final[int] = 0o600
_WORLD_WRITE_MASK: Final[int] = 0o002

class KeyStoreRefusedError(Exception):
    """... (the StoreRefusedError grammar verbatim: expected/found/next_action;
    N818 Error-suffix family; the message renders all three fields)."""
    def __init__(self, expected: str, found: str, next_action: str) -> None: ...  # the run_store.py:79-93 form

@dataclass(frozen=True)
class KeyRecord:
    """KeyRecord -- one frozen key line, provenance stamped. digest, comparator_id,
    comparator_class, scopes (frozenset), audience, created_at (carried as data,
    validated for type never value -- the clock-free discipline)."""

def _repair_path(keys_home: Path) -> str:
    # "repair the key store -- the load refuses the corrupt file whole, never a
    # silent partial load ({home}); re-mint with prioritree key mint after fixing"

def resolve_keys_home(env: Mapping[str, str] | None = None) -> Path:
    """Resolve the keys home ONCE at boot (F10): the env override
    PRIORITYTREE_KEYS_HOME if set, else KEYS_HOME; the caller renders the
    ABSOLUTE resolved path (Path.absolute()) -- the cwd-split boot killed."""

def _parse_line(line: Mapping[str, object], position: int, keys_home: Path) -> KeyRecord:
    # The pre-pass's per-line core (the run_store field-helper school): the six
    # fields required; digest a 64-char lowercase hex (re.fullmatch); comparator_id
    # a non-empty str; comparator_class from COMPARATOR_CLASSES (CITED, never
    # re-declared -- the mcp_server.py:97 fork-guard school); scopes a list of
    # str each in SCOPE_TOKENS; audience in AUDIENCES; created_at a str. Every
    # refusal names the line number + the raw value.

def _stat_check(keys_file: Path) -> None:
    # F3: stat().st_mode & 0o002 -> KeyStoreRefusedError(expected "the key store
    # mode 0600", found f"mode {oct(mode & 0o777)} world-writable",
    # next_action f"chmod 600 {keys_file}")

class KeyStore:
    """KeyStore -- the load-at-boot container with the mtime re-read.

    Attributes: .records dict[str, KeyRecord] keyed by digest; .home Path.

    load_keys(home: Path) -> dict[str, KeyRecord]: the absent file -> the EMPTY
    dict, NEVER a refusal; present -> the stat check first, then the pre-pass
    whole (every line parsed + validated before the first use), the records
    returned keyed by digest. Duplicate digest in file -> refusal (found names
    the two line numbers).

    mint(home: Path, comparator_id: str, comparator_class: str, scopes: Sequence[str],
    audience: str, created_at: str | None = None) -> tuple[str, str]:
    THE CEREMONY: (1) validate the arguments at the store (comparator_id
    non-empty; comparator_class in COMPARATOR_CLASSES; every scope in
    SCOPE_TOKENS, empty list refused; audience in AUDIENCES) -> typed refusal,
    exit 1 at the CLI, NEVER argparse choices=; (2) home.parent.mkdir(parents=True,
    exist_ok=True); (3) IF the file exists: the stat check (a world-writable
    store never widened) + the load's pre-pass (the mint appends only to a
    validated whole); (4) key = secrets.token_urlsafe(32) (the 256-bit norm,
    43 chars); digest = hashlib.sha256(key.encode("utf-8")).hexdigest();
    (5) line = json.dumps({"digest": digest, "comparator_id": comparator_id,
    "comparator_class": comparator_class, "scopes": sorted(set(scopes)),
    "audience": audience, "created_at": created_at or
    datetime.now(UTC).isoformat()}, sort_keys=True) + "\\n" -- one write of one
    complete line + newline + flush (the _append_line school); (6)
    os.chmod(home, 0o600) AFTER the write (the exact form: open("a"), write,
    flush, then os.chmod -- the create-and-append both land 0600);
    (7) return (key, digest) -- the key shown ONCE by the caller, never on disk.

    mtime(home: Path) -> float | None: the file's st_mtime or None -- the
    re-read's comparison surface (the mid-flight mint seen live).
    """

def resolve_auth_mode(raw: str | None) -> str:
    """F1: None or 'on' -> 'on'; 'off' -> 'off'; ANY OTHER VALUE -> 
    KeyStoreRefusedError(expected "AUTH one of on|off (or unset)", found the
    value verbatim, next_action "fix the AUTH value in the environment or
    Makefile and reboot -- a typo'd knob never silently means either")."""

def render_boot_marker(home: Path, mode: str, count: int) -> str:
    """The marker's exact bytes (the boot form, the log channel): 
    f"auth: {mode} | keys: {resolved_absolute_home} | count: {count}" when
    the store is present; absent store (count 0, mode on): 
    f"auth: {mode} (failopen -- no key store) | keys: {home} | next-action: 
    prioritree key mint" -- the absence LOUD, never silent (F1)."""
```

## 2. src/prioritree/key_verify.py — THE VERIFY WHOLE (fenced bytes)

```python
"""key_verify -- the wire door: verify the presented key against the store.

The verify contract: the presented key -> sha256 hexdigest -> the in-memory
dict lookup -> hmac.compare_digest at the ONE point -> the KeyRecord identity
(comparator_id + comparator_class + scopes + audience), or the 401 data.
The miss-path dummy compute (F9): the wrong key hashes a DUMMY digest first
(equalized work -- the short-circuit killed); the audience check (F5: the
tier's audience at the door, a wrong-audience key the SAME 401 -- the oracle
never fed); the class check (F8: the record's class the verified truth, the
body's self-claim never consulted here); the scope check (the route's
required scope vs the record's scopes -- the 403's source). The 401/403
bodies are TYPED DATA (the service's three-field constants cited by name),
never str(e) reparsed -- the next unit wires them into the per-route
dependencies through render_refusal. The stat ride: per-verify the mtime
compared -- changed -> the full re-load (the validation re-firing); a
mid-flight mint lands live.
"""

import hashlib, hmac

# The 401 body constants (the service's EXPECTED/FOUND/NEXT_ACTION grammar):
AUTH_HEADER_DEFAULT: Final[str] = "X-Api-Key"  # the name a knob from birth (§2h)

class KeyVerifyError(Exception):  # the 401 data: .expected/.found/.next_action
def verify(store: KeyStore, presented: str, tier_audience: str, required_scope: str | None) -> KeyRecord:
    # (1) digest = hashlib.sha256(presented.encode()).hexdigest(); (2) record =
    # store.records.get(digest) -- if None: digest = hashlib.sha256(DUMMY).hexdigest()
    # re-lookup (F9, the dummy compute -- the miss path's hash count equals the
    # hit's) then raise KeyVerifyError(401: expected f"the key in the
    # {AUTH_HEADER} header", found "absent-or-unknown", next_action
    # "mint a key: prioritree key mint <comparator-id> --class <human|llm>
    # --scopes <csv> --audience <tier>"); (3) hmac.compare_digest(digest, digest)
    # at the ONE point -- the fence test pins source.count("compare_digest") == 1;
    # (4) F5: record.audience != tier_audience -> the SAME 401 (never naming the
    # record's audience); (5) F8: the record's class returned WHOLE (the identity
    # carries it; no body claim taken); (6) required_scope not None and not in
    # record.scopes -> KeyScopeError(403: expected f"the {required_scope} scope",
    # found f"the key's scopes {sorted(record.scopes)}", next_action "re-mint
    # with the scope: prioritree key mint ... --scopes <csv>+{required_scope}");
    # (7) the stat ride: store.reload_if_changed(home) before the lookup (the
    # mtime compared, changed -> the full re-load).
```

## 3. cli.py's KEY REGION (the mint's subcommand, fenced)

```python
# New constants: KEY = "key"; MINT = "mint"; FLAG_CLASS = "--class";
# FLAG_SCOPES = "--scopes"; FLAG_AUDIENCE = "--audience"; MARKER_KEY = "key";
# MARKER_DIGEST = "digest"; MARKER_MODE = "mode".
# _build_parser: subparsers.add_parser(KEY, help="the key tools") with its OWN
# nested add_subparsers(dest="action", required=True); mint_parser =
# key_sub.add_parser(MINT, parents=[parent], ...) -- comparator_id positional
# (help "the operator id the key names"); --class default "human" (NO choices=:
# door-validated, exit 1); --scopes required, a comma list (default none --
# split on ",", the store validates); --audience default "service". The shared
# parent's --home is the KEYS home: the mint composes its OWN parent parser
# (default=KEYS_HOME, NOT STORE_HOME -- the two homes never conflated).
# _command_key_mint: key, digest = KeyStore.mint(KEYS home, ...) under
# Lock(keys_home); render: key\t{key}\ndigest\t{digest}\nmode\t0600\n (the
# plaintext ONCE, marker-first tab-separated via _report). The exit mapping
# UNCHANGED: KeyStoreRefusedError joins the exit-1 tuple clause.
```

## 4. THE TEST FILES (three, the arcs fenced by name)

tests/test_key_store.py (~13 functions): the mint's record bytes (six fields, sort_keys); the 0600 mode (stat == 0o600); the second mint's append (two lines); the mint's world-writable refusal (chmod 0o666 first); the load's stat refusal (chmod 0o666 -> the three fields); the corrupt-line parametrize (7 ids: non-hex digest, wrong-length digest, class-outside, scope-outside, audience-outside, missing-field, crash-tail); the absent-store-empty-dict-never-a-refusal; the mtime re-read (mid-flight mint live); the mid-flight chmod refused at re-load; the marker's two renders (present: count+home; absent: failopen+next-action); the knob's three (default on, AUTH=off, AUTH=typo refused -- parametrized 3); the mint's vocabulary refusals (bad class/scope/audience at the store, exit-1 data); the scopes sorted-deduped on the wire.
tests/test_key_verify.py (~9): the right key -> the record's identity whole; the wrong key -> the 401 three fields byte-exact; the dummy compute arc (the miss path's sha256 call count == the hit's -- monkeypatch the counter); the one-compare-site fence (source scan: "compare_digest" count == 1, the test_service_store.py:238 school); the audience check (mcp-audience key at the service door -> the SAME 401, never naming mcp); the class override (the record's class returned; no claim parameter exists); the scope check's two (granted passes; ungranted -> the 403 data); the reload-through-verify (mid-flight mint seen); the absent header (presented empty -> 401).
tests/test_key_mint.py (~8, the test_cli.py school): the success stdout (key\\tdigest\\tmode lines, exit 0); the plaintext once (stdout once, the file plaintext-ABSENT -- key not in file bytes); the record on disk (digest present, 0600); the vocabulary refusals at 1 (parametrize: bad class, bad scope, bad audience); argparse at 2 (missing comparator_id); the --home placement (AFTER the subcommand); the env override home; the second mint appends (two digests).

## 5. THE AUTH KNOB'S EXACT FORM

Makefile: `AUTH ?= on` after :6; the start target's env line widened: `env -u WEB_CONCURRENCY AUTH=$(AUTH) .venv/bin/uvicorn ...`. service.py's construction ONE line after :165: `app.state.auth = resolve_auth_mode(os.environ.get("AUTH"))` + the marker's log-channel render at boot (the next unit's seam noted: the routes read app.state.auth -- NOT touched here). The typo refusal: AUTH=onX -> resolve_auth_mode raises the three-field refusal AT BOOT (loud, the process dies honestly, never a silent on-or-off). Marker at each state: on+present ("auth: on | keys: {abs} | count: {n}"); on+absent ("auth: on (failopen -- no key store) | ... | next-action: prioritree key mint"); off ("auth: off (operator's explicit degrade) | keys: {abs} | count: {n}").

## 6. THE NO-BREAK PROOFS

The six routes untouched (service.py's route bodies byte-identical; the construction gains ONE line + the boot render, no handler edited); the CLI's five standing subcommands untouched (the key group ADDITIVE, the five handlers byte-identical); the floor: 203 -> the spec's count = 13 + 9 + 8 = 30 functions, ~38 runtime items with parametrizes -> ~241 (the build's floor-green step names the exact count at its own make). New per-file rulings, named: key_store.py -- NONE expected (S311 does NOT fire: secrets is not random.*; if the 43-char form ever needs it, the acceptance.py S311 precedent re-cited); key_verify.py -- NONE; tests -- the standing S101/PLR2004 ruling covers all three files; NO new ignore without a ruling (the zero-findings bar).

## 7. THE PER-STEP PLAN (R8, the file-unit; 8 dispatches, the read-backs named)

(1) key_store.py -- read-back: the module imports, the mint round-trip at the REPL, ruff+pyright on the file; (2) key_verify.py -- read-back: the fence's source scan pre-fired, ruff+pyright; (3) cli.py's key region -- read-back: `prioritree key mint --help` bytes, the five standing subcommands re-run green; (4) service.py's construction line -- read-back: the boot marker's bytes in the log at make start, the six routes' 404s unchanged; (5) Makefile's knob lines -- read-back: make start AUTH=off renders the off marker, AUTH=bogus dies loudly; (6) tests/test_key_store.py -- read-back: pytest -k key_store green, ruff green; (7) tests/test_key_verify.py -- read-back: the same; (8) tests/test_key_mint.py -- read-back: the same; then FLOOR-GREEN: make (pytest+ruff+pyright, the exact count named in the step's report). Each dispatch cites this spec + the unit brief; the web/MCP/policy surfaces untouched inside the fence.

## THE TRADE-OFF CARRIED: the 0600+stat floor is a FLOOR, never a cure (the local owner's offline edit remains the revocation path); a daemon's unread marker is still silent (the ops watch the log channel -- the residual named); the six-token vocabulary freezes with the route table (a new route mints a new token -- an amendment, never silent).
## Reported by togo — 2026-11-24T16:07:38Z

THE FOLD (R6) — the crash-tail FileExistsError (jikko's step-8 floor, 244/245): the fix's bytes + the arc's ruling.

THE STORE'S READ-BACK — the dispatcher's store-module location is REFUTED by the bytes: the mint ceremony's home-creation at src/prioritree/key_store.py:481 already rides the never-erroring form —
```
self.home.parent.mkdir(parents=True, exist_ok=True)
```
(the ceremony's docstring :431-432 names it verbatim — the same law web.py's resolve rode: the mkdir-parents form never erroring on the existing home). The store module needs NO correction. The failing mkdir is the arc's OWN setup line — home.parent IS pytest's pre-created tmp_path, and the crash-tail branch bypassed the file's own `_write_keys_file` helper (whose mkdir at tests/test_key_store.py:85 already carries exist_ok=True) to write the line without its newline.

THE FIX — tests/test_key_store.py:198, before:
```
        home.parent.mkdir(parents=True)
```
after (the corrected line — the pre-existing home the healthy case):
```
        home.parent.mkdir(parents=True, exist_ok=True)
```

THE TEST RULING: the arc's expectation is CORRECT — the assertion stands; only the setup line heals. The bytes, tests/test_key_store.py:202-205: `pytest.raises(KeyStoreRefusedError)` around `KeyStore(home)`; `_assert_three_fields(info.value, _CORRUPT_NEEDLES[case])` — crash_tail's needle "complete with its newline" (:62); `assert "line 1" in info.value.found`. The arc asserts the corrupt-tail REFUSAL, never the mkdir's error — once :198 gains exist_ok=True the arc passes as written. The setup mkdir is also superfluous (tmp_path pre-exists; write_text needs no mkdir): exist_ok=True is the minimal fold, deletion the coordinator's option.
