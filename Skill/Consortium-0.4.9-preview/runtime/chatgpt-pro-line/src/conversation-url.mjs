// Shared identity grammar. URL identity is not delivery, account, or action authority.
export const URL_POLICY_VERSION = 'rcc.conversation-url.v1';
const segment='[A-Za-z0-9_-]{1,256}';
const committed=new RegExp('^/(?:g/('+segment+')/)?c/('+segment+')/?$');
const newRoom=new RegExp('^/(?:g/('+segment+')/?)?$');
export function parseChatGptUrl(value){
 if(typeof value!=='string'||!value||value.length>8192||value!==value.trim()||/[\u0000-\u0020\u007f\\]/.test(value))return null;
 let u;try{u=new URL(value)}catch{return null}
 if(u.protocol!=='https:'||!['chatgpt.com','chat.openai.com'].includes(u.hostname)||u.username||u.password||u.port)return null;
 // Inspect the raw path too: URL() otherwise normalizes dot segments before validation.
 const raw=value.match(/^https:\/\/([^/?#]+)([^?#]*)/i);if(!raw||raw[1].includes('@'))return null;
 const rawPath=raw[2]||'/';
 if(rawPath.includes('%')||rawPath.split('/').some(p=>p==='.'||p==='..'))return null;
 const m=u.pathname.match(committed),fresh=u.pathname.match(newRoom);
 if(!m&&!fresh)return null;
 return Object.freeze({policyVersion:URL_POLICY_VERSION,kind:m?'conversation':'uncommitted',conversationId:m?.[2]||null,scope:m?.[1]||fresh?.[1]||null,origin:u.origin,legacy:u.hostname==='chat.openai.com',canonicalUrl:'https://chatgpt.com'+u.pathname.replace(/\/$/,'')+(u.pathname==='/'?'/':'')});
}
export function conversationIdFromUrl(value){const p=parseChatGptUrl(value);return p?.kind==='conversation'?p.conversationId:''}
export function sameConversationUrl(a,b){const x=parseChatGptUrl(a),y=parseChatGptUrl(b);return Boolean(x?.kind==='conversation'&&y?.kind==='conversation'&&x.conversationId===y.conversationId&&x.scope===y.scope)}
export function isChatGptPageUrl(value){return Boolean(parseChatGptUrl(value))}

// Duplicate metadata is ambiguity even if a saved transient target ID still matches.
export function uniqueConversationTarget(targets,url){
 const candidates=targets.filter(t=>t.type==='page'&&sameConversationUrl(t.url,url));
 if(candidates.length>1){const e=new Error('Multiple targets match the committed conversation');e.errorCode='room.target_ambiguous';e.details={candidateIds:candidates.map(t=>t.id)};throw e}
 return candidates[0]||null;
}
