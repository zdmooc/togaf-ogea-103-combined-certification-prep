# Introduction to ADM Techniques — Questions 166 à 210

## Q166 — Stakeholder Management
La première finalité du Stakeholder Management est de :
A. Construire la matrice de traçabilité entre exigences et building blocks
B. Identifier les parties prenantes, leurs concerns et la stratégie d'engagement
C. Prioriser les work packages
D. Remplacer Requirements Management
**Réponse : B.** La technique organise l'engagement des parties prenantes. A/C relèvent d'autres sujets ; D est faux.
**Distracteur A :** La traçabilité fait partie de la gestion des exigences ; la première étape du Stakeholder Management est l'identification et l'engagement des parties.
**Mapping : ADM Techniques — Stakeholder Management.**

## Q167 — Power/Interest
Une matrice power/interest aide principalement à :
A. Définir la Target Data Architecture
B. Choisir un SBB
C. Adapter le niveau d'engagement selon influence et intérêt
D. Vérifier la conformité des services aux exigences d'architecture
**Réponse : C.** Elle aide à segmenter l'approche d'engagement. A/B/D ne sont pas son rôle.
**Distracteur D :** Power/Interest concerne les acteurs et le plan d'engagement, non une Compliance Review.
**Mapping : ADM Techniques — Stakeholder Management.**

## Q168 — Stakeholder concern
Un stakeholder puissant exprime une inquiétude forte sur la résilience. Quelle action est la plus cohérente ?
A. Considérer le stakeholder comme satisfait tant que la Target utilise les standards approuvés
B. Consigner le risque dans le Migration Plan sans relier ses implications aux requirements
C. Préparer un test technique de résilience sans impliquer le stakeholder dans les décisions de cible
D. Capturer le concern, choisir une view adaptée et en dériver des requirements
**Réponse : D.** La technique relie stakeholder, concern, view et requirements. A/B/C sautent des étapes.
**Mapping : ADM Techniques — Stakeholder Management.**

## Q169 — Communication
Pourquoi produire des views différentes pour des stakeholders différents ?
A. Parce que leurs concerns et décisions attendues diffèrent
B. Pour augmenter artificiellement la documentation
C. Parce qu'une seule architecture n'existe pas
D. Pour éviter les requirements
**Réponse : A.** Les views doivent répondre aux concerns. B/C/D sont faux.
**Mapping : ADM Techniques — Stakeholder Management.**

## Q170 — Business Scenario
Un Business Scenario est utilisé principalement pour :
A. Comparer des architectures Baseline et Target après qu'elles ont déjà été définies et approuvées
B. Relier un problème/opportunité métier à des requirements d'architecture
C. Contrôler la conformité des composants livrés aux exigences pendant Implementation Governance
D. Prioriser les lots de migration à partir d'un calendrier sans clarifier les besoins métier initiaux
**Réponse : B.** La technique transforme un besoin métier en exigences compréhensibles. A/C/D sont d'autres usages.
**Mapping : ADM Techniques — Business Scenarios.**

## Q171 — Business Scenario components
Quel élément est typiquement utile dans un Business Scenario ?
A. La liste des solutions candidates, même sans acteurs ni résultat métier défini
B. Un diagramme technique seul, sans environnement, acteurs ni outcomes du scénario
C. Acteurs, environnement, problème, résultat attendu et requirements
D. Une matrice de comparaison des standards technologiques de la cible
**Réponse : C.** Le scénario décrit suffisamment le contexte pour dériver les requirements. A/B/D sont insuffisants.
**Distracteur D :** Une telle matrice peut être utile plus tard, mais ne définit pas le contexte d'un Business Scenario.
**Mapping : ADM Techniques — Business Scenarios.**

## Q172 — Vague objective
« Mettre de l'IA » est une formulation trop vague. Quelle technique aide à la transformer en besoin exploitable ?
A. Compliance Review
B. Migration waves uniquement
C. Architecture Contract
D. Business Scenarios
**Réponse : D.** Le Business Scenario clarifie problème, acteurs, contexte et résultats attendus.
**Mapping : ADM Techniques — Business Scenarios.**

## Q173 — Business Scenario validation
Pourquoi valider un Business Scenario avec les stakeholders ?
A. Pour vérifier que le problème et les requirements reflètent bien la réalité métier
B. Pour figer le choix du fournisseur avant d'analyser les besoins de chaque acteur
C. Pour remplacer les Business Requirements par les seules contraintes techniques
D. Pour garantir que chaque stakeholder dispose exactement du même viewpoint
**Réponse : A.** La validation garantit pertinence et compréhension partagée. B/C/D sont faux.
**Mapping : ADM Techniques — Business Scenarios.**

