# CENSUS/MECHANISM — how the existing server fronts the core's five-op interface (prioritree-ux) — rikai — part a (b: census-mechanism-b.md)

## 1. The core's public face — the five ops (`src/prioritree/session.py`, class `Session`, :95-318; the composition layer the wrappers cite)

| op | signature (session.py) | return form |
|---|---|---|
| `register_run` | `(items: Sequence[Sequence[str] \| ItemRow], operator: OperatorDeclaration, quorum: int = 1)` :161-166 | `tuple[str, RunManifest, int]` — (run_id, manifest, count); `RegistryRefusedError` wrapped into `VotesRefusedError` :184-189 |
| `next_pair` | `(run_id: str, seed: int \| None = None)` :191 | `tuple[str, str, int]` — the bare (item_a, item_b, count), no state, no scores; raises `ExhaustedQueue` (the DONE signal, three fields, :52-92, :228-238) |
| `cast_vote` | `(run_id, pair: Pair \| Sequence[str], winner, comparator_id, comparator_class, notes=None, supersedes=None)` :240-249 | `tuple[str, VoteRecord, int, bool]` — the ack quadruple; `VotesRefusedError` verbatim |
| `read_vote_state` | `(run_id: str)` :278 | `VoteCensus` — `run_id, per_pair_counts: Mapping[Pair,int], per_item_counts: Mapping[str,int], vote_log: tuple[VoteRecord,...]` (votes.py:100-103); NEVER refuses on coverage |
| `tally_rank` | `(run_id: str)` :294 | `TallyResult` — `ranked_groups: tuple[tuple[str,...],...]`, `per_item_wins/losses/ties: Mapping[str,int]`, `coverage: CoverageDatum` (`components, cycle, pair_counts: Mapping[Pair,int], done: bool`, tally.py:78-81), `algorithm_version` (tally.py:106-111); `TallyRefusedError` (SAFE HALT — the emission ALWAYS refuses on coverage) verbatim |

Types' homes: `Pair` scheduler.py:28 · `ItemRow`/`OperatorDeclaration`/`RunManifest` registry.py:29/:48/:68 · `VoteRecord`/`VoteCensus` votes.py:43/:76. Every refusal carries expected/found/next_action as data (typed exceptions).

## 2. The server's wiring — `src/prioritree/service.py`, the ONLY server module (grep: the sole fastapi import; `app = FastAPI()` :152, launch `uvicorn prioritree.service:app`)

| core op | exposed? | route → handler (service.py) | the chain (core call last) | wire success response |
|---|---|---|---|---|
| register_run | **yes** | POST `/runs` → `register` :227 | `Serialize.register` → `Persist.register` → `Session.register_run` (run_store.py:551-552) | 201 `{"run_id": <file stem>}` :253 |
| next_pair | **yes** | GET `/runs/{run_id}/next?seed=` → `serve` :256 | `Serialize.serve` → `Persist.load().serve` → `Session.next_pair` (run_store.py:832) | 200 `{"item_a","item_b","count"}` :283; DONE → 200 `{"done": true, expected, found, next_action}` :281 |
| cast_vote | **yes** | POST `/runs/{run_id}/votes` → `cast_vote` :286 | `Serialize.cast` → `Persist.load().cast` → `Session.cast_vote` (run_store.py:789) | 200 `{"vote_id","count","acknowledged"}` :319 |
| read_vote_state | **yes** | GET `/runs/{run_id}/state` → `census` :323 | `Serialize.census` → `Persist.load().census` → `Session.read_vote_state` (run_store.py:850) | 200 `{"total","items"}` :346 |
| tally_rank | **yes** | GET `/runs/{run_id}/tally` → `rank` :357 | `Serialize.rank` → `Persist.load().rank` → `Session.tally_rank` (run_store.py:866) | 200 `asdict(TallyResult)` with pair_counts re-keyed :388-392 |

Ops NOT exposed: **none** — all five ride 1:1 (route census: exactly 5 `@app.` routes + 2 exception handlers, no APIRouter elsewhere). Status mapping: `StoreRefusedError`→404 (both families), `VotesRefusedError`→422, `TallyRefusedError`→409 (SAFE HALT), `ExhaustedQueue`→200-DONE, native `RequestValidationError`→400 (re-badged, :174-195), unexpected→500 crash envelope (:198-223). Refusals rendered at ONE point, `render_refusal` :156-171.
