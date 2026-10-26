import assert from 'node:assert/strict';
import { CompletionEvidence } from '../runtime/chatgpt-pro-line/src/completion-evidence.mjs';

function feed(gate, steps) {
  let result;
  for (const step of steps) result = gate.observe(step);
  return result;
}
const seq = (options = {}) => new CompletionEvidence({ stableMs: 1000, minTerminalPolls: 3, minPollSpanMs: 1000, ...options });
const active = {text:'answer',bound:true,active:true,terminal:false};
const quiet = {text:'answer',bound:true,active:false,terminal:false};
const terminal = {...quiet,terminal:true};
const tests = [];
{
 const g=seq(); const r=feed(g,[{at:0,...quiet},{at:5000,...quiet},{at:9000,...quiet},{at:10000,...quiet}]);
 assert.equal(r.completed,false);tests.push('idle-and-text-stability-alone-rejected');
}
{
 const g=seq(); const r=feed(g,[{at:0,...active},{at:1000,...quiet},{at:3000,...quiet},{at:4500,...quiet},{at:6000,...quiet},{at:7000,...quiet}]);
 assert.equal(r.completed,false);tests.push('short-idle-gap-rejected');
}
{
 const g=seq(); const r=feed(g,[{at:0,...active},{at:1000,...quiet},{at:8000,...quiet},{at:8500,...quiet},{at:9500,...quiet}]);
 assert.equal(r.completed,true);assert.equal(r.reason,'observed_active_then_stable_inactive');tests.push('active-then-sustained-quiet-accepted');
}
{
 const g=seq(); const r=feed(g,[{at:0,...active},{at:9000,...quiet},{at:9500,...active},{at:11000,...quiet},{at:12000,...quiet}]);
 assert.equal(r.completed,false);tests.push('busy-resumes-revokes-candidate');
}
{
 const g=seq(); const r=feed(g,[{at:0,...terminal},{at:2000,...terminal},{at:2700,...terminal},{at:3500,...terminal}]);
 assert.equal(r.completed,true);assert.equal(r.reason,'anchored_terminal_controls_and_stability');tests.push('fast-terminated-with-terminal-controls-accepted');
}
{
 const g=seq(); const r=feed(g,[{at:0,...active},{at:10000,...quiet,bound:false},{at:11000,...quiet,bound:false},{at:12000,...quiet,bound:false}]);
 assert.equal(r.completed,false);tests.push('unbound-message-rejected');
}
{
 const g=seq(); const r=feed(g,[{at:0,...active},{at:10000,...quiet,placeholder:true},{at:11000,...quiet,placeholder:true},{at:12000,...quiet,placeholder:true}]);
 assert.equal(r.completed,false);tests.push('progress-placeholder-rejected');
}
{
 const g=seq(); const r=feed(g,[{at:0,...active},{at:10000,...quiet},{at:11000,...quiet,active:null},{at:12000,...quiet}]);
 assert.equal(r.completed,false);tests.push('unknown-probe-resets-candidate');
}
{
 const g=seq(); const r=feed(g,[{at:0,...active},{at:10000,...quiet},{at:11000,...quiet,text:'answer more'},{at:12000,...quiet,text:'answer more'}]);
 assert.equal(r.completed,false);tests.push('late-streamed-token-resets-stability');
}
console.log(JSON.stringify({ok:true,tests},null,2));
