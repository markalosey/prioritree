# Copyright (C) 2026 Mark Losey. All rights reserved.
"""cli — the wrapper-tier command face: command the run at the command line.

The command-face unit (G-COMMAND-FACE, the approved brief the exact-task spec):
the five subcommands 1:1 on the five ops through the run-store ONLY — register
on Persist.register; next on Persist.load + .serve(seed); vote on Persist.load
+ .cast; state on Persist.load + .census; tally on Persist.load + .rank — no op
added, no op re-derived; the key tools group (prioritree key mint — the auth
foundation's issuance verb over the KEY store) is no run op (Q-cli-shape; the
frozen door cited). The I/O contract (Q-cli-io): argv in, stdout out, exit
0/1/2 — 0 success AND DONE (ExhaustedQueue caught BY TYPE, its full three-field
message on stdout), 1 the refusal lineage (the four typed refusals, str(e)
verbatim on stderr), 2 the argv+unexpected channel (argparse's SystemExit
propagates untouched; the traceback rides verbatim). The tier fence held by
construction: value-type imports only — Persist, StoreRefusedError, STORE_HOME,
OperatorDeclaration, the three refusals, ExhaustedQueue, KEYS_HOME, KeyStore,
KeyStoreRefusedError — no Registry()/Session() at this tier, no door
composition, no value re-derived (the CLI polices only its OWN argv syntax;
the door polices values). The report language: marker-first, tab-separated —
collision-free over opaque ids, first-token parseable. argparse stdlib ONLY
(zero runtime dependencies).
"""

from __future__ import annotations

import argparse
import sys
import traceback
from pathlib import Path
from typing import TYPE_CHECKING, Final, cast

from prioritree.key_store import KEYS_HOME, KeyStore, KeyStoreRefusedError
from prioritree.registry import OperatorDeclaration
from prioritree.run_store import STORE_HOME, Persist, StoreRefusedError
from prioritree.session import ExhaustedQueue
from prioritree.store_lock import Lock
from prioritree.tally import TallyRefusedError
from prioritree.votes import PRESENTATION_CANONICAL, VotesRefusedError

if TYPE_CHECKING:
    from collections.abc import Sequence

__all__ = ["command"]

# The five subcommand names (content-in-configuration — every grammar token a
# named constant, never inline logic).
REGISTER: Final[str] = "register"
NEXT: Final[str] = "next"
VOTE: Final[str] = "vote"
STATE: Final[str] = "state"
TALLY: Final[str] = "tally"

# The flag spellings.
FLAG_OPERATOR_ID: Final[str] = "--operator-id"
FLAG_QUESTION: Final[str] = "--question"
FLAG_QUORUM: Final[str] = "--quorum"
FLAG_SEED: Final[str] = "--seed"
FLAG_NOTES: Final[str] = "--notes"
FLAG_SUPERSEDES: Final[str] = "--supersedes"
FLAG_SWAP: Final[str] = "--swap"
FLAG_PRESENTATION_ORDER: Final[str] = "--presentation-order"
FLAG_HOME: Final[str] = "--home"

# The separators: the register token's id/label split (FIRST colon — labels
# may contain colons, ids may not, the accepted cost named) and the report
# language's field join.
ITEM_SEPARATOR: Final[str] = ":"
FIELD_SEPARATOR: Final[str] = "\t"
EDGE_SEPARATOR: Final[str] = ">"

# The report markers — the marker-first, tab-separated language's first tokens.
MARKER_PAIR: Final[str] = "pair"
MARKER_VOTE: Final[str] = "vote"
MARKER_ACK: Final[str] = "ack"
MARKER_VOTES: Final[str] = "votes"
MARKER_ITEM: Final[str] = "item"
MARKER_RANK: Final[str] = "rank"
MARKER_COUNTS: Final[str] = "counts"
MARKER_COVERAGE: Final[str] = "coverage"
MARKER_CYCLE: Final[str] = "cycle"
MARKER_PAIRS: Final[str] = "pairs"
MARKER_VERSION: Final[str] = "version"

