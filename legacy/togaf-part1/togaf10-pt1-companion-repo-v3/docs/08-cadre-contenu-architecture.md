# Cadre de contenu de l’architecture

## Pourquoi cette partie est importante

C’est souvent là que les candidats mélangent les niveaux.

## Le cadre de contenu aide à structurer

- ce qu’on produit ;
- sous quelle forme ;
- pour qui ;
- avec quel niveau de détail.

## 1. Deliverables

Les deliverables sont des livrables formels.
Ils sont destinés à être remis, validés, partagés ou utilisés dans une gouvernance donnée.

Exemples :
- dossier de vision ;
- roadmap ;
- dossier d’architecture ;
- assessment formel.

## 2. Artifacts

Les artefacts sont les éléments plus fins utilisés pour décrire l’architecture.

Exemples :
- catalogues ;
- matrices ;
- diagrammes ;
- listes de composants ;
- vues de dépendances.

## 3. Building Blocks

Les building blocks sont des briques réutilisables ou structurantes.

Exemples :
- service IAM commun ;
- pattern d’exposition API ;
- socle observabilité ;
- plateforme Kubernetes standardisée.

## 4. Relation entre les trois

Un deliverable peut contenir plusieurs artefacts.
Ces artefacts peuvent décrire ou mobiliser des building blocks.

## Exemples simples

### Cas 1 — dossier de migration
- Deliverable : dossier d’architecture de migration
- Artifacts : matrice applications/environnements, diagramme cible, liste des dépendances
- Building blocks : cluster standard, IAM central, monitoring standard

### Cas 2 — trajectoire SSO
- Deliverable : note de cadrage SSO
- Artifacts : cartographie des applications, matrice des rôles, diagramme de flux
- Building blocks : IdP, reverse proxy, connecteurs OIDC

## Erreurs fréquentes

- appeler “deliverable” n’importe quel petit schéma ;
- confondre contenu et contenant ;
- oublier la notion de réutilisabilité dans les building blocks.
