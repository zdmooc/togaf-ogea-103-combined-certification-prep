# 04 — The Four Architecture Domains

## 1. Overview

TOGAF structure classiquement l’architecture d’entreprise autour de quatre grands domaines :

1. **Business Architecture**
2. **Data Architecture**
3. **Application Architecture**
4. **Technology Architecture**

Ces domaines ne sont pas quatre projets indépendants. Ils décrivent quatre perspectives complémentaires d’une même entreprise et doivent rester cohérents entre eux.

Une transformation sérieuse suit souvent cette logique :

```text
Business needs
   ↓
Business Architecture
   ↓
Data + Application Architecture
   ↓
Technology Architecture
```

La flèche ne signifie pas qu’un domaine « commande » mécaniquement le suivant. Elle rappelle surtout qu’une décision technologique doit pouvoir être reliée à un besoin métier, à des données et à des applications.

---

## 2. Business Architecture

La **Business Architecture** décrit comment l’entreprise fonctionne et ce qu’elle doit être capable de faire.

Elle peut traiter notamment :

- business strategy ;
- capabilities ;
- value streams ;
- organization ;
- business processes ;
- business services ;
- actors and roles ;
- information needed by the business ;
- business rules and policies.

### Question centrale

**Quelles capacités et quel fonctionnement métier sont nécessaires pour atteindre les objectifs ?**

### MayaBank example

Objectif : accélérer l’introduction de nouveaux moyens de paiement.

Business Architecture peut faire apparaître :

- Payment Initiation capability ;
- Payment Validation capability ;
- Fraud Screening capability ;
- Clearing & Settlement capability ;
- Customer Notification capability.

À ce stade, il serait prématuré de décider « microservice Java X » ou « topic Kafka Y ». On décrit d’abord ce que l’entreprise doit pouvoir faire.

### Common mistake

Construire une Business Architecture comme une liste d’applications.

Une application peut réaliser une capability, mais une capability n’est pas une application.

---

## 3. Data Architecture

La **Data Architecture** décrit la structure logique et physique des actifs de données importants pour l’entreprise ainsi que les ressources de gestion de ces données.

Elle s’intéresse notamment à :

- data entities ;
- ownership ;
- data lifecycle ;
- quality ;
- lineage ;
- retention ;
- classification ;
- sharing ;
- canonical information models ;
- storage and access concerns at an architectural level.

### Question centrale

**Quelles données l’entreprise utilise-t-elle, qui en est responsable et comment doivent-elles circuler et être gérées ?**

### MayaBank example

Pour les paiements :

- Payment Instruction ;
- Account ;
- Party ;
- Transaction Status ;
- Fraud Decision ;
- Clearing Status.

La Data Architecture peut décider qu’un modèle canonique ISO 20022 doit devenir la référence d’échange pour certains flux.

### Data Architecture vs database design

Data Architecture n’est pas simplement la conception des tables Oracle.

Le schéma physique d’une base est un niveau de design plus détaillé. L’architecture traite d’abord les données à l’échelle pertinente pour la transformation.

---

## 4. Application Architecture

L’**Application Architecture** décrit les applications, leurs responsabilités, leurs interactions et leur relation avec les processus métier.

Elle s’intéresse notamment à :

- application components ;
- application services ;
- interfaces ;
- interactions ;
- application ownership ;
- functional distribution ;
- application portfolio implications.

### Question centrale

**Quelles applications ou services applicatifs supportent les capacités métier et comment interagissent-ils ?**

### MayaBank example

Target Application Architecture :

- Payment API ;
- Payment Orchestrator ;
- Fraud Service ;
- Notification Service ;
- Settlement Adapter ;
- Customer Channel.

Interactions :

```text
Customer Channel
      ↓ API
Payment API
      ↓
Payment Orchestrator
   ↙       ↘
Fraud     Settlement Adapter
   ↓
Events → Notification Service
```

Le diagramme ne décrit pas encore les workers OpenShift, les VLANs ou la configuration Kafka. Ceux-ci relèvent davantage de Technology Architecture ou du design.

---

## 5. Technology Architecture

La **Technology Architecture** décrit les services et composants technologiques nécessaires pour supporter les applications et les données.

Elle peut traiter :

- compute ;
- platforms ;
- network ;
- middleware ;
- runtime ;
- storage ;
- identity technology ;
- observability platform ;
- resilience ;
- infrastructure standards ;
- deployment topology.

### Question centrale

**Quelles capacités et services technologiques doivent supporter les architectures Data et Application ?**

### MayaBank example

Technology capabilities nécessaires :

- container orchestration ;
- event streaming ;
- relational persistence ;
- secrets management ;
- centralized identity ;
- monitoring and tracing ;
- multi-site resilience.

Puis des choix de solution peuvent être faits dans le cadre approprié : OpenShift, Kafka, Oracle, etc.

### Important principle

**Technology capability before product choice.**

Dire « nous avons besoin d’une event streaming capability » est une décision architecturale plus stable que « nous avons besoin du produit X ».

---

## 6. Why the domains must be linked

Considérons une nouvelle exigence métier :

> Les clients doivent recevoir le statut d’un paiement presque en temps réel.

Cette seule exigence traverse les quatre domaines.

### Business

Créer ou améliorer une **Payment Status Notification capability**.

### Data

Définir le statut du paiement, son propriétaire, son cycle de vie et son format.

### Application

Définir quels services produisent et consomment les changements de statut.

### Technology

Fournir les mécanismes d’événement, de disponibilité, de sécurité et d’observabilité nécessaires.

C’est exactement le type de cohérence recherché par l’Enterprise Architecture.

---

