import os
import sys
import json
import base64
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

token_path = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace\gmail_api\token.json"
creds = Credentials.from_authorized_user_file(token_path, ['https://www.googleapis.com/auth/gmail.readonly'])
service = build('gmail', 'v1', credentials=creds)

msg_ids = ['19ff08dac3885de4', '19ff030337797d7c', '19fd5efab86aba2f']

def get_body(payload):
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                data = part['body'].get('data', '')
                return base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')
            elif part['mimeType'] == 'text/html':
                data = part['body'].get('data', '')
                return base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')
    elif 'body' in payload:
        data = payload['body'].get('data', '')
        return base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')
    return ""

for mid in msg_ids:
    msg = service.users().messages().get(userId='me', id=mid, format='full').execute()
    headers = {h['name']: h['value'] for h in msg['payload']['headers']}
    subject = headers.get('Subject', '')
    sender = headers.get('From', '')
    date = headers.get('Date', '')
    body = get_body(msg['payload'])
    
    print(f"📌 SUBJECT: {subject}")
    print(f"FROM: {sender}")
    print(f"DATE: {date}")
    print("BODY PREVIEW:")
    print(body[:1500])
    print("=" * 80)
