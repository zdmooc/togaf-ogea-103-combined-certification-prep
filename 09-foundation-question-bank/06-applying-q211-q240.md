# Introduction to Applying the ADM — Questions 211 à 240

## Q211 — Tailoring
Pourquoi tailor l'ADM ?
A. Pour supprimer toute structure
B. Pour éviter les stakeholders
C. Pour l'adapter au contexte, au scope et à la gouvernance de l'organisation
D. Pour imposer un seul niveau de détail
**Réponse : C.** Le tailoring garde la logique TOGAF tout en l'adaptant au contexte. A/B/D sont des déformations.
**Mapping : Applying ADM — Tailoring.**

## Q212 — Tailoring scope
Que peut-on adapter lors du tailoring ?
A. Les lois applicables
B. La réalité métier
C. Le fait qu'une architecture doive répondre à des concerns
D. Processus, terminologie, artifacts, gouvernance et niveau de détail
**Réponse : D.** TOGAF peut être adapté dans sa mise en œuvre, pas dans les contraintes externes ou la logique fondamentale.
**Mapping : Applying ADM — Tailoring.**

## Q213 — Tailoring discipline
Quel tailoring est le plus sain ?
A. Supprimer un artifact si aucune décision ni concern ne le justifie, en documentant l'adaptation
B. Supprimer Phase G pour éviter les reviews
C. Supprimer les mécanismes de gestion des requirements pour réduire le nombre d'artifacts
D. Sauter les stakeholders pour gagner du temps
**Réponse : A.** L'adaptation doit être intentionnelle et gouvernée. B/C/D suppriment des mécanismes essentiels.
**Mapping : Applying ADM — Tailoring.**

## Q214 — Tailoring vs inconsistency
Une équipe appelle « Phase A » un travail de Migration Planning sans explication. Quel risque ?
A. Améliorer automatiquement la méthode
B. Perdre le langage commun et la traçabilité
C. Réduire le besoin de gouvernance
D. Aucun risque
**Réponse : B.** Le tailoring ne doit pas rendre le framework incompréhensible ou incohérent.
**Mapping : Applying ADM — Tailoring.**

## Q215 — Iterative ADM
L'ADM peut être itératif parce que :
A. Les phases n'ont aucun objectif
B. Toute séquence est inutile
C. Les architectures et requirements sont affinées à mesure que la compréhension progresse
D. Il faut toujours recommencer depuis Preliminary
**Réponse : C.** L'itération est structurée, pas arbitraire. A/B/D sont faux.
**Mapping : Applying ADM — Iteration.**

## Q216 — Iteration between domains
Un choix Application révèle une contrainte Data majeure. Que peut-on faire ?
A. Valider l'Application Architecture sans analyser son impact sur les entités Data concernées
B. Attendre H
C. Refaire toujours Phase F
D. Itérer entre les travaux Data et Application
**Réponse : D.** L'ADM permet des boucles cohérentes entre domaines interdépendants.
**Mapping : Applying ADM — Iteration.**

## Q217 — Iteration and feedback
Pourquoi intégrer des feedback loops dans un environnement digital ?
A. Pour ajuster architecture et requirements selon les résultats réels
B. Pour supprimer la Target
C. Pour éviter les principles
D. Pour remplacer la governance
**Réponse : A.** Les feedback loops soutiennent l'apprentissage et l'évolution contrôlée.
**Mapping : Applying ADM — Iteration/Digital.**

## Q218 — Levels of Architecture
Pourquoi travailler à plusieurs niveaux d'architecture ?
A. Pour dupliquer les mêmes documents
B. Pour gérer la complexité et adapter le niveau de décision
C. Pour isoler totalement les équipes
D. Pour éviter l'Enterprise Architecture
**Réponse : B.** Les niveaux rendent les décisions proportionnées et coordonnées.
**Mapping : Applying ADM — Levels of Architecture.**

## Q219 — Enterprise level
Au niveau Enterprise, l'architecture se concentre surtout sur :
A. Le code d'une seule classe
B. Les détails de conception d'une API propre à une squad
C. Les orientations et cohérences transverses de l'entreprise
D. Une configuration de pod uniquement
**Réponse : C.** Le niveau Enterprise est large et stratégique.
**Distracteur B :** Ces décisions relèvent d'un niveau plus proche de la solution.
**Mapping : Applying ADM — Levels.**

## Q220 — Segment/Capability level
Un niveau segment/capability est utile pour :
A. Remplacer toute architecture entreprise
B. Définir un segment sans respecter les interfaces ni les standards de l'entreprise
C. Supprimer les dépendances
D. Détailler une partie cohérente de l'entreprise tout en restant aligné au niveau supérieur
**Réponse : D.** Il fournit un niveau intermédiaire de décision.
**Mapping : Applying ADM — Levels.**

