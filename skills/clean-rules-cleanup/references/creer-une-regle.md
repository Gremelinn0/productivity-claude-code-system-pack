# Écrire une règle qui tient — le format long

Détail du **§4** du SKILL.md. Celui-ci donne les cinq étapes ; ce fichier dit comment on fait
chacune, et pourquoi elle existe.

**Le problème que ça résout** : une règle mal écrite ne se voit pas. Elle est là, elle a l'air
raisonnable, et elle ne change rien — parce qu'on ne peut pas savoir en la lisant si on est en
train de la violer. Six mois plus tard il y en a quarante, le budget de contexte est mangé, et le
comportement n'a pas bougé d'un cran.

---

## Les six phases

### Phase 0 — Chercher avant d'écrire

Deux questions, dans cet ordre :

1. **Une règle existante couvre-t-elle déjà ça ?** Le cas normal est *oui, à moitié* — et alors on
   la **complète**, on n'en crée pas une deuxième à côté.
2. **L'archive en contient-elle une version ?** Si une règle a été retirée un jour, savoir
   *pourquoi* évite de la réintroduire telle quelle. Une règle qui revient sans que rien n'ait
   changé va être retirée une deuxième fois.

⚠️ **Deux règles qui se recouvrent à moitié sont pires qu'une règle absente.** Elles se
contredisent sur les bords, et c'est la plus récente — ou la mieux placée — qui gagne, jamais la
plus juste.

### Phase 1 — L'audit des voisines, et c'est un vrai passage obligé

Avant d'écrire, lire **les règles voisines**, pas seulement le titre de la section. Quatre
questions :

| | La question | Ce qu'on en fait |
|---|---|---|
| 1 | Une voisine dit-elle **déjà** ça ? | on la complète, on ne double pas |
| 2 | Une voisine dit-elle **l'inverse** ? | on tranche laquelle survit, on ne laisse pas les deux |
| 3 | Ma règle rend-elle une voisine **fausse** ? | on corrige la voisine dans la même passe |
| 4 | Ma règle **appartient**-elle à une voisine ? | on l'écrit dedans, pas à côté |

**La quatrième est celle qu'on saute.** Une idée nouvelle arrive presque toujours sous forme de
bloc autonome, alors qu'elle est le plus souvent une **phrase de plus** dans une règle existante.
Un corpus qui grossit par blocs devient illisible ; un corpus qui grossit par phrases reste
navigable.

### Phase 2 — Compresser à deux lignes, avant de placer

Écris la règle en **deux lignes maximum**. Pas comme contrainte de style — comme **test**.

Si tu n'y arrives pas, une de ces trois choses est vraie :

- il y a **plusieurs règles** dans ce que tu écris → les séparer ;
- tu écris un **cas**, pas une règle → le cas va dans un exemple, la règle reste au-dessus ;
- tu n'as **pas encore compris** ce que tu veux interdire → ce n'est pas prêt à être gravé.

Puis donne-lui un **titre court** — celui qu'on lit dans un sommaire. Un titre qui décrit la
situation (« quand un chiffre est périmé ») bat un titre qui décrit la vertu (« rigueur »).

### Phase 3 — Placer, du large vers le spécifique

L'ordre, et on s'arrête à la première qui tranche :

1. **spécifique à un seul dossier ou projet** (ses chemins, son métier, ses données) → à ce
   niveau-là ;
2. **transverse** — utile depuis deux endroits ou plus, ou règle de comportement général → au
   niveau chargé partout ;
3. **au doute, on remonte.**

**Pourquoi on remonte au doute** : mal placer trop bas coûte de recréer la règle dans chaque
projet — donc du temps, à répétition. Un cran trop haut coûte quelques lignes de contexte. Les
deux erreurs ne sont pas du même ordre de grandeur.

### Phase 4 — Proposer, phrase par phrase

Une règle se valide **par tâtonnement**, pas par livraison d'un bloc fini.

1. Montrer **la règle voisine** qui va être touchée, telle quelle.
2. Proposer **une modification minimale** — une phrase qui remplace, complète ou supprime.
3. Attendre.
4. Ajuster si besoin, une proposition à la fois.
5. Le bloc complet (anti-patterns, exemples) ne vient **qu'après** l'accord sur la phrase.

