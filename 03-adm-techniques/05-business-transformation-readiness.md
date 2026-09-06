# Business Transformation Readiness

## 1. Definition

La **Business Transformation Readiness Assessment** évalue si l’organisation est réellement capable d’absorber et réussir la transformation envisagée.

Une Target Architecture peut être excellente mais irréaliste si l’entreprise n’a pas :

- les compétences ;
- la capacité de financement ;
- le sponsorship ;
- la maturité de gouvernance ;
- les processus ;
- les ressources ;
- la capacité opérationnelle ;
- la volonté de changement.

Le raisonnement est :

**Target ambition → readiness factors → gaps in readiness → risks/actions → realistic roadmap**.

## 2. Pourquoi cette technique existe

L’architecture ne peut pas supposer que l’organisation est prête.

Exemples :

- cible Kubernetes mais aucune compétence d’exploitation ;
- architecture event-driven mais équipes organisées uniquement autour de batchs ;
- programme multi-cloud sans gouvernance FinOps ;
- nouvelle API strategy sans ownership produit ;
- modèle Zero Trust sans IAM mature.

Ces écarts ne sont pas toujours des gaps purement technologiques. Ce sont des **gaps de capacité de transformation**.

## 3. Où elle intervient

Elle est particulièrement utile lorsque l’on prépare la transformation et les trajectoires, donc autour de Phase A, E et F, mais ses résultats peuvent influencer tout le cycle.

- Phase A : tester la faisabilité globale de l’ambition ;
- B/C/D : identifier les impacts organisationnels et capacitaires ;
- E : construire des work packages réalistes ;
- F : prioriser en fonction de la readiness ;
- G : vérifier que les capacités nécessaires existent réellement.

## 4. Dimensions de readiness

### Leadership and sponsorship

- sponsor identifié ;
- décisions rapides ;
- capacité à arbitrer ;
- soutien au changement.

### Organization

- rôles clairs ;
- responsabilités ;
- operating model ;
- capacité de collaboration transverse.

### Skills

- architecture ;
- engineering ;
- security ;
- operations ;
- data ;
- platform ;
- product management.

### Governance

- Architecture Board ;
- standards ;
- exception process ;
- delivery governance ;
- risk/compliance integration.

### Technology maturity

- automation ;
- CI/CD ;
- observability ;
- IAM ;
- resilience ;
- data governance ;
- platform maturity.

### Financial readiness

- budget ;
- funding model ;
- cost transparency ;
- investment sequencing.

### Change culture

- acceptation du changement ;
- historique de transformations ;
- capacité de formation ;
- résistance organisationnelle.

## 5. Méthode pratique

1. Définir les facteurs critiques de transformation.
2. Évaluer l’état actuel.
3. Définir le niveau requis pour la Target.
4. Identifier les écarts de readiness.
5. Évaluer l’impact sur risques, coûts et délais.
6. Créer des actions de préparation.
7. Intégrer ces actions dans les work packages ou Transition Architectures.
8. Réévaluer au fur et à mesure.

## 6. Exemple de scoring

| Facteur | Actuel | Requis | Gap | Action |
|---|---:|---:|---:|---|
| OpenShift skills | 1/5 | 4/5 | 3 | formation + recrutement |
| GitOps maturity | 2/5 | 4/5 | 2 | platform enablement |
| Architecture governance | 3/5 | 4/5 | 1 | renforcer compliance reviews |
| Observability | 2/5 | 4/5 | 2 | construire shared platform |
| Sponsorship | 4/5 | 4/5 | 0 | maintenir engagement |

Le scoring est un outil ; le raisonnement est plus important que la note.

## 7. Relation avec Risk Management

Readiness insuffisante produit souvent des risques.

Exemple :

Readiness gap : absence de compétences Kafka.

Risk : erreurs d’exploitation ou indisponibilité en production.

Mitigation : formation, support expert, montée en charge progressive, Transition Architecture.

## 8. Relation avec Phase E

Phase E peut créer un work package de **Platform Foundation** ou **Capability Enablement** avant de migrer les applications.

C’est un point important : certains work packages ne livrent pas directement une fonctionnalité métier ; ils rendent la transformation possible.

## 9. Relation avec Phase F

La readiness influence le séquencement.

Même si un work package a une forte valeur métier, il peut être placé après un work package de préparation indispensable.

## 10. Exemple MayaBank

MayaBank vise :

- OpenShift ;
- Kafka ;
- API-first ;
- GitOps ;
- 24/7 operations.

Évaluation :

- équipes Java fortes ;
- faible expérience Kafka en production ;
- GitOps partiel ;
- observabilité hétérogène ;
- governance solide ;
- budget disponible.

Décision :

Avant la migration massive des paiements, MayaBank crée :

- WP01 Platform Foundation ;
- WP02 Platform Operations Enablement ;
- WP03 Observability Foundation ;
- programme de formation et runbooks.

La roadmap devient plus réaliste.

## 11. Erreurs fréquentes

- confondre readiness et architecture maturity uniquement ;
- évaluer seulement la technologie ;
- ignorer sponsorship et organisation ;
- ne pas transformer les gaps de readiness en actions ;
- supposer qu’un outil compense un manque de compétences ;
- ne pas réévaluer la readiness.

## 12. Pièges OGEA-103

- Une Target Architecture correcte peut être prématurée si l’organisation n’est pas prête.
- La readiness peut modifier les work packages et le séquencement.
- Readiness gap ≠ architecture gap, même s’ils peuvent être liés.
- Une réponse Practitioner qui tient compte de la capacité réelle de l’organisation peut être meilleure qu’une réponse qui force directement la Target finale.

## 13. Practitioner scenario

Une banque veut migrer tous ses paiements critiques vers une nouvelle plateforme conteneurisée en six mois. L’architecture cible est validée, mais aucune équipe d’exploitation ne maîtrise la plateforme et les procédures de support n’existent pas.

La meilleure réponse est d’évaluer formellement la readiness et d’intégrer des actions de capability enablement et éventuellement une transition progressive dans la roadmap.

## 14. English for Architects

> We assessed the organization’s readiness before committing to the migration sequence.

### Speak it

1. The target architecture is feasible, but the organization is not fully ready.
2. The main gaps are skills, operations and automation.
3. We added enablement work packages before the critical migration.

## 15. Key points

- Readiness = capacité réelle à réussir la transformation.
- Elle couvre leadership, organisation, skills, governance, technology, finance et culture.
- Elle influence risques, work packages et roadmap.
- Elle évite les trajectoires techniquement belles mais irréalistes.

---

Original educational content aligned with TOGAF transformation-readiness reasoning.