<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/mcpverifiedtokenspec

**Route:** prioritree-auth (executing) | **Events:** 7 | **Reports:** 3

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-25T00:53:55Z |
| 2 | report | togo | 2026-11-25T01:12:24Z |
| 3 | report | togo | 2026-11-25T01:13:13Z |
| 4 | result | shinko | 2026-11-25T01:13:44Z |
| 5 | gate | shinko | 2026-11-25T01:14:25Z |
| 6 | dispatch | shinko | 2026-11-25T01:52:41Z |
| 7 | report | togo | 2026-11-25T01:57:21Z |
## Reported by togo — 2026-11-25T01:12:24Z

# THE MCP-VERIFIED-TOKEN EXACT-TASK SPEC — togo (synthesize/mcpverifiedtokenspec, 2026-11-25)

## 0. THE GROUND READ WHOLE (every file cited)

The approved unit brief (reports/synthesize/mcp-verified-token.md — §1a-g the scope fence, §2a-f the mechanisms ruled, §3 the arcs' shape, §4 the acceptance mapping, §5 the handoff's opens); tansa's census (reports/discover/mcp-verified-token.md — mcp_server.py whole [:111-114 the plain construction, :475/:501/:521/:546/:558 the five tools, :541 the cast catch's tuple, :594-607 the run forms], the substrate ouncemcp 1.0.0rc3 pinned at the installed source, Makefile :7/:83, opencode.json :579-597, the tests' 34 collected of the 299 floor, the eight flags); rikai's maps (reports/understand/mcp-verified-token.md — the six maps: the adapter's shape, the grant map lift, the stdio trust, the audience door, the fixture seam, the config knobs); the landed foundation read whole this pass: key_verify.py (208 — the verify contract :141-208 [the stat ride :174, the F9 dummy :180-188, the ONE compare :192, F5 :196-197, the scope check :202-207], KeyVerifyError :41-75, _refuse_unknown_key :116-138 — the SAME 401 at three legs); key_store.py (600 — SCOPE_TOKENS :52, AUDIENCES :53, KeyRecord :98-125, the mint :417-508, KeyStore :305-551, resolve_auth_mode :554-578, render_boot_marker :581-600, resolve_keys_home :144-161); policy.py (89 — ROLE_SCOPES :41-47, the MappingProxyType school); votes.py (:137 SupersedeRefusedError, :497-505 the stage-5 author check, found eliding the author); service.py (672 — :111 _SERVICE_AUDIENCE, :112 _AUTH_OFF, :195-213 the boot, :219-222 _ANONYMOUS, :225-252 require_key, :527-528 the verified stamps); mcp_server.py (611 whole — the census's line-pins re-verified). The substrate read at the .venv source this pass: ouncemcp testing.py (59 — make_token :21-48, as_caller :51-59), security/policy.py (181 — PolicyRequest :23-37, evaluate :43-51 fails-closed, policy_check :146-181 [the unknown name → False :163-164, the audience gate :172-173]), security/identity.py (108 — Identity :20-46 [authenticated default True :46], identity_from_token :68-90, ANONYMOUS_IDENTITY :52), core/server.py (the constructor :747-853 [policy :765, audience :766, stdio_policy :770 the "trust" default, **fastmcp_kwargs :778 → FastMCP :787], RESERVED/INJECTED :132-151, the registration :1282-1294, the composition :1365-1378, list_tools :1802-1808 → wire_tools, call_tool :1817-1819, http_app :1823-1827), core/wire.py (13 — the in-memory Client), core/errors.py (545 — PermissionDenied :99-102 "The caller is known and not allowed. Never suggest broader authority.", the classify :417-424 OunceError lane, :462-463 the AuthorizationError → permission lane), ouncemcp/__init__.py (PermissionDenied + ToolContext exported :31-40/:23); fastmcp server/auth/__init__.py (85 — AccessToken + TokenVerifier exported :3-11), server/auth/auth.py (TokenVerifier :525-558 — async verify_token → AccessToken | None the ONE channel; get_middleware :479-491 BearerAuthBackend), server/server.py (_get_auth_context :325-343 [stdio → skip], _component_auth_allows :311-322, the list filter :1043, _get_tool :1045-1069 [unauthorized → None], the call's raise :1670 NotFoundError("Unknown tool: ..."), call_tool :1563-1617 [Raises: NotFoundError]), server/context.py (:91-106 — _current_transport default None; set_transport/reset_transport), server/mixins/transport.py (:214-251 — run_stdio_async ARMS set_transport("stdio") at :235, reset :251 — THE TRUST'S TRIGGER), server/http.py (:394-416 — RequestContextMiddleware sets the transport for HTTP alone), utilities/logging.py (configure_logging :42-123 — the "fastmcp" logger's stderr handler, propagate=False), fastmcp/__init__.py (:21-26 — the import-time config), mcp/server/auth/provider.py (AccessToken :53-60), fastmcp/exceptions.py (AuthorizationError :89, NotFoundError :78-86). The sibling specs' house form (reports/synthesize/keyinfrastructurespec.md, reports/synthesize/servingtierintegrationspec.md). The tests read whole: test_mcp_server_face.py (709), test_service_auth.py (:87-140 the fixture + _grant + _assert_same_401 schools). pyproject.toml whole (ruff ALL + the per-file named rulings; pyright strict + reportUninitializedInstanceVariable/reportUnnecessaryTypeIgnoreComment/reportCallInDefaultInitializer). The live log (.prioritree/mcp-server.log — the banner and the transport lines' channel pinned: the fastmcp namespace renders stderr at INFO at the --serve boot). opencode.json's mcp block; Makefile whole; .prioritree/ (no keys.jsonl — the live state on+absent).

THE LOAD-BEARING DISCOVERIES THIS PASS (the spec's own, each pinned at source — the brief's opens ruled on the installed bytes):
1. THE STDIO TRUST'S TRIGGER IS REAL: mixins/transport.py:235 arms set_transport("stdio") — over real stdio, _get_auth_context returns skip_auth=True and FastMCP skips component authorization (the spawn-is-the-credential law holds by the installed bytes); over HTTP (http.py:394-416 sets "streamable-http") and IN-PROCESS (the contextvar None) the checks APPLY — rikai map 3's law verified, not assumed.
2. THE ctx PARAM'S DISCOVERY KEYS ON THE ANNOTATION BEING EXACTLY ToolContext (core/server.py:1289): a union annotation (ToolContext | None) falls to plain_params and fails registration (TypeError :1295-1298). The cast tool's ctx is `ctx: ToolContext` — no default; the direct-call test tier constructs the context (ToolContext's three required fields, the dataclass :187-225).
3. THE MARKER'S CHANNEL: uvicorn's "uvicorn.error" configures inside run() (uvicorn/config.py:303) — AFTER the door module's import-time boot: an import-time marker on it would DROP (moho's F7 standing). The ONE pre-configured stderr logging channel at the door's boot is the fastmcp namespace (fastmcp/__init__.py:21-26 attaches the stderr RichHandler at INFO at the host's import — before any prioritree module). The marker rides a child of the host's boot channel — the service's uvicorn.error school re-carried at this tier's host (§1g names the prices).
4. THE DENIED TOOL'S IN-PROCESS CALL RAISES NotFoundError("Unknown tool: {name!r}") (server.py:1670) — the opaque guessed-name form, indistinguishable from absence: the teaching loss assertable as behavior (the message never names the scope or the grant).
5. THE SUPERSEDES REFUSAL'S MCP CLASS IS PermissionDenied (core/errors.py:99-102 — "The caller is known and not allowed. Never suggest broader authority.") — the service tier's 403 lineage at the substrate's error vocabulary; the render still the module's ONE render point.

## 1. src/prioritree/mcp_auth.py — THE DOOR MODULE WHOLE (every byte fenced; the R5/ASCII/ruff-ALL discipline at authoring time)

THE FILE NEW at src/prioritree/mcp_auth.py. The naming law: every public symbol's docstring-title begins with the symbol (the KeyStore/require_key school); the private members the _seam/_lock school (module members, the fixture's rebind seam).

