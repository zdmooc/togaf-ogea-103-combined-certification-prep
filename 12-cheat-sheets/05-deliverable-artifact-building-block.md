# Cheat Sheet — Deliverable vs Artifact vs Building Block

## La chaîne à retenir

```text
Deliverable
   contient / regroupe
      ↓
Artifacts
   représentent
      ↓
Building Blocks
```

## Deliverable

Un **Deliverable** est un produit de travail formel, généralement revu, approuvé ou remis à des stakeholders.

Exemples pédagogiques :

- Architecture Definition Document
- Architecture Requirements Specification
- Architecture Roadmap

Le deliverable est le **paquet de travail formel**.

## Artifact

Un **Artifact** est une représentation d’architecture.

Trois grandes formes à mémoriser :

- **Catalog** : liste structurée d’éléments.
- **Matrix** : relations entre catégories d’éléments.
- **Diagram** : représentation visuelle.

Exemples :

- Application Portfolio Catalog
- Data Entity / Business Function Matrix
- Application Communication Diagram

## Building Block

Un **Building Block** est un élément architectural réutilisable décrivant une capacité, un composant ou un ensemble cohérent de fonctionnalités.

Il peut être abstrait ou plus concret selon qu’il s’agit d’un ABB ou d’un SBB.

## Exemple MayaBank

- Deliverable : Architecture Definition Document du programme Payment Modernization.
- Artifact : diagramme des services applicatifs de paiement.
- Building Block : Payment Validation Service.

Le diagramme **représente** le building block ; il n’est pas lui-même le composant architectural.

## Pièges Foundation

### « Lequel est une représentation ? »
→ **Artifact**.

### « Lequel est un produit de travail formel remis/revu ? »
→ **Deliverable**.

### « Lequel décrit une capacité ou composant réutilisable ? »
→ **Building Block**.

## Ne pas confondre

- Artifact ≠ fichier au sens informatique uniquement.
- Deliverable ≠ diagramme unique.
- Building Block ≠ dessin qui le représente.
- Catalog/Matrix/Diagram sont des formes d’**artifacts**.

## Question flash

Un document d’architecture contient une matrice montrant quels services utilisent quelles données.

- le document formel = **Deliverable** ;
- la matrice = **Artifact** ;
- les services et éléments architecturaux représentés = **Building Blocks / éléments du metamodel** selon le cas.

## English

> Deliverables package formal architecture work. Artifacts represent architecture content. Building blocks describe reusable architectural capabilities or components.
