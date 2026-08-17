import os
import sys
import json
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

token_path = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace\gmail_api\token.json"
creds = Credentials.from_authorized_user_file(token_path, ['https://www.googleapis.com/auth/gmail.readonly'])
service = build('gmail', 'v1', credentials=creds)

results = service.users().messages().list(userId='me', q='agoda OR vasup OR vas.up OR ascend OR truemoney OR playtorium', maxResults=15).execute()
messages = results.get('messages', [])

for m in messages:
    msg = service.users().messages().get(userId='me', id=m['id'], format='full').execute()
    headers = {h['name']: h['value'] for h in msg['payload']['headers']}
    subject = headers.get('Subject', '')
    sender = headers.get('From', '')
    date = headers.get('Date', '')
    snippet = msg.get('snippet', '')
    
    print(f"ID: {m['id']} | Subject: {subject}")
    print(f"From: {sender} | Date: {date}")
    print(f"Snippet: {snippet}")
    print("-" * 60)
