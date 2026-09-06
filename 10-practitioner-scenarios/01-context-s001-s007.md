# Practitioner Scenarios — Context for Enterprise Architecture

## S001 — Une cible sans capacité d’architecture

MayaBank possède déjà plusieurs diagrammes de cible pour moderniser les paiements. Pourtant, chaque domaine applique ses propres règles, les décisions ne sont pas tracées et aucune instance n’arbitre les exceptions. Le sponsor demande de « finaliser Phase D » rapidement.

Quelle est la meilleure action ?

A. Finaliser immédiatement la Technology Architecture à partir des diagrammes existants.  
B. Lancer Phase E afin de transformer les diagrammes en work packages.  
C. Revenir sur la capacité d’architecture : gouvernance, rôles, principes, repository et tailoring avant de poursuivre le cycle.  
D. Demander uniquement au sponsor d’approuver les diagrammes existants.

**Scoring : C=5, D=3, A=1, B=0.**

**Pourquoi C est meilleure :** le problème dominant n’est pas encore la qualité de Phase D mais l’absence d’Architecture Capability permettant de produire et gouverner une architecture cohérente. D améliore un peu la gouvernance mais reste trop limité. A poursuit le travail sans corriger la cause ; B est encore plus prématurée.

**Mapping : Context for Enterprise Architecture — Architecture Capability / Preliminary.**

---

## S002 — Acquisition d’une filiale

Une banque acquiert une fintech. Les deux organisations disposent de pratiques d’architecture matures mais différentes : l’une centralisée, l’autre très distribuée. La direction veut imposer immédiatement la méthode de la banque à toutes les équipes de la fintech.

Quelle approche est la plus appropriée ?

A. Évaluer les deux capacités d’architecture, déterminer les responsabilités et adapter/fédérer les pratiques avant de lancer les transformations communes.  
B. Imposer la méthode de la banque sans analyse afin de garantir l’uniformité.  
C. Laisser chaque organisation travailler totalement séparément et ne définir aucune gouvernance commune.  
D. Commencer directement la modélisation applicative commune en Phase C.

**Scoring : A=5, B=3, C=1, D=0.**

**Pourquoi A est meilleure :** TOGAF doit être adapté au contexte. Dans une organisation fédérée, la cohérence ne signifie pas nécessairement uniformité absolue. B peut sembler efficace mais ignore maturité et responsabilités existantes ; C préserve l’autonomie mais pas la cohérence ; D saute le problème organisationnel.

**Mapping : Context — Tailoring, Federation, Architecture Capability.**

---

## S003 — « À quoi sert l’architecture ? »

Le comité exécutif considère l’Enterprise Architecture comme une activité documentaire coûteuse. Les architectes répondent en présentant 120 diagrammes techniques. Le comité reste sceptique.

Quelle action créerait le plus de valeur ?

A. Produire encore plus de modèles pour démontrer la profondeur du travail.  
B. Relier explicitement l’architecture aux business drivers, décisions, risques, capacités, coûts et trajectoires de transformation.  
C. Réduire l’architecture à un contrôle de conformité technique.  
D. Supprimer toute gouvernance afin d’accélérer les projets.

**Scoring : B=5, C=3, A=1, D=0.**

**Pourquoi B est meilleure :** la valeur de l’EA vient de l’alignement et de la qualité des décisions, pas du volume de documentation. C peut produire une valeur limitée mais réduit trop le rôle de l’EA. A traite le symptôme par davantage de documentation ; D détruit un mécanisme essentiel.

**Mapping : Context — Value of Enterprise Architecture.**

---

## S004 — TOGAF et équipes Agile

MayaBank organise ses produits en équipes Agile autonomes avec livraison toutes les deux semaines. Un architecte affirme que l’ADM impose d’attendre la fin complète de B, C et D avant toute livraison.

Quelle réponse est la plus appropriée ?

