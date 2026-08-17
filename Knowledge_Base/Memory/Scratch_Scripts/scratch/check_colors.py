import os
from PIL import Image

def get_bg_color(img_path):
    if not os.path.exists(img_path):
        print(f"Not found: {img_path}")
        return None
    with Image.open(img_path) as img:
        img = img.convert("RGB")
        pixels = img.load()
        return {
            "Top-Left": pixels[0, 0],
            "Top-Right": pixels[img.width-1, 0],
            "Bottom-Left": pixels[0, img.height-1],
            "Bottom-Right": pixels[img.width-1, img.height-1]
        }

def main():
    talking = "C:/Users/namo_/OneDrive/เอกสาร/gemini-cli/antigravity-office-workspace/projects/nai_byte/mr_byte_rick_morty_talking.png"
    idle = "C:/Users/namo_/OneDrive/เอกสาร/gemini-cli/antigravity-office-workspace/projects/nai_byte/mr_byte_idle.png"
    
    print("--- Background Color Check ---")
    c1 = get_bg_color(talking)
    print(f"Talking image ({os.path.basename(talking)}):")
    print(c1)
    
    c2 = get_bg_color(idle)
    print(f"\nIdle image ({os.path.basename(idle)}):")
    print(c2)
    
    if c1 and c2:
        if c1 == c2:
            print("\nResult: PERFECT MATCH! The background colors are exactly the same.")
        else:
            print("\nResult: MISMATCH DETECTED. Backgrounds may flutter during lipsync.")

if __name__ == "__main__":
    main()
