# Iteration 0 — Audit and OGEA-103 scope

> Audit date: 2026-09-06  
> Target: `zdmooc/togaf-ogea-103-combined-certification-prep`  
> Legacy source: `zdmooc/togaf10-pt1-companion-repo-v3`

## 1. Executive decision

The target repository is currently empty. This is an advantage: the new repository can be designed as a real **TOGAF Enterprise Architecture course + OGEA-103 exam laboratory**, instead of inheriting the structure of the legacy repository.

The legacy repository contains useful raw material, especially question ideas, comparisons, mini-cases, governance/content notes, mock material, and memory aids. However, it must **not** be migrated as-is.

Main decision:

- **REBUILD the learning architecture from the current syllabus.**
- **REUSE ideas, not structure.**
- **VERIFY every TOGAF statement before reuse.**
- **REWRITE core teaching at much greater depth.**
- Explain in clear French while preserving official TOGAF terminology in English.
- Separate **Foundation: Remember / Understand** from **Practitioner: Apply / Analyze**.
- Build Practitioner preparation around scenario reasoning and gradient scoring, not memorization.

The repository must feel like a book that can be studied from page 1, not a repository explaining how to study.

---

## 2. Official examination baseline verified

The following baseline was checked against current The Open Group information on 2026-09-06.

| Area | Verified baseline | Repository consequence |
|---|---|---|
| Certification syllabus | **X2202** for TOGAF Standard, 10th Edition certification learning outcomes | All exam-oriented content must map to X2202 |
| OGEA-103 | Combined Part 1 + Part 2 | Repository prepares for both levels together |
| Part 1 / Foundation | **40 questions**, **60 minutes**, **closed book**, pass mark **60%** | Foundation bank must train recognition, distinctions, terminology, ADM logic |
| Part 1 distribution | Concepts 8; Introduction to ADM 14; ADM Techniques 6; Applying ADM 4; Architecture Governance 3; Architecture Content 5 | Question bank and mocks must respect this weighting |
| Part 2 / Practitioner | **8 scenario-based items**, **90 minutes**, **open book**, pass mark **60%** | Scenarios must test application and analysis |
| Gradient scoring | Best / next / next / distractor = **5 / 3 / 1 / 0** | Every Practitioner scenario must explain all four answer levels |
| Combined structure | **48 items**, **150 minutes** total: 60 + 90 | Combined mocks must reproduce both sections |
| Open book | Part 2 reference is integrated into the exam through **REFERENCE** | Teach fast reference navigation, not dependency on external notes |
| Open-book Body of Knowledge | Provided as TOGAF Fundamental Content plus applicable TOGAF Series Guides | Practitioner section must teach where concepts live and when to consult them |
| Cognitive level | Foundation emphasizes **Remember / Understand**; Practitioner extends to **Apply / Analyze** | Chapters and questions must explicitly distinguish learning level |

### Official sources checked

Primary authoritative sources only:

1. The Open Group — TOGAF Certification Portfolio and exam FAQs  
   https://www.opengroup.org/certifications/togaf-portfolio-faq
2. The Open Group — TOGAF Certification Portfolio  
   https://www.opengroup.org/certifications/togaf-certification-portfolio
3. The Open Group Help Center — syllabus information / X2202  
   https://help.opengroup.org/hc/en-us/articles/32110062987154-Where-Can-I-Find-the-Syllabus-for-TOGAF-Certifications
4. The Open Group Help Center — Part 2 exam plan  
   https://help.opengroup.org/hc/en-us/articles/32158246401042-What-Is-the-Exam-Plan-for-the-OGEA-102-TOGAF-Enterprise-Architecture-Part-2-Exam
5. The Open Group Help Center — Part 2 open-book contents  
   https://help.opengroup.org/hc/en-us/articles/32109993154066-What-Open-Book-Is-Provided-With-the-TOGAF-Enterprise-Architecture-Part-2-Exam
6. The Open Group Help Center — accessing the open book  
   https://help.opengroup.org/hc/en-us/articles/32109966026514-How-Do-I-Access-the-Open-Book-in-an-Open-Book-Exam
7. X2202 — TOGAF Certification Program Conformance Requirements  
   https://www.opengroup.org/library/x2202

Exam facts must be re-checked before the mock-exam/final-revision iterations because policies can change.

---

## 3. Target repository audit

Current state:

- repository exists;
- default branch: `main`;
- no learning content exists yet;
- Iteration 0 should therefore add **only this audit**, not placeholder course files.

Recommendation: do not pre-create empty directories. A directory should appear only when its first substantial learning file is ready.

---

## 4. Legacy repository inventory and disposition

