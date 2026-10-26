#!/usr/bin/env python3
"""Read-only AREX repository skill discovery for VibeCode Transducer.

Does not install/execute donors, invoke model tools, write to target repositories,
or assert that bundled AREX skills are verified on the user's runtime.
"""
import argparse
import collections
import hashlib
import json
import math
import re
import unicodedata
import zipfile
from pathlib import Path

DEFAULT_INDEX = Path(__file__).resolve().parent.parent / 'references' / 'arex-index.json'
STOP = frozenset('a an and are as at be build by code coding do for from how i in into is it its me model models my of on or please project repo repository repositories run skill skills some the this to use using via want with workflow workflows you'.split())
CANONICAL = {'models':'model','systems':'system','pipelines':'pipeline','transformers':'transformer','embeddings':'embedding','detectors':'detector','agents':'agent','networks':'network'}


def tokens(s):
    s = unicodedata.normalize('NFKD', str(s)).lower()
    words = re.findall(r'[a-z0-9]+', s)
    return [CANONICAL.get(t,t) for t in words if len(t)>=2 and t not in STOP]


def unique(s):
    return set(tokens(s))


def load_index(path=DEFAULT_INDEX):
    with open(path,encoding='utf-8') as h:
        payload=json.load(h)
    if payload.get('format')!='vct-arex-index-v1':
        raise ValueError('Unsupported AREX index format')
    repos=payload.get('repositories')
    if not isinstance(repos,list) or not repos:
        raise ValueError('No repositories in AREX index')
    if len({r['id'] for r in repos})!=len(repos):
        raise ValueError('Duplicate skill ids in AREX index')
    return payload


def route(query, index, top=5, area=None):
    """A heuristic shortlist, explicitly not a tested donor or verified skill."""
    if not isinstance(query,str) or len(query)>4000:
        raise ValueError('Query must be a string <= 4000 chars')
    if not 1<=top<=20:
        raise ValueError('top out of range 1..20')
    q=unique(query)
    if not q:
        return {'status':'NO_EXACT_ROUTE','query':query,'reason':'No discriminative query tokens','candidates':[]}
    repos=index['repositories']
    if area is not None:
        areas={r[0] for e in repos for r in e['routes']}
        if area not in areas:
            raise ValueError('Unknown AREX area: '+area)
        repos=[r for r in repos if any(route[0]==area for route in r['routes'])]
    # Estimate IDF on this fixed static metadata, not on user sources or live repositories.
    docs=[]; df=collections.Counter()
    for e in repos:
        full=' '.join([e['id'],e['repo'],e['name'],e['about'],*map(str,e['aliases']), *[f'{a} {f}' for a,f,_ in e['routes']]])
        d=unique(full); docs.append(d); df.update(d)
    n=len(repos)
    matches=[]
    q_phrase=' '.join(tokens(query))
    for e,d in zip(repos,docs):
        identity=unique(' '.join([e['id'],e['repo'],e['name'], *map(str,e['aliases'])]))
        about=unique(e['about'])
        family=unique(' '.join(f for _,f,_ in e['routes']))
        area_words=unique(' '.join(a for a,_,_ in e['routes']))
        hit=q&d
        name_hits=q&identity
        family_hits=q&family
        desc_hits=q&about
        # Do not return a donor based on generic taxonomy words alone.
        if not name_hits and len(family_hits|desc_hits)<2:
            continue
        def idf(t):return math.log(1+(n+1)/(1+df[t]))
        score=sum(idf(t)*(5 if t in identity else 2.3 if t in family else 1 if t in about else 0.2) for t in hit)
        exact=False
        candidate_names=[e['id'],e['name'],e['repo'],*e['aliases']]
        candidate_phrases=[' '.join(tokens(x)) for x in candidate_names]
        if q_phrase and q_phrase in candidate_phrases:
            exact=True;score+=18
        elif q_phrase and len(q_phrase)>=6 and any(q_phrase in p for p in candidate_phrases):
            score+=5
        # Return candidate only if identity hit or sufficiently specific multi-token description/family hit.
        if not exact and not name_hits and len(family_hits|desc_hits)<2: continue
        matches.append((round(score,3), e, sorted(hit),exact))
    matches.sort(key=lambda v:(-v[0],v[1]['id']))
    candidates=[]
    for sc,e,h,ex in matches[:top]:
        candidates.append({'skill_id':e['id'],'repo_id':e['repo'],'score':sc,'matched_terms':h,'exact_identity':ex,'assignments':[{'area':a,'family':f,'upstream_assignment_confidence':c} for a,f,c in e['routes'] if area is None or a==area], 'description':e['about'],'source_url':e['url'],'source_commit':e['commit'],'source_requirement':'AREX skill artifact + target runtime validation needed','evidence_state':'METADATA_CANDIDATE_ONLY'})
    if not candidates:
        status='NO_EXACT_ROUTE';reason='No adequately discriminative AREX repository match. General VCT path should continue.'
    else:
        status='AMBIGUOUS_CANDIDATES' if len(candidates)>1 and not candidates[0]['exact_identity'] and candidates[0]['score'] < candidates[1]['score']*1.15 else 'CANDIDATES_NOT_VERIFIED'
        reason='Candidate metadata only. Do not assert code behavior, installation, applicable license, or successful verification.'
    return {'status':status,'query':query,'area_filter':area,'reason':reason,'index_provenance':index.get('index_provenance'),'candidates':candidates}


