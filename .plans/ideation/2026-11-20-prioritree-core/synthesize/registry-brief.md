# synthesize/registry-brief — THE REGISTRY UNIT'S BUILD BRIEF (the exact-task spec)

**Status: PROPOSAL.** Togo proposes; the collaborator rules at G-REGISTRY-BRIEF. Every [PROPOSED] element is an offered default with its one-line reason. The brief IS the spec (the exact-task law): once approved, jikko executes exactly, kensho re-runs independently.

## §0 GROUND — the rulings the brief cites (fixed by G-REGISTRY-BRIEF condition 2)

**The R-rulings (birth store, 2026-11-20, adopted wholesale):**

- **R1 session shape** (Q-granularity): one list, one operator, one sitting; the run is FROZEN at registration — register_run mints RUN-{####}, immutable thereafter; a changed list is a new run.
- **R2 item shape**: opaque (id, label) rows the core never interprets; duplicate ids within the payload REFUSED; <2 items REFUSED — the empty list AND the single item are named refusals, not special rankings.
- **R3 operator binding**: ONE operator declaration per run (id + stated question + declared verdict set); the tally never interprets it.
- **R4 vote vocabulary** (Q-solution-space): the weak-order triple {prefer-a, prefer-b, tie} is the declared verdict set's DEFAULT; binary at birth, tie per the operator's declaration.
- **R8 quorum** (Q-problem-space): k=1 at birth; quorum is policy-as-data declared at registration; the exhausted state and the coverage gate key off it.
- **The five-op interface + the split** (Q-solution-space): register_run, next_pair, cast_vote, read_vote_state, tally_rank — two append-only stores, zero edit/delete verbs; register_run is deterministic; the schema gate is the stochastic/deterministic boundary.
- **The op 1 spec verbatim** (scope-synthesis PART 3 §3.2): register_run(items, operator, quorum=k) → RUN-{####}; refusals <2 items, duplicate ids, schema violations — all expected/found/next-action; exactly one side effect: the run-manifest append, frozen thereafter.

**The legs riding this brief:** discover/registry (tansa's census — the ruled ground, the gaps (a)–(g), the laws) and understand/registry (rikai's mechanism — the chain, the refusal table, the invariants, the ten [OPEN] items). Every open item below resolves them.

**The unit's Parnas fence (U1's must-not-know):** scheduling strategy, vote semantics, ranking, who votes, display. Nothing of these crosses the module's boundary.

**The family precedent:** .opencode/scripts/friction_ledger.py — the write-discipline school (RefusedError/refuse, _req_text's non-empty discipline, the per-store max+1 mint, "a refusal raises BEFORE any byte is written", the built-in read-back) the unit inherits.

## §1 THE MODULE — the layout ruling

**[PROPOSED]: single module `src/prioritree/registry.py`.** Reason: the route's ruled vocabulary names it — G-REGISTRY, synthesize/registry, "the registry module lands per the brief" — and the naming law is honored at the symbol level, not the module's (each new symbol's name is the first word of its own act-statement; the module name follows the route's ruled vocabulary). Options (b) package, (c) split schemas, (d) flat-into-__init__ are refused: a sub-module surface for one unit's schemas adds a seam nothing cites yet, and U5 freezes the public API at the wrapper contract — flat-into-__init__ pollutes the package head.

**The public surface it exports (the citation contract, understand §5) — the frozen list:**

| Symbol | Kind | Consumers |
|---|---|---|
| `ItemRow` | frozen dataclass (id, label) | U2 (id set), U3 (ground-truth), U5 |
| `OperatorDeclaration` | frozen dataclass (id, question, verdicts) | U3 (winner validation), U4 (counting vocabulary) |
| `RunManifest` | frozen dataclass (run_id, items, operator, quorum, registered_at) | U3, U4, ops 4/5 |
| `Registry` | the container class (store-as-parameter) | U5, the tests |
| `register_run` (method) | the one mutating op | U3 via U1's own surface |
| `read_manifest` (method) | the lookup by run_id | U3's ground-truth checks, op 4 |
| `RegistryRefused` | the typed refusal exception | every downstream unit's refusal grammar |
| `WEAK_ORDER_TRIPLE` | the declared default verdict set (a module constant, frozenset) | U3, U4 |

Everything else (validation helpers, mint machinery, private container state) is internal — no unit imports it.

## §2 THE SCHEMAS — field-level

All frozen dataclasses; no runtime deps — validation hand-rolled per the friction precedent.

**`ItemRow`** (frozen dataclass):
- `id: str` — non-empty string, stripped at validation (the _req_text precedent; an empty/whitespace id is unaddressable — ids are the citation vocabulary pairs and votes cite). [PROPOSED: refuse empty ids — the precedent's non-empty discipline; ids are structure.]
- `label: str` — any string content, stored verbatim, NEVER validated beyond type (opacity, R2/F6: labels are content; ids are structure). An emptiness rule on labels would interpret content — structurally impossible because no check reads content.

**`OperatorDeclaration`** (frozen dataclass):
- `id: str` — non-empty string (same discipline).
- `question: str` — any string content, stored verbatim (opacity; the stated question's semantics act at vote-generation, never at registration).
- `verdicts: frozenset[str]` — [PROPOSED: triple-only at birth] — the weak-order triple {prefer-a, prefer-b, tie} as the declared default; a declaration omitting the set gets the triple; a declaration carrying any set other than the triple refuses naming the legal form (the F2 deferral — incomparability/abstention — is the later widening path). Reason: R4 rules the triple as the declared default; accepting custom sets at birth would mint vote vocabulary downstream units have not priced.

**`RunManifest`** (frozen dataclass):
- `run_id: str` — the RUN-{####} handle (4-digit zero-pad, natural overflow; stored, never renumbered).
- `items: tuple[ItemRow, ...]` — the frozen rows tuple [PROPOSED: payload order preserved — canonicalization (id-sorted presentation) is the SCHEDULER's ruling (R7/F3), not registration's; sorting here would pre-empt U2's seam].
- `operator: OperatorDeclaration` — the declaration, frozen.
- `quorum: int` — ≥ 1, default 1 (R8, policy-as-data).
- `registered_at: str` — the ISO-8601 UTC stamp [PROPOSED: mint provenance at birth — the CF-3b "cheap now, expensive to backfill" doctrine; determinism untouched — purity rules the tally over votes, not the manifest across runs].

**`RegistryRefused`** (the refusal exception type) [PROPOSED: typed exception, the RefusedError precedent (friction_ledger.py:241-246)]: fields `expected: str`, `found: str`, `next_action: str` — carried as the three named fields plus a rendered message; raised, never returned (the CLI/service wrappers must render it — an exception is the library-tier carrier the wrappers catch; zero runtime deps keep it a plain Exception subclass).

## §3 REGISTER_RUN — the exact signature and semantics

**The container [PROPOSED]: class `Registry`, named per the naming law from its act-statement ("Hold the run manifests… the registry"): an in-memory manifest store constructed by the caller, store-as-parameter, single-process contract documented in the class docstring (the service tier later owns serialization — no DB, Q-setup-arch).** Not a module-level singleton (test isolation forecloses it); not a file (the ruled data plane: votes are data in/out; Option B's file store is the tool-tier idiom, refused); not a Session object (U5's unit).

**The signature (the single mutating op, one per store):**

```python
def register_run(
    self,
    items: Sequence[Sequence[str] | ItemRow],   # (id, label) tuples OR rows
    operator: OperatorDeclaration,               # the declaration object
    quorum: int = 1,
) -> tuple[str, RunManifest, int]                 # handle, the stored manifest, the manifest count
```

[PROPOSED: items accept 2-tuples (id, label) or ItemRow instances, both — the ergonomic minimum that stays shape-simple; `operator` as ONE declaration object (R3's triple folds into one declaration); `quorum` keyword-with-default (R8's default 1).]

**The validation order (deterministic; fail-fast on the first violation; every refusal writes nothing):**

1. **Shape** — each item is a 2-tuple or ItemRow; each id/question a non-empty string, stripped; labels strings.
2. **Cardinality** — len(items) ≥ 2.
3. **Duplicate ids** — uniqueness across the payload (exact string equality).
4. **Declaration form** — the verdict set is the triple.
5. **Quorum form** — integer ≥ 1.

**The refusal texts (drafted verbatim — the expected/found/next-action grammar):**

- **<2 items:** `RegistryRefused(expected="at least 2 item rows (a comparison needs a pair)", found="{n} item row(s)", next_action="register at least two rows — the empty list and the single item are named refusals, not special rankings")` — found names 0 and 1 distinctly (the empty list's found is "0 item rows", the single item's is "1 item row").
- **Duplicate ids:** `RegistryRefused(expected="all item ids unique within the payload", found="duplicate id '{id}' at positions {i}, {j}", next_action="disambiguate — one id per row; even trusted-source payloads are untrusted bytes")`.
- **Bad types (rows/ids/labels):** `RegistryRefused(expected="rows of (string id, string label)", found="{offending field} got {value!r}", next_action="the schema is the module's public types (ItemRow)")` — the _req_text precedent's form: "field 'X' is required and must be a non-empty string (got …)".
- **Empty id:** `RegistryRefused(expected="a non-empty id string", found="{value!r}", next_action="an id is the addressable identity pairs and votes cite — unaddressable ids refuse")`.
- **Malformed declaration (missing/empty id or question):** the _req_text form on the declaration's fields.
- **Verdict set not the legal form:** `RegistryRefused(expected="the weak-order triple {prefer-a, prefer-b, tie} (the declared set's default)", found="{value!r}", next_action="omit the set for the default, or declare the triple — custom sets are the F2 deferral's widening path")`.
- **Quorum out of range:** `RegistryRefused(expected="an integer >= 1 (default 1)", found="{value!r}", next_action="pass a positive integer or omit for the default; no upper bound — an unreachable quorum is tally's coverage-gate territory, not registration's")`.

**The mint:** per-store max+1 over the container's live manifests — RUN-0001 first, 4-digit zero-pad, natural overflow (RUN-10000 at the fifth digit); computed in the same synchronous act as the append (the atomic-mint window — the discipline the service tier later wraps in a lock); stored, never renumbered; the number retires with the run, never reused; no UUID (the single-serializer regime). Two registries mint independently (RUN-0001 on each — the store-as-data form).

**The copy-in freeze:** the manifest stores DEEP-COPIED, FROZEN ItemRow values built from the validated bytes at the boundary — never aliased caller references (in a reference-semantics language, "frozen" without copy-in is void: the caller mutates the list they passed and the "frozen" manifest moves). The copy-in is the mechanical form of "the write returns what landed, not what was sent."

**The return: `tuple[run_id, manifest, count]`** [PROPOSED: handle + the stored manifest + the manifest count — the built-in read-back]: the caller diffs sent vs stored from the return alone, without a second call (the invariant: the landing is verifiable from the return — "OK lines are not evidence; the store is").

**The manifest read op:**

```python
def read_manifest(self, run_id: str) -> RunManifest
```

Pure lookup by run_id; refuses unknown ids naming the legal set (the live handles); this is the surface U3's ground-truth checks ride. A manifest count accessor (`read_manifest_count`) returns the store's size — the mint's read-back.

## §4 THE TESTS — the eleven edges (tests/test_registry.py, named)

1. **`test_empty_list_refused`** — register_run([]) refuses; found names 0; nothing lands (count unchanged).
2. **`test_single_item_refused`** — register_run([("a", "one")]) refuses; found names 1 — a distinct found value from the empty list (both under the <2 class, both asserted).
3. **`test_minimum_registration_mints_run_0001`** — exactly 2 items, distinct ids → returns ("RUN-0001", manifest, 1); the boundary success.
4. **`test_duplicate_ids_refused`** — duplicate id refused naming the id and its positions; the store unchanged.
5. **`test_malformed_operator_declaration_refused`** — missing/empty id or question; verdict set a foreign set / a non-set / an empty set — each refused naming the legal form (the triple).
6. **`test_verdict_set_default_lands_as_data`** — declaration with no verdict set → the stored manifest carries the triple (the default lands as data).
7. **`test_quorum_as_data`** — omitted → manifest stores k=1; quorum=2 → stored verbatim; quorum=0 / -1 / "2" / 2.5 / None → refused naming the legal form (integer ≥ 1); a large k (e.g. 1_000_000) → accepted (no artificial cap, R6).
8. **`test_read_back_round_trip`** — payload in → return out → `read_manifest(run_id)` equal to the return AND to what was sent (send-vs-stored diffable); re-reading is stable across calls (the freeze).
9. **`test_aliasing_edge`** — mutate the caller's items list after registration; the stored manifest is unchanged (the copy-in freeze — the test that proves "frozen" means frozen).
10. **`test_mint_sequence`** — three registrations → RUN-0001/0002/0003, monotone; an identical re-registration mints a NEW run (no dedup at the library tier — request idempotency is a service-tier concern).
11. **`test_two_registries_mint_independently` + `test_opacity`** — two containers in one process each mint RUN-0001 (store-as-data, test isolation); labels of any content (empty string, unicode, very long) and the stated question accepted and stored verbatim — no content check fires.

**The floor:** pyright strict 0 errors 0 warnings; ruff (select ALL, line-length 120, the one named tests ruling S101/PLR2004) zero findings; zero ignores anywhere (`enableTypeIgnoreComments = false`, dead-ignore-as-error — an ignore is a ruling, never a convenience). Example tests only (example-driven; U1's gate names no property tests — U2's does, at its own brief).

**Kensho's independent re-run:** the same suite, fresh process, on kensho's own instruments — the read-back is the evidence, not the build's word.

## §5 THE LAWS RIDING THE MODULE

- **Five-field docstrings** (Purpose / Refuses when / Re-run / Touches / Provenance) on EVERY public symbol — Registry, register_run, read_manifest, ItemRow, OperatorDeclaration, RunManifest, RegistryRefused, WEAK_ORDER_TRIPLE — Provenance citing the rulings (R1/R2/R3/R4/R8, the five-op interface, scope-synthesis PART 3 §3.2).
- **The naming law at the symbol level:** each new symbol's name is the first word of its act-statement — "Register the run…" → `register_run`; "Read the manifest…" → `read_manifest`; "Hold the run manifests" → `Registry` (the container class's act-statement names its holding role; [PROPOSED: the module's name rides the route's ruled vocabulary per §1]).
- **Zero runtime dependencies:** hand-rolled fail-loud validation, no schema library (pyproject dependencies = [] stands).
- **No content interpretation (opacity):** labels and the stated question stored verbatim; validation touches structure only.
- **The no-mutation-verb freeze:** no edit op, no delete op exists for manifests; append-only is a property of the op set, not of permissions; corrections are new runs.
- **The single-process contract:** documented in the class docstring — the store is in-memory, one process; the service tier later owns serialization (no DB at birth). The atomic-mint window (max+1 + append in one synchronous act) is the discipline the lock later hardens.
- **The no-shell law:** zero subprocess in the library (pure logic).

## §6 THE GATE'S EVIDENCE — G-REGISTRY's five conditions mapped to this spec

| G-REGISTRY condition | The spec's carrier |
|---|---|
| 1. The registry module lands per the brief | §1 the module, §2 the schemas, §3 the op — the exact-task law: signatures, field names, refusal texts, test names pinned |
| 2. Schema round-trips green | §4 tests 3, 8, 11 — valid records accepted, invalid refused with expected/found/next-action naming the legal set and the store's truth |
| 3. Duplicate-id + <2-items refusals verified | §4 tests 1, 2, 4 — the empty list AND the single item as named refusals, distinct found values |
| 4. Pyright 0/0 + ruff zero findings, zero ignores | §4 the floor — the zero-and-zero bar, zero ignores (§5) |
| 5. Kensho's independent re-run green | §4 the evidence leg — the read-back (test 8's round-trip) is the evidence, not the build's word |

**The one load-bearing decision for the collaborator's eye (discover §3(e)):** the manifest container at the library tier — [PROPOSED: Option A, the in-memory frozen value / store-as-parameter class], because the ruled data plane ("stateless core, votes are data in/out, no DB") and test isolation both point there; the file-store form (Option B) is the tool-tier idiom the service tier inherits, and its precedent-setting is named: **U1's ruling sets the family form** — the vote ledger (U3) inherits the store-as-data discipline with its own lock-file layer per R9.

**Open questions carried to the gate (each [PROPOSED] above): the module layout (§1), the container class (§3), the return's triple (§3), the triple-only birth form (§2), payload-order preservation (§2), the registered_at stamp (§2), the typed exception (§2), the tuple/row argument form (§3), example-tests-only (§4).** Every one resolves understand/registry's ten [OPEN] items; the brief carries nothing unruled past the gate.

*Provenance: togo (統合, integrate), packet synthesize/registry, route prioritree-core, 2026-11-20 session. Read-only held — the content returned in-message at execution; landed by shinko via patch under the landing discipline (small patches, read-back).*
