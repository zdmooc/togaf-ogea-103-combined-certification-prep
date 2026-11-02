# Audit de cohérence Practitioner S001–S060 — corrections du 2 novembre 2026

**Base contrôlée :** commit `69dcb672b5e09abcd848b9e738d477aabaa3e7ad` de `main` au début de la campagne.
**Branche de correction :** `fix/practitioner-s-alignment-20261102`.
**Nature de la revue :** alignement éditorial des quatre options et de leurs justifications, classement des notes 5/3/1/0 et vérification de la terminologie. Ces corrections ne constituent ni un étalonnage psychométrique, ni une attestation de conformité officielle The Open Group.

## Périmètre et résultat

- **33 scénarios modifiés**, avec leurs quatre justifications réécrites pour commenter l'action correspondante et expliquer le classement.
- **27 scénarios laissés inchangés** après comparaison. Parmi eux, `S001`, `S002`, `S005`, `S022`, `S040` n'avaient pas été retouchés lors de la passe précédente : leurs options et justifications ont été relues, sans erreur manifeste nécessitant une modification ; les autres avaient déjà été corrigés.
- Conservation de quatre notes distinctes (5, 3, 1, 0) et du meilleur choix pour chaque cas ; les **15 meilleures réponses par lettre** A/B/C/D restent inchangées.
- Changement des notes intermédiaires sur S009, S013, S019, S020, S024 et S056 ; ajustement d'options trop proches en S029, S053, S057 et S059.
- Harmonisation `Standards Library` / `Governance Repository` dans le chapitre Repository et les six sujets Combined (avec explication des appellations historiques dans le cours).
- Catégories de l'interopérabilité ajoutées en distinguant la classification TOGAF 10 des **degrés illustratifs historiques**, sans faire passer ceux-ci pour des objectifs normatifs X2202.
- Hors périmètre : banque Q001–Q300, exercices XP et barèmes des corrections Practitioner des six mocks ; les lettres des réponses des mocks Foundation restent inchangées.

## Registre synthétique par scénario

| Scénario | Fichier | Notes modifiées | Options reformulées | Justifications |
|---|---|---|---|---|
| S003 | `10-practitioner-scenarios/01-context-s001-s007.md` | — | — | Justifications A/B/C/D reformulées |
| S004 | `10-practitioner-scenarios/01-context-s001-s007.md` | — | — | Justifications A/B/C/D reformulées |
| S006 | `10-practitioner-scenarios/01-context-s001-s007.md` | — | — | Justifications A/B/C/D reformulées |
| S007 | `10-practitioner-scenarios/01-context-s001-s007.md` | — | — | Justifications A/B/C/D reformulées |
| S008 | `10-practitioner-scenarios/02-stakeholders-s008-s014.md` | — | — | Justifications A/B/C/D reformulées |
| S009 | `10-practitioner-scenarios/02-stakeholders-s008-s014.md` | B 3→1; C 1→3 | B | Justifications A/B/C/D reformulées |
| S010 | `10-practitioner-scenarios/02-stakeholders-s008-s014.md` | — | — | Justifications A/B/C/D reformulées |
| S011 | `10-practitioner-scenarios/02-stakeholders-s008-s014.md` | — | — | Justifications A/B/C/D reformulées |
| S012 | `10-practitioner-scenarios/02-stakeholders-s008-s014.md` | — | — | Justifications A/B/C/D reformulées |
| S013 | `10-practitioner-scenarios/02-stakeholders-s008-s014.md` | B 3→1; C 1→3 | B | Justifications A/B/C/D reformulées |
| S014 | `10-practitioner-scenarios/02-stakeholders-s008-s014.md` | — | — | Justifications A/B/C/D reformulées |
| S015 | `10-practitioner-scenarios/03-phase-a-s015-s021.md` | — | — | Justifications A/B/C/D reformulées |
| S016 | `10-practitioner-scenarios/03-phase-a-s015-s021.md` | — | — | Justifications A/B/C/D reformulées |
| S017 | `10-practitioner-scenarios/03-phase-a-s015-s021.md` | — | — | Justifications A/B/C/D reformulées |
| S018 | `10-practitioner-scenarios/03-phase-a-s015-s021.md` | — | — | Justifications A/B/C/D reformulées |
| S019 | `10-practitioner-scenarios/03-phase-a-s015-s021.md` | A 1→3; D 3→1 | D | Justifications A/B/C/D reformulées |
| S020 | `10-practitioner-scenarios/03-phase-a-s015-s021.md` | A 3→1; B 1→3 | A | Justifications A/B/C/D reformulées |
| S023 | `10-practitioner-scenarios/04-bcd-s022-s030.md` | — | — | Justifications A/B/C/D reformulées |
| S024 | `10-practitioner-scenarios/04-bcd-s022-s030.md` | A 3→1; B 1→3 | A | Justifications A/B/C/D reformulées |
| S026 | `10-practitioner-scenarios/04-bcd-s022-s030.md` | — | — | Justifications A/B/C/D reformulées |
| S027 | `10-practitioner-scenarios/04-bcd-s022-s030.md` | — | — | Justifications A/B/C/D reformulées |
| S028 | `10-practitioner-scenarios/04-bcd-s022-s030.md` | — | — | Justifications A/B/C/D reformulées |
| S029 | `10-practitioner-scenarios/04-bcd-s022-s030.md` | — | C | Justifications A/B/C/D reformulées |
| S030 | `10-practitioner-scenarios/04-bcd-s022-s030.md` | — | — | Justifications A/B/C/D reformulées |
| S031 | `10-practitioner-scenarios/05-efg-s031-s039.md` | — | A | Justifications A/B/C/D reformulées |
| S043 | `10-practitioner-scenarios/06-phase-h-s040-s045.md` | — | — | Justifications A/B/C/D reformulées |
| S048 | `10-practitioner-scenarios/07-requirements-s046-s052.md` | — | — | Justifications A/B/C/D reformulées |
| S050 | `10-practitioner-scenarios/07-requirements-s046-s052.md` | — | D | Justifications A/B/C/D reformulées |
| S051 | `10-practitioner-scenarios/07-requirements-s046-s052.md` | — | — | Justifications A/B/C/D reformulées |
| S053 | `10-practitioner-scenarios/08-supporting-adm-s053-s060.md` | — | C | Justifications A/B/C/D reformulées |
| S056 | `10-practitioner-scenarios/08-supporting-adm-s053-s060.md` | A 3→1; B 1→3 | A | Justifications A/B/C/D reformulées |
| S057 | `10-practitioner-scenarios/08-supporting-adm-s053-s060.md` | — | C | Justifications A/B/C/D reformulées |
| S059 | `10-practitioner-scenarios/08-supporting-adm-s053-s060.md` | — | A | Justifications A/B/C/D reformulées |