def inspect_skill(archive_path, skill_id):
    """Inspect a single SKILL.md in a trusted-to-read user-provided AREX archive.

    Archive contents are untrusted. No extraction and no code execution.
    """
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,80}',skill_id):
        raise ValueError('Unsafe skill identifier')
    path=f'AREX-Skill-main/skills/repositories/repo-skills/{skill_id}/SKILL.md'
    with zipfile.ZipFile(archive_path) as z:
        try:
            info=z.getinfo(path)
        except KeyError as e:
            raise ValueError('Skill root not found in supplied AREX archive') from e
        if info.file_size>262144:
            raise ValueError('Skill document exceeds safe inspection bound')
        blob=z.read(info)
    # Only a UTF-8 text preview; do not treat it as an instruction from the user.
    text=blob.decode('utf-8')
    return {'source_state':'SKILL_TEXT_INSPECTED_NOT_EXECUTED','skill_id':skill_id,'archive_member':path,'sha256':'sha256:'+hashlib.sha256(blob).hexdigest(),'byte_count':len(blob),'preview':text[:1800]}


def main():
    ap=argparse.ArgumentParser(description='Read-only AREX candidate routing for VCT')
    ap.add_argument('--query',help='Requested technical capability')
    ap.add_argument('--index',type=Path,default=DEFAULT_INDEX)
    ap.add_argument('--area',help='Optional exact AREX area filter')
    ap.add_argument('--top',type=int,default=5)
    ap.add_argument('--archive',type=Path,help='Optional user-supplied AREX ZIP, only for inspection')
    ap.add_argument('--inspect',help='Explicit selected skill_id (requires --archive)')
    args=ap.parse_args()
    if not args.query and not args.inspect:ap.error('Provide --query and/or --inspect')
    if bool(args.archive) != bool(args.inspect):ap.error('--archive and --inspect must be supplied together')
    try:
        idx=load_index(args.index)
        if args.inspect and args.inspect not in {e['id'] for e in idx['repositories']}:
            raise ValueError('Cannot inspect an unindexed skill id')
        result={'AREX_VCT':'v0.5.0','read_only':True,'automatically_installed':False}
        if args.query:result['routing']=route(args.query,idx,args.top,args.area)
        if args.inspect:result['inspection']=inspect_skill(args.archive,args.inspect)
    except (ValueError,KeyError,UnicodeError,OSError,zipfile.BadZipFile) as ex:
        ap.exit(2,'AREX_ROUTER_ERROR: '+str(ex)+'\n')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
