# Corrigés XP33–XP36 — classification et décisions nuancées

## XP33 — L2.1.5

**Barème pédagogique :** A=1, B=5, C=3, D=0.

- **B, 5 points :** Les éléments *livrés* sont conformes, mais la spécification contient encore l'audit des rejets non réalisé : le niveau **Compliant** convient. Le gap reste à suivre dans le dispositif d'implémentation.
- **C, 3 points :** Prendre des preuves et recontrôler l'étendue des fonctions est prudent. Toutefois, l'énoncé exclut les fonctions additionnelles et apporte déjà assez d'information pour conclure **Compliant** plutôt que **Consistent**.
- **A, 1 point :** **Conformant** suppose que tous les éléments spécifiés ont été correctement réalisés. L'audit manque ; la classification est prématurée.
- **D, 0 point :** **Fully Conformant** demanderait une correspondance complète ; écarter l'audit contredit la spécification approuvée.

## XP34 — L2.1.5

**Barème pédagogique :** A=1, B=3, C=0, D=5.

- **D, 5 points :** Toutes les fonctions spécifiées sont réalisées et le reporting constitue une fonction additionnelle sans contradiction : niveau **Conformant**, non **Fully Conformant**. La trace de l'extension dépend de son impact.
- **B, 3 points :** La réponse reconnaît que les obligations sont toutes satisfaites, mais confond la conformité exacte avec une implémentation disposant d'une fonction supplémentaire. La nuance de classification manque.
- **A, 1 point :** **Compliant** n'est pas la classe la plus précise quand la spécification entière est réalisée et que l'implémentation comporte un ajout.
- **C, 0 point :** Une fonction additionnelle qui ne contredit pas la spécification ne suffit pas à conclure **Non-conformant**.

## XP35 — L2.5.3

**Barème pédagogique :** A=5, B=3, C=1, D=0.

- **A, 5 points :** La création sans existant se prête à **greenfield** ; la coexistence du moteur et de ses partenaires justifie **evolutionary**. Les stratégies sont sélectionnées par contexte, risque et dépendances.
- **B, 3 points :** Une stratégie progressive protège les partenaires. Elle ajoute néanmoins une coexistence inutile au service totalement nouveau et ne distingue pas assez les deux contextes.
- **C, 1 point :** La stratégie greenfield convient aux alertes, mais ignore les interfaces historiques encore indispensables à la compensation.
- **D, 0 point :** Une bascule radicale générale ne respecte pas les six mois de coexistence nécessaires aux partenaires.

## XP36 — L2.5.3

**Barème pédagogique :** A=1, B=0, C=5, D=3.

- **C, 5 points :** La contrainte réglementaire impose une transition contrôlée sans coexistence après la date limite pour le premier composant, alors que les partenaires justifient une migration progressive de l'orchestration.
- **D, 3 points :** La bascule radicale protège le composant réglementé mais expose inutilement les partenaires de l'orchestrateur à une rupture de service.
- **A, 1 point :** Le recours progressif peut convenir à l'orchestration, pas à un ancien composant dont l'exploitation devient interdite.
- **B, 0 point :** Greenfield ne résout ni la date d'arrêt ni les contraintes de synchronisation des partenaires et ne constitue pas un plan de migration.
