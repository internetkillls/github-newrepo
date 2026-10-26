import test from 'node:test';import assert from 'node:assert/strict';
import {setModernChoices} from '../runtime/chatgpt-pro-line/src/modern-choices.mjs';
function fake(){const expressions=[];return {expressions,async send(method,{expression}){expressions.push(expression);return {result:{value:expression.includes('return {level:')?{level:'high',model:'Existing model'}:null}}}};}
test('already selected effort skips unavailable slider and preserves readback',async()=>{const c=fake();const r=await setModernChoices(c,{level:'high'});assert.equal(r.selected.level,'high');assert.equal(c.expressions.some(s=>s.includes('data-reasoning-slider')),false);});
test('different effort still rejects unavailable slider rather than claiming success',async()=>{const c=fake();await assert.rejects(setModernChoices(c,{level:'low'}),{errorCode:'model.option_unavailable'});assert.equal(c.expressions.some(s=>s.includes('data-reasoning-slider')),true);});
