import os
import sys
from datetime import datetime, timezone

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

workspace_dir = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
ics_output_path = os.path.join(workspace_dir, "Anniversary_Reminder.ics")

now_utc = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

ics_content = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//Malli Executive Assistant//Namo Anniversary Reminder//EN
CALSCALE:GREGORIAN
METHOD:PUBLISH
BEGIN:VEVENT
UID:namo-anniversary-every-20th@antigravity-office
DTSTAMP:{now_utc}
DTSTART;VALUE=DATE:20260820
DTEND;VALUE=DATE:20260821
RRULE:FREQ=MONTHLY;BYMONTHDAY=20
SUMMARY:❤️ วันครบรอบของบอสกับแฟน (Monthly Anniversary)
DESCRIPTION:วันครบรอบสุดพิเศษประจำเดือนของบอสกับแฟน อย่าลืมส่งข้อความน่ารักๆ หรือพาไปทานของอร่อยด้วยกันนะคะ! 🥰💐✨\\n(แจ้งเตือนโดย มอลิ)
STATUS:CONFIRMED
TRANSP:TRANSPARENT
BEGIN:VALARM
TRIGGER:-PT0M
ACTION:DISPLAY
DESCRIPTION:🎉 สุขสันต์วันครบรอบค่ะบอส! เข้าสู่วันที่ 20 แล้วนะคะ (Midnight Reminder) ❤️
END:VALARM
BEGIN:VALARM
TRIGGER:-PT12H
ACTION:DISPLAY
DESCRIPTION:❤️ เตือนความจำ: พรุ่งนี้เป็นวันครบรอบของบอสกับแฟนนะคะ!
END:VALARM
BEGIN:VALARM
TRIGGER;VALUE=DATE-TIME:20260820T010000Z
ACTION:DISPLAY
DESCRIPTION:❤️ อรุณสวัสดิ์ค่ะบอส! วันนี้วันครบรอบของบอสกับแฟน (วันที่ 20) นะคะ 💐
END:VALARM
END:VEVENT
END:VCALENDAR
"""

with open(ics_output_path, 'w', encoding='utf-8') as f:
    f.write(ics_content.strip() + "\n")

print(f"Successfully updated Anniversary_Reminder.ics with Midnight Alarm at: {ics_output_path}")
