# Correction — Mock Exam 01

## Barème

- Part 1 : 1 point par bonne réponse, total /40, réussite simulée à partir de 24/40.
- Part 2 : meilleur choix 5, deuxième 3, troisième 1, distracteur 0, total /40, réussite simulée à partir de 24/40.
- Les deux parties doivent être réussies séparément.

# Part 1 — Key et explications

Les références détaillées par objectif figurent dans `14-official-sources/06-x2202-learning-outcome-traceability.md`. Les commentaires ci-dessous ne prétendent pas être des citations précises du syllabus.

1. **B** — Concern = préoccupation d'un stakeholder.
2. **A** — la View est produite selon une Viewpoint.
3. **A** — L'EA oriente des choix de changement cohérents et non seulement la documentation ou la conformité de produits.
4. **D** — Repository organise/conserve ; Continuum classe/contextualise.
5. **D** — Architecture Capability = capacité organisationnelle à pratiquer l'EA.
6. **C** — Un ABB décrit des caractéristiques ou capacités architecturales sans figer l'implémentation ; un SBB représente une solution.
7. **A** — Un principe oriente durablement ; une requirement formule une condition vérifiable.
8. **D** — Transition Architecture = état intermédiaire cohérent.
9. **B** — Preliminary prépare capability, gouvernance, principles et tailoring.
10. **C** — Phase A cadre le travail et l'Architecture Vision.
11. **D** — La Phase B établit les besoins et représentations métier indépendamment du produit actuellement déployé.
12. **D** — Phase C Data traite ownership, lifecycle et qualité.
13. **B** — Phase C Application traite services et interactions applicatives.
14. **C** — Phase D = Technology Architecture.
15. **B** — Phase E structure options, work packages et transitions.
16. **D** — Phase F priorise et séquence la migration.
17. **B** — Phase G gouverne l'implémentation.
18. **C** — La Phase H classe le changement selon son ampleur ; la réponse peut être simplification, incremental ou re-architecting.
19. **A** — Requirements Management est transversal.
20. **B** — Gap Analysis compare Baseline et Target.
21. **A** — l'ADM est itératif et tailorable.
22. **D** — Roadmap = trajectoire ; Migration Plan = séquencement/priorisation détaillés.
23. **B** — Le Stakeholder Management éclaire la décision en associant concerns, viewpoints et autorités appropriées.
24. **A** — Business Scenarios relient problème métier et requirements.
25. **D** — Gap Analysis identifie create/change/remove entre Baseline et Target.
26. **C** — Transformation Readiness évalue capacité d'adoption.
27. **B** — Risk Management traite incertitude, impact et réponses.
28. **A** — Capability-Based Planning organise le changement autour des capabilities.
29. **C** — Tailoring adapte l'ADM au contexte.
30. **D** — Le scoping utilise breadth, depth, architecture domains et time period pour fixer un périmètre proportionné.
31. **B** — Partitioning organise espaces, responsabilités et interfaces.
32. **A** — TOGAF peut être adapté à Agile et au delivery incrémental.
33. **B** — Architecture Board = gouvernance/arbitrage.
34. **C** — Le Contract lie les acteurs à des engagements, sans remplacer les descriptions et exigences d'architecture.
35. **A** — Compliance Review vérifie l'alignement de l'implémentation.
36. **C** — Deliverable = produit formel pouvant contenir des artifacts.
37. **B** — Artifact = représentation du contenu architectural.
38. **C** — Le Content Framework distingue représentation, exigences et building blocks selon leur niveau d'abstraction.
39. **A** — la View répond aux concerns selon une Viewpoint.
40. **D** — Catalog liste, Matrix relie, Diagram visualise.

# Part 2 — Scoring argumenté

Chaque scénario suit le barème pédagogique 5/3/1/0. Ces classements ne correspondent pas à des questions confidentielles de l'examen officiel.

## P1 — Context for Enterprise Architecture — gouvernance fédérée

**Barème :** A=5, B=3, C=1, D=0.

- **A — 5 points.** Comparer les deux Architecture Capabilities et établir les autorités de gouvernance commune permet une fédération vérifiable sans jeter les architectures déjà produites.
- **B — 3 points.** Limiter d'abord les lots techniques conserve un début de trajectoire, mais les exceptions et conflits de standards restent sans arbitrage.
- **C — 1 points.** Les règles du fournisseur ne remplacent pas la capacité de décision des filiales ni les principes communs du groupe.
- **D — 0 points.** Reprendre intégralement Preliminary et abandonner les travaux utiles n'est pas proportionné ; il faut évaluer puis adapter la capacité existante.

**Source de contrôle :** X2202, Practitioner, domaine 1 ; TOGAF Standard 10th Edition, ADM et ses pratiques applicables.

## P2 — Stakeholder Management — conflit entre valeur et exploitabilité

**Barème :** A=1, B=5, C=0, D=3.

- **B — 5 points.** Operations et CISO doivent participer aux concerns et à la mise à jour de la Vision, avec requirements et views de continuité réellement validées.
- **D — 3 points.** Un atelier sur les contrôles urgents est utile, mais ni le modèle opérationnel complet ni la traçabilité de la cible ne sont réconciliés.
- **A — 1 points.** La validation du seul sponsor ne prouve pas que les exigences de reprise et de support sont satisfaites.
- **C — 0 points.** Transférer le problème à Operations sans modifier la cible conserve les incohérences architecturales.

