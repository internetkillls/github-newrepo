#!/usr/bin/env python3
"""Read-only SM-20 JSONL lexical retrieval; no invented field schema/semantic vector claims."""
import argparse, json, hashlib, sys
from pathlib import Path

def load(path):
    out=[]
    for n,line in enumerate(Path(path).read_text(encoding='utf-8-sig').splitlines(),1):
        if not line.strip():continue
        try: d=json.loads(line)
        except json.JSONDecodeError as exc:raise ValueError(f'invalid JSONL at line {n}: {exc}') from exc
        if not isinstance(d,dict):raise ValueError(f'expected object at line {n}')
        original_id=d.get('id',d.get('source_id'))
        sid= str(original_id) if original_id not in (None,'') else 'generated-sha256-'+hashlib.sha256(line.encode()).hexdigest()[:16]
        out.append({'bank':'SM-20','row':n,'id':sid,'id_kind':'original' if original_id not in (None,'') else 'derived', 'record':d})
    return out

def score(query,item):
    words=[s.lower() for s in query.strip().split() if s]
    text=json.dumps(item['record'],ensure_ascii=False,sort_keys=True).lower()
    return sum(1 for w in words if w in text)

def main():
    p=argparse.ArgumentParser(description='SM-20 read-only JSONL retrieval')
    p.add_argument('--input',required=True,help='Path to user-supplied SM-20 JSONL')
    p.add_argument('--query',default='',help='Whitespace-separated lexical query')
    p.add_argument('--limit',type=int,default=20,help='Maximum output rows; default 20')
    p.add_argument('--output',help='Optional output JSONL path')
    args=p.parse_args()
    if args.limit<1:p.error('--limit must be positive')
    records=load(args.input)
    if args.query: records=[dict(r,score=score(args.query,r)) for r in records];records=[r for r in records if r['score']];records.sort(key=lambda r:(-r['score'],r['row']))
    result=records[:args.limit]
    data=''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in result)
    if args.output:Path(args.output).write_text(data,encoding='utf-8')
    else:sys.stdout.write(data)
    print(json.dumps({'bank':'SM-20','status':'loaded','total_rows':len(load(args.input)), 'matched_rows':len(records),'returned_rows':len(result),'query':args.query,'mode':'lexical-readonly','preserved_raw':True}),file=sys.stderr)

if __name__=='__main__':
    try:main()
    except (OSError,ValueError) as e:print('ERROR:',e,file=sys.stderr);sys.exit(2)
