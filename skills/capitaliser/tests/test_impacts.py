import importlib.util
import json
import subprocess
import sys
from pathlib import Path
import tempfile
import unittest
P=Path(__file__).resolve().parents[1]/'scripts/contredit.py'
spec=importlib.util.spec_from_file_location('impacts',P)
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class ImpactsTests(unittest.TestCase):
    def setUp(self): self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
    def tearDown(self): self.tmp.cleanup()
    def put(self,name,text):
        p=self.root/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text,encoding='utf-8');return p
    def test_match(self):
        self.put('a.md','Décision : alpha');r=m.scan_report(self.root,['alpha'])
        self.assertEqual(r['terms']['alpha'],1);self.assertEqual(r['files_read'],1)
    def test_casefold(self):
        self.put('a.md','DÉCISION');self.assertEqual(len(m.scan_report(self.root,['décision'])['hits']),1)
    def test_head_first(self):
        self.put('a.md','\n'.join(['x']*19+['alpha']))
        self.put('b.md','\n'.join(['alpha']+['x']*19))
        self.assertEqual(m.scan_report(self.root,['alpha'])['hits'][0]['path'],'b.md')
    def test_archives_excluded(self):
        self.put('.archive/a.md','alpha');self.assertEqual(m.scan_report(self.root,['alpha'])['files_read'],0)
    def test_symlink_not_read(self):
        other=self.put('outside.txt','alpha');(self.root/'link.md').symlink_to(other)
        r=m.scan_report(self.root,['alpha']);self.assertTrue(r['issues'])
    def test_invalid_utf8_reported(self):
        (self.root/'a.md').write_bytes(b'\xff');self.assertTrue(m.scan_report(self.root,['alpha'])['issues'])
    def test_large_reported(self):
        self.put('a.md','x'*(m.MAX_BYTES+1));self.assertTrue(m.scan_report(self.root,['alpha'])['issues'])
    def test_no_empty_term(self):
        with self.assertRaises(ValueError): m.scan_report(self.root,[''])
    def test_missing_root(self):
        with self.assertRaises(ValueError): m.scan_report(self.root/'absent',['alpha'])
    def cli(self,*args):
        return subprocess.run([sys.executable,str(P),'alpha','--root',str(self.root),'--json',*args],capture_output=True)
    def test_cli_zero_not_success(self): self.assertEqual(self.cli().returncode,2)
    def test_cli_truncation_explicit(self):
        self.put('a.md','alpha\nalpha\nalpha')
        r=self.cli('--limit','1');self.assertEqual(r.returncode,0)
        self.assertEqual(json.loads(r.stdout)['not_displayed'],2)
    def test_cli_partial_not_success(self):
        self.put('a.md','alpha');(self.root/'b.md').write_bytes(b'\xff')
        self.assertEqual(self.cli().returncode,2)
    def test_read_only(self):
        p=self.put('a.md','alpha');before=p.read_bytes();m.scan_report(self.root,['alpha'])
        self.assertEqual(before,p.read_bytes())
    def test_legacy_tuple(self):
        self.put('a.md','alpha');hits,terms,n=m.scan(str(self.root),['alpha'],m.DEFAULT_EXT)
        self.assertEqual((len(hits),terms['alpha'],n),(1,1,1))

if __name__=='__main__': unittest.main()