# The exit codes (Q-cli-io): 0 success AND DONE; 1 the refusal lineage; 2 the
# argv+unexpected channel.
EXIT_OK: Final[int] = 0
EXIT_REFUSED: Final[int] = 1
EXIT_UNEXPECTED: Final[int] = 2

# The key region (the key-infrastructure unit, the exact-task spec
# synthesize/keyinfrastructurespec §3): the group/action tokens, the
# mint's flags, the report markers, the scopes split, and the landed
# mode render — additive; the five standing subcommands' own tokens
# untouched.
KEY: Final[str] = "key"
MINT: Final[str] = "mint"
FLAG_CLASS: Final[str] = "--class"
FLAG_SCOPES: Final[str] = "--scopes"
FLAG_AUDIENCE: Final[str] = "--audience"
MARKER_KEY: Final[str] = "key"
MARKER_DIGEST: Final[str] = "digest"
MARKER_MODE: Final[str] = "mode"
SCOPES_SEPARATOR: Final[str] = ","
MODE_LANDED: Final[str] = "0600"


def _report(line: str) -> None:
    """Render one report line to stdout.

    Purpose: the module's own ruled surface — print IS the command face's job;
    every stdout byte rides this one render function (the DONE message
    included), so the report language has ONE emission point.
    Refuses when: never.
    Re-run: deterministic — the bytes verbatim.
    Touches: stdout only.
    Provenance: command-face-brief §3 (the report language, DONE's bytes),
    Q-cli-io (stdout the success channel).
    """
    print(line)


def _report_error(line: str) -> None:
    """Render one refusal line to stderr.

    Purpose: the refusal channel's single render point — the three typed
    refusals' str(e) PASS-THROUGH bytes (the grammar already rendered; a
    re-render from fields yields identical bytes).
    Refuses when: never.
    Re-run: deterministic — the bytes verbatim.
    Touches: stderr only.
    Provenance: command-face-brief §3 (the refusals' pass-through), Q-cli-io
    (stderr the refusal channel).
    """
    print(line, file=sys.stderr)


