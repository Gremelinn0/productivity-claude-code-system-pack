---
name: dev-capitaliser
description: >-
  Quand un travail vient de se terminer — un correctif posé, une mesure faite, un piège payé, une
  décision prise, une piste ÉCARTÉE → range LE FAIT ET LE POURQUOI chez la compétence qui possède
  le sujet, puis corrige ce que ça rend faux ailleurs. La commande unique de fin de travail : on ne
  se demande plus où ranger quoi, et une session qui rouvre le sujet dans trois semaines ne refait
  pas le chemin. Porte aussi une PASSE qui balaie les compétences sans mémoire. Déclenche sur
  « capitalise », « range ce qu'on a appris », « mets à jour la compétence », « documente ça »,
  « on vient de finir », « mémorise tout ça », « on avait décidé de ne pas faire ça », « pourquoi
  on a écarté cette piste », « garde le raisonnement », « on l'a déjà mesuré », « on va le
  reperdre », « je ne veux plus qu'on repose cette question » — et dès qu'on passe à autre chose
  après avoir appris quelque chose de durable.
---

# dev-capitaliser — la commande unique de fin de travail

## Le problème

Un agent qui reprend un sujet doit charger toute sa documentation pour savoir où il en est. Quand
cette documentation n'a pas de forme fixe, personne ne la charge — donc chacun improvise, ou
remesure ce qui était déjà mesuré.

**C'est le mécanisme qui fait redemander cinquante fois la même chose.**

Cette compétence ne remplace aucune méthode. Elle fait le rangement que personne ne fait.

## Le passage de fin — même quand il n'y a rien à écrire

Toute tâche terminée passe ici, **plans compris**. Le verdict est explicite :

- `ÉCRIT` si un plan réutilisable, un fait mesuré, une décision avec sa raison, une option refusée,
  un piège payé, une méthode réussie, une frontière d'owner ou un contrôle décidable mérite de
  rejoindre la compétence propriétaire ;
- `RIEN`, avec une raison courte, si la session n'a produit qu'un statut temporaire, une intuition
  non vérifiée, un récit ou une reformulation déjà présente.

Forcer une écriture à chaque passage créerait du bruit ; sauter silencieusement le passage rendrait
le rituel invérifiable. L'unité reste **une compétence et ses tiroirs existants**, jamais un rapport
de session ajouté à côté.

## Deux natures de fait, un seul geste

| Nature | Exemple | Sans elle |
|---|---|---|
| **Ce qui EST** — le fait | « ce délai est de 3 s » · « ce sélecteur casse sur telle cible » · « 27 % d'échecs » | on remesure, et la 2ᵉ mesure coûte autant que la 1ʳᵉ |
| **POURQUOI c'est comme ça** — le raisonnement | « on a refusé le cache par nom » · « on a préféré A parce que B rend faux X » | ça revient sous un autre nom trois semaines plus tard, **proposé de bonne foi** |

⚠️ **Une décision de NE PAS FAIRE est le seul type de décision qui s'efface toute seule.** Elle ne
laisse ni code, ni test, ni écran — aucun rappel nulle part. C'est pour elle que la seconde colonne
existe, et c'est elle qui revient six semaines plus tard sans que personne puisse savoir qu'elle a
déjà été refusée.

Les deux natures atterrissent dans **le même squelette**, chez **le même propriétaire**. C'est ça
qui rend la chose utilisable : on ouvre une compétence pour travailler, jamais un dossier d'archives.

## Les cinq gestes — dans cet ordre, aucun sautable

### 1 · Mettre à jour le CONTRAT

`references/contrat.md` du sujet, **≤ 140 lignes**, quatre volets :

| Volet | Ce qu'il porte |
|---|---|
| 1 · **ce que le sujet doit faire** | la mission, ce qui est à lui, ce qui ne l'est pas et vers qui ça route |
| 2 · **ce qui est déjà tranché ou prouvé** | les décisions, les acquis, **ce qui a été REFUSÉ**, le `PARTIEL`, le `NON MESURÉ` |
| 3 · **les pièges déjà payés** | les défauts de CE mécanisme, et ce qu'ils ont coûté |
| 4 · **les différences par environnement** | ce qui vaut partout, et l'exception écrite |

**Un volet vide se DÉCLARE** (`NON MESURÉ` · `AUCUN À CE JOUR`) — jamais un silence.
*Un volet muet est indistinguable d'un volet oublié.*

