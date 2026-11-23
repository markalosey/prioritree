<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — synthesize/installspec

**Route:** prioritree-review (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T02:17:35Z |
| 2 | report | togo | 2026-11-23T02:26:43Z |
## Reported by togo — 2026-11-23T02:26:43Z

# THE INSTALL UNIT'S EXACT-TASK SPEC — the four files' bytes whole (synthesize/installspec; togo, 2026-11-22)

## §R THE READ-BACK (the ground, cited)

The approved unit brief (reports/synthesize/install.md — G-INSTALL-BRIEF approved: the force-include mechanism, the ordered resolution, the four-file fence, the test plan's split) · pyproject.toml whole (:11-13 the build system; :15-16 the console script; :18-19 the wheel target; the ruled-comment style at :26-144) · src/prioritree/web.py whole (the module docstring :14-28; the imports :46-58; the constants :62-85 incl. :76-77 the homes; the child app + mounts :112-120; the five-field docstring form at :132-143) · tests/test_web_face.py whole (the grammar :2-17; the imports :19-31; the injection fixture :44-48; the arcs :51-311) · README.md whole (:52 the web tier's line count; :55 the floor line; :103-107 the MCP's two clone forms; :159/:166/:180/:182 the four re-ruled lines in their neighborhoods) · the importlib.resources verification (§0 below — the named venv path absent; the installed packages' own forms read instead: .venv/lib/python3.13/site-packages/jsonschema_specifications/_core.py:7-37 + jinja2/loaders.py:303-364 + starlette/templating.py:1-70) · mcp_server.py:571-580 (the two run forms, port 8000 hardcoded) + :103-113 (the naming-law precedent) · service.py:530-540 (the tail mount) · tests/test_cli.py:4-5 (the suite's no-subprocess fence) · keisan's census (reports/census/commands.md — the install findings, the fresh-clone arithmetic, the 197-live floor) · suisen's recommendation (reports/design/install-story.md — the hybrid (e)) · the review brief (reports/synthesize/review-brief.md — §1a the line cites; hyoka's rank-1 the stale-count class) · the gates' conditions (the store's junro.json:516 G-INSTALLSPEC-BRIEF's three; :532 G-INSTALL's four). READ-ONLY held — nothing written beyond this report.

## §0 THE VERIFICATION STANCE (the import-verification lesson, answered honestly)

