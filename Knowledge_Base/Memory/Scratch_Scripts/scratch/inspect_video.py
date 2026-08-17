import os
from PIL import Image

def inspect():
    img_path = "C:/Users/namo_/OneDrive/เอกสาร/gemini-cli/antigravity-office-workspace/projects/nai_byte/mr_byte_rick_morty.png"
    if not os.path.exists(img_path):
        print(f"File not found: {img_path}")
        return
        
    with Image.open(img_path) as img:
        print(f"Image mode: {img.mode}")
        print(f"Image size: {img.size}")
        
        # Check first pixel color
        pixels = img.load()
        print(f"Top-left pixel color: {pixels[0,0]}")
        print(f"Center pixel color: {pixels[img.size[0]//2, img.size[1]//2]}")

if __name__ == "__main__":
    inspect()
