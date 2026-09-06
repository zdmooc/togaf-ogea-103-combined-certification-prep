# Migration and Transformation English

## 1. Vocabulaire clé

- migration strategy
- transition state
- transition architecture
- migration wave
- sequencing
- dependency
- cutover
- coexistence
- rollback
- decommissioning
- pilot scope
- phased migration
- big-bang migration
- readiness
- business continuity
- adoption
- operating model
- target operating model
- legacy system
- modernization
- technical debt

## 2. Expliquer la stratégie

> We selected a phased migration strategy because business continuity is critical. The target cannot be reached in one step, so we defined transition architectures and migration waves.

> Each wave delivers a coherent set of capabilities and reduces a defined part of the legacy footprint.

## 3. Expliquer les dépendances

> The migration sequence is driven by dependencies. For example, observability and identity capabilities must be available before we migrate business-critical services.

> Some work packages can run in parallel, while others are prerequisites.

## 4. Expliquer la coexistence

> During the transition period, legacy and target components coexist. This increases temporary complexity, so ownership, interfaces, data synchronization, and decommissioning criteria must be explicit.

## 5. Expliquer le cutover

> The cutover plan defines how traffic and responsibilities move from the existing platform to the new one. We define entry criteria, validation checks, rollback conditions, and post-cutover monitoring.

## 6. Expliquer le rollback

> A rollback is not the primary strategy; it is a controlled recovery option. We define the conditions under which rollback remains technically and operationally possible.

## 7. Expliquer une Transition Architecture

> A transition architecture is a coherent intermediate state between the baseline and the final target. It is not simply a project milestone. It describes an architecture that can operate safely for a period of time.

## 8. Expliquer la roadmap

> The roadmap shows how the organization moves from the baseline to the target through work packages and transition states. It makes dependencies, sequencing, and major outcomes visible.

## 9. Expliquer la priorisation

> We prioritize migration work based on business value, risk reduction, dependency constraints, cost, and organizational readiness.

> A technically easy migration is not always the highest-priority migration.

## 10. Expliquer une modernisation applicative

> Modernization does not automatically mean rewriting everything. We first assess business value, technical constraints, coupling, operational risk, and future capabilities. Depending on the context, the right option may be retain, rehost, replatform, refactor, replace, or retire.

## 11. Expliquer une migration vers OpenShift sans faire de TOGAF un catalogue produit

> OpenShift may be part of the target technology architecture if it satisfies the required platform capabilities, security controls, operational model, and lifecycle constraints. The architecture decision should be requirement-driven, not product-driven.

## 12. Questions d’entretien

### How do you reduce migration risk?

> I reduce migration risk by defining transition states, explicit dependencies, pilot scopes, acceptance criteria, rollback conditions, observability, and governance checkpoints. I also avoid migrating too many critical capabilities at the same time.

### How do you decide migration order?

> I consider business value, risk, dependencies, readiness, cost, and technical feasibility. I then sequence work packages into migration waves and validate the plan with the relevant stakeholders.

### What is the difference between roadmap and migration plan?

> The roadmap gives the transformation trajectory. The migration plan is more detailed and focuses on prioritized execution and sequencing.

## 13. MayaBank answer — 90 seconds

> MayaBank cannot replace the complete payment landscape in one step because the business continuity risk is too high. We therefore use an incremental migration. First, we establish common capabilities such as observability, security controls, API governance, and the target runtime platform. We then migrate a limited payment scope and validate the transition architecture in production. Additional services are migrated in waves based on dependencies, business value, and risk. Legacy components remain only while they are required for coexistence, and each wave has explicit decommissioning criteria.

## 14. Useful connectors

- first
- then
- before that
- in parallel
- as a prerequisite
- as a result
- however
- therefore
- in the short term
- in the target state
- during the transition
- once the capability is proven

## 15. Speaking drill

Répondre sans notes :

1. Why would you avoid a big-bang migration?
2. What is a transition architecture?
3. How do you prioritize migration waves?
4. How do you manage coexistence?
5. When can a legacy component be decommissioned?
