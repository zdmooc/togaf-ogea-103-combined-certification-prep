# Architecture Governance — Scenarios

## 1. Objectif

Ce chapitre entraîne à reconnaître **quel mécanisme de gouvernance utiliser** dans un scénario TOGAF.

La question Practitioner n’est souvent pas « connais-tu la définition ? » mais « quelle action protège le mieux l’intégrité de l’architecture dans ce contexte ? ».

## 2. Carte de décision

| Situation | Mécanisme dominant |
|---|---|
| conflit entre architectures | Architecture Board / escalation |
| engagement implementation | Architecture Contract |
| vérifier une solution réalisée | Compliance Review |
| écart justifié | exception / waiver |
| écart non justifié | remediation / escalation |
| changements répétés du contexte | Phase H / change management |
| absence de règles de décision | renforcer Architecture Capability / Preliminary |

## 3. Scénario 1 — conflit inter-programmes

Deux programmes veulent des standards API différents pour une capability commune.

**Mauvaise réaction :** choisir celui préféré par l’architecte.

**Bonne logique :** analyser les impacts enterprise, appliquer les principes et escalader au niveau de gouvernance approprié.

## 4. Scénario 2 — delivery non conforme

La cible exige un pipeline automatisé. Une équipe déploie manuellement en production.

**Action :** Compliance Review, analyse du gap, décision de remediation ou exception.

## 5. Scénario 3 — contrainte légitime

Un système réglementé ne peut pas adopter immédiatement le standard cible.

**Action :** traiter l’écart via un waiver explicite, risk-assessed et suivi.

## 6. Scénario 4 — architecture correcte, responsabilités floues

Les équipes ne savent pas qui doit fournir les preuves de conformité.

**Action :** clarifier les responsabilités et formaliser les engagements dans le mécanisme de gouvernance approprié, notamment Architecture Contract.

## 7. Scénario 5 — trop d’exceptions identiques

Cinq projets demandent la même dérogation au même standard.

**Action :** ne pas traiter uniquement cinq waivers isolés ; évaluer si le standard ou la Target Architecture reste adapté. Cela peut alimenter Architecture Change Management.

## 8. Scénario 6 — Board bureaucratique

Toutes les décisions mineures doivent attendre le Board central.

**Action :** adapter la gouvernance, déléguer les décisions proportionnées et définir des critères d’escalade. Governance ne signifie pas centralisation totale.

## 9. Architecture Governance vs Project Governance — scénario

Le projet dépasse son budget mais reste conforme à l’architecture.

Le problème principal relève du **Project Governance**.

Le projet respecte son budget mais viole la Target Architecture.

Le problème principal relève de l’**Architecture Governance**.

## 10. Foundation questions

### Q1
Quel mécanisme vérifie l’alignement d’une implémentation avec l’architecture ?

**Réponse : Architecture Compliance Review.**

### Q2
Quel mécanisme supervise les décisions et arbitrages majeurs ?

**Réponse : Architecture Board.**

### Q3
Quel mécanisme formalise les responsabilités et engagements de réalisation ?

**Réponse : Architecture Contract.**

## 11. Méthode Practitioner

Face à un scénario :

1. identifier ce qui est déjà approuvé ;
2. identifier l’écart ou conflit ;
3. identifier le stakeholder / owner de décision ;
4. choisir le mécanisme de gouvernance ;
5. préserver traçabilité et risk management ;
6. préférer une réponse proportionnée à une action extrême.

## 12. MayaBank — scénario intégré

Le programme paiement est à trois semaines d’une release. Un composant essentiel ne respecte pas le standard de chiffrement cible. Le supplier affirme qu’un correctif nécessite trois mois.

Une réponse robuste consiste à :

- confirmer la non-conformité ;
- évaluer l’exposition et les alternatives ;
- consulter Security/Risk ;
- soumettre la décision à l’autorité appropriée ;
- si exception, définir compensating controls, owner, échéance et remédiation ;
- enregistrer la décision.

« Livrer quand même » et « bloquer automatiquement le programme » sont deux réponses trop simplistes.

## 13. English for Architects

> Governance should be proportionate. We review significant deviations, assess the risk, make an explicit decision, and keep the evidence traceable.

## 14. Key points

- Board = arbitrage et supervision.
- Contract = engagements.
- Compliance Review = contrôle.
- Exception = décision gouvernée sur un écart.
- Phase H = évolution de l’architecture.
- Practitioner = choisir le bon mécanisme dans le bon contexte.

---

Original educational explanation based on the TOGAF Standard, 10th Edition.