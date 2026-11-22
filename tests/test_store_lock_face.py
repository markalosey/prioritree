# Copyright (C) 2026 Mark Losey. All rights reserved.
"""test_store_lock_face — the flock's own face: the lock seam probed whole.

The mcp-server unit's lock-seam test surface (the exact-task spec
reports/synthesize/mcpserverspec.md SS5(a), the step-5b fence): ten arcs over
the machine-wide lock seam (store_lock.Lock) — the seam unit's in-process
probes (the lockfile created on demand at the injected home, never truncated;
the home-injection derivation, two homes two lock paths; the release at the
with-block's exit; the reentrant second open — two Lock opens on one path
from one process, the second BLOCKS until the first releases, the flock bound
per open file description; the exclusivity block observed as a bounded wait
behind a Popen child's hold); the two-process probe (the fixed-argv Popen
child casting N votes beside the parent's M on one shared store — the
mint-order load green, the torn-tail refusal absent, the census total N+M);
the composition probes (the CLI-subprocess register beside the in-process
register; the service verb beside the core register — both runs mint
distinct stems, no half-write seen); the never-deleted law (the lockfile
present after the acts — the inode law's own probe). The no-shell law
honored: every Popen a fixed-argv LIST (sys.executable + "-c" + the fixed
in-source program strings, the console script at its full venv path; the
S603/S607 per-file entry rides pyproject; the S101/PLR2004 tests ruling
stands). The honest count: 10 test functions.
"""

from __future__ import annotations

import sys
from pathlib import Path
from subprocess import PIPE, Popen, TimeoutExpired
from threading import Thread
from time import monotonic, sleep
from typing import Final

from prioritree.registry import OperatorDeclaration
from prioritree.run_store import Persist
from prioritree.service_store import Serialize
from prioritree.store_lock import Lock

# The lockfile's name (the seam's own constant, re-carried for the assertions).
_LOCK_FILE_NAME: Final[str] = ".prioritree.lock"
# The register payload's shared question (the parents' and the child programs').
_QUESTION: Final[str] = "Which matters more?"
# The fresh home's first stem (the two-process probe's shared ground).
_RUN_ID: Final[str] = "RUN-0001"
_SECOND_RUN_ID: Final[str] = "RUN-0002"
_STEMS: Final[frozenset[str]] = frozenset({_RUN_ID, _SECOND_RUN_ID})
# The two-process probe's cast counts: the child's N beside the parent's M.
_CHILD_CASTS: Final[int] = 4
_PARENT_CASTS: Final[int] = 3
# The pair cycle both probe writers cast over (the three items' schedule).
_PAIRS: Final[tuple[tuple[str, str], ...]] = (("a", "b"), ("a", "c"), ("b", "c"))
# The vote payload constants (the core's own vocabulary).
_PREFER_A: Final[str] = "prefer-a"
_HUMAN: Final[str] = "human"
# The never-truncated arc's sentinel bytes.
_SENTINEL: Final[str] = "the inode is the lock's identity\n"
# The child programs' stdout markers (the parent reads them as bytes).
_HELD_MARKER: Final[str] = "held"
_DONE_MARKER: Final[str] = "done"
# The exclusivity arc's timing (the spec's bounded-wait form: the child holds
# _HOLD_SECONDS; the parent's acquisition observed AFTER — a timing assertion
# with a FLOOR, never a ceiling-skip: an unblocked enter returns in
# milliseconds and fails the floor).
_HOLD_SECONDS: Final[float] = 1.0
_FLOOR_SECONDS: Final[float] = 0.5
# The release arc's generous ceiling (the second acquisition immediate: no
# residual holder; generous for CI jitter, tight against a deadlock residue).
_IMMEDIATE_SECONDS: Final[float] = 5.0
# The child drain and the joins (the acceptance precedent's bounds).
_DRAIN_SECONDS: Final[float] = 5.0
_JOIN_SECONDS: Final[float] = 15.0
# The CLI child's success exit (the command face's own EXIT_OK).
_EXIT_OK: Final[int] = 0
# The console script's FULL path (the harness precedent's sibling form).
_SHIM: Final[Path] = Path(sys.executable).parent / "prioritree"

