import { existsSync } from 'node:fs';
import { resolve,dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const nodeOk=Number(process.versions.node.split('.')[0])>=20;
const files=['plugin.json','bin/rcc-consortium','runtime/chatgpt-pro-line/src/cdp-client.mjs','skills/reasoning-consortium/SKILL.md'];
const checks={node:process.versions.node,nodeOk,platform:process.platform,files:Object.fromEntries(files.map(f=>[f,existsSync(resolve(root,f))])),chromePathEnv:!!process.env.CHROME_PATH,chromeProfilePolicy:'dedicated, loopback-only'};
checks.ok=nodeOk&&Object.values(checks.files).every(Boolean);
console.log(JSON.stringify(checks,null,2));if(!checks.ok)process.exitCode=1;
