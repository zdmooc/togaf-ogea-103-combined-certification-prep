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
    return re.split(rf'(?=^## {prefix}\d+\b)', txt, flags=re.M)[1:]

fanswers = []
fids = []
for file in sorted((root / '09-foundation-question-bank').glob('0[1-8]-*q*.md')):
    text = file.read_text(encoding='utf-8')
    for part in re.split(r'(?=^## Q\d+ — )', text, flags=re.M)[1:]:
        i = re.search(r'^## Q(\d+)', part)
        a = re.search(r'\*\*Réponse\s*:\s*([ABCD])\.\*\*', part)
        opts = re.findall(r'^([ABCD])\.\s+', part, re.M)
        check(opts == list('ABCD'), f'{file}: options incorrectes')
        if i and a:
            fids.append(int(i[1]))
            fanswers.append(a[1])
check(fids == list(range(1, 301)), f'Foundation ids {len(fids)}')
check(Counter(fanswers) == dict.fromkeys('ABCD', 75), f'Foundation bias {Counter(fanswers)}')

pids, pbest = [], []
for file in sorted((root / '10-practitioner-scenarios').glob('0[1-8]-*s*.md')):
    text = file.read_text(encoding='utf-8')
    for part in re.split(r'(?=^## S\d+ — )', text, flags=re.M)[1:]:
        i = re.search(r'^## S(\d+)', part)
        m = re.search(r'\*\*Scoring\s*:\s*([^*\n]+)\*\*', part)
        opts = re.findall(r'^([ABCD])\.\s+', part, re.M)
        check(opts == list('ABCD'), f'{file}: options incorrectes')
        if i and m:
            scores = dict((k, int(v)) for k, v in re.findall(r'([ABCD])=(\d)', m[1]))
            check(sorted(scores.values()) == [0, 1, 3, 5], f'{file}: mauvais barème')
            pids.append(int(i[1]))
            pbest += [next(k for k, v in scores.items() if v == 5)]
check(pids == list(range(1, 61)), f'Practitioner ids {len(pids)}')
check(Counter(pbest) == dict.fromkeys('ABCD', 15), f'Practitioner bias {Counter(pbest)}')

for n in range(1, 7):
    exam = (root / '11-mock-exams' / f'mock-0{n}-exam.md').read_text(encoding='utf-8')
    correction = (root / '11-mock-exams' / 'corrections' / f'mock-0{n}-correction.md').read_text(encoding='utf-8')
    qids = [int(x) for x in re.findall(r'^\*\*Q(\d+)\.\*\*', exam, re.M)]
    pids = [int(x) for x in re.findall(r'^## P(\d+)\b', exam, re.M)]
    keys = [(int(i), l) for i, l in re.findall(r'^(\d+)\.\s+\*\*([ABCD])\*\*', correction, re.M)]
    check(qids == list(range(1, 41)), f'Mock {n}: question IDs not Q1..Q40')
    check(pids == list(range(1, 9)), f'Mock {n}: scenario IDs not P1..P8')
    check([i for i, _ in keys] == list(range(1, 41)), f'Mock {n}: Foundation corrections missing')
    part2 = correction[correction.index('# Part 2'):]
    gradient = re.findall(r'^\*\*(?:Barème|Scoring)\s*:\*\*\s*([^\n]+)', part2, re.M)
    check(len(gradient) == 8, f'Mock {n}: expected 8 Practitioner gradient keys')
    for i, item in enumerate(gradient, 1):
        values = re.findall(r'([ABCD])=(\d)', item)
        check(len(values) == 4 and sorted(int(v) for _, v in values) == [0, 1, 3, 5],
              f'Mock {n} P{i}: invalid gradient')

# Cross-exam integrity checks: structure, duplicate stems, and syllabus trace inventory.
seen_stems = set()
for n in range(1, 7):
    source = (root / '11-mock-exams' / f'mock-0{n}-exam.md').read_text(encoding='utf-8')
    foundation = source.split('# Part 2')[0]
    segments = re.split(r'(?=^\*\*Q\d+\.\*\*)', foundation, flags=re.M)[1:]
    check(len(segments) == 40, f'Mock {n}: expected 40 Q blocks')
    for i, question in enumerate(segments, 1):
        head = re.search(r'^\*\*Q(\d+)\.\*\*\s+([^\n]+)', question)
        check(bool(head) and int(head[1]) == i, f'Mock {n}: malformed question {i}')
        if head:
            stem = re.sub(r'\s+', ' ', head[2].casefold()).strip()
            check(stem not in seen_stems, f'Mock {n} Q{i}: repeated question stem')
            seen_stems.add(stem)
        labels = re.findall(r'(?:^|\n| {2})([ABCD])\.\s+', question)
        check(labels == list('ABCD'), f'Mock {n} Q{i}: wrong choices {labels}')

trace = (root / '14-official-sources' / '06-x2202-learning-outcome-traceability.md').read_text(encoding='utf-8')
outcomes = re.findall(r'^\| (L[12])\.(\d+)\.(\d+) \|', trace, re.M)
check(len(outcomes) == 131 and len(set(outcomes)) == 131, f'X2202 outcomes: {len(outcomes)} distinct rows, expected 131')
for path in re.findall(r'\[Cours\]\(\.\./([^)]*)\)', trace):
    check((root / path).is_file(), f'X2202 references missing source file: {path}')

advanced_f = (root / '09-foundation-question-bank' / '09-advanced-drills.md').read_text(encoding='utf-8')
advanced_p = (root / '10-practitioner-scenarios' / '09-advanced-multi-constraint-scenarios.md').read_text(encoding='utf-8')
check(len(re.findall(r'^## F\d\d\b', advanced_f, re.M)) == 24, 'Advanced Foundation: 24 expected')
check(len(re.findall(r'^## A\d\d\b', advanced_p, re.M)) == 8, 'Advanced Practitioner: 8 expected')

print('Foundation', len(fids), Counter(fanswers))
print('Practitioner', len(pids), Counter(pbest))
print('6 Combined mock exams checked')
if errors:
    for error in errors:
        print('FAIL', error, file=sys.stderr)
    sys.exit(1)
print('PASS static structure only; a human semantic and X2202 audit remains necessary')
