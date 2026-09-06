# ADM Iteration

## 1. Pourquoi l’ADM est itératif

L’**Architecture Development Method (ADM)** est représenté comme une séquence de phases, mais il ne doit pas être appliqué comme un cycle rigide et linéaire.

TOGAF prévoit l’**iteration** parce que l’architecture se développe progressivement : de nouvelles informations apparaissent, les stakeholders réagissent, les contraintes changent et certains domaines nécessitent plusieurs passages.

L’itération permet donc d’adapter la méthode à la réalité de l’entreprise.

## 2. Linéaire ne veut pas dire séquentiel rigide

Le schéma :

```text
Preliminary → A → B → C → D → E → F → G → H
```

est essentiel pour comprendre la logique générale.

Mais dans un engagement réel, on peut :

- revenir vers une phase précédente ;
- approfondir certains domaines plusieurs fois ;
- travailler en parallèle ;
- réutiliser des résultats existants ;
- exécuter un ADM ciblé sur une partie du périmètre ;
- utiliser plusieurs cycles à différents niveaux de l’entreprise.

## 3. Quatre idées d’itération

### 3.1 Iteration between ADM cycles

Une transformation peut nécessiter plusieurs cycles complets ou partiels.

Exemple :

Cycle 1 : modernisation du paiement instantané.

Cycle 2 : extension aux paiements internationaux.

Cycle 3 : évolution réglementaire.

### 3.2 Iteration between phases

Une phase peut révéler une information obligeant à revenir en arrière.

Exemple : Phase D révèle qu’une exigence de disponibilité rend la Target Application Architecture irréaliste. L’équipe peut revenir sur certains choix de Phase C.

### 3.3 Iteration within a phase

Une phase peut être répétée plusieurs fois à mesure que la compréhension progresse.

Exemple Phase B :

1. capability map high-level ;
2. ateliers métier ;
3. target refinement ;
4. gap validation.

### 3.4 Iteration across architecture domains

Business, Data, Application et Technology sont interdépendants.

Un changement Data peut affecter Application ; une contrainte Technology peut obliger à revoir Application ; une nouvelle capability métier peut obliger à revoir les trois autres domaines.

## 4. Pourquoi l’itération n’est pas un échec

Revenir sur un choix ne signifie pas que la méthode a échoué. C’est souvent la conséquence normale de l’apprentissage architectural.

Un mauvais comportement serait de maintenir artificiellement une décision simplement parce qu’une phase est “terminée”.

Le bon objectif est la cohérence, pas la conformité bureaucratique à un ordre figé.

## 5. Iteration vs Tailoring

### Iteration

Répéter ou revisiter des travaux pour améliorer ou ajuster l’architecture.

### Tailoring

Adapter la méthode, les livrables, les techniques, la gouvernance et le niveau de détail au contexte.

Les deux concepts sont liés mais différents.

Exemple :

- tailoring : décider que Phase B utilisera seulement capability mapping et value streams ;
- iteration : revenir sur la capability map après découverte d’une nouvelle contrainte réglementaire.

## 6. Iteration vs Partitioning

**Partitioning** découpe l’Enterprise Architecture en périmètres gérables.

Une grande entreprise peut avoir :

- Enterprise-level architecture ;
- domain architectures ;
- segment architectures ;
- capability architectures ;
- solution-level architecture work.

Ces travaux peuvent utiliser des ADM cycles différents mais coordonnés.

## 7. Iteration et levels of architecture

Un cycle de niveau stratégique peut rester très high-level.

Un cycle lié à une transformation particulière peut approfondir les mêmes concepts.

Exemple :

### Enterprise level

Objectif : moderniser les paiements.

### Domain level

Définir architecture cible Payments.

### Capability level

Approfondir Real-Time Payment Processing.

### Solution level

Concevoir précisément le Payment Orchestrator et sa plateforme.

Le niveau de détail dépend du purpose et du scope.

## 8. Requirements Management et iteration

Requirements Management est le moteur naturel de nombreuses itérations.

Exemple :

```text
Phase B identifies requirement R1
↓
Phase C refines R1
↓
Phase D discovers constraint C1
↓
R1 must be changed
↓
Return to affected architecture work
```

## 9. Stakeholder feedback

Les stakeholders peuvent provoquer une itération lorsque :

- la Target ne répond pas à leurs concerns ;
- de nouveaux stakeholders sont découverts ;
- un impact organisationnel a été sous-estimé ;
- une contrainte n’était pas visible auparavant.