**Pourquoi ce rythme** : personne ne relit attentivement un bloc de quarante lignes de règles. On
valide un bloc en le survolant — donc on valide des choses qu'on n'a pas lues, et on les découvre
trois semaines plus tard en les violant.

### Phase 5 — Écrire d'un coup, et propager

L'écriture est **atomique** : la règle, son interdit, son contrôle, et la correction de ce qu'elle
rend faux ailleurs — dans la même passe.

Ce qui est différé ne se fait pas. Une règle écrite pendant qu'une voisine dit encore l'inverse
laisse le corpus dans un état où **deux réponses coexistent** : la question sera reposée, et c'est
exactement le coût qu'on voulait supprimer.

---

## La forme qui tient

### Une règle utile porte son contrôle

C'est le seul critère qui sépare une règle d'un vœu.

| Vœu | Règle |
|---|---|
| « sois rigoureux » | « avant d'écrire un chiffre d'état : ai-je lancé l'instrument dans cette passe ? » |
| « documente bien » | « ce que je viens de mesurer, quelqu'un le retrouvera-t-il en travaillant ? » |
| « ne casse rien » | « ce bloc recopie-t-il, ou pointe-t-il ? » |

Le contrôle se répond **en une seconde, sans interprétation**. S'il demande un jugement, ce n'est
pas un contrôle — c'est la règle reformulée en question.

### Décidable ou jugement — et ils ne se traitent pas pareil

- **Décidable** — le lieu, la présence, le format, un compte : ça peut **bloquer**.
- **Jugement** — la qualité, la pertinence, le ton : ça se **montre**, ça ne tranche pas.

Un contrôle de jugement qui bloque crie au loup, et finit désactivé. Il emporte alors les
décidables avec lui.

### Écrire pour quelqu'un qui n'est pas développeur

Une règle rédigée en jargon ne sera ni comprise ni appliquée — y compris par toi dans trois mois.

- une idée par ligne, jamais de pavé ;
- chaque terme technique est remplacé par un mot courant, ou expliqué juste après ;
- pas de table dense d'architecture sauf demande explicite ;
- les mots exacts de la personne qui a formulé le besoin sont **repris dans la règle**, pas cités à
  côté entre guillemets.

**Reprendre ses mots n'est pas de la déférence, c'est de la précision** : la formulation d'origine
porte le cas réel ; la reformulation porte ton interprétation du cas réel.

---

## Les anti-patterns

- ❌ **Un bloc neuf** quand une phrase dans une règle existante suffisait.
- ❌ **Une règle sans contrôle** — elle sera lue, approuvée, et jamais appliquée.
- ❌ **Un contrôle de jugement qui bloque** — il sera contourné, puis retiré.
- ❌ **Une citation de trois lignes** au lieu d'une règle d'une ligne qui intègre les mots.
- ❌ **Écrire la règle et différer la propagation** — deux vérités coexistent, la question revient.
- ❌ **Réintroduire une règle archivée** sans regarder pourquoi elle avait été retirée.
- ❌ **Un titre qui nomme une vertu** au lieu de nommer une situation.

---

## Un exemple complet

**Le point de départ, brut** : *« quand tu repères un truc à faire qui sort du sujet, ouvre-moi une
tâche à part au lieu de le faire dans la foulée. »*

**Phase 0** — recherche : rien dans l'archive, rien d'existant sur ce sujet précis.

**Phase 1** — audit des voisines : une règle existe déjà sur la façon de rédiger une consigne pour
un sous-traitant. Question 4 → **oui, ça lui appartient**. Ce n'est pas un bloc neuf, c'est une
phrase de plus chez elle.

**Phase 2** — compression :

> Un travail repéré hors du sujet en cours s'ouvre comme tâche séparée, jamais dans la foulée.

**Phase 3** — placement : c'est du comportement général, valable partout → au niveau transverse.

**Phase 4** — la proposition, en une phrase, ajoutée à la règle voisine. Accord.

**Phase 5** — écriture, plus le contrôle :

> **Le contrôle** : *ce que je m'apprête à faire était-il dans la demande ?* Non → tâche séparée.

Résultat : une phrase ajoutée à une règle existante, un contrôle décidable, zéro bloc nouveau.
