# Mock Exam 02 — OGEA-103 Combined

**Part 1 : 60 min, closed book. Part 2 : 90 min, open book.**

# Part 1 — Foundation

## Concepts — Q1 à Q8

**Q1.** Quels sont les quatre domaines d'architecture de base ?
A. Strategy, Finance, HR, IT  B. Process, Project, Product, Platform  C. Business, Data, Application, Technology  D. Vision, Risk, Governance, Delivery

**Q2.** Un stakeholder est :
A. Uniquement le sponsor  B. Uniquement l'architecte  C. Un artifact  D. Toute partie ayant un intérêt dans ou étant affectée par l'architecture

**Q3.** Dans un programme de transformation, le comité cherche à choisir entre trois architectures alternatives dont les risques et coûts diffèrent. Quel bénéfice EA est le plus directement observable ?
A. Une application uniforme des standards techniques sans confrontation des options métier.  B. Un arbitrage cohérent reliant objectifs d'entreprise, choix d'architecture et impacts.  C. La remise systématique d'un diagramme de chaque couche avant de parler aux métiers.  D. Le remplacement du programme management par le seul Architecture Board.

**Q4.** Quelle relation est correcte ?
A. Baseline = état actuel pertinent ; Target = état futur souhaité  B. Baseline = cible ; Target = existant  C. Les deux sont des plans  D. Target = Transition Architecture

**Q5.** L'Enterprise Continuum aide surtout à :
A. Exécuter les applications  B. Stocker les fichiers de projet  C. Classifier et contextualiser les assets d'architecture  D. Gérer les incidents

**Q6.** Une banque possède une Architecture Vision et une Technology Architecture détaillée, mais aucune représentation des composants réutilisables au niveau de leurs capacités. Quel concept manque pour séparer besoin architectural et solution ?
A. Solution Building Block, qui doit être sélectionné avant que la capability puisse être définie.  B. Architecture Building Block, dont la description ne présuppose pas une technologie retenue.  C. Architecture Contract, qui remplace la représentation des composants.  D. Compliance Assessment, qui décrit la capacité métier indépendamment des réalisations.

**Q7.** Quels sont les trois types génériques d'Artifacts ?
A. ABB, SBB, Contract  B. Vision, Roadmap, Plan  C. Baseline, Target, Transition  D. Catalog, Matrix, Diagram

**Q8.** Architecture Capability correspond à :
A. Rôles, compétences, gouvernance, processus et moyens permettant de pratiquer l'architecture  B. Une application  C. Une seule équipe projet  D. Un catalogue

## Introduction to the ADM — Q9 à Q22

**Q9.** Quelle distinction Preliminary / Phase A est correcte ?
A. Preliminary définit la Target ; A définit les standards  B. Les deux sont identiques  C. Preliminary prépare la capacité d'architecture ; A cadre l'engagement et la Vision  D. A précède toujours Preliminary

**Q10.** Identifier les stakeholders clés et établir une Architecture Vision relève principalement de :
A. Phase G  B. Phase A  C. Phase E  D. Phase H

**Q11.** Une équipe produit veut fixer l'ensemble des choix applicatifs de la Target sans connaître encore les capabilities et processus métier visés. Quel résultat ADM manque en premier ?
A. L'Implementation Governance Model destiné à contrôler les fournisseurs déjà en delivery.  B. Le Governance Log de la Phase H, pour enregistrer les changements futurs.  C. La sélection anticipée des SBB d'infrastructure à partir du Repository.  D. La Target Business Architecture de Phase B, alimentant ensuite Data/Application/Technology.

**Q12.** Définir ownership, structure, qualité et lifecycle de l'information relève principalement de :
A. Phase C Data  B. Phase B  C. Phase E  D. Phase H

**Q13.** Décrire les services applicatifs requis par le métier relève principalement de :
A. Phase F  B. Phase D  C. Phase C Application  D. Preliminary

**Q14.** Plateformes, middleware, infrastructure et services technologiques relèvent surtout de :
A. Phase B  B. Phase D  C. Phase F  D. Phase H

**Q15.** Quel est le rôle principal de Phase E ?
A. Transformer les gaps en options de solution, work packages et Transition Architectures  B. Gouverner le code  C. Définir la Vision  D. Gérer les changements futurs

