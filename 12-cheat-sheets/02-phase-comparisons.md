# Cheat Sheet — Phase Comparisons

## Preliminary vs Phase A

| Preliminary | Phase A |
|---|---|
| prépare la **Architecture Capability** | lance un **Architecture Development Cycle** |
| rôles, governance, principles, repository, tailoring | scope, stakeholders, concerns, value, risks, Vision |
| « comment faisons-nous de l’architecture ? » | « quel travail d’architecture lançons-nous et pourquoi ? » |

**Piège :** une organisation sans règles de gouvernance ni rôles communs → problème Preliminary, même si des diagrammes existent déjà.

## Phase A vs Phase B

| Phase A | Phase B |
|---|---|
| vision de haut niveau | Business Architecture détaillée |
| valeur et sponsor | capabilities, business services, processes, actors |
| scope et stakeholders | Baseline/Target/Gaps métier |

**Piège :** une Architecture Vision n’est pas une Target Business Architecture complète.

## Phase B vs Phase C Application

| Phase B | Phase C Application |
|---|---|
| ce que l’entreprise doit savoir faire | quels services/applications soutiennent cela |
| capability indépendante de la solution | application/service comme moyen |

**Piège :** « gérer les paiements instantanés » = capability ; `Payment Orchestrator` = application/service.

## Phase C Data vs Phase C Application

| Data | Application |
|---|---|
| information, ownership, lifecycle, quality, flows | services applicatifs, interactions, interfaces, portfolio |

**Piège :** API ≠ automatiquement Data Architecture ; elle peut être un élément d’interaction applicative, alors que les objets échangés et leur gouvernance relèvent de Data.

## Phase D vs Phase E

| D | E |
|---|---|
| Technology Architecture cible | Opportunities & Solutions |
| plateformes/services technologiques | regroupement des gaps en work packages |
| Baseline/Target/Gaps techno | Transition Architectures + roadmap initiale |

**Mot clé :** **D = target technology**, **E = transformation options**.

## Phase E vs Phase F

| E | F |
|---|---|
| identifie et structure work packages | priorise et séquence |
| Transition Architectures | migration waves |
| Architecture Roadmap initiale | Implementation & Migration Plan détaillé |

**Mot clé :** **E = quoi transformer**, **F = dans quel ordre et selon quelles priorités**.

## Phase F vs Phase G

| F | G |
|---|---|
| planifie migration | gouverne implémentation réelle |
| priorités, dépendances, planning | compliance reviews, Architecture Contract, deviations |

**Piège :** un écart constaté pendant l’implémentation → G, pas F.

## Phase G vs Phase H

| G | H |
|---|---|
| conformité de l’implémentation en cours | évolution de l’architecture après/pendant changement |
| projet/programme vs architecture approuvée | nouveaux drivers, impact, nouveau cycle éventuel |

**Mot clé :** **G = implement correctly**, **H = decide how architecture evolves**.

## Phase H vs Requirements Management

| H | Requirements Management |
|---|---|
| décide comment répondre à un changement significatif | capture, trace, maintient et analyse les exigences |
| peut déclencher nouveau cycle | transversal à toutes les phases |

**Piège :** une nouvelle exigence réglementaire peut impliquer les deux : Requirements Management pour la tracer, Phase H pour décider du changement architectural.

## Baseline / Target / Transition

- **Baseline** = état actuel pertinent.
- **Target** = état futur souhaité.
- **Transition Architecture** = état intermédiaire cohérent et gouvernable.

## Roadmap vs Implementation & Migration Plan

- **Architecture Roadmap** : trajectoire de transformation, work packages, transitions, dépendances à haut niveau.
- **Implementation & Migration Plan** : plan plus détaillé et priorisé d’exécution/migration.

## Question éclair

Si une réponse saute une phase nécessaire, choisit une technologie avant le problème, ignore les stakeholders ou traite un écart sans gouvernance, elle est souvent moins bonne en Practitioner.
