import { spawnSync } from "node:child_process";
import { resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(fileURLToPath(new URL("..", import.meta.url)));
const cli = resolve(root, "bin", "rcc-consortium");

function run(args) {
  const r = spawnSync(process.execPath, [cli, ...args], { cwd: root, encoding: "utf8" });
  if (r.status !== 0) throw new Error(`command failed: ${args.join(" ")}\n${r.stdout}\n${r.stderr}`);
  return r.stdout;
}

const help = run(["help"]);
if (!help.includes("workers spawn")) throw new Error("help surface missing workers spawn");
const selftest = JSON.parse(run(["selftest"]));
if (!selftest.ok) throw new Error("runtime selftest returned not ok");
const dry = JSON.parse(run(["workers", "spawn", "--case=selftest", "--dry-run"]));
if (!dry.ok || dry.state.workers.length !== 5) throw new Error("dry-run worker spawn did not create 5 roles");
if (new Set(dry.state.workers.map((w) => w.alias)).size !== 5) throw new Error("worker aliases are not unique");
console.log(JSON.stringify({ ok: true, tests: ["help", "selftest", "dry-run-spawn"] }, null, 2));
