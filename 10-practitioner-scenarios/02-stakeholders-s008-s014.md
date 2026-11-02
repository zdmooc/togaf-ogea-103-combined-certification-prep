# Practitioner Scenarios — Stakeholder Management

## S008 — Operations découvre la cible trop tard

Le sponsor et l’équipe projet ont approuvé une cible de paiement. Lors d’une revue tardive, Operations refuse le modèle car il n’existe ni run model clair, ni stratégie de support, ni exigences de bascule exploitables.

Le modèle cible comporte plusieurs services en disponibilité étendue et une migration progressive avec coexistence de l'ancien SI. Le pilote doit commencer dans un mois. Le sponsor refuse une réouverture générale du programme, mais Operations précise qu'aucun responsable d'astreinte ni exercice de reprise n'a été défini. Le Board attend une décision fondée sur les risques opérationnels.

Quelle action est la meilleure ?
A. Consulter Operations et consigner ses principales contraintes d'exploitation pour la prochaine revue d'architecture, sans réviser immédiatement toutes les décisions.
B. Exiger au minimum un runbook et un test de bascule pour le pilote, puis formaliser ultérieurement les autres requirements d'exploitation.
C. Faire confirmer au sponsor l'acceptation du risque opérationnel, sans modifier les représentations ou responsabilités déjà approuvées.
D. Reconnaître Operations comme stakeholder critique, comprendre ses concerns, produire les vues nécessaires et intégrer les requirements opérationnels dans l’architecture.
**Scoring : A=3, B=1, C=0, D=5.**

**Justification des quatre niveaux :**

- **D — 5 points :** Reconnaître Operations comme stakeholder critique, comprendre ses concerns, produire les vues nécessaires et intégrer les requirements opérationnels dans l’architecture. Identifier Operations comme stakeholder, capturer ses concerns et mettre à jour requirements et views relie l'architecture cible à son exploitation réelle.
- **A — 3 points :** Consulter Operations et consigner ses principales contraintes d'exploitation pour la prochaine revue d'architecture, sans réviser immédiatement toutes les décisions. Consulter Operations identifie ses contraintes, mais reporter la modification de l'architecture laisse les décisions de Target déjà approuvées potentiellement invalides.
- **B — 1 points :** Exiger au minimum un runbook et un test de bascule pour le pilote, puis formaliser ultérieurement les autres requirements d'exploitation. Le runbook et le test de bascule traitent le pilote, mais ne couvrent ni les responsabilités d'exploitation ni les autres requirements de reprise de la Target.
- **C — 0 points :** Faire confirmer au sponsor l'acceptation du risque opérationnel, sans modifier les représentations ou responsabilités déjà approuvées. L'acceptation par le sponsor ne remplace pas l'analyse des concerns d'Operations ni la révision des vues et responsabilités impactées.

**Mapping : Stakeholder Management — Concerns, Views, Requirements.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 2 ; TOGAF Standard, ADM et Series Guides applicables.

---
## S009 — Sponsor contre CISO

Le sponsor veut une mise en production en trois mois. Le CISO exige des contrôles qui peuvent ajouter plusieurs semaines. Les deux parties considèrent leur priorité comme non négociable.

La date avancée dépend d'un lancement commercial ; les exigences de sécurité portent sur des accès privilégiés et une preuve d'audit réglementaire. Une option de lancement limité existe mais n'a pas été chiffrée. Le comité d'architecture doit présenter une trajectoire défendable, en laissant aux autorités désignées la responsabilité d'accepter les risques résiduels.

Quelle approche est la plus appropriée ?
A. Clarifier les concerns, contraintes et requirements, rendre visibles les impacts et arbitrages, puis utiliser la gouvernance appropriée pour obtenir une décision traçable.
B. Appliquer provisoirement un contrôle standard proposé par le CISO sans analyser les impacts métiers ni organiser l'arbitrage du conflit.
C. Documenter les exigences minimales non négociables du CISO et étudier les impacts calendaires avant l'arbitrage formel du sponsor.
D. Réduire le périmètre du produit au pilote commercial et traiter les contrôles de sécurité durant une seconde release, sans décision d'exception.
**Scoring : A=5, B=1, C=3, D=0.**

**Justification des quatre niveaux :**

