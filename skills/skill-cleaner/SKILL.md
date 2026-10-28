---
name: skill-cleaner
description: >-
  Quand un skill ou un parc de compétences est mal rangé, dupliqué, peu visible
  ou devenu incohérent, examiner propriétaire, niveau, contenu et disponibilité
  avant de décider garder, alléger, intégrer, déplacer, rendre dormant ou
  archiver. Couvre également la revue multi-projets, le diagnostic des
  compétences à partager, la recherche de capacités voisines, la migration
  entre projets et le rafraîchissement de l'inventaire utilisable par une
  marketplace. Pour écrire ou refondre le contenu d'un skill, déléguer à
  /skill-quality-guard et au skill-creator officiel d'Anthropic.
---
# skill-cleaner — auditer et organiser un parc de compétences

**Propriétaire de la revue du parc**, pas de la création d'un `SKILL.md`.
Intervient à la demande pour une compétence dans son contexte ou lors d'une
revue complète, dans un projet ou plusieurs. `/optimise-systeme` peut le
mobiliser si l'architecture des compétences pose problème.

## Les quatre décisions, dans l'ordre

1. **Niveau** : quel projet, sous-dossier ou bibliothèque possède ce geste ?
   La méthode métier reste chez son propriétaire, même si elle sert ailleurs.
2. **Responsabilité** : pourquoi la compétence existe-t-elle séparément de
   son parent et de ses voisines ? Un déclencheur différent ne suffit pas.
3. **Non-perte** : pour toute partie déplacée ou retirée, quelle destination
   conserve son contenu et sa raison ?
4. **Verdict** : GARDER, GARDER+SIMPLIFIER, INTERNE, INTÉGRER,
   DÉPLACER, DORMANT, ARCHIVER ou DÉCISION REQUISE.

Un fichier rarement appelé n'est pas automatiquement inutile. Une copie
accessible depuis un autre projet peut être un pont légitime et non un doublon.

## 0. Cibler le périmètre

À partir de la demande, déterminer les dépôts/dossiers et les compétences
concernées. Respecter leurs règles de protection et leur état de travail.
Lire les inventaires existants lorsqu'ils sont récents, puis vérifier leur
fraîcheur avant de s'en servir. Sur une petite demande, ne pas transformer
le diagnostic en inventaire de tous les projets.

## 1. Inventorier

Lister les compétences actives, dormantes, les niveaux, leurs références,
leurs dépendances, leur déclaration de déclenchement et leurs appelants.
Différencier cinq preuves : présent sur disque, exposé à l'hôte, découvert
dans une tâche neuve, invoqué naturellement, utile sur le cas demandé.
Ne pas confondre silence des journaux et absence d'usage manuel.

Le script optionnel `scripts/inventaire.py` construit un inventaire
portable depuis les dossiers fournis et peut produire `--json` pour un
catalogue. Un inventaire n'est pas un verdict de qualité.

## 2. Examiner chaque compétence avant de trancher

Lire réellement le `SKILL.md` et les références nécessaires ; un titre
similaire ne suffit pas pour conclure à un doublon. Distinguer :
méthode, contrat produit, état temporaire, preuve, historique et renvois.
Demander pour chaque compétence : quelle entrée, quel geste, quel résultat,
quel risque et quelle responsabilité la rendent distincte ?

Comparer les méthodes officielles installées aux wrappers privés :
un wrapper qui apporte une adaptation réellement nécessaire peut rester ;
un wrapper qui ne fait que recopier est un candidat à intégrer.
Une évaluation externe est une comparaison documentée, pas une installation.

## 3. Destiner le contenu avant tout déplacement

Pour chaque bloc supprimé de la surface active, noter sa destination :
compétence propriétaire, référence, documentation du produit, test ou
archive. Une simple réduction du nombre de lignes n'est pas une preuve.
Préserver les fichiers et décisions non lus plutôt que les archiver
à l'aveugle. Pour toute modification structurelle, produire un delta
et une procédure de retour arrière.

## 4. Exécuter avec les vrais propriétaires

- Déplacement ou changement de niveau : préserver les appels entre projets.
- Fusion, scission ou refonte de contenu : appeler `/skill-quality-guard`,
  qui utilise `skill-creator` pour écrire et évaluer.
- Modification d'une règle ou d'un hook : `/clean-rules-cleanup` ;
  les autorisations nécessaires pour les hooks restent applicables.
- Documentation ou copie distribuée devenue fausse : `/propage-systeme`
  et, pour un pack, le mode resynchroniser de `/skill-quality-guard`.

Ne pas modifier les surfaces protégées sans autorisation. Une suppression
irréversible, un changement de nom utilisé par l'utilisateur ou une
perte potentielle de capacité exige une décision explicite. Les gestes
réversibles déjà autorisés peuvent être appliqués avec preuves.

## 5. Modes spécialisés du même propriétaire

- **Revue multi-projets / périodique** : comparer niveaux, copies,
  worktrees et preuves de présence, puis traiter par petites vagues.
- **Répartition des responsabilités** : désigner une source canonique
  par méthode et des renvois dans les autres dépôts.
- **Recherche externe** : évaluer l'existence d'une compétence officielle
  ou publique avant de construire ; ne rien installer sans demande.
- **Partage d'une compétence** : distinguer méthode portable et données
  personnelles ; conserver les capacités dans le pack adapté.
- **Migration entre projets** : préserver les ponts et vérifier les
  consommateurs avant de retirer l'emplacement d'origine.
- **Inventaire et marketplace** : régénérer un inventaire à partir des
  sources actives, puis utiliser le générateur propriétaire du site s'il
  est disponible. Ne pas prétendre avoir déployé un catalogue à partir
  du seul export JSON.

## Fini quand

La carte des responsabilités est compréhensible ; chaque compétence du
périmètre a un verdict fondé sur son contenu ; les informations déplacées
restent accessibles ; aucune route active ne pointe vers une cible retirée ;
les tests et la disponibilité sont vérifiés au bon niveau.

Sortie courte : `périmètre | verdict par compétence | changements effectués |
preuves | écarts et décisions requises`. Distinguer un plan d'une
exécution et un inventaire d'une invocation réellement testée.
