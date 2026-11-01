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

# Ensure every assessable X2202 objective points to an existing precise item.
foundation_drills = (root / '09-foundation-question-bank' / '10-x2202-targeted-drills.md').read_text(encoding='utf-8')
practitioner_cases = (root / '10-practitioner-scenarios' / '10-x2202-targeted-cases.md').read_text(encoding='utf-8')
foundation_targeted = set(re.findall(r'^## (XF\d\d)\b', foundation_drills, re.M))
practitioner_targeted = set(re.findall(r'^## (XP\d\d)\b', practitioner_cases, re.M))
advanced_targeted_cases = (root / '10-practitioner-scenarios' / '11-x2202-gap-closure-scenarios.md').read_text(encoding='utf-8')
advanced_targeted = set(re.findall(r'^## (XP\d\d)\b', advanced_targeted_cases, re.M))
check(advanced_targeted == {f'XP{i:02d}' for i in range(5, 33)}, f'Expected 28 XP05–XP32 cases: {advanced_targeted}')
check(foundation_targeted == {'XF01', 'XF02'}, f'Unexpected Foundation targeted drills: {foundation_targeted}')
check(practitioner_targeted == {'XP01', 'XP02', 'XP03', 'XP04'}, f'Unexpected Practitioner targeted cases: {practitioner_targeted}')
practitioner_targeted |= advanced_targeted

for row in re.findall(r'^\| L[12]\.\d+\.\d+ \|[^\n]+$', trace, re.M):
    cells = [c.strip() for c in row.split('|')[1:-1]]
    if len(cells) != 5:
        check(False, f'Trace malformed: {row}')
        continue
    objective, notion, course, exercises, review = cells
    if objective == 'L1.8.1':
        check('Bloom None' in exercises, 'L1.8.1 must retain its official None/untested status')
        check('Bloom officiel : None' in review, 'L1.8.1 must show Bloom None in audit')
        continue
    check('Candidat précis' in review, f'{objective}: not associated with a precise candidate')
    check('Bloom officiel :' in review, f'{objective}: missing official Bloom level annotation')
    refs = re.findall(r'\b(XF\d\d|XP\d\d|[QSFA]\d{2,3})\b', exercises)
    check(len(refs) > 0, f'{objective}: no specific question or scenario')
    for reference in refs:
        if reference.startswith('XF'):
            check(reference in foundation_targeted, f'{objective}: missing targeted item {reference}')
        elif reference.startswith('XP'):
            check(reference in practitioner_targeted, f'{objective}: missing targeted item {reference}')
        elif reference.startswith('Q'):
            check(1 <= int(reference[1:]) <= 300, f'{objective}: invalid Foundation ID {reference}')
        elif reference.startswith('S'):
            check(1 <= int(reference[1:]) <= 60, f'{objective}: invalid Practitioner ID {reference}')
        elif reference.startswith('F'):
            check(1 <= int(reference[1:]) <= 24, f'{objective}: invalid advanced Foundation ID {reference}')
        elif reference.startswith('A'):
            check(1 <= int(reference[1:]) <= 8, f'{objective}: invalid advanced Practitioner ID {reference}')

advanced_f = (root / '09-foundation-question-bank' / '09-advanced-drills.md').read_text(encoding='utf-8')
advanced_p = (root / '10-practitioner-scenarios' / '09-advanced-multi-constraint-scenarios.md').read_text(encoding='utf-8')
check(len(re.findall(r'^## F\d\d\b', advanced_f, re.M)) == 24, 'Advanced Foundation: 24 expected')
check(len(re.findall(r'^## A\d\d\b', advanced_p, re.M)) == 8, 'Advanced Practitioner: 8 expected')


