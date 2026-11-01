# Practitioner Scenarios — Requirements Management

## S046 — Requirement trop vague

Le sponsor écrit : « la nouvelle plateforme doit être très résiliente ». Les équipes interprètent cette phrase de manière différente.

Le service doit être déployé sur deux sites et supporte les paiements urgents. Le sponsor n'a pas spécifié RTO, RPO, fenêtre d'observation ni comportement en maintenance planifiée. Les SRE proposent plusieurs interprétations contradictoires, avec des coûts sensiblement différents. Le comité de conception doit pouvoir comparer ces options sur des critères mesurables et acceptés par le métier.

Quelle action est la meilleure ?
A. Sélectionner le design haute disponibilité recommandé par l'intégrateur, puis déduire la requirement du niveau de service qu'il garantit.
B. Décomposer et clarifier la requirement en critères vérifiables — disponibilité, RTO/RPO, modes de défaillance, failover, tests — tout en conservant la traçabilité vers le concern initial.
C. Définir un premier seuil quantifié de disponibilité puis compléter les conditions de mesure et la validation par Operations.
D. Déduire des seuils de reprise provisoires du seul SLA du fournisseur, puis les appliquer sans valider leur adéquation avec les besoins des SRE et du Business Owner.
**Scoring : A=0, B=5, C=3, D=1.**

**Justification des quatre niveaux :**

- **B — 5 points :** Décomposer et clarifier la requirement en critères vérifiables — disponibilité, RTO/RPO, modes de défaillance, failover, tests — tout en conservant la traçabilité vers le concern initial. Disponibilité, RTO/RPO, modes de panne et critères de test clarifiés rendent l'exigence vérifiable.
- **C — 3 points :** Définir un premier seuil quantifié de disponibilité puis compléter les conditions de mesure et la validation par Operations. Un premier seuil quantifié est utile, mais mesures et validation Operations restent à formaliser.
- **D — 1 points :** Déduire des seuils de reprise provisoires du seul SLA du fournisseur, puis les appliquer sans valider leur adéquation avec les besoins des SRE et du Business Owner. Un SLA fournisseur ne définit pas les exigences réelles de continuité, notamment les scénarios métier.
- **A — 0 points :** Sélectionner le design haute disponibilité recommandé par l'intégrateur, puis déduire la requirement du niveau de service qu'il garantit. Un design choisi avant clarification du concern produit une exigence dictée par la solution.

**Mapping : Requirements Management — Quality of Requirements.**

**Référence d'étude :** X2202, Practitioner, unité 7 ; TOGAF Standard / Series Guides applicables.

---
## S047 — Requirements contradictoires

Finance exige de réduire fortement les coûts d’infrastructure. Operations exige une redondance maximale sur tous les composants. Les deux requirements sont approuvées séparément mais deviennent incompatibles dans la Target.

Le service concerné représente une part importante du coût du programme. Finance veut une consolidation des ressources ; Operations possède des engagements de reprise sur incident approuvés par les métiers. Le sponsor attend une décision documentée et refuse de supprimer arbitrairement l'une des deux requirements. Les architectes doivent comparer les alternatives et leur effet sur la conformité, les coûts et la capacité de reprise.

Quelle action est la meilleure ?
A. Préparer deux architectures alternatives chiffrées et faire expliciter les risques avant de demander un arbitrage métier, sans conclure encore sur leur traçabilité.
B. Adopter une redondance limitée uniquement aux composants critiques et considérer les deux requirements satisfaites, sans accord formel des owners.
C. Rendre le conflit explicite, analyser trade-offs et impacts, impliquer les stakeholders concernés et obtenir un arbitrage gouverné avec requirements mises à jour.
D. Faire expliciter et documenter les impacts des deux exigences, puis préparer une proposition de compromis pour l'autorité de décision.
**Scoring : A=1, B=0, C=5, D=3.**

**Justification des quatre niveaux :**

