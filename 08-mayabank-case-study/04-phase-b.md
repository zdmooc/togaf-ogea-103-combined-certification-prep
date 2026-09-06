# MayaBank — Phase B: Business Architecture

## 1. Objective

Phase B traduit la vision de paiement moderne en **capacités métier, processus, rôles et services métier**. Le but est de comprendre ce que MayaBank doit être capable de faire avant de décider comment les applications et technologies le supporteront.

## 2. Baseline Business Architecture

Constats principaux :

- chaînes de paiement organisées par produits et historiques techniques ;
- nombreux contrôles manuels ;
- gestion d’exception fragmentée ;
- responsabilités réparties entre plusieurs équipes ;
- visibilité temps réel limitée ;
- duplication de contrôles ;
- dépendance forte à des traitements différés.

## 3. Current capabilities

Capacités existantes :

- Payment Initiation ;
- Payment Validation ;
- Fraud Screening ;
- Clearing Integration ;
- Settlement Reconciliation ;
- Exception Handling ;
- Customer Notification ;
- Operational Monitoring.

Le problème n’est pas nécessairement l’absence de capacité, mais parfois son niveau de maturité ou sa fragmentation.

## 4. Target capabilities

MayaBank cible :

- **Real-Time Payment Orchestration** ;
- **Unified Validation** ;
- **Centralized Fraud/Risk Screening** ;
- **Exception Management** standardisé ;
- **Real-Time Operational Monitoring** ;
- **Payment Status Tracking** ;
- **Configuration and Rule Management** gouverné ;
- **Audit and Traceability** de bout en bout.

## 5. Capability gaps

| Capability | Baseline | Target | Gap |
|---|---|---|---|
| Orchestration | dispersée | unifiée | majeur |
| Validation | dupliquée | standardisée | moyen/majeur |
| Exception Management | manuel/fragmenté | orchestré | majeur |
| Monitoring | local | end-to-end | majeur |
| Auditability | partielle | traçabilité complète | majeur |
| Rule Management | dispersé | gouverné | moyen |

## 6. Value streams

Value stream simplifié :

**Initiate Payment → Validate → Screen → Route/Orchestrate → Clear/Settle → Confirm → Monitor/Resolve**.

Cette vue montre où la valeur est produite et où se trouvent les frictions.

## 7. Target business services

Services métier cibles :

- Payment Acceptance Service ;
- Payment Validation Service ;
- Risk Screening Service ;
- Payment Orchestration Service ;
- Exception Resolution Service ;
- Payment Tracking Service ;
- Settlement Reconciliation Service.

## 8. Actors and roles

Rôles clarifiés :

- Product Owner Payments ;
- Payment Operations Analyst ;
- Risk Analyst ;
- Compliance Officer ;
- Platform Operations ;
- Service Owner ;
- Data Owner.

La cible introduit notamment un **Service Owner** explicite pour les services structurants.

## 9. Process improvements

Exemples :

- automatiser certains contrôles ;
- standardiser la gestion des erreurs ;
- réduire les ressaisies ;
- rendre la décision de routage explicite ;
- exposer un statut de paiement commun ;
- centraliser la logique de certains contrôles partagés.

## 10. Requirements generated

Phase B produit ou affine :

- temps maximal de traitement pour certaines étapes ;
- disponibilité métier attendue ;
- obligation de traçabilité ;
- gestion standardisée des exceptions ;
- séparation de responsabilités ;
- exigences de suivi du statut ;
- règles d’escalade opérationnelle.

## 11. Impacts on other domains

### Data

Besoin de modèle commun pour Payment, Party, Account Reference, Payment Status, Risk Decision, Exception.

### Application

Besoin de services applicatifs correspondant aux capacités cibles.

### Technology

Besoin d’une plateforme capable de supporter disponibilité, intégration et observabilité.

## 12. Building blocks perspective

Exemples d’ABB métier :

- Payment Orchestration Capability ;
- Risk Screening Capability ;
- Exception Management Capability ;
- Payment Tracking Capability.

Ils ne sont pas encore des produits ou composants précis.

## 13. Gap Analysis outcome

Les gaps métier les plus structurants sont :

1. orchestration insuffisante ;
2. exception management trop manuel ;
3. observabilité métier insuffisante ;
4. duplication des règles ;
5. responsabilités mal alignées.

Ces gaps alimenteront Phase E pour la construction des work packages.

## 14. Practitioner trap

Si une réponse propose « installer Kafka pour résoudre le manque d’orchestration », elle saute du **business gap** directement à une solution technique. Le bon raisonnement commence par la capability et les services métier attendus, puis laisse C/D préciser le support SI.

## 15. English for Architects

> Phase B identifies the business capabilities MayaBank must strengthen, including payment orchestration, exception management, tracking, and operational visibility.

---

Original educational case study; MayaBank is fictional.