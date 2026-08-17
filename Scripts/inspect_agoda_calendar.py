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

results = service.users().messages().list(userId='me', q='agoda', maxResults=15).execute()
messages = results.get('messages', [])

for m in messages:
    msg = service.users().messages().get(userId='me', id=m['id'], format='full').execute()
    headers = {h['name']: h['value'] for h in msg['payload']['headers']}
    subj = headers.get('Subject', '')
    sender = headers.get('From', '')
    date = headers.get('Date', '')
    print(f"ID: {m['id']} | Subject: {subj} | From: {sender} | Date: {date}")
    
    def find_cal(part):
        mime = part.get('mimeType', '')
        body = part.get('body', {})
        if 'attachmentId' in body:
            try:
                att = service.users().messages().attachments().get(userId='me', messageId=m['id'], id=body['attachmentId']).execute()
                data = base64.urlsafe_b64decode(att['data']).decode('utf-8', errors='ignore')
                if 'BEGIN:VCALENDAR' in data:
                    print("--- CALENDAR ATTACHMENT ---")
                    for line in data.split('\n'):
                        if any(k in line for k in ['DTSTART', 'DTEND', 'SUMMARY', 'LOCATION']):
                            print("  ", line.strip())
            except Exception as e:
                pass
        if 'parts' in part:
            for p in part['parts']:
                find_cal(p)
    find_cal(msg['payload'])
    print("=" * 60)
