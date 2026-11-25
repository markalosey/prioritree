# Copyright (C) 2026 Mark Losey. All rights reserved.
"""mcp_auth -- the mcp door: the tree's verify behind the substrate's token channel.

The mcp-verified-token unit (the approved unit brief
reports/synthesize/mcp-verified-token.md; the exact-task spec
reports/synthesize/mcpverifiedtokenspec.md): the door whole in ONE home.
(a) THE ADAPTER: a TokenVerifier subclass re-carrying key_verify's verify
WHOLE -- the stat ride, the F9 dummy, the ONE compare, F5 the audience check
all the foundation's own (consumed at its public seam, NEVER re-implemented;
the adapter the SECOND reader of the one store, the service door the first:
one file, two doors); the KeyRecord mapped to the substrate's AccessToken
(scopes sorted, subject the comparator id, the audience and the stamps
transported as the token's claims). (b) THE GRANT MAP: the five tools'
scope tokens as module data (the policy.py ROLE_SCOPES school; five of the
six SCOPE_TOKENS -- votes.census maps to the service state door's token;
NO new vocabulary token born). (c) THE POLICY: ONE server-level callable --
the hide-and-refuse's single decision (the same AuthCheck hides from
tools/list and search AND refuses the guessed name, the substrate's own
composition; the opaque denial the substrate's own law, pinned as tested
behavior, never a bug). (d) THE AUTH READER: the AUTH knob resolved ONCE at
the door's import (a typo'd value refuses loudly, the boot dies honestly);
AUTH=off NEVER fires the hide -- the construction conditional AND the
policy's per-call read, both load-bearing. (e) THE BOOT MARKER:
render_boot_marker reused whole (never re-authored), emitted at the door's
boot on the host's pre-configured channel.
THE SUBSTRATE'S NATIVE VERIFIER FORMS, PRICED AND REFUSED per the design:
JWTVerifier (9.1x-36.4x the wire, the second secret's custody, RFC 8725's
downgrade class); StaticTokenVerifier (the closest native shape -- refused
at the hashed-at-rest law: its plaintext token dict the exact shape this
tree's store refuses, its own docstring "Never use this in production");
InMemoryOAuthProvider (the OAuth consent ceremony kills the llm ride). The
adapter IS the tree's verify behind the protocol.
THE MANIFEST ABSENCE, named never silent: the grant map carries five of
the six SCOPE_TOKENS; manifest rides the SERVICE tier's sixth route alone
-- the mcp tier has NO manifest tool, and a key minted --scopes manifest
alone opens NO mcp tool.
TWO TRANSPORT LAWS, ONE KEY FORM: the bearer grammar (Authorization:
Bearer) the transport's own -- the tree's X-Api-Key header knob does NOT
ride at this door; the typed ThreePart NEVER crosses the mcp wire (the
adapter's None the ONE channel, the transport's bearer 401 the only 401;
the scope denial a HIDE, never a taught 403); audience= LEFT UNSET at the
construction (F5 rides inside verify -- the substrate's resource-URL
grammar never bent to the tier noun; the wrong-audience bearer dies at
the same None as the digest miss, the oracle never fed).
"""

from __future__ import annotations

import logging
import os
from types import MappingProxyType
from typing import TYPE_CHECKING, Any, Final

from fastmcp.server.auth import AccessToken, TokenVerifier

from prioritree.key_store import KeyStore, render_boot_marker, resolve_auth_mode, resolve_keys_home
from prioritree.key_verify import KeyVerifyError, verify

if TYPE_CHECKING:
    from collections.abc import Mapping

    from ouncemcp.security.policy import PolicyRequest

__all__ = ["AUTH_MODE", "TOOL_SCOPES", "McpTokenVerifier", "compose_door_kwargs", "gate"]

# The tier constant (the _SERVICE_AUDIENCE school, service.py:111 -- never a
# bare literal at the call site): the mcp door's audience, F5's tier noun.
_MCP_AUDIENCE: Final[str] = "mcp"

# The auth-off literal (the service.py:112 _AUTH_OFF school): key_store's own
# _AUTH_MODE_OFF is private -- the cited literal, the fork caught by the arcs.
_AUTH_OFF: Final[str] = "off"

# The adapter's client_id (a named module constant, never a bare literal):
# the door's own name in the token's principal space.
_CLIENT_ID: Final[str] = "prioritree-mcp"

