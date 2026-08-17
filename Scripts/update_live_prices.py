import json
import os
import yfinance as yf

f1 = r'C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace\Portfolios\Namo_Real_Portfolio\current_holdings.json'

with open(f1, 'r', encoding='utf-8') as f:
    d = json.load(f)

print("Fetching latest prices from Yahoo Finance...")

total_value = 0
total_cost = 0

for h in d['holdings']:
    ticker = h['ticker']
    yf_ticker = ticker
    if ticker == 'BRK.B':
        yf_ticker = 'BRK-B'
    
    try:
        tk = yf.Ticker(yf_ticker)
        data = tk.history(period="1d")
        if not data.empty:
            current_price = float(data['Close'].iloc[-1])
            h['current_price'] = round(current_price, 2)
            print(f"Updated {ticker} to ${h['current_price']}")
        else:
            print(f"Could not fetch data for {ticker}, keeping old price ${h.get('current_price', 0)}")
    except Exception as e:
        print(f"Error fetching {ticker}: {e}")
    
    cost = h['shares'] * h['average_cost']
    value = h['shares'] * h.get('current_price', 0)
    
    h['total_value'] = round(value, 2)
    h['pl_usd'] = round(value - cost, 2)
    h['pl_pct'] = round((h['pl_usd'] / cost * 100) if cost > 0 else 0, 2)
    
    total_value += h['total_value']
    total_cost += cost

d['total_value'] = round(total_value, 2)
d['total_cost'] = round(total_cost, 2)
d['total_pl'] = round(total_value - total_cost, 2)
d['pl_percentage'] = round((d['total_pl'] / d['total_cost'] * 100) if d['total_cost'] > 0 else 0, 2)
d['current_nav'] = d['total_value']
from datetime import datetime
d['last_updated'] = datetime.now().strftime("%Y-%m-%d")

with open(f1, 'w', encoding='utf-8') as f:
    json.dump(d, f, indent=2, ensure_ascii=False)

os.chdir(r'C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace')
os.system('python Scripts\\copy_real_portfolio.py')

print(f"\nDone! New NAV: ${d['total_value']}, Total P/L: ${d['total_pl']} ({d['pl_percentage']}%)")
