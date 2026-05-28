---
name: scout-fetch
description: ค้นหาข้อมูลดิบ (Primary/Secondary Sources) ที่เชื่อถือได้และบันทึกลงใน sources/ สำหรับให้ Agent ตัวอื่นใช้งาน
---

# SOP: Data Scouting (The Sole Provider)

## ขั้นตอนการทำงาน
1. **Search:** Scout เป็นคนเดียวที่ได้รับสิทธิ์ให้ใช้ Web Search หาข้อมูลดิบของ [TICKER] เช่น:
   - "Earnings Call Transcript [TICKER] [QUARTER] 2026"
   - "Annual Report [TICKER] 2025"
   - "Recent Press Release [TICKER] May 2026"
2. **Validate:** ตรวจสอบว่าเป็นแหล่งข้อมูลที่เชื่อถือได้ (เช่น Seeking Alpha, Motley Fool, เว็บข่าวธุรกิจหลัก)
3. **Capture:** นำเนื้อหาหลักมาบันทึกเป็นไฟล์ Markdown (.md)
4. **Save:** บันทึกไฟล์ที่ `sources/[TICKER]/[FILENAME].md`
5. **Log:** ระบุแหล่งที่มา (URL) และวันที่ดึงข้อมูลไว้ที่ท้ายไฟล์

## กฎเหล็ก
- **No Summary:** Scout มีหน้าที่เอา "ข้อมูลดิบ" มาวาง ไม่ต้องสรุปเอง (สรุปเป็นหน้าที่ของ Agent ตัวอื่น)
- **Raw Focus:** เน้นตัวเลขและคำพูดตรงๆ จากผู้บริหาร (Quotes)
