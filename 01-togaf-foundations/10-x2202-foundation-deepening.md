# Compléments Foundation — objectifs X2202 sous-couverts

**Périmètre :** préparation OGEA-101 / OGEA-F101. Ce chapitre complète les fichiers 01–06 et 02–06, sans remplacer le TOGAF Standard. Les identifiants ci-dessous renvoient au syllabus public **X2202, section 3.1**.

## 1. Finalités et niveaux d'abstraction (L1 1.2–1.8, 5.5)

Le praticien développe l'architecture d'entreprise pour **orienter un changement cohérent** et réaliser des bénéfices métier. Quatre usages structurent le cadrage :

| Usage | Décision attendue | Exemple banque |
|---|---|---|
| **Strategy** | Choix d'orientation et d'investissement | Définir une cible de paiements instantanés |
| **Portfolio** | Arbitrage des initiatives et de leurs interdépendances | Prioriser les capacités Fraud et Settlement |
| **Project** | Encadrer la réalisation d'un changement délimité | Migration d'une application vers OpenShift |
| **Solution Delivery** | Orienter les décisions de conception/implémentation | Exiger idempotence et traçabilité des paiements |

Ces usages ne sont **pas** les quatre domaines Business/Data/Application/Technology. Une question peut mélanger les deux taxonomies : distinguer **pourquoi l'architecture est sollicitée** et **sur quel domaine porte le modèle**.

Quatre questions progressives d'abstraction : **Why** (motivation, outcomes), **What** (capacités/éléments nécessaires), **How** (réalisation logique et interactions), **With What** (composants physiques/solutions). Ne pas confondre ce schéma avec les phases ADM : on peut raisonner à plusieurs niveaux dans chaque phase.

**Exercice :** une banque exige « régler 99,99 % des virements en moins de 10 secondes ». Why = valeur/contrainte métier ; What = capacité de compensation rapide ; How = orchestration et contrats de service ; With What = technologies retenues après justification. Le choix « OpenShift » ne constitue pas à lui seul la Business Architecture.

## 2. Glossaire prioritaire de l'Unité 2 (L1 2.1)

| Terme | Distinction à retenir |
|---|---|
| Enterprise | Ensemble d'organisations ou de parties ayant des objectifs communs, indépendamment de leur statut juridique |
| Architecture Model | Représentation simplifiée d'un aspect de l'architecture |
| Modeling | Activité de création ou de maintien des modèles |
| Metamodel | Définit les types d'éléments, leurs propriétés et relations |
| Artifact | Représentation de contenu : Catalog, Matrix ou Diagram |
| Deliverable | Produit de travail formel soumis à revue/approbation |
| Building Block | Élément potentiellement réutilisable décrivant ou réalisant une capacité |
| Capability | Aptitude à atteindre un résultat métier, sans présupposer l'application |
| Business Model | Logique de création, de délivrance et de capture de valeur |
| Business Architecture | Structure des capacités, services, organisation et processus métier |
| Data Architecture | Organisation, gouvernance et échange des données |
| Digital Architecture | Architecture d'un système ou service numérique, articulant expériences, capacités, données, applications et technologies ; ne désigne pas une phase ADM distincte |
| Application Architecture | Structure des services applicatifs et de leurs interactions |
| Technology Architecture | Plateformes, services techniques et infrastructures |
| Architecture Landscape | Ensemble cohérent d'états architecturaux, selon les niveaux et les horizons |
| Strategic Architecture | Vue large de transformation à long horizon |
| Segment Architecture | Architecture d'un périmètre métier ou organisationnel délimité |
| Capability Architecture | Vue centrée sur une capacité et ses dépendances |
| Transition Architecture | État intermédiaire cohérent entre Baseline et Target |
| Gap | Différence établie entre l'existant et la cible |
| Requirement | Condition ou capacité exigée, analysable et vérifiable |
| Role | Ensemble de responsabilités associées à une fonction |
| Stakeholder | Partie concernée ou affectée par l'architecture |
| Work Package | Ensemble cohérent de travaux pour réaliser le changement |

**Limite officielle importante :** l'Unité 2, L1 2.1 indique que les termes ne sont pas examinables séparément s'ils ne figurent pas dans un autre learning outcome. Ils restent indispensables au raisonnement, sans créer arbitrairement une nouvelle section de questions de définitions.