A. Confirmer : l’ADM doit toujours être exécuté comme un waterfall strict.  
B. Abandonner TOGAF car il est incompatible avec Agile.  
C. Tailorer l’ADM, travailler par itérations et maintenir une gouvernance/traçabilité proportionnée tout en soutenant le delivery incrémental.  
D. Laisser chaque équipe prendre toutes les décisions sans architecture partagée.

**Scoring : C=5, D=3, B=1, A=0.**

**Pourquoi C est meilleure :** l’ADM est tailorable et itératif. D respecte l’autonomie mais sacrifie la cohérence. B oppose artificiellement Agile et TOGAF ; A transforme l’ADM en processus rigide qu’il n’est pas.

**Mapping : Context — Tailoring, Iteration, Agile.**

---

## S005 — Réutiliser avant de redéfinir

Une équipe doit définir une nouvelle architecture d’intégration. Le Repository contient déjà des standards, patterns et architectures de référence validés. L’équipe souhaite repartir de zéro « pour être indépendante ».

Quelle action est la meilleure ?

A. Rechercher et évaluer les assets réutilisables dans le Repository avant de définir ce qui doit réellement être nouveau.  
B. Copier tous les assets existants sans vérifier leur pertinence.  
C. Ignorer le Repository et concevoir une architecture totalement nouvelle.  
D. Attendre Phase G avant de consulter les standards.

**Scoring : A=5, B=3, C=1, D=0.**

**Pourquoi A est meilleure :** réutilisation et contextualisation réduisent duplication et incohérence. B reconnaît la réutilisation mais sans adaptation ; C perd la valeur du patrimoine ; D consulte les standards beaucoup trop tard.

**Mapping : Context — Architecture Repository / Reuse.**

---

## S006 — Risque et sécurité

Une architecture cible a été conçue sans participation du CISO. En fin de Phase D, une analyse révèle des exigences réglementaires fortes sur identité, chiffrement et audit. Le programme propose de « traiter la sécurité pendant Phase G ».

Quelle action est la plus appropriée ?

A. Conserver la cible et ajouter uniquement des contrôles lors du déploiement.  
B. Réintégrer sécurité et risque dans le travail d’architecture, réévaluer les requirements et itérer sur les domaines impactés avant de poursuivre la migration.  
C. Demander une exception permanente au CISO.  
D. Continuer jusqu’à Phase H puis corriger après mise en production.

**Scoring : B=5, A=3, C=1, D=0.**

**Pourquoi B est meilleure :** sécurité et risque sont transverses et doivent influencer les requirements et architectures, pas être ajoutés après coup. A limite le dommage mais reste tardif ; C peut exister comme mécanisme gouverné mais n’est pas une réponse normale à un défaut de conception ; D reporte le risque au mauvais moment.

**Mapping : Context — Integrating Risk and Security / Iteration.**

---

## S007 — Le fournisseur avant le problème

Un fournisseur présente une plateforme « idéale » de paiement temps réel. La direction demande à l’équipe d’architecture de produire immédiatement l’architecture cible autour de ce produit. Les business drivers, stakeholders et scope ne sont pas encore stabilisés.

Quelle est la meilleure réponse ?

A. Acheter le produit puis adapter les requirements à ses capacités.  
B. Utiliser la proposition comme information potentielle, mais d’abord clarifier drivers, stakeholders, scope, value et requirements avant de confirmer une solution.  
C. Rejeter automatiquement tout produit commercial.  
D. Passer directement à Phase F pour planifier son déploiement.

**Scoring : B=5, C=3, A=1, D=0.**

**Pourquoi B est meilleure :** TOGAF ne prohibe pas un produit existant, mais évite que la solution précède la compréhension du problème. C protège de la dépendance fournisseur mais est dogmatique ; A inverse la logique requirement/solution ; D est hors séquence.

**Mapping : Context — Architecture in Context / Business Drivers / Solution Bias.**

---

Ces scénarios sont des exercices pédagogiques originaux et ne reproduisent aucun item officiel.