## Q174 — Gap Analysis
La Gap Analysis compare principalement :
A. Sponsor et architecte
B. Baseline et Target
C. Les Transition Architectures et les work packages proposés
D. View et viewpoint
**Réponse : B.** Elle identifie ce qui doit être créé, modifié, supprimé ou conservé. A/C/D ne sont pas son objet.
**Distracteur C :** Ils découlent de l'analyse des gaps et ne sont pas les deux états comparés.
**Mapping : ADM Techniques — Gap Analysis.**

## Q175 — Gap categories
Quel résultat peut provenir d'une Gap Analysis ?
A. Un stakeholder map
B. Un examen de certification
C. Élément manquant dans la Baseline mais requis dans la Target
D. Une exception de gouvernance formellement approuvée
**Réponse : C.** Un manque entre actuel et cible est un gap. A est autre technique ; B/D hors sujet.
**Distracteur D :** Une exception relève d'une décision de conformité ; une Gap Analysis révèle d'abord des différences.
**Mapping : ADM Techniques — Gap Analysis.**

## Q176 — Remove gap
Un composant existe en Baseline mais ne doit plus exister en Target. Comment le considérer ?
A. Comme un nouveau building block à créer et ajouter à la Target Architecture future
B. Comme une requirement à préserver inchangée sans analyser sa nécessité dans la cible
C. Comme un standard à approuver automatiquement pour tous les composants des domaines
D. Comme un gap de suppression/retrait à traiter
**Réponse : D.** La Gap Analysis identifie aussi ce qui doit être éliminé.
**Mapping : ADM Techniques — Gap Analysis.**

## Q177 — Gap vs migration
Pourquoi Gap Analysis n'est-elle pas Migration Planning ?
A. Elle identifie les différences ; Migration Planning priorise et séquence les changements
B. Elles sont identiques
C. Elle doit nécessairement sélectionner une solution technologique pour chaque gap
D. Migration Planning décrit la Baseline
**Réponse : A.** Gap = quoi changer ; migration planning = comment/ordre de mise en œuvre.
**Distracteur C :** L'identification des gaps doit rester distincte de la sélection et du séquencement des solutions.
**Mapping : ADM Techniques — Gap Analysis.**

## Q178 — Cross-domain gap
Un gap métier provoque un besoin data et applicatif. Que faut-il faire ?
A. Traiter chaque gap comme totalement isolé
B. Tracer les dépendances entre gaps de domaines
C. Documenter les impacts Data et Application sans tracer le gap métier qui les motive
D. Passer directement à G
**Réponse : B.** Les gaps sont souvent interdépendants et doivent être consolidés.
**Mapping : ADM Techniques — Gap Analysis.**

## Q179 — Interoperability
L'interoperability traite principalement :
A. La conformité d'une implémentation aux standards techniques de l'entreprise indépendamment de ses échanges
B. La traçabilité des décisions d'Architecture Board vers les contrats des fournisseurs
C. La capacité de systèmes/organisations à travailler ensemble efficacement
D. Le classement des applications dans les différentes couches d'un Architecture Repository
**Réponse : C.** Elle concerne échanges, compatibilité et coopération à plusieurs niveaux.
**Mapping : ADM Techniques — Interoperability.**

## Q180 — Levels of interoperability
L'interoperability peut concerner :
A. La seule connectivité réseau, sans contrats d'information ni coordination métier
B. Le seul modèle de bases de données, indépendamment des services échangés
C. Les seuls Architecture Contracts entre fournisseurs, sans échanges d'information
D. Business, information, applications et technologies
**Réponse : D.** Elle est multi-dimensionnelle. A/B/C sont trop étroits.
**Mapping : ADM Techniques — Interoperability.**

## Q181 — Semantic interoperability
Deux systèmes échangent le même champ mais avec des significations différentes. C'est surtout un problème :
A. Sémantique/informationnel
B. Un problème de topologie réseau même lorsque la connectivité fonctionne correctement
C. De stakeholder map
D. De Phase H
**Réponse : A.** L'échange technique fonctionne mais le sens n'est pas partagé.
**Mapping : ADM Techniques — Interoperability.**

