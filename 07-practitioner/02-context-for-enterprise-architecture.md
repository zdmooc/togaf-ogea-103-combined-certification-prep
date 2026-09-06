# Practitioner — Context for Enterprise Architecture

## 1. Pourquoi le contexte vient avant la méthode

Le Practitioner doit savoir que l’ADM n’est jamais appliqué dans le vide. Une même organisation peut avoir :

- une Architecture Capability mature ou immature ;
- une gouvernance centralisée ou fédérée ;
- plusieurs niveaux d’architecture ;
- des contraintes réglementaires fortes ;
- un patrimoine complexe ;
- des cycles Agile ;
- des dépendances fournisseurs ;
- des standards internes déjà établis.

La première question n’est donc pas “quelle phase appliquer mécaniquement ?” mais :

**dans quel contexte l’architecture doit-elle être développée, gouvernée et utilisée ?**

## 2. Context elements à reconnaître

Dans un scénario, repère notamment :

- drivers et goals ;
- scope ;
- stakeholders ;
- Architecture Capability existante ;
- governance model ;
- principles ;
- standards ;
- repositories ;
- architecture partitions ;
- delivery approach ;
- regulatory environment ;
- dependencies ;
- maturity ;
- risk appetite.

## 3. Enterprise boundaries

Le mot “enterprise” dépend du scope.

Cela peut être :

- toute une banque ;
- une ligne métier ;
- une filiale ;
- un écosystème de partenaires ;
- un programme stratégique.

Le Practitioner doit éviter de supposer que l’entreprise correspond forcément à toute la société juridique.

## 4. Tailoring comme réponse au contexte

TOGAF doit être adapté au besoin.

Un bon tailoring peut modifier :

- le niveau de détail ;
- l’ordre ou l’intensité de certaines activités ;
- les deliverables ;
- les techniques ;
- les rôles ;
- le rythme des itérations ;
- les checkpoints de gouvernance.

Mais tailoring ne veut pas dire supprimer la logique nécessaire.

## 5. Architecture Capability

Avant d’exécuter un travail d’architecture, il faut parfois renforcer la capacité elle-même.

Indices typiques :

- aucune gouvernance claire ;
- rôles inconnus ;
- absence de repository ;
- principes non définis ;
- équipes projet qui ne savent pas qui décide ;
- standards contradictoires.

Dans ce cas, le problème peut relever du **Preliminary / Architecture Capability**, et non d’une phase B/C/D.

## 6. Architecture levels

Le Practitioner doit reconnaître différents niveaux :

- strategic ;
- segment ;
- capability ;
- solution / implementation context.

Un changement local ne doit pas forcément déclencher une refonte stratégique complète.

Inversement, un programme transverse peut nécessiter une coordination multi-niveaux.

## 7. Federation et partitioning

Dans une grande entreprise, plusieurs équipes d’architecture peuvent travailler en parallèle.

Le risque est la divergence :

- standards différents ;
- responsabilités chevauchantes ;
- incohérences de modèles ;
- solutions locales incompatibles.

La bonne réponse n’est pas toujours “centraliser tout”. Elle peut être de définir des partitions, des interfaces, des responsabilités et une gouvernance fédérée.

## 8. Architecture Repository et Enterprise Continuum

Dans un scénario, si l’équipe cherche à réutiliser des assets, modèles, standards ou patterns, pense au Repository.

Si la question porte sur l’organisation et la classification de ces assets, pense à l’Enterprise Continuum.

## 9. Digital / Agile context

TOGAF reste applicable dans un delivery Agile.

Le Practitioner doit chercher :

- décision juste à temps ;
- architecture runway appropriée ;
- garde-fous ;
- principes ;
- exigences non fonctionnelles ;
- feedback rapide ;
- gouvernance proportionnée.

Le piège est de penser :

“Agile = pas d’architecture”.

## 10. Risk and Security context

Security et risk ne sont pas une phase isolée.

Ils influencent :

- requirements ;
- principles ;
- target architectures ;
- solution selection ;
- migration ;
- governance ;
- change management.

## 11. Scénario MayaBank 1 — capacité immature

MayaBank crée une nouvelle équipe EA. Les projets ne savent pas qui approuve les décisions, aucun principe n’est partagé, et chaque programme conserve ses propres modèles.

### Mauvaise lecture

“Il faut commencer Phase B pour définir la Business Architecture.”

### Meilleure lecture

Le problème principal est d’abord la **Architecture Capability** : gouvernance, rôles, principes, repository et façon de travailler doivent être établis ou adaptés.

## 12. Scénario MayaBank 2 — fédération

Trois entités de MayaBank disposent de leurs propres architectes et réglementations locales. Le groupe veut une plateforme de paiement commune.

Réponse trop faible : imposer un modèle unique sans analyse locale.

Réponse plus TOGAF : définir ce qui est commun au niveau groupe, ce qui reste local, les interfaces, les responsabilités et les mécanismes de gouvernance fédérée.

## 13. Scénario MayaBank 3 — Agile

Les équipes livrent toutes les deux semaines. Un architecte propose de bloquer six mois le delivery pour produire l’ensemble des architectures détaillées.

Cette réponse est disproportionnée.

La meilleure approche est de tailor l’ADM : maintenir vision, principes, requirements et gouvernance tout en travaillant de manière itérative et avec le niveau de détail nécessaire au prochain ensemble de décisions.

## 14. Pièges Practitioner

### Piège 1 — traiter un problème de capability comme un problème de phase

### Piège 2 — appliquer un niveau de détail identique partout

### Piège 3 — confondre tailoring et suppression de contrôle

### Piège 4 — confondre fédération et absence de gouvernance

### Piège 5 — supposer que le contexte Agile invalide TOGAF

## 15. Méthode de décision

Quand une question porte sur le contexte, pose ces cinq questions :

1. Quel est le scope réel de l’entreprise ?
2. Quelle Architecture Capability existe déjà ?
3. Quel niveau d’architecture est concerné ?
4. Quelle gouvernance est nécessaire ?
5. Comment l’ADM doit-il être adapté sans perdre les contrôles essentiels ?

## 16. English for Architects

> Before applying the ADM, I assess the enterprise context, the existing architecture capability, the governance model, and the level of architecture required.

> I tailor the method to the organization without losing traceability, stakeholder engagement, or governance.

---

Original educational content based on the current TOGAF Enterprise Architecture Practitioner syllabus.