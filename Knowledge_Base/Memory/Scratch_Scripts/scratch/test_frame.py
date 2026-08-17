import os
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from moviepy import ImageClip, ColorClip, CompositeVideoClip

def remove_green_screen(img_np):
    if img_np.shape[2] == 3:
        alpha = np.ones((img_np.shape[0], img_np.shape[1], 1), dtype=np.uint8) * 255
        img_np = np.concatenate((img_np, alpha), axis=2)
    
    r, g, b = img_np[:,:,0], img_np[:,:,1], img_np[:,:,2]
    # mask the background color: (114, 186, 120) +/- 30
    mask = (abs(r.astype(int) - 114) < 40) & (abs(g.astype(int) - 186) < 40) & (abs(b.astype(int) - 120) < 40)
    img_np[mask, 3] = 0
    return img_np

def get_avatar():
    img_path = "C:/Users/namo_/OneDrive/เอกสาร/gemini-cli/antigravity-office-workspace/projects/nai_byte/mr_byte_rick_morty.png"
    img_np = np.array(Image.open(img_path))
    img_np = remove_green_screen(img_np)
    
    # In MoviePy v2, if the array has 4 channels, it usually uses the 4th channel as mask.
    # To be safe, we extract rgb and mask explicitly:
    rgb = img_np[:, :, :3]
    mask = img_np[:, :, 3] / 255.0
    
    clip = ImageClip(rgb)
    clip = clip.with_mask(ImageClip(mask, is_mask=True))
    return clip

def get_text():
    video_size = (1080, 1920)
    img = Image.new('RGBA', video_size, (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    
    text = "TESTING SUBTITLES"
    try:
        bbox = d.textbbox((0,0), text, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
    except:
        w, h = 100, 100
        
    x = (video_size[0] - w) / 2
    y = video_size[1] * 0.25
    
    d.text((x, y), text, font=font, fill="yellow")
    
    img_np = np.array(img)
    rgb = img_np[:, :, :3]
    mask = img_np[:, :, 3] / 255.0
    
    clip = ImageClip(rgb).with_mask(ImageClip(mask, is_mask=True))
    return clip

def main():
    bg_clip = ColorClip(size=(1080, 1920), color=(15, 23, 42))
    bg_clip = bg_clip.with_duration(1)
    
    avatar = get_avatar().resized(width=800).with_position(('center', 'bottom')).with_duration(1)
    text = get_text().with_duration(1)
    
    final = CompositeVideoClip([bg_clip, avatar, text])
    final.save_frame("test_frame.png", t=0)
    print("test_frame.png generated.")

if __name__ == "__main__":
    main()
