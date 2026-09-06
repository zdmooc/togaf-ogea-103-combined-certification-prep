# 03 — Core Concepts

## 1. Why this chapter matters

TOGAF utilise plusieurs concepts proches. Les connaître séparément ne suffit pas : il faut comprendre leurs **relations**.

Le meilleur moyen de les mémoriser est de suivre la chaîne suivante :

```text
Stakeholder
   ↓ has
Concern
   ↓ expressed / analyzed through
Viewpoint → View
   ↓ helps identify / clarify
Requirement
   ↓ constrained by / guided by
Principle
   ↓ contributes to
Architecture Description
   ↓ contains
Artifacts / Building Blocks
   ↓ supports
Baseline → Target → Gap → Transition → Roadmap
```

Ce chapitre introduit les concepts. Les chapitres suivants les approfondissent.

---

## 2. Stakeholder

Un **Stakeholder** est une personne, un groupe ou une organisation ayant un intérêt dans le système ou la transformation considérée.

Exemples MayaBank :

- Chief Information Officer ;
- responsable paiements ;
- RSSI ;
- équipes d’exploitation ;
- architectes ;
- équipes de développement ;
- conformité ;
- finance ;
- partenaires externes.

Un stakeholder n’est pas simplement « quelqu’un à informer ». Il peut influencer les décisions, porter des exigences, approuver des choix ou subir les conséquences de l’architecture.

### Exam trap

Ne confonds pas **Stakeholder** et **role in the architecture team**. Un architecte peut être stakeholder, mais tous les stakeholders ne sont pas architectes.

---

## 3. Concern

Un **Concern** est un intérêt, une préoccupation ou un enjeu important pour un stakeholder.

Exemples :

- disponibilité 24/7 ;
- conformité réglementaire ;
- réduction du coût ;
- délai de mise sur le marché ;
- sécurité ;
- maintenabilité ;
- résilience ;
- expérience utilisateur.

Le même système peut être observé sous plusieurs concerns différents.

### Example

Pour une plateforme OpenShift :

- le RSSI regarde les droits, secrets et segmentation ;
- l’exploitation regarde logs, métriques et reprise ;
- la finance regarde coût et capacité ;
- les développeurs regardent expérience de déploiement et autonomie.

Une architecture unique doit pouvoir répondre à ces perspectives différentes.

---

## 4. Viewpoint and View

Cette distinction est classique dans l’examen.

### Viewpoint

Un **Architecture Viewpoint** définit les conventions permettant de construire et utiliser une vue pour répondre à certains concerns.

Il répond à la question :

**Comment allons-nous regarder l’architecture pour répondre à ce type de préoccupation ?**

### View

Une **Architecture View** est la représentation concrète d’une architecture depuis la perspective d’un ensemble de concerns.

Il répond à la question :

**Que voit-on effectivement de cette architecture en utilisant ce viewpoint ?**

### Memory aid

**Viewpoint = règle / perspective de construction.**

**View = résultat concret.**

### Example

Viewpoint : représentation des dépendances applicatives destinée à analyser les impacts de changement.

View : le diagramme réel montrant Payment API, Fraud Service, Kafka et Core Banking pour MayaBank.

---

## 5. Requirement

Une **Requirement** exprime un besoin qui doit être satisfait par l’architecture ou sa réalisation.

Une exigence peut venir :

- d’un objectif métier ;
- d’un stakeholder ;
- d’une réglementation ;
- d’une contrainte technique ;
- d’une analyse de risque ;
- d’une décision d’architecture.

Exemple :

> Le service de paiement doit continuer à traiter les transactions lors de la perte d’un site.

Cette exigence pourra influencer Technology Architecture, Data Architecture, deployment, réseau et exploitation.

### Requirements are not static

Dans TOGAF, Requirements Management traverse le cycle. Les exigences peuvent être :

- identifiées ;
- analysées ;
- priorisées ;
- modifiées ;
- réutilisées ;
- validées.

Une exigence découverte en Phase D peut conduire à réexaminer une décision précédente.

---

## 6. Constraint

Une **Constraint** limite la liberté de conception.

Exemples :

