---
name: pordee-optimizer
description: ระบบจัดการและบีบอัด Token ข้อมูลสำหรับ Agent (ลดค่าใช้จ่ายและเพิ่มความเร็ว)
---

# SOP: Pordee Token Optimization (พอดี)

## วัตถุประสงค์
เพื่อลดการสิ้นเปลือง Token (Token Optimization) ในระหว่างที่ Agent สื่อสารกันเอง โดยเฉพาะการประมวลผลข้อมูลภาษาไทยซึ่งกิน Token มากกว่าภาษาอังกฤษ 2-3 เท่า

## กฎการทำงาน (Pordee Rules)

1. **Internal Communication in English Only:**
   - เมื่อ Agent (เช่น Scout, Fundamentokung, Earnchan, Newwy, Reese) คุยกันเอง ค้นหาข้อมูล หรือบันทึกข้อมูลดิบลงไฟล์ (เช่น `sources/` หรือ `briefs/`) **ห้ามใช้ภาษาไทย** 
   - ให้ใช้ภาษาอังกฤษที่สั้น กระชับ ไร้คำฟุ่มเฟือย (Stop-word reduction) 

2. **JSON/Bullet Format Priority:**
   - ข้อมูลที่ถูกบันทึกหรือส่งต่อ ต้องอยู่ในรูปแบบ JSON หรือ Bullet point สั้นๆ ห้ามเขียนเป็นย่อหน้าบรรยายยาวๆ โดยไม่จำเป็น
   - ตัวอย่าง: แทนที่จะเขียน "บริษัท NVDA มีรายได้เพิ่มขึ้น 85% เมื่อเทียบกับปีที่แล้ว" ให้เขียน `{"NVDA": {"rev_growth_yoy": "85%"}}`

3. **Translation on Demand (Malli/Oman Only):**
   - **Malli** และ **Oman** เป็น Agent เพียงสองตัวที่ได้รับอนุญาตให้ใช้ภาษาไทยได้ **เฉพาะเมื่อ** ต้องสรุปรายงาน (Executive Briefing) หรือสื่อสารกับผู้ใช้ (CEO) โดยตรงเท่านั้น
   - การสื่อสารกับ CEO ต้องใช้ภาษาไทยที่สละสลวย อ่านง่าย และตรงประเด็น (CEO Conciseness)

## วิธีใช้งาน
- Agent ทุกตัวต้องตรวจสอบและบีบอัด Context ของตัวเองตามกฎ Pordee ก่อนที่จะบันทึกไฟล์หรือส่งต่อให้ Agent ตัวอื่น
