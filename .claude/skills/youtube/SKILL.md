---
name: youtube
description: Pull the transcript from a YouTube video, then summarize it or extract key points. Use when the user shares a YouTube link and wants a summary, notes, or to "learn from this video".
---

# YouTube Transcript & Summary

Turn any YouTube video into text you can read, summarize, or save to the brain.

## Setup (one time)
Install the transcript library:
```
pip install youtube-transcript-api
```

## How to use
1. Get the video URL or ID from the user.
2. Run the helper script to fetch the transcript:
   ```
   python .claude/skills/youtube/get_transcript.py "<youtube-url-or-id>"
   ```
   It prints the full transcript text.
3. Read the transcript and do what the user asked:
   - **Summarize** — give the main points concisely.
   - **Extract lessons** — pull out actionable takeaways.
4. **If it's worth remembering**, save a note in `Brain/knowledge/` (one
   file, kebab-case name) and add a line to `Brain/00_Index.md`. Link it with
   `[[ ]]` to anything related.

## Notes
- If a video has no transcript/captions, the script will say so — tell the user.
- For long transcripts, summarize in sections rather than dumping the whole thing.
