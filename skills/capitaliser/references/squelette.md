# Le squelette — le gabarit des 4 fichiers, et comment on descend un bloc

> Annexe de **`/capitaliser`**. À lire une fois, quand on pose le squelette sur un morceau neuf.

## Le gabarit du contrat

```markdown
# CONTRAT — <morceau>

> La première chose qu'on charge, et la seule obligatoire. Quatre volets. Le SKILL.md et les
> documents derrière ne s'ouvrent que quand il manque un détail précis.

## 1 · CE QUE CE MORCEAU DOIT FAIRE
   la mission · à moi / pas à moi et vers qui ça route · la frontière qui le justifie
   📍 Le détail : <adresses>

## 2 · CE QUI EST DÉJÀ PROUVÉ OU TRANCHÉ — ne pas re-décider, ne pas re-mesurer
   TRANCHÉ / PROUVÉ / PARTIEL / NON MESURÉ, chacun daté
   📍 Le détail : decisions.md · <adresses>

## 3 · LES PIÈGES DÉJÀ PAYÉS SUR CE MORCEAU
   un par bloc, avec ce qu'il a coûté et la leçon en une phrase
   📍 Le détail : pieges.md · un fichier de référence transverse

## 4 · LES DIFFÉRENCES PAR PLATEFORME
   le commun d'abord, l'exception écrite ensuite
   📍 Le détail : plateformes.md · la fiche de l'environnement
```

## Comment on descend un bloc du SKILL.md — cinq gestes

1. **LIRE** le fichier en entier. Pas de ratio, pas de ressemblance de titre : la lecture.
2. **Repérer par CONTENU**, jamais par numéro de ligne — un index est périmé à la seconde où on
   l'écrit, et l'assertion casse en silence pendant que le commit part quand même.
3. **Déplacer le bloc ENTIER, verbatim.** Découper sémantiquement, c'est réécrire.
4. **Poser un en-tête** qui dit : l'objet, quand l'ouvrir, d'où le contenu vient et à quelle date.
5. **PROUVER la non-perte** contre `git show HEAD:<fichier>` — chaque ligne de fond de l'ancien
   fichier doit se retrouver dans l'union des nouveaux. Zéro perdue, ou la passe s'arrête.

⚠️ **Le témoin positif est obligatoire** : afficher le nombre de lignes lues depuis `git`. Sans lui,
un zéro de perte est indistinguable d'un fichier qu'on n'a jamais réussi à lire.

## Ce qui reste dans le SKILL.md

La règle · l'interdit · l'ordre à respecter · le contrôle décidable · le pointeur vers les annexes ·
le bloc `<!-- dev-qa-link -->`. **Le test du lecteur pressé** : il n'ouvre que le `SKILL.md` et doit
repartir avec tout l'opérationnel. S'il lui manque un geste, on a trop descendu ; s'il traverse trois
écrans de récit avant le premier geste, on n'a pas assez descendu.
