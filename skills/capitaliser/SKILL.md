---
name: capitaliser
description: >-
  Après une tâche, un plan, une correction ou une décision, transforme ce qui vient d'être appris
  en savoir réutilisable au bon endroit au lieu de le laisser mourir dans la conversation. Trouve
  ce qui mérite d'être gardé, son propriétaire et la surface réellement relue la prochaine fois ;
  conserve le fait ET le pourquoi, corrige ce que la nouvelle information rend faux ailleurs, puis
  vérifie qu'aucune information utile n'a été perdue. S'adapte à un repo de code, une base de
  connaissance, Notion, des docs, un workflow marketing ou un autre environnement. Déclenche sur
  « capitalise », « garde ce qu'on a appris », « mémorise ça », « documente cette décision »,
  « on vient de finir », « range le fait et le pourquoi », « je ne veux pas qu'on refasse cette
  erreur », « on l'a déjà mesuré » — et en fin de travail quand une leçon durable vient d'apparaître.
---

# /capitaliser — empêcher le système de reperdre la même leçon

## Le résultat attendu

Cette compétence ne fabrique pas un compte rendu de session.

Elle répond à une question :

> **Qu'est-ce qui vient d'être appris et qui évitera de refaire le même chemin la prochaine fois ?**

Une bonne capitalisation rend le savoir **retrouvable au moment d'agir**. Un texte parfaitement
écrit dans un endroit que personne ne recharge est une archive, pas une mémoire utile.

Le passage se termine par un verdict explicite :

- **ÉCRIT** — un apprentissage durable a été rangé chez son propriétaire ;
- **RIEN** — la tâche n'a produit aucun savoir durable à ajouter ;
- **NON PERSISTÉ** — un apprentissage existe mais l'environnement ne permet pas de l'écrire de
  façon fiable ; rendre alors la destination proposée et le patch à appliquer.

Ne jamais inventer du contenu pour satisfaire le rituel.

## 1. Décider ce qui mérite d'être gardé

Garder seulement ce qui a une forte chance de resservir :

- un fait mesuré, avec son périmètre ;
- une décision et **la raison** qui l'a fait gagner ;
- une option refusée et la raison du refus ;
- une méthode qui a réellement fonctionné ;
- un piège payé et son symptôme reconnaissable ;
- une règle réutilisable ;
- une frontière claire entre deux propriétaires ;
- un contrôle ou critère de fin qui évite une erreur silencieuse ;
- l'adresse d'un livrable réutilisable si le projet possède déjà un registre d'assets.

Ne pas garder :

- le récit chronologique de la session ;
- un statut temporaire ;
- une intuition non vérifiée présentée comme un fait ;
- une reformulation déjà présente ;
- une liste de tentatives sans leçon générale.

**Une cause n'entre comme cause que si elle est prouvée.** Sinon écrire le fait observé et marquer
la cause comme non mesurée.

## 2. Trouver le propriétaire ET le point de chargement

Deux questions séparées :

1. **Qui possède ce savoir ?**
2. **Où le prochain agent le lira-t-il réellement avant de refaire le geste ?**

Ordre de préférence :

1. la compétence, le process, la page ou la documentation qui possède déjà le sujet ;
2. la source canonique du projet ou du métier ;
3. une règle globale uniquement si elle vaut réellement partout.

Ne jamais créer automatiquement un nouveau dossier « mémoire », un rapport de session ou une
nouvelle compétence juste pour ranger quelque chose.

**Le bon propriétaire n'est pas suffisant si sa surface n'est jamais chargée.** Quand une règle doit
mordre avant une action, sa version courte doit vivre dans la surface effectivement lue à ce moment.
Le détail peut rester dans la source canonique et être pointé depuis cette entrée courte.

## 3. Écrire le fait ET le pourquoi

Une entrée durable garde au minimum :

- **le fait / la décision** ;
- **pourquoi** c'est vrai ou pourquoi ce choix a gagné ;
- **la preuve ou la source** quand elle existe ;
- **la portée** : où cela s'applique et où cela ne s'applique pas ;
- **la condition de réouverture** si la décision peut changer.

Une décision sans sa raison protège mal contre le retour d'une ancienne option sous un autre nom.

Corriger l'entrée existante plutôt qu'empiler deux versions contradictoires.

## 4. S'adapter à l'environnement

La méthode ne dépend pas d'un outil précis.

