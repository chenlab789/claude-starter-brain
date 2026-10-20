---
name: notebooklm
description: Use Google NotebookLM to turn documents into a queryable knowledge base or an audio podcast. Use when the user wants to "make a podcast about X", build a notebook from sources, or ask questions across a set of documents.
---

# NotebookLM

[NotebookLM](https://notebooklm.google.com) is a free Google tool that turns your
documents into an AI you can ask questions, and can even generate an audio "podcast"
discussion of your sources. Great for studying or digesting lots of material.

## The simple way (no setup)
Just use the website: https://notebooklm.google.com
1. Create a new notebook.
2. Upload sources (PDFs, Google Docs, pasted text, YouTube links, websites).
3. Ask questions, or click **Audio Overview** to generate a podcast.

For most people, the website is enough. Use it directly.

## The power way (drive it from the command line)
If you want your AI to create notebooks and add sources programmatically, there's a
community tool called `notebooklm-py`. This is optional and more advanced:
```
pip install notebooklm-py
```
You'll need to log in with your Google account once. After that you can create
notebooks, add sources, and generate podcasts from the terminal.

> Heads up: this is an unofficial tool, so Google changing their site can break it.
> If a command fails, fall back to the website above and log the issue in
> `Brain/lessons/`.

## Remember what you build
When you create a notebook for an ongoing topic, save a note in
`Brain/projects/` with the notebook's purpose and link, and add it to
`Brain/00_Index.md`.
