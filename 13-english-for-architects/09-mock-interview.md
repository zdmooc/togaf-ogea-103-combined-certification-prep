# Mock Interview — Enterprise / Solution Architect

## Instructions

Durée cible : 25 à 35 minutes.

Règles :

- répondre à voix haute ;
- ne pas lire les réponses modèles avant la simulation ;
- limiter les réponses simples à 45–90 secondes ;
- utiliser Context → Problem → Decision → Trade-off → Outcome pour les questions d’expérience.

---

## Part 1 — Introduction

### Q1 — Tell me about yourself and your current architecture focus.

Points attendus : rôle, domaines, valeur apportée, contexte récent.

Réponse modèle :

> I am an enterprise and solution architect with experience in complex banking and payment environments. My work combines application, integration, cloud platform, security, and architecture governance concerns. I focus especially on modernization and transformation: understanding the current landscape, defining a realistic target, and creating a migration path that delivery teams can actually implement.

### Q2 — What is the difference between an enterprise architect and a solution architect?

> An enterprise architect focuses on coherence across business capabilities, domains, standards, and transformation roadmaps. A solution architect works closer to a specific initiative and turns enterprise direction and requirements into a concrete solution. In practice, the roles must collaborate closely.

---

## Part 2 — TOGAF and method

### Q3 — How do you use TOGAF in practice?

> I use TOGAF as a structuring framework. I use the ADM concepts to understand context, stakeholders, baseline and target states, gaps, migration, governance, and change. I tailor the depth and artifacts to the organization instead of applying every activity mechanically.

### Q4 — Explain the ADM in less than one minute.

Attendu : Preliminary/A/B/C/D/E/F/G/H + Requirements Management transversal, sans récitation détaillée.

### Q5 — What is the difference between Phase E and Phase F?

Attendu : E = work packages/options/transitions ; F = prioritize/sequence/migration plan.

---

## Part 3 — Architecture problem

### Q6 — You join a company with 300 applications and no reliable architecture repository. What do you do first?

Bonne direction :

- clarify business scope and priorities;
- understand existing governance and ownership;
- establish architecture capability/repository practices;
- build a useful landscape incrementally;
- avoid trying to document all 300 applications before creating value.

Réponse modèle :

> I would not start by documenting all 300 applications in detail. I would first clarify the business priorities, key stakeholders, major risks, and transformation scope. Then I would establish a minimum architecture repository and ownership model, identify the most critical capabilities and applications, and improve the landscape iteratively.

### Q7 — A team proposes a new technology because it is more modern. How do you respond?

> I would ask which requirement or architecture problem the technology solves. Then I would compare it against the current option using decision criteria such as business value, security, resilience, operability, lifecycle, skills, cost, vendor risk, and migration impact. “More modern” is not an architecture requirement.

---

## Part 4 — Migration

### Q8 — How would you modernize a critical payment application?

Attendu : baseline/dependencies, target capabilities, risk, transition states, pilot, observability, migration waves, governance.

### Q9 — When would you choose a big-bang migration?

> Only when the business, technical, and operational context makes it safer or simpler than coexistence—for example when coexistence is technically impossible and the cutover can be fully controlled. For a critical platform, I would need strong evidence before choosing a big bang.

### Q10 — How do you decide when to decommission a legacy system?

> I decommission only when the required capabilities have moved, dependencies are removed or replaced, data and compliance obligations are addressed, operational acceptance is complete, and rollback to the legacy system is no longer required.

---

## Part 5 — Risk and governance

### Q11 — A delivery team asks for an exception to an architecture standard two weeks before release. What do you do?

> I first understand why the standard cannot be met and whether the issue is a real constraint or simply schedule pressure. I assess the impact and risk, identify possible alternatives, and use the architecture governance process to decide. If an exception is approved, it should be explicit, traceable, owned, and reviewed under defined conditions.

### Q12 — What is architecture governance for?

> Architecture governance makes important architecture decisions consistent, traceable, and enforceable. It defines decision rights, compliance mechanisms, exception handling, and how architecture evolves without losing coherence.

### Q13 — How do you avoid architecture becoming bureaucracy?

> I use proportionate governance. I focus documentation and reviews on decisions that are high-risk, expensive, cross-domain, difficult to reverse, or strategically important. Reusable patterns and automated controls can replace many manual reviews.

---

## Part 6 — Stakeholders

### Q14 — How do you deal with an executive who does not want technical detail?

> I explain business outcomes, risk, cost, options, and the decision required. I keep the technical detail available as supporting evidence but do not make it the center of the discussion.

### Q15 — How do you deal with engineers who think enterprise architecture is too abstract?

> I connect the enterprise decision to concrete engineering consequences: interfaces, standards, deployment constraints, failure modes, data ownership, and reusable platform capabilities. Architecture must be actionable at the right level.

---

## Part 7 — MayaBank challenge

### Q16 — Present MayaBank modernization in two minutes.

Réponse cible :

> MayaBank has a fragmented payment landscape with overlapping applications, batch processing, point-to-point integration, and limited observability. The target is a more modular and governable platform with clear service boundaries, standardized APIs and events, explicit data ownership, strong observability, and a standardized runtime platform. Because payment continuity is critical, I would not use a big-bang migration. I would establish common platform capabilities first, migrate a limited scope, validate a transition architecture, and then expand through controlled migration waves. Architecture governance would continue during implementation through reviews, traceable decisions, and controlled exceptions.

### Q17 — What is the main trade-off in this transformation?

> The main trade-off is migration speed versus operational risk and coexistence complexity. A phased approach is slower and temporarily more complex, but it reduces the probability and impact of a large production failure.

---

## Part 8 — Behavioral questions

### Q18 — Tell me about a time you disagreed with another architect.

Structure :

- what was the decision;
- what did each person value;
- what evidence was used;
- how the disagreement was resolved;
- what was learned.

### Q19 — Tell me about a decision you would change today.

Éviter « I have no regrets ». Montrer capacité d’apprentissage.

> I would change a decision where we optimized too much for short-term delivery speed and underestimated operational complexity. The lesson was to involve operations earlier and make transition-state requirements explicit.

### Q20 — How do you know an architecture is successful?

> I look at whether the architecture enables the intended business outcomes and whether the solution remains secure, operable, evolvable, and governable. Success is not the production of architecture documents; it is the quality of the resulting decisions and transformation.

---

## Final self-assessment

Pour chaque réponse, noter 0–2 :

- **Structure** — ai-je répondu clairement ?
- **Reasoning** — ai-je expliqué pourquoi ?
- **English** — phrases simples et compréhensibles ?
- **Architecture depth** — ai-je montré stakeholders/requirements/risk/trade-off ?

Maximum : 8 points par question.

Objectif avant entretien réel : moyenne ≥ 6/8 sur les 20 questions.
