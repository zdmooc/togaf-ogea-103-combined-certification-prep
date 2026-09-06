# 01 — Enterprise Architecture

## 1. Definition

L’**Enterprise Architecture (EA)** est une discipline qui aide une entreprise à comprendre sa situation actuelle, définir une situation cible et organiser une transformation cohérente entre stratégie, métier, information, applications et technologie.

Une architecture d’entreprise n’est donc pas un simple schéma technique. Elle répond à une question beaucoup plus large : **comment faire évoluer l’entreprise sans perdre la cohérence entre ce qu’elle veut accomplir et les moyens qu’elle utilise pour y parvenir ?**

Dans TOGAF, le mot *Enterprise* ne signifie pas nécessairement « très grande entreprise ». Il désigne le périmètre que l’on choisit d’architecturer. Ce périmètre peut être une organisation entière, un groupe, une division, un domaine métier, une plateforme ou une transformation transverse.

## 2. Why Enterprise Architecture exists

Sans architecture, les décisions sont souvent prises localement :

- un projet sélectionne une technologie pour résoudre son propre problème ;
- une équipe métier crée un nouveau processus sans regarder les dépendances ;
- une application duplique une donnée déjà détenue ailleurs ;
- une plateforme ajoute un produit sans vérifier les standards ;
- plusieurs transformations poursuivent des objectifs contradictoires.

Chaque décision peut sembler raisonnable isolément, mais l’ensemble devient coûteux, fragile et difficile à faire évoluer.

L’Enterprise Architecture cherche à créer une **cohérence globale**. Elle permet notamment de relier :

**Business Drivers → Goals → Capabilities → Requirements → Architecture → Roadmap → Implementation → Change**

Cette chaîne est fondamentale. Un bon architecte ne commence pas par « quel produit devons-nous acheter ? ». Il cherche d’abord à comprendre le besoin, le contexte, les contraintes et la capacité à construire.

## 3. Architecture is about decisions

Une architecture est utile lorsqu’elle aide à prendre de meilleures décisions.

Exemples :

- devons-nous conserver une application, la remplacer ou la moderniser ?
- devons-nous créer une capacité mutualisée ou plusieurs solutions locales ?
- faut-il centraliser l’identité ?
- peut-on migrer directement vers la cible ou faut-il une **Transition Architecture** ?
- quelles dépendances doivent être traitées avant une migration ?
- quelles décisions doivent être standardisées à l’échelle de l’entreprise ?

Le travail d’architecture produit des modèles et des documents, mais leur valeur vient des décisions qu’ils rendent possibles.

## 4. Architecture vs design vs implementation

Ces notions sont liées mais différentes.

| Notion | Question dominante | Exemple |
|---|---|---|
| Enterprise Architecture | Où voulons-nous aller et comment maintenir la cohérence globale ? | définir une cible d’entreprise pour les paiements |
| Solution Architecture | Comment une solution répond-elle à un besoin dans ce cadre ? | architecture d’un nouveau Payment Hub |
| Technical Architecture | Comment les composants techniques sont-ils structurés ? | OpenShift, Kafka, réseau, IAM, observabilité |
| Design | Comment réaliser concrètement un composant ? | topologie Kafka, schéma d’API, sizing |
| Implementation | Comment construire/configurer/déployer ? | manifests Kubernetes, code, pipelines |

TOGAF est centré sur l’Enterprise Architecture, mais il peut soutenir des travaux à plusieurs niveaux d’architecture.

## 5. Architecture as Baseline, Target and Transition

Une transformation peut être comprise avec trois concepts très importants.

### Baseline Architecture

La **Baseline Architecture** décrit l’état de départ pertinent : ce qui existe actuellement.

Exemple MayaBank :

- paiements traités par plusieurs applications historiques ;
- intégrations point-à-point ;
- fichiers batch ;
- bases Oracle séparées ;
- exploitation fortement manuelle.

### Target Architecture

La **Target Architecture** décrit l’état futur recherché.

Exemple :

- services de paiement découplés ;
- APIs standardisées ;
- événements Kafka ;
- déploiement OpenShift ;
- observabilité commune ;
- politique IAM transverse.

### Transition Architecture

Une **Transition Architecture** est un état intermédiaire nécessaire ou utile entre la Baseline et la Target.

Exemple : pendant 18 mois, MayaBank doit conserver l’ancien moteur de paiement tout en introduisant une couche API et un nouveau bus événementiel. Cet état transitoire est une architecture à part entière : il possède des composants, des interfaces, des risques et des règles propres.

### Exam trap

**Transition Architecture ≠ simple planning.**

C’est un état architectural intermédiaire, pas seulement une date dans une roadmap.

## 6. Enterprise transformation and coherence

Une transformation sérieuse concerne plusieurs dimensions en même temps.

Prenons une migration vers OpenShift.

Une approche purement technique pourrait dire : « déplacer les applications sur Kubernetes ».

Une approche Enterprise Architecture demandera aussi :

- quelles capacités métier sont concernées ?
- quels services doivent rester disponibles pendant la migration ?
- quelles données sont critiques ?
- quels contrats d’interface existent ?
- quelles contraintes réglementaires s’appliquent ?
- quelles équipes exploitent la cible ?
- quelle gouvernance contrôle les écarts ?
- quelle trajectoire réduit le risque ?

