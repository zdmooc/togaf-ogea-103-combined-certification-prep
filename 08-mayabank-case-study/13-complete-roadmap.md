# MayaBank — Complete ADM Roadmap

## 1. Purpose

Ce chapitre reconnecte tout le cas MayaBank en un seul raisonnement. L’objectif est de pouvoir expliquer la transformation sans réciter les phases séparément.

La chaîne est :

**Capability → Vision → Business Target → Data/Application Target → Technology Target → Gaps → Work Packages → Transition Architectures → Migration Plan → Implementation Governance → Change Management**.

Requirements Management traverse tout le parcours.

## 2. End-to-end summary

### Preliminary — Prepare the capability

MayaBank met en place :

- Architecture Board ;
- rôles ;
- principles ;
- Architecture Repository ;
- compliance et exception process ;
- tailoring de l’ADM.

**Question résolue :** comment MayaBank pratique-t-elle et gouverne-t-elle l’architecture ?

### Phase A — Architecture Vision

MayaBank :

- cadre les paiements européens ;
- identifie stakeholders et concerns ;
- clarifie business drivers ;
- produit une vision cible de haut niveau ;
- formalise le Statement of Architecture Work ;
- obtient l’accord du sponsor.

**Question :** quel changement veut-on conduire et pourquoi ?

### Phase B — Business Architecture

Cible :

- Payment Orchestration Capability ;
- Unified Validation ;
- Risk Screening ;
- Exception Management ;
- Payment Tracking ;
- Operational Visibility.

**Question :** que doit savoir faire le métier ?

### Phase C — Data Architecture

Cible :

- modèle Payment partagé ;
- ownership ;
- lifecycle ;
- qualité ;
- lineage ;
- auditability ;
- gouvernance de statuts.

**Question :** quelles informations doivent être maîtrisées ?

### Phase C — Application Architecture

Cible :

- Payment Intake ;
- Validation ;
- Risk Screening ;
- Orchestration ;
- Tracking ;
- Exception Management ;
- adapters et services de notification.

**Question :** quels services applicatifs supportent les capacités ?

### Phase D — Technology Architecture

Cible :

- container platform ;
- API management ;
- event streaming ;
- secrets ;
- observability ;
- CI/CD/GitOps ;
- network/security controls ;
- resilience.

**Question :** quelle plateforme technologique supporte les applications et NFR ?

### Phase E — Opportunities & Solutions

Work packages :

1. Platform Foundation ;
2. Canonical Data Model ;
3. Integration Foundation ;
4. Payment Orchestration ;
5. Risk & Exception Modernization ;
6. Legacy Rationalization.

Transition Architectures :

- T1 Foundation + coexistence ;
- T2 Hybrid Processing ;
- T3 Target.

**Question :** comment regrouper les changements et définir les étapes de transformation ?

### Phase F — Migration Planning

Migration waves :

- Wave 1 Foundations ;
- Wave 2 Pilot ;
- Wave 3 Scale ;
- Wave 4 Rationalize.

Les work packages sont priorisés selon valeur, risque, dépendances et readiness.

**Question :** dans quel ordre exécuter la transformation ?

### Phase G — Implementation Governance

MayaBank gouverne :

- Architecture Contract ;
- Compliance Reviews ;
- deviations ;
- exceptions ;
- evidence ;
- corrective actions.

**Question :** l’implémentation respecte-t-elle l’architecture approuvée ?

### Phase H — Change Management

MayaBank surveille :

- business drivers ;
- réglementation ;
- technologie ;
- risques ;
- coûts ;
- performance ;
- exceptions ;
- dette.

Puis décide : changement local, architecture work ciblé ou nouveau cycle ADM.

**Question :** l’architecture doit-elle évoluer ?

## 3. Roadmap table

| Stage | Main outcome | Main value |
|---|---|---|
| Preliminary | Architecture Capability | cohérence de gouvernance |
| A | Vision + scope | alignement sponsor |
| B | Business target | capacités métier claires |
| C Data | governed information | cohérence et traçabilité |
| C App | application services | responsabilités SI claires |
| D | technology target | plateforme cohérente |
| E | work packages + transitions | trajectoire architecturale |
| F | migration plan | exécution priorisée |
| G | compliance governance | contrôle de l’implémentation |
| H | change management | architecture durable |

## 4. Transition roadmap

