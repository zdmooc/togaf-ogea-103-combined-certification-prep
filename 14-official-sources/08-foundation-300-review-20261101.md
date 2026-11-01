# Audit pédagogique Foundation — banque Q001–Q300 (1er novembre 2026)

## Périmètre et point de départ

- Source : `main` au commit `4ae0d8d0d3f08cb4b3f3fe6e034fae77e6ea5fb3` (PR #3 déjà fusionnée).
- Les **300 énoncés, les 1 200 choix, les 300 clés et leurs explications principales** ont fait l'objet d'une lecture structurée par plages Q001–Q060, Q061–Q095, Q096–Q130, Q131–Q165, Q166–Q210, Q211–Q240, Q241–Q262 et Q263–Q300.
- Les cas litigieux ont été relus dans leur bloc complet, incluant les commentaires de distracteurs présents.
- Il s'agit d'une **revue éditoriale et conceptuelle ciblée**, pas d'un étalonnage psychométrique, d'une accréditation officielle, ni d'une reproduction de sujets d'examen.

## Anomalies confirmées et corrections

| Catégorie | Questions corrigées | Motif |
|---|---|---|
| Attribution incorrecte aux phases de l'ADM | Q061, Q062, Q100, Q108 | Q061/Q062 mélangeaient E/F/G/A/B ; Q100 disait « C termine la définition de domaine » au lieu de D ; Q108 associait mal les choix aux phases |
| Explication ABB/SBB imprécise | Q031 | Un composant choisi (choix B) relève du SBB ; il ne devait pas être classé « hors sujet » |
| Typographie spécialisée | Q284 | `AB Bs` corrigé en `ABB` |
| Distracteurs faibles, artificiels ou pédagogiquement peu discriminants | Q002, Q027, Q034, Q046, Q049, Q052, Q053, Q054, Q059, Q067, Q071, Q113, Q120, Q184, Q197, Q218, Q243, Q257, Q273, Q274, Q294, Q295 | Alternatives recentrées sur des confusions plausibles : driver/goal/principle/requirement, repository/continuum, catalog/matrix/diagram, phase E/F/G, gouvernance et delivery |

**Total : 28 QCM modifiés dans 7 fichiers de banque**, sans changer les lettres ni les concepts des bonnes réponses. Les anciennes corrections Q073, Q090 et « B'est » n'ont pas été réintroduites.

## Contrôles structurels après correction

- 300 questions dans l'ordre Q001–Q300 ; 4 choix A/B/C/D et une clé explicite par question.
- Répartition des réponses inchangée : **A=75, B=75, C=75, D=75**.
- Indice de longueur : bonne réponse la plus longue dans **29 %** des QCM ; ratio moyen bonne réponse / moyenne des distracteurs **1,03** ; **aucune** réponse correcte de longueur supérieure au double de la moyenne des distracteurs.
- Tests de non-régression ajoutés pour Q031, Q061, Q062, Q100, Q108 et la coquille Q284.
- Les deux scripts CI existants restent les garde-fous de structure ; une exécution réussie ne valide pas les nuances sémantiques de chaque question.

## Limites et risques pédagogiques résiduels

Certaines questions sont délibérément très accessibles et utiles à la **mémorisation Foundation**, mais peu discriminantes pour un entraînement avancé :

- Q004, Q155 et Q259 : restitution directe de noms et d'une séquence ADM.
- Q146–Q154 : reconnaissance directe des phases de l'ADM.
- Q201–Q208 : intitulé de la technique fortement suggéré par l'énoncé.
- Q198 : dépendance élémentaire entre deux work packages.

Ces questions ne sont pas nécessairement fausses ; elles ne doivent simplement pas être présentées comme des scénarios de difficulté Practitioner. Des distracteurs encore trop facilement éliminables peuvent subsister au-delà des 28 corrections effectuées. Aucun test lexical ne permet de trancher automatiquement l'ambiguïté réelle de toutes les options.

## Suite recommandée

1. Vérifier la CI sur la PR de cette revue et analyser d'éventuelles régressions.
2. Relire séparément les **240 questions Foundation des six examens Combined** : ce ne sont pas les 300 questions de la banque.
3. Réaliser une revue sémantique indépendante des **48 scénarios Practitioner des mocks**, puis calibrer les niveaux 5/3/1/0 avec des profils d'apprenants.
4. Ne pas déclarer ce dépôt « équivalent à l'examen officiel » ni « certifié conforme » sans preuve externe.

## Références

- The Open Group, `X2202` v4.0, syllabus Foundation/Practitioner : https://www.opengroup.org/library/x2202
- The Open Group, OGEA-101 exam plan : https://help.opengroup.org/hc/en-us/articles/32158230604050-What-Is-the-Exam-Plan-for-the-OGEA-101-TOGAF-Enterprise-Architecture-Part-1-Exam
