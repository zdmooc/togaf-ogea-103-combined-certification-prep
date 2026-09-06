# Content Metamodel

## 1. Définition

Le **Content Metamodel** définit les types d’éléments que l’organisation souhaite gérer dans son architecture et les relations autorisées ou utiles entre ces éléments.

Il apporte une grammaire au contenu architectural.

Sans metamodel, les diagrammes peuvent être visuellement lisibles mais sémantiquement incohérents.

## 2. Exemple simple

Une organisation peut décider de gérer :

- Business Capability ;
- Business Service ;
- Data Entity ;
- Application Component ;
- Application Service ;
- Technology Service ;
- Technology Component ;
- Requirement ;
- Principle ;
- Stakeholder.

Puis définir des relations telles que :

- Capability **is supported by** Business Service ;
- Business Service **uses** Application Service ;
- Application Component **realizes** Application Service ;
- Application **accesses** Data Entity ;
- Application **is hosted on** Technology Component.

## 3. Pourquoi le metamodel est utile

Il facilite :

- cohérence ;
- traçabilité ;
- impact analysis ;
- repository management ;
- réutilisation ;
- génération de vues ;
- contrôle de qualité.

## 4. Core et extensions

Une organisation ne doit pas forcément gérer tous les concepts possibles. Le metamodel peut être adapté selon :

- taille ;
- secteur ;
- gouvernance ;
- besoins de sécurité ;
- maturité ;
- outils ;
- niveau de détail requis.

Exemple : une banque peut étendre le modèle avec Control, Regulatory Requirement, Data Classification ou Criticality.

## 5. Metamodel vs Modeling Language

Un metamodel décrit **quels concepts et relations** sont utilisés.

Un langage comme ArchiMate fournit une notation et une sémantique de modélisation plus formelles.

TOGAF et ArchiMate sont complémentaires, mais il ne faut pas les confondre.

## 6. Metamodel vs Repository

- Content Metamodel = structure logique des types de contenu.
- Architecture Repository = lieu / dispositif de gestion des contenus et autres assets.

## 7. Exemple MayaBank

MayaBank veut pouvoir répondre à :

« Quelles applications supportent la capability Instant Payment et quelles technologies hébergent ces applications ? »

Le metamodel doit permettre la chaîne de traçabilité :

**Capability → Business Service → Application Service → Application Component → Technology Service / Component**.

## 8. Impact analysis

Si `Kafka Platform` change, le repository peut retrouver :

- applications dépendantes ;
- services concernés ;
- capabilities impactées ;
- owners ;
- requirements associés.

Cette puissance vient des relations structurées, pas du nombre de diagrammes.

## 9. Pièges OGEA-103

- Metamodel ≠ repository.
- Metamodel ≠ diagramme.
- Metamodel ≠ ADM.
- Il peut être tailored.
- Son intérêt principal est la cohérence des types et relations.

## 10. Foundation question

Quel concept définit les types d’entités architecturales et leurs relations ?

A. Content Metamodel
B. Architecture Contract
C. Migration Plan
D. Architecture Board

**Réponse : A.**

## 11. Practitioner scenario

Trois équipes utilisent le terme « service » pour trois choses différentes. Les analyses d’impact deviennent impossibles. Une réponse robuste consiste à normaliser le content metamodel et les définitions avant d’augmenter la quantité de documentation.

## 12. English for Architects

> The content metamodel defines the architecture concepts we manage and the relationships between them.

## 13. Key points

- Metamodel = types + relations.
- Il soutient traçabilité et impact analysis.
- Il est adaptable au contexte.
- Il structure le repository mais n’est pas le repository.

---

Original educational explanation based on the TOGAF Standard, 10th Edition.