Une bonne architecture se construit par validation progressive.

## 10. MayaBank — exemple

### Passage 1

Phase C Application propose un Payment Orchestrator unique.

### Phase D

L’analyse de résilience révèle que certains flux réglementaires exigent un mode dégradé autonome.

### Itération

Retour vers Application Architecture pour introduire une stratégie de fallback et réduire certaines dépendances.

### Résultat

La Target Application Architecture est améliorée avant Phase E.

L’itération évite d’attendre Phase G pour découvrir le problème.

## 11. Autre exemple — Data ↔ Application

La Data Architecture définit un canonical payment model.

L’équipe Application constate que deux systèmes externes ne peuvent pas adopter immédiatement ce modèle.

Itération :

- revoir mappings ;
- définir Anti-Corruption Layer / adapters ;
- mettre à jour transition requirements.

## 12. Quand arrêter d’itérer

L’objectif n’est pas la perfection infinie.

On arrête un niveau d’itération lorsque :

- le niveau de confiance est suffisant ;
- les concerns critiques sont couverts ;
- les risques majeurs sont compris ;
- les decisions nécessaires peuvent être prises ;
- le niveau de détail est adapté au purpose ;
- continuer n’apporte plus une valeur proportionnée.

## 13. Risques de sur-itération

- analysis paralysis ;
- retard des décisions ;
- documentation excessive ;
- perte d’orientation business ;
- confusion entre architecture et design détaillé.

TOGAF doit être configuré pour permettre des décisions, pas empêcher le delivery.

## 14. Agile et iteration

L’itération rend TOGAF compatible avec des modes de delivery progressifs.

On peut :

- maintenir une vision et une target architecture ;
- livrer par increments ;
- utiliser des Transition Architectures ;
- intégrer feedback ;
- gouverner la conformité sans imposer un Big Design Up Front exhaustif.

Le détail sera approfondi dans `04-applying-the-adm/07-agile-and-togaf.md`.

## 15. Pièges OGEA-103

### Piège 1

L’ADM n’est pas obligatoirement exécuté une seule fois de Preliminary à H.

### Piège 2

Iteration ≠ désordre.

L’itération reste gouvernée, motivée et traçable.

### Piège 3

Tailoring ≠ iteration.

### Piège 4

Toutes les phases n’ont pas besoin du même niveau de détail.

## 16. Foundation questions

### Q1
Pourquoi l’ADM est-il itératif ?

A. parce que les phases sont facultatives  
B. parce que l’architecture se développe progressivement et peut nécessiter des révisions  
C. uniquement pour réduire le nombre de documents  
D. parce que Requirements Management remplace les phases

**Réponse : B.**

### Q2
Quelle affirmation est correcte ?

A. une fois Phase C terminée, elle ne peut jamais être revisitée  
B. l’ADM doit toujours avoir le même niveau de détail  
C. on peut itérer entre domaines et phases selon le contexte  
D. iteration signifie abandonner la gouvernance

**Réponse : C.**

## 17. Practitioner scenario

Pendant Phase D, une contrainte d’infrastructure rend impossible une partie de la Target Application Architecture. Quelle est la meilleure approche ?

Ne pas continuer mécaniquement vers Phase E. Il est préférable d’itérer vers Phase C, réévaluer la Target Application Architecture, mettre à jour les requirements puis reprendre le flux ADM.

## 18. English for Architects

> The ADM is iterative. We can revisit earlier architecture work when new information, constraints or stakeholder concerns emerge.

### Speak it

1. We revisited the application architecture after identifying a technology constraint.
2. The ADM is structured but not rigid.
3. We iterate until we have enough confidence to make the next decision.

## 19. Interview question

**Question:** Is the TOGAF ADM a waterfall process?

**Answer:**

No. The ADM provides a structured progression, but it is explicitly iterative and can be tailored. I can iterate within phases, between phases, across architecture domains, and between ADM cycles depending on the context.

## 20. Key points

- ADM structuré mais non rigide ;
- iteration within/between phases and cycles ;
- domains interdépendants ;
- Requirements Management favorise l’itération ;
- iteration ≠ tailoring ;
- iteration ≠ absence de gouvernance ;
- niveau de détail adapté au purpose.

---

Official baseline: The Open Group TOGAF Standard, 10th Edition — Fundamental Content / Architecture Development Method and Applying the ADM. Original educational explanation.