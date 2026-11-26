# Copyright (C) 2026 Mark Losey. All rights reserved.
"""test_mcp_server_face -- the tool face's falsification set, in-process.

The mcp-server unit's test surface (SS5(b) of the exact-task spec,
reports/synthesize/mcpserverspec.md): the five tools' arcs over the
caller-side harness -- ouncemcp.testing.as_caller around
OunceServer.call_tool in-process (the census's proof form), the caller's
identity a GRANTED ouncemcp.testing.make_token mint (the door's five scope
tokens, the door-shaped claims -- under the mcp-verified-token unit's
armed door the scope-less subject-only tokens deny, the granted form the
standing arcs' ride), the direct-call tier's ctx the headless ToolContext
(the anonymous identity outside any caller context, the body's claims
standing). (1) Each tool's
success form asserted field-for-field: the register ack (the verdicts echo
sorted), the served pair's one-model shape, the cast ack (the record
elided), the census's exact two-key body, TallyView whole at full coverage
(the coverage summary, pair_counts elided) -- and DONE a value never an
error (done=true a RESULT, the three fields populated, no error raised).
(2) The structured error assertions: the ThreePart's three fields as data
at every refusal surface -- the unknown run at next/census/tally (the wire
text's labeled segments, the live set named), and the out-of-set winner
AND the class refused BOTH ways: at the SCHEMA (the Literal's own gate,
the typed validation form) and at the CORE (a corrupted body past
validation fed to the handler, the raised ThreePart the payload). (3) The
SAFE HALT: the under-cap refusal's fields pass through verbatim with the
wire's 300-char clip governing the visible bytes (the grown render
clipped, the heads asserted), and the K=10 capped render probed twice --
the raised payload (legs 1-2 whole, the elision named in found AND
next_action, the first ten shown, the eleventh capped) and the wire (the
same render clipped at Limits.max_error_chars=300, the step-4 finding
made visible, the total's head and the ellipsis asserted -- the two-cap
reality: the found's 10-cap, the wire's 300-clip). (4) The idempotency
replay arcs: the guard replays per
principal -- under the armed door a fresh principal is a fresh comparator,
so the re-send rides the SAME principal with the body's id fabricated (the
transport guard bypassed by the args diff, the core's dedup hit on the
VERIFIED id: acknowledged=true, the count unchanged, the original's
vote_id -- the self-claim never forks a voice), the changed verdict a new
record, and the cross-session re-register mints RUN-0002 (the fresh
caller's granted token a fresh principal). (5) The stamps' schema gates
(comparator_class required and pattern-gated; the llm class landing at
equal weight), supersedes' correction both ways, the seed's stability, the
scheduler-suggests seam (a vote lands un-served), the census's AS-IS law
after a correction, the served-pair skip at quorum, and the full sitting
walked end-to-end with the re-tally after the cure. Isolation by injection
(the service-face precedent): each test re-binds the module's _seam/_lock
over a fresh tmp home and redirects the module's STORE_HOME binding (the
halt shaper's fresh read rides it; monkeypatch's string form -- the Final
symbol never re-assigned, the real default never touched on disk), and
mints a unique caller subject per test (the idempotency claims key per
principal -- a shared subject would replay an earlier test's writes through
the server's process-wide MemoryStore; the "face-{N}" stem keeps that
uniqueness suite-scope -- another file's mints ride the same process-wide
store, so the file-prefixed stems fence the cross-file seam). The S101/PLR2004
tests ruling stands.
"""

from __future__ import annotations

import asyncio
from itertools import count
from typing import TYPE_CHECKING, Any, cast

import pytest
from mcp_types import TextContent
from ouncemcp import InvalidInput, ToolContext
from ouncemcp.testing import as_caller, make_token

from prioritree import mcp_server
from prioritree.mcp_server import CastInput, TallyInput
from prioritree.service_store import Serialize
from prioritree.store_lock import Lock

if TYPE_CHECKING:
    from collections.abc import Iterator
    from pathlib import Path

    from fastmcp.server.auth import AccessToken
    from fastmcp.tools import ToolResult

