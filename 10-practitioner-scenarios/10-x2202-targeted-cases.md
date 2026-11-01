# X2202 Practitioner — quatre cas ciblés sur des lacunes (XP01–XP04)

Exercices **originaux**, niveau application/raisonnement. Une seule meilleure réponse est attendue, avec classement pédagogique **5/3/1/0** disponible dans le fichier de correction séparé. Les scores ne représentent pas des items officiels.

## XP01 — L2.1.11 : quatre contextes du DPBoK

Une plateforme bancaire d'IA est née d'une expérimentation menée par une seule personne. Elle est devenue un produit géré par une équipe, puis a dû s'intégrer aux systèmes de plusieurs équipes produit. Aujourd'hui, le groupe veut la gouverner dans son portefeuille et partager des contrôles de conformité entre filiales. L'architecte doit aider les responsables à comprendre comment son rôle et les mécanismes de coordination évoluent sans confondre les niveaux d'organisation avec les quatre domaines d'architecture Business/Data/Application/Technology.

**Quelle proposition convient ?**

A. Employer les quatre domaines d'architecture comme contextes DPBoK et attribuer un domaine à chaque étape de croissance.
B. Classer les livraisons selon Preliminary, Phase A, Phase C et Phase G : les quatre contextes DPBoK correspondent à ces phases.
C. Distinguer Individual/Founder, Team, Team of Teams et Enterprise ; augmenter progressivement la coordination, les standards et la gouvernance selon les interdépendances réelles.
D. Séparer seulement les activités individuelles et l'entreprise entière ; la coordination des équipes doit être traitée exclusivement par la gestion des projets.

## XP02 — L2.8.5 : les sept rubriques du Repository

Un architecte arrive dans une banque où les décisions d'exception sont conservées dans des tickets, les exigences dans un tableur et les patterns dans des dossiers d'équipe. Le sponsor veut réorganiser les ressources sans inventer un huitième compartiment incompatible avec le syllabus. L'architecte doit distinguer le référentiel d'entreprise, le paysage des solutions en service et les standards. Il doit être capable de citer les sept rubriques présentées à l'objectif X2202 Practitioner 8.5.

**Quelle proposition est la plus conforme ?**

A. Séparer Architecture Landscape, Reference Library, Standards Library, Governance Repository, Architecture Requirements Repository, Solutions Landscape et Enterprise Repository.
B. Utiliser Architecture Metamodel, Architecture Capability, Architecture Landscape, Standards Information Base, Reference Library, Governance Log et Architecture Requirements Repository comme la liste canonique exacte du LO 8.5.
C. Conserver Architecture Landscape et Standards Library, puis gérer toutes les exigences, exceptions et solutions dans une seule Reference Library.
D. Réunir Architecture Metamodel et Enterprise Repository sous une catégorie unique et classer les autres éléments par projet de livraison.

## XP03 — L2.8.14 : Implementation Factor Catalog et consolidation

Le programme de modernisation de MayaBank doit traiter trois gaps : absence d'événements de paiement standardisés, besoin d'un service Fraud partagé et manque de capacité de support 24/7. Fraud dépend de la publication d'événements. Une migration évolutive permettrait une coexistence limitée, mais son coût d'exploitation n'est pas encore accepté. Le Board demande des objets précis pour représenter les facteurs d'implémentation, les dépendances entre gaps et les incréments d'architecture, afin de passer de la cible aux décisions de migration.

**Quelle démarche est la plus appropriée ?**

A. Mettre les gaps directement dans un Architecture Contract et demander aux équipes de les prioriser pendant Phase G.
B. Produire uniquement un Architecture Roadmap Diagram ; les facteurs d'implémentation et dépendances seront implicites dans les dates.
C. Valider une Technology Architecture et ne pas représenter la dépendance Fraud → Event Platform avant la mise en production.
D. Utiliser l'Implementation Factor Catalog pour les contraintes et readiness, la Consolidated Gaps, Solutions, and Dependencies Matrix pour relier les gaps et solutions, et l'Architecture Definition Increments Table pour suivre le développement de l'architecture par incréments.

## XP04 — L2.8.18 : taxonomie et métamodèle

Trois filiales classent leurs assets d'architecture différemment. Dans l'une, « service » désigne une activité métier ; dans une autre, une API ; dans la troisième, une plateforme technique. Leur Repository devient difficile à rechercher et leurs modèles ne sont plus comparables. Une équipe propose une liste de catégories, une autre un modèle formel des relations et des propriétés. L'architecte doit expliquer comment la taxonomie contribue à l'organisation des connaissances sans la confondre avec l'Enterprise Metamodel.

**Quelle décision est préférable ?**

A. Choisir un unique diagramme technique, qui rend inutile l'alignement des catégories et des définitions.
B. Définir une taxonomie cohérente pour classer les éléments, puis aligner les types, attributs et relations du métamodèle ; gouverner les synonymes et classifications afin de soutenir les usages du Repository.
C. Remplacer toutes les exigences d'architecture par la taxonomie, car une classification suffit à exprimer les relations de conformité.
D. Conserver les taxonomies locales avec une simple liste de synonymes, sans vérifier les contradictions des modèles ni les usages interfiliales.
