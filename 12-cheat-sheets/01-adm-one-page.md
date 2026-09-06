# Cheat Sheet — ADM One Page

## La carte mentale

```text
Preliminary
   ↓
Phase A — Architecture Vision
   ↓
Phase B — Business Architecture
   ↓
Phase C — Data Architecture + Application Architecture
   ↓
Phase D — Technology Architecture
   ↓
Phase E — Opportunities & Solutions
   ↓
Phase F — Migration Planning
   ↓
Phase G — Implementation Governance
   ↓
Phase H — Architecture Change Management

Requirements Management = transversal à tout le cycle
```

## Une phrase par étape

| Étape | Question principale | Résultat mental |
|---|---|---|
| Preliminary | Sommes-nous organisés pour faire et gouverner l’architecture ? | Capability, principes, gouvernance, repository, tailoring |
| A | Quel travail lançons-nous, pourquoi et avec qui ? | Scope, stakeholders, value, risks, Architecture Vision |
| B | De quoi le métier doit-il être capable ? | Business Baseline/Target/Gaps |
| C Data | Quelles informations faut-il structurer, gouverner et faire circuler ? | Data Baseline/Target/Gaps |
| C Application | Quels services/applications soutiennent les capacités ? | Application Baseline/Target/Gaps |
| D | Quelles plateformes et technologies soutiennent la cible ? | Technology Baseline/Target/Gaps |
| E | Comment transformer les gaps en solutions et work packages ? | Work Packages, Transition Architectures, Architecture Roadmap |
| F | Dans quel ordre migrer avec quelles priorités ? | Priorisation, séquencement, Implementation & Migration Plan |
| G | Comment gouverner ce qui est réellement implémenté ? | Architecture Contract, Compliance Reviews, exceptions |
| H | Que faire quand l’environnement ou les besoins changent ? | Change requests, impact, nouveau cycle éventuel |

## Le flux complet

```text
Drivers
  → Stakeholders / Concerns
  → Requirements
  → Baseline
  → Target
  → Gaps
  → Work Packages
  → Transition Architectures
  → Roadmap
  → Migration Plan
  → Implementation Governance
  → Change Management
```

## Les quatre domaines

- **Business** : capabilities, services, processes, actors, organization.
- **Data** : data entities, ownership, lifecycle, flows, governance.
- **Application** : application services, interactions, portfolio, interfaces.
- **Technology** : platforms, infrastructure, runtime, networks, technology services.

## Les confusions qui tombent souvent

- Preliminary ≠ Phase A.
- Phase A Vision ≠ Target Architecture détaillée.
- Business Capability ≠ Application.
- Phase D définit la cible technologique ; Phase E transforme les gaps en solutions/work packages.
- Phase E structure les options ; Phase F priorise et séquence.
- Phase F planifie ; Phase G gouverne l’implémentation.
- Phase G traite l’implémentation en cours ; Phase H traite l’évolution de l’architecture.
- Requirements Management n’est pas une phase finale : il est transversal.

## Réflexe Foundation

Pour une question de définition : identifier le **concept exact**, pas l’objet voisin.

Exemple : « état intermédiaire cohérent » → **Transition Architecture**, pas roadmap.

## Réflexe Practitioner

Avant de lire les réponses, demander :

1. Où en sommes-nous dans l’ADM ?
2. Quel est le problème dominant ?
3. Quels stakeholders/concerns/requirements sont en jeu ?
4. Quelle action respecte la séquence et la gouvernance ?

## MayaBank en une ligne

MayaBank passe d’un paysage paiement fragmenté à une cible plus cohérente en reliant : **business capabilities → data/application services → technology platform → gaps → work packages → transition states → migration waves → governance → change**.

## English

> The ADM connects business drivers to target architectures, migration planning, implementation governance, and continuous change management.
