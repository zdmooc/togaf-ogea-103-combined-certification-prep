# MayaBank Case Study — Context

## 1. Purpose

Ce cas fil rouge applique TOGAF à une transformation réaliste d’une banque fictive nommée **MayaBank**. Le but n’est pas de produire une architecture bancaire complète mais de montrer comment un architecte raisonne de bout en bout avec l’ADM.

Le cas sert à relier :

- stratégie ;
- stakeholders ;
- requirements ;
- Business, Data, Application et Technology Architecture ;
- work packages ;
- Transition Architectures ;
- roadmap ;
- migration ;
- governance ;
- change management.

## 2. Business context

MayaBank opère plusieurs chaînes de paiement européennes héritées de programmes successifs. Le SI fonctionne mais présente plusieurs difficultés :

- délais variables selon les canaux ;
- forte dépendance à des traitements batch ;
- composants redondants ;
- intégrations point-à-point ;
- incidents complexes à diagnostiquer ;
- observabilité insuffisante ;
- responsabilités fragmentées ;
- coûts d’exploitation élevés ;
- évolution lente face aux exigences réglementaires et marché.

La banque veut développer une plateforme de paiement plus rapide, résiliente et gouvernable, tout en limitant le risque de migration.

## 3. Business drivers

Drivers principaux :

1. améliorer le traitement temps réel ;
2. réduire les opérations manuelles ;
3. accélérer l’intégration de nouveaux services de paiement ;
4. renforcer résilience, sécurité et traçabilité ;
5. rationaliser le patrimoine ;
6. standardiser les interfaces ;
7. réduire le délai entre besoin métier et mise en production ;
8. préserver la continuité des paiements pendant la transformation.

## 4. Strategic goals

Les objectifs initiaux sont formulés à haut niveau :

- diminuer le temps de traitement des paiements ;
- augmenter la disponibilité ;
- réduire les erreurs manuelles ;
- diminuer le coût d’exploitation ;
- améliorer la conformité et l’auditabilité ;
- permettre une évolution incrémentale de la plateforme.

Ces objectifs ne sont pas encore des requirements détaillées.

## 5. Stakeholders

| Stakeholder | Concern principal |
|---|---|
| Executive Sponsor Payments | valeur, délai, risque |
| Business Operations | efficacité, exceptions, continuité |
| Product | rapidité d’évolution, nouveaux services |
| Enterprise Architecture | cohérence cible, réutilisation |
| Solution Architecture | faisabilité et intégration |
| CISO / Security | identité, secrets, sécurité des flux |
| Risk & Compliance | réglementation, traçabilité |
| Operations / SRE | résilience, observabilité, supportabilité |
| Data Governance | qualité, ownership, rétention |
| Finance | coût, investissement, dépendances |
| Delivery Teams | contraintes d’implémentation |
| Vendor Management | dépendance fournisseurs |

## 6. Initial Baseline

La Baseline est volontairement simplifiée :

- plusieurs applications de paiement ;
- middleware d’intégration historique ;
- bases relationnelles distinctes ;
- échanges fichiers et API ;
- traitements synchrones et batch ;
- monitoring fragmenté ;
- déploiements semi-automatisés ;
- responsabilités métier et IT distribuées.

## 7. Initial Target vision

La cible envisagée repose sur :

- services de paiement clairement découpés ;
- contrats d’API et événements standardisés ;
- traitement temps réel lorsque nécessaire ;
- données gouvernées ;
- plateforme conteneurisée ;
- observabilité et sécurité intégrées ;
- automatisation du delivery ;
- gouvernance d’architecture et conformité explicites.

Attention : à ce stade il s’agit d’une **vision**, pas encore de l’architecture détaillée.

## 8. Scope assumptions

Le premier cycle couvre :

- paiements européens ;
- orchestration ;
- validation ;
- screening risque/fraude ;
- gestion d’exceptions ;
- intégration clearing/settlement ;
- observabilité ;
- IAM technique ;
- données opérationnelles associées.

Sont hors scope initial :

- refonte complète du core banking ;
- CRM ;
- crédit ;
- gestion de patrimoine ;
- remplacement intégral des systèmes comptables.

## 9. Constraints

Contraintes majeures :

- aucune interruption prolongée des paiements ;
- conservation de certaines applications legacy pendant la transition ;
- exigences de sécurité fortes ;
- auditabilité des décisions ;
- budget par étapes ;
- compétences cloud-native encore inégales ;
- plusieurs équipes autonomes ;
- dépendances avec partenaires externes.

## 10. Principles used in the case

Exemples de principes MayaBank :

- business continuity first ;
- security by design ;
- API and event contracts are governed ;
- reuse before duplication ;
- observable by default ;
- data ownership must be explicit ;
- automation before manual operation ;
- architecture decisions must be traceable.

## 11. What the architect must avoid

- choisir les produits avant d’avoir compris les besoins ;
- confondre capability et application ;
- transformer la roadmap en simple liste de projets ;
- supposer qu’une migration cloud-native suffit à produire de la valeur ;
- ignorer les stakeholders opérationnels ;
- traiter sécurité et données après coup ;
- viser une cible finale sans Transition Architecture.

## 12. Practitioner lens

Dans un scénario d’examen, MayaBank pourrait être présentée avec beaucoup de détails techniques. La première question à se poser reste :

**Quel problème ADM doit être résolu maintenant ?**

Le meilleur raisonnement privilégie la séquence TOGAF, les stakeholders, les requirements, les gaps et la gouvernance avant l’optimisation technique locale.

## 13. English for Architects

> MayaBank is modernizing its payment landscape while preserving business continuity and regulatory compliance.

> The transformation is organized as an incremental architecture roadmap rather than a single big-bang migration.

---

This case study is original educational content inspired by TOGAF concepts. MayaBank is fictional.