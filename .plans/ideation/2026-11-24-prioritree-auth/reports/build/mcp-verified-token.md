<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — build/mcp-verified-token

**Route:** prioritree-auth (executing) | **Events:** 12 | **Reports:** 6

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-25T01:14:32Z |
| 2 | report | jikko | 2026-11-25T01:18:38Z |
| 3 | dispatch | shinko | 2026-11-25T01:18:48Z |
| 4 | report | jikko | 2026-11-25T01:26:45Z |
| 5 | dispatch | shinko | 2026-11-25T01:27:03Z |
| 6 | dispatch | shinko | 2026-11-25T01:27:03Z |
| 7 | report | jikko | 2026-11-25T01:39:28Z |
| 8 | report | jikko | 2026-11-25T01:51:01Z |
| 9 | dispatch | shinko | 2026-11-25T01:51:25Z |
| 10 | report | jikko | 2026-11-25T01:52:31Z |
| 11 | dispatch | shinko | 2026-11-25T01:57:37Z |
| 12 | report | jikko | 2026-11-25T02:03:47Z |
## Reported by jikko — 2026-11-25T01:18:38Z

STEP 1 LANDED (R8 file-unit 1 of 5): src/prioritree/mcp_auth.py NEW, 251 lines — the spec §1 fence whole (reports/synthesize/mcpverifiedtokenspec.md).
Structure read back: module docstring (a-e the door whole; JWTVerifier/StaticTokenVerifier/InMemoryOAuthProvider priced-and-refused; the manifest absence named; the two transport laws); constants _MCP_AUDIENCE="mcp", _AUTH_OFF="off", _CLIENT_ID="prioritree-mcp"; TOOL_SCOPES the frozen MappingProxyType five-row proxy; _BOOT_LOG_CHANNEL="fastmcp.prioritree.mcp_auth"; THE BOOT — AUTH_MODE=resolve_auth_mode(os.environ.get("AUTH")), _keys=KeyStore(resolve_keys_home().absolute()), render_boot_marker on the host's pre-configured channel.
McpTokenVerifier(TokenVerifier).verify_token — verify(_keys, token, _MCP_AUDIENCE, None) whole; KeyVerifyError→None (the bearer 401's one channel); AccessToken(client_id the constant, scopes sorted, subject comparator_id, claims aud/comparator_id/comparator_class); _verifier; gate(PolicyRequest) — off→True, absent row→False, authenticated AND granted (fails closed, the opaque denial); compose_door_kwargs — off→{}, on→{"auth": _verifier, "policy": gate} (stdio_policy never rides).
THE FIVE ROWS VERBATIM: "runs.register": "register", "runs.next": "next", "votes.cast": "cast", "votes.census": "state", "runs.tally": "tally".
PATCH FINDINGS FIXED SAME-TURN (the ONLY deltas from the fence's bytes — ruff's own fixes, zero rulings, zero ignores): RUF022 (__all__ isort-style order: AUTH_MODE, TOOL_SCOPES, McpTokenVerifier, compose_door_kwargs, gate) + COM812 (the map literal's trailing comma).
INSTRUMENTS: ruff ALL zero findings; pyright strict 0 errors/0 warnings/0 informations (make lint + make typecheck green).
NOT DONE: steps 2-5 (mcp_server.py's construction+cast folds, tests/test_mcp_auth.py, tests/test_mcp_server_face.py growth, the floor-green) — later dispatches; nothing else touched.
## Reported by jikko — 2026-11-25T01:26:45Z

STEP 2 LANDED — src/prioritree/mcp_server.py per mcpverifiedtokenspec §2: imports grown (ouncemcp +PermissionDenied,ToolContext; `from prioritree.mcp_auth import compose_door_kwargs` before policy; votes +SupersedeRefusedError), construction grown `server = OunceServer(name="prioritree", **compose_door_kwargs())` (now :126, comment re-fenced), module docstring's door clause before "NO runner" (:20-27), cast folds (:533-576: `def cast(body: CastInput, ctx: ToolContext)`, the verified-stamps delegation, the SupersedeRefusedError->PermissionDenied catch) — docstrings byte-standing.
READ-BACKS — construction: `server = OunceServer(name="prioritree", **compose_door_kwargs())`; stamping: `identity = ctx.identity` / `if identity.authenticated:` / `comparator_id = str(identity.claims["comparator_id"])` / `comparator_class = str(identity.claims["comparator_class"])` else the body's claims; the fold's catch: `except SupersedeRefusedError as refusal:` / `raise PermissionDenied(_render_three_part(refusal.expected, refusal.found, refusal.next_action),) from refusal`.
ONE DEVIATION (the patch's own pyright finding, fixed same-turn): mcp_auth.py compose_door_kwargs' return `dict[str, object]` -> `dict[str, Any]` (+Any import) — object fits no OunceServer kwarg at the **-unpack (26 errors at the construction); the substrate's `**fastmcp_kwargs: Any` school (ouncemcp server.py:778); semantics identical, docstrings untouched.
INSTRUMENTS: ruff whole-tree green (zero findings, zero new rulings); pyright 0/0/0.
NOT DONE: the suite (the floor step's; known-red window per spec §5 step 2 — the armed door denies the scope-less tokens, and the two direct-call arcs face :301/:344 await step 4's _headless()); no behavioral probes (the seat never verifies its own work — the read-backs are disk quotes).
## Reported by jikko — 2026-11-25T01:39:28Z

STEP 4 of 5 (build/mcp-verified-token): tests/test_mcp_server_face.py grown per mcpverifiedtokenspec §3b — one file, nothing else touched.
THE FIXTURE SEAM LANDED: _GRANTED at :94 ("register", "next", "cast", "state", "tally" — manifest absent); _granted() at :127 — `make_token(subject=caller, scopes=list(_GRANTED), claims={"aud": "mcp", "comparator_id": caller, "comparator_class": comparator_class})`; _call at :97 grown `*, token: AccessToken | None = None` + `with as_caller(access_token=token or _granted(caller)):` (the granted-default docstring clause); _cast's return line carries `token=_granted(caller, comparator_class=comparator_class)` (the class knob shapes the token's claims — the twins' bodies byte-standing).
THE FOUR RE-DERIVED ARCS: (1) test_cast_resend_acknowledged — `again = _call(caller, "votes.cast", {**arguments, "comparator_id": "imposter"})` (the same principal, the transport guard bypassed by the args diff, the core's dedup hit on the VERIFIED id — VOTE-0001/count 1/acknowledged True stand); (2) test_cast_winner_refused_at_the_core + (3) test_cast_class_refused_at_the_core — `mcp_server.cast(body, _headless())` over the NEW helper at :110 (`ToolContext(tool="votes.cast", response_format="concise", result_budget=0)` — the anonymous identity, the body's claims stand); (4) test_cast_llm_class_lands — the inline body rides `token=_granted(caller, comparator_class="llm")` (the llm class LANDS). Each arc's docstring re-trued in the same edit.
THE STANDING ARCS: 34 collected, byte-standing — the caller fixture, every other arc's asserted bytes untouched; the module docstring's three re-truthings landed (the harness paragraph's granted-token clause naming the grown imports; the idempotency paragraph's re-send clause re-trued; the headless ToolContext named).
ONE PLACEMENT RULING (reported, never silent): AccessToken rides the TYPE_CHECKING block (:78) — annotation-only use; a top-level import would fire TC002 against the zero-findings bar (the spec's import-list item placed at the tree's own law); ouncemcp's ToolContext/make_token top-level (runtime uses at :119/:136).
THE FILE'S OWN SUITE (the patch's own finding per the dispatch; the floor decides): pytest tests/test_mcp_server_face.py → 34 passed in 1.36s — ALL GREEN under the armed door (the standing arcs' asserted values byte-held; the four re-derivations green; the count 34 stands, the growth re-derives never adds).
NOT DONE (honestly): the floor — step 5's read-back (336 collected, ruff/pyright at the same make) is not mine this dispatch; tests/test_mcp_auth.py (step 3's file) is absent on disk at this step's landing — a parallel dispatch, not touched by this step.
## Reported by jikko — 2026-11-25T01:51:01Z

STEP 3 LANDED — tests/test_mcp_auth.py (NEW, 631 lines): 24 arcs at the spec's names, 37 runtime items (21 singles + the marker's 3 + the granted's 5 + the denials' 8) — 37/37 green at `pytest tests/test_mcp_auth.py`; ruff zero findings, pyright 0/0 (the file's own suite + instruments per the school; the full floor is step 5's).
DEVIATIONS, each pinned at bytes: (1) arc 5 — the spec's "_verify(_grant(...)) is None" is inverted against its own name ("lands_live") and the service twin's 201; landed the LIVE form (access is not None, subject mapped — the stat ride seen).
(2) arc 18 — "the SCOPE-LESS subject-only token (as_caller(subject=...))" + "the cast ack" are jointly unachievable: a claims-less token at the cast door hits the spec's OWN §1 KeyError crash lane (the honest crash, never an ack); landed the scope-less CLAIMS-CARRYING token (_token(()) — the file's own helper) — all five asserted outcomes whole, the no-hide teaching intact.
(3) arc 17 — the raw NotFoundError the spec pinned (server.py:1670) never crosses the Ounce door: OunceMiddleware's every-exception envelope (execution/middleware.py:162-168) converts it to the opaque unknown-tool RESULT; landed the envelope form through server.call_tool ("No such tool", the name/scope/grant never disclosed — the teaching loss pinned stricter); the NotFoundError import removed.
(4) arc 12 — the present-count read through a SECOND container (a fresh container's first mint never repopulates .records, key_store.py:482's pre-existing-file reload); FBT001 answered with the spec's own "present"/"absent" words as the parametrize states.
(5) signatures — the arcs that take the door's effects without its value ride @pytest.mark.usefixtures("door") (ARG001 fires on unused test args; no ARG ruling exists to ride); the fence's import list grown where its own arcs demand it (asyncio, itertools.count, TextContent, render_boot_marker; AccessToken TYPE_CHECKING-only for TC002).
VERIFIED AT THE RUN: arc 16's wire-form `mcp_server.server.list_tools()` DOES propagate as_caller's token through the in-memory client — the spec's exact form green (the hide per caller); arc 10's stdio skip lands the CORE's "Not found:" (the door never consulted); arcs 19-23's stamps/supersedes oracles green.
NOT DONE: tests/test_mcp_server_face.py (step 4) + the floor-green make (step 5) — the standing face arcs remain in the spec's own known-red window under the armed door.
## Reported by jikko — 2026-11-25T01:52:31Z

STEP 5 — THE FLOOR (R11), the three fixed-argv acts, outcomes verbatim:
TEST ACT (the full suite): "3 failed, 333 passed in 32.89s" — 336 COLLECTED, the spec's estimate EXACT. The three failing arcs' names: tests/test_mcp_server_face.py::test_census_view (census after one vote => {'total': 0, 'items': {'a': 0, 'b': 0, 'c': 0}} != {'total': 1, 'items': {'a': 1, 'b': 1, 'c': 0}}); tests/test_mcp_server_face.py::test_tally_view_at_full_coverage (runs.tally => is_error, "Invalid input: expected: the coverage gate met: no zero-..."); tests/test_mcp_server_face.py::test_next_done_terminal (runs.next => is_error, "Not found: expected: a run file in the store home (live:...)").
The three ride TO THE FOLD as UNEXPECTED suite failures: each file green alone (face 34 passed at step 4; auth 37/37 at step 3), red only in the full suite's company — cross-file state, NOT fixed (outside the floor's own findings; the steps 1-4 fence holds).
LINT ACT (uv run ruff check src/ tests/): "All checks passed!" — zero findings.
TYPECHECK ACT (uv run pyright): "0 errors, 0 warnings, 0 informations".
NOT DONE: nothing fixed at the floor — the three red arcs untouched, the fold owns them; no re-run post-fold.
## Reported by jikko — 2026-11-25T02:03:47Z

