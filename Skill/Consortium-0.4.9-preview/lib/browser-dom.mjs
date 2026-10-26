import { listTargets,CdpSession,evaluate } from '../runtime/chatgpt-pro-line/src/cdp-client.mjs';

export async function extractVisibleDom({port=9222,urlPrefix='https://chatgpt.com/',selector='pre, code, svg',limit=50}={}){
 if(!Number.isInteger(port)||port<1||port>65535)throw new Error('Invalid port');
 if(!Number.isInteger(limit)||limit<1||limit>100)throw new Error('limit must be 1..100');
 const parsed=new URL(urlPrefix);if(parsed.protocol!=='https:'||parsed.hostname!=='chatgpt.com')throw new Error('DOM extraction allowlisted to chatgpt.com only');
 const targets=await listTargets(port);const pages=targets.filter(t=>t.type==='page'&&t.webSocketDebuggerUrl&&(t.url||'').startsWith(urlPrefix));
 if(pages.length!==1)throw new Error(`Expected exactly one matching ChatGPT page, got ${pages.length}; narrow --url-prefix`);
 const cdp=await CdpSession.open(pages[0].webSocketDebuggerUrl);
 try {
 const js=`(() => {const selector=${JSON.stringify(selector)},limit=${limit};let list;try{list=Array.from(document.querySelectorAll(selector)).slice(0,limit)}catch(e){return {error:'invalid selector'}};
 const visible=e=>{const rect=e.getBoundingClientRect();const style=getComputedStyle(e);return rect.width>0&&rect.height>0&&style.visibility!=='hidden'&&style.display!=='none'&&e.getAttribute('aria-hidden')!=='true'&&!e.closest('[aria-hidden="true"]')};
 const safeSvg=e=>{const cp=e.cloneNode(true);cp.querySelectorAll('script,foreignObject,iframe,style').forEach(x=>x.remove());[cp,...cp.querySelectorAll('*')].forEach(n=>{for(const a of [...n.attributes]){if(a.name.toLowerCase().startsWith('on')||/(href|src)/i.test(a.name)&&/^(data:|https?:|javascript:)/i.test(a.value))n.removeAttribute(a.name)}});return cp.outerHTML.slice(0,20000)};
 return {url:location.origin+location.pathname,items:list.filter(e=>visible(e)&&!e.closest('input,textarea,form,[contenteditable="true"]')).map(e=>({tag:e.tagName.toLowerCase(),text:(e.tagName.toLowerCase()==='svg'?safeSvg(e):e.innerText||e.textContent||'').slice(0,20000)})).filter(x=>x.text),scope:'visible matched DOM only; no form fields or raw DOM dump'};
 })()`;
 const data=await evaluate(cdp,js);if(data?.error)throw new Error(data.error);return {ok:true,kind:'browser.dom',targetId:pages[0].id,...data};
 }finally{await cdp.close()}
}
