# Audit sémantique Practitioner — S001–S060, XP01–XP36 et mocks (1er novembre 2026)

## Source et portée

- Base auditée : `main` à `d3ebfaa456aee57634b86ff64530716221385f47` (PR #4 fusionnée).
- Lecture des 60 scénarios S, de leurs quatre options et de leur barème 5/3/1/0.
- Lecture des 36 cas ciblés XP01–XP36 et des six jeux de corrigés correspondants.
- Lecture des 48 scénarios Practitioner des six examens Combined et de leurs 192 justifications notées.
- Les **240 questions Foundation contenues dans les six mocks** ne font pas partie de cet audit sémantique Practitioner ; leur couverture reste distincte.
- Support original non officiel. Les barèmes 5/3/1/0 expriment un jugement pédagogique et ne prouvent pas une difficulté équivalente à l'examen OGEA-102.

## Résultats et corrections

| Lot | Vérification | Modifications |
|---|---|---|
| S001–S060 | 60 jeux de quatre options, scores distincts 5/3/1/0 ; concordance options / textes des justifications | **22 scénarios** corrigés ou clarifiés : S021, S025, S032–S039, S041, S042, S044–S047, S049, S052, S054, S055, S058, S060 |
| XP01–XP36 | Séquence de 36 exercices, barèmes et justifications | **11 cas** : XP01–XP05, XP10, XP11, XP13, XP15, XP16, XP19. Les options à 3 points ont été renforcées pour former des alternatives partiellement valides et non manifestement fautives |
| Mock 01 | 8 scénarios, 32 justifications | **32 justifications** réécrites ; l'inversion des références **B/D en P5** corrigée (B=5 ; D=3 inchangés) |
| Mocks 02–06 | 40 scénarios, 160 justifications | **120 commentaires de niveaux 3/1/0** réécrits selon le contexte du scénario ; les 40 justifications de niveau 5 déjà spécifiques ont été conservées |
| CI | Tests de structure et vérification sémantique ciblée | Ajout de contrôles empêchant une justification S de répéter une ancienne option, le retour de l'inversion P5 et plusieurs phrases génériques dans les mocks |

## Anomalies caractéristiques

1. **Anciennes justifications après déplacement des réponses** : le mock 01 P5 attribuait à B une explication commençant par D, et à D une explication commençant par B.
2. **Barèmes non discriminants** : plusieurs options à 3 et 1 points de S033, S036, S045, S046, S052, S054, S055, S060 étaient trop proches ou inversaient le mérite relatif.
3. **Justifications résiduelles obsolètes** : les explications de S032, S034–S039, S042, S044, S047, S049, S058 faisaient parfois référence à des actions absentes de l'option actuelle.
4. **Distracteurs de 3 points clairement invalides** : XP01, XP02, XP03, XP04, XP05, XP10, XP11, XP13, XP15, XP16 et XP19 ont été redéfinis afin de représenter un véritable début de démarche à compléter.

## Limites

- Une vérification de la structure et des justifications ne peut déterminer à elle seule la valeur pédagogique effective des notes 3 versus 1.
- Les scénarios XP33–XP34 ont été comparés à la taxonomie « Consistent / Compliant / Conformant / Fully Conformant » ; ils restent corrects sous les conditions énoncées, notamment l'absence de fonction supplémentaire non spécifiée dans XP33.
- Des scénarios continuent d'offrir des distracteurs relativement faciles ; leur présence peut servir la révision mais ne prouve pas un niveau Practitioner.
- La répartition 5/3/1/0 et la distribution des meilleures réponses par lettre restent inchangées ; la calibration par des apprenants indépendants n'a pas été effectuée.
- La conformité exhaustive de l'ensemble des **131 learning outcomes X2202**, les 240 questions Foundation de mocks et l'absence d'ambiguïté de tous les scénarios nécessitent encore un contrôle spécialisé indépendant.

## Prochaines validations

1. Exécuter les deux scripts de validation GitHub Actions sur la PR, puis après fusion.
2. Tester à l'aveugle les 48 scénarios Combined auprès d'un groupe de candidats et relever les désaccords sur les barèmes 5/3/1/0.
3. Vérifier la difficulté et la validité sémantique des 240 questions Foundation des mocks.
4. Éviter toute mention « support officiellement accrédité » ou « équivalent à l'examen officiel » sans preuve externe.

## Sources

- The Open Group, TOGAF Enterprise Architecture syllabus X2202 v4.0 : https://www.opengroup.org/library/x2202
- The Open Group, TOGAF Standard 10th Edition et documents de gouvernance d'architecture : https://pubs.opengroup.org/togaf-standard/
- Terminologie comparative d'Architecture Compliance (TOGAF 9.2, utile comme référence historique pour XP33–XP34) : https://www.togafcertified.com/TOGAF%209.2%20HTML/chap42.html
