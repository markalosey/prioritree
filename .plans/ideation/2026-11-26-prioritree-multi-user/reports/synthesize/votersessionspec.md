<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/votersessionspec

**Route:** prioritree-multi-user (executing) | **Events:** 8 | **Reports:** 3

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-26T18:28:38Z |
| 2 | report | togo | 2026-11-26T18:46:55Z |
| 3 | result | shinko | 2026-11-26T18:47:41Z |
| 4 | gate | shinko | 2026-11-26T18:50:52Z |
| 5 | dispatch | shinko | 2026-11-26T19:37:44Z |
| 6 | report | togo | 2026-11-26T19:39:09Z |
| 7 | dispatch | shinko | 2026-11-26T20:50:46Z |
| 8 | report | togo | 2026-11-26T20:51:56Z |
## Reported by togo — 2026-11-26T18:46:55Z

# THE VOTER-SESSION EXACT-TASK SPEC — the unit's bytes whole (togo, packet synthesize/votersessionspec, route prioritree-multi-user, 2026-11-26)

The exact-task spec for the unit **build/voter-session**, closing G-VOTERSESSIONSPEC-BRIEF at the collaborator's approval: every edit fenced at its exact bytes, every byte the R5/ASCII/ruff-ALL discipline at authoring time (the three acts: ruff zero findings, pyright 0/0, the suite green). The build dispatches cite THIS spec; this spec cites the approved unit brief (reports/synthesize/voter-session.md — G-VOTER-SESSION-BRIEF green) and the design brief (reports/synthesize/multi-user-design.md — G-MULTI-USER-DESIGN green). READ-ONLY held; this report the packet's only write. Nothing decided here that is the collaborator's to decide.

## 0. THE GROUND (read whole this pass; the pins re-verified at the tree's bytes)

The approved unit brief (§1 the eight landings; §2 the mechanisms ruled; §3 the test shape ~26; §5 the eight spec opens; R8's seven file-dispatches — the tool-carried count at 7); the design brief (§1 the five shape-compositions; §2 the five resolutions — the seam A, the mount B, the CSRF C, the naming D: the mint "remember" from the act-statement "Remember the voter across every page load…", the correction E; §3 the honest statement; §4 the build set). The cycle's record: suisen's recommendation, hyoka's adversarial (the nine cures), moho's walks (findings 2/3/6/7/8; the record re-counted at 241/312), keisan's ledgers (the rank; the ±2-B unpadding residual), shindan's residual maps, tansa's census (12 identity-asking surfaces, 0 cookie surfaces), rikai's mechanism maps (the engine's installed bytes: sessions.py:16-40 the construction — secret_key REQUIRED, session_cookie/max_age/same_site the knobs, HttpOnly HARDCODED at :34; :55-59 the BadSignature silence; :80-89 the deletion cookie; requests.py:170-177 the mount-order assert). The tree's own bytes re-read this pass: web.py:114-170 (the CSRF region — the env-or-boot-mint secret at :119-120, _mint_csrf at :144-146, the guard at :149-170, the refusal copy at :166-170), :231-233 (the child construction), :239-245 (the in-process client school), :473 (the register mint, path-bound), :546 + :698 + :935 (the three vote mints), :842-885 (the register POST), :946 (the guard before _service), :965-973 (the vote POST's read), :177-198 (the lanes' legal set); service.py:564-565 (the door conditional — F8's stamping), :200-218 (the parent's construction — NO middleware mount), :234-263 (the require_key factory); sitting.html:6-7 (the ask, the "THIS PAGE" copy), pair.html:3-7 (the hx-include + the hidden fields), landing.html:12 (the operator input, no value); pyproject.toml:9 (the six dependencies), :45-220 (the per-file rulings' precedent form); test_web_face.py:82-93 (the injection fixture), :96-111 (_scrape_csrf), :461-521 (the CSRF arcs), :590 (the auth-off degrade); test_service_auth.py:366-395 (the three pinned seam arcs). THE MINT CLEAN re-verified: zero "remember" hits over src/prioritree.

## 1. THE DEPENDENCY DOOR (pyproject.toml) — dispatch 1 of 7

**THE WHEEL'S FORM (the exact before/after at :9):**

before:
```toml
dependencies = ["fastapi", "httpx2", "jinja2", "ouncemcp", "python-multipart", "uvicorn[standard]"]
```
after (the tree's precedent form: the bare unpinned name — the version pin lives in the lock, never the manifest; the list's alphabetical order held):
```toml
dependencies = ["fastapi", "httpx2", "itsdangerous", "jinja2", "ouncemcp", "python-multipart", "uvicorn[standard]"]
```
6 → 7 direct dependencies (+16.7%); ONE pure-Python wheel, no transitive (itsdangerous declares none — the lock gains exactly one package entry); $0 money; the precedent class starlette itself already is.

