# Views and Viewpoints

## 1. Définition

Un **Viewpoint** définit les conventions, règles et préoccupations utilisées pour construire une représentation de l’architecture.

Une **View** est la représentation concrète produite à partir d’un viewpoint pour répondre aux concerns de stakeholders déterminés.

La relation à mémoriser :

**Stakeholder → Concern → Viewpoint → View**.

## 2. Pourquoi cette distinction existe

Une architecture complexe ne peut pas être expliquée correctement dans une seule représentation.

Le sponsor, le CISO, les opérations et les équipes de delivery ne posent pas les mêmes questions.

Le viewpoint permet donc de définir **comment regarder** l’architecture ; la view montre **ce que l’on voit** dans un cas donné.

## 3. Exemple simple

Concern du CISO : « où circulent les données sensibles ? »

Viewpoint : règles permettant de montrer data flows, trust boundaries, controls et systèmes concernés.

View : représentation réelle de MayaBank construite selon ces règles.

## 4. Viewpoint réutilisable

Un viewpoint peut être réutilisé sur plusieurs architectures.

Exemple : un `Operational Resilience Viewpoint` peut spécifier que la représentation doit montrer :

- services critiques ;
- dépendances ;
- sites ;
- failover ;
- RTO/RPO ;
- monitoring.

Chaque programme crée ensuite sa propre **view**.

## 5. Relation avec Stakeholder Management

La bonne séquence n’est pas :

« j’ai ce diagramme, à qui puis-je l’envoyer ? »

mais :

1. qui est le stakeholder ?
2. quel est son concern ?
3. quel viewpoint convient ?
4. quelle view doit être produite ?

## 6. View vs Artifact

Une view est une représentation répondant à des concerns.

Un artifact est une unité de contenu architectural telle qu’un catalog, une matrix ou un diagram.

Une view peut s’appuyer sur un ou plusieurs artifacts.

## 7. Exemple MayaBank

### Sponsor View

Montre :

- objectifs ;
- capabilities ;
- value ;
- roadmap de haut niveau.

### Security View

Montre :

- flux sensibles ;
- IAM ;
- trust boundaries ;
- controls.

### Operations View

Montre :

- composants exécutables ;
- monitoring ;
- disponibilité ;
- dépendances runtime.

La Target Architecture est la même ; les views diffèrent.

## 8. Viewpoint vs Perspective

Dans les questions d’examen, rester attentif au vocabulaire officiel. Un viewpoint spécifie la manière de construire une view. Ne remplacer pas cette relation par des termes vagues comme « angle de vue » sans retenir la distinction formelle.

## 9. Pièges OGEA-103

- Viewpoint ≠ view.
- View ≠ stakeholder.
- Une view doit répondre à des concerns.
- Un même stakeholder peut avoir plusieurs concerns.
- Une architecture peut avoir plusieurs views cohérentes.

## 10. Foundation question

Quel concept définit les conventions de construction d’une représentation destinée à répondre à des concerns ?

A. Viewpoint
B. View
C. Deliverable
D. Work Package

**Réponse : A.**

## 11. Practitioner scenario

Le Board reçoit un diagramme réseau très détaillé pour décider du business value d’une transformation. La représentation est techniquement correcte mais mal adaptée au concern. La meilleure action est de sélectionner un viewpoint répondant au besoin de décision puis de produire la view correspondante.

## 12. English for Architects

> A viewpoint defines how a view is constructed; the view is the actual representation created for specific stakeholder concerns.

## 13. Key points

- Stakeholder → Concern → Viewpoint → View.
- Viewpoint = conventions.
- View = représentation concrète.
- Une view peut utiliser plusieurs artifacts.
- Choisir la représentation selon la décision à prendre.

---

Original educational explanation based on the TOGAF Standard, 10th Edition.