## 7. Phase mapping in the ADM

Les domaines sont développés principalement dans les phases suivantes :

| ADM Phase | Main domain |
|---|---|
| Phase B | Business Architecture |
| Phase C | Data Architecture + Application Architecture |
| Phase D | Technology Architecture |

Pourquoi Data et Application sont-elles toutes les deux en Phase C ? Parce qu’elles constituent les **Information Systems Architectures**.

### Exam trap

Phase C n’est pas seulement « Application Architecture ».

Elle contient deux parties distinctes : **Data Architecture** et **Application Architecture**.

---

## 8. Baseline and Target in every domain

Pour chaque domaine, l’architecte peut décrire :

- **Baseline Architecture** ;
- **Target Architecture** ;
- **Gaps**.

Example :

| Domain | Baseline | Target | Gap |
|---|---|---|---|
| Business | batch payment operations | real-time payment operation | no real-time operational capability |
| Data | proprietary payment format | canonical ISO 20022 model | transformation/ownership gap |
| Application | monolith | decoupled payment services | missing orchestration/services |
| Technology | VM + point-to-point middleware | container/event platform | platform capability gap |

Ces gaps alimentent Phase E.

---

## 9. Architecture domains vs organization teams

Une erreur courante est de croire que chaque domaine correspond obligatoirement à une équipe séparée.

Ce n’est pas nécessaire.

Une petite organisation peut avoir un seul architecte couvrant plusieurs domaines. Une grande organisation peut avoir plusieurs équipes spécialisées.

TOGAF structure le **contenu de l’architecture**, pas obligatoirement l’organigramme.

---

## 10. Domain boundaries are useful, not absolute walls

Certaines décisions traversent naturellement plusieurs domaines.

Exemple : security.

- Business : policy, segregation of duties.
- Data : classification, confidentiality.
- Application : authorization and API security.
- Technology : IAM, network security, secrets, certificates.

La sécurité ne doit donc pas être « ajoutée en Phase D » comme une technologie. Elle est transverse.

Même logique pour :

- performance ;
- resilience ;
- regulatory requirements ;
- sustainability ;
- cost.

---

## 11. MayaBank end-to-end example

### Driver

Réduction du délai de lancement d’un nouveau schéma de paiement.

### Business Architecture

Créer des capabilities indépendantes pour initiation, validation, fraud screening et settlement.

### Data Architecture

Standardiser les principales entités de paiement et établir le modèle de données canonique.

### Application Architecture

Séparer les responsabilités dans des services et définir des APIs/events stables.

### Technology Architecture

Fournir container platform, event streaming, database services, IAM, observability et multi-site resilience.

La Technology Architecture est donc la conséquence d’une chaîne de décisions, pas le point de départ.

---

## 12. Common confusions

### Business Architecture vs Solution Architecture

Business Architecture décrit l’organisation, les capabilities, value streams, processes et services métier.

Solution Architecture conçoit une solution spécifique traversant souvent plusieurs domaines.

### Data Architecture vs Application Architecture

Data Architecture : **information/data itself and its management**.

Application Architecture : **software applications/services and interactions**.

### Application Architecture vs Technology Architecture

Application : responsabilités logicielles et interactions.

Technology : plateformes et services technologiques qui hébergent/supportent ces applications.

---

## 13. OGEA-103 exam traps

1. Une question sur les **business capabilities** pointe vers Business Architecture, pas Technology Architecture.
2. Une question sur ownership, lifecycle ou structure des données pointe vers Data Architecture.
3. Une question sur application interactions pointe vers Application Architecture.
4. Une question sur infrastructure/platform services pointe vers Technology Architecture.
5. Phase C inclut Data + Application.
6. Ne choisis pas un produit avant d’avoir clarifié la capability technologique nécessaire lorsque le scénario demande un raisonnement d’architecture.

---

## 14. Foundation questions

### Q1
Quels sont les quatre domaines d’architecture principaux dans TOGAF ?

**Answer:** Business, Data, Application, Technology.

### Q2
Dans quelle phase ADM développe-t-on principalement Data et Application Architecture ?

**Answer:** Phase C — Information Systems Architectures.

### Q3
Une business capability est-elle une application ?

**Answer:** non. Une capability décrit ce que l’entreprise est capable de faire ; une application peut contribuer à la réaliser.

### Q4
Pourquoi Technology Architecture ne devrait-elle pas commencer par une liste de produits ?

**Answer:** parce qu’il faut d’abord comprendre les capabilities/services technologiques nécessaires pour supporter les architectures métier, data et application.

---

## 15. English for Architects

Useful sentences:

- Business Architecture describes how the enterprise operates and what it needs to be able to do.
- Data Architecture defines the structure and management of important data assets.
- Application Architecture describes applications and their interactions.
- Technology Architecture defines the technology services that support applications and data.

### Speak it

1. The business capability drives the application requirements.
2. The application architecture requires an event-streaming capability.
3. The technology architecture provides the platform services.

---

## 16. Interview question

**Question:** Can you explain the four TOGAF architecture domains?

**Simple answer:**

TOGAF uses four main domains: Business, Data, Application and Technology. Business Architecture explains what the organization must be able to do. Data Architecture covers important data assets. Application Architecture covers software applications and interactions. Technology Architecture defines the infrastructure and platform services that support them.

---

## 17. Key points to remember

**B → C(Data + Application) → D(Technology)** is the basic ADM mapping.

But do not memorize only the letters. Memorize the questions:

- **Business:** what must the enterprise do?
- **Data:** what information is required and how is it managed?
- **Application:** what software responsibilities and interactions are needed?
- **Technology:** what technical services and platforms support them?
