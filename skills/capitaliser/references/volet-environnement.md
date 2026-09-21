# Volet 4 · la PLATEFORME — le savoir du métier

> Annexe de **`/capitaliser`**. On l'ouvre **quand on doute**, jamais à chaque
> invocation. Le geste et l'ordre vivent dans le `SKILL.md`.
>
> **L'objet** : le fonctionnement d'une **application hôte** — sa barre latérale, ses conteneurs,
> comment elle range et nomme ses conversations, sa cardinalité, ses sélecteurs, ses ports, ses
> pièges, ce qui casse et pourquoi.
>
> **Le discriminant, une question** : *si le produit disparaissait, ce fait resterait-il vrai ?*
> Oui → il vit ici. Non → c'est du produit, il vit dans la feature doc.

🩸 **Pourquoi cette annexe existe.** Beaucoup de compétences **lisent** les fiches d'environnement.
Aucune ne **possédait** le geste de les écrire — la règle vivait dans les instructions racine,
trente-huit lecteurs, zéro exécutant. C'est la forme classique du défaut : *l'artefact existe, la
fonction non*. Et le coût se lit en une phrase — **c'est ce qui fait redemander la même chose
cinquante fois**.

## 🌍 Ce qui vaut PARTOUT, et ce qui est une DIFFÉRENCE

La loi d'échelle (`CLAUDE.md` racine) dit que tout ce qu'on décide vaut pour **toutes** les cibles.
Une fiche de plateforme est l'**exception écrite** — et une différence non écrite n'existe pas.

En écrivant, une question : *je décris une **différence propre à cette application**, ou un
**mécanisme** qui vaut pour toutes ?*

- **Différence** (un dossier de données à un endroit inattendu, un suffixe de titre au milieu, un port)
  → elle vit ici, dans la fiche de cette app.
- **Mécanisme** (« on énumère un magasin clé-valeur et on trie par taille, jamais une clé devinée »)
  → il vit chez le **propriétaire du geste**, et la fiche **pointe** vers lui.

⚠️ **Écrire un mécanisme dans une fiche de plateforme le rend invisible aux quatorze autres.** C'est
le défaut le plus cher de la famille, parce qu'il se répète à chaque cible neuve.

## 📍 La structure ne se réinvente pas

`les fiches d'environnement, _TEMPLATE.md` porte le gabarit, et les fiches existantes le suivent :

```text
## 0. Identité              ← cardinalité, ports, exécutable, MULTI/MONO
## 1. Boutons répertoriés
## 2. Zones DOM / UI lues
## 3. Docs et panneaux attachés à la réponse
## 4. Features le produit implémentées ici
## 5. Référence matrice
## 6. Pièges et incidents historiques   ← le plus consulté
```

**Un constat neuf rejoint la section qui le porte déjà.** On n'ouvre pas une section de plus parce
que le sujet paraît nouveau : rassembler bat séparer, et une fiche qui gonfle reste lisible quand
une fiche éparpillée ne l'est plus : un sujet, un propriétaire, un point d'entrée.

**La fiche n'existe pas encore** → la créer depuis `_TEMPLATE.md`, **jamais depuis une fiche
voisine** : on copierait ses différences, et une différence copiée devient un faux fait.

### Les quatre choses qu'un constat doit porter

La troisième est celle qu'on oublie, et c'est la plus utile six mois plus tard.

1. **Le fait**, écrit comme on le dirait à quelqu'un — pas en jargon.
2. **La date**, en clair. Une fiche sans date ne se distingue pas d'une fiche périmée.
3. **Comment on le sait** — l'utilisateur l'a dit · mesuré avec telle commande · lu dans le DOM.
   *Un fait dicté et un fait mesuré ne se re-vérifient pas de la même façon.*
4. **Ce que ça change**, si ce n'est pas évident — quel geste devient faux, quel code doit s'y plier.

⚠️ **Un fait d'hôte périmé est pire qu'un fait absent** : on le relit comme vrai.

## 🕳️ « PAS TROUVÉ » N'EST PAS « INEXISTANT »

Le piège qui coûte un mois, et il se rejoue à chaque cible neuve : **un outil dérivé d'un autre
hérite la structure de données de son parent sans l'utiliser** — la clé est présente, indexée, et
**vide**. Une recherche naïve y conclut « pas de fichier local ». Le vrai magasin vivait ailleurs,
rangé sous le nom du **moteur** et non sous celui du produit.

Les trois règles qui en sortent, pour toute cible neuve :

1. sur un magasin clé-valeur, on **énumère et on trie par TAILLE** — jamais on n'interroge une clé
   **devinée** ; celle qu'on devine est celle qu'on a héritée, donc vide ;
2. l'inventaire des racines **ne se borne jamais aux dossiers qui portent le nom du produit** ;
3. on **compte par FORMAT, jamais par fichier** — un même dossier peut mélanger deux formats sous
   le même nommage, et un comptage naïf se trompe d'un facteur sept.

**Un contenu encodé ne se trahit par aucun `grep` de texte clair** : l'absence de mots lisibles ne
prouve rien.

⇒ **Le critère de fin d'une recherche de magasin** : la fiche porte **soit** le store identifié
avec une extraction prouvée, **soit** `PAS DE STORE LOCAL` **avec la trace de ce qui a été
fouillé**. Jamais un silence — *un silence n'est pas une différence, c'est un oubli*.

## 🧭 La cardinalité se classe AVANT tout code

`la documentation de la fonctionnalité § Vocabulaire cardinalité` porte les définitions. Une plateforme non
classée **MULTI** ou **MONO** se classe dans sa section 0 avant qu'une ligne de code ne la suppose.

⚠️ **Le vide se comble par analogie** : deux sessions différentes ont réinventé « une session égale
une fenêtre » la même semaine, faute de trouver la réponse là où elles la cherchaient — et ça a
justifié un abandon de fonctionnalité. Une case vide ne reste jamais vide longtemps ; elle se
remplit toute seule, et mal.

## ✅ Fini quand

- Le constat est dans la fiche de **son** application, section existante, daté, avec sa provenance.
- Ce qui était un **mécanisme** est parti chez le propriétaire du geste, et la fiche pointe vers lui.
- Rien n'est resté dans une réponse de chat sans être écrit dans la fiche.
- Le commit est parti — une écriture de mémoire ne reste jamais en attente sur un dépôt à quinze
  sessions.

**Deux contrôles qui valent la peine d'être outillés**, une fois que tu tiens des fiches
d'environnement :

- **chaque fiche déclare-t-elle son canal** — celle qui se tait est un oubli, pas une exception ;
- **une fiche neuve fait-elle rougir le contrôle** — sinon il garde un plancher, pas un zéro.
