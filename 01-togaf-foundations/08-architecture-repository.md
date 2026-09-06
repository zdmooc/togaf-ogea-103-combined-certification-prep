# 08 — Architecture Repository

## 1. Definition

The **Architecture Repository** is the structured collection used to store, organize, manage and retrieve architecture assets created or reused by the Enterprise Architecture practice.

It supports reuse, governance, traceability and consistency.

The Repository is not limited to a single software tool. An organization may implement it using an EA platform, document repository, modeling tool, Git, knowledge base or a combination of systems.

The TOGAF concept is logical: the organization needs a managed structure for its architecture knowledge.

---

## 2. Why it exists

Without a managed repository, architecture knowledge becomes fragmented.

Typical symptoms:

- each architect has local files ;
- the latest architecture cannot be identified ;
- principles and standards exist in multiple versions ;
- reusable patterns are repeatedly reinvented ;
- governance decisions cannot be traced ;
- decommissioned systems still appear in diagrams ;
- projects cannot determine which standards apply.

The Architecture Repository is intended to reduce these problems.

---

## 3. What can be stored

An Architecture Repository can contain or reference many types of assets, such as:

- architecture principles ;
- standards ;
- reference architectures ;
- viewpoints ;
- models ;
- catalogs ;
- matrices ;
- diagrams ;
- Architecture Definitions ;
- Architecture Roadmaps ;
- governance records ;
- compliance information ;
- reusable Building Blocks ;
- external reference material.

Not every asset must physically live in the same database. The repository can provide an organized logical structure across multiple systems.

---

## 4. Major repository areas

For learning purposes, remember the key logical areas commonly associated with the TOGAF Architecture Repository.

### Architecture Metamodel

Defines how architecture content is structured and related.

It answers questions such as:

- what concepts do we model?
- how are artifacts related?
- what extensions are used by the enterprise?

### Architecture Capability

Contains information supporting the operation and governance of the architecture practice.

Examples:

- organization ;
- roles ;
- responsibilities ;
- governance processes ;
- skills.

### Architecture Landscape

Provides representations of architectures across the enterprise at different levels and points in time.

It helps answer:

**What architectures exist across our enterprise landscape?**

### Standards Information Base

Contains standards that guide architecture and solution decisions.

Examples:

- approved platform standards ;
- technology standards ;
- integration standards ;
- data standards.

### Reference Library

Contains reusable reference material.

Examples:

- external frameworks ;
- patterns ;
- reference architectures ;
- industry material.

### Governance Log

Contains governance-related records.

Examples:

- compliance decisions ;
- dispensations/exceptions ;
- review outcomes ;
- governance actions.

The exact implementation can be tailored to the enterprise.

---

## 5. Architecture Landscape

The **Architecture Landscape** is particularly useful because an enterprise usually needs architecture information at multiple levels.

A large bank may need to understand:

- strategic architecture across the group ;
- segment architecture for Payments ;
- capability architectures ;
- solution-level architectures.

The Landscape helps maintain an integrated view of the current and future enterprise architecture.

### Example

MayaBank Landscape:

```text
Enterprise
 ├── Customer & Channels
 ├── Payments
 │    ├── Payment Initiation
 │    ├── Fraud
 │    ├── Clearing & Settlement
 │    └── Payment Platform
 ├── Risk
 └── Data & Analytics
```

The exact representation can vary, but the concept is to maintain coherent visibility over architecture assets.

---

## 6. Standards Information Base

The **Standards Information Base** supports consistency by making relevant standards discoverable.

Example MayaBank:

| Area | Standard example |
|---|---|
| Container platform | approved OpenShift versions/patterns |
| Event streaming | approved event platform standards |
| APIs | interface governance and security rules |
| Databases | supported database services |
| Identity | enterprise IAM standards |
| Observability | logging/metrics/tracing requirements |

A standard is more specific than a broad Architecture Principle.

Example:

- Principle: reuse approved platform capabilities first.
- Standard: OpenShift is the supported container platform for specified workloads.

---

## 7. Governance Log

Architecture Governance needs memory.

If an exception is approved today, future architects should be able to know:

- what was approved ;
- why ;
- by whom ;
- for how long ;
- what risk was accepted ;
- whether remediation is required.

The **Governance Log** helps preserve this information.

Without it, organizations repeatedly debate the same decisions and lose accountability.

---

## 8. Repository vs Content

