import {resolve} from 'node:path';
// Only a fresh, exact invocation receipt can prove that Send was never attempted.
export function classifySubmission(receipt, {token, job, root} = {}) {
  const key=p=>process.platform==='win32'?resolve(p).toLowerCase():resolve(p);
  if (!token || receipt?.rccInvocationToken !== token || receipt.queueBinding?.jobId !== job?.id
      || receipt.queueBinding?.payloadHash !== job?.payloadHash || receipt.input?.promptSha256 !== job?.prompt?.sha256
      || !receipt.project?.repoRoot || key(receipt.project.repoRoot)!==key(root)
      || !Array.isArray(receipt.steps) || receipt.ok !== false) return 'UNKNOWN';
  if (receipt.submission?.phase !== 'NOT_ATTEMPTED' || receipt.steps.some(s=>s.step==='sent-prompt')) return 'UNKNOWN';
  if (!receipt.errorCode || !receipt.steps.some(s=>s.ok===false) && !receipt.steps.some(s=>s.step==='acquire-operation')) return 'UNKNOWN';
  return 'NOT_SENT_CONFIRMED';
}
