// prioritree-owned (.opencode/tools/_run.ts) — maintained by hand in prioritree's tree; composed 2026-11-19 from tane's amendment-354 helper (FR-MEM-0145's durable fix — the multiline-mangling fix's recorded provenance, tane/_run.ts:1-7)
//
// Purpose: runArgv — one shared subprocess channel for the .opencode/tools/ wrappers: it takes the explicit argv array, spawns it via Bun.spawn (no shell, no template literal, no interpolation), captures stdout and stderr whole, and returns them with the exit code; the multiline payload (a patch's --diff=...) rides as one argv element, byte-preserved.
// Refuses when: nothing — a failed spawn is returned honestly (exit code + captured output), never a silent empty.
// Re-run: imported by the wrappers at .opencode/tools/*.ts (dead code until the first wrapper imports it); verified by the per-file tsc lane after each edit.
// Touches: nothing on disk — the capture is in memory; the only writes are the spawned child's.
// Provenance: FR-MEM-0145 (the pain, open, tool-usage — the Bun.$ shell template literal mangles multiline payloads); CR-MEM-0036 (the composed design — decision 1: candidate B, the shared helper); amendment 354 (the tane-ownership stamp shape).

export interface RunArgvOptions {
  /** The directory the invocation runs in — the wrappers' convention is the seat's context.directory. */
  cwd?: string
  /** Extra env composition: process.env + NO_COLOR ("1") + the options layer. */
  env?: Record<string, string | undefined>
}

/** The result: the exit code + stdout and stderr captured whole — the shape formatOutput consumes today (text() is the ShellResult-compatible accessor; stderr is a string, whose .toString() works). */
export interface RunArgvResult {
  exitCode: number
  stdout: string
  stderr: string
  text(): string
}

export async function runArgv(
  argv: readonly string[],
  options?: RunArgvOptions,
): Promise<RunArgvResult> {
  const env: Record<string, string | undefined> = { ...process.env, NO_COLOR: "1", ...options?.env }
  try {
    const proc = Bun.spawn({
      cmd: [...argv],
      cwd: options?.cwd,
      env,
      stdout: "pipe",
      stderr: "pipe",
      stdin: "ignore",
    })
    const [stdout, stderr] = await Promise.all([
      new Response(proc.stdout).text(),
      new Response(proc.stderr).text(),
    ])
    const exitCode = await proc.exited
    return {
      exitCode,
      stdout,
      stderr,
      text: () => stdout,
    }
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error)
    return {
      exitCode: 127,
      stdout: "",
      stderr: message,
      text: () => "",
    }
  }
}
