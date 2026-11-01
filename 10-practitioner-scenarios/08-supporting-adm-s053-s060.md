# Practitioner Scenarios — Supporting the ADM Work

## S053 — Transformer une idée vague en besoin exploitable

La direction dit : « nous devons devenir la banque la plus rapide sur les paiements ». Aucun acteur, problème concret ni résultat mesurable n’est défini.

Les équipes métier parlent de rapidité mais ne définissent ni latence attendue ni situation insatisfaisante. Operations redoute une promesse impossible à soutenir en production et Risk signale des contrôles obligatoires pouvant rallonger le parcours. Le sponsor veut choisir un fournisseur dès la semaine suivante. L'architecte doit transformer une ambition générale en un scénario d'affaires validable et en exigences mesurables.

Quelle technique aiderait le mieux à démarrer ?
A. Utiliser un Business Scenario pour expliciter problème/opportunité, acteurs, environnement, desired outcomes et requirements.
B. Utiliser un entretien métier structuré pour clarifier objectifs, acteurs et indicateurs, puis formaliser un Business Scenario dans un second temps.
C. Organiser un entretien avec les métiers pour définir les acteurs et un indicateur de temps de traitement, puis compléter le scénario d'affaires plus tard.
D. Dériver directement un objectif technique de latence depuis l'offre fournisseur la plus rapide, puis vérifier la valeur métier après le pilote.
**Scoring : A=5, B=3, C=1, D=0.**

**Justification des quatre niveaux :**

- **A — 5 points :** Utiliser un Business Scenario pour expliciter problème/opportunité, acteurs, environnement, desired outcomes et requirements. Le Business Scenario relie acteurs, problème, environnement et outcomes.
- **B — 3 points :** Utiliser un entretien métier structuré pour clarifier objectifs, acteurs et indicateurs, puis formaliser un Business Scenario dans un second temps. Décrire le parcours actuel est une entrée, pas un scénario cible.
- **C — 1 point :** Organiser un entretien avec les métiers pour définir les acteurs et un indicateur de temps de traitement, puis compléter le scénario d'affaires plus tard. Un seul diagramme technique n'explique pas la demande métier.
- **D — 0 point :** Dériver directement un objectif technique de latence depuis l'offre fournisseur la plus rapide, puis vérifier la valeur métier après le pilote. Choisir le fournisseur avant le scénario inverse besoin et solution.

**Mapping : Supporting ADM Work — Business Scenarios.**

**Référence d'étude :** X2202, Practitioner, unité 8 ; TOGAF Standard / Series Guides applicables.

---
## S054 — Une Gap Analysis qui choisit déjà la solution

Une équipe compare Baseline et Target. Pour chaque gap, elle inscrit immédiatement un nom de produit unique sans distinguer le besoin de la solution.

Le référentiel des gaps comporte des lignes comme « remplacer Oracle par PostgreSQL », alors que certains besoins concernent en réalité la gouvernance et la disponibilité des données. Finance souhaite chiffrer les work packages et le comité veut comparer plusieurs solutions. L'architecte doit préserver la distinction entre différence architecturale, option de solution, dépendance et décision d'investissement.

Quelle action est la meilleure ?
A. Conserver le nom des produits comme unique entrée du plan d'implémentation et traiter les besoins métier dans les fiches projets après financement.
B. Identifier d’abord les différences à conserver, supprimer, modifier ou créer ; utiliser ensuite ces gaps comme entrée des options de solution et work packages.
C. Conserver les produits candidats dans une colonne de solutions potentielles tout en distinguant les gaps architecturaux eux-mêmes.
D. Classer les applications candidates en familles de produits afin d'orienter l'appel d'offres, puis déduire les gaps de leurs principales fonctionnalités sans comparer d'abord Baseline et Target.
**Scoring : A=0, B=5, C=3, D=1.**

**Justification des quatre niveaux :**

