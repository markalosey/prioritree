// kumi_render — the packet-report view's wrapper (the report-op port's view half,
// 2026-11-21): renders a store's packet ledger as markdown AT READ TIME through
// hikari's render home (scripts/kumi_render.py). One home, any store: the caller
// names the store and the packet; nothing lands, nothing goes stale (the
// generated-on-read doctrine). Hand-maintained in prioritree's tree (the junro.ts
// family).
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
  description:
    "The packet-report view — render a store's packet ledger as markdown AT READ TIME (generated-on-read: the structured ledger is canonical, the markdown a derived projection; no file lands, nothing goes stale). The report events' content served whole under engine-stamped provenance. The store is any effort directory carrying a .junro/ heart — either tree's stores serve. anti_scenario: NOT a writer — this view only renders; the junro tool stays the only writer inside .junro/; do NOT use it to mutate any store.",
  args: {
    store: tool.schema
      .string()
      .describe("the effort directory (the store) — the packet ledger's home (either tree's store serves)"),
    packet: tool.schema
      .string()
      .describe("the packet id whose chain and reports render (e.g. build/core or synthesize/service-store)"),
    view: tool.schema
      .string()
      .optional()
      .describe("the view to render (default: packet-report — the packet ledger's projection)"),
  },
  async execute(args, context) {
    const eargs = ["--view", args.view ?? "packet-report", "--store", args.store, "--packet", args.packet]
    return formatOutput(
      await runArgv(
        [
          "uv",
          "run",
          "--project",
          "/Users/marklosey/projects/kepric/hikari",
          "python",
          "/Users/marklosey/projects/kepric/hikari/scripts/kumi_render.py",
          ...eargs,
        ],
        { cwd: context.directory },
      ),
    )
  },
})
