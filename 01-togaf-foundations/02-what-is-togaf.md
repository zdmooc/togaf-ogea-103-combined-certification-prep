# 02 — What is TOGAF?

## 1. Definition

**TOGAF®** est un standard d’Enterprise Architecture développé et maintenu par **The Open Group Architecture Forum**. Il fournit un ensemble de concepts, une méthode de développement d’architecture, des techniques, un cadre de gouvernance et des mécanismes de gestion du contenu permettant d’organiser une pratique d’architecture d’entreprise.

TOGAF n’est pas une architecture prête à l’emploi. Ce n’est pas non plus un catalogue imposant une technologie, un cloud, un produit ou un langage de modélisation particulier.

La bonne lecture est :

**TOGAF fournit un cadre configurable pour conduire et gouverner le travail d’Enterprise Architecture.**

## 2. Why TOGAF exists

Une transformation d’entreprise implique souvent de nombreuses équipes, plusieurs domaines d’architecture, des contraintes contradictoires et des décisions prises sur plusieurs années.

Sans méthode commune, chaque architecte peut :

- employer son propre vocabulaire ;
- organiser les travaux différemment ;
- produire des livrables incompatibles ;
- oublier certaines parties prenantes ;
- confondre vision, cible, migration et gouvernance ;
- démarrer au mauvais niveau de détail.

TOGAF fournit une structure commune pour réduire ces incohérences.

## 3. The TOGAF Standard, 10th Edition

Le TOGAF Standard, 10th Edition repose sur une structure modulaire.

Il faut distinguer deux grands ensembles :

### TOGAF Fundamental Content

Le **Fundamental Content** contient les concepts durables et structurants qui constituent le socle du framework.

On y retrouve notamment les éléments nécessaires pour comprendre :

- l’Architecture Development Method ;
- les concepts fondamentaux ;
- l’application de l’ADM ;
- la gouvernance ;
- le contenu d’architecture.

### TOGAF Series Guides

Les **TOGAF Series Guides** fournissent des recommandations plus ciblées sur la manière d’appliquer ou configurer ce socle dans différents contextes.

L’idée importante est la suivante :

**stable universal concepts + context-specific guidance**.

Le standard ne suppose pas que toutes les organisations doivent appliquer TOGAF exactement de la même manière.

## 4. TOGAF is configurable

Le terme **configured Enterprise Architecture practice** est important.

Une organisation doit adapter son usage de TOGAF selon :

- sa taille ;
- sa maturité ;
- son modèle de gouvernance ;
- ses réglementations ;
- ses méthodes de delivery ;
- son organisation ;
- le type de transformation ;
- le niveau d’architecture visé.

Ce processus d’adaptation est appelé **tailoring**.

Tailoring ne veut pas dire « ignorer ce qui nous dérange ». Il signifie adapter consciemment la méthode tout en conservant une logique d’architecture cohérente.

## 5. The main TOGAF building blocks of knowledge

Pour l’examen et pour la pratique, tu dois construire une carte mentale de TOGAF autour de plusieurs blocs.

### 5.1 The ADM

L’**Architecture Development Method (ADM)** organise le développement et la gouvernance des architectures.

Il couvre :

- préparation de la capacité d’architecture ;
- vision ;
- Business Architecture ;
- Information Systems Architectures ;
- Technology Architecture ;
- opportunités et solutions ;
- migration ;
- gouvernance de l’implémentation ;
- changement ;
- Requirements Management.

### 5.2 ADM Techniques

TOGAF décrit ou référence des techniques permettant d’effectuer le travail, par exemple :

- Stakeholder Management ;
- Business Scenarios ;
- Gap Analysis ;
- Risk Management ;
- Capability-Based Planning ;
- Business Transformation Readiness ;
- techniques de Migration Planning.

### 5.3 Applying the ADM

L’ADM doit être appliqué dans un contexte réel. Il faut donc comprendre :

- iteration ;
- levels of architecture ;
- partitioning ;
- security ;
- tailoring ;
- interactions avec des modes de delivery modernes.

### 5.4 Architecture Governance

Une architecture n’a de valeur que si les décisions sont suivies, arbitrées et gouvernées.

TOGAF fournit des concepts pour :

- Architecture Board ;
- Architecture Contract ;
- compliance ;
- governance of implementation ;
- exceptions et changements.

### 5.5 Architecture Content

TOGAF distingue plusieurs types de contenu :

- Deliverables ;
- Artifacts ;
- Building Blocks ;
- Catalogs ;
- Matrices ;
- Diagrams ;
- Views et Viewpoints.

Cette distinction est fréquemment testée.

## 6. TOGAF is not ArchiMate

**TOGAF** est principalement un framework/méthode d’Enterprise Architecture.

**ArchiMate®** est un langage de modélisation d’architecture d’entreprise.

Ils sont complémentaires mais différents.

Exemple :

- TOGAF peut dire qu’il faut comprendre stakeholders, concerns, baseline, target et gaps ;
- ArchiMate peut fournir des concepts graphiques pour représenter une partie de cette architecture.

Il est donc incorrect de dire : « TOGAF utilise obligatoirement ArchiMate ».

## 7. TOGAF is not project management

TOGAF ne remplace ni Scrum, ni SAFe, ni PRINCE2, ni PMBOK, ni une méthode interne de gestion de projet.

