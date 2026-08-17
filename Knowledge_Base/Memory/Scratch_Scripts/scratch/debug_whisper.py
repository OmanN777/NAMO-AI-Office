import whisper
import os
import numpy as np
from moviepy import AudioFileClip
from PIL import ImageFont

def main():
    audio_file = "C:/Users/namo_/OneDrive/เอกสาร/gemini-cli/antigravity-office-workspace/projects/nai_byte/ElevenLabs_2026-05-24T18_20_42_Larry – High-Energy Social Media Voice for Reels & Shorts_pvc_sp93_s22_sb35_v3.mp3"
    
    print("1. Checking Font...")
    try:
        font = ImageFont.truetype("tahoma.ttf", 90)
        print("Font Tahoma loaded successfully.")
    except Exception as e:
        print("Failed to load Tahoma font:", e)
        
    print("\n2. Checking Whisper transcription...")
    temp_audio = AudioFileClip(audio_file)
    audio_array = temp_audio.to_soundarray(fps=16000)
    if audio_array.ndim > 1:
        audio_array = audio_array.mean(axis=1)
    audio_array = audio_array.astype(np.float32)
    
    model = whisper.load_model("base")
    result = model.transcribe(audio_array, language="th")
    segments = result["segments"]
    
    print(f"Found {len(segments)} segments.")
    for i, seg in enumerate(segments[:5]):
        print(f"Segment {i}: [{seg['start']:.2f} - {seg['end']:.2f}] {seg['text']}")
        
if __name__ == "__main__":
    main()
