# Agile and TOGAF

## 1. Core idea

TOGAF et Agile ne répondent pas à la même question.

- **TOGAF** organise le raisonnement d’architecture d’entreprise, la cohérence, les requirements, la roadmap et la governance.
- **Agile** organise principalement la livraison incrémentale de valeur dans des boucles courtes.

Ils peuvent être combinés.

Le piège est de croire :

- soit que TOGAF impose un waterfall lourd ;
- soit qu’Agile élimine le besoin d’architecture.

Les deux affirmations sont fausses.

## 2. ADM Phase vs Sprint

Une phase ADM n’est pas un sprint.

Un sprint peut contenir des activités qui contribuent à plusieurs préoccupations architecturales.

Inversement, une phase ADM peut être développée au fil de plusieurs sprints ou ateliers.

Le mapping est donc contextuel, pas un tableau 1 phase = 1 sprint.

## 3. Architecture Intent

Dans un contexte Agile, l’architecture peut être construite comme un ensemble de décisions et guardrails suffisants pour permettre le delivery :

- principles ;
- target direction ;
- key NFRs ;
- reference architectures ;
- reusable building blocks ;
- decision records ;
- standards ;
- constraints.

On évite deux extrêmes :

- Big Design Up Front inutilement détaillé ;
- aucune direction architecturale.

## 4. Incremental architecture

L’architecture cible peut être développée progressivement.

Exemple MayaBank :

### Increment 1

- API foundation ;
- identity ;
- first payment flow.

### Increment 2

- event streaming ;
- observability ;
- resilience patterns.

### Increment 3

- migration multi-scheme ;
- legacy decommissioning.

Chaque increment respecte une direction architecturale cohérente.

## 5. Agile in Phase A

Phase A peut être réalisée rapidement avec :

- concise Architecture Vision ;
- key stakeholders ;
- scope ;
- initial requirements ;
- high-level target ;
- key risks ;
- Statement of Architecture Work adapté.

Le but est d’obtenir suffisamment d’alignement pour avancer, pas de tout concevoir.

## 6. Agile in B/C/D

Les domaines peuvent être approfondis selon les décisions à prendre.

Exemple :

Sprint/iteration 1 : business capability et high-level application decomposition.

Iteration 2 : data contracts et event model.

Iteration 3 : technology decisions for resilience.

Les architectures restent cohérentes via Requirements Management et Architecture Repository.

## 7. Agile in E/F

Phase E/F s’intègre naturellement au backlog et portfolio planning si l’on distingue :

- work package ;
- epic ;
- feature ;
- story.

Ils ne sont pas synonymes.

Un **Work Package** représente un ensemble architectural de travail nécessaire à la transformation.

Il peut être réalisé par plusieurs epics/features.

## 8. Agile in Phase G

Implementation Governance peut devenir plus fréquente et plus légère :

- automated compliance ;
- architecture tests ;
- policy-as-code ;
- ADR review ;
- Definition of Done incluant NFRs ;
- architecture checkpoints ;
- pipeline evidence.

La governance se rapproche du delivery.

## 9. Agile in Phase H

Feedback rapide :

- production telemetry ;
- user feedback ;
- incidents ;
- new regulation ;
- product strategy.

Ces signaux peuvent produire des Architecture Change Requests ou déclencher un nouveau travail ADM.

## 10. Architecture backlog

Un backlog d’architecture peut contenir :

- enablers ;
- technical debt ;
- platform capabilities ;
- migration items ;
- risk mitigations ;
- standards adoption ;
- decommissioning.

Mais le backlog ne remplace pas la Target Architecture et la Roadmap.

## 11. Decision latency

Un objectif important de l’architecture Agile est de réduire le temps entre :

**question → analysis → architecture decision → delivery feedback**.

Pour cela :

- decision rights clairs ;
- standards connus ;
- reusable patterns ;
- architecture office hours ;
- lightweight approval path.

## 12. MayaBank operating model

MayaBank met en place :

- Product Teams Payments ;
- Platform Team OpenShift ;
- Event Platform Team ;
- Security Architecture ;
- Enterprise Architecture guardrails.

Les product teams peuvent choisir localement dans les limites des standards.

Une déviation significative passe par un processus d’exception.

## 13. Agile vs lack of governance

Autonomy ≠ absence de contrôle.

Agile Architecture fonctionne mieux quand :

- principles sont clairs ;
- APIs et events ont des standards ;
- teams comprennent les NFRs ;
- compliance est automatisée autant que possible ;
- exceptions sont rapides mais tracées.

## 14. Common mistakes

- mapper chaque phase ADM à un sprint ;
- remplacer roadmap par backlog ;
- confondre Work Package et User Story ;
- refuser toute architecture « parce qu’on est Agile » ;
- créer une architecture exhaustive avant tout delivery ;
- laisser les teams diverger sans governance.

## 15. OGEA-103 traps

- ADM est iterative et tailorable.
- Agile et TOGAF peuvent coexister.
- L’architecture doit rester proportionnée au besoin.
- Governance peut être continue et légère sans disparaître.
- Une réponse Practitioner équilibrée évite autant le Big Design Up Front que l’absence d’architecture.

## 16. Practitioner scenario

Une organisation Agile veut supprimer Architecture Vision, standards et compliance reviews pour accélérer les sprints. La meilleure réponse est de tailor l’ADM : conserver une vision légère, des guardrails, des requirements et une governance intégrée au delivery, plutôt que supprimer la discipline architecturale.

## 17. English for Architects

> We integrate architecture into Agile delivery through lightweight guardrails, reusable patterns, incremental target states and continuous governance.

### Speak it

1. An ADM phase is not the same as a sprint.
2. We develop architecture incrementally.
3. Governance is integrated into the delivery pipeline.

## 18. Key points

- TOGAF ≠ waterfall.
- Agile ≠ no architecture.
- ADM phase ≠ sprint.
- Work Package ≠ User Story.
- Incremental architecture + guardrails + continuous governance permettent d’aller vite sans perdre la cohérence.

---

The Open Group publishes guidance on applying the TOGAF ADM using Agile Sprints and enabling enterprise agility. This chapter is an original educational explanation.