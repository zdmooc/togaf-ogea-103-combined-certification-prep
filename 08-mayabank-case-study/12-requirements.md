# MayaBank — Requirements Management Across the ADM

## 1. Purpose

Requirements Management est le fil transversal du cas MayaBank. Les exigences ne sont pas collectées une fois au début puis oubliées : elles sont identifiées, précisées, validées, tracées, modifiées et parfois supprimées tout au long de l’ADM.

## 2. Requirement categories

MayaBank organise les requirements en catégories :

- business ;
- data ;
- application ;
- technology ;
- security ;
- compliance ;
- operational ;
- migration ;
- governance.

## 3. Initial requirements from Phase A

Exemples :

- continuité des paiements ;
- meilleure traçabilité ;
- capacité de migration incrémentale ;
- sécurité intégrée ;
- réduction du délai de traitement.

À ce stade, plusieurs formulations restent volontairement de haut niveau.

## 4. Requirements refined in Phase B

Exemples :

- standardiser la gestion des exceptions ;
- fournir un statut de paiement cohérent ;
- clarifier les responsabilités ;
- automatiser certains contrôles ;
- disposer d’un service de tracking temps réel.

## 5. Requirements refined in Phase C Data

- Payment ID unique ;
- ownership explicite ;
- lifecycle documenté ;
- règles de rétention ;
- lineage ;
- qualité ;
- chiffrement ;
- auditabilité des changements de statut.

## 6. Requirements refined in Phase C Application

- services aux responsabilités claires ;
- APIs versionnées ;
- events gouvernés ;
- correlation ID ;
- idempotence ;
- coexistence avec legacy ;
- contrat d’erreur standardisé.

## 7. Requirements refined in Phase D

- availability ;
- latency ;
- scalability ;
- RTO/RPO ;
- secrets management ;
- network controls ;
- observability ;
- deployment automation ;
- disaster recovery.

## 8. Migration requirements in E/F

- migration sans big bang ;
- capacité de fallback pendant les étapes critiques ;
- critères de passage entre waves ;
- réconciliation entre ancien et nouveau traitement ;
- non-régression métier ;
- limitation du nombre de changements simultanés.

## 9. Governance requirements in G

- compliance evidence ;
- respect des standards ;
- exceptions documentées ;
- reviews à des gates convenus ;
- Architecture Contract ;
- traceability des décisions.

## 10. Change requirements in H

- critères de déclenchement d’un nouveau cycle ;
- surveillance des drivers ;
- revue des standards devenus obsolètes ;
- réévaluation des requirements après changement réglementaire ou stratégique.

## 11. Example requirements register

| ID | Requirement | Source | Priority | Status |
|---|---|---|---|---|
| R-001 | Payment continuity during migration | Sponsor/Ops | Must | Approved |
| R-002 | End-to-end transaction traceability | Compliance | Must | Approved |
| R-003 | Governed API contracts | Architecture | Must | Approved |
| R-004 | Explicit data ownership | Data Governance | Must | Approved |
| R-005 | Automated deployment evidence | Operations/Governance | Should | Planned |
| R-006 | Incremental migration with fallback | Risk | Must | Approved |

## 12. Traceability example

`R-002 End-to-end traceability` est reliée à :

- Business concern : auditabilité ;
- Data artifact : Audit Event model ;
- Application building block : Tracking/Audit Service ;
- Technology building block : logging/tracing platform ;
- Governance control : compliance evidence.

Cette trace montre pourquoi une requirement n’appartient pas à une seule phase.

## 13. Requirement conflict example

Operations demande une rétention longue des données de diagnostic.

Data Privacy demande une minimisation et une rétention limitée.

La bonne réponse n’est pas de choisir arbitrairement l’un des deux. L’équipe doit :

1. identifier le conflit ;
2. clarifier les obligations ;
3. évaluer alternatives ;
4. décider au bon niveau ;
5. mettre à jour requirements et architecture ;
6. tracer la décision.

## 14. Change control

Chaque modification significative d’une requirement doit conserver :

- source ;
- justification ;
- impact ;
- owner ;
- décision ;
- version ;
- liens vers artifacts/building blocks concernés.

## 15. Practitioner trap

Si le scénario présente une nouvelle exigence qui impacte plusieurs phases, la bonne action est rarement de la traiter uniquement dans la phase courante. Il faut la **gérer via Requirements Management**, analyser ses impacts puis retourner vers les travaux ADM nécessaires.

## 16. English for Architects

> Requirements Management is continuous across the ADM. MayaBank traces each important requirement from stakeholder concern to architecture decisions, building blocks, implementation controls, and change management.

---

Original educational case study; MayaBank is fictional.