# The hold child (the exclusivity arc): acquire, print the marker the instant
# the hold begins, hold the named seconds, exit.
_HOLD_CHILD: Final[str] = f"""import sys
import time
from pathlib import Path

from prioritree.store_lock import Lock

lock = Lock(Path(sys.argv[1]))
with lock:
    print('{_HELD_MARKER}', flush=True)
    time.sleep({_HOLD_SECONDS})
"""

# The cast child (the two-process probe): register one run under the lock,
# print its stem, then cast N votes — each act whole under the lock (the
# composition's own form: the register's mkdir-scan-mint-write, then per cast
# the load+cast window).
_CAST_CHILD: Final[str] = f"""import sys
from pathlib import Path

from prioritree.registry import OperatorDeclaration
from prioritree.run_store import Persist
from prioritree.store_lock import Lock

home = Path(sys.argv[1])
casts = int(sys.argv[2])
lock = Lock(home)
items = [['a', 'a'], ['b', 'b'], ['c', 'c']]
operator = OperatorDeclaration(id='op-child', question='{_QUESTION}')
with lock:
    run_id = Persist.register(home, items, operator).run_id
print(run_id, flush=True)
pairs = {_PAIRS}
for index in range(casts):
    with lock:
        Persist.load(home, run_id).cast(pairs[index % len(pairs)], 'prefer-a', f'child-{{index}}', 'human')
print('{_DONE_MARKER}', flush=True)
"""


def _reap(process: Popen[bytes]) -> None:
    """Reap the child: terminate, drain the graceful wait, kill the backstop.

    Purpose: the teardown half of every Popen arc — terminate() (a no-op when
    the child was already waited: Popen's own returncode guard sends nothing),
    wait the _DRAIN_SECONDS graceful drain, kill() + wait the backstop on
    TimeoutExpired (the acceptance precedent's form), close the stdout pipe.
    Refuses when: never — the teardown always runs (the finally owns it); a
    dead child is a closed book, a live one is stopped.
    Re-run: deterministic — a reaped child is fully waited and its pipe closed.
    Touches: the child's process entry and the stdout pipe alone.
    Provenance: test_service_acceptance.py:167-173 (the drain-then-backstop
    form), the spec SS5(a) (the probe arcs' teardown).
    """
    process.terminate()
    try:
        process.wait(timeout=_DRAIN_SECONDS)
    except TimeoutExpired:
        process.kill()
        process.wait(timeout=_DRAIN_SECONDS)
    if process.stdout is not None:
        process.stdout.close()


def test_create_the_lockfile_on_demand(tmp_path: Path) -> None:
    """Create the lockfile on demand at the injected home — absent before, present at __enter__.

    Purpose: the seam's own first law — the lockfile is CREATED ON DEMAND:
    absent before any acquisition (the fresh home carries no lock file),
    present the instant __enter__ opens it (the "a" create-if-absent form —
    the home's own mkdir riding the enter, the register precedent's
    create-if-absent law).
    Refuses when: the lockfile exists before the enter, or fails to exist at
    the enter — the two-sided assertion, both directions named.
    Re-run: deterministic — a fresh tmp home per test (pytest's tmp_path),
    the same derivation each run.
    Touches: the tmp home's tree alone (the mkdir + the lockfile).
    Provenance: the spec SS5(a) (the created-on-demand arc), store_lock.py:6-8
    (the created-on-demand clause), G-MCPSERVER.
    """
    home = tmp_path / "store"
    lock_path = home / _LOCK_FILE_NAME
    assert not lock_path.exists()
    with Lock(home):
        assert lock_path.exists()


