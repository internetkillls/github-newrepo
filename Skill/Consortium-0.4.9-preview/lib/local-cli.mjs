import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { inspect, patchPlan, applyPlan } from './local-git.mjs';
import { aifCommand, contextPlan, executeAif } from './local-acquisition.mjs';
function fail(message) {throw new Error(message);}
function value(args,k,defaultValue='') {const item=args.find(x=>x.startsWith(`--${k}=`));return item?item.slice(k.length+3):defaultValue;}
function has(args,k) {return args.includes(`--${k}`);}
function writeOptional(result,args,field='output'){const file=value(args,field);if(file){const path=resolve(file);mkdirSync(dirname(path),{recursive:true});writeFileSync(path,JSON.stringify(result,null,2)+'\n',{mode:0o600});return {...result,writtenTo:path};}return result;}
export function localUsage() {
 return `Local-first (Node 20+ and Git):\n`+
 `  rcc-consortium local git inspect --repo=<exact-worktree-root>\n`+
 `  rcc-consortium local git plan --repo=<root> --patch=<diff> --output=<plan.json>\n`+
 `  rcc-consortium local git apply --repo=<root> --plan=<plan.json> --approve=<24-char-plan-id> [--output=<receipt.json>]\n`+
 `  rcc-consortium local context plan --repo=<root> --task=<task> [--level=inventory|task|complete|delta] [--portable] [--output=<file>]\n`+
 `  rcc-consortium local aif task|complete --repo=<root> --exe=<AIFolderFlatten.exe> --output=<parent> [--task=<task>] [--execute] [--receipt=<file>]\n`+
 `  rcc-consortium local aif verify-task|verify-complete --repo=<root> --exe=<AIFolderFlatten.exe> --bundle=<dir> [--execute] [--receipt=<file>]\n`+
 `No network, server, automatic commit, automatic stage, or automatic tab access.\n`;
}
export function runLocal(args) {
 const area=args[0], command=args[1], rest=args.slice(2);
 const repo=value(rest,'repo'); if(!repo)fail('--repo=<exact-worktree-root> is required');
 let result;
 if(area==='git'&&command==='inspect') result=inspect(repo);
 else if(area==='git'&&command==='plan'){
   if(!value(rest,'patch'))fail('Provide --patch=<diff>');
   if(!value(rest,'output'))fail('Provide --output=<plan.json>, outside the repository is recommended');
   result=patchPlan(repo,value(rest,'patch'));
 } else if(area==='git'&&command==='apply'){
   if(!value(rest,'plan'))fail('Provide --plan=<plan.json>');
   const plan=JSON.parse(readFileSync(resolve(value(rest,'plan')),'utf8'));
   result=applyPlan(repo,plan,value(rest,'approve'));
 } else if(area==='context'&&command==='plan'){
   result=contextPlan({repo,task:value(rest,'task'),level:value(rest,'level','task'),portable:has(rest,'portable')});
 } else if(area==='aif'){
   if(!['task','complete','verify-task','verify-complete'].includes(command))fail('Unknown AIF action');
   const spec=aifCommand({repo,executable:value(rest,'exe'),action:command,output:value(rest,'output'),task:value(rest,'task'),bundle:value(rest,'bundle'),chars:Number(value(rest,'budget-chars','180000'))});
   result=has(rest,'execute')?executeAif(spec):{...spec,execution:'NOT_RUN; pass --execute to launch AIFolderFlatten'};
 } else fail(localUsage());
 return writeOptional(result,rest,area==='aif'?'receipt':'output');
}
