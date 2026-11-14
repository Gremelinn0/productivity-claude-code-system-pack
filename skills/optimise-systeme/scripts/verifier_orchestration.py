#!/usr/bin/env python3
"""Contrôle structurel de la famille : ne prouve pas les choix d'un agent."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys
import yaml

ENTRIES={'optimise-systeme','capitaliser'}
OWNERS=ENTRIES | {'clean-rules-cleanup','skill-cleaner','skill-quality-guard','propage-systeme'}
ALIASES={'router-ameliorer-systeme-ia':'optimise-systeme',
         'router-entretien-systeme':'optimise-systeme','router-capitalisation':'capitaliser'}

class UniqueLoader(yaml.SafeLoader): pass

def unique_mapping(loader,node,deep=False):
    value={}
    for k,v in node.value:
        key=loader.construct_object(k,deep=deep)
        if key in value: raise ValueError(f'Clé YAML répétée : {key}')
        value[key]=loader.construct_object(v,deep=deep)
    return value
UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,unique_mapping)


def metadata(path: Path, limit_description: bool=True) -> tuple[dict,str]:
    text=path.read_text(encoding='utf-8')
    match=re.match(r'\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)',text,re.S)
    if not match: raise ValueError('Frontmatter absent ou BOM')
    data=yaml.load(match.group(1),Loader=UniqueLoader)
    if not isinstance(data,dict) or data.get('name')!=path.parent.name:
        raise ValueError('Nom absent ou différent du dossier')
    desc=data.get('description')
    if not isinstance(desc,str) or not desc.strip() or (limit_description and len(desc.strip())>1024):
        raise ValueError('Description invalide')
    return data,text


def validate_graph(contract: dict) -> list[str]:
    if not isinstance(contract,dict): return ['Contrat non objet']
    errors=[]
    if contract.get('schema')!='orchestration-v1': errors.append('Schéma incorrect')
    if set(contract.get('entries',[]))!=ENTRIES: errors.append('Les deux entrées ne sont pas conservées')
    owners=contract.get('owners',{})
    if not isinstance(owners,dict) or any(not isinstance(v,dict) for v in owners.values()):
        return ['Propriétaires invalides']
    if set(owners)!=OWNERS: errors.append('Inventaire des propriétaires incorrect')
    if contract.get('aliases')!=ALIASES: errors.append('Matrice des alias incorrecte')
    if owners.get('optimise-systeme',{}).get('role')!='orchestration': errors.append('Pilote incorrect')
    if owners.get('capitaliser',{}).get('role')!='capitalisation': errors.append('Capitalisation incorrecte')
    graph={}
    for owner,info in owners.items():
        calls=info.get('calls',[])
        if not isinstance(calls,list) or any(not isinstance(x,str) for x in calls):
            errors.append(f'{owner}: appels invalides'); continue
        if len(set(calls))!=len(calls): errors.append(f'{owner}: appel déclaré deux fois')
        if set(calls)-OWNERS: errors.append(f'{owner}: cible inconnue ou alias utilisé comme propriétaire')
        graph[owner]=calls
    visiting=set(); seen=set()
    def visit(name):
        if name in visiting: errors.append(f'Cycle de pilotage : {name}');return
        if name in seen: return
        visiting.add(name)
        for target in graph.get(name,[]): visit(target)
        visiting.remove(name);seen.add(name)
    for node in graph: visit(node)
    if 'optimise-systeme' in graph.get('capitaliser',[]): errors.append('Capitaliser rappelle automatiquement le pilote')
    expected={'delegates_return_to_caller','reuse_completed_operations','audit_does_not_authorize_mutation',
              'no_automatic_optimizer_callback','no_automatic_new_routine','hooks_need_explicit_authorization'}
    if any(contract.get('guards',{}).get(k) is not True for k in expected): errors.append('Garantie de mandat manquante')
    return errors


def inspect(root: Path) -> list[str]:
    if not root.is_dir(): return ['Racine des compétences absente']
    contract_path=root/'optimise-systeme/references/contrat-orchestration.json'
    contract=json.loads(contract_path.read_text(encoding='utf-8'));errors=validate_graph(contract)
    for name in sorted(OWNERS):
        try: metadata(root/name/'SKILL.md',limit_description=name in ENTRIES)
        except (OSError,ValueError,yaml.YAMLError) as exc: errors.append(f'{name}: {exc}')
    for name,target in ALIASES.items():
        path=root/name/'SKILL.md'
        if not path.exists(): continue  # Ne pas installer un alias absent du pack d'origine.
        try:
            meta,_=metadata(path)
            if meta.get('metadata',{}).get('role')!='compatibility-alias' or meta.get('metadata',{}).get('canonical')!=target:
                errors.append(f'{name}: second propriétaire au lieu d’un alias')
            if meta.get('disable-model-invocation') is True: errors.append(f'{name}: anciens appels automatiques bloqués')
        except (OSError,ValueError,yaml.YAMLError) as exc: errors.append(f'{name}: {exc}')
    for owner in ENTRIES:
        for path in [root/owner/'SKILL.md',*(root/owner/'references').glob('*.md')]:
            if not path.is_file(): continue  # Déjà signalé par le contrôle du propriétaire.
            text=path.read_text(encoding='utf-8')
            body=re.sub(r'```.*?```','',text,flags=re.S)
            for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',body):
                if target.startswith(('http:','https:','#','mailto:')): continue
                local=target.split('#',1)[0]
                if local and not (path.parent/local).is_file(): errors.append(f'{path.name}: lien absent {target}')
    workflow=root/'router-ameliorer-systeme-ia/references/workflow.json'
    if workflow.exists():
        data=json.loads(workflow.read_text(encoding='utf-8'))
        if data.get('routeur')!='optimise-systeme' or data.get('commande')!='/optimise-systeme': errors.append('Workflow : propriétaire périmé')
        names=[c.get('nom') for e in data.get('etapes',[]) for c in e.get('competences',[])]
        if 'optimise-systeme' in names: errors.append('Workflow : auto-invocation du pilote')
        if names.count('capitaliser')!=1 or 'router-capitalisation' in names: errors.append('Workflow : capitalisation double ou absente')
    return errors


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[2])
    args=parser.parse_args(argv)
    try: errors=inspect(args.root)
    except (OSError,ValueError,TypeError,yaml.YAMLError) as exc:
        print(f'NON MESURÉ : {exc}');return 2
    if errors:
        print('\n'.join('ERREUR : '+e for e in errors));return 1
    print('ORCHESTRATION DOCUMENTAIRE PASS — entrées/alias, présence et YAML des spécialistes, graphe déclaré. Usage agent non testé.')
    return 0


if __name__=='__main__': raise SystemExit(main())
