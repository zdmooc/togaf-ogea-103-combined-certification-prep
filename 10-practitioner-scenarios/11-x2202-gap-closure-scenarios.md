# Consolidation X2202 — 22 cas de couverture ciblée XP05–XP26

Exercices originaux : choisir la meilleure action. Les scores gradués 5/3/1/0 sont pédagogiques ; corrigés séparés. Ces cas complètent la banque historique S001–S060 et les cas XP01–XP04.

## XP05 — L2.1.7 : États d'architecture et décisions différenciées

Trois programmes migrent la même capacité métier. Le Repository contient un modèle cible approuvé, une version candidate soumise à revue, une description du déploiement courant et une architecture transitoire utilisée par la première filiale. Une équipe décide d'appeler toutes les représentations 'Target' car leurs composants sont techniquement similaires. L'Architecture Board veut anticiper les incompatibilités et savoir quel état est réellement en service et lequel relève d'une décision future.

**Quelle réponse est la plus appropriée ?**

A. Fusionner tous les états dans la Target en conservant les versions comme métadonnées mineures.

B. Conserver seulement l'état courant et ajouter les futurs changements dans le plan de projet, sans architecture transitoire.

C. Maintenir candidate, current, transition et target avec horizon, approbation, domaine et relations de traçabilité explicites.

D. Ajouter un tableau des applications en production et reporter les modèles futurs à la revue du portefeuille suivant.

## XP06 — L2.3.3 : Sécurité dès la Phase A

Une banque prépare une API de vérification de bénéficiaire partagée par deux métiers. Le sponsor a demandé de détailler la cible avant l'arbitrage. Le CISO souligne que les données traversent plusieurs frontières de confiance et que la durée de conservation peut dépendre du territoire. Un diagramme produit existe mais aucune hypothèse de sécurité n'a été identifiée dans le Statement of Architecture Work. Quelle décision prépare le mieux la Vision et les travaux B/C/D ?

**Quelle réponse est la plus appropriée ?**

A. Choisir la passerelle d'API déjà approuvée et considérer ses fonctions de sécurité comme suffisantes.

B. Définir les security stakeholders, les besoins de sécurité, les risques majeurs, les contraintes et les objectifs d'architecture à explorer, puis incorporer ces éléments au cadrage Phase A.

C. Confier au CISO une analyse des seuls flux externes afin de préparer les principaux critères de sécurité, avant d'intégrer les autres risques à la Target.

D. Attendre les tests de pénétration de Phase G pour déterminer les exigences de confidentialité et de résilience.

## XP07 — L2.5.6 : Migration et effets sur l'organisation

Une banque migre sa plateforme d'autorisations vers une architecture événementielle. Le nouveau modèle exige une équipe d'astreinte, des procédures de réconciliation et une responsabilité partagée entre l'équipe produit et Operations. La coexistence de deux systèmes durera quatre mois. Le sponsor a validé la valeur métier mais n'a pas financé la formation ni les contrats de support nécessaires. Quel travail de Phase F doit précéder l'approbation des vagues ?

**Quelle réponse est la plus appropriée ?**

A. Intégrer coûts et capacités d'organisation, responsabilités, readiness et dépendances au Migration Plan, puis faire arbitrer les mesures de transition.

B. Limiter Phase F à l'ordre des composants techniques ; le modèle opérationnel sera décidé en Phase G.

C. Faire chiffrer les besoins d'astreinte et prévoir une vague préparatoire, puis vérifier la répartition complète des responsabilités après le premier pilote.

D. Réduire le périmètre métier de la première vague sans informer le sponsor ni mettre à jour la Roadmap.

## XP08 — L2.8.1 : TOGAF Library ou Repository local ?

Une direction d'architecture cherche une démarche réutilisable pour établir son Architecture Capability et piloter un programme de transformation agile. Elle possède un Repository interne avec ses standards et solutions, mais ne trouve pas de méthodologie sur l'organisation des responsabilités et le travail itératif. L'architecte doit distinguer l'usage de la TOGAF Library publiée par The Open Group du stockage de documents internes et sélectionner les ressources adaptées.

**Quelle réponse est la plus appropriée ?**

A. Considérer la TOGAF Library comme la base des solutions installées de l'entreprise ; les Series Guides sont des standards de matériel.

B. Utiliser exclusivement le Governance Log interne, car aucun guide externe ne peut contribuer au tailoring ADM.

C. Copier l'ensemble des guides de la Library dans chaque dossier projet, puis choisir ceux que le fournisseur préfère.

D. Consulter le Leader's Guide et le Practitioners' Approach pertinents dans la TOGAF Library, puis adapter leur guidance à l'Architecture Capability et au Repository interne.