- une réglementation impose une localisation des données ;
- un contrat impose une technologie pendant trois ans ;
- un système legacy ne peut pas être modifié avant une date donnée ;
- un budget limite le choix de scénario.

### Requirement vs Constraint

Une constraint peut être vue comme une condition limitante imposée au travail d’architecture.

Dans les questions, évite de réduire une requirement à « fonctionnalité demandée par le métier ». Les exigences peuvent être fonctionnelles, non fonctionnelles, réglementaires ou architecturales.

---

## 7. Architecture Principle

Un **Architecture Principle** est une règle générale qui guide les décisions d’architecture.

Un principe doit être suffisamment stable pour servir sur plusieurs projets et suffisamment clair pour influencer les choix.

Exemples pédagogiques :

- API before point-to-point integration ;
- data is protected according to classification ;
- reuse before build ;
- observability by design.

Attention : un exemple n’est pas automatiquement un principe TOGAF officiel. Chaque organisation définit ses propres principes selon son contexte.

### Principle vs Requirement

| Architecture Principle | Requirement |
|---|---|
| règle générale et durable | besoin à satisfaire dans un contexte donné |
| influence plusieurs décisions | peut être spécifique à une initiative |
| guide la formulation/évaluation | doit être traçable et gérée |

Example :

- Principle : « services are exposed through managed APIs ».
- Requirement : « Payment Status API must support 2,000 requests/s ».

---

## 8. Architecture Description

Une **Architecture Description** est l’ensemble structuré des représentations et informations permettant de décrire une architecture.

Elle peut inclure différents views, modèles, principes, exigences, artifacts et building blocks.

Ne pense pas « un fichier Word ». Une Architecture Description peut être distribuée entre plusieurs outils et livrables.

---

## 9. Deliverable, Artifact and Building Block — introduction

Ces notions seront approfondies dans `06-architecture-content/`, mais il faut les reconnaître dès maintenant.

### Deliverable

Un **Deliverable** est un produit de travail formel, généralement contractuellement ou formellement revu et approuvé.

### Artifact

Un **Artifact** est un produit architectural décrivant un aspect de l’architecture.

Les trois catégories classiques d’artifacts sont :

- **Catalog** ;
- **Matrix** ;
- **Diagram**.

### Building Block

Un **Building Block** représente un composant potentiellement réutilisable de capacité métier, applicative ou technologique.

### Relationship

Un Deliverable peut contenir plusieurs Artifacts ; les Artifacts peuvent représenter des Building Blocks.

```text
Deliverable
   └── contains → Artifacts
                    ├── Catalogs
                    ├── Matrices
                    └── Diagrams
                           ↓ describe
                      Building Blocks
```

### Exam trap

Un Building Block n’est pas un document.

---

## 10. ABB and SBB — introduction

### Architecture Building Block (ABB)

Un **ABB** décrit une capacité nécessaire de façon architecturale, en se concentrant sur **ce qui est requis**.

Example :

- centralized identity service ;
- event streaming capability ;
- API management capability.

### Solution Building Block (SBB)

Un **SBB** représente une solution plus concrète qui contribue à réaliser un ABB.

Example pédagogique :

- un cluster Kafka particulier ;
- un produit API Management sélectionné ;
- une implémentation IAM donnée.

### Exam memory

**ABB = what capability is required.**

**SBB = how it is realized in a solution.**

Ne transforme pas cette règle en opposition absolue « abstrait contre produit » ; la relation dépend du niveau d’architecture.

---

## 11. Baseline Architecture

La **Baseline Architecture** représente l’état de l’architecture avant la transformation considérée.

Elle doit être suffisamment détaillée pour permettre de comprendre les écarts, mais il est inutile de documenter tout l’existant sans rapport avec le scope.

Example MayaBank :

- monolithe de paiement ;
- échange de fichiers ;
- Oracle RAC ;
- exploitation manuelle ;
- intégration partenaire spécifique.

---

## 12. Target Architecture

La **Target Architecture** décrit l’état futur que l’entreprise cherche à atteindre.

Elle doit répondre aux objectifs, principles, requirements et constraints.

