import sys
import json
from datetime import datetime, date
from openbb import obb

def make_serializable(data):
    if isinstance(data, list):
        return [make_serializable(item) for item in data]
    elif isinstance(data, dict):
        return {key: make_serializable(value) for key, value in data.items()}
    elif isinstance(data, (datetime, date)):
        return data.isoformat()
    elif hasattr(data, "model_dump"):
        return make_serializable(data.model_dump())
    elif hasattr(data, "__dict__"):
        return make_serializable(data.__dict__)
    else:
        return data

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except AttributeError:
        pass # Python versions or environments where reconfigure is not available

    if len(sys.argv) < 3:
        print(json.dumps({"error": "Missing arguments. Usage: python openbb_fetcher.py [price|news|profile] [ticker]"}))
        return

    command = sys.argv[1]
    ticker = sys.argv[2]

    try:
        if command == "price":
            res = obb.equity.price.historical(ticker, provider="yfinance", limit=5)
            df = res.to_dataframe()
            df.index = df.index.astype(str)
            data = df.to_dict(orient="index")
            print(json.dumps({"ticker": ticker, "prices": data}, ensure_ascii=False))
        elif command == "news":
            res = obb.news.company(symbol=ticker, provider="yfinance", limit=5)
            results = res.results if hasattr(res, "results") else res
            serializable = make_serializable(results)
            print(json.dumps({"ticker": ticker, "news": serializable}, ensure_ascii=False))
        elif command == "profile":
            res = obb.equity.profile(ticker, provider="yfinance")
            results = res.results if hasattr(res, "results") else res
            serializable = make_serializable(results)
            print(json.dumps({"ticker": ticker, "profile": serializable}, ensure_ascii=False))
        else:
            print(json.dumps({"error": f"Unknown command: {command}"}))
    except Exception as e:
        print(json.dumps({"error": str(e)}))

if __name__ == "__main__":
    main()