## 3. Architecture Repository : les sept rubriques à connaître pour X2202 Practitioner (L2 8.5)

**Correction du 1er novembre 2026 :** une ancienne version de ce chapitre présentait **huit** catégories et mélangeait le composant technique *Architecture Metamodel* avec la liste pédagogique de l'objectif **X2202 L2 8.5**. Le syllabus officiel énumère précisément les **sept** rubriques suivantes, avec les intitulés ci-dessous.

| Rubrique officielle de l'objectif L2 8.5 | Usage |
|---|---|
| Architecture Landscape | États, domaines, niveaux et horizons des architectures |
| Reference Library | Références, patterns et éléments réutilisables |
| Standards Library | Standards applicables aux architectures et solutions |
| Governance Repository | Décisions de gouvernance, conformité, exceptions et preuves |
| Architecture Requirements Repository | Exigences et traçabilité |
| Solutions Landscape | Solutions mises en œuvre et leur rapport aux architectures |
| Enterprise Repository | Ensemble de ressources et référentiels au niveau entreprise |

**Attention aux variantes terminologiques :** *Standards Information Base* et *Governance Log* sont des termes TOGAF employés dans certaines représentations du Repository, mais il ne faut pas les substituer sans explication aux libellés de l'objectif 8.5. L'**Architecture Metamodel** reste une notion fondamentale du Content Framework et du Repository, **sans constituer une huitième rubrique dans la liste X2202 8.5**.

**Piège :** *Standards Library* rassemble les standards, alors que l'Architecture Definition Document décrit une architecture et l'Architecture Requirements Specification les conditions qu'elle doit satisfaire.

**Référence officielle :** X2202 v4.0 (avril 2022), §3.2.8, learning outcome **8.5**, page imprimée 19.

## 4. Architecture Principles : forme et qualités (L1 4.2–4.4)

Le canevas utile est **Name / Statement / Rationale / Implications**. Un bon ensemble de principes possède cinq qualités : **Understandable, Robust, Complete, Consistent, Stable**.

- Understandable : compréhensible sans ambiguïté par les parties prenantes.
- Robust : suffisamment précis pour soutenir des décisions difficiles.
- Complete : couvre les grands enjeux pertinents sans trous majeurs.
- Consistent : évite des contradictions bloquantes entre principes.
- Stable : reste durable tout en permettant des révisions gouvernées.

**Exemple :** « Reuse before buy before build » doit préciser sa portée et ses exceptions : réutiliser à tout prix n'est pas un principe robuste quand cela viole une exigence réglementaire.

## 5. Gouvernance et conformité (L1 6.1–6.5)

Les six caractéristiques classiques de la gouvernance sont **Discipline, Transparency, Independence, Accountability, Responsibility, Fairness**. Les mécanismes TOGAF à distinguer : Architecture Board (arbitrage), Architecture Contract (engagements), Compliance Review (évaluation), exception/dispensation (décision tracée).

Exemple : un fournisseur met en production un protocole non approuvé. Le Board ne répare pas le protocole ; il statue sur le constat de non-conformité, les risques et l'action corrective, puis suit sa réalisation avec des responsables désignés.

## 6. ADM : statut, scoping, informations échangées (L1 3.2, 3.5, 3.25)

**Draft :** architecture/livrable en cours d'élaboration et de validation ; **Approved :** version revue et acceptée selon les règles de gouvernance applicables. Approuvé ne signifie pas « immuable » : un changement passe par la gouvernance.

**Quatre dimensions de scoping :** largeur de l'entreprise concernée, profondeur de détail, domaines d'architecture inclus, période/horizon de planification.

**Flux d'informations :** Phase A établit une Vision et un Statement of Architecture Work, B/C/D définissent Baseline/Target/gaps et enrichissent Roadmap/requirements, E regroupe les work packages et les transitions, F affine la priorisation et le plan de migration, G vérifie l'implémentation, H évalue les changements. Requirements Management interagit avec toutes les phases ; l'ADM n'est pas un waterfall.

**Exercice :** un changement de réglementation découvert en D peut modifier la requirement, le modèle Data en C et le coût de migration en F. Le bon raisonnement est itératif, pas « terminer D et ignorer C ».

## 7. Phase H : trois classes de changement (L1 3.21–3.22 ; L2 6)

