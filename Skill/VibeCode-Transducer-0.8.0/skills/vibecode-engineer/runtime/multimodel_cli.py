#!/usr/bin/env python3
"""Read-only JSON CLI for bounded cross-model reasoning with actual Python receipt."""
import argparse,json,sys
from multimodel_engine import execute, MultiModelInputError

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--spec',required=True)
    ns=ap.parse_args()
    try:
        with open(ns.spec,encoding='utf8') as f: p=json.load(f)
        r=execute(p)
        print(json.dumps(r,indent=2,ensure_ascii=False,allow_nan=False))
        return 0
    except (OSError,ValueError,TypeError) as e:
        print('INVALID_INPUT: '+str(e),file=sys.stderr)
        return 2
if __name__=='__main__':raise SystemExit(main())
