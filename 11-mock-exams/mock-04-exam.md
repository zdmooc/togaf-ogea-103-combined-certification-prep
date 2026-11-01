# Mock Exam 04 — OGEA-103 Combined

**Part 1 : 60 minutes, closed book. Part 2 : 90 minutes, open book.**

# Part 1 — Foundation

## Concepts

**Q1.** L'Enterprise Architecture sert principalement à :
A. Administrer les serveurs  B. Relier stratégie, capacités, décisions et évolution de l'entreprise  C. Remplacer le delivery  D. Produire des normes comptables

**Q2.** Un Concern est :
A. Une solution  B. Une phase  C. Une préoccupation importante d'un stakeholder  D. Un SBB

**Q3.** Une entreprise veut expliquer pourquoi une architecture d'entreprise n'est pas qu'une description du SI. Quel choix exprime le mieux sa fonction ?
A. Elle guide des changements cohérents et relie les décisions techniques à la stratégie et aux capacités métier.  B. Elle définit une seule Technology Architecture obligatoire pour toutes les équipes avant le recueil de concerns.  C. Elle établit principalement les Architecture Contracts des fournisseurs et remplace les décisions du portefeuille.  D. Elle classe toutes les applications actuelles comme des Solution Building Blocks approuvés.

**Q4.** Un Architecture Principle est :
A. Un ticket projet  B. Une requirement détaillée  C. Une préférence fournisseur  D. Une règle directrice durable pour les décisions

**Q5.** La Baseline Architecture décrit :
A. La cible future  B. L'état actuel pertinent  C. Le Migration Plan  D. Les stakeholders

**Q6.** Le Repository possède des décisions de conformité, des requirements et des patterns réutilisables. Où chercher les exigences d'architecture gouvernées et leurs relations de traçabilité ?
A. Dans le Standards Information Base, car toutes les exigences approuvées deviennent automatiquement des normes.  B. Dans le Solutions Landscape, qui remplace les exigences par les systèmes livrés.  C. Dans l'Architecture Requirements Repository, plutôt que dans le seul Governance Log ou la Reference Library.  D. Dans l'Architecture Metamodel, qui est un catalogue des instances de requirements.

**Q7.** Le Continuum aide principalement à :
A. Positionner et classifier les assets du générique vers le spécifique  B. Stocker les logs  C. Gérer le budget  D. Exécuter des applications

**Q8.** Le comité doit approuver un Architecture Definition Document contenant plusieurs matrices et diagrammes. Quelle définition de Deliverable convient ?
A. Un Deliverable est une application cible dont le code source a été approuvé.  B. Un Deliverable est toujours un diagramme individuel sans exigences associées.  C. Un Deliverable correspond au seul modèle de métadonnées utilisé par une entreprise.  D. Un Deliverable est un produit de travail formel pouvant comprendre plusieurs artifacts.

## Introduction to the ADM

**Q9.** Où établit-on principalement principes, gouvernance et Architecture Capability ?
A. Preliminary  B. Phase C  C. Phase F  D. Phase H

**Q10.** Où clarifie-t-on principalement scope, stakeholders, business value et Architecture Vision ?
A. Phase E  B. Preliminary  C. Phase A  D. Phase G

**Q11.** En Phase B, l'équipe examine une capacité « suivre les réclamations » indépendamment du CRM historique. Pourquoi ce découplage est-il important pour la Target ?
A. Il permet de supprimer la Data Architecture car toutes les informations appartiennent au domaine Business.  B. Il transforme automatiquement chaque capability en un work package financé.  C. Il conduit à sélectionner le SBB préféré dès la Phase B, puis à adapter les besoins métier.  D. Il permet de définir les capacités et processus métier avant de déterminer quelles applications et solutions les réalisent.

**Q12.** Où traite-t-on principalement structure, ownership et lifecycle des données ?
A. Phase F  B. Phase C Data  C. Phase G  D. Phase A

**Q13.** Où décrit-on principalement les services et interactions applicatives cibles ?
A. Phase C Application  B. Phase B  C. Phase H  D. Phase F

**Q14.** Où développe-t-on principalement la Target Technology Architecture ?
A. Phase E  B. Phase C  C. Phase D  D. Phase F

