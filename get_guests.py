import re
import sys

import feedparser

feed_url = "https://rss.art19.com/sean-carrolls-mindscape"
feed = feedparser.parse(feed_url)

guests = set()


_GUEST_NAME_SPLIT_RE = re.compile(r"(?:,| and )")

for entry in feed.entries:
    title = entry.title
    # Remove "Episode [number]: " prefix
    if " | " in title:
        parts = title.split(" | ", 1)
        if len(parts) != 2:
            continue
        parts = parts[1].split(" on ", 1)
        if len(parts) < 2:
            continue
        guest_names = parts[0]
        for guest_name in _GUEST_NAME_SPLIT_RE.split(guest_names):
            guest_name = guest_name.strip()
            if guest_name.count(" ") >= 4:
                print("Skipping:", guest_name, file=sys.stderr)
            else:
                guests.add(guest_name)
    else:
        # Handle special cases or older episodes if necessary
        continue

for guest in sorted(guests):
    print(guest)
