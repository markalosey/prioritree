/**
 * OpenCode local plugin: empty-return detector (CA-29) + plain-edit-JSON
 * warning (B-k §4.4 fold).
 *
 * Written origin (Gate 1):
 *   - CA-29 — SE review `.plans/postmortems/2026-09-09-retro-agent-system-evolve-2-evolve-review.md`
 *     §1 (:17) + §4 item 12 (:90); retro CA-29 (:251-259).
 *   - B-k §4.4 fold — b-k-assess.md:80-82, coordinator-approved per the s6/08
 *     delegation (rides cheaply on this plugin's already-built pattern).
 *   - RN-ML-28 toast amendment (agent-system-evolve-3 s2-e2/02, CA-56
 *     propagation): the EMPTY-RETURN toast now carries the git-status
 *     recovery step between re-attach and fresh-session restart — "if still
 *     empty, INSPECT GIT STATUS for completed work before re-delegating (the
 *     work may exist)" (both observed RN-ML-28 cases: the deliverables
 *     existed on the branch though the completion report was lost).
 *     Text-only change inside the existing showToast call — flags-only
 *     contract and v1 module shape untouched.
 *
 * Auto-discovered from `.opencode/plugins/` (project dir — same as
 * tool-use-enforcement.ts). NO opencode.json entry: local .ts plugins are not
 * registered there (opencode.json lists npm packages only).
 *
 * Restart caveat: changes take effect only after an opencode restart
 * (tool-use-enforcement.ts:34 precedent).
 *
 * FLAGS ONLY (VS-01 boundary — b-m-discover.md §2.4):
 *   - NEVER throws (contrast tool-use-enforcement's deliberate block-throw; a
 *     throw at tool.execute.after is out-of-contract anyway and would be a
 *     crash risk, not a flag);
 *   - NEVER mutates output/output.metadata (read-only observation);
 *   - NEVER acts — no auto-restart, no re-invocation, no bypass of the
 *     re-attach protocol. The toast text POINTS AT VS-01 rule 14, it does not
 *     perform it.
 *
 * CA-43 AMENDMENT (user directive 2026-09-10): the JSON-plain-edit fold now
 * BOTH toasts (the human sees it — kept, a good notification pattern) AND
 * THROWS at tool.execute.before so the AGENT is blocked and self-corrects.
 * Throwing at before-time IS the sanctioned block mechanism
 * (tool-use-enforcement.ts precedent, opencode issue #5894): the thrown
 * message is surfaced to the agent as the blocked-tool error. The flags-only
 * contract is AMENDED for this one fold, not abandoned: the empty-return
 * detector (after-hook) stays flags-only because throwing at after-time is
 * out-of-contract.
 *
 * Hook signatures — confirmed from installed types
 * (`.opencode/node_modules/@opencode-ai/plugin/dist/index.d.ts:235-258`):
 *
 *     "tool.execute.before"?: (input: {
 *         tool: string; sessionID: string; callID: string;
 *     }, output: { args: any }) => Promise<void>;
 *
 *     "tool.execute.after"?: (input: {
 *         tool: string; sessionID: string; callID: string; args: any;
 *     }, output: { title: string; output: string; metadata: any }) => Promise<void>;
 *
 * Toasts are SHOWN via the SDK client: `input.client.tui.showToast({ body: {...} })`
 * (POST /tui/show-toast; TuiShowToastData = { title?, message, variant,
 * duration? } — sdk types.gen.d.ts:3264-3279). `tui.toast.show` is an inbound
 * EVENT plugins can only receive, not a way to show a toast.
 *
 * Shape drift ≠ empty (b-m-discover.md §2.3): a missing/non-string
 * output.output is logged as drift-debug, NEVER flagged — the API surface is
 * version-volatile (otel-enrich's own output?.ok read at :460 drifted against
 * the installed types); flagging on an absent field would fire on every call
 * after a shape change.
 *
 * Debug channel: ~/.config/opencode/_debug/empty-return-detector.txt
 * (otel-enrich.ts:46-54 precedent — append-file with all errors swallowed).
 * Markers: [EMPTY-RETURN], [JSON-PLAIN-EDIT], [JSON-FULL-FILE-WRITE],
 * plus LOAD / SHAPE_DRIFT / EVT_FAIL / TOAST_FAIL diagnostics.
 *
 * Design authority: artifacts/b-m-discover.md §2 (detector), §3 (JSON fold).
 */

import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import type { Plugin, PluginModule } from "@opencode-ai/plugin";

// ---------------------------------------------------------------------------
// Debug log (never crash opencode)
// ---------------------------------------------------------------------------

function debugLog(line: string) {
  try {
    const dir = path.join(os.homedir(), ".config", "opencode", "_debug");
    fs.mkdirSync(dir, { recursive: true });
    fs.appendFileSync(path.join(dir, "empty-return-detector.txt"), line + "\n", "utf8");
  } catch {
    // swallow everything: never crash opencode
  }
}

