# Architecture Board

## 1. Définition

L’**Architecture Board** est un mécanisme de gouvernance chargé de superviser les décisions d’architecture importantes, de promouvoir la cohérence, de traiter les arbitrages et de soutenir la conformité à l’architecture approuvée.

Il ne faut pas l’imaginer comme « le groupe qui dessine l’architecture ». Son rôle est surtout de **gouverner** : examiner, décider, arbitrer, escalader et suivre.

## 2. Pourquoi un Architecture Board ?

Dans une grande organisation, les décisions traversent plusieurs équipes, domaines et programmes. Sans instance commune :

- les standards divergent ;
- les exceptions se multiplient ;
- les dépendances restent locales ;
- les projets optimisent leur périmètre au détriment de l’entreprise ;
- les décisions deviennent incohérentes.

Le Board crée un point de cohérence.

## 3. Responsabilités typiques

Selon l’organisation, il peut :

- approuver des principes et standards ;
- revoir des architectures significatives ;
- arbitrer des conflits ;
- examiner des exceptions ;
- suivre des Architecture Compliance Reviews ;
- contrôler la cohérence avec la Target Architecture ;
- sponsoriser des actions de remédiation ;
- maintenir certains éléments de governance.

## 4. Ce que le Board ne doit pas devenir

Un Board inefficace devient :

- un goulot d’étranglement ;
- une réunion de validation formelle sans analyse ;
- une instance trop technique ;
- une instance trop éloignée du métier ;
- un lieu où toutes les décisions, même mineures, sont centralisées.

Le niveau de décision doit être proportionné à l’impact.

## 5. Composition

La composition dépend du scope. On peut y trouver :

- Enterprise Architecture ;
- Business Architecture ;
- Data / Application / Technology Architecture ;
- Security ;
- Operations ;
- Risk / Compliance ;
- représentants métier ;
- portfolio / transformation ;
- parfois finance ou procurement.

Le Board doit réunir les compétences et autorités nécessaires pour décider réellement.

## 6. Board vs Architecture Team

| Architecture Board | Architecture Team |
|---|---|
| gouverne | conçoit / analyse |
| approuve / arbitre | produit recommandations et artifacts |
| traite exceptions | développe Baseline/Target/Gaps |
| porte une autorité de décision | apporte expertise et options |

Le même individu peut parfois participer aux deux, mais les responsabilités restent différentes.

## 7. Relation avec Preliminary

Preliminary est le moment naturel pour définir :

- mandat du Board ;
- composition ;
- responsabilités ;
- critères d’escalade ;
- fréquence ;
- interfaces avec d’autres instances ;
- types de décisions à soumettre.

## 8. Relation avec Phase G

En Phase G, le Board peut être mobilisé pour :

- conformité ;
- déviations ;
- changements significatifs ;
- arbitrages entre delivery et Target Architecture.

## 9. Exemple MayaBank

Le programme Payments décide d’utiliser un composant propriétaire qui déroge à un standard groupe.

Le Board doit répondre à des questions comme :

1. l’écart est-il justifié ?
2. existe-t-il une alternative conforme ?
3. quel risque introduit-on ?
4. l’exception est-elle temporaire ?
5. qui accepte le risque ?
6. quelle remédiation est requise ?

## 10. Pièges OGEA-103

- Architecture Board ≠ équipe projet.
- Architecture Board ≠ tous les architectes.
- Le Board ne remplace pas le sponsor.
- Le Board ne doit pas approuver chaque détail technique.
- Son rôle principal est governance, pas production d’architecture.

## 11. Foundation question

**Quelle fonction correspond le mieux à une Architecture Board ?**

A. Développer tout le code
B. Superviser et gouverner les décisions d’architecture
C. Gérer uniquement le budget
D. Administrer la base de données

**Réponse : B.**

## 12. Practitioner scenario

Deux programmes proposent des solutions incompatibles pour une capability partagée. Les deux sont viables localement. La meilleure réponse est d’escalader l’arbitrage au niveau de gouvernance approprié, avec analyse des impacts enterprise, plutôt que de laisser chaque programme optimiser son propre périmètre.

## 13. English for Architects

> The Architecture Board provides governance, resolves architecture conflicts, and reviews significant deviations.

## 14. Key points

- Board = governance authority.
- Preliminary définit son fonctionnement.
- Phase G l’utilise fortement pour conformité et déviations.
- Il doit rester proportionné et éviter la bureaucratie.

---

Original educational explanation based on the TOGAF Standard, 10th Edition.