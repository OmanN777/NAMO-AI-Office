# 🎯 Focus 7 Blueprint: Selected Tools & Techniques (2026)

**ผู้จัดทำ:** มอลิ (Malli - Chief Executive Secretary)  
**เป้าหมาย:** บันทึกแผนการติดตั้ง ใช้งาน และกระจายงานสู่ Agent ทั้ง 7 คนสำหรับ 7 เครื่องมือ/เทคนิคที่บอสเลือก  
**วันที่บันทึก:** 30 สิงหาคม 2026  

---

## 🛠️ รายการ 7 โฟกัสหลักที่เลือก (The Selected 7)

### 1. 🎭 Playwright MCP Server (Official / ExecuteAutomation)
* **ผู้รับผิดชอบหลัก:** Malli & Namo (QA Automation)
* **สถานะ:** คอนฟิกใน [`mcp_config.json`](file:///C:/Users/namo_/.gemini/config/mcp_config.json) เรียบร้อย (`npx @executeautomation/playwright-mcp-server`)
* **Use Case:** ให้ AI เปิดเบราว์เซอร์จริง, ตรวจสอบ DOM/Accessibility Tree, รันสคริปต์ Playwright, แคปภาพหน้าจอตรวจสอบ Visual Bugs และ Auto-Heal Locators ทันทีในแชท

---

### 2. 🐙 GitHub MCP Server (`@modelcontextprotocol/server-github`)
* **ผู้รับผิดชอบหลัก:** Malli & Reese
* **สถานะ:** คอนฟิกใน [`mcp_config.json`](file:///C:/Users/namo_/.gemini/config/mcp_config.json) เรียบร้อย (รอใส่ GitHub Personal Access Token เมื่อต้องการเชื่อมต่อ)
* **Use Case:** ตรวจสอบ Pull Requests, อ่าน Failure Logs จาก GitHub Actions CI/CD Pipeline และดึงโค้ดมาร่วมรีวิวอัตโนมัติ

---

### 3. 📊 Financial Modeling Prep (FMP API)
* **ผู้รับผิดชอบหลัก:** Fundamentokung (Valuation Lead)
* **สถานะ:** เตรียมสคริปต์ตัวดึงข้อมูลใน `Scripts/`
* **Use Case:** ดึงข้อมูลงบดุล (Balance Sheet), งบกระแสเงินสด (Cash Flow Statement), และ Free Cash Flow (FCF) ย้อนหลัง 5 ปีของหุ้นใน Master Universe 25 ตัว

---

### 4. 🏛️ SEC EDGAR RSS / Insider Trading Radar (Form 4 & 8-K)
* **ผู้รับผิดชอบหลัก:** Newwy (News Scout) & Oman (CIO)
* **สถานะ:** พร้อมเชื่อมต่อ Webhook ผ่าน SEC EDGAR Public API (ฟรี ไม่ต้องใช้ Token)
* **Use Case:** สแกนหาการเข้าซื้อหุ้นของผู้บริหาร (Insider Buying) และรายงานเหตุการณ์พิเศษด่วน (8-K) ของหุ้นเป้าหมายเพื่อเป็น Leading Indicator

---

### 5. 🧮 Scenario-Based DCF Modeling (Bull / Base / Bear Valuation)
* **ผู้รับผิดชอบหลัก:** Fundamentokung (Valuation Lead)
* **สถานะ:** จัดทำเป็นมาตรฐานการประเมินมูลค่า Fair Value
* **Use Case:** คำนวณราคายุติธรรมของหุ้น Growth/AI โดยแบ่งเป็น 3 สถานการณ์ (Bull Case / Base Case / Bear Case) เพื่อหาจุด Margin of Safety ในการเข้าซื้อ

---

### 6. ⚖️ Risk-Parity & Volatility-Weighted Sizing
* **ผู้รับผิดชอบหลัก:** Vera (Quant & Risk Manager)
* **สถานะ:** ประยุกต์ใช้กับพอร์ตจำลอง Oman และการคำนวณ DCA พอร์ตจริง
* **Use Case:** คำนวณขนาดไม้ลงทุนตามความผันผวน (หุ้นซิ่งขนาดเล็กความผันผวนสูง ให้สัดส่วนน้อย, หุ้น Mega-Cap ให้สัดส่วนหลัก) เพื่อคุม Drawdown ไม่ให้พอร์ตเหวี่ยงรุนแรง

---

### 7. 🎙️ Whisper AI / Audio Transcription Pipeline
* **ผู้รับผิดชอบหลัก:** Tubemaster (YouTube Gaming Director)
* **สถานะ:** ใช้คู่กับ `capcut_mcp_server` ที่ติดตั้งแล้ว
* **Use Case:** แปลงเสียงพูดในคลิปสตรีมเกมยาวๆ เป็นข้อความและช่วงเวลา (Timestamps) เพื่อให้ AI หาช็อตไฮไลต์และส่งไปตัดต่อเป็น Shorts บน CapCut ได้อัตโนมัติ
