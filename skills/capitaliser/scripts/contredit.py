#!/usr/bin/env python3
"""Localise les occurrences d'une décision ; ne décide pas qu'elles sont fausses.
0 : occurrences sur le corpus lu ; 1 : erreur ; 2 : absence ou couverture partielle à vérifier.
Lecture seule, racine explicite, liens symboliques non suivis, omissions toujours signalées.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import sys

DEFAULT_EXT={'.md','.html','.json','.yaml','.yml','.txt','.mdx'}
SKIP_DIRS={'.git','node_modules','.venv','venv','__pycache__','.mypy_cache','.pytest_cache',
           'dist','build','.next','.turbo','.cache','coverage','worktrees','_archive',
           'skills-store','.archive','.store','stash-janitor-archive','.claude-plugin-cache','site-packages'}
MAX_BYTES=2_000_000


def scan_report(root: str | Path, terms: list[str], exts: set[str] | None=None) -> dict:
    base=Path(root)
    if base.is_symlink() or not base.is_dir():
        raise ValueError(f'Racine absente ou symbolique : {base}')
    if not terms or any(not isinstance(t,str) or not t.strip() for t in terms):
        raise ValueError('Au moins un terme non vide ; les termes vides sont refusés.')
    base=base.resolve(); terms=list(dict.fromkeys(terms)); exts=exts or DEFAULT_EXT
    hits=[]; issues=[]; excluded=[]; files_read=0; per_term={t:0 for t in terms}
    def walk_error(exc): issues.append({'path':str(exc.filename),'reason':'unreadable_directory'})
    for directory, dirs, names in os.walk(base, followlinks=False, onerror=walk_error):
        keep=[]
        for name in sorted(dirs):
            path=Path(directory)/name
            if path.is_symlink(): issues.append({'path':str(path.relative_to(base)),'reason':'symlink'})
            elif name in SKIP_DIRS or name.startswith(('.git','.archive-','_archive-')):
                excluded.append(str(path.relative_to(base)))
            else: keep.append(name)
        dirs[:]=keep
        for name in sorted(names):
            path=Path(directory)/name
            if path.suffix.lower() not in exts: continue
            relative=str(path.relative_to(base))
            try:
                if path.is_symlink():
                    issues.append({'path':relative,'reason':'symlink'}); continue
                if path.stat().st_size>MAX_BYTES:
                    issues.append({'path':relative,'reason':'oversized'}); continue
                lines=path.read_text(encoding='utf-8-sig').splitlines()
            except (OSError,UnicodeError):
                issues.append({'path':relative,'reason':'unreadable_text'}); continue
            files_read+=1; total=max(1,len(lines))
            for number,line in enumerate(lines,1):
                matched=[t for t in terms if t.casefold() in line.casefold()]
                if not matched: continue
                for term in matched: per_term[term]+=1
                hits.append({'path':relative,'line':number,'head':number/total<=0.15,
                             'terms':matched,'text':line.strip()[:160]})
    hits.sort(key=lambda h:(not h['head'],h['path'],h['line']))
    return {'root':str(base),'files_read':files_read,'terms':per_term,'hits':hits,'issues':issues,
            'excluded':excluded,'extensions':sorted(exts),'complete_for_declared_scope':not issues,
            'meaning':'Occurrences à relire ; ni contradictions prouvées ni absence globale certifiée.'}


def scan(root,terms,exts):
    """Ancienne interface conservée. Consulter scan_report pour la couverture détaillée."""
    report=scan_report(root,terms,exts)
    return report['hits'],report['terms'],report['files_read']


def main(argv=None):
    for stream in (sys.stdout,sys.stderr):
        try: stream.reconfigure(encoding='utf-8',errors='replace')
        except (AttributeError,OSError,ValueError): pass
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('terms',nargs='+');parser.add_argument('--root',default='.')
    parser.add_argument('--ext',default='');parser.add_argument('--limit',type=int,default=40)
    parser.add_argument('--all',action='store_true');parser.add_argument('--json',action='store_true')
    args=parser.parse_args(argv)
    if args.limit<1: parser.error('--limit doit être positif')
    exts=DEFAULT_EXT | {('.'+s.strip().lstrip('.')).lower() for s in args.ext.split(',') if s.strip()}
    try: report=scan_report(args.root,args.terms,exts)
    except (OSError,ValueError) as exc:
        print(json.dumps({'status':'ERROR','error':str(exc)},ensure_ascii=False));return 1
    count=len(report['hits']); omitted=0 if args.all else max(0,count-args.limit)
    code=0 if count and not report['issues'] else 2
    report['status']='OCCURRENCES' if code==0 else 'A_VERIFIER'
    report['total_hits']=count;report['not_displayed']=omitted
    if not args.all: report['hits']=report['hits'][:args.limit]
    if args.json: print(json.dumps(report,ensure_ascii=False,indent=2))
    else:
        print(f"{report['status']} — {count} occurrence(s), {report['files_read']} fichiers lus")
        print(report['meaning'])
        for hit in report['hits']: print(f"{'TETE' if hit['head'] else '    '} {hit['path']}:{hit['line']} {hit['text']}")
        print(f"{omitted} occurrence(s) non affichée(s), {len(report['issues'])} omission(s), {len(report['excluded'])} dossier(s) exclus.")
        if not count: print('Vérifier termes, corpus et accès avant de conclure à une absence.')
        for issue in report['issues']: print(f"NON LU : {issue['path']} ({issue['reason']})")
    return code


if __name__=='__main__': raise SystemExit(main())
