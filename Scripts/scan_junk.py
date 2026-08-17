import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

folders_to_check = [
    r"C:\Users\namo_\AppData\Local\Temp",
    r"C:\Users\namo_\AppData\Local\pip\cache",
    r"C:\Users\namo_\AppData\Local\npm-cache",
    r"C:\Users\namo_\AppData\Local\Microsoft\Windows\INetCache",
    r"C:\Users\namo_\AppData\Local\CrashDumps",
    r"C:\Users\namo_\.cache",
    r"C:\Users\namo_\AppData\Local\Google\Chrome\User Data\Default\Cache",
    r"C:\Users\namo_\AppData\Local\ms-playwright",
    r"C:\Windows\Temp",
]

def get_dir_size(path):
    total = 0
    count = 0
    if not os.path.exists(path):
        return 0, 0
    try:
        for root, dirs, files in os.walk(path):
            for f in files:
                fp = os.path.join(root, f)
                try:
                    total += os.path.getsize(fp)
                    count += 1
                except:
                    pass
    except:
        pass
    return total, count

print("--- JUNK / TEMP DIRECTORIES SCAN ---")
for f in folders_to_check:
    size, count = get_dir_size(f)
    size_mb = size / (1024 * 1024)
    size_gb = size / (1024 * 1024 * 1024)
    if size_gb >= 1.0:
        print(f"📦 {f}: {size_gb:.2f} GB ({count:,} files)")
    else:
        print(f"📁 {f}: {size_mb:.2f} MB ({count:,} files)")
