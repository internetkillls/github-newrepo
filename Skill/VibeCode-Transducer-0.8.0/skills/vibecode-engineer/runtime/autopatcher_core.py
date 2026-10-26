#!/usr/bin/env python3
"""VCT autonomous patching control-plane *beta* with fail-closed test scope.

Operational scope: signed policy, pinned-Git-source snapshot, SQLite job/event
ledger, baseline red and after green on a trusted JSON assertion fixture, and
an exact bounded change in an ephemeral snapshot. No arbitrary project code,
network, hosted MCP, Git push, CI, or deployment is performed.

A real target test suite requires an independently attested sandbox worker and
is explicitly UNSUPPORTED here. Signing authority must be outside model tools.
"""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from contextlib import contextmanager
from datetime import datetime, timezone
import fnmatch
import hashlib
import hmac
import io
import json
import os
import re
import sqlite3
import subprocess
import tarfile
import tempfile
import time
import uuid

MAX_PATCH_BYTES=100_000
MAX_ARCHIVE_BYTES=5_000_000
MAX_ARCHIVE_FILES=1000
MAX_PAYLOAD_BYTES=80_000
SHA_RE=re.compile(r'^[0-9a-f]{40}$')
SHA256_RE=re.compile(r'^[0-9a-f]{64}$')

class GateError(ValueError):
    def __init__(self, code:str, detail:str):
        self.code=code
        super().__init__(f'{code}: {detail}')


def canonical(obj)->bytes:
    return json.dumps(obj,sort_keys=True,ensure_ascii=False,allow_nan=False,separators=(',',':')).encode('utf-8')

def digest(obj)->str:
    return hashlib.sha256(obj if isinstance(obj,bytes) else canonical(obj)).hexdigest()

def path_ok(value, *, protected=True)->str:
    if not isinstance(value,str) or not value or len(value)>180 or '\\' in value or '\x00' in value:
        raise GateError('UNSAFE_PATH','invalid file path')
    parts=value.split('/')
    if any(x in ('','.','..') for x in parts) or value.startswith('/') or re.match(r'^[A-Za-z]:',value):
        raise GateError('UNSAFE_PATH','absolute, escaping or noncanonical path')
    if protected and (parts[0] in {'.git','.github','.vct','tests','test','secrets'} or
        any(x.startswith('.env') for x in parts) or
        re.search(r'(^|/)(test_[^/]*|[^/]+\.(?:test|spec)\.[^/]+)$',value)):
        raise GateError('PROTECTED_PATH',value)
    if PurePosixPath(value).suffix not in {'.json','.py','.ts','.tsx','.js','.jsx','.md','.yaml','.yml','.html','.css','.sql'}:
        raise GateError('UNSUPPORTED_FILE_TYPE',value)
    return value


def _git(root:Path,*args)->str:
    p=subprocess.run(['git','-C',str(root),'-c','core.hooksPath=/dev/null',*args],
                     capture_output=True,text=True,timeout=12,check=False,
                     env={**os.environ,'GIT_CONFIG_NOSYSTEM':'1','GIT_OPTIONAL_LOCKS':'0'})
    if p.returncode:
        raise GateError('GIT_PREFLIGHT_FAILED',(p.stderr or p.stdout)[:250])
    return p.stdout.strip()


def repo_preflight(root:Path,base_sha:str)->dict:
    if not isinstance(base_sha,str) or not SHA_RE.fullmatch(base_sha):
        raise GateError('INVALID_SHA','requires full 40-char SHA')
    if root.is_symlink() or not root.is_dir():raise GateError('UNTRUSTED_REPOSITORY','root not real directory')
    root=root.resolve(strict=True)
    top=Path(_git(root,'rev-parse','--show-toplevel')).resolve()
    if top!=root:raise GateError('WRONG_REPO_ROOT','root is not repository toplevel')
    head=_git(root,'rev-parse','HEAD')
    if head!=base_sha:raise GateError('STALE_COMMIT',f'expected {base_sha}, current {head}')
    if _git(root,'status','--porcelain','--untracked-files=all'):
        raise GateError('DIRTY_REPOSITORY','source repository has modifications')
    tree=_git(root,'ls-tree','-r','HEAD')
    for line in tree.splitlines():
        # Symlinks and gitlinks cannot be rendered into our isolated snapshot.
        if line.startswith('120000 ') or line.startswith('160000 '):
            raise GateError('UNSAFE_GIT_ENTRY','symlink or submodule in source')
    if (root/'.gitmodules').exists():raise GateError('SUBMODULE_POLICY_REQUIRED','submodules not enabled')
    return {'base_sha':head,'root':str(root),'tree_sha':_git(root,'rev-parse','HEAD^{tree}'),'status':'VERIFIED_LOCAL_GIT_SNAPSHOT_SOURCE'}