- **B — 5 points :** Identifier d’abord les différences à conserver, supprimer, modifier ou créer ; utiliser ensuite ces gaps comme entrée des options de solution et work packages. Comparer Baseline et Target détermine les changements à traiter avant de grouper les solutions candidates.
- **C — 3 points :** Conserver les produits candidats dans une colonne de solutions potentielles tout en distinguant les gaps architecturaux eux-mêmes. Distinguer les gaps des produits candidats est utile, mais il reste à identifier leurs dépendances.
- **D — 1 points :** Classer les applications candidates en familles de produits afin d'orienter l'appel d'offres, puis déduire les gaps de leurs principales fonctionnalités sans comparer d'abord Baseline et Target. Le catalogue de produits peut orienter le marché mais ne permet pas de déduire les écarts métier de référence.
- **A — 0 points :** Conserver le nom des produits comme unique entrée du plan d'implémentation et traiter les besoins métier dans les fiches projets après financement. Partir du portefeuille commercial sans identifier les écarts architecturaux inverse le raisonnement.

**Mapping : Supporting ADM Work — Gap Analysis.**

**Référence d'étude :** X2202, Practitioner, unité 8 ; TOGAF Standard / Series Guides applicables.

---
## S055 — Organisation pas prête

La Target est techniquement faisable. Pourtant, aucune équipe ne sait exploiter la nouvelle plateforme, le support fournisseur n’est pas contractualisé et le modèle opérationnel n’existe pas.

La transformation doit couvrir plusieurs équipes qui exploitent aujourd'hui des applications traditionnelles. La nouvelle plateforme exige des rotations d'astreinte et un modèle de facturation nouveau. Le sponsor estime la faisabilité technique acquise, mais les managers d'exploitation signalent une dépendance forte à un intégrateur extérieur. Le comité demande des actions préparatoires, des coûts et une estimation des risques avant le lancement des waves.

Quelle action est la meilleure ?
A. Faire prendre en charge le support par un fournisseur en ajoutant une courte formation technique, puis présumer la capacité d'adoption sans évaluer les processus et responsabilités d'exploitation.
B. Conserver le calendrier et engager une formation générique pendant les premiers mois de production, sans revoir les responsabilités de support.
C. Utiliser une Business Transformation Readiness Assessment pour identifier les facteurs de readiness et intégrer les actions nécessaires à la transformation.
D. Conduire une évaluation limitée des compétences et du modèle opérationnel avec les responsables de plateforme, puis enrichir l'évaluation globale de readiness.
**Scoring : A=1, B=0, C=5, D=3.**

**Justification des quatre niveaux :**

- **C — 5 points :** Utiliser une Business Transformation Readiness Assessment pour identifier les facteurs de readiness et intégrer les actions nécessaires à la transformation. La Transformation Readiness Assessment couvre organisation, compétences, financement et actions d'adoption.
- **D — 3 points :** Conduire une évaluation limitée des compétences et du modèle opérationnel avec les responsables de plateforme, puis enrichir l'évaluation globale de readiness. L'étude limitée aux compétences et au modèle opérationnel est un début sans couvrir les autres facteurs.
- **A — 1 points :** Faire prendre en charge le support par un fournisseur en ajoutant une courte formation technique, puis présumer la capacité d'adoption sans évaluer les processus et responsabilités d'exploitation. Une assistance fournisseur et une formation isolée ne démontrent pas l'adhésion ni les responsabilités du futur run.
- **B — 0 points :** Conserver le calendrier et engager une formation générique pendant les premiers mois de production, sans revoir les responsabilités de support. Maintenir le calendrier sans traiter les responsabilités de support expose le service à des défaillances.

**Mapping : Supporting ADM Work — Business Transformation Readiness.**

**Référence d'étude :** X2202, Practitioner, unité 8 ; TOGAF Standard / Series Guides applicables.

---
## S056 — Risque résiduel caché

Après plusieurs controls, un risque de perte temporaire de service subsiste lors d’une migration. L’équipe veut marquer le risque « fermé » parce que des mesures existent.