## Q221 — Solution level
Une Solution Architecture doit idéalement :
A. Réaliser les intentions d'architecture supérieures tout en répondant au contexte de solution
B. Écarter les ABB approuvés même lorsqu'ils expriment des capacités requises par la solution
C. Redéfinir seule la stratégie d'entreprise
D. Échapper à la governance
**Réponse : A.** Les niveaux doivent rester cohérents, sans nier les contraintes locales.
**Mapping : Applying ADM — Levels.**

## Q222 — Partitioning
Architecture Partitioning sert à :
A. Définir une même profondeur de détail et une même durée pour toutes les architectures de l'entreprise
B. Diviser le paysage d'architecture en parties gouvernables avec frontières et responsabilités
C. Ordonner les releases d'un programme sans identifier les espaces de responsabilité
D. Appliquer des standards identiques à tous les composants sans gérer les interfaces entre domaines
**Réponse : B.** Le partitioning structure la complexité et les responsabilités.
**Mapping : Applying ADM — Partitioning.**

## Q223 — Partition boundary
Pourquoi clarifier les frontières entre partitions ?
A. Pour empêcher tout partage
B. Pour éliminer le Repository
C. Pour maîtriser ownership, interfaces et dépendances
D. Pour choisir un vendor
**Réponse : C.** Les frontières ambiguës génèrent incohérences et doublons.
**Mapping : Applying ADM — Partitioning.**

## Q224 — Federation
Dans une architecture fédérée, que recherche-t-on ?
A. Centraliser chaque décision
B. Autoriser toute divergence
C. Supprimer les standards
D. Un équilibre entre autonomie locale et cohérence globale
**Réponse : D.** La fédération combine autonomie et gouvernance partagée.
**Mapping : Applying ADM — Federation.**

## Q225 — Federation governance
Quel mécanisme aide une fédération d'équipes ?
A. Des principles, standards, interfaces et forums de gouvernance communs
B. Aucun contrat d'interface
C. Laisser chaque équipe décider ses standards sans mécanisme de cohérence transverse
D. Des décisions secrètes
**Réponse : A.** Des règles partagées rendent l'autonomie compatible avec la cohérence.
**Mapping : Applying ADM — Federation.**

## Q226 — Security cross-cutting
Comment appliquer la sécurité avec l'ADM ?
A. Ne traiter les risques de sécurité qu'après la dernière revue de conformité
B. Comme concern transverse intégré aux phases et requirements
C. Concentrer les exigences de sécurité exclusivement dans la Technology Architecture
D. Inscrire les contrôles de sécurité seulement après le choix de toutes les solutions
**Réponse : B.** Security/risk doivent influencer architecture, requirements et governance dès le début.
**Mapping : Applying ADM — Security.**

## Q227 — Security in A
En Phase A, la sécurité doit notamment :
A. Attendre la production
B. Choisir toutes les configurations finales
C. Identifier concerns, contraintes et risques majeurs de haut niveau
D. Être hors scope par défaut
**Réponse : C.** Les enjeux majeurs doivent être intégrés dès le cadrage sans sur-détailler.
**Mapping : Applying ADM — Security.**

## Q228 — Security in B/C/D
En B/C/D, une approche correcte est :
A. Traiter sécurité uniquement en D
B. Déduire les exigences de sécurité exclusivement de la plateforme technique retenue
C. Éviter toute traçabilité
D. Raffiner les requirements et controls de sécurité dans chaque domaine pertinent
**Réponse : D.** La sécurité traverse Business, Data, Application et Technology.
**Mapping : Applying ADM — Security.**

## Q229 — Security in G
En Phase G, la sécurité est notamment vérifiée par :
A. Des preuves de conformité aux requirements/controls approuvés
B. Le nombre de diagrams
C. La seule opinion du sponsor
D. La couleur du backlog
**Réponse : A.** G vérifie l'implémentation concrète.
**Mapping : Applying ADM — Security/Governance.**

## Q230 — Digital Enterprise
Dans une digital enterprise, l'architecture doit souvent :
A. Fixer une Architecture Definition Document immuable avant les premières itérations produit
B. Supporter vitesse, feedback, modularité et évolution continue tout en gardant la gouvernance
C. Remplacer toute gouvernance de domaine par les seules décisions quotidiennes des squads
D. S'appuyer exclusivement sur la Target Technology sans expliciter les drivers métier évolutifs
**Réponse : B.** TOGAF peut être appliqué dans un contexte digital de manière adaptée.
**Mapping : Applying ADM — Digital Enterprise.**

## Q231 — Digital building blocks
Pourquoi modulariser des building blocks dans un contexte digital ?
A. Pour créer davantage de dépendances cachées
B. Pour supprimer les contracts
C. Pour favoriser réutilisation, autonomie et évolution maîtrisée
D. Pour rendre les interfaces implicites
**Réponse : C.** La modularité bien gouvernée soutient vitesse et cohérence.
**Mapping : Applying ADM — Digital Enterprise.**

