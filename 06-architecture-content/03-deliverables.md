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

## 1 bis. Les 16 livrables explicitement nommés par X2202 Foundation 7.3

Le syllabus officiel **X2202 §3.1.7, objectif 7.3** demande de pouvoir décrire brièvement les livrables ci-dessous, produits et consommés à différents moments de l'ADM. **La phase indiquée n'est qu'un repère pédagogique** : les travaux peuvent débuter, être mis à jour ou consommés dans plusieurs phases et les cycles ADM sont itératifs.

| Livrable demandé par X2202 7.3 | Rôle de décision / contenu distinctif | Repère de phase |
|---|---|---|
| Architecture Contract | Formalise les engagements des parties réalisant et gouvernant l'architecture | F/G, gouvernance de réalisation |
| Architecture Definition Document | Décrit Baseline et Target Architectures, modèles et vues des domaines | B/C/D, évolue au fil de l'ADM |
| Architecture Principles | Règles de décision durables, justification et implications | Preliminary, réutilisé ensuite |
| Architecture Requirements Specification | Exigences d'architecture, contraintes et critères à satisfaire | A/B/C/D, affinée transversalement |
| Architecture Roadmap | États de transition et grands work packages menant vers la cible | A, enrichie en E/F |
| Architecture Vision | Direction, valeur métier, objectifs et périmètre de haut niveau | A |
| Business Principles, Business Goals, and Business Drivers | Fondements, objectifs et moteurs métier qui orientent les arbitrages | Preliminary/A, entrées métiers |
| Capability Assessment | Apprécie les capacités existantes ou nécessaires pour réaliser la transformation | Preliminary/A puis mise à jour |
| Change Request | Formalise une demande d'évolution de l'architecture approuvée | G/H et Requirements Management |
| Communications Plan | Prévoit qui informer, sur quels sujets, à quel moment et par quel canal | A, suit l'engagement |
| Compliance Assessment | Évalue la conformité d'une implémentation aux exigences et décisions approuvées | G |
| Implementation and Migration Plan | Détaille priorités, vagues, dépendances, ressources et séquencement | F |
| Implementation Governance Model | Définit les règles, instances et processus permettant de gouverner la réalisation | E/F, utilisé en G |
| Request for Architecture Work | Exprime et déclenche une demande métier de travail architectural | Entrée vers A |
| Requirements Impact Assessment | Analyse les conséquences d'une modification des exigences sur l'architecture et la trajectoire | Requirements Management, toutes phases |
| Statement of Architecture Work | Formalise le mandat de la mission d'architecture, scope, approche, contraintes et engagements | A |

**Ne pas confondre :** Request for Architecture Work = demande initiale ; Statement of Architecture Work = mandat convenu ; Architecture Vision = direction et valeur ; Architecture Definition Document = description structurée ; Architecture Requirements Specification = contraintes et critères ; Architecture Roadmap = trajectoire ; Implementation and Migration Plan = séquencement opérationnel ; Implementation Governance Model = mode de contrôle de la réalisation ; Architecture Contract = engagements ; Compliance Assessment = mesure de conformité ; Change Request = demande d'évolution ; Requirements Impact Assessment = analyse d'impact d'une requirement.

**Exercice ciblé :** `09-foundation-question-bank/11-x2202-deliverables-drills.md` (16 QCM couvrant les 16 livrables). Référence à relire : [X2202, §3.1.7, learning outcome 7.3](https://www.opengroup.org/library/x2202). La formulation des explications est originale et n'est pas une reproduction des questions officielles.


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