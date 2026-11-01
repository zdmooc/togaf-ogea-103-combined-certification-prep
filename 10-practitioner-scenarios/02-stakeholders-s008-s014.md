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

- **D — 5 points :** Reconnaître Operations comme stakeholder critique, comprendre ses concerns, produire les vues nécessaires et intégrer les requirements opérationnels dans l’architecture. Operations doit contribuer aux requirements de reprise et au modèle d'exploitation.
- **A — 3 points :** Consulter Operations et consigner ses principales contraintes d'exploitation pour la prochaine revue d'architecture, sans réviser immédiatement toutes les décisions. La consultation seule ne change pas les décisions de Target.
- **B — 1 point :** Exiger au minimum un runbook et un test de bascule pour le pilote, puis formaliser ultérieurement les autres requirements d'exploitation. La note technique ne documente pas les responsabilités de run.
- **C — 0 point :** Faire confirmer au sponsor l'acceptation du risque opérationnel, sans modifier les représentations ou responsabilités déjà approuvées. Reporter l'étude à la livraison fige le risque d'exploitation.

**Mapping : Stakeholder Management — Concerns, Views, Requirements.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 2 ; TOGAF Standard, ADM et Series Guides applicables.

---
## S009 — Sponsor contre CISO

Le sponsor veut une mise en production en trois mois. Le CISO exige des contrôles qui peuvent ajouter plusieurs semaines. Les deux parties considèrent leur priorité comme non négociable.

La date avancée dépend d'un lancement commercial ; les exigences de sécurité portent sur des accès privilégiés et une preuve d'audit réglementaire. Une option de lancement limité existe mais n'a pas été chiffrée. Le comité d'architecture doit présenter une trajectoire défendable, en laissant aux autorités désignées la responsabilité d'accepter les risques résiduels.

Quelle approche est la plus appropriée ?
A. Clarifier les concerns, contraintes et requirements, rendre visibles les impacts et arbitrages, puis utiliser la gouvernance appropriée pour obtenir une décision traçable.
B. Appliquer provisoirement les contrôles de sécurité prioritaires du CISO et faire arbitrer les impacts métier restants.
C. Documenter les exigences minimales non négociables du CISO et étudier les impacts calendaires avant l'arbitrage formel du sponsor.
D. Réduire le périmètre du produit au pilote commercial et traiter les contrôles de sécurité durant une seconde release, sans décision d'exception.
**Scoring : A=5, B=3, C=1, D=0.**

**Justification des quatre niveaux :**

- **A — 5 points :** Clarifier les concerns, contraintes et requirements, rendre visibles les impacts et arbitrages, puis utiliser la gouvernance appropriée pour obtenir une décision traçable. Un arbitrage documenté concilie sponsor et CISO.
- **B — 3 points :** Appliquer provisoirement les contrôles de sécurité prioritaires du CISO et faire arbitrer les impacts métier restants. Une mitigation partielle ne règle pas l'autorité d'acceptation.
- **C — 1 point :** Documenter les exigences minimales non négociables du CISO et étudier les impacts calendaires avant l'arbitrage formel du sponsor. L'aval du sponsor ne remplace pas l'acceptation sécurité.
- **D — 0 point :** Réduire le périmètre du produit au pilote commercial et traiter les contrôles de sécurité durant une seconde release, sans décision d'exception. Ignorer le CISO crée une dérogation implicite.

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

- **B — 5 points :** Mettre à jour la stakeholder map, les concerns et les plans d’engagement, puis vérifier l’impact sur requirements et vues. La carte actualisée révèle les actors et concerns réellement touchés.
- **C — 3 points :** Mettre à jour les stakeholders les plus influents et leurs préoccupations, sans refaire encore la cartographie complète des dépendances. Les acteurs puissants ne couvrent pas toutes les dépendances.
- **D — 1 point :** Mettre à jour les rôles de décision et le registre des risques, puis reporter la révision des views et concerns après la validation de la Data Architecture. Une liste de sponsors omet les acteurs opérationnels.
- **A — 0 point :** Conserver les anciennes validations tout en ajoutant les nouveaux responsables comme simples destinataires du rapport d'architecture. Une carte périmée fausse les consultations.

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

- **C — 5 points :** Produire des views adaptées aux concerns des stakeholders, construites à partir d’une base architecturale cohérente. Les viewpoints doivent traduire les concerns de chaque public.
- **D — 3 points :** Conserver un modèle d'architecture partagé, mais préparer des explications distinctes pour les principaux groupes de stakeholders. Une synthèse unique est trop vague pour les décisions spécialisées.
- **A — 1 point :** Produire une synthèse métier et réserver le schéma exhaustif aux revues techniques, sans encore formaliser explicitement les viewpoints. Un diagramme technique n'éclaire pas les capacités métier.
- **B — 0 point :** Ajouter des légendes et des annotations de risques au diagramme unique, puis demander aux différents acteurs de formuler leurs questions. La même vue exhaustive ne sert pas tous les décideurs.

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

