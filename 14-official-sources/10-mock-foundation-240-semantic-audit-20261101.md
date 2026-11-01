# Audit sémantique des 240 QCM Foundation des six examens Combined — 2026-11-01

Base : main, commit `0c9c35d`, après fusion de la PR #5.

## Périmètre
Six examens de 40 questions chacun, soit 240 énoncés, 960 choix, 240 clés et explications relus. Audit éditorial, non officiel et non étalonné.

## Erreurs corrigées
- Mock 01 : Q7 (disponibilité versus TLS, indice de longueur), Q33 (Architecture Board), Q35 (Architecture Compliance Review).
- Mock 02 : Q22 (Architecture Roadmap).
- Mock 03 : Q35 (Architecture Compliance Review).
- Mock 04 : Q26 (erreur conceptuelle Risk Management versus Business Transformation Readiness ; choix A/C et justification alignés).
- Mock 05 : Q21 (Gap Analysis), Q22 (Architecture Roadmap), Q33 (Architecture Board).
- Mock 06 : Q5 (Architecture Principle), Q8 (Baseline/Target/Gap).

Total : 11 QCM modifiés, sans changer les lettres des réponses. Les 48 références génériques « X2202, domaine correspondant » ont été supprimées. Les objectifs sont retracés séparément dans `14-official-sources/06-x2202-learning-outcome-traceability.md`.

## Contrôles et limites
Chaque sujet comporte 40 QCM et 40 clés, avec quatre options par question. Distribution globale des réponses : A=60, B=61, C=63, D=56.

Environ 123 questions reprennent des cadrages génériques. Les six examens répètent des thèmes similaires ; leurs difficultés ne sont pas statistiquement indépendantes. Plusieurs distracteurs restent faciles et les corrigés Foundation sont courts. Aucun étalonnage externe des difficultés ni audit psychométrique n'a été réalisé.

Les corrections s'ajoutent aux audits de la banque Foundation Q001–Q300, des scénarios Practitioner S001–S060, des XP01–XP36 et des 48 scénarios Practitioner des mocks. Les CI vérifient structure et cas de non-régression, non l'équivalence avec une certification officielle.
