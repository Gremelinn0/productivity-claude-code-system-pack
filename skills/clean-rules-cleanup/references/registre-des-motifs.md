# Registre des motifs — pourquoi chaque règle existe

> **Ce que ce fichier répond, et rien d'autre** : *pourquoi cette règle a-t-elle été inscrite,
> et cette raison tient-elle encore aujourd'hui ?*
>
> Il ne se charge jamais tout seul. Il est lu par la compétence — au moment de graver une règle
> (mode NOUVELLE RÈGLE, on y écrit) et au moment de faire le ménage (Phase 1, on le lit pour
> juger). Ailleurs, il coûte zéro jeton.

## Pourquoi il existe

Une règle chargée à chaque session doit porter **le comportement et son contrôle**, rien de plus.
Donc au fil des nettoyages, le « pourquoi » se fait couper : le cas payé, le chiffre, la phrase
exacte qui l'a déclenchée. Il part dans l'historique Git, c'est-à-dire nulle part.

Trois mois plus tard, personne ne sait plus si la règle protège encore quelque chose. Elle n'est
donc **jamais retirée** — au doute on garde, et le corpus grossit d'un cran de plus. À chaque
passe, le ménage ne sait plus que **compresser**, et le fichier remonte.

Le registre casse ça : la prose descend ici, la règle reste maigre, et le ménage peut **juger**
au lieu de supposer.

## Les sept colonnes

| Colonne | Ce qu'on y met | Ce qui la rend inutile |
|---|---|---|
| **ID** | `<PRÉFIXE>-<date de gravure>-<slug>`, généré par `scripts/registre.py sync`. Stable même si la section est renumérotée. | Le réécrire à la main. |
| **Adresse** | Fichier · § · titre court de la règle. | Un numéro de section seul — ils bougent. |
| **Gravée** | Date ISO de la gravure d'origine, jamais celle du dernier amendement. | — |
| **Déclencheur** | **Ce qui a été payé** : le cas inaugural en une phrase, avec son chiffre s'il existe, et la demande exacte s'il y en a une. | Une justification abstraite (« pour éviter les erreurs ») : elle est vraie de toutes les règles, donc elle n'en défend aucune. |
| **Contrôle** | La question **décidable** qui fait respecter la règle, telle qu'elle est écrite dans le corpus. Vide → la règle est un vœu. | Un jugement (« vérifier que c'est bien fait »). |
| **Péremption** | **Ce qui rendrait la règle caduque**, écrit de façon vérifiable : un outil qui disparaît, une plateforme abandonnée, un mécanisme réparé en amont, une date. `—` = rien ne la périme (règle de comportement pure). | « à revoir plus tard ». |
| **Revue** | `<date> — <verdict>` du dernier passage : `VIVANTE`, `AFFAIBLIE`, `PÉRIMÉE`, `FUSIONNÉE dans <id>`. `jamais` tant que personne n'a regardé. | Cocher `VIVANTE` sans avoir rien mesuré. |

### La colonne qui fait tout le travail, c'est **Péremption**

Les six autres décrivent le passé — elles se relisent, et **une raison écrite se croit**. Seule la
péremption rend le ménage *décidable* : elle dit à l'avance à quoi ressemblerait un monde où la
règle ne sert plus, et ce monde-là se **mesure**.

Sans elle, un ménage ne peut faire que deux choses : garder par prudence, ou couper au flair.

**Le contrôle, en écrivant une péremption** : *pourrais-je, aujourd'hui, lancer une commande ou
ouvrir un fichier qui me dise si c'est arrivé ?* Non → ce n'est pas une péremption, c'est un vœu,
et la règle restera indéfiniment.

## Comment on s'en sert

```bash
python scripts/registre.py audit CLAUDE.md
```

- **`sync`** — scanne le corpus, ajoute en squelette toute règle datée absente du registre.
  Ne réécrit jamais une cellule déjà remplie.
- **`audit`** — rend ce qu'un ménage doit regarder : motifs manquants, contrôles manquants,
  règles disparues du corpus (motif orphelin), péremptions échues, revues trop vieilles,
  règles regravées après retrait.
- **`show <motif>`** — sort les lignes qui contiennent un mot, avant de toucher à une règle.

Sans argument, les emplacements usuels d'un fichier de règles sont essayés. L'expression qui
repère une gravure (`GRAVURE`, en tête du script) s'adapte au marqueur employé par votre corpus :
par défaut « gravée AAAA-MM-JJ », « inscrite le … », « ajoutée le … ».

## Ce que ce fichier n'est pas

- **Pas un journal de passes.** Un journal raconte les *passes* (date, action, delta de lignes).
  Ici, une ligne par **règle**, et elle vit aussi longtemps que la règle.
- **Pas une archive.** Une règle retirée voit sa ligne passer en `PÉRIMÉE` avec la date et le
  motif du retrait, puis descendre dans « Motifs archivés » — jamais supprimée : c'est la trace
  qui empêche de la regraver six mois plus tard, et `audit` signale la regravure.
- **Pas un gate.** `audit` ne bloque rien. Il rend une liste ; c'est le ménage qui tranche —
  un gate qui crie au loup finit ignoré.

---

## Table

Vide au départ : `sync` la remplit en squelettes, vous écrivez les motifs.

| ID | Adresse | Gravée | Déclencheur — ce qui a été payé | Contrôle | Péremption — ce qui la rendrait caduque | Revue |
|---|---|---|---|---|---|---|

---

## Motifs archivés

Les règles retirées descendent ici avec leur ligne intacte, `Revue` = `<date> — PÉRIMÉE : <motif du retrait>`.
Aucune ligne ne se supprime : elle est ce qui empêchera de regraver la même règle plus tard.

| ID | Adresse | Gravée | Déclencheur — ce qui a été payé | Contrôle | Péremption — ce qui la rendrait caduque | Revue |
|---|---|---|---|---|---|---|
