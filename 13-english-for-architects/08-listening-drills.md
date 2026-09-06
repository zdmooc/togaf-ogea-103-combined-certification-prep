# Listening Drills for Architects

## 1. Objectif

La compréhension orale en entretien vient rarement d’un manque de vocabulaire TOGAF. Le problème est souvent la vitesse, les accents, les mots faibles et les formulations indirectes.

Le but de ce chapitre est d’apprendre à reconnaître les **signaux de décision**.

## 2. Ce qu’il faut écouter en priorité

Dans une question longue, repérer :

- current state;
- target state;
- main issue;
- constraint;
- stakeholder;
- risk;
- timeline;
- decision required.

Ne pas chercher à comprendre chaque mot.

## 3. Signaux fréquents

### Problème

- `The main challenge is...`
- `We are struggling with...`
- `One concern is...`
- `The issue we have is...`
- `What worries us is...`

### Contrainte

- `We cannot...`
- `We have to...`
- `The deadline is...`
- `The regulation requires...`
- `The platform must remain available...`

### Demande

- `How would you approach...?`
- `What would you recommend?`
- `What would you do first?`
- `How would you decide between...?`
- `How would you handle...?`

## 4. Drill — reformulation

Lire une fois la question, cacher le texte, puis reformuler en français ou en anglais simple.

### Question 1

> We have several business units using different integration technologies, and each unit has its own standards. Management wants to standardize everything in six months, but some teams have strong regulatory constraints. How would you approach the architecture?

Reformulation attendue :

> Multiple units, inconsistent standards, pressure to standardize, but local constraints. Need federation/tailoring and governance.

### Question 2

> The delivery team says the architecture review is blocking the release because the new security requirement appeared only two weeks before production. What would you do?

Reformulation :

> Late security requirement, delivery pressure, need impact analysis and governance rather than ignore it.

## 5. Drill — mot manquant

Même si un mot n’est pas compris, continuer.

Exemple :

> The proposed solution introduces a significant **[unknown word]** on the legacy platform, which could increase migration risk.

Même sans le mot : on entend `legacy platform` + `increase migration risk`. On peut demander :

> When you say that it introduces a significant dependency on the legacy platform, do you mean that the target would still require the legacy component?

## 6. Drill — accents et réduction

À l’oral :

- `What do you` peut sonner comme `Whaddaya`.
- `going to` devient souvent `gonna` dans l’anglais informel.
- `want to` peut devenir `wanna`.
- `could you` peut être fortement réduit.

En entretien professionnel, l’interlocuteur n’utilisera pas toujours ces formes, mais il faut savoir qu’elles existent.

## 7. Phrases pour faire répéter

- `Could you repeat the last part, please?`
- `Could you say that again a little more slowly?`
- `I understood the migration constraint, but could you repeat the question?`
- `When you say “platform ownership”, what exactly do you mean?`
- `Just to confirm, are you asking how I would prioritize the migration?`

Demander une clarification est préférable à répondre à côté.

## 8. Drill — détecter la vraie question

### Long prompt

> The organization has grown through acquisitions. It now has five architecture teams, several repositories, different technology standards, and duplicated applications. The CIO wants a single target architecture. Before discussing the target, what would you focus on?

Vraie question : **What first?**

Réponse : architecture capability, governance, scope, stakeholders, landscape, principles; pas immédiatement la cible détaillée.

## 9. Drill — chiffres et délais

S’entraîner à entendre :

- `three months`
- `thirteen months`
- `thirty months`
- `fifteen percent`
- `fifty percent`
- `one point five million`
- `zero downtime`
- `ninety-nine point nine percent availability`

Les nombres changent souvent la réponse architecturale.

## 10. Drill — meeting language

Reconnaître :

- `Let’s park this for now.` = on reporte ce point.
- `Let’s take this offline.` = discussion séparée après réunion.
- `Can you walk us through it?` = peux-tu l’expliquer étape par étape ?
- `What’s the rationale?` = quelle est la justification ?
- `What’s the impact?` = quel est l’impact ?
- `Who owns this?` = qui en est responsable ?
- `Is this a hard constraint?` = est-ce une contrainte réellement non négociable ?
- `What are we trading off?` = quel compromis faisons-nous ?

## 11. Listening simulation

Lire ce paragraphe à voix haute ou le faire lire par une synthèse vocale :

> We are planning to modernize a payment platform that currently processes most transactions in batch. The initial idea was to move everything to a container platform, but operations is concerned about observability and rollback, while security requires stronger identity controls. The sponsor still expects the first business capability in production within six months. How would you structure the transformation?

Puis, sans regarder, noter cinq mots :

`batch / container / observability / identity / six months`

Ensuite répondre en une minute.

## 12. Self-test

Après une question orale, vérifier :

1. Qui parle ?
2. Quel est le problème ?
3. Quelle est la contrainte ?
4. Où est le risque ?
5. Quelle décision demande-t-on ?

Si ces cinq éléments sont compris, il n’est pas nécessaire d’avoir compris 100 % des mots.
