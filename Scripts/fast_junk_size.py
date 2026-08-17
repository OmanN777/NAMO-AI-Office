import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

targets = [
    ("Windows User Temp", os.environ.get("TEMP", r"C:\Users\namo_\AppData\Local\Temp")),
    ("Pip Cache", os.path.expandvars(r"%LOCALAPPDATA%\pip\cache")),
    ("NPM Cache", os.path.expandvars(r"%LOCALAPPDATA%\npm-cache")),
    ("Crash Dumps", os.path.expandvars(r"%LOCALAPPDATA%\CrashDumps")),
    ("Downloads", r"C:\Users\namo_\Downloads"),
    ("Windows Temp", r"C:\Windows\Temp"),
    ("Antigravity Brain Temp", r"C:\Users\namo_\.gemini\antigravity-cli\brain"),
    ("Hermes Local Data", r"C:\Users\namo_\AppData\Local\hermes"),
]

def fast_dir_size(path):
    total = 0
    count = 0
    if not os.path.exists(path):
        return 0, 0
    try:
        with os.scandir(path) as it:
            for entry in it:
                try:
                    if entry.is_file(follow_symlinks=False):
                        total += entry.stat().st_size
                        count += 1
                    elif entry.is_dir(follow_symlinks=False):
                        # 1 level recursion
                        with os.scandir(entry.path) as sub_it:
                            for sub in sub_it:
                                try:
                                    if sub.is_file(follow_symlinks=False):
                                        total += sub.stat().st_size
                                        count += 1
                                    elif sub.is_dir(follow_symlinks=False):
                                        # 2 level recursion
                                        for root, dirs, files in os.walk(sub.path):
                                            for f in files:
                                                try:
                                                    total += os.path.getsize(os.path.join(root, f))
                                                    count += 1
                                                except:
                                                    pass
                                except:
                                    pass
                except:
                    pass
    except:
        pass
    return total, count

print("=== JUNK & CACHE FOLDER AUDIT ===")
for name, path in targets:
    if os.path.exists(path):
        size_bytes, count = fast_dir_size(path)
        size_gb = size_bytes / (1024 ** 3)
        size_mb = size_bytes / (1024 ** 2)
        if size_gb >= 1.0:
            print(f"📦 {name}: {size_gb:.2f} GB ({count:,} files) -> {path}")
        else:
            print(f"📁 {name}: {size_mb:.2f} MB ({count:,} files) -> {path}")
