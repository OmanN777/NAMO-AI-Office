import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

user_dir = r"C:\Users\namo_"
targets = [
    os.path.join(user_dir, "Downloads"),
    os.path.join(user_dir, "Videos"),
    os.path.join(user_dir, "Desktop"),
    os.path.join(user_dir, "Documents"),
    os.path.join(user_dir, "AppData", "Local", "Roblox"),
    os.path.join(user_dir, "AppData", "Local", "Discord"),
    os.path.join(user_dir, "AppData", "Roaming", "Spotify"),
    os.path.join(user_dir, "AppData", "Local", "Spotify"),
    os.path.join(user_dir, "AppData", "Local", "DBeaverData"),
    os.path.join(user_dir, "AppData", "Local", "Programs"),
    r"C:\Program Files",
    r"C:\Program Files (x86)",
    r"C:\XboxGames",
    r"C:\Riot Games",
    r"C:\Games"
]

print("=== FOLDER SIZE ANALYSIS ===")
for p in targets:
    if os.path.exists(p):
        total = 0
        file_count = 0
        try:
            for root, dirs, files in os.walk(p):
                for f in files:
                    try:
                        total += os.path.getsize(os.path.join(root, f))
                        file_count += 1
                    except:
                        pass
            gb = total / (1024**3)
            mb = total / (1024**2)
            if gb >= 1.0:
                print(f"📦 {p}: {gb:.2f} GB ({file_count:,} files)")
            else:
                print(f"📁 {p}: {mb:.2f} MB ({file_count:,} files)")
        except Exception as e:
            print(f"Error {p}: {e}")
