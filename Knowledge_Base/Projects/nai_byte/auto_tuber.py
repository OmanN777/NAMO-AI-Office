import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import whisper
from moviepy import AudioFileClip, ImageClip, ColorClip, CompositeVideoClip, concatenate_videoclips

def apply_alpha_mask(img_np):
    """
    Given an RGBA numpy array (H, W, 4), returns a MoviePy ImageClip with proper mask.
    """
    if img_np.shape[2] == 3:
        return ImageClip(img_np)
        
    rgb = img_np[:, :, :3]
    mask = img_np[:, :, 3] / 255.0
    clip = ImageClip(rgb).with_mask(ImageClip(mask, is_mask=True))
    return clip

def remove_green_screen(img_np):
    """
    Converts specific green background pixels to transparent.
    """
    print("Applying Chroma Key (Green Screen Removal)...")
    if img_np.shape[2] == 3:
        # Add alpha channel if it doesn't exist
        alpha = np.ones((img_np.shape[0], img_np.shape[1], 1), dtype=np.uint8) * 255
        img_np = np.concatenate((img_np, alpha), axis=2)
    
    r, g, b = img_np[:,:,0], img_np[:,:,1], img_np[:,:,2]
    
    # Specific color of mr_byte_rick_morty.png background is roughly (114, 186, 120)
    # We use a broad tolerance around it
    mask1 = (abs(r.astype(int) - 114) < 40) & (abs(g.astype(int) - 186) < 40) & (abs(b.astype(int) - 120) < 40)
    
    # Also handle pure green backgrounds just in case (g > 150, r < 100, b < 100)
    mask2 = (g > 150) & (r < 100) & (b < 100)
    
    final_mask = mask1 | mask2
    img_np[final_mask, 3] = 0 # Set Alpha to 0
    return img_np

def get_volume_envelope(audio_clip, chunk_fps=10):
    print("Analyzing audio volume envelope...")
    sample_rate = 22050
    audio_array = audio_clip.to_soundarray(fps=sample_rate)
    
    chunk_size = int(sample_rate / chunk_fps)
    n_chunks = len(audio_array) // chunk_size
    trimmed_array = audio_array[:n_chunks * chunk_size]
    
    if trimmed_array.ndim > 1:
        trimmed_array = trimmed_array.mean(axis=1)
        
    chunks = trimmed_array.reshape((n_chunks, chunk_size))
    rms = np.sqrt(np.mean(chunks**2, axis=1))
    
    threshold = np.max(rms) * 0.05
    is_talking = rms > threshold
    return is_talking, chunk_fps

def create_avatar_track(is_talking, chunk_fps, idle_path, talking_path):
    print("Generating Avatar Video Track...")
    # Load images using PIL to avoid moviepy color space weirdness
    idle_np = np.array(Image.open(idle_path).convert("RGBA"))
    talking_np = np.array(Image.open(talking_path).convert("RGBA"))
    
    idle_np = remove_green_screen(idle_np)
    talking_np = remove_green_screen(talking_np)
    
    idle_clip = apply_alpha_mask(idle_np)
    talking_clip = apply_alpha_mask(talking_np)
    
    clips = []
    current_state = is_talking[0]
    start_t = 0
    
    for i in range(1, len(is_talking)):
        if is_talking[i] != current_state:
            end_t = i / chunk_fps
            duration = end_t - start_t
            clip = talking_clip.copy() if current_state else idle_clip.copy()
            clips.append(clip.with_duration(duration))
            current_state = is_talking[i]
            start_t = end_t
            
    end_t = len(is_talking) / chunk_fps
    duration = end_t - start_t
    clip = talking_clip.copy() if current_state else idle_clip.copy()
    clips.append(clip.with_duration(duration))
    
    avatar_track = concatenate_videoclips(clips, method="compose")
    return avatar_track

def create_text_clip(text, duration, video_size=(1080, 1920)):
    img = Image.new('RGBA', video_size, (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    
    try:
        font = ImageFont.truetype("tahoma.ttf", 90) # Larger font
    except:
        font = ImageFont.load_default()
            
    try:
        bbox = d.textbbox((0,0), text, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
    except:
        w, h = 100, 100 
        
    x = (video_size[0] - w) / 2
    y = video_size[1] * 0.25 # Place it at 25% from top
    
    stroke_width = 5
    for dx in range(-stroke_width, stroke_width+1):
        for dy in range(-stroke_width, stroke_width+1):
            if dx*dx + dy*dy <= stroke_width*stroke_width:
                d.text((x+dx, y+dy), text, font=font, fill="black")
                
    d.text((x, y), text, font=font, fill="yellow")
    
    np_img = np.array(img)
    clip = apply_alpha_mask(np_img).with_duration(duration)
    return clip

def generate_subtitles(audio_file, video_size=(1080, 1920)):
    print("Transcribing audio with Whisper...")
    # Load audio using moviepy to avoid ffmpeg system dependency in whisper
    temp_audio = AudioFileClip(audio_file)
    audio_array = temp_audio.to_soundarray(fps=16000)
    if audio_array.ndim > 1:
        audio_array = audio_array.mean(axis=1)
    audio_array = audio_array.astype(np.float32)
    
    model = whisper.load_model("tiny")
    result = model.transcribe(audio_array)
    segments = result["segments"]
    
    text_clips = []
    for seg in segments:
        start = seg['start']
        end = seg['end']
        text = seg['text'].strip()
        duration = end - start
        tc = create_text_clip(text, duration, video_size).with_start(start)
        text_clips.append(tc)
        
    return text_clips

def main():
    print("=== Auto Tuber PNGTuber Engine V3 ===")
    
    audio_file = "ElevenLabs_2026-05-24T18_20_42_Larry – High-Energy Social Media Voice for Reels & Shorts_pvc_sp93_s22_sb35_v3.mp3"
    idle_img = "mr_byte_rick_morty.png"
    talking_img = "mr_byte_rick_morty_talking.png"
    output_file = "ariane5_shorts_draft_v3.mp4"
    video_size = (1080, 1920)
    
    for f in [audio_file, idle_img, talking_img]:
        if not os.path.exists(f):
            print(f"Error: Required file '{f}' not found in the current directory.")
            return

    print(f"Loading Audio: {audio_file}")
    audio = AudioFileClip(audio_file)
    
    is_talking, chunk_fps = get_volume_envelope(audio, chunk_fps=10)
    avatar_track = create_avatar_track(is_talking, chunk_fps, idle_img, talking_img)
    
    # 4. Position and Resize Avatar
    avatar_track = avatar_track.resized(width=800)
    avatar_track = avatar_track.with_position(('center', 'bottom'))
    
    # 5. Generate Subtitles using Whisper
    subtitle_clips = generate_subtitles(audio_file, video_size)
    
    # 6. Create Background
    print("Creating Background and Compositing...")
    bg_clip = ColorClip(size=video_size, color=(15, 23, 42))
    bg_clip = bg_clip.with_duration(audio.duration)
    
    # 7. Final Composite (Background + Avatar + Subtitles)
    final_video = CompositeVideoClip([bg_clip, avatar_track] + subtitle_clips)
    final_video = final_video.with_audio(audio)
    
    print(f"Rendering Video to: {output_file}")
    final_video.write_videofile(output_file, fps=24, codec="libx264", audio_codec="aac")
    
    try:
        print("\u2705 Rendering Complete!")
    except:
        print("Rendering Complete!")

if __name__ == "__main__":
    main()
