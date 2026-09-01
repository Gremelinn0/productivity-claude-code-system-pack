#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Registre des motifs — synchronisation et audit.

Le registre repond a une seule question : POURQUOI cette regle a-t-elle ete
inscrite, et cette raison tient-elle encore aujourd'hui ?

Il vit dans references/registre-des-motifs.md, hors du budget de session : rien
n'y est charge automatiquement. La regle chargee porte le comportement et son
controle ; le registre porte le cas paye, le cout et la condition de peremption.

Trois commandes :
  sync   [corpus...]  ajoute les regles datees absentes du registre (squelette),
                      ne reecrit JAMAIS une cellule deja remplie
  audit  [corpus...]  rend ce qu'un menage doit regarder : motifs manquants,
                      regles disparues du corpus, revues perimees, peremptions
                      declarees echues
  show   <motif>      affiche les lignes dont un champ contient <motif>

Sans argument, le corpus par defaut est cherche aux emplacements usuels d'un
fichier de regles (voir DEFAULT_CORPUS). Passer les chemins en arguments pour
viser un autre corpus.

Sortie : texte, une ligne par constat. Code de retour 0 toujours — c'est un
instrument de lecture, pas un gate : un gate qui crie au loup finit ignore.

Aucune dependance : bibliotheque standard uniquement.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from datetime import date, datetime
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REGISTRE = SKILL_DIR / "references" / "registre-des-motifs.md"

# Emplacements usuels d'un fichier de regles. Seuls ceux qui existent sont lus.
DEFAULT_CORPUS = [
    Path.cwd() / "CLAUDE.md",
    Path.cwd() / ".claude" / "CLAUDE.md",
    Path.home() / ".claude" / "CLAUDE.md",
]

# Une gravure = un marqueur date. C'est le seul repere fiable : les titres
# changent, les numeros de section bougent, la date de gravure ne bouge pas.
# Adapter cette expression au marqueur employe par votre corpus.
GRAVURE = re.compile(
    r"(?:grav[ée]{1,2}e?|inscrite?|ajout[ée]e?)\s+(?:le\s+)?(\d{4}-\d{2}-\d{2})",
    re.IGNORECASE,
)

TODO = "À DOCUMENTER"
JAMAIS = "jamais"
PEREMPTION_VIDE = "—"

# Tout ce qui suit cette borne est la table des motifs ARCHIVES : elle se lit,
# elle ne se synchronise pas.
BORNE_ARCHIVE = "## Motifs archivés"

# Une revue plus vieille que ca n'est plus une revue, c'est un souvenir.
REVUE_PERIMEE_JOURS = 180

MOTS_VIDES = {
    "le", "la", "les", "un", "une", "des", "de", "du", "et", "ou", "au",
    "aux", "en", "ne", "pas", "qui", "que", "quoi", "dans", "pour", "sur",
    "est", "sont", "ce", "cet", "cette", "se", "son", "sa", "ses", "il",
    "elle", "on", "je", "tu", "nous", "vous", "par", "avec", "plus", "tout",
    "the", "and", "for", "with", "this", "that", "from", "not",
}


def _slug(texte: str, mots: int = 4) -> str:
    """Slug ASCII court, stable, tire du titre de la regle."""
    sans_accent = unicodedata.normalize("NFKD", texte)
    sans_accent = "".join(c for c in sans_accent if not unicodedata.combining(c))
    jetons = re.findall(r"[a-z0-9]+", sans_accent.lower())
    utiles = [j for j in jetons if j not in MOTS_VIDES and len(j) > 2]
    retenu = (utiles or jetons)[:mots]
    return "-".join(retenu) or "sans-titre"


def _titre_de_ligne(ligne: str) -> str:
    """Extrait un titre lisible d'une ligne de corpus, sans son balisage."""
    t = ligne.strip()
    t = re.sub(r"^[#>\-\*\d\.\s]+", "", t)            # puces, titres, citations
    t = re.sub(r"[*_`]", "", t)                        # emphase markdown
    t = re.sub(r"\([^)]*grav[ée]{1,2}e?[^)]*\)", "", t, flags=re.IGNORECASE)
    t = GRAVURE.sub("", t)
    t = t.replace("|", "/")                            # la table est en pipes
    t = re.sub(r"\s+", " ", t).strip(" -—,;:.")
    return t[:110]


