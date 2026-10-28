#!/usr/bin/env python3
"""Contrôles documentaires du pack (ne remplace pas les essais Claude Code)."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
NAMES = (
    "capitaliser", "clean-rules-cleanup", "optimise-systeme",
    "skill-cleaner", "skill-quality-guard", "propage-systeme",
    "router-entretien-systeme",
)
REQUIRED = {
    "skill-quality-guard": ("fabriquer", "refondre", "vérifier", "resynchroniser", "skill-creator"),
    "optimise-systeme": ("skill-cleaner", "capitaliser", "propage-systeme"),
    "clean-rules-cleanup": ("gerer-les-hooks.md", "skill-cleaner"),
    "router-entretien-systeme": ("skill-cleaner", "optimise-systeme"),
}
issues = []
for name in NAMES:
    skill = ROOT / "skills" / name / "SKILL.md"
    if not skill.exists():
        issues.append(f"{name}: SKILL.md absent")
        continue
    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        issues.append(f"{name}: début de frontmatter absent")
    if not re.search(r"(?m)^name:\s*" + re.escape(name) + r"\s*$", text):
        issues.append(f"{name}: name incorrect")
    if not re.search(r"(?m)^description:\s*(?:>-)?", text):
        issues.append(f"{name}: description absente")
    for word in REQUIRED.get(name, ()):
        if word not in text:
            issues.append(f"{name}: responsabilité ou route manquante : {word}")
    for ref in set(re.findall(r"references/([\w-]+\.md)", text)):
        if not (skill.parent / "references" / ref).is_file():
            issues.append(f"{name}: référence absente : {ref}")

for path in (
    "skills/skill-quality-guard/references/fabriquer-une-competence.md",
    "skills/skill-quality-guard/references/refondre-une-competence.md",
    "skills/skill-quality-guard/references/resynchroniser-une-copie-publiee.md",
    "skills/clean-rules-cleanup/references/gerer-les-hooks.md",
    "docs/contrat-capacites.md",
    "skills/skill-cleaner/scripts/inventaire.py",
):
    if not (ROOT / path).is_file():
        issues.append(f"fichier manquant : {path}")

script = ROOT / "skills/skill-cleaner/scripts/inventaire.py"
if script.is_file():
    try:
        compile(script.read_text(encoding="utf-8"), str(script), "exec")
    except SyntaxError as exc:
        issues.append(f"inventaire.py: erreur de syntaxe : {exc}")

if issues:
    print("\n".join("ERREUR " + problem for problem in issues))
    raise SystemExit(1)
print("Pack : présence, références et contrats essentiels vérifiés.")
print("Restent à tester : installation, appels à Anthropic et scénarios de comportement.")
