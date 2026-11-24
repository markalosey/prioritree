<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/auth-arithmetic

**Route:** prioritree-auth (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-24T06:22:09Z |
| 2 | report | keisan | 2026-11-24T06:28:55Z |
## Reported by keisan — 2026-11-24T06:28:55Z

keisan's auth arithmetic (census/auth-arithmetic) — the numbers, each with its derivation. Sources read on the tree: the 17 test files (186 test functions + 21 parametrize cases − 4 collapsed defs = 203 collected), .prioritree/runs/ the store-home precedent (RUN-0001's manifest line = 199 bytes), .envrc the env precedent (direnv loads the gitignored .env), the scheduler's 10 items → 45 pairs; every arithmetic act run on the calculate surface.

1. KEY FORMS. token_urlsafe: 128/192/256-bit = 16/24/32 random bytes = 22/32/43 chars (128/6=21.3→22; 256/6=42.7→43) — 22-43 bytes on the wire. Storage per key: plaintext 22-43 B; hash-at-rest SHA-256 = 64 hex chars — hashing costs MORE bytes than the 128-bit token it replaces; the purchase is the plaintext's absence, not size. A key-store line ≈ 80 B (the tree's own JSONL precedent: a manifest line runs 199 B); 6 operators → 480 B ≈ 0.5 KB, one file, $0. JWT: HS256 ≈ 36 B header + ~55-110 B payload + 43 B signature ≈ 110-200 B minimum, 200-800 B typical — 9.1× to 36.4× the 22-B token; RS256's signature alone is 342 B and its keypair custody ~1.7 KB private PEM. The structured forms' overhead at this tree's scale (≤8 named operators): expiry/claims/kid/rotation machinery priced against a need a one-line file already meets — infrastructure without a need.

2. VERIFICATION. Per request: SHA-256 of a 30-B input ~1 µs + hmac.compare_digest on 30 B ~1 µs + in-memory dict lookup ~0.1 µs ≈ 2 µs. File-read-per-request ≈ 100 µs (open+read+parse the 0.5-KB store) = 50× the in-memory hit — load-at-startup wins. JWT: HS256 ~10-50 µs; RS256 ~100-500 µs + the key's fetch. At the tree's load: a handful of comparators — 6 × 4 votes/min = 24 votes/min; a sitting = 45 pairs × 2 votes = 90 votes ÷ 24 ≈ 3.75 min (225 s), ~200 requests: in-memory random-token 200×2 µs = 0.4 ms/sitting (1.8e-6 of the sitting); file-read form 200×100 µs = 20 ms; RS256 200×300 µs = 60 ms — every form noise against the human's ~15 s per judgment.

3. INFRASTRUCTURE. The key store: a file in .prioritree/ (the home the tree already owns), 480 B, $0. The env-var form: $0 (.envrc precedent). Secret managers PRICED AND REFUSED: AWS Secrets Manager $0.40/secret/mo × 6 = $2.40/mo = $28.80/yr; GCP Secret Manager $0.06/version/mo × 6 = $0.36/mo = $4.32/yr — plus per-call fees and the cloud-credential chain (the runner would need cloud credentials to fetch the key — a second credential problem bigger than the first). Rotation's dual-key window: both keys valid = one extra store line, 160 B total, $0 — a line edit, not a ceremony. The llm-class constraint's price: the llm's key rides the same file in the same line form — $0 extra infrastructure.

4. TRANSITION. The CLI: the local tool at localhost, dev mode, no key — $0 (--home already the local trust). The tests: 203 collected (census verified); the fixture mints one key into the tmp_path store (~µs) + ~2 µs/request ≈ 10 µs/test × 203 ≈ 2 ms added to the suite — noise against the subprocess probes the suite already runs. The CI: the runner never needs a real key (dev mode again) — $0, no Actions secret plumbed.

VERDICT: every $0 line is a file the tree already owns; every nonzero line is a secret manager, refused at this scale.
