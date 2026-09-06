# Deliverables

## 1. Définition

Un **Deliverable** est un produit de travail formel, contractuellement spécifié ou officiellement revu, destiné à une partie prenante.

Un deliverable peut contenir plusieurs artifacts et peut être versionné, approuvé et gouverné.

Exemples fréquemment rencontrés :

- Architecture Vision ;
- Architecture Definition Document ;
- Architecture Requirements Specification ;
- Architecture Roadmap ;
- Implementation and Migration Plan ;
- Architecture Contract.

## 2. Deliverable vs Artifact

Un deliverable est le **package formel**.
Un artifact est une **représentation** utilisée dans ou avec ce package.

Exemple :

`Architecture Definition Document` = deliverable.

À l’intérieur :

- Application Portfolio Catalog ;
- Data Entity/Application Matrix ;
- Technology Platform Diagram.

Ces trois éléments sont des artifacts.

## 3. Pourquoi les deliverables existent

Ils servent à :

- communiquer ;
- obtenir approbation ;
- contractualiser le travail ;
- établir une baseline ;
- soutenir governance ;
- conserver evidence ;
- transférer une architecture vers d’autres équipes.

## 4. Deliverable ≠ document Word

Un deliverable est défini par sa fonction dans le travail d’architecture, pas par son format technique.

Il peut être matérialisé dans :

- un document ;
- un repository ;
- une page collaborative ;
- plusieurs vues assemblées ;
- un workflow d’approbation.

Dans un environnement Agile, le contenu peut être géré de façon incrémentale tout en conservant la notion de produit formel gouverné.

## 5. Versioning

Une architecture évolue. Les deliverables peuvent donc exister sous plusieurs états :

- draft ;
- reviewed ;
- approved ;
- superseded ;
- archived.

La gouvernance doit permettre de savoir quelle version fait autorité.

## 6. Exemple MayaBank

Le programme Instant Payments produit :

### Architecture Vision

Vision de haut niveau approuvée en Phase A.

### Architecture Definition Document

Contient Baseline/Target Business, Data, Application et Technology Architectures.

### Architecture Requirements Specification

Regroupe les exigences d’architecture traçables.

### Architecture Roadmap

Présente les work packages et transitions principales.

## 7. Deliverables et ADM

Les deliverables sont créés et enrichis au fil du cycle. Ils ne sont pas nécessairement « écrits une fois à la fin d’une phase ».

L’ADM est itératif : un deliverable peut évoluer lorsque de nouvelles informations apparaissent.

## 8. Pièges OGEA-103

- Deliverable ≠ artifact.
- Deliverable ≠ building block.
- Deliverable ≠ forcément un fichier bureautique.
- Architecture Definition Document et Architecture Requirements Specification sont différents : description de l’architecture vs exigences auxquelles elle doit répondre.

## 9. Foundation question

Lequel est le meilleur exemple de deliverable ?

A. Application Communication Diagram
B. Data Entity Catalog
C. Architecture Definition Document
D. Application Component

**Réponse : C.**

## 10. Practitioner scenario

Une équipe possède des diagrammes de qualité mais personne ne sait quelle architecture a été approuvée. Le problème n’est pas le manque d’artifacts ; il faut rétablir le deliverable gouverné, son statut, sa version et son approbation.

## 11. English for Architects

> A deliverable is a formal architecture work product that may contain multiple artifacts and is typically subject to review and approval.

## 12. Key points

- Deliverable = produit formel.
- Il peut contenir plusieurs artifacts.
- Son format n’est pas limité à un document.
- Version et statut sont importants pour governance.

---

Original educational explanation based on the TOGAF Standard, 10th Edition.