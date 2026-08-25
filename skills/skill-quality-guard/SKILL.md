---
name: skill-quality-guard
description: >-
  Le contrôle final avant qu'une compétence soit considérée comme prête : 7 axes vérifiés, dont le
  poids (moins de 500 lignes), le frontmatter qui doit parser en YAML strict sous peine que la
  description soit ignorée, la description qui dit QUAND se déclencher avant de dire quoi elle
  fait, le routage documentaire (pointer, jamais recopier), la porte d'entrée (une compétence
  orpheline ne s'invoque pas), l'ensemble Dev/Test/QA, et la resynchronisation des copies publiées
  dans un pack. À invoquer avant toute création ou mise à jour de compétence, et avant tout commit
  qui touche un dossier de compétences. Triggers : « audite ce skill », « le skill est trop long »,
  « description pas à jour », « vérifie la qualité du skill », « ce skill a-t-il sa QA », « les
  compétences sont-elles bien reliées entre elles », « pourquoi mon skill ne se déclenche jamais ».
---

# skill-quality-guard — le contrôle final, 7 axes

**Principe fondamental** : une compétence bien construite s'organise selon une **taxonomie
structurée par concepts**, pas en tas chronologique ni en accumulation de correctifs. À chaque
ajout, se demander : *ce nouveau bloc rentre dans quel concept existant, ou faut-il introduire un
concept clair ?*

Ce contrôle est le **dernier maillon** d'une chaîne : quelque chose écrit la compétence, quelque
chose la conduit et la nomme, **et celui-ci la refuse ou la laisse passer**.

---

## Axe 1 — POIDS

**Cible : moins de 500 lignes.** Au-delà, la compétence pollue le contexte à **chaque** invocation,
pour toujours.

```bash
wc -l SKILL.md
```

Au-dessus, identifier ce qui s'externalise :

| Ce qui déborde | Où ça descend |
|---|---|
| tables de sélecteurs, d'identifiants, de valeurs par environnement | un fichier de référence par environnement |
| spécifications fonctionnelles détaillées | la documentation du produit |
| matrices transverses de plus de 20 lignes | un fichier de référence dédié |
| scripts de plus de 50 lignes | `scripts/`, chargé à la demande — pas en ligne |
| exemples longs, journaux annotés, jurisprudence datée | `references/` |

**Le bon geste** : le `SKILL.md` dit *« lis `references/x.md` § 2 »*, il ne recopie pas le § 2.

### La méthode d'allègement — 4 gestes

1. **Une annexe sous le MÊME propriétaire** : `<compétence>/references/<sujet>.md`. **Jamais une
   deuxième compétence** — un sujet, un propriétaire, un point d'entrée. Y descendent l'historique
   daté, les dossiers d'instruction, la jurisprudence : tout ce qui se consulte quand on doute, pas
   à chaque invocation.
2. **Ce qui RESTE** : la règle, l'interdit, l'ordre à respecter, le pointeur. Le test : *un lecteur
   pressé garde-t-il tout l'opérationnel ?*
3. **PROUVER la non-perte** : sonder des chaînes retirées et vérifier qu'elles existent d'un côté ou
   de l'autre. Sans cette preuve, **alléger est indistinguable de perdre** — et l'archive a l'air
   d'un geste sain, c'est ce qui la rend dangereuse.
4. ⚠️ **VÉRIFIER AVANT DE COUPER — le geste que tout le monde saute.** Le bloc qui ressemble le plus
   à un doublon n'en est pas forcément un. *Mesuré : 55 lignes candidates parfaites à la coupe, avec
   une documentation de 345 lignes sur le même sujet à côté. Elles ne recopiaient rien : elles
   **pointaient** vers elle et portaient des décisions absentes partout ailleurs.*
   Le contrôle : *ce bloc RECOPIE-t-il, ou POINTE-t-il ?*

---

## Axe 2 — STRUCTURE

### Le frontmatter DOIT parser en YAML strict — sinon la description est IGNORÉE

C'est le défaut le plus coûteux du lot, parce qu'il est **totalement silencieux**. Si le frontmatter
ne parse pas, le harnais retombe sur le titre du corps et **ignore complètement ta `description:`**.
Tu as écrit une belle description : elle ne sert à rien, et la compétence ne se déclenche jamais
toute seule.

**Trois casseurs récurrents** :

- **Un `: ` (deux-points + espace) dans une valeur écrite sur une ligne** → YAML croit lire un
  mapping imbriqué. **Correctif : bloc replié `>-`**, où les `:` `,` `"` deviennent du texte.
  ```yaml
  description: >-
    Fait X — cascade : a → b. Triggers : « ... ».
  ```
