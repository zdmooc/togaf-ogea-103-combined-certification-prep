# MayaBank — Phase E: Opportunities & Solutions

## 1. Objective

Phase E transforme les gaps Business, Data, Application et Technology en **initiatives de transformation cohérentes**. C’est ici que MayaBank commence à organiser la trajectoire : work packages, dépendances, Transition Architectures et première Architecture Roadmap consolidée.

## 2. Inputs from B/C/D

Les gaps majeurs sont :

- orchestration métier fragmentée ;
- gestion des exceptions trop manuelle ;
- données et statuts non harmonisés ;
- services applicatifs dupliqués ;
- intégrations point-à-point ;
- plateforme hétérogène ;
- observabilité et sécurité non homogènes.

## 3. Work packages

MayaBank regroupe les changements en work packages :

### WP1 — Platform Foundation

- plateforme conteneurisée ;
- CI/CD ;
- GitOps ;
- secrets ;
- observability de base ;
- réseau et sécurité.

### WP2 — Payment Canonical Model

- identifiants ;
- statuts ;
- ownership ;
- contrats de données ;
- règles de qualité.

### WP3 — API & Event Integration Foundation

- API governance ;
- event contracts ;
- adapters legacy ;
- standards d’intégration.

### WP4 — Payment Orchestration

- Payment Intake ;
- Validation ;
- Orchestration ;
- Tracking.

### WP5 — Risk & Exception Modernization

- screening intégré ;
- exception management ;
- audit trail.

### WP6 — Legacy Rationalization

- retrait ou simplification progressive des composants remplacés.

## 4. Dependency map

Dépendances simplifiées :

- WP4 dépend fortement de WP1, WP2 et WP3 ;
- WP5 dépend de WP2 et WP3 ;
- WP6 dépend de la stabilisation de WP4/WP5 ;
- l’observabilité doit commencer dès WP1, pas à la fin.

## 5. Transition Architecture 1

### Plateau T1 — Foundation + coexistence

- plateforme cible disponible ;
- anciens services toujours actifs ;
- adapters entre legacy et nouvelle plateforme ;
- modèle de données commun introduit progressivement ;
- premières APIs gouvernées.

Cette transition produit une valeur limitée mais réduit le risque des étapes suivantes.

## 6. Transition Architecture 2

### Plateau T2 — Hybrid Payment Processing

- nouveaux paiements passent par la nouvelle orchestration pour un sous-périmètre ;
- certains contrôles legacy restent utilisés ;
- tracking et observability sont centralisés ;
- exception management commence à être mutualisé.

## 7. Target state

### Plateau T3 — Target

- orchestration généralisée ;
- données et contrats gouvernés ;
- composants legacy non nécessaires retirés ;
- run model standardisé ;
- conformité et observabilité intégrées.

## 8. Solution concept

MayaBank distingue :

- **architecture target** : capacités et building blocks nécessaires ;
- **solution implementation** : produits, configurations, équipes et lots de delivery.

Phase E commence à relier ces deux mondes sans transformer l’architecture en planning projet détaillé.

## 9. Initial Architecture Roadmap

Ordre indicatif :

1. Platform Foundation ;
2. Canonical Data Model ;
3. Integration Foundation ;
4. Pilot Orchestration ;
5. Risk/Exception Integration ;
6. Extend Payment Scope ;
7. Retire Legacy Components.

## 10. Benefits and risks

Chaque work package est évalué sur :

- valeur ;
- coût ;
- risque ;
- dépendances ;
- readiness ;
- capacité des équipes ;
- contribution aux gaps.

## 11. Phase E vs F

**Phase E** : construit les work packages, Transition Architectures et la logique de solution/roadmap.

**Phase F** : priorise, séquence et transforme cette matière en **Implementation and Migration Plan** plus précis.

## 12. Practitioner trap

Si les gaps sont connus et la question porte sur « comment les regrouper en initiatives et définir des états de transition », la meilleure réponse est Phase E, pas Phase F.

## 13. English for Architects

> In Phase E, MayaBank consolidates architecture gaps into work packages and transition architectures, creating the first coherent transformation roadmap.

---

Original educational case study; MayaBank is fictional.