| Environnement | Destination habituelle | Preuve utile |
|---|---|---|
| **Repo de code / système de skills** | compétence propriétaire, références, règles ou docs du projet | diff / historique Git, tests ou gate existant |
| **Notion / wiki / base de connaissance** | page ou base canonique du sujet | historique de page, comparaison avant/après, liens résolus |
| **Marketing / sales / ops** | process propriétaire, CRM, playbook, automation ou doc de campagne | champ/source relu, run de workflow, version du playbook |
| **Fichier local / document** | document canonique existant | copie avant/après ou historique de fichier |
| **Aucune surface persistante accessible** | ne rien prétendre avoir mémorisé | rendre le patch + la destination proposée : **NON PERSISTÉ** |

Utiliser les conventions déjà présentes dans l'environnement. Ne pas imposer Git, un squelette de
fichiers ou Notion à quelqu'un qui n'en a pas.

### Cas avancé : système de compétences

Si le projet entretient un parc de skills et veut un squelette stable, les annexes de cette
compétence donnent un modèle possible :

- [`references/raisonnement.md`](references/raisonnement.md) — garder décisions, refus, mesures et ouverts ;
- [`references/squelette.md`](references/squelette.md) — exemple de structure propriétaire ;
- [`references/volet-produit.md`](references/volet-produit.md) — distinguer produit et méthode ;
- [`references/volet-methode.md`](references/volet-methode.md) — ranger une méthode réutilisable ;
- [`references/volet-environnement.md`](references/volet-environnement.md) — isoler les différences de contexte.

Ces annexes sont **des patrons**, pas des prérequis. Un utilisateur non-développeur peut utiliser
`/capitaliser` sans adopter cette arborescence.

## 5. Propager ce que l'apprentissage rend faux

Après l'écriture, demander :

> **Qu'est-ce qui vient de devenir faux ailleurs parce que cette information a changé ?**

Exemples : une autre règle, une documentation, un template, un workflow, une page d'aide, une
automatisation, une carte d'architecture.

Corriger les surfaces actives qui portent l'ancienne vérité, ou nommer explicitement ce qui reste à
propager. Une source canonique correcte entourée de copies fausses ne suffit pas.

## 6. Prouver la non-perte

La preuve dépend de l'environnement ; le principe ne change pas.

### Avec historique ou versioning

- conserver l'état avant modification ;
- comparer avant / après ;
- vérifier que chaque fait durable retiré de la source existe encore à destination ;
- si un bloc est simplement déplacé, préférer le déplacement intact à la réécriture ;
- une suppression accidentelle d'information utile fait échouer la passe.

### Sans historique exploitable

- relever les faits durables de la source avant réécriture ;
- après modification, vérifier chacun d'eux dans la nouvelle destination ;
- si cette vérification n'est pas fiable, ne pas faire une grosse réécriture destructive :
  ajouter ou proposer un patch ciblé.

**« C'est plus court » n'est jamais une preuve de non-perte.**

## 7. Ne pas recopier ce qui doit être calculé

Un chiffre qui évolue, un stock, un état de file ou un résultat de métrique ne doit pas être copié
partout comme une vérité permanente.

Quand c'est possible, garder :

- la source ;
- la requête, commande ou instrument qui rend la valeur ;
- le dernier résultat daté seulement s'il aide réellement à reprendre.

Le but de la capitalisation est d'éviter les vérités périmées, pas d'en créer.

## Fini quand

- le verdict **ÉCRIT / RIEN / NON PERSISTÉ** est explicite ;
- chaque apprentissage gardé a un propriétaire ;
- il est écrit là où le prochain utilisateur ou agent peut réellement le rencontrer ;
- le fait et sa raison sont conservés ;
- la portée et la preuve sont claires quand elles comptent ;
- aucune information utile n'a disparu pendant le rangement ;
- les surfaces rendues fausses ont été corrigées ou listées comme reste ;
- aucun nouveau « dossier mémoire » n'a été créé par défaut.

## Anti-patterns

- « Résumé de la session » comme destination de mémoire durable.
- Créer une nouvelle compétence pour ranger une leçon qui appartient déjà à une autre.
- Garder seulement « on a choisi A » sans pourquoi.
- Transformer une intuition en cause certaine.
- Recopier un chiffre mouvant au lieu de garder son instrument.
- Mettre une règle dans une annexe que l'agent fautif ne lira jamais avant d'agir.
- Dire « mémorisé » quand aucun stockage persistant n'a réellement été modifié.
- Exiger Git, du code ou une arborescence précise dans un environnement qui n'en a pas.

## Sortie courte

Rendre seulement :

```text
CAPITALISATION : ÉCRIT | RIEN | NON PERSISTÉ
Propriétaire : <surface>
Gardé : <1-3 lignes>
Propagation : <corrigé / reste>
Preuve : <comment la non-perte a été vérifiée>
```
