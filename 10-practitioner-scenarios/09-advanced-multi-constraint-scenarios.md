# Practitioner — atelier avancé de 8 scénarios multi-contraintes

**Nature :** exercices originaux, non officiels. Niveau visé : application/analyse. Une question = une seule réponse ; le score pédagogique est 5/3/1/0. **Répondre avant de consulter** `09-advanced-scenarios-corrections.md`.

## A01 — Contexte d'entreprise, conformité et gouvernance

Une banque a obtenu l'approbation d'une Target Architecture pour ses virements instantanés. Le programme couvre quatre entités, dont deux ont déjà engagé des migrations différentes. La filiale A utilise le service commun d'authentification mais pas le modèle d'audit exigé ; la filiale B fournit l'ensemble des fonctions spécifiées mais a ajouté une interface non prévue dans les vues approuvées. Les deux filiales se déclarent « fully conformant ». Le Board apprend que les contrats d'architecture ne précisent ni l'autorité capable de statuer sur les exceptions ni les critères d'évaluation. Une mise en production est annoncée dans trois semaines. Le sponsor exige de ne pas retarder les travaux mais le CISO veut une preuve vérifiable de conformité.

**Quelle action doit être recommandée en premier ?**

A. Classer les deux filiales comme Non-conformant et ordonner le gel du programme ; toute différence avec la Target suffit pour invalider une implémentation.
B. Évaluer les implémentations contre les features de la spécification, distinguer les niveaux de conformité appropriés, établir les preuves et faire arbitrer les exceptions sous un cadre de gouvernance clarifié.
C. Faire accepter par le sponsor les écarts déjà identifiés, puis mettre à jour les diagrammes pour qu'ils décrivent les solutions en production.
D. Engager une revue d'architecture limitée aux exigences d'audit à risque élevé et autoriser provisoirement la filiale B sous réserve d'une analyse ultérieure de l'interface ajoutée.

## A02 — Stakeholders avec préoccupations opposées

Un établissement prépare l'unification de la gestion des réclamations de trois métiers. La direction commerciale exige une expérience client unique dans six mois. Les équipes de conformité signalent des périodes légales de conservation distinctes. Le service Operations, consulté après les premières vues, demande la possibilité de revenir à un mode dégradé sans perte des dossiers. Une première Architecture Vision a été validée par le sponsor, mais les représentants métier n'ont pas vu les processus des services concernés. Une architecture cible applicative est déjà partiellement dessinée. La réunion de décision de mardi doit choisir une trajectoire et non simplement prendre connaissance du dossier.

**Quelle démarche maximise la qualité de cette décision ?**

A. Produire un diagramme applicatif unique de plus haut niveau et demander au sponsor de trancher ; les détails peuvent être étudiés après la décision.
B. Organiser un atelier avec toutes les équipes techniques afin de compléter les requirements, puis laisser le sponsor présenter seul la décision.
C. Faire approuver un jeu de SLA d'exploitation, car c'est le seul point susceptible de compromettre la trajectoire.
D. Actualiser la stakeholder map, expliciter les concerns contradictoires et leurs owners, produire les vues métier/données/exploitation nécessaires, puis faire arbitrer les options et risques par l'autorité appropriée.

## A03 — Phase A, cadrage et valeur

La direction d'une banque demande « une plateforme IA pour tous les métiers » et annonce un plafond de financement. Plusieurs équipes disposent déjà de prototypes ; l'une traite des données de paiement soumises à des exigences de localisation, une autre produit des rapports internes non critiques. Le CTO veut retenir un fournisseur dès cette semaine. Les responsables des risques exigent une distinction entre expérimentation et traitements de production, mais personne n'a défini les bénéfices cibles ni le périmètre temporel du programme. Un cadre de gouvernance d'architecture existe et peut être réutilisé.

**À ce stade, quelle est la meilleure action ?**

A. Lancer Phase C et définir un Data Model générique, puis obtenir l'accord du métier lorsque la plateforme commune sera conçue.
B. Suspendre tous les prototypes jusqu'à ce que les quatre domaines d'architecture soient détaillés.
C. Utiliser la capacité d'architecture existante pour cadrer la demande en Phase A : drivers, outcomes, scope, concerns, risques, scénarios et options de Vision, puis établir un Statement of Architecture Work validable.
D. Sélectionner d'abord les deux prototypes les plus avancés comme cible provisoire, et documenter les hypothèses métier au premier sprint.

## A04 — Itération entre B, C Data, C Application et D

Un groupe bancaire souhaite unifier le parcours de paiement dans quatre pays. L'équipe Business Architecture a identifié une capacité commune de vérification de bénéficiaire et un indicateur métier de réduction de fraude. La Data Architecture envisage un référentiel client central ; une autorité locale exige néanmoins la conservation et le traitement d'une partie des informations dans son territoire. L'équipe Application propose un service central unique ; la Technology Architecture a déjà choisi une plateforme multirégion. Le Board demande une Target cohérente et un dossier d'options avant de confirmer le programme. La direction financière préfère un service unique, l'équipe locale refuse le transfert de données, et la sécurité demande la preuve de l'application des règles.

**Quelle réponse est la plus appropriée ?**

