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

# Foundation 7.3: sixteen distinct deliverables with one answer key per question.
drills=read("09-foundation-question-bank/11-x2202-deliverables-drills.md")
answers=read("09-foundation-question-bank/11-x2202-deliverables-drills-corrections.md")
exercise_sections=blocks(drills,r"## D\d\d\b")
answer_sections=blocks(answers,r"## D\d\d\b")
check(len(exercise_sections)==16 and len(answer_sections)==16,
      f"Deliverable exercises must total 16: {len(exercise_sections)} / {len(answer_sections)}")
for i, exercise_section in enumerate(exercise_sections, 1):
    ident=f"D{i:02d}"
    check(bool(re.match(rf"^## {ident}\b",exercise_section)),f"{ident}: incorrect exercise sequence")
    opts=options(exercise_section, ident)
    if i<=len(answer_sections):
        correction=answer_sections[i-1]
        match=re.match(rf"^## {ident} — ([ABCD])", correction)
        check(bool(match), f"{ident}: missing or incorrect correction header")
        if match:
            check(match[1] in opts, f"{ident}: correction has no corresponding answer")
            check("**Réponse :" in correction, f"{ident}: missing rationale")


# Lexical near-duplicate screen across the six mock exams.
# Strip reusable context prefixes, so the screen examines the actual question.
stems=[]
generic_contexts=(
    "le comité examine les acteurs, états et référentiels pour orienter la transformation.",
    "l'équipe doit choisir les responsabilités et résultats des phases ADM selon le travail déjà effectué.",
    "les architectes hésitent entre plusieurs techniques de diagnostic et de planification.",
    "la gouvernance doit permettre plusieurs équipes et horizons de livraison.",
    "le Board doit différencier arbitrage, conformité et exceptions.",
    "le dossier d'architecture doit distinguer représentations, livrables et building blocks.",
)
for n in range(1,7):
    exam=read(f"11-mock-exams/mock-0{n}-exam.md").split("# Part 2")[0]
    for part in re.split(r"(?=^\*\*Q\d+\.\*\*)",exam, flags=re.M)[1:]:
        head=re.search(r"^\*\*Q(\d+)\.\*\*\s+([^\n]+)",part)
        if not head: 
            continue
        stem=head[2]
        for boilerplate in generic_contexts:
            if boilerplate in stem:
                stem=stem.split(boilerplate,1)[1].strip()
        stems.append((n,int(head[1]),stem))
STOP=set("une un dans pour aux avec cette comme les des dont doit que qui quelle quel quelles est sont comment pourquoi principalement faut entre avant apres architecture architectures adm togaf phase phases le la de du un une et ou est en ce cet les".split())
def terms(value):
    return set(t for t in re.findall(r"[a-z0-9]+",value.casefold()) if len(t)>=4 and t not in STOP)
close=[]
for i, (m1,q1,t1) in enumerate(stems):
    a=terms(t1)
    for m2,q2,t2 in stems[i+1:]:
        if m1==m2: 
            continue
        b=terms(t2)
        common=a&b
        ratio=len(common)/len(a|b) if a|b else 0
        if len(common)>=3 and ratio>=0.78:
            close.append((m1,q1,m2,q2,round(ratio,2)))
check(not close, f"Near-identical mock stems after context removal: {close[:10]}")
print(f"Lexical mock overlap screen: {len(stems)} questions, {len(close)} pairs >= 0.78 (not a semantic-independence proof)")


# Perplexity semantic audit non-regression checks (2026-11-01).
historical_phrases = (
    "Répond aux enjeux structurants, à leur séquencement",
    "Action pertinente mais incomplète, qui reporte",
    "Peut contribuer ponctuellement, mais ne traite",
    "Peut avoir un intérêt dans un autre contexte",
    "Couvre les dépendances, l'ordre des actions",
    "Apporte une avancée réelle mais reporte",
    "Action partielle dont la valeur est limitée",
    "Peut être pertinente sous d'autres hypothèses",
    "L'action traite l'impact global et les responsabilités",
    "Elle apporte une amélioration utile mais n'assure",
    "Peut éclairer une partie du problème",
    "Peut fonctionner dans un autre contexte, mais"
)
for f in sorted((ROOT / "10-practitioner-scenarios").glob("0[1-8]-*s*.md")):
    content=f.read_text(encoding="utf-8")
    for phrase in historical_phrases:
        check(phrase not in content, f"{f.name}: generic 5/3/1/0 explanation persists: {phrase}")

