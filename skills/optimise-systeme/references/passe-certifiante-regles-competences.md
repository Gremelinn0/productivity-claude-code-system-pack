# Passe certifiante des règles, compétences et sources documentaires

> À lire seulement pour une **revue complète**, une migration multi-dépôts, une recertification ou
> un assainissement structurel avec garantie de non-perte. Pour un défaut isolé, le cycle normal de
> `/optimise-systeme` suffit.

## Résultat attendu

Rendre le système plus simple à utiliser et plus fiable, sans développer un système de développement
plus lourd que les produits qu'il sert. La passe doit prouver cinq choses :

1. chaque information utile a un propriétaire et une seule source active ;
2. chaque compétence active a une responsabilité distincte et reste atteignable là où elle sert ;
3. chaque règle ambiante mérite réellement d'être chargée dans son périmètre ;
4. chaque contrôle mécanique est appelé et son verdict est consommé ;
5. une tâche neuve choisit naturellement la bonne compétence sans qu'on lui souffle son nom.

Le but n'est jamais d'obtenir moins de fichiers pour le plaisir. Le but est de réduire le bruit,
les contradictions et les choix artificiels sans perdre de capacité.

## Frontière : trois travaux, trois preuves

| Travail | Ce que la passe peut prouver | Ce qu'elle ne prouve pas |
|---|---|---|
| **Système de développement** | règles, compétences, sources, owners, gates, exposition | comportement de l'application |
| **Produit** | où vit le contrat et qui le possède | que le contrat fonctionne au runtime |
| **Runtime** | seulement l'existence d'un protocole et de ses owners | un verdict live sans exécution réelle |

Une passe système ne devient jamais une campagne produit ou runtime par glissement. Elle peut rendre
ces campagnes possibles, les router et déclarer ce qui reste non mesuré.

## Modèle d'exposition — cinq états, jamais un raccourci

```text
présent sur disque
→ exposé à l'hôte depuis ce dossier
→ découvert dans une tâche neuve
→ invoqué naturellement sans donner son nom
→ utile : produit le bon owner, la bonne méthode et les bonnes limites
```

Un état ne prouve pas le suivant. Un lien résolu ne prouve pas la découverte ; une découverte ne
prouve pas l'invocation ; une invocation ne prouve pas une meilleure décision. Mesurer Claude et
Codex séparément lorsque les deux hôtes sont visés.

## Où ranger chaque bloc

Attribuer exactement une catégorie avant de déplacer quoi que ce soit :

| Catégorie | Destination |
|---|---|
| **Règle ambiante** | invariant court, stable, nécessaire dans presque toute tâche du périmètre |
| **Compétence** | méthode ou décision contextuelle avec déclencheur identifiable |
| **Référence de compétence** | piège, exemple, jurisprudence ou procédure consultée seulement au besoin |
| **Source produit** | fait sur le produit ou contrat souverain d'une fonctionnalité |
| **Gate / hook / test** | défaut réel, silencieux et mécaniquement décidable |
| **Archive** | formulation remplacée, préimage ou fait seulement historique |

La documentation de référence produit n'est pas un fourre-tout pour les incidents de compétences.
Une référence vit sous l'owner qui saura quand la relire.

## Owners à orchestrer, jamais à recopier

| Question | Owner |
|---|---|
| topologie d'un dépôt | le la carte « où vit quoi » de ton projet réel du dépôt (la carte d'architecture de ton projet dans le produit) |
| architecture couvrant plusieurs dépôts | la carte d'architecture transverse |
| contradiction ou responsabilité documentaire multi-dépôts | `/propage-systeme` |
| altitude globale | la compétence qui décide du niveau d'une règle |
| règles `CLAUDE.md` | `/clean-rules-cleanup` |
| parc de compétences, verdicts et non-perte | `/clean-rules-cleanup` (mode audit du parc) |
| création ou réécriture substantielle | `skill-creator → /skill-factory → /skill-quality-guard` |
| décision qui vient de rendre une source fausse | `/dev-capitaliser` |
| partage public ou lead magnet | la compétence qui décide si ça peut sortir |
| propagation finale des surfaces humaines | `/propage-systeme` |

La passe est le chef d'orchestre. Elle n'absorbe aucune de ces méthodes.

## Déroulé certifiant

### 0. Figer le monde observé

- identifier tous les dépôts, sous-dossiers propriétaires et hôtes concernés ;
- relever `HEAD`, remote, branche, worktrees chauds, locks et chemins déjà modifiés ;
- travailler sur des worktrees propres issus des derniers remotes ;
- relever SHA-256, EOL et encodage des fichiers touchés ;
- créer une préimage exacte hors de la surface active avant toute réécriture substantielle ;
- interrompre uniquement la sous-vague dont une empreinte change.

Aucun stash, reset, nettoyage de WIP ou incorporation silencieuse du travail d'un tiers.

### 1. Mesurer la topologie réelle

Pour chaque compétence ou règle candidate, relever : dépôt, portée, poids, description réellement
lue, spécificité, tests/outils dépendants, routes entrantes et sortantes, jonctions, plugin éventuel,
owner, portée réelle et verdict antérieur.

Lire d'abord les inventaires et rapports frais, puis revalider leur delta sur le SHA figé. Un ancien
rapport est une photo, jamais une todo-list.

### 2. Séparer actif, contradictoire et historique

