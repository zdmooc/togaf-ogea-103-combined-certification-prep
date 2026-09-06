# Practitioner Scenarios — Stakeholder Management

## S008 — Operations découvre la cible trop tard

Le sponsor et l’équipe projet ont approuvé une cible de paiement. Lors d’une revue tardive, Operations refuse le modèle car il n’existe ni run model clair, ni stratégie de support, ni exigences de bascule exploitables.

Quelle action est la meilleure ?

A. Rappeler que le sponsor a déjà approuvé l’architecture et poursuivre.  
B. Reconnaître Operations comme stakeholder critique, comprendre ses concerns, produire les vues nécessaires et intégrer les requirements opérationnels dans l’architecture.  
C. Ajouter uniquement une réunion d’information pour Operations sans changer l’architecture.  
D. Demander à l’équipe delivery de résoudre seule le problème après mise en production.

**Scoring : B=5, C=3, A=1, D=0.**

**Pourquoi B :** une approbation du sponsor ne remplace pas l’analyse des stakeholders affectés. C améliore la communication mais pas le contenu ; A ignore un concern majeur ; D reporte le problème hors du travail d’architecture.

**Mapping : Stakeholder Management — Concerns, Views, Requirements.**

---

## S009 — Sponsor contre CISO

Le sponsor veut une mise en production en trois mois. Le CISO exige des contrôles qui peuvent ajouter plusieurs semaines. Les deux parties considèrent leur priorité comme non négociable.

Quelle approche est la plus appropriée ?

A. Choisir automatiquement la préférence du sponsor car il finance le programme.  
B. Choisir automatiquement la préférence du CISO car la sécurité est toujours prioritaire.  
C. Clarifier les concerns, contraintes et requirements, rendre visibles les impacts et arbitrages, puis utiliser la gouvernance appropriée pour obtenir une décision traçable.  
D. Demander au delivery de décider discrètement pendant l’implémentation.

**Scoring : C=5, B=3, A=1, D=0.**

**Pourquoi C :** le rôle de l’architecture est de rendre les conflits explicites et gouvernables. B peut être prudent mais ne traite pas l’arbitrage de manière structurée ; A réduit la gouvernance au pouvoir budgétaire ; D évite la décision.

**Mapping : Stakeholder Management — Conflicting Concerns / Governance.**

---

## S010 — Carte de stakeholders devenue obsolète

Pendant Phase C, MayaBank fusionne deux directions opérationnelles. De nouveaux responsables apparaissent et les responsabilités sur la donnée changent. L’équipe souhaite garder la stakeholder map de Phase A pour « ne pas rouvrir le cadrage ».

Quelle action est la meilleure ?

A. Conserver la carte initiale jusqu’à Phase H.  
B. Mettre à jour la stakeholder map, les concerns et les plans d’engagement, puis vérifier l’impact sur requirements et vues.  
C. Recommencer tout l’ADM depuis Preliminary.  
D. Ignorer l’organisation et se concentrer uniquement sur l’Application Architecture.

**Scoring : B=5, C=3, A=1, D=0.**

**Pourquoi B :** stakeholder management est continu. C peut être nécessaire seulement si le changement est structurel au point d’exiger un nouveau cycle ; A fige une information devenue fausse ; D ignore un impact architectural réel.

**Mapping : Stakeholder Management — Continuous Engagement.**

---

## S011 — Un diagramme pour tout le monde

L’architecte prépare un diagramme technique de 80 composants et veut l’utiliser pour le comité exécutif, le CISO, les équipes métier et les SRE.

Quelle approche est la meilleure ?

A. Utiliser le même diagramme pour garantir une « source unique ».  
B. Produire des views adaptées aux concerns des stakeholders, construites à partir d’une base architecturale cohérente.  
C. Supprimer toute modélisation et envoyer uniquement du texte.  
D. Présenter la vue technique uniquement au sponsor afin qu’il la redistribue.

**Scoring : B=5, A=3, D=1, C=0.**

**Pourquoi B :** cohérence de la source ne signifie pas uniformité des vues. A a une intention de cohérence mais ignore les concerns ; D délègue mal la communication ; C abandonne un moyen utile sans raison.

**Mapping : Stakeholder Management — Viewpoints and Views.**

---

## S012 — Forte influence, faible intérêt

Un directeur infrastructure a un fort pouvoir d’arbitrage mais peu d’intérêt quotidien pour la transformation. L’équipe lui envoie chaque jour tous les détails de conception, ce qui provoque une perte d’attention.

Quelle action est la meilleure ?

A. Maintenir le stakeholder satisfait avec une communication ciblée sur décisions, risques et impacts, sans le surcharger.  
B. L’exclure totalement car son intérêt est faible.  
C. Continuer à envoyer tous les détails par prudence.  
D. Le traiter comme un membre à temps plein de l’équipe projet.

**Scoring : A=5, C=3, D=1, B=0.**

**Pourquoi A :** l’engagement doit être proportionné à influence et intérêt. C maintient l’information mais la rend inefficace ; D sur-engage ; B ignore un acteur influent.

**Mapping : Stakeholder Management — Influence / Interest.**

---

## S013 — Du concern à la requirement

Le responsable Operations dit : « je ne veux plus passer mes nuits à gérer des bascules manuelles ». L’équipe copie cette phrase telle quelle dans l’Architecture Requirements Specification.

Quelle action est la meilleure ?

A. Conserver uniquement la phrase : elle représente parfaitement une requirement.  
B. Transformer le concern en requirements vérifiables sur failover, automatisation, RTO/RPO, observabilité et tests, tout en gardant la traçabilité vers le stakeholder.  
C. Ignorer ce concern car il n’est pas formulé techniquement.  
D. Choisir immédiatement un produit de haute disponibilité.

**Scoring : B=5, A=3, D=1, C=0.**

**Pourquoi B :** un concern alimente des requirements mais n’est pas automatiquement une requirement testable. A préserve la voix du stakeholder mais pas l’exploitabilité ; D saute directement à la solution ; C perd une information essentielle.

**Mapping : Stakeholder Management — Concern → Requirement.**

---

## S014 — Architecture Board et acceptation métier

L’Architecture Board valide une cible. Les responsables métier clés déclarent ensuite qu’elle ne répond pas à leur processus critique. Un architecte affirme que la validation du Board rend leur avis inutile.

Quelle est la meilleure réponse ?

A. La décision du Board remplace toujours l’acceptation des stakeholders.  
B. Le Board est un mécanisme de gouvernance, mais il faut revoir les concerns métier non satisfaits, vérifier requirements et vues, puis soumettre les ajustements à la gouvernance appropriée.  
C. Dissoudre l’Architecture Board.  
D. Demander au métier de s’adapter à la cible sans analyse.

**Scoring : B=5, A=3, D=1, C=0.**

**Pourquoi B :** gouvernance et stakeholder management se complètent. A reconnaît le pouvoir du Board mais le transforme en substitut à l’analyse des concerns ; D nie la valeur métier ; C détruit le mécanisme au lieu de corriger le processus.

**Mapping : Stakeholder Management — Governance and Stakeholder Acceptance.**

---

Contenu pédagogique original ; aucun scénario officiel n’est reproduit.