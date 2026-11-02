# Correction — Mock Exam 05

## Barème
Part 1 : /40, passage simulé ≥24. Part 2 : /40 avec gradient 5/3/1/0, passage simulé ≥24.

# Part 1

1. **A** — stakeholder = partie intéressée/affectée.
2. **C** — concern = ce qui importe au stakeholder.
3. **D** — Au niveau Portfolio, l'EA guide la sélection et la cohérence d'un ensemble de changements.
4. **B** — Principle = règle directrice générale.
5. **A** — Target = futur souhaité.
6. **C** — Le Content Framework sépare représentation graphique, éléments architecturaux et engagements formels.
7. **B** — Repository organise les assets.
8. **D** — Continuum classe/contextualise les assets.
9. **B** — Preliminary installe capability et gouvernance.
10. **A** — Architecture Vision = Phase A.
11. **A** — La Phase B décrit les besoins métier et prépare la cohérence des domaines qui suivent.
12. **D** — data ownership = C Data.
13. **B** — interactions/services applicatifs = C Application.
14. **D** — plateforme cible = Phase D.
15. **A** — work packages/transitions = E.
16. **D** — séquencement de migration = F.
17. **B** — Contract/Compliance soutiennent G.
18. **C** — La Phase H ne présuppose pas qu'une exigence réglementaire impose un type unique de changement.
19. **A** — Requirements Management est continu.
20. **C** — ADM tailorable et itératif.
21. **D** — Gap = différence Baseline/Target.
22. **C** — Roadmap montre la trajectoire.
23. **C** — La readiness mesure la capacité de l'entreprise à transformer et exploiter, pas seulement la faisabilité technique.
24. **A** — Business Scenarios.
25. **B** — Interoperability Analysis.
26. **B** — Transformation Readiness.
27. **C** — Risk Management.
28. **A** — Capability-Based Planning.
29. **B** — Tailoring.
30. **D** — L'ADM peut coexister avec des approches agiles et reste itératif.
31. **A** — Partitioning.
32. **C** — security est transverse.
33. **B** — Architecture Board.
34. **C** — Architecture Governance demande une décision d'exception et une preuve, pas une approbation implicite.
35. **A** — une exception doit être analysée, approuvée et suivie.
36. **D** — Deliverable = produit formel.
37. **A** — Matrix = Artifact.
38. **B** — Une matrice est une représentation ; elle ne devient ni une solution ni un contrat.
39. **C** — ABB architectural, SBB plus concret.
40. **D** — Catalog liste, Matrix relie, Diagram visualise.

# Part 2 — correction des scénarios

## P1 — Context

**Barème :** A=1, B=5, C=3, D=0.

- **B (5) :** Tailorer le processus selon risque, scope et maturité tout en conservant contrôles essentiels, en distinguant changements locaux et structurants et en définissant des contrôles adaptés au risque. Le tailoring conserve la discipline de gouvernance tout en évitant les activités sans valeur.
- **C (3) :** Établir une voie rapide de revue pour les changements à faible impact et préciser progressivement les conditions d'escalade. Une voie rapide accélère les petits changements, mais les seuils de risque et les responsabilités d'escalade restent incomplets.
- **A (1) :** Réduire le nombre de documents d'architecture exigés pour les produits agiles, sans encore réviser le circuit de validation. Réduire la documentation ne corrige pas à lui seul le circuit de validation trop lourd du Board.
- **D (0) :** Maintenir le Board central pour toutes les décisions et instaurer seulement un délai de réponse maximal aux demandes. Un délai de réponse plus court n'adapte pas les contrôles aux différents risques des produits.

**Référence :** X2202, Practitioner, unité 1.

## P2 — Stakeholder Management

**Barème :** A=3, B=1, C=0, D=5.

