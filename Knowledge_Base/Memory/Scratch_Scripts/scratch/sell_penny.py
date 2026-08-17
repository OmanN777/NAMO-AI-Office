import json
import os

portfolio_path = 'My_Portfolio/my_portfolio.json'

with open(portfolio_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

tickers_to_sell = ['USBC', 'JUNS', 'SLAI', 'MBIO', 'NEON', 'FIG']
proceeds = 0.0
realized_loss = 0.0

new_holdings = []
for h in data['holdings']:
    if h['ticker'] in tickers_to_sell:
        proceeds += h['total_value']
        realized_loss += h['pl_usd']
    else:
        new_holdings.append(h)

data['holdings'] = new_holdings
data['cash_balance'] = data.get('cash_balance', 0.0) + proceeds
data['realized_pl_total'] = data.get('realized_pl_total', 0.0) + realized_loss

# Recalculate totals
total_value = data['cash_balance']
total_cost = data['cash_balance']  # Cash is worth its cost

for h in data['holdings']:
    total_value += h['total_value']
    total_cost += (h['shares'] * h['average_cost'])

data['total_value'] = round(total_value, 2)
data['total_cost'] = round(total_cost, 2)
data['total_pl'] = round(data['total_value'] - data['total_cost'], 2)
data['pl_percentage'] = round((data['total_pl'] / data['total_cost']) * 100, 2)

for h in data['holdings']:
    h['allocation_pct'] = round((h['total_value'] / data['total_value']) * 100, 2)

with open(portfolio_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'Sold {tickers_to_sell}. Proceeds: ${proceeds:.2f}, Realized Loss: ${realized_loss:.2f}')
print(f'New Cash Balance: ${data["cash_balance"]:.2f}, New NAV: ${data["total_value"]:.2f}')
