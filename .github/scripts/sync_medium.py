"""
Fetches posts from a Medium RSS feed and writes them as Jekyll-compatible
Markdown files in _posts/. Skips posts already synced (by URL or title match).
"""

import feedparser
import html2text
import os
import re
import glob
from datetime import datetime, timezone

MEDIUM_USERNAME = "nityaakalra5"
FEED_URL = f"https://medium.com/feed/@{MEDIUM_USERNAME}"
POSTS_DIR = "_posts"


def slugify(title):
    title = title.lower()
    title = re.sub(r"[^\w\s-]", "", title)
    title = re.sub(r"[\s_]+", "-", title)
    title = re.sub(r"-{2,}", "-", title)
    title = title.strip("-")
    return title[:60]


def load_existing_metadata():
    """Return sets of already-synced Medium URLs and normalised titles."""
    synced_urls = set()
    synced_titles = set()
    for filepath in glob.glob(f"{POSTS_DIR}/*.md"):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        m = re.search(r"^medium_url:\s*\"?(.+?)\"?\s*$", content, re.MULTILINE)
        if m:
            synced_urls.add(m.group(1).strip())
        m = re.search(r"^title:\s*\"?(.+?)\"?\s*$", content, re.MULTILINE)
        if m:
            synced_titles.add(m.group(1).strip().lower())
    return synced_urls, synced_titles


def escape_yaml_string(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def main():
    print(f"Fetching feed: {FEED_URL}")
    feed = feedparser.parse(FEED_URL)

    if feed.bozo and not feed.entries:
        raise RuntimeError(f"Failed to parse feed: {feed.bozo_exception}")

    print(f"Found {len(feed.entries)} entries in feed.")

    os.makedirs(POSTS_DIR, exist_ok=True)
    synced_urls, synced_titles = load_existing_metadata()

    converter = html2text.HTML2Text()
    converter.ignore_links = False
    converter.ignore_images = False
    converter.body_width = 0
    converter.protect_links = True

    new_count = 0
    for entry in feed.entries:
        post_url = entry.link.strip()
        title = entry.title.strip()
        title_lower = title.lower()

        if post_url in synced_urls:
            print(f"  skip (url match):   {title}")
            continue
        if title_lower in synced_titles:
            print(f"  skip (title match): {title}")
            continue

        # Parse publish date
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            pub_dt = datetime(*entry.published_parsed[:6], tzinfo=timezone.utc)
        else:
            pub_dt = datetime.now(timezone.utc)
        date_str = pub_dt.strftime("%Y-%m-%d")

        slug = slugify(title)
        filename = f"{date_str}-{slug}.md"
        filepath = os.path.join(POSTS_DIR, filename)

        # Avoid overwriting a manually created file with the same slug
        if os.path.exists(filepath):
            print(f"  skip (file exists): {filename}")
            continue

        # Extract tags from Medium
        raw_tags = [t.term for t in entry.get("tags", [])]
        # Medium sometimes adds the username as a tag — filter it out
        tags = [t for t in raw_tags if t.lower() != MEDIUM_USERNAME.lower()]

        # Convert HTML content to Markdown
        if hasattr(entry, "content") and entry.content:
            html_body = entry.content[0].value
        else:
            html_body = entry.get("summary", "")
        markdown_body = converter.handle(html_body).strip()

        # Build YAML frontmatter
        tag_lines = "\n".join(f'  - "{escape_yaml_string(t)}"' for t in tags) if tags else '  - "blog"'
        frontmatter = (
            f'---\n'
            f'title: "{escape_yaml_string(title)}"\n'
            f'date: {date_str}\n'
            f'categories:\n'
            f'  - blog\n'
            f'tags:\n'
            f'{tag_lines}\n'
            f'medium_url: "{post_url}"\n'
            f'---\n\n'
        )

        origin_line = f'_Originally published on [Medium]({post_url})._\n\n'

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter + origin_line + markdown_body + "\n")

        print(f"  created: {filename}")
        new_count += 1

    print(f"\nDone. {new_count} new post(s) created.")


if __name__ == "__main__":
    main()
