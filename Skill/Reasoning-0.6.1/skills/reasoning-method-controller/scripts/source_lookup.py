#!/usr/bin/env python3
"""Read/search bundled evidence. Python standard library; no network or writes."""
import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def normalize(text):
    return ''.join(c for c in unicodedata.normalize('NFKD', text.casefold())
                   if not unicodedata.combining(c))

def contained(rel):
    path = (ROOT / rel).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError('Source path escapes skill directory')
    return path

def pages(entry):
    for chunk in entry['chunks']:
        body = contained(chunk['path']).read_text(encoding='utf-8')
        if entry.get('pdf_pages'):
            pieces = re.split(r'^## PDF page (\d+)\s*$', body, flags=re.M)
            for i in range(1, len(pieces), 2):
                yield int(pieces[i]), pieces[i+1].strip(), chunk['path']
        else:
            for match in re.finditer(r'^(\d+): (.*)$', body, flags=re.M):
                yield int(match[1]), match[2], chunk['path']

def range_arg(value):
    match = re.fullmatch(r'(\d+)(?::(\d+))?', value)
    if not match:
        raise ValueError('Range must be N or N:M')
    first, last = int(match[1]), int(match[2] or match[1])
    if first < 1 or last < first:
        raise ValueError('Invalid range')
    return first, last

def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest='command', required=True)
    sub.add_parser('list')
    search = sub.add_parser('search')
    search.add_argument('--source')
    search.add_argument('--query', required=True)
    search.add_argument('--limit', type=int, default=5)
    read = sub.add_parser('read')
    read.add_argument('--source', required=True)
    read.add_argument('--pages')
    read.add_argument('--lines')
    read.add_argument('--max-chars', type=int, default=30000)
    args = ap.parse_args()
    index = json.loads((ROOT/'references/source-index.json').read_text())
    entries = index['sources']
    if args.command == 'list':
        result = [{k:v for k,v in e.items() if k not in ('chunks','sha256')}
                  for e in entries]
    else:
        if args.source:
            entries = [e for e in entries if e['id'] == args.source.upper()]
            if not entries:
                raise ValueError('Unknown source ID')
        if args.command == 'search':
            if not 1 <= args.limit <= 20:
                raise ValueError('Limit must be 1–20')
            terms = re.findall(r'\w+', normalize(args.query))
            if not terms:
                raise ValueError('Query must contain a word')
            result = []
            for e in entries:
                for number, text, path in pages(e):
                    norm = normalize(text)
                    if not all(term in norm for term in terms):
                        continue
                    score = sum(norm.count(term) for term in terms)
                    pos = max(0, norm.find(terms[0])-180)
                    result.append({'source_id':e['id'],'title':e['title'],
                        'original_filename':e.get('original_filename'),
                        'pdf_page' if e.get('pdf_pages') else 'line':number,
                        'passage_file':path,'score':score,
                        'excerpt':text[pos:pos+900],
                        'status':'candidate passage; read full context before attribution'})
            result.sort(key=lambda x:(-x['score'],x['source_id'],x.get('pdf_page',x.get('line'))))
            result = result[:args.limit]
        else:
            e = entries[0]
            if bool(args.pages) == bool(args.lines):
                raise ValueError('Specify exactly one of --pages or --lines')
            if bool(args.pages) != bool(e.get('pdf_pages')):
                raise ValueError('Use --pages for PDF sources and --lines for text sources')
            start,end = range_arg(args.pages or args.lines)
            if end-start > (15 if args.pages else 200):
                raise ValueError('Read at most 16 pages or 201 lines per request')
            if not 1 <= args.max_chars <= 100000:
                raise ValueError('max-chars must be 1–100000')
            selected = [(n,t,p) for n,t,p in pages(e) if start<=n<=end]
            if len(selected) != end-start+1:
                raise ValueError('Requested range is not available')
            budget = args.max_chars
            passages = []
            for n,t,p in selected:
                shown=t[:budget]
                passages.append({'pdf_page' if args.pages else 'line':n,
                                 'passage_file':p,'text':shown,
                                 'truncated':len(shown)<len(t)})
                budget=max(0,budget-len(shown))
            result={'source_id':e['id'],'title':e['title'],'authors':e.get('authors'),
                    'identity':e['identity'],'original_asset':e['asset'],
                    'citation_rule':('Physical PDF pages differ from printed/journal pages. Verify the original for formulas, figures and exact quotes.'
                                     if args.pages else 'Line numbers refer to the supplied text file. User reports and historical model claims are not independently verified external evidence.'),
                    'passages':passages}
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__ == '__main__':
    try:
        main()
    except (ValueError,OSError,json.JSONDecodeError) as error:
        print(json.dumps({'error':str(error)}),file=sys.stderr)
        sys.exit(2)
