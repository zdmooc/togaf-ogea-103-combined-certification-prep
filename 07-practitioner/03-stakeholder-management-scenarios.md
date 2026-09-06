# Practitioner — Stakeholder Management Scenarios

## 1. Pourquoi ce sujet est différent en Practitioner

En Foundation, tu dois connaître Stakeholder, Concern, Viewpoint et View.

En Practitioner, tu dois déterminer :

- quels stakeholders comptent réellement dans le scénario ;
- quel concern est bloquant ;
- quel type d’engagement est approprié ;
- quelle vue ou quel message permet la décision ;
- comment transformer les concerns en requirements.

La règle centrale :

**un problème de stakeholder ne se résout pas automatiquement par plus de documentation.**

## 2. Pattern 1 — Stakeholder oublié

### Scénario

MayaBank a validé une nouvelle architecture de paiement avec le sponsor métier et le CTO. Quelques semaines plus tard, Operations bloque la mise en production car le modèle de support n’a jamais été discuté.

### Analyse

Operations est un stakeholder critique dont les concerns n’ont pas été couverts.

### Meilleure action

Réengager Operations, comprendre les concerns de supportability/resilience, mettre à jour les requirements et produire les vues nécessaires.

### Mauvaise réponse typique

“Rappeler que le sponsor a déjà approuvé l’architecture.”

L’approbation ne supprime pas les concerns non traités.

## 3. Pattern 2 — Sponsor dominant

Un sponsor pousse une date très agressive, tandis que le CISO exige des contrôles supplémentaires.

La meilleure réponse n’est ni d’ignorer le CISO ni de bloquer automatiquement le programme. Il faut rendre les concerns explicites, traduire les impacts en exigences/risques et organiser une décision gouvernée.

## 4. Pattern 3 — Trop de stakeholders

Une équipe invite 40 personnes à chaque atelier, sans distinction d’influence ni de concern.

La bonne approche consiste à segmenter l’engagement selon :

- pouvoir ;
- intérêt ;
- concern ;
- décision attendue ;
- niveau de détail nécessaire.

## 5. Pattern 4 — Concern vague

Stakeholder : “Je veux que ce soit robuste.”

L’architecte ne doit pas conserver cette phrase telle quelle comme exigence.

Il faut la qualifier :

- disponibilité ;
- RTO ;
- RPO ;
- capacité ;
- tolérance aux pannes ;
- observabilité ;
- reprise.

## 6. Pattern 5 — Vue inadaptée

Le comité exécutif reçoit un diagramme de 150 composants Kubernetes.

Le problème n’est pas que le diagramme soit faux. Il ne répond pas au concern du stakeholder.

Une meilleure vue doit montrer par exemple : valeur, risques, trajectoire, coûts ou impacts métier.

## 7. Pattern 6 — Stakeholder conflict

Finance veut réduire le coût. Operations veut maximiser la résilience. Le métier veut accélérer le time-to-market.

Le Practitioner doit reconnaître qu’il s’agit d’un arbitrage, pas d’une simple optimisation technique.

Approche :

1. expliciter les concerns ;
2. relier aux drivers et requirements ;
3. montrer les compromis ;
4. utiliser la gouvernance appropriée pour décider.

## 8. Pattern 7 — Stakeholder change

Un nouveau régulateur ou un nouveau partenaire critique apparaît en Phase F.

Stakeholder Management n’est pas terminé après Phase A.

Il faut mettre à jour la stakeholder map, les concerns, les requirements et potentiellement la roadmap.

## 9. Pattern 8 — Communication vs décision

Un architecte envoie une présentation à un stakeholder et considère le sujet “traité”.

L’engagement réel demande parfois :

- validation ;
- arbitrage ;
- engagement ;
- accord formel ;
- décision ;
- feedback.

Communiquer n’est pas forcément obtenir une décision.

## 10. Matrice Practitioner

| Signal dans le scénario | Réflexe |
|---|---|
| acteur ignoré | identifier stakeholder + concern |
| conflit d’intérêts | arbitrage gouverné |
| incompréhension | adapter la view |
| concern vague | dériver des requirements |
| stakeholder nouveau | mettre à jour l’engagement |
| mauvais niveau de détail | changer viewpoint/view |

## 11. Mini-scenario A

Le CISO refuse une cible car il n’a aucune visibilité sur les trust boundaries.

**Meilleure réponse :** produire/adapter une vue de sécurité répondant à son concern et réconcilier les requirements.

**Réponse moyenne :** lui transmettre l’Architecture Definition Document complet.

Pourquoi moyenne ? Le document peut contenir l’information, mais il ne cible pas forcément le concern.

## 12. Mini-scenario B

Le sponsor réclame une décision immédiate alors que deux stakeholders clés n’ont pas été consultés.

La meilleure réponse est d’éviter une validation artificielle et d’obtenir suffisamment de perspectives pour que la décision soit solide.

## 13. Mini-scenario C

Les équipes locales d’un groupe bancaire refusent une architecture globale parce qu’elle ignore des obligations pays.

La réponse TOGAF est d’intégrer ces stakeholders/constraints dans le modèle fédéré, pas simplement d’imposer le standard central.

## 14. Questions d’élimination

Élimine souvent une option si elle :

- suppose qu’un seul sponsor représente tous les stakeholders ;
- remplace un concern par une solution ;
- traite la communication comme un acte unique ;
- propose le même artifact à tous ;
- ignore la gouvernance d’un conflit.

## 15. English for Architects

> I do not treat stakeholder management as a one-time activity. I revisit stakeholders and concerns whenever the architecture context changes.

> When concerns conflict, I make the trade-offs explicit and bring the decision to the appropriate governance level.

---

Original educational scenarios. No official exam questions are reproduced.