@contextmanager
def verified_snapshot(root:Path,base_sha:str):
    """Pin an immutable commit into disposable regular files; NOT an executing sandbox."""
    preflight=repo_preflight(root,base_sha)
    # archive output is bounded; do not run checkout filters or git hooks.
    p=subprocess.run(['git','-C',str(root),'archive','--format=tar',base_sha],
                     stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=15,check=False)
    if p.returncode:raise GateError('GIT_ARCHIVE_FAILED',p.stderr.decode(errors='replace')[:160])
    if len(p.stdout)>MAX_ARCHIVE_BYTES:raise GateError('SNAPSHOT_TOO_LARGE','archive exceeds beta limit')
    with tempfile.TemporaryDirectory(prefix='vct-pinned-') as temp:
        out=Path(temp)
        with tarfile.open(fileobj=io.BytesIO(p.stdout),mode='r:') as tar:
            items=tar.getmembers()
            if len(items)>MAX_ARCHIVE_FILES:raise GateError('SNAPSHOT_TOO_LARGE','too many members')
            total=0
            for m in items:
                if m.isdir():continue
                if not m.isfile():raise GateError('UNSAFE_ARCHIVE_ENTRY','links/special entries unsupported')
                relative=path_ok(m.name,protected=False)
                total+=m.size
                if total>MAX_ARCHIVE_BYTES:raise GateError('SNAPSHOT_TOO_LARGE','unpacked source too large')
                path=out/relative
                path.parent.mkdir(parents=True,exist_ok=True)
                with tar.extractfile(m) as read:
                    data=read.read(MAX_ARCHIVE_BYTES+1)
                if len(data)!=m.size:raise GateError('ARCHIVE_CORRUPT',relative)
                path.write_bytes(data)
                path.chmod(0o600)
        yield out,preflight


def sign_grant(fields:dict, signing_key:bytes)->dict:
    """TRUSTED OPERATOR ONLY; never expose via MCP or model-accessible tool."""
    if not isinstance(signing_key,bytes) or len(signing_key)<32:
        raise GateError('SIGNING_KEY_INVALID','operator-owned key >=32 bytes required')
    blob=canonical(fields)
    return {'fields':fields,'mac':hmac.new(signing_key,blob,hashlib.sha256).hexdigest()}


def verify_grant(grant:dict,key:bytes,*,job_id:str,repo_id:str,base_sha:str,path:str,patch_hash:str,now:float|None=None)->dict:
    if not isinstance(grant,dict) or not isinstance(grant.get('fields'),dict):
        raise GateError('GRANT_REQUIRED','signed grant missing')
    f=grant['fields']; mac=grant.get('mac','')
    if not isinstance(mac,str) or not SHA256_RE.fullmatch(mac) or not isinstance(key,bytes) or len(key)<32:
        raise GateError('GRANT_INVALID','invalid MAC or configured signing key')
    calc=hmac.new(key,canonical(f),hashlib.sha256).hexdigest()
    if not hmac.compare_digest(calc,mac):raise GateError('GRANT_INVALID','MAC mismatch')
    for k,v in [('job_id',job_id),('repo_id',repo_id),('base_sha',base_sha),('patch_hash',patch_hash)]:
        if f.get(k)!=v:raise GateError('GRANT_SCOPE_MISMATCH',k)
    if f.get('operation')!='apply_isolated' or path not in f.get('permitted_paths',[]):
        raise GateError('GRANT_SCOPE_MISMATCH','operation or path')
    if not isinstance(f.get('expires_at'),(float,int)) or (now or time.time())>=f['expires_at']:
        raise GateError('GRANT_EXPIRED','expiry passed')
    if not isinstance(f.get('nonce'),str) or len(f['nonce'])<12:
        raise GateError('GRANT_INVALID','nonce missing')
    if f.get('policy_version')!='vct-autopatch-policy-1':
        raise GateError('GRANT_INVALID','wrong policy revision')
    return f


