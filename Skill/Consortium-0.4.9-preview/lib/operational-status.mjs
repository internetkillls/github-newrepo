export function operationalStatus(queue, {pidAlive=pid=>{try{process.kill(pid,0);return true}catch(e){return e.code==='EPERM'}}}={}) {
  const active=queue.jobs.filter(j=>['DISPATCHING','UNCERTAIN','TRANSPORT_RETURNED'].includes(j.status));
  const blocked=active.find(j=>j.status==='UNCERTAIN');
  const sending=active.find(j=>j.status==='DISPATCHING');
  const review=active.find(j=>j.status==='TRANSPORT_RETURNED');
  const ownerExists=Boolean(sending && queue.lock?.pid && pidAlive(queue.lock.pid));
  const status=blocked?'BLOCKED':sending?(ownerExists?'DISPATCHING':'BLOCKED_ORPHANED_DISPATCH'):review?'AWAITING_REVIEW':queue.jobs.some(j=>j.status==='PENDING')?'QUEUED':'IDLE';
  return {schema:'rcc.operational-status.v1',caseId:queue.caseId,status,
    jobId:(blocked||sending||review)?.id||null,role:(blocked||sending||review)?.role||null,
    transportProcessExists:ownerExists,generationVerified:false,schedulerActiveMeansWorkerRunning:false,
    counts:queue.jobs.reduce((a,j)=>(a[j.status]=(a[j.status]||0)+1,a),{}),
    limitation:'Process existence is not incarnation, browser generation, artifact completion or product correctness proof.'};
}