## XP09 — L2.8.6 : Repository opérationnel et bien gouverné

Une banque possède un référentiel contenant des standards, diagrams et contrats, mais les équipes ne savent pas quelle Target est approuvée, quelles exceptions restent ouvertes ni qui maintient les descriptions de solutions. Des instances incohérentes ont conduit à une migration basée sur une version obsolète. Le Board veut mettre en place des critères permettant de juger si le Repository soutient réellement les décisions et réutilisations.

**Quelle réponse est la plus appropriée ?**

A. Conserver uniquement les documents les plus récents et supprimer les autres sans validation des owners.

B. Mettre en place des responsabilités de mise à jour, versionnage, états de validation, liens entre requirements, standards, décisions, Landscape et solutions, plus des contrôles de cohérence et d'accès.

C. Publier les documents de plus haute visibilité dans une bibliothèque commune, puis introduire une gestion des versions après les prochaines migrations.

D. Considérer un Repository comme bien géré dès qu'il dispose de suffisamment de diagrammes de haute qualité.

## XP10 — L2.8.7,L2.8.8 : Niveaux d'architecture dans le Landscape

Le groupe veut une direction commune pour la modernisation sur cinq ans, mais une division doit préciser son architecture de paiements sur dix-huit mois, puis une squad doit cadrer la capacité de gestion des rejets. Les trois initiatives sont interdépendantes et les sponsors souhaitent partager des principes communs sans imposer le même niveau de détail à tous. Quel mode d'organisation des architectures correspond à ce besoin ?

**Quelle réponse est la plus appropriée ?**

A. Construire une seule Architecture de solution, avec une même profondeur de détail pour les trois horizons.

B. Classer les décisions uniquement par phase ADM sans référencer le niveau organisationnel des modèles.

C. Articuler Strategic, Segment et Capability Architecture dans l'Architecture Landscape, avec niveaux de détail et interfaces adaptés aux enjeux.

D. Créer trois Repositories indépendants, sans standard ni relation entre les vues, pour préserver l'autonomie.

## XP11 — L2.8.9 : Choisir la profondeur du modèle architectural

Un comité exécutif doit arbitrer une mutualisation des capacités bancaires alors que l'équipe de migration doit définir les interfaces et critères de reprise d'une application de paiement critique. Le sponsor veut un dossier unique pour économiser des efforts. La première décision concerne le portefeuille à trois ans ; la seconde porte sur la mise en œuvre technique à six mois. Comment choisir les représentations et les détails ?

**Quelle réponse est la plus appropriée ?**

A. Garder les mêmes modèles techniques détaillés pour les deux décisions, en ajoutant un résumé financier en introduction.

B. Limiter les deux décisions à une Business Architecture car le domaine technique importe seulement en Phase G.

C. Décrire uniquement la Technology Architecture et présumer les capacités communes déjà définies.

D. Produire des représentations liées au niveau stratégique et à celui de la capability/projet, chacune avec la profondeur nécessaire aux décisions et aux stakeholders.

## XP12 — L2.8.11 : Capabilities, value streams, organisation et information

Le processus de gestion des rejets de paiement mobilise trois directions et traverse deux plateformes techniques. Le métier souhaite une réduction des corrections manuelles et Finance veut comprendre où se crée la valeur. Le Data Owner ne connaît pas tous les usages de l'information échangée ; les responsables fonctionnels se renvoient la propriété des décisions. Quelle combinaison de techniques apporte le meilleur cadre pour Phase B ?

**Quelle réponse est la plus appropriée ?**

A. Cartographier capabilities et étapes de value stream, relier les acteurs via organization mapping et clarifier les échanges métier par information mapping avant de dériver les solutions.

B. Construire d'abord les diagrammes de déploiement, puis demander au métier de valider les capacités disponibles.

C. Construire une capability map initiale et relever les owners les plus évidents, puis compléter value streams et flux d'information lors de la revue cible.

D. Limiter l'analyse à la Gap Analysis technologique puisque les plateformes existantes définissent déjà le processus.

## XP13 — L2.8.15 : Nécessité du métamodèle et relation au Content Framework

Une équipe décrit des capabilities, applications, data entities et services de plateforme dans des documents différents. Leurs matrices utilisent des identifiants incohérents et ne permettent pas de relier les requirements à la Target. Le sponsor veut un Repository exploitable plutôt qu'un autre jeu de dessins. Quel rapport entre Enterprise Metamodel et Architecture Content Framework aide à résoudre le problème ?

**Quelle réponse est la plus appropriée ?**

