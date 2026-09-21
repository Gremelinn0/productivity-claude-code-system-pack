# La mémoire d'un morceau — garder le POURQUOI, pas seulement le fait

> Annexe de **`/capitaliser`**. À ouvrir quand on écrit ou qu'on relit le bloc
> `<!-- raisonnement -->` d'un morceau, et pour dérouler le **mode PASSE**.
>
> **Origine** : cette annexe est l'ancienne compétence `/capitaliser`, fusionnée dans
> `/capitaliser`. Le geste de garder le POURQUOI et celui de garder le FAIT sont le même geste :
> les séparer en deux compétences oblige à choisir laquelle invoquer au moment précis où l'on ne sait
> pas encore ce qu'on a appris.
> **Pourquoi la fusion** : les deux faisaient le même geste — capitaliser à la fin d'un dev, chez le
> propriétaire du morceau, dans le même squelette de fichiers. Deux portes pour un geste, c'est une
> porte que personne ne prend.

---

## Pourquoi ce volet existe

Une décision **prise** laisse du code, un test, une ligne de contrat produit. Elle a des rappels partout.

Une décision de **ne pas faire** ne laisse rien. Aucun fichier ne la porte, aucun gate ne la surveille, aucun
écran ne la montre. Elle revient donc — sous un autre nom, trois semaines plus tard, proposée de bonne foi par
quelqu'un qui n'a aucun moyen de savoir qu'elle a déjà été refusée. C'est le seul type de décision qui
**s'efface toute seule**.

Même chose pour une **mesure**. Une hypothèse chiffrée un soir, rangée nulle part, se remesure — et la
deuxième mesure coûte autant que la première.

> **L'idée en une phrase** : encapsuler les décisions **dans la compétence**, et y garder les
> réflexions sur ce qu'elle fait et comment l'améliorer — pour toutes les compétences, pas seulement
> celles qu'on retouche souvent.

**Le foyer, c'est la compétence** — pas un dossier de fiches, pas un tableau de bord, pas un ticket. On ouvre
une compétence pour travailler ; on n'ouvre jamais un dossier d'archives. Un raisonnement rangé ailleurs que
chez celui qui va s'en servir est un raisonnement perdu, même s'il est parfaitement écrit.

## Ce que ce volet n'est pas — la frontière, en une ligne chacune

| Voisine | Elle fait | Ce qui la distingue |
|---|---|---|
| `/propage-systeme` | diffuse une décision produit sur le site, le légal, la roadmap, Notion | **vers l'extérieur** — ici on garde, on ne diffuse pas |
| la compétence qui met à jour la documentation produit phase 4 | écrit ce que le **produit fait**, dans la doc feature | le **quoi** — ici on garde le **pourquoi** |
| la carte d'architecture de ton projet | l'architecture et l'ownership du système | le **système** — ici une seule fonctionnalité |
| `/capitaliser` | trouve ce qui devient faux et route vers les propriétaires | **le routage** — ici on écrit chez le propriétaire une fois qu'il est connu |
| la compétence qui lit tes journaux, la compétence qui mesure dans la durée | produisent des mesures | eux **mesurent**, ce volet **garde le résultat** pour qu'on ne remesure pas |

Une même passe de travail peut appeler plusieurs de ces compétences. Elles ne se remplacent pas : elles
écrivent dans des maisons différentes.

**Par où on entre** : la porte la porte de développement de ton projet (§ Frontières) — une vague de dev qui produit un raisonnement durable
arrive ici. `/capitaliser` (global) reste le réflexe amont : elle cherche ce qui devient faux et
désigne le propriétaire ; une fois le propriétaire connu, c'est ce geste-ci qui écrit chez lui.

## Les quatre états — et rien d'autre

Le bloc de mémoire d'une compétence ne contient que ces quatre choses. La contrainte est volontaire : une
mémoire qui accepte tout devient un journal, et un journal ne se relit pas.

**🟢 TRANCHÉ** — ce qui est décidé et ne se rediscute pas. La date, la décision en une phrase, la
raison, et les mots exacts de qui a tranché s'ils existent. Sans la raison, la décision se
rediscutera : c'est la raison qu'on oublie, jamais la conclusion.

