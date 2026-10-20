---
name: manual
description: Scan the AI's own installed skills and generate a friendly HTML manual the user can open in a browser. Use when the user asks "what can you do?", "make me a manual", or after adding new skills.
---

# Self-Documenting Manual

Your AI can read its own skills and write a human-friendly manual. This means the
manual never goes out of date — regenerate it any time you add a skill.

## How to use
1. Run the generator:
   ```
   python .claude/skills/manual/build_manual.py
   ```
   It scans every `.claude/skills/*/SKILL.md`, reads each skill's name and
   description, and writes `manual.html` in the project root.
2. Tell the user to open `manual.html` in their browser.

## Make it better (optional)
After generating, you can hand-improve the descriptions in the HTML to be friendlier
or add examples — you understand the skills, so write the explanations a beginner
would actually get. Re-run the script any time to regenerate the base.

## Remember
If you add or change skills often, mention in `Brain/projects/` that the
manual should be regenerated, so it stays current.
