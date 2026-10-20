# Claude Starter Brain

**A ready-made memory for Claude Code.** Clone the folder, start `claude` inside it, and your assistant remembers who you are, how you like to work, and every mistake it already made, across every session. That memory is a plain Markdown vault you can open in Obsidian and read yourself.

[ภาษาไทย](README.th.md)

Made for people who are new to AI agents. No coding needed, setup takes about 10 minutes.

## What you get

- **Memory that sticks.** `CLAUDE.md` tells Claude to read `Brain/00_Index.md` at the start of every session and to write anything worth keeping back into the vault: one topic per file, linked with `[[ ]]`, always listed in the index
- **It learns from its errors.** When something breaks, Claude logs what happened, the root cause and the fix in `Brain/lessons/`, then reads those lessons first next time
- **`/onboard` wizard.** About 9 quick questions (what to call each other, tone, language, answer length, what you do, hard rules) and the answers go straight into the vault
- **Obsidian-friendly.** Open `Brain/` as a vault and Graph View shows how your AI's knowledge connects, updating as it learns
- **4 starter skills:**
  - `/onboard`: setup wizard
  - `youtube`: paste a link to get the transcript and a summary, optionally saved to the vault
  - `notebooklm`: use Google NotebookLM for notebooks and audio podcasts
  - `manual`: Claude scans its own skills and builds `manual.html`, so the "what can you do?" page never goes stale
- **Safe defaults.** Claude says its plan before big changes, asks before deleting or overwriting, never commits secrets and sticks to what you asked for

## Layout

```
claude-starter-brain/
├── CLAUDE.md              ← the rulebook Claude reads every session
├── .claude/skills/        ← onboard, youtube, notebooklm, manual
└── Brain/                 ← the memory (an Obsidian vault)
    ├── 00_Index.md        ← table of contents, read first every session
    ├── identity/          ← ai-persona.md (the AI), about-me.md (you)
    ├── preferences.md
    ├── knowledge/         ← facts, one topic per file
    ├── lessons/           ← errors and their fixes
    └── projects/          ← ongoing work
```

## Setup

1. Install [Claude Code](https://docs.claude.com/en/docs/claude-code): `npm install -g @anthropic-ai/claude-code`
2. Get the folder and keep it somewhere permanent (not Downloads):
   ```
   git clone https://github.com/chenlab789/claude-starter-brain.git
   cd claude-starter-brain
   ```
   No git? Use **Code → Download ZIP** and unzip it.
3. Start Claude **inside the folder**. That's what makes it read `CLAUDE.md`:
   ```
   claude
   ```
4. Type `/onboard` and answer the questions.
5. *(Optional)* Install [Obsidian](https://obsidian.md), choose **Open folder as vault** and pick `Brain/`.
6. *(Optional)* For the YouTube skill: `pip install youtube-transcript-api`

## Try it

- *"Read your index and tell me what you know so far."*
- *"I prefer bullet points over paragraphs. Remember that."* Then check `Brain/preferences.md`
- *"What can you do?"* Claude regenerates `manual.html` for you to open

## Customize

Everything is plain Markdown. Edit `Brain/identity/ai-persona.md` to change the personality, or just tell Claude *"from now on, talk like X"* and it updates the file itself. Add your own skills under `.claude/skills/<name>/SKILL.md` and they show up in the manual.

## License

MIT
