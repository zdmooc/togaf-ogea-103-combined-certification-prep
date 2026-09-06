# Practitioner — How to Eliminate Answers

## 1. Pourquoi l’élimination est essentielle

Dans un scénario Practitioner, plusieurs réponses peuvent contenir des éléments corrects. L’objectif est de supprimer d’abord les réponses manifestement moins adaptées, puis de comparer les deux meilleures.

## 2. Filtre 1 — Mauvaise phase

Si la réponse intervient au mauvais moment de l’ADM, elle perd fortement en qualité.

Exemple : produire un Migration Plan alors que la Target Architecture n’est pas encore définie.

## 3. Filtre 2 — Solution prématurée

Une option qui choisit immédiatement un produit ou une technologie peut être séduisante mais prématurée si le besoin, la cible ou les requirements ne sont pas assez définis.

## 4. Filtre 3 — Mauvais problème

Un scénario stakeholder ne se résout pas forcément par un nouveau diagramme technique.

Un problème de governance ne se résout pas forcément par une nouvelle architecture.

Un problème de migration ne se résout pas forcément par une nouvelle requirement.

## 5. Filtre 4 — Ignore les stakeholders

Une option qui contourne un stakeholder critique, surtout quand son concern est explicitement décrit, est souvent faible.

## 6. Filtre 5 — Ignore Requirements Management

Si un changement d’exigence a un impact sur l’architecture, une réponse qui modifie directement la solution sans analyse d’impact ni traçabilité est généralement moins bonne.

## 7. Filtre 6 — Ignore governance

Si le problème implique :

- déviation ;
- conformité ;
- exception ;
- arbitrage ;

une réponse purement technique est rarement suffisante.

## 8. Filtre 7 — Réponse absolue

Méfie-toi des formulations telles que :

- toujours ;
- jamais ;
- obligatoirement tout refaire ;
- ignorer le contexte ;
- appliquer la même profondeur partout.

TOGAF est tailorable et contextuel.

## 9. Filtre 8 — Trop de documentation

“Produire davantage de documents” n’est pas automatiquement la bonne action.

Le bon artifact doit répondre à un concern ou soutenir une décision.

## 10. Filtre 9 — Confusion de concepts

Élimine une réponse qui confond :

- ABB et SBB ;
- View et Viewpoint ;
- Repository et Continuum ;
- Roadmap et Migration Plan ;
- Transition Architecture et work package ;
- Phase G et H.

## 11. Filtre 10 — Architecture vs Project Management

TOGAF interagit avec programme/project management mais ne le remplace pas.

Une réponse qui demande à l’architecte de gérer directement budget, staffing et sprint planning sans lien architectural peut être hors scope.

## 12. Méthode en 30 secondes

Pour chaque option :

1. est-elle dans la bonne phase ?
2. traite-t-elle la cause principale ?
3. respecte-t-elle les stakeholders ?
4. respecte-t-elle les requirements ?
5. utilise-t-elle la gouvernance appropriée ?
6. est-elle proportionnée ?

Si trois réponses survivent, compare leur complétude et leur séquence.

## 13. Exemple MayaBank

### Situation

Une implémentation dévie d’une décision approuvée.

### Option A

Ignorer l’écart car le projet respecte sa date.

→ éliminer.

### Option B

Refaire entièrement Phase A.

→ généralement disproportionné.

### Option C

Effectuer une Compliance Review, analyser l’écart et utiliser le processus de gouvernance approprié.

→ meilleure réponse probable.

### Option D

Mettre à jour uniquement le diagramme.

→ incomplet.

## 14. Comparer les deux meilleures

Quand deux réponses restent, choisis celle qui :

- est plus directement reliée au problème ;
- est mieux séquencée ;
- maintient plus de traçabilité ;
- utilise le mécanisme TOGAF le plus approprié ;
- évite les actions inutiles.

## 15. English for Architects

> I eliminate answers that are premature, out of sequence, weak on stakeholder engagement, or inconsistent with requirements and governance.

---

Original exam-preparation method. No official exam questions are reproduced.