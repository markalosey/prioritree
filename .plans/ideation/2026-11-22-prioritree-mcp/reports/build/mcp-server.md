<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — build/mcp-server

**Route:** prioritree-mcp (executing) | **Events:** 6 | **Reports:** 3

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T21:30:42Z |
| 2 | report | jikko | 2026-11-22T21:34:02Z |
| 3 | dispatch | shinko | 2026-11-22T21:34:15Z |
| 4 | report | jikko | 2026-11-22T21:59:12Z |
| 5 | dispatch | shinko | 2026-11-22T21:59:34Z |
| 6 | report | jikko | 2026-11-22T22:43:31Z |
## Reported by jikko — 2026-11-22T21:34:02Z

# JIKKO — build/mcp-server step 1 — the dep + the sync-check (2026-11-22)

THE DEP (spec §4): pyproject.toml:7 landed byte-exact — dependencies = ["fastapi", "httpx2", "jinja2", "ouncemcp", "python-multipart", "uvicorn[standard]"] (the sorted position, j-o-p holds); no other pyproject byte touched, the dev group unchanged (patch: 1 hunk, zero findings; line 7 read back verbatim).

THE SYNC'S FOLD (named per the dispatch): jikko's pack carries no make dev verb (lifecycle: start/stop/status/restart/log/output; the Makefile's dev/uv-sync target unrouted) — the mint rides the floor's own uv run at a later step: step 2's uv run ruff / uv run pyright read-back is the first uv run after the dep, step 3's uv run pytest otherwise (the standing fold form, spec §4).

THE LOCK: uv.lock at HEAD (version 1 / revision 3, 37 [[package]] entries) carries NO ouncemcp entry (grep-verified) — the lock regen rides the fold.

THE INSTALLED: .venv/lib/python3.13/site-packages/ (77 entries, populated: fastapi, jinja2, pydantic, pytest, ruff) carries NO ouncemcp — glob-verified, the package dir and any dist-info both absent.

THE SURFACE VERIFICATION (OunceServer's constructor, @server.tool's params, the Effect enum, the Budget form, the idempotency/approval params): DEFERRED — the dispatch's no-verb branch fired; no installed object exists to read, and the pass rides the minting step's read-back. DIVERGENCES: NONE COMPARABLE YET — never "none found"; the comparison's object is absent; every divergence reports at the fold, never absorbed.

NOT DONE (honest): the install-verification (uv run python -c "import ouncemcp") — no routed verb carries the sync from this seat; the spec's green-before-step-2 gate rides the coordinator's own make dev or step 2's mint.
## Reported by jikko — 2026-11-22T21:59:12Z

STEP 2 LANDED -- src/prioritree/store_lock.py whole per the spec's SS1 fence: the Lock context manager (the naming law's symbol; __all__ = ["Lock"]), one advisory exclusive fcntl.flock LOCK_EX blocking on {store_home}/.prioritree.lock, the "a"-open create-if-absent, the inode law (never deleted) in the docstring, the lock path derived from the injected home, never re-defaulted. 91 lines = the fence's 87 + the NOTES' four mandated lines (the __init__ "IO[str] | None" declaration, the __exit__ None guard's two, the __init__ home hold the fenced __enter__ body requires). Two build deltas reported, no pyproject touch: the fence's TYPE_CHECKING tenant Iterator was dead under the classic __enter__/__exit__ shape -- swapped for the needed IO (F401, the zero-findings bar); Path moved under TYPE_CHECKING per TC003 (annotation-only here; the service_store.py:31 precedent). INSTRUMENTS: make lint (ruff ALL) "All checks passed" whole-tree; make typecheck (pyright strict) 0 errors, 0 warnings, 0 informations -- clean at the new file. NOTHING else touched.
## Reported by jikko — 2026-11-22T22:43:31Z

STEP 3 — the two compositions landed per mcpserverspec §3; pyright 0/0/0, ruff zero findings, uv run pytest = 156 passed (the floor held — behavior-transparent: the lockfile is invisible to the RUN-*.jsonl mint glob; the missing-home refusal bytes unchanged).
service_store.py: `from prioritree.store_lock import Lock` added after the Persist import (:31); the six verb heads now `with Lock(self._store_home), self._lock:` — register :125, serve :146, cast :175, census :196, rank :215, manifest :240 — the flock acquired FIRST, the threading.Lock within, per-acquisition.
cli.py: `from prioritree.store_lock import Lock` added (:33, the isort slot); the five handler windows hoist `home = cast("Path", args.home)` and wrap the load+verb whole under `with Lock(home):` — register :205-212, next :235-238, vote :261-271, state :296-299, tally :326-329 — every render OUTSIDE the with, released before rendering.
Docstring clause lines updated per the spec: each verb/handler names the machine-wide file-lock wrap; service_store's module + class clauses amended (the flock outermost, the single-worker banking superseded, the lockfile named in Touches).
Choice reported (collision resolved): the pre-existing `from threading import Lock` aliased `as ThreadLock` (:27) — the spec's bare `Lock` at the heads demands the name for store_lock's Lock; `self._lock = ThreadLock()` (:96); the HTTPException-as-StarletteHTTPException alias precedent.
Same-turn findings: two E501 (serve/manifest summaries at 124>120) trimmed to "under the file lock outermost"; zero new per-file-ignores.
Not done: nothing beyond §3's regions — service.py/web.py untouched (the flock rides inside the seam), zero core edits.
