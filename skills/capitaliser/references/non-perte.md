# Non-perte — trois preuves différentes

## Conservation historique

Préserver une préimage complète et identifiable : fichier, unité de compétence, export de
page ou version distante. Une archive permet le retour arrière ; elle ne démontre pas que
la nouvelle méthode utilise encore chaque capacité.

## Conservation active

Pour un déplacement intact, comparer les blocs complets avant/après et retrouver chaque
bloc retiré chez son propriétaire actif. Un pointeur qui annonce le déplacement ne suffit
pas. Ne pas ignorer une règle courte. Le contrôle fourni exclut archives, caches et magasins
dormants ; il refuse une source inexistante, vide ou illisible.

```text
python <skill>/scripts/verification.py --before <snapshot> --after <cible-active>
python <skill>/scripts/verification.py --before <snapshot> --after <cible-active> --destination <autre-owner>
```

Le contrôle ne fait aucune écriture et n'appelle aucun réseau. Les chemins sont explicites.
Codes : 0 = blocs conservés ; 1 = blocs manquants ; 2 = mesure impossible ou invalide ;
3 = transformation déclarée présente mais revue sémantique encore nécessaire.
Un code 3 n'est jamais un PASS de non-perte.

Pour une reformulation nécessaire, fournir `--transformations <json>` :

```json
{"transformations":[{"source_sha256":"<hash du bloc avant>","destination":"<fichier exact dans une racine après autorisée>","replacement":"<bloc exact de remplacement>","preserve":["<fragment de l'ancien bloc qui ne doit pas disparaître>"],"reason":"<raison du changement>"}]}
```

La cible doit être réellement lue, le remplacement présent comme bloc complet et tous les
fragments protégés conservés. Une transformation porte une seule unité de sens ; une
exception ne doit pas faire disparaître le reste d'un grand paragraphe. Même présente,
la substitution exige une revue humaine/éditoriale du sens : le script ne la certifie pas.

Une déduplication de blocs strictement identiques est comptée comme conservation de
l'information ; les changements de portée ou d'application exigent la revue de contexte.
Les formats binaires, relations, pièces jointes, permissions et comportements ne sont pas
couverts par une comparaison de texte : les vérifier séparément.

## Utilité réelle

Comparer la table des capacités : déclencheurs, décisions, sorties, limites, preuves,
livrables et adaptations. Vérifier que le prochain agent rencontrera les contraintes au
bon moment. Une archive complète ne remplace aucune de ces vérifications.

Rejouer un cas propre, une perte franche, une perte dans une transformation et un déplacement
vers une autre destination. Saboter une copie isolée de la source réelle, jamais le travail
partagé. Tester le verdict du script comme son appelant : un échec ne doit pas être ignoré.

Enfin, lancer les scénarios de `evals/evals.json` dans une session neuve pour chaque hôte.
Une lecture de contrat, une suite Python ou une revue par le même rédacteur ne remplace pas
ces essais de comportement. Le reçu nomme précisément ce qui a été testé et ce qui ne l'a pas été.
