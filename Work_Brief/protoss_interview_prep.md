# 🎯 คู่มือพิชิตสัมภาษณ์เทคนิค Protoss Technology (Automate Tester - Krungsri 1KS Project)

คู่มือฉบับนี้เตรียมไว้สำหรับบอส **นะโม** เพื่อใช้ในการติวเข้มและตอบคำถามสัมภาษณ์ด้วยแนวคิดแบบ **Senior-ready QA** (เป็นกลาง เป็นจริง กระชับ และไม่โอ้อวด) โดยอ้างอิงจากประสบการณ์ฝึกงาน 8 เดือน และการทำโปรเจกต์อัตโนมัติจริงค่ะ

---

## 💻 ส่วนที่ 1: เฉลยคำตอบแนวทาง Guideline 23 ข้อ (Factual & Professional Answers)

### 1. Flow การทำงาน ตั้งแต่ได้รับ Requirement จนถึง Production
* **คำตอบ:** "เริ่มจากเมื่อได้รับ Requirement (มักอยู่ในรูปของ User Story หรือ PRD) ผมจะเข้าร่วมประชุม **Refinement/Planning** เพื่อคุยทำความเข้าใจร่วมกับ Product Owner (PO), System Analyst (SA) และทีม Developer จากนั้นผมจะเริ่มร่าง **Test Scenario และ Test Case** เพื่อส่งให้ทีมหรือ Developer รีวิวคู่ขนานไปกับการพัฒนาของ Dev เมื่อ Dev พัฒนาเสร็จและส่งงานขึ้น Environment สำหรับการเทส (เช่น QA/SIT) ผมจะเริ่มรัน **Manual Test** ในรอบแรกเพื่อตรวจเช็กฟังก์ชันการทำงานหลัก (Smoke Test) และรัน **Automation Script** สำหรับการทำ Regression Test เมื่อเทสผ่านตามเกณฑ์ (Exit Criteria) ก็จะเซ็น UAT Sign-off เพื่อเตรียม Deploy ขึ้น Production โดยหลังจากขึ้น Production แล้ว ผมจะทำการรัน **Sanity/Smoke Test บน Production** อีกครั้งเพื่อยืนยันว่าระบบทำงานได้ปกติไม่มีสิ่งใดผิดพลาดหลัง Deployment ครับ"

### 2. เวลาเขียน Test Case Review ทำร่วมกับใครบ้าง
* **คำตอบ:** "ในการรีวิว Test Case ผมจะนัดหมายรีวิวร่วมกับ **Product Owner (PO) หรือ System Analyst (SA)** เพื่อดูว่าครอบคลุม Business Logic และ Accept Criteria ครบถ้วนหรือไม่ และรีวิวร่วมกับ **Lead Developer หรือ Developer** ประจำฟีเจอร์นั้นๆ เพื่อยืนยันว่ามี Technical Flow หรือข้อยกเว้น (Exception handling) ตัวไหนที่ผมอาจจะตกหล่นไปบ้างครับ"

### 3. รูปแบบการทำงาน (Agile / Scrum / Waterfall)
* **คำตอบ:** "ช่วงฝึกงานผมทำงานในรูปแบบ **Agile (Scrum Framework)** ครับ มีรอบการทำงานเป็น Sprint (เช่น 2 สัปดาห์) มีพิธีกรรมต่างๆ อย่าง Daily Scrum ทุกเช้าเพื่ออัปเดตงาน, Sprint Planning ก่อนเริ่มรอบงาน, Sprint Review/Demo หลังจบ Sprint และ Sprint Retrospective เพื่อปรับปรุงการทำงานภายในทีมครับ"

### 4. ทำงานในส่วนไหนบ้าง ทำได้ทั้ง Manual และ Automate เลยไหม
* **คำตอบ:** "ผมทำได้ทั้งสองส่วนครับ โดยสัดส่วนจะเริ่มที่การทำความเข้าใจ Requirement และเขียนเทสเคสสำหรับ **Manual Test** ก่อนเพื่อทดสอบกรณีปกติ (Positive) และกรณีแปลกๆ (Negative) ในรอบแรก จากนั้นสำหรับเทสเคสที่มีการทำงานซ้ำๆ หรือฟีเจอร์ที่มีความเสถียรแล้ว ผมจะนำมาพัฒนาต่อเป็น **Automation Script** ด้วย Playwright หรือ Robot Framework เพื่อประหยัดเวลาในการทำ Regression Test รอบถัดไปครับ"

