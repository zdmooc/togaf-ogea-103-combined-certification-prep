# Practitioner Scenarios — Supporting the ADM Work

## S053 — Transformer une idée vague en besoin exploitable

La direction dit : « nous devons devenir la banque la plus rapide sur les paiements ». Aucun acteur, problème concret ni résultat mesurable n’est défini.

Quelle technique aiderait le mieux à démarrer ?

A. Utiliser un Business Scenario pour expliciter problème/opportunité, acteurs, environnement, desired outcomes et requirements.  
B. Faire immédiatement une Gap Analysis détaillée de Technology Architecture.  
C. Écrire un Architecture Contract avec le fournisseur.  
D. Lancer une Compliance Review.

**Scoring : A=5, B=3, C=1, D=0.**

**Pourquoi A :** le Business Scenario aide à passer d’une ambition vague à des requirements contextualisées. B suppose une Baseline/Target plus avancée ; C et D interviennent dans des contextes différents.

**Mapping : Supporting ADM Work — Business Scenarios.**

---

## S054 — Une Gap Analysis qui choisit déjà la solution

Une équipe compare Baseline et Target. Pour chaque gap, elle inscrit immédiatement un nom de produit unique sans distinguer le besoin de la solution.

Quelle action est la meilleure ?

A. Identifier d’abord les différences à conserver, supprimer, modifier ou créer ; utiliser ensuite ces gaps comme entrée des options de solution et work packages.  
B. Conserver les noms de produits comme définition des gaps.  
C. Supprimer la Gap Analysis et passer directement à Phase G.  
D. Classer tous les gaps comme requirements de sécurité.

**Scoring : A=5, B=3, D=1, C=0.**

**Pourquoi A :** Gap Analysis identifie ce qui change ; elle ne doit pas confondre différence architecturale et solution choisie. B peut accélérer mais crée un biais ; D déforme les gaps ; C saute l’analyse.

**Mapping : Supporting ADM Work — Gap Analysis.**

---

## S055 — Organisation pas prête

La Target est techniquement faisable. Pourtant, aucune équipe ne sait exploiter la nouvelle plateforme, le support fournisseur n’est pas contractualisé et le modèle opérationnel n’existe pas.

Quelle action est la meilleure ?

A. Utiliser une Business Transformation Readiness Assessment pour identifier les facteurs de readiness et intégrer les actions nécessaires à la transformation.  
B. Considérer que la faisabilité technique suffit.  
C. Reporter tous les sujets humains et opérationnels après la mise en production.  
D. Changer automatiquement de fournisseur.

**Scoring : A=5, D=3, B=1, C=0.**

**Pourquoi A :** readiness couvre compétences, organisation, gouvernance et capacité à changer. D peut être une option si le fournisseur est réellement la cause mais ne couvre pas le problème complet ; B/C ignorent la capacité de transformation.

**Mapping : Supporting ADM Work — Business Transformation Readiness.**

---

## S056 — Risque résiduel caché

Après plusieurs controls, un risque de perte temporaire de service subsiste lors d’une migration. L’équipe veut marquer le risque « fermé » parce que des mesures existent.

Quelle action est la meilleure ?

A. Distinguer risque initial, mitigation et residual risk, attribuer ownership et obtenir l’acceptation/escalade appropriée du risque résiduel.  
B. Fermer le risque dès qu’un control existe.  
C. Supprimer le risque du Repository pour ne pas retarder le programme.  
D. Considérer qu’Architecture Governance ne traite jamais les risques.

**Scoring : A=5, B=3, D=1, C=0.**

**Pourquoi A :** un control réduit un risque sans nécessairement l’éliminer. B reconnaît la mitigation mais confond traitement et disparition ; D réduit la gouvernance ; C détruit la traçabilité.

**Mapping : Supporting ADM Work — Risk Management.**

---

## S057 — Planifier par capability

