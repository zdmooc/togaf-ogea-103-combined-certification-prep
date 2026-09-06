# Risk Management

## 1. Definition

Le **Risk Management** en architecture consiste à identifier, analyser, traiter, suivre et gouverner les risques qui peuvent empêcher l’entreprise d’atteindre les objectifs associés à l’architecture.

Le risque n’est pas un simple défaut technique. Il peut être :

- métier ;
- réglementaire ;
- sécurité ;
- opérationnel ;
- fournisseur ;
- coût ;
- planning ;
- compétences ;
- disponibilité ;
- data ;
- migration ;
- dépendance technologique.

Le raisonnement est :

**Objective → threat/uncertainty → impact + likelihood → response → residual risk → governance**.

## 2. Pourquoi le risque est transversal

Chaque phase ADM peut créer, révéler ou réduire des risques.

- Phase A : risques stratégiques et de scope ;
- Phase B : risques d’organisation ou processus ;
- Phase C : risques data/applications ;
- Phase D : risques technologiques ;
- Phase E/F : risques de transformation et migration ;
- Phase G : risques de non-conformité d’implémentation ;
- Phase H : risques liés aux changements externes ou obsolescence.

Risk Management n’est donc pas une phase indépendante.

## 3. Risk vs Issue vs Constraint vs Gap

### Risk

Événement ou condition incertaine pouvant avoir un impact.

### Issue

Problème déjà matérialisé.

### Constraint

Limite imposée à l’architecture.

### Gap

Différence entre Baseline et Target.

Exemple MayaBank :

- Constraint : certaines données doivent rester dans une zone réglementaire donnée.
- Gap : absence de plateforme de streaming cible.
- Risk : équipe insuffisamment expérimentée pour opérer Kafka 24/7.
- Issue : incident récurrent actuel sur la réplication d’un système legacy.

## 4. Processus pratique

### Étape 1 — Identifier

Sources :

- stakeholder concerns ;
- requirements ;
- assumptions ;
- architecture gaps ;
- dependencies ;
- vendor choices ;
- technical debt ;
- transformation readiness ;
- compliance constraints.

### Étape 2 — Analyser

Pour chaque risque :

- cause ;
- événement ;
- impact ;
- likelihood ;
- scope ;
- owner.

### Étape 3 — Évaluer

Une matrice qualitative peut aider :

| Likelihood | Impact | Niveau |
|---|---|---|
| faible | faible | faible |
| moyen | fort | important |
| fort | fort | critique |

Le score ne remplace pas le jugement architectural.

### Étape 4 — Traiter

Réponses classiques :

- avoid ;
- reduce / mitigate ;
- transfer / share ;
- accept.

### Étape 5 — Suivre le residual risk

Après mitigation, il reste souvent un **residual risk**.

Il doit être explicitement accepté au bon niveau si nécessaire.

## 5. Risk and Security

La sécurité est un concern transverse de l’architecture.

Exemples :

- mauvaise séparation des privilèges ;
- secrets exposés ;
- trust boundary mal définie ;
- supply-chain compromise ;
- accès excessifs ;
- absence de chiffrement ;
- mauvaise résilience à une attaque.

TOGAF dispose de guidance spécifique pour intégrer risk et security à l’Enterprise Architecture. L’idée essentielle est de ne pas ajouter la sécurité à la fin.

## 6. Relation avec Requirements Management

Les risques peuvent créer ou modifier des exigences.

Exemple :

Risk : perte de messages pendant une panne.

Requirements possibles :

- durabilité des événements ;
- réplication ;
- reprise ;
- monitoring ;
- tests de failover.

Inversement, une requirement peut introduire un risque de coût ou de complexité.

## 7. Relation avec Architecture Decisions

Une décision d’architecture doit parfois être comprise comme un arbitrage de risques.

Exemple :

Option A : plateforme managée, coût supérieur mais risque d’exploitation inférieur.

Option B : plateforme auto-gérée, coût licence inférieur mais besoin de compétences et run plus importants.

Le rôle de l’architecte n’est pas seulement de dire « A est meilleure », mais de rendre visibles les risques et trade-offs.

## 8. Risk Register minimal

| Risk | Cause | Impact | Likelihood | Response | Owner | Residual |
|---|---|---|---|---|---|---|
| perte compétence Kafka | faible expérience | incident prod | moyen | formation + support | Platform Lead | faible/moyen |
| vendor lock-in | service propriétaire | coût de sortie | moyen | abstraction + exit plan | Architecture | moyen |
| retard migration | dépendances legacy | délai programme | fort | transition progressive | Program | moyen |

## 9. Exemple MayaBank

MayaBank veut traiter des paiements critiques sur une plateforme event-driven.

Risques :

1. perte ou duplication d’événements ;
2. mauvaise gestion des secrets ;
3. saturation pendant les pics ;
4. compétences d’exploitation limitées ;
5. dépendance à un composant fournisseur ;
6. migration simultanée trop ambitieuse.

Réponses :

- idempotence ;
- schema governance ;
- secret management ;
- performance testing ;
- observability ;
- enablement des équipes ;
- Transition Architecture ;
- migration par vagues.

## 10. Risk vs Architecture Governance

Risk Management identifie et traite les risques.

Architecture Governance s’assure notamment que :

- les décisions sont approuvées ;
- les risques majeurs sont visibles ;
- les exceptions sont contrôlées ;
- le residual risk est accepté par l’autorité compétente.

## 11. Erreurs fréquentes

- limiter le risque à la cybersécurité ;
- noter un risque sans owner ;
- créer un registre sans actions ;
- confondre issue et risk ;
- croire qu’une mitigation supprime toujours le risque ;
- oublier les risques organisationnels ;
- accepter implicitement un residual risk.

## 12. Pièges OGEA-103

- Risk Management est transversal.
- Un risque peut générer de nouvelles requirements.
- Une réponse Practitioner qui identifie, évalue puis gouverne le risque est souvent meilleure qu’une réponse qui l’ignore pour aller plus vite.
- Risk ≠ constraint, issue ou gap.

## 13. Foundation questions

### Q1
Qu’est-ce qu’un residual risk ?

A. Un risque restant après traitement  
B. Un gap technique  
C. Une contrainte  
D. Un work package

**Réponse : A.**

### Q2
Le Risk Management intervient :

A. uniquement en Phase D  
B. uniquement en Phase G  
C. à travers le cycle d’architecture  
D. uniquement après déploiement

**Réponse : C.**

## 14. Practitioner scenario

Une option de migration réduit fortement le délai mais augmente le risque d’interruption d’un service de paiement critique. La meilleure approche est d’évaluer formellement le risque, analyser les mitigations et obtenir l’acceptation appropriée du residual risk, plutôt que de sélectionner l’option uniquement sur la vitesse.

## 15. English for Architects

> We identified the architecture risks, defined mitigation actions, and made the residual risks explicit for governance approval.

### Speak it

1. This option introduces an operational risk.
2. We can mitigate the risk with a phased migration.
3. The remaining risk must be accepted by the appropriate stakeholder.

## 16. Key points

- Risk ≠ issue ≠ constraint ≠ gap.
- Le risque est transversal à l’ADM.
- Il faut owner, response et residual risk.
- Risk Management influence requirements, decisions et roadmap.
- Security and risk doivent être intégrés, pas ajoutés à la fin.

---

Original educational content aligned with TOGAF risk and security guidance.