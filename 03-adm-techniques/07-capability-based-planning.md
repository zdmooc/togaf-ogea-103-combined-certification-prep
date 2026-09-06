# Capability-Based Planning

## 1. Definition

Le **Capability-Based Planning** est une approche de planification centrée sur les **capabilities** que l’entreprise doit posséder ou renforcer pour atteindre ses objectifs, plutôt que sur une liste de projets ou de produits.

Une **Business Capability** exprime ce que l’entreprise est capable de faire. Elle est relativement stable par rapport aux applications, équipes ou produits qui peuvent changer.

Le raisonnement est :

**Strategy → Outcomes → Capabilities → Capability gaps → Increments / Work Packages → Roadmap**.

## 2. Pourquoi cette technique existe

Une organisation peut accumuler des projets sans construire les capacités nécessaires.

Exemple :

- projet API Gateway ;
- projet Kafka ;
- projet OpenShift ;
- projet observability.

Pris séparément, ces projets ne disent pas quelle capacité métier ou d’entreprise est recherchée.

Une formulation capability-based serait :

« construire une capacité de traitement de paiement temps réel, observable, résiliente et réutilisable ».

Les solutions techniques deviennent alors des moyens, pas la finalité.

## 3. Capability vs Application

**Capability** = ce que l’entreprise doit être capable de faire.

**Application** = un élément du système d’information qui peut supporter cette capability.

Exemple :

Capability : Fraud Detection.

Applications possibles : fraud engine, rules service, ML service, case management.

Une capability peut être supportée par plusieurs applications et plusieurs capacités peuvent partager une application.

## 4. Capability vs Process

Capability = capacité relativement stable.

Process = manière d’exécuter des activités pour produire un résultat.

Les processus peuvent changer alors que la capability reste nécessaire.

## 5. Position dans l’ADM

- Phase A : relier stratégie, goals et capabilities ;
- Phase B : modéliser et analyser les business capabilities ;
- Phase E : regrouper les changements autour de capacités ;
- Phase F : séquencer les increments ;
- Phase H : réévaluer les capabilities si la stratégie change.

## 6. Méthode pratique

### Étape 1 — Partir des outcomes

Exemples :

- réduction du délai de paiement ;
- disponibilité 24/7 ;
- conformité à un nouveau scheme ;
- diminution du coût de traitement.

### Étape 2 — Identifier les capabilities

Exemples MayaBank :

- Payment Initiation ;
- Payment Validation ;
- Fraud Screening ;
- Payment Orchestration ;
- Clearing Integration ;
- Exception Management ;
- Real-Time Monitoring.

### Étape 3 — Évaluer la maturité

| Capability | Current | Target | Gap |
|---|---:|---:|---:|
| Payment Orchestration | 2/5 | 5/5 | 3 |
| Real-Time Monitoring | 1/5 | 4/5 | 3 |
| API Management | 2/5 | 4/5 | 2 |
| Event Streaming | 1/5 | 4/5 | 3 |

### Étape 4 — Identifier les increments

Une capability complexe peut être développée progressivement.

Exemple :

1. foundational platform ;
2. first payment flow ;
3. additional schemes ;
4. full decommissioning.

### Étape 5 — Relier aux work packages

Les work packages réalisent les changements nécessaires pour construire ou renforcer les capabilities.

## 7. Capability Increment

Un **capability increment** représente une augmentation cohérente et exploitable d’une capability.

L’intérêt est de créer de la valeur progressivement plutôt que d’attendre une cible finale très lointaine.

Exemple :

- Increment 1 : payment API + basic orchestration ;
- Increment 2 : fraud + real-time events ;
- Increment 3 : full multi-scheme resilience.

## 8. Relation avec Transition Architecture

Une Transition Architecture peut matérialiser un plateau intermédiaire où certaines capabilities sont déjà disponibles tandis que d’autres restent en transformation.

Capability planning aide donc à expliquer **pourquoi** un état intermédiaire existe.

## 9. Relation avec Portfolio Planning

Capability-Based Planning aide à éviter un portefeuille organisé uniquement par technologies ou projets.

On peut demander :

- quelle capability ce projet renforce-t-il ?
- quelle valeur produit-elle ?
- existe-t-il un doublon ?
- quelle dépendance entre capabilities ?

## 10. Exemple MayaBank

Objectif : paiement instantané européen.

Capabilities prioritaires :

1. Payment Orchestration ;
2. ISO 20022 Information Management ;
3. Real-Time Event Distribution ;
4. Fraud Screening ;
5. Observability ;
6. Resilient Platform Operations.

Work packages :

- WP01 Platform Foundation ;
- WP02 ISO 20022 Canonical Model ;
- WP03 Event Streaming ;
- WP04 Payment Orchestration ;
- WP05 Observability ;
- WP06 Migration Waves.

La roadmap peut maintenant être justifiée par les capabilities, pas par une collection d’outils.

## 11. ArchiMate — extension professionnelle

ArchiMate permet de représenter :

- Capability ;
- Resource ;
- Course of Action ;
- Work Package ;
- Plateau ;
- Gap.

Cela crée une bonne continuité entre stratégie et transformation, mais ArchiMate n’est pas requis pour comprendre le principe TOGAF.

## 12. Erreurs fréquentes

- appeler une application une capability ;
- définir des capabilities trop techniques ;
- confondre capability et process ;
- créer une capability map sans lien avec la stratégie ;
- ne pas évaluer Current vs Target ;
- ne pas transformer les gaps en increments.

## 13. Pièges OGEA-103

- Capability-Based Planning part de résultats et capacités, pas de produits.
- Une capability est relativement stable et indépendante d’une solution particulière.
- Les capability gaps peuvent influencer Phase E/F.
- Une réponse qui propose immédiatement une application peut être moins bonne qu’une réponse qui clarifie d’abord la capability requise.

## 14. Foundation questions

### Q1
Quel énoncé décrit le mieux une capability ?

A. Un logiciel précis  
B. Ce que l’entreprise doit être capable de faire  
C. Un projet temporaire  
D. Une vue d’architecture

**Réponse : B.**

## 15. Practitioner scenario

Un programme possède quinze projets techniques mais ne peut expliquer quelle valeur métier ils créent. La meilleure approche est de reconnecter stratégie, outcomes, capabilities, gaps et work packages pour rationaliser la roadmap.

## 16. English for Architects

> We used capability-based planning to connect the transformation roadmap to business outcomes rather than individual technologies.

## 17. Key points

- Strategy → Capability → Gap → Increment → Work Package.
- Capability ≠ application.
- Capability ≠ process.
- Les increments permettent une montée progressive.
- La technique relie architecture et portfolio transformation.

---

Original educational content aligned with TOGAF capability-based planning concepts.