class JobStore:
    """SQLite WAL, unique idempotency, chained append-only event payloads."""
    def __init__(self,path:Path):
        self.path=Path(path)
        self.path.parent.mkdir(parents=True,exist_ok=True)
        self.db=sqlite3.connect(str(self.path),timeout=10,isolation_level=None)
        self.db.execute('PRAGMA journal_mode=WAL')
        self.db.execute('PRAGMA busy_timeout=10000')
        self.db.execute('''CREATE TABLE IF NOT EXISTS jobs(id TEXT PRIMARY KEY,idempotency TEXT UNIQUE NOT NULL,
         spec_hash TEXT NOT NULL, spec_json TEXT NOT NULL,state TEXT NOT NULL,updated REAL NOT NULL)''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS events(seq INTEGER PRIMARY KEY AUTOINCREMENT,
         job_id TEXT NOT NULL,kind TEXT NOT NULL,payload TEXT NOT NULL,prev_hash TEXT NOT NULL,
         event_hash TEXT NOT NULL,created REAL NOT NULL)''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS consumed_grants(nonce TEXT PRIMARY KEY,job_id TEXT NOT NULL)''')
        self.db.execute('''CREATE TABLE IF NOT EXISTS receipts(job_id TEXT PRIMARY KEY, body TEXT NOT NULL,sha256 TEXT NOT NULL)''')

    def submit(self,spec:dict,idempotency:str)->dict:
        if not isinstance(idempotency,str) or not re.fullmatch(r'[A-Za-z0-9_-]{8,100}',idempotency):
            raise GateError('INVALID_IDEMPOTENCY','bounded nonsecret key required')
        if not isinstance(spec,dict) or len(canonical(spec))>MAX_PAYLOAD_BYTES:
            raise GateError('INVALID_JOB','bounded JSON object expected')
        validate_spec(spec)
        self.db.execute('BEGIN IMMEDIATE')
        try:
            row=self.db.execute('SELECT id,spec_hash,state FROM jobs WHERE idempotency=?',(idempotency,)).fetchone()
            if row:
                if row[1]!=digest(spec):raise GateError('IDEMPOTENCY_CONFLICT','same key different request')
                self.db.execute('COMMIT')
                return {'job_id':row[0],'state':row[2],'replayed':True}
            jid='job_'+uuid.uuid4().hex
            self.db.execute('INSERT INTO jobs VALUES (?,?,?,?,?,?)',(jid,idempotency,digest(spec),canonical(spec).decode(),'REQUESTED',time.time()))
            self._event_tx(jid,'SUBMITTED',{'spec_hash':digest(spec)})
            self.db.execute('COMMIT')
            return {'job_id':jid,'state':'REQUESTED','replayed':False}
        except Exception:
            self.db.execute('ROLLBACK');raise

    def _event_tx(self,jid,kind,payload):
        previous=self.db.execute('SELECT event_hash FROM events WHERE job_id=? ORDER BY seq DESC LIMIT 1',(jid,)).fetchone()
        prev=previous[0] if previous else '0'*64
        packet={'job_id':jid,'kind':kind,'payload':payload,'prev_hash':prev}
        eh=digest(packet)
        self.db.execute('INSERT INTO events(job_id,kind,payload,prev_hash,event_hash,created) VALUES(?,?,?,?,?,?)',
                        (jid,kind,canonical(payload).decode(),prev,eh,time.time()))
        return eh

    def transition(self,jid,from_state,to_state,event):
        self.db.execute('BEGIN IMMEDIATE')
        try:
            r=self.db.execute('SELECT state FROM jobs WHERE id=?',(jid,)).fetchone()
            if not r or r[0]!=from_state:raise GateError('INVALID_TRANSITION',f'{r} to {to_state}')
            self.db.execute('UPDATE jobs SET state=?,updated=? WHERE id=?',(to_state,time.time(),jid))
            h=self._event_tx(jid,to_state,event)
            self.db.execute('COMMIT')
            return h
        except Exception:
            self.db.execute('ROLLBACK');raise

    def consume_grant(self,nonce,jid):
        self.db.execute('BEGIN IMMEDIATE')
        try:
            self.db.execute('INSERT INTO consumed_grants VALUES(?,?)',(nonce,jid))
            self._event_tx(jid,'GRANT_CONSUMED',{'nonce_digest':digest(nonce.encode())})
            self.db.execute('COMMIT')
        except sqlite3.IntegrityError:
            self.db.execute('ROLLBACK');raise GateError('GRANT_REPLAY','nonce already consumed')
        except Exception:
            self.db.execute('ROLLBACK');raise

    def status(self,jid):
        r=self.db.execute('SELECT id,state,spec_hash,updated FROM jobs WHERE id=?',(jid,)).fetchone()
        if not r:return None
        return {'job_id':r[0],'state':r[1],'spec_hash':r[2],'updated':r[3]}

    def spec(self,jid):
        row=self.db.execute('SELECT spec_json FROM jobs WHERE id=?',(jid,)).fetchone()
        if not row:raise GateError('JOB_NOT_FOUND','unknown job id')
        return json.loads(row[0])

    def events(self,jid):
        rows=self.db.execute('SELECT kind,payload,prev_hash,event_hash FROM events WHERE job_id=? ORDER BY seq',(jid,)).fetchall()
        return [{'kind':k,'payload':json.loads(p),'prev_hash':ph,'event_hash':eh} for k,p,ph,eh in rows]

    def verify_chain(self,jid):
        last='0'*64
        for e in self.events(jid):
            if e['prev_hash']!=last:return False
            expect=digest({'job_id':jid,'kind':e['kind'],'payload':e['payload'],'prev_hash':last})
            if expect!=e['event_hash']:return False
            last=e['event_hash']
        return True

    def save_receipt(self,jid:str,receipt:dict):
        if self.status(jid) is None:raise GateError('JOB_NOT_FOUND','cannot save receipt')
        body=canonical(receipt)
        self.db.execute('BEGIN IMMEDIATE')
        try:
            self.db.execute('INSERT INTO receipts VALUES(?,?,?)',(jid,body.decode(),digest(body)))
            self._event_tx(jid,'RECEIPT_STORED',{'receipt_sha256':digest(body)})
            self.db.execute('COMMIT')
        except Exception:
            self.db.execute('ROLLBACK');raise

    def receipt(self,jid:str):
        row=self.db.execute('SELECT body,sha256 FROM receipts WHERE job_id=?',(jid,)).fetchone()
        if not row:return None
        data=json.loads(row[0]);return data if digest(data)==row[1] else {'integrity_error':'RECEIPT_TAMPERED'}

    def cancel(self,jid:str):
        status=self.status(jid)
        if status is None:raise GateError('JOB_NOT_FOUND','cannot cancel')
        if status['state']!='REQUESTED':raise GateError('CANNOT_CANCEL_RUNNING_JOB','requires worker cancellation protocol')
        self.transition(jid,'REQUESTED','CANCELLED',{'reason':'USER_REQUESTED_BEFORE_WORKER'})
        return self.status(jid)

    def close(self):self.db.close()


