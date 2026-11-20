# Fleet pack census — the regenerated opencode surface (packet scope/pack-census)

- Date: 2026-11-19 (fired after the opencode surface regeneration + restart)
- Packet: scope/pack-census · Member: shinko (convenor; the census executes at shinko's hand) · Route: prioritree-birth
- Question home: Q-problem-space (the web-validation lane's unblock state)
- Friction lane: FR-MEM-0002 (origin) → FR-MEM-0003/0004/0005/0006 (the four validation walls, filed by tansa)

## The fleet table (13 seats, live surfaces)

| Seat | Live tool surface | Web (surface) |
|---|---|---|
| shinko (self-report) | friction, git (sync/drift/land/discard/move), junro, patch, task, web | PRESENT |
| tansa | base 9 + web | PRESENT |
| jikko | base 9 + patch, curate, lint | absent |
| keikaku | base 9 + junro | absent |
| hansei | base 9 | absent |
| hyoka | base 9 | absent |
| keisan | base 9 | absent |
| kensho | base 9 | absent |
| moho | base 9 | absent |
| rikai | base 9 | absent |
| shindan | base 9 | absent |
| suisen | base 9 | absent |
| togo | base 9 | absent |

base 9 = calculate, friction, glob, grep, read, test, list_mcp_resources, list_mcp_resource_templates, read_mcp_resource.
All seats connect one MCP server: hikari-prod (resources deliverable_view + proven_surface; template deliverable).

## The grant's shape

Web rides exactly the discovery lane — tansa (the discover seat) and shinko (the convenor). The mutation grant (patch+curate+lint) rides jikko; the composition grant (junro) rides keikaku. Targeted grants, not a blanket — the closed-world discipline held through the regeneration.

## The runtime axis (the census's second leg)

Surface presence ≠ operability. The four validation packets (scope/prior-art-validate-a/b1/b2/b3) re-fired on this census's PRESENT lines and failed fast at the wrapper's credential guards:
- tansa's wrapper (.opencode/tools/web.ts:92-93, :132-133, :177-178, :204-205 — disk-verified): every op returns "Error: TAVILY_API_KEY not set in environment." (search/extract/research) and "Error: CONTEXT7_API_KEY not set in environment." (lookup). Zero bytes of web content retrieved. One op anomaly: validate-a's lookup returned "Error: Unknown operation 'undefined'." (a wrapper variation worth one look when keys land).
- shinko's platform web (a DIFFERENT tool, outside the opencode wrapper) returned the identical string on a one-op claim-neutral smoke test ("Tavily API getting started documentation") — the same missing key covers the entire session, not just the tree's wrapper.

## The re-fire gate (ruled by this census's outcome)

Future web-validation re-fires gate on a KEYED SMOKE TEST — one live search returning content through the seat's wrapper — never on a census presence line. The keys (TAVILY_API_KEY, CONTEXT7_API_KEY) must ride the session env that launches opencode before any web seat dispatches; the wrapper reads process.env directly (no .env loader).

## Provenance

- Census packet: scope/pack-census (packets.jsonl line 57, dispatched 2026-11-19).
- Census probes: 12 parallel seat reports + shinko self-report, all 2026-11-19; runtime smoke test 2026-11-19.
- Validation re-fires: packets a/b1/b2/b3, fail-fast returns in-message 2026-11-19/20; their evidence files ride the landing sweep (the second-round content supersedes the first-round drafts at the same paths).
- Landed by shinko via patch (the convenor's own pack carries the verb); read-back verification rides the landing.
