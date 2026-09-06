# Tailoring the ADM

## 1. Definition

Le **tailoring** consiste à adapter l’Architecture Development Method au contexte réel de l’entreprise et du travail d’architecture.

TOGAF ne demande pas d’exécuter chaque phase, activité, artifact et deliverable de manière identique dans toutes les organisations.

Le principe est :

**Use the ADM deliberately, not mechanically.**

L’ADM fournit une structure de raisonnement. L’architecte adapte :

- profondeur ;
- ordre ;
- itérations ;
- niveau de détail ;
- techniques ;
- deliverables ;
- gouvernance ;
- rôles ;
- outils ;
- intégration avec les méthodes de delivery.

## 2. Pourquoi le tailoring est nécessaire

Une architecture pour une nouvelle réglementation de paiement critique n’a pas le même besoin qu’une petite évolution interne.

Les différences peuvent concerner :

- taille ;
- criticité ;
- maturité EA ;
- réglementation ;
- niveau de risque ;
- organisation ;
- méthodes Agile/DevOps ;
- existence d’architectures réutilisables ;
- contraintes de temps ;
- nombre de domaines impactés.

Appliquer le même processus lourd partout réduirait l’efficacité de l’architecture.

## 3. Tailoring vs supprimer la discipline

Tailoring ne signifie pas :

- ignorer les stakeholders ;
- supprimer Requirements Management ;
- sauter l’analyse des gaps sans raison ;
- choisir une solution avant de comprendre le besoin ;
- éviter la gouvernance.

Tailoring signifie conserver la logique essentielle en l’adaptant proportionnellement.

## 4. Quand le tailoring est-il défini ?

Le cadre général de tailoring appartient à l’**Architecture Capability** et est fortement lié à la **Preliminary Phase**.

Pour un engagement donné, il est ensuite affiné selon :

- scope ;
- stakeholders ;
- constraints ;
- objectives ;
- required outputs.

## 5. Dimensions de tailoring

### Process tailoring

Adapter les phases, activités et cycles d’itération.

### Content tailoring

Adapter les deliverables, artifacts, viewpoints et niveau de détail.

### Governance tailoring

Adapter les forums, approvals, compliance reviews et règles d’escalade.

### Organization tailoring

Adapter rôles, responsabilités et interaction entre Enterprise, Domain, Solution et Delivery Architects.

### Method integration

Aligner TOGAF avec :

- Agile ;
- product management ;
- project management ;
- DevSecOps ;
- portfolio governance ;
- security/risk processes.

## 6. Exemples de tailoring

### Petit changement applicatif

- réutilisation d’une architecture existante ;
- scope étroit ;
- Phase A légère ;
- B/C/D ciblées ;
- governance proportionnée.

### Transformation réglementaire multi-système

- stakeholder management renforcé ;
- exigences et traceability fortes ;
- B/C/D détaillées ;
- risques formalisés ;
- Transition Architectures ;
- reviews de conformité fréquentes.

### Innovation / prototype

- itérations courtes ;
- hypothèses explicites ;
- architecture intentionnelle mais légère ;
- décision rapide sur ce qui doit être industrialisé.

## 7. Tailoring et Deliverables

Un piège fréquent est de mesurer la conformité TOGAF au nombre de documents.

Le vrai objectif est de produire **le contenu nécessaire pour les décisions et la gouvernance**.

Exemple : un même Architecture Definition Document peut agréger plusieurs artifacts plutôt que créer une multitude de fichiers isolés.

## 8. Tailoring et Requirements Management

Requirements Management reste transversal même dans un processus simplifié.

La forme peut varier : outil dédié, backlog gouverné, repository, requirement catalog, mais les exigences importantes doivent rester maîtrisées.

## 9. Tailoring et governance

Plus le risque augmente, plus la gouvernance peut être renforcée.

Exemple :

- architecture standard réutilisée → review légère ;
- déviation de sécurité majeure → Architecture Board + risk acceptance ;
- système critique réglementé → evidence et compliance review formels.

## 10. MayaBank

MayaBank définit trois niveaux de tailoring :

### Tier 1 — Critical Payment Transformation

- ADM complet ;
- traceability forte ;
- formal Architecture Board ;
- security/risk review ;
- Transition Architectures ;
- implementation governance.

### Tier 2 — Major Product Evolution

- Phase A structurée ;
- B/C/D proportionnées ;
- roadmap et governance standard.

### Tier 3 — Minor Change

- réutilisation de patterns approuvés ;
- impact assessment ;
- exceptions uniquement si déviation.

Cette approche évite d’appliquer un processus lourd aux petits changements tout en protégeant les transformations critiques.

## 11. Erreurs fréquentes

- croire que tailoring = choisir les phases qu’on aime ;
- supprimer les exigences ;
- supprimer la gouvernance ;
- garder tous les documents par habitude ;
- ne pas documenter les décisions de tailoring ;
- utiliser le même tailoring pour tous les engagements.

## 12. Pièges OGEA-103

- L’ADM est adaptable, pas rigide.
- Tailoring doit être intentionnel et contextualisé.
- L’absence de documents inutiles n’est pas une non-conformité en soi.
- Une réponse Practitioner qui adapte le niveau de travail au risque et au contexte est souvent meilleure qu’une application mécanique de toutes les activités.

## 13. Foundation questions

### Q1
Pourquoi tailor l’ADM ?

A. Pour supprimer la gouvernance  
B. Pour adapter méthode et contenu au contexte  
C. Pour éviter les stakeholders  
D. Pour remplacer Requirements Management

**Réponse : B.**

## 14. English for Architects

> We tailored the ADM to the risk, scope, maturity and delivery model of the organization.

### Speak it

1. TOGAF is not a rigid waterfall process.
2. We adapted the level of architecture work to the context.
3. Critical changes require stronger governance and traceability.

## 15. Key points

- Tailoring = adaptation intentionnelle.
- ADM n’est pas un processus rigide.
- Process, content, governance et roles peuvent être adaptés.
- Les principes essentiels restent : stakeholders, requirements, decisions, gaps, governance.
- Le niveau de rigueur doit être proportionné au contexte et au risque.

---

Original educational content aligned with TOGAF Standard, 10th Edition tailoring concepts.