// ---------------------------------------------------------------------------
// Pure classifiers (side-effect free so they are unit-testable without a
// running opencode — tool-use-enforcement.ts:89 discipline)
// ---------------------------------------------------------------------------

/**
 * Classify a tool.execute.after event for the CA-29 empty-return class.
 *
 * - `task` tool + a present, empty/whitespace-only output string → FLAG.
 * - `task` tool + missing/non-string output.output → shape-drift (debug line,
 *   NEVER a flag/toast — b-m-discover.md §2.3).
 * - any other tool → no flag (scope filter: only the task/delegation tool has
 *   the evidenced empty-return class; broader scope false-positives on
 *   legitimately-empty results like a no-match grep).
 */
export type TaskReturnClassification =
  | { flag: false; reason?: undefined }
  | { flag: true; reason: "empty"; output_bytes: number }
  | { flag: false; reason: "shape-drift" };

export function classifyTaskReturn(
  input: { tool?: unknown } | undefined | null,
  output: { output?: unknown } | undefined | null,
): TaskReturnClassification {
  if (input?.tool !== "task") return { flag: false };
  const text = output?.output;
  if (typeof text !== "string") return { flag: false, reason: "shape-drift" };
  if (text.trim() === "") return { flag: true, reason: "empty", output_bytes: 0 };
  return { flag: false };
}

/**
 * Classify a tool.execute.before event for the PR-H33 JSON-edit fold.
 *
 * - `edit` on *.json → WARN (targeted text edits on JSON are never sanctioned —
 *   PR-H33 "never by targeted text edits"; the RN-AE2-07 incident class).
 * - `write` on *.json → LOG-ONLY (the PR-H33 full-file fallback is sanctioned
 *   when reconstructed from a parsed load + explicit parse check; the hook
 *   cannot observe the check at before-time, so it keeps the audit trail
 *   without alarm-fatiguing the sanctioned path).
 *
 * Shape-tolerant path read (otel-enrich learnRuntimeFromPayload idiom): the
 * built-in edit/write tools take `filePath`; alternates cover arg-name drift.
 */
export type JsonEditClassification =
  | { level: "warn"; kind: "edit"; filePath: string }
  | { level: "log"; kind: "write"; filePath: string }
  | { level: null };

export function classifyJsonWriteAttempt(tool: unknown, args: any): JsonEditClassification {
  const p = args?.filePath ?? args?.file_path ?? args?.path;
  if (typeof p !== "string" || !p.toLowerCase().endsWith(".json")) return { level: null };
  if (tool === "edit") return { level: "warn", kind: "edit", filePath: p };
  if (tool === "write") return { level: "log", kind: "write", filePath: p };
  return { level: null };
}

// ---------------------------------------------------------------------------
// Small defensive helpers
// ---------------------------------------------------------------------------

/** JSON.stringify().length of the args, defensive (-1 if unserializable). */
function safeJsonLength(v: unknown): number {
  try {
    const s = JSON.stringify(v);
    return typeof s === "string" ? s.length : -1;
  } catch {
    return -1;
  }
}

function safeTitle(output: unknown): string {
  const t = (output as any)?.title;
  return typeof t === "string" ? t : "?";
}

/**
 * Show a TUI toast via the SDK client. Wrapped in its own try/catch: a failing
 * toast must never lose the log line (callers log BEFORE toasting) and must
 * never crash opencode.
 */
async function showToast(
  ctx: any,
  body: {
    title?: string;
    message: string;
    variant: "info" | "success" | "warning" | "error";
    duration?: number;
  },
): Promise<void> {
  try {
    await ctx?.client?.tui?.showToast?.({ body });
  } catch (e: any) {
    debugLog(`TOAST_FAIL ${String(e?.message ?? e)}`);
  }
}

// ---------------------------------------------------------------------------
// The plugin
// ---------------------------------------------------------------------------

