# Practitioner — Phase H Scenarios

## 1. Objectif Practitioner

La **Phase H — Architecture Change Management** intervient lorsque l’architecture existe et doit être surveillée, maintenue et éventuellement faire l’objet d’un nouveau cycle de transformation.

Le Practitioner doit savoir distinguer :

- un changement mineur traité dans la gouvernance courante ;
- une évolution qui nécessite une modification d’architecture ;
- un changement majeur qui justifie un nouveau cycle ADM.

## 2. Signal typique : nouveau driver

### Scénario

Après la mise en œuvre de la plateforme MayaBank, une nouvelle réglementation impose des contrôles supplémentaires sur les paiements.

La bonne lecture est Phase H : évaluer l’impact du changement, déterminer sa nature et décider de l’action architecturale appropriée.

## 3. Signal typique : technologie obsolète

Un composant critique arrive en fin de support.

Ce n’est pas automatiquement “Phase D”. Il faut d’abord déterminer, via Change Management, si le changement reste local ou modifie suffisamment l’architecture pour déclencher un nouveau cycle.

## 4. Signal typique : business strategy change

MayaBank acquiert une fintech et veut intégrer ses services au modèle cible.

Si l’impact est important sur les capabilities, applications, data et technology, la meilleure réponse peut être de déclencher un nouveau travail d’architecture plutôt que de traiter cela comme simple maintenance.

## 5. H vs G

### Phase G

Question dominante : l’implémentation actuelle respecte-t-elle l’architecture approuvée ?

### Phase H

Question dominante : l’architecture elle-même doit-elle évoluer face à de nouveaux drivers ou changements ?

## 6. H vs Requirements Management

Requirements Management gère les exigences à travers tout l’ADM.

Phase H surveille et gouverne les changements d’architecture dans le temps.

Une nouvelle requirement peut être un signal qui déclenche une analyse en H.

## 7. Change request

Une change request doit être évaluée selon :

- impact ;
- scope ;
- valeur ;
- risque ;
- conformité ;
- coût ;
- dépendances ;
- degré de modification de la cible.

## 8. Scénario MayaBank — petite évolution

Une équipe demande d’ajouter un nouveau dashboard sans modifier les principes, les interfaces majeures ni la cible.

Cela peut être traité comme une évolution gouvernée sans nouveau cycle complet.

## 9. Scénario MayaBank — changement majeur

Une nouvelle réglementation impose une refonte de la gestion d’identité et modifie plusieurs domaines.

La meilleure action est probablement d’évaluer l’impact en H puis de déclencher un nouveau cycle ADM avec un scope adapté.

## 10. Pièges Practitioner

- tout changement ≠ nouveau cycle complet ;
- tout problème d’implémentation ≠ Phase H ;
- une déviation en cours de delivery relève d’abord souvent de G ;
- un nouveau driver stratégique peut nécessiter H puis un nouveau cycle ;
- H n’est pas de la simple maintenance technique.

## 11. Questions d’élimination

Élimine souvent une option si elle :

- traite une déviation d’implémentation comme une refonte stratégique ;
- ignore l’analyse d’impact ;
- déclenche toujours un cycle complet sans proportionnalité ;
- suppose que l’architecture est figée après livraison.

## 12. English for Architects

> In Phase H, I assess changes to the enterprise environment and determine whether the existing architecture can absorb them or whether a new ADM cycle is required.

---

Original educational scenarios.