### 2 · Ranger le DÉTAIL à sa place fixe

```text
skills/<sujet>/
├── SKILL.md              la MÉTHODE seule — cycle, préflight, arrêts
└── references/
    ├── contrat.md        les 4 volets · TOUJOURS chargé en premier
    ├── decisions.md      ce qui a été tranché, daté, avec son anti-retour
    │                     + le bloc <!-- raisonnement --> : TRANCHÉ · REFUSÉ · MESURÉ · OUVERT
    ├── pieges.md         les défauts payés sur ce sujet, en détail
    └── environnements.md les différences par cible, et leurs adresses
```

**Les mêmes noms partout, pour tous les sujets.** C'est ça qui rend la chose utilisable : un agent
sait où regarder **sans lire le `SKILL.md` pour le savoir**.

Le raisonnement va dans `decisions.md`, sa maison naturelle — et **le volet 2 du contrat en porte la
version courte avec son adresse**. Le contrat étant le premier fichier chargé, celui qui ouvre le
sujet pour agir croise ce qu'on sait **avant** de commencer.

⚠️ **Rien de neuf ne s'écrit dans le `SKILL.md`.** Il est chargé **entier** à chaque invocation, pour
toujours — quarante lignes de récit en haut sont un **péage prélevé sur toutes les invocations
futures**. Le `SKILL.md` garde la règle, l'ordre, l'interdit, le pointeur.

### 3 · REMONTER ce qui dépasse le sujet

Un défaut hors périmètre **ne reste pas dans une réponse de chat**. Il part dans le registre des
chantiers de ton projet, avec son **propriétaire nommé** — un nom qui existe vraiment.

⚠️ **Jamais un nom inventé.** *Le contrôle, avant de committer la ligne : ce nom, puis-je le
RETROUVER ?* Non → il ne route vers personne **et** il fait croire que le poste est pourvu.
Écrire alors `À ATTRIBUER`, remonté à un humain — jamais « sans propriétaire », qui déclare un poste
vacant sans le pourvoir, et qui donne l'air d'avoir répondu.

### 4 · PROPAGER ce que ça rend FAUX ailleurs

**Capitaliser sans propager laisse des cartes qui mentent** — et une carte qui ment coûte plus cher
qu'une carte absente, parce qu'on la croit. Ce geste n'est pas optionnel : c'est la **sortie** de la
commande.

La question : *qu'est-ce qui vient de devenir FAUX, et qui doit être prévenu ?* (une règle · une
autre compétence · la doc produit · ce que voit l'utilisateur · les réglages · les cartes).
**Corriger l'existant AVANT d'ajouter.**

**Le contrôle, décidable** : *ce que je viens d'écrire rend-il faux quelque chose que quelqu'un
d'autre lit ?* Oui → ça part maintenant, pas « au fil de l'eau » (= jamais).

### 5 · PROUVER, puis committer

**La preuve qui compte, et elle est obligatoire quand on a descendu du contenu** — la non-perte,
mesurée contre l'historique, jamais supposée :

```bash
git show HEAD:skills/<sujet>/SKILL.md > /tmp/avant.md
# chaque ligne de fond de l'ancien fichier doit se retrouver dans l'union des nouveaux
```

Un compte de lignes perdues **différent de zéro** arrête la passe. *Alléger est indistinguable de
perdre : sans cette mesure, le geste a la même signature qu'une suppression.*

## La règle qui interdit la perte

> **Aucun fait ne vit SEULEMENT dans le contrat.**
> Chaque volet **dit le fait en clair**, puis **donne l'adresse** de sa version longue.

Le contrat n'est pas un résumé qui remplace : c'est une **porte d'entrée**. Le corpus détaillé ne
bouge pas d'un octet.

⚠️ **Le contrat DIT avant de RENVOYER.** S'il faut ouvrir un deuxième fichier pour savoir **quoi
faire**, il est raté.

## Le mode PASSE — balayer les compétences

La passe se déroule **par famille, un commit par famille** — jamais sur tout le dépôt d'un coup :
une passe massive produit des blocs creux, et **un bloc creux est pire que pas de bloc**, il fait
croire que le sujet est couvert.

