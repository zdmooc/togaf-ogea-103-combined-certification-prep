#!/usr/bin/env python3
"""Extra pedagogical integrity checks. Does not establish external exam calibration."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
failures = []
def check(ok, detail):
    if not ok:
        failures.append(detail)

def read(path):
    return (ROOT / path).read_text(encoding="utf-8")

def blocks(text, pat):
    return re.split(rf"(?=^{pat})", text, flags=re.M)[1:]

def grades(raw):
    return {l: int(n) for l, n in re.findall(r"([ABCD])=(\d)", raw)}

def verify_grades(scores, source):
    check(set(scores) == set("ABCD") and sorted(scores.values()) == [0,1,3,5],
          f"{source}: must have a distinct 5/3/1/0 choice")
    return set(scores) == set("ABCD")

def options(text, source):
    choices = re.findall(r"^([ABCD])\.\s+(.+)$", text, flags=re.M)
    check([l for l, _ in choices] == list("ABCD"), f"{source}: options A to D missing/duplicated")
    return {l: value for l, value in choices}

# Standalone Practitioner bank: check all 60 choices against their local explanations.
count = 0
for file in sorted((ROOT / "10-practitioner-scenarios").glob("0[1-8]-*s*.md")):
    for section in blocks(file.read_text(encoding="utf-8"), r"## S\d+ — "):
        id_match = re.match(r"## (S\d+)", section)
        ident = id_match[1] if id_match else "UNKNOWN"
        a = re.search(r"\*\*Scoring\s*:\s*([^*\n]+)\*\*", section)
        score = grades(a[1]) if a else {}
        if verify_grades(score, ident):
            for letter, points in score.items():
                check(bool(re.search(rf"^\s*-\s*\*\*{letter}\s*(?:[—–-]\s*{points}\b|,\s*{points}\s*points?|\(\s*{points}\s*\))", section, flags=re.M)),
                      f"{ident}: explanation for {letter}={points} missing")
        options(section.split("**Scoring")[0], ident)
        count += 1
check(count == 60, f"Expected 60 Practitioner scenarios, found {count}")

# Combined mocks: 8 scenarios with 4 options + 4 graded explanations each.
for n in range(1, 7):
    exam = read(f"11-mock-exams/mock-0{n}-exam.md").split("# Part 2")[1]
    correction = read(f"11-mock-exams/corrections/mock-0{n}-correction.md").split("# Part 2")[1]
    es = blocks(exam, r"## P\d+ — ")
    cs = blocks(correction, r"## P\d+ — ")
    check(len(es)==8 and len(cs)==8, f"Mock {n}: expected 8 case/correction blocks")
    for i in range(min(len(es), len(cs))):
        a,b = es[i],cs[i]
        ident=f"Mock {n} P{i+1}"
        options(a, ident)
        m = re.search(r"\*\*(?:Barème|Scoring)\s*:\*\*\s*([^\n]+)", b)
        scores=grades(m[1]) if m else {}
        if verify_grades(scores,ident):
            for letter, points in scores.items():
                check(bool(re.search(rf"^\s*-\s*\*\*{letter}\s*(?:[—–-]\s*{points}\b|,\s*{points}\s*points?|\(\s*{points}\s*\))",b,re.M)),
                      f"{ident}: explanation for {letter}={points} missing")

# Targeted cases XP01..XP32 and dedicated corrections.
s1=read("10-practitioner-scenarios/10-x2202-targeted-cases.md")
s2=read("10-practitioner-scenarios/11-x2202-gap-closure-scenarios.md")
c1=read("10-practitioner-scenarios/10-x2202-targeted-cases-corrections.md")
c2=read("10-practitioner-scenarios/11-x2202-gap-closure-corrections.md")
case_sections = {}
correction_sections = {}
for text in (s1,s2):
    for b in blocks(text, r"## XP\d\d\b"):
        ident=re.match(r"## (XP\d\d)", b)[1]
        check(ident not in case_sections, f"Duplicate targeted case {ident}")
        case_sections[ident]=b
for text in (c1,c2):
    for b in blocks(text, r"## XP\d\d\b"):
        ident=re.match(r"## (XP\d\d)", b)[1]
        check(ident not in correction_sections, f"Duplicate targeted correction {ident}")
        correction_sections[ident]=b
expected={f"XP{i:02d}" for i in range(1,33)}
check(set(case_sections)==expected and set(correction_sections)==expected,
      f"XP inventory mismatch: cases={len(case_sections)} corrections={len(correction_sections)}")
for ident in sorted(expected):
    a=case_sections.get(ident, "")
    b=correction_sections.get(ident, "")
    options(a, ident)
    m=re.search(r"(?:Barème pédagogique|Barème)\s*:\*\*\s*([^\n]+)",b)
    if ident in {"XP01","XP02","XP03","XP04"}:
        m=re.search(r"^## XP\d\d — ([^\n]+)",b)
    scores=grades(m[1]) if m else {}
    if verify_grades(scores,ident):
        for letter in "ABCD":
            # XP01-04 use **A (5)**, XP05-32 use **A, 5 points**
            check(bool(re.search(rf"\*\*{letter}\s*(?:\({scores[letter]}\)|[,—–]\s*{scores[letter]}\s*points?)",b)),
                  f"{ident}: missing separate reasoning for {letter}")
                
# Two extra Foundation drills with answer keys.
exercise=read("09-foundation-question-bank/10-x2202-targeted-drills.md")
answers=read("09-foundation-question-bank/10-x2202-targeted-drills-corrections.md")
for name in ("XF01","XF02"):
    check(bool(re.search(rf"^## {name}\b",exercise,re.M)), f"{name}: exercise missing")
    check(bool(re.search(rf"^## {name}\s+—\s+[ABCD]\b",answers,re.M)), f"{name}: correction missing")

print(f"Reviewed structurally: {count} S-cases, 48 mock cases, 32 XP targeted, 2 XF")
if failures:
    for failure in failures:
        print("FAIL", failure, file=sys.stderr)
    sys.exit(1)
print("PASS: all scoring rubrics have four distinct choices and explanations; semantic review remains necessary")
