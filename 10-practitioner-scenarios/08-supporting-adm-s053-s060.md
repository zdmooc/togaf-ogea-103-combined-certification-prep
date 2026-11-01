# Practitioner Scenarios — Supporting the ADM Work

## S053 — Transformer une idée vague en besoin exploitable

La direction dit : « nous devons devenir la banque la plus rapide sur les paiements ». Aucun acteur, problème concret ni résultat mesurable n’est défini.

Quelle technique aiderait le mieux à démarrer ?
A. Utiliser un Business Scenario pour expliciter problème/opportunité, acteurs, environnement, desired outcomes et requirements.
B. Utiliser un entretien métier structuré pour clarifier objectifs, acteurs et indicateurs, puis formaliser un Business Scenario dans un second temps.
C. Écrire un Architecture Contract avec le fournisseur.
D. Lancer une Compliance Review.
**Scoring : A=5, B=3, C=1, D=0.**

**Justification révisée :** le choix A (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix B (3 points) constitue une étape utile, mais partielle : utiliser un entretien métier structuré pour clarifier objectifs, acteurs et indicateurs, puis formaliser un Business Scenario dans un second temps. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Supporting ADM Work — Business Scenarios.**

---

## S054 — Une Gap Analysis qui choisit déjà la solution

Une équipe compare Baseline et Target. Pour chaque gap, elle inscrit immédiatement un nom de produit unique sans distinguer le besoin de la solution.

Quelle action est la meilleure ?
A. Supprimer la Gap Analysis et passer directement à Phase G.
B. Identifier d’abord les différences à conserver, supprimer, modifier ou créer ; utiliser ensuite ces gaps comme entrée des options de solution et work packages.
C. Conserver les produits candidats dans une colonne de solutions potentielles tout en distinguant les gaps architecturaux eux-mêmes.
D. Classer tous les gaps comme requirements de sécurité.
**Scoring : A=0, B=5, C=3, D=1.**

**Justification révisée :** le choix B (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix C (3 points) constitue une étape utile, mais partielle : conserver les produits candidats dans une colonne de solutions potentielles tout en distinguant les gaps architecturaux eux-mêmes. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Supporting ADM Work — Gap Analysis.**

---

## S055 — Organisation pas prête

La Target est techniquement faisable. Pourtant, aucune équipe ne sait exploiter la nouvelle plateforme, le support fournisseur n’est pas contractualisé et le modèle opérationnel n’existe pas.

Quelle action est la meilleure ?
A. Considérer que la faisabilité technique suffit.
B. Reporter tous les sujets humains et opérationnels après la mise en production.
C. Utiliser une Business Transformation Readiness Assessment pour identifier les facteurs de readiness et intégrer les actions nécessaires à la transformation.
D. Conduire une évaluation limitée des compétences et du modèle opérationnel avec les responsables de plateforme, puis enrichir l'évaluation globale de readiness.
**Scoring : A=1, B=0, C=5, D=3.**

**Justification révisée :** le choix C (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix D (3 points) constitue une étape utile, mais partielle : conduire une évaluation limitée des compétences et du modèle opérationnel avec les responsables de plateforme, puis enrichir l'évaluation globale de readiness. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Supporting ADM Work — Business Transformation Readiness.**

---

## S056 — Risque résiduel caché

Après plusieurs controls, un risque de perte temporaire de service subsiste lors d’une migration. L’équipe veut marquer le risque « fermé » parce que des mesures existent.

Quelle action est la meilleure ?
A. Maintenir la mitigation et son suivi dans le registre de risque, tout en demandant une validation différée de l'acceptation du risque résiduel.
B. Considérer qu’Architecture Governance ne traite jamais les risques.
C. Supprimer le risque du Repository pour ne pas retarder le programme.
D. Distinguer risque initial, mitigation et residual risk, attribuer ownership et obtenir l’acceptation/escalade appropriée du risque résiduel.
**Scoring : A=3, B=1, C=0, D=5.**

**Justification révisée :** le choix D (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix A (3 points) constitue une étape utile, mais partielle : maintenir la mitigation et son suivi dans le registre de risque, tout en demandant une validation différée de l'acceptation du risque résiduel. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Supporting ADM Work — Risk Management.**

---

## S057 — Planifier par capability

La direction veut financer « Kafka », « Kubernetes » et « API Gateway » comme trois programmes indépendants. Aucun lien avec les outcomes métier n’est explicite.

Quelle action est la meilleure ?
A. Utiliser Capability-Based Planning pour relier les investissements aux capabilities/outcomes nécessaires, puis déterminer les building blocks et work packages qui les réalisent.
B. Commencer par une carte de capabilities métier et la relier aux principaux produits, sans prioriser encore les work packages sur les gaps.
C. Financer uniquement la technologie la plus populaire.
D. Attendre Phase G pour identifier les outcomes.
**Scoring : A=5, B=3, C=1, D=0.**

**Justification révisée :** le choix A (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix B (3 points) constitue une étape utile, mais partielle : commencer par une carte de capabilities métier et la relier aux principaux produits, sans prioriser encore les work packages sur les gaps. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Supporting ADM Work — Capability-Based Planning.**

---

## S058 — Deux systèmes « compatibles » qui ne coopèrent pas

Deux applications utilisent toutes deux REST/JSON mais emploient des identifiants client, statuts et règles de transaction incompatibles. L’équipe conclut que l’interopérabilité est acquise parce que le protocole est commun.

Quelle action est la meilleure ?
A. Traiter le problème seulement comme un incident réseau.
B. Évaluer l’interopérabilité sur plusieurs dimensions — sémantique, information, processus, technique et gouvernance — et traiter les incompatibilités.
C. Revoir les contrats d'échange et la sémantique de l'information avant toute refonte, sans établir encore un modèle complet d'interopérabilité.
D. Considérer REST/JSON comme preuve suffisante.
**Scoring : A=0, B=5, C=3, D=1.**

**Justification révisée :** le choix B (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix C (3 points) constitue une étape utile, mais partielle : revoir les contrats d'échange et la sémantique de l'information avant toute refonte, sans établir encore un modèle complet d'interopérabilité. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Supporting ADM Work — Interoperability.**

---

## S059 — Deliverable, artifact ou building block ?

Le comité demande l’Architecture Definition Document. L’équipe répond qu’un seul diagramme de services « est le deliverable complet » et que chaque service représenté est un artifact.

Quelle correction est la meilleure ?
A. Appeler chaque diagramme un SBB.
B. Supprimer les distinctions car elles n’ont aucun rôle dans l’ADM.
C. Expliquer que le deliverable est le produit de travail formel, qu’il peut contenir plusieurs artifacts, et que les services/capacités représentés peuvent être des building blocks.
D. Requalifier le diagramme comme artifact du livrable et lister les building blocks représentés, tout en laissant à compléter les autres vues requises.
**Scoring : A=1, B=0, C=5, D=3.**

**Justification révisée :** le choix C (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix D (3 points) constitue une étape utile, mais partielle : requalifier le diagramme comme artifact du livrable et lister les building blocks représentés, tout en laissant à compléter les autres vues requises. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Supporting ADM Work — Architecture Content.**

---

## S060 — Réutilisation et adaptation

Une nouvelle initiative ressemble fortement à une transformation précédente. Le Repository contient Architecture Vision, patterns, standards, lessons learned et building blocks. L’équipe hésite entre copier intégralement l’ancienne architecture ou repartir de zéro.

Quelle action est la meilleure ?
A. Réutiliser une partie des patterns existants après une comparaison technique préliminaire, avant la revue complète du scope et des concerns.
B. Réutiliser uniquement les noms de produits.
C. Ignorer tous les assets pour éviter l’influence du passé.
D. Rechercher les assets pertinents, évaluer leur réutilisabilité dans le nouveau contexte, adapter ce qui est applicable et documenter ce qui doit changer.
**Scoring : A=3, B=1, C=0, D=5.**

**Justification révisée :** le choix D (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix A (3 points) constitue une étape utile, mais partielle : réutiliser une partie des patterns existants après une comparaison technique préliminaire, avant la revue complète du scope et des concerns. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Supporting ADM Work — Repository / Reuse / Tailoring.**

---

Contenu pédagogique original ; aucun scénario officiel n’est reproduit.