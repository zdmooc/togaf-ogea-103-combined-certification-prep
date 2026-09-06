# Cheat Sheet — Architecture Repository vs Enterprise Continuum

## La différence en une phrase

- **Architecture Repository** : organise et conserve les assets d’architecture.
- **Enterprise Continuum** : aide à **classer et contextualiser** ces assets du générique vers le spécifique.

## Repository — penser « où et comment j’organise »

Le Repository permet de retrouver notamment :

- metamodel ;
- architecture capability ;
- architecture landscape ;
- standards ;
- reference library ;
- governance log ;
- architectures, patterns, décisions, roadmaps.

## Enterprise Continuum — penser « comment je positionne »

Le Continuum aide à raisonner sur le degré de généricité/spécificité d’un asset et sur sa réutilisation.

Exemple pédagogique :

```text
Generic / Foundation
       ↓
Common Systems
       ↓
Industry
       ↓
Organization-Specific
```

L’objectif n’est pas d’apprendre une arborescence comme un stockage physique, mais de comprendre la logique de **classification et contextualisation**.

## Exemple MayaBank

MayaBank dispose d’un pattern générique de gestion d’événements, d’une référence sectorielle paiement, puis d’une architecture spécifique au programme Payment Modernization.

- Le **Repository** conserve ces assets.
- Le **Continuum** aide à comprendre leur position et leur degré de spécialisation.

## Pièges Foundation

- Repository ≠ Continuum.
- Le Continuum n’est pas simplement un dossier ou une base de données.
- Le Repository ne remplace pas l’ADM.
- La réutilisation ne signifie pas copier sans adaptation.

## Practitioner

Avant de repartir de zéro, vérifier les assets existants, leur pertinence et leur niveau de généralité. La meilleure réponse est souvent **reuse + adapt**, pas **reuse blindly** ni **ignore everything**.

## Mémo

> **Repository stores/organizes. Continuum classifies/contextualizes.**

## English

> The Architecture Repository organizes architecture assets. The Enterprise Continuum helps classify and contextualize those assets from generic to organization-specific.
