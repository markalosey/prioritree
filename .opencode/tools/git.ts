// prioritree-owned (2026-11-19, G-TOOL-GRANTS-BRIEF): composed from hikari's current render, the cross-project junro.ts form (engine stays home at hikari); hand-maintained in prioritree's tree
import { tool } from "@opencode-ai/plugin"
import { runArgv } from "./_run"

function formatOutput(result: {
  exitCode: number
  text(): string
  stderr: Buffer | string
}): string {
  const stdout = result.text()
  const stderr = result.stderr.toString()
  if (result.exitCode === 0) {
    return stdout.trim() || "Done."
  }
  if (stderr.trim()) {
    return `${stdout}${stdout.trim() ? "\n" : ""}stderr:\n${stderr}`.trim()
  }
  return stdout.trim() || `Exited with code ${result.exitCode} (no output captured).`
}

export default tool({
  description: "Machinery-class git instrument at prioritree (packet CF-5's engine behind the G-TOOL-GRANTS-BRIEF worktree-less ruling, 2026-11-19) — the cross-project wrapper form (the junro.ts precedent): the ENGINE stays home at hikari, this wrapper forwards argv only, and cwd stays the invoking session's tree (the invoking-tree seat resolution serves exactly). Prioritree's tree is WORKTREE-LESS: the seats derive subject==main; the never-edit-main law's LETTER cannot carry here, and its SPIRIT carries whole (per-leg exit codes — a failed leg marks the op FAILED with prior legs' state reported, the choreography never marches on, R-9; sync/land success reported ONLY from tracked-ref comparison). The ruled per-op accounting: sync = push + tracked-ref verify; drift = read-only comparison (exit 0 may carry per-branch error fields — read them); land = the single-tree landing — add-all + trailer-commit + push, the hook firing on every landing; discard = main-seat named-paths restore, the named-paths-only law scoping it; move = works as-is. unshroud NOT carried (inert — no skip-worktree bits exist at prioritree). The upstream precondition stands: prioritree's checked-out branch needs origin tracking (a remote-config fact at the collaborator's hand). Exit codes forwarded verbatim: 0 ok (JSON envelope on stdout) / 1 refused-or-failed (envelope + stderr; refused = no legs ran, failed = state may have mutated — read status + failed_leg, never collapse to the exit code) / 2 argparse (stderr only, NO envelope — an incomplete land reaches this shape). anti_scenario: NOT a general git wrapper — the closed set is the five ruled ops (discard paths are whitespace-split in one --paths value; stash/reset/cherry-pick/git rm are ruled candidates, not ops); the --project arg forwards verbatim (dead but correct at a worktree-less tree — the engine REFUSES loudly on the missing worktree, never a silent fallback); --timeout stays CLI-only; no fetch, ever (Q7).",
  args: {
    operation: tool.schema
      .enum(["sync","drift","land","discard","move"])
      .or(tool.schema.literal("help"))
      .describe("Operation to perform (use \"help\" to print this tool's usage)"),
    project: tool.schema.string().optional()
      .describe("Plan worktree slug under .worktrees/ (CF-6) — when set, the ENGINE derives both seats from that worktree (resolved against the main clone root; a named-but-missing worktree refuses loudly); omit to derive the seats from the invoking session's tree (unchanged behavior)"),
    message: tool.schema.string().optional()
      .describe("the commit subject+body (the first -m block)"),
    subtask: tool.schema.string().optional()
      .describe("the Subtask: trailer value"),
    agent: tool.schema.string().optional()
      .describe("the Agent: trailer value"),
    verified_by: tool.schema.string().optional()
      .describe("the Verified-by: trailer value (CF-5d ruling 2: the TS-identifier-safe alias — the engine accepts both spellings)"),
    sparse_stage: tool.schema.string().optional()
      .describe("the named-paths --sparse stage (A-2, build/cure-a — the read-back sensor's refuse-then-remedy form; whitespace-separated in one value; working-present paths only: an absent path refuses, naming unshroud)"),
    paths: tool.schema.string().optional()
      .describe("the named paths to restore, whitespace-separated in ONE value (an empty value refuses — RULING Q5)"),
    source: tool.schema.string().optional()
      .describe("the source path (CF-5d ruling 1 — the flag form)"),
    destination: tool.schema.string().optional()
      .describe("the destination path (CF-5d ruling 1 — the flag form)"),
  },
  async execute(args, context) {

    switch (args.operation) {
      case "sync": {
        const eargs = ["sync"]
        if (args.project !== undefined) eargs.push(`--project=${args.project}`)
        return formatOutput(await runArgv(["uv", "run", "--project", "/Users/marklosey/projects/kepric/hikari", "python", "/Users/marklosey/projects/kepric/hikari/scripts/git_tool.py", ...eargs], { cwd: context.directory }))
      }
      case "drift": {
        const eargs = ["drift"]
        if (args.project !== undefined) eargs.push(`--project=${args.project}`)
        return formatOutput(await runArgv(["uv", "run", "--project", "/Users/marklosey/projects/kepric/hikari", "python", "/Users/marklosey/projects/kepric/hikari/scripts/git_tool.py", ...eargs], { cwd: context.directory }))
      }
      case "land": {
        const eargs = ["land"]
        if (args.message !== undefined) eargs.push(`--message=${args.message}`)
        if (args.subtask !== undefined) eargs.push(`--subtask=${args.subtask}`)
        if (args.agent !== undefined) eargs.push(`--agent=${args.agent}`)
        if (args.verified_by !== undefined) eargs.push(`--verified_by=${args.verified_by}`)
        if (args.sparse_stage !== undefined) eargs.push(`--sparse_stage=${args.sparse_stage}`)
        if (args.project !== undefined) eargs.push(`--project=${args.project}`)
        return formatOutput(await runArgv(["uv", "run", "--project", "/Users/marklosey/projects/kepric/hikari", "python", "/Users/marklosey/projects/kepric/hikari/scripts/git_tool.py", ...eargs], { cwd: context.directory }))
      }
      case "discard": {
        const eargs = ["discard"]
        if (args.paths !== undefined) eargs.push(`--paths=${args.paths}`)
        if (args.project !== undefined) eargs.push(`--project=${args.project}`)
        return formatOutput(await runArgv(["uv", "run", "--project", "/Users/marklosey/projects/kepric/hikari", "python", "/Users/marklosey/projects/kepric/hikari/scripts/git_tool.py", ...eargs], { cwd: context.directory }))
      }
      case "move": {
        const eargs = ["move"]
        if (args.source !== undefined) eargs.push(`--source=${args.source}`)
        if (args.destination !== undefined) eargs.push(`--destination=${args.destination}`)
        if (args.project !== undefined) eargs.push(`--project=${args.project}`)
        return formatOutput(await runArgv(["uv", "run", "--project", "/Users/marklosey/projects/kepric/hikari", "python", "/Users/marklosey/projects/kepric/hikari/scripts/git_tool.py", ...eargs], { cwd: context.directory }))
      }
      case "help": {
        return "git — Machinery-class git instrument at prioritree (packet CF-5's engine behind the G-TOOL-GRANTS-BRIEF worktree-less ruling, 2026-11-19) — the cross-project wrapper form (the junro.ts precedent): the ENGINE stays home at hikari, this wrapper forwards argv only, and cwd stays the invoking session's tree (the invoking-tree seat resolution serves exactly). Prioritree's tree is WORKTREE-LESS: the seats derive subject==main; the never-edit-main law's LETTER cannot carry here, and its SPIRIT carries whole (per-leg exit codes — a failed leg marks the op FAILED with prior legs' state reported, the choreography never marches on, R-9; sync/land success reported ONLY from tracked-ref comparison). The ruled per-op accounting: sync = push + tracked-ref verify; drift = read-only comparison (exit 0 may carry per-branch error fields — read them); land = the single-tree landing — add-all + trailer-commit + push, the hook firing on every landing; discard = main-seat named-paths restore, the named-paths-only law scoping it; move = works as-is. unshroud NOT carried (inert — no skip-worktree bits exist at prioritree). The upstream precondition stands: prioritree's checked-out branch needs origin tracking (a remote-config fact at the collaborator's hand). Exit codes forwarded verbatim: 0 ok (JSON envelope on stdout) / 1 refused-or-failed (envelope + stderr; refused = no legs ran, failed = state may have mutated — read status + failed_leg, never collapse to the exit code) / 2 argparse (stderr only, NO envelope — an incomplete land reaches this shape). anti_scenario: NOT a general git wrapper — the closed set is the five ruled ops (discard paths are whitespace-split in one --paths value; stash/reset/cherry-pick/git rm are ruled candidates, not ops); the --project arg forwards verbatim (dead but correct at a worktree-less tree — the engine REFUSES loudly on the missing worktree, never a silent fallback); --timeout stays CLI-only; no fetch, ever (Q7).\n\nOperations:\n  sync  [uv run python /Users/marklosey/projects/kepric/hikari/scripts/git_tool.py sync]\n    push + tracked-ref verify (the ruled worktree-less accounting: the seats derive subject==main; per-leg exit codes as data; success ONLY from tracked-ref comparison; a failed leg marks the op FAILED with prior legs' state — never marches on, R-9)\n      - project [optional]: Plan worktree slug under .worktrees/ (CF-6) — when set, the ENGINE derives both seats from that worktree (resolved against the main clone root; a named-but-missing worktree refuses loudly); omit to derive the seats from the invoking session's tree (unchanged behavior)\n    example: operation=\"sync\"\n  drift  [uv run python /Users/marklosey/projects/kepric/hikari/scripts/git_tool.py drift]\n    read-only comparison (the ruled accounting; ls-remote --exit-code + rev-list counts + reflog last-push; no fetch, no local ref mutation — Q7); exit 0 may carry per-branch error fields — read them (rider 4)\n      - project [optional]: Plan worktree slug under .worktrees/ (CF-6) — when set, the ENGINE derives both seats from that worktree (resolved against the main clone root; a named-but-missing worktree refuses loudly); omit to derive the seats from the invoking session's tree (unchanged behavior)\n    example: operation=\"drift\"\n  land  [uv run python /Users/marklosey/projects/kepric/hikari/scripts/git_tool.py land]\n    the single-tree landing (the ruled accounting: add-all + trailer-commit + push, the hook firing on every landing — the commit leg runs the repo hooks, a hook's non-zero exit IS the leg's failure)\n      - message [required]: the commit subject+body (the first -m block)\n      - subtask [required]: the Subtask: trailer value\n      - agent [required]: the Agent: trailer value\n      - verified_by [optional]: the Verified-by: trailer value (CF-5d ruling 2: the TS-identifier-safe alias — the engine accepts both spellings)\n      - sparse_stage [optional]: the named-paths --sparse stage (A-2, build/cure-a — the read-back sensor's refuse-then-remedy form; whitespace-separated in one value; working-present paths only: an absent path refuses, naming unshroud)\n      - project [optional]: Plan worktree slug under .worktrees/ (CF-6) — when set, the ENGINE derives both seats from that worktree (resolved against the main clone root; a named-but-missing worktree refuses loudly); omit to derive the seats from the invoking session's tree (unchanged behavior)\n    example: operation=\"land\", message=\"<value>\", subtask=\"<value>\", agent=\"<value>\"\n  discard  [uv run python /Users/marklosey/projects/kepric/hikari/scripts/git_tool.py discard]\n    main-seat named-paths restore (the ruled accounting; the named-paths-only law scoping it — explicit paths, no unnamed-scope restores, RULING Q5; per-path diff-index verification; --paths carries whitespace-separated paths in one value, CF-5d ruling 1)\n      - paths [required]: the named paths to restore, whitespace-separated in ONE value (an empty value refuses — RULING Q5)\n      - project [optional]: Plan worktree slug under .worktrees/ (CF-6) — when set, the ENGINE derives both seats from that worktree (resolved against the main clone root; a named-but-missing worktree refuses loudly); omit to derive the seats from the invoking session's tree (unchanged behavior)\n    example: operation=\"discard\", paths=\"<value>\"\n  move  [uv run python /Users/marklosey/projects/kepric/hikari/scripts/git_tool.py move]\n    works as-is (the ruled accounting): git mv for record-class file migrations — the staged rename is verified from the index (strict R* source/destination pair; CF-3b's migration)\n      - source [required]: the source path (CF-5d ruling 1 — the flag form)\n      - destination [required]: the destination path (CF-5d ruling 1 — the flag form)\n      - project [optional]: Plan worktree slug under .worktrees/ (CF-6) — when set, the ENGINE derives both seats from that worktree (resolved against the main clone root; a named-but-missing worktree refuses loudly); omit to derive the seats from the invoking session's tree (unchanged behavior)\n    example: operation=\"move\", source=\"<value>\", destination=\"<value>\""
      }
    }
    return `Unknown operation: ${args.operation}`
  },
})