R11 — jikko, step 5b: the fold's landing + the floor re-run (build/mcp-verified-token, prioritree-auth).
THE FIX (togo's R6 fence, mcpverifiedtokenspec.md — the mint sites verbatim): tests/test_mcp_server_face.py:198 `return f"caller-{next(_CALLERS)}"` -> `return f"face-{next(_CALLERS)}"`;
:505 `second = _call(f"caller-{next(_CALLERS)}", "runs.register", arguments)` -> the same inline mint `f"face-{next(_CALLERS)}"`;
tests/test_mcp_auth.py — the nine mints at :349/:354/:371/:398/:443/:473/:543/:564/:591: f"caller-{next(_CALLERS)}" -> f"door-{next(_CALLERS)}";
the two "unique caller subject" docstring clauses re-trued suite-scope (BOTH in the face file — the module docstring :50-53 + the caller fixture :185-187; the auth file carries no such clause, grep-verified); the asserted census/tally/ack bytes byte-standing.
THE FLOOR (the three acts, outcomes verbatim): the test act (full suite) -> "336 passed in 33.48s" (the fold's 336 exact; the three cross-file reds gone);
the lint act -> "uv run ruff check src/ tests/" / "All checks passed!" (zero findings);
the typecheck act -> "uv run pyright" / "0 errors, 0 warnings, 0 informations" (0/0/0).
DEVIATIONS, named: two strict-patch refusals cured same-turn (a context transcription slip at auth :368-369; a dropped context line at :562 — both re-read, regenerated, applied); no other bytes touched.
