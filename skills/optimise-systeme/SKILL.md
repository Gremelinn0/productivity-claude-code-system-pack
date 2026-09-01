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

Ils ont un mécanisme commun : ils consomment le problème sans le résoudre.

1. **Découvrabilité** : une ligne de plus dans un routeur n'est jamais le seul correctif. Agir sur
   ce que l'utilisateur touche : nom, description, déclencheurs et nombre de portes concurrentes.

2. **Propriété** : noter un sujet dans un registre ne le place pas. L'owner doit le retrouver dans
   son propre contrat ; s'il risque de ne jamais être invoqué, un index ou un moment de revue doit
   le rappeler sans devenir du papier peint.

3. **Cliquet** : avant de figer un nombre, demander s'il change sans action humaine. Population ou
   horloge mobiles exigent un arriéré nommé qui ne peut que rétrécir, et une paire de sabotages :
   un cas neuf fautif rougit, plusieurs cas neufs conformes restent verts.

Une décision se rouvre avec une mesure fraîche, jamais au flair. Un remède appliqué une deuxième
fois est d'abord la preuve que le premier n'a pas tenu.

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