### 5. ได้รับ Requirement มาจากใคร ก่อนจะทำการเขียนเทส
* **คำตอบ:** "ปกติผมจะอ่านและวิเคราะห์ Requirement ที่ส่งต่อมาจาก **Product Owner (PO) หรือ System Analyst (SA)** ซึ่งเขียนไว้ในการ์ดงานบน Jira หรือในเอกสาร Requirement Specification ครับ"

### 6. ใช้ Tool อะไรบ้างในการทำงาน
* **คำตอบ:** 
  * **Test Automation:** Playwright, Robot Framework (Python/TypeScript)
  * **Test Management & Bug Tracking:** Jira, Confluence, Trello
  * **API Testing:** Postman, Thunder Client
  * **Database:** DBeaver, MySQL, PostgreSQL (ใช้เขียน SQL Query เพื่อตรวจสอบข้อมูลหลังบ้าน)
  * **Version Control:** Git, GitHub, GitLab

### 7. หากหยิบการ์ดงานมาทำ แล้วไม่เข้าใจ Requirement จะทำอย่างไร
* **คำตอบ:** "อันดับแรกผมจะค้นหาและอ่านข้อมูลเพิ่มเติมในเอกสารรายละเอียดบน Confluence หรือการ์ดงานอื่นที่เกี่ยวข้องก่อนครับ หากยังไม่ชัดเจน ผมจะ **จดประเด็นคำถามที่สงสัยเป็นข้อๆ** แล้วทักไปคุยกับ SA หรือ PO เพื่อขอคำชี้แจงโดยตรง ไม่เดา Requirement เองเด็ดขาด เพราะหากเข้าใจผิดจะทำให้เขียนเทสเคสและสคริปต์ผิดพลาดตามไปด้วยครับ"

### 8. เทส Web หรือ Mobile มากกว่ากัน
* **คำตอบ:** "ในช่วงการฝึกงานและทำโปรเจกต์ที่ผ่านมา ผมมีประสบการณ์เทสทั้ง **Web Application และ Mobile Application** ควบคู่กันครับ โดย Web App จะเน้นการทำ E2E automation ด้วย Playwright ส่วน Mobile App จะเน้นการทำ Manual Test บน Emulator/Real Device และฝึกเขียนสคริปต์อัตโนมัติด้วย Appium ครับ"

### 9. สามารถเทสทั้ง Front-End และ Back-End ได้ไหม
* **คำตอบ:** "ทำได้ครับ โดย **Front-End** จะเทสผ่าน UI, ตรวจสอบการแสดงผลของ Element, Responsive Design, และพฤติกรรมการตอบสนองของผู้ใช้ ส่วน **Back-End** จะเทสผ่าน API (Postman) เพื่อดูการตอบสนองของ Response (JSON), รหัส HTTP Status Code และเขียนคำสั่ง SQL Query เข้าไปค้นหาข้อมูลใน Database โดยตรงเพื่อตรวจสอบความถูกต้องของข้อมูลหลังบ้านครับ"

### 10. เคยเขียน SQL Queue ไหม (หมายถึง SQL Query ในการดึงข้อมูลและทำคิวรี่ตรวจสอบ)
* **คำตอบ:** "เคยครับ ผมเขียน SQL Query เพื่อใช้ตรวจสอบความถูกต้องของข้อมูล (Data Verification) ในตารางหลังบ้านเป็นประจำ เช่น การใช้ `SELECT` ร่วมกับ `WHERE`, `JOIN` เพื่อดึงข้อมูลข้ามตารางเพื่อตรวจสอบธุรกรรม, การใช้ `ORDER BY` และ `LIMIT` เพื่อสืบค้นข้อมูลธุรกรรมล่าสุด และการใช้คำสั่ง `UPDATE` ในสภาพแวดล้อมเทส (Test environment) เพื่อเปลี่ยนสถานะข้อมูลในการทดสอบเคสต่าง ๆ ครับ"

