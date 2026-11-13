# Adapter les supports, pas retirer des capacités

| Contexte | Source et preuve |
| --- | --- |
| Développement / skills | source canonique, références et tests existants ; historique et diff borné |
| Notion / wiki / documents partagés | identifiants exacts, version ou export avant ; modification ciblée et relecture ; préserver propriétés, relations, enfants et pièces jointes |
| CRM / marketing / opérations | playbook ou méthode propriétaire pour les règles ; enregistrement métier pour les données du cas ; ne pas exécuter un changement de production sous couvert de mémoire |
| Fichiers locaux | document canonique et copie avant/après ; signaler un stockage seulement local |
| Conversation sans stockage accessible | produire le delta et la destination candidate ; verdict NON PERSISTÉ |

Un connecteur connecté n'est pas une preuve d'accès en écriture à une cible. Vérifier la
capacité réellement disponible ; respecter la lecture seule et le minimum de données.
Ne pas créer de compte, d'abonnement, d'autorisation ou de dépendance pour forcer le passage.

Un fait sur un environnement porte sa source, sa date, sa portée et son effet opérationnel.
Distinguer la différence propre à la cible du mécanisme commun : le mécanisme reste chez
l'owner transversal. Ne pas copier une fiche voisine avec ses différences comme nouveau modèle.

Pour une capacité à porter sur d'autres cibles, vérifier trois destinations : la fiche de
la cible actuelle, la méthode qui traite la famille et la procédure d'ajout d'une cible neuve.
Un apprentissage rangé seulement dans une fiche ancienne ne protège pas le prochain portage.

Une recherche infructueuse ne prouve pas l'absence d'une donnée. Décrire le périmètre fouillé,
les formats inspectés et les limites d'accès. Pour les inventaires, distinguer un dossier
vide d'un dossier absent, illisible, tronqué ou non parcouru.

Après publication d'une modification Git, le checkout et le catalogue chargés par une
session peuvent rester différents. Les vérifier sur l'hôte avant d'affirmer qu'ils sont à
jour. Ne jamais restaurer un fichier par-dessus un travail concurrent ni importer un test
qui suppose un code absent de l'arbre local. Une synchronisation partielle ne doit pas créer
un arbre incohérent. Sans accès à cet hôte, déclarer la vérification locale non effectuée.
