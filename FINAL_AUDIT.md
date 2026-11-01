# Mise à jour — contre-audit Perplexity (01/11/2026)

Le contrôle des seules structures effectué avant la première fusion n'avait pas détecté des erreurs de correction, des indices de bonne réponse et des barèmes de cas peu discriminants. Une seconde remédiation est décrite dans `14-official-sources/07-perplexity-followup-semantic-audit.md`. Les examens restent des **simulations pédagogiques non étalonnées** et non des sujets officiels. **Ne pas interpréter les tests CI verts comme une validation sémantique indépendante de l'intégralité des questions.**

---

# Bilan de remédiation TOGAF X2202 — 1er novembre 2026

**Statut : publication possible comme support indépendant d'autoformation.** Les contrôles automatisés de structure, de barème et de traçabilité ont été renforcés et passent sur la branche de correction. **Ce statut n'est pas une accréditation, un audit pédagogique indépendant, une validation psychométrique ou une garantie de réussite.** La fusion éventuelle de la PR #2 correspond à une publication interne du contenu, non à une certification du support.

## Résultats établis

| Dimension | Résultat démontré | Limite |
|---|---|---|
| Syllabus X2202 | 131 objectifs inventoriés, Bloom transcrits et 130 associations candidates vers des questions précises (L1.8.1 non évalué séparément) | La pertinence cognitive de toutes les associations n'a pas été revue indépendamment |
| Foundation | 300 QCM, 75 bonnes réponses par lettre, corrigés ; 24 QCM avancés et 2 QCM ciblés | La qualité et la difficulté de chaque distracteur ne sont pas certifiées |
| Livrables Foundation 7.3 | 16 livrables explicitement décrits dans `06-architecture-content/03-deliverables.md`, 16 QCM dédiés D01–D16 et corrigés | Repères de phases indicatifs, l'ADM étant itératif |
| Practitioner | 60 scénarios S et 32 cas ciblés XP, avec justifications 5/3/1/0 | Les classements restent pédagogiques, pas issus d'un étalonnage officiel |
| Examens blancs | 6 × (40 Foundation + 8 Practitioner), corrigés ; aucun intitulé identique ; contrôle lexical inter-examens | Deux sujets peuvent encore évaluer le même concept ; variété psychométrique non garantie |
| Contrôle automatisé | `scripts/validate_togaf_banks.py` et `scripts/validate_pedagogical_consistency.py` exécutés par GitHub Actions | La CI vérifie des propriétés vérifiables, non la vérité de toutes les explications |
| Longueur des réponses | Foundation : bonne réponse la plus longue 34 %, ratio moyen 1,12, aucune > 2× ; mocks : plus courte 38 %, ratio moyen 1,03 | Une longueur équilibrée ne prouve pas une difficulté réaliste |

## Vérifications documentaires

- **Source normative :** The Open Group, `X2202`, version 4.0, avril 2022, sections 3.1 et 3.2.
- **L1 7.3 :** l'énumération officielle comporte **16 livrables**. Le document de cours a été complété à partir de cette liste et les 16 items ont une question dédiée.
- **L1 7.3 — Bloom :** le PDF officiel affiche le libellé atypique `2_Remembering` ; il est conservé tel quel, sans prétendre qu'il s'agit d'une valeur standard de Bloom.
- **L1 2.1 :** `Digital Architecture` a été ajouté au glossaire, conformément à la liste officielle. Le syllabus précise que les définitions de cette unité ne sont pas examinables séparément sauf si reprises dans un autre objectif.
- **L2 8.5 :** les sept rubriques officielles de l'Architecture Repository ont été rétablies ; les synonymes issus d'autres représentations ne constituent pas une huitième rubrique.
- **Examens en français :** OGEA-F101 et OGEA-F102 figurent dans le tableau officiel Pearson VUE ; il n'y figure pas de Combined français. Vérifier le système de réservation pour les options en vigueur.

## Revue des répétitions

