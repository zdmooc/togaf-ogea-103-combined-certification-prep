# Introduction to Architecture Governance — Questions 241 à 262

## Q241 — Architecture Governance
Architecture Governance sert principalement à :
A. Organiser décisions, conformité, responsabilités et exceptions d'architecture
B. Écrire tout le code
C. Remplacer la stratégie métier
D. Supprimer les stakeholders
**Réponse : A.** La gouvernance rend les décisions explicites, appliquées et traçables. B/C/D sont faux.
**Mapping : Architecture Governance — Fundamentals.**

## Q242 — Governance vs project management
Quelle distinction est correcte ?
A. Elles sont synonymes
B. Architecture Governance veille à la conformité et aux décisions d'architecture ; Project Governance pilote notamment coûts/délais/risques projet
C. Architecture Governance pilote uniquement les coûts et délais du portefeuille
D. Project Governance définit seule la Target Architecture
**Réponse : B.** Les deux se coordonnent mais ont des objets différents.
**Distracteur C :** Coûts et délais sont des dimensions de pilotage de projet, pas la finalité propre de la gouvernance d'architecture.
**Mapping : Architecture Governance — Governance boundaries.**

## Q243 — Architecture Board
Le rôle principal d'un Architecture Board est :
A. Développer tout le code
B. Prioriser les activités quotidiennes de développement des squads
C. Arbitrer et gouverner les décisions d'architecture significatives
D. Remplacer toutes les équipes projet
**Réponse : C.** Le Board fournit un forum de décision et de conformité. A/B/D sont opérationnels ou excessifs.
**Distracteur B :** Le Board porte sur les grandes décisions et la conformité, non le management quotidien des équipes.
**Mapping : Architecture Governance — Architecture Board.**

## Q244 — Board decision
Quand un Architecture Board est-il particulièrement utile ?
A. Pour chaque correction orthographique
B. Pour toutes les tâches d'exploitation
C. Pour supprimer les requirements
D. Lorsqu'une décision transverse ou une exception importante nécessite arbitrage
**Réponse : D.** Le Board doit se concentrer sur les décisions architecturales significatives.
**Mapping : Architecture Governance — Architecture Board.**

## Q245 — Board composition
Un Architecture Board efficace doit idéalement :
A. Avoir l'autorité et la représentation nécessaires aux décisions qu'il porte
B. Être composé uniquement de développeurs d'un seul produit
C. Ne jamais inclure le métier
D. Ne disposer d'aucune règle de décision
**Réponse : A.** Sa composition dépend du scope mais doit rendre les arbitrages crédibles et exécutoires.
**Mapping : Architecture Governance — Architecture Board.**

## Q246 — Architecture Contract
Un Architecture Contract est principalement :
A. Un diagramme réseau
B. Un accord formalisant les responsabilités et attentes entre parties autour de l'architecture
C. Une Business Capability
D. Une Transition Architecture
**Réponse : B.** Il explicite les engagements de conformité et collaboration. A/C/D sont d'autres objets.
**Mapping : Architecture Governance — Architecture Contract.**

## Q247 — Contract in implementation
Pendant Phase G, l'Architecture Contract aide à :
A. Redéfinir la Business Architecture
B. Remplacer le code
C. Clarifier ce que les équipes d'implémentation doivent respecter et fournir comme preuves
D. Supprimer les reviews
**Réponse : C.** Le contrat soutient la gouvernance de mise en œuvre.
**Mapping : Architecture Governance — Architecture Contract.**

## Q248 — Contract vs Architecture Vision
Quelle différence est correcte ?
A. Ils sont identiques
B. Le Contract définit toujours la Target Data Architecture
C. La Vision est un waiver
D. La Vision aligne sur la direction cible ; le Contract formalise des engagements de gouvernance entre parties
**Réponse : D.** Les deux ont des finalités différentes.
**Mapping : Architecture Governance — Contract vs Vision.**

## Q249 — Compliance Review
Une Architecture Compliance Review sert à :
A. Comparer une implémentation ou solution aux requirements et décisions d'architecture approuvées
B. Créer le scope
C. Définir les business goals
D. Remplacer Phase E
**Réponse : A.** Elle vérifie l'alignement effectif.
**Mapping : Architecture Governance — Compliance.**

## Q250 — Compliance evidence
Quel élément est utile lors d'une Compliance Review ?
A. Uniquement le nom du projet
B. Requirements, decisions, architecture contracts et preuves d'implémentation
C. Un simple état d'avancement du planning projet
D. Uniquement les impressions du sponsor
**Réponse : B.** Une review doit être factuelle et traçable.
**Distracteur C :** Le respect du calendrier ne démontre pas la conformité architecturale.
**Mapping : Architecture Governance — Compliance.**