# The face's own vocabulary (the literals ARE the specification under test,
# the test_service_face school): the bare-id register body (label=id at the
# door), the three-item sitting (three scheduled pairs -- full coverage at
# three prefer-a votes, the ranked whole hand-computable), and the callers'
# mint (a unique subject per test).
_ITEMS = ["a", "b", "c"]
_OPERATOR = {"operator_id": "op-1", "question": "Which matters more?"}
_RUN_ID = "RUN-0001"
_VERDICTS = ["prefer-a", "prefer-b", "tie"]
_CALLERS: Iterator[int] = count(1)


# The door's granted vocabulary (the five tools' scope tokens -- the map's
# own rows; manifest absent: no mcp tool carries it): the standing arcs'
# default grant under the armed door.
_GRANTED: tuple[str, ...] = ("register", "next", "cast", "state", "tally")


def _call(caller: str, tool: str, arguments: dict[str, Any], *, token: AccessToken | None = None) -> ToolResult:
    """Call the tool in-process as the granted caller -- the census's harness form, door-armed.

    The granted default: the caller's token minted by _granted (the five
    scope tokens, the door-shaped claims -- under the armed door the
    scope-less subject-only tokens deny at the policy, so the granted
    identity is the standing arcs' ride); the token knob the
    claims-shaping arcs' own.
    """
    with as_caller(access_token=token or _granted(caller)):
        return asyncio.run(mcp_server.server.call_tool(tool, arguments))


def _headless() -> ToolContext:
    """Construct the headless tool context -- the direct-call tier's own form.

    The model_construct school (the corrupted body past validation fed to
    the handler): the ctx the wire always injects, constructed bare at the
    direct tier -- the three required fields alone; the identity resolves
    ANONYMOUS outside any caller context (the body's claims stand, the
    core's gates fire on the body's stamps -- the asserted bytes stand).
    """
    return ToolContext(tool="votes.cast", response_format="concise", result_budget=0)


def _join(result: ToolResult) -> str:
    """Join the result's text channel -- the error labels' assertable ground."""
    return "".join(part.text for part in result.content if isinstance(part, TextContent))


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


def _register(caller: str, items: list[str], quorum: int = 1) -> ToolResult:
    """Register a sitting over the module's seam -- the shared setup's one line."""
    return _call(caller, "runs.register", {"items": items, "quorum": quorum, **_OPERATOR})


def _cast(
    caller: str,
    pair: list[str],
    winner: str,
    comparator_id: str,
    comparator_class: str = "human",
    supersedes: str | None = None,
) -> ToolResult:
    """Cast a judgment over the module's seam -- the shared setup's one line.

    The six-argument form (the run id the module constant -- every test's
    fresh home mints RUN-0001; the class the parameter's own default human
    -- the corroborating llm casts ride the parameter; the class-gate arcs
    inline their own bodies at the wire).
    """
    arguments: dict[str, Any] = {
        "run_id": _RUN_ID,
        "pair": pair,
        "winner": winner,
        "comparator_id": comparator_id,
        "comparator_class": comparator_class,
    }
    if supersedes is not None:
        arguments["supersedes"] = supersedes
    return _call(caller, "votes.cast", arguments, token=_granted(caller, comparator_class=comparator_class))


