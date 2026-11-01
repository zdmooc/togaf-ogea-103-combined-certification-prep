# Correction — Mock Exam 03

## Barème
Part 1 : /40, passage simulé ≥24. Part 2 : /40, scoring 5/3/1/0, passage simulé ≥24.

# Part 1

1. **D** — Concern = préoccupation d'un stakeholder.
2. **A** — Stakeholder → Concern → Viewpoint → View.
3. **B** — La capability décrit ce que l'entreprise sait faire, pas le moyen contingent de le réaliser. [X2202, objectifs du domaine concerné].
4. **C** — Baseline = état actuel pertinent.
5. **D** — Principle = règle directrice durable.
6. **A** — Le métamodèle organise le vocabulaire et les relations d'architecture. [X2202, objectifs du domaine concerné].
7. **B** — Repository contient standards, references, decisions et autres assets.
8. **C** — Transition Architecture = état intermédiaire.
9. **C** — Preliminary établit gouvernance/capability.
10. **D** — Statement of Architecture Work est associé à Phase A.
11. **B** — La cible métier fait apparaître les capabilities et gaps avant le choix ou la réutilisation des composants. [X2202, objectifs du domaine concerné].
12. **A** — entités et data ownership relèvent de C Data.
13. **C** — services applicatifs = C Application.
14. **B** — services technologiques = Phase D.
15. **D** — work packages/transitions candidats = Phase E.
16. **A** — priorisation valeur/risque/dépendances = F.
17. **C** — écart pendant implémentation = G.
18. **B** — Phase H surveille l'adéquation de l'architecture livrée aux besoins évolutifs. [X2202, objectifs du domaine concerné].
19. **D** — Requirements Management intègre les nouvelles requirements.
20. **A** — l'ADM permet l'itération.
21. **C** — les gaps alimentent changements/work packages.
22. **B** — Roadmap = trajectoire structurée.
23. **A** — La readiness couvre capacité organisationnelle, funding, leadership, ressources et exploitation. [X2202, objectifs du domaine concerné].
24. **D** — Business Scenarios clarifient le besoin.
25. **B** — Gap Analysis compare Baseline/Target.
26. **C** — Transformation Readiness traite adoption et capacité de changement.
27. **A** — Capability-Based Planning.
28. **D** — Migration Planning Techniques.
29. **B** — Tailoring adapte artifacts et profondeur.
30. **C** — L'ADM autorise des itérations et du travail concurrent lorsque les décisions restent gouvernées. [X2202, objectifs du domaine concerné].
31. **A** — Levels of Architecture permettent plusieurs scopes liés.
32. **D** — federation = partitions + interfaces + gouvernance cohérente.
33. **A** — Architecture Board arbitre les exceptions.
34. **D** — La conformité d'architecture ne se réduit jamais à l'emploi de produits autorisés. [X2202, objectifs du domaine concerné].
35. **C** — Compliance Review contrôle l'alignement.
36. **B** — Deliverable = produit formel.
37. **A** — un diagramme applicatif est un Artifact.
38. **D** — Le deliverable rassemble des représentations et autres éléments nécessaires à l'approbation. [X2202, objectifs du domaine concerné].
39. **C** — ABB plus architectural, SBB plus solution/réalisation.
40. **B** — L'Architecture Content distingue des forms de représentation, pas des étapes de migration.

# Part 2 — corrections détaillées

## P1 — Context

**Barème :** A=3, B=1, C=5, D=0.

- **C — 5 points :** Tailorer l'ADM et la gouvernance selon le contexte tout en préservant les objectifs essentiels, en fixant des seuils d'escalade et une gouvernance proportionnée au risque des initiatives. L'ADM est adaptable ; la gouvernance doit être explicite et proportionnée à la maturité et aux risques.
- **A — 3 points :** Conserver le cycle ADM comme référence et supprimer plusieurs validations manuelles dans les produits à faible risque, puis clarifier plus tard la matrice des responsabilités. Traite une partie utile mais ne complète pas l'arbitrage.
- **B — 1 point :** Appliquer les mêmes livrables de gouvernance à toutes les équipes, mais réduire leur format et leur fréquence pour limiter l'effort. À envisager seulement en complément et sans remplacer le travail central.
- **D — 0 point :** Exempter les produits agiles de toute revue de conformité et faire auditer uniquement la Target Technology Architecture globale. Évite ou déplace indûment la décision.

