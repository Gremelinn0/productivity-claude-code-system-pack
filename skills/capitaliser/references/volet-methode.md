# Volet 2-3 · la MÉTHODE — le savoir du métier

> Annexe de **`/capitaliser`**. On l'ouvre **quand on doute**, jamais à chaque
> invocation. Le geste et l'ordre vivent dans le `SKILL.md`.
>
> **L'objet** : une **méthode** — comment on s'y prend, quel interdit tient, dans quel ordre, quel
> piège a déjà été payé.
>
> ⚠️ **Cette annexe ne dit pas COMMENT on construit une compétence** — ça appartient à
> `/skill-quality-guard` (les 7 axes) et à la compétence qui fabrique tes compétences. Elle dit
> **OÙ un fait va** une fois qu'on a décidé de l'écrire — rien d'autre.

## 🚨 LA RÈGLE, ET ELLE N'A PAS D'EXCEPTION DE CONFORT

> **La règle, en une phrase** : on écrit dans les fichiers **associés** à la compétence, plutôt que
> dans la compétence elle-même.

**Un fait neuf va dans `<compétence>/references/<sujet>.md`. Le `SKILL.md` ne reçoit que ce dont un
lecteur a besoin À CHAQUE invocation.**

**Le contrôle, décidable, avant d'écrire une ligne dans un `SKILL.md`** :

> *Est-ce que quelqu'un qui invoque cette compétence pour travailler a besoin de cette ligne
> maintenant — ou seulement le jour où il doute ?*

Le jour où il doute → **annexe**. Pas « plus tard », pas « quand ça deviendra gros » : maintenant,
au moment où on l'écrit.

### Pourquoi ce n'est pas du rangement, mais un COÛT

Un `SKILL.md` est chargé **en entier**, dans **chaque** session qui déclenche la compétence, **pour
toujours**. Une annexe n'est lue que quand on la cite. Donc une jurisprudence de quarante lignes
gravée dans un `SKILL.md` n'est pas « une compétence un peu longue » : c'est **un péage prélevé sur
toutes les invocations futures**, y compris celles qui n'ont rien à voir avec elle.

🩸 **Mesuré sur le parc** : **18 compétences dépassent le plafond de 500 lignes, 5 272 lignes de
débordement** — dont le registre des chantiers de ton projet (562), c'est-à-dire la compétence qui porte le chantier de
ménage du système. Le plafond existait depuis toujours ; **personne ne le comptait**. La dette ne
s'est pas construite par négligence, elle s'est construite **une bonne ligne à la fois**.

## 📐 Ce qui RESTE en haut, ce qui DESCEND

| Reste dans le `SKILL.md` | Descend en annexe |
|---|---|
| la **règle** et l'**interdit** | l'**historique daté** et les cas inauguraux |
| l'**ordre** à respecter | la **jurisprudence** (« ce qu'on a essayé et écarté ») |
| le **contrôle décidable** (la question qu'on se pose) | les **mesures** et leurs chiffres |
| le **pointeur** vers l'annexe | les **dossiers d'instruction**, les tables longues |
| le bloc `<!-- dev-qa-link -->` | les **variantes par objet ou par plateforme** |

**Le test du lecteur pressé** : il ouvre le `SKILL.md`, il ne lit que lui, et il doit repartir avec
**tout l'opérationnel**. S'il lui manque un geste, on a trop descendu. S'il traverse trois écrans de
récit avant le premier geste, on n'a pas assez descendu.

**Une annexe vit sous le MÊME propriétaire** : `<compétence>/references/<sujet>.md`. **Jamais une
deuxième compétence** (un sujet, un propriétaire, un point
d'entrée). Créer un second artefact pour désengorger le premier, c'est de l'entropie déguisée en
rangement.

## 🛑 VÉRIFIER AVANT DE COUPER — le geste que tout le monde saute

**Le bloc qui ressemble le plus à un doublon n'en est pas forcément un.** Le contrôle tient en une
question : *ce bloc **RECOPIE**-t-il, ou **POINTE**-t-il ?*

*Mesuré : sur la porte du domaine concerné, les 55 lignes du « parcours d'achat » avaient une doc
produit de 345 lignes sur le même sujet — candidat parfait. Elles ne recopiaient rien : elles
pointaient vers elle et portaient des décisions absentes partout ailleurs. Les couper aurait détruit
le design qu'elles incarnent.*

⚠️ **Et le piège plus grand, celui qui a failli coûter la moitié d'un corpus** : un **ratio
volumétrique compare des volumes, jamais des contenus**. Quinze journaux de boucle affichaient cinq
lignes de protocole pour une ligne de mémoire — le ratio désignait 5 074 lignes comme du doublon
recopié. **La lecture réelle, bloc par bloc, en a rendu 2 554 (50 %) utiles et absentes partout
ailleurs**, dont une décision produit que l'utilisateur avait tranchée **deux fois**. Supprimer sur le
ratio, c'était appeler « ménage » une perte de moitié — et une perte **invisible**, puisqu'un
dossier vidé a l'air d'un dossier rangé.

**⛔ On ne déplace pas un bloc qu'on n'a pas LU.** Aucun ratio, aucun compteur, aucune ressemblance
de titre ne remplace la lecture.

## 🔍 Prouver la non-perte, sinon alléger est indistinguable de perdre

Après avoir descendu du contenu : sonder des **chaînes retirées** et vérifier qu'elles existent
d'un côté ou de l'autre. Sans cette preuve, le geste a la même signature qu'une suppression — et
l'archive a l'air d'un geste sain, c'est précisément ce qui la rend dangereuse.

```bash
rg --no-ignore "<une phrase retirée>" `skills/<compétence>/
```

## 🔗 Ce que l'annexe doit dire d'elle-même

Une annexe qui ne dit pas **de qui elle est l'annexe** devient un document orphelin, et un document
orphelin se re-crée ailleurs six semaines plus tard. Elle porte donc, en tête :

- **l'objet** qu'elle couvre, en une phrase ;
- **ce qu'elle ne couvre PAS**, et vers qui ça route ;
- son **historique** si elle vient d'ailleurs — d'où le contenu a été déplacé, et quand.

Et le `SKILL.md` la **cite explicitement**, avec la raison de l'ouvrir : *« quand tu doutes de X,
lis `references/x.md` »*. Une annexe que le `SKILL.md` ne nomme pas n'est jamais lue.

## ✅ Fini quand

- Le fait neuf est dans une annexe, et le `SKILL.md` la cite avec la raison de l'ouvrir.
- Le `SKILL.md` a **baissé** ou n'a pas monté : `wc -l `skills/<x>/SKILL.md`.
- Ce qui a été descendu se retrouve par `rg --no-ignore` — la non-perte est prouvée, pas supposée.
- Rien n'a été coupé sans avoir été lu.

**Les trois contrôles à outiller, si tu ne devais en avoir que trois :**

- le **poids** de chaque `SKILL.md` — sous le plafond que tu t'es donné ;
- la **déclaration** Dev / Test / QA / Cadence — présente, jamais muette ;
- les **renvois** — chaque fichier cité existe vraiment.