| Legacy area | Decision | Reason / destination |
|---|---|---|
| `README.md` | **REWRITE** | Too focused on study workflow, Git setup, V2/V3 history, trackers; replace with a short entrance to the course |
| `LEGAL_AND_SCOPE.md` | **MERGE / IMPROVE** | Keep only a concise legal/trademark/copyright disclaimer |
| `docs/` | **MERGE + REWRITE** | Useful topic seeds for concepts, ADM, techniques, governance, content, glossary, comparisons; insufficient depth |
| `chapter-notes/` | **REWRITE** | Files called “detailed” are extremely short; concepts need full teaching chapters |
| `chapter-notes/worksheets/` | **DROP** | Low-value meta/practice layer compared with required deep course |
| `daily-plan/` | **DROP** | Study planning is not the repository's purpose |
| `practice/question-bank-v2.*` | **IMPROVE / MERGE** | Useful topic inventory, but many items are short Q&A/reformulations; rebuild into syllabus-mapped Foundation MCQs |
| `practice/deep-drills/` | **MERGE** | Confusion topics are useful; integrate into deep chapters and cheat sheets |
| `mcq/question-bank-mcq.*` | **REWRITE** | Significant repetition/near-duplication; distractors and explanations must be rebuilt |
| `mcq/mcq-mock-exam-*` | **REWRITE / MERGE** | Can provide topic ideas but must not be treated as current Combined mocks |
| `mock-exams/` | **REWRITE** | Existing exams are mostly open-answer study exercises, not 40 MCQ + 8 gradient scenarios |
| `cases/` | **IMPROVE / MERGE** | Useful themes; evolve into MayaBank and Practitioner scenarios |
| `flashcards/` | **MERGE** | Fold useful memory material into final cheat sheets |
| `memory-aids/` | **MERGE** | Keep only accurate high-value mnemonics/recaps after verification |
| `interview-mission/` | **REWRITE / MERGE** | Good intent but too small and Part-1-centric; move to English/interview track |
| `sources/` | **REWRITE** | Replace minimal source list with a current official-source map |
| `trackers/` | **DROP** | Progress logging is not substantive TOGAF learning content |
| `scripts/` | **DROP from learner content** | Recreate only later if technical validation scripts are useful for links/numbering/Markdown checks |

### Important evidence from the legacy audit

1. The legacy README describes a companion/study-plan repository and explicitly emphasizes daily plans, trackers, Git setup, and V2/V3 repository history.
2. `chapter-03-adm-detaillee.md` reduces the ADM largely to a short phase grouping. This is a useful recap but cannot be the main ADM course.
3. The seven “detailed” chapter files are all very small. They do not meet the required depth for major TOGAF concepts.
4. The V2 question bank contains useful concepts, but many explanations are generic and many questions are simple reformulations.
5. The V3 MCQ bank contains repeated questions with almost identical options under “variante 2/3/4/5”. These must be deduplicated, not migrated.
6. Existing mock exams do not reproduce the current OGEA-103 Combined exam structure.
7. The source file is too minimal and does not provide a real X2202 / official-source traceability model.

---

## 5. Major gaps in the legacy repository

### 5.1 Foundation gaps

The new course needs substantially deeper treatment of:

- Enterprise Architecture purpose and value;
- TOGAF structure and core concepts;
- the four architecture domains;
- stakeholders, concerns, views, and viewpoints;
- Architecture Principles;
- Enterprise Continuum;
- Architecture Repository;
- Architecture Capability;
- every ADM phase individually;
- Requirements Management as a cross-cutting process;
- ADM iteration and relationships between phases;
- ADM techniques and when to select each technique;
- tailoring, partitioning, levels of architecture, security, agile/digital context;
- Architecture Governance, Architecture Board, Architecture Contract, compliance, exceptions;
- Architecture Content and the exact distinctions among Deliverable, Artifact, Building Block, ABB, SBB, Catalog, Matrix, Diagram, View, and Viewpoint.

### 5.2 Practitioner gaps

The legacy repository has no adequate end-to-end Practitioner learning path. Missing or insufficient:

- all current Part 2 topic areas;
- systematic scenario interpretation;
- phase recognition from context rather than keywords;
- stakeholder reasoning;
- Requirements Management reasoning;
- governance reasoning;
- sequencing across ADM phases;
- choosing the **best TOGAF answer** rather than merely a technically possible answer;
- full **5 / 3 / 1 / 0** explanation for every scenario;
- open-book navigation strategy using the provided Body of Knowledge;
- realistic long-form scenarios.

### 5.3 Exam-practice gaps

Required target state still missing:

