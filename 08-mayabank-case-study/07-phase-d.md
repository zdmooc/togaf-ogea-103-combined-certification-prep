# MayaBank — Phase D: Technology Architecture

## 1. Objective

Phase D définit la **Technology Architecture** nécessaire pour exécuter les architectures Business, Data et Application de MayaBank.

Le but n’est pas de sélectionner des produits parce qu’ils sont modernes, mais de traduire les requirements en capacités technologiques cohérentes.

## 2. Baseline Technology Architecture

Constats simplifiés :

- environnements hétérogènes ;
- middleware historique fortement couplé ;
- déploiements partiellement manuels ;
- supervision par silos ;
- gestion des secrets non homogène ;
- capacités de scaling différentes selon les applications ;
- dépendance à des configurations locales ;
- reprise après incident complexe.

## 3. Technology capabilities required

La cible doit fournir :

- compute conteneurisé ;
- orchestration de workloads ;
- networking sécurisé ;
- API exposure ;
- messaging/event streaming ;
- secrets management ;
- identity and access controls ;
- persistent storage lorsque requis ;
- logs, metrics et traces ;
- CI/CD automatisé ;
- configuration management ;
- backup/recovery ;
- multi-zone ou mécanismes de résilience appropriés.

## 4. Target platform concept

MayaBank choisit comme orientation :

- plateforme Kubernetes/OpenShift pour services cloud-native ;
- API gateway / API management ;
- event streaming pour événements métier adaptés ;
- observability platform centralisée ;
- secrets manager ;
- GitOps/CI-CD ;
- intégration sécurisée avec les systèmes legacy et partenaires.

Important : **OpenShift, Kafka ou un produit précis sont des choix du cas MayaBank, pas des prescriptions TOGAF**.

## 5. Baseline → Target → Gap

| Technology area | Baseline | Target | Gap |
|---|---|---|---|
| runtime | hétérogène | plateforme standardisée | majeur |
| deployment | semi-manuel | automatisé/GitOps | majeur |
| integration | point-à-point | API + events gouvernés | majeur |
| observability | silos | end-to-end | majeur |
| secrets | hétérogène | service central/gouverné | majeur |
| resilience | variable | patterns standardisés | moyen/majeur |
| network policy | locale | contrôles homogènes | moyen |

## 6. Technology principles applied

- immutable deployment where practical ;
- infrastructure/configuration as code ;
- least privilege ;
- encryption in transit ;
- automated evidence generation ;
- standardized telemetry ;
- platform services shared when this reduces duplication ;
- avoid technology lock-in without explicit decision.

## 7. Non-functional requirements

Exemples à préciser contractuellement :

- availability targets ;
- latency budgets ;
- RTO/RPO ;
- scalability ;
- security controls ;
- audit logging ;
- capacity management ;
- disaster recovery ;
- operational support model.

## 8. Security architecture implications

La Technology Architecture doit intégrer :

- segmentation réseau ;
- workload identity ;
- RBAC ;
- secrets rotation ;
- image security ;
- policy enforcement ;
- vulnerability management ;
- audit trails.

Security reste cross-cutting et ne doit pas être considérée comme un ajout de dernière minute.

## 9. Operational architecture

Le run cible inclut :

- SLO/SLA ;
- alerting ;
- incident response ;
- runbooks ;
- capacity monitoring ;
- patching ;
- disaster recovery tests ;
- ownership de plateforme.

## 10. Technology ABB/SBB

### ABB

- Container Platform ;
- Event Streaming ;
- API Management ;
- Secrets Management ;
- Observability ;
- CI/CD Automation.

### SBB examples for MayaBank

- OpenShift cluster ;
- Kafka distribution ;
- selected API management product ;
- chosen secrets manager ;
- selected observability stack.

Le passage ABB → SBB rend la solution plus concrète.

## 11. Transition constraints

La nouvelle plateforme doit coexister avec :

- applications legacy ;
- bases existantes ;
- partenaires externes ;
- réseaux et zones de sécurité actuels.

Les patterns de bridge/adapters doivent être temporaires et gouvernés.

## 12. Phase D output

MayaBank dispose maintenant de :

- Baseline Technology Architecture ;
- Target Technology Architecture ;
- technology gaps ;
- standards candidats ;
- NFR enrichies ;
- ABB/SBB initiaux ;
- risques et dépendances pour Phase E.

## 13. Practitioner trap

Si le scénario demande « quelle plateforme et quels services technologiques supportent la cible applicative ? », Phase D est pertinente. Si le scénario demande « comment regrouper les changements en work packages et transitions ? », on est déjà en Phase E.

## 14. English for Architects

> Phase D defines the technology platform, shared services, resilience, security, and operational capabilities required to support the target applications and data architecture.

---

Original educational case study; MayaBank is fictional.