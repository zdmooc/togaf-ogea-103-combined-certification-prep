# 05 — Stakeholders, Concerns, Views and Viewpoints

## 1. Why this topic matters

Une architecture n’est pas créée pour elle-même. Elle doit répondre aux préoccupations des personnes et groupes qui ont un intérêt dans la transformation.

TOGAF utilise quatre concepts étroitement liés :

```text
Stakeholder
   ↓ has
Concern
   ↓ addressed through
Viewpoint
   ↓ governs construction of
View
```

Cette relation est essentielle pour Foundation et très importante pour Practitioner.

---

## 2. Stakeholder

Un **Stakeholder** est une personne, un groupe ou une organisation ayant un intérêt dans un système, une architecture ou une transformation.

Examples:

- executive sponsor ;
- business owner ;
- regulator ;
- security officer ;
- operations team ;
- development team ;
- architect ;
- customer representative ;
- finance ;
- external partner.

Un stakeholder peut :

- financer ;
- approuver ;
- utiliser ;
- exploiter ;
- contrôler ;
- être affecté ;
- porter une contrainte ;
- bloquer la transformation.

### Key idea

Tous les stakeholders n’ont pas la même influence ni les mêmes préoccupations.

---

## 3. Concern

Un **Concern** est un intérêt important pour un stakeholder à propos de l’architecture.

Examples:

- security ;
- availability ;
- cost ;
- business continuity ;
- performance ;
- interoperability ;
- compliance ;
- user experience ;
- maintainability ;
- time-to-market.

### MayaBank example

Pour la même target payment platform :

| Stakeholder | Concern |
|---|---|
| Head of Payments | faster product launch |
| CIO | simplification and strategic alignment |
| CISO | security and regulatory compliance |
| Operations | recoverability and observability |
| Finance | cost and investment |
| Development teams | platform usability |

Le rôle de l’architecture est de rendre ces concerns explicites et de montrer comment les décisions y répondent.

---

## 4. Why stakeholder management starts early

Les stakeholders doivent être identifiés tôt, notamment en **Phase A — Architecture Vision**.

Pourquoi ?

Parce que le scope, la valeur, les risques et même la définition du problème peuvent être incomplets si les acteurs importants sont absents.

Example :

Une équipe propose une migration vers OpenShift et consulte seulement les développeurs.

La solution semble excellente jusqu’à ce que :

- Security refuse le modèle de secrets ;
- Operations découvre l’absence de stratégie DR ;
- Finance découvre un coût GPU/infra non prévu ;
- Compliance exige une conservation spécifique des logs.

Le problème n’est pas uniquement technique : le stakeholder analysis était incomplet.

---

## 5. Stakeholder analysis

Une pratique utile consiste à analyser au moins :

- stakeholder identity ;
- role ;
- key concerns ;
- level of influence ;
- level of interest ;
- required engagement ;
- communication needs.

Un modèle classique peut utiliser une matrice pouvoir/intérêt.

```text
High power
  |
  | Manage closely       Keep satisfied
  |
  | Keep informed        Monitor
  +------------------------------> Interest
```

Le modèle exact peut être adapté. L’objectif est de déterminer la stratégie d’engagement.

### Practitioner insight

Dans un scénario Part 2, une réponse qui ignore un stakeholder critique est souvent moins bonne qu’une réponse qui traite correctement ses concerns, même si elle paraît techniquement plus rapide.

---

## 6. Viewpoint

Un **Architecture Viewpoint** définit les conventions nécessaires pour construire, interpréter et utiliser un type de view afin d’adresser certains concerns.

Un viewpoint peut préciser :

- quels stakeholders sont visés ;
- quels concerns sont adressés ;
- quelles informations doivent être montrées ;
- quelles conventions ou notations sont utilisées ;
- quel niveau de détail est approprié.

### Think of it as

**Viewpoint = recipe / rules for a view.**

Ce n’est pas encore la représentation d’un système spécifique.

---

## 7. View

Une **Architecture View** est une représentation de l’architecture construite selon un viewpoint et destinée à répondre à certains concerns.

Example :

Viewpoint : « application dependency viewpoint for operational impact analysis ».

View : le diagramme réel de MayaBank montrant :

```text
Mobile App
   ↓
Payment API
   ↓
Orchestrator
   ↓        ↓
Fraud     Settlement
   ↓
Kafka
```

Cette view est spécifique à MayaBank.

---

## 8. View vs diagram

Une **View** n’est pas nécessairement un diagramme unique.

Une view exprime une architecture depuis une perspective donnée. Selon le besoin, elle peut s’appuyer sur différents artifacts et modèles.

Pour l’examen, retiens surtout la relation conceptuelle :

**Viewpoint defines conventions; View is the representation.**

---

## 9. Why one architecture needs multiple views

Une représentation unique ne peut généralement pas répondre correctement à toutes les préoccupations.

Exemple : un diagramme d’infrastructure détaillé avec nodes, network zones et storage est utile à Operations, mais très mauvais pour expliquer la valeur métier au sponsor.

Inversement, une capability map high-level est utile à la direction mais insuffisante pour un design review réseau.

L’architecte choisit donc les views en fonction des stakeholders et concerns.

### Rule

**Do not communicate everything to everyone in the same way.**

---

## 10. Stakeholder communication

Le bon niveau de communication dépend du stakeholder.

### Executive sponsor