### 11. เคยเทส API ไหม
* **คำตอบ:** "เคยเทสเป็นประจำครับ โดยใช้เครื่องมืออย่าง **Postman** ในการส่ง Request (GET, POST, PUT, DELETE) พร้อมทั้งส่ง Header และ Body ไปยัง API Endpoint จากนั้นตรวจสอบ Response Body ที่ตอบกลับมาว่าเป็นข้อมูลรูปแบบ JSON ที่ถูกต้องหรือไม่ ตรวจสถานะของ HTTP Response Status Code และเช็ก Response Time ให้ตรงตามเอกสารสเปกของระบบครับ"

### 12. หากเจอเหตุการณ์ที่ทำการเทสอยู่แล้วมีเวลาจำกัด จะทำอย่างไร
* **คำตอบ:** "ผมจะใช้วิธี **Prioritization (การจัดลำดับความสำคัญ)** โดยคุยร่วมกับทีมและ PO เพื่อแยกแยะว่าส่วนใดคือฟีเจอร์หลักที่เป็น Core Business Value และมีระดับความเสี่ยงสูง (High Risk/High Priority) เช่น ระบบโอนเงิน/ชำระเงินสำเร็จ และจะเลือกเน้นเทสกรณีหลักเหล่านั้นก่อน (Happy Path/Smoke Test) ส่วนเคสที่เป็นขอบเขตย่อยหรือ Edge Cases ที่มีความเสี่ยงต่ำ จะทยอยเทสทีหลังเพื่อไม่ให้บล็อกวันปล่อยงาน (Release date) ครับ"

### 13. ถ้ามีเวลาจำกัด จะเลือกเทส Mobile หรือ API ก่อน
* **คำตอบ:** "ผมเลือกเทส **API ก่อน** ครับ เพราะการเทส API (Back-End) ช่วยให้เราเจอข้อผิดพลาดทางด้าน Business Logic และการไหลเวียนข้อมูลหลังบ้านได้เร็วกว่า (Early Testing / Shift Left) หาก API ขัดข้อง ตัว Mobile UI ก็จะไม่สามารถใช้งานได้อยู่ดี การคอนเฟิร์มว่า API ทำงานถูกต้องและปลอดภัยก่อน จะช่วยให้การเทส Mobile UI ในภายหลังรวดเร็วและจับจุดบั๊กได้ง่ายขึ้นครับ"

### 14. เวลาเปิดเจอ Defect กรอกอะไรลงใน Jira บ้าง
* **คำตอบ:** "ข้อมูลที่จำเป็นอย่างน้อยในการเปิดบั๊กของผมมีดังนี้ครับ:
  1. **Summary:** ชื่อหัวข้อบั๊กที่สั้น กระชับ แต่อ่านเข้าใจทันทีว่าเกิดอะไรขึ้นที่ส่วนใด
  2. **Description (Steps to Reproduce):** ขั้นตอนการรันระบบทีละขั้นตอนเพื่อให้ผู้อื่นสามารถรันตามเพื่อเจอบั๊กตัวเดิมได้
  3. **Expected Result:** ผลลัพธ์ที่ถูกต้องตาม Requirement
  4. **Actual Result:** ผลลัพธ์จริงที่พบว่าเกิดข้อผิดพลาด
  5. **Environment:** ข้อมูลแพลตฟอร์มที่ทดสอบ เช่น OS (iOS/Android/Windows), เวอร์ชันแอป, เบราว์เซอร์
  6. **Evidence:** หลักฐานประกอบ เช่น รูปภาพ Screenshot, ไฟล์บันทึกหน้าจอ (Recording), หรือ Log ข้อผิดพลาดของระบบ
  7. **Severity / Priority:** ระดับความรุนแรงและระดับความสำคัญของบั๊ก"

### 15. ทีมที่ทำงานร่วมกันมีกี่คน และมีใครบ้าง
* **คำตอบ:** "ในทีมพัฒนาที่ผมเคยทำงานร่วมด้วย มีสมาชิกประมาณ 8-10 คน ประกอบด้วย Product Owner (PO) 1 คน, System Analyst (SA) 1 คน, Scrum Master 1 คน, Front-End Developer 2 คน, Back-End Developer 2 คน และมีทีม QA (Manual & Automate) 2 คนครับ"