La recherche a été menée sur les 240 questions Foundation des six examens après retrait de leurs introductions génériques. Les paires de formulations modérément similaires examinées concernent en général des distinctions proches mais non identiques (p. ex. Catalog/Matrix/Diagram, Baseline/Target, Data/Application). Le contrôle de CI bloque désormais des formulations presque identiques à travers les examens, mais **ne sait pas mesurer l'équivalence sémantique comme un relecteur spécialiste**.

## Points à contrôler avant de prétendre à une conformité pédagogique indépendante

1. Relecture indépendante, **question par question**, des 300 QCM Foundation, des 60 scénarios Practitioner, des 48 scénarios des mocks et des exercices ajoutés.
2. Contrôle de chaque association parmi les 130 objectifs évaluables au regard du texte exact X2202, des KLP et du niveau Bloom ; une référence précise reste une **preuve candidate** et non une validation de maîtrise.
3. Essais chronométrés par des personnes externes, comparaison de difficulté avec des supports officiels autorisés et test de navigation Open Book.
4. Vérification des dernières conditions Pearson VUE au moment de l'inscription.

**Décision de maintenance :** les contrôles CI réussis peuvent permettre la fusion des ressources d'autoformation dans `main` ; les quatre actions ci-dessus sont des exigences de validation externe, non des tâches que des tests statiques pourraient clore à eux seuls.

---

## Audit historique (6 septembre 2026) — archivé pour traçabilité

Le verdict `READY` ci-dessous est **historique, remplacé** par le statut ci-dessus. Il ne doit pas être repris comme une attestation de qualité officielle.

# FINAL AUDIT — TOGAF OGEA-103 Combined Certification Prep

Audit date: **2026-09-06**

## 1. Final verdict

**STATUS: READY FOR SERIOUS OGEA-103 SELF-STUDY AND EXAM PREPARATION**

This verdict means the repository now provides a coherent, end-to-end learning and practice path aligned to the current public TOGAF Standard, 10th Edition certification syllabus and exam structure.

It does **not** mean guaranteed exam success, official accreditation, or equivalence to The Open Group's official study materials.

## 2. Official baseline re-verified

Current public official information confirms:

- certification syllabus: **X2202**;
- OGEA-101: 40 questions, 60 minutes, 60% pass mark;
- OGEA-101 distribution: 8 Concepts / 14 ADM / 6 ADM Techniques / 4 Applying ADM / 3 Governance / 5 Architecture Content;
- OGEA-102: 8 scenario-based questions, 90 minutes, 60% pass mark;
- Practitioner gradient scoring: 5 / 3 / 1 / 0;
- Part 2 open-book access through `REFERENCE`;
- current open-book content: TOGAF Fundamental Content + Applicable TOGAF Series Guides.

See `14-official-sources/` for links and policy notes.

## 3. Final repository coverage

### Core learning

- `01-togaf-foundations/` — core concepts and terminology
- `02-adm/` — full ADM, Preliminary through H + Requirements Management + iteration
- `03-adm-techniques/` — stakeholder management, business scenarios, gaps, readiness, risk, migration and supporting techniques
- `04-applying-the-adm/` — tailoring, iteration, levels, partitioning, security, digital, Agile, large enterprise
- `05-architecture-governance/` — Board, Contract, Compliance Reviews, deviations and exceptions
- `06-architecture-content/` — deliverables, artifacts, building blocks, ABB/SBB, views/viewpoints, catalogs/matrices/diagrams

### Practitioner application

- `07-practitioner/` — scenario reasoning, answer elimination, scoring and open-book strategy
- `08-mayabank-case-study/` — complete fictional case Preliminary → H with Requirements and roadmap

### Practice

- `09-foundation-question-bank/` — **300 original Foundation questions**, Q001 → Q300
- `10-practitioner-scenarios/` — **60 original Practitioner scenarios**, S001 → S060
- `11-mock-exams/` — **6 Combined mocks**, each 40 Foundation + 8 Practitioner, with separate corrections

### Revision and professional extension

- `12-cheat-sheets/` — **13 rapid revision sheets**
- `13-english-for-architects/` — interview, speaking/listening and architecture communication practice
- `14-official-sources/` — official source map, exam policies, X2202-to-repository mapping and study boundaries

