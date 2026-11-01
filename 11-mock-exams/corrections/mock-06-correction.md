# Correction — Mock Exam 06

## Barème
Part 1 : /40, réussite simulée ≥24. Part 2 : /40, gradient 5/3/1/0, réussite simulée ≥24. Réussir l'un ne compense pas l'échec de l'autre.

# Part 1

1. **C** — l'EA aligne structure, capacités et transformation.
2. **A** — stakeholder = partie intéressée/affectée.
3. **D** — Le Continuum est un mécanisme de classification ; le Repository organise et conserve les ressources. [X2202, domaine correspondant].
4. **B** — Concern = préoccupation stakeholder.
5. **C** — Principle guide durablement les décisions.
6. **A** — Le Governance Log permet de tracer décisions de conformité et exceptions. [X2202, domaine correspondant].
7. **D** — Architecture Capability = rôles, compétences, gouvernance, processus et moyens.
8. **C** — Baseline → Target → Gap.
9. **A** — Preliminary prépare la capacité et le cadre.
10. **B** — Phase A établit Vision et alignement initial.
11. **C** — La Phase B traduit la Vision dans un modèle de capacités et processus métier cible. [X2202, domaine correspondant].
12. **D** — data ownership/flux = Phase C Data.
13. **A** — services applicatifs = C Application.
14. **B** — plateformes/services technologiques = D.
15. **C** — options/work packages candidats = E.
16. **D** — priorisation/séquencement = F.
17. **A** — conformité de l'implémentation = G.
18. **C** — La Phase H surveille la pertinence de l'architecture et gouverne son adaptation. [X2202, domaine correspondant].
19. **D** — Requirements Management interagit avec toutes les phases.
20. **B** — l'itération permet de revisiter le travail lorsque nécessaire.
21. **C** — les gaps peuvent exister dans les quatre domaines.
22. **A** — Roadmap montre la trajectoire vers la cible.
23. **A** — L'interopérabilité inclut processus, signification de l'information et moyens techniques. [X2202, domaine correspondant].
24. **C** — Business Scenarios.
25. **B** — Gap Analysis.
26. **D** — Transformation Readiness.
27. **A** — Risk Management.
28. **B** — Migration Planning Techniques.
29. **C** — Tailoring = adaptation consciente de l'ADM.
30. **A** — TOGAF permet itération et tailoring sans perdre la traçabilité ni les autorités de décision. [X2202, domaine correspondant].
31. **B** — Partitioning = espaces, responsabilités, interfaces.
32. **D** — ADM peut être itératif/tailorable avec Agile.
33. **C** — Architecture Board = autorité de gouvernance.
34. **A** — Le Contract définit des engagements entre les parties et peut guider les Compliance Reviews. [X2202, domaine correspondant].
35. **B** — un écart doit être analysé et gouverné.
36. **D** — Deliverable = produit formel contenant potentiellement plusieurs artifacts.
37. **A** — Artifact = Catalog/Matrix/Diagram, etc.
38. **B** — Le Content Framework articule livrables, représentations et éléments d'architecture. [X2202, domaine correspondant].
39. **C** — SBB correspond à une réalisation plus spécifique.
40. **D** — Content Metamodel définit types d'objets et relations.

# Part 2 — correction des scénarios

## P1 — Context

**Barème :** A=3, B=5, C=0, D=1.

- **B (5) :** Renforcer en priorité capacité, gouvernance, compétences, repository et tailoring afin de soutenir les transformations, avec une approche de gouvernance par priorités, des rôles nommés et une trajectoire de montée en capacité. La pratique d'architecture doit permettre de guider plusieurs changements en cohérence.
- **A (3) :** Désigner temporairement des architectes responsables par domaine et enregistrer les décisions critiques, puis structurer la capacité formelle. Partiellement adapté, avec une dépendance ou décision laissée ouverte.
- **D (1) :** Mettre en place une bibliothèque de patterns communs avant de clarifier les personnes autorisées à valider les exceptions. Couvre un aspect secondaire, insuffisant au moment décrit.
- **C (0) :** Confier la cohérence globale au fournisseur principal, puis internaliser les décisions d'architecture après la première mise en production. Contourne la contrainte structurante.

**Référence :** X2202, Practitioner, unité 1.

## P2 — Stakeholder Management

**Barème :** A=1, B=5, C=0, D=3.

- **B (5) :** L'intégrer comme stakeholder, clarifier concerns et requirements de conformité, puis adapter les views et décisions, avec identification des concerns, consultation des owners et adaptation des views avant approbation. Les acteurs réglementaires critiques doivent peser sur la Target, pas être informés seulement après.
- **D (3) :** Demander un avis ciblé sur la résidence des données et préparer une analyse des implications, puis élargir les autres vues dans une seconde revue. Partiellement adapté, avec une dépendance ou décision laissée ouverte.
- **A (1) :** Reporter la consultation de conformité à la revue de migration lorsque le design technique sera stabilisé. Couvre un aspect secondaire, insuffisant au moment décrit.
- **C (0) :** Faire accepter provisoirement les risques de transfert par le sponsor et ajouter la conformité comme contrôle de Phase G. Contourne la contrainte structurante.

**Référence :** X2202, Practitioner, unité 2.

## P3 — Phase A

**Barème :** A=5, B=1, C=0, D=3.