### 16. ทีม Automate กับ ทีม Manual แชร์ Scope งานกันไหม
* **คำตอบ:** "แชร์กันอย่างใกล้ชิดครับ โดยทีม Manual จะทำหน้าที่นำ Requirement มาออกแบบเขียนรายละเอียด Test Case และทำเทสในรอบแรกเพื่อให้ระบบนิ่ง จากนั้นทีม Manual จะระบุว่าเทสเคสไหนที่มีความสำคัญและมีลักษณะการทำงานซ้ำๆ (Regression Suite) เพื่อส่งต่อข้อมูลให้ทีม Automate นำไปเขียนโค้ดสคริปต์รันอัตโนมัติ ช่วยลดความซ้ำซ้อนของการทำงานครับ"

### 17. เคยทำงานมากกว่า 1 โปรเจกต์ในเวลาเดียวกันไหม (การบริหารงาน)
* **คำตอบ:** "เคยครับ วิธีการจัดการของผมคือ **1. จัดระดับความสำคัญ (Priority) ของงานรายวัน** โดยใช้บอร์ดคัมบัง (Kanban/Jira) ช่วยดู 2. คอยอัปเดตบล็อกเกอร์หรือจุดขัดข้องให้ทีมรับทราบใน Daily Standup เพื่อให้วางแผนช่วยเหลือได้ทันท่วงที 3. แบ่งบล็อกเวลาการทำงาน (Time-blocking) สำหรับพัฒนาสคริปต์อัตโนมัติสลับกับการทำ Manual Test เพื่อไม่ให้งานใดงานหนึ่งล่าช้าเกินกำหนดครับ"

### 18. ถ้าเทสไม่เสร็จเรียบร้อย แต่จำเป็นต้องส่งงานทันที จะจัดการอย่างไร
* **คำตอบ:** "ผมจะทำการสรุปข้อมูลผลกระทบจริงและระดับความเสี่ยงของฟีเจอร์ที่ยังเทสไม่เสร็จ (Remaining Scope) ออกมาอย่างละเอียด เพื่อรายงานให้ QA Lead, Dev Lead และ PO ทราบทันที โดยจะแสดงรายงานส่วนที่เทสผ่านไปแล้ว (Passed) และจุดที่ยังมีบั๊กค้างอยู่ (Open Bugs) เพื่อให้ทีมและผู้บริหารประเมินร่วมกันว่าจะตัดสินใจปล่อยงานแบบจำกัดฟีเจอร์ (Feature Toggle) หรือยอมเลื่อนเวลาปล่อยออกไปตามระดับความเสี่ยงทางธุรกิจครับ"

### 19. เลือกเคสไหนเป็น Manual และเคสไหนเป็น Automate
* **คำตอบ:**
  * **เคสที่เลือกทำ Automate:** เคสที่เป็น Regression Test (รันซ้ำทุก Sprint), เคสการคำนวณซับซ้อนที่มีความเสถียรไม่มีการเปลี่ยน UI บ่อยๆ, Happy Path หลักของระบบ, เคสทดสอบความเข้ากันได้ของระบบ (Compatibility test ข้ามเวอร์ชัน)
  * **เคสที่เลือกทำ Manual:** เคสทดสอบรอบแรกที่เพิ่งพัฒนาเสร็จใหม่ๆ (ยังไม่เสถียร), เคสเกี่ยวกับความคุ้มค่า/ความรู้สึกของผู้ใช้งาน (UX/UI Look and feel), เคสข้อยกเว้นแปลกๆ (Ad-hoc / Exploratory Testing) ที่เกิดขึ้นได้ยากและใช้เวลาเขียนโค้ดสคริปต์ไม่คุ้มทุน

### 20. เคยมี Bug หลุดไปถึง Production ไหม (หากเคย มีวิธีจัดการอย่างไร)
* **คำตอบ:** "เคยพบครับ วิธีการจัดการของผมคือ:
  1. **Hotfix & Mitigate:** รายงานแจ้งบั๊กใน Jira ทันทีและประสานงานกับทีม Dev เพื่อหาสาเหตุและหาวิธีสกัดกั้นผลกระทบ (เช่น การปิดสวิตช์ฟีเจอร์ชั่วคราว หรือเร่งทำ Hotfix)
  2. **Verify:** เมื่อ Dev พัฒนา Hotfix เสร็จเรียบร้อย ผมจะรีบเข้าไปทำการทดสอบตรวจซ้ำบน Environment จำลองและ Production ทันทีหลัง Deployment
  3. **Root Cause Analysis & Retrospective:** นำปัญหานี้เข้าคุยใน Retrospective เพื่อวิเคราะห์ร่วมกันว่าหลุดไปได้อย่างไร และเพิ่ม Test Scenario ตัวนี้เข้าไปใน Automation Regression Suite เพื่อป้องกันไม่ให้เกิดบั๊กเดิมซ้ำซากในอนาคตครับ"

