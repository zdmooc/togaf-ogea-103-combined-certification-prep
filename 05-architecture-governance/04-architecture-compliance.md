# Architecture Compliance Review

## 1. Définition

Une **Architecture Compliance Review** évalue si une implémentation, une solution ou un projet respecte l’architecture approuvée, les principes, standards et exigences applicables.

La review ne cherche pas uniquement à répondre « conforme / non conforme ». Elle sert à comprendre :

- quelles exigences sont satisfaites ;
- quels écarts existent ;
- pourquoi ils existent ;
- quel risque ils introduisent ;
- quelle décision de gouvernance est nécessaire.

## 2. Quand la review intervient

Elle est particulièrement importante pendant **Phase G — Implementation Governance**, mais des contrôles intermédiaires peuvent être organisés avant et pendant le delivery.

Attendre la mise en production pour découvrir une non-conformité coûte généralement beaucoup plus cher.

## 3. Sources de conformité

Une review peut s’appuyer sur :

- Architecture Principles ;
- Architecture Requirements Specification ;
- Target Architecture ;
- standards ;
- reference architectures ;
- Architecture Contract ;
- security requirements ;
- decisions et waivers existants.

## 4. Processus pratique

1. définir le scope de la review ;
2. identifier les exigences applicables ;
3. collecter les preuves ;
4. comparer implementation et architecture ;
5. classifier les écarts ;
6. évaluer risques et impacts ;
7. décider : acceptation, correction, exception ou escalade ;
8. tracer la décision.

## 5. Evidence

Une revue sérieuse s’appuie sur des preuves :

- diagrammes as-built ;
- configurations ;
- tests ;
- security evidence ;
- monitoring ;
- décisions ;
- documentation d’exploitation ;
- résultats de validation.

## 6. Compliance vs Quality Assurance

La conformité architecturale ne remplace pas les tests fonctionnels ou techniques.

Une solution peut fonctionner parfaitement et être non conforme à la Target Architecture ; inversement, une solution conforme architecturalement peut contenir des défauts logiciels.

## 7. Exemple MayaBank

Target : les services de paiement doivent être stateless lorsque possible, observables et déployés via pipeline automatisé.

Review :

- service A : conforme ;
- service B : logs non centralisés ;
- service C : déploiement manuel ;
- service D : stockage local non approuvé.

Chaque écart doit être analysé et traité selon son impact.

## 8. Pièges OGEA-103

- Review ≠ test de code.
- Review ≠ simple checklist documentaire.
- Non-conformité ≠ rejet automatique : une exception peut être gouvernée.
- La review doit s’appuyer sur une architecture et des exigences approuvées.

## 9. Foundation question

Quel est le but principal d’une Architecture Compliance Review ?

A. Écrire la Target Architecture
B. Vérifier l’alignement d’une implémentation avec l’architecture approuvée
C. Gérer le budget
D. Identifier les stakeholders de Phase A

**Réponse : B.**

## 10. Practitioner scenario

Un projet a dévié d’un standard mais démontre qu’une contrainte réglementaire rend l’option standard impossible. La meilleure réponse est d’évaluer formellement l’écart, le risque et la justification, puis d’utiliser le processus d’exception approprié.

## 11. English for Architects

> We perform architecture compliance reviews to verify that the implementation remains aligned with the approved architecture.

## 12. Key points

- Compliance = comparaison implementation vs architecture approuvée.
- Phase G est centrale.
- Les preuves sont indispensables.
- Un écart doit déclencher une décision, pas être ignoré.

---

Original educational explanation based on the TOGAF Standard, 10th Edition.