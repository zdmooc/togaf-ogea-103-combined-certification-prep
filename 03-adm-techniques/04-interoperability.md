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

## 4. Catégories TOGAF et grille d'analyse pratique

Le TOGAF Standard, 10th Edition (Introduction and Core Concepts, rubrique *Interoperability*) propose trois **catégories usuelles** d'interopérabilité :

| Catégorie | Question d'architecture | Exemple MayaBank |
|---|---|---|
| **Operational or Business Interoperability** | Comment les entités travaillent-elles ensemble au niveau des processus et responsabilités ? | Une banque émettrice et un service de compensation coordonnent le traitement d'une exception. |
| **Information Interoperability** | Comment les informations sont-elles partagées et comprises ? | Les deux parties interprètent correctement les données d'un message ISO 20022. |
| **Technical Interoperability** | Comment les ressources et services techniques échangent-ils et se connectent-ils ? | Des API, files de messages et contrôles de transport compatibles permettent l'échange. |

Ces catégories structurent la discussion, **sans affirmer que X2202 exige de mémoriser leur liste mot pour mot**. La grille plus détaillée ci-dessous est une déclinaison pédagogique de mise en œuvre et non une nouvelle liste normative TOGAF.

### Dimensions de travail supplémentaires (grille pédagogique)

**Attention certification :** la décomposition Business / Information / Application / Technology / Security ci-dessous est une **grille d'analyse pédagogique** pour les scénarios d'intégration, **pas** une liste normative de « cinq dimensions TOGAF » imposée par X2202. Le syllabus Foundation L1 4.7 demande de savoir **expliquer l'interopérabilité et son utilisation**. Il ne prescrit pas de réciter cinq catégories. Une différence de sémantique, d'organisation ou de confiance peut croiser plusieurs dimensions.

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

### Définir le degré d'interopérabilité

Il ne suffit pas de déclarer qu'un système est « interopérable ». L'architecte définit **la nature, la portée, la direction et le niveau d'automatisation** de chaque échange, de façon testable. Dans les lignes directrices TOGAF historiques, un **exemple** de modèle de degrés d'échange est :

| Degré illustratif | Nature de l'échange |
|---|---|
| 1 — *Unstructured Data Exchange* | Information non structurée, interprétée par une personne |
| 2 — *Structured Data Exchange* | Données structurées, avec étapes manuelles de réception ou de traitement |
| 3 — *Seamless Sharing of Data* | Partage automatisé selon un modèle d'échange commun |
| 4 — *Seamless Sharing of Information* | Exploitation cohérente de l'information par des applications coopérantes |

**Important :** ces degrés proviennent d'un exemple de classification cité dans des guides TOGAF antérieurs ; ce ne sont **pas quatre niveaux universels obligatoires** ni un learning outcome indépendant du syllabus X2202. Une entreprise doit spécifier et mesurer les degrés adaptés à son contexte.

**Exemple MayaBank :** échanger automatiquement un message ISO 20022 pain.001 ne prouve pas à lui seul l'interopérabilité métier. Il faut aligner les définitions et statuts, les rôles, les mécanismes de reprise et les contrôles de conformité. Documenter les couples émetteur/destinataire et les exigences par échange dans une matrice d'interopérabilité.

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
- On peut analyser business, information/data, application, technology et security comme **angles de diagnostic**, sans les présenter comme cinq catégories certifiées par X2202.
- Integration est plus étroit.
- Contrats et sémantique sont essentiels.
- Elle traverse plusieurs phases ADM.

---

Original educational content aligned with TOGAF concepts.