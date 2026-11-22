# CENSUS/MECHANISM — part b of the set (a: census-mechanism-a.md) — the state mechanism; the seams; the read-back

## 3. The state mechanism — the chain, named
1. **Module-level singleton (per process)**: `app.state.seam = Serialize(STORE_HOME)` at import (service.py:153); `STORE_HOME = Path(".prioritree/runs")` CWD-relative (run_store.py:53) — resolved once at import; the lock minted at `Serialize.__init__` (service_store.py:89). Handlers read the seam per request via `cast("Serialize", request.app.state.seam)` — no `Depends` (B008 dodge).
2. **Per-request reconstruction**: each verb is ONE `threading.Lock` acquisition wrapping `Persist.load` + the act whole (service_store.py:118-208; sync handlers on FastAPI's threadpool, :7-9). `Persist.load` reads the whole JSONL file, pre-pass validates every line, then rebuilds a **fresh in-memory door** — `Session(Registry())`, re-register from the manifest line, in-order re-casts of every vote line (run_store.py:684-705).
3. **Lifetime**: lock + seam = process · in-memory Session/Registry/ledger = **one request** (the dedup index fresh by construction) · the **append-only JSONL files on disk are the only cross-request state** (save-at-cast, one line + newline + flush per write, run_store.py:726-736). Multi-process widening banked under the single-worker launch (service_store.py:56-58).

## 4. The seams — envelope divergences from the core's ruled return forms
1. **register**: core returns the `(run_id, manifest, count)` triple → wire returns `{"run_id": stem}` ALONE (manifest + count dropped) — and the wire's `run_id` is the **file stem**, not the core's in-file handle (two id spaces: file `RUN-0007.jsonl`'s lines may say `RUN-0001`; run_store.py:536-539, service_store.py:104, run_store.py:868-882). Clients address runs by stem; the built-in read-back (handle + post-append count) never crosses the wire.
2. **cast**: `VoteRecord` **elided** from the ack (service.py:288-295) — pair/winner/stamps/notes/supersedes durable only in the file.
3. **state**: `VoteCensus` → `{"total","items"}` — `vote_log` elided (the stamps re-mint at load; "rendering lies", service.py:329-330) and `per_pair_counts` dropped entirely.
4. **tally**: `coverage.pair_counts` re-keyed `Pair` → `"item_a|item_b"` strings (service.py:387-392, JSON keys must be strings) — the one priced reconciliation; all else asdict-whole.
5. **DONE**: the core's RAISED `ExhaustedQueue` becomes a 200 VALUE body `{"done": true, + three fields}` (service.py:280-282).
6. **Refusals**: typed exceptions → three-key bodies; the 400 re-badge carries FastAPI's native `{"detail": [...]}` grammar, NOT the three-field form (deliberate, service.py:174-195); the 500 fabricates a three-part envelope with no core counterpart (expected = method+path, :198-223).

Ruled properties holding at the wire (conformity, stated as fact): the state read never refuses on coverage (service.py:331-333); the tally ALWAYS refuses on it (409, :385-386); `tally_rank`'s write target is nothing (rank appends nothing — a locked read); `next_pair` serves the bare pair, no scores.

**Read-back** (files actually read): `.plans/ideation/2026-11-19-prioritree-birth/.junro/junro.json` (whole — Q-solution-space's five-op ruling + Q-setup-arch) · `src/prioritree/__init__.py`, `session.py`, `service.py`, `service_store.py`, `run_store.py` (whole) · `votes.py` :43-105, `tally.py` :40-154, `registry.py` :29-110, `scheduler.py` :28-42 · greps: the fastapi sweep (service.py the sole server), the `@app.` route census, the value-type sweep. READ-ONLY — nothing written to disk.
