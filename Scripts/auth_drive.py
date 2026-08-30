import os
import sys
import webbrowser
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

def authenticate():
    print("Starting Google Drive OAuth Flow with dynamic port...")
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
    # Use standard run_local_server which handles state matching seamlessly
    creds = flow.run_local_server(port=0, open_browser=True, prompt='consent')
    with open(TOKEN_DRIVE_PATH, 'w', encoding='utf-8') as f:
        f.write(creds.to_json())
    print("SUCCESS: Google Drive token successfully saved to token_drive.json!")

if __name__ == '__main__':
    authenticate()
