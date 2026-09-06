# Cheat Sheet — Phase E vs Phase F

## La différence en une phrase

- **Phase E — Opportunities & Solutions** : transforme les gaps en **work packages**, options de solution et **Transition Architectures**.
- **Phase F — Migration Planning** : **priorise, séquence et planifie** ces work packages pour produire l’Implementation & Migration Plan.

## Tableau comparatif

| Sujet | Phase E | Phase F |
|---|---|---|
| Question | Que devons-nous transformer et comment regrouper les changements ? | Dans quel ordre devons-nous migrer ? |
| Inputs typiques | gaps B/C/D, target architectures | roadmap initiale, work packages, contraintes |
| Focus | solution grouping, dependencies, transitions | prioritization, sequencing, value/risk/cost |
| Output mental | work packages + Transition Architectures + roadmap initiale | Implementation & Migration Plan détaillé |

## Les mots qui orientent vers E

- identify opportunities
- solution options
- work packages
- consolidate gaps
- Transition Architecture
- major implementation projects
- initial Architecture Roadmap

## Les mots qui orientent vers F

- prioritize
- sequence
- migration wave
- cost / benefit / risk
- dependency ordering
- detailed migration plan
- implementation schedule

## Exemple MayaBank

### Situation

Gaps identifiés :

- absence d’API governance ;
- batch trop important ;
- faible observabilité ;
- plateformes hétérogènes ;
- données dupliquées.

### Phase E

L’architecte regroupe les gaps en work packages :

1. API & Event Governance
2. Observability Foundation
3. Payment Services Modernization
4. Data Ownership & Quality
5. Platform Standardization

Puis il définit des Transition Architectures réalistes.

### Phase F

Il décide par exemple :

1. Observability Foundation d’abord ;
2. API/Event Governance ensuite ;
3. migration d’un périmètre pilote ;
4. extension par vagues ;
5. retrait du legacy en dernier.

La logique de priorité dépend de la valeur, du risque, des dépendances, des capacités et des contraintes.

## Pièges d’examen

### Piège 1

« Identifier les work packages » → **E**, pas F.

### Piège 2

« Déterminer quelle initiative passe en premier » → **F**.

### Piège 3

Une **Transition Architecture** n’est pas une migration wave. La première décrit un **état architectural intermédiaire** ; la seconde décrit un **lot séquencé de changement**.

### Piège 4

Une roadmap n’est pas automatiquement le plan de migration détaillé.

## Mémo

> **E = Explore and package the change.**
>
> **F = Fix the order of migration.**

## English for Architects

> In Phase E, we consolidate architecture gaps into work packages and transition states. In Phase F, we prioritize and sequence those work packages into an implementation and migration plan.
