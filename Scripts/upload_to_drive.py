import os
import sys
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

workspace_dir = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
credentials_path = os.path.join(workspace_dir, "gmail_api", "credentials.json")
token_path = os.path.join(workspace_dir, "gmail_api", "token.json")
zip_path = r"C:\Users\namo_\Downloads\NotebookLM_Knowledge.zip"

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file'
]

def get_credentials():
    creds = None
    if os.path.exists(token_path):
        try:
            with open(token_path, 'r', encoding='utf-8') as f:
                token_data = json.load(f)
                token_scopes = token_data.get('scopes', [])
            # Skip strict scope check to allow drive.file
            creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        except Exception as e:
            print(f"Failed to load cached token: {e}")
            
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print("Credentials missing or completely invalid. Cannot proceed without user auth.")
            sys.exit(1)
            
    return creds

def upload_zip():
    print("Authenticating with Google Drive...")
    creds = get_credentials()
    service = build('drive', 'v3', credentials=creds)
    
    print("Uploading NotebookLM_Knowledge.zip to Google Drive...")
    file_metadata = {'name': 'NotebookLM_Knowledge.zip'}
    media = MediaFileUpload(zip_path, mimetype='application/zip', resumable=True)
    
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"Upload Complete! File ID: {file.get('id')}")

if __name__ == '__main__':
    upload_zip()
