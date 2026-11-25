<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — validate/mcp-verified-token

**Route:** prioritree-auth (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-25T02:04:10Z |
| 2 | report | kensho | 2026-11-25T02:06:57Z |
## Reported by kensho — 2026-11-25T02:06:57Z

# THE MCP-VERIFIED-TOKEN INDEPENDENT VERIFICATION — kensho (validate/mcp-verified-token, 2026-11-24)

THE VERDICT: GREEN — the zero-errors/zero-warnings bar met at every instrument; jikko's step-5b count 336 confirmed by my own run; the spec's clauses each found at the landed bytes; the deviations each honest against the substrate; the fold's cross-file cure verified live.

## 1. THE INSTRUMENTS RE-RUN (kensho's own runs — never the build's word)

- THE FULL SUITE (the tree's own way, the fixed-argv test act): **336 passed in 33.61s** — zero failed, zero warnings. JIKKO'S STEP-5B COUNT CONFIRMED EXACT (336; the fold's three cross-file reds gone — the face-/door- stems' cure verified live in my own run). The floor arithmetic reconciles: 299 standing + the auth file's 37 new items = 336; the face file's 34 stands (the growth re-derives, never adds).
- THE LINT ACT (uv run ruff check src/ tests/): "All checks passed!" — zero findings under select=ALL.
- THE TYPECHECK ACT (uv run pyright): "0 errors, 0 warnings, 0 informations" — strict + the standing reportUn* extras, 0/0/0.

## 2. THE SPEC'S CLAUSES — THE CHECK-LIST (the landed source read against the fences)

### 2a. src/prioritree/mcp_auth.py (251 lines, NEW) — the door module whole
- THE ADAPTER: McpTokenVerifier(TokenVerifier).verify_token at :158-188 — verify(_keys, token, _MCP_AUDIENCE, None) WHOLE re-carried (:175), KeyVerifyError -> None the ONE channel (:176-177), the AccessToken mapping whole (client_id _CLIENT_ID="prioritree-mcp" the named constant :76, scopes sorted :181, subject record.comparator_id :182, claims aud/comparator_id/comparator_class :183-187).
- THE GRANT MAP: TOOL_SCOPES the frozen MappingProxyType five-row proxy (:86-94), the rows verbatim: runs.register->register, runs.next->next, votes.cast->cast, votes.census->state, runs.tally->tally — five of the six SCOPE_TOKENS, no new vocabulary token born.
- THE POLICY: gate(PolicyRequest) at :196-226 — the per-call AUTH_MODE read (off -> True :221-222), the map's row (absent -> False :223-225, DEFAULT-DENY live), identity.authenticated AND token in identity.scopes (:226, fails closed).
- compose_door_kwargs at :229-251: off -> {} (the plain construction, NEITHER kwarg); on -> {"auth": _verifier, "policy": gate}; stdio_policy NEVER rides.
- THE BOOT: AUTH_MODE = resolve_auth_mode(os.environ.get("AUTH")) (:121 — the typo'd value refuses loudly), _keys = KeyStore(resolve_keys_home().absolute()) (:122 — the same home the service door reads), the marker on the host's PRE-CONFIGURED channel (:123-125 over _BOOT_LOG_CHANNEL="fastmcp.prioritree.mcp_auth" :110 — render_boot_marker reused whole, never re-authored).
- The RUF022/COM812 same-turn fixes landed (:64 the __all__ order, :93 the map literal's trailing comma).

### 2b. src/prioritree/mcp_server.py — the construction + the cast folds
- The imports grown exactly per the fence: :36 +PermissionDenied, ToolContext; :39 `from prioritree.mcp_auth import compose_door_kwargs` before policy (the import FIRES the door's boot BEFORE the construction); :48 +SupersedeRefusedError.
- THE CONSTRUCTION at :126: `server = OunceServer(name="prioritree", **compose_door_kwargs())` — the auth= composition riding **fastmcp_kwargs, the plain form byte-identical at off.
- The module docstring's door clause at :19-25 before "NO runner" — the landing itself the amendment.
- THE CAST TOOL at :533-577: the signature `def cast(body: CastInput, ctx: ToolContext)` (the annotation EXACTLY ToolContext — the substrate's registration law); THE STAMPING DELEGATION :554-560 (identity = ctx.identity; if authenticated -> the claims read DIRECT, the KeyError the honest crash; else the body's claims — the anonymous fallback); THE SUPERSEDES FOLD :573-576 (SupersedeRefusedError -> PermissionDenied(_render_three_part(refusal.expected, refusal.found, refusal.next_action)) at the module's ONE render point). The docstring byte-standing.

### 2c. tests/test_mcp_auth.py (632 lines, NEW) — 24 arcs / 37 items, each at the spec's names
- THE NONE FAMILY: arcs 2/3/4 (the wrong key :194, the absent token :200, the service-audience key :206 -> the SAME None, the oracle never fed); arc 1 the AccessToken whole field-for-field :182-191; arc 5 the mid-flight mint LIVE :212-218 (the stat ride); arc 6 the cross-tier replay's REVERSE leg :221-230 (the landed 401 bytes, "mcp" never named).
- THE CROSS-TIER REPLAY BOTH DIRECTIONS: arc 4 (forward: F5 fires at the mcp door) + arc 6 (reverse: the landed family's bytes at the service door) — dead both ways.
- THE HIDE + THE OPAQUE GUESSED-NAME: arc 16 :343-358 (the comparator's list carries next+cast not register; the auditor's census+tally not cast — the hide PER CALLER); arc 17 :362-382 (the guessed name -> the OPAQUE refusal, the name/scope/grant never disclosed — the teaching loss PINNED).
- THE OFF NO-HIDE: arc 18 :386-437 (the re-bound off + the scope-less token -> all five REACHED in-process — the degrade never a lockout).
- THE STDIO TRUST: arc 10 :258-266 (set_transport("stdio") -> the anonymous call reaches the CORE's "Not found:", the door never consulted — the skip EFFECT asserted); arc 11 :269-275 (the spawn source-scan: opencode.json's bare module command, NO env, NO auth — the spawn IS the credential).
- THE STAMPING ARCS: 19 :441-467 (the llm-class claims stamp over the body's human claim — the halt names "missing human"); 20 :471-508 (the body's changed id unread — the correction lands on the VERIFIED id); 21 :512-537 (off -> the body's class stamps — the degrade's price); 22 :541-585 (the supersedes author-refusal as the PermissionDenied VALUE, found eliding the author — "author-a" never named); 23 :589-626 (the own-author pass under the verified id).
- THE FORK-GUARD: arc 24 :629-632 (the map's keys the five registered tool names; the tokens within the SCOPE_TOKENS vocabulary, cited as literals).
- The counts verified at the file: 24 functions; 21 singles + the marker's 3 (:278-293) + the granted's 5 (:304-314) + the denials' 8 (:317-339) = 37 runtime items.

### 2d. tests/test_mcp_server_face.py — the granted fixture + the four re-derived arcs + the 34 standing
- _GRANTED at :96 (the five tokens, manifest absent); _granted at :129-142 (the door-shaped claims); _call grown the token knob (:99-109, the granted default); _cast's return line carries the class-shaped token (:174); _headless at :112-121 (the direct-call tier's anonymous ToolContext).
- THE FOUR RE-DERIVED ARCS confirmed at bytes: test_cast_resend_acknowledged (:469-492 — the args-diff bypass, the core's dedup on the VERIFIED id, the original's vote_id/count, acknowledged=True); test_cast_winner_refused_at_the_core + test_cast_class_refused_at_the_core (:336-355/:379-398 — mcp_server.cast(body, _headless())); test_cast_llm_class_lands (:581-599 — the llm-claims token rides, the class LANDS).
- THE 34 STANDING: 31 singles + the parse-argv's 3 (:713-769) = 34 collected — the count STANDS; the asserted values byte-held, verified arc-by-arc.
- The docstring re-truthings landed (the harness paragraph's granted-token clause :8-13, the idempotency paragraph's re-send clause :33-38, the face-{N} suite-scope clause :50-54).
- THE FOLD'S STEMS: the caller fixture :201 f"face-{next(_CALLERS)}"; :508 the inline mint; the auth file's nine door- mints (:349/:354/:371/:398/:443/:473/:543/:564/:591) — the cross-file idempotency replay cured; my own 336-pass run the live proof (the trio's reds gone).

## 3. THE LAWS

- THE LLM-CLASS CONSTRAINT at the built surface: the llm's key the SAME mint ceremony — key_store.py:53 AUDIENCES = {"service", "mcp"} (the mint's --audience mcp legal, cli.py:216); cli.py:95 FLAG_CLASS="--class" (human|llm, key_store.py:466's own teaching); the vote scope granted (the comparator's row carries "cast" — the ROLE_SCOPES literals at the auth file :75; the mint's --scopes csv); the stdio trust preserved (compose NEVER passes stdio_policy — arc 9; the bare spawn — arc 11; NO human gate anywhere at either transport). HELD.
- THE THREEPART at the refusals that can carry it: the supersedes PermissionDenied's three-part body (the ONE render point's fields asserted at arc 22 — the expected/found/next_action labels, found eliding the author); the bearer 401's grammar residual named honestly (the module docstring :37-40 — the typed ThreePart NEVER crosses the mcp wire, the transport's 401 the only 401, the scope denial a HIDE never a taught 403). NAMED, never silent.
- THE CONFIGURABILITY at every knob: AUTH (Makefile:7 `AUTH ?= on` the standing knob, :83 the carrier, mcp_auth.py:121 the reader — the same resolve_auth_mode the service door reads); PRIORITYTREE_KEYS_HOME (key_store.py:48 the env override, resolve_keys_home :145 — the door's :122 reads the same absolute home); the substrate's own (the host's log_enabled/log_level governing the marker's channel — named at the constant's comment :106-107). NO new knob minted un-shaped.
- THE ZERO-IGNORE STRICTNESS: pyproject.toml read whole — every per-file-ignores entry a NAMED RULING with its provenance; ZERO new entries for this unit (the spec's "NONE expected" holds — no mcp_auth.py entry, no test_mcp_auth.py entry; the mcp_server.py D205 + the face file's PLR0913/PLR0917 the STANDING rulings re-carried, unchanged); ruff ALL green + pyright strict-with-extras 0/0/0 with ZERO in-code ignores at the new surfaces.

## 4. THE DEVIATIONS — each verified honest against the landed substrate

1. THE dict[str, Any] WIDENING (jikko step 2): confirmed at mcp_auth.py:229 (+ Any at :52) — the spec fenced dict[str, object]; pyright refused the **-unpack (26 errors — object fits no OunceServer kwarg); the substrate's own **fastmcp_kwargs: Any school; semantics identical. HONEST.
2. THE ENVELOPE-FORM GUESSED-NAME ARC (jikko step 3): confirmed at :362-382 — the spec's raw NotFoundError (server.py:1670) never crosses the Ounce door (OunceMiddleware's every-exception envelope); the landed form asserts the opaque unknown-tool RESULT ("No such tool", the name never confirmed, the scope never disclosed) — the teaching loss pinned STRICTER than the fence; the NotFoundError import removed. HONEST.
3. THE IS-NONE INVERSION (arc 5): confirmed at :212-218 — the spec's fence inverted against its own name ("lands_live"); the landed LIVE form (access is not None, subject mapped) — the stat ride's truth asserted. HONEST.
4. THE SCOPE-LESS CLAIMS-CARRYING TOKEN (arc 18): confirmed at :386-437 — the spec's claims-less form + the cast ack jointly unachievable (the §1 KeyError crash lane the honest crash); the landed scope-less CLAIMS-CARRYING token asserts all five outcomes, the no-hide teaching intact. HONEST.
5. THE COUNT VIA THE SECOND CONTAINER (arc 12): confirmed at :288-293 — the fresh container's first mint never repopulates .records (key_store.py:482's pre-existing-file reload); the present/absent parametrize states. HONEST.
6. THE USEFIXTURES FORM (jikko step 3): confirmed — the sixteen door-effect arcs ride @pytest.mark.usefixtures("door") (ARG001 never fires on an unused test arg; no ARG ruling exists to ride). HONEST.
7. THE STEP-5B PATCH REFUSALS (two, cured same-turn): build-process honesty — the landed bytes green in my own run; nothing owed.

## THE VERDICT

G-MCP-VERIFIED-TOKEN's build leg VERIFIED GREEN: the instruments my own (336/336 passed, ruff clean, pyright 0/0/0 — the zero-errors AND zero-warnings bar met); the spec's clauses each found at the landed bytes (the door whole, the construction, the cast folds, the 24+37 arcs, the face's granted fixture + the four re-derivations + the 34 standing); the deviations each honest (the Any widening, the envelope form, the four test-side deviations, the fold's stems); the laws held (the llm-class constraint, the ThreePart named, the configurability at every knob, zero new rulings). The door armed at --serve, the ride preserved at stdio, the cross-tier replay dead both directions — the build's word confirmed by the runtime's own.
