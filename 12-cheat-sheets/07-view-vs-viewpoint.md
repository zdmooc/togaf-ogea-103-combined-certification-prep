# Cheat Sheet — View vs Viewpoint

## La différence en une phrase

- **Viewpoint** = la convention / manière de construire une représentation pour répondre à certains concerns.
- **View** = la représentation concrète produite selon ce viewpoint.

## Chaîne mentale

```text
Stakeholder
   ↓
Concern
   ↓
Viewpoint
   ↓
View
```

## Exemple MayaBank

### Stakeholder
CISO

### Concern
Comment les flux de paiement sont-ils protégés et où sont les trust boundaries ?

### Viewpoint
Une manière structurée de représenter composants, flux, frontières de confiance et contrôles.

### View
Le diagramme concret de sécurité de la plateforme de paiement.

## Autre exemple

### Stakeholder
COO / Operations

### Concern
Comment la plateforme bascule-t-elle en cas de panne ?

### Viewpoint
Operational / resilience-oriented viewpoint.

### View
Le schéma réel de déploiement, redondance, monitoring et failover.

## Pièges Foundation

- Viewpoint ≠ diagramme final.
- View ≠ règle pour construire le diagramme.
- Un même stakeholder peut avoir plusieurs concerns.
- Plusieurs views peuvent être nécessaires pour répondre à différents concerns.

## Practitioner

Si un stakeholder important ne comprend pas ou refuse l’architecture, la bonne réponse n’est pas toujours « produire plus de documentation ».

Réflexe :

1. identifier le stakeholder ;
2. clarifier le concern ;
3. choisir le viewpoint approprié ;
4. produire/adapter la view nécessaire ;
5. obtenir la décision ou le feedback attendu.

## Mémo

> **Viewpoint = recipe. View = meal.**

La métaphore sert uniquement à mémoriser : le viewpoint définit comment construire ; la view est ce qui est produit.

## English

> A viewpoint defines how to construct a representation for specific concerns. A view is the actual representation produced for stakeholders.
