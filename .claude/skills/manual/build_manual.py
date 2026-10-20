"""Scan installed Claude Code skills and generate a friendly manual.html.

Usage:
    python .claude/skills/manual/build_manual.py

Run from the project root (the folder that contains the .claude directory).
"""
import os
import re
import glob
import html


def parse_frontmatter(path: str):
    """Return (name, description) from a SKILL.md YAML frontmatter block."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    except OSError:
        return None, None

    m = re.search(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    block = m.group(1) if m else text

    def field(key):
        fm = re.search(rf"^{key}\s*:\s*(.+)$", block, re.MULTILINE)
        return fm.group(1).strip().strip('"').strip("'") if fm else None

    name = field("name")
    desc = field("description")
    # Fallback: use folder name if no `name:` field.
    if not name:
        name = os.path.basename(os.path.dirname(path))
    return name, desc or "(no description)"


def main():
    root = os.getcwd()
    skill_files = sorted(glob.glob(os.path.join(root, ".claude", "skills", "*", "SKILL.md")))

    skills = []
    for path in skill_files:
        name, desc = parse_frontmatter(path)
        if name:
            skills.append((name, desc))

    cards = "\n".join(
        f"""    <div class="card">
      <h2>{html.escape(name)}</h2>
      <p>{html.escape(desc)}</p>
    </div>"""
        for name, desc in skills
    )

    if not cards:
        cards = '    <p class="muted">No skills found in .claude/skills/</p>'

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Your AI — Manual</title>
<style>
  body {{ margin:0; background:#0b0f0d; color:#e8eee9;
         font-family:-apple-system,Segoe UI,Roboto,sans-serif; padding:40px 20px; }}
  .wrap {{ max-width:820px; margin:0 auto; }}
  h1 {{ font-size:2rem; margin:0 0 6px; }}
  .sub {{ color:#7fae93; margin:0 0 32px; }}
  .card {{ background:#121a16; border:1px solid #1f2e26; border-radius:14px;
          padding:18px 20px; margin-bottom:14px; }}
  .card h2 {{ margin:0 0 6px; font-size:1.15rem; color:#34d399; }}
  .card p {{ margin:0; color:#c4d2c9; line-height:1.55; }}
  .muted {{ color:#6b7d72; }}
  footer {{ margin-top:36px; color:#5c6b61; font-size:.85rem; }}
</style>
</head>
<body>
  <div class="wrap">
    <h1>🤖 Your AI Assistant — What It Can Do</h1>
    <p class="sub">{len(skills)} skill(s) installed. This page is generated from the
    AI's own skills, so it's always up to date.</p>
{cards}
    <footer>Regenerate any time with:
      <code>python .claude/skills/manual/build_manual.py</code></footer>
  </div>
</body>
</html>"""

    out = os.path.join(root, "manual.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"Wrote {out} ({len(skills)} skills)")


if __name__ == "__main__":
    main()
