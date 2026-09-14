---
name: clean-rules-cleanup
description: >-
  L'outil unique pour créer, modifier, supprimer et réorganiser les règles d'un agent — aucune
  écriture de règle ne se fait sans passer par ici. L'invoquer avant toute édition ou demande
  « ajoute, grave, nettoie, compresse ou optimise les règles », et pour auditer un parc de
  compétences. Au lancement, il rend le corpus caché navigable pour l'utilisateur : ce qui aide,
  ce qui gêne, ce qui est toujours chargé et où gagner réellement de la place. Modes : nettoyage
  en 4 phases, audit du parc, création guidée d'une règle.
---

# clean-rules-cleanup — écrire, alléger et ranger les règles

## Au lancement — rendre le corpus navigable

Avant toute modification, commencer par une carte courte pour l'utilisateur, jamais par l'inventaire interne exhaustif : **où je regarde** (chemins cliquables et couches) · **ce qui aide** · **ce qui gêne** · **où gagner de la place** (1 à 3 gestes réversibles, gain mesuré et contrepartie). Distinguer ce qui est chargé à chaque session de ce qui ne l'est qu'à la demande : déplacer une règle ciblée ne libère pas le même budget qu'alléger une règle toujours chargée.

La carte sert à naviguer dans l'inventaire des Phases 1 ; elle ne le remplace pas et n'est pas un gate d'approbation. Nettoyage autorisé → poursuivre le réversible ; audit seul → s'arrêter après les recommandations. **Contrôle** : l'utilisateur peut-il répondre depuis l'ouverture seule « qu'est-ce qui me gouverne, qu'est-ce qui me coûte, que puis-je déplacer sans casse » ? Non → la Phase 1 n'a pas commencé.

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

**Lancer d'abord `python scripts/registre.py audit <corpus>`** (§7) : il rend en une passe les règles dont personne n'a écrit la raison, celles dont la condition de péremption est atteinte, et celles que plus rien ne fait respecter — la seule entrée qui permette de juger la **pertinence** d'une règle plutôt que sa taille. Rendre ensuite la carte utilisateur obligatoire définie au lancement. Puis scanner le fichier entier. Lister **chaque** règle avec son numéro de ligne. Classer par thème.
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
| **PÉRIMÉE → archiver le motif** | sa **condition de péremption est atteinte** (registre, §7) : l'outil visé a disparu, la plateforme est abandonnée, le mécanisme est réparé en amont. La seule action qui retire une règle **sur preuve** et non au flair |
| **COMPRESSER sur place** | garder mais réduire — verbatim long en une phrase, exemples au-delà d'un seul coupés. ⚠️ La prose coupée **descend au registre**, elle ne disparaît pas : sinon la règle devient irretirable au ménage suivant |

Sortie : une table `règle | ligne | thème | action | cible et justification`. **Sans le registre (§7), une règle ne se juge que sur sa taille** — donc on compresse, on ne retire jamais, et le corpus remonte d'un cran à chaque passe ; avec lui, elle se juge sur ce qu'elle **protège encore**.

### Phase 3 — Exécuter le réversible, présenter le reste

Ce qui est **réversible** s'exécute en autonomie. Ce qui ne l'est pas — une suppression définitive,
un changement de comportement — se présente en **delta final**, court, à réviser.

### Phase 4 — Appliquer, puis prouver

**La preuve de non-perte est obligatoire**, mesurée contre l'historique, jamais supposée : chaque
ligne de fond de l'ancien fichier existe dans l'union des nouveaux. Un compte différent de zéro
arrête la passe.

*Alléger est indistinguable de perdre : sans cette mesure, le geste a la même signature qu'une
suppression.*