The dispatch named `.venv/lib/python3.13/importlib/resources/__init__.py` as the verification target IF READABLE — IT IS NOT: the venv is thin (site-packages only; the stdlib lives in the uv base install, outside this tree's permission boundary; the named path does not exist). NEVER MEMORY ALONE — the in-tree verification instead, against the INSTALLED REALITY of this exact interpreter (CPython 3.13.9):

- **VERIFIED — files()'s whole call form**: .venv/.../site-packages/jsonschema_specifications/_core.py:7-12 imports `from importlib.resources import files` (the try/except's first branch — resolving in the modern stdlib; the package WORKS on this interpreter, its REGISTRY built at import by the mcp stack) and :29 calls `files(__package__).joinpath("schemas")` — the string anchor + the tail-join, the exact form this spec's fallback uses, plus the Traversable protocol's methods (:30-37: iterdir/is_file/read_text/name) exercised live.
- **VERIFIED — the mounts' parameter surface**: starlette/templating.py:54-70 (Jinja2Templates' directory overloads, str accepted) — the current web.py passes str literals today; str stays type-correct.
- **UNVERIFIABLE THIS SEAT, NAMED (never ruled blind)**: (a) `as_file()` — NO in-tree source exercises it; the spec does NOT rule it; (b) whether files()'s Traversable is a pathlib.Path on filesystem installs (the str() consumption's real-path claim) — the ruled lanes (the clone's CWD-first branch; the filesystem install's fallback) make it so per the API's documented contract, but the PROOF is split exactly as the brief ruled (§4): **the suite falsifies the order logic + the derivation's form at the editable clone; the gate's live install proves the fallback's rendered truth** (the brief's own words: "the fallback branch's INSTALLED reality is provable only at the gate's live install").
- jinja2's own PackageLoader (loaders.py:303-364, installed 3.1.6) was read as the cross-check: the installed ecosystem resolves package-data REAL paths via find_spec + submodule_search_locations — the honest alternative NAMED but declined: the brief RULED importlib.resources as the mechanism (§2c), and its forms are the verified surface above.

## §1 PYPROJECT.TOML — THE WHEEL REGION (exact bytes)

The region :18-19 today:

```toml
[tool.hatch.build.targets.wheel]
packages = ["src/prioritree"]
```

REPLACE with (the packages line byte-unchanged; the region grows the ruled comment + the force-include sub-table):

```toml
[tool.hatch.build.targets.wheel]
packages = ["src/prioritree"]

# RULING (install-brief §2 + Q-repo-review ruling 4, G-INSTALL-BRIEF approved
# 2026-11-22): the wheel SHIPS the web tier's authored homes as package data —
# web/templates + web/static map INTO the package at flat dests (prioritree/
# templates, prioritree/static — NO prioritree/web/ directory: the web.py
# module's namespace-portion is never shadowed). The clone is untouched (the
# mapping is build-time only, zero moves on disk); web.py's loader seam
# resolves the CWD's copy first, this shipped copy the fallback. The MCP rides
# by construction (mcp_server.py among the fifteen modules packages carries).
[tool.hatch.build.targets.wheel.force-include]
"web/templates" = "prioritree/templates"
"web/static" = "prioritree/static"
```

THE FORM'S PINS: quoted keys (TOML bare keys bar "/"), double quotes (the tree's style), the sub-table's dotted path exact, the placement directly under the wheel target (before [tool.ruff] at :21). **THE COHERENCE PIN**: the dests' tails (templates/static) ARE web.py's tail constants AND the resolver's joinpath tails — one spelling across the mapping, the constants, and the derivation; a divergence at any of the three is the unit's own falsification. uv.lock untouched (hatchling is already the pinned backend; no dep change). The carriage is PROVEN at the gate's build inspection (the wheel carries prioritree/templates' 14 + prioritree/static's 2 + the fifteen modules incl. mcp_server.py) — never a suite test (the brief §4's ruled split).

## §2 SRC/PRIORITREE/WEB.PY — THE LOADER SEAM (exact bytes)

**(a) THE IMPORTS (:46-58 today) — the stdlib group grows two lines (alphabetical: importlib.resources < pathlib < typing; the isort law held):**

```python
from __future__ import annotations

from importlib.resources import files
from pathlib import Path
from typing import Any, Final

import httpx2
```

(all following lines byte-unchanged; the brief §6.2's "importlib.resources imported at the top" held.)

**(b) THE CONSTANTS — the homes :76-77 byte-unchanged; INSERT after :77 (_STATIC_HOME):**

```python
# The fallback's own vocabulary (install-brief §2): the shipped package's
# name — the force-include dest root, pyproject's mapping naming the same
# package — + the two tails (the dests' tails; one spelling across the
# mapping, these constants, and the resolver's derivation).
_PACKAGE: Final[str] = "prioritree"
_TEMPLATES_TAIL: Final[str] = "templates"
_STATIC_TAIL: Final[str] = "static"
```

**(c) THE RESOLVER — INSERT after the UNION_LANES line (:110), before the child-app comment (:112). THE NAME per the naming law: the act-statement's first word (the brief's own example verbatim — "Resolve the web home: the CWD's copy first, the shipped package's the fallback" → the resolve symbol; the tree's function-symbols' verb form, schedule_pairs/tally_votes the precedents; the nominalization (server/Registry) is the object-symbol case — declined for a function):**

```python
def _resolve(home: str, tail: str) -> str:
    """Resolve the web home: the CWD's copy first, the shipped package's the fallback.

    Purpose: the ordered resolution for both authored homes (the templates
    + the static): the CWD-relative copy WINS when present (the clone's
    repo-root discipline byte-preserved — the mounts receive the same
    bytes they receive today), else the shipped package's own copy
    (importlib.resources' files() over the wheel's force-include mapping
    — the installed lane renders from the package).
    Refuses when: never — a missing directory is a VALUE, never an error
    (the resolution lands on the derived path; the fold is the render
    tier's honest behavior — the wrong-cwd clone folds at the honest 500,
    the scratch-cwd boot stands on check_dir=False).
    Re-run: deterministic given the filesystem (the CWD's state + the
    package's own).
    Touches: nothing — a pure resolution over the filesystem's state.
    Provenance: install-brief §2/§3 (the ordered resolution),
    Q-repo-review ruling 4, G-INSTALLSPEC-BRIEF.
    """
    if Path(home).is_dir():
        return home
    return str(files(_PACKAGE).joinpath(tail))
```

THE CONTRACT IN BYTES: the CWD branch returns the home VERBATIM (the current mounts' form preserved byte-for-byte — the clone's behavior unchanged); the fallback branch derives the shipped package's path (the verified files()+joinpath form); the missing-directory case NEVER raises (the fold stays the render tier's — the wrong-cwd clone's honest 500, the scratch-cwd boot's check_dir=False cure). pyright strict: `Path(home).is_dir()` bool; `files(_PACKAGE).joinpath(tail)` Traversable; `str(...)` of it legal; the return `str` — zero ignores (the zero-findings bar).

