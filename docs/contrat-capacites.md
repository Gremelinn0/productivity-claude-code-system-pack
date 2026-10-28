# Contrat de capacités — entretien du système

Cette fiche définit la parité fonctionnelle attendue d'une compétence entre sa source et sa version distribuée. Les changements de chemin, d'outils et d'exemples liés à un environnement sont permis ; **la disparition d'une fonction ne l'est pas**.

| Responsable | Capacités à conserver | Dépendances |
| --- | --- | --- |
| /capitaliser | Fait et raison réutilisables, propriétaire, chargement futur, preuve de non-perte, propagation utile, retrouvabilité des livrables | Sources du domaine |
| /clean-rules-cleanup | Créer, modifier, ranger, retirer et contrôler les règles ; registre de motifs ; audit et entretien des hooks sur autorisation | Contrats des règles et hooks |
| /optimise-systeme | Réflexion et amélioration pendant la tâche, revue d'ensemble sur demande, mesures proportionnées, orchestration, vérification avant/après | Les spécialistes ci-dessous |
| /skill-cleaner | Audit d'une compétence dans son parc ou du parc entier ; niveau, doublons, migration, partage, conservation, inventaire et alimentation d'un catalogue | Accès aux différents dossiers, éventuel générateur de marketplace |
| /skill-quality-guard | Fabriquer, refondre, vérifier et resynchroniser une compétence ; contrôle des contrats, des liens, du déclenchement et des copies publiques | skill-creator officiel d'Anthropic pour écrire et évaluer |
| /propage-systeme | Propagation des décisions vers les fichiers, cartes, versions distribuées et pages humaines, avec preuve | Accès aux surfaces concernées |

Le routeur /router-entretien-systeme est une entrée de compatibilité, pas un septième propriétaire de méthode.

## Scénarios de vérification

1. « Garde ce qu'on a appris sur cette tâche » : /capitaliser conserve le fait et le pourquoi au bon endroit.
2. « Crée cette règle et applique-la à ce projet » : /clean-rules-cleanup regarde l'existant et écrit au bon niveau.
3. « Optimise les instructions et routines de cette tâche » : /optimise-systeme limite l'analyse aux dépendances pertinentes.
4. « Range mon parc et retrouve les doublons » : /skill-cleaner rend une carte et des verdicts justifiés.
5. « Crée cette skill » : /skill-quality-guard appelle le skill-creator, teste, intègre et contrôle.
6. « Refonds cette skill sans perdre ses décisions » : le mode refonte confronte et reconstruit, puis teste.
7. « Synchronise sa copie publiée » : le mode resynchronisation préserve les adaptations et toutes les capacités.
8. « Mets aussi à jour le README et les vues humaines » : /propage-systeme traite les surfaces réellement concernées.
9. « Donne un diagnostic sans modifier » : aucun fichier n'est changé.
10. Plugin Anthropic absent : aucune évaluation inventée et état bloqué explicite.

## Les preuves à distinguer

- **Contrôle documentaire** : fichier, description et références présents.
- **Contrôle mécanique** : scripts et tests réellement exécutés, avec témoin capable d'échouer.
- **Contrôle d'usage** : découverte/invocation dans une session neuve, puis comportement pertinent.
- **Contrôle de parité** : mêmes scénarios sur source et adaptation distribuée, mêmes responsabilités effectivement couvertes.

L'inventaire documentaire de cette branche ne vaut pas une évaluation Claude Code. Un contrôle non exécuté est déclaré comme tel.
