# Architecture Partitioning

## 1. Definition

L’**Architecture Partitioning** consiste à découper un paysage d’entreprise complexe en parties cohérentes afin de distribuer le travail et les responsabilités d’architecture sans perdre la cohérence globale.

Le but n’est pas de créer des silos. Il s’agit de définir des **boundaries** utiles : qui est responsable de quoi, quels éléments sont partagés, quelles dépendances traversent les partitions et quelles règles assurent l’alignement.

## 2. Pourquoi partitionner ?

Une grande entreprise peut contenir :

- plusieurs business units ;
- plusieurs pays ;
- plusieurs produits ;
- plusieurs plateformes ;
- des domaines de données ;
- des environnements réglementaires différents ;
- des équipes d’architecture distribuées.

Sans partitioning :

- le scope devient ingérable ;
- les responsabilités sont floues ;
- plusieurs équipes modélisent la même chose ;
- des standards contradictoires apparaissent ;
- les dépendances transverses sont oubliées.

## 3. Partitioning vs Levels of Architecture

**Levels of Architecture** répond à : à quel niveau de scope et de détail travaillons-nous ?

**Partitioning** répond à : comment découpons-nous l’espace architectural et distribuons-nous les responsabilités ?

Les deux sont complémentaires.

## 4. Critères possibles de partitioning

Une organisation peut partitionner par :

- business domain ;
- geography ;
- legal entity ;
- product ;
- capability ;
- data domain ;
- technology platform ;
- lifecycle ;
- security boundary.

Il n’existe pas une seule méthode universelle. Le choix doit refléter l’organisation et les dépendances réelles.

## 5. Good partition characteristics

Une partition utile doit avoir :

- une responsabilité claire ;
- un scope compréhensible ;
- des interfaces explicites ;
- des dépendances connues ;
- des standards communs lorsque nécessaire ;
- des mécanismes de gouvernance inter-partitions.

## 6. Shared concerns

Certaines capabilities traversent plusieurs partitions :

- IAM ;
- security ;
- observability ;
- API management ;
- event streaming ;
- data governance ;
- network ;
- cloud platform.

Ces éléments nécessitent souvent une architecture transverse ou des building blocks partagés.

## 7. Federation

Dans une grande organisation, l’architecture peut être **federated** : plusieurs équipes possèdent des responsabilités locales tout en respectant un cadre commun.

Exemple :

- Enterprise Architecture définit principles et standards ;
- Domain Architecture définit les cibles de domaine ;
- Platform Architecture fournit les shared services ;
- Solution Architecture applique et remonte les besoins de changement.

## 8. Governance des partitions

Il faut définir :

- ownership ;
- decision rights ;
- escalation ;
- standards communs ;
- exception process ;
- interfaces entre repositories ;
- dependency management.

Une partition sans governance devient rapidement un silo.

## 9. MayaBank

MayaBank organise son architecture en partitions :

### Business domains

- Payments ;
- Customer ;
- Risk ;
- Finance.

### Shared platforms

- OpenShift Platform ;
- API Platform ;
- Event Streaming ;
- Observability ;
- IAM.

### Cross-domain governance

Le domaine Payments est propriétaire de Payment Orchestration, mais il consomme les shared platform building blocks.

Cela évite que chaque domaine construise son propre Kafka, son propre IAM ou sa propre observability.

## 10. Partitioning et Repository

Le Architecture Repository doit permettre :

- de localiser les architectures par partition ;
- de référencer les shared building blocks ;
- de comprendre les dépendances ;
- de publier les standards transverses ;
- de retrouver les décisions et exceptions.

## 11. Partitioning et Requirements

Une requirement locale peut avoir un impact global.

Exemple : Payments demande un nouveau mode de chiffrement qui affecte le shared API platform.

La gouvernance doit déterminer si :

- la requirement reste locale ;
- le shared platform évolue ;
- une exception est accordée.

## 12. Erreurs fréquentes

- partitionner selon l’organigramme uniquement ;
- oublier les shared services ;
- dupliquer les plateformes ;
- créer des boundaries sans interfaces ;
- ne pas définir decision rights ;
- confondre autonomie et indépendance totale.

## 13. Pièges OGEA-103

- Partitioning aide à gérer la complexité.
- Il doit préserver la cohérence globale.
- Les partitions ont des interfaces et dépendances.
- Partitioning ≠ Levels of Architecture.
- Federation n’annule pas governance et standards communs.

## 14. Practitioner scenario

Trois business units créent chacune une plateforme d’événements différente avec des règles de sécurité incompatibles. La meilleure réponse est de revoir le partitioning et la governance : clarifier les responsabilités locales et identifier les building blocks transverses qui doivent être partagés ou standardisés.

## 15. English for Architects

> We partitioned the architecture by business domain while keeping shared platform capabilities under common governance.

## 16. Key points

- Partitioning = découpage des responsabilités architecturales.
- Il sert à gérer la complexité, pas à créer des silos.
- Les interfaces et dépendances entre partitions doivent être explicites.
- Les shared capabilities nécessitent souvent une governance transverse.
- Federation = autonomie encadrée par un cadre commun.

---

Original educational content aligned with TOGAF architecture partitioning concepts.