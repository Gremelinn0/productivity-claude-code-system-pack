---
name: optimise-systeme
description: >-
  La méthode objective pour optimiser un système d'agent — les règles, les compétences,
  l'architecture, la documentation, les cartes. Mesure d'abord (chiffré, jamais à l'oreille),
  diagnostique, trouve les problèmes réels (doublons, mauvais niveau, gonflement, cartes périmées,
  rôles mélangés), conçoit le correctif avec ses arbitrages, grave au bon niveau, propage,
  re-mesure. Elle n'exécute pas à la place des compétences dédiées : elle les orchestre dans
  l'ordre. Triggers : « optimise le système », « améliore le système », « le système est en
  bordel », « rends le système plus propre », « on accumule trop de règles », « compacter les
  règles », « on a trop de compétences », « passe d'optimisation ».
---

# optimise-systeme — la méthode objective

## Posture — l'objectif d'abord

- **Mesurer AVANT de juger.** Pas de « c'est le bordel » à l'oreille → **chiffrer** : nombre de
  lignes de règles, nombre de compétences, doublons détectés, règles mal placées, cartes périmées.
  Toute affirmation = méthode + preuve chiffrée + où la retrouver.
- **Orchestrer, pas refaire.** Un problème de niveau, un doublon, une règle à graver, une compétence
  à créer : chacun a sa compétence propriétaire. Ne jamais réimplémenter leur travail ici.
- **Observer seulement, par défaut.** Au-delà de trois fichiers touchés, le diagnostic et le plan
  se font valider. Le diagnostic est gratuit ; l'exécution se valide.
- **Économe en contexte.** Optimiser un système, c'est souvent le **réduire**. Une optimisation qui
  gonfle est suspecte.
- **Les compétences s'appellent les unes les autres — la cohésion est un livrable.** Un système
  efficace, ce sont des compétences qui se routent, jamais des silos. Toute passe vérifie et câble
  les renvois croisés ; une compétence orpheline — qui n'appelle personne et que personne n'appelle
  — est une dérive à corriger.

---

## Les trois faux remèdes

Ils ont un mécanisme commun, et c'est lui qu'il faut reconnaître : **ils consomment le problème sans
le résoudre**. Gratuits à écrire, visibles dans le diff, ils donnent l'impression que c'est réglé —
donc le vrai correctif n'est jamais fait.

### N°1 — « j'ajoute une ligne dans le routeur » ne répare jamais une découvrabilité

Quelqu'un ne trouve pas une compétence. Le réflexe immédiat, et il est presque toujours faux, est
d'ajouter une ligne dans le routeur, la carte, l'index.

**Le cas mesuré, chiffré des deux côtés.** Une porte de domaine introuvable. Remède posé : une ligne
dans la table du routeur racine, plus un bandeau — avec la décision explicite de **ne pas** renommer,
au motif de 108 références. **Le lendemain, la même porte est reperdue.** Durée de vie du remède :
**24 heures**.

Ce que la mesure disait, et qu'une ligne ne pouvait pas changer :

| Compétence | Fichiers qui la citent |
|---|---:|
| la plomberie du domaine | **105** |
| la porte du domaine | **60** |

**Une porte citée deux fois moins que son propre enfant n'a pas un problème d'annonce : elle a un
problème de NOM et de DÉCLENCHEURS.** Les deux se disputaient les mêmes déclencheurs, et le nom ne
disait pas « porte ». Ajouter une 375ᵉ ligne à un routeur que personne ne relit ne déplace aucun de
ces deux chiffres. Le vrai correctif a été le **renommage** — 146 réécritures, zéro référence morte.

**Le contrôle, avant de « documenter » une découvrabilité, en une question** : *est-ce que je change
quelque chose que la personne TOUCHE — le nom qu'elle tape, la description qui décide de
l'invocation, le nombre de noms qu'elle doit distinguer ? Ou est-ce que j'ajoute du texte dans un
fichier qu'elle ne rouvrira pas ?*

- ❌ Une ligne de plus dans un routeur **comme seul remède** · un bandeau « la compétence existe » ·
  un renvoi croisé de plus. Ces trois-là sont des **compléments**, jamais le correctif.
- ✅ **Renommer** · **réécrire les déclencheurs** pour que la porte gagne contre ses propres enfants ·
  **réduire le nombre de noms** à distinguer.
- 🔁 **Un remède reposé une deuxième fois est la preuve qu'il ne marchait pas.** *Sa répétition EST la
  mesure de son échec.*

⚠️ **Corollaire, dans les deux sens** : une décision gravée la veille se **rouvre** quand son remède
est mesuré inefficace — ce n'est pas de l'instabilité, c'est l'arrivée d'un fait nouveau. Ce qui
serait de l'instabilité : rouvrir **sans** mesure. On écrit donc toujours **ce qui a échoué et
combien de temps ça a tenu**, jamais seulement la nouvelle décision.

### N°2 — « je note le sujet quelque part » n'est pas le PLACER

Un sujet sans maison apparaît. Le réflexe est d'ouvrir un **registre**, une liste « points ouverts »,
un tableau de suivi. C'est gratuit, ça se voit, et ça donne l'impression que le sujet est pris en
charge.

**Le vrai geste, et c'est LE livrable de la passe** : le sujet **entre dans le périmètre d'une
compétence propriétaire** — écrit **chez elle**, dans ses termes, de sorte que **toute passe future
de cette compétence le relise et le fasse avancer**. On ne dépose pas une note à côté d'un
propriétaire : on **améliore le propriétaire** pour qu'il devienne meilleur sur cette tâche-là.

Une porte peut ensuite tenir une table de routage — qui nomme le propriétaire et ne stocke rien
d'autre — mais elle vient **après** le placement, jamais à sa place.

**Le contrôle, en une question** : *si cette compétence propriétaire est invoquée demain sans que
personne ne se souvienne d'aujourd'hui, retrouve-t-elle le sujet dans son propre fichier ?* Non →
ce n'est pas placé, c'est stocké ailleurs.

⚠️ **Et « personne ne le prend » ne s'écrit qu'APRÈS avoir cherché.** Un orphelin déclaré qui n'a pas
coûté une lecture des descriptions candidates du domaine n'est pas un état mesuré — c'est une paresse
déguisée en rigueur, et elle est **pire que le silence**, parce qu'elle a l'air d'un travail fait.
*Cas mesuré : six points annoncés orphelins, trois marqués « sans exécutant » ; une simple lecture des
descriptions du domaine a rendu un propriétaire vivant pour les six.*

#### Le troisième étage : placer ne suffit pas non plus — il faut RAPPELER

La chaîne complète est **noter → placer → rappeler**, et on s'arrête presque toujours à la deuxième.

Une compétence est un **dépôt passif** : elle n'oublie rien, et elle ne se réveille jamais seule. Un
sujet parfaitement placé chez son propriétaire n'est lu que par quelqu'un qui invoquait déjà ce
propriétaire — c'est-à-dire par personne, puisque c'est justement ce dont on ne se souvient pas.

**Les deux questions, dans l'ordre, pour savoir où on s'est arrêté** :

1. *Si la compétence propriétaire est invoquée demain, retrouve-t-elle le sujet chez elle ?*
   Non → étage 1, c'est noté ailleurs.
2. *Si PERSONNE ne l'invoque, quelque chose finit-il par le dire ?* Non → étage 2, c'est placé et
   muet.

**Ce qui fait passer au troisième étage** : le sujet entre dans un **format que la machine compte
déjà** — un index dérivé, un compteur, une vue générée — et **une compétence porte le devoir de le
dire**, pas seulement la capacité de répondre.

⚠️ **Le piège symétrique, qui rend cet étage rare et cher** : un rappel qui parle à chaque session
devient du papier peint, donc pire que rien. Le rappel s'attache à un **moment que la personne lit
déjà** (une clôture, un récapitulatif), ou se **déclenche sur un changement** — jamais un compteur
permanent affiché en boucle.

### N°3 — un cliquet posé sur une grandeur qui BOUGE TOUTE SEULE

On vient de mesurer une dette. On veut l'empêcher de grossir. Le réflexe — et il a l'air
irréprochable — est de **graver le nombre du jour comme plafond** : *« 206 fichiers, ça ne doit pas
monter »*. C'est la forme canonique du cliquet, et elle marche… **tant que la grandeur ne bouge que
par le travail humain.**

**Elle casse dès que la grandeur bouge toute seule.** Il n'y a que deux façons, toujours les mêmes :

| Ce qui bouge sans que personne n'agisse | Ce que le contrôle devient |
|---|---|
| **la POPULATION grandit** (un corpus qui gagne des fichiers, des items, des lignes) | rouge sur du travail **sain** — celui qui a ajouté un fichier conforme se fait accuser |
| **l'HORLOGE avance** (un âge, une péremption, une échéance) | vert aujourd'hui, rouge **pour toujours** dans N jours, sur du travail que **personne n'a fait** |

⚠️ **Et le coût n'est pas le rouge : c'est la DÉSACTIVATION.** Un contrôle qui crie à tort finit
ignoré, puis retiré — donc il ne protège plus de rien, et la dette qu'il gardait redevient invisible.
*On a payé le prix d'un contrôle pour se retrouver sans contrôle, avec en prime la conviction qu'il
y en avait un.*

**LE CONTRÔLE, décidable, avant de graver un plafond** :
*si personne ne touche à rien pendant un mois, ce nombre change-t-il ?*

- **Non** → un plafond chiffré convient.
- **Oui** → **le plafond ne doit pas être un NOMBRE, mais un ARRIÉRÉ NOMMÉ ET GELÉ.** On liste les
  cas existants **un par un**, et le contrat ne porte plus que sur ce qui **ARRIVE** : tout élément
  absent de la liste doit être conforme. La liste ne peut que **rétrécir**.

**Pourquoi la liste nommée est strictement meilleure, et pas seulement plus douce** — c'est le point
contre-intuitif : elle est **plus sévère**. Un plafond chiffré laisse un élément neuf **se cacher
dans le compte** dès qu'un ancien a été réparé le même jour. Une liste nommée ne le permet pas : le
neuf n'y est pas, donc il rougit.

**Le geste, en trois clauses** :

1. **geler par NOM** — la liste vit dans le fichier de budget, à côté de sa raison ;
2. **un plafond de TAILLE de liste**, qui ne monte jamais ;
3. **un élément réparé ne fait rougir personne** — son nom devient périmé, on le publie pour que la
   liste rétrécisse. Faire rougir sur un nom périmé punirait exactement le geste qu'on veut.

🩸 **Les deux cas, mesurés la même nuit, posés par la même passe** :

- **la POPULATION** — un cliquet gravé à `206`, soit la population publiée à la seconde près. Deux
  fichiers sont arrivés **dans les quatre minutes**, et le contrôle est passé rouge sur du travail
  sain. ⚠️ Sa propre documentation invoquait l'arbitrage *« un contrôle qui crie à tort finit
  désactivé »* — **il le violait dans la ligne suivante**.
- **l'HORLOGE** — un cliquet sur l'âge des vérifications en attente, vert le jour de la pose parce
  que l'arriéré était gelé… et le contrôle annonçait lui-même **71 items au-delà du seuil dans
  7 jours, 130 dans 30**. Rouge programmé, sur du travail que personne n'aurait fait.

✅ **La falsification qui tranche, et c'est une PAIRE** — un seul sabotage ne sépare pas les deux
mondes : *un élément neuf NON conforme doit rougir* **et** *dix éléments neufs CONFORMES ne doivent
rien casser*. Le second est celui qu'on oublie, et c'est lui qui prouve qu'on a réparé le bon défaut.

⚠️ **Un sabotage se falsifie AVANT le contrôle qu'il teste.** Payé dans la même heure : un premier
essai est resté vert parce que la phrase de sabotage disait *« AUCUN témoin négatif »* — elle
**contenait donc le motif** qu'elle prétendait retirer. On mesure l'état saboté **avec l'instrument
lui-même**, et on montre qu'il a changé, avant de conclure quoi que ce soit.

---

## La passe — 7 étapes dans l'ordre

### 1 · CIBLER

Quel système ? Un projet précis, ou l'écosystème entier. Le dossier courant donne le défaut.
Plusieurs projets → traiter chacun, jamais un seul en oubliant les autres.

### 2 · DIAGNOSTIC — demander la carte, pas la refaire

Partir de ce qui prétend **déjà** répondre à la question : la carte « où vit quoi » du projet, son
état, ses inventaires. Carte périmée ou absente → la régénérer d'abord, puis repartir de là.
Inventorier : les fichiers de règles (lignes, sections), les compétences actives, les cartes.

### 3 · MESURER — chiffré, reproductible

Sortir des **nombres**, pas des impressions :

- Lignes par fichier de règles (coût en contexte × nombre de sessions).
- Compétences : total, actives contre dormantes, candidates au doublon.
- Règles mal placées — trop bas, trop haut.
- Cartes : dernière mise à jour contre réalité (périmé = ment).
- Rôles mélangés : une compétence qui fait deux choses.

🔇 **Les descriptions RÉELLEMENT LUES.** Une compétence dont le frontmatter ne parse pas en YAML
strict a sa `description:` **ignorée** par le harnais, qui retombe sur le titre du corps : elle
paraît normale, elle ne se déclenche **jamais** toute seule, et **rien ne crie**.

```bash
python - <<'PY'
import io, yaml, glob, os
bad = []
for p in glob.glob("skills/*/SKILL.md") + glob.glob(os.path.expanduser("~/.claude/skills/*/SKILL.md")):
    if "_archive" in p:
        continue
    try:
        y = yaml.safe_load(io.open(p, encoding="utf-8").read().split("---", 2)[1])
        assert (y.get("name") or "").strip(), "name absent ou vide"
        assert (y.get("description") or "").strip(), "description absente ou vide"
    except Exception as e:
        bad.append((os.path.basename(os.path.dirname(p)), str(e).split("\n")[0][:50]))
print(len(bad), "description(s) muette(s) :", *bad, sep="\n  ")
PY
```

*Mesure inaugurale sur un parc de 215 compétences : **14 muettes**, dont la porte principale d'un
domaine entier. Cause dans 11 cas sur 14 : un `: ` dans une valeur scalaire écrite sur une ligne →
correctif = bloc replié `>-`.*

> 🧪 **Et ce zéro-là se falsifie avant d'être cru.** Une version antérieure de cette recette ne savait
> pas refuser une `description:` **vide** : `str(y.get("description",""))` sur une valeur YAML nulle
> rend la chaîne `"None"` — **non vide, donc verte**. Elle attrapait le `: ` mal échappé et manquait
> le cas le plus simple, en rendant « 0 muettes » avec l'aplomb d'une mesure.
> **Le geste, avant de citer le chiffre** : donner à l'instrument 6 frontmatters qu'on SAIT faux
> (deux-points nu · description vide · description d'espaces · name vide · name absent · aucun
> frontmatter) et 2 qu'on sait sains (scalaire simple · bloc replié), et exiger **8/8**.

### 3bis · MESURER LA COUVERTURE — « est-ce que ce qu'on PRÉTEND est VRAI ? »

Un système décrit ce qu'il fait. La question suivante est de savoir si c'est vrai : combien de ce
qui est annoncé est réellement câblé, invoqué, mesuré. L'écart entre les deux est la vraie dette.

### 4 · TROUVER les problèmes

Doublons · mauvais niveau · gonflement · cartes qui mentent · rôles mélangés · compétences orphelines
· descriptions muettes · contrôles posés sur une grandeur qui bouge seule (faux remède n°3).

### 4bis · ARBITRER — règle en prose, ou CONTRÔLE mécanique ?

La ligne de partage : le **DÉCIDABLE** bloque, le **JUGEMENT** se montre sans trancher.

- Une chose qu'une machine peut vérifier sans interpréter (un fichier existe, un plafond, un format)
  → **un contrôle**, qui bloque.
- Une chose qui demande de lire et d'apprécier → **une règle en prose**, et un rappel au bon moment.

⚠️ Un contrôle qui crie au loup finit ignoré. Tout contrôle se prouve par un **témoin positif** — il
doit être capable de rendre NON sur une entrée qu'on sait fausse. *Un contrôle incapable de refuser
ne vaut pas son OUI.*

### 5 · CONCEVOIR le correctif — ouvrir, trancher, PUIS casser

Produire au moins trois options réellement distinctes quand l'enjeu le mérite, trancher avec ses
arbitrages écrits, **puis attaquer son propre plan** avant de graver. Un plan qui ne peut pas
échouer dans sa formulation n'est pas testable.

### 6 · GRAVER au bon niveau

Une chose vraie partout monte ; une chose vraie ici seulement reste ici. Au doute, on remonte : mal
placer bas coûte du temps à tout recréer, un cran trop haut coûte quelques jetons.

Pour une compétence existante ou une famille, entretenir l'owner en place : même squelette
sémantique, trois pilotes représentatifs (`dev-*`, `test-*`, `router-*`) avant le lot, snapshot puis
preuve de non-perte capable d'échouer sur une copie amputée. Créer ou refondre structurellement un
owner reste un autre geste ; une passe d'entretien ne fabrique pas une compétence « mémoire ».

### 7 · PROPAGER + RE-MESURER

Corriger **toutes** les surfaces que le changement rend fausses, puis relancer la mesure de l'étape 3.
Une optimisation non re-mesurée est une intention, pas un résultat.

---

## Sortie

Un rapport court : ce qui a été mesuré (avec les nombres et comment les reproduire), ce qui a été
trouvé, ce qui a été décidé et pourquoi, ce qui a été écarté, ce qui reste ouvert avec son critère
de sortie.

## Anti-patterns

- Juger à l'oreille et présenter ça comme un diagnostic.
- Réimplémenter le travail d'une compétence dédiée au lieu de l'appeler.
- Ajouter du texte là où il fallait changer un nom (faux remède n°1).
- Ouvrir un registre là où il fallait améliorer un propriétaire (faux remède n°2).
- Graver le nombre du jour comme plafond sans se demander s'il bouge seul (faux remède n°3).
- Livrer une optimisation qui **gonfle** le système.
- Conclure sans re-mesurer.

## Pour aller plus loin

| Sujet | Fichier |
|---|---|
| revue complète — règles, compétences et documentation, avec non-perte prouvée | [`references/passe-certifiante-regles-competences.md`](references/passe-certifiante-regles-competences.md) |
---

<!-- dev-qa-link -->
| Rôle | Propriétaire |
|---|---|
| **Dev** | cette compétence |
| **Test** | les mesures qu'elle prescrit — poids, descriptions muettes, renvois morts — à outiller chez toi |
| **QA** | la re-mesure après la passe : les chiffres ont-ils bougé dans le bon sens |
| **Cadence** | `AUCUNE` par défaut — armable si tu veux une passe régulière ; une fois par trimestre suffit |
<!-- /dev-qa-link -->