- **A — 5 points :** Clarifier les concerns, contraintes et requirements, rendre visibles les impacts et arbitrages, puis utiliser la gouvernance appropriée pour obtenir une décision traçable. La gouvernance documente les arbitrages de scope, exigences métier et sécurité en impliquant les autorités appropriées ; elle rend la décision traçable.
- **B — 1 points :** Appliquer provisoirement un contrôle standard proposé par le CISO sans analyser les impacts métiers ni organiser l'arbitrage du conflit. Appliquer un contrôle standard sans analyser les impacts ni traiter le conflit d'autorité réduit le problème à une action technique et diffère l'arbitrage.
- **C — 3 points :** Documenter les exigences minimales non négociables du CISO et étudier les impacts calendaires avant l'arbitrage formel du sponsor. Documenter les contraintes CISO et les impacts avant arbitrage est pertinent, mais l'option ne résout pas encore l'autorité d'acceptation ni tous les concerns métier.
- **D — 0 points :** Réduire le périmètre du produit au pilote commercial et traiter les contrôles de sécurité durant une seconde release, sans décision d'exception. Livrer sans décision d'exception sur les contrôles CISO crée une non-conformité implicite contraire à l'Architecture Governance.

**Mapping : Stakeholder Management — Conflicting Concerns / Governance.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 2 ; TOGAF Standard, ADM et Series Guides applicables.

---
## S010 — Carte de stakeholders devenue obsolète

Pendant Phase C, MayaBank fusionne deux directions opérationnelles. De nouveaux responsables apparaissent et les responsabilités sur la donnée changent. L’équipe souhaite garder la stakeholder map de Phase A pour « ne pas rouvrir le cadrage ».

Le regroupement change le data ownership et le modèle de support de deux applications critiques. La cible reste approuvée mais les futurs responsables refusent de signer les exigences de conservation. Un jalon de validation C Data est imminent. La direction souhaite éviter toute remise à plat, tout en disposant d'une traçabilité claire des décisions et des changements de parties prenantes.

Quelle action est la meilleure ?
A. Conserver les anciennes validations tout en ajoutant les nouveaux responsables comme simples destinataires du rapport d'architecture.
B. Mettre à jour la stakeholder map, les concerns et les plans d’engagement, puis vérifier l’impact sur requirements et vues.
C. Mettre à jour les stakeholders les plus influents et leurs préoccupations, sans refaire encore la cartographie complète des dépendances.
D. Mettre à jour les rôles de décision et le registre des risques, puis reporter la révision des views et concerns après la validation de la Data Architecture.
**Scoring : A=0, B=5, C=3, D=1.**

**Justification des quatre niveaux :**

- **B — 5 points :** Mettre à jour la stakeholder map, les concerns et les plans d’engagement, puis vérifier l’impact sur requirements et vues. Mettre à jour stakeholders, concerns, engagement et impacts sur views/requirements rétablit la traçabilité des parties concernées.
- **C — 3 points :** Mettre à jour les stakeholders les plus influents et leurs préoccupations, sans refaire encore la cartographie complète des dépendances. Réexaminer les acteurs influents est utile, mais les acteurs moins visibles peuvent porter des contraintes et dépendances non évaluées.
- **D — 1 points :** Mettre à jour les rôles de décision et le registre des risques, puis reporter la révision des views et concerns après la validation de la Data Architecture. Réviser les rôles et risques aide la gouvernance ; reporter les vues et concerns laisse provisoirement des représentations architecturales périmées.
- **A — 0 points :** Conserver les anciennes validations tout en ajoutant les nouveaux responsables comme simples destinataires du rapport d'architecture. Les destinataires ajoutés ne participent pas aux décisions ni à l'analyse des concerns : les validations anciennes ne suffisent pas pour le nouveau périmètre.

**Mapping : Stakeholder Management — Continuous Engagement.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 2 ; TOGAF Standard, ADM et Series Guides applicables.

---
## S011 — Un diagramme pour tout le monde

L’architecte prépare un diagramme technique de 80 composants et veut l’utiliser pour le comité exécutif, le CISO, les équipes métier et les SRE.

Le comité exécutif doit arbitrer un investissement tandis que les SRE veulent vérifier les dépendances de reprise et le CISO le modèle de confiance. Le même contenu de référence peut être réutilisé, mais leurs préoccupations et leur niveau d'abstraction diffèrent. Le directeur métier ne dispose que de vingt minutes pour décider ; les architectes doivent préserver la cohérence sans imposer la même représentation à tous.

Quelle approche est la meilleure ?
A. Produire une synthèse métier et réserver le schéma exhaustif aux revues techniques, sans encore formaliser explicitement les viewpoints.
B. Ajouter des légendes et des annotations de risques au diagramme unique, puis demander aux différents acteurs de formuler leurs questions.
C. Produire des views adaptées aux concerns des stakeholders, construites à partir d’une base architecturale cohérente.
D. Conserver un modèle d'architecture partagé, mais préparer des explications distinctes pour les principaux groupes de stakeholders.
**Scoring : A=1, B=0, C=5, D=3.**