Besoin typique :

- why change ;
- business value ;
- scope ;
- major risks ;
- high-level target ;
- cost/time implications.

### Security

Besoin typique :

- threat exposure ;
- trust boundaries ;
- IAM ;
- data classification ;
- regulatory controls.

### Operations

Besoin typique :

- deployment topology ;
- monitoring ;
- failure modes ;
- RTO/RPO ;
- operational ownership.

Une Architecture Vision ne doit donc pas devenir un dump de détails techniques.

---

## 11. Stakeholders and requirements

Concerns ne sont pas automatiquement des requirements.

Example :

Concern : « je crains une indisponibilité lors de la perte d’un datacenter ».

Après analyse, cela peut générer plusieurs requirements :

- service availability objective ;
- RTO ;
- RPO ;
- dual-site deployment ;
- failover testing.

Relationship:

```text
Stakeholder
   ↓
Concern
   ↓ analysis
Requirement(s)
   ↓
Architecture decision
```

---

## 12. Stakeholders and governance

Stakeholders ne disparaissent pas après Phase A.

Leur rôle continue pendant :

- validation des architectures ;
- arbitrage ;
- roadmap ;
- implementation governance ;
- change management.

Certaines décisions nécessitent également l’intervention de l’**Architecture Board** ou d’autres instances de gouvernance.

---

## 13. MayaBank detailed example

### Transformation

Moderniser les paiements et introduire une plateforme temps réel.

### Stakeholder 1 — Head of Payments

Concern : capacité à lancer rapidement de nouveaux parcours.

Relevant view : capability/value-stream view montrant où la nouvelle plateforme améliore le métier.

### Stakeholder 2 — CISO

Concern : fraude, authentication, authorization, audit.

Relevant view : security architecture view montrant trust boundaries et controls.

### Stakeholder 3 — Operations

Concern : incident recovery.

Relevant view : deployment/resilience view montrant sites, platform services et failover.

### Stakeholder 4 — Finance

Concern : coût de coexistence legacy + target.

Relevant view : transition roadmap / cost-oriented representation.

Même architecture, plusieurs concerns, donc plusieurs views.

---

## 14. Common mistakes

1. Identifier seulement les « utilisateurs » comme stakeholders.
2. Confondre stakeholder et concern.
3. Créer un diagramme unique pour tout le monde.
4. Choisir les views avant d’identifier les concerns.
5. Communiquer avec le sponsor au niveau de détail technique de l’équipe plateforme.
6. Traiter stakeholder management comme une activité uniquement initiale.
7. Confondre Viewpoint et View.

---

## 15. OGEA-103 exam traps

### Trap 1
« A view defines the conventions for representation. »

→ Faux. C’est le **Viewpoint** qui définit les conventions.

### Trap 2
Un scénario mentionne un stakeholder mécontent mais propose immédiatement une technologie.

→ Il faut souvent d’abord comprendre/traiter le concern.

### Trap 3
Une réponse crée une architecture détaillée avant d’obtenir l’alignement des stakeholders clés en Phase A.

→ Mauvaise séquence probable.

### Trap 4
Un stakeholder concern est traité comme s’il était déjà une requirement formelle.

→ Le concern doit être analysé et peut conduire à une ou plusieurs requirements.

---

## 16. Foundation questions

### Q1
Quelle est la relation entre Stakeholder et Concern ?

**Answer:** un stakeholder porte un ou plusieurs concerns concernant l’architecture.

### Q2
Quelle notion définit les conventions utilisées pour construire une représentation ?

**Answer:** Viewpoint.

### Q3
Quelle notion est la représentation concrète de l’architecture depuis une perspective donnée ?

**Answer:** View.

### Q4
Pourquoi utiliser plusieurs views ?

**Answer:** parce que différents stakeholders ont différents concerns et niveaux d’information nécessaires.

---

## 17. Practitioner mini-scenario

Le CISO de MayaBank rejette une architecture en Phase A car aucun traitement de la conformité et des données sensibles n’est visible. L’équipe propose de continuer jusqu’en Phase D puis de « traiter la sécurité plus tard ».

La meilleure logique TOGAF est de reconnaître immédiatement le stakeholder et son concern, de clarifier les requirements/constraints correspondants et de s’assurer que la vision et le scope prennent correctement en compte ces préoccupations.

Pourquoi ? Parce qu’un concern critique peut changer le scope et les décisions des phases suivantes.

---

## 18. English for Architects

Useful sentences:

- We identified the key stakeholders and their concerns.
- The security team is a high-influence stakeholder.
- This viewpoint addresses availability and recovery concerns.
- This view shows the application dependencies.
- We need a different view for the executive sponsor.

### Speak it

1. The main concern is regulatory compliance.
2. This view is designed for the operations team.
3. We must involve the security stakeholder early.

---

## 19. Interview question

**Question:** How do you manage stakeholders in an architecture engagement?

**Simple answer:**

I identify the key stakeholders, understand their concerns and influence, and define how to engage them. I use different architecture views for different concerns. I keep stakeholder management active throughout the architecture lifecycle, not only at the beginning.

---

## 20. Key points to remember

Memorize:

**Stakeholder = who cares.**

**Concern = what they care about.**

**Viewpoint = how to look.**

**View = what is shown.**

And always keep the sequence:

**Stakeholders → Concerns → Viewpoints → Views → Requirements/decisions.**