Example :

- payment orchestration services ;
- canonical ISO 20022 model ;
- API gateway ;
- event streaming ;
- OpenShift ;
- shared observability.

### Architecture Vision vs Target Architecture

Une **Architecture Vision** est volontairement high-level et sert à aligner les stakeholders sur l’ambition, la valeur et le scope.

La **Target Architecture** développée dans B/C/D est beaucoup plus détaillée.

---

## 13. Gap

Un **Gap** est une différence significative entre Baseline et Target qui doit être adressée.

Examples :

- capability missing in Baseline ;
- composant legacy à retirer ;
- nouvelle interface à construire ;
- compétence opérationnelle inexistante ;
- niveau de sécurité insuffisant.

Le **Gap Analysis** permet de convertir la comparaison Baseline/Target en éléments exploitables pour la transformation.

### Memory chain

**Baseline + Target → Gap.**

Puis les gaps alimentent les travaux de réalisation dans les phases suivantes.

---

## 14. Transition Architecture

Une **Transition Architecture** décrit un état architectural intermédiaire entre Baseline et Target lorsque la transformation ne peut pas être réalisée en un seul changement.

Example :

```text
Baseline
Legacy Payment Hub
      ↓
Transition 1
Legacy + API façade
      ↓
Transition 2
New Payment Services + legacy settlement
      ↓
Target
Modern payment platform
```

Une transition peut être motivée par :

- dépendances ;
- risque ;
- réglementation ;
- capacité de delivery ;
- contraintes budgétaires ;
- besoin de coexistence.

---

## 15. Capability

Une **Capability** représente une capacité qu’une organisation possède ou doit posséder pour atteindre un objectif.

Une capability est centrée sur **ce que l’entreprise est capable de faire**, pas sur l’application qui le fait actuellement.

Example :

Capability : **Real-Time Payment Processing**.

Cette capability peut être réalisée aujourd’hui par un monolithe et demain par plusieurs services.

### Capability vs Application

| Capability | Application |
|---|---|
| ability to do something | software system/component |
| relativement stable | peut être remplacée |
| utile pour strategy/planning | utile dans Application Architecture |

C’est une distinction importante pour éviter de construire une Business Architecture comme un simple inventaire applicatif.

---

## 16. Work Package

Un **Work Package** représente un ensemble d’actions conçu pour atteindre un objectif architectural.

Il apparaît particulièrement dans la logique de réalisation des Phases E et F.

Examples MayaBank :

- WP01 — Platform Foundation ;
- WP02 — API Foundation ;
- WP03 — Event Streaming ;
- WP04 — Payment Orchestration ;
- WP05 — Observability.

Ne confonds pas Work Package et Architecture Building Block. L’un organise du travail ; l’autre décrit une brique d’architecture.

---

## 17. Architecture Roadmap

L’**Architecture Roadmap** représente la trajectoire architecturale : changements, work packages, transitions et progression vers la cible.

Elle évolue au fil de l’ADM.

### Architecture Roadmap vs Implementation and Migration Plan

La roadmap exprime principalement la trajectoire architecturale et ses work packages.

L’**Implementation and Migration Plan**, développé davantage en Phase F, organise la réalisation de manière plus détaillée, en tenant compte des priorités, dépendances, coûts et contraintes du portefeuille.

---

## 18. Architecture Repository

L’**Architecture Repository** organise et stocke les informations utiles à la pratique d’architecture : modèles, standards, governance information, architectures, reference material et autres éléments réutilisables.

Il répond à une question pratique :

**où conservons-nous et retrouvons-nous les actifs d’architecture ?**

Il ne faut pas le confondre avec l’Enterprise Continuum.

---

## 19. Enterprise Continuum

L’**Enterprise Continuum** est un mécanisme de classification et de compréhension des assets d’architecture et de solution, depuis des éléments très génériques jusqu’à des éléments propres à une organisation.

Memory aid :

- **Repository = where assets are stored/managed.**
- **Continuum = how we classify/understand them.**

---

## 20. Common confusion map

