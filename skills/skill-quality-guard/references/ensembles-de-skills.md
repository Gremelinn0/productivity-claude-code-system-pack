# Une compétence ne vit jamais seule — elle appartient à un ensemble

Détail de l'**Axe 6**. Le SKILL.md porte le bloc à remplir ; ce fichier dit pourquoi il existe et
comment décider ce qu'on écrit dedans.

## Le problème

Une compétence qui **produit** quelque chose — du code, une décision, un document, une
configuration — a besoin de deux choses qui ne sont pas elle : un moyen de **rejouer** ce qu'elle
fait, et quelqu'un qui **juge** si le résultat est conforme. Sans ça, elle s'auto-certifie : elle
déclare que ça marche parce que ça a tourné.

Le défaut n'est presque jamais que le test manque. C'est que **personne ne sait s'il manque** —
la compétence n'en parle pas, donc rien ne distingue « pas de test parce qu'on n'en a pas besoin »
de « pas de test parce qu'on a oublié ».

## Les quatre rôles

| Rôle | La question à laquelle il répond |
|---|---|
| **Dev** | qui écrit le changement |
| **Test** | comment on rejoue le comportement, à l'identique |
| **QA** | qui juge la conformité au contrat, et peut refuser |
| **Cadence** | à quel rythme ça tourne, s'il y a un rythme |

Les quatre peuvent être la **même** compétence. C'est fréquent et légitime pour une compétence
petite ou purement documentaire. Ce qui n'est pas légitime, c'est de ne pas le dire.

## La règle, en une phrase

**Le silence est le seul interdit.** Une case se remplit avec un nom, ou avec `AUCUNE — <raison>`.

*Un état déclaré est une information ; un silence est un oubli, et rien ne les distingue de
l'extérieur.*

## Ce qui rend cette règle mesurable

C'est un bloc à format fixe. Une passe automatique peut donc compter les compétences qui le
portent, et celles dont une case est vide — sans juger le contenu, seulement la présence.

C'est la différence entre une règle et un contrôle : la règle demande à chacun d'y penser, le
contrôle rend le trou **visible sans que personne y pense**.

⚠️ **Ne pas confondre la doctrine et le statut.** La doctrine — les quatre rôles, la règle du
silence — vit ici, elle est stable. Le statut — quelle compétence a quoi aujourd'hui — se
**dérive** par une passe qui lit les fichiers. Une table de statut tapée à la main ment en trois
à six semaines, et son mensonge est invisible : elle a l'air à jour parce qu'elle est bien
formatée.

## L'erreur qui coûte le plus cher

Créer une compétence de test **préventivement**, pour toutes les compétences, afin que le contrôle
passe. On obtient un parc où chaque case est remplie et où la moitié des tests ne testent rien.

Le bon geste : **déclarer l'absence**. `AUCUNE — le comportement est vérifié à la main à chaque
usage, il n'y a rien à rejouer` est une réponse complète, et elle est honnête.