**Puis rendre le rapport d'exécution — et c'est ce que la personne qui a demandé le ménage attend
vraiment.** Un gros nettoyage (plus d'une section touchée, une préimage archivée) se termine par un
fichier écrit dans l'archive de la passe, `RAPPORT.md`, à côté des préimages : avant/après en lignes
et en octets, puis **une ligne par règle** — ce qui est gardé · la décision (KEEP / COMPRESS /
FUSION / PÉRIMÉE) · **ce qui est parti, où, pourquoi** — les verbatims gardés et ceux descendus au
registre, le résultat du contrôle de non-perte, et « rien de supprimé » prouvé par les préimages.
Le message à la personne tient en trois lignes et donne le lien ; le rapport porte le détail.
Gabarit : [`references/rapport-d-execution.md`](references/rapport-d-execution.md).

*Pourquoi un rapport, et pas un récapitulatif* : sur quarante sections, un récapitulatif ne dit pas
où est parti tel verbatim. Sans la ligne, la personne ne peut ni relire ni contester — elle ne peut
que faire confiance, et c'est exactement ce qu'un ménage ne doit pas demander. **Contrôle** : *le
rapport existe-t-il dans l'archive de la passe, avec une ligne par règle ?* Non → la passe n'est pas
finie.

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

**Phase 1 — Carte utilisateur, puis inventaire complet** : rendre d'abord la carte définie au lancement ; ensuite chaque compétence, son niveau, son propriétaire, sa taille, qui
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
5. **Écrire le MOTIF au registre, même passe** (§7) : ce qui a été payé, le contrôle décidable, et
   **la condition de péremption**. C'est là que descend la prose que §5 va couper de la règle —
   sans elle, le « pourquoi » part dans l'historique Git et la règle devient irretirable.
   **Contrôle** : la règle est-elle écrite sans que sa ligne de registre existe ? Alors ce n'est
   pas fini.
6. **Propager** ce que la nouvelle règle rend faux ailleurs.

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

## §7 — Le registre des motifs : pourquoi chaque règle existe

**Le trou.** §1 veut une règle chargée réduite au comportement et à son contrôle ; §5 coupe donc le
cas payé, le chiffre et la phrase qui l'a déclenchée — ils partent dans l'historique Git,
c'est-à-dire nulle part. Personne ne sait plus ce que la règle protège : au doute on garde, et le
corpus monte d'un cran à chaque passe. **C'est pour ça qu'un ménage finit toujours par ne savoir
que compresser.**

**Le registre** — [`references/registre-des-motifs.md`](references/registre-des-motifs.md), jamais
chargé — porte **une ligne par règle** : adresse · date de gravure · ce qui a été payé · contrôle
décidable · **condition de péremption** · dernière revue. Format et méthode de remplissage dans son
en-tête.

**La colonne qui fait le travail, c'est la péremption** : les autres décrivent le passé, donc elles
se relisent et **se croient**. *Contrôle en l'écrivant* : pourrais-je lancer aujourd'hui une
commande qui me dise si c'est arrivé ? Non → c'est un vœu, et la règle restera pour toujours.

**L'outil** — [`scripts/registre.py`](scripts/registre.py), bibliothèque standard uniquement.
`sync` ajoute les règles datées absentes en squelette sans jamais réécrire une cellule remplie ·
`audit` rend motifs manquants, contrôles manquants, règles disparues, **péremptions échues**,
revues de plus de 180 jours, règles regravées après retrait · `show <motif>` sort une ligne avant
de toucher à une règle. Il **ne bloque rien** — un gate qui crie au loup finit ignoré.

```bash
python scripts/registre.py audit CLAUDE.md
```

**Où il s'accroche** : mode NOUVELLE RÈGLE étape **5** (le motif s'écrit dans la même passe que la
règle) · Phase **1** du nettoyage (`audit` avant de cartographier) et Phase **2** (action
`PÉRIMÉE`). L'orphelinat se juge sur l'**adresse `§N`**, jamais sur la date de gravure : un
nettoyage qui coupe le récit d'une règle efface sa date sans toucher à la règle, et chercher par
date déclarerait tout le registre orphelin pile le jour où il sert.

**Anti-patterns** : graver une règle sans sa ligne · un déclencheur abstrait (« pour éviter les
erreurs » est vrai de toutes les règles, donc n'en défend aucune) · laisser la péremption à `—`
sans avoir cherché la condition · cocher `VIVANTE` sans rien avoir mesuré.

---

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