def _section_courante(lignes: list, index: int) -> str:
    """Remonte au dernier titre markdown au-dessus de la ligne.

    Le numero se lit sur le titre BRUT : `_titre_de_ligne` mange les chiffres
    de tete avec la puce markdown, et rendrait « 4. Reponses » sous la forme
    « Reponses » — l'adresse perdrait le seul repere tenu pour stable.
    """
    for i in range(index, -1, -1):
        m = re.match(r"^#{2,4}\s+(.*)$", lignes[i])
        if not m:
            continue
        brut = re.sub(r"^[\s*_`>]+", "", m.group(1))
        num = re.match(r"§?\s?(\d+[a-zA-Z]*(?:bis|ter|quater|quinquies)?)\b", brut)
        if num:
            return "§" + num.group(1)
        return _titre_de_ligne(brut)[:40] or "?"
    return "?"


def scanner_corpus(chemins: list) -> list:
    """Rend une entree par gravure datee trouvee dans le corpus."""
    trouvees = []
    for chemin in chemins:
        if not chemin.exists():
            continue
        lignes = chemin.read_text(encoding="utf-8", errors="replace").splitlines()
        prefixe = re.sub(r"[^A-Z0-9]", "", chemin.stem.upper())[:4] or "REGL"
        for i, ligne in enumerate(lignes):
            m = GRAVURE.search(ligne)
            if not m:
                continue
            titre = _titre_de_ligne(ligne)
            if not titre:
                continue
            trouvees.append(
                {
                    "id": "%s-%s-%s" % (prefixe, m.group(1), _slug(titre)),
                    "fichier": chemin.name,
                    "section": _section_courante(lignes, i),
                    "ligne": i + 1,
                    "gravee": m.group(1),
                    "titre": titre,
                }
            )
    # Deux gravures peuvent porter la meme date et le meme slug (amendement
    # ecrit deux fois). On desambigue par un suffixe, jamais en en jetant une.
    vus = {}
    for e in trouvees:
        n = vus.get(e["id"], 0)
        vus[e["id"]] = n + 1
        if n:
            e["id"] = "%s-%d" % (e["id"], n + 1)
    return trouvees


SECTION = re.compile(r"§\s?(\d+[a-zA-Z]*(?:bis|ter|quater|quinquies)?)")


def sections_du_corpus(chemins: list) -> set:
    """Toutes les adresses de section citees ou definies par le corpus vivant."""
    vivantes = set()
    for chemin in chemins:
        if not chemin.exists():
            continue
        texte = chemin.read_text(encoding="utf-8", errors="replace")
        vivantes.update(m.lower() for m in SECTION.findall(texte))
        for m in re.finditer(r"^#{2,4}\s+(\d+[a-zA-Z]*(?:bis|ter)?)\b", texte, re.M):
            vivantes.add(m.group(1).lower())
    return vivantes


def adresse_vivante(adresse: str, sections: set) -> bool:
    """Une adresse sans numero de section ne se juge pas — on la garde."""
    numeros = SECTION.findall(adresse)
    if not numeros:
        return True
    return any(n.lower() in sections for n in numeros)


def lire_registre():
    """Rend (lignes brutes, entrees parsees, index de la 1re ligne de table)."""
    if not REGISTRE.exists():
        return [], [], -1
    lignes = REGISTRE.read_text(encoding="utf-8").splitlines()
    entrees = []
    debut = -1
    for i, ligne in enumerate(lignes):
        if ligne.startswith(BORNE_ARCHIVE):
            break
        if not ligne.startswith("| "):
            continue
        cells = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if len(cells) < 7:
            continue
        if debut < 0:
            debut = i
        if cells[0].lower() == "id" or set(cells[0]) <= set("-: "):
            continue
        entrees.append(
            {
                "index": i,
                "id": cells[0],
                "adresse": cells[1],
                "gravee": cells[2],
                "declencheur": cells[3],
                "controle": cells[4],
                "peremption": cells[5],
                "revue": cells[6],
            }
        )
    return lignes, entrees, debut


