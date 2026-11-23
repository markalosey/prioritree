<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — census/actions-free-forms

**Route:** prioritree-ci (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-23T23:02:03Z |
| 2 | report | tansa | 2026-11-23T23:05:05Z |
## Reported by tansa — 2026-11-23T23:05:05Z

THE GITHUB ACTIONS FREE-FORMS INVENTORY (census/actions-free-forms, tansa seat)

1. THE FREE RUNNER. Standard GitHub-hosted runners (ubuntu-latest's class) are FREE in public
repositories — free independently, never drawing from included compute; larger runners are
billed even in public repos. Private repos: usage draws from monthly included compute —
GitHub Free $12/month (at $0.006/min for the 2-core Linux runner ≈ 2,000 minutes); usage
beyond blocks without a payment method. Free plan concurrency cap: 20 standard-runner jobs.

2. THE WORKFLOW GRAMMAR. YAML at .github/workflows/*.yml|.yaml: name, run-name, on (single,
array like [push], or filtered: on.push.branches, on.pull_request.branches), jobs.<id>
carrying runs-on and steps; each step is uses: owner/action@ref (+with:) or run: shell text
(multi-line via run: |). Docs' floor example (quickstart): name, run-name, on: [push], one
job on runs-on: ubuntu-latest, echo steps, uses: actions/checkout@v6, run: | ls ${{ github.workspace }}.
Default non-Windows shell: bash -e {0}.

3. THE WORKFLOW-NATIVE UV. uses: astral-sh/setup-uv@v10.3.3 (README's pinned form). version
input "" defaults to the required-version in uv.toml/pyproject.toml, else latest. python-version
sets UV_PYTHON, overriding pyproject.toml and .python-version specs. enable-cache: auto|true|false
(auto = on for GitHub-hosted runners); cache-dependency-glob defaults include **/pyproject.toml
and **/uv.lock. working-directory locates pyproject.toml/uv.toml/.python-version. Checkout
must run BEFORE setup-uv. Docs' test step: run: uv run --frozen pytest.

4. THE CODEQL FREE FORM. Code scanning is free of charge on all public repositories; private
repos need a Code Security license. Default setup = UI-enrolled, no workflow file; advanced
setup = editable workflow (default .github/workflows/codeql-analysis.yml). Docs' current refs:
github/codeql-action/init@v4 / analyze@v4 (v3 = prior major). Python is interpreted:
build-mode: none (buildless, no autobuild needed for pure Python; matrix include:
- language: python / build-mode: none). Config file: init's config-file:
./.github/codeql/codeql-config.yml, with paths / paths-ignore arrays. Trigger form:
on: push: branches: [main], pull_request: branches: [main], schedule cron.

5. THE MAKE TARGETS' RIDABILITY. Yes: make 4.3 ships in the ubuntu runner image's apt packages
(Ubuntu2404-Readme), so run: make test is a legal run step (≤21,000 chars, default shell).
Steps execute in the checkout workspace (github.workspace) by default; working-directory
relocates per step/job/workflow if the Makefile lives deeper. Runner-image announcements
also note ubuntu-latest moves to 26.04 in November 2026 (label mid-transition).

SOURCES. docs.github.com: about-billing-for-github-actions; actions/reference/limits;
actions/get-started/quickstart; understanding-github-actions; workflow-syntax-for-github-actions;
code-scanning configuring-default-setup + customizing-advanced-setup + about-code-scanning;
about-billing-for-github-advanced-security. github.com: astral-sh/setup-uv README;
actions/runner-images Ubuntu2404-Readme.
