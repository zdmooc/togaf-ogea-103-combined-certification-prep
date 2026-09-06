# Exceptions and Deviations

## 1. Définition

Une **deviation** est un écart entre l’implémentation proposée ou réalisée et l’architecture, les principes, standards ou exigences approuvés.

Une **exception / waiver** est une décision de gouvernance qui autorise explicitement un écart dans des conditions déterminées.

L’idée essentielle est : **deviation constatée ≠ exception automatiquement acceptée**.

## 2. Pourquoi gérer les exceptions

Une architecture trop rigide peut bloquer le delivery. Une architecture sans contrôle des exceptions se désagrège.

Le bon modèle permet donc :

- de détecter les écarts ;
- de comprendre leur justification ;
- d’évaluer leur risque ;
- de décider explicitement ;
- de limiter leur durée ou leur portée ;
- de suivre une remédiation lorsque nécessaire.

## 3. Cycle de décision

**Detect → Analyze → Assess Risk → Decide → Record → Monitor → Remediate / Close**.

## 4. Informations nécessaires

Une demande d’exception devrait préciser :

- règle ou exigence concernée ;
- justification ;
- alternatives étudiées ;
- impacts ;
- risques ;
- propriétaire du risque ;
- durée ;
- périmètre ;
- plan de remédiation éventuel.

## 5. Exception permanente ou temporaire

Une exception temporaire peut être acceptable si elle contient :

- une date d’expiration ;
- des conditions de contrôle ;
- une trajectoire de retour à la conformité.

Une exception permanente peut indiquer soit un cas réellement particulier, soit un standard devenu inadapté. Plusieurs exceptions identiques doivent pousser à réexaminer le standard lui-même.

## 6. Relation avec Phase H

Des déviations répétées ou l’évolution du contexte peuvent signaler que la Target Architecture doit être réévaluée en Phase H.

## 7. Exemple MayaBank

Un composant legacy ne peut pas encore utiliser l’authentification cible. Une exception est accordée pour six mois avec :

- isolation réseau ;
- monitoring renforcé ;
- owner nommé ;
- date de migration ;
- revue mensuelle.

Ce n’est pas une « dette invisible » : c’est une dette gouvernée.

## 8. Pièges OGEA-103

- Exception ≠ ignorance d’un standard.
- Exception ≠ non-conformité cachée.
- Une bonne exception est explicite, justifiée, tracée et contrôlée.
- Des exceptions répétées peuvent déclencher une réévaluation de l’architecture.

## 9. Foundation question

Une équipe doit déroger temporairement à un standard. Quelle est la meilleure approche ?

A. Ignorer le standard
B. Obtenir une exception gouvernée avec justification et suivi
C. Modifier silencieusement la Target Architecture
D. Supprimer le standard

**Réponse : B.**

## 10. English for Architects

> An architecture exception should be explicit, risk-assessed, time-bounded when possible, and traceable.

## 11. Key points

- Deviation = écart observé.
- Exception = écart explicitement autorisé.
- Risk ownership et evidence sont essentiels.
- L’exception doit rester gouvernée dans le temps.

---

Original educational explanation based on the TOGAF Standard, 10th Edition.