def test_preserve_the_preseeded_lockfile_bytes(tmp_path: Path) -> None:
    """Preserve the preseeded lockfile's bytes across a lock/unlock cycle — never truncated.

    Purpose: the inode law's own probe — the lockfile is opened "a"
    (create-if-absent, NEVER truncated: the file's bytes are nobody's, the
    INODE is the lock's identity); a file preseeded with sentinel bytes at
    the lock path keeps its bytes whole across a full lock/unlock cycle.
    Refuses when: the sentinel diverges after the cycle — a truncated or
    rewritten lockfile fails the equality (the "w" form would zero it; the
    probe catches exactly that regression).
    Re-run: deterministic — the same sentinel, the same cycle, the same bytes.
    Touches: the tmp home's lockfile alone.
    Provenance: the spec SS5(a) (the never-truncated arc), store_lock.py:40-44
    (the docstring's own clause), G-MCPSERVER.
    """
    home = tmp_path / "store"
    home.mkdir()
    lock_path = home / _LOCK_FILE_NAME
    lock_path.write_text(_SENTINEL, encoding="utf-8")
    with Lock(home):
        pass
    assert lock_path.read_text(encoding="utf-8") == _SENTINEL


def test_derive_the_lock_path_from_the_injected_home(tmp_path: Path) -> None:
    """Derive the lock path from the injected home — two homes, two lock paths, never re-defaulted.

    Purpose: the home-injection law — the lock path DERIVES from the injected
    home ({store_home}/.prioritree.lock), never from any module default: two
    homes probed in one test, the first home's enter creates ITS lockfile and
    never the second's; the second's enter creates its own — the
    hidden-global drift refused at the seam's own tier.
    Refuses when: the first home's lockfile appears under the second home, or
    the second home's enter fails to mint its own — both directions asserted.
    Re-run: deterministic — the derivation is pure (the home in, the path out).
    Touches: the two tmp homes' lockfiles alone.
    Provenance: the spec SS5(a) (the home-injection arc), store_lock.py:58-75
    (the __init__ derivation, the never-re-defaulted clause), G-MCPSERVER.
    """
    home_one = tmp_path / "one"
    home_two = tmp_path / "two"
    with Lock(home_one):
        assert (home_one / _LOCK_FILE_NAME).exists()
        assert not (home_two / _LOCK_FILE_NAME).exists()
    with Lock(home_two):
        assert (home_two / _LOCK_FILE_NAME).exists()


def test_release_the_lock_at_the_with_block_exit(tmp_path: Path) -> None:
    """Release the lock at the with-block's exit — the second acquisition immediate.

    Purpose: the exit's own law — __exit__ releases the flock and closes the
    handle; a second Lock on the same home acquired AFTER the first
    with-block's exit completes immediately (no residual holder, no
    re-acquire ceremony): the elapsed acquisition bounded by the generous
    _IMMEDIATE_SECONDS ceiling — generous for CI jitter, tight against a
    deadlock-adjacent residue.
    Refuses when: the second acquisition stalls past the ceiling — a leaked
    holder from the first block fails the timing bound.
    Re-run: deterministic — the cycle is pure enter/exit.
    Touches: the tmp home's lockfile alone (two cycles).
    Provenance: the spec SS5(a) (the release-at-exit arc), store_lock.py:86-91
    (the __exit__ law), G-MCPSERVER.
    """
    home = tmp_path / "store"
    with Lock(home):
        pass
    started = monotonic()
    with Lock(home):
        pass
    elapsed = monotonic() - started
    assert elapsed < _IMMEDIATE_SECONDS


def test_serialize_the_reentrant_second_open(tmp_path: Path) -> None:
    """Serialize the reentrant second open — two Lock opens on one path, the second blocks until the first releases.

    Purpose: the reentrancy question's arc — the fence's ruled behavior
    ("re-entry serializes: a second holder blocks until the first releases"):
    the flock binds the OPEN FILE DESCRIPTION, not the process, so two Lock
    objects opening the same path CONFLICT within one process — the main
    thread holds the first open, a second thread's open blocks through the
    _FLOOR_SECONDS window (the block OBSERVED, not assumed), the first's
    exit grants the second (the join's bound the backstop against a
    deadlock).
    Refuses when: the second open grants while the first holds (the lock
    would be per-process, no serialization) or never grants after the release
    (a deadlock at the exit) — both directions asserted.
    Re-run: deterministic in shape — the interleaving's ORDER ruled by the
    fence, only the timing's noise free.
    Touches: the tmp home's lockfile alone (two opens, one at a time).
    Provenance: the spec SS5(a) (the seam unit's arcs) + the dispatch's
    reentrancy clause, store_lock.py:47-49 (the docstring's re-entry
    serialization clause), G-MCPSERVER.
    """
    home = tmp_path / "store"
    grants: list[bool] = []

    def _second_open() -> None:
        """Open the second Lock on the same path; record the grant inside the hold."""
        with Lock(home):
            grants.append(True)

    with Lock(home):  # the first open holds
        thread = Thread(target=_second_open)
        thread.start()
        sleep(_FLOOR_SECONDS)  # the window the second open must spend blocked
        assert not grants  # still blocked: two opens CONFLICT within one process
    thread.join(timeout=_JOIN_SECONDS)
    assert not thread.is_alive()  # granted at the release — never deadlocked
    assert grants  # the second holder entered after the first's exit