const EmptyReturnDetectorServer: Plugin = async (ctx: any) => {
  // LOAD line at init — the post-restart proof leg (otel-enrich.ts:285 idiom).
  debugLog(`LOAD ${new Date().toISOString()} cwd=${ctx?.directory ?? "?"}`);

  return {
    // ---- JSON plain-edit warning fold (B-k §4.4, CA-43 amended) -----------
    // Both channels: the toast notifies the human; the thrown error blocks
    // the agent's edit call and surfaces the corrective instruction (use
    // make json-edit). The throw happens OUTSIDE the fail-open try/catch so
    // the fail-open path cannot swallow the intentional block
    // (tool-use-enforcement.ts precedent).
    "tool.execute.before": async (
      input: { tool: string; sessionID: string; callID: string },
      output: { args: any },
    ): Promise<void> => {
      let block: Error | undefined;
      try {
        const c = classifyJsonWriteAttempt(input?.tool, output?.args);
        if (c.level === null) return;

        if (c.kind === "edit") {
          // NEVER sanctioned (PR-H33: targeted text edits on JSON): warn
          // the human AND block the agent (CA-43).
          debugLog(
            `[JSON-PLAIN-EDIT] ${new Date().toISOString()} ` +
              `session=${input?.sessionID ?? "?"} call=${input?.callID ?? "?"} ` +
              `file=${c.filePath}`,
          );
          await showToast(ctx, {
            title: "Plain edit on a .json file",
            message:
              `[JSON-PLAIN-EDIT] ${path.basename(c.filePath)} — PR-H33: use ` +
              `make json-edit (the structured editor). Only if a full-file ` +
              `rewrite is genuinely needed: write from a parsed load, then run ` +
              `an explicit parse check.`,
            variant: "warning",
            duration: 15000,
          });
          block = new Error(
            `[JSON-PLAIN-EDIT] targeted text edits on .json files are never ` +
              `sanctioned (PR-H33) — a plain edit can silently corrupt JSON ` +
              `structure. Use the structured editor instead: ` +
              `make json-edit FILE=${c.filePath} OP=get|set|del|append ` +
              `KEY=<dotpath> VALUE=<json>. Only if a full-file rewrite is ` +
              `genuinely needed: write from a parsed load (load-modify-dump), ` +
              `then run an explicit parse check.`,
          );
        } else {
          // The sanctioned PR-H33 fallback (write from parsed load + parse
          // check) is indistinguishable at before-time from an unchecked
          // write — LOG-ONLY, no toast (b-m-discover.md §3.1).
          debugLog(
            `[JSON-FULL-FILE-WRITE] ${new Date().toISOString()} ` +
              `session=${input?.sessionID ?? "?"} call=${input?.callID ?? "?"} ` +
              `file=${c.filePath}`,
          );
        }
      } catch (e: any) {
        debugLog(`EVT_FAIL tool.execute.before ${String(e?.message ?? e)}`);
      }
      if (block) throw block;
    },

    // ---- empty-return detector (CA-29) -------------------------------------
    "tool.execute.after": async (
      input: { tool: string; sessionID: string; callID: string; args: any },
      output: { title: string; output: string; metadata: any },
    ): Promise<void> => {
      try {
        const c = classifyTaskReturn(input, output);
        if (c.reason === "shape-drift") {
          // Drift-debug, not a flag (b-m-discover.md §2.3).
          debugLog(
            `SHAPE_DRIFT tool.execute.after tool=${input?.tool} — output.output missing/non-string`,
          );
          return;
        }
        if (!c.flag) return;

        // ---- the flag (fail-loud, grep-able) — LOG BEFORE TOAST ----
        const args = input?.args ?? {};
        const prompt = typeof args.prompt === "string" ? args.prompt : "";
        const desc = typeof args.description === "string" ? args.description : "";
        const agent = typeof args.subagent_type === "string" ? args.subagent_type : "?";
        const argsBytes = safeJsonLength(args);
        debugLog(
          `[EMPTY-RETURN] ${new Date().toISOString()} ` +
            `session=${input?.sessionID ?? "?"} call=${input?.callID ?? "?"} ` +
            `agent=${agent} desc="${desc}" prompt_chars=${prompt.length} ` +
            `args_bytes=${argsBytes} output_bytes=0 title="${safeTitle(output)}"`,
        );
        await showToast(ctx, {
          title: "Empty delegation return",
          message:
            `[EMPTY-RETURN] call=${input?.callID ?? "?"} agent=${agent} ` +
            `prompt_chars=${prompt.length} — re-attach to the SAME session per ` +
            `VS-01 (coordinator-system.md rule 14); if still empty, INSPECT GIT ` +
            `STATUS for completed work before re-delegating (the work may ` +
            `exist); do NOT restart from fresh.`,
          variant: "warning",
          duration: 15000,
        });
      } catch (e: any) {
        debugLog(`EVT_FAIL tool.execute.after ${String(e?.message ?? e)}`);
      }
    },
  };
};

// V1 plugin-module shape: the loader readV1Plugin detects { id, server } and
// calls ONLY server as the factory. Any other default shape falls through to
// getLegacyPlugins, which calls EVERY function export as a factory — the
// classify helpers are miscalled (inert today only by luck: their
// misscalled returns happen to be non-hook objects). Hardened to the v1
// shape per the tool-use-enforcement fix (fdee6a50 — same loader miscall
// threw "{} is not iterable" there and took the enforcement layer down).
const EmptyReturnDetector: PluginModule = {
  id: "empty-return-detector",
  server: EmptyReturnDetectorServer,
};

export default EmptyReturnDetector;