## 4. Syllabus coverage verdict

### Foundation

All six public OGEA-101 exam-plan categories have dedicated teaching and dedicated practice material.

**Verdict: COVERED.**

### Practitioner

All eight major public OGEA-102 syllabus areas have dedicated Practitioner teaching and dedicated scenario practice.

**Verdict: COVERED.**

### Combined

The repository provides six complete simulations using the public Part 1 and Part 2 structures, with independent section scoring.

**Verdict: COVERED FOR SELF-STUDY SIMULATION.**

## 5. Structural quality checks

Checks performed during final audit:

- no `TODO`, `TBD`, `placeholder` or `coming soon` marker found in the repository search;
- no obvious `TOGAF 9` residue found in target learning content;
- no artificial legacy duplicate pattern such as `variante 2/3/4/5` found;
- final Foundation endpoint **Q300** verified in the actual file;
- final Practitioner endpoint **S060** verified in the actual file;
- current repository tree contains the complete learning path through `13-english-for-architects/` before final source files are added;
- no empty placeholder directories were intentionally introduced.

### Duplicate-control limitation

The audit did not run a mathematical semantic-similarity analysis across every sentence/question. Therefore the correct claim is:

**no obvious synthetic duplicate pattern was detected**, not "every question is provably semantically unique".

## 6. High-risk confusion pairs

The repository explicitly teaches and revises the major confusion pairs identified in Iteration 0:

- Preliminary / Phase A
- Phase A / Phase B
- C Data / C Application
- Phase D / Phase E
- Phase E / Phase F
- Phase F / Phase G
- Phase G / Phase H
- Phase H / Requirements Management
- Baseline / Target / Transition
- Deliverable / Artifact / Building Block
- ABB / SBB
- View / Viewpoint
- Catalog / Matrix / Diagram
- Repository / Enterprise Continuum
- Principle / Requirement
- Vision / Target
- Architecture Roadmap / Implementation & Migration Plan
- Architecture Governance / project governance
- Architecture Board / Architecture Team
- Requirement / Constraint
- Capability / Application
- Business Architecture / Solution Architecture

**Verdict: COVERED.**

## 7. What is intentionally not claimed

This repository does not claim:

- official accreditation;
- official exam questions;
- leaked or reconstructed live items;
- identical live-exam difficulty;
- guaranteed pass probability;
- replacement of official TOGAF publications;
- that OpenShift, Kafka, GitOps, APIs or any specific technology is mandated by TOGAF;
- that the English-for-Architects block is part of X2202.

## 8. Recommended study path

### Stage 1 — Learn

Study `01` through `06`, then use `12-cheat-sheets/` only as reinforcement.

### Stage 2 — Apply

Study `07-practitioner/` and work through the complete MayaBank case in `08`.

### Stage 3 — Drill

Use:

- `09-foundation-question-bank/`
- `10-practitioner-scenarios/`

Track weak areas by syllabus domain, not only total score.

### Stage 4 — Simulate

Take the six Combined mocks under time constraints, with Part 1 closed book and Part 2 using only the relevant official references.

### Stage 5 — Final revision

Use `12-cheat-sheets/`, then re-check `14-official-sources/` before booking/sitting the exam.

## 9. Internal readiness threshold — not official

A conservative self-study target before attempting the real exam is:

- at least **32/40** on Foundation practice;
- at least **32/40 points** on Practitioner practice;
- both thresholds reached on **three fresh Combined mocks in a row**;
- ability to explain every wrong answer, especially why the 5-point Practitioner answer is better than the 3-point answer.

This 80% internal threshold is a repository recommendation, not an official The Open Group pass mark. The official public pass mark remains 60% per part.

## 10. Final conclusion

The repository has changed from an empty target plus shallow legacy material into a structured self-study course, practice laboratory and interview aid.

From a **coverage and learning-architecture perspective**, it is now ready to be used for OGEA-103 preparation.

The final responsibility before the exam is to combine this repository with the current official TOGAF Body of Knowledge and re-check The Open Group exam policies.
