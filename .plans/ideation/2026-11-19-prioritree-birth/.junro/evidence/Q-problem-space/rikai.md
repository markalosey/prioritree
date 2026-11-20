# rikai — Q-problem-space: the product's Problem Space (solution-neutral)

- Packet: scope/pspace · Seat: rikai (理解, understand) · Route: prioritree-birth · Date: 2026-11-19
- Ground: Q-purpose's ruling (junro.json:429-434, README.md:3-9), Q-setup-arch's ruling (junro.json:442-447, README.md:13-18), the product naming at G-BIRTH-RECORDS (junro.json:209), FR-MEM-0001, the FR-MEM-0143 re-fire note (junro.json:474). Absence stated as fact: the product is unborn on disk — no items, comparison operator, pair scheduling, votes, or tally exist anywhere in src/ (src/prioritree/__init__.py:2; foundations-brief.md:382).
- Landed: shinko via patch, 2026-11-20; the in-message return's transit truncation at [OPEN] item 11 was recovered by session resume the same day; read-back verified.

## 1. The core state transition (Input → Output)

IN [STATED]: (a) any list of items, (b) any comparison operator ("for any list and comparison operator" — junro.json:434; README.md:3), (c) the votes, gathered during the run — "votes are data in/out" (junro.json:442; README.md:15).

