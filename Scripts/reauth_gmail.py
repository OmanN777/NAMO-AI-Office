import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.compose'
]

workspace_dir = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
creds_path = os.path.join(workspace_dir, "gmail_api", "credentials.json")
token_path = os.path.join(workspace_dir, "gmail_api", "token.json")

def reauth():
    print("Opening browser for Gmail authentication...")
    flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
    creds = flow.run_local_server(port=0)
    with open(token_path, 'w') as token:
        token.write(creds.to_json())
    print("✅ Gmail API successfully authenticated and token saved!")

if __name__ == "__main__":
    reauth()