### 21. Project ที่ยากที่สุดที่เคยทำงานมา
* **คำตอบ:** "สำหรับผมคือโปรเจกต์พัฒนาระบบเทส **Visual QA Agent ด้วย Playwright ร่วมกับ Gemini Vision API** ครับ ความยากคือระบบ UI ปลายทางมักมีการเปลี่ยนแปลงพิกัดการวางหน้าจอหรือดีไซน์ปุ่ม ทำให้ Selector ของโค้ดอัตโนมัติแบบเดิมหักง่าย ผมจึงต้องศึกษาการผสานงานของ AI เพื่อให้ตัวสคริปต์ตรวจวิเคราะห์ความผิดพลาดจากหน้าจอภาพจับโดยอัตโนมัติแทนการใช้ Hardcoded Locator แบบเดิม ทำให้เข้าใจเชิงลึกเรื่องการทำ Visual Regression Testing และการใช้ API ข้ามระบบครับ"

### 22. เคยมีปัญหากับคนในทีม หรือ User บ้างไหม
* **คำตอบ:** "โดยส่วนตัวไม่เคยมีปัญหาขัดแย้งรุนแรงครับ หากมีความเห็นต่างกัน เช่น Developer คิดว่าสิ่งที่พบคือกฎการทำงานปกติ (Behavior) แต่ผมพบว่าขัดแย้งกับ Requirement ผมจะ **หลีกเลี่ยงการใช้อารมณ์ตัดสิน** และนำตัวเอกสารคู่มือ Requirement หรือ Accept Criteria มาเปิดดูอ้างอิงอภิปรายร่วมกันด้วยข้อมูลที่เป็นจริงและสุภาพ เพื่อหาข้อตกลงร่วมกันกับผู้รับผิดชอบระบบอย่างเป็นวิชาชีพครับ"

### 23. เวลาเทส เทสใน Environment ไหนบ้าง
* **คำตอบ:** "โดยทั่วไปจะเทสในสภาพแวดล้อมจำลองการทำงาน ได้แก่:
  1. **SIT (System Integration Testing):** เพื่อเช็กการเชื่อมต่อระบบ Front-End, Back-End และ Database ร่วมกัน
  2. **UAT (User Acceptance Testing):** เพื่อให้ทีมธุรกิจหรือลูกค้าเข้ามาทดลองใช้จริงบนข้อมูลจำลองที่ใกล้เคียงข้อมูลจริงมากที่สุด ก่อนจะ Deploy ขึ้น Production จริงครับ"

---

## 🏦 ส่วนที่ 2: ด่านการทดสอบสด (Live Technical Assessment Simulation)

ในการทดสอบโครงการ **1KS Project (ธนาคารกรุงศรีอยุธยา - BAY)** โจทย์มักจำลองฟีเจอร์เกี่ยวกับ **"ธุรกรรมการเงินบนมือถือ" (Financial Transaction / Payment)** เช่น การโอนเงิน หรือชำระค่าบริการ

### 📝 ด่านที่ 1: การออกแบบ Test Case (โจทย์: ชำระบิลบัตรเครดิตผ่าน Mobile App)
บอสควรแบ่งโครงสร้างการตอบเป็นหมวดหมู่ให้ชัดเจน (คิดเสียงดังตลอดการเขียน):