| Confusion | Key distinction |
|---|---|
| Stakeholder vs Concern | who cares vs what they care about |
| Viewpoint vs View | conventions/perspective vs representation produced |
| Principle vs Requirement | durable rule vs need to satisfy |
| Requirement vs Constraint | need vs limiting condition |
| Baseline vs Target | current vs desired future |
| Target vs Transition | final desired state vs intermediate state |
| Deliverable vs Artifact | formal work product vs architectural representation/content |
| Artifact vs Building Block | representation vs architectural component/capability |
| ABB vs SBB | architectural need/capability vs solution realization |
| Capability vs Application | ability vs software system |
| Roadmap vs Migration Plan | architectural trajectory vs detailed implementation planning |
| Repository vs Continuum | storage/organization vs classification concept |

---

## 21. MayaBank mini-scenario

MayaBank wants instant payment capability.

- **Stakeholder:** Head of Payments.
- **Concern:** transaction availability and speed.
- **Requirement:** process an eligible payment within the agreed response time.
- **Constraint:** existing settlement engine remains until contract expiry.
- **Principle:** integration through managed APIs/events.
- **Baseline:** batch-oriented payment processing.
- **Target:** near-real-time payment services.
- **Gap:** no real-time orchestration capability.
- **ABB:** real-time orchestration capability.
- **SBB:** selected orchestration/service implementation.
- **Transition Architecture:** new initiation layer coexists with legacy settlement.
- **Work Package:** Payment Orchestration Foundation.
- **Roadmap:** introduce API foundation → orchestration → migrate flows → retire legacy.

Cette chaîne montre pourquoi apprendre les concepts séparément est insuffisant.

---

## 22. OGEA-103 exam traps

### Trap 1
Une réponse parle d’un diagramme et l’appelle Building Block.

→ probablement faux : le diagramme est un Artifact qui peut représenter des Building Blocks.

### Trap 2
Une réponse appelle la Target Architecture « Architecture Vision ».

→ vérifier le niveau de détail et la phase. La Vision est high-level ; la Target complète se développe dans B/C/D.

### Trap 3
Une réponse traite Enterprise Continuum comme un dossier de fichiers.

→ faux : le Repository stocke ; le Continuum aide à classifier/comprendre.

### Trap 4
Une application legacy est présentée comme une business capability.

→ attention : une capability décrit ce que l’entreprise peut faire, indépendamment de l’application qui la réalise.

---

## 23. Foundation questions

### Q1
Quelle notion décrit « ce qui préoccupe un stakeholder » ?

**Answer:** Concern.

### Q2
Quelle est la différence entre Viewpoint et View ?

**Answer:** le Viewpoint définit les conventions/perspective ; la View est la représentation réelle produite.

### Q3
Que produit une comparaison Baseline/Target ?

**Answer:** des gaps à analyser et adresser.

### Q4
Quelle notion est un état architectural intermédiaire ?

**Answer:** Transition Architecture.

### Q5
Quelle différence entre Architecture Repository et Enterprise Continuum ?

**Answer:** le Repository organise/stocke les assets ; l’Enterprise Continuum fournit une façon de les classifier et de les comprendre.

---

## 24. English for Architects

Useful sentences:

- A stakeholder has concerns that the architecture must address.
- A viewpoint defines how a view is constructed.
- We compare the baseline and target architectures to identify gaps.
- A transition architecture represents an intermediate state.
- A capability describes what the enterprise is able to do.

### Speak it

1. The main stakeholder concern is availability.
2. The main gap is the lack of real-time processing capability.
3. We need one transition architecture before reaching the target state.

---

## 25. Interview question

**Question:** What is the difference between a requirement and an architecture principle?

**Simple answer:**

A requirement is a specific need that the architecture must satisfy. An architecture principle is a more stable rule that guides architecture decisions across multiple initiatives.

---

## 26. Key points to remember

Memorise the relationships:

**Stakeholder → Concern → Viewpoint/View → Requirement → Architecture.**

**Baseline → Target → Gap → Transition → Roadmap.**

**Deliverable contains Artifacts; Artifacts describe Building Blocks.**

**ABB = architectural need; SBB = solution realization.**

**Repository stores; Continuum classifies.**
