---
name: router-entretien-systeme
description: >-
  Porte d'entrée du Claude Code System Pack : quand un agent répète une erreur corrigée,
  que les règles gonflent, que les compétences se contredisent, qu'une modification
  n'a pas été propagée ou que l'on veut mesurer avant d'optimiser, choisir parmi
  capitaliser, clean-rules-cleanup, optimise-systeme, skill-quality-guard et
  propage-systeme, les invoquer dans le bon ordre et restituer leur verdict.
  Triggers : « entretenir mon système », « quelle compétence pour mes règles »,
  « mon agent refait la même erreur », « mes skills se contredisent »,
  « la doc est périmée », « mesure avant de corriger », « route le System Pack ».
metadata:
  owns: "la sélection des cinq propriétaires et le passage de leurs sorties, jamais leur méthode"
  consumes: "description du symptôme, surfaces de règles, résultats et preuves des compétences"
---

# router-entretien-systeme — une porte, cinq propriétaires

**Rôle unique :** traduire un symptôme en propriétaire(s), puis transmettre le contexte
nécessaire à chacun. Ce routeur ne nettoie aucune règle, ne mesure aucun système,
ne modifie aucune compétence et ne capitalise aucun apprentissage lui-même.
**Ne fait pas :** recopier la procédure d'une autre compétence ; créer un deuxième
registre de vérité ; imposer les cinq étapes à tous les cas.
**Rend :** choix motivé, enchaînement réel, preuves/contrôles et statut `fait / bloqué / non exécuté`.

## Carte : symptôme → propriétaire

| Le symptôme réel | Propriétaire de la première action | Suite si nécessaire |
|---|---|---|
| « Mon agent refait une erreur corrigée » ; décision ou leçon non réutilisée | `/capitaliser` | `/clean-rules-cleanup` si la leçon nécessite une règle ; `/propage-systeme` si la nouvelle information invalide d'autres surfaces |
| « Mes règles gonflent », doublons, instruction sans raison ni échéance | `/clean-rules-cleanup` | `/skill-quality-guard` si une compétence a changé, puis `/propage-systeme` pour les renvois et pages humaines |
| « Mes compétences se contredisent » ou carte documentaire mensongère | `/optimise-systeme` pour constater et mesurer le conflit | `/clean-rules-cleanup` sur la règle propriétaire, `/skill-quality-guard` sur les compétences touchées, `/propage-systeme` |
| « Je veux mesurer avant d'optimiser » ; trop de compétences ; système confus | `/optimise-systeme` | En fonction du diagnostic seulement : `/clean-rules-cleanup`, `/skill-quality-guard`, `/propage-systeme` ; `/optimise-systeme` re-mesure |
| « Je veux écrire ou déplacer une règle » | `/clean-rules-cleanup` | `/skill-quality-guard` si SKILL.md modifié, puis `/propage-systeme` |
| « Cette compétence est-elle prête ? » ; déclenchement cassé | `/skill-quality-guard` | Revenir au propriétaire du défaut, puis **refaire** le contrôle sur les sept axes |
| « Une règle a changé, le Hub/README/le projet dit encore l'ancien fait » | `/propage-systeme` | `/skill-quality-guard` si la correction modifie une compétence |
| « Je viens de finir : que faut-il retenir ? » | `/capitaliser` | Rien si le verdict est `RIEN` ; propagation si une nouvelle règle change d'autres surfaces |

Ce tableau choisit **la première compétence**, pas une autorisation de modifier le dépôt.
La compétence appelée conserve **la seule autorité** sur son domaine.

## Orchestration d'une demande

1. **Définir le besoin** en une phrase : symptôme, résultat recherché et surfaces concernées
   (global, dépôt, compétence, page humaine, autre outil). Séparer un fait observé d'un soupçon.
2. **Choisir une première porte** avec la carte. Si un simple apprentissage a été perdu,
   commencer par `capitaliser`. Si des règles se contredisent, ne pas proclamer une
   optimisation sans inventaire : commencer par `optimise-systeme` et son diagnostic.
