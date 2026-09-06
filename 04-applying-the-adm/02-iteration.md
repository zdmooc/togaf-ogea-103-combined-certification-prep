# Iteration When Applying the ADM

## 1. Definition

L’ADM est **iterative**. Cela signifie que l’architecture peut être développée par boucles successives plutôt que comme une chaîne linéaire exécutée une seule fois.

L’itération peut se produire :

- entre phases ;
- à l’intérieur d’une phase ;
- entre domaines ;
- entre niveaux d’architecture ;
- entre cycles ADM successifs.

Le but n’est pas de « recommencer parce qu’on s’est trompé », mais d’apprendre progressivement et de maintenir la cohérence lorsque de nouvelles informations apparaissent.

## 2. Pourquoi l’itération est normale

L’architecture travaille avec :

- informations incomplètes ;
- stakeholders multiples ;
- risques ;
- dépendances ;
- décisions progressives ;
- contraintes qui évoluent.

Il est donc irréaliste de figer une fois pour toutes Business, Data, Application et Technology Architectures sans retour en arrière.

## 3. Types d’itération

### Iteration between ADM phases

Exemple : Phase D révèle une contrainte technologique qui oblige à ajuster Phase C Application.

### Iteration within a phase

Exemple : plusieurs versions de Target Business Architecture sont explorées avant validation.

### Iteration over the whole ADM cycle

Phase H peut déclencher un nouveau cycle ADM lorsqu’un changement majeur survient.

### Iteration between architecture levels

Enterprise Architecture et Solution Architecture peuvent se nourrir mutuellement : l’entreprise fournit des constraints et patterns ; les solutions remontent des découvertes ou besoins de changement.

## 4. Iteration vs rework

Iteration = apprentissage contrôlé.

Rework = travail à refaire parce que la démarche ou la qualité était insuffisante.

TOGAF accepte l’itération mais l’architecte doit garder :

- traceability ;
- versioning ;
- governance ;
- contrôle des requirements ;
- décisions explicites.

## 5. Exemples entre domaines

### Business → Data

Un nouveau business process exige une nouvelle information.

### Data → Application

La gouvernance d’une donnée impose une séparation de responsabilités applicatives.

### Application → Technology

Une exigence de low latency exige une capability technologique spécifique.

### Technology → Application

Une contrainte de plateforme peut conduire à revoir certains services applicatifs.

## 6. Iteration et Requirements Management

Requirements Management est essentiel pendant les boucles d’itération.

Chaque changement doit permettre de savoir :

- quelle requirement a changé ;
- pourquoi ;
- quels artifacts sont impactés ;
- quels stakeholders doivent être reconsultés ;
- si la Roadmap ou les risks changent.

## 7. Iteration et checkpoints

Une bonne pratique consiste à définir des checkpoints de cohérence :

- après Architecture Vision ;
- après B/C/D ;
- avant consolidation Phase E ;
- avant validation de Phase F ;
- pendant Implementation Governance.

Cela évite une dérive incontrôlée.

## 8. MayaBank

### Iteration 1

Phase B définit Payment Orchestration comme capability cible.

### Iteration 2

Phase C Data identifie l’exigence de canonical payment information.

### Iteration 3

Phase C Application découvre qu’une séparation synchrone de tous les services rendrait la latence trop forte.

### Iteration 4

Phase D évalue les capabilities de messaging et conduit à ajuster Application Architecture vers un mélange API + event-driven.

### Résultat

L’architecture a itéré sans perdre le fil : goals, requirements, risks et decisions restent tracés.

## 9. Iteration et Agile

Iteration ADM et Agile ne sont pas identiques.

- ADM iteration = progression et révision du travail d’architecture ;
- Agile iteration/sprint = cadence de delivery.

Ils peuvent être alignés sans les confondre.

Exemple : une architecture runway peut être enrichie au fil de sprints tout en gardant des checkpoints de gouvernance.

## 10. Erreurs fréquentes

- apprendre ADM comme waterfall ;
- croire qu’une phase terminée ne peut jamais être revisitée ;
- itérer sans versioning ;
- modifier une Target sans mettre à jour les requirements ;
- confondre Agile sprint et ADM phase ;
- refaire toute l’architecture lorsqu’un petit élément change.

## 11. Pièges OGEA-103

- ADM est adaptable et iterative.
- Une phase précédente peut être revisitée si de nouvelles informations l’exigent.
- Requirements Management aide à contrôler les impacts.
- L’itération doit être gouvernée et proportionnée.

## 12. Foundation question

Quel énoncé décrit correctement l’ADM ?

A. Il doit toujours être exécuté une seule fois dans un ordre rigide  
B. Il peut être adapté et utilisé de manière iterative  
C. Une phase précédente ne peut jamais être revisitée  
D. L’itération remplace Requirements Management

**Réponse : B.**

## 13. Practitioner scenario

Pendant Phase D, un architecte découvre que la plateforme imposée ne peut satisfaire une exigence de latence de l’Application Architecture. La meilleure réponse n’est pas d’ignorer le problème au motif que Phase C est terminée. Il faut itérer vers le travail précédent, ajuster l’architecture ou l’exigence avec les stakeholders, puis maintenir la traceability.

## 14. English for Architects

> The ADM is iterative. We may revisit earlier architecture work when new constraints or requirements are discovered.

### Speak it

1. Iteration is expected in complex architecture work.
2. We revisited the application architecture after a technology constraint was discovered.
3. Requirements and decisions remained traceable.

## 15. Key points

- ADM iteration est normale.
- Elle peut être intra-phase, inter-phase, inter-domaines ou entre cycles.
- Iteration ≠ désordre.
- Requirements Management et governance maintiennent la cohérence.
- ADM iteration ≠ Agile sprint.

---

Original educational content aligned with TOGAF ADM iteration concepts.