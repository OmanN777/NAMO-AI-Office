# Natawat Resume - Harvard LaTeX Source Code

บอสสามารถคัดลอกโค้ด LaTeX ด้านล่างนี้ไปวางในระบบ Overleaf เพื่อกด Compile ออกมาเป็น PDF สไตล์ Harvard ที่บีบกระชับช่องว่างรอบหัวข้อหลัก หัวเรื่อง และโปรเจกต์ลงอีกเล็กน้อย ทำให้ส่วนของ Methodologies ที่ล้นไปอยู่หน้า 2 หดกลับขึ้นมาวางเรียงอยู่บนหน้า 1 หน้าเดียวถ้วนได้อย่างสมบูรณ์แบบค่ะ:

```latex
\documentclass[11pt,a4paper]{article}
\usepackage{graphicx} % Required for inserting images
\setlength{\parindent}{0pt}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage[utf8]{inputenc} 
\usepackage[T1]{fontenc}
\usepackage[english]{babel}
\usepackage[left=1.25cm,top=0.8cm,right=1.25cm,bottom=0.8cm,a4paper]{geometry}

% ป้องกันไม่ให้ LaTeX ยืดช่องไฟแนวตั้งเองโดยอัตโนมัติ
\raggedbottom

\begin{document}
\begin{center}
    \vspace{-6pt}
    \textbf{\huge Natawat Tephassadin na Ayutaya (Namo)}\\ 
    \vspace{-10pt}
    \hrulefill
\end{center}

\begin{center}
    \vspace{-10pt}
    \small namo.nanon5@gmail.com \textbullet \ (+66) 63-435-8908 \textbullet \ LINE: mosung123 \textbullet \ github.com/OmanN777 \textbullet \ linkedin.com/in/natawat-t
\end{center}

\vspace{6pt}

\centerline{\textbf{\Large Education}}

\vspace{2pt}
\textbf{Mahidol University} \hfill Nakhon Pathom, Thailand\\
Bachelor of Science (B.Sc.) in Digital Science and Technology \hfill Graduated: 2026\\
Relevant Coursework: Software Quality Assurance and Testing, Software Engineering, Database Systems (GPAX: 2.84 / 4.00)

\vspace{6pt}

\centerline{\textbf{\Large Experience}}
\vspace{2pt}
\textbf{Course Square Co., Ltd.} \hfill Bangkok, Thailand\\
\textbf{QA Tester (Internship)} \hfill May 2025 -- Dec 2025
\begin{itemize}[noitemsep, topsep=1pt, partopsep=0pt, parsep=0pt]
    \item Developed E2E UI automation test suites from scratch using Playwright and JavaScript.
    \item Implemented Page Object Model (POM) design patterns to ensure script reusability and scalability.
    \item Built and monitored the automated testing suite (Admin-iNT-AutoTest) for the internal admin platform.
    \item Conducted regression testing and logged defects to ensure system stability prior to major releases.
\end{itemize}

\vspace{3pt}

\textbf{SellSuki Co., Ltd.} \hfill Bangkok, Thailand\\
\textbf{QA Tester (Internship)} \hfill June 2024 -- July 2024
\begin{itemize}[noitemsep, topsep=1pt, partopsep=0pt, parsep=0pt]
    \item Developed automated API test scripts utilizing Robot Framework and Python.
    \item Conducted API testing and database validation against MongoDB using custom libraries.
    \item Executed functional test cases, logged detailed bug reports, and collaborated on defect resolutions.
\end{itemize}

\vspace{6pt}

\centerline{\textbf{\Large Projects}}
\vspace{2pt}

\textbf{Playwright eCommerce Test Automation} \hfill Personal Project\\
\textit{Test Automation Developer} \hfill github.com/OmanN777/playwright-pom-ecommerce
\begin{itemize}[noitemsep, topsep=1pt, partopsep=0pt, parsep=0pt]
    \item Developed E2E UI test automation scenarios for an eCommerce platform using Playwright, Python, and Pytest.
    \item Implemented Page Object Model (POM), data-driven testing (DDT) with external JSON files, and GitHub Actions CI/CD.
\end{itemize}

\vspace{3pt}

\textbf{Playwright Gemini Visual QA Agent} \hfill Personal Project\\
\textit{Test Automation Developer} \hfill github.com/OmanN777/visual-qa-agent-gemini
\begin{itemize}[noitemsep, topsep=1pt, partopsep=0pt, parsep=0pt]
    \item Built a prototype test script combining Playwright and Gemini API vision models for visual grounding tests.
    \item Mapped element coordinates from vision responses to viewport pixels and integrated automated URL checks.
\end{itemize}

\vspace{3pt}

\textbf{Playwright AI-Reporter} \hfill Personal Project\\
\textit{Test Automation Developer} \hfill github.com/OmanN777/playwright-ai-reporter
\begin{itemize}[noitemsep, topsep=1pt, partopsep=0pt, parsep=0pt]
    \item Built a Playwright E2E testing framework integrated with GitHub Actions CI/CD pipeline for automated test execution.
    \item Integrated the Gemini AI API to automatically analyze test failures, identify root causes, and output markdown reports.
\end{itemize}

\vspace{3pt}

\textbf{Playwright Automation Study} \hfill Training Project\\
\textit{Test Automation Learner} \hfill github.com/OmanN777/playwright-udemy-course
\begin{itemize}[noitemsep, topsep=1pt, partopsep=0pt, parsep=0pt]
    \item Set up a test automation study project for a local shopping web application using Playwright and JavaScript.
    \item Implemented custom page assertions, API authentication calls, and global setup hooks to manage test states.
\end{itemize}

\vspace{3pt}

\textbf{Software Quality Assurance Suite} \hfill Academic Project\\
\textit{QA Test Developer} \hfill github.com/OmanN777/Testing-Website-Project
\begin{itemize}[noitemsep, topsep=1pt, partopsep=0pt, parsep=0pt]
    \item Developed Robot Framework E2E UI automation and JavaScript-based k6 load/stress testing scripts to validate web application quality.
    \item Designed comprehensive manual test cases, executed validation suites, and documented test execution logs.
\end{itemize}

\vspace{6pt}

\centerline{\textbf{\Large Technical Skills \& Methodologies}}
\vspace{2pt}
\textbf{Technical Skills:} Playwright, Robot Framework, k6, JUnit, Postman, Swagger, Git, JavaScript, TypeScript, Python, Java, SQL, Node.js, MongoDB, GitHub Actions\\
\textbf{Methodologies:} E2E Testing, Performance Testing, API Testing, Unit Testing, Regression Testing, Page Object Model (POM), Database Validation

\end{document}
```
