# Security When Applying the ADM

## 1. Core principle

La **security** doit être intégrée à l’architecture de manière transverse. Elle ne doit pas être ajoutée à la fin comme une revue séparée.

Le raisonnement est :

**Business risk → security concern → security requirement → architecture controls → implementation evidence → governance**.

La sécurité influence Business, Data, Application et Technology Architectures, ainsi que Requirements Management, Risk Management et Implementation Governance.

## 2. Pourquoi la sécurité est transverse

Un problème de sécurité peut venir de :

- l’organisation ;
- un processus ;
- une donnée ;
- un service applicatif ;
- une identité ;
- un secret ;
- un réseau ;
- une plateforme ;
- une dépendance fournisseur ;
- une opération de migration ;
- une mauvaise gouvernance.

Limiter la sécurité à Phase D serait donc une erreur.

## 3. Security dans Preliminary

La capacité d’architecture doit définir :

- les rôles sécurité ;
- les standards ;
- la relation avec risk/compliance ;
- les autorités d’acceptation du risque ;
- les exigences de documentation ;
- les processus d’exception.

## 4. Security dans Phase A

Identifier :

- security stakeholders ;
- major concerns ;
- regulatory constraints ;
- initial risks ;
- high-level security principles ;
- critical assets.

Exemple MayaBank :

Concern : compromission d’un paiement ou accès non autorisé.

Conséquences :

- identity requirements ;
- segregation of duties ;
- auditability ;
- encryption ;
- fraud controls.

## 5. Security dans Phase B

Questions métier :

- qui peut initier un paiement ?
- qui peut l’approuver ?
- quelles responsabilités doivent être séparées ?
- quels processus sont sensibles ?
- quels acteurs externes sont impliqués ?

La sécurité métier précède souvent les contrôles techniques.

## 6. Security dans Phase C Data

Analyser :

- classification ;
- ownership ;
- confidentiality ;
- integrity ;
- retention ;
- lineage ;
- privacy ;
- access rights ;
- encryption needs.

## 7. Security dans Phase C Application

Analyser :

- authentication ;
- authorization ;
- service identity ;
- API security ;
- input validation ;
- audit trail ;
- session/token handling ;
- application trust boundaries.

## 8. Security dans Phase D

Analyser les technology capabilities nécessaires :

- IAM ;
- PKI/certificates ;
- secrets management ;
- network segmentation ;
- encryption services ;
- security monitoring ;
- vulnerability management ;
- hardened runtimes ;
- backup and recovery ;
- supply-chain controls.

Phase D choisit les capabilities et technologies nécessaires, mais les requirements viennent de préoccupations et risques définis plus tôt.

## 9. Security dans Phase E/F

La migration peut introduire des états temporaires plus risqués.

Exemples :

- coexistence legacy/target ;
- double exposition d’API ;
- réplication temporaire de données ;
- nouveaux accès privilégiés ;
- période de double-run.

Les Transition Architectures doivent donc inclure les contrôles de sécurité nécessaires.

## 10. Security dans Phase G

Implementation Governance vérifie :

- conformité aux requirements ;
- evidence de sécurité ;
- résultats de tests ;
- déviations ;
- risk acceptance ;
- respect des Architecture Contracts et standards.

## 11. Security dans Phase H

Les menaces évoluent.

Triggers possibles :

- nouvelle vulnérabilité ;
- nouveau règlement ;
- changement fournisseur ;
- nouvelle attaque ;
- changement de classification des données.

Phase H peut conduire à un changement mineur ou à un nouveau cycle ADM.

## 12. Security vs Risk

Security est un domaine de concerns et controls.

Risk Management est la discipline qui traite l’incertitude et les impacts de manière plus générale.

Un risque sécurité doit être analysé comme un risque d’entreprise, avec owner, response et residual risk.

## 13. Security Principles vs Security Requirements

Principle : règle directrice stable.

Exemple : **Least Privilege**.

Requirement : contrainte concrète pour un engagement.

Exemple : « les comptes de service du Payment Orchestrator ne doivent avoir accès qu’aux secrets et APIs nécessaires à leur namespace et rôle ».

## 14. Zero Trust — extension professionnelle

Zero Trust peut être utilisé comme direction de sécurité, mais ne doit pas devenir un slogan.

Questions :

- quelle identité ?
- quelle ressource ?
- quel contexte ?
- quel niveau de confiance ?
- quelle politique ?
- quelle evidence ?

## 15. MayaBank

### Business concern

Empêcher les transactions frauduleuses et protéger les données de paiement.

### Requirements

- strong service identity ;
- least privilege ;
- encryption in transit/at rest ;
- immutable audit trail ;
- secret rotation ;
- segregation of duties ;
- monitored privileged access.

### Technology capabilities

- centralized IAM ;
- secrets management ;
- mTLS where required ;
- SIEM/security telemetry ;
- network policy ;
- image scanning ;
- policy-as-code.

### Governance evidence

- threat model ;
- access matrix ;
- test results ;
- compliance evidence ;
- approved exceptions.

## 16. Erreurs fréquentes

- traiter sécurité uniquement en D ;
- confondre tool et control objective ;
- ne pas relier control à risk/requirement ;
- accepter implicitement une exception ;
- oublier les états de transition ;
- ne pas demander d’evidence en G.

## 17. Pièges OGEA-103

- Security est cross-cutting.
- Risk and Security doivent être intégrés dans l’ADM.
- Les security requirements peuvent influencer tous les domaines.
- Une réponse Practitioner qui implique tôt les stakeholders et requirements sécurité est généralement meilleure qu’une revue tardive.

## 18. English for Architects

> Security is a cross-cutting concern. We derive security requirements from business risks and verify the controls throughout the ADM.

### Speak it

1. Security is not only a technology concern.
2. We integrated security requirements from Phase A onward.
3. Implementation governance verifies the security evidence.

## 19. Key points

- Security traverse l’ADM.
- Business risk → security requirement → control → evidence.
- Security ≠ uniquement Phase D.
- Les Transition Architectures ont aussi besoin de controls.
- Phase G vérifie la conformité et les déviations.

---

The Open Group provides a Series Guide on integrating Risk and Security within a TOGAF Enterprise Architecture. This chapter is an original educational explanation.