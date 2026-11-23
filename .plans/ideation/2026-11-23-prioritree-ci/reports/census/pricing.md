<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/pricing

**Route:** prioritree-ci (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T23:02:49Z |
| 2 | report | keisan | 2026-11-23T23:06:01Z |
## Reported by keisan — 2026-11-23T23:06:01Z

# THE PRICING CENSUS — the free tier's numbers against the tree's floor (keisan, 2026-11-23)

## THE FLOOR'S RUNTIME PRICE (per run)
- THE FLOOR: 203 passed in 26.32s (reports/validate/lifecycleintegration.md:20; 25.99s at the build leg) + ruff ~8s + pyright ~10s = 44.32s ≈ ~45s (calculate: 26.32+8+10).
- THE SYNC: uv.lock carries 88 packages (grep-counted) − prioritree itself − pywin32 (Windows-only, skipped on linux) ≈ 86 wheels; the compiled tail (pydantic-core, uvloop, watchfiles, httptools, tiktoken, rpds-py, cryptography) all manylinux wheels — zero builds at install. COLD ~45-60s at the runner; with setup-uv's cache ~10-20s. Pyright's first-run node download adds ~10-20s cold.
- THE JOB WHOLE (cold): checkout ~30s + uv setup ~30s + sync ~60s + floor ~45s = 165s = 2.75 min ≈ ~3 min/push; the cached form ~110s ≈ ~1.8 min.

## THE CODEQL PRICE
- The surface: 15 src modules (~6k lines — the composition's sizing; the grep's 100-match cap blown within the first files, consistent) + 18 test files extracted by default too.
- The scan: init (bundle download 1-2 min cold, ~30s warm) + extract ~1-2 min + analyze at the default security suite ~3-6 min → ~5-10 min/scan; the nominal ~8 min.
- The coverage: PUBLIC repos scan FREE — the default setup already live (FR-MEM-0033: the alert fired at $0); the advanced setup free at the public form too.

## THE FREE-TIER HEADROOM
- THE TERMS: public repos = UNLIMITED free standard-runner minutes (ubuntu-latest $0); the private contrast = 2,000 min/mo.
- PER PUSH: floor ~2.75 + CodeQL ~8 = 10.75 ≈ ~11 min.
- THE RATE (the reflog, .git/logs/HEAD): 112 commits over 367,489s = 4.25 days ≈ 26 commits/day; the last 48h carry 85 commits ≈ 42/day; at the observed land cadence (~2-3 commits/push) ≈ ~30 pushes in two days — the burst rate confirmed; the steady state ~10-30 pushes/mo.
- THE MONTHLY: steady 110-330 min/mo (10-30 × 11); the sustained-burst ceiling 450 pushes/mo × 11 = 4,950 min/mo.
- THE VERDICT: the public form is UNLIMITED — the free tier suffices at ANY multiple (∞×; even the burst ceiling bills $0). The private contrast would hold steady state at 6.1-18.2× (2,000/330-2,000/110) and break only at a month-long sustained burst (4,950 ≈ 2.5× over) — moot: the repo rides the public form.

## THE CONSERVATION FORMS' SAVINGS
- CANCEL-IN-PROGRESS at the burst: the uncancelled burst bill = 30 pushes × 11 = 330 min/two days; the reflog's clustered lands (pushes minutes apart) supersede live runs — ~30-50% saved: ~99-165 min per two-day burst (a cancelled run bills only its elapsed fraction; a mid-run cancel saves ~4-6 of an 11-min run).
- BRANCH FILTER (main-only): the reflog is 100% main — one linear history, no feature branch ever — so the filter costs ZERO coverage today; the form's value is held for the future: ~3 min (floor-only) to ~11 min (with CodeQL) avoided per feature-branch push, and ~1 duplicate floor run (~3 min) per PR update avoided against the every-branch + PR double-billing.

THE LAW HELD (R1, priced not assumed): nothing in this arithmetic bills — the floor ~3 min, the scan ~8 min, the steady month 110-330, the burst ceiling ~4,950 — every surface $0 at the public form.
