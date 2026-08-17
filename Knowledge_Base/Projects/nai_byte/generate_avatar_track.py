import os
import numpy as np
from PIL import Image
from moviepy import AudioFileClip, ImageClip, ColorClip, CompositeVideoClip, concatenate_videoclips

def apply_alpha_mask(img_np):
    if img_np.shape[2] == 3:
        return ImageClip(img_np)
    rgb = img_np[:, :, :3]
    mask = img_np[:, :, 3] / 255.0
    clip = ImageClip(rgb).with_mask(ImageClip(mask, is_mask=True))
    return clip

def remove_green_screen(img_np):
    if img_np.shape[2] == 3:
        alpha = np.ones((img_np.shape[0], img_np.shape[1], 1), dtype=np.uint8) * 255
        img_np = np.concatenate((img_np, alpha), axis=2)
    
    r, g, b = img_np[:,:,0], img_np[:,:,1], img_np[:,:,2]
    # Broad tolerance for the specific dirty green background of both images
    mask1 = (abs(r.astype(int) - 114) < 40) & (abs(g.astype(int) - 186) < 40) & (abs(b.astype(int) - 120) < 40)
    img_np[mask1, 3] = 0 
    return img_np

def get_volume_envelope(audio_clip, chunk_fps=10):
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
    # Use PIL to load images, apply mask to remove dirty backgrounds
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

def main():
    print("=== Avatar Green Screen Generator (For CapCut) ===")
    
    audio_file = "ElevenLabs_2026-05-24T18_20_42_Larry – High-Energy Social Media Voice for Reels & Shorts_pvc_sp93_s22_sb35_v3.mp3"
    idle_img = "mr_byte_idle.png"
    talking_img = "mr_byte_rick_morty_talking.png"
    output_file = "ariane5_avatar_greenscreen.mp4"
    video_size = (1024, 1024) 
    
    for f in [audio_file, idle_img, talking_img]:
        if not os.path.exists(f):
            print(f"Error: Required file '{f}' not found in the current directory.")
            return

    print(f"Loading Audio: {audio_file}")
    audio = AudioFileClip(audio_file)
    
    print("Generating Lipsync (Standardizing Green Screen)...")
    is_talking, chunk_fps = get_volume_envelope(audio, chunk_fps=15) 
    avatar_track = create_avatar_track(is_talking, chunk_fps, idle_img, talking_img)
    
    print("Compositing on pure Green Screen (#00FF00)...")
    bg_clip = ColorClip(size=video_size, color=(0, 255, 0))
    bg_clip = bg_clip.with_duration(audio.duration)
    
    avatar_track = avatar_track.with_position('center')
    final_video = CompositeVideoClip([bg_clip, avatar_track])
    final_video = final_video.with_audio(audio)
    
    print(f"Rendering Video to: {output_file} (This should be VERY fast)")
    final_video.write_videofile(output_file, fps=15, codec="libx264", audio_codec="aac", preset="ultrafast")
    
    try:
        print("\u2705 Done! Ready to drop into CapCut.")
    except:
        print("Done! Ready to drop into CapCut.")

if __name__ == "__main__":
    main()
