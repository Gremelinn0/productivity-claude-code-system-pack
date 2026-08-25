# Le nom de la fonctionnalité en premier — jurisprudence et chiffrages

> Annexe de [`/skill-quality-guard`](../SKILL.md) **Axe 2**. La **règle** vit là-bas et tient en
> quatre lignes ; ici vivent les **mesures**, qu'on ouvre le jour où l'on prépare une migration —
> jamais à chaque invocation.

## Pourquoi cette règle ne prend jamais du premier coup

Le symptôme, qui revient toujours dans les mêmes mots : *« je ne sais jamais ce que j'ai en
compétences — elles ont bien toutes le préfixe de la fonctionnalité ? Je n'ai pas l'impression. »*

**Ce n'était pas un oubli : la table de conventions se contredisait elle-même.** Un patron mettait
la fonctionnalité en **suffixe** (`test-<feature>`), deux autres la mettaient en **préfixe**
(`<feature>-logs`, `<feature>-tuning`) — dans le même tableau, depuis toujours. Rien n'avait donc
**jamais tranché où va le nom**, et la convention dominante était celle qui contredit la demande :
**19 compétences en suffixe contre 8 en préfixe**.

*Une règle qu'on redemande cent cinquante fois sans qu'elle prenne décrit rarement un oubli — elle
décrit une contradiction que personne n'a levée.*

## L'état d'un parc réel — 139 compétences, 24 familles

Mesuré par regroupement des noms sur la racine de chaque fonctionnalité produit, avec témoin
positif (la famille `design`, dont les 2 membres sont conformes, sort bien 2/0) et témoin négatif
(la famille dictée, dont la réponse était connue d'avance, sort bien 1/4).

| Famille | Conformes | Non conformes |
|---|---:|---:|
| **Lecture** — le cœur du produit | 0 | **22** (`lgm-*`, `test-lecture-*`, `dev-*`, `qa-lecture`…) |
| Session (atteindre, écrire dedans) | 1 | 8 |
| Commandes vocales | 0 | 5 |
| **Dictée** | 1 | 4 |
| Propagation multi-plateformes | 0 | 5 |
| Colibri · Autopilote · Abonnement · Extension | 1 à 4 chacune | 2 à 4 chacune |
| Design | 2 | 0 |

⚠️ **La limite du critère littéral, et elle est réelle** : il ne peut rien dire quand une
fonctionnalité a **deux vocabulaires** — lecture *vs* `lgm`, réglages *vs* `parameters`, commandes
vocales *vs* `cmd-voc`, abonnement *vs* `billing`/`subscription`. Dans ces familles le zéro de
conformes est vrai, mais il désigne un problème de **vocabulaire**, pas seulement de préfixe : la
migration doit d'abord choisir **le mot**.

## Chiffrage d'une migration de famille — le patron

Fait **avant** de renommer les quatre compétences d'une même fonctionnalité, pour faire passer
son nom du suffixe au préfixe.

**Le chiffrage sert à PLANIFIER — il dit quels gates patcher AVANT, dans quel ordre, avec quels
témoins. Il ne sert jamais à refuser.**

**Références** (`git grep`, jamais `grep -r` — il descend dans les worktrees et compte 3 à 6× trop) :

| | refs | fichiers |
|---|---:|---:|
| la compétence de **test** de la famille | 357 | 138 |
| sa **porte** | 187 | 101 |
| sa **QA** | 128 | 57 |
| une compétence **spécialisée** | 34 | 18 |
| **le dépôt du projet** | **706** | |
| le **plugin publié** qui en embarque une copie | 153 | |
| le dossier de skills **global** | 80 | |
| un **dépôt voisin** | 2 | |
| **total réel** | **941** | |

⚠️ **Le dépôt du projet ne portait que 75 % du total.** Le quart restant vit dans trois racines
qu'on ne pense pas à balayer — et c'est là que se logent les références mortes qui survivent au
renommage.

⚠️ **Un outil de renommage ne voit que les racines qu'on lui donne.** Le tien ignorera
probablement les dossiers cachés, les plugins installés, et les dépôts voisins. *Ce qu'il ne voit
pas ne rougit pas* — donc son « zéro référence morte » ne prouve rien sur ce qu'il n'a pas balayé.

### Les deux familles de surfaces, et la seconde est pire

**Celles qui CASSENT DUR** — un plancher numérique, un `assert len(...) == 3`, un `startswith()`
sur l'ancien préfixe. Elles échouent bruyamment, donc on les trouve. À patcher **avant** le
renommage, jamais après.

**Celles qui DÉGRADENT EN SILENCE** — une génération de vue qui range mal, un `glob("dev-*")` qui
perd une couverture sans échouer, un rappel pré-commit qui cesse d'être déclenché. **Rien ne
rougit.** Ce sont elles qui font découvrir la casse trois semaines plus tard, sur un autre sujet.

⚠️ **Et les liens symboliques ou jonctions qui pointaient l'ancien nom deviennent morts** —
silencieusement, eux aussi.

## La bonne façon de patcher — elle sert toutes les familles suivantes

**On rend la machinerie tolérante aux DEUX formes**, `<role>-<feature>` et `<feature>-<role>`, avant
de renommer quoi que ce soit. Et quand c'est possible, **on reconnaît par ce que le fichier DIT de
lui-même** — bloc `<!-- dev-qa-link -->`, présence d'un `references/contrat.md`, déclaration de
porte — plutôt que par son nom. La formule qui tient : *une porte se reconnaît à ce qu'elle dit
d'elle-même, jamais à son nom.* Le nom reste un signal **accepté**, jamais **exigé**.

⚠️ Un plancher numérique ou un assert de comptage se **re-dérive**, il ne se décrémente pas — et le
commentaire dit pourquoi le nombre bouge.
