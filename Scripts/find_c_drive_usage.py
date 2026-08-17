import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def get_folder_size_fast(path, max_depth=3):
    total = 0
    try:
        for root, dirs, files in os.walk(path):
            depth = root[len(path):].count(os.sep)
            if depth > max_depth:
                del dirs[:]  # don't recurse deeper than max_depth
            for f in files:
                try:
                    total += os.path.getsize(os.path.join(root, f))
                except:
                    pass
    except:
        pass
    return total

print("=== 1. C:\\ ROOT DIRECTORIES ===")
root_dirs = ["C:\\Program Files", "C:\\Program Files (x86)", "C:\\Users", "C:\\Windows", "C:\\ProgramData", "C:\\Riot Games", "C:\\Games", "C:\\XboxGames"]
for rd in root_dirs:
    if os.path.exists(rd):
        size = get_folder_size_fast(rd, max_depth=5)
        print(f"📁 {rd}: {size / (1024**3):.2f} GB")

print("\n=== 2. C:\\Users\\namo_ USER DIRECTORIES ===")
user_sub = [
    r"C:\Users\namo_\AppData\Local",
    r"C:\Users\namo_\AppData\Roaming",
    r"C:\Users\namo_\Downloads",
    r"C:\Users\namo_\Documents",
    r"C:\Users\namo_\Desktop",
    r"C:\Users\namo_\Videos",
    r"C:\Users\namo_\Pictures",
    r"C:\Users\namo_\.gemini",
    r"C:\Users\namo_\.cache",
    r"C:\Users\namo_\.vscode",
    r"C:\Users\namo_\OneDrive",
]
for us in user_sub:
    if os.path.exists(us):
        size = get_folder_size_fast(us, max_depth=4)
        print(f"📁 {us}: {size / (1024**3):.2f} GB")
