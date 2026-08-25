# Volet 1 · le PRODUIT — le savoir du métier

> Annexe de **`/dev-capitaliser`**. On l'ouvre **quand on doute**, jamais à chaque
> invocation. Le geste et l'ordre vivent dans le `SKILL.md`.
>
> **L'objet** : ce que le **produit** fait, promet, refuse. Le contrat.
>
> ⚠️ Cette annexe ne dit pas **comment** on rédige une feature doc — ça appartient à
> la compétence qui met à jour la documentation produit (les 13 phases) et au gabarit
> `un fichier de référence transverse`. Elle dit **où un fait va**, et **quelle surface se
> met à jour en premier**. C'est là que ça se joue vraiment.

## 🧱 Quatre surfaces, quatre vitesses — et le mélange est la racine

| Ce que je viens d'apprendre | Sa surface | Sa vitesse |
|---|---|---|
| le **contrat** — ce que la feature fait, ses règles numérotées, ses non-objectifs | `la documentation de la fonctionnalité` | **stable** — on vient le lire |
| le **chantier** — tickets, à-faire, mesures du jour | `la documentation des fonctionnalités, <slug>/plan.md` | volatil |
| une **décision** et son anti-yoyo | `la documentation des fonctionnalités, <slug>/decisions.md` | définitif, adressé |
| un **fait daté** — une expérience, un tour de boucle | le journal de la boucle | jetable après agrégation |

🩸 **La racine n'est pas la taille, c'est le mélange.** Sur deux semaines mesurées, **93 % des
écritures** d'un gros fichier de spécification ont atterri dans sa section « travail en cours », et
**zéro** dans la partie qui porte le contrat. Un fichier qui porte à la fois un contrat stable et
un chantier volatil se fait écrire dedans en permanence, et **le contrat se noie**. Personne ne
mentait : chacun ajoutait une ligne juste, au mauvais endroit.

**Le tell le plus fiable** : une **mention d'avancement** (« à porter », « en cours », « pas encore
branché ») est **une date déguisée en fait** — vraie le lundi, fausse le mercredi, jamais relue. Elle
n'appartient pas au contrat. *Une fiche décrit un monde ; un plan décrit un chantier.*

## 🚨 LA RÈGLE LA PLUS IMPORTANTE : un contrat qui CHANGE met à jour d'abord la surface qui sert à le TESTER

> **Le raisonnement qui fonde cette règle** : *« on devra tout retester dans le temps, et aussi
> pour un autre système d'exploitation — c'est pour ça qu'il est vraiment important de bien
> documenter dans les compétences et dans leurs documents associés. C'est la règle la plus
> importante. »*

Écrire la **décision** ne suffit pas. Une décision se lit quand on **conçoit** ; ce qu'on lit quand
on **teste**, c'est la **fiche QA** et la **description fonctionnelle**. Tant que ces deux-là
décrivent l'ancien comportement, elles ne sont pas « en retard » : **elles mentent activement**.

**Le coût est double, et c'est ce qui met cette règle en tête** :

1. **dans le temps** — six mois plus tard, quelqu'un joue le geste décrit, constate autre chose, et
   conclut à une **régression**. Il « répare » un comportement voulu ;
2. **au portage** — la version Mac se construit à partir de ces documents. Une fiche fausse ne
   produit pas un bug sur Mac : elle produit **la mauvaise feature**, et personne ne le voit puisque
   le document le confirme.

**L'ordre, MÊME PASSE, et il est l'inverse de l'ordre naturel** :

1. la **fiche QA** — l'item qui décrit le geste ;
2. la **description fonctionnelle** — ce que l'utilisateur lit ;
3. la **compétence** propriétaire (la méthode) ;
4. la **décision** et son anti-yoyo.

Beaucoup font (4) d'abord, et s'arrêtent là.

**Le contrôle qui tranche, en une question** :

> *Quelqu'un qui ne lit QUE la fiche QA rejouerait-il le bon geste, et attendrait-il le bon
> résultat ?*

Non → la vague n'est pas finie, quels que soient le code et les tests verts.

⚠️ **Contrat dont la promesse est une ABSENCE** (« ça ne revient plus », « ça ne se coupe plus ») :
l'item de fiche doit porter **la fenêtre de mesure ET le témoin positif**. Sans témoin, une absence
ne prouve rien — elle peut être un décor absent. *Ne rien trouver n'est pas trouver un garde.*

*Cas typique : un comportement inversé, quatre documents mis à jour… et un item de fiche de test
annonçant toujours l'ancien comportement, retiré le jour même. Trouvé parce que quelqu'un a demandé
« c'est bien posé dans la doc et dans les fiches ? », jamais par un contrôle.*

## 🧪 `LIVRÉ` n'est pas `OBSERVÉ` — l'intention documentaire

Une description écrite **après le code mais avant le premier geste réel** est une **intention**, pas
un constat. « Tests verts » et « livré » ne valent pas `OBSERVÉ`.

Le bloc de contrat porte donc son **état d'observation** et la trace minimale qui l'établit. Router
la forme exacte vers la compétence qui met à jour la documentation produit ; ne pas inventer ici une variante de format.

⚠️ Même famille que la règle transverse du `CLAUDE.md` racine : *la réponse d'un outil sur son propre
effet n'est pas une source*. Un test qui passe décrit ce que le test mesure, pas ce que l'utilisateur
obtient.

## 🔤 Le slug, et la seule façon d'énumérer

Un lecteur qui fait `glob("*.md")` sur `la documentation des fonctionnalités, ` n'est pas *faux*, il est **étroit** : il
rend un résultat parfaitement valide, juste incomplet — rien ne rougit. Et `path.stem` rend `plan`
pour un sous-document, donc une **feature fantôme** et un lien vers un fichier qui n'existe pas.

**Le geste** : écrire **un seul** lecteur de ta documentation, et le faire consommer par tous —
jamais une variante locale par outil. Un lecteur neuf hérite alors de chaque correction ; une
recopie, elle, dérive en silence.

## ✅ Fini quand

- Le fait est dans **la surface de sa vitesse** — contrat, plan, décision ou journal, jamais deux.
- Aucune mention d'avancement n'est entrée dans le contrat.
- La **fiche QA** et la **description fonctionnelle** décrivent le comportement **actuel**, et le
  contrôle du lecteur-qui-ne-lit-que-la-fiche passe.
- Une promesse d'absence porte sa fenêtre de mesure **et** son témoin positif.
- L'état d'observation est écrit — `LIVRÉ` n'a pas été confondu avec `OBSERVÉ`.

**Les deux contrôles qui valent d'être outillés ici :** un fait n'a **qu'un** propriétaire, et
une correction touche **toutes** les surfaces qui portaient l'ancienne version.
