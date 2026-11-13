#!/usr/bin/env python3
"""Compare des instantanés textuels, sans modifier les sources.

0 : blocs conservés ; 1 : perte ; 2 : mesure invalide ; 3 : transformation à relire.
Ce contrôle de présence n'évalue pas le sens, le chargement ou l'usage par un agent.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

EXCLUDED = {'.git', '.archive', '_archive', 'archive', 'archives', '.store',
            '__pycache__', '.pytest_cache', '.venv', 'venv', 'node_modules'}


def excluded(name: str) -> bool:
    return name.lower() in EXCLUDED or name.lower().startswith(('.archive-', '_archive-'))


def blocks(text: str) -> set[str]:
    """Pas de seuil de longueur : une interdiction courte peut être essentielle."""
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    values = {'\n'.join(line.rstrip() for line in b.strip().splitlines()).strip()
              for b in re.split(r'\n[ \t]*\n', text)}
    return values - {'', '---', '***', '___'}


def digest(block: str) -> str:
    return hashlib.sha256(block.encode('utf-8')).hexdigest()


def collect(root: Path, *, active: bool) -> dict[Path, set[str]]:
    if root.is_symlink():
        raise ValueError(f'Racine symbolique non suivie : {root}')
    if not root.exists():
        raise ValueError(f'Source absente : {root}')
    root = root.resolve()
    if active and any(excluded(p) for p in root.parts):
        raise ValueError(f'Une archive ou un cache ne prouve pas une conservation active : {root}')
    found: dict[Path, set[str]] = {}

    def visit(path: Path) -> None:
        if path.is_symlink():
            raise ValueError(f'Lien symbolique à vérifier séparément : {path}')
        if path.is_dir():
            for child in sorted(path.iterdir()):
                if not excluded(child.name):
                    visit(child)
        elif path.is_file():
            raw = path.read_bytes()
            if b'\x00' in raw:
                raise ValueError(f'Fichier binaire hors preuve textuelle : {path}')
            try:
                text = raw.decode('utf-8-sig')
            except UnicodeDecodeError as exc:
                raise ValueError(f'Export UTF-8 requis : {path}') from exc
            found[path.resolve()] = blocks(text)
        else:
            raise ValueError(f'Type de source non pris en charge : {path}')

    visit(root)
    if not found:
        raise ValueError(f'Aucun fichier textuel actif lu : {root}')
    return found


def transformations(path: Path | None, before: dict[str, str],
                    available: dict[Path, set[str]]) -> dict[str, dict]:
    if path is None:
        return {}
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, dict) or set(data) != {'transformations'}:
        raise ValueError('Manifeste attendu : objet avec la seule clé transformations.')
    rows = data['transformations']
    if not isinstance(rows, list):
        raise ValueError('transformations doit être une liste.')
    result = {}
    for row in rows:
        keys = {'source_sha256', 'destination', 'replacement', 'preserve', 'reason'}
        if not isinstance(row, dict) or set(row) != keys:
            raise ValueError('Transformation : source_sha256, destination, replacement, preserve, reason requis.')
        sha = row['source_sha256']
        if not isinstance(sha, str) or not re.fullmatch('[0-9a-f]{64}', sha) or sha not in before:
            raise ValueError('Hash source inconnu ou invalide ; pas de dispense générique.')
        if sha in result:
            raise ValueError(f'Transformation déclarée deux fois : {sha}')
        if any(not isinstance(row[k], str) or not row[k].strip()
               for k in ('destination', 'replacement', 'reason')):
            raise ValueError('Destination, substitution et raison doivent être explicites.')
        target = Path(row['destination'])
        if not target.is_absolute():
            target = path.parent / target
        target = target.resolve()
        if target not in available:
            raise ValueError(f'Destination non lue dans le périmètre autorisé : {target}')
        replacement = blocks(row['replacement'])
        if len(replacement) != 1:
            raise ValueError('Une transformation désigne exactement un bloc de remplacement.')
        replacement = next(iter(replacement))
        if replacement not in available[target]:
            raise ValueError(f'Bloc complet absent de la destination désignée : {target}')
        keep = row['preserve']
        if not isinstance(keep, list) or any(not isinstance(s, str) or not s.strip() for s in keep):
            raise ValueError('preserve doit être une liste de fragments non vides.')
        if any(s not in before[sha] or s not in replacement for s in keep):
            raise ValueError('Un fragment déclaré conservé manque à la source ou à la destination.')
        result[sha] = {**row, 'destination': str(target), 'replacement': replacement}
    return result


def verify(before: Path, after: Path, destinations: list[Path] | None = None,
           manifest: Path | None = None) -> tuple[int, dict]:
    old_files = collect(before, active=False)
    new_files = collect(after, active=True)
    for destination in destinations or []:
        new_files.update(collect(destination, active=True))
    if set(old_files) & set(new_files):
        raise ValueError('Avant et après doivent être des instantanés distincts, sans fichiers communs.')
    old = {digest(b): b for values in old_files.values() for b in values}
    if not old:
        raise ValueError('Comparaison vide : aucun bloc source vérifiable.')
    declared = transformations(manifest, old, new_files)
    missing, preserved, reviewed = [], [], []
    for sha, block in sorted(old.items()):
        witnesses = [str(p) for p, values in new_files.items() if block in values]
        if sha in declared:
            # Même si une ancienne copie existe ailleurs, valider la destination désignée.
            reviewed.append({'sha256': sha, **declared[sha]})
        elif witnesses:
            preserved.append({'sha256': sha, 'found_in': witnesses})
        else:
            missing.append({'sha256': sha, 'preview': re.sub(r'\s+', ' ', block)[:160]})
    code = 1 if missing else 3 if reviewed else 0
    report = {
        'status': {0: 'PRESERVED', 1: 'LOSS', 3: 'REVIEW_REQUIRED'}[code],
        'before_files': len(old_files), 'after_files': len(new_files),
        'unique_source_blocks': len(old), 'preserved': preserved,
        'transformations_to_review': reviewed, 'missing': missing,
        'limits': 'Présence textuelle seulement ; ni équivalence sémantique, ni chargement, ni usage réel.'}
    return code, report


def self_test() -> None:
    with tempfile.TemporaryDirectory(prefix='capitaliser-check-') as tmp:
        root = Path(tmp)
        before, after = root / 'before', root / 'after'
        before.mkdir(); after.mkdir()
        rule = 'Ne jamais publier.'
        (before / 'source.md').write_text(rule, encoding='utf-8')
        (after / 'reference.md').write_text(rule, encoding='utf-8')
        if verify(before, after)[0] != 0:
            raise AssertionError('Déplacement intact refusé.')
        (after / 'reference.md').write_text('Autre contenu.', encoding='utf-8')
        if verify(before, after)[0] != 1:
            raise AssertionError('Suppression courte non détectée.')
        archive = after / '.archive'; archive.mkdir()
        (archive / 'old.md').write_text(rule, encoding='utf-8')
        if verify(before, after)[0] != 1:
            raise AssertionError('Archive prise pour une destination active.')
        try:
            verify(root / 'absent', after)
        except ValueError:
            pass
        else:
            raise AssertionError('Source absente acceptée.')
    print('SELF-TEST PASS : déplacement, suppression courte, archive exclue, source absente refusée.')


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding='utf-8', errors='replace')
        except (AttributeError, ValueError):
            pass
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--before', type=Path)
    parser.add_argument('--after', type=Path)
    parser.add_argument('--destination', action='append', type=Path, default=[])
    parser.add_argument('--transformations', type=Path)
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args(argv)
    if args.self_test:
        self_test()
        return 0
    if not args.before or not args.after:
        parser.error('--before et --after sont requis.')
    try:
        code, report = verify(args.before, args.after, args.destination, args.transformations)
    except (OSError, ValueError) as exc:
        code, report = 2, {'status': 'ERROR', 'error': str(exc)}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
