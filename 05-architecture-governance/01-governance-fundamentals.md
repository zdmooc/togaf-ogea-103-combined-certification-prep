# Architecture Governance — Fundamentals

## 1. Definition

**Architecture Governance** organise la manière dont les décisions d’architecture sont prises, approuvées, appliquées, contrôlées et réévaluées.

Elle ne consiste pas simplement à créer un comité. Elle fournit les règles, responsabilités, mécanismes de décision, critères de conformité, processus d’escalade et preuves permettant de maintenir l’intégrité de l’architecture.

Le raisonnement de base est :

**Principles → Decisions → Standards / Requirements → Implementation → Compliance → Exception / Remediation → Evidence**.

## 2. Pourquoi la gouvernance existe

Sans gouvernance, une architecture cible peut être correctement conçue mais se dégrader pendant l’exécution :

- chaque équipe choisit sa propre solution ;
- les principes ne sont pas appliqués ;
- des déviations apparaissent sans décision explicite ;
- les risques sont acceptés implicitement ;
- les dépendances inter-projets sont ignorées ;
- les décisions deviennent impossibles à retracer ;
- le portefeuille dérive progressivement loin de la Target Architecture.

La gouvernance sert donc à préserver l’intention d’architecture pendant toute la transformation.

## 3. Architecture Governance vs Project Governance

| Architecture Governance | Project Governance |
|---|---|
| cohérence architecturale | budget, délai, ressources |
| principes et standards | plan projet |
| conformité à la cible | exécution du projet |
| décisions d’architecture | décisions de delivery |
| exceptions architecturales | risques projet |

Les deux sont complémentaires mais ne sont pas interchangeables.

## 4. Architecture Governance vs Corporate Governance

La **Corporate Governance** couvre la gouvernance globale de l’organisation. L’Architecture Governance s’inscrit à l’intérieur de ce dispositif plus large.

Une bonne Architecture Governance doit donc être cohérente avec :

- stratégie ;
- gestion des risques ;
- sécurité ;
- conformité ;
- finance ;
- portfolio governance ;
- change governance.

## 5. Mécanismes typiques

Une organisation peut utiliser :

- Architecture Board ;
- Architecture Principles ;
- standards et reference architectures ;
- Architecture Contracts ;
- Architecture Compliance Reviews ;
- decision records ;
- waiver / exception process ;
- architecture repositories ;
- review gates ;
- escalation paths.

TOGAF fournit un cadre. Chaque entreprise doit adapter ces mécanismes à son contexte.

## 6. Où intervient la gouvernance dans l’ADM

La gouvernance n’existe pas uniquement en Phase G.

### Preliminary

On met en place la capacité, les rôles, règles, principes et mécanismes de gouvernance.

### A à F

On gouverne les décisions, les arbitrages, le scope, les standards, les gaps et la roadmap.

### Phase G

La gouvernance devient particulièrement visible pendant l’implémentation : conformité à la Target Architecture, gestion des déviations, Architecture Contracts et reviews.

### Phase H

On gouverne les changements de l’Architecture Landscape et on décide si un nouveau cycle ADM est nécessaire.

## 7. Accountability et Responsibility

Un bon dispositif distingue :

- qui **prépare** une décision ;
- qui **recommande** ;
- qui **approuve** ;
- qui **exécute** ;
- qui **contrôle** ;
- qui **accepte le risque**.

L’erreur classique est de faire de l’architecte le propriétaire de toutes les décisions. L’architecte structure et éclaire la décision ; la responsabilité finale peut appartenir à un sponsor, une Architecture Board, un risk owner ou une autre autorité.

## 8. Governance repository

La gouvernance doit laisser des traces exploitables :

- décisions ;
- principes ;
- standards ;
- modèles de conformité ;
- exceptions ;
- preuves de revue ;
- Architecture Contracts ;
- plans de remédiation.

Sans ces éléments, il devient difficile de comprendre pourquoi une architecture existe sous sa forme actuelle.

## 9. Exemple MayaBank

MayaBank modernise sa plateforme de paiement.

Principes retenus :

- API-first ;
- encryption by default ;
- observability built-in ;
- reuse before custom build ;
- automated deployment.

Pendant l’implémentation, une équipe veut utiliser un stockage local non redondé pour gagner du temps.

La gouvernance doit permettre de :

1. détecter la déviation ;
2. comprendre la justification ;
3. évaluer le risque ;
4. accepter, refuser ou encadrer l’exception ;
5. enregistrer la décision ;
6. fixer éventuellement une date de remédiation.

## 10. Pièges OGEA-103

### Piège 1 — Governance ≠ documentation

Produire des documents n’est pas gouverner. La gouvernance porte sur les décisions, responsabilités, conformité et preuves.

### Piège 2 — Governance ≠ Phase G uniquement

Phase G est le point fort de l’implementation governance, mais les mécanismes existent dès Preliminary.

### Piège 3 — Architecture Governance ≠ Project Governance

Une décision de budget ou de planning n’est pas automatiquement une décision d’architecture.

## 11. Foundation questions

### Q1
+Quel est l’objectif principal de l’Architecture Governance ?
+
+A. Produire tous les diagrammes
+B. Maintenir la cohérence, la conformité et la traçabilité des décisions d’architecture
+C. Gérer uniquement le budget
+D. Choisir les produits
+
+**Réponse : B.**
+
+### Q2
+La gouvernance d’architecture commence principalement :
+
+A. seulement en Phase G
+B. dès Preliminary, puis continue pendant le cycle ADM
+C. après la mise en production
+D. uniquement en Phase H
+
+**Réponse : B.**
+
+## 12. Practitioner scenario
+
+Un projet respecte son budget et son planning, mais déploie une solution qui viole plusieurs principes d’architecture approuvés. La meilleure réponse n’est pas « le projet est réussi ». Il faut déclencher le mécanisme de gouvernance architecturale : review, analyse de conformité, décision sur la déviation et remédiation éventuelle.
+
+## 13. English for Architects
+
+> Architecture governance ensures that architecture decisions are applied consistently and that deviations are explicitly reviewed and managed.
+
+## 14. Key points to remember
+
+- Governance = décisions + responsabilités + conformité + preuves.
+- Elle commence dès Preliminary.
+- Phase G renforce l’implementation governance.
+- Project Governance et Architecture Governance sont complémentaires.
+- Une déviation doit être explicite, évaluée et traçable.
+
+---
+
+Official baseline: TOGAF Standard, 10th Edition — Enterprise Architecture Capability and Governance. Original educational explanation.