## Q182 — Organizational interoperability
Deux entités ont des responsabilités incompatibles malgré des APIs compatibles. Le problème est principalement :
A. Technique : les protocoles et les versions empêchent l'établissement d'une connexion entre les services
B. Organisationnel/business interoperability
C. Informationnelle : les deux entités attribuent des significations différentes aux mêmes données
D. Applicative : les deux partenaires utilisent des frameworks différents malgré des règles métier identiques
**Réponse : B.** L'interopérabilité dépasse la technique et inclut processus et responsabilités.
**Mapping : ADM Techniques — Interoperability.**

## Q183 — Transformation Readiness
Business Transformation Readiness sert à :
A. Vérifier uniquement que les composants livrés utilisent les standards de plateforme
B. Identifier les gaps entre Baseline et Target sans analyse des capacités organisationnelles
C. Évaluer si l'organisation est prête à absorber et soutenir la transformation
D. Comparer les performances des produits d'infrastructure sans évaluer les équipes d'exploitation
**Réponse : C.** La technique évalue capacité organisationnelle, culture, compétences, leadership, etc.
**Distracteur D :** La readiness porte sur la capacité de transformation de l'organisation, plus large que la conformité technique.
**Mapping : ADM Techniques — Business Transformation Readiness.**

## Q184 — Readiness factors
Quel facteur est pertinent pour Transformation Readiness ?
A. Couleur du diagramme
B. La conformité technique des seuls composants applicatifs
C. Nombre de pages du document
D. Leadership, compétences et capacité au changement
**Réponse : D.** La readiness est organisationnelle et humaine autant que technique.
**Distracteur B :** Elle est utile mais ne remplace pas sponsor, capacités humaines et exploitation.
**Mapping : ADM Techniques — Business Transformation Readiness.**

## Q185 — Low readiness
La cible est correcte mais les équipes n'ont pas les compétences nécessaires. Quelle technique aide à caractériser ce risque ?
A. Transformation Readiness Assessment
B. Architecture Compliance Review des composants déjà déployés par l'équipe de réalisation
C. Gap Analysis centrée sur les différences entre plateformes matérielles
D. Architecture Contract fixant les engagements des seuls fournisseurs techniques
**Réponse : A.** Le manque de compétences est un frein de readiness.
**Mapping : ADM Techniques — Business Transformation Readiness.**

## Q186 — Readiness action
Une faible readiness doit conduire à :
A. Déployer la Target sans adapter la capacité organisationnelle ou le modèle d'exploitation
B. Prévoir des actions de changement, compétences et gouvernance dans la roadmap
C. Retenir la Target actuelle comme acquise sans mesurer les capacités d'adoption
D. Confier le risque de résistance au seul fournisseur de la plateforme
**Réponse : B.** La technique alimente la planification de transformation.
**Mapping : ADM Techniques — Business Transformation Readiness.**

## Q187 — Risk Management
Risk Management sert principalement à :
A. Définir uniquement les exigences de performance du service technique le plus critique
B. Construire la Business Architecture sans étudier les conséquences des incertitudes
C. Identifier, analyser, traiter et suivre les risques d'architecture/transformation
D. Vérifier seulement la conformité aux standards des composants déjà livrés
**Réponse : C.** Le risque traverse le cycle. A/B/D sont faux.
**Mapping : ADM Techniques — Risk Management.**

## Q188 — Risk exposure
Un risque combine généralement :
A. Nombre de diagrams et de pages
B. Stakeholder et viewpoint
C. ABB et SBB
D. Probabilité et impact
**Réponse : D.** L'exposition est classiquement appréciée par likelihood × impact.
**Mapping : ADM Techniques — Risk Management.**

## Q189 — Mitigation
Une mitigation est :
A. Une action visant à réduire probabilité et/ou impact d'un risque
B. Une description de gap entre Baseline et Target avant toute solution candidate
C. Une classification des informations échangées entre services interbancaires
D. Une preuve de conformité d'un composant déployé à ses standards
**Réponse : A.** La mitigation réduit l'exposition. B/C/D sont autres concepts.
**Mapping : ADM Techniques — Risk Management.**

## Q190 — Residual risk
Le residual risk est :
A. Le niveau de risque estimé avant l'application de contrôles ou de mesures de mitigation
B. Le risque restant après traitements/mitigations
C. Une opportunité de gain qui n'a pas encore été transformée en work package financé
D. Un gap architectural entre les états Baseline et Target indépendamment de l'exposition au risque
**Réponse : B.** Après mitigation, une exposition peut subsister et doit être acceptée ou traitée.
**Mapping : ADM Techniques — Risk Management.**