- **C — 5 points :** Rendre le conflit explicite, analyser trade-offs et impacts, impliquer les stakeholders concernés et obtenir un arbitrage gouverné avec requirements mises à jour. Les deux exigences incompatibles sont analysées avec leurs owners et font l'objet d'un arbitrage traçable.
- **D — 3 points :** Faire expliciter et documenter les impacts des deux exigences, puis préparer une proposition de compromis pour l'autorité de décision. Une proposition de compromis aide l'autorité de décision, mais le conflit reste à trancher.
- **A — 1 points :** Préparer deux architectures alternatives chiffrées et faire expliciter les risques avant de demander un arbitrage métier, sans conclure encore sur leur traçabilité. Comparer les alternatives en coûts/risques éclaire le débat, sans garantir encore l'arbitrage ni la mise à jour des requirements.
- **B — 0 points :** Adopter une redondance limitée uniquement aux composants critiques et considérer les deux requirements satisfaites, sans accord formel des owners. Une architecture locale dite suffisante ne remplace pas l'accord des owners sur leurs exigences contradictoires.

**Mapping : Requirements Management — Conflicting Requirements.**

**Référence d'étude :** X2202, Practitioner, unité 7 ; TOGAF Standard / Series Guides applicables.

---
## S048 — Requirement sans traçabilité

Une exigence de chiffrement apparaît dans le document Technology, mais personne ne sait quel stakeholder ou quelle obligation l’a créée. Elle n’est reliée ni aux controls sécurité ni aux décisions de Phase A.

La demande est apparue après une revue de sécurité externe mais ne cite ni l'obligation précise ni le risque couvert. Le Product Owner suppose qu'elle ne concerne que les APIs publiques, alors que les équipes d'intégration envisagent aussi les flux batch. Le Board souhaite une preuve que les contrôles réalisés couvrent réellement les exigences métier et réglementaires, sans imposer un chiffrement inutile partout.

Quelle action est la meilleure ?
A. Rattacher l'exigence au composant principal et à un critère de vérification, puis étendre ensuite la traçabilité aux autres dépendances.
B. Rattacher l'exigence à une obligation ou un stakeholder identifiable et demander une revue rapide de ses périmètres, puis compléter la traçabilité technique.
C. Retenir l'interprétation la plus large et imposer le même contrôle à tous les flux, en laissant les exceptions se négocier pendant l'implémentation.
D. Restaurer la traçabilité vers source/concern, analyser où la requirement s’applique et relier les artifacts et building blocks concernés.
**Scoring : A=3, B=1, C=0, D=5.**

**Justification des quatre niveaux :**

- **D — 5 points :** Restaurer la traçabilité vers source/concern, analyser où la requirement s’applique et relier les artifacts et building blocks concernés. La relation requirement→building blocks permet de calculer les impacts.
- **A — 3 points :** Rattacher l'exigence au composant principal et à un critère de vérification, puis étendre ensuite la traçabilité aux autres dépendances. Une liaison à l'application est utile, mais laisse les données hors traçabilité.
- **B — 1 point :** Rattacher l'exigence à une obligation ou un stakeholder identifiable et demander une revue rapide de ses périmètres, puis compléter la traçabilité technique. Un identifiant de ticket ne prouve pas que la requirement est satisfaite.
- **C — 0 point :** Retenir l'interprétation la plus large et imposer le même contrôle à tous les flux, en laissant les exceptions se négocier pendant l'implémentation. Une requirement sans lien reste impossible à vérifier après évolution.

**Mapping : Requirements Management — Traceability.**

**Référence d'étude :** X2202, Practitioner, unité 7 ; TOGAF Standard / Series Guides applicables.

---
## S049 — Nouvelle requirement en Phase F

Pendant Migration Planning, un régulateur impose un nouveau contrôle sur les données. La requirement affecte Data Architecture et le séquencement des work packages.

Cette contrainte modifie le cycle de vie d'informations de paiement et les dépendances entre deux releases. Le plan de migration est presque approuvé ; les équipes Data veulent recalculer les volumes et les délais de reprise. Finance demande le chiffrage des impacts tandis que le sponsor souhaite préserver au maximum la valeur prévue. L'architecte doit intégrer la nouvelle requirement sans masquer les conséquences de la modification.

Quelle action est la meilleure ?
A. Enregistrer et analyser la nouvelle requirement, itérer sur les architectures impactées si nécessaire, puis mettre à jour gaps, work packages et Migration Plan.
B. Ouvrir une évaluation d'impact de la nouvelle requirement sur le planning de migration avant de décider des ajustements du plan approuvé.
C. Évaluer prioritairement le gap Data et ses conséquences sur le lot immédiat, puis inscrire les impacts des autres work packages à une revue suivante.
D. Conserver le plan approuvé et demander à l'équipe technique de satisfaire la règle réglementaire par configuration locale, sans revoir les dépendances.
**Scoring : A=5, B=3, C=1, D=0.**

