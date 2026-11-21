# recommend/next-effort — THE NEXT EFFORT'S RECOMMENDATION (suisen; the collaborator rules)

- Provenance: suisen (推薦, recommend), packet recommend/next-effort, route prioritree-cli, 2026-11-21 — the collaborator asked for recommendations and reasoning on the next steps at the CLI close; read-only held (6 reads: CONTINUATION.md whole, the acceptance-brief §5, the birth store's Q-setup-arch, the core store's Q-mcp-surface, pyproject.toml, the k=1 baseline table); returned in-message; landed by shinko via patch.

## (1) THE STAGED CANDIDATES, PRICED

- **THE FASTAPI SERVICE** (Q-setup-arch's third layer): the five ops over HTTP — routes 1:1, the request/response shapes, the uvicorn lifecycle. THE RUNTIME-DEPS QUESTION: `dependencies = []` cannot hold at this tier — fastapi + uvicorn enter, the tree's FIRST runtime deps (the zero-dep law's per-tier reading ruled at the service's own brief). THE CONCURRENCY QUESTION: the CLI's single-writer-by-contract store vs concurrent HTTP clients — the lock weight priced OUT at the CLI tier re-opens here as a real design cost. THE STORE QUESTION: per-request run-store composition or in-memory session state — a service-era design ruling not yet made. WHAT IT UNLOCKS: the MCP era (OunceMCP per the banked ruling) and the web app beyond — pure delivery value, zero claim value.
- **THE BUDGET CURVE** (R13's comparative-empirical claim measured): the sizer arm per §5 — each item sized by the same noisy comparator at the same p, the sizings repeated to equal budget (n₀ judgments total), the sizes sorted into the sizer's own ranking, tau computed identically, the two taus compared per cell. SCOPE: small — one module + tests in the acceptance harness's own form (the seeded sizer, the equal-budget spend, the per-cell comparison; the matrix, the seeds, the k=3 quorum ride). THE OPENING EVIDENCE: the k=1 baseline table already recorded (8 of 27 in-band cells sub-floor at single judgment, min tau 0.4714 — the pairwise side's fragility at minimal budget measured; the sizer arm the missing half). WHAT IT EARNS: the purpose sentence graduates from ruled language to MEASUREMENT — the README's own claim at last demonstrated, or honestly falsified (either result clears the debt).
- **THE MCP TIER: banked, not a candidate** — Q-mcp-surface's own words: it composes when the service era arrives.

## (2) THE CLAIM-DEBT READING

- The purpose sentence's comparison is UNMEASURED — the deferral priced twice (acceptance-brief §5's honest deferral; the core close's banked framing). The debt's age: TWO EFFORTS CLOSED CARRYING IT (core, CLI). The cost of carrying it further: every tier built on an unmeasured central claim — the service would serve it, the MCP tier would expose it, the web app would front it: three more forms fronting a comparison that has never been run once. The k=1 table sharpens it: "superior at equal budget" is currently a belief, not a datum.

## (3) THE RECOMMENDATION — ONE PRIMARY

- **THE BUDGET CURVE.** The reasoning: CLAIM-VALUE — the only candidate that touches the debt; the service adds delivery, the curve converts the tree's whole reason to exist into evidence. SCOPE AND RISK — one module + tests inside a harness that already runs green; the mechanism priced (§5), the earning condition ruled (seeds fixed, runs deterministic, the per-cell comparison recorded as data), zero new deps, zero new tiers; the service carries three open design questions (deps, concurrency, store), each a brief gate's worth of deliberation — the concurrency weight deliberately priced OUT once already. HARNESS-WARM — the acceptance unit's matrix, seeds, quorum, tau-b integer measure, and RNG discipline ARE the curve's substrate, closed one day ago; the sizer arm is a second arm in a warm harness, not a new build. THE DECLARED ARC IS A LAYERING, NOT A CALENDAR — Q-setup-arch's four forms order the stack; the MCP ruling leaves the era's arrival to the ruling; the curve rides the earned-later menu's own first cousin. WHAT IT BANKS — the service era then arrives with the claim measured; and if the curve falsifies the claim at equal budget, better to learn it BEFORE three delivery tiers than after.

## (4) THE PRICED RUNNER-UP

- **THE FASTAPI SERVICE — defers, not loses.** The stack's arc continues the moment the curve closes: the deps question (the table opens at the service brief), the concurrency question (the lock weight ruled at its own gate), the store question — all arrive intact, and the service's own acceptance unit is stronger for serving a measured claim. None of the service's costs compound while it waits; the claim's debt does. The MCP tier stays banked beyond it.

## (5) THE NEXT STORE'S BIRTH FORM

- At the ruling: the store at `.plans/ideation/<date>-budget-curve/` (the name the ruling mints — the vitals-store precedent carried at both prior births), born via the tree's own shinko seat + patch — the junro grant live through the cross-project wrapper, the git instrument landed and serving: the tree owns its own convening. The birth recorded at the close's records, the done call at the collaborator's ruling.

*The tree is the truth; the ruling is the collaborator's.*
