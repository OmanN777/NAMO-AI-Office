import os
import sys
import json
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
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
                print(f"Token error for {t_path}: {e}", file=sys.stderr)
    return None

def create_draft():
    service = get_gmail_service()
    if not service:
        print("❌ Could not authenticate Gmail API for draft creation.")
        return

    recipient = "HRRM@bol.co.th"
    subject = "Application for Software Tester (Automate) - Natawat Tephassadin na Ayutaya"

    body_text = """Dear K. Waralee and the Recruitment Team at Business Online PCL (BOL),

I am writing to express my interest in the Software Tester (Automate) position at Business Online PCL.

I believe I am a strong fit for this role because of my hands-on experience in automated testing and software quality assurance, developed during my 8-month QA internship. I have designed and executed automated test suites using Robot Framework (Python) and Playwright (TypeScript), covering functional, regression, and REST API testing. As an ICT graduate from Mahidol University, I am familiar with Agile development workflows and data verification. I am prepared to contribute effectively to maintaining the reliability of BOL's business information platforms and data-driven solutions.

Candidate Summary:
- Degree: B.Sc. in ICT, Mahidol University (Faculty of ICT)
- Core Skills: Robot Framework (Python), Playwright (TypeScript), REST API Testing (Postman), Manual Testing, Git/GitHub, SQL Validation
- Expected Salary: 28,000 - 35,000 THB/Month (Negotiable)
- Availability: Immediately available
- Work Arrangement: Comfortable with On-site at MS Siam Tower, Rama 3 / Hybrid

Thank you for considering my application. My resume and portfolio details are attached for your review.

Sincerely,

Natawat Tephassadin na Ayutaya (Namo)
Quality Assurance / Software Tester
Tel: 063-435-8908 | Email: namo.nanon5@gmail.com
LinkedIn: linkedin.com/in/natawat-tephassadin-na-ayutaya/
GitHub: github.com/OmanN777
"""

    message = MIMEText(body_text, 'plain', 'utf-8')
    message['to'] = recipient
    message['subject'] = subject

    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')

    try:
        draft = service.users().drafts().create(
            userId='me',
            body={'message': {'raw': raw_message}}
        ).execute()

        print(f"✅ สร้างร่างอีเมล (Draft) ใน Gmail สำเร็จเรียบร้อยแล้วค่ะ! Draft ID: {draft['id']}")
    except Exception as e:
        print(f"❌ Failed to create draft: {e}")

if __name__ == '__main__':
    create_draft()
