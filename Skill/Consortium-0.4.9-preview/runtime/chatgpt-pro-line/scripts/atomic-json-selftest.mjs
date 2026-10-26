import assert from "node:assert/strict";
import fs from "node:fs";
import { mkdtempSync, readFileSync, readdirSync, rmSync } from "node:fs";
import { syncBuiltinESMExports } from "node:module";
import { tmpdir } from "node:os";
import { resolve } from "node:path";
import { writeTextAtomic } from "../src/atomic-json.mjs";

const dir = mkdtempSync(resolve(tmpdir(), "rcc-atomic-json-test-"));
const target = resolve(dir, "state.json");
const originalFsync = fs.fsyncSync;

function failFsync(code) {
  fs.fsyncSync = () => {
    const error = new Error(`injected ${code}`);
    error.code = code;
    throw error;
  };
  syncBuiltinESMExports();
}

try {
  writeTextAtomic(target, "before\n");
  assert.equal(readFileSync(target, "utf8"), "before\n");

  failFsync("EPERM");
  assert.throws(() => writeTextAtomic(target, "after\n"), { code: "EPERM" });
  assert.equal(readFileSync(target, "utf8"), "before\n");

  failFsync("EIO");
  assert.throws(() => writeTextAtomic(target, "uncommitted\n"), { code: "EIO" });
  assert.deepEqual(readdirSync(dir), ["state.json"]);
  assert.equal(readFileSync(target, "utf8"), "before\n");
} finally {
  fs.fsyncSync = originalFsync;
  syncBuiltinESMExports();
  rmSync(dir, { recursive: true, force: true });
}

console.log(JSON.stringify({ ok: true, tested: "atomic-json-fsync" }));
