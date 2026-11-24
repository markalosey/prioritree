<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/auth-mechanisms

**Route:** prioritree-auth (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-24T06:21:51Z |
| 2 | report | rikai | 2026-11-24T06:26:23Z |
## Reported by rikai — 2026-11-24T06:26:23Z

# THE AUTH CANDIDATES' MECHANISM MAPS (rikai, census/auth-mechanisms, 2026-11-24)

## 1. THE API-KEY MECHANISM — verify, bind, rotate, revoke
- BEARER: FastAPI's APIKeyHeader declares the header once; the route's dependency resolves it at the door before the handler body. Insertion: one dep per route at service.py:322/351/381/418/452/491 — the Annotated form (the dependency in the type, never a default argument) composes with the routes' no-Depends/B008 discipline (service.py:12-13).
- CONSTANT-TIME: hmac.compare_digest runs in time ∝ input length, never ∝ match length — a naive == short-circuits at the first differing byte, leaking the key's prefix through response timing (the timing oracle); compare_digest closes it.
- HASHED-AT-REST: the store holds the digest (sha/blake over the key), plaintext never on disk; the lookup hashes the presented key and seeks the digest (a fixed-length-digest dict lookup — constant per key), the record {digest, comparator_id, scopes, created_at} one self-describing line (the JSONL school, run_store.py:111-120).
- BINDING: the record IS the key→comparator_id map; the verified id overrides/cross-checks the body's comparator_id — today self-declared at the door (service.py:153) and the web form (web.py:648), the key's whole job is that verification.
- ROTATION: the dual-key window — two digests on one record, both resolving to the same identity during the transition; the old digest's retirement a superseding append (the ledger's own supersedes precedent, votes.py:72).
- REVOCATION: the append-only school prices the tombstone — a record retiring the digest (absence of a live record = refused; the store IS the denylist); the inverse form (a revoked-list checked at verify) is the same mechanism read backwards.

## 2. THE POLICY MECHANISM — how a scope grants
- RBAC: operator (register/state/tally), comparator (next/cast), auditor (state/tally) — the grant map as DATA (COMPARATOR_CLASSES' frozenset precedent, votes.py:31-33). THE IN-TREE PRECEDENT: opencode.json's per-seat rows — default-deny ("*": "deny") + named allows; rikai's own row: next/tally/census allow, register/cast deny (opencode.json:333-337); lifecycle.ts:33-35's op enum the same grant-map form at the tool tier.
- ABAC: the key record carries per-run scopes; the check composes the key's identity + the route's run_id path param → grant/deny; the run's own operator_id (the manifest) the natural attribute.
- TOOL-LEVEL: OunceMCP policies hide-and-refuse — the unauthorized tool absent from tools/list, the direct call refused; exactly what opencode.json does at the harness tier, lifted to the server's five tools (mcp_server.py:6-7).
- COMPOSITION WITH THE STAMPS: comparator_id + class already ride every VoteRecord (votes.py:68-69); the class already schema-gated (the Literal drift-guard, mcp_server.py:96-98; the door's COMPARATOR_CLASSES check) — the key verifies the ID, the schema keeps gating the class; nothing new at the record.

## 3. THE MIDDLEWARE MECHANISM — how auth composes per tier
- SERVICE: the per-route dependency (§1); the 401/403 statuses ride the named-constant discipline (the 404/405 freeze precedent, service.py:262-265).
- MCP: three named options — OunceMCP's own verified-token + policies (the claims lane's read; composes at the OunceServer construction, mcp_server.py:113), FastMCP's auth layer, or a raw ASGI middleware before the server; the policies gate the five tools per identity.
- WEB: the session is anonymous today (comparator_id a form field, web.py:648); the shapes: the key at the browser (a login route minting a session cookie), OR the web tier holds the key server-side (it is a true in-process client of the service, web.py:164-167 — one credential, the humans ride forms), OR the tiers stay key-free (the service trusts its own child).
- THREEPART AT 401/403: expected [the key in the named header], found [absent/unknown | the scope not granted], next_action [the acquisition path]; rendered at ONE point (the render_refusal precedent, service.py:168-183); 401 = authentication's refusal (no/unknown key), 403 = authorization's (key good, scope denied) — the two codes carry Q-auth-design's two halves.

## 4. THE FALLBACK MECHANISM — how the tree degrades
- NO-KEY MODE: the dev trust today is the LOOPBACK BIND, not an auth layer (HOST ?= 127.0.0.1, MCP_HOST ?= 127.0.0.1, Makefile:4/6); the degradation: the key store ABSENT = auth OFF — the dependency short-circuits on the absent store (the mkdir-on-demand asymmetry's precedent, web.py:145-147).
- TRANSITION: the CLI composes Persist directly, never the service (cli.py:5-7) — untouched by construction; the tests inject the seam (app.state.seam per test, service.py:162-163) — the key store injects the same way (or the dev mode carries the arcs); the CI runs the dev mode (no key in the runner, the suite's arcs unedited).
- CONFIGURABILITY AT EVERY KNOB: the ?= form the precedent (Makefile:3-6) — the key store's home (STORE_HOME's own CWD-relative form, run_store.py:53; the env knob banked, service.py:161-163), the header names (named constants, the service.py:73-87 school), the policy toggles (the grant map as data, the frozenset school) — every knob ?=-shaped from birth.
