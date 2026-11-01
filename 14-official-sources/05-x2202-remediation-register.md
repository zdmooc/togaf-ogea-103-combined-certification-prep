# Registre de conformité X2202 — audit correctif du 1er novembre 2026

**Statut : remédiation en cours, couverture exhaustive non certifiée.** Source : [X2202](https://www.opengroup.org/library/x2202) — TOGAF Certification Program Conformance Requirements (Multi-Level), §3.1 et §3.2.

## Règles de validation

Chaque *learning outcome* doit obtenir (1) une référence du cours avec explication vérifiée, (2) au moins une évaluation pertinente, (3) un corrigé contrôlé avec justification et (4) une source TOGAF de référence. La présence d'un titre de chapitre ou d'une référence d'exercice seule ne suffit pas. **Non vérifié** n'est jamais équivalent à **couvert**.

| Groupe de learning outcomes X2202 | Enseignement principal | Lacune/contrôle à résoudre | Statut |
|---|---|---|---|
| Foundation L1 U1 : 1.1–1.12 | `01-togaf-foundations/` + `10-x2202-foundation-deepening.md` | Vérifier chaque objectif, notamment abstraction et repository | Partiellement corrigé |
| Foundation L1 U2 : 2.1 | `01-togaf-foundations/10-x2202-foundation-deepening.md` | Glossaire et usage contextuel ; vérifier note officielle de non-examinabilité isolée | Complément ajouté |
| Foundation L1 U3 : 3.1–3.26 | `02-adm/` + addendum Foundation | Draft/Approved, 4 dimensions du scope, flux inter-phases | Partiellement corrigé |
| Foundation L1 U4 : 4.1–4.9 | `03-adm-techniques/` + addendum Foundation | Principes, interopérabilité, readiness | Partiellement corrigé |
| Foundation L1 U5 : 5.1–5.6 | `04-applying-the-adm/` + addendum Foundation | Quatre finalités Strategy/Portfolio/Project/Solution Delivery | Partiellement corrigé |
| Foundation L1 U6 : 6.1–6.5 | `05-architecture-governance/` + addendum Foundation | Caractéristiques de gouvernance et compliance | Partiellement corrigé |
| Foundation L1 U7 : 7.1–7.3 | `06-architecture-content/` + addendum Foundation | Livrables supplémentaires/relations phases | Partiellement corrigé |
| Foundation L1 U8 : 8.1 | `14-official-sources/02-exam-format-and-policies.md` | Différencier niveaux, langues et règles en vigueur | À revalider avant inscription |
| Practitioner L2 U1 : contexte et conformité | `07-practitioner/` et addendum Practitioner | Niveaux de conformance, vues multiples, états | Partiellement corrigé |
| Practitioner L2 U2 : stakeholder management | `07-practitioner/03-stakeholder-management-scenarios.md` | Exercice complet map → concerns → views → décision | À enrichir |
| Practitioner L2 U3 : Phase A | `07-practitioner/04-phase-a-scenarios.md` | Test de readiness, périmètre et livrables | À enrichir |
| Practitioner L2 U4 : B/C/D | `07-practitioner/05-bcd-architecture-development-scenarios.md` | Alternatives contradictoires et itérations | À enrichir |
| Practitioner L2 U5 : E/F/G | `07-practitioner/06-efg-implementation-scenarios.md` | Implementation/Migration Strategy, factor catalog, matrix, outputs | Partiellement corrigé |
| Practitioner L2 U6 : Phase H | `07-practitioner/07-phase-h-scenarios.md` | Classes de changement et décisions d'ADM re-entry | À enrichir |
| Practitioner L2 U7 : requirements | `07-practitioner/08-requirements-management-scenarios.md` | Requirements Impact Assessment, traçabilité | Partiellement corrigé |
| Practitioner L2 U8 : supporting ADM | `07-practitioner/09-supporting-adm-work.md` | TOGAF Library, repository, reuse et Series Guides | Partiellement corrigé |

## Constats de qualité des banques

- Banque Foundation : ancien état 272 A / 26 B / 2 C / 0 D. **Correctif mécanique** : 75 bonnes réponses par lettre, propositions réordonnées ; cela **ne prouve pas** une difficulté réaliste.
- Banque Practitioner : ancien état 43 A / 14 B / 3 C / 0 D. **Correctif de premier niveau** : les 60 scénarios ont été développés avec enjeux métier, contraintes et alternatives révisées, et les meilleures réponses réparties sur A/B/C/D. Une revue de qualité **indépendante** des options et de chaque gradient reste obligatoire.
- Six examens blancs : les 48 scénarios Practitioner ont été développés et les 240 QCM Foundation ont été retravaillés (48 réécrits en profondeur, 192 avec distracteurs liés aux notions TOGAF et contextualisation). La vérification pédagogique indépendante reste nécessaire. L'indépendance psychométrique et la difficulté restent **non validées**.

## Indicateurs de qualité mesurés le 1er novembre 2026

| Contrôle | Avant corrections | Après corrections | Ce que cela prouve |
|---|---:|---:|---|
| Foundation : bonne réponse la plus longue | 70 % des 300 | **34 %** | Réduction du biais de longueur, pas validation du contenu |
| Foundation : longueur moyenne bonne réponse / distracteur | 2,08 | **1,12** | Options plus comparables |
| Foundation : bonne réponse au moins 2× la longueur moyenne des distracteurs | 133 questions | **0** avec ratio strictement supérieur à 2 | Le test de non-régression bloque le retour des cas extrêmes |
| Mocks Foundation : bonne réponse la plus courte | 48 % des 240 | **38 %** | Réduction d'un biais inverse |
| Mocks Foundation : longueur relative moyenne de la bonne réponse | 0,95 | **1,03** | Comparabilité améliorée |
| Objectifs syllabus X2202 individuellement inventoriés | Non | **131** | Inventaire des objectifs et de leurs niveaux Bloom |
| Objectifs avec références d'exercices candidates | Partiel | **130 évaluables** | Traçabilité candidate, pas preuve d'adéquation cognitive |

La sélection des distracteurs reste une revue **qualitative** : une longueur comparable ne garantit ni unicité de la bonne réponse, ni distracteur plausible. Les corrections ont réduit une anomalie détectable, pas étalonné l'examen. Les **28 scénarios XP05–XP32** ciblent des objectifs insuffisamment évalués par la banque d'origine ; **31 associations** de la matrice ont été renforcées avec ces cas dédiés. L'examen en français : OGEA-F101 / OGEA-F102 ; aucun Combined français listé dans la table publique consultée au 1er novembre 2026. Sources dans `02-exam-format-and-policies.md`.

## Résultats supplémentaires du contrôle final de contenu

- [x] Foundation 7.3 : **16 livrables** vérifiés dans le syllabus et décrits dans le cours ; 16 QCM `D01–D16` avec corrigés dédiés.
- [x] Glossaire Foundation 2.1 : terme `Digital Architecture` rétabli.
- [x] Contrôle CI complémentaire sur **140 scénarios Practitioner** et **16 exercices de livrables** (présence des options, quatre notes, justifications et clés).
- [x] Écran lexical contre les formulations inter-examens presque identiques, après retrait des introductions génériques ; ce contrôle ne garantit pas l'unicité sémantique.
- [ ] Étalonnage indépendant de la qualité des distracteurs et de l'adéquation au niveau Bloom réel ; voir `FINAL_AUDIT.md`.

## Contre-audit Perplexity — actions de suivi

La PR #3 a corrigé les explications erronées et coquilles Foundation, précisé les noms officiels du Repository, révisé les méthodes de Phase H, individualisé les 60 grilles de scénarios et équilibré les 48 réponses des examens blancs. Quatre cas complémentaires XP33–XP36 abordent Conformance et les stratégies de migration. **L'audit expert indépendant et la calibration au véritable niveau d'examen ne sont pas achevés.** Voir `07-perplexity-followup-semantic-audit.md`.

## Critères de sortie bloquants

- [x] 130 objectifs évaluables disposent de références candidates exactes vers un cours et des exercices ; les dossiers comportent des corrigés. **À vérifier encore : adéquation au wording officiel, au niveau Bloom et à la référence TOGAF exacte pour chaque association.**
- [ ] Analyse humaine indépendante de l'exactitude des 300 QCM, de tous les distracteurs et des explications.
- [ ] 60 scénarios validés comme décisions réellement nuancées, avec score 5/3/1/0 justifié.
- [ ] Six examens blancs sans reprises sémantiques entre les mêmes concepts et évalués avec lecteurs indépendants. Les intitulés identiques ont été contextualisés ; les recouvrements de notions restent possibles et une revue de proximité sémantique est nécessaire.
- [ ] Pratique chronométrée et usage du corpus Open Book intégré.
- [x] Codes, langues, Open Book et modalités Combined vérifiés sur les pages publiques officielles au 1er novembre 2026 (réservation effective à confirmer chez Pearson).

## Contrôles réalisés (1er novembre 2026)

- [x] 300 QCM Foundation : 75 bonnes réponses A/B/C/D et sens des bonnes réponses préservé.
- [x] 60 scénarios Practitioner : 15 meilleures réponses A/B/C/D et quatre niveaux distincts.
- [x] 6 examens blancs : 40 QCM + 8 scénarios chacun et corrections présentes.
- [x] 48 scénarios des mocks repris avec des contextes plus développés.
- [x] 240 QCM des mocks retravaillés (48 réécrits en profondeur, 192 révisés par concept) et 14 intitulés répétés contextualisés.
- [x] **131 objectifs X2202** inventoriés ; **130** disposent d'un numéro précis d'exercice candidat et **L1.8.1** n'exige pas de question dédiée (Bloom None). Les associations restent à relire pédagogiquement.
- [x] **34 exercices ciblés** ajoutés : XF01–XF02 et XP01–XP32, avec corrections séparées et objectifs précis.
- [x] Correction du cours : **7 rubriques officielles du Repository** à L2 8.5, et non 8 ; termes Standards Library et Governance Repository distingués des variantes historiques.
- [x] 133 distracteurs faibles corrigés dans le premier audit (53 + 80), puis **133 ensembles supplémentaires de trois distracteurs** retravaillés durant l'audit du biais de longueur (31 + 35 + 40 + 27).
- [x] Biais de longueur Foundation ramené à **34 %** de bonnes réponses les plus longues, ratio moyen 1,12, aucun cas >2× ; seuils automatisés en CI.
- [x] Biais inverse des mocks Foundation réduit : bonne réponse la plus courte de 48 % à 38 % et ratio de 0,95 à 1,03 ; **24 réponses trop courtes et 37 énoncés trop génériques** révisés. Seuils de non-régression ajoutés en CI.
- [x] GitHub Actions : contrôles structurels des banques, six mocks, 131 objectifs et liens vers les cours.
- [x] Renseigner les **131 niveaux Bloom** tels qu'indiqués dans X2202, y compris l'étiquette atypique `2_Remembering` de L1 7.3.
- [ ] Examiner la pertinence **cognitive** des 130 associations candidates pour le niveau Bloom indiqué ; les références ne sont pas certifiées.
- [ ] Validation sémantique indépendante et approfondie de l'ensemble du corpus par relecteur qualifié.

## Distinction importante

`OGEA-F101` et `OGEA-F102` (épreuves individuelles en français, selon disponibilité) ne sont pas l'équivalent d'une session `OGEA-103` en français. Vérifier la liste des sessions officielles avant réservation.

Le dépôt est un support original d'autoformation, pas un matériel accrédité. Les questions reproduisent **les notions** du syllabus, jamais les questions officielles.
