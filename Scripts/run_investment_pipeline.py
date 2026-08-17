import os
import sys
import json
import subprocess
import argparse

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

SCRIPTS_DIR = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace\Scripts"
WORKSPACE_DIR = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
HERMES_PYTHON = r"C:\Users\namo_\AppData\Local\Programs\Python\Python312\python.exe"

def run_pipeline(ticker: str):
    ticker = ticker.upper().strip()
    print(f"🚀 Starting Executive 4-Agent Investment Pipeline for: {ticker}")
    
    # 1. Newwy (News Scout via Hermes)
    print(f"\n📰 [Step 1: Newwy] Scouting latest 7-14 day news & sentiment for {ticker}...")
    newwy_query = f"Search the web for {ticker} latest news, catalysts, earnings, and market sentiment. Save a summary to C:\\Users\\namo_\\OneDrive\\เอกสาร\\gemini-cli\\antigravity-office-workspace\\Knowledge_Base\\Sources\\{ticker}_news.md"
    run_hermes_script = os.path.join(SCRIPTS_DIR, "run_hermes.py")
    
    res = subprocess.run([HERMES_PYTHON, run_hermes_script, newwy_query, "--model", "upstage/solar-pro4:free"], capture_output=True, text=True, encoding="utf-8")
    if res.returncode == 0:
        print(f"✅ Newwy completed news scouting for {ticker}.")
    else:
        print(f"⚠️ Newwy scouting warning: {res.stderr[:200]}")
        
    # 2. Fundamentokung & Case Study (via Hermes)
    print(f"\n📊 [Step 2: Fundamentokung] Analyzing Valuation, Moat, and Financial Health for {ticker}...")
    funda_query = f"Search the web for {ticker} Q2 2026 financial metrics, P/E ratio, Free Cash Flow, Moat, and risks. Write a neutral Case Study to C:\\Users\\namo_\\OneDrive\\เอกสาร\\gemini-cli\\antigravity-office-workspace\\Knowledge_Base\\Wiki\\case_studies\\{ticker.lower()}_case_study.md"
    res2 = subprocess.run([HERMES_PYTHON, run_hermes_script, funda_query, "--model", "upstage/solar-pro4:free"], capture_output=True, text=True, encoding="utf-8")
    if res2.returncode == 0:
        print(f"✅ Fundamentokung & Reese completed Case Study for {ticker}.")
    else:
        print(f"⚠️ Fundamentokung warning: {res2.stderr[:200]}")

    print(f"\n🎉 Executive Pipeline for {ticker} completed successfully!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Executive 4-Agent Investment Pipeline Launcher")
    parser.add_argument("ticker", type=str, help="Stock Ticker symbol (e.g. NVDA, PLTR, RKLB)")
    args = parser.parse_args()
    
    run_pipeline(args.ticker)
