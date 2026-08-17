import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

user_dir = r"C:\Users\namo_"
entries = os.listdir(user_dir)

results = []
for entry in entries:
    full_path = os.path.join(user_dir, entry)
    if os.path.isdir(full_path) and not entry.startswith('.'):
        total = 0
        try:
            for root, dirs, files in os.walk(full_path):
                for f in files:
                    try:
                        total += os.path.getsize(os.path.join(root, f))
                    except:
                        pass
            results.append((entry, total))
        except:
            pass

results.sort(key=lambda x: x[1], reverse=True)
print("--- TOP USER FOLDERS BY SIZE ---")
for name, size in results[:10]:
    print(f"📁 {name}: {size / (1024**3):.2f} GB")
