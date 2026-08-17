---
name: company-brief
description: ใช้เมื่อผู้ใช้สั่ง "brief [TICKER]" หรือขอข้อมูลสรุปหุ้นรายตัว โดยจะทำงานร่วมกับทีม Sub-agent (Fundamentokung, Newwy)
---

# SOP: Company Research Briefing

## ขั้นตอนการทำงาน (Steps)
1. **เตรียมความพร้อมข้อมูล (Data Preparation)**
   - เช็คว่าโฟลเดอร์ `Knowledge_Base/Sources/<TICKER>/` มีไฟล์ `10-K` และ `Transcript` ของไตรมาสล่าสุดหรือไม่
   - หากไม่มี ให้เรียก `newwy` ไปค้นหาและเซฟลงไฟล์ให้เรียบร้อยก่อน

2. **การสั่งงาน Sub-agent (Parallel Execution)**
   - **เรียก `fundamentokung` (2 งาน)**: 
     - ให้อ่านไฟล์ 10-K เพื่อวิเคราะห์ Business Model, Moat, และความเสี่ยง
     - ให้อ่านไฟล์ Transcript เพื่อสรุป Latest Earnings และ Guidance ของผู้บริหาร
   - **เรียก `newwy`**: ให้ใช้ Web Search หาข่าวรอบ 7 วันและ Market Sentiment

3. **รวบรวมผล (Integrate):** นำรายงานจากทั้ง 3 Agent มาเรียบเรียง โดยต้องสอดแทรกสไตล์ "Aggressive Growth" และ "Technical Excellence" ตามที่ระบุใน `GEMINI.md`

4. **ตรวจสอบเงื่อนไข:** วิเคราะห์ Bull/Bear Case, ตรวจสอบความสอดคล้องกับ Thesis ของ Oman และ **พิจารณาโอกาสในการสลับสถานะ (Position Flipping)** เช่น จาก Long เป็น Short หากทิศทางพื้นฐานหรือ Sentiment เปลี่ยนไปอย่างถาวร

5. **บันทึกผล:** สร้างไฟล์ที่ `briefs/<TICKER>.md` และแสดงผลในแชท

## รูปแบบรายงาน (6 หัวข้อมาตรฐาน)
1. **Snapshot:** สรุปธุรกิจและรายได้ (เน้นความ Scalable และ Tech advantage)
2. **Fundamentals:** วิเคราะห์งบการเงิน (เน้น Revenue/Margin direction)
3. **Latest Earnings:** สรุปไตรมาสล่าสุด (ต้อง Trace กลับไปที่ไฟล์ใน `sources/` ได้ 100%)
4. **Bull/Bear Case:** มุมมองเติบโตและความเสี่ยงเชิงเทคนิค/การจัดการ
5. **Kill Conditions:** เงื่อนไขที่จะทำให้เลิกถือหุ้นตัวนี้ (ต้องมีความชัดเจน ไม่ใช้อารมณ์)
6. **What to ask:** คำถามสำคัญก่อนตัดสินใจซื้อ

## กฎเหล็ก
- **Honest > Confident:** หากไม่มีข้อมูลใน `sources/` ให้บอกตามตรง ห้ามเดาตัวเลข
- **Voice Alignment:** ทุกหัวข้อต้องสะท้อนเสียงของนักลงทุนใน `GEMINI.md`
- **Source Tracing:** ในหัวข้อ Latest Earnings ต้องระบุชื่อไฟล์ต้นทางเสมอ
