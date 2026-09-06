# Artifacts

## 1. Définition

Un **Artifact** est une représentation d’un aspect de l’architecture. Dans TOGAF, les artifacts sont généralement classés en trois grandes familles : **Catalogs, Matrices et Diagrams**.

Ils servent à rendre l’architecture compréhensible, analysable et communicable.

## 2. Artifact vs Deliverable

Un artifact peut faire partie d’un deliverable.

Exemple :

- Deliverable : Architecture Definition Document
- Artifact : Application Portfolio Catalog
- Artifact : Data Entity/Application Matrix
- Artifact : Technology Platform Diagram

## 3. Artifact vs Building Block

L’artifact **représente** ou décrit des éléments.
Le building block est un **élément de l’architecture**.

Exemple :

- `Payment API` = building block potentiel ;
- diagramme montrant Payment API et ses dépendances = artifact.

## 4. Catalogs

Un catalog est une liste structurée d’éléments homogènes.

Exemples :

- Application Portfolio Catalog ;
- Technology Portfolio Catalog ;
- Data Entity/Data Component Catalog ;
- Principle Catalog.

Question typique : **quels éléments existent ?**

## 5. Matrices

Une matrix met en relation deux ensembles d’éléments.

Exemples :

- Business Interaction Matrix ;
- Data Entity/Business Function Matrix ;
- Application/Organization Matrix ;
- Role/Application Matrix.

Question typique : **qui utilise quoi ? qui dépend de quoi ?**

## 6. Diagrams

Un diagram montre visuellement des structures, flux ou interactions.

Exemples :

- Business Footprint Diagram ;
- Application Communication Diagram ;
- Processing Diagram ;
- Environments and Locations Diagram.

Question typique : **comment ces éléments sont-ils organisés ou connectés ?**

## 7. Choisir un artifact

La sélection doit partir du concern et de la décision à prendre.

Ne pas commencer par « quel diagramme puis-je dessiner ? » mais par :

1. quel stakeholder ?
2. quel concern ?
3. quelle question ?
4. quel viewpoint / artifact répond le mieux ?

## 8. Exemple MayaBank

Question : « quelles applications manipulent les données de paiement ? »

Une **Data Entity/Application Matrix** répond mieux qu’un diagramme réseau.

Question : « comment les applications communiquent-elles ? »

Un **Application Communication Diagram** est plus adapté.

Question : « quelles applications existent dans le portefeuille ? »

Un **Application Portfolio Catalog** est plus direct.

## 9. Pièges OGEA-103

- Artifact ≠ deliverable.
- Artifact ≠ building block.
- Catalog, matrix et diagram ont des objectifs différents.
- Plus de diagrammes ≠ meilleure architecture.

## 10. Foundation question

Quel type d’artifact est le plus adapté pour représenter une relation entre deux ensembles d’éléments ?

A. Catalog
B. Matrix
C. Contract
D. Work Package

**Réponse : B.**

## 11. Practitioner scenario

Le CISO veut savoir quelles applications manipulent des données sensibles. La meilleure réponse est de sélectionner un artifact relationnel approprié plutôt qu’un diagramme générique conçu pour un autre stakeholder.

## 12. English for Architects

> We select architecture artifacts based on stakeholder concerns and the question the view needs to answer.

## 13. Key points

- Artifact = représentation.
- Trois familles : catalogs, matrices, diagrams.
- La sélection part du concern.
- Les artifacts peuvent être contenus dans des deliverables.

---

Original educational explanation based on the TOGAF Standard, 10th Edition.