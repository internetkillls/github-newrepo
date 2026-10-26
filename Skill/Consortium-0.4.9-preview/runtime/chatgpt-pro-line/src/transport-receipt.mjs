export function sessionTargetReceipt(target){
 if(typeof target?.id!=='string'||!target.id)throw Error('transport.target_id_required');
 return {targetId:target.id,title:target.title||'',url:target.url||''};
}