On ne **fabrique** pas du raisonnement qui n'a pas eu lieu : on **rapatrie** celui qui est dispersé
(décisions datées de la doc, journaux, tableaux de bord). Rien à rapatrier → on écrit
`AUCUN raisonnement gardé à ce jour`, et la prochaine session sait qu'elle est la première au lieu
de chercher.

Avant une famille entière, convertir **trois pilotes de natures différentes** : un owner `dev-*`,
un owner `test-*` et une porte `router-*`. Les trois doivent rendre retrouvables les mêmes huit
réponses : frontmatter utile, lien Dev/Test/QA, problème résolu, stratégie, étapes et tiroirs,
décisions et rejets, frontières, preuves restantes. La famille ne part qu'après un contrôle de
non-perte réussi **et** un témoin saboté qui échoue réellement.

Déroulé complet et gabarit du bloc : [`references/raisonnement.md`](references/raisonnement.md).

## Cinq interdits, chacun payé

**On ne descend pas un bloc qu'on n'a pas LU.** Un **ratio volumétrique compare des volumes, jamais
des contenus** — mesuré sur un corpus réel : un ratio désignait 5 074 lignes comme du doublon
recopié, la lecture réelle en a rendu **2 554 (50 %) uniques**, dont une décision tranchée deux fois.

**On ne déchire pas un paragraphe.** Les blocs se déplacent **entiers, verbatim**. Découper
sémantiquement, c'est réécrire, et réécrire c'est perdre.

**On ne crée pas un artefact de plus.** Le savoir d'un sujet vit sous **son** propriétaire. Jamais
une compétence de plus « pour que ce soit plus propre » — c'est de l'entropie déguisée en rangement.

**On ne garde pas la conclusion sans sa raison.** « On a choisi A » ne protège de rien : c'est la
raison qui empêche de re-choisir B six semaines plus tard, et c'est elle qu'on oublie.

**On n'empile pas, on corrige.** Un raisonnement dont la prémisse s'avère fausse se corrige **sur
place**, avec la date et ce qui l'a démenti. Deux entrées contradictoires au même endroit, c'est la
garantie qu'on lira la mauvaise.

## Fini quand

- Le contrat est **≤ 140 lignes**, ses 4 volets remplis ou déclarés vides.
- Chaque volet porte **au moins une adresse vivante**.
- Le raisonnement est **chez son propriétaire** dans `decisions.md` — ou j'ai écrit
  `AUCUN raisonnement gardé à ce jour`. Un silence ici est le seul interdit.
- Le détail est dans le fichier de sa nature ; le `SKILL.md` a **baissé** ou n'a pas monté.
- La non-perte est **prouvée** contre l'historique, avec son témoin positif.
- Une passe de famille a commencé par trois pilotes représentatifs et son contrôle a vu un sabotage.
- Ce qui dépasse le sujet est **au registre**, avec un propriétaire retrouvable.
- Ce que ça rend **faux ailleurs** est corrigé — ou j'ai vérifié que rien ne devient faux, et je le
  dis. Un silence ici laisse des cartes qui mentent.
- Le commit est parti et le contenu est **vérifié sur le dépôt distant** — jamais sur l'accusé de
  push.

## Le savoir par volet

| Quand tu doutes de… | Lis |
|---|---|
| ce qui entre dans la **mémoire** d'un sujet, les 4 états, le mode PASSE | [`references/raisonnement.md`](references/raisonnement.md) |
| ce que le **produit** fait, et quelle surface se met à jour d'abord | [`references/volet-produit.md`](references/volet-produit.md) |
| où va une **méthode**, et comment alléger sans perdre | [`references/volet-methode.md`](references/volet-methode.md) |
| ce qui est propre à un **environnement** | [`references/volet-environnement.md`](references/volet-environnement.md) |
| le **gabarit** des 4 fichiers, et comment descendre un bloc sans perdre | [`references/squelette.md`](references/squelette.md) |
---

<!-- dev-qa-link -->
| Rôle | Propriétaire |
|---|---|
| **Dev** | cette compétence |
| **Test** | `AUCUN` — ce qu'elle produit est du texte chez un propriétaire ; le rejeu utile est la **passe** elle-même, pas un script |
| **QA** | le contrôle de fin — *quelqu'un qui ouvrira cette compétence demain retrouvera-t-il le fait chez elle ?* |
| **Cadence** | `AUCUNE` — elle se déclenche à la **fin d'un travail**, jamais à une heure |
<!-- /dev-qa-link -->
