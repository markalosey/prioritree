<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/auth-sources

**Route:** prioritree-auth (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-24T06:21:17Z |
| 2 | report | tansa | 2026-11-24T06:28:04Z |
## Reported by tansa — 2026-11-24T06:28:04Z

# Auth-source census — tansa, 2026-11-24

## 1. OunceMCP verified-token model (subbusainath.github.io/ouncemcp/concepts/security/, /guides/safe-writes/)

- Token's form → identity: `ctx.identity` comes only from the verified access token — principal (issuer+subject), tenant, scopes, claims; `clientInfo` is never used (SEC-1).
- Hide-and-refuse: `policy=` on the server and per tool; one decision hides the tool from lists and search AND refuses calls (SEC-2); policies read the effect declared at registration, never MCP annotations (SEC-3).
- Audience scoping: `OunceServer(audience=...)` checks `aud`/`resource`; `check_outbound` and `passthrough_guard()` block forwarding the caller's token (SEC-4); caches keyed by principal/tenant/scopes (SEC-5).
- Caller-bound handles: `ctx.issue_state`/`ctx.verify_state` bind tokens to caller+request+expiry, `consume=True` single-use (SEC-6); replay-safe effects (SEC-7); `safe_client` refuses private/loopback/link-local/metadata addresses and re-checks every redirect (SEC-9); auth = FastMCP providers, OunceOAuth client (SEC-10).
- stdio: FastMCP skips component authorization over stdio (server runs as the local user); default `stdio_policy="trust"` makes every tool visible/callable; `"enforce"` applies every check with the anonymous caller; `ouncemcp check` warns (stdio-skips-policy).
- Writes: `approval="required"`/function + `preview=`; the model cannot approve by itself; `idempotency=True` keys by caller+tenant+arguments (RedisStore for replicas).
- Verified against the 2026-11-22 census (.plans/ideation/2026-11-22-prioritree-mcp/reports/census/ouncemcp.md): consistent — handles/approval (pt 3), signed cursors + redacted traces (pts 2/5), FastMCP 4.1.6 substrate (pt 4). New detail here: identity shape, clientInfo exclusion, audience/passthrough_guard, stdio_policy, safe_client. No contradictions.

## 2. FastAPI/FastMCP/Starlette ecosystems

- FastAPI (fastapi.tiangolo.com/tutorial/security/, /tutorial/security/first-steps/, /tutorial/security/oauth2-jwt/, /reference/security, /advanced/security/): OpenAPI schemes apiKey (query/header/cookie), http bearer, oauth2 flows (implicit/clientCredentials/authorizationCode/password), openIdConnect; fastapi.security utilities inherit SecurityBase → automatic OpenAPI/docs integration; OAuth2PasswordBearer extracts the Bearer token as a str, 401 on missing header; APIKeyHeader/APIKeyQuery/APIKeyCookie extract the key from header/query/cookie; JWT tutorial: HS256 with an openssl-generated secret, sub/exp claims, dummy-hash verify to equalize timing.
- FastMCP (gofastmcp.com/servers/auth, /servers/auth/token-verification): "Authentication applies only to FastMCP's HTTP-based transports"; "The STDIO transport inherits security from its local execution environment"; default auth=None (unauthenticated; gateway enforcement is the deployer's responsibility). Provider spectrum: TokenVerifier (base; JWTVerifier: jwks_uri+issuer+audience, RS*/PS*/ES*/Ed25519/Ed448, HS via the public_key param; JWKS auto-rotation), RemoteAuthProvider (DCR), OAuthProxy (non-DCR: GitHub/Google/Azure/AWS), OAuthProvider (full authorization server), MultiAuth (first successful verification wins). Opaque tokens via RFC 7662 introspection; each session is bound to the credential that created it (different credential on an Mcp-Session-Id → 404); session identity = (client_id, issuer, subject).
- Starlette (starlette.dev/authentication/, /middleware/): AuthenticationMiddleware + AuthenticationBackend.authenticate(conn) → request.user (BaseUser: is_authenticated/display_name; SimpleUser/UnauthenticatedUser) + request.auth (AuthCredentials.scopes); @requires scope decorator (403, or 404 "to hide information about the URL layout"); middleware forms: pure-ASGI (scope/receive/send), BaseHTTPMiddleware (dispatch(request, call_next); contextvars limitation), built-ins CORSMiddleware, SessionMiddleware (signed cookie, HttpOnly, "readable but not modifiable"), HTTPSRedirectMiddleware, TrustedHostMiddleware (Host-header attacks), RequestBodyLimitMiddleware, GZipMiddleware.

## 3. API-key infrastructure landscape

- Key form (random): secrets module — token_bytes/token_hex/token_urlsafe over OS randomness; DEFAULT_ENTROPY; "32 bytes (256 bits) of randomness is sufficient" (2015 belief); prefer secrets over random (docs.python.org/3/library/secrets.html).
- Key form (structured): JWT — RFC 7519 registered claims iss/sub/aud/exp/nbf/iat/jti; aud: each intended recipient "MUST identify itself with a value in the audience claim" or reject; jti "can be used to prevent the JWT from being replayed"; jwt.io: signed ≠ secret — payload readable by anyone.
- Hashed-at-rest + storage: OWASP Key Management (cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html) — API keys never committed to repos, never stored plaintext, dedicated vault/HSM, all operations in the vault; env-var loading (FastMCP configuration) vs config-constant SECRET_KEY (FastAPI tutorial) are the two env/file forms seen.
- Rotation/revocation: cryptoperiods limit the window of exposure; originator vs recipient usage periods give a dual-key overlap (encrypt ≤2y; decrypt ≤3y beyond); JWKS rotation without server changes (FastMCP); revoke on usage-agreement violation (OWASP REST); jti+aud denylist until exp (OWASP REST JWT).
- Verification: hmac.compare_digest — designed "to prevent timing analysis by avoiding content-based short circuiting behaviour" (docs.python.org/3/library/hmac.html); OWASP Authentication Cheat Sheet: hash comparisons must return in constant time; hash-lookup form: store keys hashed, look up by digest (ecosystem practice, e.g. blog.masteringbackend.com FastAPI auth).

## 4. Threat-model literature

- STRIDE (Microsoft; Kohnfelder & Garg 1999): Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege — six classes, each mapped to a violated property (authentication, integrity, non-repudiation, confidentiality, availability, authorization).
- RBAC (NIST): formalized 1992 by Ferraiolo/Kuhn; ANSI/INCITS 359-2004, revised INCITS 359-2012; users→roles→privileges (csrc.nist.gov/projects/role-based-access-control). ABAC (NIST SP 800-162): authorization by evaluating subject/object/operation/environment attributes against policy; contrast: RBAC "does not easily support multi-factor decisions".
- Bearer-token threats: RFC 6750 §5.1 names token manufacture/modification, token disclosure, token redirect (one resource server's token replayed at another), token replay; mitigations: audience restriction in the token, TLS, short-lived (≤1h), scoped. RFC 6819 (OAuth 2.0 threat model): eavesdropping on transport, replay, guessing, leakage via logs/referrers. RFC 8725 (JWT BCP): alg "none", RS256→HS256 confusion (downgrade), weak symmetric keys, substitution/cross-JWT confusion; mitigations: validate iss/sub, use aud, explicit typing. OWASP OAuth2 Cheat Sheet: bearer tokens "should be audience-restricted, preferably to a single Resource Server".
- Corroboration: NIST IR 8587 (2026): "all tokens and assertions MUST include explicit audience fields, and all access control mechanisms MUST reject tokens with incorrect or missing audience restrictions."