```python
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
from typing import TYPE_CHECKING, Final

from fastmcp.server.auth import AccessToken, TokenVerifier

from prioritree.key_store import KeyStore, render_boot_marker, resolve_auth_mode, resolve_keys_home
from prioritree.key_verify import KeyVerifyError, verify

if TYPE_CHECKING:
    from collections.abc import Mapping

    from ouncemcp.security.policy import PolicyRequest

__all__ = ["AUTH_MODE", "McpTokenVerifier", "TOOL_SCOPES", "compose_door_kwargs", "gate"]

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
    }
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


def compose_door_kwargs() -> dict[str, object]:
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
```

THE MODULE'S OWN RULINGS (each priced, never silent):
- THE MARKER'S CHANNEL (§0-discovery 3): the service's exact channel ("uvicorn.error") is REFUSED at this tier — uvicorn configures it inside run() (config.py:303), AFTER the door's import-time boot: the marker would DROP and moho's F7 would stand. The fastmcp child rides the host's pre-configured stderr channel — the banner's own (pinned in the live log). The prices named at the constant's comment.
- THE KEYERROR CRASH LANE: the adapter ALWAYS mints the three claims; a token that carries the identity without them is a verifier-contract violation — the cast door's direct claims read KeyErrors (the honest crash, the body's claim NEVER consulted at the verified door — the fabrication hole stays closed).
- THE UNCAUGHT STORE LANE: KeyStoreRefusedError at the stat ride rides through verify_token uncaught (the 500-class crash lane, the operator's evidence) — only the CALLER's refusals (KeyVerifyError) become None.
- THE ASYNC-WITHOUT-AWAIT FORM: verify_token's async is the BASE'S CONTRACT (auth.py:556) — not our choice; ruff's RUF029 (preview) never fires under select=ALL; if the floor instruments ever grow it, the named-ruling form rides pyproject.

## 2. src/prioritree/mcp_server.py — THE CONSTRUCTION REGION + THE CAST FOLDS (exact before/after)

### (a) The imports grown
BEFORE (:30): `from ouncemcp import Effect, InvalidInput, NotFound, OunceServer`
AFTER: `from ouncemcp import Effect, InvalidInput, NotFound, OunceServer, PermissionDenied, ToolContext`
BEFORE (:33): `from prioritree.policy import missing_classes` (the first prioritree line)
AFTER: a NEW line before it: `from prioritree.mcp_auth import compose_door_kwargs` (mcp_auth < policy, the isort order; the import FIRES the door's boot — the AUTH resolve, the store load, the marker — BEFORE the construction: the compose reads the booted member).
BEFORE (:41): `from prioritree.votes import COMPARATOR_CLASSES, VotesRefusedError`
AFTER: `from prioritree.votes import COMPARATOR_CLASSES, SupersedeRefusedError, VotesRefusedError`

### (b) The construction at :114 — the auth= composition riding **fastmcp_kwargs
BEFORE (:104-114):
```python
# The module-level objects (the spec Section 2(c); the service.py:158-165
# precedent): the seam injected at construction over the CLI's own store home,
# the server minted plain (OunceServer(name=...) per the census's form; NO
# Budget override -- the startup whole is 25% of the 4,000 default, the
# design brief Section 4), NO runner at import. The naming law: the
# act-statement "Serve the five ops as OunceMCP tools" -- the first word the
# symbol: server.
LOCK_HOME: Final[Path] = STORE_HOME
_seam = Serialize(STORE_HOME)
_lock = Lock(STORE_HOME)
server = OunceServer(name="prioritree")
```
AFTER:
```python
# The module-level objects (the spec Section 2(c); the service.py:158-165
# precedent): the seam injected at construction over the CLI's own store home,
# the server composed over the door's kwargs (OunceServer(name=...,
# **compose_door_kwargs()) -- the auth adapter + the tool-scope policy at
# AUTH=on riding **fastmcp_kwargs to FastMCP's own auth parameter, the PLAIN
# construction byte-identical at AUTH=off: neither auth= nor policy=, the
# bearer middleware never mounted, the degrade never a lockout; NO Budget
# override -- the startup whole is 25% of the 4,000 default, the design brief
# Section 4; NO stdio_policy -- the substrate default "trust", the
# spawn-is-the-credential law), NO runner at import. The naming law: the
# act-statement "Serve the five ops as OunceMCP tools" -- the first word the
# symbol: server.
LOCK_HOME: Final[Path] = STORE_HOME
_seam = Serialize(STORE_HOME)
_lock = Lock(STORE_HOME)
server = OunceServer(name="prioritree", **compose_door_kwargs())
```
THE POLICY WIRING: ONE site — the five tools' rows never touch the decorators (the per-tool policy= form priced and refused at the brief §1c: locality at five sites, the grant data multiplied); the map's five rows live in TOOL_SCOPES, composed onto every tool by the substrate's chain (§1c's ruling).

### (c) The module docstring's amendment (the landing the amendment)
The docstring's tail (":19-22") BEFORE: "NO runner at import (the service's app precedent): the boot the host's command -- bare python -m prioritree.mcp_server is stdio per session; the --serve flag is the shared streamable-HTTP form."
AFTER (one clause grown before "NO runner"): "The mcp-verified-token unit's door (the exact-task spec reports/synthesize/mcpverifiedtokenspec.md): the five ops gated at --serve by the door module's adapter + policy (prioritree.mcp_auth -- the construction's compose at :114; the stdio trust whole: the spawn IS the credential, the checks skipped at the transport), the cast tool's stamps the VERIFIED identity's claims at the authenticated door (the body's self-claims the degrade's fallback). NO runner at import (the service's app precedent): the boot the host's command -- bare python -m prioritree.mcp_server is stdio per session; the --serve flag is the shared streamable-HTTP form."

