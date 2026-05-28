import json
import yfinance as yf
import os

filepath = 'real_portfolio/current_holdings.json'
with open(filepath, 'r') as f:
    data = json.load(f)

tickers = []
for h in data['holdings']:
    t = h['ticker']
    if t == 'BRK.B': t = 'BRK-B'
    if t not in tickers:
        tickers.append(t)

prices = {}
for t in tickers:
    try:
        ticker_obj = yf.Ticker(t)
        hist = ticker_obj.history(period='1d')
        if not hist.empty:
            prices[t] = float(hist['Close'].iloc[-1])
        else:
            prices[t] = ticker_obj.info.get('previousClose', 0)
    except Exception as e:
        print(f'Error fetching {t}: {e}')
        prices[t] = 0

print('Fetched prices:', prices)

if 'BRK-B' in prices:
    prices['BRK.B'] = prices['BRK-B']

total_value = 0
total_cost = 0
stale_tickers = []

for h in data['holdings']:
    t = h['ticker']
    p = prices.get(t, 0)
    if p > 0:
        h['current_price'] = round(p, 2)
        h['total_value'] = round(h['shares'] * p, 2)
        cost = h['shares'] * h['average_cost']
        h['pl_usd'] = round(h['total_value'] - cost, 2)
        if cost > 0:
            h['pl_pct'] = round((h['total_value'] - cost) / cost * 100, 2)
        else:
            h['pl_pct'] = 0
    else:
        stale_tickers.append(t)
    total_value += h['total_value']
    total_cost += (h['shares'] * h['average_cost'])

data['total_value'] = round(total_value, 2)
data['total_cost'] = round(total_cost, 2)
data['total_pl'] = round(total_value - total_cost, 2)
if total_cost > 0:
    data['pl_percentage'] = round((total_value - total_cost) / total_cost * 100, 2)
data['last_updated'] = '2026-05-23'
data['stale_tickers'] = stale_tickers

with open(filepath, 'w') as f:
    json.dump(data, f, indent=2)

print(f'Done. Total Value: {data["total_value"]}, P/L: {data["total_pl"]}')
