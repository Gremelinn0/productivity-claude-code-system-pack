"""Tests du contrôle textuel, pas des décisions d'un modèle."""
import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'verification.py'
spec = importlib.util.spec_from_file_location('verification', SCRIPT)
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)


class VerificationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.before = self.root / 'before'; self.before.mkdir()
        self.after = self.root / 'after'; self.after.mkdir()
        self.rule = 'Ne jamais publier.'
        self.write(self.before / 'source.md', self.rule)
        self.write(self.after / 'target.md', self.rule)

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding='utf-8')
        return path

    def check(self, **kw):
        return v.verify(self.before, self.after, **kw)

    def manifest(self, **changes):
        row = {'source_sha256': v.digest(self.rule),
               'destination': 'after/target.md',
               'replacement': 'Ne jamais publier. Préserver les données.',
               'preserve': [self.rule], 'reason': 'Ajout de la condition de conservation.'}
        row.update(changes)
        path = self.root / 'manifest.json'
        path.write_text(json.dumps({'transformations': [row]}), encoding='utf-8')
        return path

    def test_intact(self):
        self.assertEqual(self.check()[0], 0)

    def test_move_to_reference(self):
        (self.after / 'target.md').unlink()
        self.write(self.after / 'references' / 'decision.md', self.rule)
        self.assertEqual(self.check()[0], 0)

    def test_short_deletion(self):
        self.write(self.after / 'target.md', 'Autre règle.')
        self.assertEqual(self.check()[0], 1)

    def test_partial_paragraph_deletion(self):
        self.write(self.before / 'source.md', self.rule + ' Conserver le refus et sa raison.')
        self.assertEqual(self.check()[0], 1)

    def test_missing_before(self):
        with self.assertRaises(ValueError): v.verify(self.root / 'missing', self.after)

    def test_empty_before(self):
        self.write(self.before / 'source.md', '\n---\n')
        with self.assertRaises(ValueError): self.check()

    def test_no_before_files(self):
        (self.before / 'source.md').unlink()
        with self.assertRaises(ValueError): self.check()

    def test_missing_after(self):
        with self.assertRaises(ValueError): v.verify(self.before, self.root / 'missing')

    def test_empty_after(self):
        self.write(self.after / 'target.md', '')
        self.assertEqual(self.check()[0], 1)

    def test_archive_is_not_active(self):
        self.write(self.after / 'target.md', 'Autre règle.')
        self.write(self.after / '.archive' / 'old.md', self.rule)
        self.assertEqual(self.check()[0], 1)

    def test_dated_archive_is_not_active(self):
        self.write(self.after / 'target.md', 'Autre règle.')
        self.write(self.after / '_archive-2020' / 'old.md', self.rule)
        self.assertEqual(self.check()[0], 1)

    def test_explicit_archive_destination_rejected(self):
        archive = self.after / '.archive'
        self.write(archive / 'old.md', self.rule)
        with self.assertRaises(ValueError): self.check(destinations=[archive])

    def test_cache_does_not_cover(self):
        self.write(self.after / 'target.md', 'Autre règle.')
        self.write(self.after / '__pycache__' / 'old.md', self.rule)
        self.assertEqual(self.check()[0], 1)

    def test_external_owner_covers(self):
        self.write(self.after / 'target.md', 'Voir le propriétaire.')
        dest = self.write(self.root / 'owner' / 'rule.md', self.rule)
        self.assertEqual(self.check(destinations=[dest])[0], 0)

    def test_pointer_not_proof(self):
        self.write(self.after / 'target.md', 'Voir la règle Ne jamais publier. chez le propriétaire.')
        self.assertEqual(self.check()[0], 1)

    def test_missing_destination_rejected_even_when_after_matches(self):
        with self.assertRaises(ValueError): self.check(destinations=[self.root / 'missing'])

    def test_snapshot_must_be_distinct(self):
        with self.assertRaises(ValueError): v.verify(self.before, self.before)

    def test_binary_not_silently_skipped(self):
        (self.before / 'image.bin').write_bytes(b'\x00\xff')
        with self.assertRaises(ValueError): self.check()

    def test_non_utf8_not_silently_skipped(self):
        (self.before / 'legacy.txt').write_bytes(b'\xff')
        with self.assertRaises(ValueError): self.check()

    def test_symlink_not_followed(self):
        (self.after / 'link.md').symlink_to(self.before / 'source.md')
        with self.assertRaises(ValueError): self.check()

    def test_crlf_equivalent(self):
        (self.before / 'source.md').write_bytes(b'First\r\nSecond\r\n')
        self.write(self.after / 'target.md', 'First\nSecond\n')
        self.assertEqual(self.check()[0], 0)

    def test_duplicate_information_can_be_deduplicated(self):
        self.write(self.before / 'copy.md', self.rule)
        self.assertEqual(self.check()[0], 0)
        self.assertEqual(self.check()[1]['unique_source_blocks'], 1)

    def test_valid_transformation_is_never_pass(self):
        path = self.manifest()
        self.write(self.after / 'target.md', 'Ne jamais publier. Préserver les données.')
        self.assertEqual(self.check(manifest=path)[0], 3)

    def test_unknown_hash(self):
        path = self.manifest(source_sha256='a' * 64)
        with self.assertRaises(ValueError): self.check(manifest=path)

    def test_empty_reason(self):
        path = self.manifest(reason=' ')
        with self.assertRaises(ValueError): self.check(manifest=path)

    def test_wrong_destination_despite_replacement_elsewhere(self):
        path = self.manifest()
        self.write(self.after / 'elsewhere.md', 'Ne jamais publier. Préserver les données.')
        with self.assertRaises(ValueError): self.check(manifest=path)

    def test_fragment_is_not_full_replacement(self):
        path = self.manifest(replacement=self.rule)
        self.write(self.after / 'target.md', self.rule + ' Un autre contexte qui change le sens.')
        with self.assertRaises(ValueError): self.check(manifest=path)

    def test_preserved_fragment_cannot_disappear(self):
        path = self.manifest(replacement='Publier sans contrôle.')
        self.write(self.after / 'target.md', 'Publier sans contrôle.')
        with self.assertRaises(ValueError): self.check(manifest=path)

    def test_preservation_fragment_must_have_existed(self):
        path = self.manifest(preserve=['Préserver les données.'])
        self.write(self.after / 'target.md', 'Ne jamais publier. Préserver les données.')
        with self.assertRaises(ValueError): self.check(manifest=path)

    def test_duplicate_manifest_entry(self):
        path = self.manifest()
        data = json.loads(path.read_text()); data['transformations'] *= 2
        path.write_text(json.dumps(data))
        self.write(self.after / 'target.md', 'Ne jamais publier. Préserver les données.')
        with self.assertRaises(ValueError): self.check(manifest=path)

    def test_malformed_manifest_type(self):
        path = self.root / 'manifest.json'; path.write_text('[]')
        with self.assertRaises(ValueError): self.check(manifest=path)

    def test_manifest_target_outside_read_scope(self):
        outside = self.write(self.root / 'other.md', 'Ne jamais publier. Préserver les données.')
        path = self.manifest(destination=str(outside))
        with self.assertRaises(ValueError): self.check(manifest=path)

    def test_sources_unchanged_by_verification(self):
        expected = {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.check()
        self.assertEqual(expected, {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def cli(self, *extra):
        return subprocess.run([sys.executable, str(SCRIPT), '--before', str(self.before),
                               '--after', str(self.after), *extra], capture_output=True)

    def test_cli_success_exit(self):
        result = self.cli()
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)['status'], 'PRESERVED')

    def test_cli_loss_exit(self):
        self.write(self.after / 'target.md', 'Autre contenu.')
        self.assertEqual(self.cli().returncode, 1)

    def test_cli_invalid_input_exit(self):
        self.write(self.before / 'source.md', '')
        self.assertEqual(self.cli().returncode, 2)

    def test_cli_transformation_exit(self):
        path = self.manifest()
        self.write(self.after / 'target.md', 'Ne jamais publier. Préserver les données.')
        self.assertEqual(self.cli('--transformations', str(path)).returncode, 3)

    def test_ascii_console_does_not_hide_error(self):
        result = subprocess.run([sys.executable, str(SCRIPT), '--before', str(self.root / 'absent😀'),
                                 '--after', str(self.after)], capture_output=True,
                                 env={**os.environ, 'PYTHONIOENCODING':'ascii'})
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stdout)['status'], 'ERROR')

    def test_self_test(self):
        v.self_test()


if __name__ == '__main__':
    unittest.main()
