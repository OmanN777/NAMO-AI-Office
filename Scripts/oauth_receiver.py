import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse
from google_auth_oauthlib.flow import InstalledAppFlow

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

SCOPES = [
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive'
]

WORKSPACE_DIR = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
GMAIL_API_DIR = os.path.join(WORKSPACE_DIR, "gmail_api")
CREDENTIALS_PATH = os.path.join(GMAIL_API_DIR, "credentials.json")
TOKEN_DRIVE_PATH = os.path.join(GMAIL_API_DIR, "token_drive.json")

class OAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        if 'code' in params:
            code = params['code'][0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(b"<h1>SUCCESS: Google Drive Authorized!</h1><p>You can close this tab now.</p>")
            
            # Exchange code for token
            flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES, redirect_uri='http://localhost:8080/')
            flow.fetch_token(code=code)
            creds = flow.credentials
            with open(TOKEN_DRIVE_PATH, 'w', encoding='utf-8') as f:
                f.write(creds.to_json())
            print("Successfully saved token_drive.json!")
            sys.exit(0)

def run_server():
    server = HTTPServer(('localhost', 8080), OAuthHandler)
    print("Listening on http://localhost:8080/ for OAuth code...")
    server.handle_request()

if __name__ == '__main__':
    run_server()
