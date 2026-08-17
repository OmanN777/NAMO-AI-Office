# QA Automation Skill Gap Analysis (Ascend Group / Super App Role)
**Date:** June 26, 2026

Based on the required Responsibilities for a "Super App QA Automation" role, here is the analysis of Oman's current profile vs. Market Requirements.

## ✅ จุดที่ตรงเป๊ะ (Strengths / Matching)
1. **Develop Automated Test Scripts:** 
   - **Requirement:** Scripting in Python/JS, using Selenium/Cypress.
   - **Oman:** มีความเชี่ยวชาญใน **Python, Playwright และ Robot Framework** ซึ่งเป็นเทคโนโลยีที่ใหม่และเร็วกว่า Selenium ถือเป็นจุดแข็งมาก
2. **Defect Tracking & Reporting:**
   - **Requirement:** Document bugs, track resolution.
   - **Oman:** มีผลงานชิ้นโบแดงคือ **"Playwright AI REPORT"** ซึ่งตอบโจทย์ข้อนี้แบบทะลุหลอด โชว์ให้เห็นว่าไม่แค่หาบั๊ก แต่สร้างระบบ Report ได้ด้วย
3. **Version Control Systems:**
   - **Requirement:** Git.
   - **Oman:** ใช้งาน Git/GitHub เป็นประจำอยู่แล้ว
4. **Innovation and Improvement:**
   - **Requirement:** Look for new tools, trends in QA automation.
   - **Oman:** มีแนวคิด **"AI-Augmented QA"** ใช้ Generative AI ช่วยทำงาน ซึ่งล้ำกว่าตลาดทั่วไป ถือเป็นอาวุธลับ!

---

## ❌ จุดที่ไม่ตรง & ต้องรีบอัปสกิล (Gaps / Areas for Improvement)
เพื่อยกระดับจาก Junior สู่ "Senior-ready" อย่างแท้จริง นี่คือสิ่งที่เราต้องทำโปรเจกต์เสริมลง Portfolio:

1. **Continuous Integration/Continuous Deployment (CI/CD) Support:**
   - **Gap:** บริษัทยักษ์ใหญ่ต้องการคนที่รันเทสต์บน Pipeline อัตโนมัติ (Jenkins, GitLab CI)
   - **Next Action:** ลองเอา Playwright ไปรันบน **GitHub Actions** หรือตั้งเซิร์ฟเวอร์ Jenkins จำลอง แล้วทำโปรเจกต์ลง GitHub
2. **Performance Testing (Load Test):**
   - **Gap:** ขาดประสบการณ์การยิง Load เพื่อหาคอขวดของระบบ (JMeter, LoadRunner)
   - **Next Action:** ควรศึกษา **k6 (ใช้เขียนด้วย JS ได้)** หรือ **JMeter** แล้วทำรายงานสรุปผล Load Test ของเว็บสักเว็บ
3. **Cross-Platform / Mobile Testing:**
   - **Gap:** ระบบระดับ "Super App" จะเป็น Mobile App 100% แต่ Playwright ของเราเน้น Web-based เป็นหลัก
   - **Next Action:** ต้องศึกษา **Appium** (ใช้ร่วมกับ Robot Framework หรือ Python ได้) เพื่อทำ Mobile App Automation
4. **Compliance and Security Testing:**
   - **Gap:** การเทสต์ความปลอดภัยและข้อมูลส่วนบุคคล
   - **Next Action:** อาจจะลองศึกษา OWASP Top 10 หรือลองใช้ Tool ยิงหาช่องโหว่พื้นฐาน (แต่ข้อนี้สำหรับ Junior อาจจะยังไม่ต้องเน้นมากที่สุด)

---
**💡 สรุปแผนปฏิบัติการ (Action Plan):**
หลังจากช่วงตะลุยยื่นใบสมัคร โปรเจกต์ถัดไปที่เราควรทำเพื่ออุดรอยรั่วคือ **"การทำ CI/CD Pipeline ให้ Playwright"** และ **"ลองเขียนสคริปต์ Appium เทสต์มือถือ"** ค่ะ!
