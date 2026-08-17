import os
import sys
import json
import base64
from bs4 import BeautifulSoup
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

token_path = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace\gmail_api\token.json"
creds = Credentials.from_authorized_user_file(token_path, ['https://www.googleapis.com/auth/gmail.readonly'])
service = build('gmail', 'v1', credentials=creds)

msg_ids = ['19ff08dac3885de4', '19ff030337797d7c', '19fd5efab86aba2f']

def get_text_from_payload(payload):
    text = ""
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/html':
                html = base64.urlsafe_b64decode(part['body'].get('data', '')).decode('utf-8', errors='ignore')
                soup = BeautifulSoup(html, 'html.parser')
                text += soup.get_text('\n')
            elif part['mimeType'] == 'text/plain':
                text += base64.urlsafe_b64decode(part['body'].get('data', '')).decode('utf-8', errors='ignore')
    elif 'body' in payload:
        html = base64.urlsafe_b64decode(payload['body'].get('data', '')).decode('utf-8', errors='ignore')
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text('\n')
    return text

for mid in msg_ids:
    msg = service.users().messages().get(userId='me', id=mid, format='full').execute()
    headers = {h['name']: h['value'] for h in msg['payload']['headers']}
    print(f"📌 SUBJECT: {headers.get('Subject')}")
    print(f"FROM: {headers.get('From')}")
    print(f"DATE: {headers.get('Date')}")
    text = get_text_from_payload(msg['payload'])
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    print("TEXT CONTENT:")
    print('\n'.join(lines[:30]))
    print("=" * 80)
