#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""derive_bloc.py — une règle vit UNE fois ; les fichiers qui doivent la porter en tête reçoivent
un bloc DÉRIVÉ, et `--check` rougit dès que l'un d'eux diverge.

Le problème qu'il règle : la même doctrine recopiée à la main dans trois fichiers (la règle, et
les deux compétences qui l'appliquent). Le jour où l'un des trois bouge, rien ne rougit — et
l'agent charge selon la session l'une ou l'autre version.

Le mécanisme : la section source est lue dans le fichier de règles ; chaque cible porte, entre
deux marqueurs HTML, une copie GÉNÉRÉE de cette section. Personne n'édite le bloc : on édite la
source et on rejoue le script. Le contrôle compare les mots, pas la mise en page.

Usage :
  python scripts/derive_bloc.py --source CLAUDE.md --section "^## 33" --cible skills/a/SKILL.md --cible skills/b/SKILL.md
  python scripts/derive_bloc.py ... --check        # 0 si tout est aligné, 1 sinon (liste des écarts)
  python scripts/derive_bloc.py --self-test        # prouve le contrôle dans les deux sens

Bibliothèque standard uniquement. Le bloc est posé après le premier titre `# ` de la cible quand
les marqueurs n'existent pas encore ; ensuite les marqueurs font foi.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
import textwrap
from pathlib import Path

LARGEUR = 100


def lire_section(source: Path, section: str) -> tuple[str, str]:
    """(titre, corps) de la section dont la ligne de titre matche `section`."""
    motif = re.compile(section)
    lignes = source.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")
    debut = next((i for i, l in enumerate(lignes) if motif.search(l)), None)
    if debut is None:
        raise SystemExit(f"[derive] {source} : aucune ligne ne matche {section!r}")
    titre = re.sub(r"^#+\s*", "", lignes[debut]).strip()
    niveau = len(lignes[debut]) - len(lignes[debut].lstrip("#"))
    corps: list[str] = []
    for l in lignes[debut + 1:]:
        if re.match(r"^#{1,%d}\s" % max(niveau, 1), l):
            break
        if l.strip():
            corps.append(l.strip())
    if not corps:
        raise SystemExit(f"[derive] {source} : section {titre!r} vide")
    return titre, "\n".join(corps)


def normaliser(t: str) -> str:
    return re.sub(r"\s+", " ", t).strip()


def marqueurs(ident: str) -> tuple[str, str]:
    return f"<!-- bloc:{ident}", f"<!-- /bloc:{ident} -->"


def bloc_derive(ident: str, source_nom: str, titre: str, corps: str) -> str:
    debut, fin = marqueurs(ident)
    lignes = [
        f"{debut} — DÉRIVÉ de `{source_nom}` ({titre}) par scripts/derive_bloc.py. Ne pas éditer ici : "
        "éditer la source et rejouer le script ; `--check` rougit dès que ça diverge. -->",
        f"> **{titre}** *(source unique : `{source_nom}`)*",
    ]
    for paragraphe in corps.split("\n"):
        for l in textwrap.wrap(paragraphe, width=LARGEUR, break_long_words=False, break_on_hyphens=False):
            lignes.append("> " + l)
    lignes.append(fin)
    return "\n".join(lignes)


def _region(lignes: list[str], debut: str, fin: str) -> tuple[int, int] | None:
    i = next((k for k, l in enumerate(lignes) if l.startswith(debut)), None)
    if i is None:
        return None
    j = next((k for k in range(i, len(lignes)) if lignes[k].strip() == fin), None)
    return None if j is None else (i, j)


def bloc_courant(texte: str, ident: str) -> str | None:
    debut, fin = marqueurs(ident)
    lignes = texte.split("\n")
    r = _region(lignes, debut, fin)
    return None if r is None else "\n".join(lignes[r[0]: r[1] + 1])


def poser(texte: str, bloc: str, ident: str) -> str:
    debut, fin = marqueurs(ident)
    lignes = texte.split("\n")
    r = _region(lignes, debut, fin)
    if r is not None:
        return "\n".join(lignes[: r[0]] + bloc.split("\n") + lignes[r[1] + 1:])
    k = next((i for i, l in enumerate(lignes) if l.startswith("# ")), None)
    if k is None:
        raise SystemExit("[derive] nulle part où poser le bloc : ni marqueurs, ni titre `# `")
    return "\n".join(lignes[: k + 1] + [""] + bloc.split("\n") + lignes[k + 1:])


def lire(p: Path) -> tuple[str, bool]:
    raw = p.read_bytes()
    return raw.decode("utf-8").replace("\r\n", "\n"), b"\r\n" in raw


def ecrire(p: Path, texte: str, crlf: bool) -> None:
    data = (texte.replace("\n", "\r\n") if crlf else texte).encode("utf-8")
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, p)


