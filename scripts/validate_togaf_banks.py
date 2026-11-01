#!/usr/bin/env python3
"""Validate question-bank structure; does NOT certify exam-level difficulty."""
from pathlib import Path
from collections import Counter
import re
import sys

root = Path(__file__).resolve().parent.parent
errors = []
def check(condition, message):
    if not condition:
        errors.append(message)

def parts(txt, prefix):
    return re.split(rf'(?=^## {prefix}\\d+\\b)', txt, flags=re.M)[1:]

fanswers = []
fids = []
for file in sorted((root / '09-foundation-question-bank').glob('0[1-8]-*q*.md')):
    text = file.read_text(encoding='utf-8')
    for part in re.split(r'(?=^## Q\\d+ — )', text, flags=re.M)[1:]:
        i = re.search(r'^## Q(\\d+)', part)
        a = re.search(r'\\*\\*Réponse\\s*:\\s*([ABCD])\\.\\*\\*', part)
        opts = re.findall(r'^([ABCD])\\.\\s+', part, re.M)
        check(opts == list('ABCD'), f'{file}: options incorrectes')
        if i and a:
            fids.append(int(i[1]))
            fanswers.append(a[1])
check(fids == list(range(1, 301)), f'Foundation ids {len(fids)}')
check(Counter(fanswers) == dict.fromkeys('ABCD', 75), f'Foundation bias {Counter(fanswers)}')

pids, pbest = [], []
for file in sorted((root / '10-practitioner-scenarios').glob('0[1-8]-*s*.md')):
    text = file.read_text(encoding='utf-8')
    for part in re.split(r'(?=^## S\\d+ — )', text, flags=re.M)[1:]:
        i = re.search(r'^## S(\\d+)', part)
        m = re.search(r'\\*\\*Scoring\\s*:\\s*([^*\\n]+)\\*\\*', part)
        opts = re.findall(r'^([ABCD])\\.\\s+', part, re.M)
        check(opts == list('ABCD'), f'{file}: options incorrectes')
        if i and m:
            scores = dict((k, int(v)) for k, v in re.findall(r'([ABCD])=(\\d)', m[1]))
            check(sorted(scores.values()) == [0, 1, 3, 5], f'{file}: mauvais barème')
            pids.append(int(i[1]))
            pbest += [next(k for k, v in scores.items() if v == 5)]
check(pids == list(range(1, 61)), f'Practitioner ids {len(pids)}')
check(Counter(pbest) == dict.fromkeys('ABCD', 15), f'Practitioner bias {Counter(pbest)}')

for n in range(1, 7):
    exam = (root / '11-mock-exams' / f'mock-0{n}-exam.md').read_text(encoding='utf-8')
    check(len(re.findall(r'^\\*\\*Q\\d+\\.\\*\\*', exam, re.M)) == 40, f'Mock {n}: 40 QCM')
    check(len(re.findall(r'^## P\\d+\\b', exam, re.M)) == 8, f'Mock {n}: 8 scenarios')

print('Foundation', len(fids), Counter(fanswers))
print('Practitioner', len(pids), Counter(pbest))
print('6 Combined mock exams checked')
if errors:
    for error in errors:
        print('FAIL', error, file=sys.stderr)
    sys.exit(1)
print('PASS static structure only; a human semantic and X2202 audit remains necessary')
