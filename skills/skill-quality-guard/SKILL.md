---
name: skill-quality-guard
description: >-
  Quand une compétence doit être fabriquée, refondue, contrôlée ou resynchronisée
  avec sa copie distribuée, conduire ce geste jusqu'à son verdict. Pour la rédaction,
  l'amélioration et les évaluations comportementales, appeler d'abord le skill officiel
  d'Anthropic skill-creator, s'il est disponible. Porter ensuite les décisions de
  propriétaire, niveau, nommage, routage, Dev/Test/QA, références, non-perte et
  publication sans divulgation. Modes fabriquer / refondre / verifier / resynchroniser.
  Après modification du SKILL.md, vérifier les contrôles applicables avant de dire
  « prêt ». Ne jamais prétendre avoir appelé un plugin absent.
---

# skill-quality-guard — fabriquer, refondre, vérifier et resynchroniser une compétence

## Une seule responsabilité, quatre modes

Cette compétence est **le propriétaire de l'intervention sur une compétence individuelle**.
Elle ne se limite pas à relire une checklist : elle conduit une création, une refonte,
une vérification ou une resynchronisation de copie publique, puis rend un verdict.
Le `/skill-cleaner` s'occupe de **l'organisation d'un parc** ; `/optimise-systeme`
coordonne les améliorations touchant plusieurs éléments du système.

| Demande | Mode | Contrat |
| --- | --- | --- |
| « Crée une compétence » / « crée une famille » | **Fabriquer** | Lire [`references/fabriquer-une-competence.md`](references/fabriquer-une-competence.md) |
| « Reprends / refonds cette compétence » | **Refondre** | Lire [`references/refondre-une-competence.md`](references/refondre-une-competence.md) |
| « Cette compétence est-elle prête ? » | **Vérifier** | Appliquer les axes actifs ci-dessous |
| « La copie du plugin est en retard » | **Resynchroniser** | Lire [`references/resynchroniser-une-copie-publiee.md`](references/resynchroniser-une-copie-publiee.md) |

**Chaîne canonique quand un SKILL.md est écrit ou réécrit :**
1. Appeler le **`skill-creator` officiel d'Anthropic** pour concevoir, éditer et
   tester la compétence (y compris évaluer ses déclencheurs). Son installation
   dépend du plugin officiel `skill-creator@claude-plugins-official`.
2. Dans cette compétence, décider de la responsabilité distincte, de son propriétaire,
   de son niveau, de son nom, de ses renvois et de ses conditions d'exécution.
   Si la compétence appartient à une famille, traiter les dépendances ensemble,
   sans créer de doublons.
3. Appliquer les contrôles ci-dessous et les tests du propriétaire ; vérifier les
   copies publiques concernées **dans la même intervention**, sans recopier de
   données personnelles dans le pack.
4. Rendre `FAIT / BLOQUÉ / NON EXÉCUTÉ` avec chemins réellement touchés, preuves
   lancées, résultat des essais, capacité éventuellement non vérifiée et suite.

Si `skill-creator` est absent, **signaler la dépendance** et expliquer ce qui
ne peut pas être évalué ; un audit statique ne tient pas lieu d'essai comportemental.
Ne jamais déclarer « évalué » ou « prêt » sans exécution des contrôles prévus.

## Vérifications d'intégration — rubriques historiques 1 à 7

**Principe fondamental** : une compétence bien construite s'organise selon une **taxonomie
structurée par concepts**, pas en tas chronologique ni en accumulation de correctifs. À chaque
ajout, se demander : *ce nouveau bloc rentre dans quel concept existant, ou faut-il introduire un
concept clair ?*

Ce contrôle est le **dernier maillon** d'une chaîne : quelque chose écrit la compétence, quelque
chose la conduit et la nomme, **et celui-ci la refuse ou la laisse passer**.

---

## Axe 1 — Poids : seuil historique retiré

Il n'existe **aucun plafond fixe de lignes pour déclarer une compétence valide**.
Le critère est la disponibilité de l'information au moment d'agir : les étapes
indispensables restent dans le `SKILL.md`, les dossiers volumineux et le détail
réservé aux cas particuliers vivent dans des références nommées et réellement
pointées. Les déplacements exigent une preuve de non-perte. Ne pas réduire une
compétence uniquement pour atteindre un quota. Ce retrait est intentionnel ;
les six autres rubriques ci-dessous continuent de s'appliquer.

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

### Une compétence propriétaire est prête pour la reprise

Un propriétaire décrit un contrat complet, pas une microtâche : résultat, sources et état
canonique, progression exécutable, preuves, capitalisation et conditions de fin. Réinvoquée avec
cet état, la compétence doit retrouver le premier geste et poursuivre sans transcript ni prompt
qui recopie sa méthode. Elle ne porte aucun timer et ne s'impose aucune timebox, quantité de lots,
d'actions ou de jetons : un mécanisme de reprise peut la réactiver, mais n'ajoute jamais une
seconde méthode et ne limite jamais l'avancement du tour courant.

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

### Une copie divergente ne ment que si elle est CHARGÉE

Quand on finit par compter la dérive de **tout** le parc, le nombre qui sort fait peur et ne veut
rien dire tout seul. Le discriminant n'est pas *combien de fichiers diffèrent*, c'est **est-ce que
ce pack est activé** — la liste des plugins réellement chargés par le harnais.

- Pack **activé** et divergent → il **ment à qui l'invoque**. Défaut réel, à traiter.
- Pack **désactivé** et divergent → sa dérive **n'atteint personne**, et le re-synchroniser
  **rallumerait un miroir volontairement éteint**. Ne rien lancer.

*Mesure faite une fois : des dizaines de fiches divergentes sur plusieurs packs, **aucun** activé.
Le compte brut aurait déclenché une campagne entière pour zéro effet.*

⚠️ **Et cette lecture est bornée à la machine qui mesure.** Un pack peut être inactif ici tout en
étant **publié et installé ailleurs** : on lit la configuration de **ce** poste, pas celle des
gens qui l'ont installé. Chez eux la dérive est **NON MESURÉE** — et « non mesuré » ne se lit
jamais « nul ». Le rendu doit écrire cette frontière, sinon la conclusion voyage sans elle.

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

Les rubriques actives (2 à 7), les tests adaptés à la modification et la preuve de non-perte passent, ou chaque écart est **déclaré avec sa raison**. La rubrique 1 est retirée et ne doit pas redevenir un seuil de poids. Une dépendance Anthropic non disponible est signalée comme non évaluée, pas présentée comme un succès.
---

<!-- dev-qa-link -->
| Rôle | Propriétaire |
|---|---|
| **Dev** | cette compétence — c'est elle le contrôle |
| **Test** | les 7 axes, appliqués à la compétence qu'on vient d'écrire |
| **QA** | `AUCUNE` distincte — le gate **est** le verdict ; un axe muet compte comme un échec |
| **Cadence** | `AUCUNE` — elle se déclenche avant de dire qu'une compétence est prête |
<!-- /dev-qa-link -->