| Type | Traitement type | Exemple |
|---|---|---|
| Simplification | Gouvernance/changement limité | Rationaliser des composants équivalents |
| Incremental | Changement maîtrisé, parfois ré-architecture partielle | Ajouter une capacité sans renverser la Target |
| Re-architecting | Nouveau travail d'architecture / nouveau cycle ADM | Changement de modèle métier remettant en cause la cible |

La distinction **minor/major** est une simplification utile, **pas** la taxonomie à trois classes à apprendre.

## 8. Interoperability (L1 4.7)

Ne pas remplacer la présentation TOGAF par un inventaire inventé de « cinq dimensions ». Distinguer les catégories **Operational/Business**, **Information** et **Technical**. La sécurité peut être une contrainte transversale, pas une quatrième catégorie officielle de cette classification.

Un exemple classique de **degrés d'interopérabilité** porte sur la progression : échanges non structurés, échanges structurés, partage automatisé de données, puis interprétation commune de l'information. Ces degrés illustrent un cadre de mesure, à adapter au contexte.

**Cas :** deux API utilisent HTTPS et JSON mais codifient différemment « date de règlement ». Il existe une compatibilité technique partielle, pas une interopérabilité informationnelle suffisante.

## 9. Business Transformation Readiness (L1 4.8)

L'évaluation doit considérer non seulement la maturité technique mais les facteurs **Vision ; Desire/Willingness/Resolve ; Need ; Business Case ; Funding ; Sponsorship and Leadership ; Governance ; Accountability ; Workable Approach and Execution Model ; IT Capacity to Execute ; Enterprise Capacity to Execute ; Ability to Implement and Operate**.

Pour chaque facteur : importance/urgence, état de préparation, difficulté de remédiation, risque, action et conséquence sur les work packages E/F. Un score élevé de technologie ne neutralise pas l'absence d'exploitation opérationnelle.

## 10. Livrables ADM : ne pas mémoriser uniquement six titres (L1 7.3)

| Livrable | Utilité principale |
|---|---|
| Request for Architecture Work | Déclencher le travail |
| Statement of Architecture Work | Formaliser scope et engagement |
| Architecture Vision | Établir valeur et direction |
| Communications Plan | Coordonner l'information aux stakeholders |
| Architecture Definition Document | Documenter Baseline/Target et représentations de l'architecture |
| Architecture Requirements Specification | Spécifier les exigences de l'architecture |
| Architecture Roadmap | Visualiser transformations, work packages et étapes |
| Implementation and Migration Plan | Prioriser, séquencer et planifier la migration |
| Implementation Governance Model | Définir contrôle et responsabilités d'implémentation |
| Architecture Contract | Formaliser engagements entre rôles/organisations |
| Compliance Assessment | Apprécier le respect des exigences et des standards |
| Requirements Impact Assessment | Analyser l'effet d'une exigence nouvelle/modifiée |
| Change Request | Enregistrer une demande d'évolution |
| Capability Assessment | Évaluer la capacité à transformer |
| Architecture Principles | Cadre stable de décision |
| Business Principles, Goals and Drivers | Fondement des choix métier |

Cette table est une **aide de mémorisation** ; consulter la liste exacte de L1 7.3 et la section Architecture Content du TOGAF Standard en cas d'ambiguïté de nom ou de statut.

## 11. Contrôles de compréhension

1. Si une décision doit différencier ADD et Standards Information Base, lequel expose la cible et les vues ? **ADD** : SIB répertorie les standards.
2. Une cible requiert une capacité que les collaborateurs ne savent pas exploiter. Quelle technique en premier ? **Business Transformation Readiness** pour rendre visible et traiter l'écart organisationnel.
3. Des services échangent des messages JSON mais ne donnent pas le même sens au champ « statut ». De quel problème s'agit-il ? **Interopérabilité informationnelle/sémantique**, pas seulement connectivité.
4. Un modèle contient le portefeuille de capacités métier et une application qui supporte deux de ces capacités. Quelle est la représentation correcte ? **Capabilities indépendantes des applications**, liens de support explicites.

**Sources de contrôle :** [X2202](https://www.opengroup.org/library/x2202), sections 3.1, [The Open Group Certification Portfolio](https://www.opengroup.org/certifications/togaf-certification-portfolio). Ce texte est une synthèse pédagogique originale, non un texte officiel ni un cours accrédité.
