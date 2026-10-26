/** Small, opt-in by trust, Codex Stop event hook; never starts Codex or browser. */
import { armFromStopEvent } from '../lib/deferred-handoff.mjs';
let payload='';for await(const chunk of process.stdin){payload+=chunk;if(payload.length>1024*1024)break;}
try {const input=JSON.parse(payload);armFromStopEvent(input.cwd||process.cwd(),input);}
catch(error){console.error('RCC Stop hook did not arm handoff:',String(error?.message||error));}
process.stdout.write(JSON.stringify({continue:true})+'\n');
