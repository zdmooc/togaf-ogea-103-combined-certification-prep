# Building Blocks

## 1. Définition

Un **Building Block** est un élément potentiellement réutilisable qui représente une capacité, un composant ou un ensemble cohérent de fonctions nécessaires à l’architecture.

Les building blocks permettent de décomposer une architecture complexe en éléments plus simples à comprendre, comparer, réutiliser et gouverner.

## 2. Pourquoi utiliser des Building Blocks

Ils permettent :

- modularité ;
- réutilisation ;
- standardisation ;
- séparation entre besoin architectural et solution concrète ;
- traçabilité ;
- gestion progressive du niveau de détail.

## 3. Architecture Building Block

Un **Architecture Building Block (ABB)** décrit généralement une capacité ou un besoin architectural à un niveau logique.

Exemples :

- Identity Service ;
- Event Streaming Capability ;
- Payment Validation Service ;
- Observability Capability.

## 4. Solution Building Block

Un **Solution Building Block (SBB)** décrit un élément de solution plus concret qui peut réaliser un ABB.

Exemple :

ABB : `Enterprise Event Streaming Service`

SBB possibles :

- une plateforme Kafka managée ;
- une distribution Kafka on-premise ;
- une autre solution répondant aux exigences.

## 5. Building Block Specification

Un building block utile ne doit pas être seulement un nom. Il peut être caractérisé par :

- responsabilités ;
- interfaces ;
- exigences ;
- contraintes ;
- dépendances ;
- niveau de service ;
- standards applicables.

## 6. Granularité

Un building block peut exister à plusieurs niveaux. La bonne granularité dépend du scope et du niveau d’architecture.

Trop gros : difficile à réutiliser.
Trop fin : repository illisible.

## 7. Relation avec ADM

Les ABB émergent pendant le développement des architectures B/C/D.

En Phase E, on cherche comment les réaliser par des solutions et work packages. Les SBB deviennent alors particulièrement pertinents.

## 8. Exemple MayaBank

Target Architecture :

- ABB `Payment Orchestration Service` ;
- ABB `Fraud Screening Service` ;
- ABB `Event Streaming Service` ;
- ABB `Observability Service`.

En solution, MayaBank peut sélectionner des SBB concrets : produits, plateformes ou composants implémentables.

## 9. Building Block vs Artifact

`Event Streaming Service` = building block.

Le diagramme montrant ses connexions = artifact.

Le document formel contenant ce diagramme = deliverable.

## 10. Pièges OGEA-103

- Building block ≠ diagramme.
- ABB ≠ produit concret par définition.
- SBB réalise ou supporte plus concrètement le besoin exprimé par ABB.
- La frontière ABB/SBB dépend du niveau d’abstraction.

## 11. Foundation question

Quel concept représente un élément constitutif réutilisable de l’architecture ?

A. Building Block
B. Concern
C. Architecture Contract
D. Business Scenario

**Réponse : A.**

## 12. Practitioner scenario

Une équipe sélectionne immédiatement un produit avant d’avoir défini la capacité attendue. La meilleure approche consiste à clarifier d’abord l’ABB et ses exigences, puis à évaluer les SBB capables de le réaliser.

## 13. English for Architects

> Architecture Building Blocks describe the required architecture capability, while Solution Building Blocks describe more concrete realizations.

## 14. Key points

- Building blocks décomposent l’architecture.
- ABB = plus logique / architectural.
- SBB = plus concret / solution.
- Ils sont représentés par des artifacts mais ne sont pas eux-mêmes des artifacts.

---

Original educational explanation based on the TOGAF Standard, 10th Edition.