@pytest.fixture
def caller(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> str:
    """Isolate the face by injection and mint the test's caller -- fresh store, fresh session.

    Purpose: re-bind the module's level objects over a fresh tmp home (the
    service-face fixture precedent -- the tools' bodies read the module
    globals at call time), redirect the module's STORE_HOME binding to the
    same home (the halt shaper's fresh read rides it; monkeypatch's string
    form -- the Final symbol never re-assigned, the real default never
    touched on disk, the binding restored at teardown), and mint the test's
    unique caller subject (the idempotency claims key per principal -- a
    shared subject would replay an earlier test's writes through the
    server's process-wide MemoryStore; the "face-{N}" stem keeps the pool
    suite-unique -- another file's mints ride the same process-wide store).
    Refuses when: never -- a fixture (the isolate-then-yield form).
    Re-run: deterministic -- a fresh tmp home and a fresh caller per test.
    Touches: the tmp home only (pytest's own tmp_path); the module's
    bindings, restored or re-minted by the next test.
    Provenance: the spec SS5(b) (the isolation clause), the service-face
    precedent (Q-service-lifecycle), G-MCPSERVERSPEC-BRIEF.
    """
    monkeypatch.setattr(mcp_server, "STORE_HOME", tmp_path)
    monkeypatch.setattr(mcp_server, "_seam", Serialize(tmp_path))
    monkeypatch.setattr(mcp_server, "_lock", Lock(tmp_path))
    return f"face-{next(_CALLERS)}"


def test_register_ack(caller: str) -> None:
    """A register over the face => the ack field-for-field, the verdicts echoed sorted."""
    result = _call(caller, "runs.register", {"items": _ITEMS, "quorum": 1, **_OPERATOR})
    assert result.is_error is False
    assert result.structured_content == {
        "run_id": _RUN_ID,
        "count": 3,
        "quorum": 1,
        "verdicts": _VERDICTS,
    }


def test_next_serves_the_first_pair(caller: str) -> None:
    """A next after register => the first under-quorum pair with count 0, the one-model shape."""
    _register(caller, _ITEMS)
    result = _call(caller, "runs.next", {"run_id": _RUN_ID})
    assert result.is_error is False
    assert result.structured_content == {
        "done": False,
        "item_a": "a",
        "item_b": "b",
        "count": 0,
        "presentation_order": "canonical",
        "expected": "",
        "found": "",
        "next_action": "",
    }


def test_cast_ack(caller: str) -> None:
    """A cast on the served pair => the ack triple (the VoteRecord elided)."""
    _register(caller, _ITEMS)
    result = _cast(caller, ["a", "b"], "prefer-a", "x")
    assert result.is_error is False
    assert result.structured_content == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}


def test_census_view(caller: str) -> None:
    """A census after one vote => the exact two-key body, per_pair_counts and the log elided."""
    _register(caller, _ITEMS)
    _cast(caller, ["a", "b"], "prefer-a", "x")
    result = _call(caller, "votes.census", {"run_id": _RUN_ID})
    assert result.is_error is False
    assert result.structured_content == {"total": 1, "items": {"a": 1, "b": 1, "c": 0}}


def test_tally_view_at_full_coverage(caller: str) -> None:
    """A tally at full coverage => TallyView whole -- the coverage summary, pair_counts elided."""
    _register(caller, _ITEMS)
    for pair in (["a", "b"], ["a", "c"], ["b", "c"]):
        _cast(caller, pair, "prefer-a", "x")
        _cast(caller, pair, "prefer-a", "x", "llm")
    result = _call(caller, "runs.tally", {"run_id": _RUN_ID})
    assert result.is_error is False
    assert result.structured_content == {
        "ranked_groups": [["a"], ["b"], ["c"]],
        "per_item_wins": {"a": 4, "b": 2, "c": 0},
        "per_item_losses": {"a": 0, "b": 2, "c": 4},
        "per_item_ties": {"a": 0, "b": 0, "c": 0},
        "coverage": {
            "components": [["a", "b", "c"]],
            "cycle": [],
            "pairs_expected": 3,
            "pairs_at_quorum": 3,
            "done": True,
        },
        "algorithm_version": "win-rate-v1",
    }


def test_next_done_terminal(caller: str) -> None:
    """The exhausted two-item sitting => done=true a RESULT, the three fields populated, no error."""
    _register(caller, ["a", "b"])
    _cast(caller, ["a", "b"], "prefer-a", "x")
    result = _call(caller, "runs.next", {"run_id": _RUN_ID})
    assert result.is_error is False
    body = result.structured_content
    assert body is not None
    assert set(body) == {"done", "item_a", "item_b", "count", "presentation_order", "expected", "found", "next_action"}
    assert body["done"] is True
    assert body["item_a"] == ""
    assert body["item_b"] == ""
    assert body["count"] == 0
    assert body["expected"] == "all 1 scheduled pairs at quorum k=1"
    assert "the queue is exhausted" in body["found"]
    assert "call tally_rank(run_id)" in body["next_action"]


def test_next_unknown_run_refused(caller: str) -> None:
    """A next on an unknown run => Not found, the three labeled fields, the id in found."""
    result = _call(caller, "runs.next", {"run_id": "RUN-9999"})
    assert result.is_error is True
    text = _join(result)
    assert "Not found:" in text
    assert "expected: a run file in the store home (live: (none on disk))" in text
    assert "'RUN-9999'" in text
    assert "next_action: register a run first" in text
    assert result.structured_content is None