La coupure de service envisagée concerne un système de compensation qui ne peut tolérer plus de quelques minutes de perte. Un test de bascule a amélioré la situation mais le niveau résiduel reste supérieur au seuil approuvé par Operations. Le sponsor souhaite clôturer le registre de risques pour présenter un tableau de bord favorable. L'architecte doit décider ce qui nécessite une acceptation explicite et quelles preuves sont attendues.

Quelle action est la meilleure ?
A. Maintenir la mitigation et son suivi dans le registre de risque, tout en demandant une validation différée de l'acceptation du risque résiduel.
B. Documenter le contrôle, maintenir le risque résiduel ouvert et demander une nouvelle estimation avec les équipes métiers avant l'escalade formelle.
C. Réduire la sévérité du risque dans le registre et replanifier sa revue au prochain comité de performance, sans traiter le dépassement du seuil.
D. Distinguer risque initial, mitigation et residual risk, attribuer ownership et obtenir l’acceptation/escalade appropriée du risque résiduel.
**Scoring : A=3, B=1, C=0, D=5.**

**Justification des quatre niveaux :**

- **D — 5 points :** Distinguer risque initial, mitigation et residual risk, attribuer ownership et obtenir l’acceptation/escalade appropriée du risque résiduel. Une mitigation doit être suivie de la mesure du risque résiduel.
- **A — 3 points :** Maintenir la mitigation et son suivi dans le registre de risque, tout en demandant une validation différée de l'acceptation du risque résiduel. Une mesure sans owner laisse l'acceptation du risque ambiguë.
- **B — 1 point :** Documenter le contrôle, maintenir le risque résiduel ouvert et demander une nouvelle estimation avec les équipes métiers avant l'escalade formelle. Un score de risque initial seul ne prouve pas son traitement.
- **C — 0 point :** Réduire la sévérité du risque dans le registre et replanifier sa revue au prochain comité de performance, sans traiter le dépassement du seuil. Cacher le risque résiduel empêche toute acceptation éclairée.

**Mapping : Supporting ADM Work — Risk Management.**

**Référence d'étude :** X2202, Practitioner, unité 8 ; TOGAF Standard / Series Guides applicables.

---
## S057 — Planifier par capability

La direction veut financer « Kafka », « Kubernetes » et « API Gateway » comme trois programmes indépendants. Aucun lien avec les outcomes métier n’est explicite.

La direction voit ces produits comme des programmes autonomes, mais leur valeur dépend d'un parcours métier unique de gestion des exceptions. Le budget est limité et plusieurs solutions sont déjà présentes dans le groupe. Finance demande de relier les dépenses aux bénéfices métier et de justifier les dépendances. Le Board attend une trajectoire alignée sur les capabilities plutôt qu'une liste de composants techniques.

Quelle action est la meilleure ?
A. Utiliser Capability-Based Planning pour relier les investissements aux capabilities/outcomes nécessaires, puis déterminer les building blocks et work packages qui les réalisent.
B. Commencer par une carte de capabilities métier et la relier aux principaux produits, sans prioriser encore les work packages sur les gaps.
C. Construire une première carte de capabilities et associer les produits aux fonctions qu'ils supportent, puis évaluer les gains à la prochaine revue.
D. Financer d'abord la plateforme la moins coûteuse en supposant qu'elle créera automatiquement la capacité métier recherchée.
**Scoring : A=5, B=3, C=1, D=0.**

**Justification des quatre niveaux :**

- **A — 5 points :** Utiliser Capability-Based Planning pour relier les investissements aux capabilities/outcomes nécessaires, puis déterminer les building blocks et work packages qui les réalisent. Capability-Based Planning relie outcomes et investissements aux capacités.
- **B — 3 points :** Commencer par une carte de capabilities métier et la relier aux principaux produits, sans prioriser encore les work packages sur les gaps. Une capability map initie le travail sans prioriser les work packages.
- **C — 1 point :** Construire une première carte de capabilities et associer les produits aux fonctions qu'ils supportent, puis évaluer les gains à la prochaine revue. Un inventaire applicatif ne mesure pas les capacités manquantes.
- **D — 0 point :** Financer d'abord la plateforme la moins coûteuse en supposant qu'elle créera automatiquement la capacité métier recherchée. Partir des produits déployés plutôt que des besoins biaise la Roadmap.

