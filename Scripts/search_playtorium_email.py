import os
import sys
import json
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

workspace_dir = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
gmail_api_dir = os.path.join(workspace_dir, "gmail_api")
token_paths = [
    os.path.join(gmail_api_dir, "token.json"),
    os.path.join(gmail_api_dir, "token_gmail.json"),
    os.path.join(gmail_api_dir, "token_compose.json")
]

def get_gmail_service():
    for t_path in token_paths:
        if os.path.exists(t_path):
            try:
                c = Credentials.from_authorized_user_file(t_path)
                if c and c.valid:
                    return build('gmail', 'v1', credentials=c)
                elif c and c.expired and c.refresh_token:
                    c.refresh(Request())
                    with open(t_path, 'w', encoding='utf-8') as f:
                        f.write(c.to_json())
                    return build('gmail', 'v1', credentials=c)
            except Exception as e:
                pass
    return None

def main():
    service = get_gmail_service()
    if not service:
        print("Could not authenticate Gmail API")
        return

    results = service.users().messages().list(userId='me', q="Playtorium", maxResults=5).execute()
    messages = results.get('messages', [])

    print(f"Found {len(messages)} Playtorium messages:")
    for msg_ref in messages:
        msg = service.users().messages().get(userId='me', id=msg_ref['id'], format='full').execute()
        payload = msg.get('payload', {})
        headers = payload.get('headers', [])

        subject = "(No Subject)"
        sender = "(Unknown Sender)"
        date_str = ""

        for h in headers:
            name = h.get('name', '').lower()
            if name == 'subject':
                subject = h.get('value', subject)
            elif name == 'from':
                sender = h.get('value', sender)
            elif name == 'date':
                date_str = h.get('value', date_str)

        snippet = msg.get('snippet', '')

        # Try to extract body text
        body_text = ""
        parts = [payload]
        while parts:
            part = parts.pop()
            mime_type = part.get('mimeType', '')
            body = part.get('body', {})
            data = body.get('data', '')
            if data and (mime_type == 'text/plain' or mime_type == 'text/html'):
                import base64
                try:
                    decoded = base64.urlsafe_b64decode(data).decode('utf-8', errors='ignore')
                    body_text += decoded + "\n"
                except Exception:
                    pass
            if 'parts' in part:
                parts.extend(part['parts'])

        print("="*60)
        print(f"ID: {msg_ref['id']}")
        print(f"Subject: {subject}")
        print(f"Sender: {sender}")
        print(f"Date: {date_str}")
        print(f"Snippet: {snippet}")
        print("-" * 30)
        print("Body Sample:")
        print(body_text[:1000])

if __name__ == '__main__':
    main()