3. **Lire le `SKILL.md` de la compétence retenue** dans le même dépôt et lui transmettre :
   symptôme et exemple, propriétaire soupçonné, références sources, accès autorisés, résultat
   attendu et modifications interdites. Ne pas reproduire ses étapes ici.
4. **Recevoir sa sortie et décider de la suite**. Une propagation est nécessaire quand une
   information rend d'autres surfaces fausses ; le contrôle à sept axes est nécessaire
   lorsqu'un `SKILL.md` a été modifié. Ne jamais relancer les mêmes opérations en boucle.
5. **Clore par des faits** : fichiers et surfaces effectivement vus/modifiés, mesures avant/après
   si disponibles, contrôles lancés/non lancés, verdicts, propriétaires des blocages.
   Une proposition ne compte pas pour une exécution.

### Chaînes usuelles (seulement si le diagnostic les justifie)

- **Erreur réapparue** : `capitaliser` → *si nouvelle règle* `clean-rules-cleanup`
  → *si compétences touchées* `skill-quality-guard` → *si surfaces incohérentes* `propage-systeme`.
- **Audit complet** : `optimise-systeme` (état initial, mesures) →
  propriétaire(s) selon diagnostic → `skill-quality-guard` si compétences modifiées →
  `propage-systeme` si renvois/humains touchés → `optimise-systeme` (re-mesure).
- **Règle à mettre à jour** : `clean-rules-cleanup` → contrôle de la compétence touchée →
  `propage-systeme` ; `capitaliser` **uniquement** si une leçon durable supplémentaire apparaît.
- **Simple contrôle de qualité** : `skill-quality-guard` seul. Un échec se rapporte au
  propriétaire ; il ne déclenche pas cinq nettoyages automatiques.
- **Documentation humaine obsolète** : `propage-systeme` seul lorsque la source est déjà exacte.

## Garde-fous et frontières

- **Global ou local** : une règle universelle vit au niveau global seulement si elle gouverne
  réellement tous les travaux ; les autres vont dans la compétence ou le dépôt propriétaire.
  Le routeur identifie ce niveau, `clean-rules-cleanup` décide et applique.
- **Mesures** : aucune économie de tokens, amélioration de qualité ou absence de doublons
  ne se déduit du seul changement de fichier. Seul `optimise-systeme` peut comparer son
  état mesuré au même protocole. Si la mesure est absente : `non mesuré`.
- **Réversibilité** : lire l'archive et préserver l'original avant toute suppression ou migration.
  Respecter les autorisations et le seuil d'approbation fixés par le propriétaire
  (notamment le diagnostic `optimise-systeme` avant un lot dépassant trois fichiers).
- **Édition de SKILL.md** : passe finale `skill-quality-guard` (sept axes), aucune prétendue
  validation tant que les contrôles exigés n'ont pas été réellement lancés.
- **Propagation** : vérifier les surfaces lisibles par l'agent **et par les humains**.
  Un pointeur vers une page privée ou un guide périmé n'est pas une preuve d'installation.
- **Pack indépendant** : cinq compétences propriétaires dans `../` ;
  `/dev-capitaliser` a été retiré au profit de `/capitaliser`. Ne pas invoquer l'ancien nom.
- **Ne pas confondre** ce pack avec `claude-code-guardrails` : ce dernier contient
  des garde-fous mécaniques (hooks). Le routeur ne promet pas de mécanisme bloquant qu'il
  n'exécute pas.

## Contrat de sortie court

```text
Symptôme / fait observé :
Première compétence et raison :
Autres compétences effectivement appelées (ordre) :
Surfaces/propriétaire :
Changements réellement faits (ou aucun) :
Vérifications lancées / non lancées :
Mesure avant / après (ou non mesuré) :
Verdict : fait | bloqué | non exécuté
Suite requise / accord humain :
```

**Fini quand** chaque composante exécutée a sa preuve et que toute compétence non
exécutée reste signalée comme telle. Une simple carte de routage ne vaut pas
« système optimisé ».