```text
Baseline
  |
  | WP1 Platform Foundation
  | WP2 Canonical Data
  | WP3 Integration Foundation
  v
Transition 1 — Foundation + Legacy Coexistence
  |
  | WP4 Pilot Orchestration
  v
Transition 2 — Hybrid Payment Processing
  |
  | WP5 Risk & Exception Modernization
  | Extend scope
  v
Target — Governed Real-Time Payment Platform
  |
  | WP6 Legacy Rationalization
  v
Optimized Target Landscape
```

## 5. Why no big bang

Le big bang est rejeté car :

- business continuity critique ;
- dépendances legacy ;
- besoin de preuve opérationnelle ;
- apprentissage progressif ;
- réduction du risque ;
- possibilité de rollback/fallback.

Les Transition Architectures ne sont donc pas des compromis accidentels : ce sont des états intermédiaires intentionnels.

## 6. Critical traceability chain

Exemple :

**Concern** : continuité de paiement  
→ **Requirement** : migration avec fallback  
→ **Business impact** : continuité du service  
→ **Application design** : coexistence/adapters  
→ **Technology design** : platform resilience  
→ **Work Package** : Platform Foundation + Pilot  
→ **Governance** : go/no-go + evidence  
→ **Phase H** : monitoring des résultats.

## 7. Main confusion pairs resolved by the case

### Preliminary vs A

- Preliminary : capacité d’architecture.
- A : engagement de transformation.

### A vs B

- A : vision de haut niveau.
- B : Business Architecture détaillée au niveau nécessaire.

### C Data vs C Application

- Data : information, ownership, lifecycle.
- Application : services et responsabilités applicatives.

### D vs E

- D : cible technologique.
- E : work packages et Transition Architectures.

### E vs F

- E : structure la transformation.
- F : priorise et séquence l’exécution.

### F vs G

- F : planifie.
- G : gouverne l’implémentation.

### G vs H

- G : conformité pendant delivery.
- H : évolution après changement de contexte.

### H vs Requirements Management

- H : décide comment répondre aux changements.
- Requirements Management : gère les exigences tout au long du cycle.

## 8. Foundation revision test

Tu dois pouvoir répondre sans notes :

1. Quelle phase définit la Business Architecture ?
2. Où sont consolidés les work packages ?
3. Où sont-ils priorisés ?
4. Quelle phase gouverne l’implémentation ?
5. Quelle phase évalue les nouveaux change drivers ?
6. Quelle fonction reste transversale ?

Réponses : B, E, F, G, H, Requirements Management.

## 9. Practitioner reasoning test

### Scenario

MayaBank possède une Target Architecture approuvée. Les gaps ont été identifiés, mais personne n’a encore défini les groupes cohérents de changements ni les états intermédiaires.

**Best direction:** Phase E — regrouper les gaps en work packages et définir les Transition Architectures.

### Scenario

Les work packages sont définis mais le budget impose de choisir leur ordre.

**Best direction:** Phase F — prioriser et construire l’Implementation and Migration Plan.

### Scenario

Une équipe modifie le mécanisme d’authentification sans respecter un standard approuvé.

**Best direction:** Phase G — Compliance Review et gestion contrôlée de l’écart.

### Scenario

Une nouvelle réglementation change profondément les données nécessaires au paiement.

**Best direction:** Phase H évalue le changement et peut déclencher un nouveau cycle ; Requirements Management enregistre et trace les nouvelles exigences.

## 10. 90-second interview explanation

> MayaBank started by establishing its architecture capability and governance. In Phase A, we aligned stakeholders on the payment modernization vision and scope. We then developed the target business capabilities, data architecture, application services, and technology platform through Phases B, C, and D. In Phase E, we consolidated the gaps into work packages and transition architectures. Phase F prioritized them into migration waves. During implementation, Phase G governed compliance and exceptions. Finally, Phase H monitored business, regulatory, and technology change. Requirements Management remained continuous across the entire lifecycle.

## 11. What this case proves

TOGAF n’est pas une collection de documents. Le cas montre une logique de transformation :

**understand → decide → design → transition → plan → govern → evolve**.

C’est cette logique qui doit être maîtrisée pour OGEA-103, particulièrement pour la partie Practitioner où plusieurs réponses peuvent sembler acceptables mais une seule respecte le mieux le contexte et la séquence.

---

Original educational case study; MayaBank is fictional. Product and technology examples are illustrative, not TOGAF prescriptions.