**Justification des quatre niveaux :**

- **C — 5 points :** Produire des views adaptées aux concerns des stakeholders, construites à partir d’une base architecturale cohérente. Des views adaptées à chaque concern, issues d'une base cohérente, appliquent la distinction TOGAF entre stakeholder, concern, viewpoint et view.
- **D — 3 points :** Conserver un modèle d'architecture partagé, mais préparer des explications distinctes pour les principaux groupes de stakeholders. Des explications différenciées facilitent la communication, mais un modèle unique sans vues distinctes reste moins exploitable pour les décisions.
- **A — 1 points :** Produire une synthèse métier et réserver le schéma exhaustif aux revues techniques, sans encore formaliser explicitement les viewpoints. La synthèse métier répond partiellement à un public, mais les viewpoints ne sont pas définis pour assurer la couverture de tous les concerns.
- **B — 0 points :** Ajouter des légendes et des annotations de risques au diagramme unique, puis demander aux différents acteurs de formuler leurs questions. Annoter un diagramme unique ne change pas le viewpoint : la même représentation demeure inadaptée à des préoccupations divergentes.

**Mapping : Stakeholder Management — Viewpoints and Views.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 2 ; TOGAF Standard, ADM et Series Guides applicables.

---
## S012 — Forte influence, faible intérêt

Un directeur infrastructure a un fort pouvoir d’arbitrage mais peu d’intérêt quotidien pour la transformation. L’équipe lui envoie chaque jour tous les détails de conception, ce qui provoque une perte d’attention.

Le directeur siège au comité d'investissement mais n'intervient pas dans les choix d'interfaces. Il doit néanmoins être informé de toute variation de budget ou d'orientation stratégique. Les équipes produit souhaitent maintenir une information détaillée sans créer de fatigue décisionnelle. Une réunion de jalon important aura lieu dans deux semaines ; la stratégie d'engagement doit rester proportionnée.

Quelle action est la meilleure ?
A. Prévoir une synthèse décisionnelle périodique pour cet acteur et garder les détails accessibles à la demande, sans cartographier tous ses concerns.
B. Limiter ses interactions aux points d'arbitrage formels, avec un résumé en amont mais sans prévoir de suivi lors d'une évolution majeure.
C. Maintenir la communication quotidienne sous forme de compte rendu condensé, puis réduire la fréquence après le prochain jalon.
D. Maintenir le stakeholder satisfait avec une communication ciblée sur décisions, risques et impacts, sans le surcharger.
**Scoring : A=3, B=1, C=0, D=5.**

**Justification des quatre niveaux :**

- **D — 5 points :** Maintenir le stakeholder satisfait avec une communication ciblée sur décisions, risques et impacts, sans le surcharger. Tenir cet acteur satisfait grâce à des messages ciblés sur décisions, risques et impacts applique la stratégie d'engagement adaptée à forte influence/faible intérêt.
- **A — 3 points :** Prévoir une synthèse décisionnelle périodique pour cet acteur et garder les détails accessibles à la demande, sans cartographier tous ses concerns. La synthèse périodique limite les sollicitations et facilite les décisions ; l'absence de cartographie des concerns ne garantit pas qu'elle couvre les risques importants.
- **B — 1 points :** Limiter ses interactions aux points d'arbitrage formels, avec un résumé en amont mais sans prévoir de suivi lors d'une évolution majeure. Limiter l'échange aux arbitrages sans suivi des changements majeurs risque de surprendre un acteur doté d'un fort pouvoir.
- **C — 0 points :** Maintenir la communication quotidienne sous forme de compte rendu condensé, puis réduire la fréquence après le prochain jalon. Une communication quotidienne surcharge inutilement un stakeholder à faible intérêt et peut dégrader son engagement.

**Mapping : Stakeholder Management — Influence / Interest.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 2 ; TOGAF Standard, ADM et Series Guides applicables.

---
## S013 — Du concern à la requirement

Le responsable Operations dit : « je ne veux plus passer mes nuits à gérer des bascules manuelles ». L’équipe copie cette phrase telle quelle dans l’Architecture Requirements Specification.

Le service concerne des paiements critiques et un objectif de bascule automatique en moins de deux minutes est envisagé. Les SRE considèrent qu'un temps de rétablissement et un seuil de perte de données doivent être définis séparément. Le métier n'a pas validé ces chiffres et le sponsor attend un critère de recette opposable avant de signer la prochaine Architecture Requirements Specification.

