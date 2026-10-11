"""Offline visual contract validation, build planning, cue calculation and catalog."""
from pathlib import Path
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
import argparse, hashlib, json, math, re, sqlite3
from contextlib import closing

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False)

def digest(value):
    return hashlib.sha256(canonical(value).encode('utf-8')).hexdigest()

def require(condition, message):
    if not condition:
        raise ValueError(message)

def number(value):
    return type(value) in (int, float) and math.isfinite(value)

def integer(value):
    return type(value) is int

def clock(value):
    require(isinstance(value,str) and re.fullmatch(r'\d{2}:\d{2}',value), 'clock must be HH:MM')
    h,m=map(int,value.split(':'))
    require(0<=h<24 and 0<=m<60,'invalid clock')
    return h*3600+m*60

def center(p,face,u,frame,count,j):
    alpha=2*math.pi*(face+u)/4
    theta=2*math.pi*frame/count
    return .5+p['band_span']*((j+.5)/p['ribbon_count']-.5)+p['amplitude']*math.sin(p['spatial_harmonic']*alpha+p['temporal_cycles']*theta+2*math.pi*j/p['ribbon_count'])

def validate(spec):
    require(isinstance(spec,dict),'spec must be an object')
    require(spec['schema_version']=='studio-project/1.0','unsupported schema')
    require(isinstance(spec['project_id'],str) and re.fullmatch(r'[a-z0-9][a-z0-9-]{0,63}',spec['project_id']),'invalid project_id')
    c=spec['canvas']; t=spec['timing']; r=spec['recipe']; s=spec['show']
    require(c['face_count']==4 and integer(c['face_count']),'this recipe requires 4 faces')
    require(all(integer(c[x]) and 1<=c[x]<=16384 for x in ['width','height']),'invalid dimensions')
    require(c['packing'] in ['linear','grid'],'packing must be linear or grid')
    require(integer(t['fps']) and 1<=t['fps']<=240,'fps must be integer 1..240')
    require(integer(t['frame_count']) and t['frame_count']>1,'frame_count must be integer >1')
    require(t['clock']=='explicit_frame_index','explicit frame clock required')
    require(r['id']=='studio-cube-perimeter-ribbons' and r['version']=='1.0.0','unsupported recipe/version')
    require(integer(r['seed']),'seed must be integer')
    p=r['parameters']
    bounds={'ribbon_count':(3,12),'band_span':(.2,.6),'amplitude':(.01,.08),'stroke_width':(.002,.02),'spatial_harmonic':(2,8),'temporal_cycles':(1,3)}
    for name,(a,b) in bounds.items():
        require(number(p[name]) and a<=p[name]<=b,f'{name} outside bounds')
    require(all(integer(p[x]) for x in ['ribbon_count','spatial_harmonic','temporal_cycles']),'count/harmonic/cycles must be integers')
    require(p['band_span']/2+p['amplitude']+p['stroke_width']/2<=.42,'top/bottom safe margin violated')
    require(isinstance(r['palette'],list) and len(r['palette'])>=2 and all(isinstance(x,str) and re.fullmatch(r'#[0-9a-fA-F]{6}',x) for x in r['palette']),'palette needs at least2 sRGB hex colors')
    targets=spec['targets']
    require(isinstance(targets,list) and targets and len(targets)==len(set(targets)) and all(x in ['touchdesigner','blender','p5js'] for x in targets),'invalid targets')
    for x in targets:
        a=spec['adapters'][x]
        require(isinstance(a['version'],str) and a['version'],'adapter version required')
        require(a['engine_build'] is None or isinstance(a['engine_build'],str),'invalid engine build')
        require(type(a['runtime_verified']) is bool,'runtime_verified must be boolean')
    require(isinstance(spec['assets'],list),'assets must be array')
    for asset in spec['assets']:
        require(isinstance(asset,dict) and isinstance(asset['id'],str),'asset id required')
        require(re.fullmatch(r'[0-9a-f]{64}',asset['sha256']) is not None,'asset sha256 required')
        require(isinstance(asset['path'],str) and asset['path'],'asset path required')
    require(s['timezone'] is None or isinstance(s['timezone'],str),'timezone must be null or IANA identifier')
    require(type(s['boundaries_approved']) is bool,'boundaries_approved must be boolean')
    duration=(clock(s['end'])-clock(s['start']))%86400
    require(duration>0,'zero/full-day show unsupported')
    require(len(s['sessions'])==4,'four sessions required')
    require([x['id'] for x in s['sessions']]==['opening','warming_up','party_peak','farewell'],'incorrect session order/IDs')
    previous=0
    for session in s['sessions']:
        a,b=session['start_offset'],session['end_offset']
        require(integer(a) and integer(b) and a==previous and b>a,'sessions must be contiguous half-open intervals')
        previous=b
    require(previous==duration,'sessions do not cover show duration')
    max_error=0.
    for f in [0,t['frame_count']//3,t['frame_count']-1]:
        for j in range(p['ribbon_count']):
            for face in range(4):
                max_error=max(max_error,abs(center(p,face,1,f,t['frame_count'],j)-center(p,(face+1)%4,0,f,t['frame_count'],j)))
    for j in range(p['ribbon_count']):
        for face in range(4):
            for u in [0,.25,.5,.75,1]:
                max_error=max(max_error,abs(center(p,face,u,0,t['frame_count'],j)-center(p,face,u,t['frame_count'],t['frame_count'],j)))
    require(max_error<1e-12,'analytic closure failed')
    return {'contract_valid':True,'analytic_closure_max_error':max_error,'spec_hash':digest(spec),'native_pixels':4*c['width']*c['height'],'duration_seconds':t['frame_count']/t['fps'],'export_frames':[0,t['frame_count']-1],'runtime_verified':False,'limitations':['No render/codec/player tests performed','Asset digests declared, not checked against files','Timezone and design/session approvals may remain unresolved']}

def plan(spec):
    check=validate(spec); c=spec['canvas']
    dims=[4*c['width'],c['height']] if c['packing']=='linear' else [2*c['width'],2*c['height']]
    return {'manifest_version':'studio-build-plan/1.0','project_id':spec['project_id'],'spec_hash':check['spec_hash'],'build_key':digest({'spec':spec,'helper_version':'1.0.0'}),'status':'plan_only_unrendered','canvas_dimensions':dims,'face_order':[0,1,2,3],'spec':spec,'jobs':[{'target':x,'job_id':digest({'spec_hash':check['spec_hash'],'target':x,'adapter':spec['adapters'][x]}),'adapter':spec['adapters'][x],'frame_range':check['export_frames'],'render_status':'pending'} for x in spec['targets']],'checks':check}

def cue(spec, at):
    validate(spec)
    s=spec['show']
    require(s['timezone'] is not None,'venue timezone unresolved; set an explicit IANA identifier')
    moment=datetime.fromisoformat(at)
    require(moment.utcoffset() is not None,'--at must include a timezone offset')
    try:
        zone=ZoneInfo(s['timezone'])
    except ZoneInfoNotFoundError as e:
        raise ValueError('IANA timezone unavailable; install tzdata or provide OS zoneinfo data') from e
    local=moment.astimezone(zone)
    now_seconds=local.hour*3600+local.minute*60+local.second
    start=clock(s['start']); end=clock(s['end'])
    active=(now_seconds>=start or now_seconds<end) if end<start else start<=now_seconds<end
    if not active:
        return {'active':False,'session':None,'show_day':None,'timezone':s['timezone'],'action':'none','schedule_approved':s['boundaries_approved']}
    day=local.date()-timedelta(days=1) if end<start and now_seconds<end else local.date()
    offset=(now_seconds-start)%86400
    session=next(x['id'] for x in s['sessions'] if x['start_offset']<=offset<x['end_offset'])
    return {'active':True,'show_day':day.isoformat(),'theme_id':s['theme_id'],'session':session,'offset_seconds':offset,'timezone':s['timezone'],'action':'none','schedule_approved':s['boundaries_approved'],'note':'Read-only cue proposal; civil-clock boundaries apply, no DST elapsed-time promise'}

def catalog(manifest,path):
    require(manifest['manifest_version']=='studio-build-plan/1.0','unsupported manifest')
    check=validate(manifest['spec'])
    require(check['spec_hash']==manifest['spec_hash'],'manifest/spec hash mismatch')
    require(manifest['project_id']==manifest['spec']['project_id'],'manifest project mismatch')
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    with closing(sqlite3.connect(p)) as conn:
        with conn:
            conn.execute('CREATE TABLE IF NOT EXISTS projects(project_id TEXT NOT NULL,spec_hash TEXT NOT NULL,status TEXT NOT NULL,manifest_json TEXT NOT NULL,PRIMARY KEY(project_id,spec_hash))')
            conn.execute('INSERT INTO projects VALUES(?,?,?,?) ON CONFLICT(project_id,spec_hash) DO UPDATE SET status=excluded.status,manifest_json=excluded.manifest_json',(manifest['project_id'],manifest['spec_hash'],manifest['status'],canonical(manifest)))
    return {'saved':True,'database':str(p.resolve()),'project_id':manifest['project_id'],'spec_hash':manifest['spec_hash']}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='command',required=True)
    for name in ['validate','plan','cue','catalog']:
        cmd=sub.add_parser(name); cmd.add_argument('input',type=Path)
        if name=='plan':cmd.add_argument('--out',type=Path,required=True)
        if name=='cue':cmd.add_argument('--at',required=True)
        if name=='catalog':cmd.add_argument('--db',required=True)
    args=parser.parse_args()
    try:
        data=json.loads(args.input.read_text(encoding='utf-8-sig'))
        if args.command=='validate':result=validate(data)
        elif args.command=='cue':result=cue(data,args.at)
        elif args.command=='catalog':result=catalog(data,args.db)
        else:
            result=plan(data); args.out.mkdir(parents=True,exist_ok=True)
            dest=args.out/'build-plan.json'
            text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
            if dest.exists() and dest.read_text(encoding='utf-8')!=text:
                raise ValueError('build-plan.json exists with different content; use a new version directory')
            dest.write_text(text,encoding='utf-8')
        print(json.dumps(result,ensure_ascii=False,indent=2))
    except (ValueError,KeyError,TypeError,OSError,StopIteration) as exc:
        parser.exit(2,'Error: '+str(exc)+'\n')

if __name__=='__main__':main()