- **D — 5 points :** Maintenir le stakeholder satisfait avec une communication ciblée sur décisions, risques et impacts, sans le surcharger. Une communication ciblée préserve la satisfaction d'un stakeholder influent.
- **A — 3 points :** Prévoir une synthèse décisionnelle périodique pour cet acteur et garder les détails accessibles à la demande, sans cartographier tous ses concerns. Un rapport périodique manque l'analyse de ses concerns.
- **B — 1 point :** Limiter ses interactions aux points d'arbitrage formels, avec un résumé en amont mais sans prévoir de suivi lors d'une évolution majeure. L'accès passif à un dossier ne suffit pas à le tenir informé.
- **C — 0 point :** Maintenir la communication quotidienne sous forme de compte rendu condensé, puis réduire la fréquence après le prochain jalon. Le solliciter en permanence surcharge sa faible disponibilité.

**Mapping : Stakeholder Management — Influence / Interest.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 2 ; TOGAF Standard, ADM et Series Guides applicables.

---
## S013 — Du concern à la requirement

Le responsable Operations dit : « je ne veux plus passer mes nuits à gérer des bascules manuelles ». L’équipe copie cette phrase telle quelle dans l’Architecture Requirements Specification.

Le service concerne des paiements critiques et un objectif de bascule automatique en moins de deux minutes est envisagé. Les SRE considèrent qu'un temps de rétablissement et un seuil de perte de données doivent être définis séparément. Le métier n'a pas validé ces chiffres et le sponsor attend un critère de recette opposable avant de signer la prochaine Architecture Requirements Specification.

Quelle action est la meilleure ?
A. Transformer le concern en requirements vérifiables sur failover, automatisation, RTO/RPO, observabilité et tests, tout en gardant la traçabilité vers le stakeholder.
B. Traduire l'inquiétude en une cible indicative de disponibilité puis confirmer ultérieurement ses seuils, ses conditions de mesure et son propriétaire.
C. Enregistrer une exigence de disponibilité chiffrée et préparer un atelier de clarification ultérieur avec le métier et les SRE.
D. Définir provisoirement le critère à partir des capacités du produit actuel, puis demander au sponsor une approbation sans tests de faisabilité.
**Scoring : A=5, B=3, C=1, D=0.**

**Justification des quatre niveaux :**

- **A — 5 points :** Transformer le concern en requirements vérifiables sur failover, automatisation, RTO/RPO, observabilité et tests, tout en gardant la traçabilité vers le stakeholder. Une requirement traçable traduit une préoccupation en critère vérifiable.
- **B — 3 points :** Traduire l'inquiétude en une cible indicative de disponibilité puis confirmer ultérieurement ses seuils, ses conditions de mesure et son propriétaire. Un besoin formulé sans critères est difficile à tester.
- **C — 1 point :** Enregistrer une exigence de disponibilité chiffrée et préparer un atelier de clarification ultérieur avec le métier et les SRE. Une note de réunion ne garantit pas la traçabilité.
- **D — 0 point :** Définir provisoirement le critère à partir des capacités du produit actuel, puis demander au sponsor une approbation sans tests de faisabilité. Choisir directement un produit court-circuite le besoin.

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

- **B — 5 points :** Le Board est un mécanisme de gouvernance, mais il faut revoir les concerns métier non satisfaits, vérifier requirements et vues, puis soumettre les ajustements à la gouvernance appropriée. Conformité Board et acceptation métier portent sur des responsabilités distinctes.
- **C — 3 points :** Obtenir la validation de conformité du Board et organiser ensuite l'acceptation métier formelle, sans l'intégrer au même cycle de décision. Les validations séparées manquent de réconciliation des concerns.
- **D — 1 point :** Demander au Business Owner d'établir une liste d'impacts précis et préparer leur présentation au Board lors de la prochaine revue. Le Board ne peut accepter à lui seul la valeur métier.
- **A — 0 point :** Laisser le sponsor approuver provisoirement le parcours cible et traiter les concerns métier au comité de conformité de la Phase G. L'accord d'architecture n'efface pas les requirements métier.

**Mapping : Stakeholder Management — Governance and Stakeholder Acceptance.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 2 ; TOGAF Standard, ADM et Series Guides applicables.

---
