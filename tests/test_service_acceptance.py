# Copyright (C) 2026 Mark Losey. All rights reserved.
"""test_service_acceptance — the service accepted over the real socket, e2e.

The service-acceptance unit's test surface (service-acceptance-brief §1-§7 +
the ux build's sixth query + ThreePart cures): six arcs over a live uvicorn
subprocess — the eleven-request arc (register => manifest => next => vote x6
=> the exhausted turn => tally, each body asserted against the
named-constant literals); the determinism replay (two fresh homes,
byte-identical [r.content] lists); the four refusal arcs (404 the unknown
run, 422 the bogus winner, 409 the SAFE HALT, 400 the malformed items —
the family grammar taught, the violation named in found); the concurrency
arc (N=2 threads x M=2 casts through the seam's
process-wide lock, aggregate-only assertions, the file's direct read via
Persist.load the oracle). The honest count: ~5 test functions. The
no-shell law honored: every Popen a fixed-argv LIST, never a shell string
(the S603/S607 per-file entry rides pyproject; the S101/PLR2004 tests
ruling stands). The sizing law's region form: the file assembled from two
verified regions — region 1 the boot instrument (this head through the
fixture), region 2 the five arcs (the next single-goal dispatch).
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from subprocess import PIPE, Popen, TimeoutExpired
from threading import Barrier, Thread
from time import monotonic, sleep
from typing import TYPE_CHECKING

import httpx2 as httpx  # httpx2 the lock's name; the floor verifies the import resolves
import pytest

from prioritree.run_store import Persist  # THE ORACLE IMPORT — the file's direct read

if TYPE_CHECKING:
    from collections.abc import Iterator

# The boot instrument (service-acceptance-brief §1-§2, content-in-configuration).
_UVICORN = Path(sys.executable).parent / "uvicorn"
_ARGV = [
    str(_UVICORN),
    "prioritree.service:app",
    "--host",
    "127.0.0.1",
    "--port",
    "0",
    "--no-access-log",
]
_DEADLINE = 15.0
_INTERVAL = 0.1
_CALL_TIMEOUT = 0.5
_BANNER = re.compile(r"Uvicorn running on http://127\.0\.0\.1:(\d+)")

# The payload literals (the face tests' own on-disk literals, carried 1:1).
_ITEMS = [["a", "one"], ["b", "two"], ["c", "three"]]
_OPERATOR = {"operator_id": "op-1", "question": "Which matters more?"}
_RUN_ID = "RUN-0001"
_VOTE_BODY = {
    "pair": ["a", "b"],
    "winner": "prefer-a",
    "comparator_id": "x",
    "comparator_class": "human",
}

def _boot(home: Path) -> tuple[Popen[bytes], int]:
    """Start the uvicorn subprocess at home and parse the banner for the port.

    Purpose: Popen(_ARGV, cwd=home, stderr=PIPE, env={**os.environ,
    "AUTH": "off"}) — the fixed-argv boot at the auth-off degrade (the
    real-socket suite's dev mode preserved, the doors pass bare —
    servingtierintegrationspec §7c); read stderr lines bounded by
    _DEADLINE, match _BANNER, close the pipe after the port is taken,
    and return (process, port).
    Refuses when: the deadline passes without a banner — terminate, wait,
    and FAIL the assertion with the diagnostic (the lines read so far +
    the returncode). A timeout FAILS, never skips.
    Re-run: deterministic in shape — the port kernel-assigned per boot.
    Touches: the subprocess's stderr pipe; the home's tree via the child.
    Provenance: service-acceptance-brief §1-§2 (the boot instrument),
    the dispatch synthesize/service-acceptance-bytes (region 1).
    """
    process = Popen(_ARGV, cwd=home, stderr=PIPE, env={**os.environ, "AUTH": "off"})
    assert process.stderr is not None  # the PIPE contract; the loop's read member
    lines: list[bytes] = []
    deadline = monotonic() + _DEADLINE
    while monotonic() < deadline:
        line = process.stderr.readline()
        if not line:
            sleep(_INTERVAL)
            continue
        lines.append(line)
        match = _BANNER.search(line.decode("utf-8", errors="replace"))
        if match is not None:
            process.stderr.close()
            return process, int(match.group(1))
    process.terminate()
    process.wait(timeout=5)
    message = (
        f"uvicorn did not announce its port within {_DEADLINE}s at {home}; returncode="
        f"{process.returncode}; stderr so far: {b''.join(lines).decode('utf-8', errors='replace')}"
    )
    pytest.fail(message)
    raise AssertionError(message)  # unreachable; the floor's narrow reach


def _wait_ready(client: httpx.Client, base_url: str) -> None:
    """Probe the 404-as-ready endpoint until the whole chain answers.

    Purpose: retry GET {base_url}/runs/RUN-0001/next with
    timeout=_CALL_TIMEOUT — 404 => ready (the whole chain proven: TCP
    accepted, HTTP parsed, route matched, the sync handler through the
    seam, the unknown-run refusal rendered); ConnectError/ConnectTimeout
    => sleep(_INTERVAL), retry; any other status => fail loudly.
    Refuses when: the deadline exhausts without a 404 — the assertion
    fails with the diagnostic. A timeout FAILS, never skips.
    Re-run: deterministic — the fresh home's empty live-set always 404s.
    Touches: the socket only (the probe doubles as the first refusal data
    point; the home's store untouched — RUN-0001 unknown).
    Provenance: service-acceptance-brief §2 (the readiness probe), the
    dispatch synthesize/service-acceptance-bytes (region 1).
    """
    deadline = monotonic() + _DEADLINE
    while monotonic() < deadline:
        try:
            response = client.get(
                f"{base_url}/runs/{_RUN_ID}/next", timeout=_CALL_TIMEOUT,
            )
        except (httpx.ConnectError, httpx.ConnectTimeout):
            sleep(_INTERVAL)
            continue
        if response.status_code == 404:
            return
        pytest.fail(
            f"readiness probe returned {response.status_code}: {response.text}",
        )
    pytest.fail(
        f"service at {base_url} not ready within {_DEADLINE}s (404 probe)",
    )


@pytest.fixture
def service(tmp_path: Path) -> Iterator[tuple[httpx.Client, str]]:
    """Boot the real socket per test and yield the (client, base_url) pair.

    Purpose: function-scoped by structure — one boot per test shares no
    home (the session form rejected: the stem sequence test-order-coupled,
    the refusal arcs polluting the shared home, the replay needing two
    fresh homes by its own claim). _boot at tmp_path (the home isolation
    the Popen's cwd alone provides — STORE_HOME CWD-relative, never
    .resolve()d); httpx.Client(); _wait_ready; yield (client, base_url).
    Refuses when: never — a fixture (the boot-then-yield form); the
    teardown always runs (pytest's finalization guarantees it on
    assertion failure — no orphaned uvicorns).
    Re-run: deterministic in shape — the port kernel-assigned, the home
    fresh per test (the register's own mkdir builds the store home).
    Touches: the subprocess tree (terminate => wait(timeout=5) => kill()
    only on TimeoutExpired — the graceful drain, then the backstop); the
    client closed.
    Provenance: service-acceptance-brief §1 (the fixture), the
    dispatch synthesize/service-acceptance-bytes (region 1).
    """
    process, port = _boot(tmp_path)
    base_url = f"http://127.0.0.1:{port}"
    client = httpx.Client()
    try:
        _wait_ready(client, base_url)
        yield client, base_url
    finally:
        client.close()
        process.terminate()
        try:
            process.wait(timeout=5)
        except TimeoutExpired:
            process.kill()


def _drive_arc(client: httpx.Client, base_url: str) -> list[httpx.Response]:
    """Drive the eleven-request arc and return the responses in arc order.

    Purpose: the arc shared by the assertion test and the replay test —
    register (POST /runs, _ITEMS + _OPERATOR), the manifest read (GET
    .../manifest — the sixth query over the live seam, the lock + the full
    load under the real process), next (GET .../next), vote x6 over the
    three pairs (a,b)/(a,c)/(b,c), each body the _VOTE_BODY form with the
    pair swapped, the exhausted next turn, and tally; return the responses
    whole — the parsed-body assertions are the CALLER's own (test 1 asserts
    .json(), test 2 compares the .content byte lists).
    Refuses when: never — a driver (the responses returned unasserted; the
    caller owns the judgment).
    Re-run: deterministic — the arc's bodies carry no timestamps (the census
    elides the vote_log; the manifest body elides the registration stamp),
    the fresh home's stems identical.
    Touches: the socket only; the home's store via the service.
    Provenance: service-acceptance-brief §3-§4 (the arc, the replay), the
    dispatch synthesize/service-acceptance-bytes (region 2), the ux build's
    sixth query (the manifest leg — the service unit brief §5).
    """
    responses: list[httpx.Response] = []
    responses.append(client.post(f"{base_url}/runs", json={"items": _ITEMS, **_OPERATOR}))
    responses.append(client.get(f"{base_url}/runs/{_RUN_ID}/manifest"))
    responses.append(client.get(f"{base_url}/runs/{_RUN_ID}/next"))
    for pair in (("a", "b"), ("a", "c"), ("b", "c")):
        responses.extend([client.post(f"{base_url}/runs/{_RUN_ID}/votes", json={**_VOTE_BODY, "pair": list(pair)})])
        responses.append(
            client.post(
                f"{base_url}/runs/{_RUN_ID}/votes",
                json={**_VOTE_BODY, "pair": list(pair), "comparator_class": "llm"},
            ),
        )
    responses.append(client.get(f"{base_url}/runs/{_RUN_ID}/next"))
    responses.append(client.get(f"{base_url}/runs/{_RUN_ID}/tally"))
    return responses


def test_accept_the_eleven_request_arc(service: tuple[httpx.Client, str]) -> None:
    """Register => manifest => next => vote x6 => the exhausted turn => tally, each body asserted.

    Purpose: the full eleven-request arc over the real socket — register
    201 {"run_id": _RUN_ID}; the manifest read 200 the five-key body (the
    stem echoed, the question, the verdicts sorted, the quorum, the items
    payload-order-preserved — the operator id and the stamp elided); next
    200 the first pair with count 0; the six votes 200 with the acks
    {"vote_id": "VOTE-000N", "count": N, "acknowledged": False} (the wire's
    count the run's census count 1..6, the running total); the exhausted
    next 200 the DONE body (done is True, "tally" in next_action — DONE a
    state, never an error); tally 200 the frozen whole, the exact literal
    the face tests assert.
    Refuses when: any step's status or body diverges — each response's
    status and .json() asserted against the named-constant literals
    (content-in-configuration).
    Re-run: deterministic — the fresh home's stems and the census's frozen
    whole carry no timestamps across the wire.
    Touches: the socket; the home's store via the service.
    Provenance: service-acceptance-brief §3 (the arc), the dispatch
    synthesize/service-acceptance-bytes (region 2), the ux build's sixth
    query (the manifest leg — the service unit brief §5).
    """
    client, base_url = service
    responses = _drive_arc(client, base_url)
    assert len(responses) == 11  # the arc's own shape: 1 register, 1 manifest, 1 next, 6 votes, 1 done, 1 tally
    assert [response.status_code for response in responses] == [
        201, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200,
    ]
    bodies = [response.json() for response in responses]
    assert bodies[0] == {"run_id": _RUN_ID}
    assert bodies[1] == {
        "run_id": _RUN_ID,
        "question": "Which matters more?",
        "verdicts": ["prefer-a", "prefer-b", "tie"],
        "quorum": 1,
        "items": [["a", "one"], ["b", "two"], ["c", "three"]],
    }
    assert bodies[2] == {"item_a": "a", "item_b": "b", "count": 0}
    assert bodies[3] == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}
    assert bodies[4] == {"vote_id": "VOTE-0002", "count": 2, "acknowledged": False}
    assert bodies[5] == {"vote_id": "VOTE-0003", "count": 3, "acknowledged": False}
    assert bodies[6] == {"vote_id": "VOTE-0004", "count": 4, "acknowledged": False}
    assert bodies[7] == {"vote_id": "VOTE-0005", "count": 5, "acknowledged": False}
    assert bodies[8] == {"vote_id": "VOTE-0006", "count": 6, "acknowledged": False}
    done = bodies[9]
    assert done["done"] is True
    assert "tally" in done["next_action"]
    assert bodies[10] == {
        "ranked_groups": [["a"], ["b"], ["c"]],
        "per_item_wins": {"a": 4, "b": 2, "c": 0},
        "per_item_losses": {"a": 0, "b": 2, "c": 4},
        "per_item_ties": {"a": 0, "b": 0, "c": 0},
        "coverage": {
            "components": [["a", "b", "c"]],
            "done": True,
            "cycle": [],
            "pair_counts": {"a|b": 2, "a|c": 2, "b|c": 2},
            "pair_class_counts": {
                "a|b": {"human": 1, "llm": 1},
                "a|c": {"human": 1, "llm": 1},
                "b|c": {"human": 1, "llm": 1},
            },
        },
        "algorithm_version": "win-rate-v1",
    }


def test_replay_byte_identical(tmp_path: Path) -> None:
    """Two fresh homes driven through the same arc => byte-identical content lists.

    Purpose: the determinism replay — two homes (tmp_path/"one",
    tmp_path/"two"), a boot at each, the same eleven-request arc against
    each via _drive_arc; assert the .content byte lists equal — THE BYTES,
    not parsed dicts; byte-identity IS the claim (no recorded_at crosses
    the wire: the register body the stem alone, the manifest the five
    clock-free keys, the acks the triple, the tally the frozen whole).
    The teardown the test's own finally (the fixture manages one boot; the
    replay manages its pair).
    Refuses when: the byte lists diverge — any timestamped or
    order-dependent byte escaping into a body fails the equality.
    Re-run: deterministic — the fresh homes' stems identical, the port
    never appears in any body.
    Touches: the two subprocess trees; the two homes' stores via the
    services; two clients (closed in the finally).
    Provenance: service-acceptance-brief §4 (the replay), the dispatch
    synthesize/service-acceptance-bytes (region 2).
    """
    homes = (tmp_path / "one", tmp_path / "two")
    processes: list[Popen[bytes]] = []
    clients: list[httpx.Client] = []
    arc_lists: list[list[bytes]] = []
    try:
        for home in homes:
            home.mkdir()
            process, port = _boot(home)
            processes.append(process)
            client = httpx.Client()
            clients.append(client)
            base_url = f"http://127.0.0.1:{port}"
            _wait_ready(client, base_url)
            arc_lists.append([response.content for response in _drive_arc(client, base_url)])
        assert arc_lists[0] == arc_lists[1]  # THE BYTES
    finally:
        for client in clients:
            client.close()
        for process in processes:
            process.terminate()
            try:
                process.wait(timeout=5)
            except TimeoutExpired:
                process.kill()
                process.wait(timeout=5)


# The refusal grammar's three fields as a set (the family grammar asserted
# EXACTLY — the native detail grammar of the 400 re-badge never carries
# these keys; the service-face precedent carried 1:1).


def test_refuse_the_four_arcs(service: tuple[httpx.Client, str]) -> None:
    """The four refusals through the socket: 404, 422, 409 the SAFE HALT, 400 the re-badge.

    Purpose: each refusal arc asserted against the wire's own grammar —
    404 GET /runs/RUN-9999/next with the three refusal fields and
    "RUN-9999" in found; 422 the vote with winner "bogus-winner" (the
    run registered so the VALUE owns the refusal); 409 a fresh cast then
    GET tally with "at quorum" in expected (the SAFE HALT never
    swallowed); 400 POST /runs with items "not-a-list" with the family
    grammar, the violation taught in found (the re-badge cured — 422
    exclusively the door's value refusals).
    Refuses when: any status or grammar diverges — the three-field set
    asserted exactly where the family grammar owns the body.
    Re-run: deterministic — the fresh home's refusals carry no state
    across arcs within the one test home.
    Touches: the socket; the home's store via the service (the register
    + the one cast land — the test's own data points).
    Provenance: service-acceptance-brief §5 (the refusals), the
    dispatch synthesize/service-acceptance-bytes (region 2).
    """
    client, base_url = service
    # 404 — the unknown run.
    response = client.get(f"{base_url}/runs/RUN-9999/next")
    assert response.status_code == 404
    body = response.json()
    assert set(body) == _REFUSAL_KEYS
    assert "RUN-9999" in body["found"]
    # 422 — the bogus winner (the run registered so the value owns the refusal).
    client.post(f"{base_url}/runs", json={"items": _ITEMS, **_OPERATOR})
    response = client.post(
        f"{base_url}/runs/{_RUN_ID}/votes",
        json={**_VOTE_BODY, "winner": "bogus-winner"},
    )
    assert response.status_code == 422
    assert set(response.json()) == _REFUSAL_KEYS
    # 409 — one legal cast then tally: the SAFE HALT.
    response = client.post(f"{base_url}/runs/{_RUN_ID}/votes", json=_VOTE_BODY)
    assert response.status_code == 200
    response = client.get(f"{base_url}/runs/{_RUN_ID}/tally")
    assert response.status_code == 409
    assert "at quorum" in response.json()["expected"]
    # 400 — the malformed items (the family grammar taught; 422 the door's alone).
    response = client.post(f"{base_url}/runs", json={"items": "not-a-list", **_OPERATOR})
    assert response.status_code == 400
    body = response.json()
    assert set(body) == _REFUSAL_KEYS
    assert "items" in body["expected"]
    assert "body.items" in body["found"]


def test_interleave_the_concurrency_arc(service: tuple[httpx.Client, str], tmp_path: Path) -> None:
    """Two threads x two casts through the barrier => the aggregate-only assertions + the oracle.

    Purpose: the concurrency arc — Barrier(2) releases both threads'
    first casts together; thread-1 casts (a,b) then (a,c) with
    comparator_id "c1"; thread-2 casts (b,c) then (a,b) with
    comparator_id "c2"; each thread its own httpx.Client. THE
    AGGREGATE-ONLY assertions: every cast 200 (the four responses
    collected); GET /state => 200 {"total": 4, "items": {"a": 3,
    "b": 3, "c": 2}}; the vote-id set from the acks exactly
    {VOTE-0001..VOTE-0004} — the ORDER NEVER asserted (the lock
    serializes, arrival order decides). THE FILE'S DIRECT READ: the
    fresh Persist.load at tmp_path/".prioritree"/"runs" (STORE_HOME
    CWD-relative to the subprocess's cwd=tmp_path) — the census: 4
    records, the vote-id set unique, the per-pair counts exact.
    Refuses when: any cast fails, a count diverges (total < 4 the lost
    update; a duplicate id the doubled mint), or the file's direct read
    disagrees with the wire.
    Re-run: deterministic in AGGREGATE — the interleaving nondeterministic
    by construction, the order-invariant totals the claim.
    Touches: the socket; the home's store via the service AND directly
    (the test process reads the subprocess's home — safe: each request
    composes a fresh run-store inside the lock, the file closed between
    requests; after the census confirms 4, the file quiescent).
    Provenance: service-acceptance-brief §6 (the concurrency arc), the
    dispatch synthesize/service-acceptance-bytes (region 2).
    """
    client, base_url = service
    client.post(f"{base_url}/runs", json={"items": _ITEMS, **_OPERATOR})
    barrier = Barrier(2)
    acks: list[httpx.Response] = []

    def _cast_thread(pairs: tuple[tuple[str, str], ...], comparator_id: str) -> None:
        """Cast this thread's two votes through its own client."""
        thread_client = httpx.Client()
        try:
            barrier.wait(timeout=_DEADLINE)
            for pair in pairs:
                body = {**_VOTE_BODY, "pair": list(pair), "comparator_id": comparator_id}
                acks.append(thread_client.post(f"{base_url}/runs/{_RUN_ID}/votes", json=body))
        finally:
            thread_client.close()

    thread_one = Thread(target=_cast_thread, args=((("a", "b"), ("a", "c")), "c1"))
    thread_two = Thread(target=_cast_thread, args=((("b", "c"), ("a", "b")), "c2"))
    thread_one.start()
    thread_two.start()
    thread_one.join(timeout=_DEADLINE)
    thread_two.join(timeout=_DEADLINE)

    assert len(acks) == 4
    assert all(response.status_code == 200 for response in acks)
    vote_ids = {response.json()["vote_id"] for response in acks}
    assert vote_ids == {"VOTE-0001", "VOTE-0002", "VOTE-0003", "VOTE-0004"}

    response = client.get(f"{base_url}/runs/{_RUN_ID}/state")
    assert response.status_code == 200
    assert response.json() == {"total": 4, "items": {"a": 3, "b": 3, "c": 2}}

    # THE FILE'S DIRECT READ — the oracle against the subprocess's own home.
    store_home = tmp_path / ".prioritree" / "runs"
    census = Persist.load(store_home, _RUN_ID).census()
    assert len(census.vote_log) == 4
    assert {record.vote_id for record in census.vote_log} == vote_ids
    pair_counts: dict[str, int] = {}
    for record in census.vote_log:
        key = f"{record.pair.item_a}|{record.pair.item_b}"
        pair_counts[key] = pair_counts.get(key, 0) + 1
    assert pair_counts == {"a|b": 2, "a|c": 1, "b|c": 1}
_REFUSAL_KEYS = frozenset({"expected", "found", "next_action"})
