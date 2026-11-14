# Deux entrées, des spécialistes, un contexte local

Cette carte porte les frontières du pack. Les méthodes restent dans chaque compétence.

| Intention | Entrée ou propriétaire | Ne fait pas |
| --- | --- | --- |
| Améliorer le résultat de l'existant, choisir ce qui doit changer | optimise-systeme | Se réduire à un ménage ou opérer tous les métiers lui-même |
| Intégrer une décision, une leçon ou un livrable déjà acquis | capitaliser | Ouvrir une refonte globale à chaque correction |
| Gérer une règle et son mécanisme d'application | clean-rules-cleanup | Décider seul d'une fusion du parc ; modifier un hook sans accord |
| Organiser, fusionner, déplacer, archiver les compétences | skill-cleaner | Réécrire toutes les méthodes ni posséder la carte métier |
| Fabriquer, refondre, vérifier une compétence ; synchroniser sa copie | skill-quality-guard | Remplacer le pilotage global ou inventer une évaluation non exécutée |
| Corriger les consommateurs rendus faux par un changement connu | propage-systeme | Redécider le changement ou devenir un second pilote |
| Bâtir un système entièrement neuf | parcours de création disponible | Réappliquer huit étapes de création à tout système existant |
| Opérer un système métier | sa compétence opératrice | Devenir une copie locale de l'optimiseur global |

## Compatibilité

- router-ameliorer-systeme-ia → optimise-systeme.
- router-entretien-systeme → optimise-systeme ; pour une demande précise, il choisit le propriétaire une seule fois.
- router-capitalisation → capitaliser.
- dev-capitaliser → capitaliser avec le profil du projet, lorsqu'un ancien appel existe.

Les alias ne contiennent ni workflow ni doctrine. Ils restent invocables pendant la migration :
interdire leur invocation avant de migrer les appelants casserait la compatibilité.
Ne pas ajouter les alias absents à un pack qui ne les a jamais distribués.

## Contrat d'intervention et anti-boucle

Le pilote transmet objectif, origine, périmètre, autorisations, sources/version, opérations déjà
faites et preuves attendues. Une trace existante suffit ; pas de registre automatique nouveau.
Identifier une opération par son objet canonique, le geste, le périmètre et la version de départ,
pas par sa formulation. Un résultat déjà traité se réutilise tant que ses hypothèses sont valides.

Un spécialiste rend son résultat à l'appelant, pas à un autre pilote. Capitaliser ne rappelle
jamais automatiquement optimise-systeme ; il rend une proposition distincte si une refonte est
nécessaire. Propager ne rappelle pas capitaliser pour le même changement. Le pilote clôt une
fois. Une modification de la preuve ou de l'objectif peut justifier une nouvelle intervention,
jamais la seule récursion de noms.

Le fichier `contrat-orchestration.json` décrit ces relations pour les contrôles structurels.
Il ne décide pas à la place d'un agent et ne certifie pas ses appels réels.