- 300 high-quality original Foundation questions;
- syllabus weighting and topic mapping;
- explanation of every option A/B/C/D;
- 60 original Practitioner scenarios with 5/3/1/0 rationale;
- 6 complete Combined-style mocks;
- separate exam/correction files;
- scoring, weak-area mapping, and timing guidance.

### 5.4 Professional-practice gaps

Missing or too shallow:

- one coherent Enterprise Architecture transformation running across Preliminary through Phase H;
- Baseline → Target → Gap → Work Packages → Transition Architectures → Roadmap → Migration Plan → implementation governance → change management;
- explicit connections to real architecture decisions;
- MayaBank payment/ISO 20022/API/Kafka/Oracle/OpenShift/security/HA-DR context;
- optional ArchiMate professional modelling examples, clearly separated from mandatory TOGAF exam content;
- usable professional English for architecture interviews and presentations.

---

## 6. Final target table of contents

This is the approved target architecture unless official syllabus changes require adjustment.

```text
.
├── README.md
├── AUDIT.md
│
├── 01-togaf-foundations/
│   ├── 01-enterprise-architecture.md
│   ├── 02-what-is-togaf.md
│   ├── 03-core-concepts.md
│   ├── 04-four-architecture-domains.md
│   ├── 05-stakeholders-concerns-views.md
│   ├── 06-architecture-principles.md
│   ├── 07-enterprise-continuum.md
│   ├── 08-architecture-repository.md
│   └── 09-architecture-capability.md
│
├── 02-adm/
│   ├── 00-adm-big-picture.md
│   ├── 01-preliminary-phase.md
│   ├── 02-phase-a-architecture-vision.md
│   ├── 03-phase-b-business-architecture.md
│   ├── 04-phase-c-data-architecture.md
│   ├── 05-phase-c-application-architecture.md
│   ├── 06-phase-d-technology-architecture.md
│   ├── 07-phase-e-opportunities-solutions.md
│   ├── 08-phase-f-migration-planning.md
│   ├── 09-phase-g-implementation-governance.md
│   ├── 10-phase-h-architecture-change-management.md
│   ├── 11-requirements-management.md
│   ├── 12-adm-iteration.md
│   └── 13-adm-complete-flow.md
│
├── 03-adm-techniques/
│   ├── 01-stakeholder-management.md
│   ├── 02-business-scenarios.md
│   ├── 03-gap-analysis.md
│   ├── 04-interoperability.md
│   ├── 05-business-transformation-readiness.md
│   ├── 06-risk-management.md
│   ├── 07-capability-based-planning.md
│   ├── 08-migration-planning-techniques.md
│   └── 09-technique-selection-guide.md
│
├── 04-applying-the-adm/
│   ├── 01-tailoring.md
│   ├── 02-iteration.md
│   ├── 03-levels-of-architecture.md
│   ├── 04-partitioning.md
│   ├── 05-security.md
│   ├── 06-digital-enterprise.md
│   ├── 07-agile-and-togaf.md
│   └── 08-large-enterprise-context.md
│
├── 05-architecture-governance/
│   ├── 01-governance-fundamentals.md
│   ├── 02-architecture-board.md
│   ├── 03-architecture-contract.md
│   ├── 04-compliance-review.md
│   ├── 05-exceptions-and-deviations.md
│   └── 06-governance-scenarios.md
│
├── 06-architecture-content/
│   ├── 01-content-framework.md
│   ├── 02-content-metamodel.md
│   ├── 03-deliverables.md
│   ├── 04-artifacts.md
│   ├── 05-building-blocks.md
│   ├── 06-abb-vs-sbb.md
│   ├── 07-views-viewpoints.md
│   ├── 08-catalogs-matrices-diagrams.md
│   └── 09-common-confusions.md
│
├── 07-practitioner/
│   ├── 00-part2-big-picture.md
│   ├── 01-context-for-enterprise-architecture.md
│   ├── 02-stakeholder-management.md
│   ├── 03-phase-a-scenarios.md
│   ├── 04-phases-bcd-scenarios.md
│   ├── 05-phases-efg-scenarios.md
│   ├── 06-phase-h-scenarios.md
│   ├── 07-requirements-management-scenarios.md
│   ├── 08-supporting-adm-work.md
│   ├── 09-gradient-scoring.md
│   ├── 10-how-to-eliminate-answers.md
│   └── 11-open-book-strategy.md
│
├── 08-mayabank-case-study/
│   ├── 00-context.md
│   ├── 01-preliminary.md
│   ├── 02-phase-a.md
│   ├── 03-phase-b.md
│   ├── 04-phase-c-data.md
│   ├── 05-phase-c-application.md
│   ├── 06-phase-d-technology.md
│   ├── 07-phase-e.md
│   ├── 08-phase-f.md
│   ├── 09-phase-g.md
│   ├── 10-phase-h.md
│   ├── 11-requirements.md
│   └── 12-complete-roadmap.md
│
├── 09-foundation-question-bank/
├── 10-practitioner-scenarios/
├── 11-mock-exams/
│
├── 12-cheat-sheets/
│   ├── 01-adm-one-page.md
│   ├── 02-adm-phases-comparison.md
│   ├── 03-e-vs-f.md
│   ├── 04-g-vs-h.md
│   ├── 05-deliverable-artifact-building-block.md
│   ├── 06-abb-vs-sbb.md
│   ├── 07-view-vs-viewpoint.md
│   ├── 08-repository-vs-continuum.md
│   ├── 09-techniques-map.md
│   ├── 10-governance-map.md
│   ├── 11-foundation-last-day.md
│   ├── 12-practitioner-last-day.md
│   └── 13-english-last-day.md
│
├── 13-english-for-architects/
│   ├── 01-core-togaf-vocabulary.md
│   ├── 02-architecture-verbs.md
│   ├── 03-explain-the-adm-in-english.md
│   ├── 04-present-an-architecture.md
│   ├── 05-describe-a-migration.md
│   ├── 06-discuss-risk-security-governance.md
│   ├── 07-interview-questions.md
│   ├── 08-listening-sentences.md
│   ├── 09-speaking-drills.md
│   └── 10-30-minute-mock-interview.md
│
└── 14-official-sources/
    ├── README.md
    ├── 01-exam-structure.md
    ├── 02-x2202-syllabus-map.md
    └── 03-open-book-reference-map.md
```

