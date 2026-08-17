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

msg = service.users().messages().get(userId='me', id='19ff08dac3885de4', format='full').execute()
headers = {h['name']: h['value'] for h in msg['payload']['headers']}

print("SUBJECT:", headers.get("Subject"))
print("FROM:", headers.get("From"))

def walk_parts(part):
    mime = part.get('mimeType', '')
    print("MIME:", mime)
    if 'body' in part and 'data' in part['body']:
        data = part['body']['data']
        content = base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')
        if 'html' in mime:
            soup = BeautifulSoup(content, 'html.parser')
            print("HTML TEXT:\n", soup.get_text('\n')[:2000])
        else:
            print("PLAIN TEXT:\n", content[:2000])
    if 'parts' in part:
        for p in part['parts']:
            walk_parts(p)

walk_parts(msg['payload'])
