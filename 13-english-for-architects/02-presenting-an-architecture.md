# Presenting an Architecture in English

## 1. La structure la plus sûre

Pour présenter une architecture, utiliser toujours la même ossature :

```text
1. Context
2. Business problem
3. Current state
4. Target state
5. Key decisions
6. Risks and trade-offs
7. Migration approach
8. Governance and next steps
```

## 2. Opening

> I will first explain the business context, then the current architecture, the target state, the main decisions, and finally the migration approach and risks.

Cette phrase donne immédiatement une structure à l’interlocuteur.

## 3. Context

Phrases utiles :

- `The company is modernizing...`
- `The program was initiated because...`
- `The main business drivers are...`
- `The scope includes...`
- `The following areas are out of scope...`

Exemple MayaBank :

> MayaBank is modernizing its European payment platform. The main drivers are faster processing, higher resilience, better auditability, and a shorter time to market. The first scope covers payment orchestration, fraud screening, clearing integration, operational data, and the supporting technology platform.

## 4. Current state

Utiliser trois niveaux : architecture, opération, conséquence métier.

> The current landscape is fragmented. Several applications provide overlapping functions, integration is partly point-to-point, and a significant part of the processing is batch-based. As a result, changes are slow, incidents are difficult to diagnose, and operational costs are high.

## 5. Target state

Éviter la liste de produits. Parler d’abord des propriétés de la cible.

> The target architecture introduces clear service boundaries, governed APIs and events, explicit data ownership, stronger observability, and a standardized runtime platform. The objective is not only modernization; it is to improve business agility and operational resilience.

## 6. Key decisions

Formule : decision → reason → consequence.

> We chose an incremental migration rather than a big-bang replacement because payment continuity is critical. This reduces migration risk, but it requires temporary coexistence between legacy and target components.

> We standardized integration contracts because multiple local interfaces were increasing coupling and maintenance cost.

## 7. Trade-offs

Un architecte crédible ne présente pas une solution parfaite.

Phrases :

- `The main trade-off is between...`
- `This option improves X but increases Y.`
- `We accepted this complexity because...`
- `The alternative would reduce cost but increase risk.`
- `There is no zero-risk option.`

Exemple :

> The main trade-off is between migration speed and operational risk. A faster migration would reduce coexistence cost, but it would increase business continuity risk. We therefore selected a phased approach.

## 8. Risks

Présenter : risk → impact → mitigation.

> One major risk is inconsistent adoption across delivery teams. The impact would be architecture drift and additional support complexity. We mitigate this through standards, automated controls, architecture reviews, and a formal exception process.

## 9. Migration approach

> We first establish the common platform capabilities and observability. We then migrate a limited business scope, validate the transition architecture, and expand through additional migration waves. Legacy components are decommissioned only after the required capabilities have been proven in production.

## 10. Governance

> Architecture governance continues during implementation. We use architecture contracts, compliance reviews, traceable decisions, and governed exceptions. The objective is not to block delivery; it is to preserve the architectural intent while allowing controlled change.

## 11. Closing

> In summary, the architecture moves MayaBank from a fragmented payment landscape to a more modular, observable, and governable platform. The transformation is incremental, and the main architectural priority is to balance business continuity, delivery speed, and long-term coherence.

## 12. Questions difficiles

### Why not use a big-bang migration?

> Because the business impact of a failure would be too high. A phased migration gives us controlled transition states, measurable feedback, and rollback options.

### Why did you choose this technology?

> We did not start with the technology. We first defined the required capabilities, constraints, and quality attributes. We then evaluated technology options against those requirements.

### What is the biggest weakness of the target architecture?

> The main weakness is temporary complexity during coexistence. We accept it because it reduces migration risk, but we manage it with explicit transition architectures and decommissioning criteria.

## 13. Exercise — 2 minutes

Présenter oralement MayaBank sans notes avec les huit blocs : Context → Problem → Baseline → Target → Decisions → Risks → Migration → Governance.

Objectif : parler lentement, avec des phrases courtes, sans chercher un vocabulaire sophistiqué.
