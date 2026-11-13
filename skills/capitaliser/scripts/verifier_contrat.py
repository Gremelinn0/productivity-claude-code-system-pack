#!/usr/bin/env python3
"""Contrôle documentaire : YAML strict et références locales, pas comportement agent."""
from pathlib import Path
import argparse
import json
import re
import sys


def inspect(root: Path) -> list[str]:
    try:
        import yaml
    except ImportError:
        raise RuntimeError('PyYAML manque : contrôle documentaire non exécuté.')
    class StrictLoader(yaml.SafeLoader):
        pass
    def mapping(loader, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in result:
                raise ValueError(f'Clé YAML dupliquée : {key}')
            result[key] = loader.construct_object(value_node, deep=deep)
        return result
    StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
    issues = []
    path = root / 'SKILL.md'
    text = path.read_text(encoding='utf-8')
    match = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    if not match:
        return ['Frontmatter absent ou BOM interdit.']
    meta = yaml.load(match.group(1), Loader=StrictLoader)
    if not isinstance(meta, dict):
        return ['Frontmatter non mapping.']
    name, description = meta.get('name'), meta.get('description')
    if name != root.name or not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
        issues.append('Nom invalide ou différent du dossier.')
    if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
        issues.append('Description absente, vide, non textuelle ou hors contrat 1–1024 caractères.')
    for doc in [path, *sorted((root / 'references').glob('*.md'))]:
        body = doc.read_text(encoding='utf-8')
        body = re.sub(r'```.*?```', '', body, flags=re.S)
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', body):
            if target.startswith(('https:', 'http:', '#', 'mailto:')):
                continue
            target = target.split('#', 1)[0]
            if not target or not (doc.parent / target).is_file():
                issues.append(f'{doc.name}: référence locale absente : {target}')
    data = json.loads((root / 'evals' / 'evals.json').read_text(encoding='utf-8'))
    if data.get('skill_name') != name or not data.get('evals'):
        issues.append('Scénarios absents ou rattachés à un autre skill.')
    for script in (root / 'scripts').glob('*.py'):
        compile(script.read_text(encoding='utf-8'), str(script), 'exec')
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('skill', type=Path)
    args = parser.parse_args()
    try:
        issues = inspect(args.skill)
    except Exception as exc:
        print(f'NON MESURÉ : {exc}', file=sys.stderr)
        return 2
    for issue in issues:
        print('ERREUR :', issue)
    if issues:
        return 1
    print('CONTRAT DOCUMENTAIRE PASS — YAML, références, scénarios et syntaxe Python. Usage agent non testé.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