## Scénarios sans modification pendant cette passe

`S001`, `S002`, `S005`, `S021`, `S022`, `S025`, `S032`, `S033`, `S034`, `S035`, `S036`, `S037`, `S038`, `S039`, `S040`, `S041`, `S042`, `S044`, `S045`, `S046`, `S047`, `S049`, `S052`, `S054`, `S055`, `S058`, `S060`.

Pour les 22 cas déjà corrigés précédemment, cette campagne a maintenu leur contenu. Le contrôle structurel les inspecte tous, **mais leur qualité pédagogique n'a pas fait l'objet d'une nouvelle contre-expertise indépendante**.

## Registre option par option

Chaque ligne donne la note avant et après, et la justification **hors répétition du texte de l'option**. Les différences d'options sont visibles dans les fichiers source et dans la PR.

| Scénario | Option | Note avant → après | Ancienne justification | Nouvelle justification |
|---|---|---|---|---|
| S003 | A | 1 → 1 | Une présentation technique n'explique pas les outcomes métier. | Le tableau d'économies apporte une première donnée de coût, mais il ne rattache aucun investissement aux capabilities et outcomes métier demandés par le comité. |
| S003 | B | 0 → 0 | Les diagrammes seuls ne répondent pas à Finance et Operations. | Une revue de conformité limitée à une application inverse les priorités : la valeur et les business drivers doivent éclairer la décision d'investissement en amont. |
| S003 | C | 5 → 5 | Les business drivers, coûts et risques démontrent la valeur pour le comité. | La liaison explicite drivers–capacités–risques–coûts relie la motivation de l'architecture aux décisions de transformation attendues. |
| S003 | D | 3 → 3 | Quelques décisions mesurables ne prouvent pas encore l'alignement stratégique. | Les décisions mesurables constituent une base de dialogue, mais l'absence de relation systématique avec les drivers stratégiques laisse la valeur globale incertaine. |
| S004 | A | 3 → 3 | Une revue par release oublie les dépendances transverses. | Des revues légères sur interfaces et risques transverses protègent l'autonomie Agile ; l'option ne prévoit toutefois pas le tailoring ADM complet ni la traçabilité inter-domaines. |
| S004 | B | 1 → 1 | L'autonomie produit ne garantit pas la cohérence inter-domaines. | La synchronisation sur les seules API traite une interface technique mais reporte les concerns métier et Data, pourtant essentiels à la cohérence des incréments. |
| S004 | C | 0 → 0 | Éliminer la gouvernance fait disparaître les engagements d'architecture. | Reporter la gouvernance à la fin du trimestre expose les produits à des écarts d'architecture avant leur intégration ; l'ADM doit accompagner les incréments. |
| S004 | D | 5 → 5 | Le tailoring ADM garde gouvernance et traçabilité dans les incréments Agile. | Le tailoring et l'itération de l'ADM maintiennent les exigences et décisions traçables tout en permettant la livraison incrémentale. |
| S006 | A | 0 → 0 | Migrer sans qualification des risques expose le service critique. | Une dérogation d'identité engagée sans évaluation transversale du risque compromet les exigences de sécurité du service critique. |
| S006 | B | 5 → 5 | Le risque et la sécurité impactent chaque architecture de domaine. | Réévaluer requirements et risques et itérer sur les domaines affectés intègre réellement la sécurité dans la Target et les décisions de migration. |
| S006 | C | 3 → 3 | La revue suivante reporte la propagation des exigences transverses. | La revue suivante est une étape utile mais tardive : la propagation immédiate des exigences dans Data, Application et Technology manque. |
| S006 | D | 1 → 1 | La seule validation du CISO ne traite pas les dépendances Data/Application. | L'audit et les critères de recette sécurisent certains échanges, mais arrivent trop tard pour réconcilier les exigences et building blocks des trois domaines. |
| S007 | A | 1 → 1 | Une fiche produit ne justifie pas la valeur du service. | La comparaison technique fournit une information de solution, mais démarre avant la définition des outcomes métier ; la valeur n'est pas encore démontrée. |
| S007 | B | 0 → 0 | Le fournisseur ne peut définir seul la Target métier. | Un Architecture Contract prématuré fixe une relation fournisseur avant que le scope et les requirements aient été clarifiés ; la gouvernance ne compense pas l'absence de Vision. |
| S007 | C | 5 → 5 | La proposition fournisseur doit être évaluée après drivers et requirements. | Clarifier les business drivers, stakeholders, scope et exigences avant le choix évite de transformer une proposition fournisseur en Target prédéfinie. |
| S007 | D | 3 → 3 | Une évaluation préliminaire ne compare pas encore toutes les options. | La clarification initiale et la comparaison avec une référence sont utiles, mais l'absence d'alternatives laisse l'arbitrage de solution incomplet. |
| S008 | A | 3 → 3 | La consultation seule ne change pas les décisions de Target. | Consulter Operations identifie ses contraintes, mais reporter la modification de l'architecture laisse les décisions de Target déjà approuvées potentiellement invalides. |
| S008 | B | 1 → 1 | La note technique ne documente pas les responsabilités de run. | Le runbook et le test de bascule traitent le pilote, mais ne couvrent ni les responsabilités d'exploitation ni les autres requirements de reprise de la Target. |
| S008 | C | 0 → 0 | Reporter l'étude à la livraison fige le risque d'exploitation. | L'acceptation par le sponsor ne remplace pas l'analyse des concerns d'Operations ni la révision des vues et responsabilités impactées. |
| S008 | D | 5 → 5 | Operations doit contribuer aux requirements de reprise et au modèle d'exploitation. | Identifier Operations comme stakeholder, capturer ses concerns et mettre à jour requirements et views relie l'architecture cible à son exploitation réelle. |
| S009 | A | 5 → 5 | Un arbitrage documenté concilie sponsor et CISO. | La gouvernance documente les arbitrages de scope, exigences métier et sécurité en impliquant les autorités appropriées ; elle rend la décision traçable. |
| S009 | B | 3 → 1 | Une mitigation partielle ne règle pas l'autorité d'acceptation. | Appliquer un contrôle standard sans analyser les impacts ni traiter le conflit d'autorité réduit le problème à une action technique et diffère l'arbitrage. |
| S009 | C | 1 → 3 | L'aval du sponsor ne remplace pas l'acceptation sécurité. | Documenter les contraintes CISO et les impacts avant arbitrage est pertinent, mais l'option ne résout pas encore l'autorité d'acceptation ni tous les concerns métier. |
| S009 | D | 0 → 0 | Ignorer le CISO crée une dérogation implicite. | Livrer sans décision d'exception sur les contrôles CISO crée une non-conformité implicite contraire à l'Architecture Governance. |
| S010 | A | 0 → 0 | Une carte périmée fausse les consultations. | Les destinataires ajoutés ne participent pas aux décisions ni à l'analyse des concerns : les validations anciennes ne suffisent pas pour le nouveau périmètre. |
| S010 | B | 5 → 5 | La carte actualisée révèle les actors et concerns réellement touchés. | Mettre à jour stakeholders, concerns, engagement et impacts sur views/requirements rétablit la traçabilité des parties concernées. |
| S010 | C | 3 → 3 | Les acteurs puissants ne couvrent pas toutes les dépendances. | Réexaminer les acteurs influents est utile, mais les acteurs moins visibles peuvent porter des contraintes et dépendances non évaluées. |
| S010 | D | 1 → 1 | Une liste de sponsors omet les acteurs opérationnels. | Réviser les rôles et risques aide la gouvernance ; reporter les vues et concerns laisse provisoirement des représentations architecturales périmées. |
| S011 | A | 1 → 1 | Un diagramme technique n'éclaire pas les capacités métier. | La synthèse métier répond partiellement à un public, mais les viewpoints ne sont pas définis pour assurer la couverture de tous les concerns. |
| S011 | B | 0 → 0 | La même vue exhaustive ne sert pas tous les décideurs. | Annoter un diagramme unique ne change pas le viewpoint : la même représentation demeure inadaptée à des préoccupations divergentes. |
| S011 | C | 5 → 5 | Les viewpoints doivent traduire les concerns de chaque public. | Des views adaptées à chaque concern, issues d'une base cohérente, appliquent la distinction TOGAF entre stakeholder, concern, viewpoint et view. |
| S011 | D | 3 → 3 | Une synthèse unique est trop vague pour les décisions spécialisées. | Des explications différenciées facilitent la communication, mais un modèle unique sans vues distinctes reste moins exploitable pour les décisions. |
| S012 | A | 3 → 3 | Un rapport périodique manque l'analyse de ses concerns. | La synthèse périodique limite les sollicitations et facilite les décisions ; l'absence de cartographie des concerns ne garantit pas qu'elle couvre les risques importants. |
| S012 | B | 1 → 1 | L'accès passif à un dossier ne suffit pas à le tenir informé. | Limiter l'échange aux arbitrages sans suivi des changements majeurs risque de surprendre un acteur doté d'un fort pouvoir. |
| S012 | C | 0 → 0 | Le solliciter en permanence surcharge sa faible disponibilité. | Une communication quotidienne surcharge inutilement un stakeholder à faible intérêt et peut dégrader son engagement. |
| S012 | D | 5 → 5 | Une communication ciblée préserve la satisfaction d'un stakeholder influent. | Tenir cet acteur satisfait grâce à des messages ciblés sur décisions, risques et impacts applique la stratégie d'engagement adaptée à forte influence/faible intérêt. |
| S013 | A | 5 → 5 | Une requirement traçable traduit une préoccupation en critère vérifiable. | RTO/RPO, reprise, observabilité, critères de test et traçabilité transforment le concern en requirements vérifiables et gouvernables. |
| S013 | B | 3 → 1 | Un besoin formulé sans critères est difficile à tester. | Une simple cible indicative sans seuil ni mesure ne permet pas de tester le résultat ni de relier le concern à une décision d'architecture. |
| S013 | C | 1 → 3 | Une note de réunion ne garantit pas la traçabilité. | Une disponibilité chiffrée et un atelier permettent de démarrer la spécification ; manquent encore RTO/RPO, conditions de mesure, ownership et traçabilité complète. |
| S013 | D | 0 → 0 | Choisir directement un produit court-circuite le besoin. | Déduire le critère des limites du produit existant plutôt que du concern et éviter la faisabilité produit une requirement non justifiée. |
| S014 | A | 0 → 0 | L'accord d'architecture n'efface pas les requirements métier. | Le sponsor ne peut remplacer l'analyse des concerns métier par une approbation provisoire suivie d'une revue en Phase G ; l'acceptation métier reste ouverte. |
| S014 | B | 5 → 5 | Conformité Board et acceptation métier portent sur des responsabilités distinctes. | Distinguer autorité du Board et acceptation métier, puis réviser views/requirements et soumettre les arbitrages traite les deux décisions. |
| S014 | C | 3 → 3 | Les validations séparées manquent de réconciliation des concerns. | Faire suivre la conformité par l'acceptation métier est utile, mais des validations séquentielles sans réconciliation préalable peuvent entraîner de nouveaux écarts. |
| S014 | D | 1 → 1 | Le Board ne peut accepter à lui seul la valeur métier. | La liste d'impacts du Business Owner informe le Board, mais ne remplace ni la mise à jour des requirements ni l'acceptation par les parties métier. |
| S015 | A | 1 → 1 | Un backlog sans drivers ne justifie pas le travail d'architecture. | Comparer des plateformes avant d'avoir établi la valeur et le scope ancre trop tôt le débat sur la solution au lieu de la Vision. |
| S015 | B | 0 → 0 | Choisir directement les technologies contourne la Vision. | Élaborer le plan de migration avant une Architecture Vision inverse l'ordre du cadrage et expose le programme à des lots sans mandat. |
| S015 | C | 5 → 5 | Phase A clarifie drivers, stakeholders, scope et Vision avant la cible. | La Phase A construit la Vision à partir des drivers, stakeholders, périmètre et valeur attendue avant de figer les solutions. |
| S015 | D | 3 → 3 | Une réunion métier peut cadrer un besoin mais pas confirmer le mandat. | Le cadrage de Vision avec stakeholders est une bonne entrée, mais l'hypothèse de plateforme ne doit pas remplacer l'analyse d'alternatives et d'impacts. |
| S016 | A | 3 → 3 | Une mise à jour de governance doit être distinguée du cadrage métier A. | Vérifier l'adéquation des principes et instances est utile ; l'option ne confirme pas explicitement toute l'Architecture Capability avant de cadrer Phase A. |
| S016 | B | 1 → 1 | Des principes ne suffisent pas à établir le travail architectural demandé. | Vérifier les impacts réglementaires et réutiliser Board/Repository protège une partie des contrôles, mais omet l'examen des autres rôles et pratiques de gouvernance. |
| S016 | C | 0 → 0 | Confondre les phases conduit à un mandat incomplet. | Recommencer tout Preliminary sans raison proportionnée et retarder Phase A ne répond pas au besoin d'architecture du projet. |
| S016 | D | 5 → 5 | Preliminary prépare la capacité d'architecture ; A traite la Vision du projet. | Adapter au besoin la capability construite en Preliminary, puis cadrer la Vision propre à l'initiative en Phase A, distingue correctement les finalités. |
| S017 | A | 5 → 5 | La Vision doit traduire des drivers en outcomes et valeur mesurable. | Relier drivers, outcomes, valeur, risques et mesures de succès donne au sponsor une Architecture Vision permettant une décision éclairée. |
| S017 | B | 3 → 3 | Un premier KPI aide mais la justification de transformation reste lacunaire. | Des KPI et hypothèses de valeur renforcent la Vision, mais stakeholder concerns et exigences restent à consolider. |
| S017 | C | 1 → 1 | Un diagramme technique ne démontre pas la proposition de valeur. | Un business case succinct et des indicateurs apportent un début d'argument économique ; sans lien aux stakeholders et requirements, la Vision demeure insuffisamment justifiée. |
| S017 | D | 0 → 0 | Un projet sans bénéfice démontré n'a pas de raison architecturale. | Enrichir les diagrammes applicatifs démontre la structure de la solution, mais pas sa valeur, ses outcomes ni les concerns du sponsor. |
| S018 | A | 0 → 0 | Étendre le scope sans arbitrage fragilise calendrier et coût. | Inclure toutes les directions dans le scope sans arbitrage de valeur et capacité de delivery risque de créer une architecture trop large et peu finançable. |
| S018 | B | 5 → 5 | Définir les dimensions du scope évite une architecture exhaustive et hors mandat. | Le scoping documente drivers, valeur, capacité de delivery, in-scope/out-of-scope et suites éventuelles pour maîtriser l'Architecture Vision. |
| S018 | C | 3 → 3 | Un périmètre partiel aide mais ne délimite pas les interdépendances critiques. | Figer le périmètre avant d'analyser les demandes nouvelles évite une dérive immédiate, mais ne traite pas leurs dépendances ni la justification de l'exclusion. |
| S018 | D | 1 → 1 | Une limite applicative seule ignore données et métier. | Prioriser Payments et consigner les demandes adjacentes est un premier cadrage, mais l'arbitrage du scope et des interdépendances reste à valider. |
| S019 | A | 1 → 3 | Un choix de solution ne traite pas les compétences des équipes. | Diagnostiquer les compétences et chiffrer leur acquisition prépare concrètement la readiness ; la traçabilité globale des risques et impacts dans la trajectoire reste à intégrer. |
| S019 | B | 0 → 0 | Ignorer Operations reporte une incapacité de mise en service. | Maintenir le calendrier puis réévaluer la readiness après la première production reporte un risque d'exploitation connu à un moment irréversible. |
| S019 | C | 5 → 5 | La readiness doit être examinée dès la Vision pour crédibiliser le projet. | Évaluer la capacité de transformation comme risque architectural et intégrer les actions de montée en compétence dans la roadmap traite la readiness de bout en bout. |
| S019 | D | 3 → 1 | Un risque d'adoption signalé ne crée pas les capacités manquantes. | Annoncer une phase de formation sans évaluer les capacités réellement manquantes ni leur financement reste une intention partielle. |
| S020 | A | 3 → 1 | Une consultation ciblée apporte un avis mais laisse d'autres exigences hors du mandat. | Une présentation de la Vision aux responsables concernés, sans collecte des concerns ni mise à jour des décisions, fournit une information mais pas une nouvelle validation métier. |
| S020 | B | 1 → 3 | Une validation sponsor seule ne vaut pas acceptation des utilisateurs. | La consultation des trois responsables et la liste de concerns constituent une étape substantielle ; les impacts doivent encore modifier la Vision et les requirements avant approbation. |
| S020 | C | 0 → 0 | Poursuivre malgré les désaccords invalide la Vision commune. | Maintenir la Vision et repousser les exigences à la construction fait courir le risque d'une solution non acceptée et invalide le cadrage. |
| S020 | D | 5 → 5 | Les stakeholders concernés doivent valider leurs concerns avant d'autoriser la suite. | Réviser stakeholders, concerns, impacts, Vision et exigences avant autorisation assure une gouvernance cohérente de la Phase A. |
| S023 | A | 1 → 1 | L'inventaire exhaustif coûte du temps sans bénéfice proportionné. | Une Baseline ciblée et un registre d'hypothèses évitent l'inventaire exhaustif, mais les critères de suffisance et de dépendances restent à consolider. |
| S023 | B | 0 → 0 | Ignorer l'existant prive l'architecte de base de comparaison. | Concevoir la Target sans aucune dépendance actuelle reporte les gaps et fragilise les travaux de migration. |
| S023 | C | 5 → 5 | Une Baseline proportionnée donne les informations nécessaires pour calculer les gaps. | Documenter seulement l'existant nécessaire au périmètre, aux impacts et aux gaps rend la Baseline proportionnée à la décision. |
| S023 | D | 3 → 3 | Les processus critiques constituent une première sélection sans critère de suffisance. | Restreindre la collecte aux seuls processus désignés sans critère de suffisance risque d'ignorer interfaces et dépendances critiques. |
| S024 | A | 3 → 1 | Un schéma SQL clarifie le stockage sans la gouvernance des données. | Recenser quelques entités techniques est une première observation, mais ne décrit ni les propriétaires, ni la gouvernance, ni le cycle de vie ; PostgreSQL reste une hypothèse de solution non justifiée. |
| S024 | B | 1 → 3 | Une liste d'entités peut aider sans clarifier ownership et signification. | Entités, flux et sensibilité caractérisent la Data Architecture, mais la gouvernance, le cycle de vie et l'ownership doivent encore être traités. |
| S024 | C | 0 → 0 | La sélection du SGBD ne remplace pas les exigences Data. | Déduire gouvernance et organisation des données d'un benchmark de SGBD inverse besoin métier et choix technologique. |
| S024 | D | 5 → 5 | La Data Architecture traite informations, usages, propriétaires et règles de cycle de vie. | Entities, ownership, lifecycle, quality, flows et exigences produisent une Data Architecture complète indépendamment du SGBD choisi. |
| S026 | A | 0 → 0 | Choisir le produit avant les besoins contredit la séquence de décision. | Dérogations aux objectifs de résilience sans analyse des flux B/C risquent de masquer une incompatibilité de la Target Technology avec les requirements. |
| S026 | B | 5 → 5 | Les choix de D doivent servir les besoins des domaines B et C et leurs contraintes. | Raccorder building blocks et requirements des phases B/C aux choix D et aux gaps assure la cohérence de l'architecture cible. |
| S026 | C | 3 → 3 | Une étude de plateformes amorce la cible, mais ne réconcilie pas les requirements. | L'analyse d'impact explicite les besoins non couverts, mais la cible standard n'est pas encore révisée ni les gaps reconsolidés. |
| S026 | D | 1 → 1 | Un standard technique peut être réutilisé sans démontrer la compatibilité globale. | Tester le socle standard apporte des preuves de performance, sans démontrer qu'il satisfait tous les requirements métier, Data et Application. |
| S027 | A | 1 → 1 | Une difficulté technique isolée ne suffit pas à construire la trajectoire. | Un chantier commun Data/Application lance la coordination transverse, mais la consolidation des gaps métier et Technology reste à expliciter avant la trajectoire. |
| S027 | B | 0 → 0 | Planifier des lots sans gaps consolidés rend les dépendances invisibles. | Déployer une infrastructure événementielle avant de définir les besoins métier revient à financer une solution sans gaps consolidés. |
| S027 | C | 5 → 5 | Les gaps des domaines doivent être réconciliés pour révéler les dépendances. | Tracer les impacts cross-domain et consolider les gaps avant Phase E relie les décisions B, C et D à des work packages justifiables. |
| S027 | D | 3 → 3 | Une liste de gaps séparés est utile mais ne décrit pas leurs impacts mutuels. | Enregistrer le gap et sa dépendance à une analyse future rend le risque visible, mais ne réconcilie pas encore les impacts entre domaines. |
| S028 | A | 3 → 3 | Modéliser une interface fournit une vue partielle des dépendances d'information. | Différer la réouverture de la Data Architecture jusqu'à l'approbation du modèle applicatif peut figer provisoirement des décisions incohérentes. |
| S028 | B | 1 → 1 | Une liste de messages ne décrit ni consommateurs ni ownership. | Une hypothèse Data explicitement provisoire et un impact sur les services amorcent une itération, mais interfaces et requirements restent à réconcilier. |
| S028 | C | 0 → 0 | Figer l'un des domaines sans consulter l'autre casse la cohérence. | Approuver séparément Data et Application et reporter les conflits en dérogation après la production détruit la cohérence de Phase C. |
| S028 | D | 5 → 5 | Les phases C Data et Application s'influencent et exigent des itérations. | Itérer entre Data et Application jusqu'à satisfaire les requirements garantit une Target cohérente et traçable. |
| S029 | A | 5 → 5 | La vue métier doit traiter les capabilities et concerns du décideur. | Le viewpoint sélectionné en fonction des concerns donne au directeur une view métier lisible des capacités, services et impacts. |
| S029 | B | 3 → 3 | Une vue simplifiée aide sans sélectionner encore le viewpoint adapté. | Une vue simplifiée des services en complément du réseau constitue une aide immédiate ; faute de viewpoint formalisé, elle peut manquer certains concerns. |
| S029 | C | 1 → 1 | Le seul réseau répond plutôt à Operations qu'aux résultats métiers. | Le catalogue de services et propriétaires apporte une information métier isolée, mais ne montre pas visuellement les transformations ni les concerns pertinents. |
| S029 | D | 0 → 0 | Une représentation universelle ne traite pas les préoccupations spécifiques. | Ajouter des bénéfices marginaux au diagramme de plateforme ne répond pas aux concerns du directeur métier et maintient une vue inadaptée. |
| S030 | A | 0 → 0 | L'attente de G laisse les décisions de Target non conformes. | Approuver un hébergement local sans analyser les flux Data/Application affectés crée une cible incohérente avec les exigences découvertes. |
| S030 | B | 5 → 5 | Une requirement découverte en D doit être tracée vers C/B et la migration. | Requirements Management traite la nouvelle exigence comme un changement traçable, avec itérations B/C/D et mise à jour des gaps. |
| S030 | C | 3 → 3 | La prendre en compte en D seulement laisse les autres modèles périmés. | La correction de Technology et la demande de changement sont utiles, mais la réconciliation immédiate des impacts métier et Data n'est pas menée. |
| S030 | D | 1 → 1 | Le ticket initial n'identifie pas encore les systèmes impactés. | Corriger d'abord le schéma d'hébergement et décaler les flux laisse les requirements transverses partiellement non satisfaits. |
| S031 | A | 1 → 1 | Le détail des tâches techniques ne prouve pas la valeur des transformations. | Les dépendances les plus visibles amorcent une première estimation, mais sans rapprochement des gaps métier, Data, Application et Technology les work packages restent non justifiés. |
| S031 | B | 0 → 0 | Séquencer des produits sans analyser les gaps est prématuré. | Planifier selon la seule disponibilité des équipes avant de traiter les gaps et prérequis ne peut produire une migration finançable et cohérente. |
| S031 | C | 5 → 5 | Consolider gaps, options, work packages et transitions relie la Target au plan. | La consolidation cross-domain, les SBB candidats, work packages et Transition Architectures forment la sortie utile de Phase E. |
| S031 | D | 3 → 3 | Un premier lot constitue une option mais laisse les autres dépendances ouvertes. | Regrouper les gaps et chiffrer des lots provisoires rend une trajectoire possible ; les dépendances et solutions candidates demandent encore une évaluation. |
| S043 | A | 1 → 1 | Un inventaire technique ne contient pas les états d'architecture. | La correction des diagrammes critiques est utile, mais la réconciliation partielle des décisions/dispensations ne garantit pas l'intégrité de l'Architecture Landscape. |
| S043 | B | 0 → 0 | Utiliser un Repository obsolète fausse les arbitrages de migration. | Déduire automatiquement une Target approuvée du dernier déploiement renverse le contrôle de conformité et efface les décisions historiques sans arbitrage. |
| S043 | C | 5 → 5 | Le Landscape doit rester cohérent avec les décisions et les services livrés. | Maintenir le Landscape avec les changements approuvés et surveiller les dérives relie architecture de référence, solutions déployées et gouvernance Phase H. |
| S043 | D | 3 → 3 | La mise à jour ponctuelle ne règle pas le processus de maintenance. | Mettre à jour les views affectées est une bonne première opération, mais l'absence de réconciliation complète laisse une dette de traçabilité. |
| S048 | A | 3 → 3 | Une liaison à l'application est utile, mais laisse les données hors traçabilité. | Le composant principal et le critère de test donnent un premier lien d'implémentation, mais la source du concern et les dépendances transverses restent incomplètes. |
| S048 | B | 1 → 1 | Un identifiant de ticket ne prouve pas que la requirement est satisfaite. | Lier l'exigence à une obligation ou stakeholder restaure une partie de son origine, mais la revue rapide ne relie pas encore sa portée aux artifacts et building blocks. |
| S048 | C | 0 → 0 | Une requirement sans lien reste impossible à vérifier après évolution. | Appliquer indistinctement le contrôle à tous les flux, puis négocier les exceptions en implémentation, évite l'analyse d'applicabilité et compromet la conformité. |
| S048 | D | 5 → 5 | La relation requirement→building blocks permet de calculer les impacts. | Tracer la source et les concerns, puis déterminer les artifacts et building blocks affectés permet l'impact analysis et la vérification de la requirement. |
| S050 | A | 0 → 0 | Une suppression sans traçabilité détruit la justification antérieure. | Supprimer les contraintes dès l'abrogation de la politique sans évaluer leurs autres sources ni conserver les décisions détruit la traçabilité. |
| S050 | B | 5 → 5 | Les exigences obsolètes demandent une décision et un historique gouvernés. | Une requalification gouvernée de la requirement, avec source, décision, versionnement et impacts, applique Requirements Management. |
| S050 | C | 3 → 3 | Un statut local aide mais n'actualise pas les autres livrables. | La revalidation auprès du sponsor et la conservation des versions protègent l'historique, mais les autres sources et impacts architecturaux restent à vérifier. |
| S050 | D | 1 → 1 | Conserver toutes les exigences actives crée des contradictions. | Consigner la demande de modification sans examiner les dépendances et les usages de la requirement ne suffit pas à décider de son retrait ou maintien. |
| S051 | A | 1 → 1 | Un standard local ne remplace pas le principe transversal. | Une requirement mesurable sur les secrets est utile, mais reporter les implications du principe sans expliciter sa portée fragilise la traçabilité de la décision. |
| S051 | B | 0 → 0 | Confondre les deux niveaux fausse les exigences applicables. | Transformer le choix d'un produit de secrets en principe d'entreprise permanent confond un standard contingent avec une règle directrice stable. |
| S051 | C | 5 → 5 | Principe durable et requirement testable restent deux catégories distinctes. | Le principe oriente les décisions durables, tandis qu'une requirement ou un standard défini pour le contexte doit être vérifiable et tracé. |
| S051 | D | 3 → 3 | Dériver une requirement est utile mais les implications restent à tracer. | Conserver le principe et en dériver une exigence mesurable respecte les niveaux d'abstraction, mais les implications du principe restent à formaliser. |
| S053 | A | 5 → 5 | Le Business Scenario relie acteurs, problème, environnement et outcomes. | Le Business Scenario explicite ensemble problème, acteurs, environnement, outcomes et requirements ; il permet de valider la demande avant le choix d'une solution. |
| S053 | B | 3 → 3 | Décrire le parcours actuel est une entrée, pas un scénario cible. | L'entretien structuré recueille objectifs, acteurs et indicateurs en vue du Business Scenario ; la formalisation et la validation du scénario restent différées. |
| S053 | C | 1 → 1 | Un seul diagramme technique n'explique pas la demande métier. | Un seul indicateur de latence, sans analyse du problème ni du contexte métier, ne permet pas d'établir des outcomes et requirements suffisants pour le Business Scenario. |
| S053 | D | 0 → 0 | Choisir le fournisseur avant le scénario inverse besoin et solution. | Fonder la latence sur l'offre fournisseur avant de clarifier la valeur et le besoin inverse l'enchaînement business scenario → requirements → solutions. |
| S056 | A | 3 → 1 | Une mesure sans owner laisse l'acceptation du risque ambiguë. | Suivre la mitigation sans recalcul du risque résiduel ni responsable identifié laisse le dépassement du seuil sans décision de gouvernance et reporte l'acceptation. |
| S056 | B | 1 → 3 | Un score de risque initial seul ne prouve pas son traitement. | Garder le risque ouvert et demander une estimation actualisée avec le métier est une démarche utile ; l'ownership et l'escalade au bon niveau ne sont pas encore obtenus. |
| S056 | C | 0 → 0 | Cacher le risque résiduel empêche toute acceptation éclairée. | Abaisser arbitrairement la gravité puis différer la revue masque un risque résiduel au-dessus de la tolérance d'Operations. |
| S056 | D | 5 → 5 | Une mitigation doit être suivie de la mesure du risque résiduel. | Qualifier risque initial et résiduel, propriétaires, mitigation et acceptation ou escalade appropriée fournit une décision traçable et conforme à la tolérance. |
| S057 | A | 5 → 5 | Capability-Based Planning relie outcomes et investissements aux capacités. | Le Capability-Based Planning rattache outcomes et capacités aux investissements, building blocks, work packages et dépendances, ce que demande Finance. |
| S057 | B | 3 → 3 | Une capability map initie le travail sans prioriser les work packages. | La carte des capabilities reliée aux produits amorce la justification métier ; sans gaps ni priorisation des work packages, l'arbitrage budgétaire reste incomplet. |
| S057 | C | 1 → 1 | Un inventaire applicatif ne mesure pas les capacités manquantes. | L'inventaire Kafka/Kubernetes/API Gateway fournit des informations de fonctions techniques, mais ne caractérise ni les capabilities manquantes ni les résultats métier visés. |
| S057 | D | 0 → 0 | Partir des produits déployés plutôt que des besoins biaise la Roadmap. | Financer le produit le moins cher sans évaluer les capabilities et outcomes transforme une contrainte budgétaire en décision d'architecture non justifiée. |
| S059 | A | 1 → 1 | Un composant de solution n'est pas un document d'architecture. | Un catalogue technique identifie des composants potentiels, mais ne corrige pas la confusion entre deliverable formel, artifact de représentation et building block. |
| S059 | B | 0 → 0 | Confondre les catégories détruit la traçabilité entre intention et réalisation. | Considérer un diagramme et une annexe de standards comme livrable complet confond une représentation partielle avec un produit de travail gouverné. |
| S059 | C | 5 → 5 | Le Framework distingue deliverable formel, artifact et building block. | La distinction explicite entre deliverable formel, artifacts constitutifs et building blocks représentés répond au besoin du comité de validation. |
| S059 | D | 3 → 3 | Un diagramme seul ne décrit pas toutes les obligations du livrable. | Requalifier l'artifact et identifier les building blocks constitue une remise en ordre correcte, mais la composition complète du deliverable doit encore être définie. |

## Vérifications et limites

Les tests automatiques vérifient la structure, le barème, le préfixe exact de l'option dans chaque explication, les formulations obsolètes ciblées et la distribution des meilleures lettres. Ils **ne peuvent pas démontrer à eux seuls** qu'une option vaut exactement 3 ou 1 point selon un examinateur indépendant. Une seconde revue humaine est recommandée avant de considérer les cas S comme matériel pédagogiquement calibré.
