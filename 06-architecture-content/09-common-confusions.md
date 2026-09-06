# Architecture Content — Common Confusions

## 1. Objectif

Ce chapitre consolide les distinctions qui provoquent le plus d’erreurs en Foundation et Practitioner.

## 2. Deliverable vs Artifact vs Building Block

| Concept | Question | Exemple |
|---|---|---|
| Deliverable | quel produit formel est remis / approuvé ? | Architecture Definition Document |
| Artifact | quelle représentation est utilisée ? | Application Communication Diagram |
| Building Block | quel élément d’architecture est représenté ? | Payment API |

### Mémo

**Deliverable contains Artifacts; Artifacts describe Building Blocks.**

## 3. ABB vs SBB

| ABB | SBB |
|---|---|
| besoin / capacité architecturale | réalisation plus concrète |
| plus logique | plus solution-oriented |
| définit ce qui est requis | définit comment cela peut être réalisé |

Exemple :

ABB = Event Streaming Service.

SBB = plateforme Kafka concrète retenue.

## 4. View vs Viewpoint

| Viewpoint | View |
|---|---|
| conventions de construction | représentation concrète |
| réutilisable | spécifique à une architecture / situation |
| répond « comment regarder ? » | répond « que montre-t-on ici ? » |

Chaîne : **Stakeholder → Concern → Viewpoint → View**.

## 5. Catalog vs Matrix vs Diagram

- Catalog : liste structurée.
- Matrix : relations entre deux ensembles.
- Diagram : structure ou interactions visuelles.

## 6. Content Metamodel vs Repository

- Content Metamodel = types d’éléments + relations.
- Repository = stockage et gestion des assets d’architecture.

Le metamodel structure ce qui peut être enregistré dans le repository.

## 7. Enterprise Continuum vs Architecture Repository

- Enterprise Continuum = mécanisme de classification / perspective de réutilisation.
- Architecture Repository = ensemble structuré où les assets sont gérés.

## 8. Architecture Definition Document vs Architecture Requirements Specification

### Architecture Definition Document

Décrit Baseline et Target Architectures et leur structure.

### Architecture Requirements Specification

Regroupe les exigences auxquelles l’architecture et l’implémentation doivent satisfaire.

**Description de la cible ≠ exigences sur la cible.**

## 9. Architecture Roadmap vs Implementation and Migration Plan

### Architecture Roadmap

Vue de trajectoire : work packages, Transition Architectures, évolution vers la cible.

### Implementation and Migration Plan

Plan plus détaillé et coordonné de mise en œuvre / migration, renforcé en Phase F.

## 10. Building Block vs Work Package

- Building Block = élément architectural ou solution.
- Work Package = ensemble de travail nécessaire pour réaliser une partie de la transformation.

## 11. Principle vs Requirement

### Principle

Règle durable qui guide les décisions.

### Requirement

Besoin ou condition spécifique à satisfaire.

Exemple :

Principle : `Data is protected by design`.

Requirements possibles : chiffrement AES-256 au repos, TLS en transit, classification obligatoire.

## 12. Baseline vs Target vs Transition Architecture

- Baseline = état actuel pertinent.
- Target = état futur souhaité.
- Transition Architecture = état intermédiaire cohérent entre les deux.

Transition ≠ roadmap. La transition est un **état** ; la roadmap organise le **chemin**.

## 13. MayaBank — exercice intégré

MayaBank définit un service logique `Payment Event Streaming`.

- ABB : Payment Event Streaming Service.
- SBB : plateforme Kafka retenue.
- Artifact : Technology Platform Diagram montrant la plateforme.
- Deliverable : Architecture Definition Document qui contient ce diagramme.
- Requirement : chiffrement des événements sensibles.
- Principle : Security by Design.
- Work Package : construire et industrialiser la plateforme streaming.
- Transition Architecture : coexistence legacy messaging + Kafka.
- Roadmap : séquence de migration des flux vers Kafka.

Cette chaîne est l’un des meilleurs exercices pour vérifier que les concepts sont réellement compris.

## 14. Pièges Foundation

### Question : « un diagramme est quoi ? »

**Artifact.**

### Question : « un élément réutilisable de l’architecture ? »

**Building Block.**

### Question : « conventions utilisées pour construire une vue ? »

**Viewpoint.**

### Question : « produit formel soumis à review ? »

**Deliverable.**

### Question : « relation entre deux ensembles d’éléments ? »

**Matrix.**

## 15. Pièges Practitioner

Le scénario donne rarement la définition explicitement. Il faut reconnaître la fonction.

Exemple :

« Le sponsor ne comprend pas le diagramme technique. »

Le problème n’est pas forcément l’architecture : le viewpoint/view ne répond peut-être pas au concern du sponsor.

« Les équipes choisissent un produit avant d’avoir défini le besoin. »

Le problème peut être le passage prématuré au SBB avant l’ABB et les requirements.

« Personne ne sait quelle version est approuvée. »

Le problème concerne la gouvernance du deliverable et du repository.

## 16. Quiz rapide

### Q1
Une liste d’applications est un :

**Catalog.**

### Q2
Un diagramme de communication est un :

**Artifact.**

### Q3
`Payment API` représenté dans ce diagramme est un :

**Building Block.**

### Q4
Les règles pour construire une représentation sécurité constituent un :

**Viewpoint.**

### Q5
La représentation sécurité concrète de MayaBank constitue une :

**View.**

## 17. English for Architects

> A deliverable is a formal work product. It contains artifacts such as catalogs, matrices, and diagrams. These artifacts represent architecture building blocks.

> A viewpoint defines how to construct a view for specific stakeholder concerns.

> Architecture Building Blocks describe architectural needs; Solution Building Blocks describe more concrete realizations.

## 18. Final memory map

```text
Stakeholder
   ↓ concern
Viewpoint
   ↓ constructs
View
   ↓ uses
Artifact (Catalog / Matrix / Diagram)
   ↓ represents
Building Block (ABB / SBB)

Artifacts
   ↓ packaged into
Deliverable
```

## 19. Key points

- Deliverable ≠ Artifact ≠ Building Block.
- ABB ≠ SBB.
- View ≠ Viewpoint.
- Catalog ≠ Matrix ≠ Diagram.
- Repository ≠ Continuum.
- Roadmap ≠ Migration Plan.
- Transition Architecture = état intermédiaire, pas plan.

---

Original educational explanation based on the TOGAF Standard, 10th Edition.