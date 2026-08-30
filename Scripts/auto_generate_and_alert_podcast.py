import os
import sys
import time
import subprocess
import requests

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE_DIR = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
OUTPUT_MP3 = os.path.join(WORKSPACE_DIR, "Knowledge_Base", "Reports", "daily", "malli_executive_podcast.mp3")
DISCORD_WEBHOOK_DAILY = "https://discord.com/api/webhooks/1543334492457009322/zVCTRfqTGGdtZWWXpb3MidxAm7KRQ6FRZQNko3Ea4v5GrlcrFMZfLh2MQSVtd_ZMHHFZ"

def generate_and_notify():
    print("==================================================")
    print("🎙️ Auto NotebookLM Audio Pipeline + Discord Alert")
    print("==================================================")
    
    # 1. Trigger Generation
    print("1. Triggering audio generation...")
    subprocess.run(["notebooklm", "generate", "audio"], check=True)
    
    # 2. Wait until status is completed
    print("2. Polling for audio completion (usually takes 2-4 mins)...")
    completed = False
    title = "Malli Executive Podcast"
    
    for _ in range(30): # max 10 mins
        time.sleep(20)
        res = subprocess.run(["notebooklm", "artifact", "list"], capture_output=True, text=True, encoding='utf-8', errors='ignore')
        out = res.stdout
        if "completed" in out and "Audio" in out:
            print("Audio generation completed!")
            completed = True
            break
        print("Still processing audio...")
        
    if not completed:
        print("Timeout waiting for audio.", file=sys.stderr)
        return
        
    # 3. Download MP3
    print("3. Downloading MP3 to local Knowledge Base...")
    subprocess.run(["notebooklm", "download", "audio", OUTPUT_MP3], check=True)
    print(f"Downloaded: {OUTPUT_MP3}")
    
    # 4. Notify Discord
    print("4. Sending notification to Discord (#mallicord)...")
    embed = {
        'title': '🎧 Executive Audio Overview พร้อมฟังแล้วค่ะบอส!',
        'description': 'ระบบ AI สังเคราะห์พอดแคสต์สรุปภาพรวมพอร์ตและทิศทางกลยุทธ์เสร็จสมบูรณ์เรียบร้อยแล้วค่ะ!',
        'color': 0x9B59B6,
        'fields': [
            {'name': '📁 ไฟล์ในเครื่อง', 'value': f'`{OUTPUT_MP3}`', 'inline': False},
            {'name': '🌐 ฟังผ่านมือถือ/เว็บ', 'value': '[เปิดฟังบน NotebookLM](https://notebooklm.google.com/)', 'inline': False}
        ],
        'footer': {'text': 'Malli Autonomous Pipeline'}
    }
    requests.post(DISCORD_WEBHOOK_DAILY, json={'username': 'Malli (Podcast Anchor)', 'embeds': [embed]})
    print("All tasks finished successfully!")

if __name__ == '__main__':
    generate_and_notify()
