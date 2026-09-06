# Practitioner — Implementing the Architecture Scenarios (Phases E, F, G)

## 1. Objectif Practitioner

Les phases E, F et G sont souvent confondues parce qu’elles parlent toutes de transformation et mise en œuvre.

La distinction essentielle :

- **E — Opportunities & Solutions** : regrouper les changements en work packages, définir des Transition Architectures et construire la logique de transformation.
- **F — Migration Planning** : prioriser, séquencer, estimer et finaliser l’Implementation and Migration Plan.
- **G — Implementation Governance** : gouverner l’exécution et vérifier la conformité de l’implémentation à l’architecture.

## 2. Phase E — reconnaître les work packages

### Scénario

Les gaps B/C/D sont connus. MayaBank doit maintenant déterminer quels ensembles de changements permettent d’atteindre la cible.

La bonne réponse se situe en **Phase E** : identifier les work packages, dépendances, possible Transition Architectures et options de solution.

## 3. Transition Architecture

Une Transition Architecture est un état intermédiaire de l’architecture.

Exemple :

- Baseline : monolithe on-premise
- Transition 1 : APIs exposées mais cœur historique conservé
- Transition 2 : orchestration événementielle + coexistence
- Target : plateforme cible complète

Le piège Practitioner est de confondre cet état intermédiaire avec le plan qui explique quand et comment y arriver.

## 4. Phase F — reconnaître la priorisation

### Scénario

Les work packages sont identifiés, mais le budget impose un déploiement sur trois ans.

La meilleure action est de **prioriser et séquencer** selon valeur, coût, risque, dépendances et readiness, puis finaliser l’Implementation and Migration Plan.

## 5. Phase G — reconnaître la conformité d’implémentation

### Scénario

Une équipe de delivery remplace le mécanisme de chiffrement approuvé par une alternative plus rapide à intégrer.

Le problème relève de **Implementation Governance** : vérifier la conformité, documenter l’écart, décider s’il doit être corrigé ou traité via exception/change gouverné.

## 6. E vs F

| Question | Phase |
|---|---|
| Quels work packages ? | E |
| Quelles Transition Architectures ? | E |
| Dans quel ordre ? | F |
| Avec quelles priorités ? | F |
| Quel calendrier et plan de migration ? | F |

## 7. F vs G

| Question | Phase |
|---|---|
| Comment planifier la migration ? | F |
| Le delivery implémente-t-il conformément ? | G |
| Quel ordre de projets ? | F |
| Comment gérer une déviation d’implémentation ? | G |

## 8. Architecture Contract

En G, un Architecture Contract peut formaliser les engagements entre architecture et implementation organization.

Il aide à rendre explicites :

- responsibilities ;
- conformance expectations ;
- deliverables ;
- acceptance criteria ;
- governance checkpoints.

## 9. Compliance Review

Une Architecture Compliance Review permet de comparer l’implémentation aux attentes architecturales.

Elle ne doit pas être utilisée comme simple sanction tardive. Elle fait partie de la gouvernance.

## 10. Scénario MayaBank — E

Les gaps identifiés sont :

- absence d’orchestration ;
- données de paiement incohérentes ;
- monitoring insuffisant ;
- dépendance au legacy.

La meilleure action : regrouper ces gaps en work packages cohérents et identifier les Transition Architectures nécessaires.

## 11. Scénario MayaBank — F

Le programme a cinq work packages mais ne peut en financer que deux la première année.

La meilleure action : prioriser selon valeur, risque, dépendances, readiness et coût, puis finaliser le plan de migration.

## 12. Scénario MayaBank — G

Pendant l’implémentation, une équipe contourne le service IAM commun pour respecter une deadline.

La meilleure réponse n’est ni d’ignorer l’écart ni de stopper automatiquement le projet. Il faut l’évaluer via la gouvernance, vérifier la conformité, analyser le risque et prendre une décision formelle.

## 13. Pièges Practitioner

- Work Package ≠ Project forcément 1:1
- Transition Architecture ≠ Implementation Plan
- Phase E ≠ détailler le calendrier
- Phase F ≠ contrôler le code livré
- Phase G ≠ refaire l’architecture cible entière
- déviation ≠ automatiquement exception acceptée

## 14. English for Architects

> Phase E structures the transformation, Phase F prioritizes and sequences it, and Phase G governs implementation against the approved architecture.

---

Original educational scenarios based on TOGAF Practitioner concepts.