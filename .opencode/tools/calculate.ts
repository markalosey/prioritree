// prioritree-owned (2026-11-19, G-HARNESS-BRIEF): composed from hikari's current render + tane's channel; hand-maintained in prioritree's tree
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
  description: "Pure-query arithmetic and counting — six ops (add, subtract, multiply, divide, sum, count), each a deterministic read that returns a number. Stateless, actorless, refuse-nothing: no store, no provenance stamp, no session — the same inputs always return the same number (Q-CALC-1, the calculate composition, 2026-09-28). anti_scenario: NOT a calculator for prose, NOT a mutation surface, NOT a substitute for kensho's verification — arithmetic and counting only.",
  args: {
    operation: tool.schema
      .enum(["add","subtract","multiply","divide","sum","count"])
      .or(tool.schema.literal("help"))
      .describe("Operation to perform (use \"help\" to print this tool's usage)"),
    a: tool.schema.string().optional()
      .describe("the first operand (a number)"),
    b: tool.schema.string().optional()
      .describe("the second operand (a number)"),
    values: tool.schema.string().optional()
      .describe("a JSON array of numbers to total"),
  },
  async execute(args, context) {

    switch (args.operation) {
      case "add": {
        const eargs = ["add"]
        if (args.a !== undefined) eargs.push(`--a=${args.a}`)
        if (args.b !== undefined) eargs.push(`--b=${args.b}`)
        return formatOutput(await runArgv(["uv", "run", "python", ".opencode/scripts/calculate.py", ...eargs], { cwd: context.directory }))
      }
      case "subtract": {
        const eargs = ["subtract"]
        if (args.a !== undefined) eargs.push(`--a=${args.a}`)
        if (args.b !== undefined) eargs.push(`--b=${args.b}`)
        return formatOutput(await runArgv(["uv", "run", "python", ".opencode/scripts/calculate.py", ...eargs], { cwd: context.directory }))
      }
      case "multiply": {
        const eargs = ["multiply"]
        if (args.a !== undefined) eargs.push(`--a=${args.a}`)
        if (args.b !== undefined) eargs.push(`--b=${args.b}`)
        return formatOutput(await runArgv(["uv", "run", "python", ".opencode/scripts/calculate.py", ...eargs], { cwd: context.directory }))
      }
      case "divide": {
        const eargs = ["divide"]
        if (args.a !== undefined) eargs.push(`--a=${args.a}`)
        if (args.b !== undefined) eargs.push(`--b=${args.b}`)
        return formatOutput(await runArgv(["uv", "run", "python", ".opencode/scripts/calculate.py", ...eargs], { cwd: context.directory }))
      }
      case "sum": {
        const eargs = ["sum"]
        if (args.values !== undefined) eargs.push(`--values=${args.values}`)
        return formatOutput(await runArgv(["uv", "run", "python", ".opencode/scripts/calculate.py", ...eargs], { cwd: context.directory }))
      }
      case "count": {
        const eargs = ["count"]
        if (args.values !== undefined) eargs.push(`--values=${args.values}`)
        return formatOutput(await runArgv(["uv", "run", "python", ".opencode/scripts/calculate.py", ...eargs], { cwd: context.directory }))
      }
      case "help": {
        return "calculate — Pure-query arithmetic and counting — six ops (add, subtract, multiply, divide, sum, count), each a deterministic read that returns a number. Stateless, actorless, refuse-nothing: no store, no provenance stamp, no session — the same inputs always return the same number (Q-CALC-1, the calculate composition, 2026-09-28). anti_scenario: NOT a calculator for prose, NOT a mutation surface, NOT a substitute for kensho's verification — arithmetic and counting only.\n\nOperations:\n  add  [uv run python .opencode/scripts/calculate.py add]\n    a + b — the sum of two numbers (deterministic)\n      - a [required]: the first operand (a number)\n      - b [required]: the second operand (a number)\n    example: operation=\"add\", a=\"<value>\", b=\"<value>\"\n  subtract  [uv run python .opencode/scripts/calculate.py subtract]\n    a - b — the difference of two numbers (deterministic)\n      - a [required]: the first operand (a number)\n      - b [required]: the second operand (a number)\n    example: operation=\"subtract\", a=\"<value>\", b=\"<value>\"\n  multiply  [uv run python .opencode/scripts/calculate.py multiply]\n    a * b — the product of two numbers (deterministic)\n      - a [required]: the first operand (a number)\n      - b [required]: the second operand (a number)\n    example: operation=\"multiply\", a=\"<value>\", b=\"<value>\"\n  divide  [uv run python .opencode/scripts/calculate.py divide]\n    a / b — the quotient of two numbers (deterministic)\n      - a [required]: the first operand (a number)\n      - b [required]: the second operand (a number)\n    example: operation=\"divide\", a=\"<value>\", b=\"<value>\"\n  sum  [uv run python .opencode/scripts/calculate.py sum]\n    the total of a JSON array of numbers (deterministic)\n      - values [required]: a JSON array of numbers to total\n    example: operation=\"sum\", values=\"<value>\"\n  count  [uv run python .opencode/scripts/calculate.py count]\n    the number of elements in a JSON array (deterministic)\n      - values [required]: a JSON array whose elements to count\n    example: operation=\"count\", values=\"<value>\"\n\nTo list every make target, use the `help` tool or run `make help`."
      }
    }
    return `Unknown operation: ${args.operation}`
  },
})
