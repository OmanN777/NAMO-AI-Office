import os
import sys
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE_DIR = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
TOKEN_DRIVE_PATH = os.path.join(WORKSPACE_DIR, "gmail_api", "token_drive.json")
FOLDER_NAME = "Malli_HQ_Knowledge_Base"

def sync():
    creds = Credentials.from_authorized_user_file(TOKEN_DRIVE_PATH)
    service = build('drive', 'v3', credentials=creds)

    print("Checking Google Drive folder...")
    query = f"name = '{FOLDER_NAME}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    res = service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
    files = res.get('files', [])

    if files:
        folder_id = files[0]['id']
        print(f"Using existing Drive folder: {FOLDER_NAME} (ID: {folder_id})")
    else:
        meta = {'name': FOLDER_NAME, 'mimeType': 'application/vnd.google-apps.folder'}
        folder = service.files().create(body=meta, fields='id').execute()
        folder_id = folder.get('id')
        print(f"Created new Drive folder: {FOLDER_NAME} (ID: {folder_id})")

    # Files to sync
    files_to_sync = [
        os.path.join(WORKSPACE_DIR, "Knowledge_Base", "Reports", "daily", "2026-08-29-malli-daily.md"),
        os.path.join(WORKSPACE_DIR, "Knowledge_Base", "Wiki", "case_studies", "crm_case_study.md"),
        os.path.join(WORKSPACE_DIR, "Knowledge_Base", "Wiki", "case_studies", "dell_ai_infrastructure_case_study.md"),
        os.path.join(WORKSPACE_DIR, "Knowledge_Base", "Wiki", "strategy", "boss_strategic_profile_2026.md")
    ]

    for fp in files_to_sync:
        if os.path.exists(fp):
            fn = os.path.basename(fp)
            q_file = f"name = '{fn}' and '{folder_id}' in parents and trashed = false"
            existing = service.files().list(q=q_file, spaces='drive', fields='files(id, name)').execute().get('files', [])
            media = MediaFileUpload(fp, resumable=True)
            if existing:
                fid = existing[0]['id']
                up = service.files().update(fileId=fid, media_body=media, fields='id, name, webViewLink').execute()
                print(f"✅ Updated: {fn} -> {up.get('webViewLink')}")
            else:
                fmeta = {'name': fn, 'parents': [folder_id]}
                cr = service.files().create(body=fmeta, media_body=media, fields='id, name, webViewLink').execute()
                print(f"✅ Uploaded: {fn} -> {cr.get('webViewLink')}")

    print("\n🎉 Google Drive Sync Completed 100%!")

if __name__ == '__main__':
    sync()
