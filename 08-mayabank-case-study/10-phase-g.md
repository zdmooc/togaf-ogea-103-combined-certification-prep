# MayaBank — Phase G: Implementation Governance

## 1. Objective

Phase G gouverne l’implémentation de l’architecture approuvée. MayaBank ne demande plus seulement « quelle cible ? » ou « dans quel ordre ? », mais :

**les solutions livrées respectent-elles l’architecture, les requirements et les décisions approuvées ?**

## 2. Governance setup

MayaBank met en place :

- Architecture Contract entre gouvernance et delivery ;
- Architecture Compliance Reviews ;
- checkpoints par wave ;
- registre des deviations ;
- processus d’exception/waiver ;
- suivi des architecture requirements ;
- preuves de conformité automatisées lorsque possible.

## 3. Architecture Contract

Le contrat précise notamment :

- responsabilités ;
- constraints ;
- standards obligatoires ;
- deliverables attendus ;
- evidence requirements ;
- règles d’escalade ;
- modalités d’exception.

Le contrat n’est pas nécessairement un contrat juridique : il formalise les engagements d’architecture.

## 4. Compliance checkpoints

Exemples de points de contrôle :

### Design checkpoint

- boundaries applicatives conformes ;
- APIs/events compatibles avec standards ;
- requirements de sécurité intégrées ;
- data ownership respecté.

### Build checkpoint

- configuration et policies conformes ;
- telemetry présente ;
- secrets correctement gérés ;
- tests automatisés exécutés.

### Pre-production checkpoint

- SLO validés ;
- runbooks ;
- disaster recovery ;
- audit evidence ;
- exceptions ouvertes connues.

## 5. Typical deviation example

Une équipe souhaite utiliser un datastore non standard pour atteindre une latence spécifique.

La gouvernance ne doit ni :

- accepter automatiquement ;
- refuser automatiquement.

Elle doit :

1. documenter le besoin ;
2. vérifier le requirement ;
3. analyser impact/risque ;
4. évaluer alternatives ;
5. décider exception ou correction ;
6. tracer la décision et sa durée.

## 6. Architecture Compliance Review

La review compare l’implémentation à :

- Target Architecture ;
- principles ;
- Architecture Requirements Specification ;
- standards ;
- Architecture Contract ;
- décisions enregistrées.

## 7. Governance evidence

MayaBank automatise progressivement :

- policy checks ;
- security scans ;
- configuration validation ;
- API linting ;
- deployment evidence ;
- traceability links.

L’automatisation soutient la gouvernance ; elle ne remplace pas les décisions humaines.

## 8. Handling exceptions

Une exception doit contenir :

- justification ;
- scope ;
- owner ;
- risque ;
- mesures compensatoires ;
- date d’expiration ou de révision ;
- décision d’autorité appropriée.

## 9. Role of Architecture Board

Le Board intervient surtout sur :

- écarts structurants ;
- conflits de principes ;
- risques majeurs ;
- exceptions à fort impact ;
- décisions inter-domaines.

Il ne doit pas micro-manager chaque commit de code.

## 10. Phase G outputs

- conformité surveillée ;
- exceptions documentées ;
- actions correctives ;
- architecture contract appliqué ;
- décisions de gouvernance traçables ;
- implementation governance evidence.

## 11. G vs H

**G** gouverne l’implémentation en cours.

**H** surveille l’architecture après ou pendant son usage pour décider si de nouveaux changements nécessitent adaptation ou nouveau cycle ADM.

## 12. Practitioner trap

Si le problème est « l’équipe implémente une solution différente de la cible approuvée », le sujet principal est **Phase G / architecture compliance**, pas Phase H.

## 13. English for Architects

> In Phase G, MayaBank governs implementation through architecture contracts, compliance reviews, evidence, and controlled exception management.

---

Original educational case study; MayaBank is fictional.