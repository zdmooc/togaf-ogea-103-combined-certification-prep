# Practitioner Scenarios — Context for Enterprise Architecture

## S001 — Une cible sans capacité d’architecture

MayaBank possède déjà plusieurs diagrammes de cible pour moderniser les paiements. Pourtant, chaque domaine applique ses propres règles, les décisions ne sont pas tracées et aucune instance n’arbitre les exceptions. Le sponsor demande de « finaliser Phase D » rapidement.

Quelle est la meilleure action ?
A. Revenir sur la capacité d’architecture : gouvernance, rôles, principes, repository et tailoring avant de poursuivre le cycle.
B. Obtenir rapidement un accord provisoire du sponsor sur les principes de décision, puis planifier la formalisation de la capacité d'architecture avant les choix irréversibles.
C. Finaliser immédiatement la Technology Architecture à partir des diagrammes existants.
D. Lancer Phase E afin de transformer les diagrammes en work packages.
**Scoring : A=5, B=3, C=1, D=0.**

**Justification révisée :** le choix A (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix B (3 points) constitue une étape utile, mais partielle : obtenir rapidement un accord provisoire du sponsor sur les principes de décision, puis planifier la formalisation de la capacité d'architecture avant les choix irréversibles. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Context for Enterprise Architecture — Architecture Capability / Preliminary.**

---

## S002 — Acquisition d’une filiale

Une banque acquiert une fintech. Les deux organisations disposent de pratiques d’architecture matures mais différentes : l’une centralisée, l’autre très distribuée. La direction veut imposer immédiatement la méthode de la banque à toutes les équipes de la fintech.

Quelle approche est la plus appropriée ?
A. Commencer directement la modélisation applicative commune en Phase C.
B. Évaluer les deux capacités d’architecture, déterminer les responsabilités et adapter/fédérer les pratiques avant de lancer les transformations communes.
C. Définir d'abord quelques principes communs et un mécanisme d'arbitrage, tout en reportant l'évaluation détaillée des capacités locales.
D. Laisser chaque organisation travailler totalement séparément et ne définir aucune gouvernance commune.
**Scoring : A=0, B=5, C=3, D=1.**

**Justification révisée :** le choix B (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix C (3 points) constitue une étape utile, mais partielle : définir d'abord quelques principes communs et un mécanisme d'arbitrage, tout en reportant l'évaluation détaillée des capacités locales. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Context — Tailoring, Federation, Architecture Capability.**

---

## S003 — « À quoi sert l’architecture ? »

Le comité exécutif considère l’Enterprise Architecture comme une activité documentaire coûteuse. Les architectes répondent en présentant 120 diagrammes techniques. Le comité reste sceptique.

Quelle action créerait le plus de valeur ?
A. Produire encore plus de modèles pour démontrer la profondeur du travail.
B. Supprimer toute gouvernance afin d’accélérer les projets.
C. Relier explicitement l’architecture aux business drivers, décisions, risques, capacités, coûts et trajectoires de transformation.
D. Sélectionner un petit portefeuille de décisions d'architecture et montrer leurs impacts mesurables, sans encore relier systématiquement le travail à la stratégie.
**Scoring : A=1, B=0, C=5, D=3.**

**Justification révisée :** le choix C (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix D (3 points) constitue une étape utile, mais partielle : sélectionner un petit portefeuille de décisions d'architecture et montrer leurs impacts mesurables, sans encore relier systématiquement le travail à la stratégie. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Context — Value of Enterprise Architecture.**

---

## S004 — TOGAF et équipes Agile

MayaBank organise ses produits en équipes Agile autonomes avec livraison toutes les deux semaines. Un architecte affirme que l’ADM impose d’attendre la fin complète de B, C et D avant toute livraison.

Quelle réponse est la plus appropriée ?
A. Conserver des décisions autonomes dans les squads tout en instituant des revues légères sur les interfaces et les risques transverses.
B. Abandonner TOGAF car il est incompatible avec Agile.
C. Confirmer : l’ADM doit toujours être exécuté comme un waterfall strict.
D. Tailorer l’ADM, travailler par itérations et maintenir une gouvernance/traçabilité proportionnée tout en soutenant le delivery incrémental.
**Scoring : A=3, B=1, C=0, D=5.**

**Justification révisée :** le choix D (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix A (3 points) constitue une étape utile, mais partielle : conserver des décisions autonomes dans les squads tout en instituant des revues légères sur les interfaces et les risques transverses. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Context — Tailoring, Iteration, Agile.**

---

## S005 — Réutiliser avant de redéfinir

Une équipe doit définir une nouvelle architecture d’intégration. Le Repository contient déjà des standards, patterns et architectures de référence validés. L’équipe souhaite repartir de zéro « pour être indépendante ».

Quelle action est la meilleure ?
A. Rechercher et évaluer les assets réutilisables dans le Repository avant de définir ce qui doit réellement être nouveau.
B. Réutiliser les patterns déjà approuvés après une vérification technique limitée, sans revoir complètement leurs hypothèses métier.
C. Ignorer le Repository et concevoir une architecture totalement nouvelle.
D. Attendre Phase G avant de consulter les standards.
**Scoring : A=5, B=3, C=1, D=0.**

**Justification révisée :** le choix A (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix B (3 points) constitue une étape utile, mais partielle : réutiliser les patterns déjà approuvés après une vérification technique limitée, sans revoir complètement leurs hypothèses métier. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Context — Architecture Repository / Reuse.**

---

## S006 — Risque et sécurité

Une architecture cible a été conçue sans participation du CISO. En fin de Phase D, une analyse révèle des exigences réglementaires fortes sur identité, chiffrement et audit. Le programme propose de « traiter la sécurité pendant Phase G ».

Quelle action est la plus appropriée ?
A. Continuer jusqu’à Phase H puis corriger après mise en production.
B. Réintégrer sécurité et risque dans le travail d’architecture, réévaluer les requirements et itérer sur les domaines impactés avant de poursuivre la migration.
C. Réexaminer les principaux risques de sécurité à la revue de conception suivante et ajuster la cible si nécessaire, sans intégrer encore les exigences de bout en bout.
D. Demander une exception permanente au CISO.
**Scoring : A=0, B=5, C=3, D=1.**

**Justification révisée :** le choix B (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix C (3 points) constitue une étape utile, mais partielle : réexaminer les principaux risques de sécurité à la revue de conception suivante et ajuster la cible si nécessaire, sans intégrer encore les exigences de bout en bout. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Context — Integrating Risk and Security / Iteration.**

---

## S007 — Le fournisseur avant le problème

Un fournisseur présente une plateforme « idéale » de paiement temps réel. La direction demande à l’équipe d’architecture de produire immédiatement l’architecture cible autour de ce produit. Les business drivers, stakeholders et scope ne sont pas encore stabilisés.

Quelle est la meilleure réponse ?
A. Acheter le produit puis adapter les requirements à ses capacités.
B. Passer directement à Phase F pour planifier son déploiement.
C. Utiliser la proposition comme information potentielle, mais d’abord clarifier drivers, stakeholders, scope, value et requirements avant de confirmer une solution.
D. Comparer le produit proposé avec une architecture de référence après une première clarification des besoins, sans élargir immédiatement l'analyse aux autres options.
**Scoring : A=1, B=0, C=5, D=3.**

**Justification révisée :** le choix C (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix D (3 points) constitue une étape utile, mais partielle : comparer le produit proposé avec une architecture de référence après une première clarification des besoins, sans élargir immédiatement l'analyse aux autres options. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Context — Architecture in Context / Business Drivers / Solution Bias.**

---

Ces scénarios sont des exercices pédagogiques originaux et ne reproduisent aucun item officiel.