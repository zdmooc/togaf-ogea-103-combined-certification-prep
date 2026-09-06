# Practitioner — Architecture Development Scenarios (Phases B, C, D)

## 1. Objectif Practitioner

Les phases B, C et D développent la cible détaillée par domaine. Le piège principal consiste à choisir la bonne phase et le bon niveau de décision.

- **B** = Business Architecture
- **C Data** = Data Architecture
- **C Application** = Application Architecture
- **D** = Technology Architecture

La logique reste : **Baseline → Target → Gap**.

## 2. Phase B — reconnaître le problème métier

### Scénario

MayaBank veut réduire le délai de traitement, mais les responsabilités entre front-office, contrôle et back-office sont incohérentes.

La meilleure action est de travailler la **Business Architecture** : capabilities, processes, services, roles, ownership et gaps.

Erreur classique : commencer par sélectionner une application.

## 3. Phase C Data — reconnaître le problème d’information

### Scénario

Plusieurs systèmes ont des définitions différentes du statut d’un paiement. Les équipes ne savent pas quelle source fait foi.

Le problème dominant relève de **Data Architecture** : information entities, ownership, quality, lifecycle, exchange, authoritative sources.

## 4. Phase C Application — reconnaître le problème de services applicatifs

### Scénario

Le métier a défini les capacités cibles et les données nécessaires. Il faut maintenant déterminer quels services applicatifs fournissent validation, orchestration, screening et exception management.

Le problème relève de **Application Architecture**.

## 5. Phase D — reconnaître le problème technologique

### Scénario

Les services applicatifs cibles sont définis. L’équipe doit décider des plateformes, middleware, compute, network, storage et runtime nécessaires.

Le problème relève de **Technology Architecture**.

## 6. Pattern : technologie prématurée

Si le scénario indique que les besoins métier, data ou application ne sont pas encore compris, une réponse qui sélectionne immédiatement Kubernetes, Kafka, Oracle ou un cloud est souvent moins bonne.

## 7. Pattern : gap mal interprété

Un gap identifié en B/C/D n’est pas encore un work package séquencé.

B/C/D répondent d’abord :

- qu’avons-nous aujourd’hui ?
- que voulons-nous demain ?
- quels écarts existent ?

E/F traiteront la transformation.

## 8. Pattern : niveau de détail excessif

Le Practitioner doit adapter la profondeur au besoin.

Documenter chaque table, API ou pod n’est pas automatiquement meilleur.

## 9. Pattern : dépendance entre domaines

Exemple :

- Business gap : automatiser exceptions
- Data implication : état et motif d’exception normalisés
- Application implication : service d’exception management
- Technology implication : runtime, messaging, observability

Le meilleur raisonnement relie les domaines au lieu de les traiter comme silos.

## 10. Scénario gradué pédagogique

### Situation

MayaBank veut une nouvelle capacité d’orchestration. Le métier est défini mais les données de paiement sont incohérentes et aucun modèle d’information partagé n’existe.

### Meilleure réponse

Développer la Data Architecture cible, identifier les gaps d’information et mettre à jour les requirements avant de figer les services applicatifs dépendants.

### Réponse plausible mais moins bonne

Choisir directement une plateforme de streaming.

Pourquoi ? Elle peut être pertinente plus tard, mais elle ne résout pas encore le problème d’information.

## 11. B vs C vs D — tableau décisionnel

| Question dominante | Phase |
|---|---|
| Comment le métier doit fonctionner ? | B |
| Quelles informations/données sont nécessaires ? | C Data |
| Quels services/applications soutiennent le métier ? | C App |
| Quelle infrastructure/plateforme soutient les applications ? | D |

## 12. Pièges Practitioner

- Capability ≠ application
- information need ≠ database product
- application service ≠ technology platform
- gap ≠ work package
- target architecture ≠ migration plan
- technologie raisonnable ≠ bonne réponse si elle arrive trop tôt

## 13. English for Architects

> In Phases B, C, and D, I develop the domain architectures, compare baseline and target states, and identify gaps that will later drive the transformation roadmap.

---

Original educational scenarios. No exam dump content.