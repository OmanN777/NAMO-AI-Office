import os
import sys

# Set encoding for Windows console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

target_file = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace\Work_Brief\agoda_qa_masterclass.html"

with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# New Section 3 Content with crystal-clear categorization and comprehensive deep dives
new_sec_3 = """    <!-- SECTION 3: Acceptance Testing Hierarchy -->
    <section id="sec-acceptance">
      <div class="section-header">
        <span class="section-num">PART 03</span>
        <h2>Acceptance Testing Hierarchy: UAT vs. SAT vs. FAT vs. Alpha / Beta</h2>
      </div>
      
      <!-- Crystal Clear Mental Model Explanation -->
      <div class="card" onclick="toggleCardLang(this)" style="margin-bottom: 1.5rem; border-left: 4px solid var(--primary);">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="lang-en">
          <span class="card-tag tag-blue">Mental Model & Context</span>
          <h3 style="margin-top: 0.25rem;">💡 What is Acceptance Testing & Why are there 2 Different Worlds?</h3>
          <p style="font-size: 0.9rem; color: #cbd5e1;">
            <strong>Acceptance Testing</strong> is the final phase of testing where the software is validated to determine whether it is ready for <strong>business sign-off, contractual delivery, or commercial release</strong>.
          </p>
          <div style="background: rgba(255,255,255,0.02); padding: 0.85rem 1rem; border-radius: 8px; border: 1px solid var(--card-border); margin: 0.75rem 0;">
            <strong style="color: #38bdf8;">To never get confused, split them into 2 distinct industry models:</strong>
            <ul style="font-size: 0.85rem; margin: 0.4rem 0 0 1.25rem;">
              <li><strong>Track A: Enterprise Outsource & Government Contracts (FAT ➔ SAT ➔ UAT):</strong> Used when Company A (Vendor) builds custom software/hardware for Company B (Client).</li>
              <li><strong>Track B: Commercial Product & Tech Startups / Agoda (Alpha ➔ Beta ➔ Production UAT):</strong> Used for SaaS web & mobile apps released directly to global public end-users.</li>
            </ul>
          </div>
        </div>
        <div class="lang-th">
          <span class="card-tag tag-blue">แผนผังความคิดให้เข้าใจแจ่มแจ้ง</span>
          <h3 style="margin-top: 0.25rem; color: #38bdf8;">💡 Acceptance Testing คืออะไร และทำไมถึงแบ่งเป็น 2 รูปแบบใหญ่ๆ ในวงการ?</h3>
          <p style="font-size: 0.9rem; color: #cbd5e1;">
            <strong>Acceptance Testing (การทดสอบเพื่อตรวจรับงาน):</strong> คือขั้นตอนสุดท้ายของการทดสอบ เพื่อให้ผู้มีอำนาจตัดสินใจเซ็นอนุมัติรับมอบงาน (Sign-off) ว่าซอฟต์แวร์พร้อมใช้งานตามสัญญาหรือพร้อมปล่อยสู่ตลาดจริง
          </p>
          <div style="background: rgba(255,255,255,0.02); padding: 0.85rem 1rem; border-radius: 8px; border: 1px solid var(--card-border); margin: 0.75rem 0;">
            <strong style="color: #38bdf8;">วิธีจำให้เคลียร์ 100% คือการแบ่งออกเป็น 2 รูปแบบธุรกิจ (Business Tracks):</strong>
            <ul style="font-size: 0.85rem; margin: 0.4rem 0 0 1.25rem;">
              <li><strong>กลุ่มที่ 1: งานรับจ้างทำระบบ / องค์กร / รัฐวิสาหกิจ (FAT ➔ SAT ➔ UAT):</strong> บริษัทผู้รับเหมา (Vendor) พัฒนาระบบให้ลูกค้าองค์กร (Client) จึงต้องมีการตรวจรับที่โรงงานผู้ผลิต ก่อนย้ายมาตรวจที่ไซต์ลูกค้า</li>
              <li><strong>กลุ่มที่ 2: งานสร้าง Product ของตัวเอง / Tech Platform เช่น Agoda (Alpha ➔ Beta ➔ UAT):</strong> ทำเว็บ/แอปเพื่อปล่อยให้ประชาชนทั่วไปใช้งาน จึงเริ่มจากคนในบริษัทลองเล่น ก่อนปล่อย Beta สู่ผู้ใช้จริง</li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Comparison Cards Grid -->
      <div class="grid-2">
        <!-- Track A: Vendor & Contract Track -->
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-amber">Track A: Vendor & Enterprise Contracts</span>
          <div class="lang-en">
            <h3>FAT ➔ SAT ➔ UAT (Step-by-Step Delivery)</h3>
            <ul style="font-size: 0.86rem; line-height: 1.8;">
              <li>
                <strong style="color: #fbbf24;">1. FAT (Factory Acceptance Testing):</strong>
                <br>• <strong>Location:</strong> At Vendor's Office/Factory (Developer site).
                <br>• <strong>Who:</strong> Vendor Developers & QA with Client observing.
                <br>• <strong>Goal:</strong> Prove the system works in the lab before packing and shipping hardware/servers to the client site.
                <br>• <em>Example:</em> Testing airport baggage scanners or banking servers inside the manufacturer warehouse.
              </li>
              <li style="margin-top: 0.5rem;">
                <strong style="color: #38bdf8;">2. SAT (Site Acceptance Testing):</strong>
                <br>• <strong>Location:</strong> At Client's Actual Physical Site / Data Center.
                <br>• <strong>Who:</strong> Client's Engineers & Operations Team.
                <br>• <strong>Goal:</strong> Verify system works after installation on client's live environment, network, and power backup.
                <br>• <em>Example:</em> Installing the baggage scanners at Suvarnabhumi Airport and testing live radar connectivity.
              </li>
              <li style="margin-top: 0.5rem;">
                <strong style="color: #34d399;">3. UAT (User Acceptance Testing):</strong>
                <br>• <strong>Location:</strong> Staging / Client Business Department.
                <br>• <strong>Who:</strong> Real Business End-Users (Not Techies), POs, Accountants.
                <br>• <strong>Goal:</strong> Verify daily operational workflows and business contract satisfaction before final payment sign-off.
                <br>• <em>Example:</em> Airport check-in staff testing passenger bag check-in workflows.
              </li>
            </ul>
          </div>
          <div class="lang-th">
            <h3 style="color: #fbbf24;">สายงานจ้างทำระบบ: FAT ➔ SAT ➔ UAT (ส่งมอบทีละขั้น)</h3>
            <ul style="font-size: 0.86rem; line-height: 1.8;">
              <li>
                <strong style="color: #fbbf24;">1. FAT (ตรวจรับที่โรงงานผู้ผลิต - Factory):</strong>
                <br>• <strong>สถานที่:</strong> ที่บริษัทผู้รับจ้าง/โรงงานผลิต (ฝั่งผู้รับเหมา)
                <br>• <strong>ใครเป็นคนเทส:</strong> ทีม Dev/QA ของผู้รับจ้าง โดยมีตัวแทนลูกค้ามานั่งดู
                <br>• <strong>เป้าหมาย:</strong> ตรวจว่าสร้างเสร็จตามสเปกไหม ก่อนจะแพ็กของยกส่งไปให้ลูกค้า
                <br>• <em>ตัวอย่าง:</em> ตรวจระบบสายพานโหลดกระเป๋าหรือเซิร์ฟเวอร์ Core-Banking ภายในโรงงานผู้ผลิต
              </li>
              <li style="margin-top: 0.5rem;">
                <strong style="color: #38bdf8;">2. SAT (ตรวจรับที่หน้างานจริงของลูกค้า - Site):</strong>
                <br>• <strong>สถานที่:</strong> หน้างานจริง / ศูนย์ Data Center ของลูกค้า (ฝั่งลูกค้า)
                <br>• <strong>ใครเป็นคนเทส:</strong> ทีมวิศวกรไอทีและฝ่ายปฏิบัติการของลูกค้า
                <br>• <strong>เป้าหมาย:</strong> ตรวจว่าพอยกมาติดตั้งที่หน้างานจริง เชื่อมเน็ตจริง ไฟฟ้าสำรองจริง แล้วระบบทำงานได้สมบูรณ์
                <br>• <em>ตัวอย่าง:</em> ยกเครื่องสายพานมาติดตั้งจริงที่สนามบินสุวรรณภูมิ แล้วเทสเชื่อมระบบเรดาร์จริง
              </li>
              <li style="margin-top: 0.5rem;">
                <strong style="color: #34d399;">3. UAT (ตรวจรับการใช้งานจริงโดยผู้ใช้งาน - User):</strong>
                <br>• <strong>สถานที่:</strong> สภาพแวดล้อม Staging / แผนกธุรกิจ
                <br>• <strong>ใครเป็นคนเทส:</strong> พนักงานผู้ใช้งานจริง, Product Owner, ฝ่ายบัญชี
                <br>• <strong>เป้าหมาย:</strong> ตรวจว่า Flow การทำงานตอบโจทย์ธุรกิจครบไหม เพื่อเซ็นรับมอบงานงวดสุดท้าย
                <br>• <em>ตัวอย่าง:</em> เจ้าหน้าที่เคาน์เตอร์เช็กอินลองกดออกบัตรที่นั่งและแท็กกระเป๋าจริง
              </li>
            </ul>
          </div>
        </div>

        <!-- Track B: Commercial Tech & Product Track -->
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-purple">Track B: Commercial Tech & SaaS Products</span>
          <div class="lang-en">
            <h3>Alpha ➔ Beta ➔ Production (Product Release Cycle)</h3>
            <ul style="font-size: 0.86rem; line-height: 1.8;">
              <li>
                <strong style="color: #c084fc;">1. Alpha Testing (Internal Dogfooding):</strong>
                <br>• <strong>Location:</strong> Internal Development / Staging Environment.
                <br>• <strong>Who:</strong> Internal Employees, Developers, QA, Product Managers.
                <br>• <strong>Goal:</strong> Catch critical bugs and evaluate usability internally before exposing unfinished features to external customers ("Eating your own dog food").
                <br>• <em>Example:</em> Agoda employees booking test hotels using internal staging builds.
              </li>
              <li style="margin-top: 0.5rem;">
                <strong style="color: #38bdf8;">2. Beta Testing (Real External Users):</strong>
                <br>• <strong>Location:</strong> Real World / Production Environment (Controlled).
                <br>• <strong>Who:</strong> External Public Users / Limited Beta Testers (e.g. TestFlight, Early Access).
                <br>• <strong>Goal:</strong> Discover unexpected real-world edge cases across diverse mobile devices, screen sizes, weak 4G networks, and gather UX feedback.
                <br>• <em>Example:</em> Releasing Agoda App Beta to 10,000 users in Thailand before worldwide launch.
              </li>
              <li style="margin-top: 0.5rem;">
                <strong style="color: #34d399;">3. General Availability (GA) / Live Release:</strong>
                <br>• <strong>Location:</strong> 100% Global Production.
                <br>• <strong>Goal:</strong> Stable rollout monitored by live telemetry, crash analytics (Sentry), and feature flags.
              </li>
            </ul>
          </div>
          <div class="lang-th">
            <h3 style="color: #c084fc;">สายงาน Tech Product / Startups: Alpha ➔ Beta ➔ Live Release</h3>
            <ul style="font-size: 0.86rem; line-height: 1.8;">
              <li>
                <strong style="color: #c084fc;">1. Alpha Testing (คนในบริษัททดลองใช้กันเอง - Dogfooding):</strong>
                <br>• <strong>สถานที่:</strong> สภาพแวดล้อมภายในบริษัท (Staging/Dev)
                <br>• <strong>ใครเป็นคนเทส:</strong> พนักงานในองค์กร, ทีม Dev, QA, Product Managers
                <br>• <strong>เป้าหมาย:</strong> ดักเก็บบั๊กร้ายแรงและดูภาพรวมความลื่นไหลก่อนปล่อยให้คนภายนอกเห็น ("Dogfooding = กินอาหารหมาที่ตัวเองผลิต")
                <br>• <em>ตัวอย่าง:</em> พนักงาน Agoda ลองกดจองโรงแรมบนแอปเวอร์ชันภายใน
              </li>
              <li style="margin-top: 0.5rem;">
                <strong style="color: #38bdf8;">2. Beta Testing (ปล่อยให้ผู้ใช้ภายนอกกลุ่มจำกัดทดลองใช้):</strong>
                <br>• <strong>สถานที่:</strong> โลกความเป็นจริง / Production แบบจำกัดกลุ่ม (TestFlight / Early Access)
                <br>• <strong>ใครเป็นคนเทส:</strong> ลูกค้าจริงภายนอกกลุ่มทดลอง
                <br>• <strong>เป้าหมาย:</strong> ดักเจอบั๊กบนเครื่องรุ่นแปลกๆ, หน้าจอขนาดต่างๆ, สภาพเน็ตมือถือช้า และเก็บ Feedback ด้าน UX
                <br>• <em>ตัวอย่าง:</em> ปล่อยแอป Agoda Beta ให้ผู้ใช้ 10,000 คนในไทยลองเล่นก่อนเปิดตัวทั่วโลก
              </li>
              <li style="margin-top: 0.5rem;">
                <strong style="color: #34d399;">3. GA (General Availability - ปล่อยใช้งานจริง 100%):</strong>
                <br>• <strong>สถานที่:</strong> Production ทั่วโลก พร้อมระบบมอนิเตอร์ Crash และ Error Logs แบบ Real-time
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- Master Summary Table -->
      <div class="card" onclick="toggleCardLang(this)" style="margin-top: 1.25rem;">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="lang-en">
          <span class="card-tag tag-emerald">Master Reference Matrix</span>
          <h3>Quick-Reference Comparison Matrix</h3>
          <div class="table-wrapper" style="margin-top: 0.5rem;">
            <table>
              <thead>
                <tr>
                  <th>Testing Type</th>
                  <th>Full Form</th>
                  <th>Primary Tester</th>
                  <th>Test Environment</th>
                  <th>Core Purpose & Deciding Metric</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong style="color: #fbbf24;">FAT</strong></td>
                  <td>Factory Acceptance Testing</td>
                  <td>Vendor Developers & QA (Client witnessing)</td>
                  <td>Vendor's Development Site</td>
                  <td>Validates build meets specs <strong>before packaging & shipping</strong>.</td>
                </tr>
                <tr>
                  <td><strong style="color: #38bdf8;">SAT</strong></td>
                  <td>Site Acceptance Testing</td>
                  <td>Client's IT & Operations Team</td>
                  <td>Client's Real Live Infrastructure</td>
                  <td>Validates integration with <strong>client's on-site hardware, power & network</strong>.</td>
                </tr>
                <tr>
                  <td><strong style="color: #34d399;">UAT</strong></td>
                  <td>User Acceptance Testing</td>
                  <td>Business End-Users & Product Owners</td>
                  <td>Staging (Sanitized Real Data)</td>
                  <td>Validates <strong>business processes & contract compliance</strong> for final sign-off.</td>
                </tr>
                <tr>
                  <td><strong style="color: #c084fc;">Alpha</strong></td>
                  <td>Alpha Acceptance Testing</td>
                  <td>Internal Employees & Staff</td>
                  <td>Internal Lab Environment</td>
                  <td>Catches critical bugs <strong>before external exposure</strong>.</td>
                </tr>
                <tr>
                  <td><strong style="color: #fb7185;">Beta</strong></td>
                  <td>Beta Acceptance Testing</td>
                  <td>Real External Public Users</td>
                  <td>Real World / TestFlight</td>
                  <td>Gathers <strong>usability feedback & edge device compatibility</strong> in the wild.</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="punchline">
            <strong>🗣️ 10-Second Interview Answer:</strong><br>
            <em>"In enterprise contracts, <strong>FAT</strong> is tested at the vendor factory, <strong>SAT</strong> is tested on the client's live site, and <strong>UAT</strong> is tested by business users for contract sign-off. In commercial products like Agoda, <strong>Alpha</strong> is tested internally by employees, and <strong>Beta</strong> is released to real external users for feedback."</em>
          </div>
        </div>
        <div class="lang-th">
          <span class="card-tag tag-emerald">ตารางสรุปเปรียบเทียบมาตรฐานแม่นยำ 100%</span>
          <h3 style="color: #34d399;">ตารางสรุปความแตกต่างแบบเข้าใจง่าย</h3>
          <div class="table-wrapper" style="margin-top: 0.5rem;">
            <table>
              <thead>
                <tr>
                  <th>ประเภท</th>
                  <th>ชื่อเต็ม</th>
                  <th>ใครเป็นคนเทสหลัก?</th>
                  <th>เทสที่สภาพแวดล้อมไหน?</th>
                  <th>หัวใจสำคัญ & การตัดสินผล</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong style="color: #fbbf24;">FAT</strong></td>
                  <td>Factory Acceptance Testing</td>
                  <td>ทีมผู้รับเหมา (ลูกค้ามาร่วมดู)</td>
                  <td>โรงงาน / ออฟฟิศของผู้รับเหมา</td>
                  <td>ตรวจความพร้อมของระบบ <strong>ก่อนแพ็กของส่งมอบไปหาลูกค้า</strong></td>
                </tr>
                <tr>
                  <td><strong style="color: #38bdf8;">SAT</strong></td>
                  <td>Site Acceptance Testing</td>
                  <td>ทีมวิศวกรไอทีของลูกค้า</td>
                  <td>สถานที่จริง / เซิร์ฟเวอร์จริงของลูกค้า</td>
                  <td>ตรวจการเชื่อมต่อกับ <strong>ระบบเครือข่ายและฮาร์ดแวร์จริงหน้างาน</strong></td>
                </tr>
                <tr>
                  <td><strong style="color: #34d399;">UAT</strong></td>
                  <td>User Acceptance Testing</td>
                  <td>ผู้ใช้งานจริง / Product Owner</td>
                  <td>Staging (ข้อมูลจำลองเหมือนจริง)</td>
                  <td>ตรวจรับงานตามกระบวนการธุรกิจ <strong>เพื่อเซ็นรับมอบงานตามสัญญา</strong></td>
                </tr>
                <tr>
                  <td><strong style="color: #c084fc;">Alpha</strong></td>
                  <td>Alpha Testing</td>
                  <td>พนักงานภายในองค์กร</td>
                  <td>ระบบทดสอบภายใน (Internal)</td>
                  <td>ดักเก็บบั๊กร้ายแรง <strong>ก่อนปล่อยให้คนภายนอกเห็น</strong></td>
                </tr>
                <tr>
                  <td><strong style="color: #fb7185;">Beta</strong></td>
                  <td>Beta Testing</td>
                  <td>ผู้ใช้งานจริงภายนอกกลุ่มทดลอง</td>
                  <td>สภาพแวดล้อมจริง (TestFlight)</td>
                  <td>เก็บ <strong>Feedback ประสบการณ์ใช้งาน & ดักบั๊กบนเครื่องรุ่นแปลกๆ</strong></td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="punchline">
            <strong>🗣️ สูตรประโยคทองสำหรับตอบสัมภาษณ์:</strong><br>
            <em>"ในงานรับเหมาทำระบบ <strong>FAT</strong> จะตรวจที่โรงงานผู้ผลิต, <strong>SAT</strong> จะตรวจที่หน้างานจริงของลูกค้า, และ <strong>UAT</strong> จะตรวจโดยผู้ใช้งานฝ่ายธุรกิจเพื่อเซ็นรับมอบงานค่ะ ส่วนในสายพัฒนา Product ทั่วไปอย่าง Agoda <strong>Alpha</strong> จะให้คนในบริษัทลองเล่นกันเอง และ <strong>Beta</strong> จะปล่อยให้ผู้ใช้จริงภายนอกทดลองใช้งานเพื่อเก็บ Feedback ค่ะ"</em>
          </div>
        </div>
      </div>
    </section>"""

import re
# Replace the old section 3
pattern = r'<!-- SECTION 3: Acceptance Testing Hierarchy -->.*?<!-- SECTION 4: Entry & Exit Criteria -->'
updated_content = re.sub(pattern, new_sec_3 + "\n\n    <!-- SECTION 4: Entry & Exit Criteria -->", content, flags=re.DOTALL)

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(updated_content)

print(f"Successfully rewritten Section 3 with crystal-clear explanations in {target_file}")
