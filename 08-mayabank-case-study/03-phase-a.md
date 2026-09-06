# MayaBank — Phase A: Architecture Vision

## 1. Purpose

Phase A transforme la demande initiale en **engagement d’architecture cadré et approuvé**. MayaBank doit aligner sponsor et stakeholders sur le problème, le scope, la valeur, les contraintes et une vision cible de haut niveau.

## 2. Scope

Le scope retenu couvre le domaine paiements européens, l’orchestration, la validation, le screening fraude/risque, la gestion des exceptions, les interfaces clearing/settlement, les données opérationnelles et la plateforme technique associée.

Hors scope : core banking complet, CRM, crédit et remplacement global de la comptabilité.

## 3. Stakeholder map

| Stakeholder | Concern |
|---|---|
| Sponsor Payments | valeur, délai, risque |
| Operations | continuité, supportabilité |
| CISO | sécurité, secrets, identité |
| Compliance | auditabilité, réglementation |
| Product | time-to-market |
| Finance | coût et séquencement |
| Delivery | faisabilité et dépendances |
| Data Governance | qualité et ownership |

## 4. Business drivers refined

Les drivers sont reformulés en objectifs mesurables à préciser pendant le cycle :

- réduire les délais de traitement ;
- augmenter la disponibilité ;
- réduire les opérations manuelles ;
- améliorer la traçabilité ;
- accélérer l’intégration de nouveaux services ;
- simplifier le run ;
- réduire la duplication de composants.

## 5. High-level Baseline

La Baseline montre :

- chaînes de paiement multiples ;
- forte dépendance à des traitements batch ;
- middleware historique ;
- intégrations point-à-point ;
- données dupliquées ;
- monitoring fragmenté ;
- changements coûteux et lents.

## 6. High-level Target

La Target Vision prévoit :

- orchestration de paiement unifiée ;
- APIs et événements gouvernés ;
- traitements temps réel pour les cas critiques ;
- plateforme conteneurisée ;
- sécurité et observabilité intégrées ;
- gouvernance des données ;
- delivery automatisé ;
- coexistence temporaire avec le legacy.

## 7. Value proposition

La valeur attendue ne se résume pas à une modernisation technique. Elle porte sur :

- rapidité de traitement ;
- résilience ;
- réduction du coût d’exploitation ;
- réduction du risque opérationnel ;
- meilleure capacité d’évolution ;
- meilleure conformité.

## 8. Risks identified early

- migration trop rapide ;
- dépendance à une technologie mal maîtrisée ;
- sous-estimation des données ;
- manque de compétences cloud-native ;
- surcharge du programme ;
- fragmentation des décisions ;
- absence d’ownership sur certains services.

## 9. Architecture Vision

La vision est synthétisée ainsi :

> MayaBank évolue vers une plateforme de paiement modulaire, gouvernée, observable et résiliente, permettant des traitements temps réel et une migration incrémentale depuis les systèmes existants.

Cette formulation n’est volontairement pas une architecture détaillée.

## 10. Statement of Architecture Work

Le Statement of Architecture Work précise notamment :

- objectifs ;
- scope ;
- stakeholders ;
- approche et tailoring ;
- principaux deliverables ;
- gouvernance ;
- hypothèses ;
- risques ;
- calendrier de travail d’architecture ;
- critères d’acceptation.

## 11. Initial requirements

Exemples :

- continuité de paiement ;
- traçabilité des transactions ;
- chiffrement des données sensibles ;
- support d’interfaces standardisées ;
- observabilité de bout en bout ;
- capacité de migration par étapes.

Ces requirements seront affinées pendant B/C/D.

## 12. Decision gate

Le sponsor et l’Architecture Board approuvent :

- le scope ;
- la vision ;
- la valeur attendue ;
- le Statement of Architecture Work ;
- la poursuite vers les architectures détaillées.

## 13. Phase A vs Phase B

Phase A donne une vision et un accord de haut niveau. Phase B ne doit pas refaire la Vision ; elle développe la **Business Architecture** nécessaire pour atteindre les objectifs approuvés.

## 14. Practitioner scenario

Si le sponsor demande « prouvez-moi la valeur avant d’investir dans les modèles détaillés », la bonne réponse est typiquement Phase A : clarifier business drivers, stakeholders, scope, valeur et Architecture Vision, pas commencer par un choix de plateforme.

## 15. English for Architects

> Phase A aligns MayaBank stakeholders on the scope, business value, high-level target, risks, and the Statement of Architecture Work.

---

Original educational case study; MayaBank is fictional.