A. Le Content Framework définit les relations de données en production, tandis que le Metamodel définit uniquement les méthodes de migration.

B. Créer une nomenclature commune sans définir de types ni relations ; la cohérence peut être vérifiée manuellement à chaque comité.

C. Définir concepts, propriétés et relations dans un Enterprise Metamodel cohérent avec le Content Framework, puis l'utiliser pour structurer artifacts, deliverables et traçabilité.

D. Remplacer toutes les matrices par des diagrams, qui garantissent automatiquement la conformité des relations.

## XP14 — L2.8.16 : Quand alimenter le Content Framework ?

Le programme suit un cycle ADM itératif. Après Phase B, des business requirements sont clarifiées ; au cours de C, de nouvelles data entities sont identifiées, et en D une contrainte de résilience impose un building block supplémentaire. Les équipes proposent de n'actualiser le Content Framework que lors du dernier comité de migration pour éviter des mises à jour répétées. Quelle pratique convient ?

**Quelle réponse est la plus appropriée ?**

A. Ne tenir à jour les artifacts qu'en Phase G après livraison, pour éviter les versions transitoires.

B. Faire progresser les contenus, relations et versions des artifacts à chaque itération et phase utile de l'ADM, en respectant la gouvernance de validation.

C. Conserver les concepts de métamodèle initiaux, mettre à jour les principaux diagrammes seulement à chaque jalon, puis réconcilier les autres relations après approbation de la Target.

D. Figer le Content Framework dès Preliminary, car les phases suivantes doivent produire des solutions sans modifier les modèles.

## XP15 — L2.8.17 : Utiliser le TOGAF Enterprise Metamodel

Une Architecture Definition Document de la banque contient un catalog des applications et une matrix reliant les applications aux données. Le responsable du Repository veut ajouter des liens entre business services, application components et data entities. Plusieurs équipes ont déjà des objets de même nom avec des natures différentes. L'architecte doit employer le TOGAF Enterprise Metamodel comme référence et gouverner l'adaptation au besoin de l'entreprise.

**Quelle réponse est la plus appropriée ?**

A. Créer directement des SBB correspondant à toutes les entités, sans distinguer les types abstraits du Metamodel.

B. Remplacer les objets métier par les noms des produits existants pour garantir la convergence.

C. Laisser chaque application définir son propre modèle et vérifier seulement les contrats d'API lors de la migration.

D. Définir les types d'entités, leurs propriétés et relations autorisées selon le TOGAF Enterprise Metamodel, puis adapter et versionner les extensions spécifiques.

## XP16 — L2.6.2 : Stakeholders et changement en Phase H

Une nouvelle réglementation de vérification des bénéficiaires modifie les critères d'acceptation d'une plateforme déjà en production. Le métier demande une release rapide, mais le DPO et Operations redoutent des impacts sur rétention et reprise. Le sponsor qualifie le changement de mineur sans consultation. Quel travail relève des activités de Change Management ?

**Quelle réponse est la plus appropriée ?**

A. Accepter la classification du sponsor et adapter seulement les composants techniques déjà identifiés.

B. Recommencer toutes les phases ADM sans réaliser d'analyse de concerns ou d'impacts.

C. Réviser la stakeholder map et les concerns, analyser les exigences et options avec leurs owners, puis classer le changement et préparer les décisions gouvernées.

D. Réaliser une réunion technique entre équipes de réalisation puis reporter la consultation des responsables métier après déploiement.

## XP17 — L1.3.6 : Pourquoi envisager plusieurs options architecturales ?

Pour moderniser le traitement des rejets, l'équipe propose un service centralisé. L'équipe Operations préfère une architecture régionale plus résiliente, tandis que Finance souhaite limiter le coût de coexistence. Une option technique a déjà été prototypée, mais le Board n'a pas reçu de comparaison des outcomes ni des trade-offs. Pourquoi explorer des alternatives avant de figer la Target ?

**Quelle réponse est la plus appropriée ?**

A. Parce que TOGAF oblige à implémenter au moins deux solutions complètes avant toute approbation de la Vision.

B. Pour révéler les impacts des concerns et des contraintes contradictoires, comparer valeur, coût, risque et faisabilité, puis faire arbitrer la cible.

C. Parce que le nombre de diagrammes produits prouve la qualité de l'architecture finale.

D. Pour choisir provisoirement le produit du fournisseur préféré, en comparant le reste lors de la première Compliance Review.


## XP18 — L2.1.10 : Piloter l'incertitude et la perte potentielle

