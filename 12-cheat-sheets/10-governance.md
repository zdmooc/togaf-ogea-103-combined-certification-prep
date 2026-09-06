# Cheat Sheet — Architecture Governance

## La logique générale

Architecture Governance sert à rendre les décisions :

- explicites ;
- approuvées au bon niveau ;
- traçables ;
- contrôlables ;
- réévaluables quand le contexte change.

## Architecture Board

Rôle principal : **gouverner et arbitrer** l’architecture.

Exemples :

- approuver des orientations ;
- arbitrer des conflits ;
- décider des exceptions importantes ;
- suivre la conformité et les risques architecturaux.

**Board ≠ architecture team** : le Board gouverne ; l’équipe produit/analyse l’architecture.

## Architecture Contract

Rôle : formaliser les **engagements, responsabilités et attentes** entre parties impliquées dans la réalisation de l’architecture.

Réflexe : Contract = engagements et responsabilités, pas simple diagramme de solution.

## Architecture Compliance Review

Rôle : comparer l’implémentation avec l’architecture approuvée.

Question :

> Ce qui est construit respecte-t-il les décisions, principes, requirements et standards approuvés ?

## Deviation vs Exception

- **Deviation** : écart constaté par rapport à la cible/standard/règle.
- **Exception / waiver** : décision gouvernée autorisant explicitement un écart sous certaines conditions.

Un écart n’est pas automatiquement acceptable parce qu’il est techniquement justifié.

## Phase G

C’est la phase où la gouvernance d’implémentation devient centrale :

- compliance ;
- Architecture Contract ;
- reviews ;
- deviation management ;
- escalations ;
- evidence.

## Architecture Governance vs Project Governance

- Architecture Governance : cohérence, conformité et décisions d’architecture.
- Project Governance : budget, délais, ressources, delivery, reporting projet.

Les deux se croisent mais ne sont pas synonymes.

## Scénario flash

Une équipe veut contourner un standard pour respecter une deadline.

Mauvaise réponse : « le sponsor accepte donc on continue ».

Meilleure logique :

1. documenter l’écart ;
2. analyser impact/risque ;
3. réaliser la revue appropriée ;
4. décider correction ou exception via la gouvernance ;
5. conserver la traçabilité.

## Pièges Foundation

- Board = gouvernance/arbitrage.
- Contract = engagements.
- Compliance Review = contrôle de conformité.
- Exception = autorisation gouvernée, pas simple deviation.

## English

> Architecture governance ensures that architecture decisions, compliance, deviations, and exceptions are handled through explicit and traceable decision mechanisms.
