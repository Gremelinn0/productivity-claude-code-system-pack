---
name: clean-rules-cleanup
description: >-
  L'outil unique pour créer, modifier, supprimer et réorganiser les règles d'un agent — aucune
  écriture de règle ne se fait sans passer par ici. À invoquer AVANT toute édition d'un fichier de
  règles (ajouter, graver, compresser, nettoyer, déplacer vers une compétence ou un hook), et pour
  auditer un parc de compétences devenu trop gros. Trois modes : la passe de nettoyage en 4 phases,
  l'audit du parc de compétences, et la création guidée d'une règle isolée. Triggers : « ajoute une
  règle », « grave cette règle », « nettoie les règles », « compresse », « réorganise le fichier de
  règles », « optimise les tokens », « audit des compétences », « renomme une compétence »,
  « on accumule trop de règles ».
---

# clean-rules-cleanup — écrire, alléger et ranger les règles

## §1 — Doctrine : le contexte est un budget

Un fichier de règles est chargé **entier, à chaque session, pour toujours**. Chaque ligne est donc un
péage prélevé sur toutes les sessions futures, y compris celles qui n'ont rien à voir avec elle.

**Ce qui mérite d'être une règle chargée partout** : une chose qui s'applique à **toute** réponse,
indépendamment du sujet en cours — le style, un garde-fou universel, un ordre de travail. Sinon →
une compétence ciblée.

- **1 information = 1 endroit.** Une duplication est un défaut. Une référence courte bat un contenu
  recopié.
- **Un verbatim** ne se garde que s'il est explicitement non négociable **et** que le comportement
  n'est pas évident. Sinon → reformuler en une ligne.
- **Les articulations de prose** (« ceci COMPLÈTE cela », « pourquoi cette règle existe ») se
  coupent, sauf décision explicite.
- **Un exemple par règle au maximum**, et seulement si le comportement est contre-intuitif.
- **Une table de plus de 8 lignes** s'externalise.

### Le seuil qui compte, et le contre-effet qu'on oublie

Au-delà d'une certaine taille, **ajouter des règles fait en suivre MOINS**. Le fichier ne devient pas
« un peu lourd » : il devient un décor que plus rien ne lit vraiment.

Le remède, prouvé plusieurs fois : **déménager la jurisprudence chez son propriétaire**
(`skills/<propriétaire>/references/`) et ne laisser que **la règle + le pointeur**. Une passe réelle :
93 537 → 73 053 caractères, sans perdre une décision.

⚠️ **Une doctrine qui déménage laisse un renvoi à son ancienne adresse, dans la même passe.** Une
adresse morte ne rend pas d'erreur : elle rend du **silence**, et le silence se comble par analogie.
*Mesuré : environ 14 000 citations d'adresses de sections qui ne résolvaient plus, et deux sessions
différentes ont réinventé la même règle fausse pour combler le vide.*

⚠️ **Et un chiffre d'état se re-mesure au moment où on l'écrit, jamais ne se recopie.** *Payé trois
fois sur le même paragraphe : un plafond annoncé dépassé pendant six jours après sa résolution, puis
quatre jours de plus. La troisième fois ment dans le sens le plus coûteux — elle accuse un chantier
**déjà livré**, et envoie quelqu'un chercher un problème qui n'existe plus.*
**Le contrôle** : *ai-je lancé l'instrument dans cette passe ?* Non → la ligne ne s'écrit pas.

---

## §2 — Où va une règle ?

### §2.1 Le niveau : global ou local ?

| Niveau | Chargé quand | Quand l'utiliser |
|---|---|---|
| **Local** (défaut) | dans ce projet uniquement | une fonctionnalité, un environnement, un flux propre au projet — **90 % des cas** |
| **Global** (exception) | toutes les sessions, tous les projets | un flux vraiment transverse **et** léger, identique partout sans variation |

**Deux critères obligatoires pour le global** :

1. **Vraiment transverse** — utile dans au moins trois projets actifs, sans variation de contenu.
2. **Léger** — un flux, pas un catalogue. Au-delà de 100 lignes de contenu spécifique → local.

**Au doute, rester local** : le global se mérite, il coûte à chaque session.

⚠️ **Une règle globale avec une exception « sauf dans le projet X » n'est pas une règle globale.**
C'est le signal le plus fiable qu'elle est mal placée. Deux correctifs : la déplacer en compétence
globale avec une condition explicite, ou la dupliquer proprement dans les projets concernés.

### §2.2 La cible : quatre options, par ordre de préférence