- **D (5) :** Réengager Data comme stakeholder, clarifier concerns/requirements et analyser les impacts sur architecture et roadmap, en remettant les concerns Data au centre et en révisant les vues, exigences, gaps et options de migration. Une contrainte de qualité peut imposer des itérations entre les domaines et la trajectoire.
- **A (3) :** Organiser une revue des données critiques et proposer des règles temporaires de validation, puis analyser les autres impacts. La revue des données critiques met au jour les premiers écarts, mais ne réengage pas encore tous les Data Owners pour arbitrer la cible.
- **B (1) :** Documenter les limites des sources et ajuster les tests de recette, sans renégocier les exigences avec les owners. Modifier seulement les tests de recette masque les exigences de qualité potentiellement irréalisables.
- **C (0) :** Conserver la Target et transférer la responsabilité de qualité aux équipes d'exploitation après le déploiement. Transférer la qualité à l'exploitation sans réévaluer la Target reporte une non-conformité prévisible.

**Référence :** X2202, Practitioner, unité 2.

## P3 — Phase A

**Barème :** A=5, B=3, C=1, D=0.

- **A (5) :** Cadrer formellement scope, approche, responsabilités, risques et engagement en Phase A, en définissant les livrables, ressources, risques, rôles, périmètre et conditions d'approbation. Le Statement of Architecture Work structure l'engagement et précède les décisions détaillées.
- **B (3) :** Formaliser un mandat provisoire pour les éléments indispensables au contrôle réglementaire, puis faire valider le reste du scope. Le mandat provisoire cadre les contrôles urgents, mais le scope et les approbations de l'engagement restent à finaliser.
- **C (1) :** Autoriser une étude détaillée des interfaces de paiement critiques sous l'autorité du sponsor, en documentant les décisions en attente. L'étude détaillée des interfaces avance un sous-ensemble sans Statement of Architecture Work convenu.
- **D (0) :** Démarrer le plan de migration sur la base du budget et demander la formalisation du mandat après la première release. Le Migration Plan lancé avant le mandat ne clarifie ni les responsabilités ni les engagements d'architecture.

**Référence :** X2202, Practitioner, unité 3.

## P4 — B/C/D

**Barème :** A=1, B=0, C=5, D=3.

- **C (5) :** Itérer entre Business et Application Architecture pour réaligner cible et requirements avant Phase E, en réconciliant capabilities, services, données et plateformes et en documentant les gaps. La Target Application doit démontrer qu'elle supporte la capacité métier souhaitée.
- **D (3) :** Réviser les services exposés à partir des parcours métier critiques, puis compléter l'analyse des composants moins impactés. Réviser les principaux services métier limite les écarts, mais la réconciliation avec toutes les capabilities et gaps reste ouverte.
- **A (1) :** Ajouter un adaptateur autour de l'application existante pour couvrir rapidement un sous-ensemble du besoin, sans réviser toutes les interactions. Un adaptateur local contourne une partie du problème sans corriger la Target Application Architecture.
- **B (0) :** Conserver l'architecture applicative approuvée et demander au métier d'adapter les processus au produit disponible. Demander au métier de s'adapter à une cible inadéquate inverse l'alignement métier-application.

**Référence :** X2202, Practitioner, unité 4.

## P5 — E/F/G

**Barème :** A=5, B=3, C=0, D=1.

- **A (5) :** Utiliser les mécanismes de Phase G pour Compliance Review, analyse de l'écart et décision gouvernée, en réalisant une Compliance Assessment, en évaluant le risque et en faisant décider l'exception ou la correction. La Phase G compare preuves d'implémentation, exigences et dérogations approuvées.
- **B (3) :** Documenter le problème et appliquer des mesures compensatoires provisoires, puis soumettre l'exception au Board avant la release. Les mesures compensatoires et l'escalade au Board réduisent le risque, mais la Compliance Review complète et les preuves manquent.
- **D (1) :** Ajouter un test d'audit à la campagne de validation et considérer l'écart comme un défaut technique de priorité moyenne. Un test d'audit isolé n'arbitre ni la violation de principe ni la décision d'exception.
- **C (0) :** Mettre à jour l'Architecture Definition Document pour refléter la solution livrée, sans analyser la contradiction avec le principe. Modifier la Target pour refléter un contrôle non conforme sans analyse contourne la gouvernance de phase G.

