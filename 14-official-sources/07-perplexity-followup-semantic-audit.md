# Contre-audit pédagogique après relecture Perplexity — 1er novembre 2026

## Périmètre et statut

Correctifs proposés dans la **PR #3**. La branche de correction part du commit `57743847` de `main`. Le dépôt demeure un **support de préparation original, non accrédité et non étalonné**. Les tests automatiques ne démontrent pas une difficulté équivalente à l'examen officiel.

## Constats contrôlés et corrections appliquées

| Constat externe | Contrôle dans le dépôt | Remédiation |
|---|---|---|
| Huit coquilles `B'est` | **8 confirmées** (Q023, Q088, Q095, Q107, Q119, Q140, Q155, Q264) | Remplacées et test anti-régression |
| Explication inversée Q073 | **Confirmée** : A et B étaient inversées | Différence Phase A/Phase B réécrite |
| Anciennes lettres dans les corrigés | Confirmées sur plusieurs QCM (dont 066, 085, 090, 102, 117, 119, 126, 293) | **24** explications Foundation réécrites avec notions explicites plutôt que lettres ambiguës |
| Sept rubriques Architecture Repository | Le cours principal utilisait une ancienne présentation | Les 7 intitulés X2202 8.5 sont explicitement enseignés ; Standards Information Base et Governance Log définis comme termes historiques ou sous-ensembles |
| Interoperability / Phase H | Deux chapitres donnaient des grilles pédagogiques sans distinguer leur statut | Dimensions d'interopérabilité qualifiées de grille d'analyse ; Phase H décrit Simplification, Incremental, Re-architecting |
| 60 justifications Practitioner répétitives | **Confirmé** | **240** justifications de niveaux 5/3/1/0 remplacées par des explications contextualisées aux 60 scénarios |
| XP05–XP32, notes faibles génériques | Confirmé | **84** justifications de notes 3/1/0 individualisées ; XP08/XP17/XP31 ont reçu des options 3 points plus plausibles |
| Meilleure réponse mock Practitioner A/B | L'audit de `main` donnait **42/48** en A/B (et non 46/48) | Options et barèmes de 48 cas réordonnés : **12** réponses à 5 points pour chacune des lettres A/B/C/D ; chaque mock a 2 de chaque |
| Objectifs de conformité et stratégies trop peu exercés | L2 1.5 et 5.3 avaient peu d'items dédiés | Ajout de **XP33–XP36** sur conformance et Greenfield/Revolutionary/Evolutionary ; matrice X2202 enrichie |
| Distracteurs Foundation caricaturaux | Exemples Q037, Q042, Q112 confirmés | 10 nouvelles questions aux distracteurs réécrits, dont les 3 exemples |

## Garde-fous automatiques

- Validation des 300 QCM Foundation, 60 scénarios Practitioner et six examens Combined.
- Détection de la réapparition des coquilles et de l'inversion Q073.
- Blocage du retour des quatre familles de phrases types des scénarios S001–S060.
- Validation de la répartition des **48** meilleures réponses des mocks.
- Vérification de la liste des **sept** rubriques X2202 Repository.
- Vérification de la présence des XP33–XP36 et de leurs quatre justifications.

## Ce qui reste hors validation

1. **Relecture experte indépendante des 300 QCM et des 48 cas de mocks** : plusieurs distracteurs peuvent encore être éliminés trop rapidement.
2. **Validation sémantique de chaque objectif Bloom** : les 130 références candidates ne constituent pas, seules, une preuve de maîtrise.
3. **Étalonnage du niveau d'examen** par des tests officiels autorisés et des résultats d'apprenants.
4. **Calibration des notes intermédiaires** des scénarios ; la distribution de lettres équilibrée prévient un indice de réponse mais n'améliore pas mécaniquement la qualité des quatre choix.

**Politique de fusion :** les changements peuvent être revus et fusionnés comme remédiation technique/pédagogique ; ne pas déclarer le dépôt « certifié conforme » ou « identique à l'examen ».

## Références

- The Open Group X2202 v4.0, §3.1.4 LO 4.7, §3.2.1 LO 1.5 et §3.2.8 LO 8.5, [bibliothèque The Open Group](https://www.opengroup.org/library/x2202).
- TOGAF Standard, 10th Edition ; phase H — Architecture Change Management.
