# Practitioner — Requirements Management Scenarios

## 1. Pourquoi Requirements Management est central

Requirements Management n’est pas une phase terminale. Il fonctionne à travers tout le cycle ADM.

Au niveau Practitioner, il faut savoir reconnaître quand le problème principal concerne :

- une requirement nouvelle ;
- une requirement contradictoire ;
- une requirement devenue obsolète ;
- une requirement mal formulée ;
- un manque de traçabilité ;
- un changement qui impacte plusieurs phases.

## 2. Le flux mental

**Concern → Requirement → Architecture decision → Traceability → Validation → Change**

Une requirement peut apparaître, être affinée, être remplacée ou provoquer une modification d’architecture.

## 3. Pattern : requirement vague

### Scénario

Le sponsor dit : “la plateforme doit être très rapide”.

Ce n’est pas encore une requirement exploitable.

Il faut clarifier les critères mesurables : latence, débit, disponibilité, temps de traitement, charge cible, etc.

## 4. Pattern : requirements conflictuelles

Finance exige une réduction forte du coût alors que Operations exige une duplication multi-site complète.

Le Practitioner ne doit pas choisir arbitrairement.

La bonne approche :

1. rendre les requirements explicites ;
2. identifier les stakeholders ;
3. analyser les impacts et trade-offs ;
4. utiliser la gouvernance pour arbitrer ;
5. conserver la décision et la traçabilité.

## 5. Pattern : requirement découverte en Phase D

Une contrainte de souveraineté impose que certaines données restent dans une juridiction donnée.

Il faut :

- enregistrer/mettre à jour la requirement ;
- analyser l’impact sur Data et Technology Architecture ;
- ajuster la cible si nécessaire ;
- conserver la traçabilité.

Il ne faut pas simplement “patcher” le diagramme technique.

## 6. Pattern : requirement change en Phase F

Le métier exige soudain un lancement six mois plus tôt.

Cette nouvelle requirement peut modifier :

- priorities ;
- work packages ;
- Transition Architectures ;
- risk ;
- Migration Plan.

Elle doit être traitée comme un changement d’exigence avec analyse d’impact.

## 7. Pattern : requirement après implémentation

Une nouvelle obligation réglementaire apparaît après mise en production.

Requirements Management capture l’exigence ; Phase H aide à décider si elle nécessite un nouveau cycle d’architecture.

## 8. Requirement vs Constraint

Une **requirement** exprime ce qui doit être satisfait.

Une **constraint** limite les options disponibles.

Exemple :

- Requirement : paiements critiques disponibles 24/7.
- Constraint : certaines données ne peuvent pas sortir de l’UE.

Les deux influencent la solution, mais ne sont pas identiques.

## 9. Requirement vs Principle

Un principle guide de nombreuses décisions sur la durée.

Une requirement est liée à un besoin spécifique et vérifiable.

Exemple :

- Principle : API-first.
- Requirement : le service X doit exposer une API REST versionnée avant la date Y.

## 10. Traçabilité

Une bonne architecture peut montrer :

**Business goal → Requirement → Architecture element → Work Package → Implementation evidence**.

Sans cette chaîne, il devient difficile d’expliquer pourquoi une décision existe.

## 11. Scénario MayaBank

### Situation

Le CISO exige chiffrement bout-en-bout. L’équipe delivery propose un compromis pour respecter le délai.

### Mauvaise réponse

Changer l’architecture sans mettre à jour l’exigence ni la gouvernance.

### Meilleure réponse

Identifier l’exigence de sécurité, analyser l’impact du compromis, documenter le risque, soumettre l’écart à la gouvernance et maintenir la traçabilité de la décision.

## 12. Pièges Practitioner

- Requirement ≠ solution.
- Concern ≠ requirement formalisée.
- Requirement change ≠ simple modification documentaire.
- Requirements Management ≠ uniquement Phase A.
- Une nouvelle requirement peut renvoyer vers une phase précédente.
- Les requirements doivent rester cohérentes avec stakeholders, architecture et governance.

## 13. Question d’élimination

Si une option :

- ignore une requirement nouvelle ;
- modifie la solution sans analyse d’impact ;
- supprime une requirement parce qu’elle est difficile ;
- ne conserve aucune trace de l’arbitrage ;

elle est rarement la meilleure réponse TOGAF.

## 14. English for Architects

> Requirements Management is continuous. When a requirement changes, I assess the impact on the architecture, update the relevant artifacts, and maintain traceability to the decision.

---

Original educational scenarios based on the TOGAF Practitioner syllabus.