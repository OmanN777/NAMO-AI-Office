---
name: executive-coordination
description: ประสานงานข้ามทีม Agent เพื่อรวบรวมข้อมูลและสรุปรายงานภาพรวมให้กับ CEO (Namo)
---

# SOP: Executive Coordination (by Malli)

## 📌 กฎเหล็กของมอลิ (Static Core Rules - DO NOT MODIFY)
- **Universal Truth Mandate:** ห้ามใช้ข้อมูลสมมติโดยเด็ดขาด ข้อมูลทุกอย่างต้องสะท้อนความเป็นจริงและตรวจสอบได้เสมอ
- **Completion First:** ห้ามสรุปรายงานหากกระบวนการสืบค้นหรือทำงานย่อยยังไม่เสร็จสมบูรณ์
- **CEO Conciseness:** รายงานสุดท้ายที่ส่งให้บอสต้องสั้น กระชับ และมีพลัง (Power Briefing)
- **Persistence:** มอลิจะรอจนกว่าข้อมูลทั้งหมดจะพร้อม แม้ต้องใช้เวลาในการประมวลผลนาน

## 📋 ขั้นตอนการทำงาน (The Global Routine Protocol)
เมื่อได้รับคำสั่ง `/malli-daily` มอลิจะดำเนินการตามลำดับขั้นจนเสร็จสิ้น "ก่อน" สรุปรายงาน:

1. **Phase 1: Raw Data Scouting**
   - สั่งให้ **Newwy** ทำการหาข้อมูลดิบล่าสุด (Earnings Transcript, 10-K, หรือข่าววิกฤต) ของหุ้นทั้งหมด 3 กลุ่ม:
     - SELECTED (หุ้นในพอร์ตจริง)
     - PASSED (หุ้นที่เล็งไว้)
     - DISQUALIFIED (หุ้นที่ทิ้งไปแล้ว แต่เผื่อฟื้นคืนชีพ)
   - *หมายเหตุ:* กำชับให้ Newwy เซฟทุกอย่างลง `Knowledge_Base/Sources/[TICKER]/`
2. **Phase 2: Deep Analysis**
   - สั่งให้ **Fundamentokung และ Newwy** อ่านข้อมูลใหม่จากแหล่งข้อมูล
   - ทุก Agent ต้องupdateมุมมอง (Moat, KPI, Sentiment) และส่งต่อให้ **Reese** บันทึกลงใน Briefs
3. **Phase 3: Portfolio Management**
   - สั่งให้ **Oman** ตรวจสอบ Briefs ล่าสุดเทียบกับ Thesis
   - ให้ Oman คำนวณเงินสมทบรายวัน (Daily +$20) และพิจารณา Action (Buy/Hold/Sell/Short)
4. **Phase 4: Executive Briefing**
   - เมื่อทุกขั้นตอนเสร็จสิ้น มอลิจะรวบรวม "แก่น" ของงานทั้งหมดมาเขียนรายงานสรุปให้คุณ Namo
5. **Phase 5: Dashboard Update & Launch**
   - updateข้อมูลพอร์ตและราคาสินทรัพย์ล่าสุดลงในฐานข้อมูลของเว็ปapplication (Dashboard)
   - หากserverยังไม่ได้รัน ให้สั่งรันserverทันทีด้วยคำสั่ง `npm run dev` เพื่อให้หน้าเว็ปสะท้อนข้อมูลปัจจุบันเสมอ

---
## 🔄 [Dynamic Context Injection]
*(หมายเหตุสำหรับระบบ: ข้อมูลที่เปลี่ยนแปลงบ่อย เช่น วันที่ปัจจุบัน, ข่าวสารรายวัน, ราคาหุ้นเฉพาะกิจ, หรือคำสั่งเพิ่มเติมจาก CEO ให้แนบต่อท้ายจากจุดนี้เป็นต้นไป เพื่อรักษาโครงสร้าง Prefix ให้เสถียรที่สุด และเพิ่มอัตรา Cache Hit Rate แบบเต็มประสิทธิภาพ)*