The state machine — five sub-mechanisms [STATED as the core's named parts, junro.json:209/:442; README.md:15] chained in the ruling's own verb sequence ("run the pairwise permutations → store the votes, then tally" — README.md:7):

1. items loaded — the list enters as data; the item set is the round's universe [STATED: items named; DERIVED: the set precedes scheduling].
2. pairs scheduled — "pair scheduling" [STATED, named]; the schedule is the pairwise permutations of the item set under the operator [STATED, README.md:7]. Whether "permutations" means the n(n−1)/2 unordered pairs or the n(n−1) ordered pairs is [OPEN].
3. votes appended — a comparator answers a scheduled pair through the one vote interface, human AND LLM alike [STATED — junro.json:429; README.md:5]; "Storing the votes" [STATED, README.md:7]. The vote store is the only accumulating state [DERIVED — the core is "stateless scoring/ranking" (STATED, junro.json:442) and the tally is pure, so no other state may hold the round].
4. tally — a pure function of the stored votes [STATED — junro.json:429; README.md:5]. Mechanism consequence [DERIVED]: the tally reads only votes — not the operator, not the schedule — so identical votes ⇒ identical rank, always. The tally is operator-agnostic: the operator's semantics act at vote-generation (the comparators apply it), never at tally time [DERIVED from the purity statement].
5. rank emitted — "we get a list out that is in a superior order" [STATED, README.md:7]; "a ranked whole" [STATED, AGENTS.md:4].

OUT [STATED]: the ordered list — the ranking is the whole output. Whether scores/confidence ride with it is [OPEN].

Character [DERIVED]: a run is two-phase — a growing phase (schedule → ask → append, looping while unvoted pairs remain) and a pure phase (tally → emit, no mutation). The repo's own precedent for this exact data shape: "append-only JSONL; state is a FOLD over the file, never a rewrite" (friction_ledger.py:46). Layering [STATED]: the machine lives in src/prioritree; CLI wraps, FastAPI serves, web fronts ("the human comparator's vote surface" — junro.json:442; README.md:15-18). The human's wiring is stated; the LLM comparator's wiring at the upper tiers is [OPEN].

## 2. The input entropy (vote-stream noise/edge/ambiguity classes)

Stated premise: discernment between two items is "easy"/"far better" for humans and LLMs; absolute sizing is not (junro.json:429; AGENTS.md:4) — a comparative claim, not a perfection claim. Classes the stream can carry:

1. Comparator error (human AND LLM) — [DERIVED]: a judgment channel with nonzero error on both classes; the repo has ruled no error model (absorbed noise vs detected contamination: [OPEN]).
2. Intransitive cycles (A>B, B>C, C>A) — [DERIVED, structural]: pairwise judgments need not aggregate to a total order (Condorcet cycles). Purity guarantees determinism, not the existence of a consistent total order — cycle resolution is [OPEN]. The deepest class: it can make "a ranked whole" ill-defined for some vote sets.
3. Ties / abstentions — [OPEN]: the vote interface's outcome vocabulary (binary choice? "no difference"? "no judgment"?) is unruled.
4. Duplicate votes — [DERIVED]: the stream is append-shaped; whether a repeat vote by the same comparator on the same pair counts twice or is idempotent is [OPEN].
5. Incomplete pair coverage — [DERIVED, structural]: a round can halt with k of the scheduled permutations voted; partial-emit policy is [OPEN].
6. Item-set mutation mid-round — [DERIVED]: items are data in [STATED]; no ruling freezes the set for a round; votes reference item identities and can dangle — freezing is [OPEN].
7. Ambiguous comparison operators — [STATED-adjacent]: the operator is generalized input (README.md:7). [DERIVED]: since the tally never interprets the operator (§1), operator ambiguity degrades the votes (the comparators misjudge) while the tally faithfully ranks the misjudgments; whether any operator validation exists is [OPEN].
8. Mixed human+LLM streams — the same interface for both is [STATED — junro.json:429; README.md:5]; same weight is [OPEN] — interface sameness does not rule weight sameness, and whether a vote carries comparator-class provenance at all is [OPEN].
9. Adversarial votes — [DERIVED]: a judgment interface with two comparator classes and no stated trust boundary; no policy ruled [OPEN].
10. Degenerate inputs — [DERIVED]: empty list, single item (zero pairs), duplicate items; behavior unruled [OPEN].

## 3. Hard environmental constraints and irreversible failure modes

Constraints [STATED]: tally purity (junro.json:429; README.md:5) — the one ruled core invariant; pure-logic data plane — stateless scoring/ranking, votes data in/out, no DB at birth, persistence explicitly deferred to a service-tier ruling (junro.json:442; on disk: dependencies = [], pyproject.toml:7, tied to the ruling at understand/foundations.md:35); git-tracked record state — the efforts' stores live in .plans, git-tracked, the record home; NO worktrees (seat law, rikai.md:44-45); the root-anchored /.junro/ ignore (.gitignore:183) leaves nested store hearts tracked by default (the ruling, junro.json:389); append-only record discipline — stated as the family's own mechanism ("append-only JSONL; state is a FOLD over the file, never a rewrite" — friction_ledger.py:46; "append-only is a property of the op set, not of filesystem permissions" — :10; "the only mutable state; append-only, locked appends" — :250), its application to the product's vote store is [DERIVED-precedent → OPEN]; the construction environment — the product builds under the kumi harness, patch the one mutation verb, zero-ignore strictness (junro.json:455; rikai.md:50-60).

Learned hazards [STATED]: Parallel-write races — the FR-MEM-0143 class (the re-fire note, junro.json:474): two route-ops fired in a parallel block into one record store; both returned OK; the amendment's write clobbered the ruling's record — "SILENTLY LOST"; caught only by an independent census read-back; "the race strikes cross-op pairs, not just same-op batches — any parallel route-op pair is unsafe." Mechanism [DERIVED]: unsynchronized read-modify-write; success-return ≠ durable landing; detection requires read-back, not the write path's word. Product relevance [DERIVED]: a vote interface serving human AND LLM is by design a multi-actor surface — concurrent appends to one vote store are the expected case; the family's own cure is stated: "locked appends" (friction_ledger.py:250).

Unverified payload data-gaps — FR-MEM-0001 (.plans/state/friction-ledger.jsonl:1): a fenced payload inherited from an upstream record was landed unverified against the ruled ground truth; the executor's read-back caught it ("resolves to /Users/marklosey/projects/kepric/prioritree — a path that does not exist"); had it ridden through, "a stray tree birthed... the emission split from the configured tree." Mechanism [DERIVED]: data entering an act without a ground-truth verification step; the write path accepts it. Product relevance [DERIVED]: the vote stream is exactly such a payload surface; whether a vote is verified against its scheduled pair before it counts is [OPEN].

What is irreversible [DERIVED, from stated premises]: The votes are the single irreducible state. Purity ⇒ tally and rank are always recomputable from the vote store; nothing derives votes from anything else — they are empirical judgments of human/LLM comparators. Vote-ledger loss/corruption is the one loss that cannot be recomputed: it forces re-asking, and re-asked judgments are new facts, not the old ones. Git-tracked store homes recover committed votes; the uncommitted window is the irreducible risk. A bogus rank emitted and consumed downstream: the rank is the product's entire output; a wrong order acts downstream as if true. Asymmetry: a refused emission costs a re-run; a bogus emission costs every decision made on the false order. No consistency/quorum bar is ruled [OPEN] — that absence is a finding. Split/divergent ledgers: the family already paid this tuition (FR-MEM-0001's effect: the stray-tree/split-emission counterfactual). Purity dividend: identical votes ⇒ identical rank, so any rank divergence between two copies is proof of store divergence — the tally doubles as a divergence detector. The silent-loss mode itself: a write can return OK and be gone; without an independent read-back census in the loop, loss is silent and permanent.

