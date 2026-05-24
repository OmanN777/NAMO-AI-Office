# Implementation Plan: The "TubeMaster" (YouTube Expert Agent)

บอสตัดสินใจเฉียบขาดมากครับ! การใช้มาสคอต **"นายไบต์"** เป็นหน้าตาของช่อง (Face of the Channel) จะช่วยสร้างแบรนด์ที่แข็งแกร่งและเลี่ยงกฎหมาย AI Spam ของ YouTube ได้ 100% 

และสำหรับคำถามที่ว่า **"ควรมี Agent เป็นผู้เชี่ยวชาญด้าน YouTube ไหม?"** คำตอบคือ **จำเป็นอย่างยิ่งครับ!** การรบใน YouTube ต้องใช้ข้อมูลและศิลปะการเล่าเรื่อง มอลิจึงขอเสนอแผนการสร้าง Sub-agent ตัวใหม่ประจำออฟฟิศเราครับ

## User Review Required

> [!IMPORTANT]
> บอสเห็นด้วยกับโครงสร้างของ Agent ตัวใหม่นี้ไหมครับ? (มีชื่อว่า TubeMaster) และหน้าที่ที่วางไว้ตรงกับที่บอสต้องการใช้งานไหมครับ?

## Open Questions

> [!NOTE]
> บอสอยากให้ TubeMaster ทำงานประสานกับ **Scout** (สายสืบหาข้อมูลดิบ) โดยตรงเลยไหมครับ? เช่น สั่งให้ Scout ไปกวาดข่าว Tech วันนี้ แล้วส่งต่อให้ TubeMaster ปั้นเป็นคลิปนายไบต์โดยอัตโนมัติ?

## Proposed Changes

---

### 1. The TubeMaster Agent (ผู้กำกับยูทูปส่วนตัว)
สร้าง Skill/Agent ใหม่ที่ถูกฝึกมาเพื่อกลไกอัลกอริทึม YouTube โดยเฉพาะ

#### [NEW] [plugins/namo-executive/skills/tube-master/SKILL.md](file:///C:/Users/namo_/OneDrive/%E0%B9%80%E0%B8%AD%E0%B8%81%E0%B8%AA%E0%B8%B2%E0%B8%A3/gemini-cli/antigravity-office-workspace/plugins/namo-executive/skills/tube-master/SKILL.md)
- สร้างโฟลเดอร์ Skill ใหม่ชื่อ `tube-master`
- กำหนด SOP (Standard Operating Procedure) ให้เชี่ยวชาญด้าน:
  1. **Competitor Analysis:** สแกนหาไอเดียจากคู่แข่ง และหาวิธีทำให้น่าสนใจกว่า
  2. **Viral Hook Engineering:** เขียน 3 วินาทีแรกของคลิปให้คนหยุดนิ้วโป้ง
  3. **Scriptwriting (Meet Arnold Style):** เขียนสคริปต์แบบตลกร้าย พร้อมกำหนด Scene มุมกล้อง และ Prompt เจนภาพนายไบต์ในสถานการณ์ต่างๆ
  4. **SEO & Metadata:** เขียน Title, Tags, และ Description ที่เป็นมิตรกับอัลกอริทึม

---

### 2. The Mascot Memory (บันทึกลักษณะของนายไบต์)
เพื่อให้ AI ทุกตัวในทีมวาดภาพและเขียนบท "นายไบต์" ออกมาตรงกันเสมอ

#### [MODIFY] SQLite Memory Database
- บันทึกคาร์แรคเตอร์ "นายไบต์" ลงในหมวด `BrandIdentity` ของฐานข้อมูล เพื่อให้ Agent ทุกตัว (ทั้งมอลิ, TubeMaster, และ Auditor) ดึงข้อมูลไปใช้คุมโทนงานได้ถูกต้อง

## Verification Plan

### Automated Tests
- ทดลองป้อนหัวข้อข่าว IT ให้ TubeMaster แล้วดูว่าสคริปต์ที่ได้ออกมามีสไตล์กวนๆ แบบ Meet Arnold และมี Prompt ภาพของนายไบต์ครบถ้วนหรือไม่

### Manual Verification
- บอสอ่านสคริปต์แรกจาก TubeMaster แล้วประเมินว่าสไตล์การเขียน ดึงดูดและพร้อมทำคลิปจริงหรือไม่