# Detect answer-length cues, which make practice questions guessable.
foundation_files = sorted((root / '09-foundation-question-bank').glob('0[1-8]-*q*.md'))
lengths = []
for file in foundation_files:
    content = file.read_text(encoding='utf-8')
    questions = re.split(r'(?=^## Q\d+ — )', content, flags=re.M)[1:]
    for question in questions:
        key = re.search(r'\*\*Réponse\s*:\s*([ABCD])\.\*\*', question)
        choices_text = question.split('**Réponse')[0]
        opts = dict(re.findall(r'^([ABCD])\.\s+([^\n]+)', choices_text, re.M))
        if not key or set(opts) != set('ABCD'):
            check(False, f'{file}: cannot score choice lengths')
            continue
        correct = len(opts[key[1]])
        other_mean = sum(len(v) for k, v in opts.items() if k != key[1]) / 3.0
        lengths.append((correct, other_mean, max(len(x) for x in opts.values())))
if len(lengths) == 300:
    longest_share = sum(a == mx for a, other, mx in lengths) / len(lengths)
    extreme_count = sum(a > 2.0 * other for a, other, mx in lengths)
    average_ratio = sum(a / other for a, other, mx in lengths) / len(lengths)
    check(longest_share <= 0.40,
          f'Answer-length cue: correct option is longest {longest_share:.1%}, threshold 40%')
    check(extreme_count == 0, f'Answer-length cue: {extreme_count} options > 2x distractor mean')
    check(average_ratio <= 1.35,
          f'Answer-length cue: mean correct/distractor length ratio {average_ratio:.2f}, limit 1.35')
    print(f'Answer-length QA: longest={longest_share:.1%}, mean ratio={average_ratio:.2f}, >2x={extreme_count}')
else:
    check(False, f'Answer-length QA parsed {len(lengths)} of 300 questions')


# Also detect the reverse cue in combined mocks: correct choice systematically shortest.
mock_lengths = []
for n in range(1, 7):
    exam = (root / '11-mock-exams' / f'mock-0{n}-exam.md').read_text(encoding='utf-8')
    correction = (root / '11-mock-exams' / 'corrections' / f'mock-0{n}-correction.md').read_text(encoding='utf-8')
    keys = {int(i): l for i, l in re.findall(r'^(\d+)\.\s+\*\*([ABCD])\*\*', correction, re.M)}
    foundation = exam.split('# Part 2')[0]
    blocks = re.split(r'(?=^\*\*Q\d+\.\*\*)', foundation, flags=re.M)[1:]
    for block in blocks:
        header = re.search(r'^\*\*Q(\d+)\.\*\*', block)
        if not header or int(header[1]) not in keys:
            check(False, f'Mock {n} has missing Foundation answer key')
            continue
        qid = int(header[1])
        options_line = next((line for line in block.splitlines() if line.startswith('A. ')), '')
        opts = dict(re.findall(r'(?:^| {2})([ABCD])\.\s+(.+?)(?= {2}[ABCD]\.\s+|$)', options_line))
        if len(opts) != 4:
            check(False, f'Mock {n} Q{qid}: failed to parse all four options for length analysis')
            continue
        lengths = {l: len(v.strip()) for l, v in opts.items()}
        correct_len = lengths[keys[qid]]
        other_mean = sum(v for l, v in lengths.items() if l != keys[qid]) / 3
        mock_lengths.append((correct_len, other_mean, min(lengths.values())))
if len(mock_lengths) == 240:
    shortest_share = sum(a == short for a, other, short in mock_lengths) / 240
    mean_ratio = sum(a / other for a, other, short in mock_lengths) / 240
    check(shortest_share <= 0.45,
          f'Mock reverse answer-length cue: shortest answer {shortest_share:.1%}')
    check(0.80 <= mean_ratio <= 1.30,
          f'Mock reverse answer-length ratio {mean_ratio:.2f}')
    print(f'Mock answer-length QA: shortest={shortest_share:.1%}, mean ratio={mean_ratio:.2f}')
else:
    check(False, f'Mock answer-length QA parsed {len(mock_lengths)}/240')

print('Foundation', len(fids), Counter(fanswers))
print('Practitioner', len(pids), Counter(pbest))
print('6 Combined mock exams checked')
print('X2202: 130 candidate assessments + 1 non-assessed objective')
if errors:
    for error in errors:
        print('FAIL:', error, file=sys.stderr)
    sys.exit(1)
print('PASS: static integrity only; independent semantic review still required')