def test_block_the_second_holder_until_the_first_releases(tmp_path: Path) -> None:
    """Block the second holder until the first releases — a Popen child's hold, the parent's bounded wait.

    Purpose: the basic exclusion across processes — the fixed-argv Popen child
    (sys.executable + "-c" + the fixed _HOLD_CHILD program) acquires the lock
    and holds it _HOLD_SECONDS, printing its marker the instant the hold
    begins; the parent reads the marker (the child holds NOW), then enters
    its own Lock on the same home — the enter BLOCKS until the child's
    release, the elapsed wait observed against the _FLOOR_SECONDS FLOOR (a
    timing assertion with a floor, never a ceiling-skip: an unblocked enter
    returns in milliseconds and fails the floor). The child reaped in the
    finally (the drain-then-backstop form).
    Refuses when: the child's marker fails to arrive (the child never held),
    the parent's wait lands under the floor (the lock did not span
    processes), or the child's exit code is not _EXIT_OK.
    Re-run: deterministic — the child's program fixed in-source, the hold a
    named constant, only the scheduler's noise free.
    Touches: the tmp home's lockfile (both processes) and the child's process
    entry.
    Provenance: the spec SS5(a) (the exclusivity arc),
    test_service_acceptance.py:41-54 (the fixed-argv Popen precedent),
    G-MCPSERVER.
    """
    home = tmp_path / "store"
    process = Popen([sys.executable, "-c", _HOLD_CHILD, str(home)], stdout=PIPE)
    try:
        assert process.stdout is not None
        held_line = process.stdout.readline()
        assert held_line == f"{_HELD_MARKER}\n".encode()  # the child holds NOW
        started = monotonic()
        with Lock(home):
            pass
        elapsed = monotonic() - started
        assert elapsed >= _FLOOR_SECONDS  # the bounded wait's floor: the enter blocked
        process.wait(timeout=_JOIN_SECONDS)
        assert process.returncode == _EXIT_OK
    finally:
        _reap(process)