def test_census_unknown_run_refused(caller: str) -> None:
    """A census on an unknown run after a register => the live set named in expected."""
    _register(caller, _ITEMS)
    result = _call(caller, "votes.census", {"run_id": "RUN-9999"})
    assert result.is_error is True
    text = _join(result)
    assert "Not found:" in text
    assert "expected: a run file in the store home (live: RUN-0001)" in text
    assert "'RUN-9999'" in text


def test_tally_unknown_run_refused(caller: str) -> None:
    """A tally on an unknown run => Not found, the three labeled fields, the repair path named."""
    result = _call(caller, "runs.tally", {"run_id": "RUN-9999"})
    assert result.is_error is True
    text = _join(result)
    assert "Not found:" in text
    assert "expected: a run file in the store home (live: (none on disk))" in text
    assert "'RUN-9999'" in text
    assert "next_action: register a run first" in text


def test_cast_winner_refused_at_the_schema(caller: str) -> None:
    """A cast whose winner is outside the declared set => the Literal's gate, the typed form."""
    _register(caller, _ITEMS)
    result = _cast(caller, ["a", "b"], "bogus-winner", "x")
    assert result.is_error is True
    text = _join(result)
    assert "Invalid input:" in text
    assert "`winner` must be one of" in text
    assert "expected:" not in text


def test_cast_winner_refused_at_the_core(caller: str) -> None:
    """A corrupted-winner body past the schema => the core's gate, the ThreePart the payload.

    The schema always gates first on the wire (the Literal mirrors the
    declared set); the core leg rides a body constructed past validation
    (model_construct) fed to the handler directly -- the only path where
    the schema passes and the core refuses.
    """
    _register(caller, _ITEMS)
    body = CastInput.model_construct(
        run_id=_RUN_ID,
        pair=["a", "b"],
        winner="bogus-winner",
        comparator_id="x",
        comparator_class="human",
        notes=None,
        supersedes=None,
    )
    with pytest.raises(InvalidInput, match="a verdict from the run's declared set"):
        mcp_server.cast(body, _headless())


def test_cast_class_refused_at_the_schema(caller: str) -> None:
    """A cast with comparator_class outside {human, llm} => the Literal's gate, the typed form."""
    _register(caller, _ITEMS)
    result = _call(
        caller,
        "votes.cast",
        {
            "run_id": _RUN_ID,
            "pair": ["a", "b"],
            "winner": "prefer-a",
            "comparator_id": "x",
            "comparator_class": "robot",
        },
    )
    assert result.is_error is True
    text = _join(result)
    assert "Invalid input:" in text
    assert "`comparator_class` must be one of: human or llm" in text
    assert "expected:" not in text


def test_cast_class_refused_at_the_core(caller: str) -> None:
    """A corrupted-class body past the schema => the core's gate, the ThreePart the payload.

    The schema always gates first on the wire (the Literal mirrors the
    core's set); the core leg rides a body constructed past validation
    (model_construct) fed to the handler directly -- the only path where
    the schema passes and the core refuses.
    """
    _register(caller, _ITEMS)
    body = CastInput.model_construct(
        run_id=_RUN_ID,
        pair=["a", "b"],
        winner="prefer-a",
        comparator_id="x",
        comparator_class="robot",
        notes=None,
        supersedes=None,
    )
    with pytest.raises(InvalidInput, match="comparator_class got 'robot'"):
        mcp_server.cast(body, _headless())


def test_halt_refusal_under_the_cap(caller: str) -> None:
    """A tally one vote short of quorum 2 => the refusal's visible heads on the wire.

    The under-cap leg: the shaper never re-derives (the refusal's fields
    pass through VERBATIM -- the found's two sections both visible); the
    grown render pushes the next_action's tail past the wire's 300-char
    clip -- the section's head assertable, the tail clipped with the
    ellipsis (the two-cap reality: the found's 10-cap never fires under
    ten pairs, the wire's 300-clip does).
    """
    _register(caller, ["a", "b"], quorum=2)
    _cast(caller, ["a", "b"], "prefer-a", "x")
    result = _call(caller, "runs.tally", {"run_id": _RUN_ID})
    assert result.is_error is True
    text = _join(result)
    assert "Invalid input:" in text
    assert "expected: the coverage gate met" in text
    assert "every pair at quorum k=2" in text
    assert "found: under-quorum pairs: (a, b) 1 of 2" in text
    assert "uncorroborated pairs: (a, b) missing llm" in text
    assert "next_action: cast the missing votes: (a, b) needs" in text
    assert text.endswith("…")


