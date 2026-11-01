# Correction — Mock Exam 04

## Barème
Part 1 : /40, réussite simulée ≥24. Part 2 : /40, scoring 5/3/1/0, réussite simulée ≥24.

# Part 1

1. **B** — l'EA relie stratégie, capacités et transformation.
2. **C** — Concern = préoccupation stakeholder.
3. **A** — L'EA apporte une cohérence de changement entre métier, organisation et technologie. [X2202, domaine correspondant].
4. **D** — Principle guide durablement les décisions.
5. **B** — Baseline = état actuel.
6. **C** — Les composants logiques du Repository distinguent requirements, standards, solutions, modèles et décisions. [X2202, domaine correspondant].
7. **A** — Continuum classe du générique au spécifique.
8. **D** — Un deliverable peut agréger plusieurs artifacts et être soumis à validation formelle.
9. **A** — Preliminary établit capability/gouvernance.
10. **C** — Phase A cadre scope, stakeholders, value et Vision.
11. **D** — Les capabilities décrivent des aptitudes durables, distinctes des moyens applicatifs. [X2202, domaine correspondant].
12. **B** — C Data = structure/ownership/lifecycle des données.
13. **A** — C Application = services/interactions applicatives.
14. **C** — D = Technology Architecture.
15. **D** — E = solution options, work packages, Transition Architectures.
16. **B** — F = priorités, dépendances, séquencement.
17. **A** — G = implementation governance.
18. **C** — Phase H traite l'évolution de l'architecture de manière proportionnée et gouvernée. [X2202, domaine correspondant].
19. **D** — Requirements Management est transversal.
20. **B** — TOGAF permet de revenir sur les domaines dont les contraintes évoluent.
21. **A** — Gap = différence Baseline/Target.
22. **C** — Transition Architecture = état intermédiaire.
23. **B** — Un protocole commun n'assure pas une interprétation partagée des informations. [X2202, domaine correspondant].
24. **C** — Business Scenarios.
25. **D** — Transformation Readiness.
26. **A** — Risk Management.
27. **C** — Capability-Based Planning.
28. **B** — Migration Planning Techniques.
29. **D** — Tailoring.
30. **A** — La portée du travail se définit selon quatre dimensions et pas uniquement selon le nombre d'applications. [X2202, domaine correspondant].
31. **C** — Partitioning.
32. **B** — Agile et TOGAF peuvent coexister via tailoring/iteration.
33. **D** — Architecture Board.
34. **B** — Le modèle de gouvernance d'implémentation définit mécanismes, rôles et responsabilités de contrôle. [X2202, domaine correspondant].
35. **C** — Architecture Compliance Review.
36. **A** — Catalog/Matrix/Diagram sont des Artifacts.
37. **D** — Building Block = élément réutilisable d'architecture/solution.
38. **B** — Le Content Framework distingue trois formes d'artifacts : catalogues, matrices et diagrammes. [X2202, domaine correspondant].
39. **C** — Un viewpoint règle la construction d'une view, adaptée à des concerns.
40. **A** — Content Metamodel définit types d'entités et relations.

# Part 2 — correction approfondie

## P1 — Context

**Scoring :** A=3, B=1, C=0, D=5.

- **D — 5 points :** Tailorer et fédérer la gouvernance tout en maintenant principes et contrôles communs nécessaires, avec un noyau de principes obligatoires et une délégation de décisions selon les risques. Adapter la capacité d'architecture au contexte tout en préservant une gouvernance de groupe cohérente.
- **A — 3 points :** Définir une charte de gouvernance commune et un registre des exceptions, puis préciser les variations locales après une revue des obligations réglementaires. Une étape utile, mais insuffisante pour l'ensemble des enjeux.
- **B — 1 point :** Introduire une liste de standards techniques communes et vérifier leur usage lors des prochains projets, sans clarifier les responsabilités de décision. Action connexe sans justification globale.
- **C — 0 point :** Autoriser chaque filiale à choisir ses pratiques puis préparer une étude de cohérence groupe une fois la migration terminée. Action qui contourne la décision prioritaire.

**Référence :** X2202, Practitioner, unité 1.

## P2 — Stakeholder Management

**Scoring :** A=1, B=5, C=3, D=0.

- **B — 5 points :** Produire les vues adaptées aux concerns, expliciter valeur/coût/risque et organiser l'arbitrage, incluant un modèle de valeur, les alternatives et les conséquences opérationnelles pour chaque stakeholder. Les views doivent éclairer le choix des parties prenantes et rendre les options comparables.
- **C — 3 points :** Produire une première comparaison des coûts et bénéfices par option, puis compléter les views de conformité et d'exploitation avant le comité suivant. Une étape utile, mais insuffisante pour l'ensemble des enjeux.
- **A — 1 point :** Présenter une Architecture Roadmap technique pour donner une visibilité sur les phases de déploiement sans quantifier tous les bénéfices. Action connexe sans justification globale.
- **D — 0 point :** Choisir le fournisseur présentant le meilleur ROI déclaré et laisser les métiers vérifier après contractualisation que leurs concerns sont couverts. Action qui contourne la décision prioritaire.

**Référence :** X2202, Practitioner, unité 2.

## P3 — Phase A

**Scoring :** A=3, B=0, C=1, D=5.