def verifier(source: Path, section: str, cibles: list[Path], ident: str) -> list[str]:
    titre, corps = lire_section(source, section)
    attendu = normaliser(bloc_derive(ident, source.name, titre, corps))
    erreurs = []
    for c in cibles:
        if not c.exists():
            erreurs.append(f"{c} : cible absente")
            continue
        texte, _ = lire(c)
        bloc = bloc_courant(texte, ident)
        if bloc is None:
            erreurs.append(f"{c} : bloc `{ident}` absent")
        elif normaliser(bloc) != attendu:
            erreurs.append(f"{c} : bloc `{ident}` DIVERGE de {source.name} — rejouer derive_bloc.py")
    return erreurs


def synchroniser(source: Path, section: str, cibles: list[Path], ident: str) -> list[Path]:
    titre, corps = lire_section(source, section)
    bloc = bloc_derive(ident, source.name, titre, corps)
    touches = []
    for c in cibles:
        if not c.exists():
            continue
        texte, crlf = lire(c)
        neuf = poser(texte, bloc, ident)
        if neuf != texte:
            ecrire(c, neuf, crlf)
            touches.append(c)
    return touches


def self_test() -> int:
    """Le contrôle sait rougir : un mot changé dans une cible, la source modifiée, un bloc retiré."""
    rep = Path(tempfile.mkdtemp(prefix="derive-"))
    src = rep / "RULES.md"
    src.write_text("# Règles\n\n## 7. Cadrer, puis dérouler seul\n\nUn seul moment de validation. Puis on exécute.\n\n## 8. Autre\n\nx\n", encoding="utf-8")
    a, b = rep / "a" / "SKILL.md", rep / "b" / "SKILL.md"
    for c in (a, b):
        c.parent.mkdir()
        c.write_text("---\nname: x\n---\n\n# Compétence\n\nCorps.\n", encoding="utf-8")
    cibles, ident, sec = [a, b], "s7", r"^## 7\."
    rate = 0

    def cas(nom: str, ok: bool) -> None:
        nonlocal rate
        rate += not ok
        print("  [%s] %s" % ("OK " if ok else "RATE", nom))

    cas("avant pose : deux blocs absents", len(verifier(src, sec, cibles, ident)) == 2)
    cas("pose : deux fichiers écrits, zéro écart", len(synchroniser(src, sec, cibles, ident)) == 2 and not verifier(src, sec, cibles, ident))
    t = a.read_text(encoding="utf-8")
    a.write_text(t.replace("Puis on exécute", "Puis on redemande"), encoding="utf-8")
    cas("sabotage : un mot changé dans une cible → rouge", any("DIVERGE" in e for e in verifier(src, sec, cibles, ident)))
    synchroniser(src, sec, cibles, ident)
    src.write_text(src.read_text(encoding="utf-8").replace("Puis on exécute.", "Puis on exécute, sans revalider."), encoding="utf-8")
    cas("sabotage : la source change → les deux cibles rougissent", sum("DIVERGE" in e for e in verifier(src, sec, cibles, ident)) == 2)
    cas("régénérer → vert, et le mot neuf est dans les cibles",
        len(synchroniser(src, sec, cibles, ident)) == 2 and not verifier(src, sec, cibles, ident)
        and "sans revalider" in b.read_text(encoding="utf-8"))
    t = b.read_text(encoding="utf-8")
    d, f = marqueurs(ident)
    b.write_text(t[: t.index(d)] + t[t.index(f) + len(f):], encoding="utf-8")
    cas("sabotage : bloc retiré → rouge", any("absent" in e for e in verifier(src, sec, cibles, ident)))
    print("%d/6 cas conformes." % (6 - rate))
    return 1 if rate else 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", type=Path)
    ap.add_argument("--section", help="regex de la ligne de titre (ex. '^## 33')")
    ap.add_argument("--cible", type=Path, action="append", default=[])
    ap.add_argument("--id", help="identifiant des marqueurs (défaut : dérivé de --section)")
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        return self_test()
    if not (a.source and a.section and a.cible):
        ap.error("--source, --section et au moins une --cible sont requis (ou --self-test)")
    ident = a.id or re.sub(r"[^A-Za-z0-9]+", "", a.section).lower() or "bloc"
    if a.check:
        erreurs = verifier(a.source, a.section, a.cible, ident)
        for e in erreurs:
            print("[derive] ✗", e)
        print("[derive] " + ("OK — source et cibles alignées" if not erreurs else f"{len(erreurs)} écart(s)"))
        return 1 if erreurs else 0
    for p in synchroniser(a.source, a.section, a.cible, ident):
        print("[derive] écrit :", p)
    reste = verifier(a.source, a.section, a.cible, ident)
    for e in reste:
        print("[derive] ✗", e)
    return 1 if reste else 0


if __name__ == "__main__":
    sys.exit(main())
