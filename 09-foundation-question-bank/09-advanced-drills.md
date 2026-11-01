# Foundation — 24 exercices discriminants sur les objectifs X2202

Répondre sans lire la correction. Ces QCM sont **complémentaires** aux 300 questions de base. Leur objectif est de distinguer des concepts TOGAF voisins, sans prétendre reproduire l'examen réel. Corrections : `09-advanced-drills-corrections.md`.

## F01 — Purpose of architecture

Un groupe décide de son modèle de présence géographique à cinq ans. Quelle finalité de l'architecture décrit le mieux ce travail ?

A. Portfolio
B. Strategy
C. Project
D. Solution Delivery

## F02 — Portfolio versus project

Le comité compare huit programmes concurrents et leurs dépendances pour sélectionner ceux à financer. Quel cadre d'utilisation de l'architecture est dominant ?

A. Solution Delivery
B. Strategy
C. Portfolio
D. Project

## F03 — Abstraction

Pour un service de paiements, « une capacité de détection d'anomalie indépendante du produit choisi » se situe d'abord à quel niveau de raisonnement ?

A. What
B. With What
C. How (physique)
D. Un Technology Standard

## F04 — Architecture Repository

Lequel correspond le mieux au rôle du Solutions Landscape dans un Architecture Repository ?

A. Gouverner les exceptions
B. Lister les standards autorisés
C. Enregistrer les requirements de la cible
D. Décrire les solutions réalisées et leurs relations avec les architectures

## F05 — Architecture Metamodel

Quel composant du Repository permet d'exprimer les classes 'Application', 'Data Entity' et leurs relations autorisées ?

A. Architecture Metamodel
B. Standards Information Base
C. Solutions Landscape
D. Governance Log

## F06 — Principle versus requirement

Un comité approuve « toute donnée sensible doit être chiffrée en transit » comme règle directrice. Un projet spécifie « TLS 1.3 avec suites autorisées ». Quelle distinction est correcte ?

A. Les deux sont nécessairement des principles
B. Le principe ne doit jamais comporter d'implication technique
C. Le premier est une règle directrice, le second peut constituer une requirement ou un standard dérivé
D. Le second est une Architecture Vision

## F07 — Qualities of principles

Un jeu de principes contient deux règles incompatibles qui imposent des choix opposés dans le même contexte. Quelle qualité fait le plus directement défaut ?

A. Robust
B. Consistent
C. Stable
D. Understandable

## F08 — Draft versus Approved

Deux vues décrivent une Target Architecture ; l'une est proposée pour revue, l'autre acceptée par l'instance compétente. Quel critère distingue leurs statuts ?

A. Le nombre de diagrammes
B. L'usage de BPMN ou ArchiMate
C. La présence d'une estimation de coût
D. Le passage par le mécanisme de validation/gouvernance applicable

## F09 — Scoping ADM

Une mission définit le périmètre métier, le niveau de détail, les domaines concernés et l'horizon de trois ans. Quel sujet maîtrise-t-elle ?

A. Les dimensions du scoping de l'architecture
B. La seule Phase D
C. Le Governance Log
D. Le gradient scoring de l'examen

## F10 — Phase A communications

Le sponsor valide la Vision mais le CISO et Operations restent non informés des décisions. Quel livrable doit prioritairement soutenir la communication des décisions aux parties prenantes ?

A. Architecture Contract
B. Architecture Roadmap
C. Communications Plan
D. Compliance Assessment

## F11 — ADD versus ARS

Un dossier doit décrire les vues de l'architecture cible et ses éléments de domaine. Quel livrable est le plus approprié ?

A. Architecture Requirements Specification
B. Architecture Definition Document
C. Standards Information Base
D. Requirements Impact Assessment

## F12 — Requirement impact

Une exigence réglementaire nouvelle provoque des modifications possibles sur les phases C et F. Quel livrable aide à documenter ses impacts ?

A. Architecture Contract
B. Architecture Vision
C. Compliance Assessment
D. Requirements Impact Assessment

## F13 — Governance model versus contract

Pour déterminer qui contrôle les déviations et selon quel processus pendant la réalisation, on doit d'abord formaliser :

A. Implementation Governance Model
B. Architecture Definition Document
C. Architecture Contract uniquement
D. Architecture Roadmap uniquement

## F14 — Phase E versus F

Un architecte a regroupé les gaps en work packages et cherche à ordonner ces lots selon risques, valeur et dépendances. Quelle phase joue le rôle principal ?

A. Phase E
B. Phase G
C. Phase F
D. Phase H

## F15 — Phase H categories

Une modification améliore une solution existante sans renverser sa cible et demande une réévaluation limitée d'architecture. Quelle catégorie Phase H est la plus plausible ?

A. Simplification nécessairement
B. Incremental
C. Re-architecting nécessairement
D. Requirements Management exclusivement

## F16 — Interoperability

Deux services communiquent via HTTPS mais interprètent différemment une donnée de statut. La lacune dominante concerne :

A. Le seul réseau
B. Uniquement Technology Architecture
C. La stratégie d'implémentation
D. L'interopérabilité informationnelle

## F17 — Readiness

La Target est approuvée mais le financement du support et la capacité d'exploitation n'existent pas. Quelle approche détecte cette vulnérabilité avant migration ?

A. Business Transformation Readiness Assessment
B. Application Architecture uniquement
C. Architecture Contract uniquement
D. Content Metamodel

## F18 — Governance characteristics

Des équipes sont soumises à des règles d'architecture variables selon leur poids politique ; quel principe de bonne gouvernance est directement mis en cause ?

A. Independence uniquement
B. Stable uniquement
C. Fairness
D. Gap Analysis

## F19 — Artifact versus deliverable

Un comité reçoit un Architecture Definition Document contenant une matrice Application/Data et un diagramme de flux. Quelle relation est correcte ?

A. La matrice est un deliverable et l'ADD un artifact
B. Les deux éléments sont des artifacts pouvant composer le deliverable ADD
C. L'ADD est nécessairement un SBB
D. Un diagramme est toujours une Transition Architecture

## F20 — View versus viewpoint

Les opérations doivent visualiser la reprise sur incident et les points de surveillance. Quel rôle joue le viewpoint ?

A. Il est la preuve d'approbation du Board
B. Il correspond à une solution physique
C. Il constitue le plan de migration
D. Il prescrit la convention de représentation permettant une view répondant aux concerns

## F21 — Requirements cross-phase

Une exigence identifiée en Phase D modifie la cible applicative et les travaux de migration. Quelle assertion exprime correctement l'ADM ?

A. Requirements Management est transversal et peut provoquer des itérations entre phases
B. L'exigence attend obligatoirement Phase H pour être prise en compte
C. Phase D seule peut modifier les requirements
D. Une architecture approuvée ne peut plus changer

## F22 — Gap versus work package

Une banque constate l'absence d'une capacité de reprise que la Target impose. Quel objet représente ce constat avant la décision de solution ?

A. Architecture Contract
B. SBB déjà sélectionné
C. Gap
D. Transition Architecture

## F23 — Capability versus application

Une équipe souhaite remplacer une application nommée 'Fraud Detection' sans perdre la détection de fraude. Quel élément doit rester stable au niveau Business ?

A. Le produit exact
B. La business capability de détection
C. Le runtime actuel
D. Le Technology Platform Diagram

## F24 — Architecture Roadmap versus plan

Un comité veut voir les états architecturaux successifs et les principaux work packages menant à la Target. Quel artefact/livrable est prioritairement adapté ?

A. Standards Information Base
B. Architecture Requirements Specification
C. Architecture Contract
D. Architecture Roadmap
