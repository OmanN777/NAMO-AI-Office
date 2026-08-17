import os
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.compose'
]

workspace_dir = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
token_path = os.path.join(workspace_dir, "gmail_api", "token.json")
creds_path = os.path.join(workspace_dir, "gmail_api", "credentials.json")
zip_path = os.path.join(workspace_dir, "Work_Brief", "TrueMoney_QA_PreTest_Natawat.zip")

def get_gmail_service():
    creds = None
    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open(token_path, 'w') as token:
            token.write(creds.to_json())
    return build('gmail', 'v1', credentials=creds)

def create_reply_draft():
    service = get_gmail_service()
    
    # 1. Search for the specific Ascend Money email
    query = "subject:\"[Ascend Money] QA Test for QA Engineer\""
    results = service.users().messages().list(userId='me', q=query, maxResults=5).execute()
    messages = results.get('messages', [])
    
    if not messages:
        print("❌ Could not find Ascend Money email matching subject.")
        return
        
    msg_id = messages[0]['id']
    msg = service.users().messages().get(userId='me', id=msg_id, format='full').execute()
    
    thread_id = msg.get('threadId')
    headers = msg.get('payload', {}).get('headers', [])
    
    orig_from = ""
    orig_to = ""
    orig_cc = ""
    orig_subject = ""
    message_id_hdr = ""
    
    for h in headers:
        name = h['name'].lower()
        if name == 'from': orig_from = h['value']
        elif name == 'to': orig_to = h['value']
        elif name == 'cc': orig_cc = h['value']
        elif name == 'subject': orig_subject = h['value']
        elif name == 'message-id': message_id_hdr = h['value']

    # Build Reply All recipients
    # Reply to original sender + keep CCs
    reply_to = orig_from
    reply_cc = orig_cc
    
    subject = orig_subject if orig_subject.lower().startswith('re:') else f"Re: {orig_subject}"

    # Build MIME Message
    mime_msg = MIMEMultipart()
    mime_msg['To'] = reply_to
    if reply_cc:
        mime_msg['Cc'] = reply_cc
    mime_msg['Subject'] = subject
    if message_id_hdr:
        mime_msg['In-Reply-To'] = message_id_hdr
        mime_msg['References'] = message_id_hdr

    body_text = """เรียน คุณปัณฑารีย์ และทีมงาน Talent Acquisition (Ascend Corp),

ผม นาถวัฒน์ เทพหัสดิน ณ อยุธยา ได้ดำเนินการทำแบบทดสอบ Pre-Interview Test สำหรับตำแหน่ง Quality Assurance Engineer เรียบร้อยแล้วครับ

ทั้งนี้ ผมได้แนบไฟล์ ZIP คำตอบ TrueMoney_QA_PreTest_Natawat.zip ซึ่งประกอบด้วยไฟล์คำตอบครบถ้วนทั้ง 4 ข้อ (test1.py, test2.xlsx, test3.robot, test4.robot) มาพร้อมกับอีเมลฉบับนี้ครับ

หากต้องการข้อมูลเพิ่มเติมหรือมีข้อสงสัยประการใด สามารถติดต่อผมได้ตลอดเวลาครับ ขอบพระคุณสำหรับโอกาสในการร่วมทดสอบครั้งนี้ครับ

ขอแสดงความนับถือ,
นาถวัฒน์ เทพหัสดิน ณ อยุธยา (นะโม)
เบอร์โทรศัพท์: 063-435-8908
อีเมล: namo.nanon5@gmail.com
"""

    mime_msg.attach(MIMEText(body_text, 'plain', 'utf-8'))

    # Attach ZIP file
    if os.path.exists(zip_path):
        filename = os.path.basename(zip_path)
        with open(zip_path, 'rb') as f:
            part = MIMEBase('application', 'zip')
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{filename}"')
        mime_msg.attach(part)
        print(f"Attached file: {filename}")
    else:
        print(f"❌ Zip file not found at: {zip_path}")

    # Encode raw string
    raw_msg = base64.urlsafe_b64encode(mime_msg.as_bytes()).decode('utf-8')
    
    draft_body = {
        'message': {
            'threadId': thread_id,
            'raw': raw_msg
        }
    }

    draft = service.users().drafts().create(userId='me', body=draft_body).execute()
    print(f"\n✅ Successfully created Gmail Draft for Reply All! Draft ID: {draft['id']}")

if __name__ == "__main__":
    create_reply_draft()