Une banque prévoit de remplacer un orchestrateur de paiement utilisé pour les transactions critiques. Le business case annonce une baisse du coût d'exploitation, mais les dépendances de reprise avec le legacy sont peu documentées. Operations redoute une coupure, Finance veut confirmer les bénéfices et un prestataire affirme pouvoir basculer en une nuit. L'Architecture Board veut créer un environnement où les incertitudes sont connues, gouvernées et suivies, afin de maximiser le bénéfice et limiter les pertes métier.

**Quelle action est la plus appropriée ?**

A. Choisir le scénario de coût minimal, puis réexaminer les risques si les tests montrent un incident.

B. Mesurer les incertitudes sur les capacités et dépendances, analyser scénarios/risques/bénéfices, prévoir des mesures et décisions jalonnées, puis ajuster la trajectoire selon des preuves.

C. Documenter les risques les plus élevés dans un registre et prévoir une première Transition Architecture, puis confirmer les bénéfices et les dépendances après un pilote contrôlé.

D. Confier la décision au fournisseur ayant livré la solution et considérer son SLA comme preuve suffisante.


## XP19 — L2.4.1 : Étapes communes des phases B, C et D

L'équipe Architecture lance l'étude de sa plateforme bancaire. Les responsables métier possèdent une carte des capacités, les Data Owners signalent des risques de conservation, et le CTO défend une nouvelle plateforme technique. Les trois équipes travaillent en parallèle, mais leurs livrables manquent de structure comparable. Le Board demande un processus commun permettant d'établir les décisions de chaque domaine et de réconcilier les informations produites.

**Quelle action est la plus appropriée ?**

A. Fixer d'abord les standards technologiques puis dessiner les domaines métier, Data et Application autour du produit choisi.

B. Laisser chaque domaine produire son propre diagramme Target, puis rechercher leurs incompatibilités lors de la migration.

C. Limiter l'activité commune à une Gap Analysis après validation complète des trois Target Architectures.

D. Pour chaque domaine : sélectionner reference models/viewpoints, établir Baseline et Target proportionnées, identifier gaps et requirements, résoudre les impacts entre domaines, mener les revues et actualiser Roadmap et contenus.


## XP20 — L2.4.2 : Risque et sécurité dans B/C/D

Un service interbancaire traite des identités client et des données de règlement. Les équipes Data proposent un échange interrégional, Application veut centraliser les API et Technology met en avant une infrastructure certifiée. Le CISO indique que l'architecture doit traiter menace de détournement, restriction de transfert et reprise d'activité. Le sponsor ne veut pas que la sécurité soit examinée seulement lorsque la plateforme sera sélectionnée.

**Quelle action est la plus appropriée ?**

A. Évaluer les threats, vulnerabilities, requirements, contrôles et risques résiduels dans B/C/D ; intégrer les contraintes aux vues Data/Application/Technology, aux gaps et à la gouvernance.

B. Obtenir une validation sécurité uniquement après la Phase D pour ne pas ralentir l'analyse métier et des données.

C. Identifier les obligations de confidentialité et la résilience critique, puis détailler les controls et mitigations des domaines touchés dans une revue transverse suivante.

D. Se fier à la certification du fournisseur : les risques sont couverts par sa plateforme standard.


## XP21 — L2.4.3 : Entrées métier avant de développer B

Une mutuelle souhaite supprimer plusieurs doubles saisies entre souscription et indemnisation. L'équipe applicative présente un workflow modernisé, tandis que la direction métier demande de préserver certains contrôles réglementaires. Aucun document n'articule les principes métier, les business goals et les drivers de transformation. Les architectes doivent préparer les entrées pertinentes pour développer la Business Architecture cible.

**Quelle action est la plus appropriée ?**

A. Retenir le workflow proposé et considérer les différences de processus comme des requirements de delivery.

B. Définir uniquement les composants techniques partagés et laisser le métier produire ses indicateurs après le design.

C. Recueillir et expliciter business principles, business goals et drivers avec les stakeholders, puis les traduire en décisions et requirements de Business Architecture.

D. Consigner les business goals principaux et leurs stakeholders avant de construire le modèle complet des principes et drivers lors du jalon de revue.


## XP22 — L2.5.1 : Risque et sécurité durant E, F et G

Un programme a retenu une cible de paiement multi-sites. Phase E prépare les Transition Architectures ; Phase F doit prioriser les migrations ; Phase G contrôlera les solutions réalisées. Les données sensibles vont temporairement transiter par deux systèmes et les règles de journalisation diffèrent. Le CISO exige une vision des risques, des contrôles compensatoires, des critères de conformité et des responsabilités à chaque phase.

**Quelle action est la plus appropriée ?**

A. Concentrer l'analyse de sécurité sur la Compliance Review finale de Phase G.