- **Un champ multi-valeurs** (`trigger: "/x", "y", "z"`) = scalaire suivi de virgules, invalide,
  casse tout le bloc. Seuls `name` et `description` sont lus : mettre les déclencheurs **dans** la
  description.
- **Un BOM UTF-8** en tête → le `---` n'est plus au tout début → frontmatter non reconnu.
  Enregistrer en **UTF-8 sans BOM**.

**Vérification avant commit** (silence = tout va bien) :

```bash
python -c "import yaml,io,sys; d=io.open(sys.argv[1],encoding='utf-8').read(); \
assert not d.startswith('﻿'),'BOM'; y=yaml.safe_load(d.split('---',2)[1]); \
assert (y.get('name') or '').strip() and (y.get('description') or '').strip(),'name/description'" SKILL.md
```

⚠️ **Ce contrôle se falsifie avant d'être cru.** Une version antérieure ne savait pas refuser une
`description:` **vide** : sur une valeur YAML nulle, une conversion en chaîne rend `"None"` — non
vide, donc verte. Lui donner 6 frontmatters qu'on **sait** faux et 2 qu'on sait sains, et exiger
**8/8**. *Un contrôle incapable de refuser ne vaut pas son OUI.*

### Le corps — une taxonomie par concepts

Chaque section répond à une question conceptuelle distincte — un *quoi* ou un *pourquoi* — jamais à
un *il s'est passé tel truc telle date*.

- Pas de sous-sections au-delà de trois niveaux.
- Plus de trois domaines distincts couverts → envisager la division, avec un orchestrateur parent.
- Avant d'ajouter un bloc, vérifier s'il rentre dans un concept existant. Oui → fusionner. Non →
  introduire un concept clair, avec un titre qui dit **de quoi ça parle**.

❌ **Anti-pattern** : des sections « Update du 12 », « Fix du 18 », « Note ajoutée le 22 » empilées
dans le désordre. Si la chronologie compte vraiment → **un** bloc historique unique en fin de
fichier, le reste organisé par concepts.

### Le nommage — la FONCTIONNALITÉ est le premier mot

**Le contrôle, décidable en une seconde** : *je tape le nom de la fonctionnalité dans
l'autocomplétion — est-ce que TOUTES ses compétences sortent ?* Non → le nom est faux, quoi qu'il
dise par ailleurs.

| Motif | Usage |
|---|---|
| `<fonctionnalité>-test` | tests de bout en bout |
| `<fonctionnalité>-tuning` | les paramètres réglables |
| `<fonctionnalité>-router` | la porte du sujet, dès qu'il a 3 compétences ou plus |
| `<fonctionnalité>-qa` | le verdict de conformité |

**Le périmètre se borne** : cette règle vise les compétences attachées à une fonctionnalité. Les
familles d'**outillage système** n'ont aucune fonctionnalité derrière — elles gardent leur préfixe
de famille.

**Pour une compétence système, le nom dit l'ACTION ET SA PORTÉE**, pas juste un verbe. `duplicate`
ne dit rien : dupliquer quoi, où ? **Le test** : quelqu'un qui lit **juste le nom** doit savoir ce
que fait la compétence et sur quoi, sans ouvrir le fichier.

⚠️ **Une migration de nommage se fait en entier, pas « au fil de l'eau ».** Une famille à moitié
convertie fait coexister deux conventions, donc la session suivante ne peut plus savoir laquelle est
la bonne — **et elle repose la question**. Le chiffrage sert à planifier l'ordre des étapes, jamais
à refuser le chantier. Rendre la machinerie tolérante aux **deux** formes **avant** de renommer.

Détail et patron de chiffrage : [`references/nommage-fonctionnalite.md`](references/nommage-fonctionnalite.md).

---

## Axe 3 — ROUTAGE DOCUMENTAIRE

**Règle fondamentale** : une compétence ne duplique **jamais** le contenu d'un document canonique.
Elle pointe vers lui, avec la section exacte à lire.

Quatre questions :

1. **La compétence parle d'une fonctionnalité ?** → pointer sa documentation produit. Ne pas
   recopier sa description en ligne : le décalage est garanti dès la prochaine mise à jour.
2. **Elle mentionne des sélecteurs, des identifiants, des mécanismes d'environnement ?** → ces
   détails vivent dans le fichier de leur environnement. La compétence pointe.
3. **Elle contient une matrice transverse ?** → vérifier si elle existe déjà ailleurs. Oui → pointer
   et supprimer la copie. Non, et plus de 20 lignes → créer le fichier de référence, puis pointer.
