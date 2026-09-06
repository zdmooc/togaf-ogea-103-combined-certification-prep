# Interoperability

## 1. Definition

L’**Interoperability** décrit la capacité de systèmes, organisations ou composants à coopérer, échanger de l’information et utiliser cet échange de manière cohérente.

Dans une architecture d’entreprise, l’interopérabilité ne se réduit pas à « deux applications communiquent ». Elle concerne plusieurs dimensions :

- business ;
- information/data ;
- application/service ;
- technology ;
- semantic ;
- organizational ;
- security and governance.

## 2. Pourquoi cette technique existe

Les transformations échouent souvent aux frontières :

- deux équipes utilisent des définitions différentes ;
- deux applications échangent des formats incompatibles ;
- un protocole fonctionne mais la sémantique métier diverge ;
- l’IAM n’est pas fédéré ;
- les SLA ou responsabilités ne sont pas alignés ;
- une plateforme interne ne respecte pas les contraintes d’un partenaire externe.

L’interopérabilité force l’architecte à analyser ces frontières explicitement.

## 3. Interoperability vs Integration

**Integration** décrit souvent le mécanisme de connexion.

**Interoperability** est plus large : les parties doivent pouvoir fonctionner ensemble avec une compréhension et des règles compatibles.

Deux systèmes reliés par API peuvent être intégrés mais non réellement interopérables si les données ou comportements sont interprétés différemment.

## 4. Dimensions

### Business interoperability

Compatibilité des processus, responsabilités, services et accords métier.

### Information interoperability

Compatibilité des modèles de données, identifiants, formats, qualité, sémantique et règles de cycle de vie.

### Application interoperability

Compatibilité des services, APIs, events, contrats, versions et patterns d’interaction.

### Technology interoperability

Compatibilité des plateformes, protocoles, réseaux, middleware, runtimes et standards techniques.

### Security interoperability

Compatibilité IAM, authentification, autorisation, certificats, chiffrement, trust boundaries et audit.

## 5. Position dans l’ADM

L’interopérabilité peut être un concern dès Phase A, puis être détaillée dans :

- Phase B : processus et organisations ;
- Phase C Data : sémantique et échanges ;
- Phase C Application : interfaces et services ;
- Phase D : protocoles et plateformes ;
- Phase E/F : dépendances de migration ;
- Phase G : vérification de conformité des interfaces.

## 6. Méthode pratique

1. Identifier les frontières importantes.
2. Identifier les parties qui doivent coopérer.
3. Définir les informations/services échangés.
4. Vérifier la sémantique et les responsabilités.
5. Définir les standards et contrats.
6. Identifier les contraintes de sécurité.
7. Définir versioning, erreur, timeout et reprise.
8. Tester les scénarios de compatibilité.
9. Gouverner les changements de contrats.

## 7. Standards et building blocks

Un standard peut réduire le coût d’interopérabilité mais ne garantit pas automatiquement la compatibilité.

Exemples professionnels :

- ISO 20022 pour la messagerie paiement ;
- REST/OpenAPI pour contrats API ;
- events avec schéma gouverné ;
- OAuth/OIDC pour certains besoins IAM ;
- standards de logging/telemetry.

Le TOGAF exam teste surtout le raisonnement architectural, pas la mémorisation d’un produit spécifique.

## 8. Exemple MayaBank

MayaBank veut connecter plusieurs services de paiement à des partenaires externes.

### Problèmes Baseline

- formats propriétaires ;
- identifiants incohérents ;
- gestion d’erreur différente ;
- versions d’API non gouvernées ;
- observabilité fragmentée.

### Target

- modèle canonique aligné ISO 20022 ;
- contrats API versionnés ;
- event schemas gouvernés ;
- identité et secrets contrôlés ;
- correlation IDs communs ;
- règles de timeout/retry explicites.

La cible ne traite pas seulement la connectivité réseau : elle rend l’écosystème interopérable.

## 9. Interoperability et Requirements

Exemples d’exigences :

- les interfaces doivent respecter un contrat versionné ;
- les données critiques doivent conserver la même signification de bout en bout ;
- les erreurs doivent être corrélables ;
- les services doivent supporter une politique de compatibilité descendante définie.

## 10. Risks

Risques fréquents :

- coupling excessif ;
- divergence de schéma ;
- incompatibilité de versions ;
- changement partenaire non coordonné ;
- perte de sémantique ;
- défaut de propagation d’identité ;
- cascading failures.

## 11. Pièges OGEA-103

- Interoperability ≠ simple réseau.
- Standardisation aide mais ne remplace pas l’analyse métier et sémantique.
- Une API seule ne garantit pas l’interopérabilité.
- Le sujet traverse plusieurs domaines ADM.

## 12. Foundation questions

### Q1
Quel énoncé décrit le mieux l’interopérabilité ?

A. La capacité de composants à fonctionner ensemble de manière cohérente  
B. Le choix d’un fournisseur unique  
C. Une phase ADM  
D. Une Architecture Contract

**Réponse : A.**

## 13. Practitioner scenario

Deux banques exposent des APIs conformes au même protocole, mais interprètent différemment le statut d’un paiement. La meilleure réponse est d’analyser et gouverner la **sémantique et les contrats**, pas seulement la connectivité technique.

## 14. English for Architects

> Interoperability is not only about connectivity; the systems must also share compatible contracts, semantics, security rules and operating expectations.

## 15. Key points

- Interoperability traite les frontières.
- Elle couvre business, data, application, technology et security.
- Integration est plus étroit.
- Contrats et sémantique sont essentiels.
- Elle traverse plusieurs phases ADM.

---

Original educational content aligned with TOGAF concepts.