## Q191 — Risk owner
Pourquoi attribuer un risk owner ?
A. Pour supprimer le risk register
B. Pour choisir l'option technologique la moins coûteuse
C. Pour clarifier responsabilité de suivi et décision
D. Pour remplacer les stakeholders
**Réponse : C.** L'ownership rend le traitement gouvernable.
**Distracteur B :** Le risk owner n'est pas l'acheteur d'une solution ; il porte la responsabilité du traitement et du suivi du risque.
**Mapping : ADM Techniques — Risk Management.**

## Q192 — Capability-Based Planning
Capability-Based Planning commence principalement par :
A. Les applications déjà déployées et leurs versions pour établir la seule Baseline Technology
B. Les initiatives déjà financées, sans comparaison des capacités métier communes
C. Les projets de migration classés par date de mise en production indépendamment des résultats
D. Les capacités que l'entreprise doit posséder pour atteindre ses objectifs
**Réponse : D.** La technique part de l'aptitude métier, pas d'une solution.
**Mapping : ADM Techniques — Capability-Based Planning.**

## Q193 — Capability vs project
Pourquoi une capability n'est-elle pas un projet ?
A. Une capability est une aptitude durable ; un projet est un moyen temporaire de changement
B. Capability et Project sont des objets de même durée, différant seulement par leur budget
C. Une capability correspond à une version logicielle précise
D. Un projet est un viewpoint
**Réponse : A.** La distinction évite de confondre résultat durable et véhicule de transformation.
**Distracteur C :** L'aptitude métier perdure au-delà des versions et des projets qui la rendent possible.
**Mapping : ADM Techniques — Capability-Based Planning.**

## Q194 — Capability increment
Un capability increment représente :
A. Une étape de déploiement d'un composant technologique sans changement de capability
B. Une amélioration progressive d'une capacité dans la trajectoire
C. Une modification de requirement consignée sans impact sur les résultats métier
D. Une Architecture View qui représente la même capability sous un autre viewpoint
**Réponse : B.** La technique permet d'organiser la montée en capacité par étapes.
**Mapping : ADM Techniques — Capability-Based Planning.**

## Q195 — Capability and roadmap
Comment Capability-Based Planning aide-t-il la roadmap ?
A. En choisissant d'abord un produit cloud puis en attribuant a posteriori des capabilities
B. En définissant seulement la liste des projets déjà financés sans mesure de valeur métier
C. En reliant work packages et transitions aux capacités métier à développer
D. En remplaçant tous les work packages par une même Architecture Vision globale
**Réponse : C.** La roadmap devient orientée outcomes/capabilities plutôt que technologie seule.
**Mapping : ADM Techniques — Capability-Based Planning.**

## Q196 — Migration Planning Techniques
Quel est le but des techniques de Migration Planning ?
A. Produire directement les composants techniques d'une solution avant le cadrage du besoin
B. Évaluer uniquement la conformité de la solution achevée aux exigences approuvées
C. Définir les capabilities métier en substituant les work packages à la Business Architecture
D. Aider à prioriser et séquencer les changements
**Réponse : D.** Elles soutiennent surtout Phase F et la construction d'un plan réaliste.
**Mapping : ADM Techniques — Migration Planning.**

## Q197 — Business value
Lors de la priorisation des work packages, quel critère est pertinent ?
A. Business value
B. Ordre alphabétique
C. Couleur du diagramme
D. Préférence personnelle
**Réponse : A.** Valeur, coût, risque et dépendances sont des critères défendables.
**Mapping : ADM Techniques — Migration Planning.**

## Q198 — Dependency
Un work package B dépend d'un socle livré par A. Quel ordre est généralement nécessaire ?
A. B avant A sans mitigation
B. A avant B
C. Ordre au hasard
D. Les deux sont forcément indépendants
**Réponse : B.** La dépendance impose un prérequis, sauf solution de transition explicitement conçue.
**Mapping : ADM Techniques — Migration Planning.**

## Q199 — Risk/value balance
Deux work packages ont forte valeur, mais l'un a un risque très élevé. Que faut-il faire ?
A. Prioriser le work package offrant le meilleur bénéfice nominal indépendamment des risques résiduels
B. Retenir le work package le moins coûteux puis reporter les évaluations de dépendances à la Phase G
C. Évaluer explicitement valeur, risque, dépendances et capacité d'exécution avant priorité
D. Établir l'ordre des livraisons uniquement en fonction des disponibilités des équipes techniques
**Réponse : C.** La priorisation est multi-critères et gouvernée.
**Mapping : ADM Techniques — Migration Planning.**

