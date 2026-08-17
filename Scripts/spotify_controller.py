import os
import sys
import json
import time
import base64
import urllib.request
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler
import webbrowser

# Paths
workspace_dir = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
creds_path = os.path.join(workspace_dir, "gmail_api", "spotify_credentials.json")
token_path = os.path.join(workspace_dir, "gmail_api", "spotify_token.json")

# Spotify OAuth Scopes
SCOPES = "user-modify-playback-state user-read-playback-state user-read-currently-playing"

# HTML Page shown to user after authorization
AUTH_HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Spotify Authorized</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #121212;
            color: #ffffff;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        .container {
            text-align: center;
            background: #181818;
            padding: 40px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.5);
            border: 1px solid #282828;
        }
        h1 { color: #1DB954; margin-bottom: 10px; }
        p { color: #b3b3b3; font-size: 16px; }
        .icon { font-size: 48px; margin-bottom: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="icon">🎵</div>
        <h1>Spotify Authorized!</h1>
        <p>Antigravity CLI is now connected to your Spotify account.</p>
        <p>You can close this tab and return to your terminal.</p>
    </div>
</body>
</html>
"""

class OAuthCallbackHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        
        if 'code' in params:
            self.server.auth_code = params['code'][0]
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(AUTH_HTML.encode('utf-8'))
        else:
            self.send_response(400)
            self.send_header('Content-Type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write("Authorization code missing.".encode('utf-8'))

    def log_message(self, format, *args):
        # Suppress logging server requests to stdout
        pass

def make_request(url, method="GET", headers=None, data=None):
    if headers is None:
        headers = {}
    
    req_data = None
    if data:
        if isinstance(data, dict):
            req_data = urllib.parse.urlencode(data).encode('utf-8')
        elif isinstance(data, str):
            req_data = data.encode('utf-8')
        else:
            req_data = data
            
    req = urllib.request.Request(url, headers=headers, data=req_data, method=method)
    try:
        with urllib.request.urlopen(req) as response:
            status = response.status
            content = response.read().decode('utf-8')
            return status, content
    except urllib.error.HTTPError as e:
        status = e.code
        try:
            content = e.read().decode('utf-8')
        except Exception:
            content = str(e)
        return status, content
    except Exception as e:
        return 500, str(e)

def load_credentials():
    if not os.path.exists(creds_path):
        print(f"❌ Error: Spotify credentials file not found at {creds_path}")
        print("\n📝 วิธีการตั้งค่า Spotify Integration:")
        print("1. ไปที่ Spotify Developer Dashboard (https://developer.spotify.com/dashboard)")
        print("2. สร้าง App ใหม่ ตั้งชื่อและระบุรายละเอียดใดๆ ก็ได้")
        print("3. เพิ่ม Redirect URI ในการตั้งค่าของ App เป็น: http://localhost:8080/callback")
        print("4. คัดลอก Client ID และ Client Secret")
        print(f"5. สร้างไฟล์ '{creds_path}' ด้วยโครงสร้างดังนี้:")
        print('{\n  "client_id": "YOUR_CLIENT_ID",\n  "client_secret": "YOUR_CLIENT_SECRET",\n  "redirect_uri": "http://localhost:8080/callback"\n}')
        sys.exit(1)
        
    with open(creds_path, 'r', encoding='utf-8') as f:
        creds = json.load(f)
        
    if creds.get("client_id") == "YOUR_SPOTIFY_CLIENT_ID" or not creds.get("client_id"):
        print("⚠️ กรุณาตั้งค่า Client ID และ Client Secret ในไฟล์ spotify_credentials.json ให้ถูกต้องก่อนเริ่มใช้งานครับ")
        sys.exit(1)
        
    return creds

def get_authorization_code(creds):
    redirect_uri = creds.get("redirect_uri", "http://localhost:8080/callback")
    parsed_url = urllib.parse.urlparse(redirect_uri)
    port = parsed_url.port or 8080
    host = parsed_url.hostname or 'localhost'
    
    server = HTTPServer((host, port), OAuthCallbackHandler)
    server.auth_code = None
    
    params = {
        "client_id": creds["client_id"],
        "response_type": "code",
        "redirect_uri": redirect_uri,
        "scope": SCOPES,
        "show_dialog": "true"
    }
    auth_url = "https://accounts.spotify.com/authorize?" + urllib.parse.urlencode(params)
    
    print("\n🔄 กำลังเริ่มต้นยืนยันสิทธิ์บัญชี Spotify...")
    print(f"🔗 กรุณาเข้าลิงก์นี้ในกรณีที่เบราว์เซอร์ไม่เปิดโดยอัตโนมัติ:\n{auth_url}\n")
    
    # Open browser
    webbrowser.open(auth_url)
    
    # Wait for callback
    while server.auth_code is None:
        server.handle_request()
        
    return server.auth_code

def exchange_code_for_token(creds, code):
    url = "https://accounts.spotify.com/api/token"
    auth_header = base64.b64encode(f"{creds['client_id']}:{creds['client_secret']}".encode('utf-8')).decode('utf-8')
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": creds["redirect_uri"]
    }
    
    status, content = make_request(url, method="POST", headers=headers, data=data)
    if status == 200:
        token_data = json.loads(content)
        # Store absolute expiry timestamp
        token_data["expires_at"] = int(time.time()) + token_data["expires_in"]
        with open(token_path, 'w', encoding='utf-8') as f:
            json.dump(token_data, f)
        print("💾 บันทึก Access Token ของ Spotify สำเร็จ!")
        return token_data
    else:
        print(f"❌ Failed to exchange authorization code: {status} - {content}")
        sys.exit(1)

def refresh_token(creds, token_data):
    url = "https://accounts.spotify.com/api/token"
    auth_header = base64.b64encode(f"{creds['client_id']}:{creds['client_secret']}".encode('utf-8')).decode('utf-8')
    headers = {
        "Authorization": f"Basic {auth_header}",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "refresh_token",
        "refresh_token": token_data["refresh_token"]
    }
    
    status, content = make_request(url, method="POST", headers=headers, data=data)
    if status == 200:
        new_data = json.loads(content)
        token_data["access_token"] = new_data["access_token"]
        token_data["expires_at"] = int(time.time()) + new_data["expires_in"]
        if "refresh_token" in new_data:
            token_data["refresh_token"] = new_data["refresh_token"]
            
        with open(token_path, 'w', encoding='utf-8') as f:
            json.dump(token_data, f)
        return token_data
    else:
        print(f"⚠️ Failed to refresh Spotify token: {status} - {content}. Re-authenticating...")
        # Clear token path to trigger full re-auth next run
        if os.path.exists(token_path):
            os.remove(token_path)
        return None

def get_access_token():
    creds = load_credentials()
    token_data = None
    
    if os.path.exists(token_path):
        try:
            with open(token_path, 'r', encoding='utf-8') as f:
                token_data = json.load(f)
        except Exception:
            pass
            
    if not token_data:
        code = get_authorization_code(creds)
        token_data = exchange_code_for_token(creds, code)
    else:
        # Check expiry (with a 60-second buffer)
        if token_data.get("expires_at", 0) - 60 < int(time.time()):
            token_data = refresh_token(creds, token_data)
            # If refresh failed, do full auth
            if not token_data:
                code = get_authorization_code(creds)
                token_data = exchange_code_for_token(creds, code)
                
    return token_data["access_token"]

def format_duration(ms):
    seconds = int((ms / 1000) % 60)
    minutes = int((ms / (1000 * 60)) % 60)
    return f"{minutes}:{seconds:02d}"

def control_spotify(command, value=None):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass
        
    access_token = get_access_token()
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    if command == "status":
        url = "https://api.spotify.com/v1/me/player"
        status, content = make_request(url, method="GET", headers=headers)
        if status == 200 and content:
            data = json.loads(content)
            is_playing = data.get("is_playing", False)
            item = data.get("item")
            
            if item:
                track_name = item.get("name")
                artists = ", ".join([a.get("name") for a in item.get("artists", [])])
                album = item.get("album", {}).get("name")
                progress_ms = data.get("progress_ms", 0)
                duration_ms = item.get("duration_ms", 0)
                
                status_str = "▶️ Playing" if is_playing else "⏸️ Paused"
                print(f"{status_str}: {track_name} - {artists} (Album: {album})")
                print(f"⏱️ Progress: {format_duration(progress_ms)} / {format_duration(duration_ms)}")
            else:
                print("📭 Active device found but no track is currently loaded.")
        elif status == 204:
            print("📭 No active playback devices found. Open Spotify on one of your devices.")
        else:
            print(f"❌ Failed to get playback status: {status} - {content}")
            
    elif command == "play":
        url = "https://api.spotify.com/v1/me/player/play"
        status, content = make_request(url, method="PUT", headers=headers)
        if status in [200, 204]:
            print("▶️ Playback resumed on active device.")
        else:
            # Check if there is an error message
            try:
                err_data = json.loads(content)
                reason = err_data.get("error", {}).get("reason", "")
                if reason == "NO_ACTIVE_DEVICE":
                    print("⚠️ No active device found. Please start Spotify on your device first.")
                    return
            except Exception:
                pass
            print(f"❌ Failed to resume playback: {status} - {content}")
            
    elif command == "pause":
        url = "https://api.spotify.com/v1/me/player/pause"
        status, content = make_request(url, method="PUT", headers=headers)
        if status in [200, 204]:
            print("⏸️ Playback paused.")
        else:
            print(f"❌ Failed to pause playback: {status} - {content}")
            
    elif command == "next":
        url = "https://api.spotify.com/v1/me/player/next"
        status, content = make_request(url, method="POST", headers=headers)
        if status in [200, 204]:
            print("⏭️ Skipped to next track.")
        else:
            print(f"❌ Failed to skip to next track: {status} - {content}")
            
    elif command == "previous":
        url = "https://api.spotify.com/v1/me/player/previous"
        status, content = make_request(url, method="POST", headers=headers)
        if status in [200, 204]:
            print("⏮️ Skipped to previous track.")
        else:
            print(f"❌ Failed to skip to previous track: {status} - {content}")
            
    elif command == "volume":
        if not value:
            print("❌ Error: Volume level (0-100) must be specified.")
            return
        try:
            vol = int(value)
            if vol < 0 or vol > 100:
                raise ValueError()
        except ValueError:
            print("❌ Error: Volume level must be an integer between 0 and 100.")
            return
            
        url = f"https://api.spotify.com/v1/me/player/volume?volume_percent={vol}"
        status, content = make_request(url, method="PUT", headers=headers)
        if status in [200, 204]:
            print(f"🔊 Volume set to {vol}%.")
        else:
            print(f"❌ Failed to set volume: {status} - {content}")
    else:
        print(f"❌ Unknown command: {command}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python spotify_controller.py [status|play|pause|next|previous|volume] [volume_value]")
        return
        
    cmd = sys.argv[1].lower()
    val = sys.argv[2] if len(sys.argv) > 2 else None
    control_spotify(cmd, val)

if __name__ == "__main__":
    main()