B. Analyser le risque transitoire en E, intégrer coûts/mitigations et priorités en F, puis vérifier en G les controls, écarts, contrats et preuves d'implémentation.

C. Inscrire une mitigation pour la période de coexistence dans la roadmap E/F, puis demander au Board d'étendre le contrôle aux solutions réalisées à la première revue G.

D. Sélectionner le fournisseur le plus certifié et considérer son produit comme une dérogation permanente aux règles Data.


## XP23 — L2.5.9,L2.5.10 : Roadmap confirmée et sorties de Phase F

Le comité de migration dispose de work packages et de deux architectures transitoires proposées. Finance autorise le financement en deux vagues, mais la seconde dépend de la normalisation des événements et de la formation des opérateurs. Le Board demande une Architecture Roadmap confirmée et les informations permettant de passer à l'implémentation, avec des responsabilités claires et des critères de bascule.

**Quelle action est la plus appropriée ?**

A. Conserver la Roadmap provisoire de Phase E puisque les projets possèdent déjà un budget suffisant.

B. Préparer directement les Compliance Reviews de Phase G pour découvrir les dépendances restantes durant le delivery.

C. Prioriser les dépendances techniques dans un tableau de jalons et soumettre le plan au sponsor, puis compléter la readiness et les risques résiduels après le pilote.

D. Confirmer la Roadmap et l'Implementation and Migration Plan après analyse valeur/risque/dépendances, préciser Transition Architectures, engagements et informations à transmettre à Phase G.


## XP24 — L2.5.11,L2.5.13 : Entrées G et sorties de gouvernance

Une équipe de delivery commence à construire les SBB d'une plateforme de virements. L'Architecture Definition Document et les exigences sont approuvés, la Roadmap est financée et un Architecture Contract est proposé aux fournisseurs. Le Board doit déterminer les entrées nécessaires aux Compliance Reviews et les livrables de sortie permettant de gouverner les écarts, engagements et changements.

**Quelle action est la plus appropriée ?**

A. Garder comme seule entrée le backlog Agile de l'équipe, puis enregistrer les issues après la mise en production.

B. Relier les entrées approuvées (architecture, requirements, Contract, plan et standards) aux Compliance Assessments, décisions d'exception et Change Requests, puis répercuter les résultats dans la gouvernance.

C. Définir une grille de conformité des requirements les plus critiques et un registre d'écarts, puis compléter les autres décisions/contrats aux jalons de réalisation.

D. Créer un nouveau Statement of Architecture Work à la fin de l'implémentation et ne pas tenir compte des exigences approuvées précédentes.


## XP25 — L2.6.3 : Sorties Phase H et décision de suite

Une évolution réglementaire est apparue sur une plateforme déjà déployée. L'analyse Phase H conclut que certains services Data doivent être réarchitecturés, tandis que les APIs de paiement peuvent rester stables. Le sponsor souhaite un chemin clair, des responsabilités et un mandat pour le cycle suivant. Le Board doit distinguer une modification locale d'une initiative d'architecture plus large.

**Quelle action est la plus appropriée ?**

A. Documenter le résultat de Change Management et la décision de gouvernance, produire les Change Requests/mandats et déclencher les activités ou le nouveau cycle ADM nécessaires avec exigences et Landscape mis à jour.

B. Conserver le changement dans un ticket d'incident opérationnel sans modifier les artefacts d'architecture approuvés.

C. Émettre une Change Request et attribuer un owner, puis laisser la réconciliation des autres documents et la portée ADM à une revue ultérieure.

D. Considérer le changement comme terminé dès l'acceptation orale de la nouvelle requirement par son propriétaire.


## XP26 — L2.7.3 : Sorties de Requirements Management

Une banque en Phase F reçoit une nouvelle exigence de traçabilité des rejets. Le Requirements Manager doit éviter que le changement reste isolé dans le backlog d'une application. La Target Architecture, les Architecture Requirements Specifications et les plans de migration contiennent des dépendances vers les services Data et Fraud. Le comité demande quels livrables et preuves permettent de statuer sur les impacts de cette requirement.

**Quelle action est la plus appropriée ?**

A. Ajouter la demande au registre des changements puis demander aux équipes de l'implémenter sans toucher aux specs approuvées.

B. Documenter une seule user story et la considérer comme une architecture cible suffisante.

C. Mettre à jour les exigences et leurs liens, produire un Requirements Impact Assessment pour les modèles, décisions et work packages affectés, et soumettre les changements gouvernés.

D. Versionner la requirement et notifier les propriétaires techniques, puis compléter l'analyse des impacts sur la roadmap à la prochaine revue.

