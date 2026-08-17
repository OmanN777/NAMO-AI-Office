import whisper
import json
import os
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

def generate_hyperframes_subs():
    print("Loading Whisper model (small)...")
    model = whisper.load_model("small")
    
    audio_path = "assets/voiceover.mp3"
    print(f"Transcribing {audio_path}...")
    
    # Transcribe with Thai language
    result = model.transcribe(audio_path, language="th")
    
    html_subs = ""
    gsap_code = ""
    
    print("Generating HTML & GSAP...")
    for i, segment in enumerate(result["segments"]):
        start = segment["start"]
        end = segment["end"]
        duration = end - start
        text = segment["text"].strip()
        
        # HTML div
        html_subs += f'    <div id="sub{i}" class="subtitle" data-start="{start:.2f}" data-duration="{duration:.2f}">{text}</div>\n'
        
        # GSAP Animation
        gsap_code += f'      tl.to("#sub{i}", {{ opacity: 1, scale: 1.1, duration: 0.2 }}, {start:.2f});\n'
        gsap_code += f'      tl.to("#sub{i}", {{ opacity: 0, scale: 1, duration: 0.2 }}, {end - 0.2:.2f});\n'

    # Read index.html
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()

    # We need to replace the subtitles section in index.html
    # Let's just output it to a new file or replace it if we use standard markers.
    
    with open("subs_output.txt", "w", encoding="utf-8") as f:
        f.write(html_subs + "\n" + "-"*50 + "\n" + gsap_code)
        
    print("Saved subs_output.txt")

if __name__ == "__main__":
    generate_hyperframes_subs()