- une route active donne une instruction invocable maintenant ;
- une mention historique est au passé et ne propose aucune commande ;
- une contradiction se résout par la hiérarchie des sources ;
- deux sources de même autorité réellement incompatibles deviennent une décision à attribuer ;
- un verdict antérieur ne se rouvre qu'avec une preuve fraîche consignée.

Ne jamais réécrire les archives pour fabriquer une cohérence rétrospective.

### 3. Concevoir destination d'abord

Avant tout retrait, produire la table :

```text
bloc source → catégorie → owner → destination → consommateurs → preuve attendue
```

Ajouter et tester la destination avant de retirer l'ancienne source. Pour chaque bloc retiré :

1. prouver s'il existe déjà chez l'owner ;
2. sinon le déplacer verbatim s'il reste utile ;
3. l'archiver s'il n'est plus actif mais explique une décision ;
4. migrer tous les consommateurs actifs dans la même sous-vague ;
5. seulement ensuite retirer l'ancienne forme.

### 4. Exécuter en petites vagues réversibles

Une sous-vague contient une seule famille d'owners et un seul type de mutation risquée. Pour une
migration importante, préférer deux commits :

1. destination, pointeurs et contrôles ;
2. retrait de l'ancienne forme après preuve.

Chaque commit ne contient que les chemins concernés, est poussé, puis vérifié sur le distant. Le
rollback est un `git revert` dans l'ordre inverse ; hors Git, la préimage exacte et son empreinte
sont obligatoires.

### 5. Prouver les instruments avant de croire leurs verdicts

Tout zéro doit avoir un témoin positif connu dans le même instrument. Toute sortie tronquée est
incomplète. Pour un gate nouveau ou durci :

- sabotage réellement posé et relu ;
- cas négatif qui rougit ;
- témoin positif qui reste vert ;
- fail-silencieux lorsque l'environnement ne permet pas la mesure ;
- message qui donne le remède et nomme l'owner ;
- appelant réel **et consommateur réel du verdict**.

Un test qui existe mais que personne ne lance est de la prose coûteuse. Un test lancé dont personne
ne lit le rouge produit le même effet : rien.

### 6. Tester la sélection en tâches neuves

Le catalogue d'une tâche ouverte avant la mutation est périmé. Ouvrir une tâche neuve dans chaque
scope témoin et poser une question naturelle sans citer de compétence.

Exiger des canaris concurrents :

- méthode multi-dépôts → compétence globale transverse ;
- sujet propre au projet → owner local du projet ;
- sujet métier → compétence métier, pas l'orchestrateur système ;
- tâche étrangère → aucune connaissance projet inutilement chargée.

Une revue indépendante peut chercher les angles morts ; elle ne remplace ni ces canaris ni les
preuves mécaniques.

### 7. Re-mesurer et clôturer sans faux PASS global

Rejouer exactement les instruments du départ et rendre : avant/après, conservé, allégé, déplacé,
fusionné, archivé, supprimé, non mesuré, commits, chemins de rollback et propagations en attente.

Séparer les verdicts par dépôt, hôte et couche. Une publication externe en attente n'annule pas un
PASS local ; un PASS local ne devient pas un PASS global.

Exécuter `/propage-systeme` une seule fois à la fin, sur des cibles explicites et propres. Les vues
générées se régénèrent depuis leur générateur ; elles ne s'éditent jamais directement.

## Reçu obligatoire par sous-vague

```text
Périmètre :
Base et remote :
Chemins verrouillés :
Avant : inventaire + empreintes
Mutation :
Non-perte : blocs + destinations + témoins
Contrôles : rouge/vert + appelant + consommateur
Après : inventaire + empreintes
Commit / push :
Rollback :
Reste explicitement non mesuré :
```

## Critères d'arrêt

La passe n'est terminée que si :

- chaque objet du périmètre porte un verdict terminal chez son owner ;
- zéro route active ne pointe vers un nom retiré ;
- les blocs déplacés sont retrouvables à destination ;
- les compétences touchées passent les axes de `/skill-quality-guard` ;
- les canaris frais discriminent global, projet, métier et tâche étrangère ;
- les mêmes mesures passent deux fois sans correction structurelle ;
- le rapport explique le résultat en langage simple.

Sinon le verdict est `NON MESURÉ`, `PREUVE INSUFFISANTE`, `DETTE`, ou un PASS borné — jamais un vert
global fabriqué par agrégation.

## Les erreurs déjà payées qui justifient ce protocole

- une compétence archivée avait été archivée alors que huit routes actives la proposaient encore ; une mention
  historique et une table de routage ne sont pas le même objet.
- un `rg --glob` mal adapté au shell rendait zéro même sur le témoin positif connu ; sans témoin,
  le ménage aurait déclaré propre ce qu'il n'avait pas regardé.
- un gate vérifiait qu'un owner était nommé, pas qu'il existait ou pouvait produire une preuve ;
  le sabotage rouge/vert a révélé la différence.
- une réduction de préflight a tenu parce que le document source est resté intact et que les routes
  compactes ont été prouvées ; le gain n'était pas la suppression, mais l'accès sélectif.
- une session fraîche restait `NON MESURÉE` malgré trente tests verts : le système connaissait ses
  propres réponses et ne pouvait pas prouver sa découvrabilité naturelle.

**Le fil rouge, si tu ne devais retenir qu'une chose** : un zéro d'environnement est
indistinguable d'un zéro légitime. Seul un **témoin positif** les sépare — une valeur que tu SAIS
présente, et qui doit ressortir du même instrument. Et le témoin doit vivre dans un vocabulaire
**disjoint** de son propre contexte, sinon il valide n'importe quel zéro.