**Justification des quatre niveaux :**

- **A — 5 points :** Enregistrer et analyser la nouvelle requirement, itérer sur les architectures impactées si nécessaire, puis mettre à jour gaps, work packages et Migration Plan. Le changement réglementaire se propage aux domaines, gaps et lots avant de réviser le plan de migration.
- **B — 3 points :** Ouvrir une évaluation d'impact de la nouvelle requirement sur le planning de migration avant de décider des ajustements du plan approuvé. La première analyse de planning est utile, mais ne couvre pas encore les modèles et exigences de tous les domaines.
- **C — 1 points :** Évaluer prioritairement le gap Data et ses conséquences sur le lot immédiat, puis inscrire les impacts des autres work packages à une revue suivante. Se concentrer sur Data et le lot immédiat reporte les autres dépendances potentiellement bloquantes.
- **D — 0 points :** Conserver le plan approuvé et demander à l'équipe technique de satisfaire la règle réglementaire par configuration locale, sans revoir les dépendances. Une correction de configuration locale ne garantit ni conformité ni cohérence du plan approuvé.

**Mapping : Requirements Management — Change during ADM / Iteration.**

**Référence d'étude :** X2202, Practitioner, unité 7 ; TOGAF Standard / Series Guides applicables.

---
## S050 — Requirement devenue obsolète

Une requirement interdisait le cloud à cause d’une politique interne. La politique vient d’être remplacée et le sponsor veut conserver l’exigence « parce qu’elle a déjà été approuvée ».

La nouvelle politique autorise désormais certaines charges dans un cloud qualifié mais conserve des obligations spécifiques aux données sensibles. Le CTO veut éliminer les contraintes anciennes, alors que le Risk Officer demande une analyse différenciée selon les usages. Un changement non maîtrisé pourrait conduire à sélectionner une technologie qui reste interdite sur certains domaines. Le programme doit préserver les raisons et versions des décisions.

Quelle action est la meilleure ?
A. Supprimer sans analyse toutes les contraintes liées au cloud, car le document de politique précédent a été abrogé.
B. Réévaluer la requirement, sa source et sa validité ; la modifier ou la retirer de manière gouvernée et tracer la décision.
C. Soumettre la requirement à une nouvelle validation avec son sponsor et conserver l'historique des versions avant de la retirer ou de la modifier.
D. Enregistrer une demande de modification avec justification de politique et lancer une revue ciblée de conformité avant de modifier toutes les views.
**Scoring : A=0, B=5, C=3, D=1.**

**Justification des quatre niveaux :**

- **B — 5 points :** Réévaluer la requirement, sa source et sa validité ; la modifier ou la retirer de manière gouvernée et tracer la décision. Les exigences obsolètes demandent une décision et un historique gouvernés.
- **C — 3 points :** Soumettre la requirement à une nouvelle validation avec son sponsor et conserver l'historique des versions avant de la retirer ou de la modifier. Un statut local aide mais n'actualise pas les autres livrables.
- **D — 1 point :** Enregistrer une demande de modification avec justification de politique et lancer une revue ciblée de conformité avant de modifier toutes les views. Conserver toutes les exigences actives crée des contradictions.
- **A — 0 point :** Supprimer sans analyse toutes les contraintes liées au cloud, car le document de politique précédent a été abrogé. Une suppression sans traçabilité détruit la justification antérieure.

**Mapping : Requirements Management — Requirement Lifecycle.**

**Référence d'étude :** X2202, Practitioner, unité 7 ; TOGAF Standard / Series Guides applicables.

---
## S051 — Principle ou requirement ?

MayaBank possède le principe « Security by Design ». Pour une plateforme spécifique, le CISO exige que tous les secrets soient stockés dans un service approuvé et renouvelés automatiquement.

La plateforme manipule des certificats, jetons et secrets qui transitent entre trois équipes. Le CISO exige un renouvellement mesurable, mais le sponsor estime que le principe général Security by Design couvre déjà le sujet. Le Board doit distinguer les règles directrices de la spécification vérifiable requise pour tester les implémentations et attribuer les responsabilités.

