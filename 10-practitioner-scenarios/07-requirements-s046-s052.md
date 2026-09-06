# Practitioner Scenarios — Requirements Management

## S046 — Requirement trop vague

Le sponsor écrit : « la nouvelle plateforme doit être très résiliente ». Les équipes interprètent cette phrase de manière différente.

Quelle action est la meilleure ?

A. Décomposer et clarifier la requirement en critères vérifiables — disponibilité, RTO/RPO, modes de défaillance, failover, tests — tout en conservant la traçabilité vers le concern initial.  
B. Laisser chaque équipe définir sa propre notion de résilience.  
C. Choisir un produit “high availability” et considérer la requirement satisfaite.  
D. Supprimer la requirement car elle est ambiguë.

**Scoring : A=5, C=3, B=1, D=0.**

**Pourquoi A :** Requirements Management transforme des besoins en exigences compréhensibles et testables. C peut contribuer à la satisfaction mais confond moyen et requirement ; B crée l’incohérence ; D perd le besoin.

**Mapping : Requirements Management — Quality of Requirements.**

---

## S047 — Requirements contradictoires

Finance exige de réduire fortement les coûts d’infrastructure. Operations exige une redondance maximale sur tous les composants. Les deux requirements sont approuvées séparément mais deviennent incompatibles dans la Target.

Quelle action est la meilleure ?

A. Rendre le conflit explicite, analyser trade-offs et impacts, impliquer les stakeholders concernés et obtenir un arbitrage gouverné avec requirements mises à jour.  
B. Satisfaire automatiquement Finance.  
C. Satisfaire automatiquement Operations.  
D. Maintenir les deux requirements inchangées et laisser le delivery résoudre le conflit.

**Scoring : A=5, C=3, B=1, D=0.**

**Pourquoi A :** Requirements Management inclut identification et résolution des conflits. C peut être prudente pour la continuité mais n’est pas un arbitrage complet ; B privilégie un concern ; D déplace une contradiction non résolue.

**Mapping : Requirements Management — Conflicting Requirements.**

---

## S048 — Requirement sans traçabilité

Une exigence de chiffrement apparaît dans le document Technology, mais personne ne sait quel stakeholder ou quelle obligation l’a créée. Elle n’est reliée ni aux controls sécurité ni aux décisions de Phase A.

Quelle action est la meilleure ?

A. Restaurer la traçabilité vers source/concern, analyser où la requirement s’applique et relier les artifacts et building blocks concernés.  
B. La supprimer car son origine n’est pas immédiatement connue.  
C. La conserver comme texte isolé sans analyse.  
D. Choisir un algorithme de chiffrement et clôturer la requirement.

**Scoring : A=5, C=3, D=1, B=0.**

**Pourquoi A :** une requirement doit pouvoir être comprise, tracée et liée aux décisions d’architecture. C préserve l’exigence mais pas sa gouvernance ; D saute au design ; B risque de supprimer une obligation valide.

**Mapping : Requirements Management — Traceability.**

---

## S049 — Nouvelle requirement en Phase F

Pendant Migration Planning, un régulateur impose un nouveau contrôle sur les données. La requirement affecte Data Architecture et le séquencement des work packages.

Quelle action est la meilleure ?

A. Enregistrer et analyser la nouvelle requirement, itérer sur les architectures impactées si nécessaire, puis mettre à jour gaps, work packages et Migration Plan.  
B. Ignorer la requirement car les Phases C et E sont terminées.  
C. L’ajouter seulement au backlog du dernier projet.  
D. Attendre Phase H après mise en production.

**Scoring : A=5, C=3, D=1, B=0.**

**Pourquoi A :** Requirements Management traverse l’ADM et peut provoquer une itération. C reconnaît l’exigence mais ne traite pas l’impact architectural ; D est tardif ; B viole la logique transversale.

**Mapping : Requirements Management — Change during ADM / Iteration.**

---

## S050 — Requirement devenue obsolète

Une requirement interdisait le cloud à cause d’une politique interne. La politique vient d’être remplacée et le sponsor veut conserver l’exigence « parce qu’elle a déjà été approuvée ».

Quelle action est la meilleure ?

A. Réévaluer la requirement, sa source et sa validité ; la modifier ou la retirer de manière gouvernée et tracer la décision.  
B. Ne jamais modifier une requirement approuvée.  
C. La supprimer silencieusement.  
D. Modifier uniquement le diagramme Technology sans toucher au registre des requirements.

**Scoring : A=5, B=3, D=1, C=0.**

**Pourquoi A :** les requirements évoluent avec les drivers et constraints. B assure une stabilité apparente mais fige une contrainte obsolète ; D crée une incohérence ; C détruit la traçabilité.

**Mapping : Requirements Management — Requirement Lifecycle.**

---

## S051 — Principle ou requirement ?

MayaBank possède le principe « Security by Design ». Pour une plateforme spécifique, le CISO exige que tous les secrets soient stockés dans un service approuvé et renouvelés automatiquement.

Quelle distinction est la meilleure ?

A. Le principe guide durablement les décisions ; la règle précise de gestion des secrets est une requirement/standard applicable au contexte et doit être tracée comme telle.  
B. Les deux éléments sont exactement le même type d’objet.  
C. Le principe doit être supprimé dès qu’une requirement existe.  
D. La requirement ne doit jamais être liée au principe.

**Scoring : A=5, B=3, D=1, C=0.**

**Pourquoi A :** principle et requirement se complètent mais ne sont pas synonymes. B reconnaît leur lien mais perd la distinction de granularité ; D coupe une trace utile ; C est faux.

**Mapping : Requirements Management — Principle vs Requirement.**

---

## S052 — Beaucoup de requirements, aucune priorité

Le programme possède 250 requirements toutes marquées « critique ». Les équipes ne peuvent pas arbitrer ni savoir lesquelles conditionnent la réussite de la transformation.

Quelle action est la meilleure ?

A. Revoir la qualité, source, priorité, dépendances et critères d’acceptation des requirements avec les stakeholders, puis maintenir une gouvernance de changement.  
B. Considérer toutes les requirements également prioritaires.  
C. Laisser le chef de projet supprimer celles qui ralentissent le planning.  
D. Remplacer les requirements par la liste des produits choisis.

**Scoring : A=5, B=3, C=1, D=0.**

**Pourquoi A :** un registre utile doit soutenir les décisions, pas seulement accumuler du texte. B évite un arbitrage arbitraire mais rend la priorité inutilisable ; C retire la gouvernance ; D confond besoins et solutions.

**Mapping : Requirements Management — Prioritization / Governance.**

---

Contenu pédagogique original ; aucun scénario officiel n’est reproduit.