def test_halt_capped_render_payload(caller: str) -> None:
    """The over-cap halt's raised payload => legs 1-2 whole, the elision named twice, ten shown.

    Fifteen under-quorum pairs (n=6, quorum 1, zero votes): the shaper's
    render -- the expected carried whole, legs 1-2 whole, the elision
    phrase in found AND next_action (count == 2), the first ten pairs
    shown ((c, d) the tenth), the eleventh ((c, e)) capped out.
    """
    _register(caller, ["a", "b", "c", "d", "e", "f"])
    with pytest.raises(InvalidInput) as raised:
        mcp_server.tally(TallyInput(run_id=_RUN_ID))
    payload = str(raised.value)
    assert "the coverage gate met" in payload
    assert "zero-coverage items: a, b, c, d, e, f" in payload
    assert "components: (a), (b), (c), (d), (e), (f)" in payload
    assert payload.count("15 under-quorum pairs total; first 10 shown") == 2
    assert "(c, d) 0 of 1" in payload
    assert "(c, e) 0 of 1" not in payload
    assert "cast the bridging pairs" in payload
    assert "quorum needs MORE VOTES on existing pairs" in payload


def test_halt_capped_render_wire(caller: str) -> None:
    """The same over-cap halt through the harness => the wire's clipped form, the total's head visible.

    The Failure render clips at Limits.max_error_chars=300 (the step-4
    finding): the expected whole + legs 1-2 + the under-quorum total's
    head ride the first 300 chars; the found's internal 10-cap elision
    rides past the wire clip, the tail clips with the ellipsis -- the
    caller's honest view (the two-cap reality: the found's 10-cap, the
    wire's 300-clip).
    """
    _register(caller, ["a", "b", "c", "d", "e", "f"])
    result = _call(caller, "runs.tally", {"run_id": _RUN_ID})
    assert result.is_error is True
    text = _join(result)
    assert "Invalid input:" in text
    assert "the coverage gate met" in text
    assert "zero-coverage items: a, b, c, d, e, f" in text
    assert "components: (a), (b), (c), (d), (e), (f)" in text
    assert "under-quorum pairs: 15" in text
    assert text.endswith("…")


def test_cast_resend_acknowledged(caller: str) -> None:
    """A re-send with the body's id fabricated, the same verified id => acknowledged=true.

    The guard replays per principal -- under the armed door a fresh
    principal is a fresh comparator (the dedup would miss), so the ruled
    form bypasses the transport guard by the ARGS diff (the same
    principal, the body's id changed) and hits the core's dedup on the
    VERIFIED id: the ORIGINAL's vote_id, the UNCHANGED count,
    acknowledged=true (one voice, never double-counted -- the
    fabricated-id dodge dead at the door, the self-claim never forks a
    voice).
    """
    _register(caller, _ITEMS)
    arguments: dict[str, Any] = {
        "run_id": _RUN_ID,
        "pair": ["a", "b"],
        "winner": "prefer-a",
        "comparator_id": "x",
        "comparator_class": "human",
    }
    first = _call(caller, "votes.cast", arguments)
    again = _call(caller, "votes.cast", {**arguments, "comparator_id": "imposter"})
    assert first.structured_content == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}
    assert again.structured_content == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": True}


def test_cast_changed_verdict_new_record(caller: str) -> None:
    """A changed verdict on the same pair => a new record, acknowledged=false, the count grown."""
    _register(caller, _ITEMS)
    first = _cast(caller, ["a", "b"], "prefer-a", "x")
    second = _cast(caller, ["a", "b"], "prefer-b", "x")
    assert first.structured_content == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}
    assert second.structured_content == {"vote_id": "VOTE-0002", "count": 2, "acknowledged": False}