def validate_spec(spec:dict)->dict:
    """Non-executable typed canary fixture; no user-supplied test commands."""
    if not isinstance(spec,dict):raise GateError('INVALID_JOB','object required')
    if set(spec)!={'repo_id','base_sha','patch','test'}:
        raise GateError('INVALID_JOB','only explicitly typed keys permitted; no embedded credentials or commands')
    for k in ('repo_id','base_sha','patch','test'):
        if k not in spec:raise GateError('INVALID_JOB',k)
    if not isinstance(spec['repo_id'],str) or not re.fullmatch(r'[a-zA-Z0-9_/-]{4,100}',spec['repo_id']):
        raise GateError('INVALID_REPO_ID','explicit registry-bound identity required')
    if not SHA_RE.fullmatch(str(spec['base_sha'])):raise GateError('INVALID_SHA','bad base')
    patch=spec['patch']; test=spec['test']
    if not isinstance(patch,dict) or not isinstance(test,dict):raise GateError('INVALID_JOB','patch/test objects needed')
    if set(patch)!={'path','old','new','expected_sha256'} or set(test)!={'kind','id','path','pointer','expected'}:
        raise GateError('INVALID_JOB','unsupported field in patch/test, including commands')
    path=path_ok(patch.get('path')); path_ok(test.get('path'),protected=False)
    if path!=test['path']:raise GateError('TEST_SCOPE_MISMATCH','fixture must measure changed file')
    if not isinstance(patch.get('expected_sha256'),str) or not SHA256_RE.fullmatch(patch['expected_sha256']):raise GateError('INVALID_PATCH','expected SHA256')
    if not all(isinstance(patch.get(k),str) and patch[k] for k in ('old','new')) or patch['old']==patch['new']:
        raise GateError('INVALID_PATCH','nonempty distinct text edits')
    if len(patch['old'].encode())+len(patch['new'].encode())>MAX_PATCH_BYTES:raise GateError('PATCH_TOO_LARGE','patch over limit')
    if test.get('kind')!='json_value' or not isinstance(test.get('id'),str) or not re.fullmatch(r'[A-Za-z0-9_.-]{3,100}',test['id']):
        raise GateError('UNSUPPORTED_TEST','only nonexecuting json_value fixture supported')
    if not test['path'].endswith('.json') or not isinstance(test.get('pointer'),str) or not test['pointer'].startswith('/') or len(test['pointer'])>200:
        raise GateError('UNSUPPORTED_TEST','JSON pointer required')
    if test.get('expected') not in (True,False,None) and not isinstance(test.get('expected'),(int,float,str)):
        raise GateError('UNSUPPORTED_TEST','simple scalar expected')
    return spec


