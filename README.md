# Claude Code System Pack

**Cinq compétences pour entretenir le système d'un agent** — ses règles, ses compétences, sa
documentation — au lieu de le laisser gonfler.

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

## Les cinq compétences

| | Compétence | Le geste |
|---|---|---|
| 1 | **`dev-capitaliser`** | un travail vient de finir : range le **fait** et le **pourquoi** chez leur propriétaire, pour qu'on ne redemande pas la même chose la fois d'après |
| 2 | **`optimise-systeme`** | mesure le système entier — règles, compétences, documents — avant de le juger, puis l'améliore dans l'ordre |
| 3 | **`clean-rules-cleanup`** | écrire, alléger ou déplacer une règle, et décider à quel niveau elle vit |
| 4 | **`skill-quality-guard`** | le contrôle final : sept axes avant de dire qu'une compétence est prête |
| 5 | **`propage-systeme`** | une règle a changé : corrige **toutes** les surfaces qui disaient l'inverse |

**Elles forment une boucle**, et c'est le vrai contenu du pack : une leçon devient une règle (3) →
la règle trouve son niveau (3) → elle se propage partout (5) → le système se re-mesure (2) → ce
qu'on a appris en route se range chez son propriétaire (1) → la prochaine compétence écrite passe
le contrôle (4).

Prises une par une, ce sont cinq outils. Prises ensemble, c'est un cycle de vie.

---

## Installation

```bash
/plugin marketplace add Gremelinn0/productivity-claude-code-system-pack
```

```bash
/plugin install claude-code-system-pack
```

Puis invoque-les par leur nom : `/dev-capitaliser`, `/optimise-systeme`, `/clean-rules-cleanup`,
`/skill-quality-guard`, `/propage-systeme`.

Chacune se déclenche aussi toute seule sur ce que tu écris — « le système est en bordel »,
« ajoute cette règle », « on répète toujours la même chose ». C'est le rôle de leur `description:`,
et c'est pour ça que le pack en soigne la rédaction plutôt que la longueur.

---

## 🌍 Portabilité

Ces compétences décrivent des **méthodes**, pas une configuration. Elles ne supposent ni ton
système d'exploitation, ni ton arborescence, ni tes autres compétences. Voici tout de même ce qu'il
faut savoir avant de les lancer.

| | Ce que c'est | Ce que tu dois savoir |
|---|---|---|
| **Prérequis** | Claude Code, et un dossier de compétences (`~/.claude/skills/` ou `.claude/skills/` dans ton projet) | rien à installer de plus |
| **Un seul bout de code** | un extrait Python dans `optimise-systeme` qui vérifie que tes `description:` sont lisibles | nécessite `pyyaml` — sinon, saute cet extrait, tout le reste marche |
| **Chemins** | `skills/*/SKILL.md` et `~/.claude/skills/*/SKILL.md` | ce sont les emplacements standards ; adapte si tu ranges ailleurs |
| **Système** | testé sous Windows, écrit sans dépendance système | l'extrait Python utilise `expanduser`, donc il marche aussi sous macOS et Linux |
| **Tes propres contrôles** | les compétences te disent **quoi** outiller, jamais avec quel outil | à toi d'écrire les tests dans ton langage et ton harnais |

**Ce qui n'est pas fourni, et c'est délibéré** : aucun test, aucun script de contrôle, aucun
crochet. Ces compétences décrivent les contrôles qui valent la peine d'exister chez toi ; elles
n'imposent pas la forme qu'ils prennent. Un contrôle copié d'un autre projet mesure l'autre projet.

---

## Ce que ce pack ne fait pas

- **Il ne pose pas de garde-fous mécaniques.** Pour l'étage « contrôles qui bloquent », il y a
  [`claude-code-guardrails`](https://github.com/Gremelinn0/claude-code-guardrails), déjà public. Ce
  pack ne le recopie pas — les deux se complètent : celui-ci décide **ce qu'il faut** contrôler,
  l'autre **fait** le contrôle.
- **Il ne range pas tes compétences à ta place.** Il te dit comment décider, pas quoi décider.
- **Il ne remplace pas la compétence officielle de création de compétences.** `skill-quality-guard`
  est un **contrôle final**, pas un générateur.

---

## Une idée qui traverse les cinq

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