def test_register_cross_session_new_run(caller: str) -> None:
    """A re-register from a fresh session => a NEW run minted (RUN-0002), never a replay."""
    arguments: dict[str, Any] = {"items": _ITEMS, "quorum": 1, **_OPERATOR}
    first = _call(caller, "runs.register", arguments)
    second = _call(f"face-{next(_CALLERS)}", "runs.register", arguments)
    assert first.structured_content == {
        "run_id": _RUN_ID,
        "count": 3,
        "quorum": 1,
        "verdicts": _VERDICTS,
    }
    assert second.structured_content == {
        "run_id": "RUN-0002",
        "count": 3,
        "quorum": 1,
        "verdicts": _VERDICTS,
    }


def test_cast_missing_stamp_refused(caller: str) -> None:
    """A cast without comparator_class => the schema's required-field refusal, the field named."""
    _register(caller, _ITEMS)
    result = _call(
        caller,
        "votes.cast",
        {"run_id": _RUN_ID, "pair": ["a", "b"], "winner": "prefer-a", "comparator_id": "x"},
    )
    assert result.is_error is True
    assert "`comparator_class` is required" in _join(result)


def test_register_duplicate_items_refused(caller: str) -> None:
    """A register with duplicate ids => the model's own items gate, the rule taught."""
    result = _call(caller, "runs.register", {"items": ["a", "a"], "quorum": 1, **_OPERATOR})
    assert result.is_error is True
    assert "items must be at least two, all unique, none empty" in _join(result)


def test_supersedes_same_pair_lands(caller: str) -> None:
    """A correction citing the original on the same pair => a new record, the count grown."""
    _register(caller, _ITEMS)
    _cast(caller, ["a", "b"], "prefer-a", "x")
    result = _cast(caller, ["a", "b"], "prefer-b", "x", supersedes="VOTE-0001")
    assert result.is_error is False
    assert result.structured_content == {"vote_id": "VOTE-0002", "count": 2, "acknowledged": False}


def test_supersedes_different_pair_refused(caller: str) -> None:
    """A correction citing a record on a different pair => the same-pair rule, the ThreePart."""
    _register(caller, _ITEMS)
    _cast(caller, ["a", "b"], "prefer-a", "x")
    result = _cast(caller, ["b", "c"], "prefer-a", "y", supersedes="VOTE-0001")
    assert result.is_error is True
    text = _join(result)
    assert "expected: a live VOTE-{####} handle in the same run, on the same pair" in text
    assert "'VOTE-0001'" in text
    assert "next_action: cite the record being corrected" in text


def test_seed_serves_the_same_pair(caller: str) -> None:
    """Two nexts with the same seed between casts => the same pair (the reserved seam inert)."""
    _register(caller, _ITEMS)
    first = _call(caller, "runs.next", {"run_id": _RUN_ID, "seed": 7})
    second = _call(caller, "runs.next", {"run_id": _RUN_ID, "seed": 7})
    assert first.structured_content is not None
    assert first.structured_content == second.structured_content


def test_default_order_stable_per_run(caller: str) -> None:
    """Two default nexts without casts => the same pair (the default order stable per run)."""
    _register(caller, _ITEMS)
    first = _call(caller, "runs.next", {"run_id": _RUN_ID})
    second = _call(caller, "runs.next", {"run_id": _RUN_ID})
    assert first.structured_content is not None
    assert first.structured_content == second.structured_content


def test_cast_llm_class_lands(caller: str) -> None:
    """A cast with comparator_class=llm => lands at equal weight (the census counts it)."""
    _register(caller, ["a", "b"])
    result = _call(
        caller,
        "votes.cast",
        {
            "run_id": _RUN_ID,
            "pair": ["a", "b"],
            "winner": "prefer-a",
            "comparator_id": "x",
            "comparator_class": "llm",
        },
        token=_granted(caller, comparator_class="llm"),
    )
    assert result.is_error is False
    assert result.structured_content == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}
    census = _call(caller, "votes.census", {"run_id": _RUN_ID})
    assert census.structured_content == {"total": 1, "items": {"a": 1, "b": 1}}


def test_cast_without_serve_lands(caller: str) -> None:
    """A cast on a pair runs.next never served => lands (a vote legal on any registered pair)."""
    _register(caller, _ITEMS)
    result = _cast(caller, ["b", "c"], "prefer-a", "x")
    assert result.is_error is False
    assert result.structured_content == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}