# THE GRANT MAP AS DATA (the ROLE_SCOPES school): each mcp tool's scope token
# -- literals riding key_store's SCOPE_TOKENS vocabulary (the match pinned by
# the fork-guard arc, never by an import coupling this door to the
# vocabulary's machinery); the mapping a frozen proxy (reads only);
# DEFAULT-DENY: a tool absent from the map denies at the policy's own leg
# (the substrate's unknown-name denial the twin); votes.census maps to the
# service state door's token; manifest has NO mcp tool (the module docstring's
# named gap).
TOOL_SCOPES: Final[Mapping[str, str]] = MappingProxyType(
    {
        "runs.register": "register",
        "runs.next": "next",
        "votes.cast": "cast",
        "votes.census": "state",
        "runs.tally": "tally",
    },
)

# The marker's channel (the brief's open, ruled here): the HOST'S
# PRE-CONFIGURED boot channel -- fastmcp's import-time config attaches the
# stderr handler to the "fastmcp" logger BEFORE any prioritree module boots
# (fastmcp/__init__.py:21-26), so the child logger's INFO render rides the
# same channel the --serve banner and the transport lines ride (pinned in
# .prioritree/mcp-server.log -- the one log the Makefile :83 redirect
# captures). The service's "uvicorn.error" school re-carried at this tier's
# host: the marker rides the host's channel. THE PRICES, named: under pytest
# the channel IS configured (fastmcp imports at collection) -- the silence is
# pytest's capture, NOT the service's unconfigured-channel drop (the
# deviation named, never assumed); the host's log_enabled/log_level knobs
# govern the channel (the same school as uvicorn's log_level governing the
# service's marker); the handler's chrome and wrap the host's own form (the
# banner's kin, pinned in the live log).
_BOOT_LOG_CHANNEL: Final[str] = "fastmcp.prioritree.mcp_auth"

# THE BOOT (the service school :209-213): the AUTH knob read ONCE here (the
# carrier landed at Makefile :83; the reader THIS unit) -- a typo'd value
# refuses LOUDLY (resolve_auth_mode's own typed refusal: the process dies
# honestly, never a silent on-or-off); the store minted over the SAME home
# the service door reads (resolve_keys_home().absolute() -- one file, two
# doors); the marker the store module's own three-state render. AUTH_MODE a
# plain module member -- read PER CALL by the policy (the app.state.auth
# school; the fixture's rebind seam), never boot-captured at the policy's
# leg; _keys the same rebind seam (the adapter reads it at call time).
AUTH_MODE: str = resolve_auth_mode(os.environ.get("AUTH"))
_keys: KeyStore = KeyStore(resolve_keys_home().absolute())
logging.getLogger(_BOOT_LOG_CHANNEL).info(
    render_boot_marker(_keys.home, AUTH_MODE, len(_keys.records)),
)


class McpTokenVerifier(TokenVerifier):
    """McpTokenVerifier -- the mcp door's adapter: the tree's verify behind the substrate's token channel.

    Purpose: re-carry key_verify's verify contract WHOLE at the substrate's
    one channel -- the presented bearer through verify(_keys, presented,
    "mcp", None), the KeyRecord mapped to the substrate's AccessToken
    (token the presented, client_id the named constant, scopes sorted,
    subject the record's comparator id -- the idempotency keying
    COMPARATOR-STABLE across re-mints; the audience and the stamps
    transported as the token's claims -- F8's verified class riding as
    data, the cast door's stamp source). required_scope=None RULED: the
    tool is not known at the transport's verify leg (the scopes ride the
    AccessToken, the per-tool grant the policy's own -- authentication at
    the door, authorization at the policy).
    Refuses when: never itself -- KeyVerifyError (the absent, unknown, or
    wrong-audience key: the SAME 401-lane form, the oracle never fed) is
    CAUGHT and returned as None (the transport's bearer 401 the
    consequence, never the tree's ThreePart); the store's OWN refusals
    (F3's world-writable mode, the corrupt line at the stat ride's
    re-load) ride through UNCAUGHT by type -- the crash lane, the
    uncaught-traceback honesty (the operator's broken store is not the
    caller's refusal).
    Re-run: deterministic given the store state (the stat ride's re-load
    aside -- a mid-flight mint lands live by design).
    Touches: the module's _keys container at most (the verify seam's own
    stat ride); never the key bytes on disk (hashed-at-rest).
    Provenance: the unit brief §1a/§2a/§2e, rikai map 1 (the adapter's
    shape), G-MCP-VERIFIED-TOKEN-BRIEF.
    """

    async def verify_token(self, token: str) -> AccessToken | None:
        """Verify the presented bearer token -- the record mapped whole, or None.

        Purpose: the tree's verify WHOLE re-carried -- the stat ride, the
        F9 dummy, the ONE compare, F5 the audience check (the
        wrong-audience key the SAME None as the digest miss); on success
        the KeyRecord mapped to the substrate's AccessToken whole -- the
        record's own fields the token's data (the claims the cast door's
        stamp source).
        Refuses when: never itself -- KeyVerifyError -> None (the ONE
        channel; the class docstring's own refusal clause).
        Re-run: deterministic given the store state.
        Touches: the module's _keys container at most.
        Provenance: the unit brief §1a (the adapter's exact composition),
        key_verify.py:141 (the contract whole), G-MCP-VERIFIED-TOKEN-BRIEF.
        """
        try:
            record = verify(_keys, token, _MCP_AUDIENCE, None)
        except KeyVerifyError:
            return None
        return AccessToken(
            token=token,
            client_id=_CLIENT_ID,
            scopes=sorted(record.scopes),
            subject=record.comparator_id,
            claims={
                "aud": record.audience,
                "comparator_id": record.comparator_id,
                "comparator_class": record.comparator_class,
            },
        )


