import os
import sys
import json
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

workspace_dir = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
kb_dir = os.path.join(workspace_dir, "Knowledge_Base")
credentials_path = os.path.join(workspace_dir, "gmail_api", "credentials.json")
token_path = os.path.join(workspace_dir, "gmail_api", "token.json")
combined_md_path = r"C:\Users\namo_\Downloads\Antigravity_Knowledge_Base.md"

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file'
]

def get_credentials():
    creds = None
    if os.path.exists(token_path):
        with open(token_path, 'r', encoding='utf-8') as f:
            token_data = json.load(f)
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
    return creds

def combine_markdown():
    print("Combining all Markdown files...")
    with open(combined_md_path, 'w', encoding='utf-8') as outfile:
        outfile.write("# Antigravity Office Knowledge Base\n\n")
        
        for root, dirs, files in os.walk(kb_dir):
            for file in files:
                if file.endswith(".md"):
                    filepath = os.path.join(root, file)
                    rel_path = os.path.relpath(filepath, kb_dir)
                    outfile.write(f"\n\n---\n## File: {rel_path}\n---\n\n")
                    try:
                        with open(filepath, 'r', encoding='utf-8') as infile:
                            outfile.write(infile.read())
                    except Exception as e:
                        print(f"Skipping {filepath} due to encoding issue: {e}")
    print(f"Combined file saved to {combined_md_path}")

def upload_file():
    print("Authenticating with Google Drive...")
    creds = get_credentials()
    service = build('drive', 'v3', credentials=creds)
    
    print("Uploading Antigravity_Knowledge_Base.md to Google Drive...")
    file_metadata = {'name': 'Antigravity_Knowledge_Base.md'}
    media = MediaFileUpload(combined_md_path, mimetype='text/markdown', resumable=True)
    
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"Upload Complete! File ID: {file.get('id')}")

if __name__ == '__main__':
    combine_markdown()
    upload_file()
