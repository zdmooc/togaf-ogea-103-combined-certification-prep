# Renforcement X2202 — conformité et stratégies de migration (XP33–XP36)

Cas originaux complémentaires ; les barèmes 5/3/1/0 sont pédagogiques et ne constituent pas une calibration officielle.

## XP33 — L2.1.5 : Compliant ou Conformant ?

L'architecture approuvée du service de paiement exige trois capacités : **idempotence**, **chiffrement** et **audit des rejets**. La première wave a livré exactement idempotence et chiffrement, sans fonction additionnelle ni contradiction. Le rapport de test prouve la conformité de ces deux réalisations ; l'audit des rejets est prévu dans la wave suivante. Le Board demande le niveau de conformité applicable **à cette livraison** et la suite de gouvernance.

Quelle décision choisir ?

A. La qualifier **Conformant**, car chaque fonctionnalité implémentée respecte bien sa définition approuvée, puis clôturer la revue.
B. La qualifier **Compliant**, expliciter le périmètre des fonctionnalités encore absentes et suivre la livraison de l'audit dans le contrat et la roadmap.
C. La qualifier **Consistent** à titre provisoire, enregistrer les preuves des deux fonctions et attendre la wave suivante pour confirmer le classement précis.
D. La qualifier **Fully Conformant**, en traitant l'absence d'audit comme un détail opérationnel sans impact sur la classification.

## XP34 — L2.1.5 : Fonction additionnelle et conformité

La cible d'une API de gestion de mandats impose **authentification forte** et **journalisation auditable**. La solution en service réalise intégralement ces deux exigences et ajoute un service facultatif de reporting qui n'est pas mentionné dans la spécification. Ce reporting n'enfreint aucun principe ou standard. La revue demande d'appliquer avec précision les niveaux TOGAF et de signaler le besoin éventuel de tracer cette extension.

Quelle décision est la meilleure ?

A. Déclarer **Compliant** parce que deux exigences ont été vérifiées, sans tenir compte du fait qu'elles couvrent toute la spécification.
B. Déclarer **Fully Conformant** puisque le reporting supplémentaire ne contrevient pas aux exigences écrites.
C. Déclarer **Non-conformant** à cause de la fonctionnalité supplémentaire, même si elle ne viole aucun élément spécifié.
D. Déclarer **Conformant**, car tous les éléments spécifiés sont réalisés et une fonction additionnelle existe ; documenter cette extension si elle affecte le Landscape ou la gouvernance.

## XP35 — L2.5.3 : Greenfield et Evolutionary combinés

Un groupe bancaire lance un **nouveau service indépendant d'alertes** qui ne possède aucune Baseline applicative et peut être construit sur une nouvelle plateforme. En parallèle, il modernise un moteur de compensation lié à sept partenaires legacy, avec coexistence obligatoire pendant six mois. Les deux chantiers appartiennent au même programme mais leurs risques et dépendances diffèrent.

Quelle stratégie est la mieux fondée ?

A. Utiliser **greenfield** pour le nouveau service et **evolutionary** pour le moteur de compensation, puis expliciter les transitions et contrôles de coexistence.
B. Appliquer **evolutionary** aux deux chantiers ; la continuité prime, puis réévaluer la pertinence de la coexistence pour le service neuf.
C. Appliquer **greenfield** aux deux chantiers en retenant les exigences de la Target comme seul point de départ ; les partenaires adapteront ensuite leurs interfaces.
D. Préférer une bascule **revolutionary** pour les deux chantiers afin d'avoir un seul jalon de production et de contrôle.

## XP36 — L2.5.3 : Une date réglementaire change la stratégie

Une banque doit remplacer un composant de vérification qui ne pourra plus recevoir de données après la date d'arrêt de son agrément. Une coexistence de l'ancien et du nouveau composant serait illégale après cette date. Un autre composant d'orchestration, non concerné par cette interdiction, dessert des partenaires externes qui imposent au contraire plusieurs vagues de migration. Les tests de réversibilité et la readiness font partie des contraintes.

Quelle recommandation convient ?

A. Employer **evolutionary** partout et maintenir une coexistence temporaire même après la date réglementaire, en demandant une dérogation plus tard.
B. Employer **greenfield** pour tous les composants, en considérant les dépendances partenaires comme des problèmes de delivery.
C. Préparer une bascule **revolutionary** gouvernée pour le composant réglementé avant la date limite, et une stratégie **evolutionary** avec transitions pour l'orchestration partenaire.
D. Choisir une bascule **revolutionary** pour tout le programme afin de limiter le nombre de versions et de réduire la durée des migrations.