**Référence de contrôle :** X2202, Practitioner, unité 1.

## P2 — Stakeholder Management

**Barème :** A=1, B=3, C=0, D=5.

- **D — 5 points :** Mettre à jour stakeholder analysis, requirements et views pertinentes, puis analyser les impacts, en explicitant l'obligation, les nouveaux requirements et les impacts de modification avant la validation suivante. Un nouveau stakeholder critique modifie les concerns, exigences et décisions possibles à travers plusieurs domaines.
- **B — 3 points :** Faire analyser en urgence le périmètre de conservation par le DPO et préparer des vues de données ajustées pour les responsables concernés. Traite une partie utile mais ne complète pas l'arbitrage.
- **A — 1 point :** Conserver les vues existantes et ajouter une annexe de conformité pour la direction, sans réviser la traçabilité des services. À envisager seulement en complément et sans remplacer le travail central.
- **C — 0 point :** Prévoir un changement post-go-live pour la conservation en supposant que l'instance réglementaire acceptera une dérogation. Évite ou déplace indûment la décision.

**Référence de contrôle :** X2202, Practitioner, unité 2.

## P3 — Phase A

**Barème :** A=3, B=5, C=0, D=1.

- **B — 5 points :** Clarifier drivers, value proposition, scope et critères de succès dans Phase A, avec des indicateurs de bénéfices, hypothèses d'investissement et limites de portée explicites. La Vision est un outil de décision et de valeur ; elle doit rendre les attentes de succès comparables.
- **A — 3 points :** Établir un business case exploratoire avec deux outcomes possibles et solliciter l'accord des principaux métiers avant de rédiger la Vision complète. Traite une partie utile mais ne complète pas l'arbitrage.
- **D — 1 point :** Présenter une première Architecture Roadmap de solutions candidates pour faciliter la discussion, même si les bénéfices ne sont pas encore validés. À envisager seulement en complément et sans remplacer le travail central.
- **C — 0 point :** Demander aux équipes de delivery de commencer l'implémentation du composant principal afin de produire rapidement des coûts observés. Évite ou déplace indûment la décision.

**Référence de contrôle :** X2202, Practitioner, unité 3.

## P4 — B/C/D

**Barème :** A=1, B=3, C=0, D=5.

- **D — 5 points :** Commencer par Business Architecture pour définir la cible métier avant de figer Application et Technology Architectures, en définissant la capacité, les processus et ownership métier avant de dériver les domaines Data/Application/Technology. La Target Business Architecture dirige les autres domaines ; l'existant applicatif n'est pas une définition des capacités futures.
- **B — 3 points :** Lister les règles métier critiques et les exceptions puis établir un premier modèle de capacités, avec une revue cible complète à suivre. Traite une partie utile mais ne complète pas l'arbitrage.
- **A — 1 point :** Examiner les API des applications actuelles pour repérer les possibilités de réutilisation avant de décider du découpage métier. À envisager seulement en complément et sans remplacer le travail central.
- **C — 0 point :** Définir une plateforme technique commune qui hébergera les workflows existants, puis adapter les responsabilités métier aux contraintes du produit. Évite ou déplace indûment la décision.

**Référence de contrôle :** X2202, Practitioner, unité 4.

## P5 — E/F/G

**Barème :** A=5, B=3, C=1, D=0.

