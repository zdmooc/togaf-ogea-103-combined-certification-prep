# Introduction to Architecture Governance — Questions 241 à 262

## Q241 — Architecture Governance
Architecture Governance sert principalement à :
A. Organiser décisions, conformité, responsabilités et exceptions d'architecture
B. Concentrer le pilotage sur coûts et planning des équipes de delivery sans vérifier la cohérence architecturale
C. Définir exclusivement les choix techniques de chaque application sans responsabilité d'arbitrage transverse
D. Assurer la préparation opérationnelle des utilisateurs finaux sans décisions de conformité ni de standards
**Réponse : A.** La gouvernance rend les décisions explicites, appliquées et traçables. B/C/D sont faux.
**Mapping : Architecture Governance — Fundamentals.**

## Q242 — Governance vs project management
Quelle distinction est correcte ?
A. Architecture Governance pilote les ressources projet ; Project Governance valide les views et les standards
B. Architecture Governance veille à la conformité et aux décisions d'architecture ; Project Governance pilote notamment coûts/délais/risques projet
C. Architecture Governance concerne seulement les achats ; Project Governance contrôle les requirements d'entreprise
D. Architecture Governance et Project Governance se confondent quand le sponsor est aussi propriétaire de la Target
**Réponse : B.** Les deux se coordonnent mais ont des objets différents.
**Distracteur C :** Coûts et délais sont des dimensions de pilotage de projet, pas la finalité propre de la gouvernance d'architecture.
**Mapping : Architecture Governance — Governance boundaries.**

## Q243 — Architecture Board
Le rôle principal d'un Architecture Board est :
A. Approuver chaque choix de réalisation technique et chaque tâche de développement
B. Séquencer toutes les activités de projet à la place des responsables de delivery
C. Arbitrer et gouverner les décisions d'architecture significatives
D. Définir seul les requirements métier sans les stakeholders et les architectes de domaine
**Réponse : C.** L'Architecture Board arbitre les décisions architecturales significatives. A relève de la conception détaillée, B du pilotage de livraison et D court-circuite les responsabilités métier et les architectes de domaine.
**Distracteur B :** Le Board porte sur les grandes décisions et la conformité, non le management quotidien des équipes.
**Mapping : Architecture Governance — Architecture Board.**

## Q244 — Board decision
Quand un Architecture Board est-il particulièrement utile ?
A. Lorsque le Product Owner souhaite répartir les tâches détaillées de chaque sprint
B. Lorsque les exploitants doivent sélectionner une version de logiciel sans impact architectural
C. Lorsque les équipes demandent uniquement une approbation budgétaire de leur calendrier
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
A. Un ensemble de diagrams décrivant l'état Baseline et les building blocks de la Target
B. Un accord formalisant les responsabilités et attentes entre parties autour de l'architecture
C. Un registre des standards technologies classés par version et domaine d'application
D. Une Architecture Roadmap représentant les work packages et états intermédiaires
**Réponse : B.** Il explicite les engagements de conformité et collaboration. A/C/D sont d'autres objets.
**Mapping : Architecture Governance — Architecture Contract.**

## Q247 — Contract in implementation
Pendant Phase G, l'Architecture Contract aide à :
A. Clarifier l'ordre des work packages et les gains métier attendus en Phase F
B. Définir la Baseline et Target Business Architecture avant le choix des solutions
C. Clarifier ce que les équipes d'implémentation doivent respecter et fournir comme preuves
D. Classer les assets réutilisables selon leur position dans l'Enterprise Continuum
**Réponse : C.** Le contrat soutient la gouvernance de mise en œuvre.
**Mapping : Architecture Governance — Architecture Contract.**

## Q248 — Contract vs Architecture Vision
Quelle différence est correcte ?
A. Architecture Vision et Architecture Contract ont la même finalité et le même signataire
B. Le Contract définit toujours la Target Data Architecture
C. La Vision est un waiver
D. La Vision aligne sur la direction cible ; le Contract formalise des engagements de gouvernance entre parties
**Réponse : D.** Les deux ont des finalités différentes.
**Mapping : Architecture Governance — Contract vs Vision.**

## Q249 — Compliance Review
Une Architecture Compliance Review sert à :
A. Comparer une implémentation ou solution aux requirements et décisions d'architecture approuvées
B. Comparer les modèles Baseline et Target pour produire une première liste des gaps
C. Identifier les work packages prioritaires et leurs dépendances au cours de la Phase F
D. Construire l'Architecture Vision et faire accepter les hypothèses de périmètre
**Réponse : A.** Elle vérifie l'alignement effectif.
**Mapping : Architecture Governance — Compliance.**

## Q250 — Compliance evidence
Quel élément est utile lors d'une Compliance Review ?
A. Une liste des jalons projet, sans traçabilité vers les requirements d'architecture
B. Requirements, decisions, architecture contracts et preuves d'implémentation
C. Un simple état d'avancement du planning projet
D. Le seul accord oral du sponsor sans preuves d'implémentation ni critères mesurés
**Réponse : B.** Une review doit être factuelle et traçable.
**Distracteur C :** Le respect du calendrier ne démontre pas la conformité architecturale.
**Mapping : Architecture Governance — Compliance.**

