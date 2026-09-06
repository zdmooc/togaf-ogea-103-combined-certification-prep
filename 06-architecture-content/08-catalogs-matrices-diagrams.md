# Catalogs, Matrices and Diagrams

## 1. Trois familles d’artifacts

TOGAF utilise trois familles particulièrement utiles pour organiser les représentations d’architecture :

- **Catalogs** ;
- **Matrices** ;
- **Diagrams**.

L’enjeu n’est pas de mémoriser une liste infinie. Il faut comprendre **la question à laquelle chaque famille répond**.

## 2. Catalogs — « qu’est-ce qui existe ? »

Un catalog est une liste structurée d’éléments.

Exemples :

- Application Portfolio Catalog ;
- Technology Portfolio Catalog ;
- Data Entity/Data Component Catalog ;
- Principle Catalog ;
- Organization/Actor Catalog.

Utilité : inventaire, classification, ownership, cycle de vie, statut.

### MayaBank

`Application Portfolio Catalog` :

| Application | Owner | Criticality | Lifecycle |
|---|---|---|---|
| Payment Hub | Payments | High | Target |
| Legacy Gateway | Operations | High | Retire |
| Fraud Engine | Risk | High | Strategic |

## 3. Matrices — « quelle relation entre deux ensembles ? »

Une matrix montre de façon tabulaire les relations entre catégories d’éléments.

Exemples :

- Application/Organization Matrix ;
- Data Entity/Application Matrix ;
- Business Function/Application Matrix ;
- Role/Application Matrix.

### MayaBank

Question : quelles applications manipulent `Payment Instruction` ?

| Data Entity | Payment Hub | Fraud Engine | Reporting |
|---|---:|---:|---:|
| Payment Instruction | X | X | X |
| Customer Profile | X | X |  |
| Settlement Position | X |  | X |

La matrix révèle rapidement les dépendances.

## 4. Diagrams — « comment les éléments sont-ils organisés ou interagissent-ils ? »

Un diagram représente visuellement :

- structure ;
- interaction ;
- flux ;
- déploiement ;
- localisation ;
- séquence ;
- dépendances.

Exemples :

- Application Communication Diagram ;
- Processing Diagram ;
- Business Footprint Diagram ;
- Environments and Locations Diagram.

## 5. Même sujet, trois questions différentes

Sujet : applications de paiement.

### Catalog

Quelles applications existent ?

### Matrix

Quelles applications supportent quelles capabilities ou données ?

### Diagram

Comment ces applications communiquent-elles ?

La différence tient au **type de question**, pas seulement au format visuel.

## 6. Sélection par concern

| Concern | Artifact souvent utile |
|---|---|
| inventorier les applications | Catalog |
| identifier les dépendances Data/Application | Matrix |
| comprendre les flux runtime | Diagram |
| comparer responsabilités organisationnelles | Matrix |
| connaître cycle de vie technologique | Catalog |
| comprendre déploiement multi-site | Diagram |

## 7. Erreur fréquente : tout mettre dans un diagramme

Les équipes essaient parfois de faire un seul « mega-diagram ». Résultat :

- trop d’informations ;
- aucune audience claire ;
- aucune décision facilitée ;
- maintenance impossible.

Il vaut mieux plusieurs artifacts cohérents issus du même repository.

## 8. Relation avec le repository

Si les catalogs, matrices et diagrams reposent sur un même modèle structuré, une modification d’un élément peut être répercutée dans plusieurs views.

C’est beaucoup plus robuste que des images indépendantes sans source commune.

## 9. Pièges OGEA-103

- Catalog ≠ matrix.
- Matrix ≠ diagram.
- La matrix est particulièrement utile pour relations croisées.
- Le diagram est visuel mais pas forcément le meilleur artifact pour toute question.
- La sélection dépend du stakeholder concern.

## 10. Foundation questions

### Q1
Quel artifact convient le mieux pour inventorier un portefeuille d’applications ?

**Réponse : Catalog.**

### Q2
Quel artifact convient le mieux pour montrer quelles applications utilisent quelles données ?

**Réponse : Matrix.**

### Q3
Quel artifact convient le mieux pour montrer les communications entre applications ?

**Réponse : Diagram.**

## 11. Practitioner scenario

Le responsable Data veut identifier toutes les applications utilisant une entité classifiée « Restricted ». Une matrix Data Entity/Application est plus adaptée qu’un Technology Platform Diagram.

## 12. English for Architects

> Catalogs list architecture elements, matrices show relationships between sets of elements, and diagrams provide visual representations of structures and interactions.

## 13. Key points

- Catalog = liste.
- Matrix = relation croisée.
- Diagram = représentation visuelle.
- Toujours choisir selon la question et le concern.

---

Original educational explanation based on the TOGAF Standard, 10th Edition.