---
name: router-entretien-systeme
description: >-
  Compatibilité pour l'ancien appel /router-entretien-systeme. Transmet au propriétaire
  /optimise-systeme, sans méthode propre ni second workflow. Pour les nouvelles demandes,
  utiliser directement /optimise-systeme.
metadata:
  role: compatibility-alias
  canonical: optimise-systeme
---

# /router-entretien-systeme — alias de /optimise-systeme

Résoudre /optimise-systeme dans le catalogue réel de l'hôte, puis charger sa compétence.
Transmettre la demande, les sources, les limites et les opérations déjà réalisées.
Exécuter une seule intervention chez ce propriétaire, sans lui rappeler cet alias.

Si sa version chargée renvoie encore vers /router-entretien-systeme, signaler l'incompatibilité
et arrêter ce renvoi : ne pas créer de récursion. Un propriétaire indisponible ne donne
pas le droit de reconstruire sa méthode de mémoire.

Cet alias reste invocable pour préserver les anciens appels. Les nouvelles descriptions,
cartes et workflows utilisent /optimise-systeme. Ne retirer l'alias qu'après migration
et vérification des appelants ; sa présence n'en fait pas une compétence supplémentaire
à présenter à l'utilisateur. Les anciennes annexes conservées ne sont pas une méthode active.