**(d) THE MOUNTS (:119-120 today) — REPLACE the two lines (the check_dir=False flag byte-preserved; the :113-117 comment byte-unchanged — its rationale holds at the resolved path):**

```python
web_app.mount("/static", StaticFiles(directory=_resolve(_STATIC_HOME, _STATIC_TAIL), check_dir=False), name="static")
templates = Jinja2Templates(directory=_resolve(_TEMPLATES_HOME, _TEMPLATES_TAIL))
```

**(e) THE MODULE DOCSTRING (:23-28 today) — REPLACE the sentence (from "The CWD-relative homes" through "re-settle)."; the loader/render seam's law at :14-17 byte-unchanged — the authored files remain the source of truth, the wheel ships their copies):**

```
emits, nothing regens, no --check). The web homes resolve IN ORDER
(install-brief §2/§3): the CWD-relative copy FIRST (the repo-root launch
discipline, STORE_HOME run_store.py:53 the precedent — the authored files
win when present), the shipped package's copy the FALLBACK
(importlib.resources over the wheel's force-include mapping — the
installed lane renders from the package); the static mount's
check_dir=False is the named cure for the acceptance harness's
scratch-cwd boot (StaticFiles raises at import on an absent directory;
the store mkdirs on demand — the asymmetry named at the re-settle; a
wrong cwd in the clone folds honestly — both branches miss).
```

**(f) THE FENCE'S NEGATIVE SPACE**: the routes, the controllers, the in-process client, the fold/refuse handlers, __all__, service.py's tail mount, mcp_server.py, run_store.py's STORE_HOME, cli.py, the Makefile — zero bytes. The web.py line count changes by the seam (~+35); the honest landed number is MEASURED at step 2's read-back (never predicted) and rides README :52 at step 4 (§4 below).

## §3 TESTS/TEST_WEB_FACE.PY — THE RESOLVER'S ARCS (N=3; the suite 197 → 200)

**(a) THE FILE'S DOCSTRING — two re-rules. Line :8 today reads "...extends to the web tier whole (store-as-parameter; no env, no CWD games)." REPLACE that sentence with:**

```
extends to the web tier whole (store-as-parameter; no env, no CWD games —
the resolver arcs alone chdir, by pytest's own monkeypatch fixture with
its guaranteed restore: the CWD IS the resolution's own input).
```

**And the arcs sentence (:9-15): after "...a mis-named home fails loudly);" INSERT:**

```
the resolver arcs (the loader
seam's ordered resolution: the CWD's copy first, the package's the
fallback, the fold preserved at a wrong cwd);
```

**(b) THE IMPORTS (:19-31 today) — REPLACE whole:**

```python
from __future__ import annotations

from pathlib import Path

import pytest

from fastapi.testclient import TestClient

from prioritree.service import app
from prioritree.service_store import Serialize
from prioritree.web import _resolve
```

(Path moves OUT of the TYPE_CHECKING block to a runtime import — the arcs mkdir/exists at runtime; the TYPE_CHECKING block AND its typing import DELETE — their only tenant was Path, a dead block is out of grammar; the fixture's `tmp_path: Path` annotation resolves either way under future-annotations.)

**(c) THE FIXTURE FORM — RULED (the dispatch's own question): `monkeypatch.chdir(tmp_path)`** — pytest's sanctioned CWD control (the guaranteed restore, no os.chdir, no env, no leakage to the client-fixture arcs). The file's "no env, no CWD games" law is the SERVICE-SEAM isolation's law; the resolver's input IS the CWD — its arcs control it by the sanctioned fixture, the grammar's honest extension named in the docstring re-rule. The client fixture (:44-48) byte-unchanged; the resolver arcs take NO client (pure function arcs — no store, no service, no env).

**(d) THE THREE ARCS — INSERT after test_static_pair_serves (:68), the loader seam's own cluster, before test_sitting_serves_first_pair_server_side (the literals carried 1:1 per the file's own vocabulary grammar; the S101/PLR2004 tests ruling carries them; no subprocess — the no-shell law held):**

```python
def test_resolve_prefers_the_cwd_home(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """A present CWD home resolves to itself — the clone's form, the order's first branch."""
    monkeypatch.chdir(tmp_path)
    (tmp_path / "web" / "templates").mkdir(parents=True)
    assert _resolve("web/templates", "templates") == "web/templates"


def test_resolve_falls_back_to_the_package(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """An absent CWD home derives the package path — the installed form, the order's second branch."""
    monkeypatch.chdir(tmp_path)
    resolved = _resolve("web/templates", "templates")
    assert resolved != "web/templates"
    assert Path(resolved).is_absolute()
    assert resolved.endswith("templates")


def test_resolve_keeps_the_fold_at_a_wrong_cwd(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """The wrong-cwd fold preserved: both branches miss, the resolution never raises."""
    monkeypatch.chdir(tmp_path)
    resolved = _resolve("web/templates", "templates")
    assert not Path(resolved).exists()
```

**THE ARCS' HONESTY PINS**: arc 1 — the CWD branch returns the input BYTE-VERBATIM (the current form preserved: the clone's law); arc 2 — the derivation's FORM (absolute — the branch distinction: the CWD form is relative, the package's absolute; the tail named) WITHOUT re-running the implementation's own call; arc 3 — the fold's precondition (the clone's editable package carries no web data by design — the derived path absent, the resolver never raises, the miss travels to the render tier: the honest 500 stands, byte-preserved). The arcs do NOT assert the package path's existence (the suite never runs installed — the brief's ruled split); the existing landing/static serves (:51-68) carry the repo-root import's CWD-first proof; the fold fragment arc (:295-311) carries the render-tier fold. **N = 3 pinned: 197 → 200.**

## §4 README.MD — THE FOUR RE-RULED LINES (before/after fenced) + THE TWO COUNT CONSEQUENCES

**Line :159 (the discipline's CWD law) — BEFORE:**

```
- **The CWD law.** The store (`.prioritree/runs`) and the web mounts (`web/templates`, `web/static`) resolve CWD-relative — run from the repo root, or your data lands where you stood (the directories mint silently on demand). The CLI's `--home` is the per-invocation escape.
```

**AFTER (the store alone CWD-relative; the mounts' ordered resolution named; the wrong-cwd edge honest):**

```
- **The CWD law.** The store (`.prioritree/runs`) resolves CWD-relative — run from the repo root, or your data lands where you stood (the directory mints silently on demand); the CLI's `--home` is the per-invocation escape. The web homes resolve in order: the CWD's `web/templates` + `web/static` first (the repo's authored files — the clone's form), the installed package's copies the fallback — a wrong cwd in the clone folds honestly (the honest 500); an installed location always renders.
```

**Line :166 (the clone paragraph) — BEFORE:**

```
**The clone — the whole product.** The only path that operates all five tiers: the web tier's templates and static files ride the repo, and the CWD-relative homes resolve at the root. Requirements: Python 3.13+ and uv. The full honest sequence:
```

**AFTER (the "only path" claim cured — both lanes whole; the clone = the source + the floor, the brief §6.3's own words):**

```
**The clone — the source and the floor.** The web tier's templates and static files ride the repo (`web/`), the homes resolve at the root, and the tool lane below serves the same pages from the installed package. Requirements: Python 3.13+ and uv. The full honest sequence:
```

**Line :180 (the tool lane — the web-absence truth CURED) — BEFORE:**

```
**`uv tool install .` — the CLI anywhere.** Installs the `prioritree` console script and its six dependencies, usable from any directory. State is per-project by design: the store mints at `.prioritree/runs` under your CWD; `--home` redirects. The web tier does not ride this lane today: the wheel carries `src/prioritree` only (no web templates) — the clone is the web tier's only home.
```

**AFTER (the web truth cured, the serve form byte-runnable, the store story, the MCP's env form — never the bare form, the brief §2's own fence):**

```
**`uv tool install .` — the tool lane.** Installs the `prioritree` console script and its six dependencies — the five CLI ops run from any directory. State is per-project by design: the store mints at `.prioritree/runs` under your CWD; `--home` redirects. The web tier rides this lane too: the wheel ships the templates and static files as package data, and the web homes resolve them from the installed package. Serve the web with the tool env's uvicorn — `$(uv tool dir)/prioritree/bin/uvicorn prioritree.service:app` (any directory; the store mints where you stood). The MCP rides the same install: `$(uv tool dir)/prioritree/bin/python -m prioritree.mcp_server` for stdio, or the same command with `--serve` (port 8000 — one at a time with the web).
```

**Line :182 (the no-PyPI line) — BEFORE:**

```
**Not on PyPI.** `uv tool install prioritree` and `pip install prioritree` do not resolve — Priori-tree is not published. The publish is deferred: the license has landed; packaging and CI remain.
```

**AFTER (the precondition set shrunk — the packaging landed, CI remains):**

```
**Not on PyPI.** `uv tool install prioritree` and `pip install prioritree` do not resolve — Priori-tree is not published. The publish is deferred: the license and the packaging have landed; CI remains.
```

**THE TWO COUNT CONSEQUENCES (the spec's named additions beyond the brief's four-line letter — the collaborator rules at the gate; the reason: a stale load-bearing number is hyoka's rank-1 BLOCKING class, and this unit's own act makes both stale):** (1) line :55's "The quality floor: 197 tests green, pyright clean, ruff clean." → "The quality floor: 200 tests green, pyright clean, ruff clean." (the suite's growth, §3's N); (2) line :52's "`src/prioritree/web.py` (654 lines, nine routes, ...)" → the line count replaced with the LANDED web.py's measured count (step 2's read-back — measured, never predicted). Both ride step 4's README dispatch (one file per dispatch held).

**THE RUNNABILITY PINS (condition 2's letter)**: every command the re-ruled lines name is byte-runnable at the spec's own form — `uv tool install .` (keisan's verified path form); `prioritree` at any directory (the console script on PATH); `$(uv tool dir)/prioritree/bin/uvicorn prioritree.service:app` (the tool env's uvicorn — uvicorn[standard]'s console script rides the tool env's bin; `uv tool dir` uv's stable surface; the gate's live check runs it and probes GET /); `$(uv tool dir)/prioritree/bin/python -m prioritree.mcp_server [--serve]` (the env-interpreter form — the bare `python -m` form is NEVER documented, the brief §2's own fence). Coherence held: the Quickstart :34's `uv tool install .` and :103-107's clone MCP forms byte-unchanged.

## §5 THE NO-BREAK PROOFS

1. **THE FRESH-CLONE STORY BYTE-UNCHANGED**: the CWD-first branch returns the home VERBATIM — at the repo root the mounts receive the same bytes as today; web/ stays at the repo root; the tracked set unchanged (the force-include is a build-time mapping — ZERO moves on disk); the Quickstart (:19-27) and the clone sequence (:168-178) byte-identical; git status at the unit's close shows exactly four files changed, nothing moved.
2. **THE SUITE**: 197 + 3 = 200 green; pyright strict 0/0/0; ruff zero findings, zero new ignores (the arcs ride the S101/PLR2004 tests ruling; no subprocess — the no-shell law held; the fixture is pytest's own monkeypatch).
3. **THE AUTHORED FILES**: web/templates' 14 + web/static's 2 tracked files byte-untouched (the mapping reads them at build time; the template-source law and the never-hand-edit law stand).
4. **THE WRONG-CWD FOLD — THE EDGE RULED (the dispatch's own question)**: at a scratch cwd IN THE CLONE, both branches miss (no CWD copy; the editable package carries no web data by design) → the resolution lands on the absent package path → check_dir=False boots, the render tier folds at the honest 500 — byte-preserved (the acceptance harness's scratch-cwd boot unchanged, arc 3's pin). AT AN INSTALLED LOCATION THE FALLBACK RENDERS (the package data present) — the wrong-cwd fold is the CLONE form's behavior only, never the install's; README :159's re-ruled line names exactly this edge.
5. **THE OTHER TIERS**: service.py's tail mount consumes the same web_app (zero bytes); mcp_server.py zero bytes (rides the wheel by construction — packages' fifteen modules); run_store.py's STORE_HOME CWD-relative BY DESIGN (the --home escape named, never changed); cli.py, the Makefile, the .opencode surfaces, the .plans records — untouched.
6. **THE WHEEL'S CARRIAGE — THE GATE'S LIVE PROOF** (never a suite test, the brief §4's ruled split: the suite's laws are network-free + venv-only; the install arc needs the build + the tool env): the built wheel carries prioritree/templates' 14 + prioritree/static's 2 + the fifteen modules incl. mcp_server.py — proven at kensho's validate/install.

## §6 THE PER-STEP PLAN (R8, one file per dispatch; the exact-task law; one commit per increment)

1. **pyproject.toml** — §1's region whole. Read-back: the region's bytes at §1's fence; uv.lock untouched.
2. **src/prioritree/web.py** — §2's seam whole. Read-back: the seam's bytes at §2's fences + the LANDED line count (the honest measured number for README :52).
3. **tests/test_web_face.py** — §3's arcs whole (the docstring re-rules, the imports, the three arcs). Read-back: 200 collected; the arcs' names.
4. **README.md** — §4's four re-ruled lines + the two count lines. Read-back: every line byte-verified runnable at its cited form.
5. **THE FLOOR** — `make test` (200 green) + `make lint` (ruff zero findings) + `make typecheck` (pyright 0/0/0). The step's own gate: any finding fixed in the same turn, never a batch pile.
6. **THE GATE'S LIVE LEGS → G-INSTALL**: kensho's validate/install (the wheel build + the contents inspection — prioritree/templates 14 + prioritree/static 2 + the fifteen modules incl. mcp_server.py; `uv tool install .` at the spec's form; the CLI probes at an arbitrary CWD; the serve at the installed location — `$(uv tool dir)/prioritree/bin/uvicorn prioritree.service:app`, GET / renders, the fallback proven; the MCP under the tool env's interpreter, stdio + --serve; the floor's re-run; the fresh-clone story's byte re-walk) + moho's re-walk (the cold user's walk of the CURED README whole — the clone lane + the tool lane's new lines; the ease-of-use evidence riding the gate).

## §7 THE GATE MAPPING — G-INSTALLSPEC-BRIEF's three conditions (junro.json:516)

1. **"the exact-task spec landed — the packaging fix's bytes whole (web/ into the wheel: the ruled mechanism [package-data/importlib-resources or the spec's form]; the CWD question at an installed location answered honestly; the MCP confirmed riding) + the documented install lanes' exact commands"** → §§1-4: the force-include region + the loader seam + the arcs + the README's re-ruled lines, every command at its byte-runnable form; the CWD question honest (§2c's contract + §4's :159/:180 lines + §5.4's ruled edge — never silently wrong); the MCP confirmed riding (§1's ruled comment + §5.5).
2. **"nothing promised that doesn't run — every documented command verified at the spec's own form (uv tool install . tested; the CLI-anywhere story; the web tier's serve at an installed location or its honest limitation named)"** → §4's runnability pins + the gate's live legs running every named form; the honest limitation still named where it stands (the store CWD-relative BY DESIGN, --home the escape — :159/:180's own words).
3. **"the collaborator approves — the build fires only after"** → this spec + its ONE open question ride the gate: the two count-lines (:52/:55 — the brief's fence named four; the counts are the unit's own consequences, hyoka's rank-1 class; RECOMMENDED: land both at step 4 with the measured numbers). **THE TRADE-OFF THE UNIT CARRIES** (the brief's own, carried whole): the loader's seam grows the fork (CWD-first, package-fallback) — the price of curing the install WITHOUT moving the clone's ruled layout; and the fallback branch's installed reality is provable only at the gate's live install — the suite covers the order logic, the gate covers the truth.

— togo, the synthesis leg, read-only by design; this report is the one write.
