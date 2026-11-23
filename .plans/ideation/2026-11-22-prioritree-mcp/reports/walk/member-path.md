<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — walk/member-path

**Route:** prioritree-mcp (executing) | **Events:** 8 | **Reports:** 3

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T16:22:20Z |
| 2 | dispatch | shinko | 2026-11-23T16:36:44Z |
| 3 | report | moho | 2026-11-23T16:41:22Z |
| 4 | result | shinko | 2026-11-23T16:41:43Z |
| 5 | dispatch | shinko | 2026-11-23T16:47:18Z |
| 6 | report | moho | 2026-11-23T16:50:51Z |
| 7 | result | shinko | 2026-11-23T16:52:55Z |
| 8 | report | moho | 2026-11-23T17:29:17Z |
## Reported by moho — 2026-11-23T16:41:22Z

moho (盲歩) — packet walk/member-path — the report of what was, not a new act.

ARRIVED AT: my session's granted surface held my pack routing — calculate, friction, glob, grep, junro (packet report only), read, test — and at no point any prioritree MCP tool. The five walk ops (register, next, cast, census, tally) never appeared in my toolset; their names and descriptions never served me. The walk's instrument was absent before any step.

DID: no walk was performed. No register attempt fired, no sitting step (next/cast) ran, no comparator_id was ever chosen — the choice the dispatch names never arrived at a surface I could call. What my session's context actually holds is one read-only exchange delivered to this same session framed as tansa's ground-verification asks: a glob on .prioritree/runs, reads of opencode.json (lines ~495-598), greps over .opencode/prompts/seats. Those reads are the only acts in my context — verification reads, not walk steps.

ENCOUNTERED, the returns as I got them: (1) the first glob on ".prioritree/runs/*" returned "No files found"; a direct read of the .prioritree directory then listed runs/ holding RUN-0001..RUN-0004 and .prioritree.lock — the glob surface missed the dot-tree's contents until the directory read revealed them. (2) RUN-0004.jsonl's manifest head (line 1) names operator "shinko", quorum 1, three live-check pairs, registered_at 2026-11-23T16:21:48Z — but its run_id field reads "RUN-0001", the filename and the manifest disagreeing, and RUN-0001.jsonl itself holds a different, older run (operator "beauty", 2026-11-22). (3) Anchoring, plainly observed, never investigated: every call I hold landed in /Users/marklosey/projects/prioritree — the project's own opencode.json, its .prioritree/runs, its seats prompts. I observed no call anchored to any other tree or home directory.

EASE-OF-USE, as experienced: the walk's ease-of-use question never opened — no prioritree tool served me, so I hold no unaided teaching from register/next/cast. The only teaching my session carries comes from the reads: trust the directory read over glob for dot-directories, and read the manifest's run_id field, never the filename's number.

HONEST HEADLINE: the session cancelled (or the surface never attached) before the first walk act. Nothing was registered, nothing sat, nothing was cast. This report is what remains of the journey.
## Reported by moho — 2026-11-23T16:50:51Z

THE HONEST HALT AT ARRIVAL — moho's blind walk of walk/member-path, 2026-11-23.

ARRIVAL, what the names alone taught: prioritree_runs_register / runs_next / votes_cast / votes_census / runs_tally — two nouns (runs, votes) and a sequence that reads itself: register a run, ask the next pair, cast which is greater, repeat, tally the ranked whole, census the audit. A pairwise-comparison ranker: judgments as votes, tallies as order.

THE HALT, what the unaided walk found: the session does NOT carry the five tools. The callable surface is ten tools — calculate, friction, glob, grep, junro, list_mcp_resources, list_mcp_resource_templates, read, read_mcp_resource, test — and none is prioritree_*. The only live connection serves hikari-local and hikari-prod, a different product (query algebra, deliverables, provenance surfaces). No prioritree server, no prioritree resource.

THE REFUSAL HARVEST, verbatim: reaching for the register through the only bridge (read_mcp_resource, server "prioritree", uri "prioritree://runs/register") returned only: "Failed to read MCP resource: prioritree/prioritree://runs/register". A mute refusal — no expected/found/next-action, no list of what IS served. The two listing calls (list_mcp_resources, list_mcp_resource_templates) were the only teachers, and they confirmed absence.

REGISTER, SITTING, TALLY, CENSUS: all unreachable. No schema served, no tool-side refusal to read — the tools that would teach are not in the room. The walk cannot even fail informatively; it fails by absence.

EASE-OF-USE VERDICT (G-MEMBERPATH evidence): the break is upstream of the tool surface — the handoff, not the tools. A walker dispatched with a five-tool manifest arrives to find none seated. Nothing errored at dispatch, nothing named the gap, and the mute refusal corrected nothing. Worst failure class: silent absence, discoverable only by exhausting the session's listing verbs. For the member path: a dispatch-time check that the granted tool manifest matches the seated session would have caught this before the walk began.
## Reported by moho — 2026-11-23T17:29:17Z

THE LIVE WALK (RUN-0005) — blind, end-to-end, zero help, zero refusals.

1. Register taught by ack: quorum default held (k=1), verdicts echoed (prefer-a / prefer-b / tie, positional over the served order) BEFORE the first serve. run_id carried to every later call exactly as the ack instructed.
2. The sitting: 4 items, 6 pairs, served one at a time; each cast acked a vote_id and running count. acknowledged:false on first sends — the one-voice re-send grammar the schema taught, confirmed by the acks.
3. done:true arrived exactly at quorum, carrying the three-part grammar as data (expected / found / next_action) — the tool told me when to stop and what to do next. expected: "all 6 scheduled pairs at quorum k=1"; found: "the queue is exhausted".
4. The one naming seam: done:true's next_action said "call tally_rank(run_id)" and cited "R12's DONE" and "a census-vs-weighted seam" — internal vocabulary no served surface defines. I mapped "tally" by its verb; a stranger might not. THIS is the walk's single roughness.
5. Tally returned the ranked whole (nuts > banana > chocolate > jerky), per-item wins/losses/ties, coverage (one component, no cycle, 6/6 pairs at quorum, done), algorithm_version win-rate-v1 — self-describing; no help needed.
6. Census returned total 6 and per-item counts 3/3/3/3 — appearances, not wins. Beside the tally it reads as coverage evidence ("what has landed, never what should have"), but alone the number could surprise a walker expecting win tallies.

EASE-OF-USE VERDICT: the five tools walked blind end-to-end without one refusal; the sequence is legible from names and descriptions alone; the acks teach each next step. Single friction: the done:true payload references an untaught world (tally_rank / R12 / census-vs-weighted seam).
