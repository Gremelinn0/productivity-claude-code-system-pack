# Resynchroniser une copie distribuée

Le mode resynchroniser de /skill-quality-guard maintient une copie publique ou partagée **avec les mêmes responsabilités et capacités que sa source**.

## Comparer trois états
- La dernière base commune vérifiable.
- La compétence source actuelle.
- La copie distribuée actuelle.

Si la base commune manque, comparer les capacités une par une et déclarer cette limite. Ne jamais choisir une version parce qu'elle a une date plus récente.

## Reporter les évolutions
- Faire la liste des fonctions, modes, dépendances, entrées, sorties et contrôles de la source.
- Retrouver chaque fonction dans la copie ; une responsabilité absente est un défaut à corriger.
- Adapter chemins, exemples, références, outils et permissions propres à l'environnement ; fournir les équivalents utilisables lorsque nécessaire.
- Rejouer les modifications pertinentes dans la copie plutôt que d'écraser ses adaptations.
- Ne pas faire remonter les adaptations publiques vers la version personnelle.
- Préserver la licence et vérifier les fichiers associés : références, scripts, outils et documentation.

## Contrôler
- Vérifier que les dépendances indiquées sont installables et accessibles.
- Exécuter des demandes représentatives pour chaque mode sur les deux versions.
- Comparer les comportements et preuves, pas seulement le texte.
- Rechercher les chemins personnels et informations non destinées au partage.
- Vérifier les liens et l'installation depuis un environnement neuf.

Verdict : ALIGNÉ, ÉCART ou NON TESTÉ. Ne jamais annoncer une parité complète uniquement sur la base d'une comparaison documentaire.
