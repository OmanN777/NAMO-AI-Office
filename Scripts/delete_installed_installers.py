import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

downloads_dir = r"C:\Users\namo_\Downloads"

# Installer patterns / extensions
installer_extensions = ['.msi', '.xapk', '.apk', '.iso', '.dmg']
installer_keywords = ['setup', 'installer', 'install', 'x64', 'win64', 'x86_64', 'windows', 'update', 'desktop-runtime']

deleted_files = []
total_freed = 0

if os.path.exists(downloads_dir):
    for f in os.listdir(downloads_dir):
        fp = os.path.join(downloads_dir, f)
        if os.path.isfile(fp):
            ext = os.path.splitext(f)[1].lower()
            name_lower = f.lower()
            
            is_installer = False
            # Check extension
            if ext in installer_extensions:
                is_installer = True
            elif ext == '.exe':
                # Check if it looks like an installer
                if any(kw in name_lower for kw in installer_keywords) or any(name in name_lower for name in ['obsidian', 'postman', 'claude', 'trae', 'notion', 'teamviewer', 'surfshark', 'dbeaver', 'cloudflared', 'git', 'node', 'python', 'vlc', 'zoom', 'discord', 'spotify']):
                    is_installer = True
            
            if is_installer:
                try:
                    sz = os.path.getsize(fp)
                    os.remove(fp)
                    total_freed += sz
                    deleted_files.append((f, sz))
                except Exception as e:
                    print(f"Error deleting {f}: {e}")

print("=== DELETED INSTALLER FILES FROM DOWNLOADS ===")
for f, sz in deleted_files:
    print(f"🗑️ Deleted: {f} ({sz / (1024**2):.2f} MB)")

print(f"\n🎉 Total freed from Downloads: {total_freed / (1024**3):.2f} GB ({len(deleted_files)} files deleted)")