```
1. Positive Cases (Happy Path)
   1.1 ระบุเลขบัญชีถูกต้อง ยอดเงินพอ และระบบทำรายการสำเร็จ
   1.2 การหักเงินบัญชีต้นทางและการอัปเดตยอดวงเงินบัตรเครดิตปลายทางถูกต้องทันที (Real-time update)
   1.3 ระบบบันทึกประวัติการทำรายการสำเร็จและแสดงหน้าใบเสร็จ (e-Slip) ถูกต้อง

2. Boundary Cases (ค่าขอบเขต)
   2.1 ชำระเงินจำนวนขั้นต่ำสุดที่ระบบกำหนด (เช่น 0.01 บาท หรือ 1 บาท)
   2.2 ชำระเงินจำนวนสูงสุดต่อครั้งตามที่วงเงินบัญชีหรือระบบจำกัดไว้

3. Negative Cases (เคสข้อผิดพลาด)
   3.1 ยอดเงินคงเหลือในบัญชีไม่เพียงพอสำหรับการชำระบิล
   3.2 กรอกเลขที่บิลหรือรหัสผู้รับชำระเงินไม่ถูกต้อง (Invalid billing reference)
   3.3 ป้อนจำนวนเงินเป็นศูนย์, ค่าลบ, หรือใส่ตัวอักษรพิเศษ
   3.4 บัญชีต้นทางถูกระงับการใช้งานชั่วคราว หรือบัตรเครดิตปลายทางถูกบล็อก

4. Technical & Network Failures
   4.1 อินเทอร์เน็ตหลุด/สัญญาณขาดหายระหว่างกดยืนยันชำระเงิน (เช็กการทำ Rollback ป้องกันเงินหาย)
   4.2 การรันรายการซ้ำซ้อนโดยผู้ใช้งานกดยืนยันปุ่มรัวๆ (Double submission prevention)
```

---

### 🌐 ด่านที่ 2: การออกแบบ API (RESTful API Design)
กรรมการจะดูความเข้าใจเรื่อง REST API, JSON Payload และรหัสตอบกลับ (Status Codes) ของบอสค่ะ:

* **HTTP Method:** `POST`
* **Endpoint Path:** `/api/v1/payments/bill-payment`
* **Request Headers:**
  ```http
  Content-Type: application/json
  Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9... (Token ยืนยันตัวตน)
  ```
* **Request Body (JSON Payload):**
  ```json
  {
    "source_account_no": "004-1-23456-7",
    "biller_code": "99988",
    "reference_no_1": "REF123456789",
    "reference_no_2": "0898888888",
    "amount": 2500.00,
    "currency": "THB"
  }
  ```
* **HTTP Response Codes ที่ต้องอธิบายให้ได้:**
  * `200 OK` / `201 Created`: ชำระบิลสำเร็จ พร้อมส่งเลขที่อ้างอิงธุรกรรมกลับมาใน Response
  * `400 Bad Request`: โครงสร้างข้อมูลไม่ถูกต้องหรือกรอกข้อมูลผิดฟอร์แมต
  * `401 Unauthorized`: ไม่ได้แนบโทเคนยืนยันตัวตน หรือโทเคนหมดอายุ
  * `422 Unprocessable Entity`: ข้อมูลผ่านการตรวจรูปแบบเบื้องต้นแล้ว แต่ทำรายการไม่ได้จริง (เช่น ยอดเงินในบัญชีไม่พอ หรือเลขที่บิลนี้มอยอดค้างชำระเป็น 0 ไปแล้ว)
  * `500 Internal Server Error` / `503 Service Unavailable`: เซิร์ฟเวอร์หลังบ้านธนาคารหรือระบบปลายทางขัดข้อง

---

### 💻 ด่านที่ 3: โค้ดอัตโนมัติสดด้วย TypeScript (Playwright / Appium)

ในงานของ **1KS Project** จะเน้นการทดสอบมือถือเป็นหลัก แต่โครงสร้าง Asynchronous ของ JS/TS แทบจะเหมือนกัน มอลิทำตารางสรุปคำสั่งและ Syntax สำคัญเปรียบเทียบไว้ให้บอสนะคะ:

#### ⚡ โครงสร้าง Async/Await ใน TypeScript (Playwright Web Testing)
```typescript
import { test, expect } from '@playwright/test';

test('Verify bill payment success flow', async ({ page }) => {
  // 1. นำทางไปยัง URL หน้าหลัก
  await page.goto('https://banking.krungsri.com/payment');

  // 2. ป้อนข้อมูลการเข้าสู่ระบบ
  await page.fill('#username', 'natawat_namo');
  await page.fill('#password', 'SecurePassword123');
  await page.click('#btn-login');

  // 3. รอและเลือกเมนูชำระบิล
  await page.waitForSelector('#menu-bill-payment');
  await page.click('#menu-bill-payment');

  // 4. กรอกข้อมูลและกดยืนยัน
  await page.fill('#input-biller', '99988');
  await page.fill('#input-amount', '2500.00');
  await page.click('#btn-pay-submit');

  // 5. ตรวจสอบข้อความยืนยันความสำเร็จ (Assertion)
  const successMessage = page.locator('#txt-payment-status');
  await expect(successMessage).toHaveText('Payment Successful');
});
```

