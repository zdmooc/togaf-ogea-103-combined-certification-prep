# Risk, Security and Governance English

## 1. Vocabulaire essentiel

- risk exposure
- likelihood
- impact
- mitigation
- residual risk
- control
- compliance
- regulatory requirement
- auditability
- traceability
- security by design
- least privilege
- segregation of duties
- encryption
- identity and access management
- secrets management
- threat
- vulnerability
- exception
- deviation
- waiver
- compliance review
- architecture contract
- governance board

## 2. Expliquer un risque

Structure : risk → cause → impact → mitigation → residual risk.

> One major risk is architecture drift across delivery teams. The cause is inconsistent adoption of standards. The impact would be higher operational complexity and support cost. We mitigate this with shared patterns, automated controls, architecture reviews, and a governed exception process. Some residual risk remains during the transition period.

## 3. Expliquer la sécurité

> Security is treated as a cross-cutting architecture concern, not as a final implementation check. Security requirements influence the business, data, application, and technology architectures.

> We apply security by design, explicit identity boundaries, least privilege, encryption, secrets management, audit logging, and traceable exceptions.

## 4. Expliquer governance vs project governance

> Architecture governance focuses on the consistency, compliance, and evolution of architectural decisions. Project governance focuses more broadly on delivery, budget, schedule, resources, and project outcomes. They interact, but they are not the same thing.

## 5. Architecture Board

> The Architecture Board provides governance and arbitration for significant architecture decisions. It may approve principles, review major deviations, resolve conflicts, and oversee compliance with the architecture framework.

## 6. Architecture Contract

> An Architecture Contract expresses agreed responsibilities and expectations between architecture governance and implementation stakeholders. It helps make architectural obligations explicit during delivery.

## 7. Compliance Review

> A compliance review compares the implementation or design against the approved architecture, requirements, principles, and standards. The objective is to identify and govern deviations, not simply to generate a pass/fail report.

## 8. Deviation vs Exception

> A deviation is an observed difference from the approved architecture. An exception or waiver is a governed decision that allows a deviation under defined conditions. A deviation should not become an implicit exception just because delivery is late.

## 9. Exprimer un désaccord

- `I understand the delivery constraint, but we need to make the risk explicit.`
- `I do not think this option is aligned with the approved target architecture.`
- `The option is technically feasible, but it creates a governance issue.`
- `We can accept the deviation only if the risk owner and governance body approve the exception.`
- `I would recommend documenting the trade-off before making the decision.`

## 10. Exprimer une incertitude

- `At this stage, we do not have enough evidence to confirm the option.`
- `This assumption still needs validation.`
- `The current data suggests..., but I would not treat it as a confirmed requirement yet.`
- `We need to distinguish a constraint from a preference.`

## 11. Questions d’entretien

### How do you handle an architecture exception?

> I first document the deviation and its reason. Then I assess the impact on requirements, principles, security, operations, and the roadmap. If the deviation is justified, it should be approved through the relevant governance process with clear conditions, ownership, and an expiry or review point when appropriate.

### What do you do when security arrives late?

> I do not simply add controls at the end. I revisit the affected requirements and architecture domains, assess the impact, and iterate where necessary. Security is cross-cutting and may change data flows, application boundaries, technology choices, or migration sequencing.

### How do you balance speed and governance?

> I use proportionate governance. High-risk or irreversible decisions need stronger review; low-risk decisions can use lightweight patterns and delegated authority. The goal is controlled speed, not maximum documentation.

## 12. MayaBank example

> During implementation, one team proposes a local identity component instead of the shared platform service. The local option is faster for the team, but it creates duplicate capabilities and increases security and operational complexity. I would treat this as a potential deviation, assess the impact, and use the governance process to decide whether to reject it or grant a time-bound exception.

## 13. Speaking drill

Répondre en 45 secondes :

1. What is architecture governance?
2. What is a compliance review?
3. What is the difference between a deviation and an exception?
4. How do you handle late security requirements?
5. How do you balance delivery speed and governance?