def lire_archive():
    """IDs des motifs archives — connus de `sync` pour ne pas les regenerer.

    Une regle retiree garde sa ligne : c'est elle qui empechera de la regraver.
    Si le corpus la porte de nouveau, ce n'est pas un trou de couverture, c'est
    une RESURRECTION — et `audit` la nomme comme telle.
    """
    if not REGISTRE.exists():
        return set()
    dedans = False
    ids = set()
    for ligne in REGISTRE.read_text(encoding="utf-8").splitlines():
        if ligne.startswith(BORNE_ARCHIVE):
            dedans = True
            continue
        if not dedans or not ligne.startswith("| "):
            continue
        cells = [c.strip() for c in ligne.strip().strip("|").split("|")]
        if len(cells) < 7 or cells[0].lower() == "id" or set(cells[0]) <= set("-: "):
            continue
        ids.add(cells[0])
    return ids


def _ecrire(chemin: Path, texte: str) -> None:
    """Encode AVANT d'ouvrir : un texte mal encode ne doit jamais tronquer."""
    chemin.write_bytes(texte.encode("utf-8"))


def cmd_sync(corpus: list) -> int:
    trouvees = scanner_corpus(corpus)
    lignes, entrees, debut = lire_registre()
    if debut < 0:
        print("[ABORT] Table absente de references/registre-des-motifs.md.")
        print("        Lever la precondition : recreer le fichier avec son")
        print("        en-tete de table (| ID | Adresse | ... |), puis relancer.")
        return 0
    if not trouvees:
        print("[ABORT] Aucune gravure datee trouvee dans le corpus.")
        print("        Lever la precondition : passer les chemins en arguments,")
        print("        ou adapter GRAVURE au marqueur employe par vos regles.")
        return 0
    connus = set(e["id"] for e in entrees) | lire_archive()
    neuves = [t for t in trouvees if t["id"] not in connus]
    if not neuves:
        print("[OK] Registre a jour — %d motifs, %d gravures scannees."
              % (len(entrees), len(trouvees)))
        return 0
    fin = max(e["index"] for e in entrees) if entrees else debut + 1
    rangs = [
        "| {id} | `{fichier}` {section} — {titre} | {gravee} | {todo} | {todo} | {vide} | {jamais} |".format(
            todo=TODO, vide=PEREMPTION_VIDE, jamais=JAMAIS, **t
        )
        for t in neuves
    ]
    lignes[fin + 1: fin + 1] = rangs
    _ecrire(REGISTRE, "\n".join(lignes) + "\n")
    print("[SYNC] %d motif(s) ajoute(s) en squelette :" % len(neuves))
    for t in neuves:
        print("  + %s  (%s l.%d)" % (t["id"], t["fichier"], t["ligne"]))
    print("       A remplir : declencheur, controle, peremption.")
    print("       Aucune cellule existante touchee.")
    return 0


def _jours_depuis(iso: str):
    try:
        return (date.today() - datetime.strptime(iso, "%Y-%m-%d").date()).days
    except ValueError:
        return None


