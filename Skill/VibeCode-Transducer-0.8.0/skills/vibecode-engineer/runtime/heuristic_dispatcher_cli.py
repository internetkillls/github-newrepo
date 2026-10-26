#!/usr/bin/env python3
"""Read-only CLI for heuristic_dispatcher: Python evidence → conditional tasks."""
import argparse,json,sys
from heuristic_dispatcher import dispatch,DispatchInputError
from multimodel_engine import MultiModelInputError

def main():
    p=argparse.ArgumentParser();p.add_argument('--spec',required=True);a=p.parse_args()
    try:
        with open(a.spec,encoding='utf8') as h:spec=json.load(h)
        print(json.dumps(dispatch(spec),ensure_ascii=False,allow_nan=False,indent=2));return 0
    except (DispatchInputError,MultiModelInputError,TypeError,ValueError,OSError) as e:
        print('INVALID_INPUT: '+str(e),file=sys.stderr);return 2
if __name__=='__main__':raise SystemExit(main())
