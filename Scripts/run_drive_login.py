import os
import sys
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

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
FOLDER_NAME = "Malli_HQ_Knowledge_Base"

def run():
    print("==================================================")
    print("Malli Google Drive Authorization Engine")
    print("==================================================")
    
    flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
    creds = flow.run_local_server(port=0, open_browser=True, prompt='consent')
    
    with open(TOKEN_DRIVE_PATH, 'w', encoding='utf-8') as f:
        f.write(creds.to_json())
    print("\n[SUCCESS] Token saved to token_drive.json!")
    
    # Sync now
    service = build('drive', 'v3', credentials=creds)
    query = f"name = '{FOLDER_NAME}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    res = service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
    files = res.get('files', [])
    if files:
        folder_id = files[0]['id']
        print(f"[DRIVE] Found folder: {FOLDER_NAME} (ID: {folder_id})")
    else:
        meta = {'name': FOLDER_NAME, 'mimeType': 'application/vnd.google-apps.folder'}
        folder = service.files().create(body=meta, fields='id').execute()
        folder_id = folder.get('id')
        print(f"[DRIVE] Created new folder: {FOLDER_NAME} (ID: {folder_id})")
        
    test_file = os.path.join(WORKSPACE_DIR, "Knowledge_Base", "Reports", "daily", "2026-08-29-malli-daily.md")
    if os.path.exists(test_file):
        fn = os.path.basename(test_file)
        media = MediaFileUpload(test_file, resumable=True)
        fmeta = {'name': fn, 'parents': [folder_id]}
        cr = service.files().create(body=fmeta, media_body=media, fields='id, name, webViewLink').execute()
        print(f"[DRIVE] Uploaded '{fn}' -> {cr.get('webViewLink')}")
        
    print("\n[ALL DONE] Knowledge Base successfully linked to Google Drive!")
    input("\nPress Enter to close window...")

if __name__ == '__main__':
    run()