**Source de contrôle :** X2202, Practitioner, domaine 2 ; TOGAF Standard 10th Edition, ADM et ses pratiques applicables.

## P3 — Phase A — vision fondée sur des drivers vérifiables

**Barème :** A=1, B=3, C=5, D=0.

- **C — 5 points.** La Vision de Phase A doit relier drivers, valeur, stakeholders, risques et périmètre avant de figer les technologies candidates.
- **B — 3 points.** Une vérification des critères de valeur permet un cadrage partiel, mais le choix des deux technologies reste biaisé par une hypothèse non confirmée.
- **A — 1 points.** Des architectures produit séparées ne remplacent pas une Vision commune ni l'accord sur les objectifs du programme.
- **D — 0 points.** Un Migration Plan détaillé en F ne peut précéder le cadrage et le développement de la Target.

**Source de contrôle :** X2202, Practitioner, domaine 3 ; TOGAF Standard 10th Edition, ADM et ses pratiques applicables.

## P4 — Architecture Development B/C/D — exigence contradictoire

**Barème :** A=1, B=0, C=3, D=5.

- **D — 5 points.** L'itération B/C/D réconcilie besoins métier, données, services, technologies et règles de résidence avant le regroupement des gaps.
- **C — 3 points.** Revoir les données est nécessaire, mais les applications et technologies pourraient rester incohérentes sans analyse transverse.
- **A — 1 points.** Choisir Kafka/PostgreSQL avant la résolution des besoins inverse la relation entre exigences et solutions.
- **B — 0 points.** Une comparaison technologique isolée ne couvre ni double saisie, ni définition des données, ni impacts métier.

**Source de contrôle :** X2202, Practitioner, domaine 4 ; TOGAF Standard 10th Edition, ADM et ses pratiques applicables.

## P5 — Implementing E/F/G — dépendances, valeur et transition

**Barème :** A=1, B=5, C=0, D=3.

- **B — 5 points.** La Phase F doit prioriser les lots selon valeur, dépendances, coûts de coexistence et readiness, puis formaliser leur séquence de migration.
- **D — 3 points.** Placer les événements en premier traite la dépendance Fraud, mais laisse le coût transitoire et les autres arbitrages non validés.
- **A — 1 points.** Une revue de conformité anticipée ne justifie pas à elle seule l'ordre de migration déjà demandé par le sponsor.
- **C — 0 points.** Redémarrer intégralement la Vision et B/C/D sans nouveau gap déterminant retarde inutilement la décision de planification.

**Source de contrôle :** X2202, Practitioner, domaine 5 ; TOGAF Standard 10th Edition, ADM et ses pratiques applicables.

## P6 — Phase H — adaptation réglementaire après déploiement

**Barème :** A=0, B=3, C=1, D=5.

- **D — 5 points.** Phase H qualifie l'effet de la nouvelle réglementation sur l'architecture en service et décide de la modification ou du nouveau cycle ADM.
- **B — 3 points.** Tracer l'exigence et les composants touchés est utile, mais la portée et les dépendances du changement restent à classifier.
- **C — 1 points.** L'usage en production d'une interface par une filiale ne prouve pas sa validité réglementaire pour l'ensemble du groupe.
- **A — 0 points.** Reporter l'évaluation à une revue annuelle peut exposer le programme à une non-conformité réglementaire.

**Source de contrôle :** X2202, Practitioner, domaine 6 ; TOGAF Standard 10th Edition, ADM et ses pratiques applicables.

## P7 — Requirements Management — disponibilité contradictoire

**Barème :** A=5, B=1, C=3, D=0.

- **A — 5 points.** Une disponibilité de 99,95 % sans périmètre ni exclusion documentée doit être clarifiée, tracée, versionnée et propagée aux views concernées.
- **C — 3 points.** Un compromis provisoire alimente la discussion, mais n'évalue pas encore les conséquences techniques et contractuelles.
- **B — 1 points.** Choisir l'interprétation la moins coûteuse avant arbitrage ignore les exigences des owners et les risques de sécurité.
- **D — 0 points.** Attendre Phase G pour définir l'exigence empêche de concevoir et comparer des solutions conformes.

**Source de contrôle :** X2202, Practitioner, domaine 7 ; TOGAF Standard 10th Edition, ADM et ses pratiques applicables.

## P8 — Supporting ADM Work — réutilisation conditionnelle

**Barème :** A=1, B=0, C=5, D=3.

- **C — 5 points.** La réutilisation doit vérifier les hypothèses de capacité, volumes, sécurité et obligations réglementaires avant de choisir les adaptations.
- **D — 3 points.** Des tests de charge et sécurité ciblent de vrais risques, mais la conformité réglementaire et les hypothèses métiers restent ouvertes.
- **A — 1 points.** L'ancienneté d'un pattern ne prouve pas qu'il est inutilisable ; elle appelle une vérification de pertinence.
- **B — 0 points.** Une approbation historique du Repository ne garantit pas l'adéquation au nouveau volume et aux règles de la filiale.

**Source de contrôle :** X2202, Practitioner, domaine 8 ; TOGAF Standard 10th Edition, ADM et ses pratiques applicables.

## Diagnostic

Réviser les huit domaines Practitioner selon les erreurs de contexte, d'arbitrage et de séquencement ; ne pas juger la préparation à partir du seul score.
