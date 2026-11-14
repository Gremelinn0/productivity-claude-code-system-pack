# Architecture, mesures et arbitrages

## Parcours structurel

Conserver les quatre contributions :
1. Avis critique sur l'existant, risques et alternatives.
2. Dessin des composants, flux, état, outils, reprises et validations.
3. Décision écrite : options, choix, compromis, conditions de réouverture.
4. Invariants que la construction et les essais doivent protéger.

Les experts disponibles et leur ordre sont nommés dans l'adaptation locale. Lorsqu'ils sont
prescrits, les charger tous : quatre descriptions voisines ne prouvent pas un doublon.
Un outil absent est signalé ; ne pas prétendre l'avoir invoqué ni installer une dépendance sans
autorisation. Les livrables peuvent être préparés avec les moyens disponibles, mais leur niveau
de revue et les contributions manquantes restent explicites.

La règle « la plus précise gagne » ne peut pas contourner une permission ou une décision utilisateur.
Résoudre par autorité et périmètre, puis par précision ; une contradiction non résolue est nommée.
Une refonte structurelle passe une contradiction/prémortem : perte de capacité, nouvel échec,
responsabilités dupliquées, coût déplacé, source introuvable ou impossibilité de retour arrière.

## Mesure du résultat

Définir une mesure adaptée au but et ses contraintes de non-régression. Distinguer réduction
du coût, transfert du coût et dégradation de la qualité. Une optimisation qui ajoute un contrôle
peut être meilleure ; une réduction de contexte qui retire la bonne instruction peut être pire.
Les nombres d'anciens incidents, compétences ou lignes ne sont jamais des mesures actuelles.

Vérifier l'instrument : bon objet, bon environnement, vraie population et régime comparable.
Un silence de logs ne démontre pas une absence d'usage. Un script qui échoue à lire une source
n'a pas mesuré zéro défaut. Les valeurs mouvantes gardent leur requête et leur date, pas des copies
qui vieillissent dans toutes les cartes.

## Preuves proportionnées

Confronter demande, implémentation, tests et description utilisateur. Utiliser les contrôles du
propriétaire ; un script improvisé qui contredit un contrôle existant doit d'abord être confronté.
Tester un cas sain et un défaut sur une copie isolée. Examiner la stabilité quand le résultat peut
varier. Ne jamais saboter le checkout partagé ni faire passer un test documentaire pour une preuve
runtime. Un manque d'accès rend le résultat NON MESURÉ, pas silencieusement vert.

## Maintenance des cartes

Chaque artefact a un propriétaire et un mécanisme de mise à jour connus. La carte locale expose
sources, entrées, étapes, responsables, sorties, points humains et état courant. Elle pointe vers
les méthodes, ne les copie pas. Lire le vrai catalogue chargé avant d'affirmer qu'un nom est invocable.
