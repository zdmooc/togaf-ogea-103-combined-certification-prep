# MayaBank — Phase B: Business Architecture

## 1. Objective

Phase B traduit la vision de paiement moderne en **capacités métier, processus, rôles et services métier**. Le but est de comprendre ce que MayaBank doit être capable de faire avant de décider comment les applications et technologies le supporteront.

## 2–10. Capacités, services, Value Streams et Gap Analysis — référentiel métier unique

Le cas didactique de **baseline/target payments** (Payment Initiation, Validation, Fraud, Tracking, Exceptions, Settlement, règles et RACI) est désormais centralisé dans la [matrice AS-IS / cible et écarts des capacités de paiement](https://github.com/zdmooc/banking-payments-business-architecture/blob/main/04-capacites-metier/ECARTS_CAPACITES_ASIS_CIBLE_PAIEMENTS.md).

Les **exemples de maturité** du cas MayaBank ne sont pas une photographie d'une banque réelle. Les objectifs métier, KPI et mesures doivent être validés sur le périmètre de mission. Ce chapitre TOGAF conserve la **méthode Phase B**, la transition vers les architectures Data/Application/Technology, les building blocks et le raisonnement de certification.

**Historique intégral des exercices de capacités et du tableau Gap Analysis** : [version antérieure 7aa87263](https://github.com/zdmooc/togaf-ogea-103-combined-certification-prep/blob/7aa87263e023c95aca9f5144bb9a28022f368bd3/08-mayabank-case-study/04-phase-b.md).

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