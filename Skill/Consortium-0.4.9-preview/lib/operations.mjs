import { mkdirSync, writeFileSync, readFileSync, existsSync, appendFileSync, renameSync, copyFileSync, chmodSync } from 'node:fs';
import { resolve, dirname } from 'node:path';
import { createHash } from 'node:crypto';

export const stamp = () => new Date().toISOString();
export function safeId(s) { const id = String(s || 'default').toLowerCase().replace(/[^a-z0-9._-]+/g,'-').replace(/^-+|-+$/g,''); return (id && id !== '.' && id !== '..') ? id : 'default'; }
export function homeDir(id) { return resolve(process.cwd(),'.devspace','rcc',safeId(id)); }
export function readText(file, maxBytes=2000000) {
 const s=readFileSync(resolve(file)); if(s.length>maxBytes)throw new Error('Input exceeds size limit'); return s.toString('utf8');
}
export function saveJson(path, data) { mkdirSync(dirname(path),{recursive:true,mode:0o700}); const tmp=`${path}.${process.pid}.tmp`;writeFileSync(tmp,JSON.stringify(data,null,2)+'\n',{mode:0o600});renameSync(tmp,path); }
export function hash(s) { return createHash('sha256').update(s).digest('hex'); }
export function tokensApprox(s) { return Math.ceil(Buffer.byteLength(String(s),'utf8')/4); }
export function event(caseId, kind, status, data={}) {
 const dir=homeDir(caseId);mkdirSync(dir,{recursive:true,mode:0o700});
 const allowed={kind,status,at:stamp(),...data}; // do not persist raw prompt, browsing credentials or DOM
 appendFileSync(resolve(dir,'events.jsonl'),JSON.stringify(allowed)+'\n',{mode:0o600});return allowed;
}
const codeFence=(lang,body)=>'```'+lang+'\n'+body+'\n```';
export function transduce(input,{source='user',caseId='default'}={}) {
 if(typeof input!=='string'||!input.trim())throw new Error('Empty task text');
 const id=safeId(caseId);const terms=['repo','code','implement','debug','deploy','test','browser','DOM','Chrome','mermaid','SVG','JSON','citation'];
 const observed=terms.filter(t=>new RegExp(`\\b${t}\\b`,'i').test(input));
 return {schema:'rcc.task-ir.v1',caseId:id,origin:{kind:source,sha256:hash(input),bytes:Buffer.byteLength(input),observedTerms:observed},
   objective:{userText:input,extraction:'verbatim; no inferred acceptance or authority'},
   router:{control:'RCC',epistemics:'Reasoning Method Controller required: pinned instructions or BLOCKED',audit:'AntiSlop required: pinned instructions or BLOCKED',independence:'choose based on dependency',cloudMode:'policy-only'},
   coding:{discussionFormat:'IR/schema/module/diff/test-first',codexDefault:['prompt-enhancement','worker-routing','deployment','testing'],codeChanges:'only when explicitly authorized'},
   evidence:{primary:'actual repository/source and reproducible probes',status:'UNVERIFIED',unknowns:[],citations:[]},
   stages:['intake','normalize','evidence','route','execute','verify','merge'],
   provenance:{thinkingMode:'unknown',privateChainOfThought:'never requested or exported'},
   limits:{noAutonomousSending:true,noImplicitRemoteServer:true,noUnboundedRetry:true},createdAt:stamp()};
}
export function promptFromIR(ir) {
 if(ir?.schema!=='rcc.task-ir.v1')throw new Error('Unsupported IR schema');
 const p=['# RCC Prompt Patch','Governing user request (verbatim):',ir.objective.userText,
 '## Routing contract','Use Reasoning Consortium Controller as the bounded router. Reasoning Method Controller and AntiSlop instructions are mandatory for every worker, follow-up and merge. Load their actual pinned instructions; if unavailable stop delegation as BLOCKED, never claim an @mention invokes them. Compile with execution packet and pass execution check before worker send.',
 'Start from the actual repository and available user evidence. State unknowns, never invent run receipts. Prefer typed task IR, JSON schemas, modules, patches, commands and tests to long natural-language coding discussions.',
 'Codex defaults to prompt refinement, worker routing, deployment and testing; do not implement repo code unless the user expressly authorizes coding. Preserve independent worker evidence boundaries; merge by source, not majority.',
 'Browser controls must be user-initiated, local loopback/dedicated profile and receipt-verified. Browser HTML/code extraction must be scoped and minimized; do not read credentials or hidden UI state.',
 'For citations export accessible sources with reference, URL, claim status and reported model/effort only when observed; never expose or claim private reasoning or token counts.',
 'Record steps and approximate tokens as heuristics, bounded retries, and recovery steps. Produce auditable post-mortem handoff rather than fabricating another AI review.',
 '## Exit gates','Return final outcome, provenance, tests, failed checks, cost estimate, follow-up/reopen condition.'];
 return p.join('\n\n')+'\n';
}
export function extractSnippets(source,{maxItems=100,maxChars=100000}={}){
 if(source.length>2000000)throw new Error('Input too large');
 const found=[];const re=/```([^\n`]*)\n([\s\S]*?)```/g;let m;
 const add=(kind,body,start,end,language='')=>{if(found.length>=maxItems)return; const t=body.slice(0,maxChars);found.push({kind,language,start,end,sha256:hash(t),text:t});};
 const aliases={mermaid:'mermaid',mmd:'mermaid',svg:'svg',json:'json',jsonc:'json',js:'javascript',javascript:'javascript',ts:'typescript',typescript:'typescript',html:'html',css:'css',py:'python',python:'python',sh:'shell',bash:'shell',sql:'sql',yaml:'yaml',yml:'yaml',xml:'xml'};
 while((m=re.exec(source))&&found.length<maxItems){const lang=m[1].trim().split(' ')[0].toLowerCase();const body=m[2];const kind=aliases[lang]||(body.trimStart().startsWith('<svg')?'svg':'code');add(kind,body,m.index,re.lastIndex,lang);}
 if(found.length===0){const trim=source.trim();if(trim.startsWith('{')||trim.startsWith('[')){try{JSON.parse(trim);add('json',trim,0,source.length,'json')}catch{}}
 const svg=/<svg\b[^>]*>[\s\S]*?<\/svg>/gi;while((m=svg.exec(source))&&found.length<maxItems)add('svg',m[0],m.index,svg.lastIndex,'svg');
 if(found.length===0&&/^(flowchart|graph|sequenceDiagram|classDiagram|stateDiagram|erDiagram|gantt)\b/.test(trim))add('mermaid',trim,0,source.length,'mermaid');}
 return {schema:'rcc.snippets.v1',count:found.length,items:found};
}
export function normalizeCitations(raw,{thinkingMode='unknown',thinkingEvidence='not-supplied'}={}) {
 let obj;try{obj=JSON.parse(raw);}catch{obj=null;}
 const candidate=Array.isArray(obj)?obj:Array.isArray(obj?.citations)?obj.citations:[];
 const items=candidate.map((c,i)=>({index:i+1,ref:String(c.ref||c.id||''),url:String(c.url||c.uri||''),title:String(c.title||''),status:String(c.status||'SOURCE-ONLY'),evidence:String(c.evidence||'provided-input')}));
 const trust=thinkingEvidence==='verified-visible-receipt'?String(thinkingMode):'unknown';
 return {schema:'rcc.citations.v1',collectedAt:stamp(),coverage:'explicitly supplied source records only',reasoning:{visibleMode:trust,evidence:thinkingEvidence,privateChainOfThought:'unavailable'},items};
}
export function toCsv(citations) {
 const cols=['index','ref','url','title','status','evidence','visibleMode'];
 const cell=x=>{const raw=String(x??''); const safe=/^[\s\x00-\x1f]*[=+@\-]/.test(raw)?"'"+raw:raw;return '"'+safe.replaceAll('"','""')+'"';}; // neutralize spreadsheet formulas
 return [cols.join(','),...citations.items.map(x=>cols.map(k=>cell(k==='visibleMode'?citations.reasoning.visibleMode:x[k])).join(','))].join('\n')+'\n';
}
export function makePostmortem(caseId){const dir=homeDir(caseId);let events=[];let state=null;const ep=resolve(dir,'events.jsonl');if(existsSync(ep))events=readText(ep,2000000).split('\n').filter(Boolean).map(s=>{try{return JSON.parse(s)}catch{return {corrupt:true}}});const st=resolve(dir,'state.json');if(existsSync(st)){try{state=JSON.parse(readText(st,2000000))}catch{state={error:'unparseable; repair required'}}};return {schema:'rcc.postmortem.v1',caseId,generatedAt:stamp(),stepCount:events.length,estimation:'byte-length / 4; not billing or API actual usage',tokensApprox:events.reduce((s,x)=>s+(x.inputTokensApprox||0)+(x.outputTokensApprox||0),0),events,stateSummary:state?{workerRoles:state.workers?.map(x=>x.role),runtime:state.runtime?.mode,corrupt:state.error||null}:null,externalReview:{performed:false,packetPrompt:'Audit only the witnessed steps and evidence: find instruction drift, unsupported runtime claims, missing guards, security boundaries and smallest regression tests. Return claim -> witness -> falsifier. Do not invent execution.'}};}
export function repairCase(caseId,{apply=false}={}) {const f=resolve(homeDir(caseId),'state.json');if(!existsSync(f))return {ok:true,status:'NO_STATE_TO_REPAIR'};try{JSON.parse(readText(f,2000000));return {ok:true,status:'HEALTHY'}}catch(err){if(!apply)return{ok:false,status:'CORRUPT',nextAction:'Repeat with --apply for non-destructive backup and state quarantine',error:String(err)};const backup=f+'.corrupt.'+Date.now()+'.bak';copyFileSync(f,backup);chmodSync(backup,0o600);renameSync(f,f+'.quarantined.'+Date.now());return{ok:true,status:'QUARANTINED',backup,nextAction:'Recreate or rebind worker rooms explicitly; no lost room IDs fabricated'}}}
