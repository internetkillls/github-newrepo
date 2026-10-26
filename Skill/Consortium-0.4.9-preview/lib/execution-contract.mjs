import {readFileSync,writeFileSync,mkdirSync,existsSync,statSync} from 'node:fs';
import {resolve,dirname,isAbsolute} from 'node:path';
import {createHash} from 'node:crypto';
import {fileURLToPath} from 'node:url';
export const sha256=b=>createHash('sha256').update(b).digest('hex');
const text=x=>typeof x==='string'&&x.trim().length>0&&!/^TODO\b|^<.*>$/.test(x.trim());
const fail=reason=>{throw Error('execution.contract_required: '+reason)};
const need=(ok,why)=>{if(!ok)fail(why)};
const list=(a,why)=>{need(Array.isArray(a)&&a.length>0&&a.every(text),why);return a};
const safeId=x=>typeof x==='string'&&/^[a-z0-9][a-z0-9._-]*$/i.test(x)&&!['.','..'].includes(x);
export function contractPath(root,id){need(safeId(id),'invalid case ID');return resolve(root,'.devspace/rcc',id,'execution-contract.json')}
export function loadControllers(pluginRoot){
 const manifestPath=resolve(pluginRoot,'policies/required-controllers.json');
 need(existsSync(manifestPath),'required RMC/AntiSlop source manifest missing');
 const m=JSON.parse(readFileSync(manifestPath,'utf8'));
 need(m.schema==='rcc.required-controllers.v1'&&text(m.versions?.RMC)&&text(m.versions?.AntiSlop),'invalid controller source versions');
 need(m.bundle==='RCC-REQUIRED-CONTROLLERS.zip','invalid controller bundle path');
 const bundle=resolve(pluginRoot,'policies',m.bundle);
 need(existsSync(bundle),'required RMC/AntiSlop instruction bytes unavailable');
 const b=readFileSync(bundle);need(b.length===m.bytes&&sha256(b)===m.sha256,'controller bundle hash/length mismatch');
 need(m.core==='CONTROLLER-CORE.md','pinned controller core required');const corePath=resolve(pluginRoot,'policies',m.core);need(existsSync(corePath),'actual controller core missing');const core=readFileSync(corePath);need(core.length===m.coreBytes&&sha256(core)===m.coreSha256,'controller core hash/length mismatch');
 return {...m,bundle,coreText:core.toString('utf8'),preamble:readFileSync(resolve(pluginRoot,'policies/CONTROLLER-PREAMBLE.md'),'utf8')};
}
export function controllerInstructions(pluginRoot=resolve(dirname(fileURLToPath(import.meta.url)),'..')){const c=loadControllers(pluginRoot);return `RCC mandatory controllers: RMC ${c.versions.RMC}, AntiSlop package ${c.versions.AntiSlop}; source bundle SHA256 ${c.sha256}; inline core SHA256 ${c.coreSha256}. Apply only within the task's authorization and tools. No hidden chain-of-thought or false invocation claims.\n\n${c.coreText}\n`}
export function readContract(root,id,file){
 const path=file?resolve(root,file):contractPath(root,id);need(existsSync(path),'create '+path+' with execution init, then fill the real task/evidence');
 need(statSync(path).size<=2*1024*1024,'contract too large');
 const contract=JSON.parse(readFileSync(path,'utf8'));need(contract.schema==='rcc.execution-contract.v1'&&contract.caseId===id,'contract case/schema mismatch');
 return {contract,path};
}
function fileProof(root,p){
 need(p&&text(p.path)&&Number.isInteger(p.bytes)&&p.bytes>=0&&/^[a-f0-9]{64}$/.test(p.sha256),'artifact requires exact path/length/SHA256');
 const full=resolve(root,p.path);need(existsSync(full)&&statSync(full).isFile(),'artifact unavailable: '+p.path);
 const b=readFileSync(full);need(b.length===p.bytes&&sha256(b)===p.sha256,'artifact changed/truncated: '+p.path);return full;
}
function ownedPath(p){return text(p)&&!isAbsolute(p)&&!/[\\:]/.test(p)&&!p.startsWith('/')&&!p.split('/').some(x=>['.','..','.git',''].includes(x)||/[. ]$/.test(x)||/^(con|prn|aux|nul|com[1-9]|lpt[1-9])(?:\.|$)/i.test(x))}
export function packetPrefix(c,role,controllers){
 const worker=c.workers?.find(w=>w.role===role),blind=worker?.independence==='I2';
 const dependencies=c.dependencies?.filter(d=>d.requiredBy?.includes(role)&&(!blind||d.kind==='source'));
 const functions=blind?c.functions?.map(f=>({id:f.id,action:f.action,dataOwner:f.dataOwner,states:f.states})):c.functions;
 const view={context:c.context,functions,...(!blind?{decision:c.decision}:{}),role:worker,dependencies};
 return `RCC-EXECUTION:1\nRCC-CONTROLLERS-SHA256:${controllers.sha256}\nRCC-CASE:${c.caseId}\nRCC-ROLE:${role}\nRMC:${controllers.versions.RMC}; AntiSlop:${controllers.versions.AntiSlop}\n\n${controllers.preamble.trim()}\n\nCASE CONTEXT (supplied contract, not independent evidence):\n${JSON.stringify(view,null,2)}\n\nOWNED TASK:\n`;
}
export function composePacket(root,id,role,body,pluginRoot,file){
 const {contract:c}=readContract(root,id,file);need(c.workers?.some(w=>w.role===role),'role not declared in contract');need(text(body),'empty owned task');
 return packetPrefix(c,role,loadControllers(pluginRoot))+body;
}
export function assertExecution(root,id,{pluginRoot,file,role,prompt,stage='dispatch'}={}){
 const {contract:c,path}=readContract(root,id,file);const controllers=loadControllers(pluginRoot);
 need(['dispatch','matrix','closure','release'].includes(stage),'invalid execution stage');
 need(c.controllers?.sha256===controllers.sha256,'pin the current required controller bundle in the case contract');
 for(const k of ['generalStory','humanEpisode','goal','sourceIdentity'])need(text(c.context?.[k]),'missing causal context: '+k);
 need(['observed','user_report','scenario','not_applicable'].includes(c.context.episodeOrigin),'classify the user episode origin');
 if(c.context.episodeOrigin==='not_applicable')need(text(c.context.episodeReason),'reason needed for non-human-task context');
 need(['general','software-ui'].includes(c.profile),'choose relevant execution profile');
 need(Array.isArray(c.functions)&&c.functions.length>0,'map atomic functions before design');
 for(const f of c.functions){for(const k of ['id','action','dataOwner','representation','precedentOrReason'])need(text(f[k]),'incomplete atomic function: '+k);list(f.states,'function states required');}
 for(const k of ['chosen','rival','tradeoff','falsifier'])need(text(c.decision?.[k]),'decision/rival/falsifier required: '+k);
 need(Array.isArray(c.workers)&&c.workers.length>0,'WBS roles/deliverables required');
 need(new Set(c.workers.map(w=>w.role)).size===c.workers.length,'duplicate role');
 const ownership=new Map();
 for(const w of c.workers){
  need(safeId(w.role)&&text(w.room)&&['I0','I1','I2','I3','I4'].includes(w.independence),'role/room/independence required');
  for(const k of ['deliverable','exitTest','forbiddenMoves'])need(text(w[k]),'role deliverable/exit/limits missing');
  need(Array.isArray(w.ownedPaths),'declare exact ownership or empty array');
  for(const p of w.ownedPaths){need(ownedPath(p),'unsafe/wildcard ownership path');need(!/[?*]/.test(p),'ownership must be exact');const key=p.toLowerCase();need(!ownership.has(key),'overlapping ownership: '+p);ownership.set(key,w.role);}
 }
 need(Number.isInteger(c.maxActive)&&c.maxActive>0,'positive user-scoped active-worker cap required');
 need(Array.isArray(c.activeRoles)&&new Set(c.activeRoles).size===c.activeRoles.length&&c.activeRoles.every(r=>c.workers.some(w=>w.role===r)),'invalid active role ledger');
 need(c.transport?.uncertainPolicy==='reconcile_never_resend'&&c.transport.completion==='anchored_affirmative_terminal'&&c.transport.mutations==='serialized','mandatory completion/no-resend/lock rules required');
 need(text(c.transport.deliveryProbe)&&text(c.transport.receiverAck),'artifact transport probe and receiver acknowledgment required');
 need(Array.isArray(c.transport.uncertainRoles),'declare uncertain role ledger');
 need(Number.isInteger(c.recovery?.maxAttempts)&&c.recovery.maxAttempts>=0&&text(c.recovery.stopCondition)&&text(c.recovery.runnerOwnership),'bounded recovery/runner ownership required');
 need(Array.isArray(c.dependencies)&&Array.isArray(c.boundaries),'dependency and cross-owner boundary lists required');
 for(const d of c.dependencies){
  need(['source','closure'].includes(d.kind)&&Array.isArray(d.requiredBy)&&d.requiredBy.length>0&&d.requiredBy.every(r=>c.workers.some(w=>w.role===r)),'dependency kind/recipient scope missing');
  if(role&&!d.requiredBy.includes(role))continue;
  if(role&&c.workers.find(w=>w.role===role)?.independence==='I2')need(d.kind==='source','blind role cannot receive producer closures');
  fileProof(root,d);list(d.requiredSections,'dependency sections required');need(Array.isArray(d.sectionAck)&&d.requiredSections.every(s=>d.sectionAck.includes(s)),'required predecessor sections unread');need(Array.isArray(d.receivedBy)&&(role?d.receivedBy.includes(role):d.requiredBy.every(r=>d.receivedBy.includes(r))),'successor receipt acknowledgment missing');need(text(d.evidenceScope),'predecessor evidence scope missing');
 }
 for(const b of c.boundaries){for(const k of ['id','action','stateOwner','allowed','forbidden','negativeControl','witnessOrDebt'])need(text(b[k]),'cross-owner boundary incomplete: '+k);need(Array.isArray(b.owners)&&b.owners.length>1&&b.owners.every(r=>c.workers.some(w=>w.role===r)),'boundary owners missing');}
 if(role){need(c.workers.some(w=>w.role===role),'unknown worker role');need(!c.activeRoles.includes(role)&&c.activeRoles.length<c.maxActive,'active cap/role already running');need(!(c.transport.uncertainRoles||[]).includes(role),'uncertain submission must reconcile, never resend');need(typeof prompt==='string'&&prompt.startsWith(packetPrefix(c,role,controllers)),'compile the actual mandatory controller packet; @mentions alone are insufficient');}
 need(c.measurement&&text(c.measurement.metric)&&text(c.measurement.baselineOrDebt)&&text(c.measurement.candidateOrDebt),'before/after measurement plan or explicit debt required');
 need(Array.isArray(c.claims),'typed evidence claims required');
 for(const claim of c.claims){need(text(claim.id)&&text(claim.claim)&&text(claim.requiredLevel),'claim scope/evidence requirement missing');need(['planned','observed','unverified'].includes(claim.status),'invalid claim status');if(claim.status==='observed'){need(claim.level===claim.requiredLevel,'fixture/self-report cannot satisfy native/human evidence');fileProof(root,claim.evidence);}if(stage==='release')need(claim.status==='observed','release claim still unverified');}
 if(c.profile==='software-ui'&&(stage==='matrix'||stage==='release'||stage==='closure'&&c.statuses?.behavior==='SCOPED_PASS')){
  need(c.verticalJourney?.status==='observed'&&c.verticalJourney.level==='native','native vertical journey required before matrix/behavior closure');fileProof(root,c.verticalJourney.evidence);
 }
 need(c.statuses&&['NOT_STARTED','DELIVERED','UNCERTAIN','FAILED'].includes(c.statuses.transport)&&['PENDING','COMPLETE','PARTIAL','BLOCKED'].includes(c.statuses.artifact)&&['UNVERIFIED','SCOPED_PASS','BLOCKED'].includes(c.statuses.behavior)&&['NOT_REQUESTED','BLOCKED','READY'].includes(c.statuses.release),'separate transport/artifact/behavior/release statuses required');
 if(['closure','release'].includes(stage)){
  const cl=c.closure;need(cl&&Array.isArray(cl.debts)&&text(cl.reopenCondition),'closure debts/reopen condition required');
  if(c.profile==='software-ui'&&c.verticalJourney?.status!=='observed')need(text(c.verticalJourney?.reason)&&cl.debts.length>0,'retain explicit missing-native debt while closing delivered artifacts');
  need(['complete','partial','unavailable','not_applicable'].includes(cl.interviews?.status),'postproject interviews or explicit unavailable status required');
  if(cl.interviews.status!=='complete')need(text(cl.interviews.reason),'explain missing/partial interview evidence');
  need(cl.interviews.independence==='I0'&&cl.interviews.humanFeedback===false,'AI interviews cannot count as independent/human evidence');
  need(text(cl.materialsIndex),'retained material/provenance index required');fileProof(root,cl.materials);
  need(Array.isArray(cl.controllerReviews)&&cl.controllerReviews.length===c.workers.length,'review every worker against actual RMC/AntiSlop checks');
  for(const w of c.workers){const r=cl.controllerReviews.find(r=>r.role===w.role);need(r&&r.controllerSha256===controllers.sha256&&text(r.evidenceBackedFinding)&&text(r.negativeControl)&&text(r.residual),'controller review missing, names alone insufficient');fileProof(root,r.evidence);}
 }
 if(stage==='release')need(c.statuses.release==='READY'&&c.statuses.behavior==='SCOPED_PASS'&&c.statuses.artifact==='COMPLETE'&&c.statuses.transport==='DELIVERED','release remains blocked; retain valid delivered artifacts without reintegration');
 return {ok:true,status:'STRUCTURAL_PRECONDITIONS_MET_REVIEW_REQUIRED',stage,caseId:id,role:role||null,contractPath:path,controllerBundle:controllers.bundle,controllerSha256:controllers.sha256,release:c.statuses.release,limits:'File identity and declared preconditions only; not semantic compliance, native/human truth, or model determinism'};
}
export function initContract(root,id,pluginRoot){
 const path=contractPath(root,id);need(!existsSync(path),'refuse overwriting an existing case contract');
 const c=JSON.parse(readFileSync(resolve(pluginRoot,'assets/execution-contract.template.json'),'utf8'));c.caseId=id;c.controllers.sha256=loadControllers(pluginRoot).sha256;
 mkdirSync(dirname(path),{recursive:true});writeFileSync(path,JSON.stringify(c,null,2)+'\n',{flag:'wx',mode:0o600});return {ok:true,path,status:'DRAFT_NOT_EXECUTABLE'};
}
