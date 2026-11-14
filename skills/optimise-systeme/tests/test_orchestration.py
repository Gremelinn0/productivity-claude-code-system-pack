import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

BASE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('orch',BASE/'scripts/verifier_orchestration.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
CONTRACT=json.loads((BASE/'references/contrat-orchestration.json').read_text(encoding='utf-8'))

class GraphTests(unittest.TestCase):
    def setUp(self): self.c=copy.deepcopy(CONTRACT)
    def test_valid(self): self.assertEqual(m.validate_graph(self.c),[])
    def test_self_cycle(self):
        self.c['owners']['optimise-systeme']['calls'].append('optimise-systeme')
        self.assertTrue(m.validate_graph(self.c))
    def test_two_owner_cycle(self):
        self.c['owners']['capitaliser']['calls'].append('optimise-systeme')
        self.assertTrue(m.validate_graph(self.c))
    def test_three_owner_cycle(self):
        self.c['owners']['propage-systeme']['calls'].append('capitaliser')
        self.assertTrue(m.validate_graph(self.c))
    def test_unknown_target(self):
        self.c['owners']['capitaliser']['calls'].append('phantom')
        self.assertTrue(m.validate_graph(self.c))
    def test_alias_not_owner(self):
        self.c['owners']['optimise-systeme']['calls'].append('router-capitalisation')
        self.assertTrue(m.validate_graph(self.c))
    def test_repeated_call(self):
        self.c['owners']['optimise-systeme']['calls'].append('capitaliser')
        self.assertTrue(m.validate_graph(self.c))
    def test_one_entry_not_enough(self):
        self.c['entries']=['optimise-systeme'];self.assertTrue(m.validate_graph(self.c))
    def test_third_entry_rejected(self):
        self.c['entries'].append('router-entretien-systeme');self.assertTrue(m.validate_graph(self.c))
    def test_lost_specialist(self):
        self.c['owners'].pop('skill-cleaner');self.assertTrue(m.validate_graph(self.c))
    def test_wrong_role(self):
        self.c['owners']['optimise-systeme']['role']='cleanup';self.assertTrue(m.validate_graph(self.c))
    def test_alias_wrong_target(self):
        self.c['aliases']['router-capitalisation']='optimise-systeme';self.assertTrue(m.validate_graph(self.c))
    def test_each_guard_is_enforced(self):
        for key in self.c['guards']:
            altered=copy.deepcopy(self.c);altered['guards'][key]=False
            with self.subTest(key=key): self.assertTrue(m.validate_graph(altered))
    def test_invalid_schema(self):
        self.c['schema']='other';self.assertTrue(m.validate_graph(self.c))

class FilesTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
        for name in m.OWNERS:
            self.write(f'{name}/SKILL.md',f'---\nname: {name}\ndescription: Une méthode pour le cas demandé.\n---\n# Contrat\n')
        self.write('optimise-systeme/references/contrat-orchestration.json',json.dumps(CONTRACT))
    def tearDown(self): self.tmp.cleanup()
    def write(self,path,text):
        p=self.root/path;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8');return p
    def alias(self,extra=''):
        return self.write('router-capitalisation/SKILL.md','---\nname: router-capitalisation\ndescription: Ancien nom seulement.\n'+extra+'metadata:\n  role: compatibility-alias\n  canonical: capitaliser\n---\n# Compatibilité\n')
    def test_complete(self): self.assertEqual(m.inspect(self.root),[])
    def test_missing_owner(self):
        (self.root/'capitaliser/SKILL.md').unlink();self.assertTrue(m.inspect(self.root))
    def test_empty_description(self):
        self.write('capitaliser/SKILL.md','---\nname: capitaliser\ndescription: null\n---\n')
        self.assertTrue(m.inspect(self.root))
    def test_duplicate_yaml(self):
        self.write('capitaliser/SKILL.md','---\nname: capitaliser\nname: capitaliser\ndescription: Texte\n---\n')
        self.assertTrue(m.inspect(self.root))
    def test_alias_valid(self): self.alias();self.assertEqual(m.inspect(self.root),[])
    def test_alias_model_block_breaks_compatibility(self):
        self.alias('disable-model-invocation: true\n');self.assertTrue(m.inspect(self.root))
    def test_broken_reference(self):
        path=self.root/'capitaliser/SKILL.md';path.write_text(path.read_text()+'[Détail](references/absent.md)\n')
        self.assertTrue(m.inspect(self.root))
    def test_missing_root(self): self.assertTrue(m.inspect(self.root/'absent'))
    def workflow(self,names,owner='optimise-systeme'):
        self.write('router-ameliorer-systeme-ia/references/workflow.json',json.dumps({'routeur':owner,'commande':'/'+owner,'etapes':[{'competences':[{'nom':n} for n in names]}]}))
    def test_workflow_valid(self):
        self.workflow(['capitaliser']);self.assertEqual(m.inspect(self.root),[])
    def test_workflow_legacy(self):
        self.workflow(['capitaliser'],'router-ameliorer-systeme-ia');self.assertTrue(m.inspect(self.root))
    def test_workflow_self_call(self):
        self.workflow(['optimise-systeme','capitaliser']);self.assertTrue(m.inspect(self.root))
    def test_workflow_double_capitalisation(self):
        self.workflow(['router-capitalisation','capitaliser']);self.assertTrue(m.inspect(self.root))

if __name__=='__main__': unittest.main()
