---
name: propage-systeme
description: >-
  Quand une modification du système vient d'être faite — une règle, une compétence, une décision
  d'architecture — la répercuter sur TOUTES les surfaces qui en parlent, en forçant celles que
  personne ne met à jour spontanément : les pages que des HUMAINS lisent. On corrige les fichiers
  que l'agent lit, on oublie ceux que les gens lisent, et ils travaillent alors sur du périmé.
  Triggers : « propage ça », « mets à jour le système », « répercute partout », « tu n'as pas
  propagé », « il faut que ce soit partout », « /propage-systeme ». Ce n'est pas une clôture de
  session, et ce n'est pas la mise à jour de la doc d'une fonctionnalité.
---

# propage-systeme — répercuter une modification sur toutes ses surfaces

## Le réflexe que cette compétence remplace

Quand on change quelque chose dans le système — une règle, une compétence, l'architecture, un outil
— il faut que ça se retrouve **partout où on va le relire**.

Du côté que l'agent lit (les fichiers de règles, les compétences), c'est souvent déjà fait, parfois
même automatiquement. **Le piège est du côté HUMAIN** : les pages, les tableaux de bord, les espaces
de travail partagés. On les oublie systématiquement, parce que les mettre à jour est plus lourd — il
faut déployer, ou écrire dans un autre outil.

Résultat : **les humains lisent une documentation périmée, et rien ne casse.** C'est le mode de
défaillance le plus silencieux qui soit.

⚠️ **Une carte qui ment coûte plus cher qu'une carte absente**, parce qu'on la croit — et parce
qu'elle **empêche de chercher**. Une surface absente fait poser la question ; une surface fausse y
répond mal.

## Étape 0 — Qu'est-ce qui a changé, et quelles surfaces ?

Classer la modification **d'abord**. Ce qui n'est pas concerné se déclare en un mot — un saut
explicite, jamais un silence.

| Type de modification | Surfaces à vérifier |
|---|---|
| **Une compétence** (créée, modifiée, renommée, supprimée) | son propriétaire · la carte des compétences · les règles si un usage change · toute copie publiée dans un pack |
| **Une règle** | le fichier de règles concerné, au bon niveau · la page qui les présente aux humains · l'accueil des nouveaux si ça touche le partage |
| **L'architecture** (dépôt, dossier, découpage) | les règles du projet · la carte « où vit quoi » · la carte d'architecture · l'espace partagé |
| **Le partage / les accès** | la carte des accès · la page de partage · le fichier d'accueil de chaque destinataire |
| **Une routine, une automatisation** | sa documentation versionnée · la page qui liste les routines · l'accueil |

**Plusieurs projets concernés** → écrire la méthode **une seule fois** chez son propriétaire, puis
mettre à jour uniquement les consommateurs locaux dont une route ou un contrat change. Ne jamais
recopier une méthode transverse dans plusieurs endroits locaux.

## La passe — dans l'ordre

### A · Ce que l'agent lit

1. **Les fichiers de règles** — au bon niveau : ce qui est vrai partout monte, ce qui est vrai ici
   reste ici.
2. **Le propriétaire du sujet** — la compétence qui possède la méthode. C'est là que la modification
   vit ; les autres pointent vers elle.
3. **Les copies publiées** — une compétence qui vit aussi dans un pack distribué ne se met **pas** à
   jour toute seule. Sans ce geste, la copie dérive en silence chez tous ceux qui l'ont installée.
   ⚠️ Et une copie de pack est une **adaptation volontaire** : elle se rejoue, elle ne s'écrase pas.

### B · Ce que les HUMAINS lisent — la raison d'être de cette compétence

4. **Les pages et tableaux de bord** — celles qui présentent le système. Une page modifiée mais non
   déployée **n'existe pas** : le geste n'est fini qu'une fois l'adresse ouverte et vérifiée.
5. **L'espace de travail partagé** — la couche éditable où les gens retravaillent. **Un lien, jamais
   une copie.**

### C · Finaliser

6. **Mettre à jour la CARTE du domaine touché.** Non négociable : une carte non maintenue fait
   travailler tout le monde sur du périmé.
7. **Les outils dont le périmètre a bougé.**
8. **Commit et push de chaque dépôt touché** — la synchronisation automatique ne couvre en général
   que le dépôt courant. Les autres sont à faire à la main.

## Le contrôle anti-doublon, à chaque surface

Une information vit dans **une** couche, pas deux. Elle existe déjà ailleurs → on met un **lien**,
pas une copie. Les deux couches se renvoient la balle.

**Deux fenêtres sur une source, jamais deux vérités.** Deux copies divergent à la première
modification, et on croit alors la mauvaise sans aucun moyen de le savoir.

## Clôture — dire ce qui a été propagé

Un récapitulatif court, en langage clair : **quelles pages** ont été mises à jour, quelles adresses
ont été redéployées et **vérifiées ouvertes**, quels commits.

Si une surface lourde reste à faire, **le dire honnêtement** — ne pas laisser croire que c'est fait.
*Une propagation à moitié faite laisse deux versions en circulation, ce qui est pire que zéro : la
prochaine session ne peut plus savoir laquelle est la bonne, donc elle repose la question.*

## Quand l'invoquer

**À la demande**, dès qu'une chose importante doit se retrouver partout. Ce n'est **pas** réservé à
la fin d'une session : on peut l'invoquer en plein milieu d'un chantier, à la seconde où une décision
est prise.

## Anti-patterns

- ❌ Mettre à jour les fichiers que l'agent lit et s'arrêter là. **C'est le problème que cette
  compétence résout.**
- ❌ Recopier le contenu d'une couche dans l'autre au lieu de mettre un lien.
- ❌ Recopier une méthode transverse dans plusieurs endroits locaux au lieu de son propriétaire.
- ❌ Modifier une page sans la déployer, puis la compter comme faite.
- ❌ Écraser une copie publiée au lieu de rejouer l'écart : on republie alors exactement ce que la
  dépersonnalisation avait retiré.
- ❌ Mélanger les échelles — la clôture d'une session et la documentation d'une fonctionnalité ont
  leurs propres compétences.

## Auto-amélioration

Une nouvelle surface découverte, ou un nouveau type de modification → l'ajouter au tableau de
l'étape 0 dans la même passe. Quelqu'un signale un oubli (« tu n'as pas propagé X ») → graver la
surface manquante ici, immédiatement.
---

<!-- dev-qa-link -->
| Rôle | Propriétaire |
|---|---|
| **Dev** | cette compétence |
| **Test** | le balayage de l'étape 0 : chaque surface listée a-t-elle été ouverte |
| **QA** | `AUCUNE` distincte — la preuve est **zéro surface qui dit encore l'inverse** |
| **Cadence** | `AUCUNE` — elle se déclenche quand une décision change |
<!-- /dev-qa-link -->
