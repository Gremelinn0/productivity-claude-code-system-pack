# Claude Code System Pack

**Trois commandes au quotidien, trois spécialistes et un routeur facultatif.**
Pour entretenir les compétences, les règles et le système d'un agent après un retour concret.

---

## Le problème

Un agent qu'on utilise sérieusement finit par accumuler des instructions. Une règle par correction,
une compétence par sujet, un document par décision. Rien de tout ça n'est mauvais pris isolément, et
c'est exactement ce qui rend le problème invisible.

Trois symptômes, et ils arrivent toujours dans cet ordre :

1. **L'agent supporte le désordre — toi, non.** Il lit trois mille lignes de règles sans se
   plaindre. Toi, tu ne sais plus ce que tu lui as demandé, ni où c'est écrit.
2. **L'entretien prend plus de temps que le travail.** Chaque compétence qu'on touche oblige à
   vérifier ce qu'elle rend faux ailleurs — et on le fait à la main, à chaque fois.
3. **On répète sans arrêt les mêmes instructions.** Parce qu'une leçon apprise en session ne va
   nulle part : elle meurt avec la conversation.

Ce pack n'ajoute pas d'instructions. Il donne les **gestes qui entretiennent** celles que tu as
déjà.

---

## Une porte facultative — `/router-entretien-systeme`

Le routeur [`router-entretien-systeme`](skills/router-entretien-systeme/SKILL.md) identifie le
**symptôme**, choisit l'un des six responsables et transmet son contexte.
Il ne fusionne pas leurs méthodes et n'exécute pas lui-même les changements.

| Tu observes… | Première compétence |
|---|---|
| L'agent refait une erreur déjà corrigée | `/capitaliser` |
| Des règles gonflent ou s'entassent | `/clean-rules-cleanup` |
| Des compétences se contredisent ; tu veux mesurer avant d'optimiser | `/optimise-systeme` |
| Une compétence doit être créée, refondue ou vérifiée | `/skill-quality-guard` |
| Plusieurs compétences doublonnent ou sont mal rangées | `/skill-cleaner` |
| Une page ou une carte humaine décrit encore l'ancien système | `/propage-systeme` |

Les trois commandes quotidiennes s'invoquent directement. Le routeur aide à choisir le spécialiste pour une demande transversale. En cas de plusieurs gestes,
le routeur appelle les propriétaires dans l'ordre, puis rapporte ce qui a
**réellement été vérifié**, sans inventer de mesure.

---

## Les compétences

| Commande | Responsabilité |
| --- | --- |
| `/capitaliser` | Transformer les apprentissages et livrables en savoir retrouvable. |
| `/clean-rules-cleanup` | Créer et entretenir les règles et, sur autorisation, les hooks. |
| `/optimise-systeme` | Améliorer le système de la tâche en cours et orchestrer les spécialistes ; revue complète sur demande. |
| `/skill-cleaner` | Ranger, comparer, fusionner ou archiver les compétences d'un parc avec preuve de non-perte. |
| `/skill-quality-guard` | Fabriquer, refondre, vérifier et resynchroniser une compétence avec `skill-creator` d'Anthropic. |
| `/propage-systeme` | Actualiser toutes les sources que le changement rend fausses. |

Les trois premières sont les **entrées quotidiennes**. Les autres sont des
spécialistes appelés selon la nature de l'intervention.

Une copie distribuée conserve **les mêmes responsabilités et capacités** que
sa source. Seuls les détails propres à un environnement sont adaptés.

## Installation

```bash
/plugin marketplace add Gremelinn0/productivity-claude-code-system-pack
```

```bash
/plugin install claude-code-system-pack
```

Commence par **`/capitaliser`**, **`/clean-rules-cleanup`** ou **`/optimise-systeme`**, selon le besoin. Pour une demande transversale, `/router-entretien-systeme` reste une entrée facultative. Les trois spécialistes `/skill-cleaner`, `/skill-quality-guard` et `/propage-systeme` sont aussi invocables directement.

Chacune se déclenche aussi toute seule sur ce que tu écris — « le système est en bordel »,
« ajoute cette règle », « on répète toujours la même chose ». C'est le rôle de leur `description:`,
et c'est pour ça que le pack en soigne la rédaction plutôt que la longueur.

