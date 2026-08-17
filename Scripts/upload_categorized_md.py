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
token_path = os.path.join(workspace_dir, "gmail_api", "token.json")
temp_dir = r"C:\Users\namo_\Downloads\NotebookLM_Categorized"

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

def create_drive_folder(service, folder_name):
    file_metadata = {
        'name': folder_name,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    file = service.files().create(body=file_metadata, fields='id').execute()
    return file.get('id')

def main():
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
        
    print("Grouping Markdown files by category...")
    
    # 1. Group files by top-level directory
    categories = {}
    for item in os.listdir(kb_dir):
        item_path = os.path.join(kb_dir, item)
        if os.path.isdir(item_path):
            categories[item] = []
            for root, _, files in os.walk(item_path):
                for file in files:
                    if file.endswith(".md"):
                        categories[item].append(os.path.join(root, file))
    
    # Also grab MD files in the root of Knowledge_Base if any
    categories["Root_Knowledge"] = []
    for file in os.listdir(kb_dir):
        if file.endswith(".md") and os.path.isfile(os.path.join(kb_dir, file)):
            categories["Root_Knowledge"].append(os.path.join(kb_dir, file))
            
    # 2. Combine and format
    creds = get_credentials()
    service = build('drive', 'v3', credentials=creds)
    
    folder_id = create_drive_folder(service, 'Antigravity_NotebookLM_Sources')
    print(f"Created Google Drive Folder 'Antigravity_NotebookLM_Sources' (ID: {folder_id})")
    
    for category, files in categories.items():
        if not files:
            continue
            
        out_filename = f"KB_{category}.md"
        out_filepath = os.path.join(temp_dir, out_filename)
        
        print(f"Generating {out_filename} ({len(files)} files)...")
        with open(out_filepath, 'w', encoding='utf-8') as outfile:
            outfile.write(f"# {category.replace('_', ' ')} Knowledge Base\n\n")
            
            for filepath in files:
                rel_path = os.path.relpath(filepath, kb_dir)
                filename = os.path.basename(filepath)
                # Clean Markdown Header for NotebookLM
                outfile.write(f"\n\n## Source Document: {filename}\n")
                outfile.write(f"**Path:** `{rel_path}`\n\n")
                
                try:
                    with open(filepath, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        # Simple cleanup of empty lines
                        outfile.write(content.strip() + "\n")
                except Exception as e:
                    outfile.write(f"> Error reading file: {e}\n")
                    
        # 3. Upload to Google Drive folder
        print(f"Uploading {out_filename} to Drive...")
        file_metadata = {
            'name': out_filename,
            'parents': [folder_id]
        }
        media = MediaFileUpload(out_filepath, mimetype='text/markdown', resumable=True)
        service.files().create(body=file_metadata, media_body=media, fields='id').execute()

    print("✅ All categories uploaded successfully!")

if __name__ == '__main__':
    main()