def inspect_fixture(root:Path,test:dict)->dict:
    relative=path_ok(test['path'],protected=False)
    target=root/relative
    if target.is_symlink() or not target.is_file():raise GateError('UNSAFE_TEST_PATH','not ordinary file')
    if target.stat().st_size>MAX_PATCH_BYTES:raise GateError('TEST_FILE_TOO_LARGE','fixture over limit')
    try:obj=json.loads(target.read_text())
    except (OSError,ValueError) as e:raise GateError('INVALID_TEST_DATA',str(e))
    key_path=test['pointer'].split('/')[1:]
    try:
        for k in key_path:
            k=k.replace('~1','/').replace('~0','~')
            obj=obj[int(k)] if isinstance(obj,list) else obj[k]
    except (KeyError,IndexError,ValueError,TypeError):
        return {'test_id':test['id'],'status':'FAIL','failure_signature':'JSON_POINTER_NOT_FOUND',
                'test_spec_sha256':digest(test),'actual_sha256':None}
    ok=type(obj)==type(test['expected']) and obj==test['expected']
    return {'test_id':test['id'],'status':'PASS' if ok else 'FAIL',
            'failure_signature':None if ok else 'VALUE_MISMATCH',
            'test_spec_sha256':digest(test),'actual_sha256':digest(obj)}


def apply_exact(root:Path,patch:dict)->dict:
    path=path_ok(patch['path'])
    target=root/path
    if target.is_symlink() or not target.is_file():raise GateError('UNSAFE_PATCH_PATH','file not regular')
    if target.stat().st_size>MAX_PATCH_BYTES:raise GateError('PATCH_TOO_LARGE','file too large')
    original=target.read_bytes()
    if digest(original)!=patch['expected_sha256']:raise GateError('STALE_FILE_HASH','pre-image mismatch')
    try:before=original.decode('utf-8')
    except UnicodeDecodeError:raise GateError('UNSUPPORTED_PATCH','only UTF8')
    if before.count(patch['old'])!=1:raise GateError('AMBIGUOUS_EDIT','old span must occur exactly once')
    after=before.replace(patch['old'],patch['new'],1).encode('utf-8')
    fd,tmp=tempfile.mkstemp(dir=str(target.parent),prefix='.vct-snapshot-patch-')
    try:
        with os.fdopen(fd,'wb') as f:f.write(after);f.flush();os.fsync(f.fileno())
        os.replace(tmp,target)
    finally:
        if os.path.exists(tmp):os.unlink(tmp)
    return {'path':path,'before_sha256':digest(original),'after_sha256':digest(after)}


