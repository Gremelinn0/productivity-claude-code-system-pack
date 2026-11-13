# Claude Code System Pack

**Trois commandes au quotidien, trois spécialistes et un routeur facultatif.**
Entretenir le savoir, les règles et les compétences d'un agent après un travail réel.
Développement, rédaction, recherche, marketing, CRM et opérations : la méthode s'adapte
aux sources et aux outils disponibles, pas l'inverse.

> **Branche candidate — validation en cours.** Cette refonte n'est pas encore la version
> distribuée depuis `main`. Les tests documentaires et mécaniques ne prouvent pas à eux
> seuls l'installation ni le comportement dans une session neuve. État et limites :
> [audit de capitalisation](docs/audit-capitaliser-2026-11-13.md).

## Choisir la bonne entrée

| Situation | Commande courte dans cette documentation | Résultat attendu |
| --- | --- | --- |
| Un travail produit un acquis ou un livrable à conserver | `/capitaliser` | Le fait, sa raison et le livrable sont retrouvables au bon endroit, avec une preuve de conservation. |
| Une règle est à créer, corriger ou déplacer | `/clean-rules-cleanup` | La règle vit au bon niveau ; un hook éventuel exige les droits correspondants. |
| Le système de la tâche devient incohérent ou inefficace | `/optimise-systeme` | Un diagnostic mesuré, puis les corrections autorisées chez leurs propriétaires. |

Ces entrées ne supposent pas qu'il faut exécuter tout le pack après chaque tâche.
Une capitalisation peut conclure qu'il n'y a rien de nouveau à écrire. Une optimisation
commence par le périmètre utile, pas par un audit de tous les projets.

## Les spécialistes

| Compétence | Responsabilité |
| --- | --- |
| `/skill-cleaner` | Comparer, ranger, fusionner ou archiver les compétences d'un parc, avec conservation et migration des appelants. |
| `/skill-quality-guard` | Fabriquer, refondre, vérifier et resynchroniser une compétence ; utiliser le `skill-creator` officiel quand il est disponible. |
| `/propage-systeme` | Actualiser les consommateurs et les surfaces humaines que le changement rend faux. |
| `/router-entretien-systeme` | Choisir le bon propriétaire à partir du symptôme, sans recopier sa méthode. Entrée facultative. |

Il y a **six propriétaires de travail et un routeur** dans cette candidate. Le nombre de
cartes d'un ancien post ne constitue pas l'inventaire du pack. Le contrat de responsabilités
est dans [docs/contrat-capacites.md](docs/contrat-capacites.md).

## Capitaliser sans être développeur

La compétence distingue le propriétaire, le support de conservation et le point où le
savoir sera réellement chargé. Une décision rejoint sa source ; une donnée client reste
sur sa fiche ; une leçon transversale rejoint la méthode ; un fichier produit reste
attaché au projet ou à son registre existant.

Elle ne prétend pas entraîner le modèle. Sans stockage accessible, elle indique
**NON PERSISTÉ**. Une propagation inachevée donne **PARTIEL**, pas « terminé ».
Git, Python et une arborescence de compétences ne sont pas imposés à un utilisateur de wiki
ou de CRM. Les adaptations locales précisent les adresses et les outils, sans constituer
une deuxième méthode. La copie publique conserve les capacités du cœur commun ; elle ne
contient ni les données privées ni les destinations personnelles de sa source.

## Installation et invocation

Les commandes suivantes installent la version distribuée de `main`, pas automatiquement
cette branche candidate :

```text
/plugin marketplace add Gremelinn0/productivity-claude-code-system-pack
/plugin install claude-code-system-pack
```

Dans une installation plugin, utiliser le nom qualifié présenté par le catalogue :

```text
/claude-code-system-pack:capitaliser
/claude-code-system-pack:clean-rules-cleanup
/claude-code-system-pack:optimise-systeme
```

Les noms courts des tableaux désignent les compétences ; ils peuvent différer des noms
exposés par l'hôte. Le `description` aide l'agent à les sélectionner : ce n'est pas une
garantie de déclenchement à chaque formulation. Vérifier la découverte et l'invocation
dans une session neuve après installation.

Sources officielles : [skills Claude Code](https://code.claude.com/docs/en/skills) et
[installation des plugins](https://code.claude.com/docs/en/discover-plugins).

## Dépendances et limites

- La méthode exige seulement les accès nécessaires aux sources du travail, dans le mandat.
- Les contrôles Python fournis sont des outils à exécuter, pas des hooks installés silencieusement.
- `capitaliser/scripts/verification.py` utilise Python 3.10+ et sa bibliothèque standard.
  Le contrôle YAML strict et les outils qui importent `yaml` utilisent PyYAML ; la CI fixe
  `PyYAML==6.0.3`. Une dépendance manquante signifie contrôle non exécuté.
- Les essais sur documents locaux ne prouvent pas ceux d'un connecteur, d'un CRM ou d'un
  autre système d'exploitation. Ne pas déduire une compatibilité runtime d'un import Python.
- Les opérations externes, dépenses, modifications de droits et changements de production
  exigent leur autorisation propre. Mémoriser une décision ne l'exécute pas automatiquement.

Pour fabriquer ou évaluer une compétence, la dépendance officielle est séparée :

```text
/plugin install skill-creator@claude-plugins-official
```

Elle n'est ni recopiée ni installée sans autorisation. En son absence, la revue disponible
est décrite comme telle ; aucune évaluation indépendante n'est inventée.

## Vérifications reproductibles

Depuis la racine du dépôt candidat :

```text
python -m pip install PyYAML==6.0.3
python scripts/verifier_pack.py --self-test
python scripts/verifier_pack.py
python -m unittest discover -s skills/capitaliser/tests -v
python skills/capitaliser/scripts/verifier_contrat.py skills/capitaliser
```

Le contrôle de non-perte refuse une comparaison vide, une source absente et une archive
utilisée à la place d'une destination active. Une reformulation déclarée renvoie un état
**à relire**, pas une certification automatique de son sens.
Les scénarios de comportement se trouvent dans `skills/capitaliser/evals/evals.json`.
Leur présence ne prouve pas qu'ils ont été joués.

## Historique et licence

0.3.0 : renommage public de `dev-capitaliser` en `capitaliser`.
0.4.0 : ajout du routeur d'entretien. Cette branche poursuit la réconciliation des
responsabilités et des preuves ; aucune nouvelle release n'est annoncée avant réception.

Licence MIT. Les sources tierces gardent leurs auteurs et leur distribution d'origine.
