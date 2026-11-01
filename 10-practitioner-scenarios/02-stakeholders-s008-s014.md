# Practitioner Scenarios — Stakeholder Management

## S008 — Operations découvre la cible trop tard

Le sponsor et l’équipe projet ont approuvé une cible de paiement. Lors d’une revue tardive, Operations refuse le modèle car il n’existe ni run model clair, ni stratégie de support, ni exigences de bascule exploitables.

Quelle action est la meilleure ?
A. Consulter Operations et consigner ses principales contraintes d'exploitation pour la prochaine revue d'architecture, sans réviser immédiatement toutes les décisions.
B. Rappeler que le sponsor a déjà approuvé l’architecture et poursuivre.
C. Demander à l’équipe delivery de résoudre seule le problème après mise en production.
D. Reconnaître Operations comme stakeholder critique, comprendre ses concerns, produire les vues nécessaires et intégrer les requirements opérationnels dans l’architecture.
**Scoring : A=3, B=1, C=0, D=5.**

**Justification révisée :** le choix D (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix A (3 points) constitue une étape utile, mais partielle : consulter Operations et consigner ses principales contraintes d'exploitation pour la prochaine revue d'architecture, sans réviser immédiatement toutes les décisions. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Stakeholder Management — Concerns, Views, Requirements.**

---

## S009 — Sponsor contre CISO

Le sponsor veut une mise en production en trois mois. Le CISO exige des contrôles qui peuvent ajouter plusieurs semaines. Les deux parties considèrent leur priorité comme non négociable.

Quelle approche est la plus appropriée ?
A. Clarifier les concerns, contraintes et requirements, rendre visibles les impacts et arbitrages, puis utiliser la gouvernance appropriée pour obtenir une décision traçable.
B. Appliquer provisoirement les contrôles de sécurité prioritaires du CISO et faire arbitrer les impacts métier restants.
C. Choisir automatiquement la préférence du sponsor car il finance le programme.
D. Demander au delivery de décider discrètement pendant l’implémentation.
**Scoring : A=5, B=3, C=1, D=0.**

**Justification révisée :** le choix A (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix B (3 points) constitue une étape utile, mais partielle : appliquer provisoirement les contrôles de sécurité prioritaires du CISO et faire arbitrer les impacts métier restants. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Stakeholder Management — Conflicting Concerns / Governance.**

---

## S010 — Carte de stakeholders devenue obsolète

Pendant Phase C, MayaBank fusionne deux directions opérationnelles. De nouveaux responsables apparaissent et les responsabilités sur la donnée changent. L’équipe souhaite garder la stakeholder map de Phase A pour « ne pas rouvrir le cadrage ».

Quelle action est la meilleure ?
A. Ignorer l’organisation et se concentrer uniquement sur l’Application Architecture.
B. Mettre à jour la stakeholder map, les concerns et les plans d’engagement, puis vérifier l’impact sur requirements et vues.
C. Mettre à jour les stakeholders les plus influents et leurs préoccupations, sans refaire encore la cartographie complète des dépendances.
D. Conserver la carte initiale jusqu’à Phase H.
**Scoring : A=0, B=5, C=3, D=1.**

**Justification révisée :** le choix B (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix C (3 points) constitue une étape utile, mais partielle : mettre à jour les stakeholders les plus influents et leurs préoccupations, sans refaire encore la cartographie complète des dépendances. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Stakeholder Management — Continuous Engagement.**

---

## S011 — Un diagramme pour tout le monde

L’architecte prépare un diagramme technique de 80 composants et veut l’utiliser pour le comité exécutif, le CISO, les équipes métier et les SRE.

Quelle approche est la meilleure ?
A. Présenter la vue technique uniquement au sponsor afin qu’il la redistribue.
B. Supprimer toute modélisation et envoyer uniquement du texte.
C. Produire des views adaptées aux concerns des stakeholders, construites à partir d’une base architecturale cohérente.
D. Conserver un modèle d'architecture partagé, mais préparer des explications distinctes pour les principaux groupes de stakeholders.
**Scoring : A=1, B=0, C=5, D=3.**

**Justification révisée :** le choix C (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix D (3 points) constitue une étape utile, mais partielle : conserver un modèle d'architecture partagé, mais préparer des explications distinctes pour les principaux groupes de stakeholders. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Stakeholder Management — Viewpoints and Views.**

---

## S012 — Forte influence, faible intérêt

Un directeur infrastructure a un fort pouvoir d’arbitrage mais peu d’intérêt quotidien pour la transformation. L’équipe lui envoie chaque jour tous les détails de conception, ce qui provoque une perte d’attention.

Quelle action est la meilleure ?
A. Prévoir une synthèse décisionnelle périodique pour cet acteur et garder les détails accessibles à la demande, sans cartographier tous ses concerns.
B. Le traiter comme un membre à temps plein de l’équipe projet.
C. L’exclure totalement car son intérêt est faible.
D. Maintenir le stakeholder satisfait avec une communication ciblée sur décisions, risques et impacts, sans le surcharger.
**Scoring : A=3, B=1, C=0, D=5.**

**Justification révisée :** le choix D (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix A (3 points) constitue une étape utile, mais partielle : prévoir une synthèse décisionnelle périodique pour cet acteur et garder les détails accessibles à la demande, sans cartographier tous ses concerns. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Stakeholder Management — Influence / Interest.**

---

## S013 — Du concern à la requirement

Le responsable Operations dit : « je ne veux plus passer mes nuits à gérer des bascules manuelles ». L’équipe copie cette phrase telle quelle dans l’Architecture Requirements Specification.

Quelle action est la meilleure ?
A. Transformer le concern en requirements vérifiables sur failover, automatisation, RTO/RPO, observabilité et tests, tout en gardant la traçabilité vers le stakeholder.
B. Traduire l'inquiétude en une cible indicative de disponibilité puis confirmer ultérieurement ses seuils, ses conditions de mesure et son propriétaire.
C. Choisir immédiatement un produit de haute disponibilité.
D. Ignorer ce concern car il n’est pas formulé techniquement.
**Scoring : A=5, B=3, C=1, D=0.**

**Justification révisée :** le choix A (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix B (3 points) constitue une étape utile, mais partielle : traduire l'inquiétude en une cible indicative de disponibilité puis confirmer ultérieurement ses seuils, ses conditions de mesure et son propriétaire. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Stakeholder Management — Concern → Requirement.**

---

## S014 — Architecture Board et acceptation métier

L’Architecture Board valide une cible. Les responsables métier clés déclarent ensuite qu’elle ne répond pas à leur processus critique. Un architecte affirme que la validation du Board rend leur avis inutile.

Quelle est la meilleure réponse ?
A. Dissoudre l’Architecture Board.
B. Le Board est un mécanisme de gouvernance, mais il faut revoir les concerns métier non satisfaits, vérifier requirements et vues, puis soumettre les ajustements à la gouvernance appropriée.
C. Obtenir la validation de conformité du Board et organiser ensuite l'acceptation métier formelle, sans l'intégrer au même cycle de décision.
D. Demander au métier de s’adapter à la cible sans analyse.
**Scoring : A=0, B=5, C=3, D=1.**

**Justification révisée :** le choix B (5 points) couvre la décision structurante et son bon niveau de gouvernance. Le choix C (3 points) constitue une étape utile, mais partielle : obtenir la validation de conformité du Board et organiser ensuite l'acceptation métier formelle, sans l'intégrer au même cycle de décision. Il laisse donc un travail de cadrage, de validation ou de traçabilité avant de pouvoir conclure. Les deux autres options ont une portée plus faible ou ignorent une contrainte centrale. Ce classement est pédagogique et doit être confronté au référentiel officiel.

**Mapping : Stakeholder Management — Governance and Stakeholder Acceptance.**

---

Contenu pédagogique original ; aucun scénario officiel n’est reproduit.