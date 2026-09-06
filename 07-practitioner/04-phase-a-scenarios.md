# Practitioner — Phase A Scenarios

## 1. Ce que Phase A exige au niveau Practitioner

En Practitioner, Phase A n’est pas seulement “produire une Architecture Vision”. Il faut savoir reconnaître quand le problème principal concerne :

- le scope ;
- les stakeholders ;
- les business drivers ;
- la valeur attendue ;
- les risques initiaux ;
- les assumptions ;
- le Statement of Architecture Work ;
- la définition de haut niveau de la Baseline et de la Target ;
- l’accord pour poursuivre le cycle ADM.

## 2. Signal typique : solution trop tôt

### Scénario

MayaBank veut moderniser les paiements. Le CTO propose déjà OpenShift, Kafka et API Management. Le sponsor métier n’a pas encore défini les outcomes mesurables.

### Analyse

Le problème principal est en Phase A : la vision et la valeur doivent être clarifiées avant de figer la solution.

### Meilleure action

Définir les stakeholders, concerns, scope, drivers, outcomes et Architecture Vision ; formaliser le travail dans le Statement of Architecture Work.

## 3. Signal typique : scope flou

Un programme “modernisation data” mélange six pays, trois lignes métier et plusieurs obligations réglementaires sans frontières claires.

La meilleure action est de clarifier le scope : breadth, depth, time period et architecture domains concernés, puis d’adapter le travail.

## 4. Signal typique : sponsor sans vision partagée

Le sponsor finance le programme mais les équipes métier ne comprennent pas la transformation.

Réponse Practitioner : construire une Architecture Vision communicable, reliée aux business goals et concerns, et obtenir un engagement approprié.

## 5. Signal typique : Phase A vs Preliminary

### Cas Preliminary

Aucune Architecture Board, aucun principe, aucune règle de gouvernance.

### Cas Phase A

La capability existe, mais un nouveau programme doit être cadré.

Le Practitioner doit distinguer **préparer la capacité** de **lancer un engagement d’architecture**.

## 6. Signal typique : trop de détail

Une équipe veut modéliser en Phase A tous les flux applicatifs détaillés.

C’est souvent disproportionné. Phase A travaille à un niveau suffisamment haut pour aligner, cadrer et obtenir l’autorisation de poursuivre.

## 7. Signal typique : valeur non démontrée

Si le comité questionne “pourquoi investir ?”, la réponse n’est pas nécessairement plus de diagrammes techniques.

Il faut reconnecter :

**drivers → goals → expected outcomes → value → scope → Architecture Vision**.

## 8. Signal typique : risque critique découvert tôt

Un risque réglementaire peut modifier le scope ou rendre la vision non viable.

Il doit être traité comme input majeur de Phase A, alimenter Requirements Management et influencer les décisions.

## 9. Scénario MayaBank — choix 5/3/1/0 pédagogique

### Situation

MayaBank veut lancer un paiement instantané paneuropéen. Le sponsor est défini, mais le scope géographique et les obligations locales ne sont pas stabilisés.

### Option A

Choisir immédiatement la solution technique standard du groupe.

→ faible : trop tôt.

### Option B

Clarifier scope, stakeholders locaux, contraintes et outcomes, puis finaliser Architecture Vision et Statement of Architecture Work.

→ meilleure.

### Option C

Produire directement le Migration Plan.

→ incorrect : beaucoup trop tôt.

### Option D

Lancer une Compliance Review d’implémentation.

→ hors contexte.

## 10. Indices lexicaux

Les mots suivants doivent déclencher le réflexe Phase A :

- vision ;
- scope ;
- sponsor ;
- value ;
- drivers ;
- goals ;
- approval to proceed ;
- Statement of Architecture Work ;
- high-level baseline/target.

## 11. Ce que Phase A ne fait pas

- elle ne développe pas en détail les architectures B/C/D ;
- elle ne produit pas le séquencement de migration de Phase F ;
- elle ne réalise pas la gouvernance d’implémentation de Phase G ;
- elle ne remplace pas Requirements Management.

## 12. Questions d’élimination

Élimine souvent une option si elle :

- choisit une technologie sans vision ;
- produit une roadmap détaillée avant d’identifier la cible ;
- traite un problème de capability comme un simple problème Phase A ;
- ignore les stakeholders clés ;
- transforme la vision en architecture détaillée exhaustive.

## 13. English for Architects

> In Phase A, I establish the scope, stakeholders, business drivers, expected value, and a high-level target vision before detailed domain architecture begins.

---

Original educational scenarios based on the current Practitioner syllabus.