- **A — 5 points :** Phase G avec Architecture Contract/Compliance mechanisms, avec Architecture Contract, Compliance Reviews, preuves et décisions tracées pendant l'implémentation. Après le planning F, la Phase G gouverne la réalisation par preuves, responsabilités et mécanismes d'exception.
- **B — 3 points :** Organiser une première revue de conformité sur l'interface commune et enregistrer l'exception candidate, puis compléter le contrat d'architecture. Traite une partie utile mais ne complète pas l'arbitrage.
- **C — 1 point :** Réviser le classement des work packages à la lumière du choix de protocole, sans traiter encore l'implémentation du contrôle d'accès. À envisager seulement en complément et sans remplacer le travail central.
- **D — 0 point :** Modifier la Target pour refléter les protocoles choisis par les développeurs et considérer que la conformité est acquise. Évite ou déplace indûment la décision.

**Référence de contrôle :** X2202, Practitioner, unité 5.

## P6 — Phase H

**Barème :** A=3, B=0, C=5, D=1.

- **C — 5 points :** Évaluer le changement et appliquer une réponse proportionnée si l'impact est mineur, et enregistrer l'analyse de non-impact ainsi que le traitement opérationnel correspondant. La classification dépend de l'impact réel ; un patch peut relever d'une gestion de changement technique normale.
- **A — 3 points :** Vérifier les impacts sur standards et requirements, puis autoriser le change technique avec un contrôle de non-régression documenté. Traite une partie utile mais ne complète pas l'arbitrage.
- **D — 1 point :** Regrouper le patch avec les autres changements d'architecture mineurs pour décider d'une prochaine architecture cible commune. À envisager seulement en complément et sans remplacer le travail central.
- **B — 0 point :** Conserver la version actuelle jusqu'au prochain cycle de stratégie parce qu'une modification après go-live est toujours disruptive. Évite ou déplace indûment la décision.

**Référence de contrôle :** X2202, Practitioner, unité 6.

## P7 — Requirements Management

**Barème :** A=5, B=0, C=1, D=3.

- **A — 5 points :** Tracer la requirement, comparer les options et conserver la décision et sa justification, jusqu'aux building blocks, aux critères de validation, aux risques et à la décision d'architecture. La gestion des exigences soutient des alternatives, pas simplement la reconnaissance d'une option techniquement valide.
- **D — 3 points :** Comparer coûts et risques des deux solutions au moyen d'un tableau d'arbitrage, puis relier les décisions à la requirement approuvée. Traite une partie utile mais ne complète pas l'arbitrage.
- **C — 1 point :** Choisir la solution qui satisfait le mieux le SLA opérationnel, puis mesurer les autres contraintes après la première vague. À envisager seulement en complément et sans remplacer le travail central.
- **B — 0 point :** Utiliser la technologie déjà en place comme solution de référence et accepter les risques restants sans les présenter au comité. Évite ou déplace indûment la décision.

**Référence de contrôle :** X2202, Practitioner, unité 7.

## P8 — Supporting ADM Work

**Barème :** A=3, B=5, C=1, D=0.

- **B — 5 points :** Effectuer une analyse d'interoperability couvrant dimensions pertinentes avant de choisir les adaptations, avec analyse des dimensions métier, information et technologie et gouvernance des contrats d'échange. L'interopérabilité exige un accord sémantique et organisationnel, non la seule connexion des systèmes.
- **A — 3 points :** Documenter les modèles de données et les correspondances de statut, puis valider la sémantique avec les propriétaires de processus. Traite une partie utile mais ne complète pas l'arbitrage.
- **C — 1 point :** Installer une passerelle de conversion pour harmoniser les schémas de message sans revoir l'interprétation métier des événements. À envisager seulement en complément et sans remplacer le travail central.
- **D — 0 point :** Changer de protocole de transport pour un format commun, puis vérifier les écarts comptables à l'occasion des tests de production. Évite ou déplace indûment la décision.

**Référence de contrôle :** X2202, Practitioner, unité 8.
## Diagnostic

Analyser l'ordre des décisions, le risque résiduel et les rôles. Ces scores sont pédagogiques et non officiels.
