# Enterprise Architect Interview Questions — English

## 1. Tell me about yourself

Réponse modèle :

> I am an enterprise and solution architect with experience in complex information systems, especially in banking and payment environments. My role is to connect business needs with application, data, technology, security, and operational constraints. I am particularly comfortable with modernization, cloud-native platforms, integration, governance, and migration planning.

Version plus courte :

> I am a solution and enterprise architect focused on modernization, integration, cloud platforms, and architecture governance in complex environments.

## 2. What is your role as an architect?

> My role is to understand the business problem, identify the important stakeholders and requirements, define the target architecture, make trade-offs explicit, and help delivery teams implement the architecture in a controlled way.

## 3. How do you start an architecture engagement?

> I start with context: business drivers, stakeholders, concerns, scope, constraints, existing architecture, and expected outcomes. I avoid selecting a product before the problem and requirements are sufficiently understood.

## 4. How do you define a target architecture?

> I compare the relevant baseline with the desired business outcomes, then develop the business, data, application, and technology views needed for the decision. I identify gaps, risks, dependencies, and architectural principles before defining the transformation roadmap.

## 5. How do you make architecture decisions?

> I make the decision criteria explicit: business value, requirements, risk, security, operability, cost, lifecycle, standards, and migration impact. I compare realistic options, document the trade-offs, and make the decision traceable.

## 6. Give me an example of a trade-off

> A common trade-off is migration speed versus operational risk. A big-bang migration may reduce coexistence cost, but it can create unacceptable business continuity risk. In that case I prefer a phased migration with explicit transition architectures.

## 7. How do you work with Agile teams?

> I do not treat architecture as a waterfall gate before delivery. I establish clear principles, target direction, reusable patterns, decision boundaries, and lightweight governance. Architecture and delivery can iterate together while major decisions remain traceable.

## 8. How do you handle disagreement with a delivery team?

> I first understand the reason behind the proposed deviation. Then I compare it with the requirements, target architecture, risks, and constraints. If the team has a valid reason, we may update the architecture or request a governed exception. The objective is not to win an argument; it is to make a sound and traceable decision.

## 9. How do you handle technical debt?

> I distinguish debt that creates business or operational risk from debt that is merely imperfect. I assess impact, likelihood, cost of change, strategic relevance, and dependencies. I then include justified remediation in the roadmap instead of trying to eliminate all debt immediately.

## 10. How do you evaluate a technology?

> I evaluate technology against architecture requirements and quality attributes such as security, resilience, scalability, operability, integration, lifecycle, skills, vendor risk, and cost. I also consider how difficult it will be to migrate away from the technology later.

## 11. How do you approach cloud or OpenShift migration?

> I first determine whether the target platform capabilities are actually required. Then I assess application suitability, dependencies, data, security, operational model, observability, and migration constraints. Containerizing an application does not automatically modernize its architecture.

## 12. What is your approach to resilience?

> Resilience starts with business impact and service objectives. I look at failure domains, redundancy, recovery requirements, dependency failures, observability, operational procedures, and testing. High availability is only one part of resilience.

## 13. How do you communicate with executives?

> I focus on outcomes, risk, cost, options, and decisions. I avoid unnecessary implementation detail unless it directly affects the decision. I usually explain the current problem, the target outcome, the main options, the recommended choice, and the trade-offs.

## 14. How do you communicate with engineers?

> With engineers I go deeper into interfaces, failure modes, data flows, deployment, security controls, observability, and implementation constraints. The architecture message should be adapted to the stakeholder concern.

## 15. What is the value of TOGAF for you?

> TOGAF gives me a common structure for architecture work: context, stakeholders, baseline and target states, gaps, transformation planning, governance, and change. I use it as a framework that must be tailored, not as a rigid checklist.

## 16. Tell me about a difficult architecture decision

Structure conseillée :

```text
Situation
→ Constraint
→ Options
→ Decision
→ Trade-off
→ Outcome
```

Réponse modèle :

> We had to modernize a business-critical platform without creating a long outage. The main constraint was business continuity. We considered a direct replacement and a phased migration. The direct replacement was simpler in the final state but created too much cutover risk. We chose a phased approach with coexistence and transition architectures. The trade-off was temporary complexity in exchange for lower migration risk.

## 17. What would you do in your first weeks on a new mission?

> I would first understand the business context, stakeholders, architecture landscape, current decisions, major risks, standards, governance model, and active transformation initiatives. I would avoid proposing a new target before understanding why the current architecture exists.

## 18. What is your weakness?

Réponse sobre :

> I can go too deep into technical detail when a problem is complex. I manage this by defining the decision first and adapting the level of detail to the stakeholder.

## 19. What if you do not know the answer?

> I would not invent an answer. I would explain what I know, identify the missing information, and describe how I would validate it.

## 20. Questions à poser à l’intervieweur

- `What are the main architecture challenges today?`
- `How are architecture decisions governed?`
- `How are enterprise, solution, and platform architects organized?`
- `What are the main transformation programs?`
- `How mature is the architecture repository and standards landscape?`
- `How do architecture teams work with product and delivery teams?`
- `What would success look like after six months in this role?`

## Drill

Choisir 5 questions par séance. Répondre oralement sans lire. Réécouter son enregistrement et corriger uniquement : structure, clarté, hésitations et vocabulaire manquant.