C’est cette vision multi-domaine qui distingue un simple projet de plateforme d’un travail d’architecture d’entreprise.

## 7. Stakeholders and concerns

Une architecture existe pour répondre à des **Concerns** portées par des **Stakeholders**.

Exemple : une nouvelle plateforme de paiement n’est pas jugée de la même façon par tous.

| Stakeholder | Concern possible |
|---|---|
| Direction | valeur, délai, risque |
| Métier paiement | fonctionnalité, continuité |
| RSSI | sécurité, conformité |
| Exploitation | observabilité, résilience, support |
| Finance | coût, investissement |
| Architectes | cohérence, standards, évolutivité |
| Développeurs | utilisabilité de la plateforme |

Une architecture qui ignore une préoccupation majeure peut être techniquement élégante et néanmoins échouer.

## 8. Value of Enterprise Architecture

L’EA peut créer de la valeur de plusieurs façons :

- améliorer l’alignement entre stratégie et delivery ;
- rendre visibles les dépendances ;
- réduire les duplications ;
- faciliter la réutilisation ;
- clarifier la trajectoire de transformation ;
- rendre les arbitrages explicites ;
- mieux gérer les risques ;
- renforcer la gouvernance ;
- préparer des transformations complexes.

Attention : « produire plus de documentation » n’est pas un objectif en soi.

## 9. What Enterprise Architecture is not

### Not only documentation

Un dossier d’architecture peut être un **Deliverable**, mais l’EA n’est pas le document.

### Not only technology

L’EA couvre aussi Business Architecture, Data Architecture et Application Architecture.

### Not project management

L’architecture et le projet coopèrent mais ne répondent pas aux mêmes questions. La gouvernance d’architecture vérifie la conformité avec l’intention architecturale ; le pilotage projet gère délai, budget, ressources et delivery.

### Not a fixed future blueprint

Une Target Architecture peut évoluer lorsque les besoins ou contraintes changent. TOGAF comprend explicitement l’Architecture Change Management.

## 10. MayaBank example

MayaBank veut moderniser son traitement des paiements européens.

Le problème n’est pas : « devons-nous utiliser Kafka ? »

Le véritable problème est :

- comment améliorer le time-to-market ;
- comment supporter de nouveaux schémas de paiement ;
- comment réduire la dépendance au legacy ;
- comment garantir disponibilité et conformité ;
- comment faire évoluer l’organisation et les plateformes sans interruption majeure.

L’Enterprise Architecture va progressivement traduire ces objectifs en architectures, gaps, work packages et roadmap.

## 11. Common mistakes

1. Commencer directement par une solution technique.
2. Décrire la Target sans comprendre la Baseline.
3. Confondre architecture et inventaire applicatif.
4. Oublier les stakeholders.
5. Produire des diagrammes sans décisions associées.
6. Traiter une transformation comme un seul saut Baseline → Target alors qu’une transition est nécessaire.
7. Ignorer la gouvernance après la conception.

## 12. OGEA-103 exam traps

Pour Foundation, retiens surtout :

- Enterprise Architecture cherche la cohérence de transformation ;
- l’architecture ne se limite pas à la technologie ;
- Baseline = état actuel pertinent ;
- Target = état futur recherché ;
- Transition Architecture = état intermédiaire architectural ;
- stakeholders et concerns sont essentiels.

Pour Practitioner, une bonne réponse est rarement « choisir immédiatement la meilleure technologie ». Il faut d’abord reconnaître le contexte, les stakeholders, la phase ADM et les exigences.

## 13. Foundation questions

### Q1
Pourquoi l’Enterprise Architecture ne doit-elle pas commencer par le choix d’un produit ?

**Réponse :** parce que les choix de solution doivent être reliés au contexte, aux objectifs, aux exigences et aux contraintes de l’entreprise.

### Q2
Quelle est la différence entre Baseline et Target Architecture ?

**Réponse :** la Baseline décrit l’état actuel pertinent ; la Target décrit l’état futur recherché.

### Q3
Une Transition Architecture est-elle un plan de migration ?

**Réponse :** non. C’est un état architectural intermédiaire. Le plan de migration organise les travaux permettant de progresser entre états.

## 14. English for Architects

Useful sentence:

> Enterprise Architecture aligns business goals, capabilities, applications, data and technology.

Meaning:

L’architecture d’entreprise aligne les objectifs métier, les capacités, les applications, les données et la technologie.

### Speak it

- The current architecture is our baseline.
- The target architecture describes the future state.
- We need a transition architecture to reduce migration risk.

## 15. Interview question

**Question:** What is Enterprise Architecture?

**Simple answer:**

Enterprise Architecture helps an organization align business goals with applications, data and technology. It describes the current state, the target state and the transformation path between them.

## 16. Key points to remember

**Enterprise Architecture = comprendre l’entreprise + décider d’une cible + organiser une transformation cohérente.**

Ne pense pas « diagrammes ». Pense :

**Drivers → Goals → Capabilities → Requirements → Baseline → Target → Gaps → Roadmap → Governance → Change**.
