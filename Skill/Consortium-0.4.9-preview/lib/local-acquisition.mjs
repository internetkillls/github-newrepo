import { spawnSync } from 'node:child_process';
import { existsSync, lstatSync, realpathSync, statSync } from 'node:fs';
import { relative, resolve, sep } from 'node:path';
import { identity, inspect } from './local-git.mjs';

function fail(message) { throw new Error(message); }
function ensureOutput(repo, out) {
  const target = resolve(out), parent = resolve(target, '..');
  if (!existsSync(parent) || !statSync(parent).isDirectory()) fail('Output parent must already exist');
  const base = realpathSync(parent);
  if (base === repo || base.startsWith(repo + sep) || repo.startsWith(base + sep) && target === repo) fail('AIF output must be outside repository root');
  return target;
}
export function contextPlan({ repo, task, portable = false, level = 'task' }) {
  const s = inspect(repo);
  if (!String(task||'').trim()) fail('A task statement is required');
  if (!['inventory','task','complete','delta'].includes(level)) fail('level must be inventory|task|complete|delta');
  const rationale = {
    inventory:'Start from native Git metadata; do not flatten just to list files.',
    task:'Prefer native agent search/read; export task context only for agents without repository access.',
    complete:'Use complete eligible-source snapshot with explicit policy exclusions and verification.',
    delta:'Inspect Git changes in the selected worktree; never call a task pack a historical source snapshot.'
  };
  const recommendation = (!portable && level!=='complete')?'native-git-search-read':level==='delta'?'native-git-diff':level==='inventory'?'native-git-inventory':level==='complete'?'aif-complete-snapshot':'aif-task-context';
  return {schema:'rcc.context-request.v1',task:String(task).trim(),identity:{repo:s.repo,gitDir:s.gitDir,head:s.head},mode:level,portable,preferred:recommendation,rationale:rationale[level],sourceState:'working-tree',statusSummary:{entries:s.status.length,untracked:s.status.filter(x=>x.kind==='?').length,staged:s.status.filter(x=>x.xy?.[0]!=='.'&&x.xy?.[0]!==' ').length,unstaged:s.status.filter(x=>x.xy?.[1]!=='.'&&x.xy?.[1]!==' ').length},requestedEvidence:['original paths','content sha256','policy omissions','selection reasons','source-state identity'],limitations:['Selection is not proof of dependency closure','Snapshot capture does not imply build completeness','New changes invalidate matching source hashes'],notExecuted:true};
}
export function aifCommand({ repo, executable, action, output, task, bundle, chars = 180000 }) {
  const r = identity(repo).repo;
  if (!executable) fail('Provide --exe=<absolute path to AIFolderFlatten.exe>');
  const exe = realpathSync(resolve(executable));
  if (!lstatSync(exe).isFile()) fail('Executable must be a regular local file');
  if (!['task','complete','verify-task','verify-complete'].includes(action)) fail('Unknown AIF action');
  let args;
  if (action==='task') {
    if (!String(task||'').trim()) fail('Provide --task=<task>');
    if (!Number.isSafeInteger(Number(chars)) || chars < 1024 || chars > 50_000_000) fail('Invalid --budget-chars');
    const parent = ensureOutput(r, output);
    args=['--input',r,'--task-context',task,'--output',parent,'--task-budget-chars',String(chars),'--task-cockpit','true','--open-after-export','never'];
  } else if (action==='complete') {
    const parent = ensureOutput(r,output);
    args=['--input',r,'--snapshot-complete','true','--output',parent,'--redact','true','--open-after-export','never'];
  } else {
    const bundleDir = realpathSync(resolve(bundle||''));
    if (!statSync(bundleDir).isDirectory()) fail('Bundle directory missing');
    args=action==='verify-task'?['--verify-task-context',bundleDir,'--input',r]:['--verify-snapshot',bundleDir];
  }
  return {schema:'rcc.aif-delegation.v1',exe,args,root:r,action,limitations:action==='verify-complete'?['Offline bundle integrity verified, not current source freshness.']:['Respect AIF selection and privacy policy exclusions.']};
}
export function executeAif(command) {
  const r = spawnSync(command.exe,command.args,{encoding:'utf8',timeout:120000,maxBuffer:4*1024*1024,windowsHide:true});
  return {schema:'rcc.aif-result.v1',action:command.action,exitCode:r.status,error:r.error?.message||null,stdout:r.stdout||'',stderr:r.stderr||'',completed:r.status===0&& !r.error,claim:r.status===0?'Process succeeded; review AIF output and verification before use.':'Delegated process failed; no success inferred.'};
}
