# G-REGISTRY — the independent re-run (kensho's verification; the gate's evidence leg)

- Seat: kensho (検証, verify), packet build/registry, route prioritree-core, 2026-11-20. Landed verbatim from kensho's in-message return by shinko via patch (the landing discipline); the instrument-grant gap kensho found is FR-MEM-0013 (open) at the ledger.
- The unit under verification: src/prioritree/registry.py (405 lines) + tests/test_registry.py (178 lines) — landed per the approved brief (synthesize/registry-brief.md) with the amendment-16 cures applied (the v2 addendum + the cure delta).

## 1 — The three runs

- **The suite: RAN, GREEN.** Via this seat's fixed-argv test act (uv run pytest tests -q — the same pytest the Makefile's test target invokes, same pyproject config; -q changes verbosity only; collection: 12 registry tests + 1 smoke = 13). Pytest's own output, verbatim: `............. [100%]  13 passed in 0.01s`. Summary line, verbatim: **13 passed in 0.01s** — zero warnings (pytest emits a warnings-summary and appends ", N warnings" when any warning occurs; neither appeared).
- **make lint: NOT RUN at kensho's hand.** This seat's pack routes no lint act. The harness HAS the tool (.opencode/tools/lint.ts — ops check → make lint, typecheck → make typecheck) but it is not granted to the kensho route; the callable set is calculate/friction/glob/grep/read/test, and the test act is pytest-only (fixed argv). No shell exists to run make. "All checks passed!" is not this seat's to write without the run.
- **make typecheck: NOT RUN — same grant gap.** "0 errors, 0 warnings, 0 informations" is not this seat's to write without the run.

## 2 — The spot read-back (kensho's own reads, both files read in full)

**src/prioritree/registry.py (405 lines):**

| Item | Result |
|---|---|
| class RegistryRefusedError — Error-suffixed | CONFIRMED — line 89 |
| Five private validators | CONFIRMED — _coerce_rows :149, _check_cardinality :198, _check_duplicates :219, _check_operator :242, _require_quorum :274 |
| Object-typed boundary params | CONFIRMED — the three untrusted-input boundaries are object (items: object :149, operator: object :242, quorum: object :274); the two post-coercion interior validators take the validated tuple[tuple[str, str], ...] — object at the edge, precise after validation, exactly the amendment-16 form |
| _PAIR_LENGTH constant | CONFIRMED — line 24 (= 2), used at :174 |
| Copy-in freeze | CONFIRMED — :360 frozen_rows = tuple(ItemRow(...) ...) built from the validated rows (:353), packed into the frozen manifest (:363); test_aliasing_edge passes at runtime |
| The mint, per-store max+1 | CONFIRMED — _mint_run_id :136-146, f"{_RUN_PREFIX}{count + 1:04d}", called :359 with len(self._manifests) |
| The return (run_id, manifest, count) | CONFIRMED — :369 return run_id, manifest, len(self._manifests); annotation -> tuple[str, RunManifest, int] :332 |
| NO in-code ignores | CONFIRMED — grep "ignore" over all of src/prioritree/: zero matches (zero in tests/test_registry.py too) |
| NO adjacent string literals | CONFIRMED — same-line juxtaposition grep: zero; every line-end bare-quote hit is a docstring terminator, a plain assignment, or the explicit + form — no juxtaposed literals anywhere. The rule is live: pyproject.toml:41 reportImplicitStringConcatenation = "error" |
| No +-concatenated literal pairs (ISC003 class) | CONFIRMED — quote+quote grep: zero; the four explicit + sites (:211-215, :266-269, :289-292, :389-392) join the NAME _action_head to a literal, and :211 joins an f-string to a ternary — no literal+literal pair |

**tests/test_registry.py (178 lines):**

| Item | Result |
|---|---|
| 12 test functions | CONFIRMED — the twelve, lines 28/38/48/63/73/96/103/120/135/147/156/167 (+ 1 smoke = the run's 13) |
| cast("int", bad) in test_quorum_as_data | CONFIRMED — line 112, exact form: quorum=cast("int", bad) |
| bad_sets in test_malformed | CONFIRMED — :82-86, bad_sets: tuple[frozenset[str], ...] with exactly three frozensets (2-subset, 4-superset, empty); no set-typed fourth case |
| RegistryRefusedError at every raises site | CONFIRMED — all 7 sites (:31, :41, :66, :76, :79, :88, :111) are pytest.raises(RegistryRefusedError) |

## 3 — The verdict (kensho's own words, verbatim)

G-REGISTRY's evidence leg: BLOCKED — steps 2-3 (make lint, make typecheck) not run: no lint/typecheck act is granted to the kensho pack (the harness's lint tool exists at .opencode/tools/lint.ts but is unrouted to this seat; no shell; FR-MEM-0013). The test leg is green — 13 passed in 0.01s, zero warnings — and every named spot read-back item is confirmed. The independent confirmation of lint and typecheck needs the grant; the build's own green outputs are on record but are not this leg's word.

## 4 — The closure ruling (the collaborator, 2026-11-20)

G-REGISTRY closes GREEN on the combined evidence — jikko's floor (13 passed, All checks passed!, 0 errors/0 warnings/0 informations), the patch harness's riding checks (zero findings at every mutation), and kensho's independent suite + full read-back; the lint/typecheck grant gap rides FR-MEM-0013 (the tool-grants lane's follow-up: route lint to kensho at the next hikari regen). The closure ruling is the route's amendment 17.