def test_census_as_is_after_correction(caller: str) -> None:
    """A census after a supersedes correction => the log counted AS-IS (total 2, both records).

    The census-vs-weighted seam named: the tally would weight one (the
    original superseded-excluded); the census reads the log whole -- the
    audit surface counts what has landed.
    """
    _register(caller, ["a", "b"])
    _cast(caller, ["a", "b"], "prefer-a", "x")
    _cast(caller, ["a", "b"], "prefer-b", "x", supersedes="VOTE-0001")
    result = _call(caller, "votes.census", {"run_id": _RUN_ID})
    assert result.is_error is False
    assert result.structured_content == {"total": 2, "items": {"a": 2, "b": 2}}


def test_next_serves_past_the_quorumed_pair(caller: str) -> None:
    """A next after the first pair reached quorum => the second pair, its own count 0.

    The count riding the pair it was found on: the cast pair's 1 never
    leaks onto the served pair's 0.
    """
    _register(caller, _ITEMS)
    _cast(caller, ["a", "b"], "prefer-a", "x")
    result = _call(caller, "runs.next", {"run_id": _RUN_ID})
    assert result.is_error is False
    assert result.structured_content == {
        "done": False,
        "item_a": "a",
        "item_b": "c",
        "count": 0,
        "presentation_order": "canonical",
        "expected": "",
        "found": "",
        "next_action": "",
    }


def test_the_sitting_end_to_end(caller: str) -> None:
    """The full sitting on two items => register, next, cast, done, census, tally, each leg asserted."""
    registered = _register(caller, ["a", "b"])
    assert registered.structured_content == {
        "run_id": _RUN_ID,
        "count": 2,
        "quorum": 1,
        "verdicts": _VERDICTS,
    }
    served = _call(caller, "runs.next", {"run_id": _RUN_ID})
    assert served.structured_content is not None
    assert served.structured_content["item_a"] == "a"
    assert served.structured_content["item_b"] == "b"
    cast = _cast(caller, ["a", "b"], "prefer-a", "x")
    assert cast.structured_content == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}
    _cast(caller, ["a", "b"], "prefer-a", "x", "llm")
    done = _call(caller, "runs.next", {"run_id": _RUN_ID})
    assert done.structured_content is not None
    assert done.structured_content["done"] is True
    census = _call(caller, "votes.census", {"run_id": _RUN_ID})
    assert census.structured_content == {"total": 2, "items": {"a": 2, "b": 2}}
    tally = _call(caller, "runs.tally", {"run_id": _RUN_ID})
    assert tally.structured_content is not None
    assert tally.structured_content["ranked_groups"] == [["a"], ["b"]]
    assert tally.structured_content["coverage"]["done"] is True


def test_re_tally_after_cure(caller: str) -> None:
    """A quorum-2 halt names the missing vote; the cure cast lands; the re-tally DONEs.

    The halt's refusal names the closing pair at the wire's visible head
    (the grown render pushes the needle's tail past the wire's 300-char
    clip -- the two-cap reality: the found's 10-cap never fires at one
    shortfall, the wire's 300-clip does); a second voter's cast closes
    it (the fresh comparator y -- a distinct judgment); the re-tally emits
    the ranked whole (the halt's progressive form: nothing remains).
    """
    registered = _register(caller, ["a", "b"], quorum=2)
    assert registered.structured_content == {
        "run_id": _RUN_ID,
        "count": 2,
        "quorum": 2,
        "verdicts": _VERDICTS,
    }
    _cast(caller, ["a", "b"], "prefer-a", "x")
    halted = _call(caller, "runs.tally", {"run_id": _RUN_ID})
    assert halted.is_error is True
    assert "cast the missing votes: (a, b) needs" in _join(halted)
    _cast(caller, ["a", "b"], "prefer-a", "y", "llm")
    cured = _call(caller, "runs.tally", {"run_id": _RUN_ID})
    assert cured.is_error is False
    assert cured.structured_content == {
        "ranked_groups": [["a"], ["b"]],
        "per_item_wins": {"a": 2, "b": 0},
        "per_item_losses": {"a": 0, "b": 2},
        "per_item_ties": {"a": 0, "b": 0},
        "coverage": {
            "components": [["a", "b"]],
            "cycle": [],
            "pairs_expected": 1,
            "pairs_at_quorum": 1,
            "done": True,
        },
        "algorithm_version": "win-rate-v1",
    }