The Architecture Repository is not the same thing as Architecture Content.

### Architecture Content

The actual deliverables, artifacts, building blocks and architecture descriptions.

### Architecture Repository

The managed structure used to organize and retain them.

Think:

**Content = what we produce/use.**

**Repository = where/how we manage it.**

---

## 9. Repository vs Enterprise Continuum

This is a critical exam distinction.

### Repository

Stores and organizes assets.

### Enterprise Continuum

Helps classify and understand assets from generic to enterprise-specific.

Example:

MayaBank stores an industry payment reference architecture in its Reference Library.

- Repository tells us where it is managed.
- Enterprise Continuum helps us understand that it is an industry-level reusable asset rather than MayaBank’s organization-specific Target Architecture.

---

## 10. Repository and reuse

Before building a new architecture, an architect should search for reusable material.

Potential sequence:

1. understand scope and problem ;
2. inspect Architecture Landscape ;
3. check applicable principles and standards ;
4. search Reference Library ;
5. identify reusable Building Blocks ;
6. specialize material to the current architecture.

This can reduce cost and increase consistency.

Reuse does not mean copy without analysis.

---

## 11. Repository and the ADM

The Repository interacts with the ADM throughout the lifecycle.

### Preliminary

Set up repository structure, governance and architecture capability.

### Phase A

Reuse existing landscape, principles, stakeholder information and prior architecture assets.

### B/C/D

Store Baseline/Target architectures, artifacts and building blocks.

### E/F

Capture roadmap, transition architectures and work packages.

### G

Store compliance and governance outcomes.

### H

Update architecture assets when change occurs.

The Repository is therefore not « a final archive ». It supports active architecture work.

---

## 12. MayaBank example

MayaBank is starting an ISO 20022 modernization initiative.

The architect first checks:

- Architecture Landscape → what payment systems already exist?
- Standards Information Base → which API/event/container standards apply?
- Reference Library → do we have an ISO 20022 information model or event pattern?
- Governance Log → were exceptions previously granted for direct database integration?
- Architecture Capability information → which review board must approve the target?

This avoids restarting from zero.

---

## 13. Common mistakes

1. Treating the Repository as a simple document archive.
2. Believing one commercial tool is required.
3. Confusing Repository and Enterprise Continuum.
4. Storing architecture without version/ownership/governance.
5. Creating standards nobody can discover.
6. Ignoring the repository until project closure.
7. Assuming everything must physically be stored in one system.

---

## 14. OGEA-103 exam traps

### Trap 1
Question asks where architecture standards are managed.

→ think **Standards Information Base** within the repository concept.

### Trap 2
Question asks where governance decisions/exceptions are retained.

→ think **Governance Log**.

### Trap 3
Question asks how assets are classified from generic to specific.

→ not Repository: **Enterprise Continuum**.

### Trap 4
Question describes current enterprise architectures at multiple levels.

→ think **Architecture Landscape**.

---

## 15. Foundation questions

### Q1
What is the purpose of the Architecture Repository?

**Answer:** to organize, manage and make architecture assets reusable and traceable.

### Q2
Which repository area contains architecture standards?

**Answer:** Standards Information Base.

### Q3
Which area captures governance decisions and compliance history?

**Answer:** Governance Log.

### Q4
What is the difference between Repository and Continuum?

**Answer:** Repository manages assets; Continuum classifies/understands them.

---

## 16. English for Architects

Useful sentences:

- We checked the Architecture Repository before creating new content.
- The Standards Information Base contains the applicable platform standards.
- The Governance Log records architecture exceptions.
- The Architecture Landscape shows the current enterprise architecture.

### Speak it

1. We reuse existing architecture assets.
2. The standard is stored in the repository.
3. The exception must be recorded in the governance log.

---

## 17. Interview question

**Question:** How do you use an Architecture Repository in practice?

**Simple answer:**

I use it to find existing architecture assets, standards, reference material and previous decisions. During the project I update the relevant architecture descriptions, roadmap and governance information so future teams can reuse and trust the content.

---

## 18. Key points to remember

Architecture Repository major ideas:

- **Architecture Metamodel** — structure of content
- **Architecture Capability** — practice/governance information
- **Architecture Landscape** — enterprise architectures
- **Standards Information Base** — applicable standards
- **Reference Library** — reusable reference material
- **Governance Log** — governance history

And the exam memory line:

**Repository stores/manages. Continuum classifies.**
