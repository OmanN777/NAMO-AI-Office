# นาถวัฒน์ Resume - Harvard LaTeX Source Code (ภาษาไทย)

บอสสามารถคัดลอกโค้ด LaTeX ด้านล่างนี้ไปวางในระบบ Overleaf เพื่อกด Compile ออกมาเป็น PDF สไตล์ Harvard ในเวอร์ชันภาษาไทยได้ทันทีเลยค่ะ:

> ⚠️ **คำแนะนำทางเทคนิคสำหรับการแสดงผลภาษาไทยใน Overleaf:**
> เนื่องจากตัวแปลเอกสาร (Compiler) เริ่มต้นของ Overleaf (pdfLaTeX) จะไม่รองรับฟอนต์ภาษาไทยโดยตรง หากบอสวางโค้ดภาษาไทยด้านล่างนี้แล้ว **บอสต้องตั้งค่าเปลี่ยน Compiler ใน Overleaf ให้เป็น XeLaTeX** นะคะ โดยกดที่ปุ่ม **Menu (ซ้ายบน) -> ตรงหัวข้อ Compiler ให้เลือกเป็น XeLaTeX** ค่ะ จะช่วยให้แสดงผลภาษาไทยได้ถูกต้องและสมบูรณ์ค่ะบอส!

```latex
\documentclass[11pt]{article}
\usepackage{graphicx}
\setlength{\parindent}{0pt}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage[left=1.06cm,top=1.7cm,right=1.06cm,bottom=0.49cm]{geometry}

% สำหรับเปิดใช้งานฟอนต์ภาษาไทยใน XeLaTeX
\usepackage{fontspec}
\setmainfont{TH Sarabun PSK} % หรือฟอนต์ภาษาไทยมาตรฐานตัวอื่นในระบบ

\begin{document}
\begin{center}
    \textbf{\huge นาถวัฒน์ เทพหัสดิน ณ อยุธยา (นะโม)}\\ 
    \hrulefill
\end{center}

\begin{center}
    \small namo.nanon5@gmail.com \textbullet \ (+66) 63-435-8908 \textbullet \ LINE: mosung123 \textbullet \ github.com/OmanN777 \textbullet \ linkedin.com/in/natawat-t
\end{center}

\vspace{0.5pt}

\begin{center}
    \textbf{\large การศึกษา (Education)}
\end{center}
\textbf{มหาวิทยาลัยมหิดล} \hfill นครปฐม, ประเทศไทย

วิทยาศาสตรบัณฑิต สาขาวิทยาศาสตร์และเทคโนโลยีดิจิทัล (Digital Science and Technology) \hfill สำเร็จการศึกษา: 2569

GPAX: 2.84 / 4.00

รายวิชาที่เกี่ยวข้อง: Software Quality Assurance and Testing, Software Engineering, Database Systems

\vspace{10pt}

\begin{center}
    \textbf{\large ประสบการณ์ทำงาน (Work Experience)}
\end{center}
\textbf{บริษัท คอร์ส สแควร์ จำกัด} \hfill กรุงเทพมหานคร, ประเทศไทย

\textbf{QA Tester (ฝึกงาน)} \hfill พฤษภาคม 2568 -- ธันวาคม 2568
\begin{itemize}[noitemsep, topsep=0pt, partopsep=0pt, parsep=0pt]
    \item มีส่วนร่วมในการพัฒนาและดูแลรักษาชุดทดสอบระบบอัตโนมัติแบบ E2E (Admin-iNT-AutoTest) สำหรับแพลตฟอร์มผู้ดูแลระบบภายใน
    \item พัฒนาสคริปต์การทดสอบ E2E อัตโนมัติด้วย Playwright และ JavaScript โดยประยุกต์ใช้ Page Object Model (POM) เพื่อการนำโค้ดกลับมาใช้ซ้ำ
    \item รับผิดชอบการทดสอบ Regression Testing ค้นหาและรายงานข้อบกพร่อง (Defects) เพื่อรักษาความเสถียรของระบบก่อนการปล่อยผลิตภัณฑ์จริง
\end{itemize}

\vspace{12pt}

\textbf{บริษัท เซลล์ซูกิ จำกัด} \hfill กรุงเทพมหานคร, ประเทศไทย

\textbf{QA Tester (ฝึกงาน)} \hfill มิถุนายน 2567 -- กรกฎาคม 2567
\begin{itemize}[noitemsep, topsep=0pt, partopsep=0pt, parsep=0pt]
    \item พัฒนาสคริปต์ทดสอบ API อัตโนมัติด้วย Robot Framework และ Python เพื่อสนับสนุนการประกันคุณภาพระบบหลัก
    \item ดำเนินการทดสอบ API และตรวจสอบความถูกต้องของข้อมูล (Database Validation) บนฐานข้อมูล MongoDB ด้วยการเขียนโมดูลทดสอบเฉพาะทาง
    \item รับผิดชอบการรันเทสต์ตามกรณีทดสอบ (Test Cases) ทำรายงานบันทึก Bug และประสานงานกับทีมพัฒนาโดยตรงเพื่อปรับปรุงคุณภาพซอฟต์แวร์
\end{itemize}

\vspace{10pt}

\begin{center}
    \textbf{\large ผลงานโครงการ (Projects)}
\end{center}

\textbf{Playwright AI-Reporter} \hfill โครงการส่วนตัว (Personal Project)

\textbf{Test Automation Developer} \hfill github.com/OmanN777/playwright-ai-reporter
\begin{itemize}[noitemsep, topsep=0pt, partopsep=0pt, parsep=0pt]
    \item ออกแบบระบบทดสอบ E2E อัตโนมัติด้วย Playwright ร่วมกับท่อส่ง CI/CD บน GitHub Actions เพื่อการรันเทสต์อัตโนมัติ
    \item เชื่อมโยง Gemini AI API ในการวิเคราะห์ผลการทดสอบที่ล้มเหลว ค้นหาต้นตอปัญหา (Root Cause) และส่งรายงานความผิดพลาดเพื่อความรวดเร็วในการแก้ไข
\end{itemize}

\vspace{12pt}

\textbf{JPacman} \hfill โครงการวิชาการ (Academic Project)

\textbf{Unit Test Developer} \hfill มหาวิทยาลัยมหิดล
\begin{itemize}[noitemsep, topsep=0pt, partopsep=0pt, parsep=0pt]
    \item เขียนชุดการทดสอบระดับ Unit Test ด้วย JUnit (Java) เพื่อตรวจสอบตรรกะการเคลื่อนที่ของตัวละครและสถานะผลลัพธ์ของเกม
    \item ประยุกต์ใช้การวิเคราะห์พฤติกรรมผ่านสคริปต์ Python เพื่อตรวจสอบความถูกต้องของสถานะผลลัพธ์ของเกม
\end{itemize}

\vspace{10pt}

\begin{center}
    \textbf{\large ทักษะและใบประกาศนียบัตร (Skills \& Certifications)}
\end{center}

\textbf{ทักษะทางเทคนิค:} Playwright, Robot Framework, JUnit, Postman, Swagger, Git, JavaScript, TypeScript, Python, Java, SQL, Node.js, MongoDB, GitHub Actions

\textbf{ระเบียบวิธีทดสอบ:} E2E Testing, API Testing, Unit Testing, Regression Testing, Page Object Model (POM), Database Validation

\textbf{ใบประกาศนียบัตร:} หลักสูตรการทดสอบเว็บแอปพลิเคชันอัตโนมัติด้วย Playwright (Udemy), ใบรับรองการผ่านรายวิชา Software Quality Assurance and Testing (มหาวิทยาลัยมหิดล)

\end{document}
```
