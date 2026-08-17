import json
import os

base_dir = r'C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace'
source_path = os.path.join(base_dir, 'Portfolios', 'Namo_Real_Portfolio', 'current_holdings.json')
dest_path = os.path.join(base_dir, 'Portfolios', 'Namo_History', 'my_portfolio.json')

with open(source_path, 'r', encoding='utf-8') as f:
    real_data = json.load(f)

# Fill in missing global fields for dashboard
real_data['cash_balance'] = 0.0
real_data['total_deposited'] = real_data.get('total_cost', 0.0)
real_data['realized_pl_total'] = 0.0
real_data['total_dividends'] = 0.0

total_val = real_data.get('total_value', 0.0)

# Fill in missing holding fields
for h in real_data.get('holdings', []):
    h_val = h.get('total_value', 0.0)
    h['allocation_pct'] = round((h_val / total_val) * 100, 2) if total_val > 0 else 0.0
    h['days_held'] = 0  # Placeholder, user can update
    h['realized_pl'] = 0.0
    h['dividends'] = 0.0
    h['trades_count'] = 1

with open(dest_path, 'w', encoding='utf-8') as f:
    json.dump(real_data, f, indent=2, ensure_ascii=False)

print("Data migrated successfully.")
