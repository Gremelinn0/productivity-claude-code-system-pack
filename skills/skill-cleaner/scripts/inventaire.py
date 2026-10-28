#!/usr/bin/env python3
"""Inventaire portable des compétences actives d'un ou plusieurs dossiers."""
import argparse
import json
import tempfile
from pathlib import Path


def _meta(path):
    text = path.read_text(encoding="utf-8-sig")
    if not text.startswith("---\n"):
        return {}, ["frontmatter absent"]
    end = text.find("\n---", 4)
    if end < 0:
        return {}, ["frontmatter non terminé"]
    raw = text[4:end]
    meta = {}
    for line in raw.splitlines():
        if line and not line[0].isspace() and ":" in line:
            key, value = line.split(":", 1)
            meta[key.strip()] = value.strip()
    errors = []
    if not meta.get("name"):
        errors.append("name absent")
    if "description" not in meta:
        errors.append("description absente")
    return meta, errors


def inventory(roots):
    items = []
    for root in roots:
        root = Path(root).resolve()
        for p in sorted(root.glob("*/SKILL.md")):
            if p.parent.name.startswith("."):
                continue
            meta, errors = _meta(p)
            text = p.read_text(encoding="utf-8-sig")
            refs = sorted(set(
                part for part in text.split("references/")
                [1:] if part
            ))
            missing = []
            for ref in refs:
                name = ref.split()[0].split(")")[0].split("]")[0].strip("'\"`")
                if name.endswith(".md") and not (p.parent / "references" / name).is_file():
                    missing.append(name)
            items.append({
                "root": str(root),
                "skill": p.parent.name,
                "declared_name": meta.get("name"),
                "lines": len(text.splitlines()),
                "errors": errors,
                "references_missing": sorted(set(missing)),
            })
    return items


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("roots", nargs="*", default=["skills"])
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)
    if args.self_test:
        with tempfile.TemporaryDirectory() as tmp:
            good = Path(tmp) / "sample"
            good.mkdir()
            (good / "SKILL.md").write_text(
                "---\nname: sample\ndescription: Test\n---\n# Sample\n",
                encoding="utf-8")
            found = inventory([tmp])
            assert len(found) == 1 and not found[0]["errors"], found
            print("self-test: OK")
        return 0
    data = inventory(args.roots)
    if args.json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        for row in data:
            print(f"{row['skill']}: {row['lines']} lignes ; "
                  f"{len(row['errors'])} défaut(s) de métadonnées ; "
                  f"{len(row['references_missing'])} référence(s) absente(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
