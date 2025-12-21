from google_auth_oauthlib.flow import InstalledAppFlow

import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(override=True)

CREDENTIALS = Path(os.getenv("GOOGLE_CREDENTIALS_PATH", "client_secret_344257463423-0b1k8tlv6n8jcdvbj8e0j82b506md24q.apps.googleusercontent.com.json"))

SCOPES = ["https://www.googleapis.com/auth/calendar"]
flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS, SCOPES)
creds = flow.run_local_server(port=0)
with open("token.json", "w") as token:
    token.write(creds.to_json())
print("Token saved to token.json")