**THE LOCK — the act's own:** `uv lock` runs INSIDE the dependency act, never hand-edited (the cycle-generated lock's own law); the dispatch's read-back: the lock's itsdangerous entry present (uv.lock: the +1 package block) + the import live at the venv (§2's import exercises it).

**THE LOUD-AT-IMPORT FORM (the ModuleNotFoundError's face named):** web.py's top gains the engine import — `from starlette.middleware.sessions import SessionMiddleware` — riding the starlette surface beside the existing `from starlette.exceptions import HTTPException as StarletteHTTPException` (:67's neighborhood), NEVER wrapped in try/except (no silent degradation is legal). If the lock is skipped the face is exactly: `ModuleNotFoundError: No module named 'itsdangerous'` — raised at web.py's import, the whole web tier unimportable, LOUD, immediate, unmissable (the contrast that killed [ii]'s silent break; sessions.py:8 `import itsdangerous` is starlette's own line — the tree's door is the lock, never the engine).

## 2. THE REMEMBER REGION WHOLE (web.py) — dispatch 2 of 7

The region's law: every new Python member speaks the one word "remember" (the naming mint, resolution D); "the session" stays the record's shared shorthand, never a symbol; session.py the library's U5 chain — untouched.

### 2a. THE SECRET'S KNOB + THE BOOT-TIME STRENGTH CHECK (both knobs, the shared home)

The env-or-boot-mint school at :119-120, extended to a shared home — the check's twin carried at BOTH knobs (the design's cure-5 wording: a weak secret weakens every artifact, the CSRF token and the session both). The exact after (replacing :114-121's region; the standing comment re-authored to carry both knobs):

```python
# The signing secrets' env-or-boot-mint school (the CSRF region's own form,
# extended): each knob reads its env ONCE at import — unset => a boot-minted
# 256-bit secret (the restart-invalidation price carried honestly: a boot's
# outstanding tokens and sessions die, the re-render and the re-ask cure); an
# env secret UNDER THE FLOOR refuses AT IMPORT in the ThreePart grammar (the
# zero-findings bar applied to the knob — a weak secret weakens every
# artifact it signs, the CSRF token and the remembered session both).
_SECRET_FLOOR_BYTES: Final[int] = 32  # 256 bits — the boot-mint school's own length
_CSRF_SECRET_ENV: Final[str] = "PRIORITYREE_WEB_CSRF_SECRET"
_REMEMBER_SECRET_ENV: Final[str] = "PRIORITYREE_WEB_REMEMBER_SECRET"


def _boot_secret(env_name: str) -> bytes:
    """Read the env secret or boot-mint the 256-bit fallback — an under-floor env secret refused at import.

    Purpose: the shared home of both knobs' strength check (the CSRF secret
    + the remember secret — the same floor, the same grammar); the env value
    wins when present and at the floor; unset => the boot-mint (256 bits);
    an under-floor env value REFUSES AT IMPORT (the ThreePart bytes in the
    raise — the loud form, never a silent weak boot).
    Refuses when: the env set and shorter than the floor (RuntimeError, the
    ThreePart message).
    Re-run: deterministic given the environment.
    Touches: nothing — the environment read alone.
    Provenance: the design §1f/§2c (the twin at both knobs, hyoka's cure 5),
    the unit brief §2c, G-VOTERSESSIONSPEC-BRIEF.
    """
    given = os.environ.get(env_name, "")
    if given and len(given.encode()) < _SECRET_FLOOR_BYTES:
        raise RuntimeError(
            f"expected: the {env_name} env secret {_SECRET_FLOOR_BYTES} bytes (256 bits) or longer, or unset for the boot-mint; "
            f"found: {len(given.encode())} bytes; "
            f"next_action: set {env_name} to a 256-bit secret (python -c \"import secrets; print(secrets.token_urlsafe(32))\") or unset it"
        )
    return given.encode() or secrets.token_urlsafe(32).encode()


_csrf_secret: Final[bytes] = _boot_secret(_CSRF_SECRET_ENV)
_remember_secret: Final[bytes] = _boot_secret(_REMEMBER_SECRET_ENV)
```

**THE NO-BREAK NOTE:** the boot-mint path (env unset) is byte-equivalent to the standing line for both knobs — the CI's suite green with NO session secret IS the boot-mint form's test law (§5); the under-floor refusal fires only when an operator sets a weak env value, at import, before any request.

### 2b. THE SESSION'S KEYS + THE READ/WRITE HELPERS (the one-word family)

```python
# The remembered session's payload keys (content-in-configuration): the
# carried name + the CSRF epoch — the two values the cookie rides; the epoch
# minted ONCE at identification, never re-minted at renders (the
# concurrent-tab cure by construction: no per-render session write, two tabs
# hold the same epoch, the same token, both POSTs pass).
_SESSION_NAME: Final[str] = "name"
_SESSION_EPOCH: Final[str] = "epoch"
_REMEMBER_COOKIE: Final[str] = "remember"
_REMEMBER_MAX_AGE: Final[int] = 14 * 24 * 60 * 60  # 14 days — keisan's pricing: the 780-s card covered 1550x


def _remembered(request: Request) -> str:
    """Read the remembered name — the session's carried identity, "" when the browser is unidentified.

    Purpose: the ONE read helper every render context and the vote controller
    ride (the sitting, the judge, the pair fragment, the landing's pre-fill,
    the vote's cast read); the conditional ask's own branch key (a non-empty
    return renders the identity line, never the ask).
    Refuses when: never — a pure read ("" a VALUE, the anonymous state).
    Re-run: deterministic given the session state.
    Touches: the session read alone.
    Provenance: the unit brief §1c/§2a, G-VOTERSESSIONSPEC-BRIEF.
    """
    return str(request.session.get(_SESSION_NAME, ""))


def _remember(request: Request, name: str) -> None:
    """Identify the browser ONCE — the name written, the epoch minted; the session's ONE write act.

    Purpose: the identification's single write home (the first vote's
    identifying act and the correction verb's re-identification ride the same
    act — the epoch minted at every identification, ROTATED at every
    re-identification: the old tabs' tokens die at the next guard, the
    refusal's copy teaches the reload); NO per-render session write ever
    (the concurrent-tab cure).
    Refuses when: never — the write IS the act (the caller gates the empty name).
    Re-run: deterministic in form (the epoch random by design — the 256-bit school).
    Touches: the session alone (the browser's cookie via the engine's write intercept).
    Provenance: the unit brief §1d/§2a/§2b, hyoka's cure 8, G-VOTERSESSIONSPEC-BRIEF.
    """
    request.session[_SESSION_NAME] = name
    request.session[_SESSION_EPOCH] = secrets.token_urlsafe(32)
```

### 2c. THE MOUNT (the child's construction — the exact before/after) + THE ASSERT-GUARD

before (:231-233):
```python
web_app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
web_app.mount("/static", StaticFiles(directory=resolve(_STATIC_HOME, _STATIC_TAIL), check_dir=False), name="static")
templates = Jinja2Templates(directory=resolve(_TEMPLATES_HOME, _TEMPLATES_TAIL))
```
after (the mount line + the guard; the static mount and the templates line byte-standing after it):
```python
web_app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)
# THE REMEMBER SEAM'S MOUNT (the design §1f/§2B — THE CHILD): the session
# rides the web lanes ALONE (the service's six JSON routes session-free, the
# llm/stdio/tools lanes never see a session — the humans'-lane constraint
# MECHANICAL at the bytes); the cookie minted "remember" (the naming law's
# wire artifact), max_age the 14-day default (the sitting's floor cleared
# WHOLE — the 780-s card covered 1550x), same_site=lax (the shareable URL's
# top-level entry preserved — Strict refused), HttpOnly HARDCODED at the
# engine (sessions.py:34 — never a knob).
web_app.add_middleware(
    SessionMiddleware,
    secret_key=_remember_secret,
    session_cookie=_REMEMBER_COOKIE,
    max_age=_REMEMBER_MAX_AGE,
    same_site="lax",
)
# THE ASSERT-GUARD (the parent-service silent bypass refused): Starlette's
# own request.session read asserts the mount (requests.py:170-177 —
# "SessionMiddleware must be installed to access request.session"); the
# CHILD alone carries it, so a future service-tier controller touching the
# session REFUSES LOUDLY and this construction check refuses the same drift
# at import — a web.py edit that drops the mount never serves silently.
if not any(middleware.cls is SessionMiddleware for middleware in web_app.user_middleware):
    raise RuntimeError(
        "expected: SessionMiddleware mounted on the child web app (the remember seam); "
        "found: no SessionMiddleware in the child's middleware stack; "
        "next_action: restore the web_app.add_middleware(SessionMiddleware, ...) line — the remember region's own law",
    )
web_app.mount("/static", StaticFiles(directory=resolve(_STATIC_HOME, _STATIC_TAIL), check_dir=False), name="static")
templates = Jinja2Templates(directory=resolve(_TEMPLATES_HOME, _TEMPLATES_TAIL))
```
service.py's construction (:200-218) and its tail mount are NEVER touched (the parent's two bypass routes refused at the design — the silently-present session, the frozen wire's cookie semantics).

### 2d. THE EPOCH-BOUND CSRF (the mint/validate composition — the exact before/after)

**THE PAYLOAD'S ONE COMPOSITION HOME** (never two spellings — the mints and the guard all ride it):
```python
def _mint_bound(path: str, request: Request) -> str:
    """Mint the epoch-bound token over a path — pre-identification the path alone.

    Purpose: the ONE composition home of the CSRF payload's epoch binding
    (the sitting/judge/pair renders' mints and the guard's recompute the
    same form): the path, then "|", then the SESSION's epoch when one rides —
    never a client-echoed value (the fixation discipline held); the epoch
    absent (the anonymous browser) => the path alone (the identifying vote's
    own guard passes — its page minted path-bound, the guard recomputes
    path-bound). The register lane NEVER composes here (§2e — the binding
    never presumed).
    Refuses when: never — a pure composition.
    Re-run: deterministic given the session state.
    Touches: the session read alone (never a write — no per-render mint).
    Provenance: the unit brief §1d/§2b, hyoka's 1b (the concurrent-tab cure),
    G-VOTERSESSIONSPEC-BRIEF.
    """
    epoch = str(request.session.get(_SESSION_EPOCH, ""))
    return _mint_csrf(f"{path}|{epoch}" if epoch else path)
```

**THE GUARD'S AFTER (:149-170)** — the payload gains the epoch; the refusal's copy branches by the session's own state (the expiry's teaching, never the schema's words):
```python
async def _csrf_guard(request: Request) -> None:
    """Validate the form's CSRF token BEFORE _service — the per-route dependency (F2's cure, the epoch-bound form).

    Purpose: recompute the expected token over the request's own path + the
    SESSION's epoch (the server-side recompute, never a client-echoed value)
    + hmac.compare_digest (the timing discipline, key_verify's ONE-compare
    school); the drive-by's POST carries an absent-or-mismatched token => the
    refusal fires BEFORE _service (the write never lands). THE EXPIRY'S
    TEACHING branches on the session's own state: an EMPTY session (the cookie
    died at max_age or the secret rotated — the sitting chain's fragment trap
    never re-renders the ask) teaches the LAPSE in the human's words ("your
    identification lapsed — reload, the page re-asks your name"); a LIVE
    session (the stale tab at a rotated epoch) teaches the standing reload
    cure. Starlette caches request.form() — the route's own parse reads the
    same cached body, no double-read.
    Refuses when: the token absent or mismatched (CsrfRefusedError).
    Provenance: the unit brief §1d/§2b, moho's walk §1d (the fragment trap's
    only channel), hyoka's 1b/8, G-VOTERSESSIONSPEC-BRIEF.
    """
    form = await request.form()
    presented = str(form.get(_CSRF_FIELD, ""))
    expected = _mint_bound(request.url.path, request)
    if not hmac.compare_digest(presented, expected):
        if str(request.session.get(_SESSION_EPOCH, "")):
            _next_action = "reload the page and re-send — the re-render mints a fresh token"
        else:
            _next_action = "your identification lapsed — reload, the page re-asks your name"
        raise CsrfRefusedError(
            expected=f"the form's {_CSRF_FIELD} field (minted into the served page)",
            found="absent-or-mismatched",
            next_action=_next_action,
        )
```
(The empty-session branch keeps the elision discipline — found stays "absent-or-mismatched"; the copy aims at the human's cure, never the diagnosis.)

**THE MINT SITES' AFTER:**
- :473 the landing — BYTE-STANDING: `{"csrf_token": _mint_csrf(_REGISTER), "remembered_name": _remembered(request)}` (the register lane ALWAYS path-bound — pre-identification by flow, and NEVER epoch-bound even for a sessioned browser: the binding never presumed; the pre-fill's read added).
- :546 the sitting + :698 the judge — `"csrf_token": _mint_bound(f"/ui/runs/{stem}/vote", request), "remembered_name": _remembered(request), "unremember_token": _mint_bound(f"/ui/runs/{stem}/unremember", request),` (the visible identity + the correction affordance's token at both lanes — the one template seam).
- :935 the pair fragment — `"csrf_token": _mint_bound(f"/ui/runs/{stem}/vote", request), "remembered_name": _remembered(request),` (the fragment carries the conditional ask's twin — no identity line, no correction form: those live outside #pair-region).

### 2e. THE VOTE CONTROLLER — the cast read's before/after (:965-973)

before:
```python
    form = await request.form()
    presentation = str(form.get("presentation_order", PRESENTATION_CANONICAL))
    payload = {
        "pair": [str(form.get("item_a", "")), str(form.get("item_b", ""))],
        "winner": str(form.get("winner", "")),
        "comparator_id": str(form.get("comparator_id", "")),
```
after (the session first; the body's field the identifying act; the taught refusal before _service):
```python
    form = await request.form()
    name = _remembered(request)
    if not name:
        name = str(form.get("comparator_id", "")).strip()
        if not name:
            return _refuse_fragment(
                request,
                {
                    "expected": "your remembered name, or the ask's answer at the first judgment",
                    "found": "no remembered entry and no name in the request",
                    "next_action": "your identification lapsed — reload the page, it re-asks your name",
                },
            )
        _remember(request, name)
    presentation = str(form.get("presentation_order", PRESENTATION_CANONICAL))
    payload = {
        "pair": [str(form.get("item_a", "")), str(form.get("item_b", ""))],
        "winner": str(form.get("winner", "")),
        "comparator_id": name,
```
(the class line below — `"comparator_class": str(form.get("comparator_class", "human"))` — BYTE-STANDING; the write arms the engine's Set-Cookie on the ack response; the 422-schema-speak death moho walked is dead — the fragment teaches the reload and the write never lands.)

**THE STANDING ARCS' NOTE (the echo arc's honest form):** the identifying POST mints the epoch, so the page's path-bound token is stale AFTER the identification (the design's own stale-form residual); the real browser's next form is the chain's fresh fragment (epoch-bound); `test_vote_echo_already_recorded`'s second POST therefore scrapes the pair fragment's token (the browser's own token source) — the arc's name and assertions byte-standing, its second token composed per the session's law. The double-click's stale-token window: one refusal teaching the reload; the door's echo ack confirms the vote landed (the reload's own cure).

### 2f. THE CORRECTION ROUTE (the un-remember verb — the deletion cookie wired)

The route constant (beside the lane constants at :82-92) + the legal set's growth at :177-198 (`_WEB_LANES` gains `f"POST {_UNREMEMBER}"` — the child's refusal handler teaches the whole face honestly):
```python
_UNREMEMBER: Final[str] = "/ui/runs/{stem}/unremember"
```
The route (after the state_strip controller, the fragment tier's own grammar):
```python
@web_app.post(_UNREMEMBER, dependencies=[Depends(_csrf_guard)])
async def unremember(request: Request, stem: str) -> Response:
    """Un-remember this browser — the engine's deletion cookie wired, the sitting re-rendered.

    Purpose: the correction affordance's route (one affordance, two verbs:
    "not you? change your name" — the redirect's re-ask IS the
    re-identification, the epoch minting at the next identifying vote — and
    un-remember, the anonymous state); request.session.clear() arms the
    ENGINE'S OWN deletion cookie (sessions.py:80-89: the emptied-intercept
    emits remember=null; expires=Thu, 01 Jan 1970 — the identity-erase verb
    EXISTS at the engine, absent at the product until this route); the
    HX-Redirect response header navigates to the sitting page (the pair
    fragment's done-edge precedent, :924's form — the fresh render shows the
    ask, the conditional's own return). THE VERB'S HONESTY at [i]'s bound: it
    clears THIS browser's cookie, never a server kill — a stolen cookie
    elsewhere rides to max_age or the secret's rotation.
    Refuses when: never by this hand — the clear is the act (an empty session
    clears to the same empty state: no deletion cookie, nothing to erase).
    Re-run: deterministic given the session state.
    Touches: the session alone (the browser's cookie).
    Provenance: the unit brief §1f/§2, moho's findings 3+6 (the DIY
    cookie-edit's silent death), G-VOTERSESSIONSPEC-BRIEF.
    """
    request.session.clear()
    return Response(status_code=_OK, headers={"HX-Redirect": f"/runs/{stem}"})
```

### 2g. THE TWO-ROLE SEAM — service.py:564's web-lane branch (the ONLY service edit)

**THE MODULE-LEVEL MARKER** (service.py's constants region — the process's own web key, the same env web.py:239-245 reads; `import hashlib` joins the stdlib imports — the sha256 the key_verify school):
```python
# THE TWO-ROLE SEAM'S WEB-LANE MARKER (the voter-session spec §2g): the
# process's own web key — the same PRIORITYREE_WEB_KEY the web tier's
# in-process client carries (one process, one env, both tiers) — digested
# once at import; under a verified digest the WEB LANE'S callers alone may
# carry the body's comparator_id (the sessioned name the web tier composed);
# every OTHER keyed caller's record id stands (F8 whole for them — the
# blanket crossing refused at the design). THE HONEST RESIDUAL: the web key's
# holder + this seam = id forgery for that holder — priced at the loopback's
# no-new-reach (the class already owns the machine) and the key's custody;
# the id PERSISTENT, NEVER VERIFIED (the record says what it knows and what
# it merely carries).
_WEB_KEY_ENV: Final[str] = "PRIORITYREE_WEB_KEY"
_WEB_KEY_PRESENT: Final[str] = os.environ.get(_WEB_KEY_ENV, "")
_WEB_LANE_DIGEST: Final[str] = hashlib.sha256(_WEB_KEY_PRESENT.encode()).hexdigest() if _WEB_KEY_PRESENT else ""
```

**THE DOOR'S BEFORE/AFTER (:564-565):**

before:
```python
    comparator_id = record.comparator_id if record.digest else body.comparator_id
    comparator_class = record.comparator_class if record.digest else body.comparator_class
```
after (the three-way shape; the class line BYTE-STANDING):
```python
    _web_lane = bool(record.digest) and record.digest == _WEB_LANE_DIGEST
    comparator_id = body.comparator_id if _web_lane or not record.digest else record.comparator_id
    comparator_class = record.comparator_class if record.digest else body.comparator_class
```
- the degrade (digest ""): the body's id — which IS the sessioned name web.py composed — stands ("the auth-off fallback");
- the web lane (digest == the marker): the body's id rides, the class the record's;
- every OTHER keyed caller: the record's id (F8 unchanged for them — a second service key's body id dies at the door; a compromised mcp/tools caller never rides a human id);
- THE CLASS NEVER CROSSES FROM THE BODY at any state (key_verify.py:198-200 untouched — F8 held; an llm-class voter claiming "human" through the web lane impossible: the class is the key's).
mcp_server.py:589-595 (the MCP door), votes.py:44 + :553-558 (the class gate), key_store.py:52-53 (the grant map), key_verify.py — ALL byte-standing (§5's no-break proofs).

## 3. THE TEMPLATE FORMS (three files — the authored home web/templates/, the wheel mapping unchanged)

### 3a. sitting.html (the conditional ask's seam — both lanes; the identity line; the correction affordance; the copy re-authored)

before (:6-7, the ask):
```html
  <label for="comparator-id">Your name for yourself as a judge — it stamps your votes. The same entry rides every judgment you cast on this page.</label>
  <input id="comparator-id" name="comparator_id" required minlength="1">
```
after (the ask RETIRED from the page — its conditional twin rides the form, §3b; the identity line + the affordance + the widened copy):
```html
  {% if remembered_name %}
  <p class="quiet">voting as: {{ remembered_name }}</p>
  <form hx-post="/ui/runs/{{ stem }}/unremember" hx-swap="none" class="quiet">
    <input type="hidden" name="csrf_token" value="{{ unremember_token }}">
    <button type="submit">not you? change your name or un-remember this device</button>
  </form>
  {% else %}
  <p class="quiet">Your name is asked once — the site remembers your entry for every judgment you cast from this device.</p>
  {% endif %}
```
(moho's finding 8 ruled: the "THIS PAGE" words widened to the carry's truth — "from this device"; the anonymous state renders the teaching line, never the identity line; the quorum line, the include, the ack region, the picker: byte-standing.)

### 3b. pair.html (the conditional ask's fragment twin — INSIDE the form; the hx-include retired; the hidden fields stay)

before (:3, the form's head):
```html
  <form hx-post="/ui/runs/{{ stem }}/vote" hx-target="#ack-region" hx-swap="innerHTML" hx-include="[name='comparator_id']">
```
after (the hx-include retired — the ask's field rides the form's own body; the conditional):
```html
  <form hx-post="/ui/runs/{{ stem }}/vote" hx-target="#ack-region" hx-swap="innerHTML">
    {% if not remembered_name %}
    <label for="comparator-id">Your name for yourself as a judge — it stamps your votes. Asked once; remembered for every judgment from this device.</label>
    <input id="comparator-id" name="comparator_id" required minlength="1">
    {% endif %}
```
(the comment line's provenance note grows the spec's cite; the hidden fields item_a/item_b/csrf_token/presentation_order STAY byte-standing — pair state, never identity; the cards and verdicts byte-standing. The twin's law: the ask renders INSIDE the vote form so the identifying POST's own body carries the name — the sitting include and the fragment lane both serve it: the chain's swap re-renders the conditional — after the identification the field drops; at the expiry's reload the ask returns.)

### 3c. landing.html (the register pre-fill — the visible editable value)

before (:12):
```html
    <label>Your name for yourself on this run. <input name="operator_id" required minlength="1"></label>
```
after:
```html
    <label>Your name for yourself on this run. <input name="operator_id" required minlength="1"{% if remembered_name %} value="{{ remembered_name }}"{% endif %}></label>
```
(a VISIBLE editable value, never a silent substitute — the operator claim ALWAYS rides the body (web.py:885 → service.py:158→480, byte-standing); the two surfaces' role-cue words ("on this run" vs "as a judge") stay distinct — the copy hazard ruled once at this seam; the anonymous landing carries no pre-fill.)

## 4. THE TEST FILES (both homes grown; every arc fenced by name; the count exact)

**THE INJECTION (unchanged):** the fixture at test_web_face.py:82-93 (app.state.seam/auth, the auth-off member) byte-standing; httpx2's TestClient carries the native cookie jar — the identify POST's Set-Cookie lands automatically, every subsequent request rides it; TWO CLIENTS = TWO BROWSERS (a second TestClient(app) per arc); the tamper/expiry arcs edit or clear the jar (client.cookies); the strength-check arc fires at the import boundary in the subprocess form (sys.executable -c "import prioritree.web" with the env set — the fixed-argv law); the service_auth arcs monkeypatch `service._WEB_LANE_DIGEST` (the module-level marker's own seam — the same monkeypatch school the stale-secret arc rides at web._csrf_secret).

**THE 26 ARCS (the exact count; the floor 449 → 475, tool-carried {"op":"add","args":{"a":"449","b":"26"},"result":475}):**

test_web_face.py grows 23:
1. `test_remember_cookie_lands_in_the_jar` — the identifying vote POST's response carries Set-Cookie: the jar holds the "remember" cookie; the attributes pinned (HttpOnly, samesite=lax).
2. `test_remember_max_age_fourteen_days` — the cookie's own Max-Age attribute pinned at 1209600 (the 14-day default).
3. `test_anonymous_get_never_mints` — the anonymous landing/sitting GETs carry no Set-Cookie (the not-modified skip; the pre-identify browser carries nothing to fixate).
4. `test_service_lanes_never_see_a_session` — the service app's middleware stack carries no SessionMiddleware (the walk over app.user_middleware) and a service-lane response sets no cookie (the child mount's constraint, asserted at the parent's own bytes).
5. `test_underfloor_secret_refuses_at_import` — the subprocess form: PRIORITYREE_WEB_REMEMBER_SECRET under the floor => the import refuses carrying the ThreePart bytes (expected/found/next_action); the same twin asserted at PRIORITYREE_WEB_CSRF_SECRET (the same arc's second subprocess run — the shared home §2a's law).
6. `test_first_vote_asks_once_then_carried` — the anonymous sitting renders the ask; the identifying POST mints the session (the jar); the vote lands; the next fragment GET carries no ask.
7. `test_identified_renders_carry_no_ask_both_lanes` — the sitting and the judge pages render pre-stamped (no comparator_id field), the identity line present.
8. `test_judge_page_fresh_get_carried_identity` — the deliberate lane's fresh GET served by the carried identity (RUN-0008's own lane — the per-visit cost dead).
9. `test_vote_reads_the_remembered_id` — at the auth-off degrade the record's comparator_id == the sessioned name (the vote log read via Serialize(tmp_path)); the body's field ignored when the session carries one.
10. `test_expired_session_taught_refusal_reload_recovers` — the jar cleared; the vote POST (no name field) => the refusal fragment's next_action carries the lapse copy verbatim, never the schema's words; the write never lands (the census unchanged); the reload (the fresh GET) re-renders the ask and recovers.
11. `test_two_browsers_two_sessions` — two TestClients, two names, both votes land distinct in the log (the multi-user truth at the record).
12. `test_epoch_token_minted_once` — two identified sitting GETs hold the SAME token (no per-render session write; the epoch never re-minted).
13. `test_concurrent_tabs_same_token_both_pass` — two votes posted with the same held token both 200 (the concurrent-tab cure asserted — the naive nonce's last-write-wins race dead by construction).
14. `test_scraped_token_dead_in_another_browser` — client A's identified token posted from client B (its own empty jar) => refused; the write never lands.
15. `test_register_token_stays_path_bound` — identified, the landing's token still the path-bound form (never epoch-composed); the register POST with it lands the ack.
16. `test_reidentification_rotates_epoch_old_token_dies` — the un-remember POST then the re-identification: the pre-rotation token refused at the vote (the epoch rotated), the refusal teaches the reload, the fresh token passes.
17. `test_voting_as_renders_both_lanes` — "voting as: <name>" at the sitting and the judge pages (the visible render — the cookie-swap, the typo, the bleed all SEEN).
18. `test_anonymous_never_renders_identity_line` — the anonymous render shows the ask's twin, never the identity line nor the correction form.
19. `test_unremember_deletion_cookie_ask_returns` — the un-remember POST: the response carries the deletion cookie (remember=null; the 1970 expiry — the engine's own form asserted) + the HX-Redirect to the sitting; the next render shows the ask.
20. `test_change_verb_reidentifies_new_name_lands` — un-remember then the identifying vote with the new name: the new name lands in the log, the render shows it, the epoch differs (the rotation asserted via the token change).
21. `test_landing_prefills_operator_when_remembered` — the identified browser's landing renders the operator field's value prefilled (the visible editable value); the POST's operator claim always the body's.
22. `test_anonymous_landing_no_prefill` — the anonymous landing carries no value attribute on the operator field.
23. `test_cookie_roundtrip_within_priced_bound` — the "remember" cookie's signed value length within the priced 72-92 B ± the 2-B base64 unpadding variance (assert 70 ≤ len ≤ 94 at realistic names — keisan's one unverified residual verified at the build).

test_service_auth.py grows 3 (the two-role stamping, at the pinned arcs' home):
24. `test_web_lane_sessioned_id_rides_class_the_keys` — the marker patched to the key's digest: the body's id (the sessioned name web.py composed) rides onto the record; the class the KEY's (the body's class claim never consulted — F8 held LIVE at the web lane).
25. `test_web_lane_class_claim_dies` — the web lane's body claims "llm"; the key's class "human" stamps the record (the class gate's own truth; an llm-class voter claiming "human" through the browser impossible).
26. `test_non_web_keyed_caller_id_never_rides` — a second service key (a different digest) whose body carries a human id: the record's id stands (the blanket crossing refused; the standing test_verified_id_wiring_body_id_ignored byte-standing beside it — the web-lane branch composes, never rewrites the other lanes' law).

**THE STANDING ARCS' FENCE:** the three pinned seam arcs (test_service_auth.py:366-395) byte-standing (a non-web key's body id still ignored — arc 24's branch never fires for them); the CSRF four (test_web_face.py:461-521) byte-standing (the register lane path-bound; the drive-by/mismatch/stale arcs' bytes unchanged); `test_vote_echo_already_recorded`'s second POST scrapes the pair fragment's fresh token (§2e's note — the arc's assertions byte-standing); the four CSRF-context token scrape unchanged (pre-identification renders are path-bound by construction).

**THE NEW NAMED RULING (the precedent form, never blanket):** the strength-check arc's subprocess rides the S603/S607 school — pyproject's per-file-ignores gains, at the tests/test_harness.py + tests/test_service_acceptance.py precedent's form:
```toml
# RULING (the voter-session spec §4, G-VOTERSESSIONSPEC-BRIEF approved …): S603 — the
# strength-check arc's subprocess.run IS the no-shell law's own form (sys.executable + "-c" +
# the fixed in-source program; the untrusted-input intent never rides a deterministic
# import-boundary probe). S607 named for the ruling's form's stability. The ignores ARE the
# rulings, named.
"tests/test_web_face.py" = ["S603", "S607"]
```
(web.py's standing S105 entry's wording grows the `_REMEMBER_SECRET_ENV` name — the same ruling, the same public-name class, no new entry; service.py's edits trigger nothing new — the two-line seam composes inside the existing rulings.)

## 5. THE NO-BREAK PROOFS (the unit's fence)

- **THE LLM LANES UNTOUCHED:** cli.py, mcp_server.py, mcp_auth.py byte-standing (the stdio/tools tier — the llm votes ride the mcp audience's keys, never the browser); kensho's independent read at the build gate names the untouched bytes.
- **THE CLASS GATE + THE TALLY UNTOUCHED:** votes.py:44 + :553-558, tally.py, run_store.py, session.py (the library), key_store.py, key_verify.py — byte-standing; the class NEVER crosses from the body at any door (service.py:565 byte-standing; mcp_server.py:589-595 byte-standing).
- **THE AUTH-ON DEFAULT AT THE CI:** the suite green with NO session secret env set — the boot-mint form's test law (§2a: the unset path byte-equivalent to the standing line; the under-floor refusal fires only on a weak env value at import).
- **THE FLOOR:** 449 → 475 (26 new arcs, §4's exact count; the brief's ~475 reconciled at the tool-carried trace); ruff zero findings; pyright 0/0 (the zero-ignore strictness: the S603/S607 ruling the ONLY new ignore, named at §4's form).
- **THE STANDING BYTES:** the register lane's mint path-bound; the frozen wire's six service lanes byte-standing (no cookie semantics — the child mount's whole point); the shareable URL's READ capability unchanged (anonymous GETs stay; ack.html's quorum>1 nudge preserved); the never-log-the-cookie discipline held (no log line names cookie bytes — the new region logs nothing).

## 6. THE PER-STEP PLAN (R8 — one file per dispatch; the read-backs named)

Seven file-dispatches (tool-carried {"op":"count","args":{"values":"[\"pyproject.toml\",\"web.py\",\"sitting.html\",\"pair.html\",\"landing.html\",\"test_web_face.py\",\"test_service_auth.py\"]","result":7}), in the composition's order — the door first (the middleware unimportable without it):

1. **pyproject.toml (+ the lock inside the act):** §1's dependency line + `uv lock` + §4's new per-file ruling. Read-back: the lock's itsdangerous entry; the import live (`python -c "from starlette.middleware.sessions import SessionMiddleware"`); the six standing dependency names unchanged.
2. **web.py (the remember region whole):** §2a-§2f — the import, the secret's shared home, the helpers, the mount + the assert-guard, the epoch CSRF (the guard + the mints), the vote controller's read, the correction route, the lanes' legal set. Read-back: the mount precedes every session read (the guard's own construction check); the register mint path-bound; the refusal copies verbatim (the lapse + the reload); the standing CSRF arcs green.
3. **sitting.html:** §3a — the identity line, the correction form, the widened copy. Read-back: both lanes' renders (the sitting GET + the judge GET) show the line when identified, the teaching line when anonymous.
4. **pair.html:** §3b — the conditional ask's twin, the hx-include retired, the hidden fields standing. Read-back: the fragment GET + the sitting include both carry the conditional; the hidden pair fields byte-standing.
5. **landing.html:** §3c — the pre-fill's visible value. Read-back: the anonymous landing no value; the identified landing the editable prefill; the register POST's operator claim the body's own.
6. **test_web_face.py:** §4's 23 arcs. Read-back: the arcs' names + counts; the jar's behavior; the standing arcs green.
7. **test_service_auth.py:** §4's 3 arcs. Read-back: the web-lane branch's three-way law pinned; the standing seam arcs byte-standing.

Then **FLOOR-GREEN** (the increment's second step, the three acts verbatim): `uv run pytest` (the suite green at 475 passed — the count named), `uv run ruff check .` (zero findings), `uv run pyright` (0 errors, 0 warnings). THEN the gate's own lanes: kensho's validate/voter-session (the independent verification) + moho's cold implementation walk (the identification once, the carried operations at both lanes, the correction verbs, the expiry's teaching met) — the findings ride G-VOTER-SESSION as evidence; the RUN-0008 riding check (the deliberate judge page serving the sessioned identity — the probe's unblocking proven at the walk, never assumed).

## THE BOTTOM LINE

The spec opens the unit's every byte on the approved brief's ground: the door (one wheel, the lock inside the act, the ModuleNotFoundError face), the remember region whole (the child mount + the assert-guard + the shared secret home + the epoch CSRF + the cast read + the correction route), the three templates' exact forms, the 26 arcs at their exact names, the seven dispatches + the floor-green. The trade-off the plan carries, unchanged from the brief: a carried, browser-bound, self-claimed pseudonym — persistent, never verified — bought for the human's time back; the llm lanes, the class verification, and the tally's semantics byte-standing. The approval is the collaborator's act at G-VOTERSESSIONSPEC-BRIEF; this spec the build's whole ground.

— togo (統合), the exact-task spec whole; every edit fenced at the tree's own bytes, every choice citable to the approved brief and the cycle's record; nothing decided that is the collaborator's to decide.
## Reported by togo — 2026-11-26T19:39:09Z

R6 — the micro-fold's two rulings (togo, synthesize/votersessionspec; jikko's step-2 findings the intake, reports/build/voter-session.md).
RULING 1 — THE ENV NAME: the T-form STANDS; the spec's "PRIORITYREE_WEB_REMEMBER_SECRET" (§2a) and the §2d CSRF-knob cites are the elided-T typo, this fold its correction. Read-back web.py:124-125: _CSRF_SECRET_ENV = "PRIORITYTREE_WEB_CSRF_SECRET"; _REMEMBER_SECRET_ENV = "PRIORITYTREE_WEB_REMEMBER_SECRET" — the standing "PRIORITYTREE_WEB_*" law (web.py's constant, README:183, the auth spec's own fence); every cycle record citing the elided form corrects to the T; arc 5's subprocess cites the T-form.
RULING 2 — THE §2d FENCE STANDS, the lapse copy wins; §4's byte-standing claim is the stale one (pinned against the old single-branch copy). The expired-or-forged case is the EMPTY session (the cookie died at max_age, the secret rotated, or the drive-by never held one): the identity is gone, and "reload the page and re-send" teaches a blind re-send that re-refuses at the cast read's session-first lane (jikko's read-back, web.py:1114-1127) — the stumble NOT cured in one step (moho's walk precedent). The lapse copy names the state and the one-step cure: reload → the page re-asks the name → re-identify (the epoch re-minted, web.py:200-201) → the re-send lands.
The winning branch's exact bytes (web.py:276): "your identification lapsed — reload, the page re-asks your name". The reload copy (web.py:274): "reload the page and re-send — the re-render mints a fresh token" — stands for the LIVE-session stale-tab branch only (the rotated epoch under a live session: reload re-renders the current token, re-send passes, no re-identification needed).
THE TWO ARCS' RE-DERIVED PINNED BYTES: test_csrf_drive_by_refused_write_never_lands + test_csrf_mismatched_token_refused pin the refusal's next_action = "your identification lapsed — reload, the page re-asks your name" (re-derived from the old pinned "reload the page and re-send — the re-render mints a fresh token"; the re-derivation dispatch 6's act, named here per the fold's charge).
## Reported by togo — 2026-11-26T20:51:56Z

THE REGISTER-LANE VALIDATE-SIDE EXCEPTION FENCED (jikko's one red — test_register_token_stays_path_bound; the fix-home web.py's guard, the brief §86's own law; READ-ONLY held, the bytes the gate's to land).
BEFORE (web.py:271 verbatim): `expected = _mint_bound(request.url.path, request)` — epoch-composed whenever a live session rides, against the landing's unconditional `_mint_csrf(_REGISTER)` at :616: the sessioned browser can never register, and the :273 reload-teaching lies (the re-render mints path-bound again).
AFTER (the route-scoped branch — the register lane ALONE, NEVER a blanket bypass):
    if request.url.path == _REGISTER:  # §86 — the register validates PATH-BOUND even when the session now exists
        expected = _mint_csrf(_REGISTER)  # mirrors the landing's mint at :616
    else:
        expected = _mint_bound(request.url.path, request)  # the vote + unremember lanes: the epoch-bound recompute byte-standing
THE FENCE'S LAW (why the exception is honest): the landing's mint PRE-DATES the identification — :616 never reads the session; the epoch the SESSION's own act (minted once at identification; the register POST never writes the session), the register token the ANONYMOUS act — so the validate side now mirrors the mint side for that one lane alone.
BOTH CURES WHOLE: the epoch-rotation cure untouched on every sessioned lane (the guard's three wired POSTs — register :990, vote :1095, unremember :1181 — only the register branch changes); the register's drive-by cure standing (the POST still demands the page-minted token at the same compare_digest); the lying reload-teaching dead by construction (expected = the page's mint on that lane, whatever the session's state).
— togo (統合), R6; the guard whole + the arc's assertion + the landing's mint read back at the cited bytes this pass.