#### 📱 การทดสอบ Mobile ด้วย Appium (WebdriverIO / Webdriver TypeScript Style)
ในการสัมภาษณ์ Mobile Automate Tester ผู้สัมภาษณ์จะคาดหวังให้บอสใช้ **Accessibility ID** หรือ **Resource ID** ในการระบุ Element บน Mobile Screen ค่ะ:

```typescript
describe('Mobile Bill Payment Test', () => {
  it('should process bill payment successfully', async () => {
    // 1. ค้นหา element ด้วย Accessibility ID (~ ใน Appium) ซึ่งรองรับทั้ง iOS และ Android
    const billerField = await $('~biller-input-field');
    const amountField = await $('~amount-input-field');
    const confirmBtn = await $('~confirm-payment-button');

    // 2. ดำเนินการพิมพ์ข้อความและคลิก
    await billerField.setValue('99988');
    await amountField.setValue('2500.00');
    await confirmBtn.click();

    // 3. รอและตรวจสอบองค์ประกอบข้อความแจ้งเตือนความสำเร็จ
    const statusText = await $('~status-alert-title');
    await statusText.waitForDisplayed({ timeout: 5000 });
    
    const actualStatus = await statusText.getText();
    expect(actualStatus).toBe('Payment Complete');
  });
});
```

---

## 🔍 ส่วนที่ 3: ระบบหลังบ้านและการวิเคราะห์ปัญหา (Observability & Database)

โปรเจกต์ขนาดใหญ่ของธนาคารมักระบุวิทยฐานะพิเศษเกี่ยวกับการอ่าน Log และสืบค้น SQL หลังบ้าน:

### 1. การสืบสวนข้อผิดพลาดผ่าน Kibana หรือ Dynatrace
* **Kibana (Log Viewer):** ใช้สำหรับค้นหาข้อความ Log คีย์เวิร์ดสำคัญ เช่น `error`, `failed`, หรือรหัส HTTP `500` โดยระบุขอบเขตเวลาที่พบปัญหา หรือสืบค้นตามค่า **Correlation ID (Transaction ID)** เพื่อดูการไหลผ่านของข้อมูลข้ามโมดูลย่อยหลังบ้าน
* **Dynatrace (APM - Application Performance Monitoring):** QA ใช้ดูสุขภาพของเซิร์ฟเวอร์, ค่า Response time, ค้นหาเส้นทางเรียกใช้งานหลังบ้านที่ช้า หรือดูจุดที่ Exception โยนความล้มเหลวออกมาจาก Backend API Service

### 2. ตัวอย่าง SQL Query เพื่อการทดสอบ (Database Verification)
* **คิวรีตรวจสอบการไหลของธุรกรรมล่าสุด:**
  ```sql
  SELECT t.transaction_id, t.amount, t.status, a.account_name 
  FROM transactions t
  JOIN accounts a ON t.sender_account_id = a.id
  WHERE a.account_number = '0041234567'
  ORDER BY t.created_at DESC
  LIMIT 1;
  ```

---

## 💡 เคล็ดลับการสัมภาษณ์แบบ "Think Out Loud"
1. **เมื่อได้รับโจทย์:** ห้ามก้มหน้าก้มตาเขียนโค้ดทันที ให้เริ่มด้วยการพูดสรุปโจทย์ตามความเข้าใจของบอสออกมาดังๆ เพื่อเช็กความเข้าใจที่ตรงกันกับกรรมการก่อน
2. **ระหว่างเขียนโค้ด:** หากลืม Syntax ไม่ต้องลนลาน ให้พูดบอกกรรมการว่า *"ตรงนี้ปกติถ้าจำไม่ผิดจะเป็นฟังก์ชัน X แต่หาก Syntax ผิดพลาดผมขอเขียนจำลองตรรกะ (Logic) เป็นรูปแบบนี้ก่อนนะครับ"* กรรมการจะประทับใจความโปร่งใสและตรรกะความคิดของเราค่ะ 💚