4. **Elle référence des défauts connus ?** → pointer l'index, ne pas recopier le détail.

---

## Axe 4 — DESCRIPTION

La description est **la seule chose** que le modèle voit quand il décide d'invoquer ou non. Vague,
datée, encombrée de jargon interne, ou trop longue → la compétence n'est jamais déclenchée, et elle
pourrait aussi bien ne pas exister.

> 🕐 **Le QUAND d'abord, le QUOI en une clause.** Une description qui dit *ce que ça fait* concourt
> sur le **sujet** ; une description qui dit *quand ça s'active* concourt sur le **moment** — et
> c'est le moment que le modèle compare à ce que la personne vient d'écrire. La seconde gagne,
> **structurellement**, pas par style.
>
> **La forme juste** : « Quand `<situation, ce que la personne dit, ce qui vient de se passer>` →
> `<ce que ça fait, en une clause>`. Triggers : … »

Inclure des **déclencheurs adjacents** : le défaut le plus courant n'est pas le sur-déclenchement,
c'est le **sous-déclenchement**. Être légèrement insistant.

---

## Axe 5 — PORTE

Une compétence orpheline ne s'invoque pas. Chacune est **rangée derrière une porte d'entrée** de son
domaine, et porte des **renvois croisés** vers ses voisines.

⚠️ **Mais ajouter une ligne dans une porte ne répare jamais une découvrabilité** — c'est un
complément, jamais le correctif. Si la compétence ne se trouve pas, le problème est presque toujours
son **nom** ou ses **déclencheurs**, pas son annonce.

---

## Axe 6 — ENSEMBLE

Une compétence qui **produit quelque chose** nomme son test et son verdict. Le silence est le seul
interdit : une exception se **déclare**, avec sa raison.

Le bloc, quatre cases, à la fin du fichier :

```markdown
<!-- dev-qa-link -->
| Rôle | Propriétaire |
|---|---|
| **Dev** | la compétence elle-même |
| **Test** | le scénario reproductible, nommé |
| **QA** | qui juge la conformité |
| **Cadence** | le rythme d'exécution, ou AUCUNE — et pourquoi |
<!-- /dev-qa-link -->
```

**Une case vide n'existe pas** : on écrit `AUCUNE — <raison>`. *Un état déclaré est une information ;
un silence est un oubli, et rien ne les distingue.*

Détail : [`references/ensembles-de-skills.md`](references/ensembles-de-skills.md).

---

## Axe 7 — PLUGIN

**Si une copie de cette compétence vit dans un pack publié, elle se remet à niveau dans la MÊME
passe.** Sinon le pack dérive en silence chez tous ceux qui l'ont installé — **et rien ne casse**,
donc personne ne le voit.

⚠️ **Se remettre à niveau ne veut pas dire recopier.** Une copie de pack est une adaptation
volontaire : dépersonnalisée, sans chemins machine, sans renvoi vers une compétence absente du pack.
L'écraser republie exactement ce que la dépersonnalisation avait retiré.

**Le geste** : repartir du point où les deux ont divergé, rejouer l'écart, repasser les contrôles.

> 🩸 **Cet axe était le septième d'un contrôle qui s'annonçait « 6 axes ».** Un contrôle qui annonce
> moins d'axes qu'il n'en applique fait passer le dernier pour facultatif — et c'est justement celui
> qui empêche un pack publié de mentir à ses installateurs.

---

## Décider du NIVEAU — ici, pas ailleurs

À la création ou à l'édition, **trancher où vit la compétence** :

- spécifique à un dépôt ou un dossier, **ou** lourde et utile à un seul projet → ce niveau ;
- **légère et transverse** (utile à deux projets ou plus) → le niveau global ;
- **au doute, on remonte** : mal placer bas coûte du temps à tout recréer, un cran trop haut coûte
  quelques jetons.

---

## Fini quand

Les 7 axes passent, ou l'écart est **déclaré avec sa raison**. Un axe muet compte comme un échec.
---

<!-- dev-qa-link -->
| Rôle | Propriétaire |
|---|---|
| **Dev** | cette compétence — c'est elle le contrôle |
| **Test** | les 7 axes, appliqués à la compétence qu'on vient d'écrire |
| **QA** | `AUCUNE` distincte — le gate **est** le verdict ; un axe muet compte comme un échec |
| **Cadence** | `AUCUNE` — elle se déclenche avant de dire qu'une compétence est prête |
<!-- /dev-qa-link -->