bank = "\n".join(f.read_text(encoding="utf-8") for f in sorted((ROOT/"09-foundation-question-bank").glob("0[1-8]-*q*.md")))
check("B'est" not in bank and "B’est" not in bank,
      "Foundation: misplaced B'est typo or stale letter reference")
q73 = next((b for b in re.split(r"(?=^## Q\d+ — )",bank,flags=re.M) if b.startswith("## Q073 —")), "")
check("Phase A établit l'Architecture Vision" in q73 and "Phase B développe" in q73,
      "Q073: inversion of Phase A/B explanation has regressed")

# Verified semantic corrections from the 300-item Foundation review (2026-11-01).
# These checks protect specific corrected explanations; they are not a semantic oracle.
for ident, expected in (
    ("Q031", "A et B se rapprochent des SBB"),
    ("Q061", "B relève d'une Compliance Review"),
    ("Q062", "A relève de la phase F"),
    ("Q100", "La phase D développe la Technology Architecture"),
    ("Q108", "A désigne Business Architecture (phase B)"),
):
    section = next((b for b in re.split(r"(?=^## Q\d+ — )", bank, flags=re.M)
                    if b.startswith(f"## {ident} —")), "")
    check(expected in section, f"{ident}: verified explanation has regressed")
check("AB Bs" not in bank, "Q284: malformed ABB label has regressed")

all_best=[]
for n in range(1,7):
    correction=read(f"11-mock-exams/corrections/mock-0{n}-correction.md").split("# Part 2")[1]
    gradients=re.findall(r"\*\*(?:Barème|Scoring)\s*:\*\*\s*([^\n]+)",correction)
    best=[next((l for l,v in grades(g).items() if v==5),None) for g in gradients]
    check(len(best)==8 and {letter:best.count(letter) for letter in "ABCD"}==dict.fromkeys("ABCD",2),
          f"Mock {n}: asymmetric Practitioner best-answer positions {best}")
    all_best.extend(best)
check(len(all_best)==48 and {l:all_best.count(l) for l in "ABCD"}==dict.fromkeys("ABCD",12),
      "Combined Practitioner best-answer location remains unbalanced")

repository_course=read("01-togaf-foundations/08-architecture-repository.md")
for label in ("Architecture Landscape","Reference Library","Standards Library","Governance Repository",
              "Architecture Requirements Repository","Solutions Landscape","Enterprise Repository"):
    check(label in repository_course, f"Missing X2202 Repository category: {label}")
check("historically" in repository_course and "Governance Log" in repository_course,
      "Explain why legacy names are not a replacement for X2202 L2 8.5")


# Extra X2202 conformance/migration practice cases.
extra_exams = read('10-practitioner-scenarios/12-conformance-and-migration-xp033-xp036.md')
extra_answers = read('10-practitioner-scenarios/12-conformance-and-migration-corrections.md')
extra_blocks = blocks(extra_exams, r'## XP[0-9]{2}')
extra_keys = blocks(extra_answers, r'## XP[0-9]{2}')
check(len(extra_blocks) == len(extra_keys) == 4, 'Expected 4 XP33–XP36 with corrections')
for i in range(min(len(extra_blocks), len(extra_keys))):
    code = f'XP{i+33:02d}'
    check(extra_blocks[i].startswith('## '+code), code+': wrong exercise ID')
    check(extra_keys[i].startswith('## '+code), code+': wrong correction ID')
    options(extra_blocks[i], code)
    header = re.search(r'\*\*Barème pédagogique\s*:\*\*\s*([^\n]+)', extra_keys[i])
    score = grades(header[1]) if header else {}
    if verify_grades(score, code):
        for label, value in score.items():
            check(bool(re.search(rf'^- \*\*{label}, {value} point',extra_keys[i],re.M)), code+': graded rationale missing for '+label)