# The door's one adapter instance (stateless -- the store read at call time
# from the module member; the compose's carrier).
_verifier: Final[McpTokenVerifier] = McpTokenVerifier()


def gate(request: PolicyRequest) -> bool:
    """Gate each tool on the caller's granted token -- the hide-and-refuse's one decision.

    Purpose: THE ONE POLICY: read AUTH_MODE per call (off -> allow -- the
    anonymous ride whole, the degrade never a lockout; the member read,
    never boot-captured); the map's row for the requested tool (absent ->
    False, DEFAULT-DENY live at the policy's own leg -- the substrate's
    unknown-name denial the twin); the caller's scopes against the row's
    token -- identity.authenticated AND the token granted; anything but
    True denies (the substrate's own fails-closed law, policy.py:43-51).
    WIRED AT THE SERVER LEVEL (compose_door_kwargs) -- composed onto every
    tool by the substrate's own chain: the SAME decision hides the tool
    from tools/list and search AND refuses the call by a guessed name (the
    substrate's one-decision composition); the denial OPAQUE (no scopes
    disclosed -- the teaching loss the substrate's own law, the design's
    accepted price, pinned as tested behavior, never a bug).
    Refuses when: never -- False IS the refusal (the hide); the denial
    discloses nothing (the unauthorized agent cannot tell broken-server
    from unauthorized-self).
    Re-run: deterministic -- a pure read over the frozen map, the boot
    member, and the request's own identity.
    Touches: nothing -- pure over its argument and the module's data.
    Provenance: the unit brief §1c/§1d-ii/§2b, rikai map 2 (the grant map
    lift), G-MCP-VERIFIED-TOKEN-BRIEF.
    """
    if AUTH_MODE == _AUTH_OFF:
        return True
    token = TOOL_SCOPES.get(request.tool)
    if token is None:
        return False
    return request.identity.authenticated and token in request.identity.scopes


def compose_door_kwargs() -> dict[str, Any]:
    """Compose the door's construction kwargs -- auth and policy at on, the empty plain form at off.

    Purpose: THE ONE COMPOSE SITE: AUTH=on -> {"auth": the adapter,
    "policy": the gate} -- auth= riding OunceServer's **fastmcp_kwargs to
    FastMCP's own auth parameter (core/server.py:778/:787, the substrate's
    pass-through; the bearer middleware mounted at the transport);
    AUTH=off -> {} -- the PLAIN construction byte-identical (NEITHER
    auth= NOR policy=: the bearer middleware never mounted, the pre-auth
    surface whole over HTTP -- the degrade never a lockout). The
    stdio_policy kwarg NEVER rides (the substrate default "trust" -- the
    spawn IS the credential, the enforce form priced and refused at the
    design).
    Refuses when: never -- a pure read over the boot's members.
    Re-run: deterministic given the boot state (the member's rebind the
    fixture's seam).
    Touches: nothing.
    Provenance: the unit brief §1d-i/§1e/§2a (the construction
    conditional), G-MCP-VERIFIED-TOKEN-BRIEF.
    """
    if AUTH_MODE == _AUTH_OFF:
        return {}
    return {"auth": _verifier, "policy": gate}
