---
name: optimise-systeme
description: >-
  Améliorer un système IA existant pour mieux atteindre son objectif : architecture, agents,
  outils, données, mémoire, contexte, règles, compétences, routines et validation humaine.
  Partir du résultat recherché, lire la carte locale, diagnostiquer, choisir les changements,
  faire intervenir les propriétaires, vérifier leur effet et capitaliser les acquis.
  Utiliser sur « optimise le système », « améliore mes agents », « revois l'architecture »,
  « rends ce système plus fiable », « réduis le travail manuel » ou un problème transverse.
  Une intervention ciblée ne lance pas une revue générale ; nettoyer est un moyen, pas le but.
  Une leçon déjà connue à intégrer relève de /capitaliser ; un système entièrement neuf du
  parcours de création. Respecter diagnostic seul, permissions et limites du mandat.
metadata:
  role: orchestration
  owns: "l'amélioration du résultat d'un système existant et la coordination de ses changements"
  scope: "système de travail ou système métier identifié, dev et non-dev"
  consumes: "objectif, carte locale, état canonique, preuves, contraintes et spécialistes disponibles"
---

# /optimise-systeme — améliorer le système, pas seulement le ranger

<!-- capitaliser:squelette-v1 -->

## Résultat et responsabilité

Une seule porte conduit l'amélioration de l'existant. Elle absorbe le pilotage de
`/router-ameliorer-systeme-ia` et l'aiguillage de `/router-entretien-systeme`.
Ces anciens noms ne gardent qu'une compatibilité, jamais une méthode concurrente.

Le résultat recherché peut être une meilleure qualité, une reprise fiable, moins de travail
humain, un délai réduit, un coût maîtrisé ou une capacité manquante. Ajouter un agent, une
règle ou un contrôle peut être juste ; supprimer des fichiers ne prouve aucun gain.

Cette compétence garde la responsabilité du résultat et des arbitrages. Les spécialistes
possèdent leurs méthodes ; les opérateurs métier continuent d'opérer leurs systèmes.
La carte et les données du système restent chez lui, pas dans cette compétence globale.

## Stratégie et choix du parcours

