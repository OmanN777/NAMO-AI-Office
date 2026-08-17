import os
import sys
import json
from datetime import datetime, date, timedelta
import yfinance as yf
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Paths
workspace_dir = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
credentials_path = os.path.join(workspace_dir, "gmail_api", "credentials.json")
token_path = os.path.join(workspace_dir, "gmail_api", "token.json")
calendar_id_path = os.path.join(workspace_dir, "gmail_api", "calendar_id.txt")

oman_portfolio_path = os.path.join(workspace_dir, "Portfolios", "Oman_Mock_Portfolio", "holdings.json")
real_portfolio_path = os.path.join(workspace_dir, "Portfolios", "Namo_History", "my_portfolio.json")

# Combined scopes including Sheets, Drive, and Calendar
SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/calendar'
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
            
    # Check if we need to request new credentials (e.g. if scopes were updated)
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
                sys.exit(1)
            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)
            
        with open(token_path, 'w', encoding='utf-8') as token_file:
            token_file.write(creds.to_json())
            print("💾 Saved new OAuth token to token.json")
            
    return creds

def get_or_create_calendar(service):
    calendar_id = None
    if os.path.exists(calendar_id_path):
        with open(calendar_id_path, 'r', encoding='utf-8') as f:
            calendar_id = f.read().strip()
            
    if calendar_id:
        try:
            service.calendars().get(calendarId=calendar_id).execute()
            print(f"ℹ️ Found existing custom Calendar ID: {calendar_id}")
            return calendar_id
        except Exception:
            print("⚠️ Saved Calendar ID not found or inaccessible. Creating a new one...")
            
    # Create a secondary calendar
    calendar_body = {
        'summary': 'Antigravity Investment & Tasks',
        'timeZone': 'Asia/Bangkok'
    }
    created_calendar = service.calendars().insert(body=calendar_body).execute()
    calendar_id = created_calendar['id']
    
    with open(calendar_id_path, 'w', encoding='utf-8') as f:
        f.write(calendar_id)
        
    print(f"✅ Created dedicated secondary calendar: 'Antigravity Investment & Tasks' (ID: {calendar_id})")
    return calendar_id

def get_all_tickers():
    tickers = set()
    # Read Oman holdings
    if os.path.exists(oman_portfolio_path):
        with open(oman_portfolio_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for h in data.get("holdings", []):
                tickers.add(h.get("ticker"))
    # Read Namo real holdings
    if os.path.exists(real_portfolio_path):
        with open(real_portfolio_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for h in data.get("holdings", []):
                tickers.add(h.get("ticker"))
                
    # Filter out empty or dummy tickers
    return [t for t in tickers if t and t != 'XYZ']

def fetch_earnings_dates(tickers):
    print(f"🔍 Fetching upcoming earnings dates for {len(tickers)} tickers via yfinance...")
    earnings_map = {}
    
    for t in tickers:
        try:
            # yfinance handles tickers like BRK.B by swapping dot with dash
            yf_ticker = t.replace('.', '-')
            ticker_obj = yf.Ticker(yf_ticker)
            cal = ticker_obj.calendar
            
            if cal and isinstance(cal, dict):
                dates = cal.get('Earnings Date') or cal.get('Earnings Dates')
                if dates and isinstance(dates, list):
                    # Keep the first date found
                    earnings_date = dates[0]
                    # Convert to string date YYYY-MM-DD
                    if isinstance(earnings_date, (datetime, date)):
                        date_str = earnings_date.strftime("%Y-%m-%d")
                    else:
                        date_str = str(earnings_date)
                    earnings_map[t] = date_str
                    print(f"   - {t}: Earnings Date is {date_str}")
        except Exception as e:
            # Silent fail for individual stock scraper errors
            pass
            
    return earnings_map

def clear_upcoming_events(service, calendar_id):
    # Clear events in the next 120 days to prevent duplicates
    now = datetime.utcnow().isoformat() + 'Z'
    future = (datetime.utcnow() + timedelta(days=120)).isoformat() + 'Z'
    
    try:
        events_result = service.events().list(
            calendarId=calendar_id, 
            timeMin=now,
            timeMax=future,
            singleEvents=True
        ).execute()
        
        events = events_result.get('items', [])
        if events:
            print(f"🧹 Clearing {len(events)} upcoming automated events in calendar...")
            for event in events:
                service.events().delete(calendarId=calendar_id, eventId=event['id']).execute()
    except Exception as e:
        print(f"⚠️ Failed to clear calendar events: {e}")

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass
        
    print("🔄 Starting Google Calendar Synchronization...")
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)
    calendar_id = get_or_create_calendar(service)
    
    # Get tickers & fetch earnings dates
    tickers = get_all_tickers()
    earnings_map = fetch_earnings_dates(tickers)
    
    if not earnings_map:
        print("⚠️ No upcoming earnings dates found to sync.")
        return
        
    # Clear old future events to prevent clutter
    clear_upcoming_events(service, calendar_id)
    
    # Sync new earnings events
    for ticker, e_date in earnings_map.items():
        try:
            event_body = {
                'summary': f"📊 {ticker} Earnings Release",
                'description': f"Consensus upcoming earnings report release date for {ticker} (sourced via Antigravity). Check financial charts and analyst expectations before market open.",
                'start': {
                    'date': e_date,
                    'timeZone': 'Asia/Bangkok',
                },
                'end': {
                    'date': (datetime.strptime(e_date, "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d"),
                    'timeZone': 'Asia/Bangkok',
                },
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                        {'method': 'popup', 'minutes': 24 * 60},  # 1 day warning
                        {'method': 'popup', 'minutes': 60}       # 1 hour warning
                    ]
                }
            }
            
            created_event = service.events().insert(calendarId=calendar_id, body=event_body).execute()
            print(f"📅 Added Event: {created_event.get('summary')} on {e_date}")
        except Exception as e:
            print(f"⚠️ Failed to add event for {ticker}: {e}")
            
    print("🎉 Google Calendar sync completed successfully!")

if __name__ == "__main__":
    main()
