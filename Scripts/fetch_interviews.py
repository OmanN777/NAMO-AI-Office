import os
import sys
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

token_path = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace\gmail_api\token.json"

if not os.path.exists(token_path):
    print("Token path not found:", token_path)
    sys.exit(1)

creds = Credentials.from_authorized_user_file(token_path, ['https://www.googleapis.com/auth/gmail.readonly'])
service = build('gmail', 'v1', credentials=creds)

results = service.users().messages().list(userId='me', q='interview OR สัมภาษณ์ OR Agoda OR VAS.UP OR Feyverly OR Krungsri OR Ngernturbo OR Playtorium OR Ascend OR Capco', maxResults=30).execute()
messages = results.get('messages', [])

print(f"Found {len(messages)} relevant messages:\n")
for m in messages:
    msg = service.users().messages().get(userId='me', id=m['id'], format='full').execute()
    headers = {h['name']: h['value'] for h in msg['payload']['headers']}
    subject = headers.get('Subject', '')
    sender = headers.get('From', '')
    date = headers.get('Date', '')
    snippet = msg.get('snippet', '')
    
    print(f"ID: {m['id']}")
    print(f"Subject: {subject}")
    print(f"From: {sender}")
    print(f"Date: {date}")
    print(f"Snippet: {snippet}")
    print("=" * 60)
