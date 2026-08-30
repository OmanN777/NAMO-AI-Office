import os
import sys
import json
import requests

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# FMP API Helper
# Free tier key can be placed in environment or config
FMP_API_KEY = os.environ.get('FMP_API_KEY', 'demo')

def get_company_cashflow(ticker='CRM'):
    print(f'Fetching cash flow metrics for {ticker}...')
    url = f'https://financialmodelingprep.com/api/v3/cash-flow-statement/{ticker}?period=annual&limit=5&apikey={FMP_API_KEY}'
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            return data
        else:
            print(f'FMP API returned status {resp.status_code}', file=sys.stderr)
            return []
    except Exception as e:
        print(f'Error fetching FMP data: {e}', file=sys.stderr)
        return []

if __name__ == '__main__':
    ticker = sys.argv[1] if len(sys.argv) > 1 else 'AAPL'
    res = get_company_cashflow(ticker)
    print(f'Loaded {len(res)} financial periods for {ticker}.')
