import { spawnSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { existsSync, lstatSync, readFileSync, realpathSync } from 'node:fs';
import { isAbsolute, relative, resolve, sep } from 'node:path';

const sha = data => createHash('sha256').update(data).digest('hex');
const err = message => { throw new Error(message); };
function run(repo, ...args) {
  const r = spawnSync('git', ['-C', repo, ...args], { encoding: 'buffer', timeout: 12000, maxBuffer: 32 * 1024 * 1024, env: { ...process.env, GIT_OPTIONAL_LOCKS: '0', GIT_CONFIG_NOSYSTEM: '1' } });
  if (r.error || r.status !== 0) err(`git ${args[0]} failed: ${String(r.stderr || r.error).slice(0, 600)}`);
  return r.stdout;
}
function txt(repo, ...args) { return run(repo, ...args).toString('utf8').trim(); }
function nulList(buf) { return buf.toString('utf8').split('\0').filter(Boolean); }
export function identity(input) {
  const repo = realpathSync(resolve(input));
  const top = realpathSync(txt(repo, 'rev-parse', '--show-toplevel'));
  if (repo !== top) err('Point --repo at the exact worktree root, not a subdirectory');
  if (txt(repo, 'rev-parse', '--is-bare-repository') !== 'false') err('Bare repositories are unsupported');
  return { repo, gitDir: realpathSync(txt(repo, 'rev-parse', '--absolute-git-dir')), head: txt(repo, 'rev-parse', 'HEAD') };
}
export function parsePorcelain2(buffer) {
  const fields = buffer.toString('utf8').split('\0');
  const entries = [];
  for (let i = 0; i < fields.length; i++) {
    const row = fields[i]; if (!row) continue;
    const type = row[0];
    if (type === '?' || type === '!') { entries.push({ kind: type, path: row.slice(2) }); continue; }
    if (type === '1' || type === '2' || type === 'u') {
      const pieces = row.split(' ');
      const fixedCount = type === '1' ? 8 : type === '2' ? 9 : 10;
      if (pieces.length <= fixedCount) err('Malformed porcelain-v2 status entry');
      const path = pieces.slice(fixedCount).join(' ');
      const entry = { kind: type, xy: pieces[1], path };
      if (type === '2') { if (!fields[i+1]) err('Missing porcelain-v2 rename source'); entry.original = fields[++i]; }
      entries.push(entry); continue;
    }
    err('Unknown porcelain-v2 record type');
  }
  return entries;
}
export function inspect(input) {
  const id = identity(input);
  const status = parsePorcelain2(run(id.repo, 'status', '--porcelain=v2', '-z', '--untracked-files=all'));
  const worktreeLines = run(id.repo, 'worktree', 'list', '--porcelain', '-z').toString('utf8').split('\0');
  const worktrees = []; let current = {};
  for (const line of worktreeLines) {
    if (!line) { if (current.path) worktrees.push(current); current = {}; continue; }
    const first = line.indexOf(' '), key = first < 0 ? line : line.slice(0,first), value = first < 0 ? true : line.slice(first+1);
    if (key === 'worktree') current.path = value; else current[key] = value;
  }
  if (current.path) worktrees.push(current);
  return { schema: 'rcc.git-inspection.v1', ...id, status, worktrees, inspectionOnly: true };
}
function safePath(root, p) {
  if (typeof p !== 'string' || !p || p.includes('\0') || p.includes('\\') || isAbsolute(p) || /(^|\/)\.\.?($|\/)/.test(p) || /^[A-Za-z]:/.test(p)) err(`Invalid repository relative path: ${p}`);
  const parts = p.split('/');
  if (parts.some(x => !x || x.toLowerCase() === '.git' || x.toLowerCase() === '.devspace')) err(`Forbidden path: ${p}`);
  const name = parts.at(-1).toLowerCase();
  if (/(^\.env($|\.)|^\.npmrc$|^\.pypirc$|^id_(rsa|ed25519)$|\.(pem|p12|pfx|key)$)/i.test(name) || parts.some(x => /^(secrets?|credentials|node_modules)$/i.test(x))) err(`Sensitive/ignored path denied: ${p}`);
  const resolved = resolve(root, p);
  if (!resolved.startsWith(root + sep)) err('Path escapes repository');
  let probe = root;
  for (const segment of parts) {
    probe = resolve(probe, segment);
    if (!existsSync(probe)) break;
    if (lstatSync(probe).isSymbolicLink()) err(`Symlink traversal denied: ${p}`);
  }
  return resolved;
}
function fileState(repo, path) {
  const location = safePath(repo, path);
  if (!existsSync(location)) return { exists: false, sha256: null };
  if (!lstatSync(location).isFile()) err(`Not a regular file: ${path}`);
  return { exists: true, sha256: sha(readFileSync(location)) };
}
function getPatchPaths(repo, patch) {
  const buf = readFileSync(patch);
  if (buf.length > 2 * 1024 * 1024) err('Patch exceeds 2 MiB safety limit');
  const body = buf.toString('utf8');
  if (body.includes('\uFFFD') || /(^|\n)(GIT binary patch|Binary files |rename (from|to) |copy (from|to) |old mode |new mode |deleted file mode |new file mode 120000|index [^\n]* 160000)/m.test(body)) err('Binary, rename, deletion, mode, or symlink patch unsupported');
  if (/(^|\n)\+\+\+ \/dev\/null(?:\n|$)/.test(body)) err('File deletion denied');
  if (/\n\s*\x00/.test(body)) err('NUL in patch');
  // Git parses path identities from the actual patch; do not trust custom header parsing.
  const numstat = run(repo, 'apply', '--numstat', '-z', '--', patch).toString('utf8').split('\0');
  const paths = [];
  for (let i=0; i<numstat.length; i++) {
    const row = numstat[i]; if (!row) continue;
    const m = row.match(/^([0-9-]+)\t([0-9-]+)\t(.*)$/s);
    if (!m || !m[3] || m[1] === '-' || m[2] === '-') err('Unrecognized, rename or binary numstat format');
    safePath(repo, m[3]); paths.push(m[3]);
  }
  if (!paths.length || new Set(paths).size !== paths.length) err('Patch must change unique, inspectable paths');
  return { paths, patchSha256: sha(buf) };
}
function dirtySet(entries) { return new Set(entries.flatMap(x => [x.path, ...(x.original?[x.original]:[])])); }
function isIgnored(repo, path) {
  const r = spawnSync('git', ['-C',repo,'check-ignore','-q','--',path], {timeout:8000,encoding:'utf8'});
  if (r.error || (r.status !== 0 && r.status !== 1)) err(`Could not determine ignore policy for ${path}`);
  return r.status === 0;
}
function planBody(input, patch) {
  const before = inspect(input), patchPath = realpathSync(resolve(patch));
  const { paths, patchSha256 } = getPatchPaths(before.repo, patchPath);
  const dirty = dirtySet(before.status);
  const affected = paths.map(path => ({ path, ...fileState(before.repo,path), dirty:dirty.has(path), ignored: isIgnored(before.repo,path) }));
  if (affected.some(x=>x.ignored)) err('Patch may not touch Git-ignored paths');
  if (affected.some(x=>x.dirty)) err(`Refusing patch over already-changed paths: ${affected.filter(x=>x.dirty).map(x=>x.path).join(', ')}`);
  // Ensure that what is planned is applicable before returning any authorization handle.
  run(before.repo, 'apply', '--check', '--', patchPath);
  return {schema:'rcc.patch-plan.v1',repo:before.repo,gitDir:before.gitDir,head:before.head,patchPath,patchSha256,affected,permissions:{paths,operation:'git-apply-working-tree-only',staging:false,committing:false}};
}
export function patchPlan(repo,patch) {
  const body = planBody(repo,patch);
  const approvalId = sha(Buffer.from(JSON.stringify(body))).slice(0,24);
  return {...body,approvalId,requiresExplicitApproval:true};
}
export function applyPlan(repo, stored, approval) {
  if (!stored || stored.schema !== 'rcc.patch-plan.v1') err('Invalid stored patch plan');
  const { approvalId, requiresExplicitApproval, ...body } = stored;
  if (!requiresExplicitApproval || !/^[a-f0-9]{24}$/.test(approvalId) || approval !== approvalId || sha(Buffer.from(JSON.stringify(body))).slice(0,24) !== approvalId) err('Patch approval required or plan changed');
  const fresh = patchPlan(repo, stored.patchPath);
  if (JSON.stringify(fresh) !== JSON.stringify(stored)) err('Preimage, root, HEAD, or patch changed since plan');
  const before = fresh.affected.map(x => ({...x}));
  run(fresh.repo, 'apply', '--check', '--', fresh.patchPath);
  run(fresh.repo, 'apply', '--', fresh.patchPath);
  const after = fresh.affected.map(x => ({ path:x.path, ...fileState(fresh.repo,x.path) }));
  return {schema:'rcc.git-apply-receipt.v1',status:'APPLIED_TO_WORKTREE',repo:fresh.repo,headBefore:fresh.head,headAfter:identity(fresh.repo).head,approvalId,affectedBefore:before,affectedAfter:after,staged:false,committed:false,testsRun:false};
}
