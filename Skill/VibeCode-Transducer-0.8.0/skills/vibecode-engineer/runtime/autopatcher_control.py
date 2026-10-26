"""VCT private control-plane core, independent of MCP transport.

All API methods require a signed assertion minted by an independently trusted
auth gateway. These functions do not host or install an authorization server.
No token issuer or patch-executing method is exposed to the MCP client.
"""
from __future__ import annotations
import hashlib
import hmac
import re
import time
from autopatcher_core import JobStore, GateError, canonical, digest, validate_spec


def gateway_sign(fields:dict, gateway_key:bytes)->dict:
    """Only for the trusted gateway, NEVER exposed through MCP."""
    if not isinstance(gateway_key,bytes) or len(gateway_key)<32:
        raise GateError('INVALID_GATEWAY_KEY','gateway secret must be >=32 bytes')
    return {'fields':fields, 'mac':hmac.new(gateway_key,canonical(fields),hashlib.sha256).hexdigest()}


def gateway_verify(assertion:dict,key:bytes,*,action:str,body_hash:str,repo_id:str)->dict:
    if not isinstance(assertion,dict) or not isinstance(assertion.get('fields'),dict):
        raise GateError('UNAUTHENTICATED','gateway assertion required')
    fields=assertion['fields'];mac=assertion.get('mac','')
    if not isinstance(key,bytes) or len(key)<32 or not isinstance(mac,str):
        raise GateError('UNAUTHENTICATED','gateway configuration invalid')
    if not hmac.compare_digest(hmac.new(key,canonical(fields),hashlib.sha256).hexdigest(),mac):
        raise GateError('UNAUTHENTICATED','invalid gateway assertion')
    if fields.get('audience')!='vct-autopatcher-control-v1' or fields.get('action')!=action:
        raise GateError('UNAUTHORIZED','wrong audience or action')
    if fields.get('repo_id')!=repo_id or fields.get('body_hash')!=body_hash:
        raise GateError('UNAUTHORIZED','request payload or repository not covered')
    if not isinstance(fields.get('subject'),str) or not fields['subject'].strip():
        raise GateError('UNAUTHENTICATED','missing authenticated subject')
    if not isinstance(fields.get('expires_at'),(float,int)) or time.time()>=fields['expires_at']:
        raise GateError('UNAUTHENTICATED','assertion expired')
    return fields


class ControlPlane:
    def __init__(self,store:JobStore,registry:dict,gateway_key:bytes):
        self.store=store;self.registry=registry;self.gateway_key=gateway_key

    def submit_patch_job(self,spec:dict,idempotency_key:str,assertion:dict):
        validate_spec(spec)
        repo_id=spec['repo_id']
        gateway_verify(assertion,self.gateway_key,action='submit',
                       body_hash=digest({'spec':spec,'idempotency_key':idempotency_key}),repo_id=repo_id)
        if repo_id not in self.registry:
            raise GateError('REPO_NOT_ALLOWLISTED','no operator-owned repo identity')
        result=self.store.submit(spec,idempotency_key)
        return {'job_id':result['job_id'],'state':result['state'],'replayed':result['replayed'],
                'mutation_performed':False,'worker_required':True}

    def _read_guard(self,jid:str,assertion:dict,action:str):
        spec=self.store.spec(jid)
        gateway_verify(assertion,self.gateway_key,action=action,body_hash=digest({'job_id':jid}),repo_id=spec['repo_id'])

    def get_job_status(self,jid:str,assertion:dict):
        self._read_guard(jid,assertion,'status')
        return self.store.status(jid)

    def get_job_receipt(self,jid:str,assertion:dict):
        self._read_guard(jid,assertion,'receipt')
        return {'job_id':jid,'receipt':self.store.receipt(jid)}

    def cancel_queued_job(self,jid:str,assertion:dict):
        self._read_guard(jid,assertion,'cancel')
        return self.store.cancel(jid)


def capability_report():
    return {'module':'vct-private-control/0.8.0','authentication':'INDEPENDENT_HMAC_GATEWAY_ASSERTION_REQUIRED',
            'signed_issuer_exposed_to_mcp':False,'methods':['submit_patch_job','get_job_status','get_job_receipt','cancel_queued_job'],
            'worker_execution':'SEPARATE_TRUSTED_WORKER_NOT_MCP_REQUEST',
            'mcp_sdk_connected':False,'remote_auth_gateway_installed':False,'production_access':False}