**Q16.** Quel est le rôle principal de Phase F ?
A. Définir les stakeholders  B. Définir la Target Business  C. Prioriser et séquencer la migration  D. Établir Architecture Capability

**Q17.** Quel est le rôle principal de Phase G ?
A. Classifier les assets  B. Définir les gaps  C. Construire la Vision  D. Gouverner l'implémentation et la conformité

**Q18.** Un changement réglementaire découvert après le déploiement pourrait nécessiter des ajustements limités ou une refonte plus large. Quel principe ADM doit guider la décision ?
A. Phase G applique une Compliance Review et ne peut jamais rouvrir les architectures cibles.  B. Phase H classe les impacts et détermine une ré-entrée ADM proportionnée.  C. Un cycle Preliminary-to-H complet est obligatoire pour chaque nouvelle requirement.  D. Requirements Management traite seul la modification sans évaluation de l'architecture en service.

**Q19.** Requirements Management :
A. N'intervient qu'en A  B. N'intervient qu'en G  C. Est un domaine technique  D. Maintient, analyse et trace les exigences tout au long de l'ADM

**Q20.** Une nouvelle contrainte de résidence de données oblige à revoir plusieurs décisions de phases déjà parcourues. Quelle affirmation sur l'ADM est correcte ?
A. Les phases peuvent être revisitées pour réconcilier les modèles et exigences avec la nouvelle contrainte.  B. Une Phase C entamée ne peut pas être modifiée sans relancer Preliminary.  C. Une requirement découverte après B doit attendre Phase H après le go-live.  D. Les changements sont traités uniquement dans le Migration Plan sans mettre à jour les vues.

**Q21.** Une Gap Analysis sert à :
A. Choisir un fournisseur  B. Définir le sponsor  C. Identifier les écarts entre Baseline et Target  D. Remplacer Requirements Management

**Q22.** Une Architecture Roadmap :
A. Est uniquement un contrat  B. Présente la trajectoire de transformation à haut niveau  C. Remplace toutes les Transition Architectures  D. Est identique à un Gantt détaillé

## ADM Techniques — Q23 à Q28

**Q23.** La direction parle de « banque plus rapide », mais aucun acteur ni résultat opérationnel attendu n'est défini. Quelle technique clarifie le problème afin d'en tirer des requirements ?
A. Gap Analysis, en choisissant immédiatement la solution technique cible.  B. Compliance Review, pour évaluer un programme qui n'a pas encore de Target.  C. Migration Planning, pour établir le séquencement avant la validation du besoin.  D. Business Scenario, articulant problème, acteurs, contexte et outcomes mesurables.

**Q24.** Quelle technique relie une situation métier réaliste à des requirements ?
A. Partitioning  B. Business Scenarios  C. Compliance Review  D. Architecture Contract

**Q25.** Évaluer la capacité de systèmes ou organisations à travailler ensemble relève de :
A. Risk Management  B. Readiness Assessment  C. Interoperability Analysis  D. Capability Mapping

**Q26.** Identifier les barrières humaines, organisationnelles et opérationnelles à la transformation relève de :
A. Business Transformation Readiness Assessment  B. Gap Analysis  C. Contract Review  D. Viewpoint Selection

**Q27.** Quelle technique s'intéresse explicitement aux menaces, probabilités, impacts et traitements ?
A. Business Scenario  B. Capability-Based Planning  C. Interoperability  D. Risk Management

**Q28.** Priorisation, dépendances, valeur et faisabilité de la trajectoire relèvent fortement de :
A. Stakeholder Mapping  B. Migration Planning Techniques  C. Viewpoints  D. Catalogs

## Applying the ADM — Q29 à Q32

**Q29.** Tailoring signifie :
A. Adapter méthode, profondeur, gouvernance et artifacts au contexte  B. Ignorer les principes  C. Supprimer Requirements Management  D. Imposer tous les deliverables possibles

**Q30.** Plusieurs filiales ont un socle commun, mais leurs architectures de segment portent des besoins locaux. Quel mécanisme permet de conserver la cohérence sans supposer un niveau unique de détail ?
A. Architecture Contract, qui exige que toutes les filiales partagent exactement les mêmes diagrams.  B. Architecture Compliance, qui remplace la modélisation de segments par une liste de normes.  C. Architecture Landscape à différents niveaux et périodes, articulant visions stratégiques et architectures de segments/capacités.  D. Enterprise Continuum, utilisé uniquement comme planning de releases d'un projet.