- **D — 5 points :** Clarifier scope, stakeholders, responsabilités et Vision avant l'architecture détaillée, en documentant scope, domaines, profondeur de travail, horizon et responsabilités de validation. Un cadrage complet permet des architectures de domaine cohérentes et gouvernables.
- **A — 3 points :** Définir la largeur du périmètre et les acteurs principaux, puis préciser les autres dimensions du scope à la prochaine revue. Une étape utile, mais insuffisante pour l'ensemble des enjeux.
- **C — 1 point :** Obtenir l'accord des DSI locales sur les applications concernées, puis élaborer une Vision commune sans encore définir les outcomes. Action connexe sans justification globale.
- **B — 0 point :** Établir une liste de work packages par direction avant d'avoir distingué les responsabilités et les limites de l'architecture. Action qui contourne la décision prioritaire.

**Référence :** X2202, Practitioner, unité 3.

## P4 — B/C/D

**Scoring :** A=5, B=3, C=1, D=0.

- **A — 5 points :** Développer Application Architecture puis Technology Architecture en maintenant la traçabilité aux besoins métier/data, en dérivant les contrats de services, building blocks et contraintes de plateforme de la cible métier et data. Les domaines C Application et D doivent être dérivés des exigences et gaps existants, avec itérations si nécessaires.
- **B — 3 points :** Identifier les services applicatifs clés et les flux de données nécessaires, puis vérifier la cible technologique et les alternatives dans une seconde revue. Une étape utile, mais insuffisante pour l'ensemble des enjeux.
- **C — 1 point :** Examiner en premier la plateforme approuvée du groupe et construire un prototype, sans comparer encore les impacts sur les capacités métier. Action connexe sans justification globale.
- **D — 0 point :** Lancer la migration de l'application existante vers le cloud puis adapter les services métier lorsque la plateforme sera stabilisée. Action qui contourne la décision prioritaire.

**Référence :** X2202, Practitioner, unité 4.

## P5 — E/F/G

**Scoring :** A=3, B=1, C=5, D=0.

- **C — 5 points :** Analyser valeur, risque, dépendances et Transition Architectures en Phase F avant de séquencer, en modélisant la dépendance critique, les options de transition et les risques résiduels dans le plan. Les dépendances conditionnent la viabilité d'un work package, au-delà de son bénéfice isolé.
- **A — 3 points :** Programmer un lot IAM limité et démarrer en parallèle une validation fonctionnelle du contrôle, puis arbitrer les risques et coûts de la trajectoire complète. Une étape utile, mais insuffisante pour l'ensemble des enjeux.
- **B — 1 point :** Favoriser l'initiative de plus forte valeur mais lui associer une condition formelle de disponibilité IAM avant le go-live. Action connexe sans justification globale.
- **D — 0 point :** Accepter la priorité du sponsor et transférer les risques d'intégration au prestataire de delivery sans modifier la roadmap. Action qui contourne la décision prioritaire.

**Référence :** X2202, Practitioner, unité 5.

## P6 — Phase H

**Scoring :** A=5, B=3, C=1, D=0.

- **A — 5 points :** Évaluer l'impact et appliquer un changement proportionné si l'architecture reste valide, avec évaluation d'impact et preuve de conformité au niveau approprié. La classification de changement en H repose sur l'impact, non sur la simple existence d'une demande.
- **B — 3 points :** Vérifier les requirements et la vue impactée, puis autoriser un changement local en conservant une trace d'analyse. Une étape utile, mais insuffisante pour l'ensemble des enjeux.
- **C — 1 point :** Planifier une revue des principes de l'application avant de modifier la fonctionnalité, sans analyser immédiatement son impact concret. Action connexe sans justification globale.
- **D — 0 point :** Relancer un cycle ADM complet et suspendre la demande jusqu'à définition d'une nouvelle Architecture Vision. Action qui contourne la décision prioritaire.

**Référence :** X2202, Practitioner, unité 6.

## P7 — Requirements Management

**Scoring :** A=3, B=5, C=0, D=1.

- **B — 5 points :** Clarifier ownership, version de référence, traceability et impacts, avec identification du propriétaire, historique des versions, clarification du seuil et propagation vers les modèles. Une requirement non attribuée et non versionnée ne constitue pas un contrat de décision fiable.
- **A — 3 points :** Organiser la validation du niveau de service avec un Business Owner désigné, puis réconcilier les modèles d'architecture après l'accord. Une étape utile, mais insuffisante pour l'ensemble des enjeux.
- **D — 1 point :** Prendre la version la plus récente du document projet et la traiter comme référence provisoire sans vérifier son approbation. Action connexe sans justification globale.
- **C — 0 point :** Demander aux équipes de delivery de sélectionner la solution la plus résiliente et d'obtenir ensuite la signature métier. Action qui contourne la décision prioritaire.

**Référence :** X2202, Practitioner, unité 7.

## P8 — Supporting ADM Work

**Scoring :** A=3, B=1, C=5, D=0.

- **C — 5 points :** Utiliser Transformation Readiness et Stakeholder Management pour traiter les barrières et actions d'adoption, avec facteurs de readiness, plan d'adoption, priorisation des prérequis et budget associé. La préparation métier et opérationnelle est une dépendance de transformation, à rendre visible avant le déploiement.
- **A — 3 points :** Réaliser d'abord une évaluation des compétences et responsabilités locales, puis inscrire les actions de préparation dans les prochaines waves. Une étape utile, mais insuffisante pour l'ensemble des enjeux.
- **B — 1 point :** Rédiger des procédures d'exploitation standard pour les équipes actuelles, sans résoudre leur capacité de support 24/7. Action connexe sans justification globale.
- **D — 0 point :** Conserver le plan de migration initial et ajouter une clause de formation générale au contrat de livraison. Action qui contourne la décision prioritaire.

**Référence :** X2202, Practitioner, unité 8.
## Diagnostic

Évaluer les écarts de qualité de décision par learning outcome, pas seulement les lettres.
