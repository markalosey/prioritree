# Copyright (C) 2026 Mark Losey. All rights reserved.
"""key_verify -- the wire door: verify the presented key against the store.

The verify contract: the presented key -> sha256 hexdigest -> the in-memory
dict lookup -> the constant-time compare at the ONE point -> the KeyRecord identity
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

from __future__ import annotations

import hashlib
import hmac
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from prioritree.key_store import KeyRecord, KeyStore

__all__ = ["AUTH_HEADER_DEFAULT", "KeyScopeError", "KeyVerifyError", "verify"]

# The 401 body constants (the service's EXPECTED/FOUND/NEXT_ACTION grammar):
AUTH_HEADER_DEFAULT: Final[str] = "X-Api-Key"  # the name a knob from birth (§2h)

# The F9 dummy (the miss path's equalizer): the fixed sentinel hashed on the
# miss -- the short-circuit killed (the miss path's hash work equalized with
# the hit's); its digest matches no minted key by construction (the mint's
# tokens are random, never this fixed sentinel).
_DUMMY: Final[bytes] = b"prioritree-key-verify-f9-dummy"


class KeyVerifyError(Exception):
    """KeyVerifyError -- the 401's typed data: expected, found, next_action.

    Purpose: carry the 401 body's three fields as data -- the unverified key
    IS the refusal; raised, never returned. Every leg that must not teach
    which leg fired renders the SAME form (the digest miss, the failed
    compare, the audience mismatch: the identity oracle never fed); the next
    unit's per-route dependencies catch this type and render the fields at
    the service's one render point (never str(e) reparsed).
    Refuses when: never -- it IS the refusal; the message renders all three
    fields so an uncaught traceback still names the legal form.
    Re-run: deterministic -- the same refusal carries the same three fields.
    Touches: nothing -- a plain Exception subclass (zero runtime deps).
    Provenance: the StoreRefusedError grammar (run_store.py:77, the
    three-field school, the N818 Error-suffix family); the exact-task spec
    §2 (the 401 data: .expected/.found/.next_action); F5 (the wrong audience
    the SAME 401).
    """

    def __init__(self, expected: str, found: str, next_action: str) -> None:
        """Initialize the 401's three named fields plus the rendered message.

        Purpose: carry expected/found/next_action and render all three in
        the message (the uncaught-traceback honesty; the class name carries
        the 401).
        Refuses when: never.
        Re-run: idempotent.
        Touches: nothing.
        Provenance: the StoreRefusedError __init__ school (run_store.py:77).
        """
        self.expected = expected
        self.found = found
        self.next_action = next_action
        _prefix = "refused"
        super().__init__(f"{_prefix} — expected: {expected} | found: {found} | next: {next_action}")


class KeyScopeError(Exception):
    """KeyScopeError -- the 403's typed data: expected, found, next_action.

    Purpose: carry the 403 body's three fields as data -- the key verified
    but the route's required scope not granted (the authorization half's
    own refusal, distinct from the 401's authentication half: the key good,
    the room denied); raised, never returned; the next unit's per-route
    dependencies catch this type and render the fields at the service's one
    render point (never str(e) reparsed).
    Refuses when: never -- it IS the refusal; the message renders all three
    fields so an uncaught traceback still names the legal form.
    Re-run: deterministic -- the same refusal carries the same three fields.
    Touches: nothing -- a plain Exception subclass (zero runtime deps).
    Provenance: the StoreRefusedError grammar (run_store.py:77, the
    three-field school, the N818 Error-suffix family); the exact-task spec
    §2 step (6) (the 403: the route's required scope vs the key's scopes);
    Q-auth-design's scope ruling (authentication AND authorization -- the
    401 the first half, the 403 the second).
    """

    def __init__(self, expected: str, found: str, next_action: str) -> None:
        """Initialize the 403's three named fields plus the rendered message.

        Purpose: carry expected/found/next_action and render all three in
        the message (the uncaught-traceback honesty; the class name carries
        the 403).
        Refuses when: never.
        Re-run: idempotent.
        Touches: nothing.
        Provenance: the StoreRefusedError __init__ school (run_store.py:77).
        """
        self.expected = expected
        self.found = found
        self.next_action = next_action
        _prefix = "refused"
        super().__init__(f"{_prefix} — expected: {expected} | found: {found} | next: {next_action}")


def _refuse_unknown_key() -> KeyVerifyError:
    """Refuse the unknown key -- the 401's three fields constructed once.

    Purpose: THE SAME 401 at every leg that must not teach which leg fired
    (the digest miss, the failed compare, the audience mismatch -- all
    three the SAME form: the identity oracle never fed -- a caller probing
    key after key learns nothing about the store's contents).
    Refuses when: never -- it IS the 401's constructor.
    Re-run: deterministic -- the same three fields every call.
    Touches: nothing -- a pure construction over the module's constant.
    Provenance: the exact-task spec §2 (the 401 body: expected the named
    header / found absent-or-unknown / next-action the mint -- prioritree
    key mint); F5 (the wrong audience the SAME 401); the unit brief §1.4
    (the found "absent-or-unknown" -- the header absent, the key unknown,
    the wrong audience: the oracle never fed).
    """
    return KeyVerifyError(
        expected=f"the key in the {AUTH_HEADER_DEFAULT} header",
        found="absent-or-unknown",
        next_action=(
            "mint a key: prioritree key mint <comparator-id> --class <human|llm> --scopes <csv> --audience <tier>"
        ),
    )


def verify(store: KeyStore, presented: str, tier_audience: str, required_scope: str | None) -> KeyRecord:
    """Verify the presented key -- the record whole or the typed refusal.

    Purpose: THE VERIFY CONTRACT -- the presented key -> the sha256 hash ->
    the digest lookup against the loaded records -> the record -> the
    identity + class + scopes + audience (F8: the record's class the
    verified truth -- no claim parameter exists, the body's self-claim never
    consulted here); the F5 audience check at the door (the tier's audience
    vs the record's -- a wrong-audience key the SAME 401, never naming the
    record's audience); the scope check (the route's required scope vs the
    record's scopes -- the 403's source); the stat ride before the lookup
    (the mtime compared -- changed -> the full re-load: a mid-flight mint
    lands live).
    Refuses when: the key absent-or-unknown at this tier (KeyVerifyError --
    the 401's three fields; the header absent, the key unknown, the wrong
    audience, and the unverifiable digest all render the SAME form); the
    required scope not among the record's scopes (KeyScopeError -- the
    403's three fields).
    Re-run: deterministic -- the same presented key against the same loaded
    records yields the same record or the same refusal (the stat ride's
    re-load aside: a mid-flight mint lands live by design).
    Touches: the store's loaded state at most (the stat ride's re-load);
    never the key bytes on disk (hashed-at-rest -- only the digest crosses
    this door).
    Provenance: the exact-task spec §2 (the verify contract whole: the F9
    dummy compute, the ONE compare point, F5/F8, the scope check, the stat
    ride); the unit brief §2d/e/f; Q-auth-design's scope ruling
    (authentication AND authorization -- the 401 the first half, the 403
    the second).
    """
    # The stat ride (the spec's step 7, placed before the lookup): the mtime
    # compared -- changed -> the full re-load (the validation re-firing); a
    # mid-flight mint lands live.
    store.reload_if_changed(store.home)
    # (1) the presented key -> the sha256 hash (hashed-at-rest: only the
    # digest is ever sought, never the plaintext).
    digest = hashlib.sha256(presented.encode()).hexdigest()
    # (2) the digest lookup against the loaded records.
    record = store.records.get(digest)
    if record is None:
        # The F9 dummy compute (the spec's step 2): the miss path hashes the
        # dummy and re-looks-up before refusing -- the short-circuit killed,
        # the miss path's hash work equalized with the hit's; the re-lookup's
        # result is never a record (the fixed sentinel hashes to no minted
        # key -- its work is the point, its result nothing).
        digest = hashlib.sha256(_DUMMY).hexdigest()
        store.records.get(digest)
        raise _refuse_unknown_key()
    # (3) the ONE compare point (the fence test pins the source's count of
    # this call at one): the computed digest against the record's own -- the
    # constant-time compare, never ==.
    if not hmac.compare_digest(digest, record.digest):
        raise _refuse_unknown_key()
    # (4) F5: the tier's audience at the door -- a wrong-audience key the
    # SAME 401 (never naming the record's audience: the oracle never fed).
    if record.audience != tier_audience:
        raise _refuse_unknown_key()
    # (5) F8: the record's class the verified truth -- the identity carries
    # it whole (no claim parameter exists; the body's self-claim never
    # taken).
    # (6) the scope check: the route's required scope vs the record's scopes.
    if required_scope is not None and required_scope not in record.scopes:
        raise KeyScopeError(
            expected=f"the {required_scope} scope",
            found=f"the key's scopes {sorted(record.scopes)}",
            next_action=f"re-mint with the scope: prioritree key mint ... --scopes <csv>+{required_scope}",
        )
    return record
