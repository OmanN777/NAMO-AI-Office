import os
import sys
import json
from datetime import datetime
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Paths
workspace_dir = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
credentials_path = os.path.join(workspace_dir, "gmail_api", "credentials.json")
token_path = os.path.join(workspace_dir, "gmail_api", "token.json")
spreadsheet_id_path = os.path.join(workspace_dir, "gmail_api", "spreadsheet_id.txt")

oman_portfolio_path = os.path.join(workspace_dir, "Portfolios", "Oman_Mock_Portfolio", "holdings.json")
real_portfolio_path = os.path.join(workspace_dir, "Portfolios", "Namo_History", "my_portfolio.json")

# Google Sheets & Drive Scopes
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file'
]

def get_credentials():
    creds = None
    if os.path.exists(token_path):
        try:
            with open(token_path, 'r', encoding='utf-8') as f:
                token_data = json.load(f)
                token_scopes = token_data.get('scopes', [])
            if not all(scope in token_scopes for scope in SCOPES):
                print("⚠️ Cached token.json is missing required scopes. Re-authenticating...")
                creds = None
            else:
                creds = Credentials.from_authorized_user_file(token_path, SCOPES)
        except Exception as e:
            print(f"⚠️ Failed to load cached token: {e}")
            
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                print(f"⚠️ Failed to refresh token: {e}")
                creds = None
                
        if not creds:
            if not os.path.exists(credentials_path):
                print(f"❌ Error: Google credentials file not found at {credentials_path}")
                print("Please place your credentials.json file in the gmail_api/ directory first.")
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
            
        with open(token_path, 'w', encoding='utf-8') as token_file:
            token_file.write(creds.to_json())
            print("💾 Saved new OAuth token to token.json")
            
    return creds

def get_or_create_spreadsheet(service):
    spreadsheet_id = None
    if os.path.exists(spreadsheet_id_path):
        with open(spreadsheet_id_path, 'r', encoding='utf-8') as f:
            spreadsheet_id = f.read().strip()
            
    if spreadsheet_id:
        try:
            # Check if spreadsheet exists and is accessible
            service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
            print(f"ℹ️ Found existing Google Sheet ID: {spreadsheet_id}")
            return spreadsheet_id
        except Exception:
            print("⚠️ Saved Spreadsheet ID was not accessible. Creating a new one...")
            
    # Create new Spreadsheet
    print("🆕 Creating new Google Sheet: 'Antigravity Investment Dashboard'...")
    spreadsheet_body = {
        'properties': {
            'title': 'Antigravity Investment Dashboard'
        }
    }
    spreadsheet = service.spreadsheets().create(
        body=spreadsheet_body,
        fields='spreadsheetId'
    ).execute()
    
    spreadsheet_id = spreadsheet.get('spreadsheetId')
    
    with open(spreadsheet_id_path, 'w', encoding='utf-8') as f:
        f.write(spreadsheet_id)
        
    print(f"✅ Created new Google Sheet successfully! ID: {spreadsheet_id}")
    return spreadsheet_id

def format_portfolio_data(portfolio_path):
    if not os.path.exists(portfolio_path):
        return None
        
    with open(portfolio_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    rows = []
    # Headers
    rows.append([
        "Ticker", "Company Name", "Shares", "Avg Cost ($)", "Current Price ($)", 
        "Total Value ($)", "P/L ($)", "P/L (%)", "Allocation (%)", "Days Held"
    ])
    
    holdings = data.get("holdings", [])
    for h in holdings:
        rows.append([
            h.get("ticker", ""),
            h.get("name", "N/A"),
            h.get("shares", 0),
            h.get("average_cost", 0),
            h.get("current_price", 0),
            h.get("total_value", 0),
            h.get("pl_usd", 0),
            h.get("pl_pct", 0) / 100,  # We will divide by 100 so Sheets can format as %
            h.get("allocation_pct", 0) / 100,
            h.get("days_held", 0)
        ])
        
    # Add spacing
    rows.append([])
    
    # Summary Details
    cash = data.get("cash_balance", 0)
    total_val = data.get("total_value", 0)
    total_cost = data.get("total_cost", 0)
    total_pl = data.get("total_pl", 0)
    pl_percentage = data.get("pl_percentage", 0)
    nav = data.get("current_nav", total_val + cash)
    
    rows.append(["Cash Balance", "", "", "", "", cash])
    rows.append(["Total Cost Basis", "", "", "", "", total_cost])
    rows.append(["Unrealized P/L ($)", "", "", "", "", total_pl])
    rows.append(["Unrealized P/L (%)", "", "", "", "", pl_percentage / 100])
    rows.append(["TOTAL NAV (Net Assets)", "", "", "", "", nav])
    rows.append([])
    rows.append([f"Last Updated: {data.get('last_updated', datetime.now().strftime('%Y-%m-%d'))}"])
    
    return rows

def ensure_sheet_exists(service, spreadsheet_id, title):
    spreadsheet = service.spreadsheets().get(spreadsheetId=spreadsheet_id).execute()
    sheets = spreadsheet.get('sheets', [])
    sheet_titles = [s.get('properties', {}).get('title') for s in sheets]
    
    if title not in sheet_titles:
        print(f"➕ Adding sheet '{title}' to spreadsheet...")
        body = {
            'requests': [{
                'addSheet': {
                    'properties': {
                        'title': title
                    }
                }
            }]
        }
        service.spreadsheets().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()

def sync_sheet(service, spreadsheet_id, sheet_title, data_rows):
    if not data_rows:
        return
        
    ensure_sheet_exists(service, spreadsheet_id, sheet_title)
    
    # Clear existing content first to avoid overlapping old data
    range_name = f"'{sheet_title}'!A1:Z100"
    service.spreadsheets().values().clear(
        spreadsheetId=spreadsheet_id,
        range=range_name,
        body={}
    ).execute()
    
    # Write new content
    body = {
        'values': data_rows
    }
    service.spreadsheets().values().update(
        spreadsheetId=spreadsheet_id,
        range=f"'{sheet_title}'!A1",
        valueInputOption='USER_ENTERED',
        body=body
    ).execute()
    print(f"📊 Updated sheet '{sheet_title}' with {len(data_rows)} rows.")

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass
    print("🔄 Starting Google Sheets Synchronization...")
    creds = get_credentials()
    service = build('sheets', 'v4', credentials=creds)
    spreadsheet_id = get_or_create_spreadsheet(service)
    
    # 1. Sync Oman Mock Portfolio
    oman_data = format_portfolio_data(oman_portfolio_path)
    if oman_data:
        sync_sheet(service, spreadsheet_id, "Oman Mock Portfolio", oman_data)
    else:
        print("⚠️ Oman mock holdings data file not found. Skipping.")
        
    # 2. Sync Namo Real Portfolio
    real_data = format_portfolio_data(real_portfolio_path)
    if real_data:
        sync_sheet(service, spreadsheet_id, "Namo Real Portfolio", real_data)
    else:
        print("⚠️ Namo real portfolio data file not found. Skipping.")
        
    print(f"🎉 Synchronization complete! View it at: https://docs.google.com/spreadsheets/d/{spreadsheet_id}")

if __name__ == "__main__":
    main()
