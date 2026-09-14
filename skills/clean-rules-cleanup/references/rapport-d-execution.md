# Le rapport d'exécution d'un ménage — gabarit

> Un ménage de règles n'est fini que quand la personne qui l'a demandé peut relire, règle par règle,
> **ce qui est parti, où, et pourquoi** — sans avoir à faire confiance. Ce fichier est le gabarit du
> `RAPPORT.md` que la Phase 4 dépose dans l'archive de la passe, à côté des préimages.

Le fichier vit dans `_archive/<date>-rules-cleanup/RAPPORT.md`. Il se lit en trois minutes ; le
message qui l'annonce tient en trois lignes et donne son lien.

---

## 1. Ce que ça change (trois lignes, pour la personne)

Les fichiers de règles repassent sous les plafonds. **Aucune règle n'a été retirée, aucun contrôle
non plus** : ce qui est parti, ce sont les récits — le cas payé, la date, le chiffre, la citation
longue — et ils vivent maintenant dans le registre des motifs, une ligne par règle.

| | Avant (`<commit>`) | Après | Plafond |
|---|---|---|---|
| `<fichier 1>` | `<n>` lignes · `<n>` octets | `<n>` lignes · `<n>` octets | `<n>` · `<n>` |

Gate rejoué : `<résultat>`. Tests : `<résultat>`.

## 2. Comment ça s'est fait

1. **Archive** de la préimage exacte (manifeste : commit, blob, empreinte, restauration).
2. **Carte** : le registre des motifs audité — quelles règles ont déjà leur motif, lesquelles pas.
3. **Décision par règle** : `KEEP` (intacte) · `COMPRESS` (règle + contrôle gardés, le récit descend
   au registre) · `FUSION` (plusieurs formulations réunies) · `PÉRIMÉE` (retirée, avec sa raison).
4. **Non-perte** : chaque détail de la préimage — date, chiffre, chemin, verbatim — absent du
   fichier final est cherché **dans sa destination** (registre, propriétaire nommé). Le compte des
   introuvables est écrit ici, et il vaut zéro ou la passe n'est pas finie.
5. **Registre** : lignes neuves, lignes enrichies, doublons fusionnés (jamais supprimés).

## 3. Règle par règle

| § | Règle (gardée) | Décision | Ce qui est parti | Où | Pourquoi |
|---|---|---|---|---|---|
| `<n>` | `<la règle en une ligne, avec son contrôle>` | COMPRESS | `<le récit, le chiffre, la citation>` | `<identifiant au registre, ou propriétaire>` | `<en quelques mots>` |
| `<n>` | `<…>` | KEEP | — | — | — |

Verbatims **gardés** dans le fichier : `<liste courte>`.
Verbatims **descendus** au registre : `<liste courte, avec l'identifiant de la ligne>`.

## 4. Rien de supprimé

- Les préimages sont dans ce dossier, octet pour octet, avec leur commit.
- Les lignes du registre fusionnées gardent leur texte intact, sous « Motifs archivés ».
- Ce qui a été retiré (`PÉRIMÉE`) est listé ci-dessus avec sa raison — une ligne chacune, pour
  qu'on puisse dire « non, garde celle-là ».

---

**Le contrôle, avant de clore la passe** : *chaque règle de la préimage a-t-elle sa ligne dans la
table du §3 ?* Une règle sans ligne est une règle dont personne ne saura ce qu'elle est devenue.