The empty directories above are a **target table of contents**, not instructions to create placeholders now.

---

## 7. Learning-content rules for the rebuild

Major chapters will teach concepts through this progression:

**WHY → WHAT → WHEN → WHO → HOW → INPUTS → STEPS → OUTPUTS → RELATIONSHIPS → EXAM TRAPS → REAL EXAMPLE → MAYABANK → QUESTIONS → ENGLISH**

Core rules:

1. Explain relationships, not isolated vocabulary.
2. Every major ADM phase must show what exists before it, what changes during it, and how it feeds the next phase.
3. Distinguish official terminology from explanatory simplifications.
4. Distinguish Foundation knowledge from Practitioner reasoning.
5. Use original explanations and original questions only.
6. No exam dumps and no copied official questions.
7. Do not reproduce substantial copyrighted passages from The Open Group or commercial courses.
8. Use Mermaid only where a diagram teaches something.
9. Use MayaBank as a recurring case, not as a replacement for generic TOGAF teaching.
10. Label ArchiMate material as a professional extension where used.
11. Keep English short, reusable, and architecture-focused.
12. No fake completeness: no shallow placeholder chapters.

---

## 8. Key confusion pairs that must receive dedicated treatment

At minimum:

- Preliminary vs Phase A
- Phase A vs Phase B
- Phase C Data vs Phase C Application
- Phase D vs Phase E
- Phase E vs Phase F
- Phase F vs Phase G
- Phase G vs Phase H
- Phase H vs Requirements Management
- Baseline vs Target vs Transition Architecture
- Deliverable vs Artifact vs Building Block
- ABB vs SBB
- View vs Viewpoint
- Catalog vs Matrix vs Diagram
- Architecture Repository vs Enterprise Continuum
- Architecture Principle vs Requirement
- Architecture Vision vs Target Architecture
- Architecture Roadmap vs Implementation and Migration Plan
- Architecture Governance vs Project Governance
- Architecture Board vs Architecture Team
- Requirement vs Constraint
- Capability vs Application
- Business Architecture vs Solution Architecture

Each comparison should contain a table plus at least one scenario showing why the distinction matters.

---

## 9. Legacy reuse map

The following mapping controls reuse. No file is copied blindly.

| Legacy seed | New destination |
|---|---|
| `docs/03-concepts-cles.md` + `chapter-notes/chapter-02-*` | `01-togaf-foundations/` after verification and major expansion |
| `docs/04-adm-introduction.md` + `chapter-notes/chapter-03-*` | `02-adm/00-adm-big-picture.md` as a seed only |
| `docs/05-adm-techniques-recommandations.md` | `03-adm-techniques/` after restructuring by technique |
| `docs/06-appliquer-adm.md` | `04-applying-the-adm/` |
| `docs/07-gouvernance-architecture.md` | `05-architecture-governance/` |
| `docs/08-cadre-contenu-architecture.md` | `06-architecture-content/` |
| `docs/10-glossaire.md` + `docs/11-tableaux-comparatifs.md` | terminology reinforcement + cheat sheets |
| `cases/*` | MayaBank ideas and Practitioner scenario seeds |
| `practice/question-bank-v2.*` | topic inventory for Foundation bank; questions must be redesigned |
| `mcq/*` | topic inventory only; deduplicate and rebuild distractors/explanations |
| `mock-exams/*` | topic-balance ideas only; rebuild in Combined format |
| `flashcards/*` + `memory-aids/*` | final cheat-sheet material after verification |
| `interview-mission/*` | `13-english-for-architects/` after full rewrite |

