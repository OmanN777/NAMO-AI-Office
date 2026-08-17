import os
import sys
import shutil
import time
import subprocess

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

freed_bytes = 0

print("🧹 Starting Safe Storage Cleanup...")

# 1. Pip Cache Purge
print("\n1. Cleaning Pip Cache...")
try:
    res = subprocess.run([sys.executable, "-m", "pip", "cache", "purge"], capture_output=True, text=True)
    print("   ", res.stdout.strip())
except Exception as e:
    print("   Error purging pip cache:", e)

# 2. NPM Cache Purge
print("\n2. Cleaning NPM Cache...")
try:
    npm_path = shutil.which("npm") or shutil.which("npm.cmd")
    if npm_path:
        res = subprocess.run([npm_path, "cache", "clean", "--force"], capture_output=True, text=True, shell=True)
        print("   ", res.stdout.strip() or res.stderr.strip() or "NPM cache cleaned.")
except Exception as e:
    print("   Error cleaning npm cache:", e)

# 3. CrashDumps
print("\n3. Cleaning Windows Crash Dumps...")
crash_dir = os.path.expandvars(r"%LOCALAPPDATA%\CrashDumps")
if os.path.exists(crash_dir):
    c_freed = 0
    for f in os.listdir(crash_dir):
        fp = os.path.join(crash_dir, f)
        try:
            sz = os.path.getsize(fp)
            os.remove(fp)
            c_freed += sz
        except:
            pass
    print(f"   Cleared CrashDumps: {c_freed / (1024**2):.2f} MB")
    freed_bytes += c_freed

# 4. User Temp Folder (files not in use / older than 1 hour)
print("\n4. Cleaning User Temp Files...")
temp_dir = os.environ.get("TEMP", r"C:\Users\namo_\AppData\Local\Temp")
t_freed = 0
t_deleted = 0
now = time.time()
if os.path.exists(temp_dir):
    for root, dirs, files in os.walk(temp_dir, topdown=False):
        for f in files:
            fp = os.path.join(root, f)
            try:
                # delete if older than 1 hour
                if now - os.path.getmtime(fp) > 3600:
                    sz = os.path.getsize(fp)
                    os.remove(fp)
                    t_freed += sz
                    t_deleted += 1
            except:
                pass
        for d in dirs:
            dp = os.path.join(root, d)
            try:
                os.rmdir(dp)
            except:
                pass
    print(f"   Cleared Temp: {t_freed / (1024**2):.2f} MB ({t_deleted:,} files)")
    freed_bytes += t_freed

print(f"\n🎉 Safe automated cleanup completed! Direct temp/cache freed: {freed_bytes / (1024**2):.2f} MB + NPM/Pip caches purged!")
