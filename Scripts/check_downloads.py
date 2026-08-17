import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

downloads_dir = r"C:\Users\namo_\Downloads"
large_files = []

if os.path.exists(downloads_dir):
    for f in os.listdir(downloads_dir):
        fp = os.path.join(downloads_dir, f)
        if os.path.isfile(fp):
            try:
                sz = os.path.getsize(fp)
                if sz > 50 * 1024 * 1024:  # > 50 MB
                    large_files.append((f, sz))
            except:
                pass

large_files.sort(key=lambda x: x[1], reverse=True)
print("=== LARGE FILES IN DOWNLOADS (>50MB) ===")
total_sz = 0
for f, sz in large_files[:20]:
    total_sz += sz
    print(f"📦 {f}: {sz / (1024**2):.2f} MB")

print(f"\nTotal Top Large Downloads: {total_sz / (1024**3):.2f} GB")
