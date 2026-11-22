<!-- regen: uv run python scripts/generation/kumi_views.py -->
# Packet Report — design/adversarial-web

**Route:** prioritree-ux (executing) | **Events:** 2 | **Reports:** 1

## The packet's chain (ledger order)

| # | Op | Actor | Timestamp |
|---|---|---|---|
| 1 | dispatch | shinko | 2026-11-22T17:15:05Z |
| 2 | report | hyoka | 2026-11-22T17:21:12Z |
## Reported by hyoka — 2026-11-22T17:21:12Z

# design/adversarial-web — hyoka's adversarial pass: the re-settled web architecture + re-spec v2 (does it meet the bar?)

READ-BACK: reports/synthesize/webspec.md (whole, 3601 l. — v2's five events + v1's six) · the ux store's junro.json (R9/R10 verbatim; G-WEB/G-WEB-BRIEF/G-WEBSPEC-BRIEF conditions; R7/R8) · reports/synthesize/web.md (the approved brief, whole) · reports/discover/web.md + reports/understand/web.md · THE TREE: src/prioritree/service.py (528 l.), tests/test_service_face.py + test_service_acceptance.py, pyproject.toml, Makefile, scripts/generation/ (both zombies present), the core's ack semantics at source (votes.py:464-468, run_store.py:782, cli.py:260).

VERDICT: the re-settled ARCHITECTURE meets R9/R10 — the RE-SPEC does not meet the bar as written: one blocking defect plus letter-level cures, folded before the gates present.

BLOCKING 1 — THE IDEMPOTENT-ECHO INVERSION. The core: a fresh cast returns acknowledged=False; the byte-identical re-send returns acknowledged=True (votes.py:467-468 "UNCHANGED count, acknowledged=True (never a silent dup)"; cli.py:260 MARKER_ACK rides True). §E's vote-ack.html renders the echo `{% if not acknowledged %}` — INVERTED: every FRESH vote tells the comparator "already recorded with the same answer" (a lie per cast); the true re-send renders nothing. §V's echo test masks it twice: its first post targets `/runs/{_RUN_ID}/vote` — no such route exists (the fragment is /ui/.../vote; the service lane is /votes) — the vote never lands; the "again" post is a fresh cast whose inverted echo satisfies the assertion. CURE: flip §E to `{% if acknowledged %}`; flip §Q's vote docstring ("acknowledged:true => the echo"); the test posts BOTH through the fragment path, asserts the echo on the second alone, and the chain arc pins its absence on the fresh ack; the brief §4 route-8's "acknowledged:false → the echo" letter named as the inversion's carrier, amendment-pending at the gate.

HIGH 2 — G-WEB CONDITION 2 AS COMPOSED CANNOT GO GREEN. "zero hand-authored frontend artifacts on disk (out of grammar)" against v2's 16 authored files; the re-spec §4 defers the reading to "the build gate" — G-WEB is deterministic-check, no ruling seat there. CURE: the collaborator RECORDS the R9/R10 reading at the re-presented brief gates (G-WEB-BRIEF/G-WEBSPEC-BRIEF, collaborator-ruling) as the amendment carrying condition 2's re-composed letter — folded into §4, never deferred to a gate with no ruling seat.

HIGH 3 — §Y(3)'s "web.py carries zero human-facing words" IS FALSE at §Q's own bytes: the bad-quorum refusal's three fields (§Q:3047-3049) and the handlers' found-texts are human words in Python. CURE: name the exception class (the family-grammar field VALUES — service.py's own precedent, v1 §0 ruling 5's form) in §Y(3), or move the quorum copy to the file tier.

MEDIUM 4 — THE AMENDED-CLAUSE LIST'S STALE LETTERS: §3e "stands" but its letter rides "as data in the structure" (the structure is removed); §8 item 5 "stands" but its letter names "the Makefile's bytes (web-check, .PHONY, the lint argv)" + "pyright's include" (v2: Makefile untouched, include untouched). CURE: amend those letters in §3's re-presentation so the brief reads paper-coherent.

MEDIUM 5 — THE MOUNT SHADOW'S FALSE FOUND AT SERVICE PATHS: DELETE /runs now answers the child's 404 "no route matches the path /runs" — factually false (POST /runs matches); the brief priced the 405→404 status change (§3e.2) but never the lying found; no arc pins it (the one 405 arc re-targeted away). CURE: name the residue in §Y (the whole's 404 grammar is honest only for paths no route of the whole matches).

MEDIUM 6 — check_dir=False's SILENT-404 IS UNPINNED: no §V arc GETs /static/app.css|app.js — a mis-named static home serves unstyled pages with zero test failures (the templates' home IS pinned by every page arc). CURE: one face arc pinning the static pair's 200 + a byte.

LOW 7 — THE SCRATCH-CWD PAGE RESIDUE UNNAMED: §Y(1)'s harness proof holds — verified at the mechanism (check_dir=False at §Q's mount + Jinja2Templates' lazy loader + the arcs ride parent JSON routes; no acceptance arc breaks; the boot survives); but a page request at a scratch cwd answers the PARENT's JSON 500 (TemplateNotFound escapes the child's fold — the fold renders through the same broken loader — then the parent's fold; family grammar held, page tier dead). tansa §5's "the mounted tier's pages serve over the same socket" is false at a scratch cwd. CURE: one line in §Y(1) naming the residue; fix step 7's confused note (under check_dir=False the import needs no directory — "load-bearing" overstates).

VERIFIED SOUND (the rest): R9/R10's three beats held (§A-§P authored files; the loader at §Q; render-time generation; zero template strings in web.py; the CDN pins in base.html); the three v1 cures verified at the bytes (check_dir=False; rows-as-dict at §Q matching §K's rows[item] subscript; no web_structure import — the union composed from the module's own constants); the pinned 404 arc holds unedited (the union carries "POST /runs"); the fragment tier's manual form parsing (no framework 422); the two-step chain + HX-Redirect; the 12-step order holds (removal first — the zombies unreferenced at HEAD; pyproject→uv sync→files→web.py→mount→tests→405→floor), no step depends on a later step, none over-fat for R8's one-dispatch form.

THE BAR'S ANSWER: NOT as written — fold the echo inversion (blocking) + findings 2-4 (governance/letters) into the spec before the gates present; 5-7 are cheap one-liners riding the same fold. The architecture itself stands. — hyoka, 2026-11-22
