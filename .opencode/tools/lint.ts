// prioritree-owned (2026-11-19, G-TOOL-GRANTS-BRIEF): composed from hikari's current render, re-pointed at prioritree's host Makefile via the _run.ts channel; hand-maintained in prioritree's tree
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
  description: "Code quality — linting and type checking at prioritree, whole-tree via the host Makefile: check (make lint — ruff over src/ and tests/) and typecheck (make typecheck — pyright over the tree's [tool.pyright] include set). Host-only (no Docker, no worktrees); the explicit-argv runArgv channel, no shell.",
  args: {
    operation: tool.schema
      .enum(["check", "typecheck"])
      .or(tool.schema.literal("help"))
      .describe("Operation to perform (use \"help\" to print this tool's usage)"),
  },
  async execute(args, context) {
    switch (args.operation) {
      case "check": {
        return formatOutput(await runArgv(["make", "lint"], { cwd: context.directory }))
      }
      case "typecheck": {
        return formatOutput(await runArgv(["make", "typecheck"], { cwd: context.directory }))
      }
      case "help": {
        return "lint — Code quality — whole-tree via the host Makefile.\n\nOperations:\n  check  [make lint]\n    Run ruff over src/ and tests/\n  typecheck  [make typecheck]\n    Run pyright over the tree's [tool.pyright] include set"
      }
    }
    return `Unknown operation: ${args.operation}`
  },
})