def test_probe_two_processes_on_one_store(tmp_path: Path) -> None:
    """Probe two processes on one store — the child's N casts beside the parent's M, the whole landed clean.

    Purpose: G-MCPSERVER's condition 2, the honest concurrency state — the
    fixed-argv Popen child registers one run and casts _CHILD_CASTS votes on
    the shared tmp home (each act whole under the lock: the register's
    mkdir-scan-mint-write, then per cast the load+cast window); the parent,
    released by the child's stem line, casts _PARENT_CASTS concurrently on
    the SAME store (each act under the lock, the composition's own form).
    THE ASSERTIONS: the final load GREEN (the mint-order load — the pre-pass
    refuses a gap, a dup, or a torn tail: the load's success IS the absence
    of both "no gaps, no dups" and the crash-tail refusal on the healthy
    run); the census total N+M; the vote-id set exactly VOTE-0001..
    VOTE-{N+M} contiguous (the mints never collided); both processes'
    comparator ids present in the log.
    Refuses when: the child's stem line fails to arrive (the child never
    registered), the load raises (a torn tail or a mint collision — the
    unserialized writes caught), the total lands short (a lost cast) or the
    ids fork (a doubled mint), or the child's exit code is not _EXIT_OK.
    Re-run: deterministic in AGGREGATE — the interleaving nondeterministic by
    construction, the flock serializes the acts, the totals order-invariant.
    Touches: the shared tmp home (both processes' acts) and the child's
    process entry.
    Provenance: the spec SS5(a) (the two-process probe), G-MCPSERVER condition
    2, test_service_acceptance.py:368-436 (the aggregate-only precedent).
    """
    home = tmp_path / "store"
    process = Popen(
        [sys.executable, "-c", _CAST_CHILD, str(home), str(_CHILD_CASTS)],
        stdout=PIPE,
    )
    try:
        assert process.stdout is not None
        run_line = process.stdout.readline()
        assert run_line == f"{_RUN_ID}\n".encode()  # the child registered the shared run
        for index in range(_PARENT_CASTS):
            with Lock(home):
                Persist.load(home, _RUN_ID).cast(
                    _PAIRS[index % len(_PAIRS)],
                    _PREFER_A,
                    f"parent-{index}",
                    _HUMAN,
                )
        done_line = process.stdout.readline()
        assert done_line == f"{_DONE_MARKER}\n".encode()  # the child's casts all landed
        process.wait(timeout=_JOIN_SECONDS)
        assert process.returncode == _EXIT_OK
        census = Persist.load(home, _RUN_ID).census()  # the mint-order load GREEN
        total = _CHILD_CASTS + _PARENT_CASTS
        assert len(census.vote_log) == total
        assert {record.vote_id for record in census.vote_log} == {
            f"VOTE-{number:04d}" for number in range(1, total + 1)
        }
        expected_comparators = {f"child-{number}" for number in range(_CHILD_CASTS)}
        expected_comparators |= {f"parent-{number}" for number in range(_PARENT_CASTS)}
        assert {record.comparator_id for record in census.vote_log} == expected_comparators
    finally:
        _reap(process)


def test_probe_the_cli_subprocess_beside_the_in_process_register(tmp_path: Path) -> None:
    """Probe the CLI-subprocess register beside the in-process register — distinct stems, no half-write.

    Purpose: the composition probe at the CLI tier — the console script at
    its full venv path (the _SHIM sibling form, the harness precedent)
    registers a run on the shared home through the CLI's own flock window
    (cli.py:206-212, the landed composition); the parent concurrently
    registers its own run in-process under the seam: both writers through
    the one machine-wide lock, the mkdir-scan-mint-write TOCTOU closed by
    construction. THE ASSERTIONS: the child's exit _EXIT_OK with its bare
    stem on stdout; the two stems exactly _STEMS as a SET (the arrival order
    never asserted); both manifests load green with their own items and
    operator intact (the load's pre-pass green IS the no-half-write proof).
    Refuses when: the child fails, the stems collide (the TOCTOU reopened),
    or either manifest's fields diverge (a half-write seen).
    Re-run: deterministic in AGGREGATE — the set the claim, the arrival free.
    Touches: the shared tmp home (both registers' files, the lockfile) and
    the child's process entry.
    Provenance: the spec SS5(a) (the CLI-subprocess composition probe),
    test_harness.py:25-27 (the _SHIM precedent), G-MCPSERVER.
    """
    home = tmp_path / "store"
    child_argv = [
        str(_SHIM),
        "register",
        "a:alpha",
        "b:beta",
        "--operator-id",
        "op-cli",
        "--question",
        _QUESTION,
        "--home",
        str(home),
    ]
    process = Popen(child_argv, stdout=PIPE)
    try:
        assert process.stdout is not None
        with Lock(home):
            parent_stem = Persist.register(
                home,
                [["a", "alpha"], ["b", "beta"]],
                OperatorDeclaration(id="op-parent", question=_QUESTION),
            ).run_id
        process.wait(timeout=_JOIN_SECONDS)
        assert process.returncode == _EXIT_OK
        child_stem = process.stdout.read().decode("utf-8").strip()
        assert {parent_stem, child_stem} == _STEMS
        parent_manifest = Persist.load(home, parent_stem).manifest()
        child_manifest = Persist.load(home, child_stem).manifest()
        assert [row.id for row in parent_manifest.items] == ["a", "b"]
        assert parent_manifest.operator.id == "op-parent"
        assert [row.id for row in child_manifest.items] == ["a", "b"]
        assert child_manifest.operator.id == "op-cli"
    finally:
        _reap(process)


