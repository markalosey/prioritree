// vote_query.ts — the axis-query wrapper (FR-MEM-0043's cure): the calculate
// family's form over the vote_query engine at .opencode/scripts/vote_query.py —
// the cell-table op exposed at the seats (the registration rides opencode.json's
// seat maps, the calculate rows' form: allow at every seat but the collaborator's).
// Hand-landed at prioritree's .opencode per the dispatch (packet recommend/calc-ops,
// route order-bias-probe, 2026-11-26) — the harness lane, the calculate.ts precedent.
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
  description: "Axis query over the vote data — the structured cell table (every pair × class × presentation → count + the winners list per cell; the doubles visible at their cells), ONE CALL returning the trace line {\"op\",\"args\",\"result\"} (the provenance: the op, the args as sent, the table — the total at one call, the remaining cells derivable). Pure, deterministic, fixed-argv: the run file read whole, nothing mutated; the cell rule's ground served — the winners list per cell AS RECORDED, never the rule (the analysis stays the seats'). Domain errors refuse ThreePart-shaped (Expected/Found/Next-action) — the same inputs always return the same trace bytes. anti_scenario: NOT an analysis engine (no flips rule, no tally, no rank), NOT a mutation surface, NOT a vote store — the query verb only.",
  args: {
    operation: tool.schema
      .enum(["cell-table"])
      .or(tool.schema.literal("help"))
      .describe("Operation to perform (use \"help\" to print this tool's usage)"),
    run_file: tool.schema.string().optional()
      .describe("the run file's path (the votes' JSONL — the manifest line rides its head, skipped at the count)"),
    items: tool.schema.string().optional()
      .describe("the manifest's items — the id list (a JSON array, in the manifest's order) or the manifest file's path (read whole; the manifest line's items extracted)"),
  },
  async execute(args, context) {

    switch (args.operation) {
      case "cell-table": {
        const eargs = ["cell-table"]
        if (args.run_file !== undefined) eargs.push(`--run-file=${args.run_file}`)
        if (args.items !== undefined) eargs.push(`--items=${args.items}`)
        return formatOutput(await runArgv(["uv", "run", "python", ".opencode/scripts/vote_query.py", ...eargs], { cwd: context.directory }))
      }
      case "help": {
        return "vote_query — Axis query over the vote data — the structured cell table (every pair × class × presentation → count + the winners list per cell; the doubles visible at their cells), ONE CALL returning the trace line {\"op\",\"args\",\"result\"} (the provenance inseparable from the table).\n\nOperations:\n  cell-table  [uv run python .opencode/scripts/vote_query.py cell-table]\n    the structured table — every pair x class x presentation -> count + the winners list per cell\n      - run_file [required]: the run file's path (the votes' JSONL — the manifest line rides its head, skipped at the count)\n      - items [required]: the manifest's items — the id list (a JSON array, in the manifest's order) or the manifest file's path (read whole; the manifest line's items extracted)\n    example: operation=\"cell-table\", run_file=\"<value>\", items=\"<value>\"\n"
      }
    }
    return `Unknown operation: ${args.operation}`
  },
})
