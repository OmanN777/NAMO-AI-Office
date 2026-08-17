import os
import sys
import json
import base64
from datetime import datetime
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
credentials_path = os.path.join(gmail_api_dir, "credentials.json")
last_read_path = os.path.join(gmail_api_dir, "last_read_email.json")

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None
    used_token_path = None

    for t_path in token_paths:
        if os.path.exists(t_path):
            try:
                c = Credentials.from_authorized_user_file(t_path)
                if c and c.valid:
                    creds = c
                    used_token_path = t_path
                    break
                elif c and c.expired and c.refresh_token:
                    try:
                        c.refresh(Request())
                        with open(t_path, 'w', encoding='utf-8') as f:
                            f.write(c.to_json())
                        creds = c
                        used_token_path = t_path
                        break
                    except Exception as e:
                        print(f"⚠️ Refresh failed for {os.path.basename(t_path)}: {e}", file=sys.stderr)
            except Exception as e:
                print(f"⚠️ Load failed for {os.path.basename(t_path)}: {e}", file=sys.stderr)

    if not creds:
        print("⚠️ No valid OAuth credentials available.", file=sys.stderr)
        return None

    service = build('gmail', 'v1', credentials=creds)
    return service

def get_last_processed():
    if os.path.exists(last_read_path):
        try:
            with open(last_read_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get("last_processed_id", None), data.get("processed_ids", [])
        except Exception:
            pass
    return None, []

def save_last_processed(last_id, processed_ids):
    # Keep up to 1000 processed IDs to avoid infinite growth
    recent_ids = processed_ids[-1000:]
    with open(last_read_path, 'w', encoding='utf-8') as f:
        json.dump({
            "last_processed_id": last_id,
            "processed_ids": recent_ids,
            "last_check": datetime.now().isoformat()
        }, f, indent=2, ensure_ascii=False)

def main():
    service = get_gmail_service()
    if not service:
        print("\n🚨 [ALERT FOR BOSS] Gmail OAuth Token expired or revoked!")
        print("👉 Please run: python C:\\Users\\namo_\\OneDrive\\เอกสาร\\gemini-cli\\antigravity-office-workspace\\Scripts\\reauth_gmail.py\n")
        print(json.dumps({"status": "error", "message": "Gmail OAuth token expired or revoked. Re-authentication required."}))
        return

    last_id, processed_ids = get_last_processed()
    processed_set = set(processed_ids)

    try:
        # Fetch last 50 messages from inbox
        results = service.users().messages().list(userId='me', maxResults=50, q="in:inbox").execute()
        messages = results.get('messages', [])

        new_emails = []

        for msg_ref in messages:
            msg_id = msg_ref['id']
            if msg_id in processed_set:
                continue

            msg = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
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

            new_emails.append({
                "id": msg_id,
                "subject": subject,
                "sender": sender,
                "date": date_str,
                "snippet": snippet
            })

        if new_emails:
            # Mark these messages as processed
            latest_id = new_emails[0]["id"]
            for email in new_emails:
                if email["id"] not in processed_set:
                    processed_ids.append(email["id"])

            save_last_processed(latest_id, processed_ids)

        output = {
            "status": "success",
            "count": len(new_emails),
            "emails": new_emails
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))

    except Exception as e:
        print(json.dumps({"status": "error", "message": str(e)}))

if __name__ == '__main__':
    main()