def _build_parser() -> argparse.ArgumentParser:
    """Build the argv parser — the five subcommands, the key tools group, the shared --home parent.

    Purpose: the §2 grammar whole — a shared PARENT parser carrying --home
    (type=Path, default=STORE_HOME) attached to ALL FIVE subparsers (the
    AFTER-subcommand placement: argparse hands off at the subcommand token, a
    global-before flag dies after it — the footgun named, the alternative
    priced); register: items nargs="+" + --operator-id/--question required +
    --quorum type=int default 1; next: run_id + --seed type=int default None;
    vote: run_id, item_a, item_b, winner, comparator_id, comparator_class
    positionals + --notes/--supersedes default None; state and tally: run_id.
    key: the key tools group — its OWN nested add_subparsers(dest="action",
    required=True) carrying mint: comparator_id positional + --class (dest
    comparator_class, default human) + --scopes (required, a comma list the
    store validates) + --audience (default service), riding its OWN --home
    parent (default KEYS_HOME — the KEYS home, never conflated with the
    runs' STORE_HOME).
    No argparse choices= anywhere — door-validated values ride exit 1, never
    argparse's 2 (the fence held).
    Refuses when: never — the builder returns the parser; parse_args' own
    refusals ride argparse's channel.
    Re-run: deterministic — the same grammar each call.
    Touches: nothing — a pure construction.
    Provenance: command-face-brief §2 (the grammar, the --home placement
    ruling), Q-cli-shape, G-COMMAND-FACE.
    """
    parser = argparse.ArgumentParser(
        prog="prioritree",
        description="Command the run at the command line: register, next, vote, state, tally.",
    )
    parent = argparse.ArgumentParser(add_help=False)
    parent.add_argument(
        FLAG_HOME,
        type=Path,
        default=STORE_HOME,
        help="the store home (default: .prioritree/runs, CWD-relative)",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    register_parser = subparsers.add_parser(REGISTER, parents=[parent], help="register a run; print its RUN id")
    register_parser.add_argument(
        "items",
        nargs="+",
        help="item tokens, one per item: id:label (split on the FIRST colon)",
    )
    register_parser.add_argument(FLAG_OPERATOR_ID, required=True, help="the operator's id")
    register_parser.add_argument(FLAG_QUESTION, required=True, help="the comparison question")
    register_parser.add_argument(FLAG_QUORUM, type=int, default=1, help="votes per pair before coverage (default: 1)")
    next_parser = subparsers.add_parser(NEXT, parents=[parent], help="serve the next under-quorum pair")
    next_parser.add_argument("run_id", help="the run's RUN-{####} file stem")
    next_parser.add_argument(FLAG_SEED, type=int, default=None, help="the schedule seed (default: the door derives)")
    next_parser.add_argument(FLAG_SWAP, action="store_true", help="present the pair in the swapped order")
    vote_parser = subparsers.add_parser(VOTE, parents=[parent], help="cast one judgment")
    vote_parser.add_argument("run_id", help="the run's RUN-{####} file stem")
    vote_parser.add_argument("item_a", help="the served pair's first id, in the served order (canonical or swapped)")
    vote_parser.add_argument("item_b", help="the served pair's second id, in the served order (canonical or swapped)")
    vote_parser.add_argument("winner", help="the verdict, from the run's declared set")
    vote_parser.add_argument("comparator_id", help="who compared")
    vote_parser.add_argument("comparator_class", help="the comparator's class")
    vote_parser.add_argument(FLAG_NOTES, default=None, help="free-text notes (default: none)")
    vote_parser.add_argument(FLAG_SUPERSEDES, default=None, help="the vote id this cast corrects (default: none)")
    vote_parser.add_argument(
        FLAG_PRESENTATION_ORDER,
        default=PRESENTATION_CANONICAL,
        help="the presented order the pair was served in (default: canonical; swapped via next --swap)",
    )
    state_parser = subparsers.add_parser(STATE, parents=[parent], help="census the run's vote state")
    state_parser.add_argument("run_id", help="the run's RUN-{####} file stem")
    tally_parser = subparsers.add_parser(TALLY, parents=[parent], help="rank the run's whole")
    tally_parser.add_argument("run_id", help="the run's RUN-{####} file stem")
    key_parser = subparsers.add_parser(KEY, help="the key tools")
    key_sub = key_parser.add_subparsers(dest="action", required=True)
    keys_parent = argparse.ArgumentParser(add_help=False)
    keys_parent.add_argument(
        FLAG_HOME,
        type=Path,
        default=KEYS_HOME,
        help="the keys home (default: .prioritree/keys.jsonl, CWD-relative)",
    )
    mint_parser = key_sub.add_parser(MINT, parents=[keys_parent], help="mint one api key; print the plaintext ONCE")
    mint_parser.add_argument("comparator_id", help="the operator id the key names")
    mint_parser.add_argument(
        FLAG_CLASS,
        dest="comparator_class",
        default="human",
        help="the comparator's class (default: human)",
    )
    mint_parser.add_argument(FLAG_SCOPES, required=True, help="the granted scopes, a comma list the store validates")
    mint_parser.add_argument(FLAG_AUDIENCE, default="service", help="the key's audience tier (default: service)")
    return parser


def _command_register(args: argparse.Namespace, parser: argparse.ArgumentParser) -> int:
    """Register the run at the store; print the bare file stem.

    Purpose: the register path — split each item token on the FIRST colon
    (the CLI's OWN syntax check: a token without a colon is parser.error,
    exit 2; the EMPTY id passes through to the door's own exit-1 refusal —
    no value re-derived), then Persist.register(home, items,
    OperatorDeclaration(id=..., question=...), quorum) — the verdicts field
    the dataclass default's triple (no --verdicts flag: the door refuses any
    set but the triple — a no-op surface, never banked); print the BARE STEM
    (persist.run_id — the id IS the whole report). The register whole rides under
    one machine-wide file lock (store_lock.Lock, the flock seam), released before
    the stem renders.
    Refuses when: a colon-less item token (parser.error → SystemExit 2, the
    CLI's own channel); otherwise the door's refusals ride through (the
    handler's caller catches).
    Re-run: deterministic given the store home's state (the file-name mint
    continues the home's max).
    Touches: the store home and the new run file — through Persist.register
    only.
    Provenance: command-face-brief §2 (the items form), §3 (the bare stem),
    Q-cli-shape, G-COMMAND-FACE.
    """
    parsed_items: list[tuple[str, str]] = []
    for token in cast("list[str]", args.items):
        item_id, separator, label = token.partition(ITEM_SEPARATOR)
        if not separator:
            parser.error(f"each item token the id:label form (split on the FIRST colon) — got {token!r}")
        parsed_items.append((item_id, label))
    home = cast("Path", args.home)
    with Lock(home):
        persist = Persist.register(
            home,
            parsed_items,
            OperatorDeclaration(id=cast("str", args.operator_id), question=cast("str", args.question)),
            cast("int", args.quorum),
        )
    _report(persist.run_id)
    return EXIT_OK


def _command_next(args: argparse.Namespace) -> int:
    r"""Next the under-quorum pair at the store; print the serve triple.

    Purpose: load the run and serve its next under-quorum pair —
    Persist.load(home, run_id) then .serve(seed) with the --seed value passed
    verbatim (None included — the door derives when None, no re-derivation);
    print pair\t{item_a}\t{item_b}\t{count} — the serve triple whole. The load+serve
    window rides under one machine-wide file lock (store_lock.Lock, the flock
    seam), released before the pair line renders.
    Refuses when: never here — ExhaustedQueue rides through BY TYPE (the
    DONE signal, caught by the caller) and the refusals ride through (the
    caller's tuple clause).
    Re-run: deterministic given the run file — the same state serves the
    same pair.
    Touches: nothing — a read through the store.
    Provenance: command-face-brief §1 (the 1:1 map), §3 (the pair line),
    Q-cli-shape, G-COMMAND-FACE.
    """
    home = cast("Path", args.home)
    with Lock(home):
        persist = Persist.load(home, cast("str", args.run_id))
        item_a, item_b, count = persist.serve(cast("int | None", args.seed))
        if cast("bool", args.swap):
            item_a, item_b = item_b, item_a
    _report(FIELD_SEPARATOR.join((MARKER_PAIR, item_a, item_b, str(count))))
    return EXIT_OK


def _command_vote(args: argparse.Namespace) -> int:
    r"""Vote the judgment at the store; print the cast or the ack.

    Purpose: load the run and cast the judgment — Persist.load then .cast with
    the pair's two positionals in the served canonical order and the
    winner/comparator values passed through UNVALIDATED (the door's exit-1
    refusals — no re-derivation); the acknowledged flag picks the marker:
    ack\t{vote_id}\t{count} (the loud dedup ack) or vote\t{vote_id}\t{count}
    (a new cast). The load+cast window rides under one machine-wide file lock
    (store_lock.Lock, the flock seam), released before the vote/ack line renders.
    Refuses when: never here — the door's refusals ride through (the caller's
    tuple clause).
    Re-run: deterministic given the store state; a byte-identical re-cast is
    the door's ack.
    Touches: the run file — through Persist.cast only.
    Provenance: command-face-brief §2 (the vote grammar), §3 (the vote/ack
    lines), Q-cli-shape, G-COMMAND-FACE.
    """
    home = cast("Path", args.home)
    with Lock(home):
        persist = Persist.load(home, cast("str", args.run_id))
        vote_id, _record, count, acknowledged = persist.cast(
            [cast("str", args.item_a), cast("str", args.item_b)],
            cast("str", args.winner),
            cast("str", args.comparator_id),
            cast("str", args.comparator_class),
            cast("str | None", args.notes),
            cast("str | None", args.supersedes),
            cast("str", args.presentation_order),
        )
    marker = MARKER_ACK if acknowledged else MARKER_VOTE
    _report(FIELD_SEPARATOR.join((marker, vote_id, str(count))))
    return EXIT_OK


def _command_state(args: argparse.Namespace) -> int:
    r"""State the run's census at the store; print the summary lines.

    Purpose: load the run and census it — Persist.load then .census(); print
    votes\t{total} (total = len(census.vote_log) — the log IS the votes), then
    item\t{id}\t{count} per item in the MAP'S OWN iteration order (the door's
    construction is deterministic; the CLI adds no sort), zeros INCLUDED
    (an elided zero is indistinguishable from an absent item). Elided by
    ruling: per_pair_counts (the weighted view renders at tally), vote_log
    (recorded_at re-mints at load — rendering re-minted stamps lies),
    census.run_id (the in-file handle never crosses the CLI). The load+census
    window rides under one machine-wide file lock (store_lock.Lock, the flock
    seam), released before the summary lines render.
    Refuses when: never here — the door's refusals ride through.
    Re-run: pure — re-reading is stable between casts.
    Touches: nothing — a read through the store.
    Provenance: command-face-brief §3 (the census summary), Q-cli-io, Q-cli-shape,
    G-COMMAND-FACE.
    """
    home = cast("Path", args.home)
    with Lock(home):
        persist = Persist.load(home, cast("str", args.run_id))
        census = persist.census()
    _report(FIELD_SEPARATOR.join((MARKER_VOTES, str(len(census.vote_log)))))
    for item_id, item_count in census.per_item_counts.items():
        _report(FIELD_SEPARATOR.join((MARKER_ITEM, item_id, str(item_count))))
    return EXIT_OK


def _command_tally(args: argparse.Namespace) -> int:
    r"""Tally the run's ranking at the store; print the frozen whole.

    Purpose: load the run and rank it — Persist.load then .rank(); render the
    TallyResult WHOLE, every field (the frozen whole, tie groups and coverage
    counts included): rank\t{id}\t{id}... one line per group (the line boundary
    IS the tie-group boundary); counts\t{id}\t{wins}\t{losses}\t{ties} per
    item (map order, zeros included); coverage\t{len(components)}\t{done};
    cycle\t{a>b}\t{b>c}... ONLY when non-empty (a cycle is structural, named
    never hidden); pairs\t{a}\t{b}\t{n} per pair (the WEIGHTED counts, map
    order); version\t{algorithm_version}. The load+rank window rides under one
    machine-wide file lock (store_lock.Lock, the flock seam), released before
    the ranked whole renders.
    Refuses when: never here — TallyRefusedError (the SAFE HALT) rides
    through VERBATIM (the caller's tuple clause).
    Re-run: pure — same store state yields the byte-identical emission.
    Touches: nothing — a read through the store.
    Provenance: command-face-brief §0 (the convergence — the frozen whole),
    §3 (the tally lines), Q-cli-shape, G-COMMAND-FACE.
    """
    home = cast("Path", args.home)
    with Lock(home):
        persist = Persist.load(home, cast("str", args.run_id))
        result = persist.rank()
    for group in result.ranked_groups:
        _report(MARKER_RANK + FIELD_SEPARATOR + FIELD_SEPARATOR.join(group))
    for item_id in result.per_item_wins:
        _report(
            FIELD_SEPARATOR.join(
                (
                    MARKER_COUNTS,
                    item_id,
                    str(result.per_item_wins[item_id]),
                    str(result.per_item_losses[item_id]),
                    str(result.per_item_ties[item_id]),
                ),
            ),
        )
    _report(FIELD_SEPARATOR.join((MARKER_COVERAGE, str(len(result.coverage.components)), str(result.coverage.done))))
    if result.coverage.cycle:
        _report(
            MARKER_CYCLE
            + FIELD_SEPARATOR
            + FIELD_SEPARATOR.join(f"{source}{EDGE_SEPARATOR}{target}" for source, target in result.coverage.cycle),
        )
    for pair, pair_count in result.coverage.pair_counts.items():
        _report(FIELD_SEPARATOR.join((MARKER_PAIRS, pair.item_a, pair.item_b, str(pair_count))))
    _report(FIELD_SEPARATOR.join((MARKER_VERSION, result.algorithm_version)))
    return EXIT_OK


def _command_key_mint(args: argparse.Namespace) -> int:
    r"""Mint one api key at the key store; print the plaintext ONCE.

    Purpose: the key region's one action — compose KeyStore(home) (the
    construction IS the boot's compose: a corrupt or world-writable store
    refuses here, BY TYPE) and ride the store's OWN mint ceremony (the CLI
    never re-implements: the argument gates, the 256-bit key, the
    sort_keys line, the chmod 0600 all the store's); the --scopes value
    split on the comma here (the SPLIT the CLI's own; the TOKENS the
    store validates — no argparse choices=, the fence held); the whole
    mint under one machine-wide file lock over the keys home's PARENT
    directory (store_lock.Lock, the flock seam — the lock derives a
    directory; the keys home is a file inside it), released before the
    report renders. The report: key\t{key} on the first line, then
    digest\t{digest} then mode\t0600 — the plaintext shown ONCE
    (marker-first, tab-separated via _report; the key NEVER written,
    only the sha256 digest rides the file).
    Refuses when: never here — KeyStoreRefusedError rides through BY
    TYPE (the caller's exit-1 tuple clause).
    Re-run: the mint is random by design (a re-mint a NEW key, never a
    replay); the report's form deterministic.
    Touches: the keys home, its parent directory, and the lockfile —
    through KeyStore.mint and the Lock seam only.
    Provenance: the exact-task spec synthesize/keyinfrastructurespec §3
    (the key region, the report's bytes); the command-face precedent
    (the five handlers' school); the naming law.
    """
    home = cast("Path", args.home)
    scopes = cast("str", args.scopes).split(SCOPES_SEPARATOR)
    with Lock(home.parent):
        store = KeyStore(home)
        key, digest = store.mint(
            cast("str", args.comparator_id),
            cast("str", args.comparator_class),
            scopes,
            cast("str", args.audience),
        )
    _report(FIELD_SEPARATOR.join((MARKER_KEY, key)))
    _report(FIELD_SEPARATOR.join((MARKER_DIGEST, digest)))
    _report(FIELD_SEPARATOR.join((MARKER_MODE, MODE_LANDED)))
    return EXIT_OK


def command(argv: Sequence[str] | None = None) -> int:
    """Command the run at the command line — argv in, stdout out, the exit code out.

    Purpose: the console-script entry — argv None → sys.argv[1:]; parse the
    §2 grammar, dispatch to the 1:1 handler, and apply THE EXIT-CODE MAPPING
    in order: (1) ExhaustedQueue BY TYPE → print(str(done)) to STDOUT → 0
    (the full three-field message — DONE is success, scripts read stdout);
    (2) the typed refusals (StoreRefusedError, VotesRefusedError,
    TallyRefusedError, KeyStoreRefusedError) in ONE tuple clause BY TYPE →
    str(e) verbatim on stderr → 1 (the pass-through); (3) except Exception
    → the traceback verbatim on stderr → 2 (the unexpected is unanticipated
    by definition — the traceback is the only honest rendering); SystemExit
    propagates UNTOUCHED (BaseException — argparse's own channel, exit 2
    by construction, the CLI's own parser.error riding the same channel).
    Refuses when: never — every failure is mapped to its ruled exit code.
    Re-run: deterministic given the store state for the five ops — the
    door's semantics ride through verbatim; the key region's mint random
    by design (the store's own re-mint law).
    Touches: the store home and run files — through the run-store's verbs
    only; the keys home at the key region — through KeyStore.mint only;
    stdout and stderr per the mapping.
    Provenance: the act's first word (the naming law), command-face-brief
    §1 (the entry), §3 (the exit-code mapping), Q-cli-shape, Q-cli-io,
    G-COMMAND-FACE; the exact-task spec synthesize/keyinfrastructurespec
    §3 (the key region's dispatch + the tuple clause's widening).
    """
    parser = _build_parser()
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])
    try:
        if args.command == REGISTER:
            code = _command_register(args, parser)
        elif args.command == NEXT:
            code = _command_next(args)
        elif args.command == VOTE:
            code = _command_vote(args)
        elif args.command == STATE:
            code = _command_state(args)
        elif args.command == KEY:
            code = _command_key_mint(args)
        else:
            code = _command_tally(args)
    except ExhaustedQueue as done:
        _report(str(done))
        return EXIT_OK
    except (StoreRefusedError, VotesRefusedError, TallyRefusedError, KeyStoreRefusedError) as refusal:
        _report_error(str(refusal))
        return EXIT_REFUSED
    except Exception:
        traceback.print_exc()
        return EXIT_UNEXPECTED
    return code
