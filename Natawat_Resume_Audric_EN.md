# Natawat Resume - Audric/Lato LaTeX Source Code (ภาษาอังกฤษ)

บอสสามารถคัดลอกโค้ด LaTeX ด้านล่างนี้ไปวางในระบบ Overleaf เพื่อกด Compile ออกมาเป็น PDF สไตล์ Audric/Lato (ฟอนต์สไตล์ Sans-Serif ที่ดูโมเดิร์นและทันสมัย) ได้ทันทีเลยค่ะ:

```latex
\documentclass[letterpaper,11pt]{article}

\usepackage{fontawesome5}
\usepackage{latexsym}
\usepackage[empty]{fullpage}
\usepackage{titlesec}
\usepackage{marvosym}
\usepackage[usenames,dvipsnames]{color}
\usepackage{verbatim}
\usepackage{enumitem}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\usepackage[english]{babel}
\usepackage{tabularx}
\usepackage{graphicx}
\usepackage{mwe}
\usepackage{wrapfig}

\input{glyphtounicode}

% Custom font - Lato (Sans-Serif)
\usepackage[default]{lato}

\pagestyle{fancy}
\fancyhf{} % clear all header and footer fields
\fancyfoot{}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Adjust margins
\addtolength{\oddsidemargin}{-0.6in}
\addtolength{\evensidemargin}{-0.6in}
\addtolength{\textwidth}{1.1in}
\addtolength{\topmargin}{-.65in}
\addtolength{\textheight}{1.35in}
\setlength{\footskip}{4.08pt}

\urlstyle{same}

\raggedbottom
\raggedright
\setlength{\tabcolsep}{0in}

% Sections formatting
\titleformat{\section}{
  \vspace{-8pt}\bfseries\raggedright\large
}{}{0em}{}[\color{black}\titlerule\vspace{-4pt}]

% Ensure that generate pdf is machine readable/ATS parsable
\pdfgentounicode=1

% Custom commands
\newcommand{\resumeItem}[1]{
  \item\small{
    {#1 \vspace{-2pt}}
  }
}

\newcommand{\resumeSubheading}[4]{
  \vspace{-2pt}\item
    \begin{tabular*}{0.97\textwidth}[t]{l@{\extracolsep{\fill}}r}
      \textbf{#1} & #2 \\
      \textit{\small#3} & \textit{\small #4} \\
    \end{tabular*}\vspace{-3pt}
}

\newcommand{\resumeSubSubheading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \textit{\small#1} & \textit{\small #2} \\
    \end{tabular*}\vspace{-3pt}
}

\newcommand{\resumeProjectHeading}[2]{
    \item
    \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
      \small#1 & #2 \\
    \end{tabular*}\vspace{-3pt}
}

\newcommand{\resumeSubItem}[1]{\resumeItem{#1}\vspace{-4pt}}

\renewcommand\labelitemii{$\vcenter{\hbox{\tiny$\bullet$}}$}

\newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=0.15in, label={}, itemsep=3.5pt, parsep=0pt, topsep=2pt]}
\newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
\newcommand{\resumeItemListStart}{\begin{itemize}[itemsep=3pt, parsep=0pt, topsep=2pt]}
\newcommand{\resumeItemListEnd}{\end{itemize}\vspace{3pt}}

%-------------------------------------------
%%%%%%  RESUME STARTS HERE  %%%%%

\begin{document}

%----------HEADING----------
\begin{minipage}[t]{0.85\textwidth}
    \vspace{-4pt}
    \textbf{\Huge Natawat Tephassadin na Ayutaya} \par \vspace{10pt}
    \small 
    \faPhone \ (+66) 63-435-8908 \quad 
    \faEnvelope \ \href{mailto:namo.nanon5@gmail.com}{\underline{namo.nanon5@gmail.com}} \quad 
    \faComment \ LINE: mosung123 \\
    \faGithub \ \href{https://github.com/OmanN777}{\underline{github.com/OmanN777}} \quad 
    \faLinkedin \ \href{https://linkedin.com/in/natawat-t}{\underline{linkedin.com/in/natawat-t}}
\end{minipage}%
\begin{minipage}[t]{0.14\textwidth}
    \vspace{-10pt}
    \flushright
    \vbox to 80pt{
        % TO REMOVE PHOTO: Comment out the \includegraphics line below. The layout will not shift.
        \includegraphics[width=1.0\textwidth, height=1.3\textwidth, keepaspectratio]{profile.png}
        \vss
    }

\end{minipage}
\vspace{18pt}



%-----------EDUCATION-----------
\section{Education}
  \resumeSubHeadingListStart
    \resumeSubheading
      {Mahidol University}{Nakhon Pathom, Thailand}
      {Bachelor of Science (B.Sc.) in Digital Science and Technology}{2022 -- 2026}
      \resumeItemListStart
        \resumeItem{\textbf{GPAX:} 2.84 / 4.00}
        \resumeItem{\textbf{Relevant Coursework:} Software Quality Assurance and Testing, Software Engineering, Database Systems}
      \resumeItemListEnd
  \resumeSubHeadingListEnd

%-----------EXPERIENCE-----------
\section{Work Experience}
  \resumeSubHeadingListStart

    \resumeSubheading
      {Course Square Co., Ltd.}{Bangkok, Thailand}
      {QA Tester (Internship)}{May 2025 -- Dec 2025}
      \resumeItemListStart
        \resumeItem{Developed and maintained E2E test automation scripts from scratch using Playwright and JavaScript.}
        \resumeItem{Implemented the Page Object Model (POM) design pattern to ensure test script reusability and scalability.}
        \resumeItem{Built and monitored the automated testing suite (Admin-iNT-AutoTest) for the internal admin platform.}
        \resumeItem{Conducted regression testing and identified software defects to ensure system stability prior to releases.}
      \resumeItemListEnd

    \resumeSubheading
      {SellSuki Co., Ltd.}{Bangkok, Thailand}
      {QA Tester (Internship)}{June 2024 -- July 2024}
      \resumeItemListStart
        \resumeItem{Developed automated API test scripts utilizing Robot Framework and Python to support core testing.}
        \resumeItem{Conducted API testing and database validation against a MongoDB database utilizing custom libraries.}
        \resumeItem{Executed test cases, logged detailed bug reports, and collaborated with developers to resolve software defects.}
      \resumeItemListEnd

  \resumeSubHeadingListEnd

%-----------PROJECTS-----------
\section{Projects}
  \resumeSubHeadingListStart
    \resumeProjectHeading
      {\textbf{Playwright eCommerce Test Automation} $|$ \emph{Personal Project}}{github.com/OmanN777/playwright-pom-ecommerce}
      \resumeItemListStart
        \resumeItem{Developed E2E UI test automation scenarios for an eCommerce platform using Playwright, Python, and Pytest.}
        \resumeItem{Implemented Page Object Model (POM), data-driven testing (DDT) with external JSON files, and GitHub Actions CI/CD.}
      \resumeItemListEnd

    \resumeProjectHeading
      {\textbf{Playwright Gemini Visual QA Agent} $|$ \emph{Personal Project}}{github.com/OmanN777/visual-qa-agent-gemini}
      \resumeItemListStart
        \resumeItem{Built a prototype test script combining Playwright and Gemini API vision models for visual grounding tests.}
        \resumeItem{Mapped element coordinates from vision responses to viewport pixels and integrated automated URL checks.}
      \resumeItemListEnd

    \resumeProjectHeading
      {\textbf{Playwright AI-Reporter} $|$ \emph{Personal Project}}{github.com/OmanN777/playwright-ai-reporter}
      \resumeItemListStart
        \resumeItem{Built a Playwright E2E testing framework integrated with GitHub Actions CI/CD pipeline for automated test execution.}
        \resumeItem{Integrated the Gemini AI API to automatically analyze test failures, identify root causes, and output markdown reports.}
      \resumeItemListEnd

    \resumeProjectHeading
      {\textbf{Playwright Automation Study} $|$ \emph{Training Project}}{github.com/OmanN777/playwright-udemy-course}
      \resumeItemListStart
        \resumeItem{Set up a test automation study project for a local shopping web application using Playwright and JavaScript.}
        \resumeItem{Implemented custom page assertions, API authentication calls, and global setup hooks to manage test states.}
      \resumeItemListEnd

    \resumeProjectHeading
      {\textbf{Software Quality Assurance Suite} $|$ \emph{Academic Project}}{github.com/OmanN777/Testing-Website-Project}
      \resumeItemListStart
        \resumeItem{Developed Robot Framework E2E UI automation and JavaScript-based k6 load/stress testing scripts to validate web application quality.}
        \resumeItem{Designed comprehensive manual test cases, executed validation suites, and documented test execution logs.}
      \resumeItemListEnd
  \resumeSubHeadingListEnd

%-----------TECHNICAL SKILLS-----------
\section{Technical Skills}
 \begin{itemize}[leftmargin=0.15in, label={}]
    \small{\item{
     \textbf{Testing \& Tools}{: Playwright, Robot Framework, k6, JUnit, Postman, Swagger, Git} \\
     \textbf{Languages}{: JavaScript, TypeScript, Python, Java, SQL, Node.js} \\
     \textbf{Methodologies}{: E2E Testing, Performance Testing, API Testing, Unit Testing, Regression Testing, Page Object Model (POM), Database Validation} \\
     \textbf{CI/CD \& Database}{: GitHub Actions, MongoDB}
    }}
 \end{itemize}
\end{document}

