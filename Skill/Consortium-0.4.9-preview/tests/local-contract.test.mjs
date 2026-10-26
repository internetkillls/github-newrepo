import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import { mkdtempSync, mkdirSync, readFileSync, writeFileSync, symlinkSync, existsSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';
import { inspect, patchPlan, applyPlan, parsePorcelain2 } from '../lib/local-git.mjs';
import { aifCommand, contextPlan } from '../lib/local-acquisition.mjs';

function git(cwd, ...args) {const r=spawnSync('git',['-C',cwd,...args],{encoding:'utf8'});if(r.status!==0)throw new Error(r.stderr||r.stdout);return r.stdout;}
function fixture(){const root=mkdtempSync(join(tmpdir(),'rcc-local-test-'));git(root,'init','-q');git(root,'config','user.email','rcc-test@example.invalid');git(root,'config','user.name','RCC Test');writeFileSync(join(root,'alpha.txt'),'alpha\n');writeFileSync(join(root,'other.txt'),'other\n');git(root,'add','.');git(root,'commit','-qm','base');return root;}
function createDiff(repo, change='updated\n'){writeFileSync(join(repo,'alpha.txt'),change);const patch=git(repo,'diff','--','alpha.txt');writeFileSync(join(repo,'alpha.txt'),'alpha\n');const p=join(tmpdir(),'rcc-patch-'+Date.now()+'-'+Math.random().toString(16).slice(2)+'.diff');writeFileSync(p,patch);return p;}
test('Git inspection, status parser and worktree isolation',t=>{const r=fixture();t.after(()=>rmSync(r,{recursive:true,force:true}));const s=inspect(r);assert.equal(s.status.length,0);assert.equal(s.worktrees.length,1);writeFileSync(join(r,'odd path.txt'),'x');const u=inspect(r);assert.equal(u.status[0].path,'odd path.txt');assert.equal(u.status[0].kind,'?');assert.throws(()=>inspect(join(r,'.git')),/not a subdirectory|git .* failed|exact worktree root/);
 const parsed=parsePorcelain2(Buffer.from('2 R. N... 100644 100644 100644 abc abc R100 new name.txt\0old name.txt\0'));assert.equal(parsed[0].original,'old name.txt');
 const worktree=join(tmpdir(),'rcc-wt-'+Math.random().toString(16).slice(2));git(r,'worktree','add','--detach',worktree,'-q');t.after(()=>{try{git(r,'worktree','remove','--force',worktree);}catch{};rmSync(worktree,{recursive:true,force:true});});assert.notEqual(inspect(r).gitDir,inspect(worktree).gitDir);
});
test('Patch plan rejects dirty target, stale preimage, wrong approval, and safely applies',t=>{const r=fixture();t.after(()=>rmSync(r,{recursive:true,force:true}));const patch=createDiff(r);t.after(()=>rmSync(patch,{force:true}));writeFileSync(join(r,'other.txt'),'local work remains\n');const plan=patchPlan(r,patch);assert.equal(plan.affected[0].path,'alpha.txt');assert.ok(plan.approvalId);assert.throws(()=>applyPlan(r,plan,'bad'),/approval/);assert.equal(readFileSync(join(r,'alpha.txt'),'utf8'),'alpha\n');
 writeFileSync(join(r,'alpha.txt'),'local edit\n');assert.throws(()=>applyPlan(r,plan,plan.approvalId),/already-changed|since plan/);writeFileSync(join(r,'alpha.txt'),'alpha\n');assert.equal(patchPlan(r,patch).approvalId,plan.approvalId); // restoring the original preimage makes the plan valid again
});
test('Patch apply exact approval, permit unrelated dirty file, do not stage or commit',t=>{const r=fixture();t.after(()=>rmSync(r,{recursive:true,force:true}));const p=createDiff(r);t.after(()=>rmSync(p,{force:true}));writeFileSync(join(r,'other.txt'),'user change\n');const plan=patchPlan(r,p);const receipt=applyPlan(r,plan,plan.approvalId);assert.equal(receipt.status,'APPLIED_TO_WORKTREE');assert.equal(receipt.testsRun,false);assert.equal(readFileSync(join(r,'alpha.txt'),'utf8'),'updated\n');assert.equal(readFileSync(join(r,'other.txt'),'utf8'),'user change\n');assert.equal(git(r,'diff','--cached').length,0);assert.equal(inspect(r).head,plan.head);});
test('Patch rejects file deletions',t=>{const r=fixture();t.after(()=>rmSync(r,{recursive:true,force:true}));git(r,'rm','alpha.txt');const del=git(r,'diff','--cached');const delPath=join(tmpdir(),'rcc-deletion-'+Date.now()+'.diff');writeFileSync(delPath,del);t.after(()=>rmSync(delPath,{force:true}));assert.throws(()=>patchPlan(r,delPath),/deletion denied|already-changed|deletion, mode/);});

test('Patch rejects symlink targets when the host can create a symlink',t=>{const r=fixture();t.after(()=>rmSync(r,{recursive:true,force:true}));const ext=join(tmpdir(),'rcc-outside-'+Date.now());writeFileSync(ext,'alpha\n');t.after(()=>rmSync(ext,{force:true}));try{symlinkSync(ext,join(r,'link.txt'));}catch(error){if(process.platform==='win32'&&['EPERM','EACCES'].includes(error.code)){t.skip('Windows file-symlink privilege unavailable; symlink rejection not verified on this host');return}throw error}const fake=join(tmpdir(),'rcc-fake-'+Date.now()+'.diff');writeFileSync(fake,'diff --git a/link.txt b/link.txt\nindex 4a58007..50137a8 100644\n--- a/link.txt\n+++ b/link.txt\n@@ -1 +1 @@\n-alpha\n+changed\n');t.after(()=>rmSync(fake,{force:true}));assert.throws(()=>patchPlan(r,fake),/Symlink traversal denied/);});
test('Context acquisition selects native by default and AIF only when needed',t=>{const r=fixture();t.after(()=>rmSync(r,{recursive:true,force:true}));const native=contextPlan({repo:r,task:'fix a bug'});assert.equal(native.preferred,'native-git-search-read');const portable=contextPlan({repo:r,task:'fix a bug',portable:true});assert.equal(portable.preferred,'aif-task-context');assert.equal(contextPlan({repo:r,task:'audit',level:'complete'}).preferred,'aif-complete-snapshot');assert.throws(()=>contextPlan({repo:r,task:' '}),/task statement/);});
test('AIF delegation is explicit and cannot output inside source root',t=>{const r=fixture();t.after(()=>rmSync(r,{recursive:true,force:true}));const exe=join(tmpdir(),'aif-simulator-'+Date.now()+'.exe');writeFileSync(exe,'mock');t.after(()=>rmSync(exe,{force:true}));const out=mkdtempSync(join(tmpdir(),'aif-output-'));t.after(()=>rmSync(out,{recursive:true,force:true}));const cmd=aifCommand({repo:r,executable:exe,action:'task',task:'fix tests',output:out});assert.deepEqual(cmd.args.slice(0,2),['--input',r]);assert(cmd.args.includes('--task-context'));assert.throws(()=>aifCommand({repo:r,executable:exe,action:'complete',output:join(r,'generated')}),/outside repository|parent/);});
test('Staged state blocks patch; ignored path and stale HEAD block apply',t=>{
 const r=fixture();t.after(()=>rmSync(r,{recursive:true,force:true}));const patch=createDiff(r);t.after(()=>rmSync(patch,{force:true}));
 writeFileSync(join(r,'alpha.txt'),'staged change\n');git(r,'add','alpha.txt');assert.throws(()=>patchPlan(r,patch),/already-changed/);
 git(r,'reset','-q','HEAD','--','alpha.txt');writeFileSync(join(r,'alpha.txt'),'alpha\n');
 const plan=patchPlan(r,patch);
 writeFileSync(join(r,'new.txt'),'new\n');git(r,'add','new.txt');git(r,'commit','-qm','advance');
 assert.throws(()=>applyPlan(r,plan,plan.approvalId),/since plan/);
 writeFileSync(join(r,'.gitignore'),'ignored.txt\n');git(r,'add','.gitignore');git(r,'commit','-qm','ignore');
 const ignoredPatch=join(tmpdir(),'rcc-ignored-'+Date.now()+'.diff');writeFileSync(ignoredPatch,'diff --git a/ignored.txt b/ignored.txt\nnew file mode 100644\nindex 0000000..e69de29\n--- /dev/null\n+++ b/ignored.txt\n@@ -0,0 +1 @@\n+hidden\n');t.after(()=>rmSync(ignoredPatch,{force:true}));
 assert.throws(()=>patchPlan(r,ignoredPatch),/Git-ignored/);
});
test('CLI dispatch prints machine-readable JSON and honors dry-run AIF',t=>{
 const r=fixture();t.after(()=>rmSync(r,{recursive:true,force:true}));
 const cli=resolve('bin/rcc-consortium');
 const run=(...argv)=>spawnSync(process.execPath,[cli,...argv],{cwd:resolve('.'),encoding:'utf8'});
 const inspected=run('local','git','inspect',`--repo=${r}`);assert.equal(inspected.status,0,inspected.stderr);assert.equal(JSON.parse(inspected.stdout).inspectionOnly,true);
 const prepared=run('local','context','plan',`--repo=${r}`,'--task=inspect');assert.equal(prepared.status,0,prepared.stderr);assert.equal(JSON.parse(prepared.stdout).notExecuted,true);
 const fake=join(tmpdir(),'rcc-mock-aif-'+Date.now()+'.exe');writeFileSync(fake,'no-execution');t.after(()=>rmSync(fake,{force:true}));const out=mkdtempSync(join(tmpdir(),'rcc-ex-out-'));t.after(()=>rmSync(out,{force:true,recursive:true}));
 const aif=run('local','aif','complete',`--repo=${r}`,`--exe=${fake}`,`--output=${out}`);assert.equal(aif.status,0,aif.stderr);assert.match(aif.stdout,/NOT_RUN/);
});
