# MayaBank — Preliminary Phase

## 1. Why Preliminary matters here

MayaBank ne peut pas démarrer correctement par un diagramme cible. Avant de lancer le cycle ADM, la banque doit établir ou ajuster sa **Architecture Capability** : gouvernance, rôles, principes, méthode, repository et règles de décision.

Le problème principal n’est donc pas encore « quelle architecture de paiement ? », mais :

**sommes-nous organisés pour produire, gouverner et maintenir cette architecture ?**

## 2. Current situation

Avant Preliminary :

- plusieurs équipes d’architecture travaillent avec des pratiques différentes ;
- les décisions ne sont pas toujours centralisées ;
- les principes sont partiellement documentés ;
- les exceptions techniques sont gérées localement ;
- les artifacts sont stockés dans plusieurs outils ;
- la frontière entre architecture, delivery et gouvernance projet est floue.

## 3. Target Architecture Capability

MayaBank décide de formaliser :

- un **Architecture Board** transverse ;
- des Enterprise Architects responsables de la cohérence globale ;
- des Domain Architects Business, Data, Application, Technology et Security ;
- des Solution Architects proches des programmes ;
- une procédure de Compliance Review ;
- un processus d’exception/waiver ;
- un Architecture Repository commun ;
- un catalogue de principes et standards ;
- une gouvernance des ADR/architecture decisions.

## 4. Governance model

### Architecture Board

Responsabilités :

- approuver les orientations structurantes ;
- arbitrer les conflits ;
- décider des exceptions majeures ;
- vérifier l’alignement avec les principes ;
- suivre les risques architecturaux.

### Architecture Team

Responsabilités :

- conduire l’ADM ;
- produire les views et artifacts nécessaires ;
- gérer les requirements architecturales ;
- préparer les décisions ;
- accompagner le delivery.

### Delivery Teams

Responsabilités :

- implémenter ;
- respecter les contraintes approuvées ;
- remonter les écarts ;
- produire les preuves de conformité nécessaires.

## 5. Principles selected

MayaBank retient notamment :

1. **Business Continuity First** — une migration ne doit pas créer un risque disproportionné sur les paiements.
2. **Security by Design** — sécurité intégrée dès l’architecture.
3. **Observable by Default** — monitoring, logs, metrics et traces sont des exigences de base.
4. **Contract-First Integration** — APIs/events versionnés et gouvernés.
5. **Data Ownership** — chaque domaine de données a un owner explicite.
6. **Automation First** — delivery et opérations répétitives automatisés autant que possible.
7. **Reuse Before Build** — réutiliser capacités et building blocks pertinents avant duplication.

## 6. Tailoring the ADM

MayaBank décide de ne pas appliquer l’ADM comme un cycle lourd identique partout.

Le tailoring prévoit :

- cycles rapides pour domaines maîtrisés ;
- analyses plus profondes sur sécurité, résilience et données ;
- itérations B/C/D ;
- gouvernance continue avec les équipes Agile ;
- artifacts proportionnés aux concerns ;
- décisions importantes enregistrées dans le Repository.

## 7. Repository organization

Sections proposées :

- Architecture Metamodel ;
- Architecture Capability ;
- Architecture Landscape ;
- Standards Information Base ;
- Reference Library ;
- Governance Log.

MayaBank y stocke notamment :

- principes ;
- standards APIs/events ;
- modèles de sécurité ;
- patterns de résilience ;
- architectures baseline/target ;
- roadmaps ;
- décisions et exceptions ;
- résultats de compliance reviews.

## 8. Request for Architecture Work

Le sponsor Payments formule une demande : moderniser le paysage de paiement européen en améliorant rapidité, résilience, auditabilité et capacité d’évolution, avec migration incrémentale.

La demande ne présuppose pas encore une solution précise.

## 9. Preliminary outputs for MayaBank

À l’issue de Preliminary :

- Architecture Capability ajustée ;
- principes approuvés ;
- rôles et responsabilités définis ;
- gouvernance et Architecture Board clarifiés ;
- Repository structuré ;
- tailoring de l’ADM défini ;
- Request for Architecture Work prête ;
- readiness et contraintes organisationnelles connues.

## 10. Preliminary vs Phase A

| Preliminary | Phase A |
|---|---|
| prépare la capacité d’architecture | cadre l’engagement de transformation |
| définit gouvernance et méthode | définit scope, stakeholders et vision |
| établit principes et repository | établit Architecture Vision |
| répond « comment faisons-nous de l’architecture ? » | répond « quel travail d’architecture lançons-nous et pourquoi ? » |

## 11. Practitioner trap

Si un scénario dit que MayaBank possède déjà une cible technique mais aucune gouvernance commune, la meilleure action n’est pas d’affiner Phase D. Il faut d’abord corriger la **Architecture Capability** et le cadre de gouvernance.

## 12. English for Architects

> In the Preliminary Phase, MayaBank establishes the architecture capability, governance model, principles, roles, and repository required to conduct the transformation consistently.

---

Original educational case study; MayaBank is fictional.