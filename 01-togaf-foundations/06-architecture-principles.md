# 06 — Architecture Principles

## 1. Definition

An **Architecture Principle** is a general rule and guideline intended to be enduring and rarely amended, which informs and supports the way an organization fulfills its mission and makes architecture decisions.

In practice, architecture principles reduce arbitrary choices. They create a common decision framework across initiatives.

A principle is not merely a slogan. It should have enough explanation to influence real decisions.

---

## 2. Why principles exist

Large organizations face repeated choices:

- reuse or build?
- centralize or decentralize?
- synchronous or asynchronous integration?
- one identity platform or multiple local systems?
- standard platform or project-specific stack?
- data duplication or controlled sharing?

Without principles, each project can choose independently. This creates fragmentation.

Architecture Principles provide decision consistency.

Example:

> **Reuse before buy before build**

This kind of principle can guide multiple projects and influence solution evaluation criteria.

---

## 3. Typical structure of a principle

A useful principle is often expressed with four parts:

1. **Name**
2. **Statement**
3. **Rationale**
4. **Implications**

### Example — API-managed integration

**Name**  
Managed interfaces

**Statement**  
Business capabilities exposed across application boundaries should use governed interfaces.

**Rationale**  
Controlled interfaces reduce hidden coupling and improve lifecycle management.

**Implications**  
- interfaces must be registered;
- ownership must be explicit;
- security policies apply consistently;
- lifecycle/versioning must be managed;
- direct database access between unrelated applications should be exceptional.

The details above are pedagogical examples, not official mandatory TOGAF principles.

---

## 4. Enterprise principles vs Architecture Principles

An organization may have broad **Enterprise Principles** that guide business behavior and narrower **Architecture Principles** that guide architecture decisions.

Example:

Enterprise Principle:

> Customer data is treated as a strategic asset.

Possible Architecture Principles influenced by it:

- authoritative data ownership must be defined;
- duplication should be controlled;
- data quality responsibilities must be explicit.

The exact classification depends on the organization’s configured architecture practice.

---

## 5. Principle vs Requirement

This is one of the most important distinctions.

### Principle

- general rule;
- applies broadly;
- relatively stable;
- guides decisions.

### Requirement

- need that must be satisfied;
- can be specific to a transformation;
- managed through Requirements Management;
- can evolve as architecture work progresses.

### Example

Principle:

> Critical services should be designed for resilience.

Requirement:

> Payment Authorization must recover from a site failure within 15 minutes.

The principle guides the direction. The requirement makes the expectation specific and testable.

---

## 6. Principle vs Constraint

A **Constraint** limits the available design space due to a condition that must be respected.

Example:

- Principle: use standardized platform services where appropriate.
- Constraint: a specific legacy component must remain on the current platform until 2028 due to a vendor contract.

A principle expresses a preferred guiding rule. A constraint may force a particular limitation even when it is not architecturally ideal.

---

## 7. Principles in the Preliminary Phase

The **Preliminary Phase** is a key place to establish or review architecture principles because the organization is preparing the Architecture Capability and governance framework.

Before starting major architecture initiatives, the organization should know:

- which principles apply;
- who owns them;
- how exceptions are handled;
- how they influence solution review.

### Preliminary vs Phase A

Preliminary asks:

**What architecture practice and rules do we operate with?**

Phase A asks:

**What is the vision, scope and value of this architecture engagement?**

Architecture Principles therefore belong strongly to the preparation of the capability, even though they are applied throughout the ADM.

---

## 8. Principles and governance

A principle that cannot influence governance has little practical value.

Architecture Governance should be able to evaluate whether a solution:

- complies with principles;
- has a justified deviation;
- requires an exception;
- reveals that a principle itself must evolve.

Example:

Principle:

> Managed APIs are used for cross-domain service access.

A project proposes direct database access because of deadline pressure.

Governance should not simply say « forbidden ». It should determine:

1. whether the principle applies;
2. whether there is a valid exception;
3. what risk is introduced;
4. who approves the deviation;
5. whether remediation is required later.

---

## 9. Principles and Requirements Management

Principles can generate or shape requirements.

Example:

Principle:

> Security by design.

Architecture requirements might include:

- centralized identity integration;
- encryption requirements;
- audit logging;
- secrets management;
- segregation of duties.

Relationship:

```text
Architecture Principle
        ↓ guides
Architecture decision
        ↓ creates/refines
Requirement
```

Requirements may also reveal that an existing principle is too vague or unrealistic.

---

## 10. Good principles vs bad principles

### Bad principle — technology slogan

> We use cloud.

Problems:

- unclear rationale;
- no decision rule;
- no scope;
- no implications.

### Better principle

> Workloads should use approved scalable platform services unless regulatory, operational or economic constraints justify another deployment model.

Now the principle can influence decisions and exception handling.

### Bad principle — absolute rule with no context

> Everything must be microservices.

This is usually not a sound enterprise principle because it ignores context and can force unnecessary complexity.

A principle should improve decisions, not replace engineering judgment.

---

## 11. MayaBank architecture principles

For the case study, MayaBank can adopt example principles such as:

### Principle 1 — Business continuity by design

Critical payment capabilities must consider continuity requirements during architecture development.

### Principle 2 — Managed interfaces

Cross-domain application interaction uses governed interfaces/events.

### Principle 3 — Authoritative data ownership

Important business data has an identified accountable owner and source of truth.

### Principle 4 — Standard platform services first

Teams should reuse approved platform capabilities before creating local alternatives.

### Principle 5 — Observability is part of architecture

Critical services must expose the information required to operate and diagnose them.

Again, these are **MayaBank example principles**, not a list mandated by TOGAF.

---

## 12. How principles influence a decision

MayaBank needs a new event-streaming capability.

Without principles:

- Team A deploys Kafka itself.
- Team B buys a managed broker.
- Team C uses another technology.

With the principle **Standard platform services first**:

1. check whether an approved shared capability exists;
2. evaluate if it satisfies requirements;
3. reuse it if suitable;
4. if not suitable, document the gap and exception rationale.

The principle does not automatically select a product. It structures the decision.

---

## 13. Principle lifecycle

Principles should not change for every project, but they are not eternal.

They may need review when:

- business strategy changes;
- regulation changes;
- technology paradigm changes;
- repeated exceptions reveal a bad principle;
- merger/acquisition changes enterprise context.

Architecture Change Management can reveal the need to update the architecture capability and its rules.

---

## 14. Common mistakes

1. Treating a preference as a principle.
2. Writing only a slogan with no rationale or implications.
3. Creating a different principle set for every project.
4. Confusing principle and requirement.
5. Confusing principle and technology standard.
6. Making principles so absolute that architecture judgment disappears.
7. Ignoring principle exceptions in governance.
8. Copying generic principles without adapting them to the enterprise.

---

## 15. OGEA-103 exam traps

### Trap 1
A statement describes a specific performance target and calls it an Architecture Principle.

→ likely a requirement.

### Trap 2
A question asks where architecture principles are initially established/reviewed as part of setting up the architecture capability.

→ think **Preliminary Phase**.

### Trap 3
A scenario shows repeated non-compliance with a principle.

→ governance/exception handling and potentially review of the architecture capability may be required; simply ignoring the principle is not the TOGAF answer.

### Trap 4
A principle is treated as a specific product mandate.

→ principles guide decisions; standards/catalogs may contain more specific approved technologies.

---

## 16. Foundation questions

### Q1
What are the four common parts used to express an Architecture Principle?

**Answer:** Name, Statement, Rationale, Implications.

### Q2
What is the main difference between a principle and a requirement?

**Answer:** a principle is a broad, relatively stable decision rule; a requirement is a need that must be satisfied in a specific architecture context.

### Q3
Which ADM area is strongly associated with establishing the Architecture Capability and reviewing architecture principles?

**Answer:** Preliminary Phase.

---

## 17. Practitioner mini-scenario

MayaBank has an enterprise principle requiring approved shared platform services to be considered first. A payment project wants to deploy its own observability stack because the team is familiar with it.

A TOGAF-consistent response is to evaluate the project against the principle, check whether the shared capability satisfies requirements, document any real gap, and govern a deviation if necessary.

The correct response is not simply « reject » and not simply « let the team choose ».

---

## 18. English for Architects

Useful sentences:

- Architecture principles guide decision-making across initiatives.
- A principle should include a rationale and implications.
- This requirement is derived from our resilience principle.
- The project requests an exception to an architecture principle.

### Speak it

1. This principle guides our platform decisions.
2. The requirement is more specific than the principle.
3. We need to document the exception and its rationale.

---

## 19. Interview question

**Question:** How do architecture principles help you as an architect?

**Simple answer:**

Architecture principles provide stable decision rules across projects. I use them to evaluate options, explain why a decision is preferred, and govern exceptions. They are broader than project requirements and should include clear rationale and implications.

---

## 20. Key points to remember

**Principle = stable decision guidance.**

A strong principle has:

**Name → Statement → Rationale → Implications.**

And never forget:

**Principle ≠ Requirement ≠ Constraint ≠ Technology Standard.**