def cmd_audit(corpus: list) -> int:
    trouvees = scanner_corpus(corpus)
    _, entrees, debut = lire_registre()
    if debut < 0:
        print("[ABORT] Registre illisible. Lever la precondition : recreer la table.")
        return 0

    ids_archive = lire_archive()
    ids_registre = set(e["id"] for e in entrees) | ids_archive

    # L'orphelinat se juge sur l'ADRESSE, pas sur l'ID. Un nettoyage qui coupe
    # le recit d'une regle fait disparaitre sa date de gravure sans toucher a
    # la regle : la chercher par ID declarerait tout le registre orphelin, pile
    # le jour ou il devient utile. Les numeros de section, eux, sont tenus pour
    # des adresses stables.
    sections_vivantes = sections_du_corpus(corpus)

    sans_motif = [e for e in entrees if TODO in e["declencheur"]]
    sans_controle = [e for e in entrees if TODO in e["controle"]]
    orphelines = [e for e in entrees
                  if not adresse_vivante(e["adresse"], sections_vivantes)]
    absentes = [t for t in trouvees if t["id"] not in ids_registre]
    ressuscitees = [t for t in trouvees if t["id"] in ids_archive]

    jamais_revues, revues_perimees, peremptions_echues = [], [], []
    for e in entrees:
        revue = e["revue"].split("—")[0].strip()
        if revue.lower().startswith(JAMAIS):
            jamais_revues.append(e)
        else:
            j = _jours_depuis(revue)
            if j is not None and j > REVUE_PERIMEE_JOURS:
                revues_perimees.append((e, j))
        m = re.search(r"\b(\d{4}-\d{2}-\d{2})\b", e["peremption"])
        if m:
            j = _jours_depuis(m.group(1))
            if j is not None and j >= 0:
                peremptions_echues.append((e, m.group(1)))

    print("=== Registre des motifs — audit %s ===" % date.today().isoformat())
    print("gravures dans le corpus : %d   motifs au registre : %d"
          % (len(trouvees), len(entrees)))
    if entrees:
        print("couverture reelle (motif ecrit) : %.0f %%"
              % (100.0 * (len(entrees) - len(sans_motif)) / len(entrees)))
    print("")

    def bloc(titre, items, rendu):
        print("-- %s : %d" % (titre, len(items)))
        for it in items[:40]:
            print("   %s" % rendu(it))
        if len(items) > 40:
            print("   ... et %d de plus" % (len(items) - 40))
        print("")

    bloc("MOTIF MANQUANT (la regle vit, sa raison n'est ecrite nulle part)",
         sans_motif, lambda e: "%s — %s" % (e["id"], e["adresse"][:80]))
    bloc("CONTROLE MANQUANT (rien de decidable ne la fait respecter)",
         sans_controle, lambda e: e["id"])
    bloc("REGLE DISPARUE DU CORPUS (motif orphelin — archiver la ligne)",
         orphelines, lambda e: "%s — %s" % (e["id"], e["adresse"][:80]))
    bloc("GRAVURE HORS REGISTRE (lancer `sync`)",
         absentes, lambda t: "%s — %s l.%d" % (t["id"], t["fichier"], t["ligne"]))
    bloc("REGRAVEE APRES RETRAIT (le motif est archive, la regle est revenue)",
         ressuscitees, lambda t: "%s — %s l.%d" % (t["id"], t["fichier"], t["ligne"]))
    bloc("PEREMPTION ECHUE (la condition ecrite est atteinte — a rouvrir)",
         peremptions_echues, lambda p: "%s — echeance %s" % (p[0]["id"], p[1]))
    bloc("REVUE PERIMEE (> %d j)" % REVUE_PERIMEE_JOURS,
         revues_perimees, lambda p: "%s — %d j" % (p[0]["id"], p[1]))
    bloc("JAMAIS REVUE", jamais_revues, lambda e: e["id"])

    print("Rappel : un motif qui se relit se croit. Une peremption se MESURE.")
    return 0


def cmd_show(motif: str) -> int:
    _, entrees, debut = lire_registre()
    if debut < 0:
        print("[ABORT] Registre illisible.")
        return 0
    besoin = motif.lower()
    trouve = 0
    for e in entrees:
        blob = " ".join(str(v) for v in e.values()).lower()
        if besoin in blob:
            trouve += 1
            print("### %s" % e["id"])
            print("  adresse     : %s" % e["adresse"])
            print("  gravee      : %s" % e["gravee"])
            print("  declencheur : %s" % e["declencheur"])
            print("  controle    : %s" % e["controle"])
            print("  peremption  : %s" % e["peremption"])
            print("  revue       : %s" % e["revue"])
            print("")
    if not trouve:
        print("Aucun motif ne contient « %s »." % motif)
    return 0


def main(argv: list) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 0
    cmd, args = argv[1], argv[2:]
    if cmd == "show":
        return cmd_show(" ".join(args))
    corpus = [Path(a) for a in args] or DEFAULT_CORPUS
    if cmd == "sync":
        return cmd_sync(corpus)
    if cmd == "audit":
        return cmd_audit(corpus)
    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
