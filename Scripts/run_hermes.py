import os
import sys
import subprocess
import json
import argparse

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

HERMES_PYTHON = r"C:\Users\namo_\AppData\Local\hermes\hermes-agent\venv\Scripts\python.exe"
HERMES_DIR = r"C:\Users\namo_\AppData\Local\hermes\hermes-agent"
DEFAULT_MODEL = "upstage/solar-pro4:free"

def run_hermes(query: str, model: str = DEFAULT_MODEL, timeout: int = 1800):
    """
    Executes Hermes Agent headlessly with a given query and returns the execution result.
    """
    if not os.path.exists(HERMES_PYTHON):
        print(f"Error: Hermes Python binary not found at {HERMES_PYTHON}")
        return False, "Hermes Python binary missing"
        
    cmd = [
        HERMES_PYTHON,
        "run_agent.py",
        "--model", model,
        "--query", query
    ]
    
    print(f"🚀 Launching Hermes Agent with query: {query[:60]}...")
    try:
        result = subprocess.run(
            cmd,
            cwd=HERMES_DIR,
            capture_output=True,
            text=True,
            timeout=timeout,
            encoding="utf-8"
        )
        if result.returncode == 0:
            print("✅ Hermes Agent completed execution successfully.")
            return True, result.stdout
        else:
            print(f"❌ Hermes Agent failed with return code {result.returncode}")
            return False, result.stderr
    except subprocess.TimeoutExpired:
        print(f"⏱️ Hermes Agent timed out after {timeout} seconds.")
        return False, "Timeout expired"
    except Exception as e:
        print(f"⚠️ Exception running Hermes Agent: {str(e)}")
        return False, str(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Malli's Automation Helper for Hermes Agent")
    parser.add_argument("query", type=str, help="Prompt query to send to Hermes Agent")
    parser.add_argument("--model", type=str, default=DEFAULT_MODEL, help="Model to use in Hermes")
    args = parser.parse_args()
    
    success, output = run_hermes(args.query, args.model)
    sys.exit(0 if success else 1)
