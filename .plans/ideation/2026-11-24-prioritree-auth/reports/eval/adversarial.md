<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — eval/adversarial

**Route:** prioritree-auth (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-24T06:42:45Z |
| 2 | report | hyoka | 2026-11-24T06:47:17Z |
## Reported by hyoka — 2026-11-24T06:47:17Z

# THE ADVERSARIAL ATTACK — hyoka, eval/adversarial (2026-11-24)

Ground: the research brief (synthesize/auth-research.md), the five census reports, the store's junro.json (Q-auth-design's authn+authz scope), the birth store's four Q-auth-widening rulings (2026-11-19-prioritree-birth/.junro/junro.json:616-648); the code verified: service.py:321-490 (six authless routes, comparator_id self-declared :152), web.py:164-167/:578/:648, mcp_server.py:113/:582/:584, store_lock.py:10, run_store.py:53.

## FINDINGS, RANKED BY SEVERITY

**F1 (HIGH, blocking) THE FAILOPEN DEGRADE.** The leading shape's own rule — key store absent = auth OFF — is an attacker-operated kill switch: the local class (moho 5) removes the 0.5-KB file and every route silently degrades to today's anonymous surface, indistinguishable from dev-mode intent. The design must carry: absent store = LOUD (a rendered banner/refusal marker) or an explicit AUTH=off knob; silent security degradation is the defect class — store_lock.py:10's trust stated, never enforced.

**F2 (HIGH) THE DRIVE-BY SURVIVES ALL THREE WEB FORMS.** The browser bridge (POST /ui/register, /ui/.../vote — plain forms, no CSRF, web.py:644-651) is the only REMOTE vector found (moho 7). Form (i) cures it at the browser; form (ii) leaves it LIVE (the tier attaches its own key in-process — the anonymous browser becomes an authorized caller THROUGH the tier); form (iii) leaves it LIVE (the /ui/ routes trusted as the child, ASGITransport web.py:164-167). The dependency/CSRF must land AT the /ui/ POST routes regardless of the session form — not deferrable to the divergence.

**F3 (HIGH) THE STORE'S OWN INTEGRITY.** The auth's whole trust collapses onto a file the walk proved unfenced (shindan 2: a well-formed forged line counts at full weight): an appended record (self-minted digest, comparator_id "victim", operator scope) grants the victim's identity at the door — the forged-key attack replaces the forged-vote attack. Cure: mode 0600 at mint + the load's stat check (loud refusal on world-writable) + the accepted-residual statement (root compromise out of scope), or the store's protection enters the design's scope.

**F4 (HIGH) THE SUPERSEDES HOLE.** The tally-flip (moho 4) survives the leading shape: the key verifies the CAST's author; the SUPERSEDE's target is another author's vote. Cures priced: (A) the door check (superseder's key vs target's author) — but the 403's found MUST elide the target's author (an identity oracle otherwise); (B) the load's re-validation — refused alone: history becomes hostage to the CURRENT key store (a rotated key's old votes fail). BOTH is the defense in depth; the residual either way: the offline JSONL edit (F3's class — the auth never sees local writes). The hole must land NOW: (A) minimum, both preferred.

**F5 (MEDIUM-HIGH) THE AUDIENCE GAP.** One key form, two tiers (:8000 service, :8100 MCP --serve): without an audience binding, a service key REPLAYS at the MCP tier — RFC 6750 §5.1 token redirect; NIST IR 8587's MUST; OunceMCP SEC-4 exists for exactly this. The record needs an audience field (service|mcp), checked at both doors — the configurability law's knob, not a second store.

**F6 (MEDIUM) THE PER-ROUTE DRIFT.** The Annotated dependency is opt-in per route; the tree's own history proves the class (all six routes built authless; describe added later as the sixth query). Forced answer: the coverage invariant — a lint/test refusing any route without the dependency, exemptions named (the zero-findings bar's form). Also: the framework 404/405 handler renders _ROUTE_TABLE (service.py:309-318) OUTSIDE any dependency — the reconnaissance read survives auth unless gated or stripped.

**F7 (MEDIUM) THE POLICY GRANTS VERBS, NEVER QUANTITIES.** The operator scope gates the mint but nothing bounds it: N items → N(N-1)/2 pairs (moho 8a), over-quorum votes land (8b), changed-verdict re-votes both count (drowning). RBAC cannot price quantities; the design must rule the ownership — the mint's ceiling another unit's, or accepted residual, never silent.

**F8 (MEDIUM) THE LLM-INSIDER.** Authorization cannot cure identity fabrication: k fabricated keys defeat quorum k exactly as k fabricated ids did. What CAN, priced: the key record carries comparator_class (asserted at the mint — the class stamp verified at the door, the body's self-claim overridden as the id's is: web.py:649, mcp_server's Literal gates vocabulary only) + the per-class quorum floor (≥1 verified-human AND ≥1 verified-llm per pair — the corroboration story ENFORCED at the tally, not marketed); the census per id as detection. The issuance trust narrows to the operator's mint — accepted at this scale, or the product's public story is unenforced (moho 8d).

**F9 (LOW-MEDIUM) THE TIMING RESIDUAL.** The hashed lookup kills the prefix oracle by construction (a wrong key's digest is uniformly wrong); the residual is the hit/miss path difference (~µs, eventual) — the dummy-compute on the miss path (the tutorial's own equalization) closes it; compare_digest at the ONE verify point, a lint invariant against a second compare site.

**F10 (LOW) THE CWD RESOLUTION.** If the key store's home rides run_store.py:53's CWD-relative form, a boot from another cwd resolves an empty or attacker-authored store (F1 again; the lock-split precedent). Resolve the home ONCE at boot and render it, or default absolute.

## THE ALTERNATES' SURFACES (attacked, ranked)
JWT: the machinery's own bugs ARE the surface (RFC 8725: alg none, RS→HS confusion) + the signing key's custody — a second secret, a wider surface, zero added power at ≤8. Secret manager: the runner's cloud credential chain widens the exposure it guards — surface strictly larger. OAuth: the consent ceremony kills the llm ride (constraint breach by construction) + the external authority's compromise becomes the tree's. OunceMCP verified-token: the strongest MCP-tier form for --serve (identity-aware hide-and-refuse); the stdio hole honest — the spawn IS the credential (mcp_server.py:584); stdio_policy=enforce kills the llm ride (the constraint's own breach); FastMCP raw loses the policy layer (tools/list reconnaissance); the raw middleware splits the surface (no identity shape, OunceServer's internal endpoints ungated).

## VERDICT
The leading shape stands attacked, NOT broken: the ≤8-operator verdict holds at the wire. The design must carry F1-F5 as its own rulings (F1-F4 blocking) and price F6-F10 as named residuals. Divergences by attack-readiness: stdio trust > enforce (the llm-class constraint's own law); OunceMCP policies > FastMCP raw > middleware (identity-aware refusal vs the split surface); web form (iii) + the /ui/ dependency + the CSRF token > (i) (a second secret + the session surface + the shareable URL's death — a product feature) > (ii) (the bridge stays live).
