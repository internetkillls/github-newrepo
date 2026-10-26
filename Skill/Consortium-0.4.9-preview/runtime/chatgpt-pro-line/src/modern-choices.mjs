import { evaluate, sleep } from './cdp-client.mjs';
function failure(message) { const e = new Error(message); e.errorCode = 'model.option_unavailable'; return e; }
export async function modernState(cdp) {
  return evaluate(cdp, `(() => {
    const b = document.querySelector('button[data-selected-reasoning-effort]');
    if (!b) return null;
    return {level:b.getAttribute('data-selected-reasoning-effort'),model:document.querySelector('[data-model-selected="true"]')?.innerText.trim().split('\\n')[0] || null};
  })()`);
}
async function escape(cdp) {
  await evaluate(cdp, `document.activeElement.dispatchEvent(new KeyboardEvent('keydown',{key:'Escape',code:'Escape',bubbles:true}))`);
  await sleep(150);
}
async function open(cdp) {
  await escape(cdp);
  await evaluate(cdp, `document.querySelector('button[data-selected-reasoning-effort]').click()`);
  await sleep(350);
}
export async function readModernChoices(cdp) {
  if (!await modernState(cdp)) return null;
  try {
    await open(cdp);
    const state = await modernState(cdp);
    return {account:{detected:false},intelligence:{current:state.level,options:[]},model:{current:state.model,rootLabel:state.model,options:[]},adapter:'effort-slider'};
  } finally { await escape(cdp); }
}
export async function setModernChoices(cdp,{level,model}) {
  let before = await readModernChoices(cdp);
  for (let attempt = 0; !before && attempt < 40; attempt++) {
    await sleep(250);
    before = await readModernChoices(cdp);
  }
  if (!before) return null;
  try {
    if (model && before.model.current?.toLowerCase() !== model.toLowerCase()) {
      await open(cdp);
      const toggled = await evaluate(cdp, `(() => {const e=document.querySelector('[data-model-picker-view-toggle]');if(!e)return false;e.click();return true})()`);
      if (!toggled) throw failure('Model list toggle unavailable');
      await sleep(350);
      const selected = await evaluate(cdp, `(() => {const e=[...document.querySelectorAll('[role="menuitemradio"]')].find(e=>!e.closest('[inert]') && e.innerText.trim().split('\\n')[0].toLowerCase()===${JSON.stringify(model.toLowerCase())});if(!e || e.getAttribute('aria-disabled')==='true')return false;e.click();return true})()`);
      if (!selected) throw failure('Requested exact model is unavailable: '+model);
      await escape(cdp);
    }
    if (level && before.intelligence.current?.toLowerCase() !== level.toLowerCase()) {
      await open(cdp);
      const slider = await evaluate(cdp, `(() => {const e=document.querySelector('[data-reasoning-slider]');const s=e?.querySelector('[role="slider"]');if(!e || !s)return null;e.focus();return {min:Number(s.getAttribute('aria-valuemin')),max:Number(s.getAttribute('aria-valuemax')),value:Number(s.getAttribute('aria-valuenow'))}})()`);
      if (!slider || !Number.isFinite(slider.max) || slider.max>12) throw failure('Unsupported reasoning slider');
      const press = async key => {await evaluate(cdp, `document.querySelector('[data-reasoning-slider]').dispatchEvent(new KeyboardEvent('keydown',{key:${JSON.stringify(key)},code:${JSON.stringify(key)},bubbles:true}))`);await sleep(200);};
      for(let i=slider.min;i<slider.value;i++) await press('ArrowLeft');
      let matched=false;
      for(let i=slider.min;i<=slider.max;i++) {
        if ((await modernState(cdp))?.level === level.toLowerCase()) {matched=true;break;}
        if(i<slider.max) await press('ArrowRight');
      }
      if(!matched) {
        for(let i=slider.max;i>slider.value;i--)await press('ArrowLeft');
        throw failure('Requested reasoning level is unavailable: '+level);
      }
    }
  } finally {await escape(cdp);}
  const after = await readModernChoices(cdp);
  return {before,after,selected:{model:after.model.current,level:after.intelligence.current}};
}