### (d) The cast tool: the signature's ctx + THE STAMPING DELEGATION (exact before/after)
BEFORE (:521-543) — the signature, the body's head, the catch's tuple:
```python
@server.tool(name="votes.cast", effect=Effect.WRITE, idempotency=True)
def cast(body: CastInput) -> CastAck:
    """Cast one judgment on a pair -- the sitting's only write. The judgment
    [...the docstring BYTE-STANDING, the D205 wire description never forked...]
    """
    try:
        vote_id, _record, count, acknowledged = _seam.cast(
            body.run_id,
            body.pair,
            body.winner,
            body.comparator_id,
            body.comparator_class,
            body.notes,
            body.supersedes,
        )
    except (StoreRefusedError, VotesRefusedError) as refusal:
        raise _refuse(refusal) from refusal
    return CastAck(vote_id=vote_id, count=count, acknowledged=acknowledged)
```
AFTER:
```python
@server.tool(name="votes.cast", effect=Effect.WRITE, idempotency=True)
def cast(body: CastInput, ctx: ToolContext) -> CastAck:
    """Cast one judgment on a pair -- the sitting's only write. The judgment
    [...the docstring BYTE-STANDING -- the wire description never forked...]
    """
    # The verified stamps (the brief §1f): the token's claims over the body's
    # self-claims when the caller is authenticated (F8's law tier-agnostic --
    # the id-binding and the class-binding firing at this door exactly as at
    # the service door, service.py:527-528's school); the degrade's fallback
    # the body's claims (the anonymous identity -- auth off without a token,
    # the trust's stdio ride; the floor's input unverified again, the price
    # named at the boot marker). The claims read DIRECT -- the adapter always
    # mints them; a token carrying the identity without the claims is a
    # verifier-contract violation, the KeyError the honest crash (the body's
    # claim NEVER consulted at the verified door -- the fabrication hole
    # stays closed).
    identity = ctx.identity
    if identity.authenticated:
        comparator_id = str(identity.claims["comparator_id"])
        comparator_class = str(identity.claims["comparator_class"])
    else:
        comparator_id = body.comparator_id
        comparator_class = body.comparator_class
    try:
        vote_id, _record, count, acknowledged = _seam.cast(
            body.run_id,
            body.pair,
            body.winner,
            comparator_id,
            comparator_class,
            body.notes,
            body.supersedes,
        )
    except (StoreRefusedError, VotesRefusedError) as refusal:
        raise _refuse(refusal) from refusal
    except SupersedeRefusedError as refusal:
        raise PermissionDenied(
            _render_three_part(refusal.expected, refusal.found, refusal.next_action),
        ) from refusal
    return CastAck(vote_id=vote_id, count=count, acknowledged=acknowledged)
```
THE CTX LAW (§0-discovery 2): the annotation is EXACTLY `ToolContext` (core/server.py:1289 keys on it; a union or default fails registration); the wrapper injects by parameter NAME at the wire (INJECTED_PARAMS), the direct-call tier constructs its own (§3b's _headless); CAP-6 held — the identity from the verified context, never a model-controlled argument. THE WIRE SCHEMA UNCHANGED: CastInput still parses the stamps (the body's fields unread when authenticated). THE SUPERSEDES FOLD: today's tuple (:541) MISSES SupersedeRefusedError — the override makes the raise live at this tier (the override passes the VERIFIED id into _seam.cast → votes.py's landed stage-5 author check fires on it); the uncaught raise would be the crash lane — the refusal-as-value school demands the leg; PermissionDenied the substrate's own class ("the caller is known and not allowed", core/errors.py:99-102 — the service tier's 403 lineage at this tier's vocabulary), the fields rendered at the module's ONE render point (_render_three_part), found ELIDING the author (votes.py:503's own bytes).

[the spec's continuation — piece 2: §3 the test files, §4 the no-break proofs, §5 the per-step plan, the trade-off]
## Reported by togo — 2026-11-25T01:13:13Z

## 3. THE TEST FILES WHOLE (every arc fenced by name, the counts exact)

### 3a. tests/test_mcp_auth.py (NEW — 24 functions, 37 runtime items; the mint-at-tmp fixture)

THE FILE'S HEAD: the copyright line + the module docstring (the test_service_auth.py:2-29 school): the door's falsification set named — the adapter-ridden arcs (the true chain: the digest lookup, the ONE compare, F5), the policy arcs (the make_token form — the chain exercised, the adapter bypassed, the brief §2d's ruled split), the construction's arcs, the boot's arcs, the hide/guessed-name arcs, the stdio-trust arcs, the stamping arcs, the cross-tier replay both directions, the fork-guard; "The S101/PLR2004 tests ruling stands."

THE IMPORTS: `from __future__ import annotations`; stdlib: `json`, `from pathlib import Path`, `from typing import TYPE_CHECKING, Any`; third-party/substrate: `import pytest`, `from fastmcp.exceptions import NotFoundError`, `from fastmcp.server.auth import AccessToken`, `from fastmcp.server.context import reset_transport, set_transport`, `from ouncemcp import Effect, ToolContext`, `from ouncemcp.security.identity import identity_from_token`, `from ouncemcp.security.policy import PolicyRequest`, `from ouncemcp.testing import as_caller, make_token`; first-party: `from prioritree import mcp_auth, mcp_server`, `from prioritree.key_store import KeyStore, KeyStoreRefusedError, resolve_auth_mode`, `from prioritree.key_verify import AUTH_HEADER_DEFAULT, KeyVerifyError, verify`, `from prioritree.service_store import Serialize`, `from prioritree.store_lock import Lock`.

THE FIXTURE (the mint-at-tmp form, the test_service_auth.py:87-106 school extended to the door's members — BOTH stores isolated: the run store the face's rebind school, the key store the door's rebind seam):
```python
@pytest.fixture
def door(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> KeyStore:
    """Isolate the door by injection -- both stores fresh, the members re-bound.

    Purpose: the run store re-bound over tmp (the test_mcp_server_face.py:124-147
    school -- the tools' bodies read the module globals at call time); the door's
    _keys container over the tmp keys file (the adapter reads it at call time);
    AUTH_MODE pinned "on" (the armed door -- the boot's own default under pytest,
    AUTH unset; the off arcs rebind per test, the member the seam).
    Refuses when: never -- a fixture (the isolate-then-yield form).
    Re-run: deterministic -- a fresh tmp home per test.
    Touches: the tmp home only (pytest's own tmp_path).
    Provenance: mcpverifiedtokenspec §3a (the fixture fence), the
    test_service_auth.py:87-106 + test_mcp_server_face.py:124-147 precedents,
    G-MCPVERIFIEDTOKENSPEC-BRIEF.
    """
    monkeypatch.setattr(mcp_server, "STORE_HOME", tmp_path)
    monkeypatch.setattr(mcp_server, "_seam", Serialize(tmp_path))
    monkeypatch.setattr(mcp_server, "_lock", Lock(tmp_path))
    store = KeyStore(tmp_path / _KEYS_FILE)
    monkeypatch.setattr(mcp_auth, "_keys", store)
    monkeypatch.setattr(mcp_auth, "AUTH_MODE", "on")
    return store
```
THE HELPERS: `_grant(scopes, *, audience="mcp", comparator_class="human", home)` — the test_service_auth.py:109-131 _grant school verbatim (comparator_id "key-holder" the fixed noun; the audience knob the wrong-audience arcs' own); `_verify(key)` — `asyncio.run(mcp_auth.McpTokenVerifier().verify_token(key))` (a fresh stateless instance — the store read at call time from the member); `_token(scopes=(), *, subject="caller", comparator_id="key-holder", comparator_class="human")` — the make_token form: `make_token(subject=subject, scopes=list(scopes), claims={"aud": "mcp", "comparator_id": comparator_id, "comparator_class": comparator_class})`. The vocabulary literals: `_KEYS_FILE = "keys.jsonl"`, `_FIVE = ("register", "next", "cast", "state", "tally")`, `_COMPARATOR = ("next", "cast", "manifest")`, `_OPERATOR = ("register", "state", "tally", "manifest")`, `_AUDITOR = ("state", "tally", "manifest")` (the ROLE_SCOPES rows cited as literals — the fork-guard's school), `_TOOLS = ("runs.register", "runs.next", "votes.cast", "votes.census", "runs.tally")`.

THE ARCS (24 functions; the parametrizes: the marker's 3, the granted 5, the denials 8 — 37 runtime items):

1. `test_right_key_maps_the_access_token_whole(door)` — _grant(_FIVE) → _verify(key) → the AccessToken WHOLE: token == the key; client_id == "prioritree-mcp"; scopes == sorted(_FIVE); subject == "key-holder"; claims == {"aud": "mcp", "comparator_id": "key-holder", "comparator_class": "human"}.
2. `test_wrong_key_refuses_none(door)` — _grant then a bogus "not-the-key" → _verify → None (the F9 dummy's lane; the SAME refusal — no leg distinguishable).
3. `test_absent_token_refuses_none(door)` — _verify("") → None (the empty presented: the digest miss's lane).
4. `test_service_audience_key_at_the_mcp_door_refuses_none(door)` — _grant(_FIVE, audience="service") → _verify → None (THE CROSS-TIER REPLAY'S FORWARD LEG: the digest hits, the compare passes, F5 fires — the same None, the oracle never fed).
5. `test_midflight_mint_lands_live_through_the_adapter(door)` — _verify(_grant(...)) is None for a key minted by a SECOND container over the SAME home after the first load: the stat ride sees it (the adapter the store's second reader, live at both doors).
6. `test_mcp_key_at_the_service_door_the_same_401_reverse_leg(door)` — _grant(_FIVE, audience="mcp") then `with pytest.raises(KeyVerifyError)` around `verify(door, key, "service", None)`: the three fields the landed family's bytes — expected f"the key in the {AUTH_HEADER_DEFAULT} header", found "absent-or-unknown", next_action startswith "mint a key: prioritree key mint" (THE REVERSE LEG; "mcp" ABSENT from the rendered fields whole).
7. `test_armed_compose_carries_auth_and_policy(door)` — `kwargs = mcp_auth.compose_door_kwargs()` → set(kwargs) == {"auth", "policy"}; isinstance(kwargs["auth"], mcp_auth.McpTokenVerifier); kwargs["policy"] is mcp_auth.gate (the armed construction's exact shape).
8. `test_off_compose_the_plain_form_neither_kwarg(door, monkeypatch)` — the member rebind "off" → compose_door_kwargs() == {} (the plain construction byte-identical — the degrade never a lockout).
9. `test_compose_never_passes_stdio_policy_the_trust_default(door, monkeypatch)` — at "on" AND at the re-bound "off": "stdio_policy" not in compose_door_kwargs() (the substrate's "trust" default never overridden — the enforce form priced and refused).
10. `test_stdio_transport_skips_the_checks_anonymous_ride_preserved(door)` — `token = set_transport("stdio")` in try/finally with `reset_transport(token)`: the ANONYMOUS in-process call (NO as_caller) — `asyncio.run(mcp_server.server.call_tool("runs.next", {"run_id": "RUN-9999"}))` → is_error True with the CORE's "Not found:" (the door never consulted — THE TRUST'S EFFECT asserted in-process: the transport's own skip, mixins/transport.py:235's armed contextvar).
11. `test_harness_spawn_bare_no_auth_env_source_scan()` — json.loads(Path("opencode.json").read_text(encoding="utf-8"))["mcp"]["prioritree"]: command == ["uv", "run", "python", "-m", "prioritree.mcp_server"]; "env" not in block; "auth" not in block (the bare spawn pinned — the test_service_store.py:241-245 source-scan school; the spawn IS the credential).
12. `test_boot_marker_three_states(tmp_path)` — parametrized ("on", present, "auth: on | keys:") / ("on", absent, "auth: on (failopen -- no key store)") / ("off", present, "auth: off (operator's explicit degrade)"): render_boot_marker(home, mode, count) — the three exact byte forms (key_store.py:596-600's own), asserting the door's marker IS the store module's renderer (never re-authored).
13. `test_typo_auth_refuses_loudly_at_the_door_boot(door)` — `with pytest.raises(KeyStoreRefusedError, match="AUTH got"): resolve_auth_mode("bogus")` + assert mcp_auth.AUTH_MODE == "on" (the unset-env default the boot read; the typo'd knob dies loudly at the boot, never a silent on-or-off).
14. `test_granted_caller_passes_each_tool(door)` — parametrized the five tools: gate(PolicyRequest(tool=t, effect=Effect.READ, tags=frozenset(), identity=identity_from_token(_token(_FIVE)))) is True for each (the policy chain exercised over the granted token — the adapter bypassed, the brief §2d's ruled form).
15. `test_per_role_denials_default_deny_live(door)` — parametrized the EIGHT rows (_COMPARATOR × register/census/tally; _OPERATOR × next/cast; _AUDITOR × register/next/cast): gate(PolicyRequest(...identity_from_token(_token(role_scopes))...)) is False (DEFAULT-DENY live — the map's rows against the ROLE_SCOPES' literals).
16. `test_hide_from_tools_list_per_caller(door)` — under `as_caller(access_token=_token(_COMPARATOR))`: `names = {t.name for t in asyncio.run(mcp_server.server.list_tools())}` → "runs.next" and "votes.cast" present, "runs.register" absent; under the _AUDITOR token: "votes.census" and "runs.tally" present, "votes.cast" absent (the same AuthCheck's list face — the hide, per caller).
17. `test_guessed_name_refusal_opaque_the_reason_never_disclosed(door)` — under the _COMPARATOR token: `with pytest.raises(NotFoundError, match="Unknown tool: 'runs.register'")`: asyncio.run(mcp_server.server.call_tool("runs.register", {...})) — the refusal INDISTINGUISHABLE from absence (the reason never disclosed: no scope, no grant in the message — the teaching loss PINNED as behavior).
18. `test_auth_off_degrade_no_hide_the_scopeless_ride(door, monkeypatch)` — the member rebind "off" + the SCOPE-LESS subject-only token (as_caller(subject=...) — the standing school's old form): the five tools all REACHED in-process (the register ack, the next pair, the cast ack, the census body, the tally's own halt-or-done — NO NotFoundError anywhere): THE HIDE NEVER FIRES AT OFF (the per-call member read, the degrade never a lockout).
19. `test_verified_class_overrides_the_bodys_claim(door)` — the llm-CLASS claims token (_token(_FIVE, comparator_class="llm")) + the BODY claiming "human": register quorum=2, one cast → the tally's halt names "missing human" (the llm stamp verified — the body's claim never consulted; the class-binding at the door).
20. `test_verified_id_overrides_the_bodys_id(door)` — the same _token(_FIVE) twice, the two casts' BODY ids different ("x" then "imposter"), the second citing supersedes="VOTE-0001": the correction LANDS (VOTE-0002) — the author check passes on the VERIFIED id (the body's id unread: the id-binding at the door).
21. `test_auth_off_class_falls_back_to_the_bodys_claim(door, monkeypatch)` — the member rebind "off" + NO token (the anonymous ride): register quorum=2, one cast with the BODY claiming "llm" → the halt names "missing human" (the body's class stamped — the degrade's price, the floor's input unverified again).
22. `test_supersedes_author_refusal_through_the_door_found_elides(door)` — A's token casts VOTE-0001; B's token (comparator_id="author-b") supersedes it → the PermissionDenied VALUE through the wire: is_error True, "Not permitted:" in the text, the ThreePart's fields present, "another author's vote" in found, and "author-a" ABSENT from the rendered message whole (the elision pinned).
23. `test_own_author_supersede_passes_under_the_verified_id(door)` — the same token supersedes its own VOTE-0001 → lands (VOTE-0002, count 2, acknowledged False) — the author check's pass form under the verified id.
24. `test_fork_guard_the_map_keys_and_tokens()` — set(mcp_auth.TOOL_SCOPES) == the five registered tool names (cited as literals); set(mcp_auth.TOOL_SCOPES.values()) <= {"register", "next", "cast", "state", "tally", "manifest"} (the SCOPE_TOKENS vocabulary as literals — the policy.py fork-guard school; no import coupling).

THE BEARER 401'S GRAMMAR NOTE (the brief §2e, re-carried): the three adapter legs (arcs 2, 3, 4) render the SAME refusal — None at the ONE channel (the transport's 401 the consequence, the WWW-Authenticate challenge alone); the tree's typed ThreePart never crosses; the reverse leg (arc 6) carries the landed family's bytes at the SERVICE door's own lane (locality).

### 3b. tests/test_mcp_server_face.py (GROWN — the 34 standing arcs re-derived where the door changes them; the count 34 STANDS)

THE IMPORTS GROWN: `from fastmcp.server.auth import AccessToken`; `from ouncemcp import InvalidInput, ToolContext`; `from ouncemcp.testing import as_caller, make_token`.
THE VOCABULARY GROWS (after _CALLERS :78):
```python
# The door's granted vocabulary (the five tools' scope tokens -- the map's
# own rows; manifest absent: no mcp tool carries it): the standing arcs'
# default grant under the armed door.
_GRANTED: tuple[str, ...] = ("register", "next", "cast", "state", "tally")
```
THE TOKEN HELPER (NEW, after _join):
```python
def _granted(caller: str, *, comparator_class: str = "human") -> AccessToken:
    """Mint the granted caller token -- the five scope tokens, the door-shaped claims.

    The door-armed harness form: the standing arcs ride the granted token
    (once the policy lands, in-process calls face the checks -- the
    scope-less subject-only tokens deny), the claims shaped as the door's
    adapter mints them (the cast door's stamp source; the class knob the
    corroborating llm casts ride).
    """
    return make_token(
        subject=caller,
        scopes=list(_GRANTED),
        claims={"aud": "mcp", "comparator_id": caller, "comparator_class": comparator_class},
    )
```
THE _call GROWTH — BEFORE (:81-84): `with as_caller(subject=caller):` — AFTER: `def _call(caller: str, tool: str, arguments: dict[str, Any], *, token: AccessToken | None = None) -> ToolResult:` with `with as_caller(access_token=token or _granted(caller)):` (the docstring grows the granted-default clause).
THE _cast GROWTH (:97-121): the return line becomes `return _call(caller, "votes.cast", arguments, token=_granted(caller, comparator_class=comparator_class))` — the class parameter shapes the TOKEN's class claims too (the corroborating twins' llm casts ride it — the arcs' bodies byte-standing, the helper absorbs the door).
THE RE-DERIVED ARCS (the door changes their asserted bytes' SOURCE, never their asserted values):
- `test_cast_resend_acknowledged` (:415-433) — BEFORE: `again = _call(f"caller-{next(_CALLERS)}", "votes.cast", arguments)` — AFTER: `again = _call(caller, "votes.cast", {**arguments, "comparator_id": "imposter"})`. THE TEACHING GROWN: under the armed door a fresh PRINCIPAL is a fresh comparator (a different verified id — the dedup would miss); the ruled re-derived form bypasses the transport guard by the ARGS diff (the same principal, the body's id changed) and hits the CORE's dedup on the VERIFIED id — acknowledged=True with the ORIGINAL's vote_id and count (the asserted values STAND); the fabricated-id dodge dies at the door (the self-claim never forks a voice). The docstring's "from a fresh session" clause re-trued in the same edit.
- `test_cast_winner_refused_at_the_core` (:282-301) + `test_cast_class_refused_at_the_core` (:325-344) — `mcp_server.cast(body)` → `mcp_server.cast(body, _headless())`, with the NEW helper (beside _call):
```python
def _headless() -> ToolContext:
    """Construct the headless tool context -- the direct-call tier's own form.

    The model_construct school (the corrupted body past validation fed to
    the handler): the ctx the wire always injects, constructed bare at the
    direct tier -- the three required fields alone; the identity resolves
    ANONYMOUS outside any caller context (the body's claims stand, the
    core's gates fire on the body's stamps -- the asserted bytes stand).
    """
    return ToolContext(tool="votes.cast", response_format="concise", result_budget=0)
```
- `test_cast_llm_class_lands` (:522-539) — the inline llm body rides the llm-CLAIMS token: `result = _call(caller, "votes.cast", {...}, token=_granted(caller, comparator_class="llm"))` (the teaching preserved — the llm class LANDS; under the default human-claims token the door would stamp human and the class never land).
THE BYTE-STANDING ARCS (verified arc-by-arc against the door): the five success forms, the unknown-run refusals, the schema-gate refusals, the halt arcs (the human-claims default keeps "missing llm" true), the changed-verdict/new-record arcs, the cross-session register (RUN-0002 — the register's guard keys per principal; the fresh caller's token a fresh principal), the same-pair/different-pair supersedes arcs (the same-pair rule fires before the author check; the own-author correction passes on the shared verified id), the seed/default-order arcs, the quorumed-pair skip, the end-to-end sitting + the re-tally (the _cast class knob absorbs the twins), the census-as-is, the parse-argv arc — NO byte changes beyond the four above.
THE DOCSTRING RE-TRUTHINGS (the flag-3 school, the same edit): the harness paragraph grows the granted-token clause (the door-armed harness named); the idempotency paragraph's re-send clause re-trued (the re-derived form); the imports' clause named. THE COUNT: 34 collected stands (the growth re-derives, never adds).

## 4. THE NO-BREAK PROOFS + THE NAMED RULINGS

- THE STDIO DEFAULT PRESERVED: compose_door_kwargs NEVER passes stdio_policy (arc 9); the harness's spawn byte-standing (arc 11's source-scan — opencode.json untouched); the trust's EFFECT asserted (arc 10 — the transport's own skip, armed by the substrate's run_stdio_async, never by our bytes).
- THE FIVE TOOLS' BODIES OTHERWISE BYTE-STANDING: register/serve/audit/tally byte-exact (zero edits); the cast tool's two named folds alone (the ctx signature, the stamping branch, the SupersedeRefusedError catch); the five wire docstrings byte-standing (D205's accepted texts never forked).
- THE SERVICE/WEB TIERS UNTOUCHED: service.py, web.py, votes.py, key_store.py, key_verify.py, policy.py — zero edits (the door consumes the foundation at its public seams; the tiers' doors landed unit 3).
- THE AUTH-OFF DEFAULT AT THE CI: the suite green with NO key store anywhere (the boot's home absent → the empty dict, the failopen marker; every mint at tmp; the standing face arcs ride granted make_token tokens — never the adapter, never a real key); the degrade's lockout-proof arc 18 (the member rebind, the five reached); the CI's own boot state AUTH unset → "on" (the armed door under the suite — the granted fixtures the ride, the bare pytest env never a config).
- THE FLOOR: 299 → **336 collected** — 24 new test functions, 37 runtime items (the singles 21 + the marker's 3 + the granted 5 + the denials 8); the face file's 34 stand. THE BRIEF'S ~335 RECONCILED: its estimate priced ~20 functions/~36 items; the ruled arcs land 24/37 — the +1 item is the stdio-skip EFFECT arc (the ask's own "the stdio trust asserted [the ungated ride preserved]" — the preconditions alone assert nothing about the ride); the estimate's slack returned honestly, the floor-green step names the landed count, any drift ruled at the gate.
- THE NAMED PER-FILE RULINGS IF NEW RIDE (never blanket): NONE expected — mcp_auth.py clean by design (the gate's single param consumed; the adapter's async the base's contract; the compose's zero params); mcp_server.py's D205 ruling STANDS (the docstrings single-paragraph — the cast docstring untouched); test_mcp_server_face.py's PLR0913/PLR0917 ruling STANDS (the _cast helper's six params unchanged); test_mcp_auth.py's helpers under the args bar (_grant 4, _token 5, _verify 1, _headless 0). The zero-findings bar: ruff ALL + pyright strict (with the four reportUn* extras) green at the same make, zero in-code ignores — any finding that lands is a NAMED ruling at pyproject (the precedent form), never a blanket, never an noqa.

## 5. THE PER-STEP PLAN (R8, the file-unit; 5 dispatches, the read-backs named; each dispatch cites the unit brief + this spec — G-MCPVERIFIEDTOKENSPEC-BRIEF's precedence: the build dispatches fire only after both gates)

1. **src/prioritree/mcp_auth.py** (NEW — §1 whole). Read-back: the adapter's legs at the shell (`python -c` over a tmp mint: the right key → the AccessToken whole; the wrong/absent/service-audience keys → None — the same refusal at every leg); compose_door_kwargs' two forms (on: auth+policy; the re-bound off: {}); the marker's three rendered states; ruff/pyright green on the file.
2. **src/prioritree/mcp_server.py** (§2 whole: the imports, the compose at :114, the comment + docstring amendments, the cast tool's three folds). Read-back: the armed construction (the compose's kwargs asserted at a python -c probe), the plain form at the re-bound off; a granted make_token cast stamps the token's id (the census's halt oracle); another-author supersedes → the PermissionDenied value. THE KNOWN-RED WINDOW NAMED: from this dispatch until step 4 the standing face arcs run RED (the armed door denies the scope-less tokens — rikai map 5's load-bearing fact, the step-4 cure; the door's own read-backs above are the step's verification, the full suite's state is step 5's).
3. **tests/test_mcp_auth.py** (NEW — §3a whole). Read-back: the 24 arcs green (37 items collected at `pytest tests/test_mcp_auth.py`), the hide/guessed-name/stamping oracles asserted, the fork-guard pinned.
4. **tests/test_mcp_server_face.py** (§3b whole: _GRANTED, _granted, the _call/_cast growths, the four re-derived arcs, the docstring re-truthings). Read-back: the fixture grown — `pytest tests/test_mcp_server_face.py` → 34 collected, ALL GREEN under the armed door (the standing arcs' asserted values byte-held; the four re-derivations' values equal to today's).
5. **FLOOR-GREEN** (`make`: pytest + ruff + pyright at the same make). Read-back: 336 collected, all green; ruff zero findings; pyright 0/0; the exact count named in the build's report (any drift from 336 ruled at the build gate, never silent).

THE TRADE-OFF THE PLAN MUST CARRY: the hide's teaching loss (the opaque denial — broken-server indistinguishable from unauthorized-self; the substrate's own law, pinned as tested behavior); the bearer grammar's fork (the ThreePart never crossing the mcp wire — the transport's 401 the only 401, the mint's teaching the WWW-Authenticate challenge alone; the scope denial a hide, never a taught 403); the marker's channel prices (the host's pre-configured logger — under pytest the silence is pytest's capture, not the logging layer's drop; the host's log_enabled/log_level knobs govern; the handler's chrome and wrap the host's own form); the adapter as the store's second reader (one file, two doors — the mid-flight mint live at both, the F10 fold holding); the import-time AUTH read (the boot the host's command — a mid-flight env change never seen, the reboot the cure); the ctx param's exact-annotation law (the union form refused at registration — the direct-call tier constructs its own context, the headless form named); the stdio trust's price (every local caller rides ungated by design, the stamps self-claims over stdio — the spawn IS the credential, the §3 floor); the manifest gap (an mcp-audience key minted --scopes manifest alone opens no mcp tool — the standing shape, named never silent); the degrade's unverified stamps (the floor's input the claim again at off — the operator's explicit act, the marker naming it); the verified-door dedup semantics (two keys are two comparators are two voices — the shared-body-id dodge dead; the re-send's loud ack reachable only through the verified id's own re-mint, the §2f comparator-stable keying). Every price named, never silent — the door armed at --serve, the ride preserved at stdio, the honest statement carried whole.

THE SPEC LANDED WHOLE — two report pieces composing one document; the projection at reports/synthesize/mcpverifiedtokenspec.md; the collaborator rules on this record at G-MCPVERIFIEDTOKENSPEC-BRIEF.
## Reported by togo — 2026-11-25T01:57:21Z

FOLD (R6) — the three cross-file reds diagnosed at the bytes; the cure ruled at the honest home.
THE MECHANISM: the substrate's idempotency guard replays WRITES per (principal, tool, args-digest) — ouncemcp/execution/idempotency.py:3-5, :121-132 (make_claim, the key sha256 over principal+tenant+tool+args), :150-161 (a done record returns the STORED result, the handler NEVER re-runs; ttl 24h at :70) — over the process-wide MemoryStore (execution/store.py:71-77) of the module-level server (mcp_server.py:126); the reads (next/census/tally) never idempotent-registered — they always execute against the re-bound home.
THE POISON: test_mcp_auth.py:83 and test_mcp_server_face.py:88 each hold a PRIVATE count(1) minting "caller-{N}" — the pools COLLIDE across files; auth runs first (alphabetical) and seeds caller-4/5/6 — test_auth_off_degrade (:398), test_verified_class_overrides (:443), test_verified_id_overrides (:473) wrote register {items [a,b], quorum 1|2, op-1} + cast {RUN-0001, [a,b], prefer-a, x, human}.
THE VICTIM: the face's test_census_view (:237), test_tally_view_at_full_coverage (:246), test_next_done_terminal (:270) mint THE SAME caller-4/5/6 (the suite run prints them verbatim) — the identical-args register/cast REPLAY auth's acks, never touching the fresh tmp home; the reads execute → {'total': 0}, the coverage halt, "Not found: ... a run file". MY RUNS: the face alone 34 green; the suite 3 failed, 333 passed (33.16s) — jikko's floor EXACT; reads-fresh + writes-replayed = the arcs isolated.
THE CURE AT THE HONEST HOME — the subject mint, the isolation-by-injection school's fourth leg (the fixtures already re-bind STORE_HOME/_seam/_lock; the face docstring :46-52 itself rules the law — "a shared subject would replay an earlier test's writes through the server's process-wide MemoryStore" — the pool was merely file-scoped):
```diff
tests/test_mcp_server_face.py:198 - return f"caller-{next(_CALLERS)}" + return f"face-{next(_CALLERS)}"; :505 the same inline mint → f"face-{next(_CALLERS)}"
tests/test_mcp_auth.py — the nine mints at :349/:354/:371/:398/:443/:473/:543/:564/:591: f"caller-{next(_CALLERS)}" → f"door-{next(_CALLERS)}"
```
EITHER file's change alone cures the trio (the principals diverge); BOTH close the seam against any third file; the two fixtures' "unique caller subject" docstring clauses re-trued suite-scope. NOT the door module (AUTH_MODE/_keys re-bound per test and restored — not the poison, the run proves it); NOT the substrate (pinned ouncemcp — the replay its designed law, priced and kept).
