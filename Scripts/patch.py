import os

routes = [
    r'dashboard\src\app\api\portfolio\route.ts',
    r'dashboard\src\app\api\portfolio\thesis\route.ts',
    r'dashboard\src\app\api\real_portfolio\route.ts',
    r'dashboard\src\app\api\stock\[ticker]\route.ts',
    r'dashboard\src\app\api\universe\route.ts'
]

for route in routes:
    if not os.path.exists(route): continue
    with open(route, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Oman replacements
    content = content.replace("'..', 'portfolio',", "'..', 'Portfolios', 'Oman_Mock_Portfolio',")
    
    # Real Portfolio / My_Portfolio replacements
    content = content.replace("'..', 'My_Portfolio',", "'..', 'Portfolios', 'Namo_History',")
    content = content.replace("'..', 'real_portfolio',", "'..', 'Portfolios', 'Namo_Real_Portfolio',")
    
    # Stock route uses projectRoot
    content = content.replace("projectRoot, 'portfolio',", "projectRoot, 'Portfolios', 'Oman_Mock_Portfolio',")

    with open(route, 'w', encoding='utf-8') as f:
        f.write(content)

# Update Python Scripts
copy_script = r'Scripts\copy_real_portfolio.py'
if os.path.exists(copy_script):
    with open(copy_script, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace(r'real_portfolio\current_holdings.json', r'Portfolios\Namo_Real_Portfolio\current_holdings.json')
    c = c.replace(r'My_Portfolio\my_portfolio.json', r'Portfolios\Namo_History\my_portfolio.json')
    with open(copy_script, 'w', encoding='utf-8') as f:
        f.write(c)

live_script = r'Scripts\update_live_prices.py'
if os.path.exists(live_script):
    with open(live_script, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace(r'real_portfolio\current_holdings.json', r'Portfolios\Namo_Real_Portfolio\current_holdings.json')
    c = c.replace("'python copy_real_portfolio.py'", "'python Scripts\\\\copy_real_portfolio.py'")
    with open(live_script, 'w', encoding='utf-8') as f:
        f.write(c)

# Update Oman Script (now needs to use relative paths if run from root)
oman_script = r'Portfolios\Oman_Mock_Portfolio\update_portfolio.py'
if os.path.exists(oman_script):
    with open(oman_script, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace("portfolio_path = 'holdings.json'", "portfolio_path = r'Portfolios\Oman_Mock_Portfolio\holdings.json'")
    c = c.replace("history_path = 'nav_history.md'", "history_path = r'Portfolios\Oman_Mock_Portfolio\nav_history.md'")
    with open(oman_script, 'w', encoding='utf-8') as f:
        f.write(c)

print('Patching complete')