**Q15.** Où identifie-t-on principalement les Solution Building Blocks candidats, work packages et Transition Architectures ?
A. Phase B  B. Phase F  C. Phase G  D. Phase E

**Q16.** Où consolide-t-on priorités, dépendances et séquencement de migration ?
A. Phase E  B. Phase F  C. Phase H  D. Preliminary

**Q17.** Où contrôle-t-on principalement l'implémentation par rapport à l'architecture approuvée ?
A. Phase G  B. Phase E  C. Phase A  D. Phase B

**Q18.** Après la livraison d'une architecture, une obligation modifie les flux de données et les contrôles. Quelle réponse ADM évite une ré-architecture systématique ?
A. Traiter le sujet exclusivement en Phase G car tout changement réglementaire est une exception de réalisation.  B. Relancer directement toutes les phases depuis Preliminary indépendamment des effets constatés.  C. Analyser en Phase H l'impact et classifier le changement avant de déterminer l'ampleur du nouveau travail ADM.  D. Modifier simplement les requirements sans réexaminer les architectures et transitions impactées.

**Q19.** Requirements Management doit :
A. Commencer seulement en F  B. Finir après A  C. Être limité aux requirements techniques  D. Soutenir et tracer les requirements pendant tout l'ADM

**Q20.** Les domaines Data et Application doivent être ajustés après une nouvelle exigence. Quelle affirmation sur l'itération ADM est correcte ?
A. L'ADM impose la clôture définitive de C Data avant tout travail C Application.  B. L'ADM permet tailoring, itérations et travail concurrent sous gouvernance appropriée.  C. La Phase H doit être déclenchée dès qu'une étude produit une nouvelle requirement.  D. Chaque phase ADM possède une durée prescrite et identique quel que soit le contexte.

**Q21.** Quel concept exprime ce qui manque entre Baseline et Target ?
A. Gap  B. Viewpoint  C. Stakeholder  D. Contract

**Q22.** Quel élément décrit un état intermédiaire de l'architecture ?
A. Architecture Roadmap  B. Work Package  C. Transition Architecture  D. Requirement

## ADM Techniques

**Q23.** Deux systèmes échangent des messages corrects techniquement mais codent différemment le statut d'un virement. Quel domaine d'interopérabilité est le plus directement concerné ?
A. Technical interoperability uniquement, puisque la connexion IP est établie.  B. Information interoperability, car la signification et les modèles des données échangées divergent.  C. Operational/Business interoperability uniquement, car aucune sémantique de donnée n'est impliquée.  D. Architecture Risk Management exclusivement, car une incompatibilité n'est pas un problème d'interopérabilité.

**Q24.** Pour transformer une opportunité métier en scénario et requirements :
A. Partitioning  B. Compliance Review  C. Business Scenarios  D. Interoperability

**Q25.** Pour évaluer si l'organisation peut réellement absorber une transformation :
A. Gap Analysis  B. Business Scenario  C. Capability Map  D. Business Transformation Readiness

**Q26.** Pour analyser probabilité, impact, mitigation et residual risk :
A. Risk Management  B. Viewpoint Design  C. Organization Mapping  D. Catalog Design

**Q27.** Pour organiser la transformation autour de capabilities métier :
A. Compliance Review  B. Stakeholder Mapping  C. Capability-Based Planning  D. Architecture Contract

**Q28.** Pour choisir l'ordre de réalisation en tenant compte des dépendances et valeur :
A. Business Scenarios  B. Migration Planning Techniques  C. Interoperability  D. View Selection

## Applying the ADM

**Q29.** Choisir quels deliverables produire réellement selon le contexte correspond à :
A. Compliance  B. Partitioning  C. Gap Analysis  D. Tailoring

**Q30.** Une banque ne veut modéliser qu'un segment du SI sur deux ans, avec une profondeur accrue pour les données sensibles. Quels critères définissent correctement le scoping ?
A. Breadth, depth, architecture domains et time period, avec justification par les décisions attendues.  B. La seule Technology Architecture, puis des détails supplémentaires lorsque la solution est choisie.  C. L'ensemble des phases ADM considéré comme scope identique pour chaque projet.  D. L'Architecture Contract final, qui détermine rétroactivement les secteurs de l'entreprise inclus.