Lire la [carte des responsabilités](references/responsabilites.md), puis les
[adaptations de l'environnement](references/adaptations-locales.md).

- **Acquis déjà identifié à intégrer** : transmettre une fois à `/capitaliser`, sans diagnostic général.
- **Demande précise sur une règle ou un parc de compétences** : confier au spécialiste approprié.
- **Amélioration d'un système existant** : conduire les étapes ci-dessous.
- **Création d'un système entièrement neuf** : transmettre au parcours de création disponible et sortir.
- **Avis, audit ou plan seulement** : produire le diagnostic ou le plan ; aucune mutation.

Une demande combinée « améliore et capitalise » est une seule intervention pilotée ici,
avec une clôture par `/capitaliser`. Ce n'est pas deux orchestrateurs qui se rappellent.
Les modes sont une profondeur de travail, pas des commandes supplémentaires : ciblé,
architecture structurelle, revue complète explicitement demandée.

## Étapes

### 1. Reprendre le système et l'objectif

Identifier le système, son opérateur, son état et le résultat attendu. Lire ses sources
actuelles : carte, plan, décisions, contrats des agents et routines, données ou traces utiles.
Réutiliser ces documents. Si la carte manque, reconstituer une vue bornée depuis les sources
accessibles ; ne pas inventer un état ni créer un second cockpit ou un second registre.

Une compétence locale `/system` n'est pas présumée présente. Découvrir son vrai nom et ne
l'utiliser que pour les connaissances locales, pas pour lancer une deuxième optimisation.
Le kit et le registre de `systeme-ia`, lorsqu'ils existent, sont du contexte partagé avec la
création ; ce ne sont ni une étape d'exploitation ni un arbitre supplémentaire.

Fixer le périmètre, les invariants et le mode autorisé. Ne pas redemander un accord déjà donné.
Une demande d'optimisation n'autorise pas un envoi externe, une dépense, une modification de
droits, un hook, une nouvelle routine ou un changement de production non couvert par le mandat.

### 2. Établir le point de départ

Choisir une mesure qui juge le but : résultat utile, erreurs, reprises, étapes humaines,
délai, coût ou couverture. Distinguer observation, hypothèse causale et décision.
Utiliser les instruments du propriétaire avant d'en improviser un autre.

Documenter objet, version, périmètre, échantillon, protocole et limites. L'absence d'accès,
un inventaire vide ou des traces insuffisantes rendent la mesure non disponible, pas zéro.
Les volumes de règles ou de compétences sont des indicateurs de structure, pas le verdict
sur la qualité. Une règle de longueur ne remplace pas le chargement utile.

### 3. Diagnostiquer puis choisir

Examiner la chaîne de bout en bout, pas seulement chaque pièce isolée : entrées, agents,
transmissions, outils, état, validations et sorties. Localiser le défaut ou l'occasion de
progrès, puis comparer les options, y compris ne rien changer.

Pour un changement structurel, ouvrir les options, expliciter les compromis et soumettre
le plan à une contradiction avant l'exécution. Lire le
[parcours d'architecture](references/architecture-et-mesures.md) : avis critique, dessin,
décision et invariants restent quatre contributions distinctes. Dans l'environnement qui
les possède, charger tous les experts prévus, dans l'ordre ; ne pas remplacer cette exigence
par « choisir le meilleur ». Un correctif local sans changement d'architecture n'impose pas
ce parcours complet.

Un plan déjà autorisé se déroule. Une décision nouvelle hors délégation est isolée avec son
impact ; elle ne bloque pas les travaux indépendants déjà autorisés.

### 4. Faire réaliser les changements

Pour chaque changement, nommer l'objet, son propriétaire réel, l'effet attendu, les surfaces
concernées, les droits, les preuves et le retour arrière. Une action nouvelle doit avoir un
responsable exécutable : réutiliser un agent ou un script existant ; s'il faut en construire
un, le faire dans le mandat plutôt qu'inventer son nom ou un poste prétendument pourvu.

Transmettre le contrat d'intervention : objectif, origine, limites, sources/version, opérations
déjà faites, résultat attendu. Les spécialistes retournent leur résultat au pilote ; ils
n'ouvrent pas un nouveau pilotage. Choisir seulement les spécialistes utiles à cette passe :

| Objet à modifier | Propriétaire |
| --- | --- |
| Règle, portée d'une consigne, hook proposé | `/clean-rules-cleanup` ; accord propre aux hooks conservé |
| Organisation, doublons, fusion ou migration du parc | `/skill-cleaner` |
| Création, refonte, qualité ou copie distribuée d'une compétence | `/skill-quality-guard` et ses outils disponibles |
| Agent, outil, code, données, routine, interface | opérateur métier et constructeur réellement disponibles |
| Consommateurs devenus faux | `/propage-systeme` ou propriétaire de la surface |

Préserver les travaux concurrents. Modifier le minimum nécessaire, sans quota arbitraire de
fichiers. Une fusion conserve les capacités utiles et migre les appelants ; les anciennes
adresses restent des alias tant que leur retrait n'est pas prouvé sûr.

### 5. Vérifier l'effet et les régressions

Relire les cibles réellement écrites et rejouer les contrôles adaptés. Un test de contrôle
inclut un cas acceptable et un défaut qu'il doit refuser, dans une copie isolée de l'objet.
Vérifier les contrats entre composants : des composants sains séparément peuvent être faux
ensemble. Comparer au point de départ avec un protocole et une population comparables.

Distinguer fichiers conformes, chaîne exécutée et résultat métier amélioré. Quand une preuve
d'usage exige un hôte ou un accès absent, déclarer exactement ce qui n'est pas mesuré.
Ne pas relancer un test live interdit ni provoquer un envoi réel pour obtenir un vert.
Pour une revue complète, lire [le protocole de revue](references/passe-certifiante-regles-competences.md).

### 6. Réconcilier et capitaliser une fois

Mettre à jour la carte, le plan et les descriptions devenus faux **dans leurs maisons locales**.
Faire propager les changements autorisés, puis transmettre à `/capitaliser` les décisions,
preuves, livrables et conséquences déjà traitées. La capitalisation vérifie les restes ; elle
ne rejoue pas une propagation terminée et ne rappelle pas cet optimiseur automatiquement.

Une contradiction nouvelle hors périmètre devient un reste avec destinataire existant,
prochaine action et critère de clôture. Pas de boucle de routage, de tâche fantôme ou de
nouvelle routine. Sans changement de preuve ou d'état, ne pas refaire la même opération.

## Décisions et frontières

Le nettoyage est un levier ; le but est le résultat. La cartographie est locale ; la méthode
est commune. La création d'un système neuf reste distincte de son amélioration. Une correction
localisée ne fusionne pas tout le parc. Les spécialistes restent directement invocables.
Aucun seuil de lignes, de fichiers, de jetons ou de durée ne certifie une amélioration.

## Sortie et définition de fini

Rendre : objectif et périmètre ; changements réellement faits ; effet mesuré ou non mesuré ;
preuves ; reste et prochain geste. Employer le verdict exact :

- **PROPOSITION** : diagnostic/plan rendu, aucune exécution revendiquée.
- **APPLIQUÉ ET MESURÉ** : changements vérifiés et critère de réussite effectivement exercé.
- **APPLIQUÉ, EFFET NON MESURÉ** : écritures prouvées, résultat d'usage encore non vérifié.
- **PARTIEL / BLOQUÉ** : résultat incomplet, dépendance ou autorisation manquante nommée.
- **SANS CHANGEMENT** : pas d'amélioration justifiée, raison et périmètre observé explicites.

Une compétence, un script ou une branche présents ne prouvent pas leur découverte ni leur
exécution dans un hôte neuf. Les essais correspondants sont dans
[evals/evals.json](evals/evals.json). Le contrôle de la structure d'orchestration est
`scripts/verifier_orchestration.py` ; il ne simule pas un agent.

<!-- dev-qa-link -->
**Production** : changements candidats conduits chez leurs propriétaires.
**Test** : contrôles locaux et chaîne autorisée, témoins qui savent refuser.
**QA** : résultat du système et non-régression, au bon niveau de preuve.
**Cadence** : aucune ; ne pas créer de minuteur ou de boucle de travail par cette refonte.
