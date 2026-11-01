# Practitioner Scenarios — Context for Enterprise Architecture

## S001 — Une cible sans capacité d’architecture

MayaBank possède déjà plusieurs diagrammes de cible pour moderniser les paiements. Pourtant, chaque domaine applique ses propres règles, les décisions ne sont pas tracées et aucune instance n’arbitre les exceptions. Le sponsor demande de « finaliser Phase D » rapidement.

Le programme touche trois directions aux standards contradictoires et une date d'entrée en service réglementaire approche. L'équipe sécurité refuse d'engager la conformité sans autorité de décision, alors que le directeur de programme veut capitaliser les travaux déjà produits. Le comité attend une démarche praticable, sans reconstruire inutilement les modèles existants.

Quelle est la meilleure action ?
A. Revenir sur la capacité d’architecture : gouvernance, rôles, principes, repository et tailoring avant de poursuivre le cycle.
B. Obtenir rapidement un accord provisoire du sponsor sur les principes de décision, puis planifier la formalisation de la capacité d'architecture avant les choix irréversibles.
C. Organiser une revue des principes et consigner les décisions les plus urgentes dans un registre commun, sans clarifier les rôles de validation.
D. Préparer seulement un planning des work packages afin de donner une visibilité au sponsor, puis programmer un atelier de gouvernance après la prochaine livraison.
**Scoring : A=5, B=3, C=1, D=0.**

**Justification des quatre niveaux :**

- **A — 5 points :** Revenir sur la capacité d’architecture : gouvernance, rôles, principes, repository et tailoring avant de poursuivre le cycle. Répond aux enjeux structurants, à leur séquencement et aux responsabilités de décision.
- **B — 3 points :** Obtenir rapidement un accord provisoire du sponsor sur les principes de décision, puis planifier la formalisation de la capacité d'architecture avant les choix irréversibles. Action pertinente mais incomplète, qui reporte une partie du cadrage, de la traçabilité ou de l'arbitrage.
- **C — 1 point :** Organiser une revue des principes et consigner les décisions les plus urgentes dans un registre commun, sans clarifier les rôles de validation. Peut contribuer ponctuellement, mais ne traite pas la principale dépendance ou ne sécurise pas la décision.
- **D — 0 point :** Préparer seulement un planning des work packages afin de donner une visibilité au sponsor, puis programmer un atelier de gouvernance après la prochaine livraison. Peut avoir un intérêt dans un autre contexte, mais ici repousse ou contourne le problème central.

**Mapping : Context for Enterprise Architecture — Architecture Capability / Preliminary.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 1 ; TOGAF Standard, ADM et Series Guides applicables.

---
## S002 — Acquisition d’une filiale

Une banque acquiert une fintech. Les deux organisations disposent de pratiques d’architecture matures mais différentes : l’une centralisée, l’autre très distribuée. La direction veut imposer immédiatement la méthode de la banque à toutes les équipes de la fintech.

La fintech dispose de produits agiles et d'une gouvernance locale efficace ; la banque a une obligation d'audit de groupe. Un chantier d'identité commun doit démarrer dans deux mois. Les responsables des deux structures souhaitent préserver leurs décisions quotidiennes, mais le CISO demande un cadre vérifiable pour les exceptions et la réutilisation.

Quelle approche est la plus appropriée ?
A. Établir immédiatement une Architecture Vision commune et reporter la comparaison des capacités d'architecture à l'après-intégration.
B. Évaluer les deux capacités d’architecture, déterminer les responsabilités et adapter/fédérer les pratiques avant de lancer les transformations communes.
C. Définir d'abord quelques principes communs et un mécanisme d'arbitrage, tout en reportant l'évaluation détaillée des capacités locales.
D. Conserver temporairement les deux approches locales avec un contrôle de conformité central sur les seules interfaces critiques.
**Scoring : A=0, B=5, C=3, D=1.**

**Justification des quatre niveaux :**