## Q232 — Continuous architecture
Une architecture digitale efficace est souvent :
A. Définie une fois en Preliminary et conservée sans révision pendant les releases de l'entreprise
B. Limitée à la seule Architecture Vision initiale sans itération entre Data et Application
C. Adaptée uniquement lorsque le comité de projet annule la roadmap et lance un nouveau programme
D. Maintenue et ajustée continuellement plutôt que figée une fois pour toutes
**Réponse : D.** Les environnements digitaux évoluent et exigent feedback et change management.
**Mapping : Applying ADM — Digital Enterprise.**

## Q233 — Agile and TOGAF
TOGAF et Agile sont :
A. Compatibles si l'ADM est adapté et la gouvernance intégrée aux boucles de delivery
B. Incompatibles car l'ADM exige de terminer intégralement toutes les phases avant chaque sprint
C. Compatibles seulement si les product owners remplacent toutes les autorités de gouvernance
D. Compatibles uniquement en Phase G, lorsque les produits sont déjà réalisés et testés
**Réponse : A.** L'un organise l'architecture, l'autre le delivery adaptatif ; ils peuvent se compléter.
**Mapping : Applying ADM — Agile and TOGAF.**

## Q234 — Architecture runway
Dans un environnement Agile, l'architecture doit :
A. Figer toutes les architectures de domaine avant le premier sprint et interdire leur évolution
B. Fournir suffisamment de direction et de constraints pour permettre le delivery sans figer tout le futur
C. Déléguer toutes les décisions aux produits sans maintenir les standards et exigences transverses
D. Limiter l'architecture aux contrôles réalisés après chaque déploiement, sans Vision cible
**Réponse : B.** L'architecture donne une direction évolutive et gouvernée.
**Mapping : Applying ADM — Agile and TOGAF.**

## Q235 — Agile governance
Quelle approche est préférable ?
A. Faire une review unique trois ans après
B. Supprimer les principles
C. Intégrer les architecture decisions et compliance checks dans le flux Agile
D. Ne jamais documenter les décisions
**Réponse : C.** Une gouvernance légère et continue est plus adaptée au rythme Agile.
**Mapping : Applying ADM — Agile and TOGAF.**

## Q236 — Large Enterprise
Dans une grande entreprise, quel problème devient particulièrement important ?
A. Réduire le nombre de stakeholders à un
B. N'avoir qu'une seule solution pour tout
C. Supprimer l'Architecture Repository
D. Coordonner plusieurs domaines, niveaux, partitions et cycles
**Réponse : D.** La complexité organisationnelle nécessite fédération et coordination.
**Mapping : Applying ADM — Large Enterprise.**

## Q237 — Large enterprise consistency
Comment maintenir la cohérence entre plusieurs équipes d'architecture ?
A. Principles, standards, metamodel, repository et gouvernance partagés
B. Aucun mécanisme commun
C. Chaque équipe redéfinit le vocabulaire
D. Pas de review inter-domaines
**Réponse : A.** Les mécanismes partagés permettent une architecture fédérée mais cohérente.
**Mapping : Applying ADM — Large Enterprise.**

## Q238 — Large enterprise reuse
Pourquoi le Repository est-il particulièrement utile à grande échelle ?
A. Pour remplacer les principes d'architecture par des décisions locales
B. Pour favoriser visibilité, réutilisation et cohérence entre nombreux travaux
C. Pour remplacer les architects
D. Pour éviter les standards
**Réponse : B.** Sans repository commun, la duplication et les divergences augmentent.
**Distracteur A :** Le Repository aide à appliquer principes et réutilisation, non à les remplacer.
**Mapping : Applying ADM — Large Enterprise.**

## Q239 — Context over rigidity
Quel principe d'application est le plus cohérent ?
A. Appliquer mécaniquement tous les artifacts
B. Supprimer les phases difficiles
C. Adapter l'ADM au contexte tout en préservant objectifs, traçabilité et gouvernance
D. Choisir la méthode après la solution
**Réponse : C.** TOGAF est tailorable mais reste discipliné.
**Mapping : Applying ADM — Synthesis.**

## Q240 — Applying ADM synthesis
Une banque avec 30 équipes Agile et plusieurs domaines veut utiliser TOGAF. Quelle approche est la meilleure ?
A. Un seul document central figé
B. Aucun principle pour laisser l'autonomie totale
C. Une seule équipe qui valide chaque petite décision
D. Architecture fédérée, tailoring, niveaux cohérents, governance continue et repository partagé
**Réponse : D.** Elle combine les mécanismes d'application adaptés à une grande organisation Agile.
**Mapping : Applying ADM — Synthesis.**

---
Questions originales de préparation.