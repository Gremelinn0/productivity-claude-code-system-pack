#!/usr/bin/env python3
"""Inventaire documentaire explicite. 0 sain, 1 défaut trouvé, 2 non mesuré."""
import argparse
import json
import re
import sys
import tempfile
from pathlib import Path


def _meta(text, name):
    import yaml
    class StrictLoader(yaml.SafeLoader):
        pass
    def mapping(loader, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in result:
                raise ValueError('clé YAML dupliquée')
            result[key] = loader.construct_object(value_node, deep=deep)
        return result
    StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    if not match:
        raise ValueError('frontmatter absent ou BOM')
    meta = yaml.load(match.group(1), Loader=StrictLoader)
    if not isinstance(meta, dict) or meta.get('name') != name:
        raise ValueError('nom absent ou différent du dossier')
    desc = meta.get('description')
    if not isinstance(desc, str) or not 1 <= len(desc.strip()) <= 1024:
        raise ValueError('description vide, non textuelle ou hors contrat')
    return meta


def inventory(roots):
    import yaml  # Dépendance vérifiée avant toute conclusion sur le corpus.
    items, seen = [], set()
    for raw_root in roots:
        root = Path(raw_root)
        if root.is_symlink() or not root.is_dir():
            raise ValueError(f'Racine absente ou non directement accessible : {root}')
        root = root.resolve()
        if root in seen:
            continue
        seen.add(root)
        paths = sorted(p for p in root.glob('*/SKILL.md') if not p.parent.name.startswith('.'))
        if not paths:
            raise ValueError(f'Aucune compétence observée : {root} ; ne pas conclure à zéro défaut.')
        for path in paths:
            errors, meta, text = [], {}, ''
            if path.is_symlink() or path.parent.is_symlink():
                errors.append('lien symbolique : vérifier sa cible séparément')
            else:
                try:
                    text = path.read_text(encoding='utf-8')
                    meta = _meta(text, path.parent.name)
                except (OSError, UnicodeError, ValueError, yaml.YAMLError) as exc:
                    errors.append(str(exc))
            body = re.sub(r'```.*?```', '', text, flags=re.S)
            refs = set(re.findall(r'references/([\w.-]+\.md)', body))
            missing = sorted(ref for ref in refs if not (path.parent / 'references' / ref).is_file())
            items.append({'root': str(root), 'skill': path.parent.name,
                          'declared_name': meta.get('name'), 'description': meta.get('description'),
                          'lines': len(text.splitlines()), 'errors': errors,
                          'references_missing': missing})
    if not items:
        raise ValueError('Population non observée.')
    return items


def self_test():
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        skill = root / 'sample'; skill.mkdir()
        path = skill / 'SKILL.md'
        good = '---\nname: sample\ndescription: >-\n  Une description\n  en deux lignes.\n---\n# Sample\n'
        path.write_text(good, encoding='utf-8')
        row = inventory([root])[0]
        assert not row['errors'] and row['description'] == 'Une description en deux lignes.'
        for bad in [good.replace('name: sample', 'name: autre'),
                    good.replace('name: sample', 'name: sample\nname: sample'),
                    good.replace('description: >-\n  Une description\n  en deux lignes.', 'description: null'),
                    good.replace('description: >-\n  Une description\n  en deux lignes.', 'description: a: b'),
                    '\ufeff' + good]:
            path.write_text(bad, encoding='utf-8')
            assert inventory([root])[0]['errors']
        path.write_text(good + '[Référence](references/missing.md)\n', encoding='utf-8')
        assert inventory([root])[0]['references_missing'] == ['missing.md']
        for absent in [root / 'absent', root / 'empty']:
            if absent.name == 'empty': absent.mkdir()
            try: inventory([absent])
            except ValueError: pass
            else: raise AssertionError('Population non observée acceptée')
    print('SELF-TEST PASS : YAML replié sain ; 8 cas invalides ou non mesurables refusés.')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('roots', nargs='*')
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args(argv)
    try:
        if args.self_test:
            self_test(); return 0
        data = inventory(args.roots or ['skills'])
    except (OSError, ValueError, ImportError) as exc:
        print(json.dumps({'status': 'NON_MESURE', 'error': str(exc)}, ensure_ascii=False))
        return 2
    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        for row in data:
            print(f"{row['skill']}: {row['lines']} lignes ; {len(row['errors'])} défaut(s) ; {len(row['references_missing'])} référence(s) absente(s)")
    return 1 if any(row['errors'] or row['references_missing'] for row in data) else 0


if __name__ == '__main__':
    raise SystemExit(main())