- **B — 5 points :** Évaluer les deux capacités d’architecture, déterminer les responsabilités et adapter/fédérer les pratiques avant de lancer les transformations communes. Répond aux enjeux structurants, à leur séquencement et aux responsabilités de décision.
- **C — 3 points :** Définir d'abord quelques principes communs et un mécanisme d'arbitrage, tout en reportant l'évaluation détaillée des capacités locales. Action pertinente mais incomplète, qui reporte une partie du cadrage, de la traçabilité ou de l'arbitrage.
- **D — 1 point :** Conserver temporairement les deux approches locales avec un contrôle de conformité central sur les seules interfaces critiques. Peut contribuer ponctuellement, mais ne traite pas la principale dépendance ou ne sécurise pas la décision.
- **A — 0 point :** Établir immédiatement une Architecture Vision commune et reporter la comparaison des capacités d'architecture à l'après-intégration. Peut avoir un intérêt dans un autre contexte, mais ici repousse ou contourne le problème central.

**Mapping : Context — Tailoring, Federation, Architecture Capability.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 1 ; TOGAF Standard, ADM et Series Guides applicables.

---
## S003 — « À quoi sert l’architecture ? »

Le comité exécutif considère l’Enterprise Architecture comme une activité documentaire coûteuse. Les architectes répondent en présentant 120 diagrammes techniques. Le comité reste sceptique.

Un nouveau service de paiement doit pourtant être arbitré entre plusieurs produits, avec des coûts, risques et interdépendances significatifs. Finance demande la valeur créée, Operations veut comprendre les implications d'exploitation et le comité ne souhaite plus de présentations purement techniques. Il faut démontrer une contribution mesurable au changement plutôt qu'une accumulation documentaire.

Quelle action créerait le plus de valeur ?
A. Présenter un tableau des économies technologiques attendues, mais sans montrer les effets sur les capacités et résultats métier.
B. Proposer un exercice de conformité technique sur l'application principale, puis traiter l'alignement stratégique après la décision d'investissement.
C. Relier explicitement l’architecture aux business drivers, décisions, risques, capacités, coûts et trajectoires de transformation.
D. Sélectionner un petit portefeuille de décisions d'architecture et montrer leurs impacts mesurables, sans encore relier systématiquement le travail à la stratégie.
**Scoring : A=1, B=0, C=5, D=3.**

**Justification des quatre niveaux :**

- **C — 5 points :** Relier explicitement l’architecture aux business drivers, décisions, risques, capacités, coûts et trajectoires de transformation. Répond aux enjeux structurants, à leur séquencement et aux responsabilités de décision.
- **D — 3 points :** Sélectionner un petit portefeuille de décisions d'architecture et montrer leurs impacts mesurables, sans encore relier systématiquement le travail à la stratégie. Action pertinente mais incomplète, qui reporte une partie du cadrage, de la traçabilité ou de l'arbitrage.
- **A — 1 point :** Présenter un tableau des économies technologiques attendues, mais sans montrer les effets sur les capacités et résultats métier. Peut contribuer ponctuellement, mais ne traite pas la principale dépendance ou ne sécurise pas la décision.
- **B — 0 point :** Proposer un exercice de conformité technique sur l'application principale, puis traiter l'alignement stratégique après la décision d'investissement. Peut avoir un intérêt dans un autre contexte, mais ici repousse ou contourne le problème central.

**Mapping : Context — Value of Enterprise Architecture.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 1 ; TOGAF Standard, ADM et Series Guides applicables.

---
## S004 — TOGAF et équipes Agile

MayaBank organise ses produits en équipes Agile autonomes avec livraison toutes les deux semaines. Un architecte affirme que l’ADM impose d’attendre la fin complète de B, C et D avant toute livraison.

Le groupe conserve des standards de sécurité transverses et un service d'identité partagé. Deux squads préparent des fonctionnalités liées qui dépendent du même modèle de données ; la feuille de route exige une mise en production partielle dès le mois prochain. Le Board veut une architecture évolutive, mais les équipes refusent un processus de validation bloquant chaque sprint.

Quelle réponse est la plus appropriée ?
A. Conserver des décisions autonomes dans les squads tout en instituant des revues légères sur les interfaces et les risques transverses.
B. Définir des points de synchronisation seulement pour les API communes, puis compléter les vues métier et de données après les releases pilotes.
C. Accepter le rythme de livraison autonome et réserver une revue ADM complète à la fin du trimestre, avant d'intégrer les produits.
D. Tailorer l’ADM, travailler par itérations et maintenir une gouvernance/traçabilité proportionnée tout en soutenant le delivery incrémental.
**Scoring : A=3, B=1, C=0, D=5.**

