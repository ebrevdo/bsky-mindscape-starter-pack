import os
import sys

import requests

API_KEY = os.getenv(
    "BING_API_KEY"
)  # Launch with BING_API_KEY=your_key python find_bsky_users_via_bing.py
if not API_KEY:
    raise ValueError("BING_API_KEY environment variable not set")
ENDPOINT = "https://api.bing.microsoft.com/v7.0/search"


def search_bluesky_profile(name: str) -> str | None:
    query = f'"{name}" site:bsky.app'
    params = {
        "q": query,
        "textDecorations": True,
        "textFormat": "HTML",
    }
    headers = {"Ocp-Apim-Subscription-Key": API_KEY}

    response = requests.get(ENDPOINT, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    if "webPages" in search_results:
        for result in search_results["webPages"]["value"]:
            url = result["url"]
            if "bsky.app/profile/" in url and "post/" not in url:
                return url

    return None


# Read the guest names from stdin
guest_names = []
for line in sys.stdin:
    guest_names.append(line.strip())

for name in guest_names:
    profile = search_bluesky_profile(name)
    if not profile:
        print(f"{name}|")
    else:
        print(f"{name}|{profile}")
