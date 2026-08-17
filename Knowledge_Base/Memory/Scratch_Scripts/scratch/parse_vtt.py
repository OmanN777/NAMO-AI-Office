import re

def parse_vtt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove VTT header and timestamps
    lines = content.split('\n')
    text_lines = []
    
    for line in lines:
        line = line.strip()
        # Skip empty lines, WEBVTT, Style tags, timestamps (00:00:00.000)
        if not line or line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:") or "-->" in line or line.startswith("Style:"):
            continue
        
        # Clean HTML/VTT tags like <c>, <00:00:01.000> etc
        clean_line = re.sub(r'<[^>]+>', '', line)
        if clean_line and clean_line not in text_lines[-5:]: # basic deduplication for auto-subs
            text_lines.append(clean_line)

    summary = " ".join(text_lines[:200]) # Get first few paragraphs
    print(summary)
    
    with open("scratch/vtt_summary.txt", "w", encoding="utf-8") as out:
        out.write(" ".join(text_lines))

if __name__ == "__main__":
    parse_vtt("scratch/ผมให้ Claude ตัดต่อวิดีโอให้ผม [UmFJKFdkHQ8].th.vtt")