L’architecture et le delivery doivent coopérer.

TOGAF s’intéresse à des questions telles que :

- quelles architectures devons-nous créer ?
- quelles exigences devons-nous satisfaire ?
- quels écarts existent entre Baseline et Target ?
- quelles règles doivent gouverner l’implémentation ?

La gestion de projet traite plutôt :

- planning ;
- budget ;
- ressources ;
- coordination du delivery ;
- risques projet.

Les deux domaines s’influencent mais ne doivent pas être confondus.

## 8. TOGAF is not a rigid waterfall

Une erreur fréquente consiste à regarder l’ADM et à imaginer une séquence rigide : A puis B puis C puis D une seule fois.

En réalité, TOGAF prévoit explicitement :

- l’iteration ;
- la réutilisation ;
- l’adaptation ;
- différents niveaux de détail ;
- des boucles lorsque de nouvelles informations apparaissent.

L’ordre des phases reste important pour comprendre leur finalité, mais l’application réelle n’est pas une mécanique aveugle.

## 9. Why the ADM matters so much

L’ADM est souvent appelé le cœur opératoire de TOGAF parce qu’il relie les grandes questions d’architecture dans une progression logique.

```text
Prepare
  ↓
Vision
  ↓
Business / Data / Application / Technology architectures
  ↓
Gaps and realization options
  ↓
Work Packages and Transition Architectures
  ↓
Migration priorities
  ↓
Implementation Governance
  ↓
Architecture Change Management
```

**Requirements Management** interagit avec le travail tout au long du cycle.

## 10. MayaBank example

MayaBank souhaite moderniser son système de paiements.

TOGAF ne fournit pas la « bonne architecture MayaBank ».

TOGAF fournit plutôt un cadre permettant à MayaBank de :

1. préparer sa capacité d’architecture ;
2. cadrer la transformation ;
3. identifier stakeholders et concerns ;
4. décrire Baseline et Target ;
5. analyser les gaps ;
6. construire des work packages ;
7. organiser la migration ;
8. gouverner l’implémentation ;
9. réagir aux changements futurs.

C’est une différence essentielle : **TOGAF structure le raisonnement et le travail ; il ne choisit pas automatiquement la solution technique.**

## 11. Foundation vs Practitioner

### Foundation

Tu dois surtout pouvoir :

- reconnaître les concepts ;
- expliquer leur rôle ;
- distinguer des notions proches ;
- comprendre la logique de l’ADM.

### Practitioner

Tu dois pouvoir :

- identifier le contexte d’un scénario ;
- reconnaître la phase dominante ;
- choisir l’action la plus conforme à la logique TOGAF ;
- éliminer des réponses techniquement possibles mais mal séquencées.

## 12. Common mistakes

1. Appeler la certification « TOGAF 10 certification » comme si le numéro d’édition faisait partie du nom officiel de la certification actuelle.
2. Penser que TOGAF impose une technologie.
3. Confondre TOGAF et ArchiMate.
4. Utiliser l’ADM comme une checklist rigide.
5. Réduire TOGAF à l’ADM et ignorer gouvernance, contenu et techniques.
6. Croire qu’un bon architecte applique TOGAF sans tailoring.
7. Apprendre seulement les noms des phases sans comprendre les relations.

## 13. OGEA-103 exam traps

### Trap 1 — Framework vs solution

TOGAF fournit un **framework**, pas une solution technique prête à déployer.

### Trap 2 — Method vs modeling language

TOGAF n’est pas un langage de modélisation.

### Trap 3 — ADM phase recognition

Une question peut ne jamais écrire « Phase E ». Tu dois reconnaître la phase à partir du problème décrit.

### Trap 4 — tailoring

Adaptable ne signifie pas arbitraire.

## 14. Foundation questions

### Q1
TOGAF impose-t-il une architecture technologique standard ?

**Réponse :** non. Il fournit un cadre pour développer et gouverner une architecture adaptée au contexte.

### Q2
Quelle est la différence principale entre TOGAF et ArchiMate ?

**Réponse :** TOGAF est un framework/méthode d’Enterprise Architecture ; ArchiMate est un langage de modélisation.

### Q3
Pourquoi le TOGAF Standard, 10th Edition est-il décrit comme modulaire ?

**Réponse :** parce qu’il distingue un socle de concepts fondamentaux et des Series Guides fournissant des recommandations plus ciblées selon les contextes.

## 15. English for Architects

Useful sentences:

- TOGAF provides a configurable framework for Enterprise Architecture.
- The ADM structures the architecture development lifecycle.
- TOGAF does not prescribe a specific technology stack.

### Speak it

Repeat aloud:

1. TOGAF is a framework, not a product architecture.
2. The ADM helps us structure architecture work.
3. We tailor the method to the enterprise context.

## 16. Interview question

**Question:** Can you explain what TOGAF is?

**Simple answer:**

TOGAF is an Enterprise Architecture framework from The Open Group. It provides the ADM, governance concepts, architecture content concepts and supporting techniques. We configure and tailor it according to the enterprise context.

## 17. Key points to remember

TOGAF = **Framework + ADM + Techniques + Applying ADM + Governance + Architecture Content**.

Et surtout :

**TOGAF ne fournit pas la solution. TOGAF fournit la structure pour comprendre, décider, transformer et gouverner.**