**Mapping : Supporting ADM Work — Capability-Based Planning.**

**Référence d'étude :** X2202, Practitioner, unité 8 ; TOGAF Standard / Series Guides applicables.

---
## S058 — Deux systèmes « compatibles » qui ne coopèrent pas

Deux applications utilisent toutes deux REST/JSON mais emploient des identifiants client, statuts et règles de transaction incompatibles. L’équipe conclut que l’interopérabilité est acquise parce que le protocole est commun.

La plateforme retail et la plateforme corporate produisent des données client portant des significations différentes. Les interfaces REST fonctionnent en test, mais les rejets métier augmentent dès que les services interprètent les codes et identifiants. Les responsables Data veulent fixer un vocabulaire commun et Operations demande une traçabilité de bout en bout. Le sponsor se demande si une migration technologique serait vraiment nécessaire.

Quelle action est la meilleure ?
A. Remplacer un des deux frameworks API pour uniformiser les protocoles, sans vérifier la compatibilité sémantique des échanges.
B. Évaluer l’interopérabilité sur plusieurs dimensions — sémantique, information, processus, technique et gouvernance — et traiter les incompatibilités.
C. Revoir les contrats d'échange et la sémantique de l'information avant toute refonte, sans établir encore un modèle complet d'interopérabilité.
D. Comparer les modèles d'information et définir une table de correspondance pour les champs les plus critiques, puis élargir les contrats de service.
**Scoring : A=0, B=5, C=3, D=1.**

**Justification des quatre niveaux :**

- **B — 5 points :** Évaluer l’interopérabilité sur plusieurs dimensions — sémantique, information, processus, technique et gouvernance — et traiter les incompatibilités. L'analyse interopérabilité couvre sens des données, contrats, processus et gouvernance des deux partenaires.
- **C — 3 points :** Revoir les contrats d'échange et la sémantique de l'information avant toute refonte, sans établir encore un modèle complet d'interopérabilité. La sémantique et les contrats constituent une première analyse solide, mais pas tous les impacts.
- **D — 1 points :** Comparer les modèles d'information et définir une table de correspondance pour les champs les plus critiques, puis élargir les contrats de service. Une table de correspondance améliore certains champs sans traiter l'ensemble des processus et contrats.
- **A — 0 points :** Remplacer un des deux frameworks API pour uniformiser les protocoles, sans vérifier la compatibilité sémantique des échanges. Uniformiser le protocole ne résout pas la divergence de sens des statuts métier.

**Mapping : Supporting ADM Work — Interoperability.**

**Référence d'étude :** X2202, Practitioner, unité 8 ; TOGAF Standard / Series Guides applicables.

---
## S059 — Deliverable, artifact ou building block ?

Le comité demande l’Architecture Definition Document. L’équipe répond qu’un seul diagramme de services « est le deliverable complet » et que chaque service représenté est un artifact.

Le comité attend un livrable formel permettant la validation de plusieurs domaines et de leurs implications ; l'équipe a seulement produit un diagramme d'API. Les architectes veulent accélérer la revue en appelant les services représentés des artifacts. Le Business Owner demande une preuve que la cible répond aux concerns métier et Operations veut les éléments de reprise. La distinction entre représentation, composant et livrable influence donc la décision.

Quelle correction est la meilleure ?
A. Requalifier correctement le diagramme comme artifact et recenser les building blocks, puis compléter progressivement les autres éléments du livrable.
B. Conserver le diagramme comme preuve d'architecture approuvable et ajouter la liste des standards technologiques comme annexe au dossier.
C. Expliquer que le deliverable est le produit de travail formel, qu’il peut contenir plusieurs artifacts, et que les services/capacités représentés peuvent être des building blocks.
D. Requalifier le diagramme comme artifact du livrable et lister les building blocks représentés, tout en laissant à compléter les autres vues requises.
**Scoring : A=1, B=0, C=5, D=3.**

