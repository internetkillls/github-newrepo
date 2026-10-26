import { spawnSync } from "node:child_process";
import { mkdtempSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const cli = resolve(root, "bin", "rcc-consortium");
const testDir = mkdtempSync(resolve(tmpdir(), "rcc-runtime-test-"));

function run(program, args) {
  const r = spawnSync(process.execPath, [program, ...args], { cwd: testDir, encoding: "utf8" });
  if (r.status !== 0) throw new Error(`command failed: ${args.join(" ")}\n${r.stdout}\n${r.stderr}`);
  return r.stdout;
}

try {
  const help = run(cli, ["help"]);
  if (!help.includes("workers spawn")) throw new Error("help surface missing workers spawn");
  const selftest = JSON.parse(run(cli, ["selftest"]));
  if (!selftest.ok) throw new Error("runtime selftest returned not ok");
  const dry = JSON.parse(run(cli, ["workers", "spawn", "--case=selftest", "--dry-run"]));
  if (!dry.ok || dry.state.workers.length !== 5) throw new Error("dry-run worker spawn did not create 5 roles");
  if (new Set(dry.state.workers.map((w) => w.alias)).size !== 5) throw new Error("worker aliases are not unique");
  const atomic = JSON.parse(run(resolve(root, "runtime", "chatgpt-pro-line", "scripts", "atomic-json-selftest.mjs"), []));
  if (!atomic.ok) throw new Error("atomic JSON selftest returned not ok");
  console.log(JSON.stringify({ ok: true, tests: ["help", "selftest", "dry-run-spawn", "atomic-json-fsync"] }, null, 2));
} finally {
  rmSync(testDir, { recursive: true, force: true });
}