Quelle action est la meilleure ?
A. Transformer le concern en requirements vérifiables sur failover, automatisation, RTO/RPO, observabilité et tests, tout en gardant la traçabilité vers le stakeholder.
B. Inscrire seulement « haute disponibilité » comme cible indicative, sans fixer encore ni seuil, ni mesure, ni propriétaire.
C. Enregistrer une exigence de disponibilité chiffrée et préparer un atelier de clarification ultérieur avec le métier et les SRE.
D. Définir provisoirement le critère à partir des capacités du produit actuel, puis demander au sponsor une approbation sans tests de faisabilité.
**Scoring : A=5, B=1, C=3, D=0.**

**Justification des quatre niveaux :**

- **A — 5 points :** Transformer le concern en requirements vérifiables sur failover, automatisation, RTO/RPO, observabilité et tests, tout en gardant la traçabilité vers le stakeholder. RTO/RPO, reprise, observabilité, critères de test et traçabilité transforment le concern en requirements vérifiables et gouvernables.
- **B — 1 points :** Inscrire seulement « haute disponibilité » comme cible indicative, sans fixer encore ni seuil, ni mesure, ni propriétaire. Une simple cible indicative sans seuil ni mesure ne permet pas de tester le résultat ni de relier le concern à une décision d'architecture.
- **C — 3 points :** Enregistrer une exigence de disponibilité chiffrée et préparer un atelier de clarification ultérieur avec le métier et les SRE. Une disponibilité chiffrée et un atelier permettent de démarrer la spécification ; manquent encore RTO/RPO, conditions de mesure, ownership et traçabilité complète.
- **D — 0 points :** Définir provisoirement le critère à partir des capacités du produit actuel, puis demander au sponsor une approbation sans tests de faisabilité. Déduire le critère des limites du produit existant plutôt que du concern et éviter la faisabilité produit une requirement non justifiée.

**Mapping : Stakeholder Management — Concern → Requirement.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 2 ; TOGAF Standard, ADM et Series Guides applicables.

---
## S014 — Architecture Board et acceptation métier

L’Architecture Board valide une cible. Les responsables métier clés déclarent ensuite qu’elle ne répond pas à leur processus critique. Un architecte affirme que la validation du Board rend leur avis inutile.

La décision du Board valide les normes et la cohérence technique ; les métiers contestent l'impact sur un parcours de remboursement sensible. Le sponsor souhaite lancer le premier lot, mais le Business Owner n'a pas accepté la suppression d'une étape de contrôle. Le différend peut affecter le périmètre approuvé de l'Architecture Vision et le calendrier. Il faut préserver à la fois la gouvernance et l'acceptation métier.

Quelle est la meilleure réponse ?
A. Laisser le sponsor approuver provisoirement le parcours cible et traiter les concerns métier au comité de conformité de la Phase G.
B. Le Board est un mécanisme de gouvernance, mais il faut revoir les concerns métier non satisfaits, vérifier requirements et vues, puis soumettre les ajustements à la gouvernance appropriée.
C. Obtenir la validation de conformité du Board et organiser ensuite l'acceptation métier formelle, sans l'intégrer au même cycle de décision.
D. Demander au Business Owner d'établir une liste d'impacts précis et préparer leur présentation au Board lors de la prochaine revue.
**Scoring : A=0, B=5, C=3, D=1.**

**Justification des quatre niveaux :**

- **B — 5 points :** Le Board est un mécanisme de gouvernance, mais il faut revoir les concerns métier non satisfaits, vérifier requirements et vues, puis soumettre les ajustements à la gouvernance appropriée. Distinguer autorité du Board et acceptation métier, puis réviser views/requirements et soumettre les arbitrages traite les deux décisions.
- **C — 3 points :** Obtenir la validation de conformité du Board et organiser ensuite l'acceptation métier formelle, sans l'intégrer au même cycle de décision. Faire suivre la conformité par l'acceptation métier est utile, mais des validations séquentielles sans réconciliation préalable peuvent entraîner de nouveaux écarts.
- **D — 1 points :** Demander au Business Owner d'établir une liste d'impacts précis et préparer leur présentation au Board lors de la prochaine revue. La liste d'impacts du Business Owner informe le Board, mais ne remplace ni la mise à jour des requirements ni l'acceptation par les parties métier.
- **A — 0 points :** Laisser le sponsor approuver provisoirement le parcours cible et traiter les concerns métier au comité de conformité de la Phase G. Le sponsor ne peut remplacer l'analyse des concerns métier par une approbation provisoire suivie d'une revue en Phase G ; l'acceptation métier reste ouverte.

**Mapping : Stakeholder Management — Governance and Stakeholder Acceptance.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 2 ; TOGAF Standard, ADM et Series Guides applicables.

---