## Q251 — Non-compliance
Une review découvre un écart important. Quelle action est la plus cohérente ?
A. Modifier immédiatement la Target pour correspondre à l'état réel sans revue de gouvernance
B. Enregistrer la déviation comme un simple incident projet sans comparer les requirements
C. Enregistrer l'écart, évaluer son impact et décider correction ou exception via governance
D. Confier l'acceptation définitive de l'écart au fournisseur de la solution impliquée
**Réponse : C.** La gouvernance traite explicitement les écarts.
**Mapping : Architecture Governance — Compliance/Exception.**

## Q252 — Deviation
Une deviation est :
A. Une nouvelle requirement métier qui n'a pas encore été reliée aux composants cibles
B. Un gap identifié entre les architectures Baseline et Target pendant la conception
C. Une option de solution candidate non encore soumise à une décision de gouvernance
D. Un écart par rapport à une architecture, standard ou requirement approuvé
**Réponse : D.** Elle décrit la non-conformité constatée.
**Mapping : Architecture Governance — Deviations.**

## Q253 — Exception
Une exception/waiver est :
A. Une autorisation gouvernée de déroger à une règle sous conditions
B. Une modification de requirement sans analyse de ses impacts sur la Target Architecture
C. Un choix technique local qui remplace automatiquement un principe approuvé par le Board
D. Un gap constaté entre Baseline et Target, considéré à tort comme dérogation autorisée
**Réponse : A.** Une exception est explicitement décidée, documentée et souvent limitée.
**Mapping : Architecture Governance — Exceptions.**

## Q254 — Exception conditions
Une bonne exception doit idéalement préciser :
A. La seule date d'approbation du Board sans scope, risques ni durée de la dérogation
B. Rationale, scope, risques, owner, durée/conditions et actions futures
C. Aucun responsable
D. Aucune date de revue
**Réponse : B.** Une exception gouvernée doit être traçable et contrôlable.
**Mapping : Architecture Governance — Exceptions.**

## Q255 — Temporary waiver
Pourquoi une exception temporaire peut-elle être préférable à modifier immédiatement le standard ?
A. Parce qu'une exception locale doit toujours conduire à retirer la requirement centrale
B. Parce que le sponsor peut approuver seul une déviation sans analyse de risques
C. Parce qu'un cas local ne justifie pas forcément de changer une règle globale
D. Parce que toute déviation doit obligatoirement devenir un nouveau standard permanent
**Réponse : C.** Le waiver permet de gérer un cas particulier sans généraliser trop vite.
**Mapping : Architecture Governance — Exceptions.**

## Q256 — Governance log
Pourquoi tenir un Governance Log ?
A. Pour transformer automatiquement les écarts de réalisation en nouvelles normes obligatoires
B. Pour remplacer toutes les spécifications de requirements et les diagrams de la Target
C. Pour centraliser les tâches de support quotidien des équipes d'exploitation
D. Pour tracer décisions, reviews, exceptions et responsabilités
**Réponse : D.** Le log fournit une mémoire de gouvernance.
**Mapping : Architecture Governance — Governance Log.**

## Q257 — Escalation
Une équipe ne peut résoudre un conflit architectural local. Que faire ?
A. Escalader selon le modèle de governance prévu
B. Faire ratifier l'option par le seul responsable de livraison, même si l'impact dépasse son périmètre
C. Conserver les décisions de chaque domaine en attendant une éventuelle revue annuelle
D. Documenter les deux options dans le Repository sans demander de décision à l'autorité compétente
**Réponse : A.** Une divergence transverse se traite selon l'escalation prévue. B manque d'autorité, C reporte la décision et D confond documentation avec arbitrage ; aucun ne résout le conflit.
**Mapping : Architecture Governance — Escalation.**

## Q258 — Governance principles
Pourquoi des principles approuvés sont-ils importants pour la governance ?
A. Ils remplacent les requirements détaillées et les contrôles de conformité des solutions
B. Ils fournissent des critères durables pour guider et arbitrer les décisions
C. Ils désignent toujours les SBB retenus par les équipes de réalisation
D. Ils garantissent la même implémentation technique pour tous les domaines métier
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
B. Réviser les technologies sans considérer les nouveaux drivers ou la valeur délivrée
C. Supprimer le Board
D. Décider comment répondre aux changements et s'il faut un nouveau cycle
**Réponse : D.** H gouverne l'évolution de l'architecture.
**Mapping : Architecture Governance — Phase H.**

## Q261 — Best governance behavior
Quel comportement est le plus mature ?
A. Rendre les écarts visibles et les traiter selon un processus de décision connu
B. Tolérer les écarts si le sponsor accepte le calendrier sans mesurer leur risque métier
C. Modifier systématiquement les standards centraux afin d'aligner les règles sur chaque solution
D. Considérer une déviation comme approuvée dès qu'elle ne bloque pas la production
**Réponse : A.** La gouvernance repose sur visibilité, décision et traçabilité.
**Mapping : Architecture Governance — Synthesis.**

## Q262 — Governance synthesis
Quel enchaînement est le plus cohérent ?
A. Stakeholders → Technology Standards → Migration Plan → Business Architecture
B. Principles/requirements → Architecture Contract → implementation → Compliance Review → correction ou exception
C. Implementation Plan → Architecture Vision → Principles → Compliance Review
D. Architecture Contract → Change Request → Business Scenarios → Preliminary Phase
**Réponse : B.** Il relie règles, engagement, implémentation, contrôle et traitement des écarts.
**Mapping : Architecture Governance — Synthesis.**

---
Questions originales de préparation.