**Q31.** Dans une Digital Enterprise, l'ADM :
A. Devient inutile  B. Interdit l'itération rapide  C. Se limite aux infrastructures  D. Peut être adapté pour soutenir décisions rapides, plateformes et produits numériques

**Q32.** Dans une très grande entreprise, quelle approche aide à gérer plusieurs domaines et responsabilités ?
A. Supprimer les interfaces  B. Partitioning et gouvernance fédérée  C. Centraliser chaque décision locale  D. Abandonner l'Architecture Repository

## Architecture Governance — Q33 à Q35

**Q33.** Quel mécanisme arbitre typiquement les décisions et exceptions majeures ?
A. Delivery Team  B. Product Backlog  C. Architecture Board  D. Catalog

**Q34.** La réalisation d'une cible de paiements doit être acceptée sous réserve de mesures compensatoires pour une dérogation. Quelle fonction du Board soutient le mieux la gouvernance ?
A. Arbitrer et tracer conformité, exceptions et responsabilités selon un cadre approuvé.  B. Sélectionner directement tous les building blocks au lieu des équipes de conception.  C. Se limiter à valider le budget des lots sans examiner les exigences d'architecture.  D. Transformer toute dérogation en nouvelle norme permanente sans analyse des risques.

**Q35.** Une déviation par rapport à l'architecture approuvée doit idéalement être :
A. Cachée  B. Toujours refusée  C. Acceptée automatiquement  D. Analysée, documentée et gouvernée via un processus d'exception approprié

## Architecture Content — Q36 à Q40

**Q36.** Lequel est un Deliverable ?
A. Un serveur  B. Un produit de travail formel soumis à revue/approbation  C. Un stakeholder  D. Une phase

**Q37.** Lequel décrit le mieux un Artifact ?
A. Une capability métier  B. Un contrat fournisseur  C. Une représentation du contenu architectural  D. Un rôle organisationnel

**Q38.** Une revue a besoin d'une représentation de la relation entre des services applicatifs et leurs entités de données. Quel type d'artifact du Content Framework est le plus directement adapté ?
A. Une matrice montrant les relations entre éléments de deux catégories.  B. Un Architecture Contract car toute relation entre services et données doit être contractualisée.  C. Un catalogue listant seulement les noms de services sans dépendances.  D. Une Transition Architecture considérée comme un type de diagramme obligatoire.

**Q39.** Quelle distinction ABB/SBB est correcte ?
A. ABB est plus concret  B. Ils sont identiques  C. SBB est toujours métier  D. ABB exprime le besoin architectural, SBB une réalisation plus spécifique

**Q40.** Pour documenter un portefeuille applicatif, ses relations aux données et ses flux, quelle association Catalog / Matrix / Diagram est correcte ?
A. Catalog pour engagements fournisseurs, Matrix pour coûts projet et Diagram pour preuve de conformité.  B. Catalog pour liste structurée, Matrix pour relations entre éléments, Diagram pour représentation graphique.  C. Catalog pour solutions physiques, Matrix pour Architecture Contracts et Diagram pour exigences réglementaires.  D. Les trois sont des types de Deliverables formellement distincts par nature.

# Part 2 — Practitioner : huit scénarios multi-contraintes

Les items sont des exercices originaux non étalonnés ; choisir l'action la mieux adaptée au moment de décision.

## P1 — Context

Deux divisions fusionnent. Chacune possède une Architecture Capability mature mais des principes et processus de gouvernance différents.

Les divisions utilisent les mêmes standards IAM mais diffèrent sur la délégation des exceptions et la documentation des Architecture Contracts. La direction veut fusionner la plateforme de paiement sous quatre mois. Le CISO de groupe demande un audit commun, tandis que les équipes produit souhaitent préserver la rapidité des approbations locales. Une première Architecture Vision existe mais aucun responsable unique des dérogations n'a été désigné. Le comité doit choisir le modèle de coopération avant les projets d'intégration.

**Quelle action est la plus appropriée à ce stade ?**

A. Conserver les processus locaux et établir des principes minimums communs pour les interfaces critiques, puis évaluer les capacités des divisions dans un second temps.

B. Évaluer les deux capacités, définir responsabilités communes et tailorer un modèle fédéré, avec inventaire des principes divergents et mécanismes d'exception avant de sélectionner les lots.

