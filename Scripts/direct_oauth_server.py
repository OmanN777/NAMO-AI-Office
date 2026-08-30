import os
import sys
import json
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE_DIR = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
GMAIL_API_DIR = os.path.join(WORKSPACE_DIR, "gmail_api")
CREDENTIALS_PATH = os.path.join(GMAIL_API_DIR, "credentials.json")
TOKEN_DRIVE_PATH = os.path.join(GMAIL_API_DIR, "token_drive.json")
TOKEN_GMAIL_PATH = os.path.join(GMAIL_API_DIR, "token.json")

with open(CREDENTIALS_PATH) as f:
    client_config = json.load(f)['installed']

class OAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        query = urllib.parse.urlparse(self.path).query
        params = urllib.parse.parse_qs(query)
        if 'code' in params:
            code = params['code'][0]
            
            # Exchange code for tokens directly via Google OAuth endpoint
            token_url = client_config['token_uri']
            payload = {
                'code': code,
                'client_id': client_config['client_id'],
                'client_secret': client_config['client_secret'],
                'redirect_uri': 'http://localhost:8080/',
                'grant_type': 'authorization_code'
            }
            
            r = requests.post(token_url, data=payload)
            token_data = r.json()
            
            if 'access_token' in token_data:
                # Format to google-auth credentials format
                creds_data = {
                    'token': token_data.get('access_token'),
                    'refresh_token': token_data.get('refresh_token'),
                    'token_uri': client_config['token_uri'],
                    'client_id': client_config['client_id'],
                    'client_secret': client_config['client_secret'],
                    'scopes': [
                        'https://www.googleapis.com/auth/gmail.readonly',
                        'https://www.googleapis.com/auth/gmail.compose',
                        'https://www.googleapis.com/auth/drive.file',
                        'https://www.googleapis.com/auth/drive'
                    ]
                }
                
                # Save to token_drive.json & token.json
                with open(TOKEN_DRIVE_PATH, 'w', encoding='utf-8') as f:
                    json.dump(creds_data, f, indent=2)
                with open(TOKEN_GMAIL_PATH, 'w', encoding='utf-8') as f:
                    json.dump(creds_data, f, indent=2)
                    
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(b"<h1>SUCCESS! Google Drive & Gmail Connected.</h1><p>You can close this window and return to Antigravity.</p>")
                print("TOKEN SAVED SUCCESSFULLY!")
                sys.exit(0)
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(f"Error: {token_data}".encode('utf-8'))
                print("Error exchanging token:", token_data)

def start():
    print("Listening on http://localhost:8080/ ...")
    server = HTTPServer(('localhost', 8080), OAuthHandler)
    server.handle_request()

if __name__ == '__main__':
    start()
