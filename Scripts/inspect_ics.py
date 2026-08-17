import os
import sys
import json
import base64

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

token_path = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace\gmail_api\token.json"
creds = Credentials.from_authorized_user_file(token_path, ['https://www.googleapis.com/auth/gmail.readonly'])
service = build('gmail', 'v1', credentials=creds)

msg = service.users().messages().get(userId='me', id='19ff08dac3885de4', format='full').execute()

def find_parts(part):
    mime = part.get('mimeType', '')
    body = part.get('body', {})
    print(f"MIME: {mime}, BodyKeys: {list(body.keys())}")
    if 'attachmentId' in body:
        att = service.users().messages().attachments().get(userId='me', messageId='19ff08dac3885de4', id=body['attachmentId']).execute()
        data = base64.urlsafe_b64decode(att['data']).decode('utf-8', errors='ignore')
        print("--- ATTACHMENT CONTENT ---")
        for line in data.split('\n'):
            if any(k in line for k in ['DTSTART', 'DTEND', 'SUMMARY', 'LOCATION']):
                print(line.strip())
    if 'parts' in part:
        for p in part['parts']:
            find_parts(p)

find_parts(msg['payload'])