# Practitioner semantic-alignment regression checks (2026-11-01).
for path in sorted((ROOT / "10-practitioner-scenarios").glob("0[1-8]-*s*.md")):
    for section in blocks(path.read_text(encoding="utf-8"), r"## S\d+ — "):
        ident = re.match(r"## (S\d+)", section)[1]
        choices = options(section.split("**Scoring")[0], ident)
        rationales = re.findall(r"^- \*\*([ABCD]) — (\d) points? :\*\* (.+)$", section, re.M)
        check(len(rationales) == 4, f"{ident}: expected four complete rationales")
        for letter, score, rationale in rationales:
            check(rationale.startswith(choices.get(letter, "#NO_OPTION#")),
                  f"{ident}: {letter} rationale begins with a stale option")

mock01 = read("11-mock-exams/corrections/mock-01-correction.md")
mock01p5 = next((section for section in blocks(mock01.split("# Part 2")[1], r"## P\d+ — ")
                if section.startswith("## P5 —")), "")
check("**B — 5 points.** La Phase F doit prioriser" in mock01p5,
      "Mock 01 P5: B=5 rationale reverted to the old D answer")
check("**D — 3 points.** Placer les événements en premier" in mock01p5,
      "Mock 01 P5: D=3 rationale reverted to the old B answer")

for n in range(1, 7):
    correction = read(f"11-mock-exams/corrections/mock-0{n}-correction.md")
    for phrase in (
        "Étape utile mais encore insuffisante pour conclure",
        "Traite une partie utile mais ne complète pas l'arbitrage",
        "Une étape utile, mais insuffisante pour l'ensemble des enjeux",
        "Partiellement adapté, avec une dépendance ou décision laissée ouverte",
        "Couvre un aspect secondaire, insuffisant au moment décrit",
        "Contourne la contrainte structurante",
    ):
        check(phrase not in correction,
              f"Mock 0{n}: generic 3/1/0 explanation has returned: {phrase}")

# Targeted non-regression tests from the 240 Foundation mock editorial audit.
mock_foundation_checks = {
    1: {7: ("A", "niveau de disponibilité"), 33: ("B", "Architecture Board"), 35: ("A", "Architecture Compliance Review")},
    2: {22: ("B", "Architecture Roadmap")},
    3: {35: ("C", "Architecture Compliance Review")},
    4: {26: ("A", "Business Transformation Readiness Assessment")},
    5: {21: ("D", "Gap Analysis"), 22: ("C", "Architecture Roadmap"), 33: ("B", "Architecture Board")},
    6: {5: ("C", "Architecture Principle"), 8: ("C", "Gap =")},
}
for n, targeted in mock_foundation_checks.items():
    question_text = read(f"11-mock-exams/mock-0{n}-exam.md").split("# Part 2")[0]
    correction_text = read(f"11-mock-exams/corrections/mock-0{n}-correction.md").split("# Part 2")[0]
    questions = re.split(r"(?=^\*\*Q\d+\.\*\*)", question_text, flags=re.M)
    for number, (letter, expected) in targeted.items():
        q = next((item for item in questions if item.startswith(f"**Q{number}.**")), "")
        choice_match = re.search(rf"(?:^|  ){letter}\. (.*?)(?=  [ABCD]\. |$)", q, re.M)
        check(bool(choice_match and expected in choice_match[1]),
              f"Mock 0{n} Foundation Q{number}: expected {expected} in option {letter}")
        check(bool(re.search(rf"^{number}\. \*\*{letter}\*\* —", correction_text, re.M)),
              f"Mock 0{n} Foundation Q{number}: corrected letter {letter} has regressed")
    check("[X2202, domaine correspondant]" not in correction_text and
          "[X2202, objectifs du domaine concerné]" not in correction_text,
          f"Mock 0{n}: unverifiable generic X2202 placeholder citation")

