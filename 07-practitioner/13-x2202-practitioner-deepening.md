# Practitioner — décisions, gouvernance et livrables avancés (X2202)

**Objectif :** passer de la reconnaissance de l'ADM à son application contextuelle et argumentée. Ce module complète les 8 domaines de `07-practitioner/` et sert à préparer l'OGEA-102 / OGEA-F102. Les codes cités correspondent à la section 3.2 du syllabus [X2202](https://www.opengroup.org/library/x2202).

## 1. Architecture Compliance : six niveaux (L2 U1, 1.5)

Une compliance assessment examine une **implémentation** face à une **architecture specification**, pas simplement l'emploi d'un produit ou le respect d'un planning.

| Niveau | Relation entre spécification et réalisation |
|---|---|
| **Irrelevant** | Aucun recouvrement pertinent : la conformité n'est pas applicable |
| **Consistent** | Certaines caractéristiques communes sont correctement réalisées ; la cible comporte des éléments non réalisés et l'implémentation contient d'autres éléments |
| **Compliant** | Tous les éléments réalisés sont conformes à la spécification, mais celle-ci comporte encore des éléments non réalisés |
| **Conformant** | Tous les éléments prévus par la spécification sont réalisés correctement ; d'autres éléments additionnels existent |
| **Fully Conformant** | Correspondance complète, sans caractéristique supplémentaire hors spécification |
| **Non-conformant** | Au moins une caractéristique commune est réalisée en contradiction avec la spécification |

**Piège :** `Compliant` et `Conformant` ne sont pas synonymes dans la classification TOGAF. Une non-conformité observée doit être évaluée, justifiée et gouvernée ; l'architecte ne « déclare pas » seul une dispense implicite.

**Cas de travail :** la cible définit (a) idempotence, (b) chiffrement des échanges, (c) audit des rejets. Le lot livré ne fournit que (a) et (b), tous deux conformes ; aucun autre service n'est livré. Niveau plausible : **Compliant**, pas Fully Conformant. Si le lot ajoute des fonctions additionnelles, sans violer les spécifications, il peut entrer dans une autre catégorie selon la définition exacte du référentiel.

## 2. Architecture states et contexte (L2 U1)

Reconnaître les états **candidate, current, transition, target**, ainsi que l'écart entre une architecture approuvée et l'état effectivement déployé. Pour chaque état, demander : qui l'a approuvé, à quel horizon, avec quel niveau de détail et quelles dépendances ?

Quand plusieurs équipes travaillent en agile : distinguer le **cap de l'architecture d'entreprise** du contenu incrémental de chaque sprint. Une organisation fédérée peut partager des principes et un Board tout en maintenant des décisions locales déléguées.

## 3. Phase A : la Vision doit créer des décisions (L2 U3)

Une Phase A utile mobilise **business goals, business drivers, constraints, stakeholders, concerns, business requirements, scope, Architecture Vision, Statement of Architecture Work et Communications Plan**. La sécurité et la readiness sont déjà prises en compte.

**Arbitrage :** le sponsor exige un délai de six mois ; le CISO refuse toute exemption et Operations signale l'absence d'équipe 24/7. La meilleure action n'est ni de produire directement la Phase D ni d'annuler la cible. Il faut établir la valeur attendue, expliciter les contraintes, envisager plusieurs trajectoires et clarifier le pouvoir de décision avant de figer le Statement of Architecture Work.

## 4. B/C/D : étapes et résultats entre domaines (L2 U4)

Le développement suit un cycle **sélectionner les modèles et viewpoints → développer Baseline/Target au niveau adéquat → identifier gaps et requirements → réconcilier les impacts entre domaines → obtenir les reviews et approbations nécessaires → enrichir Roadmap et spécifications**. Les activités peuvent être itératives ; elles ne prescrivent pas forcément une séquence linéaire.

**Exercice :** MayaBank veut centraliser toutes les données des paiements pour entraîner un moteur de fraude. Business veut une vision unifiée ; juridique interdit le transfert de certaines données hors pays ; C Application recommande un service unique mondial ; D propose une plateforme régionale standard. Comparer trois alternatives :

1. Centraliser sans distinction : ambition opérationnelle forte, mais non-conformité réglementaire inacceptable.
2. Modèle fédéré des données et services régionaux avec contrats d'échange standardisés : compromis possible, dépendant de la gouvernance des données.
3. Revenir à des silos sans partage : conformité apparente mais faible valeur métier.

La décision se prend après évaluation des contraintes et des parties prenantes, puis entraîne des itérations entre Data, Application et Technology Architecture ; elle ne se réduit pas à « choisir Phase C Data ».

## 5. Phase E : stratégie de mise en œuvre (L2 U5, 5.2–5.5)

Trois approches TOGAF à distinguer :

- **Greenfield** : créer une nouvelle réalisation, sans migration directe d'un composant hérité.
- **Revolutionary** : changement radical, avec bascule clairement définie de l'ancien vers le nouveau.
- **Evolutionary** : transformation graduelle par coexistence, migration par vagues et convergence.

La stratégie ne doit pas être choisie par préférence technologique. Démontrer **coûts, risques, dépendances, disponibilité des équipes, capacité opérationnelle, valeur métier, exigences de conformité**, puis identifier et regrouper les **work packages**.

**Implementation Factor Catalog** : inventorie les facteurs qui influencent le déploiement (risques, contraintes, dépendances, hypothèses, opportunités), en distinguant leurs impacts. **Consolidated Gaps, Solutions and Dependencies Matrix** : confronte les gaps issus de B/C/D, leurs solutions potentielles et dépendances, puis alimente les work packages et la roadmap. Ne pas confondre un gap avec un nom de produit.

**Transition Architecture** : état intermédiaire cohérent, exploitable, gouvernable et orienté vers la cible. Elle doit inclure les capacités opérationnelles et les exigences nécessaires pour chaque étape, pas uniquement un diagramme technique.

**Arbitrage MayaBank :** un basculement révolutionnaire minimise la coexistence mais expose les paiements à un risque de coupure. Une migration évolutive par familles de flux augmente les coûts temporaires et les besoins de réconciliation, mais permet la validation graduelle. L'architecte compare les risques résiduels, la valeur et la readiness avant de proposer des waves.

## 6. Phase F : priorisation fondée sur la valeur (L2 U5, 5.6–5.10)

Phase E prépare les options et groupes de travaux ; Phase F **évalue business value, interdépendances, capacités de financement, risques et séquencement** et confirme la Roadmap ainsi que l'Implementation and Migration Plan. Le sponsor peut peser sur la priorité, mais sa préférence n'est pas une preuve de valeur ni de faisabilité.

**Exemple :** mettre le moteur Fraud en première vague n'a aucun sens si la capacité de collecte des événements ISO 20022 dont il dépend n'est pas prête. Le plan rend explicites les prérequis et la valeur relative ; il peut proposer une vague préparatoire de référentiel événementiel.

## 7. Phase G : conformité et contrat (L2 U5, 5.11–5.14)

Comparer solution réalisée à **Architecture Definition Document, Architecture Requirements Specification, Architecture Contract, standards et principes**. Exiger des preuves de conformité et un mécanisme de dérogation/retour en conformité ; documenter les responsabilités de l'implémenteur, du sponsor et du Board.

**Décision :** utiliser un produit déjà approuvé ne dispense pas de vérifier l'implémentation du chiffrement, la traçabilité et la résilience. Une revue peut demander correction, acceptation formelle du risque ou escalade.

## 8. Phase H et impact des exigences (L2 U6–U7)

Le changement apparaît via Change Request, nouveau driver réglementaire, problème de valeur réalisée, incidents ou nouvelles requirements. L'analyse distingue **simplification, incremental, re-architecting** ; elle conclut à un changement gouverné, une révision de phases limitées ou un nouveau cycle ADM.

**Requirements Impact Assessment** : relie un changement d'exigence à ses impacts sur les artefacts, décisions, gaps, work packages, Transition Architectures, calendrier, risques et propriétaires. Requirements Management est transversal ; Phase H décide de la réponse à l'évolution de l'architecture en service.

**Exemple :** après la migration, l'obligation de vérifier le bénéficiaire des virements change. Mettre à jour la requirement ne suffit pas : il faut évaluer impacts de parcours métier, services, données, APIs, exigences sécurité et migration.

## 9. Supporting the ADM : TOGAF Library et Series Guides (L2 U8, 8.1–8.5)

Le **TOGAF Fundamental Content** définit le cadre central ; les **TOGAF Series Guides** approfondissent son application. **TOGAF Library** sert à repérer les guides, ressources et exemples pertinents ; il ne se substitue pas à l'Architecture Repository interne à l'entreprise.

| Besoin pratique | Ressource à consulter | Usage dans le cas |
|---|---|---|
| Développer une capacité EA | Leader's Guide / Architecture Capability | Définir gouvernance et rôles |
| Conduire un cycle concret | Practitioners' Approach | Travail et livrables par étapes |
| Agilité de l'entreprise | Enabling Enterprise Agility | Concilier delivery itératif et cohérence |
| Clarifier un besoin | Business Scenarios | Passer de l'ambition aux requirements |
| Décrire une capacité métier | Business Capabilities | Distinguer capacité et application |
| Comprendre création de valeur | Business Models / Value Streams | Aligner architecture et outcomes |
| Identifier échanges d'information | Information Mapping | Localiser les flux/dépendances |
| Clarifier responsabilités | Organization Mapping | Identifier owners et frontières |
| Intégrer sécurité et risques | Integrating Risk and Security | Raisonner sur risques transversaux |
| Architecture numérique | Digital Enterprise | Adapter l'ADM à un contexte digital |

La préparation ne doit pas supposer que chaque Series Guide est intégralement exigé : **lier chaque approfondissement à un learning outcome X2202**.

## 10. Quatre contextes d'application du Digital Practitioner Body of Knowledge (DPBoK)

Le DPBoK décrit quatre contextes de pratique — **Individual/Founder, Team, Team of Teams, Enterprise** — à mobiliser pour comprendre le niveau d'organisation et de coordination du travail numérique. Ils ne se substituent ni aux quatre domaines Business/Data/Application/Technology ni aux niveaux d'Architecture Landscape.

| Contexte | Préoccupation architecturale fréquente |
|---|---|
| Individual / Founder | Expérimentation, proposition de valeur initiale, décisions techniques à portée immédiate |
| Team | Collaboration d'une équipe produit, qualité, exploitation locale, boucle de retour |
| Team of Teams | Dépendances entre produits et plateformes, coordination, interfaces, gouvernance fédérée |
| Enterprise | Cohérence inter-domaines, portefeuille, gouvernance, risque et transformation à grande échelle |

**Exemple :** MayaBank peut expérimenter un modèle de détection de fraude au niveau Team, puis devoir arbitrer ses données communes et ses contraintes de sécurité au niveau Team of Teams et Enterprise. Le niveau d'organisation conditionne la granularité de gouvernance et les choix de coordination.

## 11. Atelier Open Book pratique (90 minutes)

1. Lire le scénario sans ouvrir la référence et annoter **drivers, concerns, état ADM, rôle décisionnaire, contraintes, deadline**.
2. Éliminer les décisions sans séquence logique, puis identifier **deux options crédibles**.
3. Nommer la nuance à départager (ex. Phase E work package vs Phase F prioritization).
4. Ouvrir le **document officiel correspondant dans l'interface de test** et chercher le terme précis. Ne pas supposer un accès Internet libre.
5. Revenir au scénario, justifier la meilleure option et les limites de la seconde.
6. Consigner temps de recherche, document, section, erreur et révision nécessaire.

Un entraînement sérieux doit vérifier les **références mobilisées**, la qualité de l'arbitrage et le délai, et non seulement attribuer des scores.

## 12. Modèle de corrigé Practitioner

Pour chaque question, fournir : `X2202 LO`, hypothèses importantes, indices de l'énoncé, 5 points (meilleure action), 3 points (partiellement valide), 1 point (très limitée), 0 point (non adaptée), source pertinente, points d'attention. **Un 3 points ne peut jamais correspondre à une proposition que le corrigé reconnaît fausse sur son principe central.**

Cette pédagogie est indépendante du barème confidentiel des vraies questions d'examen. Les cas MayaBank sont fictifs et destinés à l'entraînement, non aux prévisions d'items officiels.
