# Practitioner — Gradient Scoring 5/3/1/0

## 1. Pourquoi le scoring est important

L’OGEA-102 ne fonctionne pas comme un QCM simple “vrai/faux”. Les quatre réponses sont graduées :

- meilleure réponse = 5 points ;
- deuxième meilleure = 3 points ;
- troisième = 1 point ;
- incorrecte = 0 point.

Tu ne vois pas les points pendant l’examen. Ton objectif reste de choisir **la meilleure réponse**.

## 2. Ce que cela change dans ton raisonnement

Deux options peuvent être raisonnables. La question n’est donc pas :

“Est-ce que cette réponse est possible ?”

mais :

“Est-ce que cette réponse est la plus appropriée dans ce contexte TOGAF ?”

## 3. Comment reconnaître une réponse 5 points

Elle a tendance à :

- traiter la cause principale ;
- respecter le moment ADM ;
- intégrer les stakeholders ;
- maintenir Requirements Management ;
- utiliser la gouvernance appropriée ;
- être proportionnée ;
- préserver la traçabilité ;
- éviter une décision prématurée.

## 4. Comment reconnaître une réponse 3 points

Elle est souvent correcte mais :

- incomplète ;
- moins bien séquencée ;
- trop locale ;
- moins explicite sur les stakeholders ;
- moins forte sur la gouvernance ;
- traite une conséquence plutôt que la cause.

## 5. Comment reconnaître une réponse 1 point

Elle contient parfois une idée utile, mais intervient :

- au mauvais moment ;
- avec une portée trop étroite ;
- avec un mécanisme TOGAF mal choisi ;
- avec une logique trop technique.

## 6. Réponse 0 point

Elle est hors sujet, contradictoire avec TOGAF ou dangereusement prématurée.

## 7. Exemple pédagogique

### Scénario

MayaBank veut moderniser ses paiements. Les stakeholders métier n’ont pas validé les outcomes, mais l’équipe technique propose déjà la target platform.

### A

Définir immédiatement Kubernetes, Kafka et le cloud provider.

→ probablement faible.

### B

Clarifier scope, stakeholders, concerns, business outcomes et Architecture Vision avant les choix détaillés.

→ meilleure réponse.

### C

Créer directement le Migration Plan.

→ très faible : trop tôt.

### D

Consulter le Repository pour voir les patterns existants.

→ utile, mais insuffisant comme première action.

La clé : D n’est pas “fausse”, mais B traite mieux le problème principal.

## 8. Exemple E/F/G

### Scénario

Les work packages sont connus mais ne sont pas priorisés.

- Identifier encore des gaps → possible mais probablement moins bon.
- Finaliser le séquencement et l’Implementation and Migration Plan → meilleur.
- Lancer une Compliance Review → trop tôt.
- Refaire Phase A → hors contexte.

## 9. Exemple stakeholder

Operations refuse une cible à cause du manque de supportability.

- rappeler l’approbation du sponsor → faible ;
- envoyer le document complet → partiellement utile ;
- comprendre le concern, mettre à jour les requirements et produire une vue adaptée → meilleur ;
- ignorer Operations → incorrect.

## 10. Règle pratique

Quand tu hésites entre deux options plausibles, demande :

**laquelle résout le mieux le problème principal tout en respectant le contexte, les stakeholders, les requirements et la gouvernance ?**

## 11. Ne cherche pas à “calculer” les points

Le score est une conséquence de la qualité des réponses.

Pendant l’examen :

1. classe mentalement les options ;
2. élimine la pire ;
3. compare les deux meilleures ;
4. choisis celle qui est la plus complète et la mieux séquencée.

## 12. English for Architects

> The gradient scoring model rewards the best contextual answer, not merely an answer that is technically possible.

---

Official exam scoring verified against The Open Group OGEA-102 exam plan. Examples are original.