**Q31.** Délimiter des domaines d'architecture et leurs interfaces dans une grande organisation correspond à :
A. Business Scenario  B. Risk Analysis  C. Partitioning  D. Phase G

**Q32.** Quelle affirmation Agile/TOGAF est la meilleure ?
A. Ils sont incompatibles  B. On peut itérer et tailorer l'ADM tout en conservant cohérence et gouvernance  C. Agile supprime les principles  D. TOGAF impose un cycle unique annuel

## Architecture Governance

**Q33.** Quelle entité est typiquement responsable des arbitrages d'architecture importants ?
A. Product Backlog  B. Project Office  C. Repository  D. Architecture Board

**Q34.** Un programme doit fixer le processus de revue de conformité, le traitement des écarts et les rôles de contrôle pendant les releases. Quel livrable est le plus adapté ?
A. Architecture Definition Document, qui remplace à lui seul tous les processus de gouvernance.  B. Implementation Governance Model, qui formalise l'organisation des contrôles pendant la mise en œuvre.  C. Architecture Vision, qui décrit chaque critère détaillé de conformité et les sanctions en cas d'exception.  D. Architecture Roadmap, qui tient lieu de circuit d'approbation des écarts.

**Q35.** Quel mécanisme vérifie l'alignement d'une mise en œuvre avec l'architecture approuvée ?
A. Business Scenario  B. Requirements Management  C. Architecture Compliance Review  D. Continuum

## Architecture Content

**Q36.** Un Catalog, une Matrix ou un Diagram sont des exemples de :
A. Artifacts  B. Phases  C. Boards  D. Requirements

**Q37.** Un Building Block :
A. Est toujours un produit  B. Est une réunion  C. Est une Viewpoint  D. Représente un élément architectural ou de solution réutilisable

**Q38.** Le comité demande le périmètre des applications supportant une capability et leurs relations avec des données sensibles. Quel ensemble distingue correctement les formes d'artifacts ?
A. Catalog pour décisions contractuelles, Matrix pour documents approuvés, Diagram pour solution livrée.  B. Catalog pour inventaire, Matrix pour relations, Diagram pour représentation graphique.  C. Catalog et Matrix sont des SBB ; seul Diagram constitue un artifact du Content Framework.  D. Matrix correspond uniquement au planning de migration et Diagram à l'Architecture Contract.

**Q39.** Deux stakeholders exigent des représentations différentes d'une même cible. Quelle affirmation sur View et Viewpoint est correcte ?
A. Une Viewpoint est une instance graphique construite à partir d'une View.  B. Une View est un Building Block exécuté par un service de plateforme.  C. Une View répond à des concerns en suivant la convention spécifiée par une Viewpoint.  D. Une View est obligatoirement le même modèle pour tous les stakeholders.

**Q40.** Le Content Metamodel sert principalement à :
A. Définir les types d'entités architecturales et leurs relations  B. Planifier les sprints  C. Gérer les budgets  D. Remplacer le Repository

# Part 2 — huit scénarios de décision en architecture d'entreprise

## P1 — Context

Un groupe international veut appliquer une gouvernance identique à toutes ses filiales malgré des réglementations et maturités très différentes.

Les filiales exercent des métiers proches mais sont soumises à des règles de résidence des données et de résilience différentes. Le groupe veut des standards IAM communs et un registre d'exceptions auditable ; une filiale fonctionne en autonomie produit et une autre utilise un comité technique mensuel. Le sponsor demande une Architecture Capability commune sans ralentir la transformation. Les dirigeants locaux craignent qu'un processus trop uniforme crée des décisions techniquement conformes mais inexploitables. La priorité est d'établir la répartition des responsabilités et une adaptation documentée des règles.

**Quelle décision recommander ?**

A. Définir une charte de gouvernance commune et un registre des exceptions, puis préciser les variations locales après une revue des obligations réglementaires.

B. Introduire une liste de standards techniques communes et vérifier leur usage lors des prochains projets, sans clarifier les responsabilités de décision.

C. Tailorer et fédérer la gouvernance tout en maintenant principes et contrôles communs nécessaires, avec un noyau de principes obligatoires et une délégation de décisions selon les risques.

D. Autoriser chaque filiale à choisir ses pratiques puis préparer une étude de cohérence groupe une fois la migration terminée.

## P2 — Stakeholder Management

