# Claude Code System Pack

**Deux commandes principales, quatre spécialistes.**
Améliorer un système IA existant et intégrer ce que le travail lui apprend, en développement
comme en recherche, rédaction, marketing, CRM et opérations.

> **Candidate en cours de réception, pas nouvelle release.** Cette branche n'est pas la version
> installée depuis `main`. Le numéro de distribution reste 0.4.0 jusqu'à réception et promotion.
> Les tests documentaires et Python ne prouvent ni la découverte naturelle ni le comportement
> dans une session neuve. État de migration : [deux entrées](docs/migration-deux-entrees.md).

## Les deux commandes à connaître

| Commande | La question de départ | Responsabilité |
| --- | --- | --- |
| `/optimise-systeme` | Que changer pour mieux atteindre notre objectif ? | Comprendre le système, diagnostiquer, comparer les options, faire réaliser les changements et vérifier leur effet. |
| `/capitaliser` | Comment intégrer ce que nous venons d'apprendre ? | Retrouver le propriétaire et l'antécédent, conserver le fait et sa raison, traiter les conséquences et garder les livrables retrouvables. |

L'optimisation n'est pas un grand ménage obligatoire. Elle peut ajouter une capacité manquante,
fiabiliser une reprise, améliorer la répartition du travail ou réduire l'effort humain.
La mesure porte sur le résultat recherché, pas uniquement sur le nombre de fichiers supprimés.

La capitalisation n'est pas un simple résumé. Elle peut corriger une règle ou une méthode
localisée, mais ne déclenche pas une refonte générale. Le tri d'impact et le rangement sont une
seule passe. L'optimisation se clôt par une capitalisation, pas par deux pilotes qui se rappellent.

## Quatre spécialistes, toujours accessibles directement

| Compétence | Responsabilité |
| --- | --- |
| `/clean-rules-cleanup` | Créer, corriger, retirer et placer les règles ; examiner leurs mécanismes d'application. Les hooks gardent leur autorisation explicite. |
| `/skill-cleaner` | Organiser, comparer, fusionner ou déplacer les compétences du parc sans perdre les capacités ni casser leurs appelants. |
| `/skill-quality-guard` | Fabriquer, refondre, vérifier et resynchroniser une compétence, avec les outils de création et d'évaluation disponibles. |
| `/propage-systeme` | Mettre à jour les consommateurs et les supports humains qu'un changement connu rend faux. |

Une demande précise peut aller directement à son spécialiste. Il n'est pas nécessaire de lancer
les six compétences après chaque tâche. Le système métier garde son opérateur, sa carte, son plan
et ses sources ; le pack ne recopie pas son état dans une compétence globale.

La [carte des responsabilités](skills/optimise-systeme/references/responsabilites.md) définit les
frontières. La création d'un système entièrement neuf reste un parcours distinct.

## Un ancien nom conservé, pas une troisième porte

`/router-entretien-systeme` est désormais un alias de `/optimise-systeme`, sans méthode propre.
Il reste invocable le temps de migrer les anciens appels. Le pack contient donc **six propriétaires
et un alias de compatibilité**, pas sept rôles équivalents. Les anciens noms privés mentionnés dans
la documentation ne sont pas ajoutés comme nouvelles compétences distribuées.

## Utilisation et limites

Les deux méthodes s'adaptent aux sources et outils accessibles. Pas de Git ou d'arborescence
imposés à un utilisateur de wiki ou de CRM. Une adaptation locale précise les destinations,
les droits et les dépendances ; elle ne retire pas les capacités du cœur commun.

Une source en lecture seule reste en lecture seule. Mémoriser une décision n'autorise pas un envoi,
un changement de production, une nouvelle routine ou une publication. Sans stockage vérifié,
`capitaliser` rend **NON PERSISTÉ** ; avec un reste réel, **PARTIEL**. Un modèle n'est pas entraîné
par cette opération et une mémoire automatique n'est pas garantie.

## Installation

Ces commandes installent la version distribuée depuis `main`, pas cette candidate :

```text
/plugin marketplace add Gremelinn0/productivity-claude-code-system-pack
/plugin install claude-code-system-pack
```

Dans une installation plugin, utiliser le nom qualifié exposé par le catalogue, par exemple :

```text
/claude-code-system-pack:optimise-systeme
/claude-code-system-pack:capitaliser
```

Vérifier le catalogue de l'hôte et l'invocation après installation. Une description facilite
la sélection ; elle n'en garantit pas le déclenchement dans toute formulation.

Pour fabriquer/évaluer une compétence, le `skill-creator` officiel est une dépendance séparée,
à résoudre dans le catalogue courant. Le pack ne le recopie et ne l'installe pas silencieusement.
Une dépendance absente est signalée ; aucun appel ni essai indépendant n'est inventé.

## Contrôles reproductibles

Python 3.10+ pour les scripts, PyYAML pour les contrôles YAML. Depuis ce dépôt candidat :

```text
python -m pip install PyYAML==6.0.3
python scripts/verifier_pack.py --self-test
python scripts/verifier_pack.py
python -m unittest discover -s skills/capitaliser/tests -v
python -m unittest discover -s skills/optimise-systeme/tests -v
python skills/optimise-systeme/scripts/verifier_orchestration.py --root skills
python skills/capitaliser/scripts/verifier_contrat.py skills/capitaliser
python skills/capitaliser/scripts/verifier_contrat.py skills/optimise-systeme
```

Le contrôle d'orchestration refuse un cycle dans le **graphe déclaré**, une entrée manquante ou
un alias redevenu propriétaire ; il ne prouve pas les appels réels d'un modèle. Le contrôle de
non-perte compare la présence textuelle : une reformulation demande encore une revue du sens.
Le chercheur d'impacts localise des occurrences, pas des contradictions sémantiques.

Les scénarios d'usage sont dans les dossiers `evals/` des deux entrées. Leur présence n'est pas
un résultat d'évaluation. Installation, usage en session neuve et bénéfice métier sont des
preuves distinctes des tests ci-dessus.

## Historique et licence

0.3.0 : renommage public de dev-capitaliser en capitaliser.
0.4.0 : ajout historique du routeur d'entretien.
Candidate actuelle : deux entrées principales et absorption des pilotages concurrents.
Aucune nouvelle release n'est annoncée avant réception.

Licence MIT. Les ressources tierces gardent leur distribution et leurs auteurs d'origine.
