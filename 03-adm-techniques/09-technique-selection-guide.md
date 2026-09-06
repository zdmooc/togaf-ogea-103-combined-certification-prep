# ADM Technique Selection Guide

## 1. Purpose

Ce chapitre sert de **carte de sélection**. L’objectif n’est pas de mémoriser une liste de techniques isolées, mais de savoir reconnaître **quel problème architectural appelle quelle technique**.

La logique à retenir :

**Problem → ADM context → Technique → Output / Decision**.

## 2. Quick map

| Problème | Technique principale |
|---|---|
| Comprendre qui compte et ce qui les préoccupe | Stakeholder Management |
| Clarifier un besoin métier réel | Business Scenarios |
| Comparer existant et cible | Gap Analysis |
| Faire coopérer systèmes/organisations | Interoperability Analysis |
| Vérifier que l’entreprise peut absorber la transformation | Business Transformation Readiness |
| Identifier et traiter l’incertitude | Risk Management |
| Planifier par capacités métier | Capability-Based Planning |
| Prioriser et séquencer les transformations | Migration Planning Techniques |

## 3. Mapping par phase ADM

### Preliminary

Techniques utiles :

- stakeholder identification ;
- maturity/readiness thinking ;
- risk identification ;
- capability thinking.

Objectif : préparer une capacité d’architecture adaptée au contexte.

### Phase A

Techniques dominantes :

- Stakeholder Management ;
- Business Scenarios ;
- Risk Management ;
- capability framing.

Questions typiques :

- pourquoi faisons-nous ce travail ?
- qui doit être engagé ?
- quelles préoccupations ?
- quels outcomes ?
- quels risques initiaux ?

### Phase B

Techniques :

- Gap Analysis ;
- Capability-Based Planning ;
- stakeholder engagement ;
- Business Scenarios si besoin d’affiner le contexte métier.

### Phase C

Techniques :

- Gap Analysis ;
- Interoperability ;
- Risk Management ;
- stakeholder-specific views.

### Phase D

Techniques :

- Gap Analysis ;
- Interoperability ;
- Risk Management ;
- security/risk integration.

### Phase E

Techniques :

- gap consolidation ;
- capability thinking ;
- readiness assessment ;
- risk analysis ;
- dependency analysis.

### Phase F

Techniques :

- business value assessment ;
- risk assessment ;
- cost/benefit ;
- dependency analysis ;
- prioritization ;
- readiness assessment.

### Phase G

Techniques :

- risk monitoring ;
- compliance checks ;
- stakeholder engagement ;
- interoperability verification.

### Phase H

Techniques :

- stakeholder monitoring ;
- risk review ;
- capability impact analysis ;
- change-trigger analysis.

## 4. Selection algorithm

Pour une question Practitioner, utiliser cette méthode :

### Step 1 — Identifier la phase

Demander : où en est l’entreprise dans l’ADM ?

### Step 2 — Identifier le problème

Exemples :

- manque d’adhésion ;
- besoin mal défini ;
- écart existant/cible ;
- dépendance entre systèmes ;
- organisation non prête ;
- risque majeur ;
- roadmap non priorisée.

### Step 3 — Éliminer les techniques hors sujet

Une technique peut être utile en général mais mauvaise dans le contexte immédiat.

### Step 4 — Choisir la technique qui produit l’information nécessaire à la prochaine décision

C’est souvent ce qui distingue la réponse 5 points d’une réponse seulement plausible.

## 5. Common confusions

### Stakeholder Management vs Business Scenarios

Stakeholder Management : qui et quels concerns ?

Business Scenario : quel problème métier, quels acteurs, quel outcome et quelles exigences ?

### Gap Analysis vs Readiness

Gap Analysis : différence entre architectures Baseline et Target.

Readiness : capacité organisationnelle à exécuter la transformation.

### Risk Management vs Readiness

Readiness peut révéler des risques ; Risk Management traite l’incertitude de manière plus large.

### Capability-Based Planning vs Migration Planning

Capability-Based Planning : organiser la transformation autour des capacités nécessaires.

Migration Planning : prioriser et séquencer work packages/projets.

### Interoperability vs Integration

Integration : connexion/mécanisme.

Interoperability : capacité complète à fonctionner ensemble.

## 6. Practitioner mini-scenarios

### Scenario A — Sponsor et Ops en conflit

Problème : préoccupations non alignées.

Technique dominante : **Stakeholder Management**.

### Scenario B — « Nous voulons Kafka » sans besoin clair

Problème : solution prématurée.

Technique : **Business Scenario**.

### Scenario C — Target validée mais changements inconnus

Problème : différences Baseline/Target.

Technique : **Gap Analysis**.

### Scenario D — Deux organisations échangent ISO 20022 mais interprètent différemment un statut

Problème : sémantique.

Technique : **Interoperability**.

### Scenario E — Cible OpenShift mais équipes non formées

Problème : capacité à transformer.

Technique : **Business Transformation Readiness**.

### Scenario F — Option rapide mais haut risque de panne

Technique : **Risk Management**.

### Scenario G — Portfolio organisé par outils sans lien métier

Technique : **Capability-Based Planning**.

### Scenario H — Work packages connus mais ordre contesté

Technique : **Migration Planning**.

## 7. Foundation memory map

```text
WHO / CONCERNS?        -> Stakeholder Management
WHAT BUSINESS NEED?    -> Business Scenario
WHAT CHANGES?          -> Gap Analysis
CAN THEY WORK TOGETHER?-> Interoperability
ARE WE READY?          -> Transformation Readiness
WHAT CAN GO WRONG?     -> Risk Management
WHAT MUST WE BE ABLE TO DO? -> Capability-Based Planning
IN WHAT ORDER?         -> Migration Planning
```

## 8. MayaBank end-to-end example

MayaBank veut moderniser son système de paiement.

1. **Stakeholder Management** identifie sponsor, CISO, operations, product, compliance.
2. **Business Scenario** clarifie le paiement instantané et les outcomes attendus.
3. B/C/D définissent Baseline et Target.
4. **Gap Analysis** identifie les changements nécessaires.
5. **Interoperability** traite ISO 20022, APIs, events, IAM et partenaires.
6. **Readiness Assessment** révèle les gaps de compétences et de run.
7. **Risk Management** traite migration, résilience et sécurité.
8. **Capability-Based Planning** organise la cible autour de Payment Orchestration, Event Streaming, Observability.
9. **Migration Planning** priorise les work packages.

Cette séquence montre pourquoi les techniques se complètent.

## 9. Exam traps

- Une technique n’est pas une phase ADM.
- Une technique correcte peut être utilisée au mauvais moment.
- La réponse Practitioner la plus complète respecte la séquence ADM.
- « Faire plus d’analyse » n’est pas toujours la bonne réponse : il faut produire l’information nécessaire à la décision courante.
- Les techniques doivent rester proportionnées au contexte.

## 10. English for Architects

> I select the technique based on the architecture problem and the decision we need to make next.

### Speak it

1. We used stakeholder management to understand the concerns.
2. We used gap analysis to identify what must change.
3. We used migration planning to sequence the work packages.

## 11. Final checklist

Avant de choisir une technique, demande :

- Quelle phase ?
- Quel problème ?
- Quel stakeholder ?
- Quelle décision doit venir ensuite ?
- Quelle information manque ?
- Quelle technique produit cette information ?

---

Original educational content aligned with TOGAF ADM technique concepts.