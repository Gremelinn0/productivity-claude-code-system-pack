# Candidate du 14 novembre 2026 — simplifier le pilotage, garder les capacités

## Décision

Deux commandes principales : optimise-systeme conduit l'amélioration du résultat d'un système
existant ; capitaliser intègre les acquis et leurs conséquences. Les quatre spécialistes restent
indépendants. Les cartes et opérateurs métier restent locaux ; créer un système neuf est un autre parcours.

## Changements

- Optimise-systeme n'est plus défini par le grand ménage à froid ou une réduction obligatoire.
- Capitaliser intègre la recherche d'impact auparavant séparée du rangement.
- Router-entretien-systeme devient un alias sans méthode ; les autres anciens noms ne sont pas
  installés dans ce pack s'ils n'y existaient pas.
- Les opérations déjà traitées sont transmises et réutilisées ; pas de rappel automatique du pilote.
- Les permissions, la concurrence, la conservation et la preuve d'usage restent explicites.
- README, descriptions des manifestes, contrats et CI sont alignés sur ces responsabilités.

Les versions antérieures sont conservées dans Git. Une archive ou un diff ne prouvent pas
l'équivalence fonctionnelle : vérifier les capacités et les scénarios.

## Vérifications et limites

40 nouveaux tests locaux : 26 pour le graphe/les alias et 14 pour la recherche d'impacts.
Les 39 tests antérieurs de non-perte sont conservés ; la CI du candidat doit les rejouer avec
les nouveaux tests et les validations documentaires. Le résultat de cette exécution est à lire
dans la PR, pas à déduire de ce document.

16 nouveaux scénarios d'orchestration sont écrits et marqués NOT_RUN_ON_FRESH_AGENT_HOST.
Aucune installation, découverte naturelle ni parité de comportement ne sont annoncées comme
prouvées par ces tests Python. La candidate n'est pas fusionnée dans main ni publiée comme release.

## Avant diffusion

Recevoir les essais d'hôte, migrer les consommateurs/projections restants, vérifier les adaptations,
mettre à jour la version de distribution et tester l'installation. L'ancien alias n'est retiré
qu'après preuve que ses appelants ont migré. Le carrousel doit montrer deux entrées et les
spécialistes, pas remettre l'alias au même niveau que les responsabilités réelles.
