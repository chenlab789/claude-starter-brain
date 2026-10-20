"""Fetch a YouTube transcript as plain text.

Usage:
    python get_transcript.py "<youtube-url-or-id>"

Requires:
    pip install youtube-transcript-api
"""
import sys
import re


def extract_video_id(s: str) -> str:
    """Accept a full URL or a bare 11-char video ID."""
    s = s.strip()
    # youtu.be/<id>  or  watch?v=<id>  or  /shorts/<id>  or  /embed/<id>
    m = re.search(r"(?:v=|youtu\.be/|/shorts/|/embed/)([A-Za-z0-9_-]{11})", s)
    if m:
        return m.group(1)
    # already an ID
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", s):
        return s
    raise ValueError(f"Could not find a video ID in: {s}")


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python get_transcript.py \"<youtube-url-or-id>\"")
        return 1

    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        print("Missing dependency. Run:  pip install youtube-transcript-api")
        return 1

    try:
        vid = extract_video_id(sys.argv[1])
    except ValueError as e:
        print(str(e))
        return 1

    langs = ["en", "en-US", "en-GB"]
    snippets = None

    # New API (youtube-transcript-api >= 1.0): instance .fetch() returning objects.
    try:
        api = YouTubeTranscriptApi()
        try:
            fetched = api.fetch(vid, languages=langs)
        except Exception:
            fetched = api.fetch(vid)  # any available language
        # FetchedTranscript is iterable of snippets with a .text attribute.
        snippets = [getattr(s, "text", "") for s in fetched]
    except Exception:
        # Old API (< 1.0): classmethod .get_transcript() returning dicts.
        try:
            get = getattr(YouTubeTranscriptApi, "get_transcript", None)
            if get is None:
                raise RuntimeError("get_transcript not available")
            try:
                chunks = get(vid, languages=langs)
            except Exception:
                chunks = get(vid)
            snippets = [c.get("text", "") for c in chunks]
        except Exception as e:
            print(f"No transcript available for this video. ({e})")
            return 1

    text = " ".join(s.replace("\n", " ") for s in snippets if s)
    if not text.strip():
        print("No transcript available for this video.")
        return 1
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