C. Créer un Board commun pour les seuls projets partagés, sans rapprocher encore les règles de décision applicables aux domaines métier.

D. Demander à chaque division d'approuver ses propres architectures cibles et lancer une revue de convergence à la fin de la migration.

## P2 — Stakeholder Management

Le CISO et le sponsor ne s'accordent pas sur le niveau de contrôle acceptable pour respecter la date de lancement.

Le lancement concerne une application de paiement ouverte à des partenaires. Le CISO exige une preuve de gestion des accès privilégiés ; le sponsor craint un retard sur une fenêtre commerciale. Operations confirme qu'un déploiement progressif est possible, mais le business case n'a pas chiffré cette option. Le Board peut arbitrer un risque résiduel si les constraints sont explicites. La décision doit préserver l'obligation réglementaire et comparer les trajectoires plutôt qu'opposer deux personnes.

**Quelle action est la plus appropriée à ce stade ?**

A. Organiser un atelier de clarification entre CISO et sponsor sans documenter encore les options de réalisation et leurs dépendances.

B. Appliquer d'abord les contrôles de sécurité incontestables et chiffrer leur impact sur la date avant de faire arbitrer les autres options.

C. Clarifier concerns, requirements, impacts et utiliser la gouvernance appropriée pour arbitrer de manière traçable, en comparant plusieurs lots de déploiement et en indiquant l'autorité capable d'accepter les risques.

D. Lancer un pilote limité à des transactions non critiques et reporter le conflit de sécurité à la première revue post-déploiement.

## P3 — Phase A

Un sponsor demande une transformation mondiale, mais les pays concernés, bénéfices attendus et contraintes ne sont pas clairement définis.

Le périmètre comprend potentiellement quatre pays, mais deux seulement disposent d'un sponsor identifié. Le directeur des opérations souhaite unifier le règlement et le métier corporate veut préserver des processus régionaux. Les contraintes de données et les objectifs de réduction des coûts diffèrent selon les entités. Une équipe a proposé une plateforme mondiale ; une autre insiste sur une cible fédérée. Le comité doit décider quel travail d'architecture autoriser, pas choisir un fournisseur.

**Quelle action est la plus appropriée à ce stade ?**

A. Limiter provisoirement le scope aux deux pays sponsorisés et établir une première Vision, en laissant les autres pays pour un cadrage ultérieur.

B. Cadrer scope, stakeholders, drivers, value et Architecture Vision, avec hypothèses par pays et bénéfices mesurables dans le Statement of Architecture Work.

C. Établir un plan de migration pour l'ensemble des pays puis demander à chaque entité de le confirmer au prochain comité.

D. Définir les interfaces communes entre pays avant de négocier les business drivers et la gouvernance de groupe.

## P4 — B/C/D

La Business Architecture cible montre qu'une nouvelle capability exige une vue client unifiée, mais personne n'a défini ownership ni qualité des données.

Une filiale veut détecter la fraude sur les transactions en temps réel, ce qui nécessite un historique partagé et des identifiants communs. Le modèle métier est approuvé, mais aucune équipe n'a défini la qualité, la rétention ni la propriété des données clients. Le CISO signale une obligation de localisation et Operations souhaite une stratégie de reprise. Les architectes préparent une cible applicative mais ne peuvent démontrer la disponibilité ni la signification cohérente des informations.

**Quelle action est la plus appropriée à ce stade ?**

A. Approfondir la Data Architecture et ses requirements avant de figer la solution applicative, en clarifiant ownership, qualité, cycle de vie et contraintes de transfert avant de figer les services.

B. Valider une solution d'intégration qui synchronise les référentiels clients, puis traiter les différences de sémantique au déploiement.

C. Préparer un modèle de données commun et inventorier les propriétaires connus, puis formaliser les règles de rétention dans une revue suivante.

D. Examiner les exigences d'interfaces applicatives et les contrats de services avant de résoudre toutes les définitions des données.

## P5 — E/F/G

Plusieurs Transition Architectures sont possibles. Le sponsor demande laquelle implémenter en premier selon valeur, risque et dépendances.

Deux architectures de transition sont envisagées : coexistence des anciens messages pendant six mois ou bascule de tous les partenaires en une nuit. La valeur métier est comparable, mais les risques d'interruption et de reprise diffèrent fortement. La plateforme d'événements commune est un prérequis du nouveau moteur de fraude. Finance veut limiter les coûts de double exploitation. La décision doit classer les work packages et expliciter les dépendances et critères de bascule.

