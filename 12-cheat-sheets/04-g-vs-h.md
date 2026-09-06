# Cheat Sheet — Phase G vs Phase H

## La différence en une phrase

- **Phase G — Implementation Governance** : vérifie que ce qui est implémenté reste conforme à l’architecture approuvée.
- **Phase H — Architecture Change Management** : décide comment l’architecture doit évoluer quand le contexte change.

## Tableau comparatif

| Sujet | Phase G | Phase H |
|---|---|---|
| Focus | implémentation en cours | changement de l’architecture |
| Question | Est-ce que le delivery respecte l’architecture ? | Le changement justifie-t-il une évolution ou un nouveau cycle ? |
| Objets | Architecture Contract, Compliance Review, deviations | change requests, impact assessment, governance of change |
| Horizon | projet / programme d’implémentation | évolution continue de l’entreprise et du paysage |

## Les mots qui orientent vers G

- implementation
- compliance
- Architecture Contract
- deviation
- waiver / exception
- design review
- conformance
- solution delivered differently from architecture

## Les mots qui orientent vers H

- new business driver
- regulatory change
- new technology trend
- merger / acquisition
- significant change request
- architecture lifecycle
- decide whether to initiate a new ADM cycle

## Exemple MayaBank — Phase G

Le delivery remplace le mécanisme IAM approuvé par une solution locale non standard afin de respecter le planning.

Réflexe :

1. constater l’écart ;
2. analyser impact et risque ;
3. réaliser la Compliance Review appropriée ;
4. gouverner une correction ou une exception ;
5. maintenir la traçabilité.

Ce n’est pas d’abord Phase H : le sujet principal est la **conformité de l’implémentation actuelle**.

## Exemple MayaBank — Phase H

Six mois après la première migration, une nouvelle réglementation modifie fortement les exigences de traçabilité des paiements.

Réflexe :

1. capturer la nouvelle requirement ;
2. évaluer son impact ;
3. déterminer l’importance du changement ;
4. décider s’il faut une modification locale ou un nouveau cycle ADM.

## Requirements Management dans les deux

Requirements Management reste transversal :

- en G, une deviation peut affecter des requirements ;
- en H, un nouveau driver peut créer de nouvelles requirements.

Il ne remplace ni G ni H.

## Pièges d’examen

- « Écart pendant l’implémentation » → penser **G**.
- « Nouveau driver après changement du contexte » → penser **H**.
- Une exception n’est pas une permission informelle : elle doit être **gouvernée et traçable**.
- H ne signifie pas « attendre la fin du système » : change management est continu.

## Mémo

> **G = Govern the implementation.**
>
> **H = Handle architectural change.**

## English for Architects

> Phase G governs implementation compliance. Phase H governs how the architecture responds to significant change over time.
