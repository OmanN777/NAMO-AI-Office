import os
import sys
import time

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

game_roots = [
    r"C:\Program Files (x86)\Steam\steamapps\common",
    r"C:\Program Files\Epic Games",
    r"C:\Riot Games",
    r"C:\XboxGames",
    r"C:\Games",
    r"C:\Program Files",
    r"C:\Program Files (x86)",
    r"C:\Users\namo_\AppData\Local",
    r"C:\Users\namo_\AppData\Local\Programs",
    r"C:\Users\namo_\AppData\Roaming"
]

known_games = []

# Scan Steam
steam_common = r"C:\Program Files (x86)\Steam\steamapps\common"
if os.path.exists(steam_common):
    for d in os.listdir(steam_common):
        full_p = os.path.join(steam_common, d)
        if os.path.isdir(full_p):
            sz = sum(os.path.getsize(os.path.join(r, f)) for r, dirs, files in os.walk(full_p) for f in files if os.path.exists(os.path.join(r, f)))
            mtime = os.path.getmtime(full_p)
            known_games.append(("Steam: " + d, full_p, sz / (1024**3), time.strftime("%Y-%m-%d", time.localtime(mtime))))

# Scan Riot
riot_p = r"C:\Riot Games"
if os.path.exists(riot_p):
    for d in os.listdir(riot_p):
        full_p = os.path.join(riot_p, d)
        if os.path.isdir(full_p):
            sz = sum(os.path.getsize(os.path.join(r, f)) for r, dirs, files in os.walk(full_p) for f in files if os.path.exists(os.path.join(r, f)))
            mtime = os.path.getmtime(full_p)
            known_games.append(("Riot: " + d, full_p, sz / (1024**3), time.strftime("%Y-%m-%d", time.localtime(mtime))))

# Scan XboxGames
xbox_p = r"C:\XboxGames"
if os.path.exists(xbox_p):
    for d in os.listdir(xbox_p):
        full_p = os.path.join(xbox_p, d)
        if os.path.isdir(full_p):
            sz = sum(os.path.getsize(os.path.join(r, f)) for r, dirs, files in os.walk(full_p) for f in files if os.path.exists(os.path.join(r, f)))
            mtime = os.path.getmtime(full_p)
            known_games.append(("Xbox: " + d, full_p, sz / (1024**3), time.strftime("%Y-%m-%d", time.localtime(mtime))))

# Scan Epic Games
epic_p = r"C:\Program Files\Epic Games"
if os.path.exists(epic_p):
    for d in os.listdir(epic_p):
        full_p = os.path.join(epic_p, d)
        if os.path.isdir(full_p):
            sz = sum(os.path.getsize(os.path.join(r, f)) for r, dirs, files in os.walk(full_p) for f in files if os.path.exists(os.path.join(r, f)))
            mtime = os.path.getmtime(full_p)
            known_games.append(("Epic: " + d, full_p, sz / (1024**3), time.strftime("%Y-%m-%d", time.localtime(mtime))))

# Scan Roblox
roblox_p = r"C:\Users\namo_\AppData\Local\Roblox"
if os.path.exists(roblox_p):
    sz = sum(os.path.getsize(os.path.join(r, f)) for r, dirs, files in os.walk(roblox_p) for f in files if os.path.exists(os.path.join(r, f)))
    mtime = os.path.getmtime(roblox_p)
    known_games.append(("Roblox Platform", roblox_p, sz / (1024**3), time.strftime("%Y-%m-%d", time.localtime(mtime))))

# Other Program Files games
other_paths = [
    (r"C:\Program Files\Genshin Impact", "Genshin Impact"),
    (r"C:\Program Files\Honkai Star Rail", "Honkai: Star Rail"),
    (r"C:\Program Files\Wuthering Waves", "Wuthering Waves"),
    (r"C:\Program Files\Marvel Rivals", "Marvel Rivals"),
    (r"C:\Program Files\ZenlessZoneZero", "Zenless Zone Zero"),
]
for p, name in other_paths:
    if os.path.exists(p):
        sz = sum(os.path.getsize(os.path.join(r, f)) for r, dirs, files in os.walk(p) for f in files if os.path.exists(os.path.join(r, f)))
        mtime = os.path.getmtime(p)
        known_games.append((name, p, sz / (1024**3), time.strftime("%Y-%m-%d", time.localtime(mtime))))

known_games.sort(key=lambda x: x[2], reverse=True)

print("=== INSTALLED GAMES SCAN RESULTS ===")
for name, p, sz_gb, mod_date in known_games:
    print(f"🎮 {name}")
    print(f"   📂 Path: {p}")
    print(f"   💾 Size: {sz_gb:.2f} GB")
    print(f"   📅 Last Modified: {mod_date}")
    print()
