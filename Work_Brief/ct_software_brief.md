# 🎯 CT Software — Comprehensive Interview Cheat Sheet

**Company:** CT Software Co., Ltd.  
**Role Target:** Software QA Tester / Automation QA Engineer  
**Candidate:** Natawat Tephassadin na Ayutaya (Namo)  
**Date Updated:** August 13, 2026  

---

## 📌 1. Self-Introduction (แนะนำตัว 1 นาที — กระชับ ตรงประเด็น)

### 🇹🇭 ภาษาไทย
> "สวัสดีครับ ผมชื่อ นาถวัฒน์ เทพหัสดิน ณ อยุธยา (นะโม) จบจากคณะ ICT มหาวิทยาลัยมหิดล มีประสบการณ์ฝึกงาน QA Tester รวม 8 เดือนครับ
>
> ในช่วงฝึกงาน ผมได้รับหน้าที่ดูแลการทดสอบระบบ **iNT Connect** ซึ่งเป็นแพลตฟอร์มของมหาวิทยาลัยมหิดล ผมได้ออกแบบและบริหารจัดการ Test Cases รวมกว่า 260 test cases ครอบคลุมทั้ง Functional, Web UI, API Testing และ Role-based Access Control 
>
> จุดเด่นของผมคือความเชี่ยวชาญด้าน Automation Testing โดยใช้ **Playwright (TypeScript)** และ **Robot Framework (Python)** รวมถึง **Postman** สำหรับ API รวมทั้งการต่อ Automated Test เข้ากับ **GitHub Actions CI/CD** ครับ ผมชอบการทำงานร่วมกับทีม Dev ในรูปแบบ Agile และกระตือรือร้นในการนำ AI มาช่วยเพิ่มประสิทธิภาพงาน QA ครับ"

### 🇬🇧 ภาษาอังกฤษ
> "Hello, my name is Natawat, a recent graduate from Mahidol University, Faculty of ICT. I have 8 months of QA internship experience.
>
> During my internship, I worked on the **iNT Connect** web platform. I designed and executed over 260 test cases covering Functional UI, Postman API testing, and Access Control.
>
> My key strength is QA Automation using **Playwright with TypeScript**, **Robot Framework with Python**, and **Postman**. I also set up automated test pipelines using **GitHub Actions CI/CD**. I am eager to apply my automation skills to contribute to CT Software."

---

## 🧪 2. เจาะลึก Smoke vs Sanity vs Regression Testing

| มิติการเปรียบเทียบ | 1. Smoke Testing | 2. Sanity Testing | 3. Regression Testing |
| :--- | :--- | :--- | :--- |
| **ชื่อเรียกทางการ** | Build Verification Testing | Component Verification Testing | Full System Assurance Testing |
| **ขอบเขต (Scope)** | **กว้าง แต่ไม่ลึก** (Shallow & Wide) | **แคบ แต่ลึกเฉพาะจุด** (Narrow & Deep) | **กว้าง และ ลึกทั้งระบบ** (Wide & Deep) |
| **เป้าหมายหลัก** | เช็กว่า Build ใหม่ที่ได้มามีความเสถียรพอที่จะเริ่มเทสเชิงลึกหรือไม่ | ยืนยันว่าการแก้บั๊กเฉพาะจุด หรือ Feature เล็กๆ ทำงานได้ถูกต้องไม่กระทบส่วนข้างเคียง | ยืนยันว่าการแก้โค้ดใหม่ **ไม่ไปทำลาย (Break) ฟังก์ชันเดิมที่เคยรันได้** |
| **เมื่อไหร่ที่ทำ** | ทำทันทีเมื่อรับ Build ใหม่จาก Dev ก่อนลงมือเทสอื่น | ทำหลังจาก Dev ส่งการแก้บั๊กเฉพาะจุดมาให้เทสซ้ำ | ทำก่อน Release ใหญ่ หรือหลัง Merge โค้ดสำคัญ |
| **การทำ Automation** | รันด้วยสคริปต์สั้นๆ (5-10 นาที) | มักทำด้วยการ Manual หรือ Script เฉพาะจุด | **ใช้อัลกอริทึม Automation รัน 100% (จุดที่ Playwright/Robot มีคุณค่าสูงสุด)** |

### 💡 ตัวอย่างการอธิบาย:
* **Smoke:** "พึ่งได้ Build ใหม่มา ลองเปิดแอป ล็อกอิน กดเข้าเมนูหลัก ถ้าระบบค้างหรือเปิดไม่ติด ➔ **Reject Build คืน Dev ทันที**"
* **Sanity:** "Dev แก้บั๊กคำนวณส่วนลดราคาท้ายตะกร้ามาส่ง ➔ **เทสเจาะลึกเฉพาะฟังก์ชันส่วนลดนั้น**"
* **Regression:** "มีการเพิ่มระบบชำระเงินแบบใหม่ ➔ **ใช้ออโตเมชันรันเทสระบบทั้งหมดตั้งแต่นับหนึ่ง** เพื่อให้มั่นใจว่าฟังก์ชันเดิม เช่น การสมัครสมาชิก และการค้นหาสินค้าไม่พัง"

---

## 🌐 3. เจาะลึก API Testing (Postman & REST API Validation)

การทำ API Testing ไม่ใช่แค่การกด Send แต่คือการ **ตรวจสอบความถูกต้อง 5 ชั้น (5-Layer API Verification)**:

### 1. HTTP Status Code Validation (สถานะที่ตอบกลับ):
* **200 OK:** ดึง/อัปเดตข้อมูลสำเร็จ
* **201 Created:** สร้าง Resource ใหม่สำเร็จ (เช่น สมัครสมาชิกใหม่)
* **400 Bad Request:** Client ส่งข้อมูล/Payload ผิดฟอร์แมต (เช่น ขาดฟิลด์บังคับ)
* **401 Unauthorized:** ไม่ได้ใส่ Token/JWT หรือ Token หมดอายุ
* **403 Forbidden:** มี Token แต่ไม่มีสิทธิ์เข้าถึง (Access Control / RBAC)
* **404 Not Found:** ไม่พบ Endpoint หรือข้อมูลที่ร้องขอ
* **500 Internal Server Error:** โค้ดฝั่ง Backend เกิด Crash/Exception

### 2. HTTP Methods & Operations:
* `GET` = อ่านข้อมูล (Must be Idempotent / ไม่แก้ไขข้อมูล)
* `POST` = สร้างข้อมูลใหม่
* `PUT` / `PATCH` = อัปเดตข้อมูล (PUT แก้ทั้งก้อน / PATCH แก้เฉพาะฟิลด์)
* `DELETE` = ลบข้อมูล

### 3. Response Time Check:
* เช็กว่า API ตอบกลับภายในเกณฑ์ Performance ที่กำหนดหรือไม่ (เช่น `<500ms`)

### 4. Response Payload & JSON Schema Validation:
* เช็กว่าโครงสร้าง JSON ตอบกลับตรงตาม Data Type ที่ตกลงไว้ (เช่น `id` เป็น integer, `email` เป็น string, `items` เป็น array)

### 5. Negative & Error Handling Test:
* ลองส่ง Payload ผิดประเภท (เช่น ส่ง String ในฟิลด์ที่รับตัวเลข) เพื่อเช็กว่า Backend จัดการ Exception และตอบกลับ Error Message ที่เป็นมิตร ไม่หลุด Stack Trace ออกมา

---

## 💡 4. หลักการคิด Test Case สำหรับโจทย์เปิด (5-Block Framework)

```
[1. Functional (Happy/Negative)] ➔ [2. Boundary & Edge Cases] ➔ [3. Non-Functional & Security] ➔ [4. Hardware/Offline/Stress] ➔ [5. UI/UX Feedback]
```

### ตัวอย่างโจทย์ A: "เครื่องแตะบัตรเข้างาน"
1. **Functional:** Happy Path (แตะถูกเวลา -> ไฟเขียว + บันทึกเวลา) / Negative (แตะบัตรหมดอายุ/ผิดใบ -> ไฟแดง + ไม่บันทึกเวลา)
2. **Boundary & Edge Cases:** แตะซ้ำทันที (Double-tap debounce) / แตะค้างไว้นาน / แตะตอน 23:59:59 vs 00:00:00
3. **Security:** ป้องกันการก๊อปปี้รหัส RFID (Cloning) / การดักจับแพ็กเกจส่งข้อมูล
4. **Offline & Stress:** **Offline Mode** (เน็ตหลุด เครื่องต้องแคชข้อมูลไว้แล้ว auto-sync เมื่อเน็ตกลับมา) / คนแตะ 1,000 คนตอน 08:59 น. (Stress Test) / ไฟดับข้อมูลไม่หาย
5. **UI/Feedback:** เสียง Beep และจอ LCD แสดงผลถูกต้อง

---

## 🏗️ 5. Page Object Model (POM) คืออะไร และทำไมถึงสำคัญ?

* **คำตอบหลักการ:**  
  > "**Page Object Model (POM)** คือ Design Pattern ในการทำ Automation Testing ที่ **แยกโครงสร้างหน้าเว็บ (Web Elements/Locators) ออกจากขั้นตอนการรันเทส (Test Scripts)** อย่างชัดเจนครับ"
* **ประโยชน์ 3 ข้อ:**
  1. **Maintainability (ซ่อมง่าย):** เมื่อ UI เปลี่ยน แก้แค่ไฟล์ Page Class จุดเดียว Test Script ทั้งหมดรันผ่านต่อได้ทันที
  2. **Reusability (ใช้ซ้ำได้):** เมธอดเช่น `login()`, `fillForm()` เขียนไว้ที่เดียว แล้วถูกเรียกใช้ซ้ำในหลายๆ Test Cases ได้เลย
  3. **Readability (อ่านง่าย):** โค้ดใน Test Script จะสะอาด อ่านเข้าใจง่ายเหมือนภาษาพูด เช่น `loginPage.submitLogin(user, pass)`

---

## 🙋‍♂️ 6. คำถามเด็ดที่เราควรถามกลับผู้สัมภาษณ์ (Reverse Questions)

1. *"สำหรับตำแหน่งนี้ที่ CT Software เครื่องมือหรือ Framework หลักที่ทีมใช้อยู่ในปัจจุบันคือตัวไหนเป็นหลักครับ?"*
2. *"กระบวนการทำงานร่วมกันระหว่างทีม QA, Dev และ PM ในโครงการของ CT Software เป็นรูปแบบไหนครับ (เช่น Agile/Scrum)?"*
3. *"เป้าหมายหรือความท้าทายสำคัญของทีม QA ในช่วง 3-6 เดือนข้างหน้าคืออะไรครับ?"*