---

## 10. Risks and assumptions

| Risk / assumption | Control |
|---|---|
| Exam policies can change | Re-check official sources before exam-bank, mock, and final-revision iterations |
| Legacy content may contain simplifications/errors | Verify each reused concept against the current official Body of Knowledge |
| Large question counts can create repetition | Enforce topic blueprint, unique learning objective, difficulty level, and duplicate review |
| Practitioner items can become ordinary MCQs | Require 5/3/1/0 reasoning and realistic context for every scenario |
| Repository can drift back into meta-content | Apply the quality gate: “Does this teach actual TOGAF?” |
| English could overwhelm TOGAF content | Keep English reinforcement short and subordinate to architecture learning |
| ArchiMate could be mistaken for OGEA-103 mandatory content | Explicitly label it as professional extension |
| Generated volume can create shallow files | Create files only when substantive content is ready |

---

## 11. Iteration 1 implementation plan

### Scope

Create only:

- `README.md`
- complete `01-togaf-foundations/`
- `02-adm/00-adm-big-picture.md`
- `02-adm/01-preliminary-phase.md`
- `02-adm/02-phase-a-architecture-vision.md`

### Implementation order

1. Build an X2202 coverage checklist for the Iteration 1 topics.
2. Write a short README: purpose, certification target, organization, reading order, disclaimer, quick links.
3. Build the nine Foundation chapters with real teaching depth.
4. Build `ADM Big Picture` with the lifecycle logic and Requirements Management interaction.
5. Build `Preliminary Phase` deeply: Architecture Capability, governance, principles, tailoring, roles, repository, readiness.
6. Build `Phase A — Architecture Vision` deeply: scope, stakeholders, concerns, business drivers/goals, value, Architecture Vision, Statement of Architecture Work, risks, approvals, requirements impact.
7. Integrate small MayaBank examples where they clarify the concept.
8. Add concise `English for Architects` sections with reusable sentences.
9. Review Foundation vs Practitioner boundaries and the important confusion pairs introduced in these chapters.
10. Validate Markdown, internal links, Mermaid, terminology, source traceability, and duplicate content.

### Depth target

- `00-adm-big-picture.md`: approximately 2,500–4,000 useful words.
- Preliminary and Phase A: substantial chapters, normally around 1,500–3,000 useful words when the subject warrants it.
- Foundation concept files: enough depth to teach relationships and examples; no forced padding.

### Legacy material eligible for controlled reuse in Iteration 1

Only as verified seeds:

- `docs/02-introduction.md`
- `docs/03-concepts-cles.md`
- `docs/04-adm-introduction.md`
- `docs/10-glossaire.md`
- `docs/11-tableaux-comparatifs.md`
- `chapter-notes/chapter-01-introduction-detaillee.md`
- `chapter-notes/chapter-02-concepts-cles-detaillee.md`
- `chapter-notes/chapter-03-adm-detaillee.md`
- relevant concepts from existing question banks

Everything reused must be fact-checked and rewritten where necessary.

### Iteration 1 quality gates

Before commit:

- current official terminology verified;
- required X2202 topics covered for the implemented scope;
- README remains concise;
- no shallow placeholder files;
- every major chapter explains relationships and practical use;
- Foundation / Practitioner distinction is visible;
- MayaBank examples do not replace generic TOGAF explanations;
- English reinforcement is short and usable;
- no copied exam questions or substantial copyrighted text;
- internal links and Mermaid syntax checked.

Planned commit:

`feat: establish TOGAF foundation and ADM core`

Then stop for repository review before Iteration 2.

---

## 12. Iteration 0 conclusion

The legacy repository should be treated as a **raw source library**, not as the architecture of the new course.

The new repository should be built in this order:

**official syllabus → deep TOGAF teaching → ADM relationships → Practitioner reasoning → MayaBank application → high-quality questions → Combined mocks → English/interview reinforcement → final revision material**.

This directly addresses the central legacy weakness: too much study/repository scaffolding and too little deep, connected TOGAF teaching.