| Cible | Quand | Coût en contexte |
|---|---|---|
| **Supprimer** | déjà couverte par une règle, un hook, une compétence, ou une convention évidente | **zéro** |
| **Un hook** | déclenchement automatique avant ou après une action | quasi nul en permanence, payé au déclenchement |
| **Une compétence ciblée** | une tâche, une fonctionnalité, un environnement précis | zéro par défaut, payé au chargement |
| **Une règle chargée partout** | s'applique à **toute** réponse, quel que soit le contexte | **payé à chaque session** |

**Avant d'ajouter une règle chargée partout, quatre questions** :

1. Une règle existante couvre-t-elle déjà ça ? → étendre l'existante, ne pas dupliquer.
2. Un hook ou une compétence peut-il la porter ? → alors ce n'est pas une règle globale.
3. S'applique-t-elle encore si on travaille demain sur un sujet complètement différent ? Non → c'est
   une compétence.
4. Le niveau : global ou local ? → pencher local.

**Un « oui » à 1, un « oui » à 2, ou un « non » à 3 → ce n'est pas une règle chargée partout.**

---

## §3 — Mode NETTOYAGE : la passe en 4 phases

**Ne jamais compresser, déplacer ou supprimer une règle sans avoir d'abord regroupé thématiquement
TOUT le fichier ET classé chaque règle individuellement.** Le nettoyage règle par règle, au fil de
l'eau, garantit la dérive.

### Phase 0 — Vérifier l'archive avant toute action

Avant chaque passe, **et** avant toute demande du type « recrée la règle X » : consulter l'archive
des règles retirées.

Si la règle ou une variante existe déjà :

1. vérifier la **couverture actuelle** avant de restaurer ;
2. trou réel → restaurer en priorité dans une **compétence ciblée**, sinon en local, **jamais** en
   global ;
3. déjà couvert ailleurs → **dire où c'est**, ne pas dupliquer ;
4. mettre à jour l'index de l'archive dans la même passe.

*Recréer une règle archivée sans vérifier, c'est la dérive inverse : on regonfle le fichier qu'on
vient d'alléger.*

### Phase 1 — Regroupement thématique (cartographie, zéro modification)

Scanner le fichier entier. Lister **chaque** règle avec son numéro de ligne. Classer par thème.
Sortie : une table `règle | ligne | thème`. **Aucune modification à cette phase.**

**L'ordre est non négociable : du plus LARGE au plus SPÉCIFIQUE.**

- Entre catégories : transverse universel → spécifique technique.
- Dans une catégorie : la règle qui régit les autres → les dérivées générales → les cas particuliers.
- Au doute : la règle **citée** par d'autres passe en premier. Une règle qui dit « complète X » passe
  **après** X.

❌ **Interdit** : l'ordre chronologique ou alphabétique. Toujours sémantique.

### Phase 2 — Une décision par règle

| Action | Quand |
|---|---|
| **GARDER** | vraiment transverse, applicable à toute réponse |
| **DÉPLACER → compétence** | concerne une fonctionnalité, un environnement, un flux technique |
| **DÉPLACER → hook** | comportement automatique avant ou après une action |
| **FUSIONNER avec la règle #X** | cousine d'une règle existante |
| **SUPPRIMER** | couverte ailleurs, obsolète, ou jamais appliquée |
| **COMPRESSER sur place** | garder mais réduire — verbatim long en une phrase, exemples au-delà d'un seul coupés |

Sortie : une table `règle | ligne | thème | action | cible et justification`.

### Phase 3 — Exécuter le réversible, présenter le reste

Ce qui est **réversible** s'exécute en autonomie. Ce qui ne l'est pas — une suppression définitive,
un changement de comportement — se présente en **delta final**, court, à réviser.

### Phase 4 — Appliquer, puis prouver

**La preuve de non-perte est obligatoire**, mesurée contre l'historique, jamais supposée : chaque
ligne de fond de l'ancien fichier existe dans l'union des nouveaux. Un compte différent de zéro
arrête la passe.

*Alléger est indistinguable de perdre : sans cette mesure, le geste a la même signature qu'une
suppression.*

### Anti-patterns de la passe

- ❌ Compresser sans avoir cartographié d'abord.
- ❌ **Réécrire** un corpus au lieu de l'**indexer**. Le mal, c'est presque toujours l'index
  manquant et le transitoire mélangé au canonique — rarement le volume.
- ❌ Archiver un dossier entier plutôt que par date.
- ❌ Casser une **adresse stable** citée ailleurs. On ajoute un index par-dessus, on ne renomme pas.
- ❌ Archiver un document **qu'on n'a pas ouvert**. *Un dossier vidé en poussant du travail non fait
  vers l'archive n'est pas un dossier propre : c'est une perte déguisée en rangement, et elle est
  indétectable.*

---

## §3bis — Mode AUDIT DU PARC : les compétences

