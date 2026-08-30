# 🔍 Post-Mortem Analysis: Vertiv Holdings Co (NYSE: VRT) - High Valuation Drawdown & Volatility Management

**Date:** 2026-08-30  
**Authors:** Vera (Quant & Risk Manager), Fundamentokung (Valuation Lead), Oman (CIO)  
**Status:** In-Portfolio Position Review (Unrealized P/L: -23.98% / Entry Cost: .31 / Current: .70)

---

## 1. What Happened? (สถานการณ์ที่เกิดขึ้น)
* Agent Oman ได้ทำการเข้าซื้อ VRT ในราคาทุนเฉลี่ย **.31** ในช่วงที่ตลาด AI Infrastructure กำลังอยู่ในจุดพรีเมียมสูงสุด
* ต่อมาเมื่อตลาดเกิดการปรับฐานจากความกังวลเรื่องการหมุนเวียนกลุ่มหุ้น (Sector Rotation) และนโยบายดอกเบี้ยของเฟด ทำให้ราคา VRT ย่อตัวลงมาที่ **.70** ส่งผลให้เกิด Unrealized Drawdown ประมาณ -24%

---

## 2. Root Cause Analysis (วิเคราะห์สาเหตุเชิงสถิติ & พื้นฐาน)
1. **Multiple Compression vs. Fundamentals:**
   * พื้นฐานของบริษัทยังแข็งแกร่ง (Backlog การเติบโตของระบบระบายความร้อน Liquid Cooling ยังคงโตสูง) แต่ราคาหุ้นในช่วงเข้าซื้อเทรดที่ Forward P/E สูงเกิน 35x ทำให้มีความเปราะบางต่อแรงขายทำกำไร
2. **Timing & Staggered Entry (DCA Gaps):**
   * การเข้าซื้อไม้แรกมีขนาด Position Size ใหญ่เกินไปในคราวเดียว ขาดการทยอยแบ่งไม้ (Staggered DCA) ในจังหวะที่ RSI อยู่ในโซน Overbought

---

## 3. Corrective Actions & Prevention Rules (กฎเกณฑ์ป้องกันในอนาคต)
1. **The 'Never All-In at High Multiples' Rule:** หาก Forward P/E ของหุ้น Growth สูงกว่าค่าเฉลี่ย 5 ปีเกิน +1.5 Standard Deviation ห้ามเปิด Position เกิน 50% ของเป้าหมายในไม้แรก
2. **Cash Buffer Protection:** คงระดับเงินสดสำรอง 15-20% เสมอ (เหมือนที่ทำอยู่ในปัจจุบัน .25) เพื่อรอจังหวะ Rebalance หรือถัวเฉลี่ยในจุด Fair Value
3. **Holding Verdict:** คงสถานะ HOLD เนื่องจากแนวโน้มความต้องการ Liquid Cooling สำหรับเซิร์ฟเวอร์ AI ยุคใหม่ (Blackwell / Rubin) ยังเป็นเมกะเทรนด์ระยะยาว