- **A (5) :** Revenir au cadrage Phase A pour clarifier drivers, outcomes, stakeholders et Vision tout en conservant les requirements utiles, en reliant drivers, outcomes, stakeholders et scope à une Architecture Vision défendable. Les requirements détaillées ne compensent pas l'absence de drivers et de business value en Phase A.
- **D (3) :** Rattacher les requirements existantes à quelques drivers majeurs et valider un premier jeu d'indicateurs, puis finaliser la Vision. Partiellement adapté, avec une dépendance ou décision laissée ouverte.
- **B (1) :** Proposer une Roadmap préliminaire de plateforme pour susciter la discussion métier, sans faire encore approuver les bénéfices. Couvre un aspect secondaire, insuffisant au moment décrit.
- **C (0) :** Réserver le fournisseur et répartir les exigences entre les équipes d'implémentation, puis mesurer les outcomes après livraison. Contourne la contrainte structurante.

**Référence :** X2202, Practitioner, unité 3.

## P4 — B/C/D

**Barème :** A=5, B=3, C=1, D=0.

- **A (5) :** Revoir la Technology Architecture et ses gaps en cohérence avec les requirements avant Phase E, en revisitant les contraintes de latence, les options technologiques et les dépendances B/C/D. La cible technologique doit être cohérente avec les exigences et choix des domaines précédents.
- **B (3) :** Évaluer une plateforme événementielle comme candidate et réaliser des tests de performance avant de confirmer l'architecture de domaine. Partiellement adapté, avec une dépendance ou décision laissée ouverte.
- **C (1) :** Introduire un traitement prioritaire dans le batch existant pour un sous-ensemble de flux, puis mesurer si le SLA est atteint. Couvre un aspect secondaire, insuffisant au moment décrit.
- **D (0) :** Considérer que l'équipe applicative doit ralentir le processus métier pour se conformer à la plateforme déjà approuvée. Contourne la contrainte structurante.

**Référence :** X2202, Practitioner, unité 4.

## P5 — E/F/G

**Barème :** A=3, B=5, C=1, D=0.

- **B (5) :** Utiliser Phase F pour évaluer dépendances, valeur, risques et séquencer le plan, en classant lots, risques, valeur, coûts et dépendances dans le plan final. L'existence d'une Transition Architecture ne démontre pas la viabilité de son plan.
- **A (3) :** Établir un ordre provisoire des prérequis techniques et vérifier la période de coexistence, puis obtenir un arbitrage de valeur et de financement. Partiellement adapté, avec une dépendance ou décision laissée ouverte.
- **C (1) :** Démarrer un pilote de la passerelle afin de réduire l'incertitude technique, sans décider encore des vagues de migration. Couvre un aspect secondaire, insuffisant au moment décrit.
- **D (0) :** Autoriser les projets à sélectionner eux-mêmes l'ordre de livraison, puis regrouper les calendriers en Phase G. Contourne la contrainte structurante.

**Référence :** X2202, Practitioner, unité 5.

## P6 — Phase H

**Barème :** A=5, B=1, C=0, D=3.

- **A (5) :** Évaluer les drivers et la performance de l'architecture, puis décider de l'évolution ou d'un nouveau cycle, en comparant la valeur réellement délivrée aux business drivers actuels et en classant l'impact de changement. La Phase H considère aussi l'obsolescence de valeur et l'évolution des drivers métier.
- **D (3) :** Mettre à jour les principaux KPI et préparer une analyse d'impact de la nouvelle demande avant de choisir le périmètre de réarchitecture. Partiellement adapté, avec une dépendance ou décision laissée ouverte.
- **B (1) :** Modifier uniquement la chaîne de rejet qui affiche le plus mauvais indicateur, sans réévaluer l'objectif métier global. Couvre un aspect secondaire, insuffisant au moment décrit.
- **C (0) :** Reprendre immédiatement tout l'ADM depuis Preliminary, même si l'analyse pourrait limiter le travail à quelques domaines. Contourne la contrainte structurante.

**Référence :** X2202, Practitioner, unité 6.

## P7 — Requirements Management

**Barème :** A=5, B=1, C=0, D=3.

- **A (5) :** Mettre à jour la requirement, utiliser la traceability pour identifier les impacts et déclencher les itérations nécessaires, en établissant un Requirements Impact Assessment traçant les building blocks, décisions et migrations concernés. L'impact de requirements doit être propagé et gouverné transversalement.
- **D (3) :** Réaliser une première analyse sur les services les plus exposés et chiffrer les travaux urgents, puis vérifier les autres impacts. Partiellement adapté, avec une dépendance ou décision laissée ouverte.
- **B (1) :** Appliquer la modification aux ABB du service principal et demander aux autres équipes de réévaluer leurs contrats pendant la migration. Couvre un aspect secondaire, insuffisant au moment décrit.
- **C (0) :** Conserver les work packages approuvés et considérer que le changement se limite au code déjà modifié. Contourne la contrainte structurante.

**Référence :** X2202, Practitioner, unité 7.

## P8 — Supporting ADM Work

**Barème :** A=3, B=5, C=1, D=0.

- **B (5) :** Utiliser les techniques de migration planning et risk management pour comparer valeur, dépendances, readiness et risque, en utilisant readiness, facteurs d'implémentation, matrice de dépendances et arbitrage valeur-risque. Les techniques de migration évaluent la faisabilité réelle, pas uniquement les bénéfices affichés.
- **A (3) :** Établir une comparaison des coûts et risques des deux trajectoires, puis vérifier la capacité de support avant le choix final. Partiellement adapté, avec une dépendance ou décision laissée ouverte.
- **C (1) :** Réduire le coût de la coexistence avec un pilote limité, sans résoudre la dépendance d'identité sur toutes les waves. Couvre un aspect secondaire, insuffisant au moment décrit.
- **D (0) :** Sélectionner la trajectoire économiquement la moins chère et traiter les autres contraintes pendant l'implémentation. Contourne la contrainte structurante.

**Référence :** X2202, Practitioner, unité 8.
