<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/mcpserverspec

**Route:** prioritree-mcp (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T21:12:24Z |
| 2 | report | togo | 2026-11-22T21:28:40Z |
## Reported by togo — 2026-11-22T21:28:40Z

# TOGO — synthesize/mcpserverspec — THE EXACT-TASK SPEC: the mcp-server unit's bytes whole (2026-11-22)

GROUND READ (all on disk, cited): the approved unit brief reports/synthesize/mcp-server.md (G-MCPSERVER-BRIEF); the approved design brief reports/synthesize/mcp-design.md (the §2 authored texts VERBATIM — the build's acceptance); reports/discover/mcp-server.md + reports/understand/mcp-server.md (the composition points at exact lines); reports/census/ouncemcp.md (the API forms; the package NOT installed — author against the census's recorded forms, the install-verification the build's first-step check, the import-verification lesson named: never trust the census's memory once the dep lands); reports/census/exposure.md (the ThreePart grammar, the strictly-binary signals); the tree at HEAD — service.py:158-183 (the module-level app + render_refusal precedent), service_store.py whole (the six verbs' heads: register :118-119, serve :139-140, cast :168-171, census :189-190, rank :208-209, manifest :233-234), cli.py:190-309 (the five handler windows: register :202-207, next :228-229, vote :251-259, state :282-283, tally :308-309), pyproject.toml (deps :7, the per-file-ignores rulings :31-122), session.py:161-318 (the five ops), votes.py:33 (COMPARATOR_CLASSES), tally.py:331-395 (the SAFE HALT's render), registry.py:48-64 (OperatorDeclaration, WEAK_ORDER_TRIPLE), tests/test_service_acceptance.py:41-54 (the fixed-argv Popen precedent), tests/test_service_face.py (the face-arc precedent), Makefile (the standing targets — unedited by this unit).

THE IMPORT-VERIFICATION LESSON (the dispatch's own mandate): every ouncemcp form below is authored against the census's recorded API (release 1.0.0rc3, the API frozen). The build's FIRST-STEP CHECK: `uv run python -c "import ouncemcp"` — then verify each import (OunceServer, Effect, as_caller) against the installed package; a divergence between the census's memory and the installed surface is a finding reported, never silently absorbed.

## 1. THE SEAM MODULE WHOLE — src/prioritree/store_lock.py

ASCII-only bytes; stdlib only (fcntl, pathlib); the R5/ruff-ALL discipline at authoring (no multibyte in docstrings, no implicit concatenation, any lint fire a NAMED per-file ruling at pyproject, never blanket).

THE MODULE (whole, byte-shaped):

```python
# Copyright (C) 2026 Mark Losey. All rights reserved.
"""store_lock -- the machine-wide lock seam: the flock that spans processes.

The mcp-server unit (F1's ruled clause, the approved design brief
reports/synthesize/mcp-design.md:22-23): an advisory exclusive fcntl.flock
on {store_home}/.prioritree.lock -- created on demand, NEVER deleted (flock
binds the inode; a deleted lockfile is a NEW lock -- a second writer locking
a fresh inode is no lock at all), acquired around each WHOLE store act
(load->act->save), released before rendering (the service seam's own law,
service_store.py:59-60). CLOSED because all writers are local, none
bypasses: the harness-launched session servers, the localhost service, the
CLI; external agents speak THROUGH the shared HTTP server. Stdlib only
(the tier fence, service_store.py:19); the lock path derives from the
INJECTED home, never re-defaulted (the service_store.py:77-80 precedent
-- the hidden-global drift refused).
"""

from __future__ import annotations

import fcntl
from pathlib import Path
from typing import TYPE_CHECKING, Final

if TYPE_CHECKING:
    from collections.abc import Iterator

__all__ = ["Lock"]

_LOCK_FILE_NAME: Final[str] = ".prioritree.lock"


class Lock:
    """Lock the store acts across processes under one machine-wide file lock.

    Purpose: one advisory exclusive flock (fcntl.LOCK_EX, blocking until
    granted) on the lockfile at the injected store home -- the context
    manager the three writer tiers compose (the MCP server, the service's
    Serialize verbs, the CLI's handlers): acquired around each WHOLE store
    act, held across load->act->save, released before rendering. The
    lockfile is opened "a" -- create-if-absent, NEVER truncated (the file's
    bytes are nobody's; the INODE is the lock's identity) -- and NEVER
    deleted by this hand (flock binds the inode: a deleted lockfile is a new
    lock, the cure collapsing at the first unlink -- the inode law carried
    here, never violated at exit).
    Refuses when: never -- LOCK_EX blocks until granted (advisory on darwin;
    closed because every writer is local and none bypasses the seam).
    Re-run: deterministic in effect -- the same home derives the same lock
    path; re-entry serializes (a second holder blocks until the first
    releases).
    Touches: the lockfile alone (created on demand, never truncated, never
    deleted); the store files are the CALLER's acts inside the held lock.
    Provenance: the approved design brief F1 (the seam's ruled clause
    whole), the unit brief reports/synthesize/mcp-server.md SS3 (the
    composition clauses), the naming law (the act-statement's first word),
    G-MCPSERVERSPEC-BRIEF.
    """

    def __init__(self, store_home: Path) -> None:
        """Hold the injected home and derive the lock path -- never re-defaulted.

        Purpose: the lock path DERIVES from the injected home
        ({store_home}/.prioritree.lock) -- store-as-parameter, the
        STORE_HOME law (run_store.py:48-53); the default never re-derived
        here (the hidden-global drift refused, the service_store.py:77-80
        precedent).
        Refuses when: never -- construction derives and holds.
        Re-run: idempotent -- a fresh Lock over the given home; no
        acquisition at construction.
        Touches: nothing -- the path is derived, the file opened at
        __enter__ alone.
        Provenance: F1 (the home-injection law), G-MCPSERVERSPEC-BRIEF.
        """
        self._lock_path = store_home / _LOCK_FILE_NAME

    def __enter__(self) -> None:
        """Open "a" and flock LOCK_EX -- blocking until granted."""
        # Created on demand ("a" -- create-if-absent, never truncated),
        # NEVER deleted: flock binds the inode; a deleted lockfile is a
        # NEW lock (the inode law, the docstring's own clause).
        self._store_home.mkdir(parents=True, exist_ok=True)
        self._handle = self._lock_path.open("a")
        fcntl.flock(self._handle.fileno(), fcntl.LOCK_EX)

    def __exit__(self, _exc_type: object, _exc_value: object, _traceback: object) -> None:
        """Release the flock and close the handle -- the file itself NEVER deleted."""
        fcntl.flock(self._handle.fileno(), fcntl.LOCK_UN)
        self._handle.close()
```

NOTES: `self._handle` assigned only in `__enter__` — pyright strict demands the attribute declared; the build adds `_handle: IO[str]` at __init__ (assigned an unopened sentinel via `Path("/dev/null").open()` is refused — instead `__init__` sets `self._handle: IO[str] | None = None` and `__enter__` narrows; the exit guards None). PLW3201/EM101-class fires if any — named rulings per fire. The mkdir at `__enter__` rides the home's own create-if-absent law (Persist.register does the same).

## 2. THE MCP MODULE WHOLE — src/prioritree/mcp_server.py

Tier-imports-core (the service.py:61-66 precedent); sync def bodies (the service's threadpool precedent — the blocking flock wants sync); ONE public symbol per the __all__ convention: the module-level `server` (the act-statement: "Serve the five ops as OunceMCP tools" — the first word the symbol; `__all__ = ["server"]`).

THE STRUCTURE (whole, region-by-region):

(a) MODULE DOCSTRING — five fields in prose form per the tree's convention (the module docstring carries the unit's clause whole: the five tools, the ThreePart at one render point, DONE a value never an error, the K=10 cap, the two run forms, NO runner at import — the service.py precedent).

(b) IMPORTS:
```python
from __future__ import annotations
from typing import TYPE_CHECKING, Final, Literal
from pydantic import BaseModel, Field
from ouncemcp import Effect, OunceServer
from prioritree.registry import OperatorDeclaration
from prioritree.run_store import STORE_HOME, StoreRefusedError
from prioritree.service_store import Serialize
from prioritree.session import ExhaustedQueue
from prioritree.tally import TallyRefusedError
from prioritree.votes import COMPARATOR_CLASSES, VotesRefusedError
from prioritree.store_lock import Lock
```
(The ouncemcp import forms the census's recorded surface: OunceServer, Effect; verify against the installed package at the build's first step.)

(c) THE MODULE-LEVEL OBJECTS:
```python
LOCK_HOME: Final[Path] = STORE_HOME
_seam = Serialize(STORE_HOME)
_lock = Lock(STORE_HOME)
server = OunceServer(name="prioritree")
```
(The naming law: "Serve the five ops as OunceMCP tools" — the symbol `server`, the act-statement's first word; the construction form per the census: OunceServer(name=...). The seam injected at construction, NO runner at import — the service.py:158-165 precedent. No Budget(...) at the server — the startup 1,005 = 25% of the 4,000 default, no override, per the design brief §4.)

(d) THE INPUT MODELS (byte-shaped; the Field texts VERBATIM from the design brief §2):

RegisterInput: items: list[str] with Field(min_length=2, description="The items to rank, one id per entry; at least two, all unique, none empty"); quorum: int = Field(ge=1, default=1); operator_id: str = Field(min_length=1); question: str = Field(min_length=1).
(The items as BARE IDS — the MCP tier's register carries ids, not [id, label] pairs: the design brief §4 rules the tool's items "list[str], min 2, unique, non-empty" — the label elided at the tool tier, the door builds ItemRow from (id, id). The door's register_run accepts Sequence[Sequence[str] | ItemRow] — the build passes [(id, id) for id in items]; the core's ItemRow(id, label) receives label=id. Uniqueness/non-emptiness enforced by the model (unique=True is not a Pydantic primitive — a field_validator refuses dups and empties at the SCHEMA, the stamps' schema-gate pattern re-carried; the core's gates ride beneath).

NextInput: run_id: str = Field(min_length=1); seed: int | None = Field(default=None).

CastInput: run_id, pair: list[str] with Field(description=TEXT_PAIR, min_length=2, max_length=2); winner with description=TEXT_WINNER; comparator_id with description=TEXT_COMPARATOR_ID; comparator_class: Literal["human", "llm"] with description=TEXT_COMPARATOR_CLASS (the pattern BUILT FROM the core's COMPARATOR_CLASSES: `Literal[tuple(sorted(COMPARATOR_CLASSES))]` — the vocabulary never forks, content-in-configuration held; the import-verification check confirms the literal matches the installed core); notes: str | None = None; supersedes: str | None = None.

RunInput (census + tally share the shape, two classes per the census's per-tool schema): run_id: str = Field(min_length=1).

(e) THE RETURN MODELS:

RegisterAck: run_id: str; count: int; quorum: int; verdicts: list[str] with Field(description="The run's judgment vocabulary -- votes.cast's winner comes from this set (default: prefer-a, prefer-b, tie -- positional over the pair as sent).").
(VERBATIM from the design brief §2's RegisterAck.verdicts text — the em-dash rendered "--" per the ASCII law.)

NextOutcome — ONE discriminated model: done: bool; item_a: str = ""; item_b: str = ""; count: int = 0; expected: str = ""; found: str = ""; next_action: str = "". The done tag IS the signal, never the message text: false => the pair triple populated; true => the three fields from the caught ExhaustedQueue VERBATIM (session.py:228-238), the pair fields empty. (The one-model form ruled at the brief's §7 open questions: the literal/union form declined — a union return model's outputSchema forks the client's parse; ONE model, the boolean tag, the empty-string defaults.)

CastAck: vote_id: str; count: int; acknowledged: bool with Field(description=TEXT_ACKNOWLEDGED) — VERBATIM: "true = a re-send that matched an existing judgment -- the original acked, the count unchanged, never double-counted; false = a fresh judgment, newly recorded, the count grew by one."

CensusView: total: int; items: dict[str, int] (F3: per_pair_counts and vote_log elided, run_id elided — the ack-elision law).

TallyView: ranked_groups: list[list[str]]; per_item_wins: dict[str, int]; per_item_losses: dict[str, int]; per_item_ties: dict[str, int]; coverage: CoverageView; algorithm_version: str. CoverageView: components: list[list[str]]; cycle: list[list[str]]; pairs_expected: int; pairs_at_quorum: int; done: bool (pair_counts ELIDED — the O(n^2) term is 94% of the mass; the summary totals pairs_expected/pairs_at_quorum land against CoverageDatum's own ground — the exact field names landed at the build, the brief's open question resolved: pairs_expected = len(schedule_pairs(ids)), pairs_at_quorum = the weighted count of pairs at quorum; done = coverage.done).

(f) THE ONE RENDER POINT — render_refusal (the service.py:168-183 precedent, re-carried at this tier):
```python
def _render_refusal(refusal) -> dict[str, str]:
    return {"expected": refusal.expected, "found": refusal.found, "next_action": refusal.next_action}
```
THE K=10 CAP'S SHAPER at the SAME render point, TallyRefusedError alone: the core's three fields read as DATA; legs 1-2 (zero-coverage, components) render WHOLE; leg 3 (the under-quorum enumeration in found AND next_action — both O(n^2)) renders CAPPED: the shortfall total named ("N under-quorum pairs total; first 10 shown") + the first 10 pairs in the core's canonical order, each with its count/needs. The cap's form: the render point re-derives the shortfall list ONLY from refusal.found/refusal.next_action's own structured ground — NO: the shaper NEVER reparses prose. THE HONEST FORM: the tool body catches TallyRefusedError and calls the core's OWN render members: the refusal's found/next_action strings are reparsed NEVER; instead the cap rides at the RENDER of the shortfall section — the core's `_found_sections`/`_next_action_sections` are private (the fence: no core edits) — SO the cap's shaper re-derives the shortfall list from the manifest+census INSIDE the caught window (a fresh census read under the held lock, schedule_pairs the canonical order, count each, filter < quorum) and CONSTRUCTS the capped found/next_action from the refusal's own expected (carried whole) + the re-derived capped sections — the refusal's three-field grammar held, the cap bounded linear at n=100, the shaper touching only the RENDER never the error's own values. The CLI and service keep their verbatim renders — the cap lands at the MCP render point ALONE.

(g) THE FIVE TOOLS — `@server.tool(name=..., effect=..., idempotency=...)`, sync def, the docstring the description VERBATIM:

1. `@server.tool(name="runs.register", effect=Effect.WRITE, idempotency=True)` — docstring VERBATIM (the design brief §2 Cure 2, em-dashes as "--" per the ASCII law): "Register items for a pairwise-comparison sitting: pairs are judged one against another, the votes tallied into a ranked whole. The sequence: runs.next serves each under-quorum pair, votes.cast records the judgment, runs.tally emits the rank, votes.census audits. quorum is the judgments each pair needs before the tally. The ack's run_id is the sitting's handle -- carry it to every later call; re-registering the same items mints a NEW run."
BODY: with the lock held (the flock wrapping the Serialize window — see (i)), `stem = _seam.register([(id, id) for id in body.items], OperatorDeclaration(id=body.operator_id, question=body.question), body.quorum)` — the verdicts field the dataclass default's triple; refusals caught BY TYPE -> StoreRefusedError/VotesRefusedError raise OunceMCP's error VALUE carrying the ThreePart (the raise-at-the-render form: `raise ToolError(...)`-class per the census's `raise NotFound(msg, hint=...)` idiom — the exact exception class verified at the build's first step against the installed package; the census's form `errors are values` means the ERROR carries structured fields, rendered at ONE point; the build lands the structured ThreePart {expected, found, next_action} as the error's payload — the census's NotFound(msg, hint) style DECLINED for the structured ThreePart, per the brief §2). Return RegisterAck(run_id=stem, count=len(body.items), quorum=body.quorum, verdicts=sorted(WEAK_ORDER_TRIPLE)).

2. `@server.tool(name="runs.next", effect=Effect.READ)` — docstring VERBATIM: "Serve the sitting's next under-quorum pair -- the loop's read: call until done:true (every pair at quorum), then runs.tally. Returns the pair as [item_a, item_b] (the verdicts are positional over this order) and its current count. seed optional -- the default order is stable per run."
BODY: under the lock, `item_a, item_b, count = _seam.serve(body.run_id, body.seed)`; ExhaustedQueue caught BY TYPE => return NextOutcome(done=True, expected=done.expected, found=done.found, next_action=done.next_action) — DONE A VALUE NEVER AN ERROR (the CLI's exit-0 precedent, cli.py:373-375); refusals => the ThreePart at the render point.

3. `@server.tool(name="votes.cast", effect=Effect.WRITE, idempotency=True)` — docstring VERBATIM: "Cast one judgment on a pair -- the sitting's only write. The judgment is stamped (comparator_id, comparator_class), durable at once, append-only. A byte-identical re-send acks the original (acknowledged=true, the count unchanged -- one voice, never double-counted); a changed verdict is a new record; supersedes cites a vote_id to correct one. A vote is legal on any registered pair -- no serve needed."
BODY: under the lock, `vote_id, _record, count, acknowledged = _seam.cast(body.run_id, body.pair, body.winner, body.comparator_id, body.comparator_class, body.notes, body.supersedes)`; return CastAck(vote_id=..., count=..., acknowledged=... with the ruled semantics carried by the core verbatim — true = re-send/unchanged, false = fresh/grown; the record ELIDED).

4. `@server.tool(name="votes.census", effect=Effect.READ)` — docstring VERBATIM: "Audit the sitting's counts as-is: the total judgments and each item's count. The evidence surface -- what has landed, never what should have."
BODY: under the lock, snapshot = _seam.census(run_id); return CensusView(total=len(snapshot.vote_log), items=dict(snapshot.per_item_counts)).

5. `@server.tool(name="runs.tally", effect=Effect.READ)` — docstring VERBATIM (the design brief §2 Cure 1): "Tally the sitting into the ranked whole: ranked_groups (ids best-first, equal scores grouped), per-item wins/losses/ties, coverage. Under quorum the tally SAFE-HALTs: the refusal names the failing legs and the closing pairs -- cast them via votes.cast (a legal pair needs no serve); pairs beyond your one voice mean the sitting needs more voters (resume the sitting). Re-tally after casting names what remains." With `result_tokens=4500, budget_reason="the frozen whole at n=100 minus the elided pair mass -- 100 ids in ranked groups + components + the three per-item maps ~= 3,860; 4,500 holds the verified ceiling with 640 tokens (~16%) headroom."` (the decorator kwargs per the census's per-tool form; the exact kwarg spelling verified at the build's first step).
BODY: under the lock, result = _seam.rank(run_id); TallyRefusedError => the K=10 capped ThreePart (f); asdict-style whole: TallyView(ranked_groups=[list(g) for g in result.ranked_groups], per_item_wins=dict(...), ..., coverage=CoverageView(components=[list(c) for c in result.coverage.components], cycle=[list(e) for e in result.coverage.cycle], pairs_expected=..., pairs_at_quorum=..., done=result.coverage.done), algorithm_version=result.algorithm_version).

(h) THE SYNC BODIES' COMPOSITION FORM (the same door the service rides): each body is `def` (sync) — the census records no async requirement; the blocking flock wants sync bodies; OunceMCP/FastMCP runs sync tools off the event loop (the threadpool precedent re-carried). The lock form per tool:
```python
def _under_lock(register, run_id, seed):
    with _lock:
        return _seam.serve(run_id, seed)
```
— NO: the direct form, one `with _lock:` per body wrapping the Serialize window whole (the flock outermost, the Serialize threading.Lock within — flock -> lock -> load -> act -> save, released before rendering; the render of the result happens AFTER the with-block exits, the lock never held across rendering). Each tool body: `with _lock: result_or_raise = the seam call` then render OUTSIDE the with. The caught typed exceptions (StoreRefusedError/VotesRefusedError/TallyRefusedError/ExhaustedQueue) ride through BY TYPE from inside the with — the with's __exit__ releases the flock on the exception path BY CONSTRUCTION (the context manager's own law).

(i) THE __MAIN__ BLOCK (the tree's first; the brief §4's two run forms):
```python
def main() -> None:
    """Run the server -- bare stdio, --serve the shared HTTP form."""
    if "--serve" in sys.argv[1:]:
        server.run("http", host="127.0.0.1", port=8000, allowed_hosts=["127.0.0.1", "localhost"], allowed_origins=[])
    else:
        server.run("stdio")

if __name__ == "__main__":
    main()
```
The flag's name per the naming law: the act-statement "Serve the tools over streamable HTTP rather than stdio" — the first word the symbol: `--serve`. The parsing form (the brief's open question): the bare `sys.argv` membership check — argparse DECLINED (the tree's CLI precedent weighs for argparse, but a single boolean flag with no other argv surface is argparse's ceremony over a one-token check; the no-shell law holds; the flag's help rides the module docstring). The exact `server.run("http", ...)` kwarg set per the census:22 — verified at the build's first step. The host/port/allowed forms the lifecycle unit's to widen; the defaults land the shared form's server side honestly.

## 3. THE COMPOSITION REGIONS — the exact hunks

(a) service_store.py — SIX VERB HEADS, the file-lock-outermost form: each `with self._lock:` becomes `with store_lock.Lock(self._store_home), self._lock:` — NO: the clean hunk, ONE import + six with-line edits:

- HEAD: `from prioritree.store_lock import Lock` added to the imports (the stdlib-tier import after the Persist import).
- Each verb's head, e.g. register :118-119 BEFORE:
```python
        with self._lock:
            return Persist.register(self._store_home, items, operator, quorum).run_id
```
AFTER:
```python
        with Lock(self._store_home), self._lock:
            return Persist.register(self._store_home, items, operator, quorum).run_id
```
(the flock acquired FIRST, the threading.Lock within — the reverse priced and declined, the brief §3 clause (a); no ABBA either way.) The same one-line edit at serve :139-140, cast :168-171, census :189-190, rank :208-209, manifest :233-234. The Lock object is per-acquisition (the path derivation is trivial; a held-instance would add process state for nothing — the per-act construction is the honest form; the docstrings' clause lines updated to name the file lock outermost).

(b) cli.py — FIVE HANDLER WINDOWS, the flock covering load+verb together:

- HEAD: `from prioritree.store_lock import Lock` added.
- register :202-207 — the Persist.register whole wrapped: `with Lock(home): persist = Persist.register(...)` where `home = cast("Path", args.home)` hoisted above the with.
- next :228-229 — `with Lock(home): persist = Persist.load(home, run_id); item_a, item_b, count = persist.serve(seed)` (the load+serve window whole).
- vote :251-259 — `with Lock(home):` wrapping the load+cast whole (the save rides INSIDE Persist.cast — run_store.py:797-823 — the window closed by construction).
- state :282-283 — `with Lock(home): persist = Persist.load(...); census = persist.census()`.
- tally :308-309 — `with Lock(home): persist = Persist.load(...); result = persist.rank()` (the render of the ranked whole happens OUTSIDE the with — the report loop below, released before rendering).
Each handler's docstring clause line names the wrap (the one-sentence amendment per handler, no restructure).

(c) THE PER-FILE LINT RULINGS if any new fires ride: each a pyproject per-file-ignores entry PER FIRE ONLY, citing this spec + G-MCPSERVERSPEC-BRIEF, the retires-when named — predicted candidates: store_lock.py (PYI/SLF-class on the private _handle, PTH-class on the path open if it fires — each named at the actual fire, never pre-ignored), mcp_server.py (PLR0913 on a tool body's arity if any, the D-class on the docstring VERBATIMs if a pydocstyle fire demands — the descriptions are the acceptance, never deleted to quiet a linter; a fire is a NAMED ruling), tests/test_store_lock_face.py + tests/test_mcp_server_face.py (S603/S607 the Popen/probe ruling re-carried, the test_harness/test_service_acceptance precedent). The zero-ignore bar stands — an ignore is a ruling, never a convenience.

## 4. THE DEP LINE

- pyproject.toml:7 BEFORE: `dependencies = ["fastapi", "httpx2", "jinja2", "python-multipart", "uvicorn[standard]"]` AFTER: `dependencies = ["fastapi", "httpx2", "jinja2", "ouncemcp", "python-multipart", "uvicorn[standard]"]` — the sorted position (h-o-p: httpx2 < jinja2 < ouncemcp < python-multipart, alphabetical holds).
- The lock regen rides the floor's first `uv run` (the standing fold form — the first `uv run pytest`/`uv run ruff` regenerates uv.lock; the 38th package entry lands).
- THE INSTALL-VERIFICATION AS THE BUILD'S FIRST CHECK: `uv run python -c "import ouncemcp"` — green before any other step's dispatch; then the import-verification pass (OunceServer, Effect, the error-value class, server.run's kwargs, result_tokens/budget_reason kwargs, as_caller — each verified against the installed package, the census's memory never trusted alone once the dep lands; a divergence is a finding reported at the step's return, never silently absorbed).
- NO dev-group change (pytest/pyright/ruff stand; ouncemcp.testing rides the runtime package).

## 5. THE TEST FILES WHOLE

(a) tests/test_store_lock_face.py — THE FLOCK'S OWN ARC (the seam unit + the two-process probe, the fixed-argv Popen form per test_service_acceptance.py:41-54):

- The seam unit arcs (in-process): the lockfile created on demand at the home (exists after __enter__, absent before); NEVER truncated (a file pre-seeded with sentinel bytes at the lock path keeps its bytes after a lock/unlock cycle — the inode law's own probe); exclusivity (a second Lock on the same home blocks: a Popen child holding the lock, the parent's acquisition bounded-wait observed green after the child's release; the bounded-wait form: the child holds 1s, the parent's enter returns after — a timing assertion with a floor, never a ceiling-skip); release at exit (a with-block's exit frees a second acquisition immediately); the home-injection derivation (two homes, two lock paths — the injected home is the lock's own ground, never re-defaulted).
- THE TWO-PROCESS PROBE (G-MCPSERVER's condition 2, the honest concurrency state): TWO PROCESSES ON ONE STORE — the fixed-argv Popen: the child process = `sys.executable` + `-c` + a fixed in-source program string (the no-shell law: the fixed-argv list, S603/S607 the named per-file ruling re-carried) that registers a run and casts N votes on a shared tmp store home; the parent concurrently casts M votes on the SAME store via Persist. THE ASSERTIONS: the mint-order load green (both processes' casts landed, the file loads clean — no "no gaps, no dups" refusal); the torn-tail refusal ABSENT (the load's pre-pass never fires the crash-tail refusal on the healthy run). Interleaved: the child's votes and the parent's votes both counted in a final census (total = N + M).
- The compositions probed: a CLI-subprocess write beside an in-process write (the child = the console script or `python -m` with the register/vote argv — the fixed-argv form, the store shared); a service-verb write beside (Serialize.register + Persist.register concurrently on one home — both runs mint distinct stems, no half-write seen).
- ~10-12 tests.

(b) tests/test_mcp_server_face.py — THE TOOLS' ARCS via OunceMCP's proof tooling (the census:24 — `ouncemcp.testing.as_caller`: the caller-side harness; the import form verified at the build's first step):

- THE FIVE ARCS END-TO-END (register -> next -> cast -> census -> tally, the halt's exit included): each tool's success form asserted field-for-field (register's ack {run_id: "RUN-0001", count, quorum, verdicts}; next's pair triple + the done=true terminal; cast's ack; census's {total, items}; tally's TallyView whole at full coverage — three items, three prefer-a votes, the ranked whole hand-computable — the test_service_face literals carried 1:1).
- THE STRUCTURED ERROR ASSERTIONS: the ThreePart fields {expected, found, next_action} asserted AS DATA at every refusal surface (the unknown run at next/census/tally; the out-of-set verdict at cast; the unknown class refused at the SCHEMA — the Literal's own gate — AND gated at the core: both legs asserted, the schema leg via the caller's validation error carrying the typed form, the core leg via a cast on a corrupted-class path where the schema passes and the core refuses).
- DONE A VALUE NEVER AN ERROR: next's exhausted return carries done=true as a RESULT, the three fields populated, no error raised.
- THE HALT'S CAPPED RENDER: at n items under quorum with MORE than 10 under-quorum pairs (n=6: 15 pairs, 15 > 10), the refusal's found/next_action carry the elision named ("15 under-quorum pairs total; first 10 shown"), legs 1-2 whole; the three fields present as data.
- THE IDEMPOTENCY REPLAY ARCS: cast's byte-identical re-send => acknowledged=true, the count UNCHANGED, the vote_id the ORIGINAL's; the fresh cast => acknowledged=false, the count grown by one; register's cross-session re-register (a fresh as_caller store) mints a NEW run (the ack's run_id the guard — RUN-0002).
- THE STAMPS' SCHEMA GATES: comparator_class outside {human, llm} refused at the schema (the pattern's own gate); the stamps present on every cast.
- THE VERDICTS ECHO: register's ack.verdicts == ["prefer-a", "prefer-b", "tie"] (sorted).
- SUPERSEDES' CORRECTION: a cast with supersedes=VOTE-0001 on the same pair lands; a supersedes on a different pair refused (the ThreePart).
- THE SEED'S STABILITY: next with the same seed twice between casts serves the same pair; the default order stable per run.
- THE ELISIONS HONEST: census's body exactly {total, items} (per_pair_counts and vote_log absent); tally's coverage carries pairs_expected/pairs_at_quorum, pair_counts ABSENT.
- ~28-32 tests. The isolation: a fresh tmp store home per test via the module's own injection seam — the tests overwrite the module's `_seam`/`_lock` (the service-face fixture precedent: the module-level objects re-minted per test, the STORE_HOME default never touched on disk).

## 6. THE NO-BREAK PROOFS

- THE CORE'S FIVE OPS UNTOUCHED: session.py:161-318 wrapped, never edited; zero edits to run_store.py, votes.py, tally.py, registry.py, scheduler.py (the service_store precedent's fence re-carried).
- THE 156 FLOOR HELD: the existing 15 test files untouched; the ~40 new arcs landing green; `uv run pytest` = 156 + new, zero failures.
- THE SIX JSON ROUTES BYTE-STABLE: service.py:321-490 unedited (the service composition touches Serialize's verb heads ONLY — the routes' outputs byte-identical at every existing render; the test_service_face suite green is the proof).
- THE CLI'S RENDERS BYTE-IDENTICAL: the wraps transparent; the test_harness e2e green.
- THE OUNCEMCP CHECK AS FLOOR-ADJACENT GATE EVIDENCE: `uv run ouncemcp check src/prioritree/mcp_server.py` (the census's own form) run at the floor-green step + re-run by kensho at validate/mcp-server — NAMED as gate evidence in the step's return, NEVER a Makefile edit (the standing targets unedited — the lifecycle targets the lifecycle unit's own).

## 7. THE PER-STEP DISPATCH PLAN (R8 — one step, one dispatch, one bounded return; the read-backs named per step; the commit at the coordinator's hand)

STEP 1 — THE DEP + THE SYNC-CHECK: pyproject's dep line + the lock regen (the first uv run) + the install-verification (`uv run python -c "import ouncemcp"`) + the import-verification pass (every ouncemcp form this spec cites verified against the installed package; divergences reported at the return). READ-BACK: pyproject.toml:7 + uv.lock's ouncemcp entry + the verification's output. Executor: jikko.
STEP 2 — THE SEAM MODULE: store_lock.py whole (§1). READ-BACK: the file + `uv run ruff check src/prioritree/store_lock.py` + `uv run pyright` clean at the new file. Executor: jikko.
STEP 3 — THE TWO COMPOSITIONS: service_store.py's six heads + cli.py's five windows (§3) + the per-file rulings if fires ride. READ-BACK: the twelve hunks + `uv run pytest` (the 156 floor green — the compositions behavior-transparent). Executor: jikko.
STEP 4 — THE MCP MODULE: mcp_server.py whole (§2) + any named rulings. READ-BACK: the file + the ouncemcp check zero-findings + the definitions under the 500 warn (the budget_reasons carried). Executor: jikko.
STEP 5 — THE TEST FILES: test_store_lock_face.py + test_mcp_server_face.py whole (§5) + the S603/S607 rulings. READ-BACK: the two files + the new arcs' green. Executor: jikko.
STEP 6 — THE FLOOR: `uv run pytest` (the whole ~196 green), `uv run ruff check src/ tests/` zero findings, `uv run pyright` 0/0, the ouncemcp check re-run. READ-BACK: the four outputs whole. Executor: jikko.
STEP 7 — THE LIVE CHECKS AT THE GATE: kensho's independent re-run (validate/mcp-server — the zero-trust verification: the R9 semantics cross-session, the ThreePart at every refusal, the done/halt strictly binary, the stamps' both legs, the elisions honest, the floor-adjacent ouncemcp check) + moho's implementation walk (walk/mcp-server — the uninstructed live journey over the five tools end-to-end, the ease-of-use findings riding G-MCPSERVER as evidence; the dispatch names the surface's address, NEVER the sequence). READ-BACK: both packets' reports. Executors: kensho, moho (separate dispatches).

The commit at the coordinator's hand (shinko) — no seat commits.

## 8. THE OPEN QUESTIONS RESOLVED HERE (the brief §7's list, ruled)

(1) The seam module's file name: store_lock.py (the noun_noun grammar, the service_store/run_store precedent — confirmed). (2) NextOutcome's exact shape: ONE model, done the boolean tag, the empty-string defaults (the union form declined — the client's parse never forks). (3) TallyView's coverage names: pairs_expected/pairs_at_quorum (landed against CoverageDatum's ground — pairs_expected = the full schedule's size, pairs_at_quorum = the weighted count at quorum). (4) The --serve flag's parsing: the bare sys.argv membership check (argparse's ceremony declined for a one-token flag). (5) The OunceServer's constructor: OunceServer(name="prioritree") (the census's form; the Budget override absent — 1,005 = 25% of the default); the module's __all__ symbol: server. (6) The ouncemcp check's invocation: `uv run ouncemcp check src/prioritree/mcp_server.py`. (7) The per-file-ignores: per-fire only, §3(c)'s candidates named, never pre-ignored. (8) The walk packet's id: walk/mcp-server.

## 9. THE TRADE-OFF THE PLAN MUST CARRY

The concurrency cure widens this unit's fence into service_store.py + cli.py (twelve composition hunks beyond the two new modules) — the seam must cover EVERY standing writer or it is no cure; a lock one writer takes is no lock. The cost: the wider review surface, kensho's probe spanning all three compositions. The declined alternatives priced and standing: the single-writer deployment form (F1's five reasons) and the separate store-lock unit (ceremony over wholeness). The second trade-off: the MCP tier's register elides the label (items as bare ids, label=id) — the tool tier's narrow-interface doctrine against the door's [id, label] pairs; the CLI and service keep their full form; the divergence named here, never silent.

READY TO BUILD at the collaborator's approval — the bytes whole over the approved briefs, the seven steps named, the no-break proofs carried.