**Quelle action est la plus appropriée à ce stade ?**

A. Produire un classement provisoire des lots selon la valeur et la dépendance principale, puis vérifier les capacités de reprise avant validation finale.

B. Phase F, en utilisant des critères de migration et de priorisation, en comparant les coûts transitoires, risques résiduels et conditions de réalisation par wave.

C. Construire l'Architecture Contract de la première release, puis demander aux équipes de négocier l'ordre des migrations en Phase G.

D. Évaluer rapidement les preuves de conformité des composants déjà disponibles pour éliminer les solutions les moins sûres.

## P6 — Phase H

Une acquisition change fortement les business drivers six mois après la mise en production de la cible.

La banque a intégré une entreprise qui propose un produit de paiement imposant de nouvelles données et des contrôles locaux distincts. La plateforme cible est en service, mais les business drivers de croissance et de mutualisation évoluent. Les équipes proposent deux options : réutiliser la Target avec un adaptateur ou revoir les capacités métier et les contrats de données. Le sponsor demande une décision rapide sans perdre l'historique des versions et exceptions approuvées.

**Quelle action est la plus appropriée à ce stade ?**

A. Évaluer le changement et déterminer s'il faut lancer un nouveau cycle ou une évolution ciblée, avec une Change Request documentée et une classification du changement permettant de réutiliser l'ADM de manière proportionnée.

B. Enregistrer les nouveaux business drivers et réaliser une analyse ciblée des écarts, avant de décider du périmètre exact de re-entry.

C. Mettre à jour uniquement les objectifs financiers de la Roadmap, puis évaluer l'impact architectural à la prochaine revue annuelle.

D. Adapter les interfaces de la nouvelle filiale dans une release séparée sous réserve d'une revue technique, sans analyser la stratégie globale.

## P7 — Requirements Management

Une requirement réglementaire a changé pendant Phase D, mais les modèles B et C restent basés sur l'ancienne version.

Une loi impose un suivi plus détaillé des rejets et des événements de reprise. La nouvelle formulation affecte la Data Architecture approuvée et les interfaces de deux applications. Le chef de projet considère que la Phase D peut terminer les diagrammes sans révision de C ; le DPO demande une preuve de traitement de la règle. Le programme doit conserver la date de déploiement et évaluer un éventuel lot transitoire. La traçabilité actuelle pointe vers l'ancienne version réglementaire.

**Quelle action est la plus appropriée à ce stade ?**

A. Mettre à jour et analyser la requirement, tracer les impacts et itérer sur les architectures concernées, avec Requirements Impact Assessment sur les vues, building blocks, risques et work packages affectés.

B. Mettre à jour seulement le modèle applicatif de la cible, en demandant au Data Owner de confirmer ensuite la cohérence des échanges.

C. Mettre à jour la version de l'exigence et son propriétaire puis convoquer Data et Application pour recenser les impacts détaillés.

D. Conserver l'exigence historique dans la spécification et créer une note réglementaire séparée pour les équipes de déploiement.

## P8 — Supporting ADM Work

Une transformation est techniquement solide mais les équipes opérationnelles ne sont pas formées et les responsabilités futures sont floues.

La plateforme cible est validée mais le support exige désormais une équipe de nuit que la filiale ne possède pas. Le fournisseur propose une assistance limitée à la journée et le modèle d'astreinte reste à négocier. Le sponsor a financé les composants techniques, pas la formation ni les tests opérationnels. Operations estime le risque de coupure important pendant la migration. Le comité veut décider si le programme est prêt et quelles actions doivent précéder la première vague.

**Quelle action est la plus appropriée à ce stade ?**

A. Ajouter au plan une mesure de mitigation technique et un critère de reprise, sans réexaminer l'organisation du support.

B. Effectuer une analyse de transformation readiness et intégrer les actions organisationnelles dans la trajectoire, avec facteurs de readiness, plans de montée en compétences et work packages préparatoires.

C. Évaluer d'abord les rôles d'exploitation et financer une formation ciblée, puis compléter l'examen des autres facteurs de readiness.

D. Conserver la date de mise en service et planifier le support fournisseur seulement une fois les premiers incidents observés.
---

Fin de l'examen blanc.
