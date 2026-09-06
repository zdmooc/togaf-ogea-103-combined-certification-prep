# MayaBank — Phase F: Migration Planning

## 1. Objective

Phase F transforme la roadmap de haut niveau en **Implementation and Migration Plan** priorisé, séquencé et cohérent avec les contraintes de MayaBank.

La question devient :

**dans quel ordre exécuter les work packages pour maximiser la valeur et maîtriser le risque ?**

## 2. Prioritization criteria

MayaBank utilise plusieurs critères :

- business value ;
- regulatory urgency ;
- risk reduction ;
- technical dependency ;
- cost ;
- organizational readiness ;
- delivery capacity ;
- reversibility ;
- impact on business continuity.

## 3. Work package ranking

| Work Package | Value | Risk Reduction | Dependency Criticality | Priority |
|---|---:|---:|---:|---:|
| WP1 Platform Foundation | haute | haute | très haute | 1 |
| WP2 Canonical Data Model | haute | haute | très haute | 1 |
| WP3 Integration Foundation | haute | haute | très haute | 1 |
| WP4 Payment Orchestration | très haute | haute | haute | 2 |
| WP5 Risk & Exception | haute | haute | moyenne | 2 |
| WP6 Legacy Rationalization | moyenne/haute | haute | dépend des autres | 3 |

Les priorités ne sont pas uniquement financières. Certaines fondations doivent être réalisées tôt car elles dé-risquent tout le programme.

## 4. Migration waves

### Wave 1 — Foundations

- plateforme cible ;
- observability minimum ;
- secrets et sécurité ;
- modèle de données canonique ;
- règles API/event.

### Wave 2 — Pilot

- sous-périmètre paiement ;
- orchestration moderne ;
- tracking ;
- adapters legacy ;
- tests de résilience et runbooks.

### Wave 3 — Scale

- extension à d’autres flux ;
- intégration risk/exception ;
- montée en charge ;
- automatisation accrue.

### Wave 4 — Rationalize

- retrait des composants legacy devenus inutiles ;
- simplification des intégrations ;
- optimisation coût/run.

## 5. Dependencies

Exemples :

- l’orchestration ne doit pas précéder les contrats de données et d’intégration ;
- le pilote ne doit pas être généralisé avant preuve de résilience ;
- la suppression legacy ne doit pas précéder la stabilité fonctionnelle et opérationnelle de la cible.

## 6. Migration risk management

Risques et réponses :

| Risk | Mitigation |
|---|---|
| perte de continuité | coexistence + fallback |
| surcharge équipes | vagues limitées + capacité réservée |
| divergence data | contrats + reconciliation |
| manque compétences | formation + pairing |
| observability insuffisante | telemetry comme prérequis |
| dépendance fournisseur | ADR + exit/portability assessment |

## 7. Business value increments

Chaque wave doit produire une valeur observable :

- Wave 1 : réduction du risque technique ;
- Wave 2 : preuve de valeur sur un flux réel ;
- Wave 3 : bénéfices à plus grande échelle ;
- Wave 4 : baisse du coût et de la complexité.

## 8. Implementation and Migration Plan

Le plan consolide :

- work packages ;
- séquence ;
- dépendances ;
- jalons ;
- ressources ;
- risques ;
- coûts ;
- critères de passage ;
- gouvernance.

Il est plus détaillé et orienté exécution que l’Architecture Roadmap.

## 9. Architecture Roadmap vs Implementation and Migration Plan

| Architecture Roadmap | Implementation & Migration Plan |
|---|---|
| trajectoire architecturale | plan d’exécution détaillé |
| montre changements et transitions | montre séquence, dépendances, ressources et priorités |
| commence à émerger avant F | consolidé en F |

## 10. Go/No-Go criteria

Exemples pour passage Wave 2 → Wave 3 :

- SLO atteints ;
- incidents majeurs résolus ;
- audit trail conforme ;
- runbooks testés ;
- performance validée ;
- architecture compliance acceptable ;
- sponsor confirme la valeur.

## 11. Practitioner trap

Si les work packages et transitions sont déjà connus mais que le scénario demande de les **prioriser et séquencer** selon valeur, coût, dépendances et risque, on est en Phase F.

## 12. English for Architects

> Phase F prioritizes and sequences MayaBank work packages into an implementation and migration plan based on value, dependencies, readiness, and risk.

---

Original educational case study; MayaBank is fictional.