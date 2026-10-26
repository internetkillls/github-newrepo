#!/usr/bin/env python3
"""Optional user-initiated local patch transaction. NEVER exposed through MCP.

Only exact SHA-bound replacements within a declared repository. Running configured
project tests executes local code: use a trusted disposable checkout/container.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from vibe_transducer import ContractError, valid_path,sha, MAX_EDITS

class ApplyError(ContractError):pass

def write_atomic(path:Path,content:str)->None:
    fd,tmp=tempfile.mkstemp(prefix='.vibecode-tmp-',dir=str(path.parent),text=True)
    try:
        with os.fdopen(fd,'w',encoding='utf-8',newline='') as f:
            f.write(content);f.flush();os.fsync(f.fileno())
        os.chmod(tmp,path.stat().st_mode&0o777)
        os.replace(tmp,path)
    finally:
        if os.path.exists(tmp):os.unlink(tmp)

def trusted_runner_argv(args:list[str])->bool:
    """Fail closed to approved command families; owner still vets test contents."""
    if not args or not all(isinstance(a,str) and a for a in args):return False
    executable=Path(args[0]).name.lower()
    if executable in {'python','python.exe','python3','python3.exe','py','py.exe'} or (executable.startswith('python3.') and executable.replace('python3.','').isdigit()):
        return len(args)>=3 and args[1:3] in (['-m','unittest'],['-m','pytest'])
    return executable in {'pytest','pytest.exe'}

def runner_receipt(args:list[str],output:str)->bool:
    text=output.replace('\x1b[0m','')
    # Strictly only basic well-known receipts, with nonzero test count and success markers.
    m=re.search(r'Ran (\d+) tests? in ',text)
    if m:return int(m.group(1))>0 and bool(re.search(r'\nOK(?:\s|$)',text))
    m=re.search(r'(\d+) passed(?:\s|,|in\s)',text,re.I)
    if m:return int(m.group(1))>0 and 'failed' not in text.lower()
    # Other runners need an explicit adapter, not a fabricated green receipt.
    return False

def apply_local(root:str,changes:list[dict],test_argv:list[str],*,approved:bool=False,writes_enabled:bool=False,timeout:int=45)->dict:
    if not writes_enabled or not approved:raise ApplyError('requires independent --enable-writes and --approve')
    if not isinstance(test_argv,list) or not test_argv or any(not isinstance(x,str) or not x or '\x00' in x for x in test_argv):
        raise ApplyError('trusted test argv array required; shell is not used')
    if not trusted_runner_argv(test_argv):raise ApplyError('test command family is not allowlisted (python -m unittest/pytest or pytest)')
    if not isinstance(changes,list) or not 1<=len(changes)<=MAX_EDITS:raise ApplyError('1..5 exact changes required')
    rootdir=Path(root).resolve(strict=True)
    if not rootdir.is_dir() or Path(root).is_symlink():raise ApplyError('repository must be real directory, not symlink')
    staged=[];paths=set()
    for edit in changes:
        if not isinstance(edit,dict):raise ApplyError('change must be object')
        raw=valid_path(edit.get('path'))
        if raw in paths:raise ApplyError('only one change per path')
        paths.add(raw)
        if raw.startswith(('tests/','test/')) or re.search(r'(?:^|/)(?:test_[^/]+|[^/]+\.test\.[a-z]+|[^/]+\.spec\.[a-z]+)$',raw):
            raise ApplyError('test file changes require separate user review')
        candidate=rootdir/raw
        if candidate.is_symlink() or any(p.is_symlink() for p in list(candidate.parents) if p!=rootdir and rootdir in p.parents):
            raise ApplyError('symlink traversal prohibited')
        final=candidate.resolve(strict=True)
        if not final.is_file() or rootdir not in final.parents:raise ApplyError('path escapes root or missing')
        if final.stat().st_size>100_000:raise ApplyError('file exceeds local patch size limit')
        before=final.read_text(encoding='utf-8')
        old,new,hash_expected=edit.get('old'),edit.get('new'),edit.get('sha256')
        if not isinstance(old,str) or not old or not isinstance(new,str) or old==new or not isinstance(hash_expected,str) or not re.fullmatch('[0-9a-f]{64}',hash_expected):
            raise ApplyError('invalid old/new/hash')
        if sha(before)!=hash_expected:raise ApplyError('stale source sha256')
        if before.count(old)!=1:raise ApplyError('old text must occur exactly once')
        after=before.replace(old,new,1)
        staged.append((final,before,after))
    # Avoid running tests unless there is a concrete mutation; process exit and
    # receipt remain distinct proof obligations.
    written=[]
    try:
        for path,before,after in staged:
            if sha(path.read_text(encoding='utf-8'))!=sha(before):raise ApplyError('concurrent pre-write source mutation')
            write_atomic(path,after); written.append((path,before,after))
        result=subprocess.run(test_argv,cwd=str(rootdir),capture_output=True,text=True,
                              shell=False,timeout=timeout,stdin=subprocess.DEVNULL,check=False)
        receipt=(result.stdout or '')+'\n'+(result.stderr or '')
        passed=result.returncode==0 and runner_receipt(test_argv,receipt)
        if passed:
            return {'state':'PATCH_APPLIED_TEST_RECEIPT','exit_code':result.returncode,'test_receipt':True,
                    'files':[{'path':str(p.relative_to(rootdir)),'sha256':sha(after)} for p,_,after in written],
                    'runtime_behavior_verified':False}
        reason=f'test non-pass: exit={result.returncode} receipt={bool(runner_receipt(test_argv,receipt))}'
        raise ApplyError(reason)
    except (ApplyError,subprocess.TimeoutExpired,OSError,UnicodeError) as error:
        conflicts=[];restored=[]
        for path,before,after in reversed(written):
            try:
                if sha(path.read_text(encoding='utf-8'))!=sha(after):conflicts.append(str(path.relative_to(rootdir)))
                else:write_atomic(path,before);restored.append(str(path.relative_to(rootdir)))
            except (OSError,UnicodeError):conflicts.append(str(path.relative_to(rootdir)))
        return {'state':'MANUAL_CONFLICT' if conflicts else 'ROLLED_BACK',
                'reason':str(error),'restored':restored,'conflicts':conflicts,'runtime_behavior_verified':False}

def main()->int:
    p=argparse.ArgumentParser(description='Explicit local patch+test: NEVER callable via remote MCP')
    p.add_argument('--repo',required=True)
    p.add_argument('--plan',required=True,help='JSON object containing changes[]')
    p.add_argument('--test-argv-json',required=True,help='JSON list supplied by owner, e.g. ["python","-m","unittest","discover","-s","tests"]')
    p.add_argument('--approve',action='store_true')
    p.add_argument('--enable-writes',action='store_true')
    a=p.parse_args()
    try:
        data=json.loads(Path(a.plan).read_text(encoding='utf-8'))
        receipt=apply_local(a.repo,data['changes'],json.loads(a.test_argv_json),approved=a.approve,writes_enabled=a.enable_writes)
        print(json.dumps(receipt,indent=2));return 0 if receipt['state']=='PATCH_APPLIED_TEST_RECEIPT' else 3
    except (ApplyError,ValueError,KeyError,OSError) as e:
        print(json.dumps({'state':'REJECTED','reason':str(e)}));return 2
if __name__=='__main__':raise SystemExit(main())
