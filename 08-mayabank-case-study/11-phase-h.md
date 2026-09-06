# MayaBank — Phase H: Architecture Change Management

## 1. Objective

Phase H organise la surveillance et l’évolution de l’architecture après sa mise en œuvre. L’objectif n’est pas de conserver la Target Architecture figée, mais de déterminer **quand un changement doit être absorbé, gouverné localement ou déclencher un nouveau cycle ADM**.

## 2. Change drivers at MayaBank

Exemples :

- nouvelle réglementation ;
- nouveau scheme de paiement ;
- changement de volume ;
- évolution de cyber-menace ;
- obsolescence d’un composant ;
- nouveau partenaire ;
- acquisition d’une filiale ;
- coût de plateforme trop élevé ;
- changement de stratégie produit.

## 3. Architecture monitoring

MayaBank surveille :

- business KPIs ;
- SLO/SLA ;
- incidents ;
- exceptions d’architecture ;
- coûts ;
- capacité ;
- security findings ;
- dette technique ;
- évolutions réglementaires ;
- changements de stratégie.

## 4. Change classification

Les changements sont classés selon leur impact.

### Minor change

Exemple : ajustement de capacité sans modifier les principes ou l’architecture cible.

→ gouvernance locale contrôlée.

### Incremental architectural change

Exemple : ajout d’un nouveau service de tracking dans les patterns existants.

→ architecture work ciblé, potentiellement itératif.

### Major strategic change

Exemple : acquisition d’une banque avec une plateforme de paiement différente ou nouvelle réglementation transformant profondément le modèle.

→ nouveau Request for Architecture Work et nouveau cycle ADM significatif.

## 5. Change request example

Un nouveau scheme européen exige un traitement avec de nouveaux statuts, délais et données.

Analyse :

- impact Business Capability ;
- impact Data Model ;
- nouveaux Application Services ;
- contraintes Technology ;
- impacts security/compliance ;
- impact roadmap et operating model.

Ce changement dépasse une simple correction locale : MayaBank déclenche un nouvel architecture work.

## 6. Architecture Landscape maintenance

Après la migration, MayaBank met à jour le Landscape pour refléter :

- building blocks actifs ;
- composants legacy encore présents ;
- Transition Architectures franchies ;
- Target partiellement ou totalement atteinte ;
- standards et exceptions actuels.

Une architecture non maintenue devient rapidement une documentation historique inutile.

## 7. Governance relationship

Phase H utilise les mécanismes établis en Preliminary :

- Architecture Board ;
- Repository ;
- principles ;
- governance log ;
- exception process.

Elle ne recrée pas une gouvernance différente à chaque changement.

## 8. Requirements relationship

Un nouveau driver peut :

- créer une requirement ;
- modifier une requirement ;
- rendre une requirement obsolète ;
- créer un conflit ;
- nécessiter un nouveau scope.

Requirements Management reste donc actif.

## 9. H vs Requirements Management

**Phase H** décide comment répondre aux changements de l’environnement et de l’architecture.

**Requirements Management** gère le cycle de vie des exigences à travers toutes les phases.

## 10. H vs G

| Phase G | Phase H |
|---|---|
| implémentation en cours | architecture en évolution |
| conformité aux décisions approuvées | besoin de nouvelles décisions |
| exceptions de delivery | nouveaux drivers/changements |
| Architecture Contract | change assessment |

## 11. Practitioner trap

Un incident pendant une implémentation non conforme relève souvent de G. Une nouvelle réglementation qui remet en cause la cible relève de H et peut déclencher un nouveau cycle.

## 12. English for Architects

> Phase H monitors business and technology change, assesses architecture impact, and determines whether MayaBank needs a local adjustment or a new ADM cycle.

---

Original educational case study; MayaBank is fictional.