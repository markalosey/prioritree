// prioritree-owned (2026-11-22, G-LIFECYCLESPEC-BRIEF's extension — Q-ux-surface R12/R13): the member-callable lifecycle surface; hand-maintained in prioritree's tree (lint.ts's standing form)
//
// Purpose: the lifecycle act — the members call the service's runtime directly (R12): the transitions (start/stop/status/restart) subprocess make through the _run.ts explicit-argv channel (the Makefile's recipes the ONE implementation; this wrapper the argv shim); the READ verbs are pure reads (R13): log — the server log's bounded tail (.prioritree/server.log, default the last 100 lines); output — the service's live answer, the RUN-9999 probe's response body rendered verbatim. Every op's output renders verbatim, never summarized.
// Refuses when: log finds .prioritree/server.log absent (the honest never-started report); output finds the port refused (the honest down report); the transitions refuse per the recipes' own guards — the exit codes pass through, never swallowed. NOT a shell, NOT a server manager beyond the ruled verbs: the four transitions + the two reads only.
// Re-run: the reads are pure (idempotent); the transitions idempotent per the recipes' own guards (start refuses on a live pid; stop exits 0 on the absent pidfile); the wrapper's verification is kensho's live run through the wrapper itself (validate/lifecycle — the registration + the verbs' read-backs; no pytest arc).
// Touches: nothing of its own — the recipes' writes (.prioritree/) are the only mutations; the read verbs never mutate (R13: the log is evidence, not state).
// Provenance: Q-ux-surface R12/R13 (2026-11-22, the collaborator's two rulings); the lifecyclespec extension (togo, packet synthesize/lifecyclespec); FR-MEM-0025 (the RUN-9999 context-free probe); lint.ts the wrapper precedent; _run.ts the explicit-argv channel.
import { tool } from "@opencode-ai/plugin"
import { readFileSync } from "node:fs"
import { join } from "node:path"
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
  description: "Lifecycle — the member-callable service-management surface: the transitions (start/stop/status/restart) over the host Makefile's targets via the explicit-argv runArgv channel (one implementation: the recipes; this wrapper the argv shim), plus the READ verbs (log — the server log's bounded tail, default 100; output — the service's live answer, the RUN-9999 probe's body verbatim). The reads are read-only; every op's output renders verbatim, never summarized. Host-only (no Docker, no worktrees); no shell.",
  args: {
    operation: tool.schema
      .enum(["start", "stop", "status", "restart", "log", "output"])
      .or(tool.schema.literal("help"))
      .describe("Operation to perform (use \"help\" to print this tool's usage)"),
    port: tool.schema.string().optional().describe("The service's port — appended as the make override PORT=<n> on the transitions (default 8000, the Makefile's own ?=); the probe's target on output"),
    host: tool.schema.string().optional().describe("The service's bind host — appended as the make override HOST=<h> on the transitions (default 127.0.0.1, the Makefile's own ?=); the probe's target on output"),
    tail: tool.schema.string().optional().describe("The log tail's line count (the log op only; default 100 — R13's bounded-tail discipline)"),
  },
  async execute(args, context) {
    const makeTarget = (target: string): string[] => {
      const argv = ["make", target]
      if (args.port) argv.push(`PORT=${args.port}`)
      if (args.host) argv.push(`HOST=${args.host}`)
      return argv
    }
    switch (args.operation) {
      case "start": {
        return formatOutput(await runArgv(makeTarget("start"), { cwd: context.directory }))
      }
      case "stop": {
        return formatOutput(await runArgv(makeTarget("stop"), { cwd: context.directory }))
      }
      case "status": {
        return formatOutput(await runArgv(makeTarget("status"), { cwd: context.directory }))
      }
      case "restart": {
        return formatOutput(await runArgv(makeTarget("restart"), { cwd: context.directory }))
      }
      case "log": {
        const path = join(context.directory, ".prioritree", "server.log")
        let text: string
        try {
          text = readFileSync(path, "utf8")
        } catch {
          return "log refused — Expected: .prioritree/server.log (the server's log, present after a start)\nFound: the file absent (the server has never been started)\nNext-action: lifecycle start first, or read the runtime state with lifecycle status"
        }
        const lines = text.split("\n")
        const parsed = args.tail ? Number.parseInt(args.tail, 10) : 100
        const n = Number.isFinite(parsed) && parsed > 0 ? parsed : 100
        const shown = lines.slice(-n).join("\n")
        return `log — ${path} (the last ${Math.min(n, lines.length)} of ${lines.length} lines; the bounded tail is the discipline — a full-file read is a budget question)\n${shown}`
      }
      case "output": {
        const host = args.host ?? "127.0.0.1"
        const port = args.port ?? "8000"
        const url = `http://${host}:${port}/runs/RUN-9999/next`
        try {
          const res = await fetch(url, { signal: AbortSignal.timeout(5000) })
          const body = await res.text()
          return `output — ${url} answered HTTP ${res.status} (the body verbatim):\n${body}`
        } catch (error) {
          const message = error instanceof Error ? error.message : String(error)
          return `output refused — Expected: the service answering on ${url} (the RUN-9999 probe — the honest ThreePart refusal proving the chain)\nFound: the connection refused (${message} — the server is down)\nNext-action: lifecycle start, or read the runtime state with lifecycle status`
        }
      }
      case "help": {
        return "lifecycle — the member-callable service-management surface (the transitions subprocess make — the recipes the one implementation; the reads pure).\n\nOperations:\n  start  [make start (+ PORT=/HOST= overrides)]\n    Start the server in the background; the read-back: the port answers (the RUN-9999 honest 404; 000 = still booting)\n  stop  [make stop]\n    SIGTERM + the bounded drain; the read-back: the refusal (the port down)\n  status  [make status]\n    The pid + the port, both labeled, read-only\n  restart  [make restart (+ PORT=/HOST= overrides)]\n    Stop then start: the refusal then the answer\n  log  [read .prioritree/server.log]\n    The server log's bounded tail (default the last 100 lines; tail=<n> overrides)\n  output  [probe http://127.0.0.1:8000/runs/RUN-9999/next]\n    The service's live answer — the response body verbatim"
      }
    }
    return `Unknown operation: ${args.operation}`
  },
})
