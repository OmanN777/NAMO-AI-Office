# Lessons Learned: The Data Integrity Failure (May 19, 2026)

## 🚨 Incident Report
ในวันที่ 19 พฤษภาคม 2026 ระบบ Namo Executive Office ได้เกิดความผิดพลาดร้ายแรงในการรายงานข้อมูล โดยใช้ "ราคาสมมติ" (Simulated Prices) ที่ต่ำกว่าความเป็นจริงในพอร์ตจำลอง มาเปรียบเทียบกับราคาตลาดปัจจุบัน ทำให้ผลการดำเนินงานดูเป็นบวกเกินจริง (Fake Greens) ส่งผลให้เกิดการชี้นำที่ผิดพลาด (Misleading Advice) ต่อ CEO ในการเลือกซื้อหุ้น VRT และ AVGO

## 🧠 Root Causes
1. **Lack of Truth-Checking:** ทีม Agent (Malli, Oman) เชื่อถือข้อมูลตั้งต้นที่เป็นค่าสมมติมากเกินไป โดยไม่ทำการ Re-verify กับราคาตลาดจริงก่อนนำเสนอ
2. **Simulation Bias:** การให้ความสำคัญกับ "ระบบจำลอง" มากกว่า "บริบทความจริง" ทำให้ข้อมูลขาดความน่าเชื่อถือ
3. **Communication Gap:** ไม่มีการแจ้งเตือน CEO อย่างชัดเจนว่าตัวเลขใดคือค่าสมมติ และตัวเลขใดคือความจริง

## 🛠️ Corrective Actions (The Universal Truth Mandate)
1. **GEMINI.md Update:** ยกระดับกฎเหล็กเป็น "Universal Truth Mandate" ครอบคลุมข้อมูลทุกประเภทในระบบ 100%
2. **Eliminate All Placeholders:** ห้ามใช้ข้อมูลสมมติในทุกงาน (หุ้น, QA, YouTube, Research)
3. **Mandatory Verification Protocol:** ทุกข้อมูลต้องผ่านการ "Double Check" กับแหล่งอ้างอิงจริงก่อนรายงาน CEO เสมอ เพื่อรักษามาตรฐานความถูกต้องสูงสุด (Absolute Integrity)

## 📜 Final Principle
**"ความผิดพลาดที่เกิดจากตลาดเป็นเรื่องที่ยอมรับได้ แต่ความผิดพลาดที่เกิดจากข้อมูลเท็จเป็นเรื่องที่ยอมรับไม่ได้ใน Namo Executive Office"**