def test_probe_the_service_verb_beside_the_core_register(tmp_path: Path) -> None:
    """Probe the service verb beside the core register — Serialize.register + Persist.register, distinct stems.

    Purpose: the composition probe at the service tier — a thread registers
    through the Serialize seam (the flock taken INSIDE the verb, the
    threading.Lock within), while the main line concurrently registers
    through Persist wrapped in the seam's own Lock: two writers, one home,
    the flock outermost on both sides. THE ASSERTIONS: the two stems exactly
    _STEMS as a SET (the arrival order never asserted); both manifests load
    green with their own items and operator intact (the load's pre-pass
    green IS the no-half-write proof); the thread joined within the bound
    (a hung verb fails loudly).
    Refuses when: the stems collide (the register acts interleaved
    unserialized), either manifest diverges, or the thread never joins.
    Re-run: deterministic in AGGREGATE — the set the claim, the arrival free.
    Touches: the shared tmp home (both registers' files, the lockfile).
    Provenance: the spec SS5(a) (the service-verb composition probe),
    service_store.py:125-126 (the flock-outermost verb head), G-MCPSERVER.
    """
    home = tmp_path / "store"
    seam = Serialize(home)
    outcome: dict[str, str] = {}

    def _seam_register() -> None:
        """Register through the seam's own verb — the flock taken inside the verb."""
        outcome["stem"] = seam.register(
            [["b", "beta"], ["c", "gamma"]],
            OperatorDeclaration(id="op-service", question=_QUESTION),
        )

    thread = Thread(target=_seam_register)
    thread.start()
    with Lock(home):
        core_stem = Persist.register(
            home,
            [["a", "alpha"], ["b", "beta"]],
            OperatorDeclaration(id="op-core", question=_QUESTION),
        ).run_id
    thread.join(timeout=_JOIN_SECONDS)
    assert not thread.is_alive()
    seam_stem = outcome.get("stem")
    assert seam_stem is not None
    assert {seam_stem, core_stem} == _STEMS
    seam_manifest = Persist.load(home, seam_stem).manifest()
    core_manifest = Persist.load(home, core_stem).manifest()
    assert [row.id for row in seam_manifest.items] == ["b", "c"]
    assert seam_manifest.operator.id == "op-service"
    assert [row.id for row in core_manifest.items] == ["a", "b"]
    assert core_manifest.operator.id == "op-core"


def test_keep_the_lockfile_after_the_acts(tmp_path: Path) -> None:
    """Keep the lockfile after the acts — the file present, never deleted.

    Purpose: the never-deleted law's arc — after the full round of acts (the
    service seam's register and census, the in-process cast under the lock,
    two bare enter/exit cycles), the lockfile still STANDS at the home: this
    hand never unlinks it (flock binds the inode; a deleted lockfile is a
    NEW lock — the cure collapsing at the first unlink — the inode law
    carried in the assertions, not just the docstrings).
    Refuses when: the lockfile is absent after any act — a deletion at the
    enter, the exit, or the verbs' windows fails the presence.
    Re-run: deterministic — the acts are the tree's own verbs, the presence
    their only side effect probed here.
    Touches: the tmp home's run file and lockfile (the acts' own writes).
    Provenance: the spec SS5(a) (the never-deleted arc), store_lock.py:6-8
    (the module docstring's inode law), G-MCPSERVER.
    """
    home = tmp_path / "store"
    seam = Serialize(home)
    run_id = seam.register([["a", "a"], ["b", "b"]], OperatorDeclaration(id="op-keep", question=_QUESTION))
    assert (home / _LOCK_FILE_NAME).exists()  # after the register act
    with Lock(home):
        Persist.load(home, run_id).cast(_PAIRS[0], _PREFER_A, "keeper", _HUMAN)
    seam.census(run_id)
    lock_path = home / _LOCK_FILE_NAME
    assert lock_path.exists()  # after the cast and census acts
    with Lock(home):
        pass
    with Lock(home):
        pass
    assert lock_path.exists()  # after the bare cycles — NEVER deleted
