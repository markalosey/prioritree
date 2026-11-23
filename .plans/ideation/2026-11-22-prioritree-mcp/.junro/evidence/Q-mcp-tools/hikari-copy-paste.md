# THE HIKARI COPY-PASTE — the connection config as prioritree authors it (Q-mcp-tools ruling 6's deliverable)

## THE BLOCK WHOLE (R6's deliverable — the paste-able bytes; the ruled data whole, the resolution points named where this tree cannot resolve them)

### [A] THE MCP FRAGMENT — the yaml rows (hikari's prioritree-seats.yaml; the DATA the rows must express — the yaml's exact schema OUT OF TREE, named honestly) + the emitted JSON form (this tree's opencode.json mcp block; the context7/tavily disable-rows carried — the block's standing rows, opencode.json:514-521; prioritree the tree's FIRST ENABLED server, F6):

```yaml
mcp:
  prioritree:
    command: "uv"
    args: ["run", "python", "-m", "prioritree.mcp_server"]
    enabled: true
```

```json
"mcp": {
  "prioritree": {
    "command": "uv",
    "args": ["run", "python", "-m", "prioritree.mcp_server"],
    "enabled": true
  },
  "context7": {
    "enabled": false
  },
  "tavily": {
    "enabled": false
  }
}
```

### [B] THE PER-SEAT PERMISSION ROWS (the grant map — mcp-design.md §4's final form; the five verbs, F4's ruled names: runs.register, runs.next, votes.cast, votes.census, runs.tally)

THE NAMING UNCERTAINTY, NAMED (L6): the wired tools ride into the permission map as {server}_{tool} — the standing precedent's tool part is SEPARATOR-FREE (sequential-thinking_sequentialthinking, opencode.json:112/:500); the ruled tool names carry DOTS (runs.register) — so the key spelling is TWO candidates: prioritree_runs.register (the ruled name carried verbatim) vs prioritree_runs_register (the harness normalizing the dot). Unverifiable pre-restart from this tree (the LOCAL form's command/args keys have no standing entry — the mcp block carries disable-rows only). THE KEY SPELLING RESOLVES AT THE HIKARI HAND — the schema/key check against the harness's permission-key grammar, BEFORE the regen; THE FIVE VERBS + THE GRANT MAP ARE THE DATA (spelling-agnostic); the rows below carry the dotted candidate, the alternative named.

FULL-FIVE (all five "allow") — jikko, kensho, shinko (the working seats):
```
"prioritree_runs.register": "allow"
"prioritree_runs.next": "allow"
"prioritree_votes.cast": "allow"
"prioritree_votes.census": "allow"
"prioritree_runs.tally": "allow"
```

READ-THREE (next/census/tally "allow"; register/cast "deny") — rikai, shindan (the analysis seats):
```
"prioritree_runs.register": "deny"
"prioritree_runs.next": "allow"
"prioritree_votes.cast": "deny"
"prioritree_votes.census": "allow"
"prioritree_runs.tally": "allow"
```

DENY-EIGHT (all five "deny") — keikaku, tansa, suisen, keisan, hyoka, moho, togo, hansei:
```
"prioritree_runs.register": "deny"
"prioritree_runs.next": "deny"
"prioritree_votes.cast": "deny"
"prioritree_votes.census": "deny"
"prioritree_runs.tally": "deny"
```

### [C] THE PACK ROUTING ROWS (the 13 prompts' tables; the ops alphabetical — the standing table form):
```
jikko, kensho, shinko:   | prioritree | cast, census, next, register, tally |
rikai, shindan:           | prioritree | census, next, tally |
```
ABSENT at the other eight (keikaku, tansa, suisen, keisan, hyoka, moho, togo, hansei) — the row never emitted at a deny seat.

### [D] THE DELIVERY NOTE (F7's sequence whole):
THE HIKARI EDIT (prioritree-seats.yaml: the [A] mcp rows + the [B] per-seat permission rows + the [C] Pack Routing rows — the key spelling resolved at the hand, FIRST) → THE REGEN (uv run python scripts/generation/clarity_scaffold.py --target prioritree, at the hikari tree) → THE EMISSION (this tree's opencode.json + the 13 seat prompts + AGENTS.md regenerate — never hand-edited, "do not edit manually") → THE RESTART (FR-MEM-0014: the config read at launch — a live session never sees the grant; the restart note rides the member-path unit's report verbatim).
