#!/usr/bin/env python3
"""Generate, do not fetch, safe public search links for course research."""
import argparse
from urllib.parse import quote_plus

def url_for(search_base, q, suffix=''):
    return search_base + quote_plus(q) + suffix

def generate(term, outcome=''):
    quoted='"'+term.strip().replace('"','')+'"'
    context=(outcome.strip()+" ") if outcome.strip() else ''
    return {
      'github_repositories': url_for('https://github.com/search?q=', quoted+' '+context+'course assignments', '&type=repositories'),
      'university_syllabus': url_for('https://www.google.com/search?q=', 'site:edu '+quoted+' syllabus assignments'),
      'professor_notes': url_for('https://www.google.com/search?q=',quoted+' '+context+'professor lecture notes course'),
      'critical_countercase': url_for('https://www.google.com/search?q=',quoted+' critique limitations debate'),
    }

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('term',help='source-grounded term, not an invented topic label')
    parser.add_argument('--outcome',default='',help='target performance or graduate outcome')
    args=parser.parse_args()
    for title,link in generate(args.term,args.outcome).items():
        print(f'- [{title.replace("_", " ").title()}]({link})')
