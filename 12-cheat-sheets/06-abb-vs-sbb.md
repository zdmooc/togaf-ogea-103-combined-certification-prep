# Cheat Sheet — ABB vs SBB

## Définition courte

- **ABB — Architecture Building Block** : décrit **ce qui est nécessaire** architecturalement, de façon relativement indépendante d’une implémentation précise.
- **SBB — Solution Building Block** : décrit **comment cette capacité est réalisée** dans une solution plus concrète.

## Exemple simple

### ABB

« Service d’authentification forte pour les paiements »

### SBB

« Implémentation de cette capacité via un fournisseur IAM précis, avec configuration, composants et intégrations définis »

## Tableau comparatif

| ABB | SBB |
|---|---|
| orientation architecture | orientation solution |
| exprime une capacité requise | exprime une réalisation concrète |
| moins lié à un produit précis | peut être lié à des technologies/produits précis |
| aide à définir la Target Architecture | aide à matérialiser la solution |

## Exemple MayaBank

### ABBs

- Payment Validation
- Fraud Screening
- Event Distribution
- Secrets Management
- Observability

### SBBs possibles

- une implémentation précise de broker/event streaming ;
- une solution IAM donnée ;
- une stack d’observabilité définie ;
- une base ou plateforme concrète.

Les noms de produits ne rendent pas automatiquement un objet « mauvais » ; ils indiquent surtout qu’on se rapproche du niveau **solution**.

## Pièges d’examen

- ABB ≠ artifact.
- SBB ≠ deliverable.
- ABB n’est pas « théorique inutile » : il permet de définir la capacité attendue sans verrouiller prématurément la solution.
- SBB ne signifie pas forcément code déjà déployé ; il décrit la réalisation de solution plus concrète.

## Réflexe

Question : « Que faut-il architecturalement ? » → penser **ABB**.

Question : « Avec quelle réalisation concrète ? » → penser **SBB**.

## Relation avec l’ADM

- B/C/D peuvent faire émerger ou préciser les ABBs de la cible.
- E et les travaux de solution peuvent faire évoluer le raisonnement vers des SBBs plus concrets.

## English

> An ABB describes the architectural capability required. An SBB describes a more concrete solution that realizes that capability.