**Référence :** X2202, Practitioner, unité 5.

## P6 — Phase H

**Barème :** A=0, B=5, C=1, D=3.

- **B (5) :** Évaluer l'impact sur architecture, roadmap, risks et décider de l'ampleur du nouveau travail, avec analyse d'impact, classification Phase H et conséquences sur les transitions et standards. L'obsolescence stratégique peut déclencher un changement gouverné de l'architecture en service.
- **D (3) :** Inscrire la fin de support dans le registre de risques et lancer une étude technique comparative, puis décider de la re-entry ADM. Le risque d'obsolescence et la comparaison technique préparent la décision, mais la portée ADM et la trajectoire d'architecture restent à qualifier.
- **C (1) :** Préparer une migration pilote du composant concerné en supposant que les interfaces existantes resteront compatibles. Un pilote de migration peut réduire un risque technique, sans vérifier les autres dépendances et obligations cryptographiques.
- **A (0) :** Attendre l'arrêt effectif du support et demander ensuite une dérogation générale pour conserver la Target. Attendre l'arrêt du support avant d'agir laisse une exposition de sécurité prévisible non maîtrisée.

**Référence :** X2202, Practitioner, unité 6.

## P7 — Requirements Management

**Barème :** A=3, B=0, C=5, D=1.

- **C (5) :** Identifier le conflit, engager les stakeholders, analyser options et maintenir la trace de la décision, en distinguant le besoin de valeur analytique des méthodes possibles pour préserver la confidentialité. La bonne décision relie obligations, valeur et alternatives avec acceptation des stakeholders.
- **A (3) :** Définir un modèle de données pseudonymisé comme candidat et en mesurer les conséquences métier, puis formaliser les critères de conformité. La pseudonymisation est une option pertinente à évaluer, mais le conflit de requirements n'est pas encore arbitré par les owners.
- **D (1) :** Réduire la portée du besoin analytique aux données non sensibles, sans avoir évalué les résultats métier attendus. Réduire les données analytiques peut éviter certains risques sans démontrer que les résultats métier restent atteignables.
- **B (0) :** Demander à la plateforme d'analytics de décider automatiquement de la minimisation nécessaire selon les capacités du fournisseur. Laisser le fournisseur décider seul de la minimisation ne satisfait ni ownership ni arbitrage de confidentialité.

**Référence :** X2202, Practitioner, unité 7.

## P8 — Supporting ADM Work

**Barème :** A=0, B=3, C=1, D=5.

- **D (5) :** Capability-Based Planning peut aider à regrouper et prioriser le changement autour des capacités nécessaires, en consolidant gaps, solutions potentielles et dépendances pour construire les work packages. Le regroupement des gaps évite de confondre solutions isolées et capacités partagées.
- **B (3) :** Établir une matrice provisoire des gaps liés à l'identité et proposer un lot mutualisé, puis traiter les autres dépendances lors d'une seconde revue. La matrice provisoire des gaps et le lot mutualisé sont utiles, mais les dépendances des autres capabilities restent à consolider.
- **C (1) :** Financer d'abord la capability dont le business case est le plus favorable et demander aux autres équipes de s'y raccorder. Prioriser selon le meilleur business case isolé ne représente pas les interdépendances des capacités partagées.
- **A (0) :** Attribuer un lot à chaque projet existant et optimiser séparément les coûts après le démarrage des migrations. Un lot par projet maintient le cloisonnement au lieu de regrouper les gaps en capacités réutilisables.

**Référence :** X2202, Practitioner, unité 8.