La direction veut financer « Kafka », « Kubernetes » et « API Gateway » comme trois programmes indépendants. Aucun lien avec les outcomes métier n’est explicite.

Quelle action est la meilleure ?

A. Utiliser Capability-Based Planning pour relier les investissements aux capabilities/outcomes nécessaires, puis déterminer les building blocks et work packages qui les réalisent.  
B. Conserver les produits comme capacités métier.  
C. Financer uniquement la technologie la plus populaire.  
D. Attendre Phase G pour identifier les outcomes.

**Scoring : A=5, B=3, C=1, D=0.**

**Pourquoi A :** capability-based planning part de ce que l’entreprise doit être capable de faire. B confond capability et solution ; C n’est pas un critère d’architecture ; D intervient trop tard.

**Mapping : Supporting ADM Work — Capability-Based Planning.**

---

## S058 — Deux systèmes « compatibles » qui ne coopèrent pas

Deux applications utilisent toutes deux REST/JSON mais emploient des identifiants client, statuts et règles de transaction incompatibles. L’équipe conclut que l’interopérabilité est acquise parce que le protocole est commun.

Quelle action est la meilleure ?

A. Évaluer l’interopérabilité sur plusieurs dimensions — sémantique, information, processus, technique et gouvernance — et traiter les incompatibilités.  
B. Considérer REST/JSON comme preuve suffisante.  
C. Remplacer automatiquement les deux applications.  
D. Traiter le problème seulement comme un incident réseau.

**Scoring : A=5, C=3, B=1, D=0.**

**Pourquoi A :** même protocole ne signifie pas compréhension commune. C peut résoudre le problème mais de façon disproportionnée ; B réduit l’interopérabilité au transport ; D vise le mauvais niveau.

**Mapping : Supporting ADM Work — Interoperability.**

---

## S059 — Deliverable, artifact ou building block ?

Le comité demande l’Architecture Definition Document. L’équipe répond qu’un seul diagramme de services « est le deliverable complet » et que chaque service représenté est un artifact.

Quelle correction est la meilleure ?

A. Expliquer que le deliverable est le produit de travail formel, qu’il peut contenir plusieurs artifacts, et que les services/capacités représentés peuvent être des building blocks.  
B. Confirmer que deliverable, artifact et building block sont synonymes.  
C. Appeler chaque diagramme un SBB.  
D. Supprimer les distinctions car elles n’ont aucun rôle dans l’ADM.

**Scoring : A=5, B=3, C=1, D=0.**

**Pourquoi A :** la distinction aide à comprendre le Content Framework et la traçabilité du travail. B simplifie mais devient conceptuellement faux ; C confond représentation et élément d’architecture ; D supprime une distinction évaluée.

**Mapping : Supporting ADM Work — Architecture Content.**

---

## S060 — Réutilisation et adaptation

Une nouvelle initiative ressemble fortement à une transformation précédente. Le Repository contient Architecture Vision, patterns, standards, lessons learned et building blocks. L’équipe hésite entre copier intégralement l’ancienne architecture ou repartir de zéro.

Quelle action est la meilleure ?

A. Rechercher les assets pertinents, évaluer leur réutilisabilité dans le nouveau contexte, adapter ce qui est applicable et documenter ce qui doit changer.  
B. Copier l’architecture précédente sans vérifier scope, stakeholders ni requirements.  
C. Ignorer tous les assets pour éviter l’influence du passé.  
D. Réutiliser uniquement les noms de produits.

**Scoring : A=5, B=3, D=1, C=0.**

**Pourquoi A :** le Repository soutient la réutilisation mais TOGAF reste contextuel. B valorise le reuse mais sans tailoring ; D réduit l’architecture aux solutions ; C gaspille les connaissances existantes.

**Mapping : Supporting ADM Work — Repository / Reuse / Tailoring.**

---

Contenu pédagogique original ; aucun scénario officiel n’est reproduit.