**Justification des quatre niveaux :**

- **D — 5 points :** Tailorer l’ADM, travailler par itérations et maintenir une gouvernance/traçabilité proportionnée tout en soutenant le delivery incrémental. Répond aux enjeux structurants, à leur séquencement et aux responsabilités de décision.
- **A — 3 points :** Conserver des décisions autonomes dans les squads tout en instituant des revues légères sur les interfaces et les risques transverses. Action pertinente mais incomplète, qui reporte une partie du cadrage, de la traçabilité ou de l'arbitrage.
- **B — 1 point :** Définir des points de synchronisation seulement pour les API communes, puis compléter les vues métier et de données après les releases pilotes. Peut contribuer ponctuellement, mais ne traite pas la principale dépendance ou ne sécurise pas la décision.
- **C — 0 point :** Accepter le rythme de livraison autonome et réserver une revue ADM complète à la fin du trimestre, avant d'intégrer les produits. Peut avoir un intérêt dans un autre contexte, mais ici repousse ou contourne le problème central.

**Mapping : Context — Tailoring, Iteration, Agile.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 1 ; TOGAF Standard, ADM et Series Guides applicables.

---
## S005 — Réutiliser avant de redéfinir

Une équipe doit définir une nouvelle architecture d’intégration. Le Repository contient déjà des standards, patterns et architectures de référence validés. L’équipe souhaite repartir de zéro « pour être indépendante ».

La nouvelle plateforme doit cependant gérer une contrainte de localisation des données absente du précédent projet et un trafic nettement plus important. Le sponsor demande des gains rapides de réutilisation. Les responsables Data et Risk exigent une comparaison des hypothèses de l'architecture de référence avec les besoins actuels avant d'approuver les choix de building blocks.

Quelle action est la meilleure ?
A. Rechercher et évaluer les assets réutilisables dans le Repository avant de définir ce qui doit réellement être nouveau.
B. Réutiliser les patterns déjà approuvés après une vérification technique limitée, sans revoir complètement leurs hypothèses métier.
C. Retenir les seuls standards techniques encore supportés et réserver les autres adaptations aux prochaines revues métier.
D. Dupliquer le modèle de solution le plus récent, puis vérifier uniquement la compatibilité des technologies avec l'infrastructure existante.
**Scoring : A=5, B=3, C=1, D=0.**

**Justification des quatre niveaux :**

- **A — 5 points :** Rechercher et évaluer les assets réutilisables dans le Repository avant de définir ce qui doit réellement être nouveau. Répond aux enjeux structurants, à leur séquencement et aux responsabilités de décision.
- **B — 3 points :** Réutiliser les patterns déjà approuvés après une vérification technique limitée, sans revoir complètement leurs hypothèses métier. Action pertinente mais incomplète, qui reporte une partie du cadrage, de la traçabilité ou de l'arbitrage.
- **C — 1 point :** Retenir les seuls standards techniques encore supportés et réserver les autres adaptations aux prochaines revues métier. Peut contribuer ponctuellement, mais ne traite pas la principale dépendance ou ne sécurise pas la décision.
- **D — 0 point :** Dupliquer le modèle de solution le plus récent, puis vérifier uniquement la compatibilité des technologies avec l'infrastructure existante. Peut avoir un intérêt dans un autre contexte, mais ici repousse ou contourne le problème central.

**Mapping : Context — Architecture Repository / Reuse.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 1 ; TOGAF Standard, ADM et Series Guides applicables.

---
## S006 — Risque et sécurité

Une architecture cible a été conçue sans participation du CISO. En fin de Phase D, une analyse révèle des exigences réglementaires fortes sur identité, chiffrement et audit. Le programme propose de « traiter la sécurité pendant Phase G ».

La migration porte sur des données réglementées et une interface interbancaire ouverte à plusieurs partenaires. Le plan de tests doit être approuvé dans quinze jours ; Operations craint une interruption lors du basculement et les équipes applicatives affirment que le chiffrement est déjà assuré par le réseau. Le CISO demande une analyse des risques résiduels et des requirements vérifiables.

