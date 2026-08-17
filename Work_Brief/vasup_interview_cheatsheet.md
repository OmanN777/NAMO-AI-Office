# 🎯 VAS.UP Co., Ltd. — Comprehensive Interview & Live Test Cheat Sheet

**Company:** บริษัท วาส.อัพ จำกัด (VAS.UP Co., Ltd.) — อาคาร Siamscape  
**Role Target:** Automate Software Tester / Test Engineer  
**Candidate:** นายนาถวัฒน์ เทพหัสดิน ณ อยุธยา (นะโม)  
**Interview Date & Time:** วันศุกร์ที่ 14 สิงหาคม 2026 เวลา 14:00 – 15:00 น.  
**Meeting Platform:** [Microsoft Teams Meeting Link](https://teams.microsoft.com/meet/430320859937088?p=WMrOJ1V5sqGF6ZFNtI)  
*(Meeting ID: `430 320 859 937 088` | Passcode: `Zi2wd3F2`)*  

---

## 📌 1. Self-Introduction (แนะนำตัว 1 นาที)

> "สวัสดีครับ ผมชื่อ นาถวัฒน์ เทพหัสดิน ณ อยุธยา (นะโม) จบจากคณะ ICT มหาวิทยาลัยมหิดล มีประสบการณ์ฝึกงาน QA Tester รวม 8 เดือนครับ
>
> ในช่วงฝึกงาน ผมได้รับหน้าที่ดูแลการทดสอบระบบ **iNT Connect** (แพลตฟอร์มมหาวิทยาลัยมหิดล) ออกแบบและบริหาร 260+ Test Cases ครอบคลุมทั้ง Functional, Web UI, API Testing และ Role-based Access Control
>
> จุดเด่นของผมคือความเชี่ยวชาญด้าน Automation Testing โดยใช้ **Playwright (TypeScript)** และ **Robot Framework (Python)** รวมถึง **Postman** สำหรับ API รวมทั้งการต่อ Automated Test เข้ากับ **GitHub Actions CI/CD** ครับ พร้อมเริ่มงานที่ Siamscape ได้ทันทีครับ"

---

## 🏆 2. รวม 6 คำถามหมัดเด็ดระดับท็อป (คัดจากสัมภาษณ์ CT Software & Agoda)

### Q1: ถ้าเจอ Flaky Test (เทสที่บางทีก็ผ่าน บางทีก็พัง ทั้งที่โค้ดเหมือนเดิม) คุณมีวิธีแก้อย่างไร?
* **คำตอบ:** "สาเหตุหลักของ Flaky Test มาจาก Timing Issue และการใช้ `sleep()` ครับ วิธีแก้คือ **ลบ `sleep()` ทิ้งทั้งหมด** แล้วเปลี่ยนมาใช้ **Auto-waiting / Explicit Wait** ของ Playwright พร้อมทั้งทำ **Isolated Test Data** (สร้างและลบข้อมูลเทสเฉพาะรอบ) เพื่อไม่ให้เทสแต่ละตัวแย่งข้อมูลกันครับ"

### Q2: ความแตกต่างระหว่าง Smoke Test, Sanity Test และ Regression Test?
* **Smoke Test:** เทสคร่าวๆ เช็กว่า Build ใหม่เปิดติด ไม่พังคามือ (ถ้าพัง Reject คืน Dev ทันที)
* **Sanity Test:** เทสเจาะลึกเฉพาะฟังก์ชันที่เพิ่งแก้บั๊กเสร็จสดๆ
* **Regression Test:** รันเทสระบบทั้งหมดรอบใหญ่ (เป็นจุดที่ **Automation Test** มีบทบาทและมูลค่าสูงสุด) เพื่อยืนยันว่าโค้ดใหม่ไม่ไปทำลายฟังก์ชันเดิม

### Q3: Page Object Model (POM) คืออะไร และทำไมถึงสำคัญ?
* **คำตอบ:** "POM คือ Design Pattern ที่แยก **โครงสร้างหน้าเว็บ (Locators/Elements)** ออกจาก **Logic ของการรันเทส (Test Scripts)** ช่วยให้เมื่อ UI หน้าเว็บเปลี่ยน เราแก้แค่ที่ไฟล์ Page Class จุดเดียว Test Scripts ทั้งหมดก็รันผ่านต่อได้ทันที โดยไม่ต้องไล่แก้ทุกไฟล์ครับ"

### Q4: ถ้าเวลาเทสน้อย หรือ Requirement เปลี่ยนแปลงกะทันหันก่อน Release จะทำอย่างไร?
* **คำตอบ:** "ผมจะทำ **Risk-based Testing (RBT)** โดยจัดลำดับความสำคัญ (Priority) เลือกเทส Core Flow ที่เป็น Critical Path ก่อน และใช้ Automation Test Suite รัน Regression Testing ช่วยประหยัดเวลาครับ"

### Q5: ถ้า Dev บอกว่า "ไม่ใช่วันบั๊ก (It's a feature)" หรือสื่อสารไม่ตรงกัน คุณมีวิธีจัดการอย่างไร?
* **คำตอบ:** "ผมจะยึดหลักการสื่อสารที่ **เป็นกลาง เป็นจริง และมีหลักฐานประจักษ์ (Neutral & Factual)** โดยเตรียม Steps to Reproduce, DevTools Network/Console Log และชวน Dev กับ SA/PM มายืนยัน Requirement ร่วมกันเพื่อยึดประสบการณ์ของผู้ใช้งานเป็นหลักครับ"

### Q6: ในการทำ API Testing ผ่าน Postman คุณตรวจสอบอะไรบ้าง (5 ชั้น)?
1. **Status Code:** 200 OK, 201 Created, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 500 Server Error
2. **HTTP Methods:** GET (ดึง), POST (สร้าง), PUT/PATCH (อัปเดต), DELETE (ลบ)
3. **Response Time:** เช็กว่าตอบกลับไวในเกณฑ์ เช่น `<500ms`
4. **JSON Schema:** โครงสร้าง Data Type ถูกต้อง (`id` เป็น int, `email` เป็น string)
5. **Negative Handling:** ลองส่ง Payload ผิดประเภทเพื่อดูว่า Backend ตอบ Error สวยงาม ไม่หลุด Stack trace

---

## 📝 3. เทคนิคคิด Test Case ให้ได้คะแนนเต็ม (5-Block Framework)

ท่อง 5 บล็อกนี้ไว้ตอบได้ทุกโจทย์:
1. **Positive / Happy Path:** กรอกข้อมูลถูกต้องครบถ้วน ➔ ทำงานสำเร็จ
2. **Negative Path:** กรอกรหัสผิด, เว้นว่างช่องบังคับ, ฟอร์แมตผิด ➔ แสดง Error Message
3. **Boundary Value (BVA & Edge Cases):** ค่าต่ำสุด-สูงสุด (Min/Max), กดปุ่ม Submit ซ้ำเร็วๆ (Debounce)
4. **Non-Functional & Security:** สิทธิ์ผู้ใช้งาน (RBAC), SQL Injection
5. **Offline & Stress Test:** เน็ตหลุด (Rollback Transaction), คนเข้าใช้งานพร้อมกัน 1,000 คน

---

## 💻 4. เก็งโค้ดดิ้งสด (Live Coding Snippets)

### Playwright (TypeScript):
```typescript
import { test, expect } from '@playwright/test';

test('Verify User Can Login Successfully', async ({ page }) => {
  await page.goto('https://example.com/login');
  await page.locator('#username').fill('testuser@example.com');
  await page.locator('#password').fill('P@ssword123');
  await page.locator('button[type="submit"]').click();

  await expect(page).toHaveURL(/.*dashboard/);
  await expect(page.locator('#welcome')).toBeVisible();
});
```

### Python 4 อัลกอริทึมยอดฮิต:
1. **Palindrome:** `def is_palindrome(s): return s == s[::-1]`
2. **Find Duplicates:** `def find_duplicates(nums): return list(set([x for x in nums if nums.count(x) > 1]))`
3. **FizzBuzz:** `% 15 == 0 -> FizzBuzz, % 3 == 0 -> Fizz, % 5 == 0 -> Buzz`
4. **Count Chars:** `counts = {}; for c in text: counts[c] = counts.get(c, 0) + 1`
