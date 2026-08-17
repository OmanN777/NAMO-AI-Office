# 🏢 Work Brief: KASIKORN LINE (LINE BK) - Junior Quality Assurance (1-Year Contract)

> **[IMPORTANT] INTERVIEW SCHEDULE CONFIRMED:**
> * **📅 วัน-เวลาสัมภาษณ์:** วันพุธที่ 22 กรกฎาคม 2569 เวลา 15:30 - 16:30 น. (3.30 PM)
> * **👤 ผู้สัมภาษณ์:** พี่อ้อม (QA Manager)
> * **📱 ผู้ติดต่อ (HR/TA Partner):** คุณแพร (Yutika Shinthawanna) | Tel: +66 84 550 0054 | LINE ID: pearc
> * **🎯 จุดเน้นหลักของตำแหน่งนี้:** **Manual Testing & Functional Testing (Mobile Social Banking)**
> * **🔗 ลิงก์สัมภาษณ์ MS Teams:** [คลิกเพื่อเข้าห้อง MS Teams Meeting](https://teams.microsoft.com/meet/439853535772507?p=qJdY3bBey8NoO3m3MW)
>   * **Meeting ID:** 439 853 535 772 507 | **Passcode:** LL2QP69p

---

## 📌 1. ข้อมูลเกี่ยวกับ LINE BK (Product & Domain Knowledge)
* **KASIKORN LINE (LINE BK)** เป็นแอปพลิเคชันประเภท **Social Banking บนแอป LINE**
* **4 ผลิตภัณฑ์หลักที่ต้องทดสอบแบบ Manual:**
  1. **วงเงินให้ยืม / สินเชื่อดิจิทัล (Credit Line & Personal Loan):** การสมัครวงเงิน, การอนุมัติ, การถอนเงินสินเชื่อเข้าบัญชี, การผ่อนชำระ
  2. **บัญชีเงินฝาก (Savings & Special Rate):** การเปิดบัญชีฝากประหยัด, บัญชีดอกเบี้ยพิเศษ
  3. **บัตรเดบิต LINE BK (Debit Card):** บัตรเดบิตออนไลน์ / บัตรเดบิตพร้อมอายัด, การผูกบัญชี
  4. **บริการโอนเงิน & การแจ้งเตือน (Transfer & LINE Alerts):** โอนเงินแชทผ่าน LINE, ข้อความแจ้งเตือนเงินเข้า-ออก

---

## 🎯 2. สรุปกลยุทธ์การสัมภาษณ์เน้น Manual QA Excellence

เมื่อตำแหน่งนี้เน้น **Manual Testing** เป็นหลัก สิ่งที่พี่อ้อม (QA Manager) จะพิจารณาคือ **ความละเอียด ความครอบคลุมของเทสเคส และทักษะการจับบั๊กบน Mobile App** ค่ะ:

### 🔹 1. ทักษะการออกแบบ Test Case & Test Scenario (Test Design Techniques)
* **Equivalence Partitioning (EP) & Boundary Value Analysis (BVA):**
  * เช่น การทดสอบขอวงเงินสินเชื่อขั้นต่ำ 1,000 บาท ถึงสูงสุด 500,000 บาท
  * การโอนเงินยอด 0.01 บาท, ยอดเท่ากับเงินคงเหลือพอดี
* **Decision Table Testing:**
  * การทดสอบเงื่อนไขอนุมัติวงเงินสินเชื่อตามรายได้และเอกสารประกอบ

### 🔹 2. ทักษะการทำ Exploratory Testing บน Mobile (LINE App Platform)
* **Mobile Specific Scenarios:**
  * การทดสอบบนต่าง OS (iOS vs Android) และความละเอียดหน้าจอต่างๆ
  * **Interruption Testing:** เน็ตหลุดระหว่างกดยืนยันโอนเงิน, สายโทรเข้าขณะกำลังป้อน PIN รหัสผ่าน, LINE Notification เด้งขึ้นมาแทรก
  * **Background / Foreground Testing:** การพับแอป LINE ไปทำอย่างอื่นแล้วกลับเข้ามา หน้าจอต้องล็อก PIN ป้องกันความปลอดภัย

### 🔹 3. การเปิด Defect ใน Jira อย่างมืออาชีพ (Defect Management)
* รายงานบั๊ก 7 สเต็ปมาตรฐาน: Summary, Pre-conditions, Steps to Reproduce, Expected, Actual, Device/OS Version, และแนบ Screen Recording / Screenshots
* การตรวจสอบ API ด้วย Postman และ DB Data ด้วย SQL สั้นๆ เพื่อช่วย Dev ตรวจสอบสาเหตุเบื้องต้น

### 🔹 4. จุดเด่นเพิ่มเติม: AI-Augmented Manual QA
* *"แม้ว่างานหลักจะเป็น Manual Test แต่ผมสามารถนำ AI Tools มาช่วยเจนเนอเรต Test Scenarios และ Edge Cases เพิ่มเติม ทำให้การทำ Manual Test มีความครอบคลุม (Test Coverage) สูงสุด และไม่หลุดเคสวิกฤตครับ"*