## Q200 — Incremental migration
Pourquoi une migration incrémentale peut-elle être préférable ?
A. Elle élimine toute gouvernance
B. Elle interdit les Transition Architectures
C. Elle rend les requirements inutiles
D. Elle peut réduire le risque et permettre des feedback loops
**Réponse : D.** L'incrémental peut sécuriser la transformation. A/B/C sont faux.
**Mapping : ADM Techniques — Migration Planning.**

## Q201 — Technique selection: WHO
La question principale est « qui doit être engagé et comment ? ». Quelle technique ?
A. Stakeholder Management
B. Gap Analysis
C. Risk Management
D. Migration Planning
**Réponse : A.** La technique traite identification, influence, concerns et engagement.
**Mapping : ADM Techniques — Selection.**

## Q202 — Technique selection: WHAT BUSINESS NEED
La question est « quel problème métier devons-nous réellement résoudre ? ». Quelle technique ?
A. Compliance Review
B. Business Scenarios
C. Partitioning
D. ABB/SBB
**Réponse : B.** Business Scenarios clarifie le besoin et les requirements.
**Mapping : ADM Techniques — Selection.**

## Q203 — Technique selection: WHAT MUST CHANGE
La question est « qu'est-ce qui diffère entre l'actuel et la cible ? ». Quelle technique ?
A. Stakeholder Management
B. Architecture Contract
C. Gap Analysis
D. Viewpoint selection uniquement
**Réponse : C.** Gap Analysis compare Baseline et Target.
**Mapping : ADM Techniques — Selection.**

## Q204 — Technique selection: CAN WORK TOGETHER
La question est « ces organisations et systèmes peuvent-ils travailler ensemble ? ». Quelle technique ?
A. Business Scenario
B. Architecture Board
C. Requirements repository
D. Interoperability Analysis
**Réponse : D.** L'interoperability examine compatibilité business, information, application et technology.
**Mapping : ADM Techniques — Selection.**

## Q205 — Technique selection: ARE WE READY
La question est « l'organisation est-elle prête à changer ? ». Quelle technique ?
A. Business Transformation Readiness
B. Gap Analysis uniquement
C. Compliance Review
D. SBB selection
**Réponse : A.** Elle évalue leadership, culture, compétences et capacité d'adoption.
**Mapping : ADM Techniques — Selection.**

## Q206 — Technique selection: WHAT CAN GO WRONG
La question est « quels événements pourraient empêcher les objectifs ? ». Quelle technique ?
A. Viewpoint
B. Risk Management
C. Capability Map seulement
D. Architecture Contract
**Réponse : B.** Le risque traite incertitude, impact et mitigation.
**Mapping : ADM Techniques — Selection.**

## Q207 — Technique selection: WHAT CAPABILITY
La question est « quelle aptitude métier devons-nous développer ? ». Quelle technique ?
A. Compliance Review
B. Migration wave
C. Capability-Based Planning
D. Stakeholder matrix uniquement
**Réponse : C.** La technique structure la transformation par capacités.
**Mapping : ADM Techniques — Selection.**

## Q208 — Technique selection: IN WHAT ORDER
La question est « dans quel ordre exécuter les changements ? ». Quelle technique ?
A. Business Scenarios
B. Viewpoint design
C. Architecture Principles
D. Migration Planning Techniques
**Réponse : D.** Ces techniques priorisent et séquencent la transformation.
**Mapping : ADM Techniques — Selection.**

## Q209 — Multiple techniques
Peut-on utiliser plusieurs techniques sur un même engagement ?
A. Oui, elles répondent à des problèmes complémentaires
B. Non, une seule technique est autorisée
C. Combiner les techniques uniquement lorsque l'architecture est déjà en Phase H
D. N'utiliser plusieurs techniques qu'en l'absence de stakeholders identifiables
**Réponse : A.** Un engagement réel combine souvent stakeholder, gap, risk, readiness, capability et migration planning.
**Mapping : ADM Techniques — Integration.**

## Q210 — Technique synthesis
Quel enchaînement est le plus cohérent pour une transformation complexe ?
A. Business Scenario → Compliance Review → Architecture Contract, sans Baseline ni Target
B. Stakeholders → Business Scenario → Gap/Risk/Readiness → Capability planning → Migration planning
C. Phase H → Technology Architecture → Preliminary, sans cadrage des drivers métier
D. Migration Plan → Architecture Vision → Gap Analysis, sans gestion des exigences
**Réponse : B.** Il combine les techniques selon la progression du problème. A/C/D sont prématurés ou incohérents.
**Mapping : ADM Techniques — Synthesis.**

---
Questions originales de préparation.