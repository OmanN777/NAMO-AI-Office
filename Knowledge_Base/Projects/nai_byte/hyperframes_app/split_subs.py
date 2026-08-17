import re

# Original 1x timings
subs = [
    {"start": 0.00, "duration": 3.76, "text": "รู้ไหมครับว่า ความผิดพลาด ของโค้ด เพียงแค่บรรทัดเดียว"},
    {"start": 3.76, "duration": 2.64, "text": "เคยทำเงิน หายวับไปถึง"},
    {"start": 6.40, "duration": 5.60, "text": "17,000 ล้านบาท ในเวลาแค่ 37 วินาที!"},
    {"start": 12.00, "duration": 6.32, "text": "นี่คือ เรื่องราวของ จรวด Ariane 5 ของยุโรป ในปี 1996..."},
    {"start": 18.32, "duration": 2.68, "text": "ปัญหาเกิดจาก สิ่งที่ โปรแกรมเมอร์เรียกว่า"},
    {"start": 21.00, "duration": 2.00, "text": "'Integer Overflow'"},
    {"start": 23.00, "duration": 3.40, "text": "หรือการพยายาม เอาข้อมูลตัวเลข 64-bit"},
    {"start": 26.40, "duration": 2.60, "text": "ไปยัดใส่ พื้นที่ 16-bit"},
    {"start": 29.00, "duration": 6.00, "text": "ผลก็คือ ระบบคำนวณ ทิศทางพังพินาศ จรวดหักเลี้ยว ผิดปรกติ"},
    {"start": 35.00, "duration": 3.00, "text": "และระเบิด ตู้มกลางอากาศ"},
    {"start": 38.00, "duration": 3.00, "text": "หลังจาก ปล่อยตัว ไม่ถึงนาที!"},
    {"start": 41.00, "duration": 3.00, "text": "ครั้งหน้า ถ้าคุณทำงานพลาด ให้นึกถึง จรวดลำนี้นะครับ..."},
    {"start": 44.00, "duration": 3.00, "text": "พลาดแค่ไหน ก็ไม่เท่า 17,000 ล้านแน่นอน!"},
    {"start": 47.00, "duration": 3.00, "text": "กดติดตาม ช่อง Elm0000"},
    {"start": 50.00, "duration": 5.00, "text": "สำหรับเรื่องไอที สนุกๆ แบบนี้ ทุกวันครับ!"}
]

SPEED_FACTOR = 1.4
TOTAL_DURATION = 55 / SPEED_FACTOR # ~39.2s

html_subs = ""
gsap_code = ""

sub_index = 0
for block in subs:
    start_time = block["start"] / SPEED_FACTOR
    duration = block["duration"] / SPEED_FACTOR
    text = block["text"]
    
    words = text.split()
    total_chars = sum(len(w) for w in words)
    
    current_time = start_time
    for w in words:
        if total_chars == 0: break
        word_dur = (len(w) / total_chars) * duration
        
        html_subs += f'    <div id="sub{sub_index}" class="subtitle" data-start="{current_time:.2f}" data-duration="{word_dur:.2f}">{w}</div>\n'
        
        gsap_code += f'      tl.to("#sub{sub_index}", {{ opacity: 1, scale: 1.1, duration: 0.1 }}, {current_time:.2f});\n'
        end_time = current_time + word_dur
        hide_time = max(end_time - 0.1, current_time + 0.1)
        gsap_code += f'      tl.to("#sub{sub_index}", {{ opacity: 0, scale: 1, duration: 0.1 }}, {hide_time:.2f});\n'
        
        current_time += word_dur
        sub_index += 1

# B-Roll Images logic
# We have 5 images over ~39 seconds. ~8s per image
# bg1: rocket_launchpad (0s - 8s)
# bg2: ariane_launch (8s - 16s)
# bg3: retro_code (16s - 24s)
# bg4: sad_engineer (24s - 32s)
# bg5: rocket_explosion (32s - end)

broll_html = """    <div style="position:absolute; width:100%; height:100%; background: #000; z-index: 1;">
      <img id="bg1" src="assets/rocket_launchpad.png" style="position:absolute; width:100%; height:100%; object-fit:cover; opacity:1; filter: brightness(0.5); transform: scale(1.0);">
      <img id="bg2" src="assets/ariane_launch.png" style="position:absolute; width:100%; height:100%; object-fit:cover; opacity:0; filter: brightness(0.5); transform: scale(1.0);">
      <img id="bg3" src="assets/retro_code.png" style="position:absolute; width:100%; height:100%; object-fit:cover; opacity:0; filter: brightness(0.5); transform: scale(1.0);">
      <img id="bg4" src="assets/sad_engineer.png" style="position:absolute; width:100%; height:100%; object-fit:cover; opacity:0; filter: brightness(0.5); transform: scale(1.0);">
      <img id="bg5" src="assets/rocket_explosion.png" style="position:absolute; width:100%; height:100%; object-fit:cover; opacity:0; filter: brightness(0.5); transform: scale(1.0);">
    </div>"""

# Crossfades and gentle zooms
broll_gsap = f"""      // B-Roll Crossfades & Zooms
      tl.to("#bg1", {{ scale: 1.15, duration: 8.0, ease: "none" }}, 0);
      tl.to("#bg2", {{ opacity: 1, duration: 0.5 }}, 8.0);
      tl.to("#bg2", {{ scale: 1.15, duration: 8.0, ease: "none" }}, 8.0);
      tl.to("#bg3", {{ opacity: 1, duration: 0.5 }}, 16.0);
      tl.to("#bg3", {{ scale: 1.15, duration: 8.0, ease: "none" }}, 16.0);
      tl.to("#bg4", {{ opacity: 1, duration: 0.5 }}, 24.0);
      tl.to("#bg4", {{ scale: 1.15, duration: 8.0, ease: "none" }}, 24.0);
      tl.to("#bg5", {{ opacity: 1, duration: 0.5 }}, 32.0);
      tl.to("#bg5", {{ scale: 1.15, duration: 8.0, ease: "none" }}, 32.0);
"""

# Read index.html
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace duration and sources
content = re.sub(r'data-duration="55"', f'data-duration="{TOTAL_DURATION:.2f}"', content)
content = content.replace('src="assets/voiceover.mp3"', 'src="assets/voiceover_fast.mp3"')
content = content.replace('src="assets/avatar.mp4"', 'src="assets/avatar_fast.mp4"')

# Replace background HTML
content = re.sub(r'<!-- Background.*?</div>', f'<!-- Background (B-Roll) -->\n{broll_html}', content, flags=re.DOTALL)

# Replace Subtitles HTML
content = re.sub(r'<!-- Subtitles -->.*?<script src="https://cdn\.jsdelivr', 
                 f'<!-- Subtitles -->\n{html_subs}\n    <script src="https://cdn.jsdelivr', 
                 content, flags=re.DOTALL)

# Replace GSAP Animations
content = re.sub(r'// Background B-Roll Crossfades.*window\.__timelines',
                 f'{broll_gsap}\n      // Simple subtitle pop animations\n{gsap_code}\n      window.__timelines',
                 content, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated index.html for fast video (1.4x) and 5 dynamic backgrounds!")
