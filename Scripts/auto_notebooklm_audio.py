import os
import sys
import asyncio
from notebooklm import NotebookLMClient

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

WORKSPACE_DIR = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"

async def auto_create_and_generate_audio():
    print("==================================================")
    print("🎙️ Malli Autonomous NotebookLM Audio Generator")
    print("==================================================")
    
    async with NotebookLMClient() as client:
        # 1. Check or Create Notebook
        notebook_title = "Malli Executive HQ (Auto-Audio)"
        print(f"Creating notebook: '{notebook_title}'...")
        notebook = await client.notebooks.create(notebook_title)
        notebook_id = notebook.id
        print(f"✅ Notebook Created (ID: {notebook_id})")
        
        # 2. Add Sources automatically
        sources = [
            os.path.join(WORKSPACE_DIR, "Knowledge_Base", "Wiki", "case_studies", "crm_case_study.md"),
            os.path.join(WORKSPACE_DIR, "Knowledge_Base", "Wiki", "case_studies", "dell_ai_infrastructure_case_study.md"),
            os.path.join(WORKSPACE_DIR, "Knowledge_Base", "Reports", "daily", "2026-08-29-malli-daily.md")
        ]
        
        for src in sources:
            if os.path.exists(src):
                print(f"Uploading source: {os.path.basename(src)}...")
                await client.sources.add_file(notebook_id, src)
                print(f"✅ Added {os.path.basename(src)}")
                
        # 3. Trigger Audio Overview Generation Automatically!
        print("\n⚡ Triggering Audio Overview (Deep-Dive Podcast) Generation...")
        artifact = await client.artifacts.generate_audio(notebook_id)
        print("🎙️ Audio generation started! Waiting for audio processing...")
        
        # 4. Wait for audio completion and download MP3
        audio_file = await client.artifacts.wait_for_audio(notebook_id, artifact.id)
        out_mp3 = os.path.join(WORKSPACE_DIR, "Knowledge_Base", "Reports", "daily", "latest_podcast.mp3")
        await client.artifacts.download_audio(notebook_id, artifact.id, out_mp3)
        print(f"🎉 Audio Overview Ready & Downloaded: {out_mp3}")

if __name__ == '__main__':
    asyncio.run(auto_create_and_generate_audio())
