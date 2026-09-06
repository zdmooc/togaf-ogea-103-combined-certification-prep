# OGEA-102 Part 2 — Big Picture

## 1. Ce que mesure réellement l’examen Practitioner

La certification **TOGAF Enterprise Architecture Practitioner** ne demande pas seulement de connaître les définitions. Elle vérifie que tu sais **appliquer** et **analyser** le TOGAF Standard dans une situation réaliste.

Le changement mental est simple :

**Foundation = “Qu’est-ce que TOGAF dit ?”**  
**Practitioner = “Quelle est la meilleure action TOGAF dans ce contexte précis ?”**

Une réponse peut être techniquement raisonnable et pourtant être moins bonne qu’une autre si elle :

- intervient trop tôt dans l’ADM ;
- ignore un stakeholder important ;
- traite un symptôme au lieu d’un besoin métier ;
- court-circuite Requirements Management ;
- confond architecture et gestion de projet ;
- contourne la gouvernance ;
- choisit une solution avant d’avoir défini la cible ;
- produit trop de détail par rapport au besoin.

## 2. Format officiel actuel

L’OGEA-102 comporte :

- 8 questions scénarisées ;
- 90 minutes ;
- 4 réponses possibles par question ;
- une seule réponse à sélectionner ;
- scoring gradué 5 / 3 / 1 / 0 ;
- seuil de réussite 60 %, soit 24 points sur 40 ;
- accès open book intégré.

Le but n’est pas de deviner la note de chaque option. Il faut choisir la **meilleure** réponse.

## 3. Huit grandes zones officielles

1. The Context for Enterprise Architecture
2. Stakeholder Management
3. Phase A: The Starting Point
4. Architecture Development — Phases B, C, D
5. Implementing the Architecture — Phases E, F, G
6. Architecture Change Management — Phase H
7. Requirements Management
8. Supporting the ADM Work

Un scénario peut mélanger plusieurs zones.

## 4. La méthode de lecture d’un scénario

Pour chaque question, lis dans cet ordre :

### Étape 1 — Identifier le moment ADM

Demande-toi :

- Sommes-nous avant le lancement du cycle ?
- En Phase A ?
- En train de développer une architecture de domaine ?
- En train de préparer la migration ?
- En cours d’implémentation ?
- Après la mise en œuvre ?

### Étape 2 — Identifier le problème dominant

Exemples :

- stakeholder non engagé ;
- scope mal défini ;
- exigences conflictuelles ;
- cible métier non définie ;
- gaps connus mais pas de séquencement ;
- solution déviante ;
- changement majeur après livraison.

### Étape 3 — Identifier le niveau de décision

La question porte-t-elle sur :

- une décision d’architecture ?
- une exigence ?
- un work package ?
- une gouvernance ?
- un changement ?
- une communication stakeholder ?

### Étape 4 — Éliminer les réponses hors séquence

Exemple : si la Business Architecture n’est pas encore comprise, sélectionner immédiatement une technologie est souvent trop tôt.

### Étape 5 — Choisir la réponse la plus TOGAF

Le meilleur choix est souvent celui qui :

- respecte le cycle ;
- utilise les bons stakeholders ;
- maintient la traçabilité ;
- adapte le niveau de détail ;
- utilise les mécanismes de gouvernance ;
- conserve la cohérence avec les objectifs métier.

## 5. Les trois types de mauvaises réponses

### Mauvaise mais séduisante

Exemple : “déployer immédiatement un POC Kafka”.

La réponse peut sembler efficace, mais elle saute peut-être plusieurs étapes nécessaires.

### Partiellement correcte

Elle traite une partie du problème, mais pas la cause principale.

### Correcte mais moins appropriée

Elle peut mériter 3 points : raisonnable, mais moins complète ou moins alignée avec TOGAF que la meilleure réponse.

## 6. Le principe du “best TOGAF answer”

Le Practitioner n’est pas un concours de technologie.

Face à plusieurs réponses plausibles, préfère celle qui maximise :

**context + stakeholder alignment + requirements traceability + governance + ADM sequencing + business value**.

## 7. Exemple MayaBank

### Scénario

MayaBank a décidé de moderniser ses paiements. Le CTO veut immédiatement choisir une plateforme cible. Le sponsor métier n’a pas encore validé les outcomes attendus et les équipes opérations n’ont pas été consultées.

### Analyse

- Moment : début du cycle.
- Problème : vision et stakeholders insuffisamment cadrés.
- Réponse faible : choisir tout de suite les produits.
- Réponse meilleure : clarifier scope, stakeholders, concerns, business outcomes et Architecture Vision avant de figer la solution.

## 8. Ce que signifie “analyze”

Analyser signifie notamment :

- comparer plusieurs actions possibles ;
- comprendre les conséquences ;
- reconnaître les dépendances ;
- hiérarchiser les préoccupations ;
- distinguer problème d’architecture et problème projet ;
- relier une décision au bon mécanisme TOGAF.

## 9. Ce que signifie “apply”

Appliquer signifie utiliser un concept TOGAF pour agir :

- Stakeholder Management ;
- Gap Analysis ;
- Architecture Contract ;
- Compliance Review ;
- Business Scenario ;
- Requirements Management ;
- Transition Architecture ;
- Architecture Roadmap.

## 10. Gestion du temps

90 minutes pour 8 questions donne environ 11 minutes par question.

Approche recommandée :

1. lire le scénario ;
2. identifier la phase/contexte ;
3. classer les réponses ;
4. consulter la référence uniquement pour confirmer un point précis ;
5. sélectionner et avancer.

L’open book ne doit pas remplacer la compréhension.

## 11. Erreurs fréquentes

- rechercher chaque réponse dans le PDF ;
- choisir la réponse la plus technique ;
- ignorer le mot “best” ;
- confondre phase et technique ;
- traiter une exigence comme une solution ;
- prendre une déviation pour un changement d’architecture ;
- oublier que l’ADM est tailorable et iterative.

## 12. English for Architects

> In Part 2, I first identify the architecture context, the ADM stage, the key stakeholders, and the main decision that needs to be made.

> I then eliminate answers that are premature, incomplete, or inconsistent with TOGAF governance and requirements management.

## 13. Checklist avant chaque réponse

- Où suis-je dans l’ADM ?
- Quel stakeholder est concerné ?
- Quel concern domine ?
- Quelle requirement ou décision doit être gérée ?
- Quel mécanisme TOGAF correspond au problème ?
- Quelle option respecte le mieux la séquence et la gouvernance ?

---

Official baseline: The Open Group OGEA-102 exam plan and TOGAF Standard, 10th Edition. This chapter contains original educational scenarios only; it does not reproduce exam content.