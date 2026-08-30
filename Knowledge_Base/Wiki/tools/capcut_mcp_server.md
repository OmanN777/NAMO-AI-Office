# 🎬 Technical Learning: CapCut MCP Server (Programmatic Video Editing via AI)

**Source:** [baizo7/capcut_MCP_server-](https://github.com/baizo7/capcut_MCP_server-)  
**Category:** Model Context Protocol (MCP) / Automation / Video Engineering  
**Primary Beneficiary:** Tubemaster (Director & SEO Master for YouTube Gaming) & Malli  
**Date Learned:** 2026-08-30  

---

## 📌 1. สิ่งนี้คืออะไร (What is CapCut MCP Server?)
**CapCut MCP Server** คือตัวเชื่อมต่อมาตรฐาน **Model Context Protocol (MCP)** ที่ช่วยให้ AI Coding Assistants (เช่น Antigravity, Claude, Cursor) สามารถ **"ควบคุมและตัดต่อวิดีโอบน CapCut Desktop ได้โดยตรงผ่านโค้ดและคำสั่งแชท"**

---

## 🛠️ 2. กลไกการทำงานเบื้องหลัง (How It Works)
* **Direct Draft Manipulation (`draft_content.json`):**
  * โปรเจกต์ของ CapCut Desktop บน Windows ถูกเก็บเป็นโครงสร้าง JSON (อยู่ที่โฟลเดอร์ `CapCut Drafts/`)
  * CapCut MCP Server ทำการอ่านและแก้ไขไฟล์ `draft_content.json` โดยตรง ทำให้ AI สามารถ:
    1. **สร้างและจัดการ Timeline:** ตัดคลิป, วางคลิปเรียงต่อกัน, ปรับความยาว (Duration)
    2. **ใส่ข้อความและซับไตเติล (Auto Subtitles & Text):** กำหนดฟอนต์, สี, ตำแหน่ง และ Keyframe อัตโนมัติ
    3. **จัดการเสียงและเพลงประกอบ (Audio & BGM):** นำเข้าไฟล์เสียง, ปรับระดับเสียง (Volume), วาง Sound Effects (SFX) ตรงจังหวะ
    4. **นำเข้ามีเดีย (Media Asset Import):** ดึงไฟล์ฟุตเทจเกม, มีม, และรูปภาพเข้ามาวางใน Track อัตโนมัติ
* **Safety First:** มีระบบ Auto-backup Drafts ป้องกันไฟล์งานเสียหายก่อนทำการแก้ไข

---

## 🚀 3. ประโยชน์เชิงกลยุทธ์ต่อช่อง YouTube Gaming ของบอส (Use Cases)
บอสทำช่อง **YouTube Gaming** อยู่แล้ว เครื่องมือนี้จะช่วย **Tubemaster** ปลดล็อกระบบตัดต่อแบบกึ่งอัตโนมัติ (Semi-Automated Content Engine) ได้ดังนี้:

1. **Auto-generate Gaming Shorts (ทำคลิปสั้นอัตโนมัติ):**
   * บอสส่งไฮไลต์เกมมิ่งดิบมา ➔ มอลิ/Tubemaster ให้คำสั่งตัดช่วงจังหวะพีค 30-60 วินาที ➔ แทรกแคปชันตัวหนังสือแบบไดนามิก ➔ ใส่ Sound Effect ตามจุด ➔ บอสเปิด CapCut ขึ้นมาแค่กด "Export"
2. **Batch Subtitling & Captioning:**
   * สั่งให้ AI เจนซับไตเติลคำพูดจากเสียงพูดลง Timeline ของ CapCut ได้ตรงวินาทีโดยไม่ต้องนั่งพิมพ์ทีละท่อน
3. **Template-Based Video Assembly:**
   * วางโครงสร้างคลิปตามเทมเพลตมาตรฐาน (Hook 3 วิแรก -> Gameplay -> Call to Action กด Sub) ให้อัตโนมัติ

---

## ⚙️ 4. วิธีการติดตั้งและคอนฟิกใน Antigravity (Installation Blueprint)

### 1. ติดตั้งผ่าน uv / pip:
```bash
git clone https://github.com/baizo7/capcut_MCP_server-.git
cd capcut_MCP_server-
uv pip install -e .
```

### 2. เพิ่มใน `mcp_config.json`:
```json
{
  "mcpServers": {
    "capcut": {
      "command": "python",
      "args": ["-m", "capcut_mcp_server"],
      "env": {
        "CAPCUT_DRAFTS_PATH": "C:\\Users\\namo_\\AppData\\Local\\CapCut\\User Data\\Projects\\com.lveditor.draft"
      }
    }
  }
}
```

---

## 🎯 สรุปผลลัพธ์
เครื่องมือนี้เปลี่ยนงานตัดต่อวิดีโอจากที่ต้องคลิกเมาส์ทำทีละสเต็ป ให้กลายเป็น **"AI Code-Driven Video Pipeline"** ที่ช่วยประหยัดเวลาของบอสได้อย่างมหาศาลค่ะ!
