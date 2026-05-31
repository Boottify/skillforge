#!/usr/bin/env python3
"""
Skillforge — Skill Manager for AI Coding Assistants

Browse, install, publish, and manage SKILL.md files across tools.
"""

import argparse
import json
import os
import sys
import shutil
from pathlib import Path

VERSION = "0.1.0"
SKILLFORGE_HOME = Path.home() / ".skillforge"
SKILLS_DIR = SKILLFORGE_HOME / "skills"

# ─── CLI ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        prog="skillforge",
        description="Skill manager for AI coding assistants"
    )
    parser.add_argument("--version", action="version", version=f"Skillforge {VERSION}")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("list", help="List installed skills")
    sub.add_parser("update", help="Update all installed skills")

    p = sub.add_parser("search", help="Search the skill registry")
    p.add_argument("query", nargs="?", help="Search query")

    p = sub.add_parser("install", help="Install a skill")
    p.add_argument("name", help="Skill name")

    p = sub.add_parser("create", help="Create a new skill from template")
    p.add_argument("name", help="Skill name")

    p = sub.add_parser("validate", help="Validate a skill")
    p.add_argument("name", help="Skill name")

    p = sub.add_parser("publish", help="Publish a skill to registry")
    p.add_argument("name", help="Skill name")

    p = sub.add_parser("remove", help="Remove an installed skill")
    p.add_argument("name", help="Skill name")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # Dispatch
    handlers = {
        "list": cmd_list,
        "search": cmd_search,
        "install": cmd_install,
        "create": cmd_create,
        "validate": cmd_validate,
        "publish": cmd_publish,
        "remove": cmd_remove,
        "update": cmd_update,
    }
    handlers[args.command](args)


# ─── Commands ───────────────────────────────────────────────────────────────

def cmd_list(args):
    """List all installed skills."""
    if not SKILLS_DIR.exists():
        print("No skills installed. Run 'skillforge install <name>' to get started.")
        return

    skills = sorted(SKILLS_DIR.iterdir())
    if not skills:
        print("No skills installed.")
        return

    print(f"\nInstalled skills ({len(skills)}):\n")
    for skill_dir in skills:
        if not skill_dir.is_dir():
            continue
        md = skill_dir / "SKILL.md"
        if md.exists():
            name = skill_dir.name
            desc = read_description(md)
            print(f"  {name}")
            if desc:
                print(f"    {desc}")
            print()


def cmd_search(args):
    """Search the skill registry."""
    query = args.query.lower() if args.query else ""
    print(f"Searching registry for: {query or '(all)'}")
    print("Registry coming soon — check skillforge.boottify.com\n")


def cmd_install(args):
    """Install a skill from the registry."""
    name = args.name
    skill_dir = SKILLS_DIR / name
    if skill_dir.exists():
        print(f"Skill '{name}' is already installed. Use 'skillforge update' to refresh.")
        return

    SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    skill_dir.mkdir()

    # Create default SKILL.md
    template = f"""---
name: {name}
description: Installed skill — add a description
version: 0.1.0
---

# {name}

## When to Use
- Add trigger conditions here

## Steps
1. First step

## Pitfalls
- None yet
"""
    (skill_dir / "SKILL.md").write_text(template)
    print(f"Installed '{name}' at {skill_dir}")


def cmd_create(args):
    """Create a new skill from template."""
    name = args.name
    skill_dir = Path.cwd() / name

    if skill_dir.exists():
        print(f"Directory '{name}' already exists.")
        return

    skill_dir.mkdir()
    template = f"""---
name: {name}
description: Describe what this skill does and when to use it
version: 0.1.0
tags: []
---

# {name}

## When to Use
- Trigger condition 1
- Trigger condition 2

## Prerequisites
- Requirement 1

## Steps
1. First step
2. Second step
3. Verify

## Pitfalls
- Common mistake to avoid

## Verification
- How to confirm it worked
"""
    (skill_dir / "SKILL.md").write_text(template)
    print(f"Created skill template at {skill_dir}/SKILL.md")
    print("Edit the file and use 'skillforge validate {name}' to check it.")


def cmd_validate(args):
    """Validate a skill's SKILL.md format."""
    name = args.name
    skill_dir = SKILLS_DIR / name
    if not skill_dir.exists():
        skill_dir = Path.cwd() / name

    md = skill_dir / "SKILL.md"
    if not md.exists():
        print(f"Error: No SKILL.md found in {skill_dir}")
        sys.exit(1)

    content = md.read_text()
    errors = []

    if not content.startswith("---"):
        errors.append("Missing YAML frontmatter (starts with ---)")

    if "name:" not in content[:200]:
        errors.append("Missing 'name' in frontmatter")

    if errors:
        print(f"Validation failed for {name}:")
        for e in errors:
            print(f"  ✗ {e}")
        sys.exit(1)

    print(f"✓ {name} is valid")


def cmd_publish(args):
    """Publish a skill to the registry."""
    name = args.name
    skill_dir = SKILLS_DIR / name
    if not skill_dir.exists():
        skill_dir = Path.cwd() / name

    if not (skill_dir / "SKILL.md").exists():
        print(f"Error: No skill found at {skill_dir}")
        sys.exit(1)

    print(f"Publishing '{name}'...")
    print("Registry publishing coming soon.")
    print("For now, submit a PR to github.com/Boottify/skillforge-registry")


def cmd_remove(args):
    """Remove an installed skill."""
    name = args.name
    skill_dir = SKILLS_DIR / name
    if not skill_dir.exists():
        print(f"Skill '{name}' is not installed.")
        return

    shutil.rmtree(skill_dir)
    print(f"Removed '{name}'")


def cmd_update(args):
    """Update all installed skills."""
    if not SKILLS_DIR.exists():
        print("No skills installed.")
        return

    skills = [d for d in SKILLS_DIR.iterdir() if d.is_dir()]
    print(f"Updating {len(skills)} skills...")
    print("Registry refresh coming soon.")


# ─── Helpers ────────────────────────────────────────────────────────────────

def read_description(md_path: Path) -> str:
    """Extract description from SKILL.md frontmatter."""
    try:
        content = md_path.read_text()
        for line in content.split("\n"):
            if line.startswith("description:"):
                return line.split(":", 1)[1].strip().strip('"')
    except Exception:
        pass
    return ""


if __name__ == "__main__":
    main()