# Non-régression des incohérences option/justification identifiées par la revue indépendante (2026-11-02).
# Ces assertions ciblent des anomalies démontrées ; elles ne remplacent pas une relecture de fond.
alignment_regressions = {
    "S007": ("Le fournisseur ne peut définir seul la Target métier",),
    "S008": ("Reporter l'étude à la livraison fige le risque d'exploitation",),
    "S015": ("Un backlog sans drivers ne justifie pas le travail d'architecture",),
    "S017": ("Un diagramme technique ne démontre pas la proposition de valeur",),
    "S024": ("Un schéma SQL clarifie le stockage",),
    "S048": ("Un identifiant de ticket ne prouve pas",),
    "S053": ("Un seul diagramme technique n'explique pas",),
    "S056": ("Un score de risque initial seul ne prouve pas",),
    "S059": ("Un composant de solution n'est pas un document",),
}
all_scenarios = {}
for scenario_file in sorted((ROOT / "10-practitioner-scenarios").glob("0[1-8]-*s*.md")):
    for scenario in blocks(scenario_file.read_text(encoding="utf-8"), r"## S\d+ — "):
        match = re.match(r"## (S\d+)", scenario)
        if match:
            all_scenarios[match[1]] = scenario
check(len(all_scenarios) == 60, "S-bank: expected exactly 60 scenarios")
for ident, obsolete_phrases in alignment_regressions.items():
    section = all_scenarios.get(ident, "")
    check(bool(section), f"{ident}: missing from S-bank")
    for obsolete in obsolete_phrases:
        check(obsolete not in section, f"{ident}: obsolete unrelated rationale has returned")

# On vérifie les deux notes intermédiaires, sans contraindre la lettre de la meilleure réponse.
reviewed_grade_pairs = {
    "S009": {"B": 1, "C": 3},
    "S013": {"B": 1, "C": 3},
    "S019": {"A": 3, "D": 1},
    "S020": {"A": 1, "B": 3},
    "S024": {"A": 1, "B": 3},
    "S056": {"A": 1, "B": 3},
}
for ident, expected in reviewed_grade_pairs.items():
    section = all_scenarios.get(ident, "")
    match = re.search(r"\*\*Scoring : ([^\n]+)", section)
    actual = grades(match[1]) if match else {}
    for letter, value in expected.items():
        check(actual.get(letter) == value,
              f"{ident}: expected {letter}={value}, got {actual.get(letter)}")

# Les trois paires jusque-là quasi identiques disposent de caractéristiques distinctives.
for ident, fragments in {
    "S029": ("catalogue", "viewpoint"),
    "S057": ("inventaire des produits", "carte de capabilities"),
    "S059": ("catalogue technique", "Requalifier le diagramme"),
}.items():
    scenario = all_scenarios.get(ident, "")
    check(all(fragment in scenario for fragment in fragments),
          f"{ident}: 1/3 point options have become indistinguishable again")

best_letters = []
for scenario in all_scenarios.values():
    match = re.search(r"\*\*Scoring : ([^\n]+)", scenario)
    score = grades(match[1]) if match else {}
    best_letters.append(next((k for k, v in score.items() if v == 5), None))
check(len(best_letters) == 60 and
      all(best_letters.count(letter) == 15 for letter in "ABCD"),
      "S-bank: 15 best answers per A/B/C/D must be preserved")

repo_section = read("01-togaf-foundations/08-architecture-repository.md").split("## 12. MayaBank example", 1)[-1]
check("think **Standards Library**" in repo_section and "think **Governance Repository**" in repo_section,
      "Architecture Repository: outdated exam trap nomenclature")
for n in range(1, 7):
    mock_quest = read(f"11-mock-exams/mock-0{n}-exam.md")
    check("Standards Information Base" not in mock_quest and "Governance Log" not in mock_quest,
          f"Mock 0{n}: legacy repository labels have returned")
interop = read("03-adm-techniques/04-interoperability.md")
for term in ("Operational or Business Interoperability", "Information Interoperability",
             "Technical Interoperability", "Unstructured Data Exchange", "Seamless Sharing of Information"):
    check(term in interop, f"Interoperability: missing teaching point {term}")

print(f"Reviewed structurally: {count} S-cases, 48 mock cases, 32 XP targeted, 2 XF, 16 deliverable questions")
if failures:
    for failure in failures:
        print("FAIL", failure, file=sys.stderr)
    sys.exit(1)
print("PASS: all scoring rubrics have four distinct choices and explanations; semantic review remains necessary")
