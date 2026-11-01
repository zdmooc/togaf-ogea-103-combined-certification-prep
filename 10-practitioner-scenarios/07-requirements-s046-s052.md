# Practitioner Scenarios — Requirements Management

## S046 — Requirement trop vague

Le sponsor écrit : « la nouvelle plateforme doit être très résiliente ». Les équipes interprètent cette phrase de manière différente.

Quelle action est la meilleure ?
A. Supprimer la requirement car elle est ambiguë.
B. Décomposer et clarifier la requirement en critères vérifiables — disponibilité, RTO/RPO, modes de défaillance, failover, tests — tout en conservant la traçabilité vers le concern initial.
C. Définir un premier seuil quantifié de disponibilité puis compléter les conditions de mesure et la validation par Operations.
D. Laisser chaque équipe définir sa propre notion de résilience.
**Scoring : A=0, B=5, C=3, D=1.**

**Justification révisée :** le choix B (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix C (3 points) constitue une étape utile, mais partielle : définir un premier seuil quantifié de disponibilité puis compléter les conditions de mesure et la validation par Operations. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Requirements Management — Quality of Requirements.**

---

## S047 — Requirements contradictoires

Finance exige de réduire fortement les coûts d’infrastructure. Operations exige une redondance maximale sur tous les composants. Les deux requirements sont approuvées séparément mais deviennent incompatibles dans la Target.

Quelle action est la meilleure ?
A. Satisfaire automatiquement Finance.
B. Maintenir les deux requirements inchangées et laisser le delivery résoudre le conflit.
C. Rendre le conflit explicite, analyser trade-offs et impacts, impliquer les stakeholders concernés et obtenir un arbitrage gouverné avec requirements mises à jour.
D. Faire expliciter et documenter les impacts des deux exigences, puis préparer une proposition de compromis pour l'autorité de décision.
**Scoring : A=1, B=0, C=5, D=3.**

**Justification révisée :** le choix C (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix D (3 points) constitue une étape utile, mais partielle : faire expliciter et documenter les impacts des deux exigences, puis préparer une proposition de compromis pour l'autorité de décision. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Requirements Management — Conflicting Requirements.**

---

## S048 — Requirement sans traçabilité

Une exigence de chiffrement apparaît dans le document Technology, mais personne ne sait quel stakeholder ou quelle obligation l’a créée. Elle n’est reliée ni aux controls sécurité ni aux décisions de Phase A.

Quelle action est la meilleure ?
A. Rattacher l'exigence au composant principal et à un critère de vérification, puis étendre ensuite la traçabilité aux autres dépendances.
B. Choisir un algorithme de chiffrement et clôturer la requirement.
C. La supprimer car son origine n’est pas immédiatement connue.
D. Restaurer la traçabilité vers source/concern, analyser où la requirement s’applique et relier les artifacts et building blocks concernés.
**Scoring : A=3, B=1, C=0, D=5.**

**Justification révisée :** le choix D (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix A (3 points) constitue une étape utile, mais partielle : rattacher l'exigence au composant principal et à un critère de vérification, puis étendre ensuite la traçabilité aux autres dépendances. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Requirements Management — Traceability.**

---

## S049 — Nouvelle requirement en Phase F

Pendant Migration Planning, un régulateur impose un nouveau contrôle sur les données. La requirement affecte Data Architecture et le séquencement des work packages.

Quelle action est la meilleure ?
A. Enregistrer et analyser la nouvelle requirement, itérer sur les architectures impactées si nécessaire, puis mettre à jour gaps, work packages et Migration Plan.
B. Ouvrir une évaluation d'impact de la nouvelle requirement sur le planning de migration avant de décider des ajustements du plan approuvé.
C. Attendre Phase H après mise en production.
D. Ignorer la requirement car les Phases C et E sont terminées.
**Scoring : A=5, B=3, C=1, D=0.**

**Justification révisée :** le choix A (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix B (3 points) constitue une étape utile, mais partielle : ouvrir une évaluation d'impact de la nouvelle requirement sur le planning de migration avant de décider des ajustements du plan approuvé. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Requirements Management — Change during ADM / Iteration.**

---

## S050 — Requirement devenue obsolète

Une requirement interdisait le cloud à cause d’une politique interne. La politique vient d’être remplacée et le sponsor veut conserver l’exigence « parce qu’elle a déjà été approuvée ».

Quelle action est la meilleure ?
A. La supprimer silencieusement.
B. Réévaluer la requirement, sa source et sa validité ; la modifier ou la retirer de manière gouvernée et tracer la décision.
C. Soumettre la requirement à une nouvelle validation avec son sponsor et conserver l'historique des versions avant de la retirer ou de la modifier.
D. Modifier uniquement le diagramme Technology sans toucher au registre des requirements.
**Scoring : A=0, B=5, C=3, D=1.**

**Justification révisée :** le choix B (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix C (3 points) constitue une étape utile, mais partielle : soumettre la requirement à une nouvelle validation avec son sponsor et conserver l'historique des versions avant de la retirer ou de la modifier. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Requirements Management — Requirement Lifecycle.**

---

## S051 — Principle ou requirement ?

MayaBank possède le principe « Security by Design ». Pour une plateforme spécifique, le CISO exige que tous les secrets soient stockés dans un service approuvé et renouvelés automatiquement.

Quelle distinction est la meilleure ?
A. La requirement ne doit jamais être liée au principe.
B. Le principe doit être supprimé dès qu’une requirement existe.
C. Le principe guide durablement les décisions ; la règle précise de gestion des secrets est une requirement/standard applicable au contexte et doit être tracée comme telle.
D. Conserver le principe comme règle de décision et rédiger une exigence mesurable dérivée, sans encore expliciter toutes les implications.
**Scoring : A=1, B=0, C=5, D=3.**

**Justification révisée :** le choix C (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix D (3 points) constitue une étape utile, mais partielle : conserver le principe comme règle de décision et rédiger une exigence mesurable dérivée, sans encore expliciter toutes les implications. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Requirements Management — Principle vs Requirement.**

---

## S052 — Beaucoup de requirements, aucune priorité

Le programme possède 250 requirements toutes marquées « critique ». Les équipes ne peuvent pas arbitrer ni savoir lesquelles conditionnent la réussite de la transformation.

Quelle action est la meilleure ?
A. Prioriser d'abord les exigences réglementaires et de sécurité, puis compléter l'arbitrage avec valeur, risques et dépendances.
B. Laisser le chef de projet supprimer celles qui ralentissent le planning.
C. Remplacer les requirements par la liste des produits choisis.
D. Revoir la qualité, source, priorité, dépendances et critères d’acceptation des requirements avec les stakeholders, puis maintenir une gouvernance de changement.
**Scoring : A=3, B=1, C=0, D=5.**

**Justification révisée :** le choix D (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix A (3 points) constitue une étape utile, mais partielle : prioriser d'abord les exigences réglementaires et de sécurité, puis compléter l'arbitrage avec valeur, risques et dépendances. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Requirements Management — Prioritization / Governance.**

---

Contenu pédagogique original ; aucun scénario officiel n’est reproduit.