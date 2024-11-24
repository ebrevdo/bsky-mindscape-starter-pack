import sys

import requests

# from atproto_client.client.session import Session

# SESSION_FILE = os.path.expanduser("~/atproto_session.txt")
# if not os.path.exists(SESSION_FILE):
#     raise RuntimeError(f"First run python login_atproto.py to create {SESSION_FILE}")

# with open(SESSION_FILE, "r") as f:
#     session_string = f.read()

# session = Session.decode(session_string)
# api_token = session.access_jwt

# url = "https://bsky.social/xrpc/app.bsky.actor.searchActors"
# headers = {"Authorization": f"Bearer {api_token}", "Content-Type": "application/json"}
url = "https://public.api.bsky.app./xrpc/app.bsky.actor.searchActors"
headers = {"Content-Type": "application/json"}

for name in sys.stdin:
    name = name.strip()
    params = {"q": name}
    response = requests.get(url, params=params, headers=headers)
    if response.status_code == 200:
        results = response.json().get("actors", [])
        if results:
            print(f"{name} | https://bsky.app/profile/{results[0]['handle']}")
            continue
    print(f"{name} |")