## 4. The exact binary terminal states

"DONE": [STATED] the output is an ordered list produced by tally over stored votes (README.md:7; AGENTS.md:4) — that is all that is ruled about the output. [DERIVED] the natural completion reading is full pair coverage (the ruling's verb: run the permutations, then tally). [OPEN] every done-predicate: coverage required vs partial-emit; quorum (votes per pair); consistency (must the aggregate be cycle-free before emission?). The repo's own done-shape [STATED pattern]: done is a recorded ruling over enumerated gate conditions, never self-declared (junro.json:210; the gates at :184-226); [DERIVED] the analog — a rank is done when the vote record it rests on is whole; "no claim without evidence on disk" is the law this derives from.

"SAFE HALT": [STATED precedent — the repo's refusal grammar, on disk]: every harness engine refuses with expected / found / next-action (curate.py:124-130; calculate.py:63-69; patch.py:70-74 — "a failed match is the CALLER's loop: the refusal carries expected/found/next-action with the actual current lines as evidence", patch.py:16-17); find-before-create refusals name the legal sets; patch refuses protected surfaces including append-only ledgers (patch.py:112). [STATED law as the direct analog]: "Never return an empty final message — a report saying 'not started' is a legitimate completion; silence is not" — a named refusal is a legitimate terminal state; silence never is. [DERIVED]: the product's safe halt is the tally's refusal to emit, carrying expected (the scheduled coverage), found (the actual vote state), next-action (the missing votes). Whether the terminal space is strictly binary (no partial/confidence-annotated emission between the two) is [OPEN] — the gate pattern is binary (green / not green), but no product ruling exists.

## [OPEN] — the gaps needing the collaborator's ruling

1. Done-predicate for coverage: full permutation coverage required, or may partial coverage emit?
2. Quorum: votes per pair — single vote or multiple; majority/merging rules.
3. Comparator weight: same interface is ruled, same weight is not; does a vote carry comparator-class provenance at all?
4. Vote outcome vocabulary: binary choice only, or ties/abstentions?
5. Cycle resolution: what does the tally emit when stored votes form intransitive cycles (A>B, B>C, C>A) — a total order may not exist?
6. Duplicate/repeat votes: idempotency policy for the same comparator answering the same pair twice.
7. Item-set mutation mid-round: is the set frozen for a round; the fate of votes referencing mutated items.
8. The permutation set's shape: unordered pairs (n(n−1)/2) or ordered pairs (n(n−1))? "Pairwise permutations" is ambiguous.
9. Vote-store discipline at the library tier: the library is stateless, votes data in/out — the container/record discipline (append-only? locked appends? the FR-MEM-0143 cure) is unruled; persistence is deferred to the service tier [STATED], but the library's contract for the vote container is not.
10. Adversarial-vote policy: any validation/trust boundary on the stream (votes for unscheduled pairs; voting outside one's round).
11. Safe-halt predicates: the exact refusal conditions (insufficient coverage? detected inconsistency?), and whether the terminal space is strictly binary — a refusal carrying expected/found/next-action versus an emission, with no partial or confidence-annotated emit between the poles (the gate pattern's green/not-green shape suggests binary; no product rule exists).
12. Degenerate inputs: the empty list, the single item (zero pairs — trivial rank or refusal?), and duplicate items — the behavior is unruled (flagged at §2, class 10).
13. The emission's form: the ruled output is the ordered list alone; whether scores, per-item vote counts, confidence, or cycle annotations ride with the order is unruled (flagged at §1).

- Evidence disposition (at execution): rikai's pack (read/glob/grep/calculate/friction/test) carries no write verb, so the full evidence returned in-message per the packet's fallback clause; the tail truncated in transit (items 11-13) was recovered by session resume 2026-11-20 and lands complete here.
