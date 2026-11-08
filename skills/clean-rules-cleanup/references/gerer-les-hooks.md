# Entretenir les hooks

**Propriétaire :** /clean-rules-cleanup. Un hook n'est pas une règle de prose : il s'exécute sur un événement et peut provoquer un coût ou un refus.

## Inventorier avant de juger
- Lire les fichiers de configuration de l'hôte et de chaque projet concerné, puis les scripts réellement désignés.
- Consigner événement, filtre ou matcher, commande, fréquence probable et comportement.
- Distinguer trois classes : silencieux, rappel injecté dans le contexte, refus qui bloque l'action.
- Vérifier si une règle ou un autre hook produit déjà le même effet.
- Vérifier que chaque commande existe et répond aux entrées qu'elle reçoit.

## Mesurer et présenter
Pour chaque hook candidat : ce qu'il protège ; quel défaut réel justifie un déclenchement automatique ; ce que ses sorties ajoutent au contexte ; sa fréquence ; risque de faux positif ; alternative simple dans une compétence ou une règle.

Un rappel coûte surtout son contenu injecté à chaque déclenchement. Un refus coûte aussi les reprises qu'il provoque. N'annoncer aucun gain sans relevé de fréquence. Un hook silencieux peut tout de même coûter du temps d'exécution.

## Modification
Demander **l'accord explicite** avant tout ajout, modification ou suppression, même réversible. Une fois approuvé :
1. Préserver l'ancienne configuration et ne toucher qu'au périmètre décidé.
2. Étendre un mécanisme existant plutôt que créer un doublon.
3. Tester avec une entrée conforme et une entrée connue fautive, sans perturber les autres projets.
4. Vérifier l'événement réel et le comportement attendu ; une règle écrite n'est pas une preuve de déclenchement.
5. Mettre à jour les cartes et la documentation concernées, en passant par /propage-systeme si nécessaire.
6. Rendre le changement, les essais et le moyen de revenir en arrière.

L'absence d'accès aux fichiers de configuration signifie **non vérifié**, pas zéro hook.
