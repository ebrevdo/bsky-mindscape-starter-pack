import getpass
import os

from atproto import Client

SESSION_FILE = os.path.expanduser("~/atproto_session.txt")

handle = input("Enter your handle (e.g., iamme.bsky.social) or email address: ")
# password should be silent when entered
password = getpass.getpass("Enter your password (it will not show to console): ")
sign_in_code = input("Enter your sign-in code (if emailed to you) [defafault: None]: ")
login_client = Client()
login_client.login(handle, password, auth_factor_token=sign_in_code or None)

with open(SESSION_FILE, "w") as f:
    f.write(login_client.export_session_string())
