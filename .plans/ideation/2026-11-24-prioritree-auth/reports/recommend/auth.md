<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — recommend/auth

**Route:** prioritree-auth (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-24T06:49:47Z |
| 2 | report | suisen | 2026-11-24T06:59:38Z |
## Reported by suisen — 2026-11-24T06:59:38Z

# THE AUTH RECOMMENDATION — suisen, recommend/auth (2026-11-24)

Ground read whole: togo's brief (synthesize/auth-research), hyoka's ten findings (F1-F4 blocking), keisan's dominance table, moho's walks, shindan's residuals, the five census reports, the rulings (the authn+authz scope; the four Q-auth-widening; the configurability law; the claims lane; the llm-class constraint).

## 1. THE RECOMMENDED DESIGN WHOLE — the leading shape CONFIRMED, the blocking rulings carried as its own

THE KEY: secrets.token_urlsafe(32) — the 256-bit norm (43 chars), borne in a named header, the names configurable from birth. THE STORE: one file in .prioritree/ (~80 B/line, 480 B at six operators, $0), the record {digest, comparator_id, comparator_class, scopes, audience, created_at} one self-describing JSONL line. HASHED-AT-REST: the SHA-256 digest only, plaintext never on disk; the lookup hashes the presented key + compare_digest at the ONE verify point + the in-memory dict (~2 µs; load-at-startup, the stat carrying F3's check and the mtime re-read — a mid-flight mint lands live). THE PER-ROUTE DEPENDENCY: the Annotated form at the six routes; 401 = no/unknown key, 403 = scope denied; ThreePart at each, rendered at one point. THE GRANT MAP as data: operator register/state/tally/manifest, comparator next/cast/manifest (moho's hole closed — the sitting consumes manifest+next), auditor state/tally/manifest.

THE BLOCKING RULINGS CARRIED:
- F1 THE FAILOPEN MADE LOUD: the explicit AUTH knob (?=-shaped) or the rendered boot marker — the absent store NEVER silent; the home resolved ONCE at boot and rendered (F10 folded — the cwd split killed).
- F2 THE DRIVE-BY CURED AT THE TIER ITSELF: the per-route CSRF dependency at the /ui/ POST routes — the only REMOTE vector; the loopback blocks the token's read, the blind POST dies.
- F3 THE STORE'S INTEGRITY: mode 0600 at the mint + the load's stat check (the world-writable refusal) — the forged-key attack's floor.
- F4 THE SUPERSEDES CURE LANDS WITH THE KEY: the door check — the 403 at the wrong author, the found ELIDING the target's author (the identity oracle avoided); the BOTH-depth priced as the ruling's option, its hazard named (history hostage to the current store — a rotated key's old supersedes fail); the residual either way: the offline JSONL edit.
- F5 THE AUDIENCE FIELD (service|mcp) on the record, checked at BOTH doors — the cross-tier replay closed (NIST IR 8587's MUST).

F8 RULED IN — the honest answer to the llm-insider: comparator_class ON THE KEY RECORD (verified at the door, the body's self-claim overridden as the id's is) + THE PER-CLASS QUORUM FLOOR (>=1 verified-human AND >=1 verified-llm per pair — corroboration ENFORCED at the tally, not marketed), the floor the run's declared policy at register (the configurability law; the new-run default the product's corroboration story, the legacy absent declaration read honestly). REASON: the public story IS cross-class corroboration — enforced or it is marketing; the cost $0 (one field, one door check, one tally check); the trust narrows to the honest minter — the issuance residual either way.

THE ISSUANCE NAMED (moho's six steps resolved): the CLI subcommand — `prioritree key mint` — riding the local trust (the mint writes the file, needs no key: the bootstrap's chicken-and-egg answered), the plaintext shown ONCE, the digest written, the reload landing live via the stat ride.

THE WEB TIER RULED (the evaluation's ranking carried): the key-free child at the BROWSER edge — the humans ride forms anonymously behind the tier's own server-side key (the in-process lane's mechanical necessity: the child is a true HTTP client of the gated service surface, web.py's own layering), the sitting URL stays the whole capability (the shareability preserved), the comparator's experience unchanged; + the /ui/ dependency (the CSRF token: minted into the served form, validated at the POST) + THE WEB TIER'S 401/403 LANE BUILT (the refusal fragments for the auth codes — the fold page never wearing the 401's clothes; moho's finding: the lane does not exist today). PRICES NAMED: the tier key a skeleton key at the web tier; the comparator_id at the browser stays the form's self-claim (the id-binding never fires at the browser); form (i) priced and refused (3 ceremonies + the shareable URL's death — a product feature); form (ii) bare priced and refused (the bridge stays live).

THE MCP TIER RULED: OunceMCP's verified-token + policies at --serve — the identity-aware hide-and-refuse, the audience-gated door, the grant map lifted to the five tools (the hiding's teaching loss named as the price); THE STDIO TRUST RULED: the spawn IS the credential — the llm-class constraint's own law (enforce kills the ride or re-opens the anonymous cast; the transport carries no identity).

## 2. THE ALTERNATIVES PRICED (the public record)

JWT: 9.1x-36.4x the wire, the second secret (the signing key's custody), the machinery's own bugs (RFC 8725: alg none, RS-to-HS confusion) — priced out at <=8 operators. SECRET MANAGER: $28.80/yr + the credential chain widening the exposure it guards — refused (the free-tier spirit AND the exposure logic). OAUTH: the consent ceremony kills the llm ride — the constraint's violation by construction. THE SCALE FENCE (banked, never silent): past <=8 operators, past the single machine, into multi-tenancy — the file's earn ends, the banked machinery begins.

## 3. THE RESIDUALS STATED (the honest statement)

The wire cured; THE DISK AND THE LOCAL MACHINE REMAIN TRUST: the cleartext store (hashed-at-rest guards the KEY, never the DATA — the JSONL's ids, questions, notes naked on disk), the local process's reach (the key fences the socket, not the filesystem), the offline JSONL edit (the floor every supersedes cure prices to), the issuance's honesty (the operator mints honestly — the operational trust itself); the web tier's id-binding (the form's self-claim behind the tier key); the MCP hiding's teaching loss; F7's quantities (N(N-1)/2 pairs, over-quorum votes, re-vote drowning) named and owned by the tally-policy lane, never silent; the /docs + route-table recon ruled with F6's coverage unit (gated or stripped).

## 4. THE BUILD SET EARNED (the units for the composition)

(1) KEY INFRASTRUCTURE — the store (0600, the stat check), the mint (the CLI subcommand, the plaintext once, the live reload), the verify (the digest lookup, compare_digest at one point, the miss-path dummy compute [F9], the audience + class checks), the ThreePart at 401/403 (the found eliding the target's author at the supersedes 403);
(2) POLICY LAYER — the grant map (the manifest scope closed), the per-class floor, the AUTH knob / the boot marker (F1/F10);
(3) SERVING-TIER INTEGRATION — the per-route dependencies (the Annotated form), the /ui/ cure (the CSRF + the tier key + the web 401/403 lane), the audience at both doors, the supersedes door check, the coverage invariant (F6: no route ungated, the 404/405 route-table render and /docs ruled);
(4) THE MCP TIER — the OunceMCP policies at --serve, the stdio trust ruling;
(5) THE README'S PUBLIC STORY.

## 5. THE PUBLIC STORY

Cured: the anonymous write (the operator scope at the register door), the read exposure (the per-route dependency, the auditor scope), the reconnaissance (the refusal serves key-holders only), the drive-by (the CSRF at the tier itself), the supersedes hole (the door check, the author elided), the cross-tier replay (the audience field). Remains trust: the disk's cleartext, the local machine, the issuance's honesty — the honest floor of every design at this scale. Why the choices hold: the $0 file at the <=8-operator scale (480 B, 2 µs, 0.4 ms a sitting — keisan's numbers), the llm riding its own key (no human gate anywhere — the constraint held at every surface), the corroboration enforced at the tally (the per-class floor — the product's story true, not marketed), the scale fence banked honestly: the machinery priced, the trigger named, the file's earn ending where it ends.