> **Version 0.4.0** — ajout de `router-entretien-systeme` : porte d'aiguillage sans copie des méthodes. **Migration 0.3.0** — `dev-capitaliser` s'appelle désormais **`capitaliser`**. Le geste public
> est volontairement transversal : il adapte sa preuve et sa destination à l'environnement au lieu
> de supposer un projet de développement.

---

## 🌍 Portabilité

Ces compétences décrivent des **méthodes**, pas une configuration. Elles ne supposent ni ton
système d'exploitation, ni ton arborescence, ni tes autres compétences. Voici tout de même ce qu'il
faut savoir avant de les lancer.

| | Ce que c'est | Ce que tu dois savoir |
|---|---|---|
| **Prérequis** | Claude Code, et un dossier de compétences (`~/.claude/skills/` ou `.claude/skills/` dans ton projet) | rien à installer de plus |
| **Le code fourni** | un extrait Python dans `optimise-systeme` (lisibilité des `description:`, nécessite `pyyaml`) et deux scripts en bibliothèque standard : `clean-rules-cleanup/scripts/registre.py` (le registre des motifs) et `propage-systeme/scripts/derive_bloc.py` (une règle vit une fois, ses copies sont dérivées et contrôlées) | chacun a son `--self-test` ; tout le reste marche sans |
| **Chemins** | `skills/*/SKILL.md` et `~/.claude/skills/*/SKILL.md` | ce sont les emplacements standards ; adapte si tu ranges ailleurs |
| **Système** | testé sous Windows, écrit sans dépendance système | l'extrait Python utilise `expanduser`, donc il marche aussi sous macOS et Linux |
| **Tes propres contrôles** | les compétences te disent **quoi** outiller, jamais avec quel outil | à toi d'écrire les tests dans ton langage et ton harnais |

**Ce qui n'est pas fourni, et c'est délibéré** : aucun crochet, aucun test branché sur ton
harnais. Ces compétences décrivent les contrôles qui valent la peine d'exister chez toi ; elles
n'imposent pas la forme qu'ils prennent. Un contrôle copié d'un autre projet mesure l'autre projet.

---

## Dépendance officielle

Pour fabriquer, refondre et évaluer des compétences, `/skill-quality-guard`
appelle le `skill-creator` officiel d'Anthropic. Il est à installer à part :

```text
/plugin install skill-creator@claude-plugins-official
```

Si cette dépendance est absente, le contrôle le signale et ne prétend
pas avoir exécuté les évaluations. Le pack ne l'installe pas à l'insu de l'utilisateur.

## Ce que ce pack ne fait pas

- **Il ne pose pas de garde-fous mécaniques.** Pour l'étage « contrôles qui bloquent », il y a
  [`claude-code-guardrails`](https://github.com/Gremelinn0/claude-code-guardrails), déjà public. Ce
  pack ne le recopie pas — les deux se complètent : celui-ci décide **ce qu'il faut** contrôler,
  l'autre **fait** le contrôle.
- **Il ne range pas tes compétences à ta place.** Il te dit comment décider, pas quoi décider.
- **Il ne remplace pas la compétence officielle de création de compétences.** `skill-quality-guard` conduit l'intervention et le contrôle final en appelant l'outil officiel pour la rédaction et les essais.

---

## Un principe partagé par ces compétences

**Une règle utile porte son contrôle.**

*« Sois rigoureux »* n'est pas une règle, c'est un vœu — personne ne peut savoir en la lisant s'il
est en train de la violer. *« Avant d'écrire un chiffre d'état : ai-je lancé l'instrument dans cette
passe ? »* en est une, parce qu'elle se répond **en une seconde, sans interprétation**.

Et la ligne de partage qui suit : ce qui est **décidable** (un lieu, une présence, un format, un
compte) peut bloquer ; ce qui relève du **jugement** (la qualité, la pertinence, le ton) se montre
sans trancher. Un contrôle de jugement qui bloque crie au loup, finit désactivé, et emporte les
décidables avec lui.

---

## Licence

MIT.
