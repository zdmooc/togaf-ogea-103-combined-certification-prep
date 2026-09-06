# Architecture Contract

## 1. Définition

Un **Architecture Contract** formalise les responsabilités, engagements et attentes liés à la réalisation d’une architecture.

Il sert de mécanisme de gouvernance entre les parties qui définissent l’architecture et celles qui la mettent en œuvre ou la fournissent.

Il ne faut pas le réduire à un contrat commercial. Dans TOGAF, le concept sert surtout à rendre explicites :

- ce qui doit être respecté ;
- qui est responsable ;
- comment la conformité sera évaluée ;
- comment les écarts seront gérés.

## 2. Pourquoi l’utiliser

Une architecture peut être approuvée mais mal interprétée par le delivery. Le contrat crée un lien explicite entre **architecture intent** et **implementation responsibility**.

## 3. Contenu possible

Selon le contexte :

- scope ;
- principes applicables ;
- architecture requirements ;
- standards ;
- building blocks attendus ;
- responsabilités ;
- critères de conformité ;
- review points ;
- processus de changement ;
- gestion des exceptions ;
- obligations de reporting.

## 4. Formes possibles

Le mécanisme peut être utilisé entre :

- architecture function et business stakeholders ;
- architecture function et implementation organization ;
- customer et supplier ;
- plusieurs équipes collaborant sur une transformation.

La forme exacte dépend du modèle de gouvernance.

## 5. Relation avec Phase G

Phase G — Implementation Governance est l’endroit où l’Architecture Contract prend une importance particulière.

Le raisonnement est :

**Target Architecture → Architecture Requirements → Architecture Contract → Implementation → Compliance Review**.

## 6. Contract vs Statement of Architecture Work

| Statement of Architecture Work | Architecture Contract |
|---|---|
| cadre le travail d’architecture | cadre les engagements liés à la réalisation / gouvernance |
| fortement associé à Phase A | particulièrement utile en Phase G |
| scope, approach, work plan | obligations, conformité, responsabilités |

## 7. Exemple MayaBank

Pour la plateforme de paiement, l’Architecture Contract peut préciser que :

- les API doivent respecter les standards de sécurité groupe ;
- l’observabilité doit être disponible avant production ;
- les données sensibles doivent être chiffrées ;
- toute déviation doit être soumise à review ;
- les équipes delivery fournissent les preuves de conformité.

## 8. Pièges OGEA-103

- Architecture Contract ≠ Architecture Vision.
- Architecture Contract ≠ simple contrat fournisseur.
- Il soutient la gouvernance de l’implémentation.
- Il ne remplace pas les Architecture Requirements.

## 9. Foundation question

Quel mécanisme formalise des engagements de gouvernance entre architecture et mise en œuvre ?

A. Architecture Contract
B. Capability Map
C. Business Scenario
D. Architecture Vision

**Réponse : A.**

## 10. Practitioner scenario

Une équipe affirme qu’elle n’avait pas compris quels standards étaient obligatoires. La réponse TOGAF la plus robuste est de renforcer le mécanisme qui formalise attentes, responsabilités et conformité, plutôt que d’ajouter seulement un nouveau diagramme.

## 11. English for Architects

> The Architecture Contract makes implementation responsibilities and compliance expectations explicit.

## 12. Key points

- Contract = engagement + responsabilité + conformité.
- Il relie architecture et implementation.
- Il est particulièrement pertinent en Phase G.
- Il doit être adapté au mode de gouvernance réel.

---

Original educational explanation based on the TOGAF Standard, 10th Edition.