A. Réexaminer les exigences de localisation et les interfaces, comparer centralisation, fédération et traitements locaux, itérer sur les modèles Data/Application/Technology et soumettre les arbitrages tracés avec leurs impacts métier.
B. Conserver la Target centralisée en l'assortissant d'une exception de localisation à valider après la migration.
C. Adapter immédiatement la Data Architecture à une conservation locale, tout en laissant le service applicatif unique inchangé et sans revoir les flux.
D. Revenir à quatre solutions indépendantes pour réduire le risque réglementaire, puis évaluer leurs coûts et les différences métier.

## A05 — Phases E/F/G : trajectoire et dépendances

Le programme de modernisation d'une banque prévoit la migration de l'orchestrateur de paiement, d'un moteur anti-fraude et d'un bus d'événements. Les gaps B/C/D sont documentés. Le métier veut mettre en service la fraude d'abord pour un gain rapide, mais les événements nécessaires ne sont pas disponibles dans l'ancien système. L'architecte a proposé une Transition Architecture avec double publication et réconciliation ; cette option augmente temporairement les coûts d'exploitation et la complexité de surveillance. Le sponsor est favorable au « big bang », tout en exigeant une indisponibilité quasi nulle. La phase de gouvernance de l'implémentation n'a pas commencé.

**Quelle action est la plus adaptée maintenant ?**

A. Approuver immédiatement la bascule révolutionnaire proposée par le sponsor, et intégrer les écarts éventuels dans les Compliance Reviews de Phase G.
B. Définir le modèle d'Architecture Contract de Phase G pour régler ensuite la question des dépendances entre les projets.
C. Ajouter une nouvelle technologie d'événementiel dans la Target sans rouvrir les work packages, car le défaut est surtout technique.
D. Consolider gaps, solutions et dépendances, comparer les stratégies de migration et les Transition Architectures, puis faire arbitrer en Phase F le séquencement selon valeur, readiness et risque avant de gouverner l'exécution en G.

## A06 — Phase H : quelle forme de changement ?

Deux ans après une migration, une banque voit apparaître une nouvelle obligation de contrôle des destinataires. Elle impose un service de vérification pour certains paiements, mais ne change pas le modèle de règlement ni les exigences de conservation. Un fournisseur propose une API certifiée ; le CISO souhaite en contrôler l'intégration. Par ailleurs, des équipes utilisent déjà des mécanismes de vérification régionaux. L'Architecture Landscape n'a pas été actualisé depuis douze mois. Le sponsor demande si tous les travaux d'architecture doivent repartir de zéro. Une décision doit être rendue rapidement, sans éluder les impacts.

**Quelle recommandation est la plus justifiée ?**

A. Engager un ADM complet de Preliminary à H avant toute étude, car une exigence réglementaire nouvelle impose toujours un re-architecting.
B. Traiter la demande en Phase H : documenter le changement, examiner les états actuels, évaluer l'impact et classer simplification/incremental/re-architecting, puis décider du périmètre de révision et de la gouvernance.
C. Installer l'API certifiée via un changement d'exploitation ; son agrément externe suffit à établir la conformité architecturale.
D. Mettre à jour la requirement et lancer directement une revue de Phase D, puisque seule l'interface technique change a priori.

## A07 — Requirements Impact Assessment

En Phase F, un programme a approuvé trois vagues de migration. Une nouvelle requirement de conformité impose la traçabilité de chaque événement de rejet, y compris au cours des reprises et des doubles traitements. La première vague contient déjà un service de journalisation partielle. Les responsables des applications souhaitent préserver les dates approuvées. Le métier demande si le coût et le calendrier peuvent rester identiques ; la sécurité demande une preuve de traçabilité de bout en bout. Un arbitrage est prévu devant le Board, mais le responsable Requirements Management n'a encore qu'une fiche de demande non analysée.

**Quelle action permet un arbitrage fondé ?**

A. Ajouter immédiatement l'exigence au backlog de la première vague et faire corriger le planning après l'implémentation.
B. Refuser le changement parce que le plan de Phase F était déjà approuvé.
C. Réaliser un Requirements Impact Assessment retraçant composants et livrables affectés, alternatives, risques, coûts, dépendances et impacts sur les Transition Architectures ; soumettre ensuite les décisions gouvernées.
D. Demander au responsable du service de journalisation de déclarer la conformité de sa solution, puis actualiser la requirement en conséquence.

## A08 — Supporting ADM, réutilisation et readiness

Une banque lance une architecture de données partagées. Son Architecture Repository contient un pattern de partage transfrontalier approuvé deux ans plus tôt, mais les réglementations et les volumes ont changé. La direction souhaite réduire les coûts par réutilisation. Le responsable Data signale que les responsables métier n'ont pas accepté la propriété des données, le sponsor confirme le budget, et les équipes d'exploitation n'ont pas la compétence pour assurer le service 24/7. Les standards disponibles sont corrects mais l'entreprise ne possède pas de modèle d'ownership suffisamment détaillé. Le Board demande une recommandation en dix jours avant tout engagement irréversible.

**Quelle action est préférable ?**

A. Réutiliser le pattern comme candidat après analyse de son applicabilité, compléter ownership, scénarios métier, readiness et risques, puis proposer une trajectoire avec work packages préparatoires si nécessaires.
B. Appliquer directement le pattern approuvé : la réutilisation et le financement démontrent suffisamment la faisabilité.
C. Développer un nouveau pattern interne après un benchmark technologique détaillé, puis traiter la responsabilité des données pendant le déploiement.
D. Lancer un atelier limité d'Information Mapping et d'Organization Mapping pour clarifier les flux et rôles, et remettre à plus tard l'évaluation des capacités d'exploitation.
