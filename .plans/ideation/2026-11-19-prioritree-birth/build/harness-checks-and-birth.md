# build/harness-checks-and-birth — the check legs + the live proof (the final harness evidence)

## 0. Provenance

- **The hands:** the collaborator's (marklosey@Mac, hikari's root, 2026-11-19) — the three --check legs; then the live proof at a FRESH opencode session at prioritree (its own shinko seat — the tree's first session), the friction birth-write fired and read back in-session. The captures pasted verbatim; the store's evidence artifact for kensho's G-HARNESS verification.

## 1. The three byte-contract legs — ALL PASS

```
uv run python scripts/generation/clarity_scaffold.py --target clarity --check
  → scaffold verdict: PASS 24/24 — byte-matches a fresh regen.
uv run python scripts/generation/clarity_scaffold.py --target input --check
  → scaffold verdict: PASS 24/24 — byte-matches a fresh regen.
uv run python scripts/generation/clarity_scaffold.py --target prioritree --check
  → scaffold verdict: PASS 24/24 — byte-matches a fresh regen.
```

Every artifact MATCHed on every leg (the full per-artifact byte counts in the session capture: clarity opencode.json 14,319 / input 14,293 / prioritree 14,358; the engines identical at 54,724/23,185/1,879/9,915/18,268 across all three — the shared core serving three targets, byte-true; the restored clarity tree and the refreshed input both under contract). **G-HARNESS condition 2's sibling contracts and condition 3's prioritree byte-truth: GREEN on capture.**

## 2. The live proof — the birth-write (condition 4 + 5's birth leg, one call)

The fresh opencode session at /Users/marklosey/projects/prioritree opened on **its own shinko seat** (default agent — the emitted harness live). The seat read jikko's deviation record and filed ONE friction report through the friction tool; the call ANSWERED through the registered wrapper (`.opencode/tools/friction.ts` → `_run.ts` → the emitted engine) and minted **FR-MEM-0001** — prioritree's ledger's first entry, read back verified: surface = synthesize/harness-brief.md §1.1(c)'s fenced root= line (brief :55); attempted/happened verbatim from the deviation record (the fenced form resolving to kepric/prioritree — nonexistent — vs the route-ruled root, landed as REPO_ROOT.parent.parent); the cause a labeled hypothesis (the §14 payload slip riding into togo's fence unverified); the workaround verbatim (one .parent added). The seat's judgment calls, reported: axes documentation/data-gap (a ratified seed mode), severity high, detectability immediate (caught in-session at the read-back, before harm). **The birth: prioritree/.plans/state/friction-ledger.jsonl now EXISTS carrying FR-MEM-0001** (the read-back green — the entry's fields served exactly as filed).

## 3. The standing notes for the gate

- **The brief's erroneous line (harness-brief.md:55) stands as the historical object**: the deviation is triple-recorded (jikko's build report, FR-MEM-0001, this evidence) — the landed constant is correct; patching the brief would desync the gate's object. A one-line patch remains available at the collaborator's call.
- **FR-MEM-0001's triage** rides prioritree's own shinko seat (the filing seat, its next session) — the recommended disposition: fixed-in-build/harness (the cure landed; the class documented).

## 4. The closing capture — the pyright leg (condition 2's last pending): GREEN

`uv run pyright scripts/generation/clarity_scaffold.py` at hikari (the collaborator's hand, 2026-11-19) → **"0 errors, 0 warnings, 0 informations"** — the brief's criteria-2 typechecker leg closes whole on capture; the version notice ("v1.1.409 -> v1.1.414") is the documented out-of-band wrapper notice (understand/foundations.md §3's named class — not a checker diagnostic). **Condition 2's every leg now green: ruff ×2, pyright 0/0/0, the three byte-contracts PASS 24/24.**

## 5. The inner-file removal — kensho's catch 6 closed (the collaborator's hand)

`rm /Users/marklosey/projects/prioritree/.opencode/.gitignore` (the collaborator's confirmation: ".opencode/.gitignore removed") — the unmeasured inner file (the input-tree divergence shape whose `package.json` line would have silently skipped the emitted pin file at the landing commit — the FR-MEM-0419 hazard family) is GONE; the root trio covers the substrate; the pin file trackable. **Both gate pendings now closed: the pyright leg (§4, 0/0/0 on capture) and the inner-file catch (§5, removed) — the gate's green closes whole.**
- **One leg pending capture**: `uv run pyright scripts/generation/clarity_scaffold.py` at hikari (the brief's criteria-2 typechecker leg; ruff is green ×2 on capture) — the collaborator's one-liner, to be adjudicated honestly at the gate if uncaptured.
- **What remains**: kensho's G-HARNESS verification over this evidence + the seat-side read-backs; then the landings (hikari's scaffold edit through hikari's shinko-git choreography; prioritree's harness artifacts + the born store through the collaborator's hand).