Quelle distinction est la meilleure ?
A. Rédiger une requirement mesurable pour le renouvellement des secrets tout en réservant la formalisation des implications du principe à la revue suivante.
B. Créer un nouveau principe d'architecture reprenant mot pour mot le choix du service de secrets et le traiter comme standard permanent de l'entreprise.
C. Le principe guide durablement les décisions ; la règle précise de gestion des secrets est une requirement/standard applicable au contexte et doit être tracée comme telle.
D. Conserver le principe comme règle de décision et rédiger une exigence mesurable dérivée, sans encore expliciter toutes les implications.
**Scoring : A=1, B=0, C=5, D=3.**

**Justification des quatre niveaux :**

- **C — 5 points :** Le principe guide durablement les décisions ; la règle précise de gestion des secrets est une requirement/standard applicable au contexte et doit être tracée comme telle. Principe durable et requirement testable restent deux catégories distinctes.
- **D — 3 points :** Conserver le principe comme règle de décision et rédiger une exigence mesurable dérivée, sans encore expliciter toutes les implications. Dériver une requirement est utile mais les implications restent à tracer.
- **A — 1 point :** Rédiger une requirement mesurable pour le renouvellement des secrets tout en réservant la formalisation des implications du principe à la revue suivante. Un standard local ne remplace pas le principe transversal.
- **B — 0 point :** Créer un nouveau principe d'architecture reprenant mot pour mot le choix du service de secrets et le traiter comme standard permanent de l'entreprise. Confondre les deux niveaux fausse les exigences applicables.

**Mapping : Requirements Management — Principle vs Requirement.**

**Référence d'étude :** X2202, Practitioner, unité 7 ; TOGAF Standard / Series Guides applicables.

---
## S052 — Beaucoup de requirements, aucune priorité

Le programme possède 250 requirements toutes marquées « critique ». Les équipes ne peuvent pas arbitrer ni savoir lesquelles conditionnent la réussite de la transformation.

Le portefeuille comporte des contraintes réglementaires, des améliorations de parcours client et des optimisations de coûts. Toutes les équipes revendiquent une livraison prioritaire, sans lien visible avec les dépendances de migration. Le sponsor réclame une première vague réaliste et les responsables métier craignent que la technique ne fixe seule les priorités. Une méthode de classement transparente doit être validée.

Quelle action est la meilleure ?
A. Prioriser d'abord les exigences réglementaires et de sécurité, puis compléter l'arbitrage avec valeur, risques et dépendances.
B. Traiter les demandes dans leur ordre d'arrivée, en donnant une priorité par défaut aux mentions de sécurité, puis remettre les arbitrages de valeur et de dépendance après le cadrage de livraison.
C. Distribuer le budget également entre les squads afin qu'aucune requirement qualifiée critique ne soit exclue de la première vague.
D. Revoir la qualité, source, priorité, dépendances et critères d’acceptation des requirements avec les stakeholders, puis maintenir une gouvernance de changement.
**Scoring : A=3, B=1, C=0, D=5.**

**Justification des quatre niveaux :**

- **D — 5 points :** Revoir la qualité, source, priorité, dépendances et critères d’acceptation des requirements avec les stakeholders, puis maintenir une gouvernance de changement. La qualité, la source et la traçabilité des exigences permettent une priorité fondée sur objectifs et dépendances.
- **A — 3 points :** Prioriser d'abord les exigences réglementaires et de sécurité, puis compléter l'arbitrage avec valeur, risques et dépendances. Les obligations critiques sont repérées, mais la valeur et les interdépendances ne sont pas encore analysées.
- **B — 1 points :** Traiter les demandes dans leur ordre d'arrivée, en donnant une priorité par défaut aux mentions de sécurité, puis remettre les arbitrages de valeur et de dépendance après le cadrage de livraison. L'ordre d'arrivée et un libellé de sécurité ne suffisent pas à qualifier les impacts et la priorité.
- **C — 0 points :** Distribuer le budget également entre les squads afin qu'aucune requirement qualifiée critique ne soit exclue de la première vague. Un budget également distribué ignore la criticité et les dépendances.

**Mapping : Requirements Management — Prioritization / Governance.**

**Référence d'étude :** X2202, Practitioner, unité 7 ; TOGAF Standard / Series Guides applicables.

---
