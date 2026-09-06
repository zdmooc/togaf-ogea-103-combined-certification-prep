# MayaBank — Phase C: Application Architecture

## 1. Objective

La Application Architecture définit les services applicatifs, responsabilités et interactions nécessaires pour supporter les capacités métier et la Data Architecture cible.

Elle répond à :

- quelles applications ou services sont nécessaires ?
- quelles responsabilités portent-ils ?
- comment interagissent-ils ?
- quelles fonctions doivent être partagées ou séparées ?

## 2. Baseline

Constats :

- plusieurs applications assurent des fonctions proches ;
- contrôles dupliqués ;
- dépendances point-à-point ;
- interfaces non homogènes ;
- logique métier enfouie dans des composants historiques ;
- faible autonomie des domaines ;
- monitoring applicatif fragmenté.

## 3. Target application services

Services applicatifs cibles :

- Payment Intake Service ;
- Validation Service ;
- Risk Screening Service ;
- Payment Orchestration Service ;
- Routing Service ;
- Exception Management Service ;
- Payment Tracking Service ;
- Settlement Adapter ;
- Notification Service ;
- Audit/Event Service.

## 4. Responsibility boundaries

### Payment Intake

- reçoit la demande ;
- vérifie le format ;
- crée l’identifiant initial ;
- transmet au workflow de validation.

### Validation

- applique les règles de complétude et cohérence ;
- ne décide pas du routage métier final.

### Risk Screening

- exécute contrôles fraude/risque ;
- produit une Risk Decision traçable.

### Orchestration

- coordonne le cycle ;
- ne doit pas absorber toute la logique des services spécialisés.

### Exception Management

- centralise les anomalies nécessitant traitement ou reprise.

## 5. Application interactions

Flux simplifié :

```text
Channel
  ↓
Payment Intake
  ↓
Validation
  ↓
Risk Screening
  ↓
Payment Orchestration
  ├─→ Routing / Clearing Adapter
  ├─→ Payment Tracking
  ├─→ Notification
  └─→ Exception Management
```

Les interactions doivent respecter les contrats Data définis précédemment.

## 6. API vs events

MayaBank utilise le principe :

- API synchrone quand une réponse immédiate est requise ;
- événement lorsque le découplage et la propagation asynchrone sont préférables.

Exemples :

- `POST /payments` pour initier ;
- événement `PaymentValidated` ;
- événement `RiskDecisionMade` ;
- événement `PaymentSettled` ;
- événement `PaymentExceptionRaised`.

Ces exemples sont des choix d’architecture du cas, pas des prescriptions TOGAF.

## 7. Baseline → Target → Gap

| Sujet | Baseline | Target | Gap |
|---|---|---|---|
| orchestration | dispersée | service dédié | majeur |
| interfaces | point-à-point | contrats gouvernés | majeur |
| validation | dupliquée | service partagé | moyen/majeur |
| tracking | local | service commun | majeur |
| exceptions | multiples | service structuré | majeur |
| audit | fragmenté | événements corrélables | majeur |

## 8. Application rationalization

Chaque application existante est classée :

- retain ;
- rehost ;
- replatform ;
- refactor ;
- replace ;
- retire.

Le classement ne doit pas être décidé uniquement sur l’âge technique : il dépend de la valeur, du risque, des dépendances et des capabilities supportées.

## 9. ABB perspective

ABB possibles :

- Payment Orchestration ABB ;
- Validation ABB ;
- Risk Screening ABB ;
- Tracking ABB ;
- Integration ABB ;
- Observability ABB.

Les SBB concrets seront précisés davantage avec les choix technologiques/solution.

## 10. Requirements

- APIs versionnées ;
- idempotence pour opérations critiques ;
- correlation ID de bout en bout ;
- séparation des responsabilités ;
- compatibilité avec coexistence legacy ;
- support des événements ;
- observabilité ;
- sécurité des communications.

## 11. Relation avec Phase D

Phase C Application définit **ce que le paysage applicatif doit fournir**.

Phase D définira **l’environnement technologique** qui permet d’exécuter ces services : compute, runtime, networking, messaging, secrets, observability, CI/CD, storage.

## 12. Transition concerns

La cible ne peut pas remplacer tout le legacy immédiatement. Des adapters et façades temporaires sont donc nécessaires pendant la migration.

Ils doivent être explicitement considérés comme des building blocks de transition, pas automatiquement comme la cible finale.

## 13. Practitioner trap

Un scénario décrivant des fonctions applicatives dupliquées, des services à rationaliser et des responsabilités à redistribuer pointe vers **Application Architecture**, même si plusieurs technologies sont mentionnées.

## 14. English for Architects

> MayaBank defines clear application service boundaries and governed interaction contracts before selecting the underlying technology platform.

---

Original educational case study; MayaBank is fictional.