**🛑 REFUSÉ** — la section qui justifie ce volet. Une direction envisagée puis écartée, **avec ce qui a
motivé le refus**. Elle doit être écrite de façon à être reconnue quand elle reviendra sous un autre nom —
donc on nomme le **mécanisme** proposé, pas seulement son étiquette du jour.

**📏 MESURÉ** — une hypothèse déjà chiffrée : le chiffre, la date, l'instrument, la taille de l'échantillon,
et ce que la mesure **ne** couvre **pas**. Une mesure sans son périmètre se fait sur-généraliser, et une
sur-généralisation coûte plus cher que l'absence de mesure.

**❓ OUVERT** — ce qui n'est pas tranché, dit honnêtement, avec ce qui permettrait de trancher. Un « ouvert »
sans critère de sortie est un vœu ; avec son critère, c'est un travail.

## La question qui décide de ce qui entre

Avant d'écrire une ligne, une seule question :

> *Si quelqu'un rouvrait ce sujet dans trois semaines, qu'est-ce qui lui éviterait de refaire le chemin ?*

Ce qui répond à cette question entre. Le reste — le récit de la session, l'ordre des tentatives, les détours —
n'entre pas. Ce n'est pas un journal de bord : c'est ce qu'on aurait voulu lire avant de commencer.

## La méthode

### 1. Identifier le propriétaire, et un seul

Le raisonnement va chez la compétence qui **possède la fonctionnalité**, pas chez celle qui l'a trouvé.
Au doute, la porte qui trouve la bonne compétence tranche. Une réflexion qui concerne deux fonctionnalités se **coupe
en deux**, chacune chez son propriétaire, avec un renvoi croisé d'une ligne — jamais recopiée aux deux endroits,
sinon les deux copies divergent et on croit la mauvaise.

Aucune compétence ne possède le sujet → c'est un signal, pas un blocage : le dire, et écrire
**`À ATTRIBUER`** plutôt qu'inventer un destinataire. Un nom fabriqué fait croire que le poste est
pourvu, ce qui est pire qu'un poste ouvertement vacant.

### 2. Faire penser l'architecte quand il y a un arbitrage

Si le raisonnement compare des options, pèse des compromis, ou écarte un design, invoquer
**`/engineering:architecture`** — c'est lui qui structure la comparaison (contexte, options, compromis,
conséquences). Ce geste-ci ne refait pas son travail : il **classe et garde** ce qu'il produit.

La division est nette : l'architecte **pense**, ce volet **se souvient**. Un arbitrage non structuré se
réduit vite à « on a préféré A », ce qui ne protège de rien — c'est le raisonnement qui protège, pas la
conclusion.

Pas d'arbitrage dans le sujet (un simple constat mesuré, un cadrage corrigé) → ne pas l'invoquer pour la forme.

### 3. Écrire le bloc dans `references/decisions.md` du propriétaire

Le bloc porte un marqueur, pour être retrouvable par une machine plus tard :

```markdown
<!-- raisonnement -->
## 🧠 Ce qu'on sait déjà — à lire avant de rouvrir le sujet

🟢 **TRANCHÉ — <titre court>** (<date>)
<la décision en une phrase>. **Pourquoi** : <la raison>. <les mots exacts de qui a tranché, s'ils existent>

🛑 **REFUSÉ — <le mécanisme proposé, nommé pour être reconnu>** (<date>)
<ce qui était proposé>. **Refusé parce que** : <la raison>. **Reviendra sous la forme** : <les
déguisements probables>.

📏 **MESURÉ — <ce qui est établi>** (<date>)
<le chiffre>. Instrument : <commande ou outil>. Échantillon : <taille>. **Ne couvre pas** : <la limite>.

❓ **OUVERT — <la question>**
<ce qui manque>. **Se tranchera par** : <le geste qui donnerait la réponse>.
```

**Où le bloc vit, et pourquoi là** : dans `references/decisions.md`, et sa version courte dans le **volet 2 du
contrat** avec son adresse. Quelqu'un qui ouvre la compétence pour agir doit croiser ce qu'on sait **avant** de
commencer à faire — sinon il l'aura lu trop tard ; c'est le contrat, premier fichier chargé, qui le lui
garantit. Le `SKILL.md` est chargé entier à chaque invocation : y graver de la jurisprudence est un péage
prélevé sur toutes les invocations futures — d'où la règle : **l'annexe est le défaut**.