def run_canary_job(store:JobStore,jid:str,registry:dict,grant:dict,key:bytes)->dict:
    """Trusted operator worker; allowed to modify ONLY a disposable Git snapshot."""
    spec=validate_spec(store.spec(jid))
    if store.status(jid)['state']!='REQUESTED':raise GateError('INVALID_TRANSITION','job already processed')
    repo=registry.get(spec['repo_id'])
    if not isinstance(repo,dict) or not repo.get('trusted_for_canary'):
        store.transition(jid,'REQUESTED','DENIED',{'reason':'REPO_NOT_ALLOWLISTED'})
        return {'job_id':jid,'state':'DENIED','reason':'REPO_NOT_ALLOWLISTED'}
    patch=spec['patch']; patch_hash=digest(patch)
    try:
        grant_fields=verify_grant(grant,key,job_id=jid,repo_id=spec['repo_id'],
                     base_sha=spec['base_sha'],path=patch['path'],patch_hash=patch_hash)
        if patch['path'] not in repo.get('permitted_paths',[]):
            raise GateError('REPO_POLICY_DENIED','path not in operator registry')
        preflight=repo_preflight(Path(repo['root']),spec['base_sha'])
    except GateError as e:
        store.transition(jid,'REQUESTED','DENIED',{'reason_code':e.code})
        return {'job_id':jid,'state':'DENIED','reason':e.code}
    store.transition(jid,'REQUESTED','PREFLIGHTED',{'repo_id':spec['repo_id'],'base_sha':preflight['base_sha'],
                                                   'tree_sha':preflight['tree_sha'],'grant_digest':digest(grant)})
    # replay lock occurs before patch execution; retries require separately issued job/nonce.
    store.consume_grant(grant_fields['nonce'],jid)
    with verified_snapshot(Path(repo['root']),spec['base_sha']) as (snap,metadata):
        store.transition(jid,'PREFLIGHTED','CHECKOUT_VERIFIED',{'snapshot_tree_sha':metadata['tree_sha']})
        baseline=inspect_fixture(snap,spec['test'])
        if baseline['status']!='FAIL':
            store.transition(jid,'CHECKOUT_VERIFIED','BASELINE_NOT_REPRODUCED',{'baseline':baseline})
            return {'job_id':jid,'state':'BASELINE_NOT_REPRODUCED','baseline':baseline,
                    'claim':'BUG_FIXED_WITHHELD'}
        store.transition(jid,'CHECKOUT_VERIFIED','BASELINE_REPRODUCED',{'baseline':baseline})
        patch_event=apply_exact(snap,patch)
        store.transition(jid,'BASELINE_REPRODUCED','PATCH_APPLIED_IN_ISOLATION',patch_event)
        after=inspect_fixture(snap,spec['test'])
        if after['status']!='PASS':
            store.transition(jid,'PATCH_APPLIED_IN_ISOLATION','AFTER_TEST_FAILED',{'after':after})
            return {'job_id':jid,'state':'AFTER_TEST_FAILED','baseline':baseline,'after':after,
                    'claim':'BUG_FIXED_WITHHELD'}
        receipt={'repo_id':spec['repo_id'],'base_sha':spec['base_sha'],'test':spec['test']['id'],
                 'test_spec_sha256':digest(spec['test']),'before':baseline,'after':after,
                 'patch':patch_event,'execution_scope':'NONEXECUTING_SYNTHETIC_JSON_FIXTURE',
                 'proof_ceiling':'STATIC_CANARY_RED_GREEN_ONLY_NOT_TARGET_SUITE_NOT_DEPLOYED'}
        store.transition(jid,'PATCH_APPLIED_IN_ISOLATION','CANARY_RED_GREEN',{'receipt_sha256':digest(receipt)})
        store.save_receipt(jid,receipt)
        return {'job_id':jid,'state':'CANARY_RED_GREEN','receipt':receipt,'receipt_sha256':digest(receipt),
                'patch_persisted_in_source':False,'permission_to_push':False}


def capability_report():
    return {'version':'vct-autopatcher-core/0.8.0','persistent_sqlite_jobs':True,'receipt_retrieval':True,'cancel_queued':True,
            'grant_signature':'HMAC_SHA256_OPERATOR_ONLY','repository_identity':'operator_registry+Git_SHA',
            'snapshot':'pinned_git_archive_ephemeral','baseline':'read_only_json_fixture',
            'patch':'isolated_snapshot_only','user_project_tests':'NOT_EXECUTED_SANDBOX_REQUIRED',
            'mcp_cloud_connected':False,'git_push':False,'deploy':False,
            'all_policy_grants_deployment':'DENY'}
