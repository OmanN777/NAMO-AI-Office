import os
import sys
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Combined Scopes for Gmail + Drive + Sheets
SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.compose',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]

workspace_dir = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
creds_path = os.path.join(workspace_dir, "gmail_api", "credentials.json")
token_path = os.path.join(workspace_dir, "gmail_api", "token_drive.json")

def reauth_all():
    print("==================================================")
    print("Malli Google Unified Authorization (Gmail + Drive)")
    print("==================================================")
    print("Opening browser for authentication...")
    
    flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
    creds = flow.run_local_server(port=0, prompt='select_account consent')
    
    with open(token_path, 'w', encoding='utf-8') as token:
        token.write(creds.to_json())
    print("\n✅ Google Drive & Gmail API successfully authorized!")
    print(f"Token saved to: {token_path}")
    input("\nPress Enter to close...")

if __name__ == "__main__":
    reauth_all()
