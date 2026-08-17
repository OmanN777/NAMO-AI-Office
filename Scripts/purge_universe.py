import json
import os
import shutil

# Paths
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
universe_path = os.path.join(base_dir, 'Portfolios', 'Oman_Mock_Portfolio', 'universe.json')
briefs_dir = os.path.join(base_dir, 'Knowledge_Base', 'Briefs')
sources_dir = os.path.join(base_dir, 'Knowledge_Base', 'Sources')

print("Initiating Purge Protocol...")

# Load Universe
with open(universe_path, 'r', encoding='utf-8') as f:
    u = json.load(f)

items = u.get('items', [])
to_delete = [item for item in items if item.get('status') == 'DELETE']
kept_items = [item for item in items if item.get('status') != 'DELETE']

if not to_delete:
    print("No stocks marked with 'DELETE' status found. Universe is clean.")
else:
    print(f"Found {len(to_delete)} stock(s) marked for deletion.")
    
    for item in to_delete:
        ticker = item['ticker']
        print(f"\n--- Purging {ticker} ---")
        
        # 1. Delete Brief File
        brief_file = os.path.join(briefs_dir, f"{ticker}.md")
        if os.path.exists(brief_file):
            os.remove(brief_file)
            print(f"Deleted Brief: {brief_file}")
        else:
            print(f"Brief not found (already deleted): {brief_file}")
            
        # 2. Delete Sources Folder
        source_folder = os.path.join(sources_dir, ticker)
        if os.path.exists(source_folder):
            shutil.rmtree(source_folder)
            print(f"Deleted Sources Directory: {source_folder}")
        else:
            print(f"Sources not found (already deleted): {source_folder}")
            
    # 3. Update universe.json
    u['items'] = kept_items
    with open(universe_path, 'w', encoding='utf-8') as f:
        json.dump(u, f, indent=2, ensure_ascii=False)
        
    print(f"\nPurge Complete. Removed {len(to_delete)} stock(s) from universe.json.")
