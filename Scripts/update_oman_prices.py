import json
import os
import yfinance as yf
from datetime import datetime
import shutil

# Paths
portfolio_dir = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace\Portfolios\Oman_Mock_Portfolio"
portfolio_path = os.path.join(portfolio_dir, "holdings.json")
history_dir = os.path.join(portfolio_dir, "history")

with open(portfolio_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

tickers = [h['ticker'] for h in data['holdings'] if h['ticker'] != 'XYZ']

print(f"Fetching prices for {len(tickers)} stocks and SPY...")
prices = {}
prev_prices = {}

try:
    # Add SPY to fetch list for benchmark
    fetch_list = tickers + ["SPY"]
    tickers_str = " ".join(fetch_list)
    tickers_data = yf.Tickers(tickers_str)
    
    for ticker in fetch_list:
        try:
            info = tickers_data.tickers[ticker].info
            if 'currentPrice' in info:
                prices[ticker] = info['currentPrice']
            elif 'regularMarketPrice' in info:
                prices[ticker] = info['regularMarketPrice']
            elif 'previousClose' in info:
                prices[ticker] = info['previousClose']
                
            if 'previousClose' in info:
                prev_prices[ticker] = info['previousClose']
            elif 'regularMarketPreviousClose' in info:
                prev_prices[ticker] = info['regularMarketPreviousClose']
        except Exception as e:
            print(f"Could not fetch {ticker}: {e}")
            
except Exception as e:
    print(f"Batch fetch failed: {e}")

# Calculate SPY return
spy_return = 0.0
if "SPY" in prices and "SPY" in prev_prices:
    spy_change = prices["SPY"] - prev_prices["SPY"]
    spy_return = (spy_change / prev_prices["SPY"]) * 100

today = datetime.now().strftime("%Y-%m-%d")
last_updated = data.get("last_updated", "")

# If it's a new day, backup current holdings to history before updating
if last_updated and last_updated != today:
    history_file = os.path.join(history_dir, f"{last_updated}.json")
    if not os.path.exists(history_file):
        shutil.copy2(portfolio_path, history_file)
        print(f"Backed up {last_updated} to history.")

    # Add funding since it's a new day (DCA allowance $20/day per elapsed day)
    try:
        from datetime import datetime as dt
        dt_last = dt.strptime(last_updated, "%Y-%m-%d")
        dt_today = dt.strptime(today, "%Y-%m-%d")
        elapsed_days = (dt_today - dt_last).days
        if elapsed_days < 1:
            elapsed_days = 1
    except Exception as e:
        elapsed_days = 1
    funding = 20 * elapsed_days
    data["cash_balance"] += funding
    data["total_deposited"] += funding
    
    has_today = any(today in a for a in data.get("recommended_actions", []))
    if not has_today:
        data.setdefault("recommended_actions", []).append(
            f"MALLI-DAILY UPDATE ({today}): Added daily funding (${funding} for {elapsed_days} days). Cash is ${data['cash_balance']:.2f}. Executing automatic price fetch."
        )

total_value = 0
total_cost = 0
daily_change_usd = 0

for h in data["holdings"]:
    t = h["ticker"]
    
    if t in prices and prices[t] is not None:
        h["current_price"] = prices[t]
        
    prev_price = prev_prices.get(t, h["current_price"])
    change_per_share = h["current_price"] - prev_price
    daily_change_usd += change_per_share * h["shares"]
    
    h["total_value"] = h["current_price"] * h["shares"]
    h["pl_usd"] = h["total_value"] - (h["average_cost"] * h["shares"])
    if (h["average_cost"] * h["shares"]) > 0:
        h["pl_pct"] = (h["pl_usd"] / (h["average_cost"] * h["shares"])) * 100
    else:
        h["pl_pct"] = 0
    
    total_value += h["total_value"]
    total_cost += h["average_cost"] * h["shares"]

for h in data["holdings"]:
    if total_value > 0:
        h["allocation_pct"] = (h["total_value"] / total_value) * 100
    else:
        h["allocation_pct"] = 0

data["total_value"] = total_value
data["total_cost"] = total_cost
data["total_pl"] = total_value - total_cost
if total_cost > 0:
    data["pl_percentage"] = (data["total_pl"] / total_cost) * 100
else:
    data["pl_percentage"] = 0
    
data["current_nav"] = total_value + data.get("cash_balance", 0)

data["daily_change_usd"] = daily_change_usd
prev_nav = data["current_nav"] - daily_change_usd
if prev_nav > 0:
    data["daily_change_pct"] = (daily_change_usd / prev_nav) * 100
else:
    data["daily_change_pct"] = 0

# Append to performance history if it's a new day or update today's
perf_history = data.get("performance_history", [])
existing_entry = next((item for item in perf_history if item["date"] == today), None)
if existing_entry:
    existing_entry["oman_return"] = data["daily_change_pct"]
    existing_entry["spy_return"] = spy_return
else:
    perf_history.append({
        "date": today,
        "oman_return": data["daily_change_pct"],
        "spy_return": spy_return
    })
data["performance_history"] = perf_history

data["last_updated"] = today

with open(portfolio_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Oman Portfolio successfully updated! Daily Change: ${daily_change_usd:.2f} ({data['daily_change_pct']:.2f}%)")
