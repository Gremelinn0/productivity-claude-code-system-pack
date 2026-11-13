# Audit de la candidate — 13 novembre 2026

## Ce qui a changé

Le renommage historique ne suffisait pas : le cœur générique et les annexes centrées
sur le développement se contredisaient. La candidate emploie désormais le même cœur de
capitalisation pour tous les métiers ; les adaptations changent uniquement les supports,
les droits, les destinations et les contrôles disponibles.

Le cœur couvre : sélection des acquis ; propriétaire et antécédent ; point de chargement ;
fait et raison ; décisions/refus/mesures/hypothèses ; livrables ; concurrence et permissions ;
propagation aux lecteurs actuels et futurs ; non-perte ; relecture et verdict explicite.
Les anciennes versions restent dans l'historique Git, pas dans la méthode active.

## Preuves effectuées dans cette passe

- 39 tests unitaires du contrôle de présence textuelle, exécutés localement avec succès.
- Codes de sortie CLI 0/1/2/3 exercés : conservé, perte, mesure impossible et transformation à relire.
- Mutation d'une copie du vrai SKILL candidat : retrait d'un bloc de mandat refusé ;
  conservation de ce seul bloc en archive encore refusée ; déplacement intact en référence active accepté.
- YAML strict, références de la compétence, syntaxe Python et présence des scénarios contrôlés localement.
- Auto-test du validateur YAML du pack : un cas sain accepté et huit défauts refusés.
- Empreintes Git du cœur, de ses références communes et des scripts identiques entre les
  copies candidates privée et publique. Les seuls détails d'environnement sont séparés.

Ce sont des preuves documentaires et mécaniques, pas des preuves de comportement d'un modèle.
La comparaison vérifie la présence du texte ; elle ne certifie pas son sens ou son chargement.
Le contrôle documentaire du pack entier doit aussi passer sur l'arbre distant candidat.

## Ce qui reste explicitement non prouvé

- Les 16 scénarios dans une session neuve Claude Code ou Codex, notamment sans Git,
  en lecture seule, avec un conflit concurrent et avec des données métier individuelles.
- L'installation et la sélection naturelle des compétences depuis le catalogue de l'hôte.
- La parité de comportement avec/sans adaptations locales.
- La synchronisation des machines et des catalogues de sessions déjà ouvertes.

Ne pas publier une promesse de ces résultats ni présenter cette branche comme une release
reçue avant de disposer des traces correspondantes. Le carrousel doit décrire les capacités
réellement réceptionnées, pas transformer ces tests à jouer en tests réussis.
