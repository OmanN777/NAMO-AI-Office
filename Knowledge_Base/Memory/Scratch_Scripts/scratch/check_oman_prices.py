import yfinance as yf
for t in ['VRT', 'AVGO', 'CRM', 'GOOGL', 'CCJ']:
    try:
        tk = yf.Ticker(t)
        data = tk.history(period='1d')
        if not data.empty:
            print(f'{t}: {data["Close"].iloc[-1]:.2f}')
    except Exception as e:
        print(e)