Quelle action est la plus appropriée ?
A. Demander une dérogation temporaire sur les seuls mécanismes d'identité, puis inclure les risques restants dans le plan de migration.
B. Réintégrer sécurité et risque dans le travail d’architecture, réévaluer les requirements et itérer sur les domaines impactés avant de poursuivre la migration.
C. Réexaminer les principaux risques de sécurité à la revue de conception suivante et ajuster la cible si nécessaire, sans intégrer encore les exigences de bout en bout.
D. Faire auditer les échanges sensibles et ajouter les contrôles manquants dans les critères de recette, sans reprendre toute la traçabilité B/C/D.
**Scoring : A=0, B=5, C=3, D=1.**

**Justification des quatre niveaux :**

- **B — 5 points :** Réintégrer sécurité et risque dans le travail d’architecture, réévaluer les requirements et itérer sur les domaines impactés avant de poursuivre la migration. Répond aux enjeux structurants, à leur séquencement et aux responsabilités de décision.
- **C — 3 points :** Réexaminer les principaux risques de sécurité à la revue de conception suivante et ajuster la cible si nécessaire, sans intégrer encore les exigences de bout en bout. Action pertinente mais incomplète, qui reporte une partie du cadrage, de la traçabilité ou de l'arbitrage.
- **D — 1 point :** Faire auditer les échanges sensibles et ajouter les contrôles manquants dans les critères de recette, sans reprendre toute la traçabilité B/C/D. Peut contribuer ponctuellement, mais ne traite pas la principale dépendance ou ne sécurise pas la décision.
- **A — 0 point :** Demander une dérogation temporaire sur les seuls mécanismes d'identité, puis inclure les risques restants dans le plan de migration. Peut avoir un intérêt dans un autre contexte, mais ici repousse ou contourne le problème central.

**Mapping : Context — Integrating Risk and Security / Iteration.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 1 ; TOGAF Standard, ADM et Series Guides applicables.

---
## S007 — Le fournisseur avant le problème

Un fournisseur présente une plateforme « idéale » de paiement temps réel. La direction demande à l’équipe d’architecture de produire immédiatement l’architecture cible autour de ce produit. Les business drivers, stakeholders et scope ne sont pas encore stabilisés.

Le vendeur produit une démonstration impressionnante, mais le périmètre inclut des paiements de détail et des transferts corporate aux règles différentes. La direction souhaite signer sous trois semaines. Les métiers demandent des indicateurs de valeur et le CISO alerte sur le contrôle des données. L'architecte doit distinguer l'opportunité commerciale d'une décision d'architecture approuvée.

Quelle est la meilleure réponse ?
A. Conserver le produit comme solution candidate et lancer une comparaison technique, en préparant ensuite la définition des outcomes métier.
B. Établir immédiatement un Architecture Contract avec le fournisseur pour sécuriser les exigences, en laissant le périmètre à préciser durant l'implémentation.
C. Utiliser la proposition comme information potentielle, mais d’abord clarifier drivers, stakeholders, scope, value et requirements avant de confirmer une solution.
D. Comparer le produit proposé avec une architecture de référence après une première clarification des besoins, sans élargir immédiatement l'analyse aux autres options.
**Scoring : A=1, B=0, C=5, D=3.**

**Justification des quatre niveaux :**

- **C — 5 points :** Utiliser la proposition comme information potentielle, mais d’abord clarifier drivers, stakeholders, scope, value et requirements avant de confirmer une solution. Répond aux enjeux structurants, à leur séquencement et aux responsabilités de décision.
- **D — 3 points :** Comparer le produit proposé avec une architecture de référence après une première clarification des besoins, sans élargir immédiatement l'analyse aux autres options. Action pertinente mais incomplète, qui reporte une partie du cadrage, de la traçabilité ou de l'arbitrage.
- **A — 1 point :** Conserver le produit comme solution candidate et lancer une comparaison technique, en préparant ensuite la définition des outcomes métier. Peut contribuer ponctuellement, mais ne traite pas la principale dépendance ou ne sécurise pas la décision.
- **B — 0 point :** Établir immédiatement un Architecture Contract avec le fournisseur pour sécuriser les exigences, en laissant le périmètre à préciser durant l'implémentation. Peut avoir un intérêt dans un autre contexte, mais ici repousse ou contourne le problème central.

**Mapping : Context — Architecture in Context / Business Drivers / Solution Bias.**

**Référence d'étude :** syllabus X2202, Practitioner, unité 1 ; TOGAF Standard, ADM et Series Guides applicables.

---