Même structure en 4 phases, appliquée à un parc de compétences devenu trop gros ou incohérent.

**Phase 1 — Inventaire complet** : chaque compétence, son niveau, son propriétaire, sa taille, qui
la cite, qui elle cite.

**Phase 2 — Une décision par compétence** : garder · renommer · fusionner avec une autre · déplacer
de niveau · archiver.

Les signaux qui décident :

- **elle fait deux choses** → la couper ;
- **elle double une voisine** → fusionner, et la survivante **NOMME** ce qu'elle absorbe ;
- **personne ne la cite et elle ne cite personne** → orpheline, elle ne se déclenchera jamais ;
- **son nom ne dit pas ce qu'elle fait** → renommer, avec un outil qui refuse de finir sur une
  référence morte.

⚠️ **À la fin de toute absorption, deux oui obligatoires** : la survivante **nomme** ce qu'elle
absorbe, **et** le dossier absorbé a disparu. *Mesuré : une fusion déclarée dans quatre fichiers
voisins mais pas chez la survivante, et dont le dossier n'avait jamais été supprimé — la compétence
morte a continué à se charger et à concourir six jours de plus.* **Une déclaration chez les voisins
prouve qu'on a pensé au geste ; elle ne prouve pas qu'on l'a fini.**

**Phase 3 et 4** : identiques — réversible en autonomie, non-perte prouvée, archive datée et
consultable.

---

## §4 — Mode NOUVELLE RÈGLE

1. **Chercher d'abord** : une règle existante couvre-t-elle déjà ça ? Et l'archive ?
2. **Décider la cible** (§2.2) et le **niveau** (§2.1).
3. **Écrire au format** : la règle en une à deux lignes, l'interdit s'il existe, et — si le
   comportement est contre-intuitif — **le contrôle décidable** qui permet de savoir qu'on la viole.
4. **Placer selon l'ordre** de la Phase 1 : large → spécifique.
5. **Propager** ce que la nouvelle règle rend faux ailleurs.

> 🧭 **La formulation qui tient : une règle utile porte son CONTRÔLE.**
> *« Sois rigoureux »* n'est pas une règle, c'est un vœu. *« Avant d'écrire un chiffre d'état :
> ai-je lancé l'instrument dans cette passe ? »* en est une — parce qu'elle est **décidable** en une
> seconde, sans interprétation.
> La ligne de partage : le **décidable** bloque, le **jugement** se montre sans trancher.

---

## §5 — Techniques de compression

**Le méta-principe** : garder ce qui **change un comportement**, couper ce qui **explique** un
comportement déjà clair.

| Geste | Quand |
|---|---|
| **GARDER** | la règle change ce que l'agent fait, et ce n'est pas déductible |
| **COUPER** | de l'articulation de prose, un rappel de contexte, une justification d'une chose évidente |
| **REFORMULER** | un verbatim long dont seul le fond compte → une phrase |
| **EXTERNALISER** | de la jurisprudence, un historique, un catalogue → une annexe chez le propriétaire |
| **FUSIONNER** | deux règles cousines → une, avec des sous-points |

### Les descriptions de compétences

Une description verbeuse coûte à chaque session **et** déclenche moins bien.

- ✅ **Le QUAND d'abord** : « Quand `<la situation>` → `<ce que ça fait, en une clause>` ».
- ✅ Les déclencheurs en clair, y compris les formulations adjacentes.
- ❌ Une phrase d'introduction, une justification, un historique, une liste de fichiers.

---

## §6 — Anti-patterns

- ❌ Éditer un fichier de règles sans passer par ici.
- ❌ Ajouter une règle sans avoir cherché si elle existe déjà, y compris en archive.
- ❌ Mettre en global au doute.
- ❌ Écrire une règle sans son contrôle, quand le comportement est contre-intuitif.
- ❌ Supprimer définitivement plutôt qu'archiver par date, dans une archive **consultable**.
- ❌ Recopier un chiffre d'état au lieu de le re-mesurer.
- ❌ Déclarer une passe finie sans preuve de non-perte.

## Pour aller plus loin

| Sujet | Fichier |
|---|---|
| créer une règle isolée — le format long, le détail de chaque étape | [`references/creer-une-regle.md`](references/creer-une-regle.md) |
---

<!-- dev-qa-link -->
| Rôle | Propriétaire |
|---|---|
| **Dev** | cette compétence |
| **Test** | `AUCUN` — une règle se vérifie en la **relisant**, pas en la rejouant |
| **QA** | le contrôle que porte la règle écrite : *est-il décidable en une seconde ?* |
| **Cadence** | `AUCUNE` — elle se déclenche quand une règle bouge |
<!-- /dev-qa-link -->
