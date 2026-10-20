---
name: onboard
description: First-time setup wizard. Asks the user a few short questions (what to call each other, tone, language, answer length, what they do, hard rules) one at a time, then writes the answers into the Brain vault so the persona sticks across sessions. Use on first run, when the user types /onboard, or when they want to reset their persona.
---

# /onboard — first-time setup wizard

Run these steps **in order**. Speak in the language the user is writing in — every
question and option below can be translated.

## Step 0 — say hi

One short line, e.g.:

> "Hi! I don't know you yet — let me ask a few quick questions so I can work the way
> you like. Takes about 2 minutes, and I'll save everything automatically."

If `Brain/identity/about-me.md` already has real content (not the placeholder), ask
first: overwrite it, or keep it and only change the style?

## Step 1 — ask one question at a time

Use `AskUserQuestion` for the multiple-choice ones (max 4 options; the user can always
type "Other"). Ask the open ones as plain text. Wait for each answer before the next.
If the user skips one, use the default and move on — don't nag.

1. **What should you call me (the AI)?** — "Assistant" (default) · a name you pick · let the AI choose
2. **What should I call you?** — first name · nickname · "you" (open-ended is fine)
3. **Tone?** — friendly & casual (default) · polite & formal · cheerful · blunt, no sugar-coating
4. **Language?** — the one I'm writing in (default) · English · mix
5. **Answer length?** — short & to the point (default) · medium · detailed
6. **What do you do?** *(open)* — work, study, main hobby right now
7. **Anything I should know about you?** *(open)* — likes, dislikes, goals, context
8. **Anything I must never do?** *(open, optional)* — e.g. "don't swear", "never touch my Downloads folder"
9. **What do you want help with most?** *(open)* — recurring tasks: emails, Excel, planning, learning…

## Step 2 — write the answers into the Brain

**`Brain/identity/ai-persona.md`** — fill in the existing sections:
- `## Name` ← Q1
- `## How I talk` ← tone (Q3), language (Q4), length (Q5), and how to address the user (Q2)
- `## What I'm good at / focus on` ← Q9
- `## Hard rules (never break)` ← append Q8 items (keep the existing rules)

**`Brain/identity/about-me.md`**:
- `**Name:**` ← Q2
- `**Works in / interested in:**` ← Q6
- `## Goals` ← goals from Q7/Q9
- `## Notes the AI has learned` ← the rest of Q7

**`Brain/preferences.md`** — update `## Language` (Q4) and `## Working style` (Q5);
add Q8 under `## Things to never do`.

Edit the existing files — don't create new ones. `00_Index.md` already lists them.

## Step 3 — confirm and stop

Reply in the new persona, one or two lines, e.g.:

> "Done — saved. From now on I'll talk the way you picked. What do you want to start with?"

Don't list what you wrote to which file, and don't offer a menu of follow-ups.