**Justification des quatre niveaux :**

- **C — 5 points :** Expliquer que le deliverable est le produit de travail formel, qu’il peut contenir plusieurs artifacts, et que les services/capacités représentés peuvent être des building blocks. Le Framework distingue deliverable formel, artifact et building block.
- **D — 3 points :** Requalifier le diagramme comme artifact du livrable et lister les building blocks représentés, tout en laissant à compléter les autres vues requises. Un diagramme seul ne décrit pas toutes les obligations du livrable.
- **A — 1 point :** Requalifier correctement le diagramme comme artifact et recenser les building blocks, puis compléter progressivement les autres éléments du livrable. Un composant de solution n'est pas un document d'architecture.
- **B — 0 point :** Conserver le diagramme comme preuve d'architecture approuvable et ajouter la liste des standards technologiques comme annexe au dossier. Confondre les catégories détruit la traçabilité entre intention et réalisation.

**Mapping : Supporting ADM Work — Architecture Content.**

**Référence d'étude :** X2202, Practitioner, unité 8 ; TOGAF Standard / Series Guides applicables.

---
## S060 — Réutilisation et adaptation

Une nouvelle initiative ressemble fortement à une transformation précédente. Le Repository contient Architecture Vision, patterns, standards, lessons learned et building blocks. L’équipe hésite entre copier intégralement l’ancienne architecture ou repartir de zéro.

Le précédent programme portait sur des paiements domestiques alors que l'initiative courante doit servir plusieurs juridictions. Le sponsor veut réduire les coûts en réutilisant les assets existants, tandis que Risk signale de nouveaux contrôles de données et de résilience. Les architectes doivent vérifier les hypothèses initiales, distinguer standards toujours valides et décisions de solution locales, puis documenter les adaptations nécessaires.

Quelle action est la meilleure ?
A. Réutiliser une partie des patterns existants après une comparaison technique préliminaire, avant la revue complète du scope et des concerns.
B. Reprendre les standards et patterns du Repository après la seule vérification des versions logicielles, en considérant la compatibilité de produits comme validation du nouveau contexte métier.
C. Cloner la Target Architecture précédente et ne modifier que les diagrammes de déploiement, en considérant les décisions métier acquises.
D. Rechercher les assets pertinents, évaluer leur réutilisabilité dans le nouveau contexte, adapter ce qui est applicable et documenter ce qui doit changer.
**Scoring : A=3, B=1, C=0, D=5.**

**Justification des quatre niveaux :**

- **D — 5 points :** Rechercher les assets pertinents, évaluer leur réutilisabilité dans le nouveau contexte, adapter ce qui est applicable et documenter ce qui doit changer. La réutilisation exige comparaison des hypothèses d'origine, contraintes, risques et besoins réels.
- **A — 3 points :** Réutiliser une partie des patterns existants après une comparaison technique préliminaire, avant la revue complète du scope et des concerns. Une comparaison technique préalable est utile, mais la validité métier et réglementaire reste à démontrer.
- **B — 1 points :** Reprendre les standards et patterns du Repository après la seule vérification des versions logicielles, en considérant la compatibilité de produits comme validation du nouveau contexte métier. Des versions compatibles ne prouvent ni la valeur ni la conformité d'un pattern dans le nouveau contexte.
- **C — 0 points :** Cloner la Target Architecture précédente et ne modifier que les diagrammes de déploiement, en considérant les décisions métier acquises. Le clonage des seuls diagrammes reproduit sans examen les hypothèses de la cible antérieure.

**Mapping : Supporting ADM Work — Repository / Reuse / Tailoring.**

**Référence d'étude :** X2202, Practitioner, unité 8 ; TOGAF Standard / Series Guides applicables.

---
