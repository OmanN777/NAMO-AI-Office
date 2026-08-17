import os
import sys
import json
import base64
from email.mime.text import MIMEText
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

    recipient = "Ar-titaya.pitirattanamongkhol@bangkokbank.com"
    subject = "สมัครงานตำแหน่ง QA Engineer (BBL Innovation Data & AI Fest 2026) — นาถวัฒน์ เทพหัสดิน ณ อยุธยา"

    body_text = """เรียน คุณอาทิตยา และทีมงานฝ่ายทรัพยากรบุคคล/ทีมนวัตกรรม ธนาคารกรุงเทพ จำกัด (มหาชน),

ผมมีความสนใจสมัครงานในตำแหน่ง QA Engineer ผ่านโครงการ BBL Innovation Data & AI Fest 2026 ของทางธนาคารกรุงเทพครับ 

ผมเป็นนักศึกษาจบใหม่จากคณะเทคโนโลยีสารสนเทศและการสื่อสาร (ICT) มหาวิทยาลัยมหิดล และมีประสบการณ์ฝึกงานในสายงาน Quality Assurance เป็นระยะเวลา 8 เดือน ซึ่งได้ปฏิบัติงานจริงทั้งการทำ Manual Testing, API Testing (Postman), การตรวจสอบฐานข้อมูล SQL ตลอดจนการพัฒนา Automated Testing ด้วย Playwright, Robot Framework และ Python ครับ

ผมมีความพร้อมในการเรียนรู้ระบบงานและกระบวนการทำงานจริงของธนาคาร และมุ่งมั่นที่จะนำทักษะด้านการทดสอบซอฟต์แวร์และการพัฒนา Test Automation มาช่วยเสริมสร้างคุณภาพของระบบงานและนวัตกรรมทางการเงินให้แก่ ธนาคารกรุงเทพ อย่างเต็มที่ครับ

ข้อมูลเพิ่มเติมประกอบการพิจารณา:
- Expected Salary (เงินเดือนคาดหวัง): 28,000 – 35,000 บาท/เดือน (สามารถพูดคุยต่อรองได้ครับ)
- Availability (ความพร้อมเริ่มงาน): พร้อมเริ่มงานได้ทันที (Immediately)
- Work Preference: ยินดีทำงาน On-site ณ สำนักงานใหญ่สีลม / อาคารพระราม 3 หรือแบบ Hybrid ตามที่ทางธนาคารกำหนดครับ

ผมได้แนบเรซูไม่อัปเดต (Resume PDF) มาพร้อมกับอีเมลฉบับนี้เพื่อประกอบการพิจารณาครับ ขอขอบพระคุณสำหรับเวลาและโอกาสในการพิจารณาครับ

ขอแสดงความนับถือ

นาถวัฒน์ เทพหัสดิน ณ อยุธยา (นะโม)
Quality Assurance / Software Tester
โทร: 063-435-8908 | อีเมล: namo.nanon5@gmail.com
GitHub: github.com/OmanN777 | LinkedIn: linkedin.com/in/natawat-tephassadin-na-ayutaya/
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

        print(f"✅ สร้างร่างอีเมล (Draft) สำเร็จแล้ว! Draft ID: {draft['id']}")
    except Exception as e:
        print(f"❌ Failed to create draft: {e}")

if __name__ == '__main__':
    create_draft()