## Q251 — Non-compliance
Une review découvre un écart important. Quelle action est la plus cohérente ?
A. Le cacher
B. Déclarer automatiquement l'architecture invalide sans analyse
C. Enregistrer l'écart, évaluer son impact et décider correction ou exception via governance
D. Supprimer le requirement localement
**Réponse : C.** La gouvernance traite explicitement les écarts.
**Mapping : Architecture Governance — Compliance/Exception.**

## Q252 — Deviation
Une deviation est :
A. Une phase ADM
B. Un stakeholder
C. Un building block
D. Un écart par rapport à une architecture, standard ou requirement approuvé
**Réponse : D.** Elle décrit la non-conformité constatée.
**Mapping : Architecture Governance — Deviations.**

## Q253 — Exception
Une exception/waiver est :
A. Une autorisation gouvernée de déroger à une règle sous conditions
B. Toute erreur non détectée
C. Une Target Architecture
D. Un business goal
**Réponse : A.** Une exception est explicitement décidée, documentée et souvent limitée.
**Mapping : Architecture Governance — Exceptions.**

## Q254 — Exception conditions
Une bonne exception doit idéalement préciser :
A. Seulement « approuvé »
B. Rationale, scope, risques, owner, durée/conditions et actions futures
C. Aucun responsable
D. Aucune date de revue
**Réponse : B.** Une exception gouvernée doit être traçable et contrôlable.
**Mapping : Architecture Governance — Exceptions.**

## Q255 — Temporary waiver
Pourquoi une exception temporaire peut-elle être préférable à modifier immédiatement le standard ?
A. Parce que les standards ne changent jamais
B. Pour éviter toute analyse
C. Parce qu'un cas local ne justifie pas forcément de changer une règle globale
D. Pour supprimer la gouvernance
**Réponse : C.** Le waiver permet de gérer un cas particulier sans généraliser trop vite.
**Mapping : Architecture Governance — Exceptions.**

## Q256 — Governance log
Pourquoi tenir un Governance Log ?
A. Pour stocker uniquement le code
B. Pour remplacer le Repository
C. Pour supprimer les audits
D. Pour tracer décisions, reviews, exceptions et responsabilités
**Réponse : D.** Le log fournit une mémoire de gouvernance.
**Mapping : Architecture Governance — Governance Log.**

## Q257 — Escalation
Une équipe ne peut résoudre un conflit architectural local. Que faire ?
A. Escalader selon le modèle de governance prévu
B. Décider secrètement
C. Ignorer le conflit
D. Supprimer le stakeholder concerné
**Réponse : A.** L'escalation vers l'autorité appropriée protège cohérence et traçabilité.
**Mapping : Architecture Governance — Escalation.**

## Q258 — Governance principles
Pourquoi des principles approuvés sont-ils importants pour la governance ?
A. Ils remplacent tous les requirements
B. Ils fournissent des critères durables pour guider et arbitrer les décisions
C. Ils éliminent le besoin de jugement
D. Ils ne servent qu'en Preliminary
**Réponse : B.** Les principles soutiennent les décisions tout au long du cycle.
**Mapping : Architecture Governance — Principles.**

## Q259 — Governance in G
Quelle phase est la plus directement associée à la governance de l'implémentation ?
A. B
B. C
C. G
D. F
**Réponse : C.** Phase G = Implementation Governance.
**Mapping : Architecture Governance — Phase G.**

## Q260 — Governance and H
En Phase H, la governance sert notamment à :
A. Déployer sans analyse
B. Ignorer les drivers
C. Supprimer le Board
D. Décider comment répondre aux changements et s'il faut un nouveau cycle
**Réponse : D.** H gouverne l'évolution de l'architecture.
**Mapping : Architecture Governance — Phase H.**

## Q261 — Best governance behavior
Quel comportement est le plus mature ?
A. Rendre les écarts visibles et les traiter selon un processus de décision connu
B. Tolérer des exceptions implicites
C. Modifier les standards sans trace
D. Éviter les compliance reviews
**Réponse : A.** La gouvernance repose sur visibilité, décision et traçabilité.
**Mapping : Architecture Governance — Synthesis.**

## Q262 — Governance synthesis
Quel enchaînement est le plus cohérent ?
A. Exception → aucun requirement → déploiement
B. Principles/requirements → Architecture Contract → implementation → Compliance Review → correction ou exception
C. Compliance Review avant toute architecture
D. Board → suppression de tout delivery
**Réponse : B.** Il relie règles, engagement, implémentation, contrôle et traitement des écarts.
**Mapping : Architecture Governance — Synthesis.**

---
Questions originales de préparation.