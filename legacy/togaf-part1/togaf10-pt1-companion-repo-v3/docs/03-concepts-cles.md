# Concepts clés

## 1. Enterprise Architecture

L’architecture d’entreprise sert à organiser la transformation d’une entreprise en gardant une cohérence entre :

- stratégie ;
- capacités métier ;
- organisation ;
- applications ;
- données ;
- technologies.

## 2. Stakeholders

Les parties prenantes sont centrales.
Une architecture n’existe pas dans le vide.
Elle doit répondre à des attentes concrètes :

- sponsor ;
- métier ;
- sécurité ;
- exploitation ;
- delivery ;
- conformité ;
- finance.

## 3. Exigences

Les exigences traversent toute la démarche.
Une bonne architecture ne part pas d’une solution déjà choisie.
Elle part de besoins, contraintes, risques et objectifs explicites.

## 4. Baseline / Target / Transition

### Baseline
L’existant, tel qu’il fonctionne aujourd’hui.

### Target
La cible recherchée.

### Transition
L’état intermédiaire utile pour passer de l’existant à la cible sans tout casser.

## 5. Principes d’architecture

Les principes servent à guider les décisions.
Ils réduisent l’arbitraire.

Exemples :
- sécurité par défaut ;
- réutilisation avant développement spécifique ;
- observabilité native ;
- API d’abord.

## 6. Value of Architecture

La valeur de l’architecture ne se résume pas à produire des documents.
Elle aide à :

- aligner ;
- arbitrer ;
- rationaliser ;
- prioriser ;
- réduire les incohérences ;
- préparer les trajectoires.

## 7. Building Blocks

Les building blocks sont des éléments réutilisables ou structurants.
Ils servent à composer une architecture plus grande.

## 8. Deliverables, Artifacts, Building Blocks

C’est une confusion classique.

### Deliverable
Produit de travail formel remis à une partie prenante.

### Artifact
Contenu architectural plus fin : catalogue, matrice, diagramme, liste, etc.

### Building Block
Élément réutilisable ou composant structurant d’une solution ou d’une capacité.

## Erreurs fréquentes

- confondre document final et contenu interne ;
- croire qu’une architecture vaut par sa beauté documentaire ;
- oublier le rôle des parties prenantes ;
- ignorer les états de transition.

## Exemples terrain

### Migration VM -> conteneurs
- Baseline : applications sur VM
- Target : plateforme conteneurisée
- Transition : coexistence VM + Kubernetes

### IAM / SSO
- Principe : centraliser l’authentification
- Exigence : respecter les contraintes de sécurité
- Stakeholders : sécurité, utilisateurs, ops, architecture