Finance estime la transformation trop coûteuse, alors que le sponsor métier la considère urgente. Aucun modèle de valeur ni vue de coûts n'a été partagé.

La banque prépare l'automatisation d'un parcours crédit qui coûte actuellement plusieurs milliers d'heures de traitement. Finance demande une démonstration chiffrée de la valeur et des coûts récurrents ; le métier attend un gain de délai de réponse mesurable, tandis que Risk veut préserver les contrôles de conformité. Un modèle technique de plateforme existe, mais aucune vue n'explique quelles capacités métier sont modifiées et quelles décisions sont demandées au comité. Le sponsor exige un arbitrage de portefeuille dans trois semaines.

**Quelle décision recommander ?**

A. Produire les vues adaptées aux concerns, expliciter valeur/coût/risque et organiser l'arbitrage, incluant un modèle de valeur, les alternatives et les conséquences opérationnelles pour chaque stakeholder.

B. Présenter une Architecture Roadmap technique pour donner une visibilité sur les phases de déploiement sans quantifier tous les bénéfices.

C. Produire une première comparaison des coûts et bénéfices par option, puis compléter les views de conformité et d'exploitation avant le comité suivant.

D. Choisir le fournisseur présentant le meilleur ROI déclaré et laisser les métiers vérifier après contractualisation que leurs concerns sont couverts.

## P3 — Phase A

Un programme possède des objectifs métiers mais son périmètre traverse plusieurs domaines dont les responsabilités sont ambiguës.

Deux directions demandent une architecture de données partagées ; les données clients sont gouvernées centralement mais les responsabilités applicatives restent locales. Le sponsor souhaite une Architecture Vision commune, tandis que l'Architecture Board souligne que le périmètre change selon les pays. Le travail détaillé ne peut démarrer sans un mandat clair sur les interfaces et le degré de centralisation. Une Architecture Capability existante fournit des principes et un référentiel déjà validés. Le comité doit décider ce que le nouveau Statement of Architecture Work autorisera.

**Quelle décision recommander ?**

A. Clarifier scope, stakeholders, responsabilités et Vision avant l'architecture détaillée, en documentant scope, domaines, profondeur de travail, horizon et responsabilités de validation.

B. Établir une liste de work packages par direction avant d'avoir distingué les responsabilités et les limites de l'architecture.

C. Obtenir l'accord des DSI locales sur les applications concernées, puis élaborer une Vision commune sans encore définir les outcomes.

D. Définir la largeur du périmètre et les acteurs principaux, puis préciser les autres dimensions du scope à la prochaine revue.

## P4 — B/C/D

La cible métier est claire. Les données nécessaires sont connues, mais les applications et plateformes capables de les fournir ne le sont pas.

La direction Business a validé le parcours cible de gestion des réclamations, qui nécessite des informations sur le client et ses contrats. Le Data Owner possède les modèles nécessaires, mais les applications actuelles sont hétérogènes et certaines plateformes ne garantissent pas la résilience requise. Une application du groupe pourrait être réutilisée, mais sa capacité multi-entités reste incertaine. Le sponsor doit choisir entre une cible mutualisée et des services locaux. Les équipes doivent comparer les options applicatives et techniques à partir des exigences B/C déjà établies.

**Quelle décision recommander ?**

A. Identifier les services applicatifs clés et les flux de données nécessaires, puis vérifier la cible technologique et les alternatives dans une seconde revue.

B. Développer Application Architecture puis Technology Architecture en maintenant la traçabilité aux besoins métier/data, en dérivant les contrats de services, building blocks et contraintes de plateforme de la cible métier et data.

C. Examiner en premier la plateforme approuvée du groupe et construire un prototype, sans comparer encore les impacts sur les capacités métier.

D. Lancer la migration de l'application existante vers le cloud puis adapter les services métier lorsque la plateforme sera stabilisée.

## P5 — E/F/G

Deux work packages sont interdépendants. Le premier apporte plus de valeur mais augmente fortement le risque de migration si réalisé seul.

Le work package de vérification d'identité promet une forte baisse de fraude ; le package de fédération IAM est pourtant son prérequis. Le sponsor privilégie le premier pour des raisons de visibilité, tandis que le CISO refuse un contrôle d'identité non gouverné. Finance propose de lisser le budget sur trois trimestres, et Operations craint le coût de coexistence des deux systèmes. Le comité doit revoir l'ordre des lots avec des preuves de valeur et de dépendance. L'implémentation n'a pas commencé.

