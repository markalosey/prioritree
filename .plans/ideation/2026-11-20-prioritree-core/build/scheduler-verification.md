# G-SCHEDULER — the independent re-run (kensho's verification; the gate's evidence leg)

- Seat: kensho (検証, verify), packet build/scheduler, route prioritree-core, 2026-11-20. Landed from kensho's in-message return by shinko via patch (the landing discipline); the stale-session grant gap is FR-MEM-0014 (open).
- The unit under verification: src/prioritree/scheduler.py (106 lines) + tests/test_scheduler.py (89 lines) — landed per the approved brief with the cure delta applied (TC003/PERF401/PLR1714 cures + the ARG001 named ruling at pyproject).

## 1 — The runs

- **The suite: RAN, GREEN** (kensho's own test act, fresh process): `.......................... [100%]  26 passed in 0.01s` — 26 passed, zero warnings (no warnings section printed; the unit's 13 named tests among the 26).
- **make lint / make typecheck: NOT RUN at kensho's hand — the grant absence named (fail fast).** The session's pack predates the amendment-42 regen (the base-only six; no lint act, no shell); the grant IS on disk at commit 8b725378 (kensho.md:30 the pack row, lint.ts:21-38 the wrapper, opencode.json:211 the permission — read back whole this dispatch). The re-dispatch rides the opencode restart (FR-MEM-0014's stale-session class).

## 2 — The spot read-back (kensho's own reads, 12/12 confirmed, zero discrepancies)

- scheduler.py (106 lines): Pair the frozen dataclass (:27-28, item_a/item_b :48-49); schedule_pairs' signature with the reserved seed (:52, the docstring ruling it UNUSED by the ruled order :75-78); the TYPE_CHECKING import form (:16-19); the extend form (:83); derive_seed's digest (SEED_ALGORITHM blake2b :23, SEED_BYTES 8 :24, the derivation :105-106); zero in-code ignores (grep zero); no adjacent literals; no literal+literal concatenation (the only + is i + 1).
- test_scheduler.py (89 lines): the 13 named tests (all thirteen, lines 7-86); the extend oracle (:32); the membership form (:41).
- pyproject.toml: the ARG001 named ruling at per-file-ignores (:34-39) citing the scheduler-brief's reservation clause verbatim — the ignore IS the ruling, named; it retires when U5's next_pair consumes the seed.

## 3 — The verdict (kensho's own words)

G-SCHEDULER's evidence leg: BLOCKED — the lint grant absent from this session (FR-MEM-0014's stale-session class). The grant is on disk at commit 8b725378; this session's pack predates the amendment-42 regen. The re-dispatch rides the opencode restart. What did run, ran green: the suite leg — 26 passed, zero warnings; the read-back leg — 12/12 confirmed, zero discrepancies. FULLY GREEN awaits the re-dispatch.

## 4 — The closure ruling (the collaborator's standing precedent, amendment 17's form)

G-SCHEDULER closes GREEN on the combined evidence per amendment 17's precedent — jikko's floor (26 passed, All checks passed!, 0/0/0), the patch harness's riding checks (zero findings at the final mutations), and kensho's independent suite + 12/12 read-back; the lint/typecheck grant gap rides FR-MEM-0014 (the re-dispatch at the next opencode restart completes the independence). The closure ruling is the route's amendment 20.
