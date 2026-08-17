import os
import sys
import json
import requests
from python_dotenv import load_dotenv if False else None # Avoid import confusion, use dotenv

# Try importing dotenv
try:
    from dotenv import load_dotenv
    # Load env from workspace root
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    load_dotenv(os.path.join(base_dir, ".env"))
except ImportError:
    pass

def send_discord_notification(message, title="Antigravity Notification", color=0x3498db, file_path=None):
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("⚠️ [Discord Notifier] Warning: DISCORD_WEBHOOK_URL is not set in the environment variables.")
        return False

    payload = {
        "embeds": [{
            "title": title,
            "description": message[:2000],  # Discord description limit is 2048 chars
            "color": color,
            "timestamp": datetime_now_iso()
        }]
    }

    files = {}
    if file_path and os.path.exists(file_path):
        try:
            files = {"file": open(file_path, "rb")}
        except Exception as e:
            print(f"⚠️ [Discord Notifier] Failed to read file {file_path}: {e}")

    try:
        if files:
            # Send file + json metadata
            response = requests.post(
                webhook_url,
                data={"payload_json": json.dumps(payload)},
                files=files
            )
        else:
            response = requests.post(webhook_url, json=payload)

        if response.status_code in [200, 204]:
            print("✅ [Discord Notifier] Notification sent successfully!")
            return True
        else:
            print(f"❌ [Discord Notifier] Failed to send: {response.status_code} - {response.text}")
            return False
    except Exception as e:
        print(f"❌ [Discord Notifier] Exception during execution: {e}")
        return False

def datetime_now_iso():
    try:
        from datetime import datetime
        return datetime.utcnow().isoformat() + "Z"
    except:
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python discord_notifier.py [message] [title] [color_hex_or_dec] [file_path]")
        return

    message = sys.argv[1]
    title = sys.argv[2] if len(sys.argv) > 2 else "Antigravity Notification"
    
    color_val = 0x3498db # Default blue
    if len(sys.argv) > 3:
        try:
            val = sys.argv[3]
            color_val = int(val, 16) if val.startswith("0x") else int(val)
        except ValueError:
            pass

    file_path = sys.argv[4] if len(sys.argv) > 4 else None

    send_discord_notification(message, title, color_val, file_path)

if __name__ == "__main__":
    main()