**Quelle décision recommander ?**

A. Programmer un lot IAM limité et démarrer en parallèle une validation fonctionnelle du contrôle, puis arbitrer les risques et coûts de la trajectoire complète.

B. Analyser valeur, risque, dépendances et Transition Architectures en Phase F avant de séquencer, en modélisant la dépendance critique, les options de transition et les risques résiduels dans le plan.

C. Favoriser l'initiative de plus forte valeur mais lui associer une condition formelle de disponibilité IAM avant le go-live.

D. Accepter la priorité du sponsor et transférer les risques d'intégration au prestataire de delivery sans modifier la roadmap.

## P6 — Phase H

Les utilisateurs demandent une amélioration locale qui ne change ni architecture cible ni principles.

La fonctionnalité demandée consiste à ajouter un filtre local dans une application dont les interfaces et les requirements restent inchangés. Le Product Owner veut une décision rapide, mais une équipe craint une violation des standards et demande une étude de cible globale. Un processus de gestion des changements techniques existe, avec un contrôle de non-régression. L'architecte doit vérifier que la modification ne crée pas de nouveau risque d'architecture et choisir le niveau de gouvernance proportionné à l'effet réel.

**Quelle décision recommander ?**

A. Vérifier les requirements et la vue impactée, puis autoriser un changement local en conservant une trace d'analyse.

B. Évaluer l'impact et appliquer un changement proportionné si l'architecture reste valide, avec évaluation d'impact et preuve de conformité au niveau approprié.

C. Planifier une revue des principes de l'application avant de modifier la fonctionnalité, sans analyser immédiatement son impact concret.

D. Relancer un cycle ADM complet et suspendre la demande jusqu'à définition d'une nouvelle Architecture Vision.

## P7 — Requirements Management

Une requirement critique n'a plus de propriétaire et plusieurs versions circulent.

Une requirement de disponibilité a été validée pour un moteur de paiement, mais le Business Owner a changé et les versions circulent entre trois équipes. Le CISO interprète le seuil de disponibilité comme une obligation permanente, Operations exclut les maintenances planifiées et Finance redoute le coût de la redondance. Le comité doit comparer deux architectures alternatives mais personne n'est autorisé à signer l'interprétation actuelle. La traçabilité doit permettre une décision auditable.

**Quelle décision recommander ?**

A. Organiser la validation du niveau de service avec un Business Owner désigné, puis réconcilier les modèles d'architecture après l'accord.

B. Clarifier ownership, version de référence, traceability et impacts, avec identification du propriétaire, historique des versions, clarification du seuil et propagation vers les modèles.

C. Demander aux équipes de delivery de sélectionner la solution la plus résiliente et d'obtenir ensuite la signature métier.

D. Prendre la version la plus récente du document projet et la traiter comme référence provisoire sans vérifier son approbation.

## P8 — Supporting ADM Work

La cible suppose une adoption organisationnelle importante, mais les managers locaux résistent au nouveau modèle opérationnel.

Une nouvelle plateforme exige un changement des rôles d'exploitation dans trois filiales. La technologie est jugée faisable et les métiers ont approuvé la Vision, mais les managers locaux refusent de financer la montée en compétences. Operations signale une absence de procédure d'escalade et plusieurs contrats fournisseur ne prévoient pas de support de nuit. Le sponsor demande une roadmap finançable plutôt qu'une liste de risques génériques. Il faut comprendre ce qui rendra la Target exploitable.

**Quelle décision recommander ?**

A. Réaliser d'abord une évaluation des compétences et responsabilités locales, puis inscrire les actions de préparation dans les prochaines waves.

B. Utiliser Transformation Readiness et Stakeholder Management pour traiter les barrières et actions d'adoption, avec facteurs de readiness, plan d'adoption, priorisation des prérequis et budget associé.

C. Rédiger des procédures d'exploitation standard pour les équipes actuelles, sans résoudre leur capacité de support 24/7.

D. Conserver le plan de migration initial et ajouter une clause de formation générale au contrat de livraison.
---

Fin de l'examen blanc.
