<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — research/publish-arithmetic

**Route:** prioritree-publish (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-28T17:10:34Z |
| 2 | report | keisan | 2026-11-28T17:20:00Z |
## Reported by keisan — 2026-11-28T17:20:00Z

# THE PUBLISH'S ARITHMETIC — keisan (research/publish-arithmetic, 2026-11-28)

The claims lane held: every number below tool-carried at the calculate instrument, its trace line quoted; every projection labeled a projection; the two numbers my instrument set cannot carry named honestly, never faked. READ-ONLY held; no file touched but this report.

## 1. THE $0 LEDGER — the free-tier bar extended, priced at the channel's recorded surfaces

THE FIVE COST COMPONENTS, each $0, the total at the tool:
{"op":"sum","args":{"values":"[0,0,0,0,0]"},"result":0}
- PyPI hosting $0 — the free tier's standing truth; PyPI carries no paid publishing tier.
- PyPI upload $0; PyPI bandwidth $0 — the free tier.
- The CI's minutes at the free runner $0 — the CI effort's own verification standing (Q-ci-surface R1's record: the public form's unlimited minutes, "$0 at any multiple").
- The tooling $0 — twine/hatchling/uv free OSS; the account itself $0 AND ALREADY EXISTS (the account ruling, settled before this leg priced the channel).

THE PAID-TIER QUESTION — THE ABSENCE PROVEN AT THE RECORDED SURFACES: none found anywhere in the channel (PyPI no paid tier; GitHub Actions free for public repositories; the manual form's tools free). Any cost found is priced and refused at the same bar the CI effort held; none found. The design gate carries the final word.

THE SIZE CAPS — the gap arithmetic (the caps' exact source numbers are rikai's landscape lane, weighed at the design gate; this seat prices the artifact's side of the gap):
- The wheel's payload = 38 text files (§2). At the long-standing published per-file cap 100 MiB = 104,857,600 bytes: {"op":"divide","args":{"a":"104857600","b":"38"},"result":2759410.5263157897} — each of the 38 files would need to AVERAGE ~2.76 MB to approach the cap. At the most conservative historical cap 60 MiB: {"op":"divide","args":{"a":"62914560","b":"38"},"result":1655646.3157894737} — ~1.66 MB/file. The tree's payload class (source modules, HTML templates, CSS/JS; the largest module ~700 lines per the record) sits orders of magnitude below either bound: THE CAP IS NOT A BINDING CONSTRAINT at any published number.

THE RATE LIMITS + THE ACCOUNT'S FORMS: the upload API's rate limits do not bind a human-paced single-package cadence (one release act per version; the limits target bulk abuse — the exact numbers rikai's source lane). The account exists ($0, the ruling); the token vs the trusted-publisher form is the design's ruling (the custody class shindan's parallel axis) — BOTH FORMS $0 money.

## 2. THE ARTIFACT'S NUMBERS

THE WHEEL'S CONTENTS (the premise law at the bytes — pyproject:18-31's mapping, tansa's census the parallel read): 19 modules (src/prioritree) + 17 templates (web/templates) + 2 statics (web/static) = {"op":"sum","args":{"values":"[19,17,2]"},"result":38} shipped files — the packaging cure's force-include (templates→prioritree/templates, static→prioritree/static, the MCP riding by construction among the nineteen).

THE BYTES — THE HONEST LIMIT, NAMED: the built artifacts stand at dist/ (prioritree-0.1.0-py3-none-any.whl + prioritree-0.1.0.tar.gz; gitignored by dist/.gitignore's "*", never committed). THIS SEAT'S INSTRUMENT SET CARRIES NO BINARY READ — the read refused verbatim: "Cannot read binary file"; the grep over the .whl: no matches (binary suppressed). The wheel/sdist BYTE TOTALS are the build unit's own live fact (a stat at the dist) or the collaborator's hands — named, never estimated. What this seat computes exactly: the file-unit count (38) and the cap-gap arithmetic (§1) — both robust at any byte total a 38-file text payload can carry.

THE DEPENDENCY COUNT — the install's total pull priced (the closure traced edge-by-edge at uv.lock's bytes, CPython 3.13, non-win32):
- The seven runtime seeds: {"op":"count","args":{"values":"[\"fastapi\",\"httpx2\",\"itsdangerous\",\"jinja2\",\"ouncemcp\",\"python-multipart\",\"uvicorn\"]"},"result":7}
- The closure by expansion level [7 seeds; +22 level-1 (fastapi 7, httpx2 3, jinja2 1, ouncemcp 3, uvicorn+standard 8); +9 (fastmcp 1, jsonschema 4, tiktoken 2, pydantic 2); +19 (fastmcp-slim base 5, client 4, server 10); +8 (mcp 2, email-validator 1, rich 2, py-key-value-aio 3); +4 (aiofile 1, requests 2, authlib 1); +4 (cryptography 1, cffi 1, markdown-it-py 1, jsonschema-path 1); +2 (cyclopts 2)]: {"op":"sum","args":{"values":"[7,22,9,19,8,4,4,2]"},"result":75} — 75 PACKAGES IN THE RUNTIME CLOSURE (7 seeds + 68 transitive), every edge read at the lock (the extras traced whole: fastmcp-slim's client+server lists, uvicorn's standard six, pydantic[email], pyjwt[crypto], py-key-value-aio's filetree+memory; pydantic-core/typing-inspection/watchfiles's edges point only inward — no new members).
- THE INSTALL'S TOTAL PULL: {"op":"add","args":{"a":"75","b":"1"},"result":76} — prioritree + 75 = 76 packages at a fresh venv. THE MARKER-EXCLUDED NAMED: pywin32 (win32), httpx2-jsfetch (emscripten), beartype at the ≥3.15 markers (beartype rides anyway — py-key-value-aio's unmarked base dep).
- The lock's whole vs the closure: 85 [[package]] blocks (tansa's count; this seat's edge-map agrees) − 75 = {"op":"subtract","args":{"a":"85","b":"75"},"result":10} outside the runtime pull: the root (prioritree) + the dev trio (pytest, pyright, ruff) + their deps (iniconfig, pluggy, nodeenv, colorama — pytest's win32-marked dep) + the two marker-excluded.

## 3. THE VERSION'S NUMBERS — the first release's candidates priced

THE TREE'S OWN SCALE (the record's numbers, tool-carried):
- The floor: 490 at the journey close; since birth's 1 test: {"op":"subtract","args":{"a":"490","b":"1"},"result":489} added across the era.
- The era: born 2026-11-19, the publish convened 2026-11-28: {"op":"subtract","args":{"a":"28","b":"19"},"result":9} days.
- The efforts whole: {"op":"count","args":{"values":"[\"birth\",\"cli\",\"core\",\"budget-curve\",\"service\",\"review\",\"mcp\",\"ux\",\"ci\",\"order-bias-probe\",\"auth\",\"multi-user\",\"polish\",\"journey\",\"publish\"]"},"result":15} stores; the inward era's build efforts: {"op":"count","args":{"values":"[\"auth\",\"order-bias-probe\",\"multi-user\",\"polish\",\"journey\"]"},"result":5}.

THE CANDIDATES:
- 0.1.0 (the field's standing value — pyproject:3 STATIC, the sole source; tansa: no dynamic, no __version__ anywhere): the edit cost to publish = {"op":"subtract","args":{"a":"1","b":"1"},"result":0} — ZERO METADATA DRIFT. The maturity claim HONEST: the development stage, no stability promise — the record backing it whole (five forms complete, floor 490, publicly right; yet ZERO external consumers — README:338's own standing truth, "pip install prioritree do[es] not resolve"; the API never yet exercised against an outside party).
- 1.0.0: the edit cost 1 (the version field); the claim = the stable-API promise — the record's citations for it: 0 consumers, 0 published versions, 0 stability exercises. THE MATURITY'S HONEST NUMBER IS 0.1.0; 1.0.0 would be a promise the record cannot yet cite. (The design gate rules; this seat prices.)

THE VERSION'S DRIFT COST (the source-of-truth question, both forms priced):
- THE STATIC FIELD (today's form): 1 field edit per release; the drift class = the tag↔field divergence (a tag minted at a stale field burns the wrong number at the IMMUTABLE index — permanent); the guard = the release unit's tag-minted-FROM-the-field discipline; the machinery = 0 new pieces.
- THE TAG-DERIVED (dynamic) FORM: the machinery = {"op":"count","args":{"values":"[\"the dynamic declaration\",\"the version plugin in build-requires\",\"the CI tag-fetch\",\"the untagged-build guard\"]"},"result":4} pieces + 1 new build-requires dep; the drift class = the untagged-build refusal (a build without tags fails or versions 0.0.0 — a new failure surface at the CI's shallow checkout, the known fetch-depth class).
- THE PRICE at this tree's cadence (human-paced, the first release unstarted): the static field is the cheaper whole — one source at the bytes (the premise law's cousin), zero machinery; the tag-derived buys automation the cadence does not yet need. The immutability guard rides either way at the release unit.

## 4. THE BENCH-TIME PRICING

THE PUBLISH'S OWN EFFORT — the file-units counted:
- The tree-file units at the CI (trusted-publishing) form: {"op":"count","args":{"values":"[\"pyproject.toml\",\"README.md\",\".github/workflows/publish.yml\"]"},"result":3} — the metadata (pyproject: urls/classifiers minted, the version standing), the install story's flip (README:338's "Not on PyPI" line + the told paths), the channel's workflow. The manual form: {"op":"count","args":{"values":"[\"pyproject.toml\",\"README.md\"]"},"result":2} (the channel rides twine at the collaborator's hands — the token's custody shindan's axis).
- The platform acts (0 tree files): the tag mint, the GitHub release, the PyPI-side configuration, the fresh-venv verification — the units named at the build stage, the design's set to earn.

THE HUMAN HANDS (the collaborator's acts, named at their units): the acts = {"op":"count","args":{"values":"[\"the trusted-publisher configuration\",\"the tag mint\",\"the GitHub release\",\"the trigger read-back\",\"the index read-back\"]"},"result":5}; the minutes priced 3-4 per act: {"op":"multiply","args":{"a":"5","b":"3"},"result":15} to {"op":"multiply","args":{"a":"5","b":"4"},"result":20} — 15-20 min one-time + first-release (the account itself 0 min — exists per the ruling; the CI effort's collaborator-leg precedent the pricing's shape).

THE MACHINE TIME (the CI precedent's recorded numbers; every projection labeled):
- The floor job's non-pytest legs at the precedent (~180s whole, ~26s pytest at the 203-suite): {"op":"subtract","args":{"a":"180","b":"26"},"result":154}
- The pytest projection at the 490-suite (the linear projection at the precedent's 26s/203): {"op":"multiply","args":{"a":"26","b":"490"},"result":12740} then {"op":"divide","args":{"a":"12740","b":"203"},"result":62.758620689655174} s
- The floor job at 490 projected: {"op":"add","args":{"a":"154","b":"62.758620689655174"},"result":216.75862068965517} s = {"op":"divide","args":{"a":"216.75862068965517","b":"60"},"result":3.6126436781609197} min
- The publish steps (build ~15 + upload ~15): {"op":"add","args":{"a":"15","b":"15"},"result":30} s
- THE FLOOR-GATED PUBLISH RUN: {"op":"add","args":{"a":"216.75862068965517","b":"30"},"result":246.75862068965517} s = {"op":"divide","args":{"a":"246.75862068965517","b":"60"},"result":4.11264367816092} min
- THE PUBLISH-ONLY RUN (no floor gate): the sync precedent's bounds (~110s cached / ~165s cold — the CI census's own pricing) + 30: warm {"op":"add","args":{"a":"110","b":"30"},"result":140} = {"op":"divide","args":{"a":"140","b":"60"},"result":2.3333333333333335} min; cold {"op":"add","args":{"a":"165","b":"30"},"result":195} = {"op":"divide","args":{"a":"195","b":"60"},"result":3.25} min.

THE VERIFICATION'S COST: the cold install (pip install prioritree at a fresh venv) — the 76-package pull within the CI precedent's cold-sync envelope (~165s at the runner's whole dev set; the runtime-only pull lighter), minutes-scale, $0; the index read (the published page read cold, the author verified at the index per the account ruling) — seconds, $0.

## 5. THE TOTAL — the publish's whole at the $0 bar

- THE MONEY: $0 verified — {"op":"sum","args":{"values":"[0,0,0,0,0]"},"result":0} (hosting, upload, bandwidth, CI minutes, tooling); NO PAID TIER found anywhere in the channel; any cost found refused at the law's bar.
- THE BENCH TIME: the publish run 2.3-4.1 min machine (the bounds above, projections at the CI precedent), the cold-install verification minutes-scale, the index read seconds — all at the free runner / the local machine, $0.
- THE HUMAN HANDS: 15-20 min one-time + first-release (5 acts), the account already settled at 0 min.
- THE FIRST-RELEASE NUMBER'S PRICE STANDING: 0.1.0 at ZERO drift cost (the field's standing value, zero edits, the maturity's honest number — 489 tests added over a 9-day, 15-store, five-effort era, yet 0 external consumers); 1.0.0 priced at 1 edit + a promise the record cannot yet cite.

PROVENANCE (the reads, all this turn, read-only): the store's heart (.junro/junro.json, 318 lines) — both rulings carried; pyproject.toml (263) whole; uv.lock (1,938) — the 85 package blocks' edges read at the bytes (the seven seeds' chains traced to their leaves); CONTINUATION.md (173) whole — the era's numbers; the parallel legs' landed reports (tansa's census, shindan's risk diagnosis — the packets.jsonl + the projected reports/research/*.md); the CI effort's pricing precedent (reports/census/pricing.md per the synthesis's citations: ~11 min/push, ~110s/~165s, 26s/203, ~3 min floor); dist/ (the directory: the two built artifacts + .gitignore). THE TWO HONEST LIMITS: the .whl's bytes (the binary read refused — quoted verbatim above) and PyPI's caps' exact source numbers (rikai's lane). No file touched; no store record written but this report.
