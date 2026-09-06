# MayaBank — Phase C: Data Architecture

## 1. Objective

La Data Architecture de MayaBank définit comment les informations nécessaires aux paiements sont structurées, gouvernées, échangées, sécurisées, conservées et tracées.

Le point clé : **Data Architecture ≠ choix de base de données**.

## 2. Baseline

Problèmes identifiés :

- plusieurs représentations du Payment ;
- statuts différents selon les applications ;
- ownership incomplet ;
- duplication de données ;
- règles de rétention hétérogènes ;
- qualité variable ;
- lineage incomplet ;
- rapprochements difficiles entre systèmes.

## 3. Core data entities

Entités principales :

- Payment ;
- Payment Instruction ;
- Party ;
- Account Reference ;
- Payment Status ;
- Risk Decision ;
- Exception ;
- Settlement Position ;
- Audit Event.

## 4. Target information model

MayaBank définit un modèle conceptuel partagé pour que les équipes parlent le même langage.

Exemple de relations :

- un Payment possède une Payment Instruction ;
- un Payment traverse plusieurs Payment Status ;
- un Payment peut produire une Risk Decision ;
- un Payment peut générer une Exception ;
- un Audit Event documente les décisions et transitions significatives.

## 5. Data ownership

| Data domain | Owner |
|---|---|
| Payment | Payments Business Owner |
| Risk Decision | Risk Domain Owner |
| Exception | Operations Owner |
| Audit Event | Compliance / Platform Governance |
| Settlement Position | Finance/Settlement Owner |

Le Data Owner n’est pas nécessairement l’équipe qui héberge physiquement les données.

## 6. Data quality requirements

Exemples :

- Payment ID unique et stable ;
- timestamps cohérents ;
- statuts contrôlés ;
- champs réglementaires obligatoires validés ;
- traçabilité des transformations ;
- règles de duplication explicites.

## 7. Data lifecycle

MayaBank documente :

**create → validate → enrich → process → store → archive → delete**.

Pour chaque étape :

- owner ;
- sensibilité ;
- rétention ;
- source of truth ;
- consommateurs ;
- exigences d’audit.

## 8. Data movement

Les échanges de données sont classés :

- API synchrone ;
- événement asynchrone ;
- fichier partenaire ;
- réplication contrôlée ;
- reporting/analytics.

L’architecture privilégie des contrats explicites plutôt que des couplages implicites aux schémas internes.

## 9. Security and privacy

Requirements :

- chiffrement en transit et au repos ;
- minimisation des données ;
- accès selon least privilege ;
- audit des accès sensibles ;
- protection des secrets et identifiants ;
- rétention compatible avec exigences légales et métier.

## 10. Baseline → Target → Gap

| Sujet | Baseline | Target | Gap |
|---|---|---|---|
| modèle Payment | multiple | partagé/gouverné | majeur |
| ownership | partiel | explicite | majeur |
| lineage | incomplet | traçable | majeur |
| qualité | locale | règles communes | moyen |
| statuts | hétérogènes | modèle commun | majeur |
| rétention | dispersée | gouvernée | moyen |

## 11. Data artifacts

Artifacts utiles :

- Data Entity Catalog ;
- Data Lifecycle Diagram ;
- Data Dissemination Diagram ;
- Data Security View ;
- Data Ownership Matrix ;
- logical data model.

## 12. Requirements produced

- canonical identifiers ;
- data ownership ;
- data lineage ;
- retention ;
- encryption ;
- data quality thresholds ;
- consistency rules ;
- auditability.

## 13. Impact on Application Architecture

La cible Application devra respecter :

- les contrats de données ;
- les owners ;
- les modèles de statut ;
- les contraintes de cycle de vie ;
- les exigences de sécurité.

## 14. Practitioner trap

Un scénario demandant qui doit résoudre l’incohérence des statuts et l’absence d’ownership pointe d’abord vers **Data Architecture**, pas vers Phase D ni vers un choix de produit database.

## 15. English for Architects

> MayaBank defines shared payment data concepts, explicit ownership, lifecycle rules, quality controls, and end-to-end traceability before selecting physical data technologies.

---

Original educational case study; MayaBank is fictional.