> 🕰️ **Les blocs écrits avant que tu adoptes l'annexe vivent dans le `SKILL.md`** de leur morceau.
> **Ils y restent jusqu'à ce que tu retouches ce morceau** — le marqueur les rend retrouvables où
> qu'ils soient, et une migration de masse produirait autant de commits qui ne corrigent rien.

### 4. Ce qui ne se recopie jamais

Un chiffre qui bouge — un stock de tickets, un compte de fichiers, un pourcentage de couverture — **ne se
recopie pas** : on écrit la commande qui le rend. Une liste recopiée ment dès la première divergence, et on
la croit d'autant plus qu'elle a l'air précise.

Ne se recopient pas non plus : le contrat produit (il vit dans la doc feature), l'état d'un chantier (il vit
dans son plan), la méthode d'une autre compétence (on pointe).

### 5. Corriger, jamais empiler

Un raisonnement dont la prémisse s'avère fausse se **corrige sur place**, avec la date et ce qui l'a démenti —
il ne se supprime pas, et il ne se double pas d'une entrée contraire plus bas. Deux entrées contradictoires
dans le même bloc, c'est la garantie qu'on lira la mauvaise.

Un bloc qui dépasse une trentaine de lignes est un signal : soit il contient du récit à retirer, soit la
compétence porte deux sujets et c'est **ça** qu'il faut regarder.

## Le mode PASSE — balayer toutes les compétences

l'utilisateur demande que ça passe partout. La passe se déroule **par famille**, jamais sur tout le dépôt en une
fois : une passe massive produit des blocs creux, et un bloc creux est pire que pas de bloc — il fait croire
que le sujet est couvert.

1. Lister les compétences de dev qui possèdent une fonctionnalité.
2. Pour chacune : est-ce qu'elle porte déjà un `<!-- raisonnement -->` ?
3. Non → chercher la matière **là où elle existe déjà** : les décisions datées de la doc feature, les
   anti-yoyo, les journaux de boucle, les tableaux de bord de chantier. On ne **fabrique** pas du raisonnement
   qui n'a pas eu lieu — on **rapatrie** celui qui est dispersé.
4. Rien à rapatrier → écrire `<!-- raisonnement -->` avec **`AUCUN raisonnement gardé à ce jour`**. C'est un
   état déclaré, pas un trou : la prochaine session sait qu'elle est la première, au lieu de chercher.
5. Une famille à la fois, commit par famille.

⚠️ **Aucun gate mécanique n'est posé aujourd'hui**, et c'est délibéré : on ne pose un contrôle qu'après une
violation réelle, sinon on maintient à vie un verrou qui crie à tort — et un verrou qui crie à tort finit
désactivé. Le marqueur `<!-- raisonnement -->` existe pour qu'un gate soit **possible** le jour où le besoin
sera prouvé.

## Anti-patterns

- **Écrire le récit de la session** — l'ordre des tentatives, les détours, ce qu'on a essayé d'abord. Personne
  ne relit ça. Seul compte ce qui évite de refaire le chemin.
- **Garder la conclusion sans la raison.** « On a choisi A » ne protège de rien : c'est la raison qui empêche
  de re-choisir B six semaines plus tard.
- **Recopier le contrat produit** dans la compétence. Deux sources pour un même fait, et la seconde ment dès
  la première divergence.
- **Créer un fichier à côté** parce que le bloc devient long. Le bloc reste chez son propriétaire ; s'il ne
  tient plus, il va en annexe **sous la même compétence** (`references/`), jamais chez un second propriétaire.
- **Remplir un bloc pour qu'il ne soit pas vide.** `AUCUN raisonnement gardé à ce jour` est une information ;
  un paragraphe creux est un mensonge poli.
- **Attendre que l'utilisateur le demande.** Le moment d'écrire, c'est quand la réflexion vient d'avoir lieu — après,
  le contexte est parti et il ne reste que la conclusion.

## Auto-amélioration

Un raisonnement qu'on redécouvre alors qu'il avait déjà eu lieu = la preuve qu'il manquait un bloc. L'écrire
dans la foulée chez son propriétaire, et **nommer ici le type de raisonnement** qui s'était échappé — c'est
ainsi que les quatre états se corrigent, s'il en manque un.
