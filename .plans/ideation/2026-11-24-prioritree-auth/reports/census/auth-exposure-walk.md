<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/auth-exposure-walk

**Route:** prioritree-auth (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-24T06:22:25Z |
| 2 | report | moho | 2026-11-24T06:27:49Z |
## Reported by moho — 2026-11-24T06:27:49Z

THE AUTH EXPOSURE WALK — the serving tiers walked as the attacker, no help. Every finding below came from the surfaces themselves (the served routes, the live calls, the on-disk files), never from the guides.

1. THE BIND (the honest limit): HOST ?= 127.0.0.1 on :8000, MCP the same on :8100 — loopback-only. The remote network is blocked; the malicious-colleague class (any process on this machine) owns every surface. The browser is a bridge (finding 7).

2. THE REACH: 6 JSON routes + 9 web routes + 5 MCP tools — NONE of the twenty asks for a credential. Identity everywhere is a self-declared string: operator_id, comparator_id ("Your name for yourself" / "pick one id and keep it") — the honor system is the only authentication.

3. ENUMERATION IS SERVED: an unknown-stem read refuses with "live: RUN-0001, RUN-0002, ..." — the refusal's expected field renders the whole live set. No guessing needed; the reconnaissance oracle is a designed feature (5 live sittings on this machine today).

4. THE WRITE ATTEMPT (the code's own contract; this walk minted nothing): POST /runs mints RUN-{max+1} for any caller — the 201 ack hands the stem back. votes.cast lands on ANY run by its stem, on ANY registered pair ("a vote is legal on any registered pair — no serve needed"), with a fabricated comparator_id and a self-picked class from {human, llm}; over-quorum votes land as legal samples; supersedes takes ANY live vote in the run — no comparator check — and the tally EXCLUDES the superseded: an attacker replaces a victim's judgment with their own and the ranked whole flips while the log still looks append-only-honest.

5. THE READ ATTEMPT (LIVE, through the anonymous MCP surface): the census of RUN-0001 served the operator's audit (total 0, {Tony: 0, Jack: 0}) — no credential asked; the tally's safe-halt served the shortfall roadmap ("under-quorum pairs: (Jack, Tony) 0 of 1; cast the bridging pairs...") — the attacker's poison to-do list; the manifest serves any run's question, items, quorum; the JSONL files carry operator ids, questions, comparator ids, notes in cleartext to anyone on the machine (RUN-0001: operator "beauty", "Who is prettier?").

6. THE WEB TIER: no session, no cookie, no CSRF token anywhere — the browser surface is anonymous by construction. The register form mints runs in-process; the sitting page's comparator entry is a free text field; the sitting URL is handed out as "shareable". Quorum's story ("2 or more means you need other judges") is unenforceable — the judges are strings.

7. THE BROWSER BRIDGE (the remote vector through the loopback): the /ui/ POST routes parse plain form bodies with NO CSRF token — a remote page can drive-by mint runs (POST /ui/register) and poison sequential stems (POST /ui/runs/RUN-000N/vote) while the server runs. The loopback bind blocks reading, not writing.

8. THE COST MAP: (a) MINT POLLUTION — every fabricated run shifts the RUN-{####} counter (max+1, "the dir is the truth"): every later legitimate registration lands on a shifted stem, and the refusal-rendered live set grows with it; the wire takes unbounded item lists — N items mint N(N-1)/2 pairs, a crafted run makes the halt's enumeration O(n^2) on the wire. (b) SITTING POISON — one fabricated voter completes ANY quorum-1 sitting alone; k fabricated ids defeat any quorum k; changed-verdict re-votes both count (drowning). (c) AUDIT EXPOSURE — the operator's census (the progress page's 5s poll) is world-readable on the machine: a colluding judge watches counts move and steers (the anchoring hazard); the halt arms them with the shortfall map. (d) TRUST EROSION — the product's public story (independent human and LLM judges, provenance stamps, quorum as corroboration) is unenforced at every tier: the trust model is "nobody helps the attacker" — exactly the case this walk was asked to break.

Nothing was minted, cast, or superseded by this walk (READ-ONLY held); every write finding is the served code's own contract, every read finding served live.
