import os
import sys
import json
import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

workspace_dir = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
output_dir = os.path.join(workspace_dir, "Work_Brief")
gmail_api_dir = os.path.join(workspace_dir, "gmail_api")
token_path = os.path.join(gmail_api_dir, "token.json")

def download_attachments():
    creds = Credentials.from_authorized_user_file(token_path)
    service = build('gmail', 'v1', credentials=creds)

    msg_id = "19fd5d59a83fe64d"
    msg = service.users().messages().get(userId='me', id=msg_id, format='full').execute()

    parts = msg.get('payload', {}).get('parts', [])
    for p in parts:
        filename = p.get('filename')
        att_id = p.get('body', {}).get('attachmentId')
        if filename and att_id:
            att = service.users().messages().attachments().get(userId='me', messageId=msg_id, id=att_id).execute()
            data = att.get('data')
            file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))
            file_path = os.path.join(output_dir, filename)
            with open(file_path, 'wb') as f:
                f.write(file_data)
            print(f"Downloaded: {filename} ({len(file_data)} bytes) to {file_path}")

if __name__ == '__main__':
    download_attachments()
