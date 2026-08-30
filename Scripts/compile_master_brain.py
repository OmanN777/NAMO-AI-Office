import os
import sys
import glob
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE_DIR = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
TOKEN_DRIVE_PATH = os.path.join(WORKSPACE_DIR, "gmail_api", "token_drive.json")
FOLDER_NAME = "Malli_HQ_Knowledge_Base"
COMPILED_FILE = os.path.join(WORKSPACE_DIR, "Knowledge_Base", "MALLI_EXECUTIVE_BRAIN_ALL_IN_ONE.md")

def compile_and_sync():
    print("Compiling all Knowledge Base files into ONE Master Brain document...")
    
    header = """# 🧠 MALLI EXECUTIVE BRAIN & KNOWLEDGE BASE (MASTER COMPILATION)
**Owner:** Boss Namo (Natawat T.)
**Compiled by:** Malli (Chief Executive Secretary)
**Target:** NotebookLM & Gemini Pro Master Grounding Source
**Last Updated:** 2026-08-30

---
"""
    content_blocks = [header]

    # Section 1: Strategy & Profile
    strat_file = os.path.join(WORKSPACE_DIR, "Knowledge_Base", "Wiki", "strategy", "boss_strategic_profile_2026.md")
    if os.path.exists(strat_file):
        with open(strat_file, encoding='utf-8') as f:
            content_blocks.append("\n\n# 🎯 SECTION 1: BOSS STRATEGIC BLUEPRINT\n\n" + f.read())

    # Section 2: Case Studies
    case_dir = os.path.join(WORKSPACE_DIR, "Knowledge_Base", "Wiki", "case_studies")
    content_blocks.append("\n\n# 📈 SECTION 2: DEEP-DIVE CASE STUDIES & VALUATION\n\n")
    for cf in glob.glob(os.path.join(case_dir, "*.md")):
        with open(cf, encoding='utf-8') as f:
            content_blocks.append(f"\n\n## Case Study: {os.path.basename(cf)}\n\n" + f.read())

    # Section 3: Latest Daily Report
    daily_file = os.path.join(WORKSPACE_DIR, "Knowledge_Base", "Reports", "daily", "2026-08-29-malli-daily.md")
    if os.path.exists(daily_file):
        with open(daily_file, encoding='utf-8') as f:
            content_blocks.append("\n\n# 📋 SECTION 3: LATEST EXECUTIVE DAILY REPORT\n\n" + f.read())

    # Write locally
    compiled_text = "".join(content_blocks)
    with open(COMPILED_FILE, "w", encoding="utf-8") as f:
        f.write(compiled_text)
    print(f"Generated: {COMPILED_FILE}")

    # Upload to Google Drive
    creds = Credentials.from_authorized_user_file(TOKEN_DRIVE_PATH)
    service = build('drive', 'v3', credentials=creds)

    query = f"name = '{FOLDER_NAME}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
    res = service.files().list(q=query, spaces='drive', fields='files(id, name)').execute()
    folder_id = res['files'][0]['id']

    fn = os.path.basename(COMPILED_FILE)
    q_file = f"name = '{fn}' and '{folder_id}' in parents and trashed = false"
    existing = service.files().list(q=q_file, spaces='drive', fields='files(id, name)').execute().get('files', [])
    media = MediaFileUpload(COMPILED_FILE, resumable=True)

    if existing:
        fid = existing[0]['id']
        up = service.files().update(fileId=fid, media_body=media, fields='id, name, webViewLink').execute()
        print(f"✅ Updated Master Brain on Drive: {fn} -> {up.get('webViewLink')}")
    else:
        fmeta = {'name': fn, 'parents': [folder_id]}
        cr = service.files().create(body=fmeta, media_body=media, fields='id, name, webViewLink').execute()
        print(f"✅ Uploaded Master Brain to Drive: {fn} -> {cr.get('webViewLink')}")

    print("\n🎉 MASTER COMPILATION COMPLETE! Only 1 file needed in NotebookLM.")

if __name__ == '__main__':
    compile_and_sync()