@pytest.mark.parametrize(
    ("argv", "expected"),
    [
        pytest.param([], (("stdio",), cast("dict[str, object]", {})), id="bare-stdio"),
        pytest.param(
            ["--serve"],
            (
                ("http",),
                {
                    "host": "127.0.0.1",
                    "port": 8100,
                    "allowed_hosts": ["127.0.0.1", "localhost"],
                    "allowed_origins": [],
                },
            ),
            id="serve-defaults",
        ),
        pytest.param(
            ["--serve", "--host", "192.0.2.10", "--port", "9000"],
            (
                ("http",),
                {
                    "host": "192.0.2.10",
                    "port": 9000,
                    "allowed_hosts": ["127.0.0.1", "localhost", "192.0.2.10"],
                    "allowed_origins": [],
                },
            ),
            id="serve-overrides",
        ),
    ],
)
def test_parse_argv_derives_the_run_call(
    argv: list[str],
    expected: tuple[tuple[str, ...], dict[str, object]],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Parse main()'s argv form => the derived server.run call whole, the three forms parametrized.

    The lifecycle-integration arc (the brief §3, the one ruled Python arc):
    the argv widening is new branch logic with a changed default -- the bare
    form the member path byte-held (server.run("stdio"), no HTTP-form call,
    no kwargs); --serve alone the defaults (127.0.0.1:8100, the loopback
    pair); the overrides flowed and the host JOINED to allowed_hosts (a
    non-loopback bind unallowed is a silent Host-header 400). The run call
    captured per the file's fixture forms (monkeypatch's setattr; sys.argv
    via the string form, the tree's own precedent); the store never touched
    -- the parse is pure.
    """
    calls: list[tuple[tuple[str, ...], dict[str, object]]] = []

    def record(*args: str, **kwargs: object) -> None:
        """Record the derived run call's whole argument shape -- the assertion's ground."""
        calls.append((args, kwargs))

    monkeypatch.setattr("sys.argv", ["prioritree.mcp_server", *argv])
    monkeypatch.setattr(mcp_server.server, "run", record)
    mcp_server.main()
    assert calls == [expected]


def test_next_swap_presents_swapped(caller: str) -> None:
    """A next with swap=true => the presented pair swapped, presentation_order naming the form."""
    _register(caller, _ITEMS)
    result = _call(caller, "runs.next", {"run_id": _RUN_ID, "swap": True})
    assert result.is_error is False
    assert result.structured_content == {
        "done": False,
        "item_a": "b",
        "item_b": "a",
        "count": 0,
        "presentation_order": "swapped",
        "expected": "",
        "found": "",
        "next_action": "",
    }


def test_cast_swapped_presentation_lands(caller: str) -> None:
    """The cast on the served swapped pair carries the token — the ack lands, the field rode whole."""
    _register(caller, _ITEMS)
    result = _call(
        caller,
        "votes.cast",
        {
            "run_id": _RUN_ID,
            "pair": ["b", "a"],
            "winner": "prefer-a",
            "comparator_id": "x",
            "comparator_class": "human",
            "presentation_order": "swapped",
        },
    )
    assert result.is_error is False
    assert result.structured_content == {"vote_id": "VOTE-0001", "count": 1, "acknowledged": False}
    census = _call(caller, "votes.census", {"run_id": _RUN_ID})
    assert census.is_error is False
    assert census.structured_content == {"total": 1, "items": {"a": 1, "b": 1, "c": 0}}


def test_cast_presentation_refused_at_the_schema(caller: str) -> None:
    """A cast with presentation_order outside the Literal => the schema's gate, the typed form."""
    _register(caller, _ITEMS)
    result = _call(
        caller,
        "votes.cast",
        {
            "run_id": _RUN_ID,
            "pair": ["a", "b"],
            "winner": "prefer-a",
            "comparator_id": "x",
            "comparator_class": "human",
            "presentation_order": "sideways",
        },
    )
    assert result.is_error is True
    text = _join(result)
    assert "`presentation_order` must be one of" in text
    assert "expected:" not in text
