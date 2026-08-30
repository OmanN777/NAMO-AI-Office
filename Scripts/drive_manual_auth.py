import os
import sys
import json
from google_auth_oauthlib.flow import InstalledAppFlow

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

SCOPES = [
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]

WORKSPACE_DIR = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
GMAIL_API_DIR = os.path.join(WORKSPACE_DIR, "gmail_api")
CREDENTIALS_PATH = os.path.join(GMAIL_API_DIR, "credentials.json")
TOKEN_DRIVE_PATH = os.path.join(GMAIL_API_DIR, "token_drive.json")

print("Google Drive Authorization Engine (Manual Code Paste)")
flow = InstalledAppFlow.from_client_secrets_file(
    CREDENTIALS_PATH,
    SCOPES,
    redirect_uri="urn:ietf:wg:oauth:2.0:oob"
)
auth_url, _ = flow.authorization_url(prompt="consent", access_type="offline")
print("\n=======================================================")
print("1. Open this URL in your browser:")
print(auth_url)
print("=======================================================\n")

code = input("2. Paste the Google Authorization Code here: ").strip()

flow.fetch_token(code=code)
creds = flow.credentials
with open(TOKEN_DRIVE_PATH, 'w', encoding='utf-8') as f:
    f.write(creds.to_json())
    
print("\n[SUCCESS] Google Drive token saved successfully!")
input("Press Enter to close...")
