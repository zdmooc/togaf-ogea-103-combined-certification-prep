# Using the ADM in the Digital Enterprise

## 1. What changes in a digital enterprise?

Le **Digital Enterprise** accélère le rythme de changement : produits numériques, APIs, plateformes, data, cloud, automation, partenaires et nouveaux business models évoluent plus vite que dans des cycles de transformation traditionnels.

Cela ne rend pas TOGAF obsolète. Cela augmente au contraire le besoin de :

- direction claire ;
- reusable building blocks ;
- architecture principles ;
- fast governance ;
- platform thinking ;
- capability planning ;
- continuous change management.

## 2. Digital does not mean “technology first”

Une transformation digitale reste une transformation d’entreprise.

Le mauvais raisonnement est :

« Nous devons adopter cloud, microservices et AI. »

Le bon raisonnement est :

**business outcomes → capabilities → operating model → information → applications → technology enablement**.

Les technologies numériques sont des enablers, pas des objectifs en elles-mêmes.

## 3. Characteristics of digital architecture

### Product orientation

Les équipes évoluent souvent de projets temporaires vers des produits ou capabilities pérennes.

### Platform orientation

Des capacités communes sont fournies comme plateformes :

- container platform ;
- API platform ;
- event streaming ;
- identity ;
- observability ;
- data platform.

### Ecosystem orientation

L’entreprise dépend davantage :

- partners ;
- SaaS ;
- cloud providers ;
- external APIs ;
- digital marketplaces.

### Continuous evolution

L’architecture doit supporter un changement fréquent sans perdre standards et coherence.

## 4. Applying the ADM differently

### Phase A

La Vision doit être rapide, claire et orientée outcomes/capabilities.

### B/C/D

Le niveau de détail peut être progressif et basé sur les décisions nécessaires.

### E/F

Les work packages peuvent devenir :

- platform increments ;
- product increments ;
- migration waves ;
- enablement initiatives.

### G

Governance doit être intégrée aux delivery pipelines lorsque possible.

### H

Architecture Change Management devient presque continu dans les environnements numériques.

## 5. Platform thinking

Une plateforme n’est pas seulement une infrastructure.

Une **platform capability** fournit un ensemble cohérent de services et guardrails permettant à plusieurs produits de livrer plus vite.

Exemple MayaBank :

OpenShift seul n’est pas la Digital Platform.

La capability inclut :

- runtime ;
- GitOps ;
- CI/CD integration ;
- secrets ;
- observability ;
- policy ;
- service templates ;
- support model ;
- SLOs.

## 6. Architecture runway

Dans un environnement digital/agile, certaines capacités architecturales doivent être préparées avant que les produits puissent les consommer.

Exemples :

- API standards ;
- event schemas ;
- identity foundation ;
- observability ;
- platform automation.

Cela correspond bien au raisonnement Phase E/F : certains work packages créent les fondations nécessaires aux increments futurs.

## 7. Data in the digital enterprise

Les données deviennent souvent un asset partagé.

L’architecture doit traiter :

- ownership ;
- quality ;
- lineage ;
- APIs/events ;
- analytical and operational use ;
- privacy ;
- lifecycle ;
- semantic consistency.

Une architecture numérique sans gouvernance data crée rapidement un écosystème incohérent.

## 8. Ecosystem architecture

Questions :

- quelles boundaries internes/externes ?
- quels trust relationships ?
- quels contracts ?
- quelles SLAs ?
- quelles dependencies fournisseur ?
- quelle exit strategy ?
- quelle interoperability ?

Le digital enterprise augmente donc l’importance d’Interoperability et Risk Management.

## 9. Continuous governance

Une Architecture Board mensuelle ne suffit pas toujours.

On peut compléter par :

- automated policy checks ;
- reference implementations ;
- architecture decision records ;
- approved templates ;
- pipeline controls ;
- self-service guardrails.

Governance devient plus proche du delivery sans disparaître.

## 10. MayaBank example

MayaBank passe d’un modèle « projet paiement » à un modèle :

- Payment Product Teams ;
- shared OpenShift Platform ;
- shared Event Platform ;
- API standards ;
- reusable security patterns ;
- product SLOs ;
- continuous architecture reviews.

L’ADM est tailored :

- Phase A légère pour increments mineurs ;
- B/C/D approfondies lorsque la capability change ;
- E/F intégrées au product/portfolio planning ;
- G intégrée à CI/CD et reviews ;
- H alimentée par telemetry, regulation et product strategy.

## 11. Common mistakes

- digital = adopter des technologies à la mode ;
- supprimer l’architecture pour aller vite ;
- centraliser toutes les décisions ;
- laisser chaque product team créer ses propres standards ;
- confondre autonomy et absence de governance ;
- ignorer operating model et skills.

## 12. OGEA-103 traps

- Digital Enterprise n’annule pas l’ADM.
- TOGAF 10 fournit plus de guidance pour Digital Transformation et Agile contexts.
- Tailoring et iteration sont essentiels.
- Product/platform operating models modifient la manière de faire l’architecture, pas les besoins fondamentaux de stakeholders, requirements et governance.

## 13. Practitioner scenario

Des product teams réclament une autonomie totale et refusent les standards d’entreprise. La meilleure réponse n’est ni de supprimer la gouvernance ni de centraliser chaque décision. Il faut définir des principles, reusable building blocks et guardrails permettant une autonomie contrôlée, avec un processus d’exception clair.

## 14. English for Architects

> In a digital enterprise, architecture must provide direction and reusable guardrails without slowing down product teams.

### Speak it

1. We use shared platforms to accelerate delivery.
2. Governance is integrated into the delivery lifecycle.
3. Product teams have autonomy within clear architecture guardrails.

## 15. Key points

- Digital ≠ technology-first.
- ADM reste pertinent mais doit être tailored.
- Platforms et reusable building blocks accélèrent le delivery.
- Governance peut devenir continuous et automated.
- H devient particulièrement important dans un environnement de changement fréquent.

---

The Open Group publishes guidance on Using the TOGAF Standard in the Digital Enterprise. This chapter is an original educational explanation.