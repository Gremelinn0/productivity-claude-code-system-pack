#!/usr/bin/env python3
"""Valide les fichiers du pack. Ne certifie pas le comportement d'un agent."""
from pathlib import Path
import re
import sys

NAMES = {'capitaliser', 'clean-rules-cleanup', 'optimise-systeme', 'skill-cleaner',
         'skill-quality-guard', 'propage-systeme', 'router-entretien-systeme'}
REQUIRED = {
    'skill-quality-guard': ('fabriquer', 'refondre', 'vérifier', 'resynchroniser', 'skill-creator'),
    'optimise-systeme': ('skill-cleaner', 'capitaliser', 'propage-systeme'),
    'clean-rules-cleanup': ('gerer-les-hooks.md', 'skill-cleaner'),
    'router-entretien-systeme': ('optimise-systeme',),
}


def metadata(text, name):
    import yaml
    class UniqueLoader(yaml.SafeLoader): pass
    def mapping(loader, node, deep=False):
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in result: raise ValueError('clé YAML dupliquée')
            result[key] = loader.construct_object(value_node, deep=deep)
        return result
    UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
    m = re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)', text, re.S)
    if not m: raise ValueError('frontmatter absent ou BOM')
    data = yaml.load(m.group(1), Loader=UniqueLoader)
    if not isinstance(data, dict) or data.get('name') != name: raise ValueError('nom incorrect')
    description = data.get('description')
    if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
        raise ValueError('description vide, non textuelle ou hors contrat')
    return data


def inspect(root):
    issues = []
    skills = root / 'skills'
    if not skills.is_dir(): return ['répertoire skills absent']
    actual = {p.name for p in skills.iterdir() if p.is_dir() and not p.name.startswith('.')}
    if actual != NAMES: issues.append(f'inventaire inattendu : manquants={NAMES-actual}, autres={actual-NAMES}')
    for name in sorted(NAMES):
        f = skills / name / 'SKILL.md'
        try:
            text = f.read_text(encoding='utf-8')
            data = metadata(text, name)
            if name == 'router-entretien-systeme':
                if data.get('metadata', {}).get('role') != 'compatibility-alias' or data.get('metadata', {}).get('canonical') != 'optimise-systeme':
                    issues.append('router-entretien-systeme: alias incorrect')
            for token in REQUIRED.get(name, ()):
                if token not in text: issues.append(f'{name}: route ou rôle déclaré absent : {token}')
        except Exception as exc: issues.append(f'{name}: {exc}')
    for f in skills.rglob('*.md'):
        if any(p.startswith('.') for p in f.relative_to(skills).parts): continue
        text = f.read_text(encoding='utf-8')
        body = re.sub(r'```.*?```', '', text, flags=re.S)
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', body):
            if target.startswith(('http:', 'https:', '#', 'mailto:')): continue
            target = target.split('#')[0]
            if target and not (f.parent / target).is_file(): issues.append(f'{f.relative_to(root)}: lien absent {target}')
        for private in ('speak-app-dev/', 'pilotage_medias', 'C:\\Users\\', 'BEGIN PRIVATE KEY'):
            if private in text: issues.append(f'{f.relative_to(root)}: détail privé interdit {private}')
    for f in skills.rglob('*.py'):
        try: compile(f.read_text(encoding='utf-8'), str(f), 'exec')
        except (SyntaxError, UnicodeError) as exc: issues.append(f'{f}: {exc}')
    return issues


def self_test():
    valid = '---\nname: exemple\ndescription: >-\n  Conserve une décision après une tâche.\n---\n'
    metadata(valid, 'exemple')
    invalid = [valid.replace('  Conserve une décision après une tâche.', ''),
               valid.replace('description: >-\n  Conserve une décision après une tâche.', 'description: null'),
               valid.replace('description: >-\n  Conserve une décision après une tâche.', 'description: 42'),
               valid.replace('name: exemple', 'name: autre'), '\ufeff' + valid,
               valid.replace('name: exemple', 'name: exemple\nname: exemple'),
               valid.replace('  Conserve une décision après une tâche.', '  ' + 'a'*1025),
               valid.replace('description: >-\n  Conserve une décision après une tâche.', 'description: a: b')]
    for i, candidate in enumerate(invalid):
        try: metadata(candidate, 'exemple')
        except Exception: continue
        raise AssertionError(f'faux positif {i}')
    print('SELF-TEST PASS : YAML conforme accepté, 8 défauts refusés.')


if __name__ == '__main__':
    if '--self-test' in sys.argv:
        self_test(); raise SystemExit(0)
    errors = inspect(Path(__file__).resolve().parents[1])
    if errors:
        print('\n'.join('ERREUR ' + e for e in errors)); raise SystemExit(1)
    print('PACK DOCUMENTAIRE PASS : inventaire, YAML, routes déclarées, références et syntaxe. Essais agent distincts.')
