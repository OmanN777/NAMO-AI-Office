import os
import sys

# Set encoding for Windows console
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Read current masterclass HTML
target_file = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace\Work_Brief\agoda_qa_masterclass.html"

# We will write the full upgraded bilingual interactive HTML
html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ISTQB Global QA Standards & Senior Fundamentals Masterclass | Namo Natawat</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Noto+Sans+Thai:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg: #0b0f19;
      --card-bg: #111827;
      --card-border: #1f293d;
      --card-hover: #162036;
      --text-main: #f3f4f6;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --primary: #38bdf8;
      --primary-glow: rgba(56, 189, 248, 0.15);
      --accent-emerald: #34d399;
      --accent-amber: #fbbf24;
      --accent-rose: #fb7185;
      --accent-indigo: #818cf8;
      --accent-purple: #c084fc;
      --accent-teal: #2dd4bf;
      --sidebar-w: 320px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
    }

    body {
      font-family: 'Plus Jakarta Sans', 'Noto Sans Thai', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.7;
      display: flex;
      min-height: 100vh;
    }

    /* Sidebar Navigation */
    aside {
      width: var(--sidebar-w);
      background-color: #080c14;
      border-right: 1px solid var(--card-border);
      position: fixed;
      top: 0;
      bottom: 0;
      left: 0;
      padding: 1.5rem 1.15rem;
      overflow-y: auto;
      z-index: 50;
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      padding-bottom: 0.85rem;
      border-bottom: 1px solid var(--card-border);
    }

    .brand-logo {
      width: 36px;
      height: 36px;
      background: linear-gradient(135deg, #0284c7, #38bdf8);
      border-radius: 9px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      color: white;
      font-size: 1.05rem;
      box-shadow: 0 4px 12px var(--primary-glow);
    }

    .brand-title {
      font-family: 'Fraunces', Georgia, serif;
      font-weight: 700;
      font-size: 1.05rem;
      color: #fff;
      letter-spacing: -0.02em;
    }

    .brand-sub {
      font-size: 0.7rem;
      color: var(--text-dim);
      font-family: 'JetBrains Mono', monospace;
    }

    /* Global Language Toggle Bar in Sidebar */
    .lang-toggle-box {
      background: rgba(56, 189, 248, 0.06);
      border: 1px solid rgba(56, 189, 248, 0.2);
      border-radius: 10px;
      padding: 0.75rem 0.85rem;
      display: flex;
      flex-direction: column;
      gap: 0.5rem;
    }

    .lang-toggle-title {
      font-size: 0.72rem;
      font-weight: 700;
      color: #94a3b8;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .lang-btn-group {
      display: flex;
      background: #0d1322;
      border-radius: 6px;
      padding: 2px;
      border: 1px solid var(--card-border);
    }

    .lang-btn {
      flex: 1;
      padding: 0.35rem 0.5rem;
      font-size: 0.75rem;
      font-weight: 600;
      border: none;
      background: transparent;
      color: var(--text-muted);
      cursor: pointer;
      border-radius: 4px;
      transition: all 0.2s ease;
      font-family: 'Plus Jakarta Sans', 'Noto Sans Thai', sans-serif;
    }

    .lang-btn.active {
      background: var(--primary);
      color: #080c14;
      font-weight: 700;
    }

    nav {
      display: flex;
      flex-direction: column;
      gap: 0.2rem;
    }

    .nav-label {
      font-size: 0.65rem;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-dim);
      font-weight: 700;
      margin: 0.75rem 0 0.25rem 0.5rem;
    }

    .nav-item {
      display: flex;
      align-items: center;
      gap: 0.55rem;
      padding: 0.45rem 0.65rem;
      border-radius: 7px;
      color: var(--text-muted);
      text-decoration: none;
      font-size: 0.78rem;
      font-weight: 500;
      transition: all 0.2s ease;
    }

    .nav-item:hover, .nav-item.active {
      color: var(--primary);
      background-color: var(--primary-glow);
    }

    .nav-item .icon {
      font-size: 0.85rem;
    }

    /* Main Content Area */
    main {
      margin-left: var(--sidebar-w);
      flex: 1;
      padding: 2.75rem 3.5rem;
      max-width: 1320px;
    }

    header {
      margin-bottom: 3.5rem;
      padding-bottom: 2rem;
      border-bottom: 1px solid var(--card-border);
    }

    .badge-bar {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 1rem;
      flex-wrap: wrap;
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      padding: 0.3rem 0.75rem;
      border-radius: 9999px;
      font-size: 0.75rem;
      font-weight: 600;
      font-family: 'JetBrains Mono', monospace;
    }

    .badge-istqb { background: rgba(192, 132, 252, 0.15); color: #c084fc; border: 1px solid rgba(192, 132, 252, 0.3); }
    .badge-agoda { background: rgba(56, 189, 248, 0.12); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.3); }
    .badge-role { background: rgba(52, 211, 153, 0.12); color: #34d399; border: 1px solid rgba(52, 211, 153, 0.3); }

    h1 {
      font-family: 'Fraunces', Georgia, serif;
      font-size: 2.6rem;
      font-weight: 700;
      color: #fff;
      line-height: 1.2;
      margin-bottom: 0.75rem;
      letter-spacing: -0.03em;
    }

    .hero-sub {
      font-size: 1.05rem;
      color: var(--text-muted);
      max-width: 900px;
    }

    /* Section Styling */
    section {
      margin-bottom: 5rem;
      scroll-margin-top: 2rem;
    }

    .section-header {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 1.75rem;
    }

    .section-num {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.85rem;
      font-weight: 700;
      background: var(--primary-glow);
      color: var(--primary);
      padding: 0.25rem 0.6rem;
      border-radius: 6px;
      border: 1px solid rgba(56, 189, 248, 0.3);
    }

    h2 {
      font-family: 'Fraunces', Georgia, serif;
      font-size: 1.85rem;
      font-weight: 700;
      color: #fff;
      letter-spacing: -0.02em;
    }

    h3 {
      font-size: 1.15rem;
      font-weight: 600;
      color: #e2e8f0;
      margin: 1.25rem 0 0.75rem 0;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    p {
      margin-bottom: 1rem;
      color: #cbd5e1;
    }

    /* Grid Layouts */
    .grid-2 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(360px, 1fr));
      gap: 1.25rem;
      margin-bottom: 1.5rem;
    }

    .grid-3 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1.25rem;
      margin-bottom: 1.5rem;
    }

    /* Card Component - Interactive Tap to Translate */
    .card, .technique-box, .qa-box {
      cursor: pointer;
      position: relative;
      user-select: text;
    }

    .card {
      background-color: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 1.5rem;
      transition: all 0.2s ease;
    }

    .card:hover {
      border-color: rgba(56, 189, 248, 0.5);
      background-color: var(--card-hover);
      transform: translateY(-2px);
    }

    /* Individual Card Language Badge */
    .card-lang-indicator {
      position: absolute;
      top: 0.85rem;
      right: 0.85rem;
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.65rem;
      font-weight: 700;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      color: var(--text-dim);
      padding: 0.15rem 0.45rem;
      border-radius: 4px;
      pointer-events: none;
      transition: all 0.2s ease;
    }

    .card:hover .card-lang-indicator,
    .technique-box:hover .card-lang-indicator,
    .qa-box:hover .card-lang-indicator {
      background: rgba(56, 189, 248, 0.15);
      border-color: rgba(56, 189, 248, 0.4);
      color: var(--primary);
    }

    .is-th-active .card-lang-indicator {
      background: rgba(52, 211, 153, 0.15) !important;
      border-color: rgba(52, 211, 153, 0.4) !important;
      color: #34d399 !important;
    }

    /* Content Switching Logic */
    .lang-th {
      display: none;
    }

    .is-th-active .lang-en {
      display: none !important;
    }

    .is-th-active .lang-th {
      display: block !important;
    }

    /* Global forced TH mode */
    body.global-th .lang-en {
      display: none !important;
    }

    body.global-th .lang-th {
      display: block !important;
    }

    body.global-th .card-lang-indicator {
      background: rgba(52, 211, 153, 0.15);
      border-color: rgba(52, 211, 153, 0.4);
      color: #34d399;
    }

    .card-tag {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.7rem;
      font-weight: 600;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      display: inline-block;
      margin-bottom: 0.75rem;
      text-transform: uppercase;
    }

    .tag-emerald { background: rgba(52, 211, 153, 0.15); color: #34d399; }
    .tag-blue { background: rgba(56, 189, 248, 0.15); color: #38bdf8; }
    .tag-amber { background: rgba(251, 191, 36, 0.15); color: #fbbf24; }
    .tag-rose { background: rgba(251, 113, 133, 0.15); color: #fb7185; }
    .tag-indigo { background: rgba(129, 140, 248, 0.15); color: #818cf8; }
    .tag-purple { background: rgba(192, 132, 252, 0.15); color: #c084fc; }
    .tag-teal { background: rgba(45, 212, 191, 0.15); color: #2dd4bf; }

    /* Deep Technique Container */
    .technique-box {
      background-color: #0d1424;
      border: 1px solid var(--card-border);
      border-radius: 12px;
      padding: 1.75rem;
      margin-bottom: 1.75rem;
      transition: all 0.2s ease;
    }

    .technique-box:hover {
      border-color: rgba(56, 189, 248, 0.4);
      background-color: #10192e;
    }

    .technique-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.06);
      padding-bottom: 0.85rem;
      margin-bottom: 1rem;
      flex-wrap: wrap;
      gap: 0.5rem;
      padding-right: 3.5rem;
    }

    .technique-title {
      font-size: 1.25rem;
      font-weight: 700;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .principle-text {
      font-size: 0.95rem;
      color: #cbd5e1;
      margin-bottom: 1rem;
      line-height: 1.7;
    }

    .scenario-badge {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.78rem;
      font-weight: 600;
      color: #38bdf8;
      background: rgba(56, 189, 248, 0.1);
      padding: 0.25rem 0.6rem;
      border-radius: 6px;
      display: inline-block;
      margin-bottom: 0.5rem;
      border: 1px solid rgba(56, 189, 248, 0.2);
    }

    .example-grid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 1rem;
      margin-top: 0.75rem;
      background: #090d16;
      border: 1px solid #1e293b;
      border-radius: 8px;
      padding: 1rem 1.25rem;
    }

    @media (max-width: 768px) {
      .example-grid { grid-template-columns: 1fr; }
    }

    /* Tables */
    .table-wrapper {
      overflow-x: auto;
      border: 1px solid var(--card-border);
      border-radius: 12px;
      margin: 1.5rem 0;
      background-color: var(--card-bg);
    }

    table {
      width: 100%;
      border-collapse: collapse;
      text-align: left;
      font-size: 0.88rem;
    }

    th {
      background-color: #0d1322;
      padding: 1rem 1.25rem;
      font-weight: 600;
      color: #94a3b8;
      border-bottom: 1px solid var(--card-border);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      font-size: 0.75rem;
      font-family: 'JetBrains Mono', monospace;
    }

    td {
      padding: 1rem 1.25rem;
      border-bottom: 1px solid var(--card-border);
      color: #cbd5e1;
      vertical-align: top;
    }

    tr:last-child td {
      border-bottom: none;
    }

    tr:hover td {
      background-color: rgba(255, 255, 255, 0.02);
    }

    /* Dialogue & Q&A Box */
    .qa-box {
      background-color: #0f172a;
      border: 1px solid #1e293b;
      border-left: 4px solid var(--primary);
      border-radius: 0 12px 12px 0;
      padding: 1.5rem;
      margin-bottom: 1.5rem;
      transition: all 0.2s ease;
    }

    .qa-box:hover {
      background-color: #141d33;
      border-color: #334155;
    }

    .qa-box.scenario { border-left-color: var(--accent-emerald); }
    .qa-box.warning { border-left-color: var(--accent-amber); }
    .qa-box.mindset { border-left-color: var(--accent-indigo); }
    .qa-box.purple { border-left-color: var(--accent-purple); }

    .qa-question {
      font-size: 1.05rem;
      font-weight: 700;
      color: #fff;
      margin-bottom: 0.75rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      padding-right: 3.5rem;
    }

    .qa-answer {
      font-size: 0.95rem;
      color: #cbd5e1;
      line-height: 1.7;
    }

    .punchline {
      margin-top: 0.75rem;
      padding: 0.75rem 1rem;
      background: rgba(56, 189, 248, 0.08);
      border-radius: 6px;
      font-size: 0.88rem;
      color: #7dd3fc;
      border: 1px dashed rgba(56, 189, 248, 0.3);
    }

    .punchline strong {
      color: #38bdf8;
    }

    /* Code & Mono Elements */
    code, .code-inline {
      font-family: 'JetBrains Mono', monospace;
      font-size: 0.82rem;
      background-color: #1e293b;
      color: #38bdf8;
      padding: 0.15rem 0.4rem;
      border-radius: 4px;
    }

    /* Bullet Points */
    ul, ol {
      margin-bottom: 1rem;
      color: #cbd5e1;
      padding-left: 1.25rem;
    }

    li {
      margin-bottom: 0.4rem;
    }

    footer {
      margin-top: 5rem;
      padding-top: 2rem;
      border-top: 1px solid var(--card-border);
      text-align: center;
      color: var(--text-dim);
      font-size: 0.85rem;
    }

    @media (max-width: 900px) {
      body { flex-direction: column; }
      aside { width: 100%; position: relative; height: auto; }
      main { margin-left: 0; padding: 2rem 1.5rem; }
    }
  </style>
</head>
<body>

  <!-- Sidebar -->
  <aside>
    <div class="brand">
      <div class="brand-logo">QA</div>
      <div>
        <div class="brand-title">Global QA Standard</div>
        <div class="brand-sub">ISTQB & Enterprise Scale</div>
      </div>
    </div>

    <!-- Interactive Language Switcher -->
    <div class="lang-toggle-box">
      <div class="lang-toggle-title">
        <span>🌐 Master Language</span>
        <span style="font-size: 0.65rem; color: #38bdf8; font-weight: normal;">Tap card to flip</span>
      </div>
      <div class="lang-btn-group">
        <button class="lang-btn active" id="btn-en" onclick="setGlobalLang('en')">English (EN)</button>
        <button class="lang-btn" id="btn-th" onclick="setGlobalLang('th')">ภาษาไทย (TH)</button>
      </div>
    </div>

    <nav>
      <div class="nav-label">ISTQB Core Principles</div>
      <a href="#sec-principles" class="nav-item"><span class="icon">📜</span> 7 Principles of Testing</a>
      <a href="#sec-terms" class="nav-item"><span class="icon">📖</span> Terminology & V&V</a>
      <a href="#sec-acceptance" class="nav-item"><span class="icon">🏛️</span> Acceptance Testing (UAT/SAT)</a>
      <a href="#sec-criteria" class="nav-item"><span class="icon">🚪</span> Entry & Exit Criteria</a>
      
      <div class="nav-label">Test Techniques & Deep Scenarios</div>
      <a href="#sec-techniques" class="nav-item"><span class="icon">🎯</span> Black-Box Techniques (In-Depth)</a>
      <a href="#sec-matrix" class="nav-item"><span class="icon">📊</span> Test Matrix & Documentation</a>
      <a href="#sec-types-deep" class="nav-item"><span class="icon">🧪</span> Testing Types & Scenarios</a>
      <a href="#sec-whitebox" class="nav-item"><span class="icon">🔬</span> White-Box vs. Gray-Box</a>
      <a href="#sec-lifecycle" class="nav-item"><span class="icon">🔄</span> STLC & Bug Lifecycle</a>

      <div class="nav-label">Engineering & Tech Depth</div>
      <a href="#sec-api" class="nav-item"><span class="icon">⚡</span> API & Status Codes</a>
      <a href="#sec-automation" class="nav-item"><span class="icon">🤖</span> Automation & Pyramid</a>
      <a href="#sec-abtesting" class="nav-item"><span class="icon">🧪</span> A/B Testing & Microservices</a>
      <a href="#sec-glossary" class="nav-item"><span class="icon">📚</span> Essential QA Terms A-Z</a>

      <div class="nav-label">Interview Battlefield</div>
      <a href="#sec-framework" class="nav-item"><span class="icon">💡</span> 3-Step Answering Framework</a>
      <a href="#sec-scenarios" class="nav-item"><span class="icon">🎤</span> Standard Live Scenarios</a>
      <a href="#sec-behavioral" class="nav-item"><span class="icon">💼</span> Conflict & Mindset</a>
      <a href="#sec-questions" class="nav-item"><span class="icon">❓</span> High-Signal Questions to Ask</a>
    </nav>

    <div style="margin-top: auto; padding: 0.85rem; background: #111827; border-radius: 8px; border: 1px solid var(--card-border);">
      <div style="font-size: 0.7rem; color: var(--text-dim); text-transform: uppercase; font-weight: 700;">Candidate Target</div>
      <div style="font-size: 0.85rem; font-weight: 700; color: #fff; margin-top: 0.2rem;">Solid Junior QA Engineer</div>
      <div style="font-size: 0.75rem; color: var(--primary); font-family: 'JetBrains Mono'; margin-top: 0.1rem;">International Standards</div>
    </div>
  </aside>

  <!-- Main Content -->
  <main>
    <header>
      <div class="badge-bar">
        <span class="badge badge-istqb">🌐 ISTQB Foundation & Advanced Standard</span>
        <span class="badge badge-agoda">🏢 Global Tech Ready (Agoda / FinTech / Enterprise)</span>
        <span class="badge badge-role">🎯 Target: The Most Solid Junior QA</span>
      </div>
      <h1>Global Software Testing Standard & Masterclass</h1>
      <p class="hero-sub">
        The definitive, uncompressed handbook for modern Quality Assurance. Built upon ISTQB principles, IEEE/ISO standards, deep scenario-based explanations, and enterprise test design techniques.
        <br><strong style="color: #38bdf8; font-size: 0.9rem;">💡 Tip: บอสสามารถ "คลิก/จิ้มที่การ์ดหรือกล่องข้อความใดก็ได้" เพื่อสลับดูคำแปลภาษาไทยเฉพาะจุด หรือกดปุ่ม TH ที่ Sidebar ซ้ายมือเพื่อแปลทั้งหน้าได้ทันทีค่ะ!</strong>
      </p>
    </header>

    <!-- SECTION 1: 7 Principles of Testing -->
    <section id="sec-principles">
      <div class="section-header">
        <span class="section-num">PART 01</span>
        <h2>The 7 Fundamental Principles of Software Testing (ISTQB Standard)</h2>
      </div>
      <p>Every senior interviewer expects you to understand these 7 core testing truths that govern software engineering:</p>

      <div class="grid-3">
        <!-- Principle 1 -->
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-rose">Principle 1</span>
          <div class="lang-en">
            <h3>1. Testing shows presence of defects, not absence</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">Testing reduces the probability of undiscovered defects, but <strong>can never prove the software is 100% bug-free</strong>.</p>
          </div>
          <div class="lang-th">
            <h3 style="color: #38bdf8;">1. การทดสอบแสดงว่ามีบั๊กอยู่ แต่ไม่ได้พิสูจน์ว่าไม่มีบั๊ก</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">การทดสอบช่วยลดโอกาสที่จะพบบั๊กที่ซ่อนอยู่ แต่<strong>ไม่มีทางพิสูจน์ได้ว่าซอฟต์แวร์ปราศจากบั๊ก 100%</strong></p>
          </div>
        </div>

        <!-- Principle 2 -->
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-amber">Principle 2</span>
          <div class="lang-en">
            <h3>2. Exhaustive testing is impossible</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">Testing all possible combinations of inputs and preconditions is infeasible. We use <strong>Risk-Based Testing (RBT) and BVA/EP techniques</strong> to prioritize.</p>
          </div>
          <div class="lang-th">
            <h3 style="color: #fbbf24;">2. การทดสอบทุกกรณีเป็นไปไม่ได้ (Exhaustive Testing)</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">เราไม่สามารถเทสทุก Input และทุกเงื่อนไขบนโลกได้ จึงต้องใช้เทคนิค <strong>Risk-Based Testing และ BVA/EP</strong> เพื่อจัดลำดับความสำคัญของเคส</p>
          </div>
        </div>

        <!-- Principle 3 -->
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-emerald">Principle 3</span>
          <div class="lang-en">
            <h3>3. Early testing (Shift-Left) saves time & money</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">Catching a requirement bug in design phase costs <strong>10x to 100x less</strong> than fixing it in Production after release.</p>
          </div>
          <div class="lang-th">
            <h3 style="color: #34d399;">3. การเทสตั้งแต่เนิ่นๆ (Shift-Left) ประหยัดเวลาและงบ</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">การเจอบั๊กตั้งแต่ช่วงวิเคราะห์ Requirement หรือ Design จะ<strong>ประหยัดต้นทุนกว่าการตามแก้บน Production ถึง 10x - 100x เท่า</strong></p>
          </div>
        </div>

        <!-- Principle 4 -->
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-purple">Principle 4</span>
          <div class="lang-en">
            <h3>4. Defect Clustering (Pareto 80/20 Rule)</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;"><strong>80% of software defects</strong> are typically concentrated in <strong>20% of the modules</strong> (e.g. complex Payment or Booking engines).</p>
          </div>
          <div class="lang-th">
            <h3 style="color: #c084fc;">4. บั๊กมักกระจุกตัว (Pareto 80/20 Rule)</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;"><strong>บั๊กกว่า 80%</strong> มักจะกระจุกตัวอยู่ใน <strong>20% ของโมดูลที่ซับซ้อนที่สุด</strong> เช่น ระบบตัดเงิน (Payment) หรือเครื่องมือจอง (Booking Engine)</p>
          </div>
        </div>

        <!-- Principle 5 -->
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-blue">Principle 5</span>
          <div class="lang-en">
            <h3>5. Beware of the Pesticide Paradox</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">If identical tests are repeated over and over, they will stop finding new bugs. QA must regularly <strong>update and review test suites</strong>.</p>
          </div>
          <div class="lang-th">
            <h3 style="color: #38bdf8;">5. ระวังภาวะดื้อยา (Pesticide Paradox)</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">ถ้าเรายิง Test Suite เดิมซ้ำๆ มันจะเริ่มไม่เจอบั๊กใหม่ เหมือนแมลงที่ดื้อยาฆ่าแมลง QA จึงต้อง<strong>คอยหมั่นอัปเดตและปรับปรุงเคสเทสเสมอ</strong></p>
          </div>
        </div>

        <!-- Principle 6 & 7 -->
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-indigo">Principle 6 & 7</span>
          <div class="lang-en">
            <h3>6. Context Dependent & 7. Absence of Errors Fallacy</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">• Banking/FinTech requires different testing than an E-commerce web.<br>• A bug-free system is still a failure if it <strong>does not fulfill user needs</strong>.</p>
          </div>
          <div class="lang-th">
            <h3 style="color: #818cf8;">6. การเทสขึ้นกับบริบท & 7. ภาพลวงตาของความไร้บั๊ก</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">• ระบบธนาคารย่อมต้องการการเทสที่ต่างจากเว็บช็อปปิ้งทั่วไป<br>• ระบบที่ไม่มีบั๊กเลย ก็ยังถือว่าล้มเหลวถ้า<strong>มันไม่ตอบโจทย์การใช้งานจริงของลูกค้า</strong></p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 2: Core Terminology -->
    <section id="sec-terms">
      <div class="section-header">
        <span class="section-num">PART 02</span>
        <h2>Core QA Fundamentals & Terminology</h2>
      </div>

      <div class="grid-2">
        <!-- Error vs Bug vs Failure -->
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-rose">Critical Distinction</span>
          <div class="lang-en">
            <h3>Error ➔ Bug/Defect ➔ Failure</h3>
            <ul style="font-size: 0.88rem;">
              <li><strong>Error (Mistake):</strong> A human mistake by developer/designer that produces an incorrect system behavior (e.g., typo, wrong logical operator <code>&lt;</code> instead of <code>&lt;=</code>).</li>
              <li><strong>Defect / Bug:</strong> The flaw in source code or specification document resulting from the Error.</li>
              <li><strong>Failure:</strong> The observable deviation where the software fails to perform its required function during live runtime execution.</li>
            </ul>
            <div class="punchline">
              <strong>🗣️ Interview Punchline:</strong><br>
              <em>"An <strong>Error</strong> is committed by a human developer, introducing a <strong>Defect/Bug</strong> into the code, which manifests as a software <strong>Failure</strong> when executed by an end-user."</em>
            </div>
          </div>
          <div class="lang-th">
            <h3 style="color: #fb7185;">ข้อผิดพลาดคน (Error) ➔ บั๊กในโค้ด (Bug) ➔ ระบบพัง (Failure)</h3>
            <ul style="font-size: 0.88rem;">
              <li><strong>Error (ความผิดพลาด):</strong> ความผิดพลาดของมนุษย์ (Dev/Designer) เช่น พิมพ์ผิด หรือใส่เครื่องหมายตรรกะผิด <code>&lt;</code> แทนที่จะเป็น <code>&lt;=</code></li>
              <li><strong>Defect / Bug (ตำหนิ/บั๊ก):</strong> จุดบกพร่องในโค้ดหรือเอกสารสเปก ที่เกิดมาจาก Error ของคน</li>
              <li><strong>Failure (ความล้มเหลว):</strong> อาการระบบพังจริงขณะรัน ที่ผู้ใช้งานพบเห็นเมื่อใช้งานซอฟต์แวร์</li>
            </ul>
            <div class="punchline">
              <strong>🗣️ ประโยคสรุปตอบกรรมการ:</strong><br>
              <em>"<strong>Error</strong> เกิดจากความผิดพลาดของมนุษย์ ก่อให้เกิด <strong>Defect/Bug</strong> ในโค้ด และเมื่อผู้ใช้เปิดใช้งานจึงส่งผลให้เกิด <strong>Failure</strong> ของระบบค่ะ"</em>
            </div>
          </div>
        </div>

        <!-- Verification vs Validation -->
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-blue">V & V Framework</span>
          <div class="lang-en">
            <h3>Verification vs. Validation (V&V)</h3>
            <div style="display: flex; flex-direction: column; gap: 0.6rem; margin-top: 0.5rem;">
              <div style="background: rgba(255,255,255,0.02); padding: 0.65rem 0.85rem; border-radius: 6px; border: 1px solid var(--card-border);">
                <strong style="color: #38bdf8;">1. Verification (Static Testing):</strong><br>
                <span style="font-size: 0.85rem; color: #cbd5e1;"><em>"Are we building the product <strong>right</strong>?"</em></span>
                <p style="font-size: 0.8rem; color: var(--text-muted); margin: 0.2rem 0 0 0;">Evaluating documents, architecture, design diagrams, and source code <strong>WITHOUT executing</strong> code. (e.g., Code Reviews, Static Analysis, Inspections).</p>
              </div>
              <div style="background: rgba(255,255,255,0.02); padding: 0.65rem 0.85rem; border-radius: 6px; border: 1px solid var(--card-border);">
                <strong style="color: #34d399;">2. Validation (Dynamic Testing):</strong><br>
                <span style="font-size: 0.85rem; color: #cbd5e1;"><em>"Are we building the <strong>right</strong> product?"</em></span>
                <p style="font-size: 0.8rem; color: var(--text-muted); margin: 0.2rem 0 0 0;">Evaluating the actual software by <strong>EXECUTING</strong> it to verify that it meets user needs and business requirements. (e.g., Functional, E2E, UAT).</p>
              </div>
            </div>
          </div>
          <div class="lang-th">
            <h3 style="color: #38bdf8;">Verification vs. Validation (ตรวจสอบความถูกต้อง vs ความตรงใจ)</h3>
            <div style="display: flex; flex-direction: column; gap: 0.6rem; margin-top: 0.5rem;">
              <div style="background: rgba(255,255,255,0.02); padding: 0.65rem 0.85rem; border-radius: 6px; border: 1px solid var(--card-border);">
                <strong style="color: #38bdf8;">1. Verification (การตรวจเอกสาร/โค้ดโดยไม่รัน - Static Testing):</strong><br>
                <span style="font-size: 0.85rem; color: #cbd5e1;"><em>"เรากำลังสร้างงานออกมา<strong>ถูกวิธีตามสเปก</strong>หรือไม่?"</em></span>
                <p style="font-size: 0.8rem; color: var(--text-muted); margin: 0.2rem 0 0 0;">การตรวจเอกสาร PRD, Architecture, ดีไซน์ และ Code Review <strong>โดยไม่ต้องสั่งรันโปรแกรม</strong></p>
              </div>
              <div style="background: rgba(255,255,255,0.02); padding: 0.65rem 0.85rem; border-radius: 6px; border: 1px solid var(--card-border);">
                <strong style="color: #34d399;">2. Validation (การทดสอบระบบจริงโดยการรัน - Dynamic Testing):</strong><br>
                <span style="font-size: 0.85rem; color: #cbd5e1;"><em>"เรากำลังสร้าง<strong>สิ่งที่ผู้ใช้ต้องการจริงๆ</strong> หรือไม่?"</em></span>
                <p style="font-size: 0.8rem; color: var(--text-muted); margin: 0.2rem 0 0 0;">การ<strong>สั่งรันโปรแกรมจริง</strong> เพื่อดูว่าระบบตอบสนองความต้องการของผู้ใช้งานและธุรกิจจริงหรือไม่ (เช่น Functional, E2E, UAT)</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Severity vs Priority -->
      <div class="card" onclick="toggleCardLang(this)">
        <div class="card-lang-indicator">EN / TH</div>
        <span class="card-tag tag-amber">Triage & Prioritization</span>
        <div class="lang-en">
          <h3>Severity vs. Priority (The 4-Quadrant Matrix)</h3>
          <div class="table-wrapper" style="margin: 0.75rem 0 0 0;">
            <table>
              <thead>
                <tr>
                  <th>Attribute</th>
                  <th>Severity (Technical Impact)</th>
                  <th>Priority (Business Urgency)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Definition</strong></td>
                  <td>Measures the technical impact on system stability/functionality.</td>
                  <td>Measures how urgently the business requires this fix to be deployed.</td>
                </tr>
                <tr>
                  <td><strong>Assigned By</strong></td>
                  <td><span class="badge badge-agoda">QA Engineer / Tester</span></td>
                  <td><span class="badge badge-date">Product Owner / Business Lead</span></td>
                </tr>
                <tr>
                  <td><strong>High Priority / Low Severity</strong></td>
                  <td colspan="2">
                    <strong style="color: #fbbf24;">Example:</strong> A misspelling on the Homepage logo (<code>"Agdo"</code>) or wrong campaign discount banner. Doesn't crash the server (Low Severity), but damages brand reputation immediately (High Priority).
                  </td>
                </tr>
                <tr>
                  <td><strong>High Severity / Low Priority</strong></td>
                  <td colspan="2">
                    <strong style="color: #818cf8;">Example:</strong> A complete database crash occurring only when running on an obsolete OS (e.g., Windows XP) used by 0.001% of customers. Technically fatal (High Severity), but rarely encountered (Low Priority).
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div class="lang-th">
          <h3 style="color: #fbbf24;">Severity (ความร้ายแรงทางเทคนิค) vs. Priority (ความเร่งด่วนทางธุรกิจ)</h3>
          <div class="table-wrapper" style="margin: 0.75rem 0 0 0;">
            <table>
              <thead>
                <tr>
                  <th>คุณสมบัติ</th>
                  <th>Severity (ผลกระทบทางเทคนิค)</th>
                  <th>Priority (ความเร่งด่วนทางธุรกิจ)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>คำนิยาม</strong></td>
                  <td>วัดระดับความรุนแรงของผลกระทบต่อระบบ/ฟังก์ชัน</td>
                  <td>วัดว่าธุรกิจต้องการให้แก้บั๊กนี้เสร็จด่วนแค่ไหน</td>
                </tr>
                <tr>
                  <td><strong>คนประเมิน</strong></td>
                  <td><span class="badge badge-agoda">QA Engineer / Tester</span></td>
                  <td><span class="badge badge-date">Product Owner / ฝ่ายธุรกิจ</span></td>
                </tr>
                <tr>
                  <td><strong>ด่วนมาก แต่ไม่ร้ายแรง (High Priority / Low Severity)</strong></td>
                  <td colspan="2">
                    <strong style="color: #fbbf24;">ตัวอย่าง:</strong> โลโก้หน้าเว็บสะกดชื่อแบรนด์ผิด (เช่น <code>"Agdo"</code>) หรือแบนเนอร์โปรโมชันขึ้นรูปผิด ระบบไม่ได้พัง (Low Severity) แต่เสียชื่อเสียงบริษัท ต้องแก้ทันที (High Priority)
                  </td>
                </tr>
                <tr>
                  <td><strong>ร้ายแรงมาก แต่ไม่เร่งด่วน (High Severity / Low Priority)</strong></td>
                  <td colspan="2">
                    <strong style="color: #818cf8;">ตัวอย่าง:</strong> ฐานข้อมูลพังทั้งระบบเมื่อรันบน Windows XP ที่มีผู้ใช้แค่ 0.001% ทางเทคนิคพังร้ายแรงมาก (High Severity) แต่แทบไม่มีลูกค้าเจอ จึงเก็บไว้แก้ทีหลังได้ (Low Priority)
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: Acceptance Testing Hierarchy -->
    <section id="sec-acceptance">
      <div class="section-header">
        <span class="section-num">PART 03</span>
        <h2>Acceptance Testing Hierarchy: UAT vs. SAT vs. FAT vs. Alpha/Beta</h2>
      </div>
      <p>Acceptance Testing is the formal phase where software is validated against contract requirements and business goals before commercial rollout.</p>

      <div class="card" onclick="toggleCardLang(this)">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="lang-en">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Testing Type</th>
                  <th>Full Form</th>
                  <th>Who Performs It?</th>
                  <th>Environment / Location</th>
                  <th>Core Goal & Real Example</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>UAT</strong></td>
                  <td><strong>User Acceptance Testing</strong></td>
                  <td>End-Users, Business Clients, or Product Managers (PO)</td>
                  <td>Staging / Pre-Production (with sanitized real data)</td>
                  <td>Validates whether the software satisfies end-to-end business requirements and real user workflows (e.g. verifying that a guest can book a hotel and receive invoices matching Thai tax invoice regulations).</td>
                </tr>
                <tr>
                  <td><strong>SAT</strong></td>
                  <td><strong>Site Acceptance Testing</strong></td>
                  <td>Client Stakeholders & Operations Team</td>
                  <td>Client's Real Target Environment / Production Infrastructure</td>
                  <td>Validates software performance, integrations, and security on the <strong>actual client site / live host infrastructure</strong> (e.g. testing payment gateway integrated directly with a partner bank's live server).</td>
                </tr>
                <tr>
                  <td><strong>FAT</strong></td>
                  <td><strong>Factory Acceptance Testing</strong></td>
                  <td>Vendor Developers & QA (Witnessed by Client)</td>
                  <td>Vendor / Developer's Environment (Before Delivery)</td>
                  <td>Validates that the software meets specifications <strong>at the supplier's development site</strong> before packaging and shipping to the client.</td>
                </tr>
                <tr>
                  <td><strong>Alpha Testing</strong></td>
                  <td>Alpha Acceptance Testing</td>
                  <td>Internal Employees, QA, & Developers</td>
                  <td>Internal Developer Environment (Controlled)</td>
                  <td>Early testing inside the organization to catch critical bugs before exposing the build to external users.</td>
                </tr>
                <tr>
                  <td><strong>Beta Testing</strong></td>
                  <td>Beta Acceptance Testing</td>
                  <td>Real External Users / Limited Public Audience</td>
                  <td>Real World Production / Field Environment</td>
                  <td>Releasing a beta version (e.g. App Beta on TestFlight) to gather usability feedback, device compatibility, and unexpected real-world edge cases.</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="punchline">
            <strong>🧠 Senior Summary Formula:</strong><br>
            <em>"<strong>FAT</strong> is tested at the vendor's factory ➔ <strong>SAT</strong> is tested on the client's live site ➔ <strong>UAT</strong> is tested by business users for contract sign-off ➔ <strong>Alpha</strong> is tested by internal staff ➔ <strong>Beta</strong> is released to the real world."</em>
          </div>
        </div>
        <div class="lang-th">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>ประเภทการเทส</th>
                  <th>ชื่อเต็ม</th>
                  <th>ใครเป็นคนเทส?</th>
                  <th>เทสที่ไหน / สภาพแวดล้อมใด?</th>
                  <th>เป้าหมายหลัก & ตัวอย่างจริง</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>UAT</strong></td>
                  <td><strong>User Acceptance Testing</strong></td>
                  <td>ผู้ใช้งานจริง, ลูกค้าฝ่ายธุรกิจ, หรือ Product Owner</td>
                  <td>Staging / Pre-Production (ใช้ข้อมูลจำลองที่เหมือนจริง)</td>
                  <td>ตรวจรับงานว่าระบบตอบโจทย์กระบวนการทางธุรกิจครบถ้วนตามสัญญาหรือไม่ (เช่น ตรวจสอบว่าจองโรงแรมแล้วได้ใบกำกับภาษีถูกต้องตามกฎหมายสรรพากร)</td>
                </tr>
                <tr>
                  <td><strong>SAT</strong></td>
                  <td><strong>Site Acceptance Testing</strong></td>
                  <td>ทีมไอทีและทีมปฏิบัติการของฝั่งลูกค้า</td>
                  <td>หน้างานจริง / Infrastructure จริงของลูกค้า (On-Site)</td>
                  <td>ตรวจสอบความพร้อมของระบบบน<strong>สถานที่จริงและเซิร์ฟเวอร์จริงของลูกค้า</strong> (เช่น ตรวจสอบระบบ Payment Gateway ที่เชื่อมกับ Core Banking ของธนาคารจริง)</td>
                </tr>
                <tr>
                  <td><strong>FAT</strong></td>
                  <td><strong>Factory Acceptance Testing</strong></td>
                  <td>ทีม Dev & QA ของผู้รับจ้าง (ลูกค้ามาร่วมสังเกตการณ์)</td>
                  <td>สถานที่พัฒนาของผู้รับจ้าง (ก่อนส่งมอบของ)</td>
                  <td>ตรวจสอบว่าซอฟต์แวร์ทำงานได้ตามสเปก<strong>ที่โรงงาน/ไซต์ของผู้ผลิต</strong> ก่อนทำการแพ็กของส่งมอบให้ลูกค้า</td>
                </tr>
                <tr>
                  <td><strong>Alpha Testing</strong></td>
                  <td>Alpha Acceptance Testing</td>
                  <td>พนักงานภายในองค์กร, QA, และ Developers</td>
                  <td>สภาพแวดล้อมภายใน (ควบคุมได้)</td>
                  <td>การเทสภายในบริษัทเพื่อดักเก็บบั๊กร้ายแรงก่อนที่จะปล่อยให้คนภายนอกเห็น</td>
                </tr>
                <tr>
                  <td><strong>Beta Testing</strong></td>
                  <td>Beta Acceptance Testing</td>
                  <td>ผู้ใช้งานจริงภายนอกกลุ่มทดลอง (Public Users)</td>
                  <td>สภาพแวดล้อมโลกจริง (Production / Field)</td>
                  <td>ปล่อยเวอร์ชันทดลอง (เช่น TestFlight App) ให้ผู้ใช้ภายนอกลองเล่น เพื่อเก็บ Feedback ด้าน Usability และดักบั๊กบนเครื่องรุ่นแปลกๆ</td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="punchline">
            <strong>🧠 สูตรจำง่ายสไตล์ Senior:</strong><br>
            <em>"<strong>FAT</strong> ตรวจที่โรงงานผู้ผลิต ➔ <strong>SAT</strong> ตรวจที่หน้างานจริงของลูกค้า ➔ <strong>UAT</strong> ตรวจรับมอบงานตามสัญญา ➔ <strong>Alpha</strong> คนในบริษัทลองเล่น ➔ <strong>Beta</strong> ปล่อยให้คนภายนอกทดลองใช้"</em>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 4: Entry & Exit Criteria -->
    <section id="sec-criteria">
      <div class="section-header">
        <span class="section-num">PART 04</span>
        <h2>Entry Criteria vs. Exit Criteria (Quality Gates)</h2>
      </div>
      <p>Quality Gates define formal conditions that must be met before transitioning between testing phases:</p>

      <div class="grid-2">
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-emerald">Phase Gate: Start</span>
          <div class="lang-en">
            <h3>1. Entry Criteria (When can we START testing?)</h3>
            <p style="font-size: 0.88rem; color: #cbd5e1;">Prerequisites required before QA begins test execution:</p>
            <ul style="font-size: 0.85rem;">
              <li>✅ Approved PRD & Acceptance Criteria in Jira.</li>
              <li>✅ Unit Tests passing with &gt; 80% code coverage.</li>
              <li>✅ Build deployed successfully to Staging environment.</li>
              <li>✅ Smoke Test Suite executed and <strong>100% PASSED</strong>.</li>
              <li>✅ Test Data & database seeds generated and verified.</li>
            </ul>
          </div>
          <div class="lang-th">
            <h3 style="color: #34d399;">1. Entry Criteria (เริ่มเทสได้เมื่อไหร่?)</h3>
            <p style="font-size: 0.88rem; color: #cbd5e1;">เงื่อนไขจำเป็นที่ต้องครบก่อนที่ QA จะเริ่มลงมือเทส:</p>
            <ul style="font-size: 0.85rem;">
              <li>✅ เอกสาร PRD และ Acceptance Criteria ใน Jira ได้รับการอนุมัติแล้ว</li>
              <li>✅ Unit Test รันผ่าน และมี Code Coverage &gt; 80%</li>
              <li>✅ Build งานขึ้น Staging สำเร็จเรียบร้อย</li>
              <li>✅ รัน Smoke Test ผ่าน <strong>100% ไม่มีตัวไหนล่ม</strong></li>
              <li>✅ ข้อมูล Test Data และ Seed ฐานข้อมูลถูกเตรียมพร้อมแล้ว</li>
            </ul>
          </div>
        </div>

        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-rose">Phase Gate: Finish</span>
          <div class="lang-en">
            <h3>2. Exit Criteria (When can we STOP testing / Release?)</h3>
            <p style="font-size: 0.88rem; color: #cbd5e1;">Conditions required before software can be signed off for Production:</p>
            <ul style="font-size: 0.85rem;">
              <li>🏁 100% planned Critical & High test cases executed.</li>
              <li>🏁 <strong>Zero P0 / P1 (Blocker / Critical) bugs remaining open</strong>.</li>
              <li>🏁 Automated Regression Suite passed (&gt; 95% pass rate).</li>
              <li>🏁 All agreed minor bugs logged with documented workarounds.</li>
              <li>🏁 Test Summary Report signed off by QA Lead & Product Owner.</li>
            </ul>
          </div>
          <div class="lang-th">
            <h3 style="color: #fb7185;">2. Exit Criteria (ปล่อยงาน/หยุดเทสได้เมื่อไหร่?)</h3>
            <p style="font-size: 0.88rem; color: #cbd5e1;">เงื่อนไขที่ต้องผ่านครบถ้วนก่อนจะเซ็นอนุมัติปล่อยงานขึ้น Production:</p>
            <ul style="font-size: 0.85rem;">
              <li>🏁 Test Case ระดับ Critical และ High รันครบ 100%</li>
              <li>🏁 <strong>ต้องไม่มีบั๊กระดับ P0 / P1 (Blocker/Critical) ค้างอยู่เด็ดขาด</strong></li>
              <li>🏁 Automated Regression Suite รันผ่านเกิน 95%</li>
              <li>🏁 บั๊กเล็กน้อยที่ยอมรับได้ ถูกบันทึกวิธีแก้ขัด (Workaround) ไว้อย่างชัดเจน</li>
              <li>🏁 รายงาน Test Summary Report ได้รับการเซ็นอนุมัติจาก QA Lead และ PO</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 5: Black-Box Test Design Techniques (DEEP-DIVE) -->
    <section id="sec-techniques">
      <div class="section-header">
        <span class="section-num">PART 05</span>
        <h2>Black-Box Test Design Techniques: Principles, Situations & In-Depth Examples</h2>
      </div>
      <p>Below is the detailed, uncompressed breakdown of every black-box test design technique, explaining <strong>the exact underlying logic, when to choose it, and full practical scenarios:</strong></p>

      <!-- Technique 1: BVA -->
      <div class="technique-box" onclick="toggleCardLang(this)">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="technique-header">
          <div class="technique-title">
            <span>📏 1. Boundary Value Analysis (BVA)</span>
          </div>
          <span class="card-tag tag-blue">Input Type: Ordered Range / Continuous Boundaries</span>
        </div>
        <div class="lang-en">
          <p class="principle-text">
            <strong>Fundamental Principle:</strong> Empirical studies show that programmers make the vast majority of coding mistakes at the <strong>extreme boundaries</strong> of an input range rather than in the middle. This is primarily caused by off-by-one errors (e.g., typing <code>&lt;</code> instead of <code>&lt;=</code>, or loop counters starting at 0 vs 1). BVA focuses 100% of test effort on the edges.
          </p>
          <div class="scenario-badge">📌 When to use this technique?</div>
          <p style="font-size: 0.88rem; color: #cbd5e1;">
            Use whenever the requirement specifies a continuous numerical range, text character length, date range, or file size limits (e.g. Password length 8–20 chars, Age 18–60, Upload size 1–10MB).
          </p>
          <div class="example-grid">
            <div>
              <strong style="color: #38bdf8;">🏨 Scenario: Hotel Booking Duration (1 to 30 Nights)</strong>
              <ul style="font-size: 0.82rem; margin-top: 0.4rem;">
                <li><code>Min - 1 (0 nights):</code> Invalid (Should throw validation error).</li>
                <li><code>Min (1 night):</code> Valid (Minimum allowable booking).</li>
                <li><code>Min + 1 (2 nights):</code> Valid (Just inside boundary).</li>
                <li><code>Nominal (15 nights):</code> Valid (Typical middle value).</li>
                <li><code>Max - 1 (29 nights):</code> Valid (Just inside upper boundary).</li>
                <li><code>Max (30 nights):</code> Valid (Maximum allowable booking).</li>
                <li><code>Max + 1 (31 nights):</code> Invalid (Should block booking).</li>
              </ul>
            </div>
            <div>
              <strong style="color: #34d399;">💳 Scenario: Credit Card Daily Transfer (100 to 50,000 THB)</strong>
              <ul style="font-size: 0.82rem; margin-top: 0.4rem;">
                <li><code>99.99 THB:</code> Invalid (Below minimum transfer).</li>
                <li><code>100.00 THB:</code> Valid (Exact minimum).</li>
                <li><code>100.01 THB:</code> Valid.</li>
                <li><code>49,999.99 THB:</code> Valid.</li>
                <li><code>50,000.00 THB:</code> Valid (Exact limit).</li>
                <li><code>50,000.01 THB:</code> Invalid (Exceeds daily limit).</li>
              </ul>
            </div>
          </div>
        </div>
        <div class="lang-th">
          <p class="principle-text">
            <strong>หลักการสำคัญ:</strong> สถิติชี้ว่าโปรแกรมเมอร์มักจะเขียนโค้ดผิดพลาดที่ <strong>"จุดขอบของข้อมูล"</strong> เสมอ โดยเกิดจากความสับสนเครื่องหมาย เช่น เผลอใส่ <code>&lt;</code> แทนที่จะเป็น <code>&lt;=</code> หรือการนับ Loop ผิด เทคนิค BVA จึงโฟกัสการเทสไปที่จุดขอบ Min / Max เพื่อดักจับข้อผิดพลาดเหล่านี้โดยเฉพาะ
          </p>
          <div class="scenario-badge">📌 ควรเลือกใช้ในสถานการณ์ไหน?</div>
          <p style="font-size: 0.88rem; color: #cbd5e1;">
            ใช้กับฟิลด์ที่มี <strong>ช่วงตัวเลขต่อเนื่อง, ความยาวตัวอักษร, ช่วงวันที่, หรือขนาดไฟล์</strong> (เช่น รหัสผ่าน 8–20 ตัวอักษร, อายุ 18–60 ปี, ขนาดไฟล์ 1–10MB)
          </p>
          <div class="example-grid">
            <div>
              <strong style="color: #38bdf8;">🏨 ตัวอย่าง: จำนวนคืนที่จองได้ (1 ถึง 30 คืน)</strong>
              <ul style="font-size: 0.82rem; margin-top: 0.4rem;">
                <li><code>Min - 1 (0 คืน):</code> ไม่ถูกต้อง (ระบบต้องแจ้งเตือน Error)</li>
                <li><code>Min (1 คืน):</code> ถูกต้อง (จำนวนขั้นต่ำที่จองได้)</li>
                <li><code>Min + 1 (2 คืน):</code> ถูกต้อง (ค่าถัดจากขอบล่าง)</li>
                <li><code>Nominal (15 คืน):</code> ถูกต้อง (ค่ากลางๆ ทั่วไป)</li>
                <li><code>Max - 1 (29 คืน):</code> ถูกต้อง (ค่าก่อนถึงขอบบน)</li>
                <li><code>Max (30 คืน):</code> ถูกต้อง (จำนวนสูงสุดที่จองได้)</li>
                <li><code>Max + 1 (31 คืน):</code> ไม่ถูกต้อง (ระบบต้องบล็อกไม่ให้จอง)</li>
              </ul>
            </div>
            <div>
              <strong style="color: #34d399;">💳 ตัวอย่าง: วงเงินโอนต่อวัน (100 ถึง 50,000 บาท)</strong>
              <ul style="font-size: 0.82rem; margin-top: 0.4rem;">
                <li><code>99.99 บาท:</code> ไม่ถูกต้อง (ต่ำกว่าขั้นต่ำ)</li>
                <li><code>100.00 บาท:</code> ถูกต้อง (ขั้นต่ำพอดี)</li>
                <li><code>100.01 บาท:</code> ถูกต้อง</li>
                <li><code>49,999.99 บาท:</code> ถูกต้อง</li>
                <li><code>50,000.00 บาท:</code> ถูกต้อง (วงเงินสูงสุดพอดี)</li>
                <li><code>50,000.01 บาท:</code> ไม่ถูกต้อง (เกินวงเงินต่อวัน)</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Technique 2: EP -->
      <div class="technique-box" onclick="toggleCardLang(this)">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="technique-header">
          <div class="technique-title">
            <span>📦 2. Equivalence Partitioning (EP)</span>
          </div>
          <span class="card-tag tag-emerald">Input Type: Discrete Classes / Partitioned Sets</span>
        </div>
        <div class="lang-en">
          <p class="principle-text">
            <strong>Fundamental Principle:</strong> When an input set is large, testing every single value is impossible and redundant. EP divides the entire input domain into mutually exclusive partitions where <strong>all values in a partition are assumed to be processed identically by the program logic</strong>. You only need to pick <em>one representative value</em> from each partition.
          </p>
          <div class="scenario-badge">📌 When to use this technique?</div>
          <p style="font-size: 0.88rem; color: #cbd5e1;">
            Use when inputs can be classified into clear categories, discrete drop-down choices, or logical demographic bands (e.g. Passenger types: Infant, Child, Adult; Payment methods: Visa, Mastercard, Cash).
          </p>
          <div class="example-grid">
            <div>
              <strong style="color: #38bdf8;">✈️ Scenario: Flight Ticket Passenger Pricing</strong>
              <p style="font-size: 0.82rem; color: #94a3b8; margin: 0.2rem 0;">Rules: &lt;2 yrs = Free Infant, 2-11 yrs = Child (50%), 12-59 yrs = Adult (Full), &ge;60 yrs = Senior (80%).</p>
              <ul style="font-size: 0.82rem; margin-top: 0.3rem;">
                <li><strong>Partition 1 (Infant):</strong> Pick Age <code>1</code> ➔ Expected: Free ticket.</li>
                <li><strong>Partition 2 (Child):</strong> Pick Age <code>7</code> ➔ Expected: 50% discount.</li>
                <li><strong>Partition 3 (Adult):</strong> Pick Age <code>30</code> ➔ Expected: Full price.</li>
                <li><strong>Partition 4 (Senior):</strong> Pick Age <code>68</code> ➔ Expected: 20% discount.</li>
                <li><strong>Invalid Partition:</strong> Pick Age <code>-5</code> or <code>"ABC"</code> ➔ Error.</li>
              </ul>
            </div>
            <div>
              <strong style="color: #34d399;">📝 Scenario: File Upload Format Validation</strong>
              <p style="font-size: 0.82rem; color: #94a3b8; margin: 0.2rem 0;">Requirement: Only PDF and PNG files are accepted.</p>
              <ul style="font-size: 0.82rem; margin-top: 0.3rem;">
                <li><strong>Valid Partition A:</strong> Pick <code>resume.pdf</code> ➔ Accepted.</li>
                <li><strong>Valid Partition B:</strong> Pick <code>photo.png</code> ➔ Accepted.</li>
                <li><strong>Invalid Partition C:</strong> Pick <code>video.mp4</code> ➔ Rejected.</li>
                <li><strong>Invalid Partition D:</strong> Pick <code>script.exe</code> ➔ Rejected.</li>
              </ul>
            </div>
          </div>
        </div>
        <div class="lang-th">
          <p class="principle-text">
            <strong>หลักการสำคัญ:</strong> เมื่อข้อมูลมีมหาศาล การไล่เทสทุกตัวเลขเป็นไปไม่ได้ เทคนิค EP จึงใช้วิธี<strong>แบ่งข้อมูลออกเป็นกลุ่มย่อย (Partitions)</strong> โดยสมมุติว่าข้อมูลทุกตัวที่อยู่ในกลุ่มเดียวกันจะถูกโปรแกรมประมวลผลเหมือนกันเป๊ะ เราจึงสุ่มหยิบ<strong>เพียง 1 ค่าตัวแทน</strong>จากแต่ละกลุ่มมาเทสก็เพียงพอ
          </p>
          <div class="scenario-badge">📌 ควรเลือกใช้ในสถานการณ์ไหน?</div>
          <p style="font-size: 0.88rem; color: #cbd5e1;">
            ใช้เมื่อข้อมูลสามารถจัดหมวดหมู่ได้ชัดเจน, ตัวเลือก Dropdown, หรือช่วงกลุ่มอายุประชากร
          </p>
          <div class="example-grid">
            <div>
              <strong style="color: #38bdf8;">✈️ ตัวอย่าง: ราคาตั๋วเครื่องบินตามวัย</strong>
              <p style="font-size: 0.82rem; color: #94a3b8; margin: 0.2rem 0;">เกณฑ์: &lt;2 ปี = ทารกฟรี, 2-11 ปี = เด็ก (ลด 50%), 12-59 ปี = ผู้ใหญ่ (เต็มราคา), &ge;60 ปี = สูงวัย (ลด 20%)</p>
              <ul style="font-size: 0.82rem; margin-top: 0.3rem;">
                <li><strong>กลุ่มที่ 1 (ทารก):</strong> สุ่มอายุ <code>1 ขวบ</code> ➔ ตั๋วฟรี</li>
                <li><strong>กลุ่มที่ 2 (เด็ก):</strong> สุ่มอายุ <code>7 ขวบ</code> ➔ ได้ลด 50%</li>
                <li><strong>กลุ่มที่ 3 (ผู้ใหญ่):</strong> สุ่มอายุ <code>30 ปี</code> ➔ จ่ายเต็มราคา</li>
                <li><strong>กลุ่มที่ 4 (สูงวัย):</strong> สุ่มอายุ <code>68 ปี</code> ➔ ได้ลด 20%</li>
                <li><strong>กลุ่มที่ไม่ถูกต้อง (Invalid):</strong> สุ่มอายุ <code>-5</code> หรือ <code>"ABC"</code> ➔ แจ้งเตือน Error</li>
              </ul>
            </div>
            <div>
              <strong style="color: #34d399;">📝 ตัวอย่าง: นามสกุลไฟล์ที่อนุญาตให้อัปโหลด</strong>
              <p style="font-size: 0.82rem; color: #94a3b8; margin: 0.2rem 0;">สเปก: ระบบรับเฉพาะไฟล์เอกสาร PDF และรูปภาพ PNG เท่านั้น</p>
              <ul style="font-size: 0.82rem; margin-top: 0.3rem;">
                <li><strong>กลุ่ม Valid A:</strong> สุ่มเทส <code>resume.pdf</code> ➔ อัปโหลดสำเร็จ</li>
                <li><strong>กลุ่ม Valid B:</strong> สุ่มเทส <code>photo.png</code> ➔ อัปโหลดสำเร็จ</li>
                <li><strong>กลุ่ม Invalid C:</strong> สุ่มเทส <code>video.mp4</code> ➔ ระบบปฏิเสธ</li>
                <li><strong>กลุ่ม Invalid D:</strong> สุ่มเทส <code>script.exe</code> ➔ ระบบปฏิเสธ</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Technique 3: Decision Table -->
      <div class="technique-box" onclick="toggleCardLang(this)">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="technique-header">
          <div class="technique-title">
            <span>📋 3. Decision Table Testing (Cause-Effect Matrix)</span>
          </div>
          <span class="card-tag tag-purple">Input Type: Complex Multi-Condition Combinations</span>
        </div>
        <div class="lang-en">
          <p class="principle-text">
            <strong>Fundamental Principle:</strong> Complex software frequently has rules where multiple conditions combine to trigger different system actions. Human testers easily miss edge combinations (e.g. what happens when Condition 1 is True, Condition 2 is False, but Condition 3 is True?). A Decision Table systematically lists all boolean permutations (<code>2^n</code> rules) to ensure <strong>100% logical branch coverage</strong>.
          </p>
          <div class="scenario-badge">📌 When to use this technique?</div>
          <p style="font-size: 0.88rem; color: #cbd5e1;">
            Use for business logic involving discount engines, loan approvals, authentication authorization rules, or insurance claim calculations.
          </p>
          <div class="table-wrapper" style="margin: 0.75rem 0 0 0;">
            <table>
              <thead>
                <tr>
                  <th>Conditions & Actions</th>
                  <th>Rule 1 (VIP + Promo)</th>
                  <th>Rule 2 (VIP Only)</th>
                  <th>Rule 3 (Promo Only)</th>
                  <th>Rule 4 (Standard User)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>Condition: Is VIP Member?</strong></td>
                  <td><span style="color: #34d399;">YES (T)</span></td>
                  <td><span style="color: #34d399;">YES (T)</span></td>
                  <td><span style="color: #fb7185;">NO (F)</span></td>
                  <td><span style="color: #fb7185;">NO (F)</span></td>
                </tr>
                <tr>
                  <td><strong>Condition: Valid Promo Code?</strong></td>
                  <td><span style="color: #34d399;">YES (T)</span></td>
                  <td><span style="color: #fb7185;">NO (F)</span></td>
                  <td><span style="color: #34d399;">YES (T)</span></td>
                  <td><span style="color: #fb7185;">NO (F)</span></td>
                </tr>
                <tr>
                  <td><strong>Condition: Order &gt; 1,000 THB?</strong></td>
                  <td><span style="color: #34d399;">YES (T)</span></td>
                  <td><span style="color: #34d399;">YES (T)</span></td>
                  <td><span style="color: #34d399;">YES (T)</span></td>
                  <td><span style="color: #fb7185;">NO (F)</span></td>
                </tr>
                <tr style="background: rgba(56, 189, 248, 0.05);">
                  <td><strong>Action: Applied Discount</strong></td>
                  <td><strong style="color: #38bdf8;">25% Discount</strong></td>
                  <td><strong style="color: #38bdf8;">15% Discount</strong></td>
                  <td><strong style="color: #38bdf8;">10% Discount</strong></td>
                  <td><strong style="color: #94a3b8;">0% (Full Price)</strong></td>
                </tr>
                <tr style="background: rgba(56, 189, 248, 0.05);">
                  <td><strong>Action: Free Shipping?</strong></td>
                  <td><strong style="color: #34d399;">YES</strong></td>
                  <td><strong style="color: #34d399;">YES</strong></td>
                  <td><strong style="color: #fb7185;">NO (+50 THB)</strong></td>
                  <td><strong style="color: #fb7185;">NO (+50 THB)</strong></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div class="lang-th">
          <p class="principle-text">
            <strong>หลักการสำคัญ:</strong> แก้ปัญหาเวลาที่ระบบมี <strong>หลายเงื่อนไข (Multiple Conditions) มาผูกรวมกัน</strong> เพื่อสร้าง Action ต่างๆ ซึ่งมนุษย์มักจะคิดเคสตกหล่น ตารางนี้จะกางทุกความเป็นไปได้ทางตรรกะ ($2^n$ กฎ) ออกมาเป็นตาราง เพื่อให้มั่นใจว่าครอบคลุม Branch การทำงาน 100%
          </p>
          <div class="scenario-badge">📌 ควรเลือกใช้ในสถานการณ์ไหน?</div>
          <p style="font-size: 0.88rem; color: #cbd5e1;">
            ใช้กับระบบคำนวณโปรโมชันลดราคา, การอนุมัติวงเงินสินเชื่อ, การคำนวณเบี้ยประกัน, หรือเงื่อนไขสิทธิ์การใช้งาน
          </p>
          <div class="table-wrapper" style="margin: 0.75rem 0 0 0;">
            <table>
              <thead>
                <tr>
                  <th>เงื่อนไข และ ผลลัพธ์</th>
                  <th>กฎข้อ 1 (VIP + โค้ด)</th>
                  <th>กฎข้อ 2 (VIP อย่างเดียว)</th>
                  <th>กฎข้อ 3 (มีโค้ดอย่างเดียว)</th>
                  <th>กฎข้อ 4 (ลูกค้าทั่วไป)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><strong>เงื่อนไข: เป็นสมาชิก VIP?</strong></td>
                  <td><span style="color: #34d399;">ใช่ (True)</span></td>
                  <td><span style="color: #34d399;">ใช่ (True)</span></td>
                  <td><span style="color: #fb7185;">ไม่ใช่ (False)</span></td>
                  <td><span style="color: #fb7185;">ไม่ใช่ (False)</span></td>
                </tr>
                <tr>
                  <td><strong>เงื่อนไข: มีโค้ดโปรโมชัน?</strong></td>
                  <td><span style="color: #34d399;">ใช่ (True)</span></td>
                  <td><span style="color: #fb7185;">ไม่ใช่ (False)</span></td>
                  <td><span style="color: #34d399;">ใช่ (True)</span></td>
                  <td><span style="color: #fb7185;">ไม่ใช่ (False)</span></td>
                </tr>
                <tr>
                  <td><strong>เงื่อนไข: ยอดสั่งซื้อ &gt; 1,000 บาท?</strong></td>
                  <td><span style="color: #34d399;">ใช่ (True)</span></td>
                  <td><span style="color: #34d399;">ใช่ (True)</span></td>
                  <td><span style="color: #34d399;">ใช่ (True)</span></td>
                  <td><span style="color: #fb7185;">ไม่ใช่ (False)</span></td>
                </tr>
                <tr style="background: rgba(56, 189, 248, 0.05);">
                  <td><strong>ผลลัพธ์: ส่วนลดที่ได้รับ</strong></td>
                  <td><strong style="color: #38bdf8;">ลด 25%</strong></td>
                  <td><strong style="color: #38bdf8;">ลด 15%</strong></td>
                  <td><strong style="color: #38bdf8;">ลด 10%</strong></td>
                  <td><strong style="color: #94a3b8;">0% (ราคาเต็ม)</strong></td>
                </tr>
                <tr style="background: rgba(56, 189, 248, 0.05);">
                  <td><strong>ผลลัพธ์: ได้ส่งฟรีไหม?</strong></td>
                  <td><strong style="color: #34d399;">ส่งฟรี</strong></td>
                  <td><strong style="color: #34d399;">ส่งฟรี</strong></td>
                  <td><strong style="color: #fb7185;">ไม่ฟรี (+50 บาท)</strong></td>
                  <td><strong style="color: #fb7185;">ไม่ฟรี (+50 บาท)</strong></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>

      <!-- Technique 4: State Transition -->
      <div class="technique-box" onclick="toggleCardLang(this)">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="technique-header">
          <div class="technique-title">
            <span>🔄 4. State Transition Testing</span>
          </div>
          <span class="card-tag tag-amber">Input Type: Finite State Machines / Sequential Lifecycles</span>
        </div>
        <div class="lang-en">
          <p class="principle-text">
            <strong>Fundamental Principle:</strong> A system can exist in different "States" (e.g., Draft, Pending, Paid, Shipped). An event/input triggers a "Transition" from one state to another. This technique tests <strong>both valid transitions AND invalid/illegal transitions</strong> (e.g. attempting to ship an order that hasn't been paid for yet).
          </p>
          <div class="scenario-badge">📌 When to use this technique?</div>
          <p style="font-size: 0.88rem; color: #cbd5e1;">
            Use for ATM machines, E-commerce order tracking, hotel booking lifecycles, account lockouts (3 failed login attempts), and game character states.
          </p>
          <div class="example-grid">
            <div>
              <strong style="color: #38bdf8;">🏧 Scenario: ATM Card Security State Machine</strong>
              <ul style="font-size: 0.82rem; margin-top: 0.4rem;">
                <li><strong>State 1 (Idle) ➔ Insert Card:</strong> Transitions to <code>PIN Entry</code> state.</li>
                <li><strong>State 2 (PIN Entry) ➔ Correct PIN:</strong> Transitions to <code>Account Menu</code> state.</li>
                <li><strong>State 2 ➔ 1st Wrong PIN:</strong> Stays in <code>PIN Entry (Attempt: 1/3)</code>.</li>
                <li><strong>State 2 ➔ 3rd Wrong PIN:</strong> Transitions to <code>Card Confiscated / Account Locked</code> state.</li>
              </ul>
            </div>
            <div>
              <strong style="color: #34d399;">📦 Scenario: E-Commerce Order Lifecycle</strong>
              <ul style="font-size: 0.82rem; margin-top: 0.4rem;">
                <li><strong>Valid Path:</strong> <code>Created ➔ Paid ➔ Packed ➔ Shipped ➔ Delivered</code>.</li>
                <li><strong>Valid Cancel:</strong> <code>Paid ➔ Cancelled ➔ Refund Initiated</code>.</li>
                <li><strong>Illegal Transition 1:</strong> <code>Created ➔ Shipped</code> (Must block without payment).</li>
                <li><strong>Illegal Transition 2:</strong> <code>Delivered ➔ Cancelled</code> (Must reject, force Return policy).</li>
              </ul>
            </div>
          </div>
        </div>
        <div class="lang-th">
          <p class="principle-text">
            <strong>หลักการสำคัญ:</strong> ซอฟต์แวร์ทำงานตาม <strong>สถานะ (States)</strong> โดยมี Event เข้ามากระตุ้นให้เกิดการเปลี่ยนสถานะ เทคนิคนี้ใช้เทสทั้ง <strong>การเปลี่ยนสถานะที่ถูกต้อง (Valid)</strong> และ <strong>การดักจับการเปลี่ยนสถานะที่ผิดกฎ (Invalid/Illegal Transition)</strong> เช่น พยายามกดส่งของทั้งๆ ที่ยังไม่ได้จ่ายเงิน
          </p>
          <div class="scenario-badge">📌 ควรเลือกใช้ในสถานการณ์ไหน?</div>
          <p style="font-size: 0.88rem; color: #cbd5e1;">
            ใช้กับตู้ ATM, วงจรคำสั่งซื้อสินค้า, วงจรการจองโรงแรม, ระบบล็อกอิน (ใส่รหัสผิด 3 ครั้งแล้วบล็อก)
          </p>
          <div class="example-grid">
            <div>
              <strong style="color: #38bdf8;">🏧 ตัวอย่าง: วงจรความปลอดภัยตู้ ATM</strong>
              <ul style="font-size: 0.82rem; margin-top: 0.4rem;">
                <li><strong>สถานะ 1 (ว่าง) ➔ เสียบบัตร:</strong> เปลี่ยนไปสู่สถานะ <code>ใส่รหัส PIN</code></li>
                <li><strong>สถานะ 2 (ใส่ PIN) ➔ รหัสถูก:</strong> เปลี่ยนไปสู่สถานะ <code>เมนูบัญชีหลัก</code></li>
                <li><strong>สถานะ 2 ➔ รหัสผิดครั้งที่ 1:</strong> อยู่ที่สถานะ <code>ใส่ PIN ซ้ำ (ครั้งที่ 1/3)</code></li>
                <li><strong>สถานะ 2 ➔ รหัสผิดครบ 3 ครั้ง:</strong> เปลี่ยนไปสู่สถานะ <code>ยึดบัตร / ล็อกบัญชี</code> ทันที</li>
              </ul>
            </div>
            <div>
              <strong style="color: #34d399;">📦 ตัวอย่าง: วงจรออเดอร์ E-Commerce</strong>
              <ul style="font-size: 0.82rem; margin-top: 0.4rem;">
                <li><strong>เส้นทางปกติ:</strong> <code>สร้างออเดอร์ ➔ จ่ายเงินแล้ว ➔ แพ็กของ ➔ จัดส่ง ➔ ส่งมอบสำเร็จ</code></li>
                <li><strong>การยกเลิกปกติ:</strong> <code>จ่ายเงินแล้ว ➔ ขอยกเลิก ➔ เริ่มกระบวนการคืนเงิน</code></li>
                <li><strong>เปลี่ยนสถานะผิดกฎ 1:</strong> <code>สร้างออเดอร์ ➔ จัดส่งทันที</code> (ระบบต้องบล็อก เพราะยังไม่จ่ายเงิน!)</li>
                <li><strong>เปลี่ยนสถานะผิดกฎ 2:</strong> <code>ส่งมอบสำเร็จ ➔ ขอยกเลิกออเดอร์</code> (ระบบต้องบล็อก และบังคับให้ไปเปิดเคลมคืนของแทน)</li>
              </ul>
            </div>
          </div>
        </div>
      </div>

      <!-- Technique 5: Use Case / E2E -->
      <div class="technique-box" onclick="toggleCardLang(this)">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="technique-header">
          <div class="technique-title">
            <span>🗺️ 5. Use Case Testing & User Journey Testing</span>
          </div>
          <span class="card-tag tag-indigo">Input Type: End-to-End Persona Workflows</span>
        </div>
        <div class="lang-en">
          <p class="principle-text">
            <strong>Fundamental Principle:</strong> Validating that individual buttons work is insufficient. Use Case testing models the software from the perspective of an actual user persona achieving a real business goal across multiple connected web pages, APIs, and databases.
          </p>
          <div class="scenario-badge">📌 When to use this technique?</div>
          <p style="font-size: 0.88rem; color: #cbd5e1;">
            Use during System Integration Testing (SIT) and User Acceptance Testing (UAT) to validate core end-to-end commercial workflows.
          </p>
          <div style="background: #090d16; border: 1px solid #1e293b; border-radius: 8px; padding: 1rem 1.25rem; margin-top: 0.75rem;">
            <strong style="color: #38bdf8;">🏨 Full User Journey Example (Hotel Booking):</strong>
            <p style="font-size: 0.85rem; color: #cbd5e1; margin-top: 0.3rem;">
              <code>Step 1 (Search):</code> Guest inputs "Bangkok", 2 Guests, Aug 25-27 ➔ <code>Step 2 (Filter):</code> Applies "4-Star & Free Cancellation" filter ➔ <code>Step 3 (Room Select):</code> Selects Deluxe King Room ➔ <code>Step 4 (Checkout):</code> Fills guest info, inputs promo code "AGODA10" ➔ <code>Step 5 (Payment):</code> Authenticates via Visa 3D Secure ➔ <code>Step 6 (Fulfillment):</code> Receives booking PDF confirmation email + Database creates booking record with status <code>CONFIRMED</code>.
            </p>
          </div>
        </div>
        <div class="lang-th">
          <p class="principle-text">
            <strong>หลักการสำคัญ:</strong> การเทสแค่ปุ่มใดปุ่มหนึ่งทำงานได้ไม่เพียงพอ Use Case Testing จะจำลองพฤติกรรมจากมุมมองของ<strong>ผู้ใช้งานจริง (Persona) ที่ต้องการบรรลุเป้าหมายทางธุรกิจ</strong> โดยทดสอบการเชื่อมโยงข้ามหน้าเว็บ ข้าม API และข้ามฐานข้อมูลตั้งแต่ต้นจนจบ
          </p>
          <div class="scenario-badge">📌 ควรเลือกใช้ในสถานการณ์ไหน?</div>
          <p style="font-size: 0.88rem; color: #cbd5e1;">
            ใช้ในช่วง System Integration Testing (SIT) และ UAT เพื่อยืนยันว่า Flow การซื้อขายหลักทำงานได้ราบรื่น
          </p>
          <div style="background: #090d16; border: 1px solid #1e293b; border-radius: 8px; padding: 1rem 1.25rem; margin-top: 0.75rem;">
            <strong style="color: #38bdf8;">🏨 ตัวอย่าง E2E Journey เต็มรูปแบบ (การจองโรงแรม):</strong>
            <p style="font-size: 0.85rem; color: #cbd5e1; margin-top: 0.3rem;">
              <code>ขั้นที่ 1 (ค้นหา):</code> ลูกค้าค้นหา "กรุงเทพฯ" 2 คน วันที่ 25-27 ส.ค. ➔ <code>ขั้นที่ 2 (กรอง):</code> เลือกโรงแรม 4 ดาว + ยกเลิกฟรี ➔ <code>ขั้นที่ 3 (เลือกห้อง):</code> เลือกห้อง Deluxe ➔ <code>ขั้นที่ 4 (Checkout):</code> กรอกข้อมูลและใส่โค้ดลดราคา ➔ <code>ขั้นที่ 5 (จ่ายเงิน):</code> ยืนยัน OTP บัตรเครดิต ➔ <code>ขั้นที่ 6 (รับของ):</code> ได้รับอีเมล Voucher ยืนยันการจอง + ฐานข้อมูลบันทึกสถานะ <code>CONFIRMED</code>
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 6: Test Matrix & Artifacts -->
    <section id="sec-matrix">
      <div class="section-header">
        <span class="section-num">PART 06</span>
        <h2>Test Matrix & Test Documentation Formats</h2>
      </div>
      <p>A <strong>Test Matrix</strong> is a structured 2-dimensional grid used by QA engineers to map variables, environments, test scenarios, or requirements to ensure comprehensive coverage without missing combinations.</p>

      <!-- Matrix 1: RTM -->
      <div class="technique-box" onclick="toggleCardLang(this)">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="technique-header">
          <div class="technique-title">
            <span>🗺️ 1. RTM (Requirements Traceability Matrix)</span>
          </div>
          <span class="card-tag tag-blue">Type: Bi-Directional Coverage & Change Tracking</span>
        </div>
        <div class="lang-en">
          <p class="principle-text">
            <strong>Fundamental Principle:</strong> In complex software projects with hundreds of user stories, manual testers frequently forget to write test cases for certain edge requirements. RTM establishes a <strong>bi-directional traceability link</strong> between every single Business Requirement (from PRD / Jira Epic), its corresponding Test Cases, and any Defects logged during execution. If a requirement changes or is deleted, RTM immediately highlights exactly which test cases need to be updated.
          </p>
          <div class="scenario-badge">📌 When to use RTM? (Exact Situations)</div>
          <p style="font-size: 0.88rem; color: #cbd5e1;">
            • <strong>During Test Planning & Design:</strong> To verify that 100% of acceptance criteria have at least one valid and one negative test case.<br>
            • <strong>During Release Quality Audits / ISTQB Compliance:</strong> To prove to Product Owners and auditors that no scope item was shipped untested.<br>
            • <strong>During Scope Changes (Change Requests):</strong> When the business modifies a payment rule mid-sprint, RTM tells you in 10 seconds which 5 test cases are affected.
          </p>
        </div>
        <div class="lang-th">
          <p class="principle-text">
            <strong>หลักการสำคัญ:</strong> ป้องกันไม่ให้ QA ลืมเขียนเคสเทสสำหรับ Requirement บางข้อ RTM จะสร้าง<strong>สะพานเชื่อมโยงแบบ 2 ทิศทาง</strong> ระหว่าง Business Requirement (จาก PRD/Jira) ➔ Test Case ➔ Defect/Bug หากมีการแก้ไขสเปกระหว่างทาง RTM จะบอกได้ทันทีใน 10 วินาทีว่ามี Test Case ตัวไหนบ้างที่ต้องแก้ตาม
          </p>
          <div class="scenario-badge">📌 สถานการณ์ที่ต้องใช้จริง:</div>
          <p style="font-size: 0.88rem; color: #cbd5e1;">
            • <strong>ช่วงวางแผนและออกแบบการเทส:</strong> ตรวจสอบว่าทุก User Story มีเคสครอบคลุมครบ 100%<br>
            • <strong>ช่วงตรวจรับงาน / Audit:</strong> แสดงหลักฐานให้ผู้บริหารดูว่าไม่มีฟีเจอร์ไหนหลุดรอดการเทส<br>
            • <strong>เมื่อเกิดการเปลี่ยนสเปก (Change Request):</strong> เช็กผลกระทบได้อย่างรวดเร็ว
          </p>
        </div>
      </div>

      <!-- Matrix 2: Compatibility Matrix -->
      <div class="technique-box" onclick="toggleCardLang(this)">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="technique-header">
          <div class="technique-title">
            <span>🌐 2. Cross-Browser & Device Compatibility Matrix</span>
          </div>
          <span class="card-tag tag-emerald">Type: Hardware, OS & Rendering Engine Matrix</span>
        </div>
        <div class="lang-en">
          <p class="principle-text">
            <strong>Fundamental Principle:</strong> Web and mobile apps render through different browser engines (Blink in Chrome, WebKit in Safari, Gecko in Firefox). A layout that looks fine on Chrome can freeze on iOS Safari. A Compatibility Matrix maps critical journeys against device market share to guarantee safety across 98%+ of actual traffic without testing every phone in the world.
          </p>
          <div class="scenario-badge">📌 When to use Compatibility Matrix?</div>
          <p style="font-size: 0.88rem; color: #cbd5e1;">
            • <strong>Before Major UI Releases:</strong> To divide manual testing and Playwright grid execution.<br>
            • <strong>When Analytics Shows High Drop-offs on Specific Devices:</strong> E.g. Safari conversion drops 30%.
          </p>
        </div>
        <div class="lang-th">
          <p class="principle-text">
            <strong>หลักการสำคัญ:</strong> เบราว์เซอร์แต่ละตัวใช้เอนจินประมวลผลต่างกัน สิ่งที่แสดงผลสวยงามบน Chrome อาจจะพังหรือค้างบน iOS Safari เมทริกซ์นี้จะช่วยแมป OS และ Browser ตามสัดส่วน Traffic จริงของลูกค้า เพื่อให้ทดสอบครอบคลุมผู้ใช้กว่า 98% โดยไม่ต้องซื้อโทรศัพท์ทุกรุ่นบนโลกมาเทส
          </p>
          <div class="scenario-badge">📌 สถานการณ์ที่ต้องใช้จริง:</div>
          <p style="font-size: 0.88rem; color: #cbd5e1;">
            • <strong>ก่อน Release ฟีเจอร์หน้าบ้าน:</strong> เพื่อกระจายคิวรัน Playwright Grid ข้ามแพลตฟอร์ม<br>
            • <strong>เมื่อตัวเลขอัตราการซื้อตกบนบางอุปกรณ์:</strong> เจาะเทสเฉพาะเครื่องที่มีปัญหาได้ทันท่วงที
          </p>
        </div>
      </div>

      <!-- Matrix 3: RBAC Matrix -->
      <div class="technique-box" onclick="toggleCardLang(this)">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="technique-header">
          <div class="technique-title">
            <span>🛡️ 3. Role & Permission Matrix (RBAC Security Matrix)</span>
          </div>
          <span class="card-tag tag-rose">Type: Security & Authorization</span>
        </div>
        <div class="lang-en">
          <p class="principle-text">
            <strong>Fundamental Principle:</strong> Validates that authorized roles have access (Positive Testing) and that unauthorized roles are strictly blocked with <code>HTTP 403 Forbidden</code> (Negative/Security Testing), preventing privilege escalation and IDOR attacks.
          </p>
          <div class="scenario-badge">📌 When to use RBAC Matrix?</div>
          <p style="font-size: 0.88rem; color: #cbd5e1;">
            • <strong>Multi-Tenant Portals & Backoffices:</strong> Such as iNT Connect or Admin Dashboard.<br>
            • <strong>API Security:</strong> Verifying token permission checks on sensitive DELETE/PUT endpoints.
          </p>
        </div>
        <div class="lang-th">
          <p class="principle-text">
            <strong>หลักการสำคัญ:</strong> ตรวจสอบสิทธิ์การเข้าถึงระบบ โดยเช็กว่า Role ที่ได้รับอนุญาตสามารถเข้าใช้งานได้ (Positive) และ Role ที่ไม่มีสิทธิ์จะต้องถูกบล็อกด้วยรหัส <code>403 Forbidden</code> เสมอ (Security Negative Test) เพื่อป้องกันช่องโหว่การแอบเข้าถึงข้อมูลลับ
          </p>
          <div class="scenario-badge">📌 สถานการณ์ที่ต้องใช้จริง:</div>
          <p style="font-size: 0.88rem; color: #cbd5e1;">
            • <strong>ระบบพอร์ทัลองค์กรที่มีผู้ใช้หลายระดับ:</strong> เช่น ระบบ iNT Connect หรือระบบหลังบ้านแอดมิน<br>
            • <strong>การเทสความปลอดภัยของ API:</strong> ยืนยันว่าการยิง API ลบหรือแก้ไขข้อมูลมีการตรวจเช็ก Token เสมอ
          </p>
        </div>
      </div>
    </section>

    <!-- SECTION 7: Testing Types & Scenarios -->
    <section id="sec-types-deep">
      <div class="section-header">
        <span class="section-num">PART 07</span>
        <h2>Comprehensive Testing Types: Principles & Real Situations</h2>
      </div>

      <div class="grid-2">
        <!-- Smoke vs Sanity -->
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-emerald">Testing Types</span>
          <div class="lang-en">
            <h3>Smoke Testing vs. Sanity Testing</h3>
            <ul style="font-size: 0.88rem;">
              <li><strong>Smoke Testing (Build Acceptance Test):</strong>
                <br><span style="color: var(--text-dim);">When:</span> Executed immediately on a new build from CI/CD pipeline.
                <br><span style="color: var(--text-dim);">Principle:</span> <em>Wide & Shallow.</em> Verifies if critical core components work so QA doesn't waste time testing a broken build.
                <br><span style="color: #38bdf8;">Scenario:</span> Daily build deployed at 09:00. QA triggers automated 5-min Smoke suite checking Login, Search, and DB connection. If Smoke fails, the build is instantly rejected.
              </li>
              <li style="margin-top: 0.85rem;"><strong>Sanity Testing (Quick Verification):</strong>
                <br><span style="color: var(--text-dim);">When:</span> Executed after a specific minor bug fix or patch build.
                <br><span style="color: var(--text-dim);">Principle:</span> <em>Narrow & Deep.</em> Verifies that the specific bug fix works and related module is intact.
                <br><span style="color: #38bdf8;">Scenario:</span> Dev commits hotfix for currency calculation on checkout. QA tests only checkout currency without re-running entire system test.
              </li>
            </ul>
          </div>
          <div class="lang-th">
            <h3 style="color: #34d399;">Smoke Testing vs. Sanity Testing</h3>
            <ul style="font-size: 0.88rem;">
              <li><strong>Smoke Testing (เทสความพร้อมเบื้องต้นของ Build):</strong>
                <br><span style="color: var(--text-dim);">เทสเมื่อไหร่:</span> รันทันทีเมื่อมี Build ใหม่ออกมาจาก CI/CD
                <br><span style="color: var(--text-dim);">หลักการ:</span> <em>กว้างแต่ตื้น (Wide & Shallow)</em> เช็กแค่ว่าฟังก์ชันหลัก (Login, Search, DB) ใช้งานได้ เพื่อไม่ให้ QA เสียเวลาเทสบน Build ที่พังยับเยิน
                <br><span style="color: #38bdf8;">ตัวอย่าง:</span> รันสคริปต์ 5 นาทีตรวจระบบหลัก ถ้าไม่ผ่าน ตีกลับให้ Dev ทันที
              </li>
              <li style="margin-top: 0.85rem;"><strong>Sanity Testing (เทสเจาะเฉพาะจุดที่แก้บั๊ก):</strong>
                <br><span style="color: var(--text-dim);">เทสเมื่อไหร่:</span> รันหลังจาก Dev แก้บั๊กเฉพาะจุดเสร็จ
                <br><span style="color: var(--text-dim);">หลักการ:</span> <em>แคบแต่ลึก (Narrow & Deep)</em> เช็กเจาะลึกเฉพาะโมดูลที่เพิ่งแก้บั๊กไป
                <br><span style="color: #38bdf8;">ตัวอย่าง:</span> Dev แก้บั๊กคำนวณอัตราแลกเปลี่ยนเงินในหน้าชำระเงิน QA ก็จะเทสเจาะเฉพาะจุดคำนวณเงินโดยไม่ต้องไปรันเทสระบบอื่น
              </li>
            </ul>
          </div>
        </div>

        <!-- Regression vs Retesting -->
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-indigo">Testing Types</span>
          <div class="lang-en">
            <h3>Retesting vs. Regression Testing</h3>
            <ul style="font-size: 0.88rem;">
              <li><strong>Retesting (Defect Verification):</strong>
                <br><span style="color: var(--text-dim);">When:</span> Whenever a logged bug moves from <code>FIXED</code> to <code>RE-TESTING</code>.
                <br><span style="color: var(--text-dim);">Principle:</span> Testing the <strong>exact same failed test case with the same test data</strong> to confirm the defect is resolved.
              </li>
              <li style="margin-top: 0.85rem;"><strong>Regression Testing (Side-Effect Hunting):</strong>
                <br><span style="color: var(--text-dim);">When:</span> Before every production release or sprint release.
                <br><span style="color: var(--text-dim);">Principle:</span> Re-running tests on <strong>unmodified surrounding features</strong> to ensure new code commits did not introduce accidental side-effects.
                <br><span style="color: #38bdf8;">Scenario:</span> Dev refactors user profile. Regression ensures checkout and password reset modules were not broken by shared model changes.
              </li>
            </ul>
          </div>
          <div class="lang-th">
            <h3 style="color: #818cf8;">Retesting (เทสซ้ำจุดเดิม) vs. Regression Testing (เทสกันระบบอื่นพัง)</h3>
            <ul style="font-size: 0.88rem;">
              <li><strong>Retesting (ตรวจยืนยันการแก้บั๊ก):</strong>
                <br><span style="color: var(--text-dim);">เทสเมื่อไหร่:</span> เมื่อบั๊กใน Jira ถูกแก้เสร็จและส่งกลับมาให้ QA
                <br><span style="color: var(--text-dim);">หลักการ:</span> รันซ้ำ<strong>ด้วย Test Case เดิมและข้อมูลเดิมเป๊ะๆ</strong> เพื่อดูว่าบั๊กหายไปจริงไหม
              </li>
              <li style="margin-top: 0.85rem;"><strong>Regression Testing (เทสรอบข้างเพื่อดักผลกระทบข้างเคียง):</strong>
                <br><span style="color: var(--text-dim);">เทสเมื่อไหร่:</span> ก่อนปล่อยงานขึ้น Production ทุกครั้ง
                <br><span style="color: var(--text-dim);">หลักการ:</span> นำเคสของ<strong>ระบบรอบข้างที่ไม่ได้แตะต้องมารันซ้ำ</strong> เพื่อให้มั่นใจว่าโค้ดใหม่ที่ใส่เข้าไปไม่ไปกระทบให้ฟีเจอร์เดิมพัง
                <br><span style="color: #38bdf8;">ตัวอย่าง:</span> Dev แก้โค้ดหน้า Profile เราต้องรัน Regression เช็กระบบ Login และ Checkout ว่าไม่พังไปด้วย
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 8: White-Box vs. Gray-Box vs. Black-Box -->
    <section id="sec-whitebox">
      <div class="section-header">
        <span class="section-num">PART 08</span>
        <h2>Black-Box vs. White-Box vs. Gray-Box Testing</h2>
      </div>

      <div class="grid-3">
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-blue">External Behavior</span>
          <div class="lang-en">
            <h3>Black-Box Testing</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">Testing software functionality without looking at internal code structure. Focuses purely on inputs and outputs.</p>
            <div style="font-size: 0.78rem; color: var(--primary); font-family: 'JetBrains Mono'; margin-top: 0.5rem;">Used in: UAT, System Test, Functional E2E.</div>
          </div>
          <div class="lang-th">
            <h3 style="color: #38bdf8;">Black-Box (กล่องดำ)</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">เทสโดยไม่สนใจโครงสร้างโค้ดภายใน ดูเฉพาะ Input ที่ป้อนเข้าไป และ Output ที่ตอบกลับมา</p>
            <div style="font-size: 0.78rem; color: var(--primary); font-family: 'JetBrains Mono'; margin-top: 0.5rem;">ใช้ใน: UAT, System Test, Manual E2E</div>
          </div>
        </div>

        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-emerald">Internal Code Structure</span>
          <div class="lang-en">
            <h3>White-Box Testing</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">Testing internal code logic, branch coverage, loop execution, and statement execution with full visibility of source code.</p>
            <div style="font-size: 0.78rem; color: var(--accent-emerald); font-family: 'JetBrains Mono'; margin-top: 0.5rem;">Used in: Unit Testing (Jest/PyTest), Code Reviews.</div>
          </div>
          <div class="lang-th">
            <h3 style="color: #34d399;">White-Box (กล่องขาว/กล่องใส)</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">เทสโดยมองเห็น Source Code ทั้งหมด ตรวจสอบความถูกต้องของตรรกะ ลูป และ Branch ของโค้ด</p>
            <div style="font-size: 0.78rem; color: var(--accent-emerald); font-family: 'JetBrains Mono'; margin-top: 0.5rem;">ใช้ใน: Unit Test (PyTest/Jest), Code Review</div>
          </div>
        </div>

        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-purple">Hybrid & API Level</span>
          <div class="lang-en">
            <h3>Gray-Box Testing</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">Testing with partial knowledge of internal data structures, DB schemas, or API contracts without full access to source code.</p>
            <div style="font-size: 0.78rem; color: var(--accent-purple); font-family: 'JetBrains Mono'; margin-top: 0.5rem;">Used in: API Testing with Postman, DB Query Checks.</div>
          </div>
          <div class="lang-th">
            <h3 style="color: #c084fc;">Gray-Box (กล่องเทา)</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">เทสแบบรู้โครงสร้างบางส่วน เช่น รู้หน้าตา Database Schema หรือเข้าใจ API Contract แต่ไม่ได้เห็นโค้ดทั้งหมด</p>
            <div style="font-size: 0.78rem; color: var(--accent-purple); font-family: 'JetBrains Mono'; margin-top: 0.5rem;">ใช้ใน: API Testing ด้วย Postman, การเขียน SQL ตรวจ DB</div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 9: STLC, Bug Lifecycle & Bug Report Anatomy -->
    <section id="sec-lifecycle">
      <div class="section-header">
        <span class="section-num">PART 09</span>
        <h2>Software Testing Life Cycle (STLC) & Professional Bug Report Anatomy</h2>
      </div>

      <div class="technique-box" onclick="toggleCardLang(this)">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="technique-header">
          <div class="technique-title">
            <span>🐞 Anatomy of a Professional Bug Report (Jira Standard)</span>
          </div>
          <span class="card-tag tag-rose">Senior QA Quality Benchmark</span>
        </div>
        <div class="lang-en">
          <p class="principle-text">
            <strong>Fundamental Principle:</strong> A bug report is the primary bridge of communication between QA and Developers. A poorly written bug report wastes hours guessing the issue. A professional Bug Report must be <strong>Clear, Reproducible, and Packed with Empirical Evidence</strong> so any developer can replicate and fix the issue within minutes.
          </p>
          <div class="example-grid">
            <div style="border-left: 3px solid #fb7185;">
              <strong style="color: #fb7185;">❌ Bad Bug Report (Amateur):</strong>
              <p style="font-size: 0.82rem; color: #cbd5e1; margin-top: 0.4rem;">
                <strong>Summary:</strong> <em>"Hotel discount button is broken"</em><br>
                <strong>Description:</strong> <em>"I clicked discount and it didn't give me the right price. Please fix asap."</em>
              </p>
              <div style="font-size: 0.78rem; color: #fb7185; font-family: 'JetBrains Mono'; margin-top: 0.5rem;">
                ⚠️ Flaws: No environment, no user role, no steps, no expected vs actual numbers, no logs.
              </div>
            </div>

            <div style="border-left: 3px solid #34d399;">
              <strong style="color: #34d399;">✅ Good Bug Report (Professional):</strong>
              <p style="font-size: 0.82rem; color: #cbd5e1; margin-top: 0.4rem;">
                <strong>Summary:</strong> <code>[Checkout] [Promo] 15% VIP discount applies before VAT calculation on Mobile Safari</code><br>
                <strong>Environment:</strong> Staging-2 (Build v2.14.0), iOS 17.5 (iPhone 15 Mobile Safari)<br>
                <strong>Precondition:</strong> Logged in as User <code>qa_vip_gold@agoda.com</code><br>
                <strong>Steps to Reproduce:</strong><br>
                1. Search hotel in 'Bangkok' for 2 nights (Base: 2,000 THB).<br>
                2. Proceed to Checkout page.<br>
                3. Input coupon code <code>'VIP15'</code> and tap Apply.<br>
                <strong>Expected Result:</strong> Discount 15% calculated from Subtotal (300 THB) ➔ Net = 1,700 THB + 7% VAT (119 THB) = <strong>1,819 THB</strong>.<br>
                <strong>Actual Result:</strong> Discount applies on Total after VAT ➔ Net = <strong>1,840 THB</strong> (21 THB overcharge).<br>
                <strong>Attachments:</strong> Screenshot of cart, HAR network log <code>checkout_calc.har</code>, Console logs.
              </p>
            </div>
          </div>
        </div>
        <div class="lang-th">
          <p class="principle-text">
            <strong>หลักการสำคัญ:</strong> Bug Report คือสะพานเชื่อมระหว่าง QA และ Dev หากเขียนคลุมเครือ Dev จะเสียเวลาเดาและอาจปิด Ticket ทิ้ง Bug Report ที่ดีจะต้อง<strong>ชัดเจน ทำซ้ำได้เป๊ะๆ (Reproducible) และมีหลักฐานตัวเลขและ Log ครบถ้วน</strong> เพื่อให้ Dev แก้ไขได้ทันที
          </p>
          <div class="example-grid">
            <div style="border-left: 3px solid #fb7185;">
              <strong style="color: #fb7185;">❌ ตัวอย่างการเปิดบั๊กแย่ๆ (ที่เด็กจบใหม่มักทำ):</strong>
              <p style="font-size: 0.82rem; color: #cbd5e1; margin-top: 0.4rem;">
                <strong>หัวข้อ:</strong> <em>"ปุ่มส่วนลดพัง"</em><br>
                <strong>รายละเอียด:</strong> <em>"ฉันกดรับส่วนลดแล้วราคาไม่ลดตามที่ควรจะเป็น ช่วยแก้ด่วนๆ"</em>
              </p>
              <div style="font-size: 0.78rem; color: #fb7185; font-family: 'JetBrains Mono'; margin-top: 0.5rem;">
                ⚠️ ข้อเสีย: ไม่มีบอกว่าทดสอบบนเครื่องไหน, ไม่บอกขั้นตอนการกด, ไม่มีตัวเลขเปรียบเทียบ, ไม่มี Log แนบ
              </div>
            </div>

            <div style="border-left: 3px solid #34d399;">
              <strong style="color: #34d399;">✅ ตัวอย่างการเปิดบั๊กแบบมืออาชีพ (Professional Standard):</strong>
              <p style="font-size: 0.82rem; color: #cbd5e1; margin-top: 0.4rem;">
                <strong>หัวข้อ:</strong> <code>[Checkout] [Promo] ส่วนลด VIP 15% ถูกคำนวณก่อนคิดภาษีมูลค่าเพิ่มบน Mobile Safari</code><br>
                <strong>Environment:</strong> Staging-2 (Build v2.14.0), iPhone 15 บน iOS 17.5 (Mobile Safari)<br>
                <strong>Precondition:</strong> ล็อกอินด้วยบัญชีทดสอบ VIP Gold <code>qa_vip_gold@agoda.com</code><br>
                <strong>ขั้นตอนการทำซ้ำ (Steps 1-2-3):</strong><br>
                1. ค้นหาโรงแรมในกรุงเทพฯ พัก 2 คืน (ยอด 2,000 บาท)<br>
                2. ไปที่หน้า Checkout<br>
                3. กรอกโค้ด <code>'VIP15'</code> แล้วกด Apply<br>
                <strong>Expected Result:</strong> ลด 15% จากยอดก่อน VAT (300 บาท) ➔ ยอดสุทธิ 1,700 + VAT 7% (119 บาท) = <strong>1,819 บาท</strong><br>
                <strong>Actual Result:</strong> ส่วนลดดันไปคิดจากยอดรวมหลัง VAT ➔ ยอดกลายเป็น <strong>1,840 บาท (คิดเงินลูกค้าเกิน 21 บาท!)</strong><br>
                <strong>สิ่งที่แนบ:</strong> รูปแคปหน้าจอ, ไฟล์ Network HAR <code>checkout_calc.har</code>, Console Log
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 10: API & Status Codes -->
    <section id="sec-api">
      <div class="section-header">
        <span class="section-num">PART 10</span>
        <h2>API & Backend Integration Testing (Enterprise Scale)</h2>
      </div>

      <div class="card" onclick="toggleCardLang(this)">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="lang-en">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>Status Code</th>
                  <th>Meaning & Core Distinction</th>
                  <th>QA Validation Focus</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><code>200 OK</code> / <code>201 Created</code></td>
                  <td>Request succeeded. 201 indicates a new resource was created.</td>
                  <td>Verify response body schema, ID generation, latency &lt; 200ms.</td>
                </tr>
                <tr>
                  <td><code>400 Bad Request</code></td>
                  <td>Malformed payload, missing required fields, or invalid format.</td>
                  <td>Verify informative error message (e.g., <code>"email is required"</code>).</td>
                </tr>
                <tr>
                  <td><code>401 Unauthorized</code></td>
                  <td><strong>Identity Unknown:</strong> Missing, invalid, or expired JWT Token.</td>
                  <td>Test without Bearer token or with expired token.</td>
                </tr>
                <tr>
                  <td><code>403 Forbidden</code></td>
                  <td><strong>Identity Known, Access Denied:</strong> Authenticated user lacks permission.</td>
                  <td>Test customer role attempting to access admin API <code>/api/v1/admin/refund</code>.</td>
                </tr>
                <tr>
                  <td><code>404 Not Found</code></td>
                  <td>Resource or URL endpoint does not exist.</td>
                  <td>Verify querying non-existent hotel ID returns 404, not 500.</td>
                </tr>
                <tr>
                  <td><code>500 Internal Error</code></td>
                  <td>Backend crashed, uncaught exception, or DB connection lost.</td>
                  <td><strong>Critical Defect:</strong> System should gracefully handle errors with 4xx instead of 500.</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div class="lang-th">
          <div class="table-wrapper">
            <table>
              <thead>
                <tr>
                  <th>รหัส HTTP Code</th>
                  <th>ความหมาย & ข้อแตกต่างสำคัญ</th>
                  <th>จุดที่ QA ต้องโฟกัสตรวจสอบ</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><code>200 OK</code> / <code>201 Created</code></td>
                  <td>ทำงานสำเร็จ (201 หมายถึงมีการสร้างข้อมูลใหม่ลง Database เรียบร้อย)</td>
                  <td>เช็กโครงสร้าง JSON Response, ID ที่สร้างขึ้นมา, และความเร็ว Latency &lt; 200ms</td>
                </tr>
                <tr>
                  <td><code>400 Bad Request</code></td>
                  <td>Payload ส่งมาผิดรูปแบบ, ลืมกรอกฟิลด์บังคับ, หรือข้อมูลผิดประเภท</td>
                  <td>เช็กว่าระบบตอบ Error Message ที่เข้าใจง่ายกลับมา (เช่น <code>"email is required"</code>)</td>
                </tr>
                <tr>
                  <td><code>401 Unauthorized</code></td>
                  <td><strong>ไม่รู้ว่าเป็นใคร (Identity Unknown):</strong> ไม่มี Token หรือ Token หมดอายุ</td>
                  <td>ทดสอบยิง API โดยไม่ใส่ Bearer Token หรือใส่ Token ปลอม</td>
                </tr>
                <tr>
                  <td><code>403 Forbidden</code></td>
                  <td><strong>รู้ตัวตนแต่ไม่มีสิทธิ์ (Access Denied):</strong> ล็อกอินผ่านแล้ว แต่สิทธิ์ไม่ถึง</td>
                  <td>ทดสอบใช้ Role ลูกค้าทั่วไป แอบยิง API แอดมิน <code>/api/v1/admin/refund</code> ต้องติด 403</td>
                </tr>
                <tr>
                  <td><code>404 Not Found</code></td>
                  <td>ไม่พบ Endpoint หรือ ID ข้อมูลนี้ในระบบ</td>
                  <td>ทดสอบยิงเรียก ID โรงแรมที่ไม่มีอยู่จริง ระบบต้องตอบ 404 ไม่ใช่พังเป็น 500</td>
                </tr>
                <tr>
                  <td><code>500 Internal Error</code></td>
                  <td>เซิร์ฟเวอร์หลังบ้านพัง, เกิด Uncaught Exception, หรือฐานข้อมูลตัดการเชื่อมต่อ</td>
                  <td><strong>บั๊กร้ายแรง:</strong> ระบบที่ดีต้องดักจับ Error และแปลงเป็น 4xx ไม่ควรปล่อยให้หลุดเป็น 500</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 11: Automation & Architecture -->
    <section id="sec-automation">
      <div class="section-header">
        <span class="section-num">PART 11</span>
        <h2>Test Automation & Scalable Architecture</h2>
      </div>

      <div class="grid-2">
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-blue">Architecture</span>
          <div class="lang-en">
            <h3>The Automation Test Pyramid (70/20/10)</h3>
            <p style="font-size: 0.88rem; color: #cbd5e1;">Why high-scale engineering squads enforce heavy API & Unit testing over UI testing:</p>
            <div style="font-family: 'JetBrains Mono'; font-size: 0.82rem; line-height: 1.8;">
              <div style="background: rgba(251, 113, 133, 0.1); border-left: 4px solid #fb7185; padding: 0.5rem 0.75rem; margin-bottom: 0.4rem;">
                ▲ <strong>10% UI E2E Tests:</strong> Slow, expensive, high maintenance. Focus only on critical user journeys (Playwright/Robot).
              </div>
              <div style="background: rgba(56, 189, 248, 0.1); border-left: 4px solid #38bdf8; padding: 0.5rem 0.75rem; margin-bottom: 0.4rem;">
                ▲▲ <strong>20% API / Service Tests:</strong> Fast, reliable, validates business logic & schema contracts (Postman/Requests).
              </div>
              <div style="background: rgba(52, 211, 153, 0.1); border-left: 4px solid #34d399; padding: 0.5rem 0.75rem;">
                ▲▲▲ <strong>70% Unit Tests:</strong> Lightning fast, cheap, tests isolated logic (Jest, PyTest).
              </div>
            </div>
          </div>
          <div class="lang-th">
            <h3 style="color: #38bdf8;">พีระมิดการทำ Automation (70 / 20 / 10)</h3>
            <p style="font-size: 0.88rem; color: #cbd5e1;">ทำไมองค์กรระดับโลกจึงเน้น Unit & API มากกว่าการเทสผ่าน UI:</p>
            <div style="font-family: 'JetBrains Mono', 'Noto Sans Thai'; font-size: 0.82rem; line-height: 1.8;">
              <div style="background: rgba(251, 113, 133, 0.1); border-left: 4px solid #fb7185; padding: 0.5rem 0.75rem; margin-bottom: 0.4rem;">
                ▲ <strong>10% UI E2E Tests:</strong> ช้า ค่าดูแลรักษาสูง เขียนเฉพาะ User Journey สำคัญจริงๆ (Playwright/Robot Framework)
              </div>
              <div style="background: rgba(56, 189, 248, 0.1); border-left: 4px solid #38bdf8; padding: 0.5rem 0.75rem; margin-bottom: 0.4rem;">
                ▲▲ <strong>20% API Tests:</strong> เร็วกว่า เสถียรกว่า ตรวจสอบ Business Logic ได้แม่นยำ (Postman/Python Requests)
              </div>
              <div style="background: rgba(52, 211, 153, 0.1); border-left: 4px solid #34d399; padding: 0.5rem 0.75rem;">
                ▲▲▲ <strong>70% Unit Tests:</strong> เร็วระดับเสี้ยววินาที เทสตรรกะแยกส่วนรายฟังก์ชัน (PyTest, Jest)
              </div>
            </div>
          </div>
        </div>

        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-amber">Best Practices</span>
          <div class="lang-en">
            <h3>How to Eliminate "Flaky Tests"</h3>
            <p style="font-size: 0.88rem; color: #cbd5e1;">A <strong>Flaky Test</strong> is an automated test that passes and fails inconsistently without code changes. How senior engineers fix them:</p>
            <ul style="font-size: 0.85rem;">
              <li><strong>Replace Static Sleeps:</strong> Never use <code>time.sleep(5)</code>. Use <strong>Explicit Waits / Auto-waiting</strong> (Playwright's built-in <code>waitForSelector</code>).</li>
              <li><strong>Robust Locator Strategy:</strong> Avoid fragile XPath indices (<code>//div[3]/span[2]</code>). Use semantic locators like <code>data-testid</code> or <code>role</code>.</li>
              <li><strong>Test Data Isolation:</strong> Generate unique test users/bookings via API fixtures for each run to avoid database collision.</li>
            </ul>
          </div>
          <div class="lang-th">
            <h3 style="color: #fbbf24;">วิธีแก้ปัญหา "Flaky Tests" (การเทสที่ไม่เสถียร เดี๋ยวผ่านเดี๋ยวพัง)</h3>
            <p style="font-size: 0.88rem; color: #cbd5e1;"><strong>Flaky Test</strong> คือสคริปต์ที่รันผ่านบ้างไม่ผ่านบ้างโดยที่โค้ดไม่ได้แก้ วิธีแก้ระดับมืออาชีพ:</p>
            <ul style="font-size: 0.85rem;">
              <li><strong>เลิกใช้ Sleep แบบคงที่:</strong> ห้ามใช้ <code>time.sleep(5)</code> เด็ดขาด ให้เปลี่ยนมาใช้ <strong>Explicit Wait / Auto-waiting</strong> ของ Playwright แทน</li>
              <li><strong>ใช้ Locator ที่แข็งแรง:</strong> หลีกเลี่ยง XPath เปราะบาง (เช่น <code>//div[3]/span</code>) ให้ใช้ <code>data-testid</code> หรือ <code>role</code> แทน</li>
              <li><strong>แยก Test Data อิสระ (Isolation):</strong> ให้สคริปต์ยิง API สร้าง User จำลองใหม่ทุกครั้งที่รัน เพื่อไม่ให้ข้อมูลใน DB ชนกันเอง</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 12: A/B Testing & Microservices -->
    <section id="sec-abtesting">
      <div class="section-header">
        <span class="section-num">PART 12</span>
        <h2>Modern Tech: A/B Testing, Feature Flags & Microservices</h2>
      </div>

      <div class="grid-2">
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-purple">Experimentation</span>
          <div class="lang-en">
            <h3>1. How to Test A/B Experiments & Feature Flags</h3>
            <ul style="font-size: 0.85rem;">
              <li><strong>Feature Flag Toggling:</strong> QA forces specific experiment variants using URL query parameters or custom HTTP headers (e.g. <code>X-Experiment-Id: 1042_B</code>).</li>
              <li><strong>Telemetry & Event Tracking:</strong> Verify that user interactions (Clicks, Checkouts, Searches) fire accurate analytics tracking events to Kafka/Data lake.</li>
              <li><strong>Zero Collision:</strong> Ensure Experiment B does not corrupt legacy booking schemas for Variant A users.</li>
            </ul>
          </div>
          <div class="lang-th">
            <h3 style="color: #c084fc;">1. วิธีการทดสอบระบบ A/B Testing & Feature Flags</h3>
            <ul style="font-size: 0.85rem;">
              <li><strong>การสลับตัวแปรทดลอง:</strong> QA บังคับดูหน้ารูปแบบ A หรือ B โดยการส่งค่าผ่าน URL Query Parameter หรือยิง Custom Header (เช่น <code>X-Experiment-Id: 1042_B</code>)</li>
              <li><strong>ตรวจเช็ก Event Tracking:</strong> ตรวจสอบว่าพฤติกรรมการคลิกหรือจองห้องของผู้ใช้ ถูกส่ง Event เข้า Kafka/Data Lake อย่างถูกต้อง</li>
              <li><strong>ป้องกัน Schema ชนกัน:</strong> มั่นใจว่าฟีเจอร์เวอร์ชัน B ไม่ไปกระทบโครงสร้างข้อมูลของผู้ใช้งานฝั่ง A</li>
            </ul>
          </div>
        </div>

        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-emerald">Distributed Systems</span>
          <div class="lang-en">
            <h3>2. Microservices, Kafka & Data Consistency</h3>
            <ul style="font-size: 0.85rem;">
              <li><strong>Event-Driven Testing (Kafka):</strong> Verify that when <code>OrderService</code> emits an <code>OrderCreated</code> event, <code>PaymentService</code> and <code>NotificationService</code> consume it correctly.</li>
              <li><strong>Race Conditions & Concurrency:</strong> Simulate 2 users clicking "Book Last Seat" simultaneously. Verify backend locking mechanisms (Distributed Locks) prevent double-allocation.</li>
              <li><strong>Contract Testing:</strong> Ensure microservices communicate via validated JSON schemas before deployment.</li>
            </ul>
          </div>
          <div class="lang-th">
            <h3 style="color: #34d399;">2. การเทสระบบ Microservices, Kafka & Race Conditions</h3>
            <ul style="font-size: 0.85rem;">
              <li><strong>Event-Driven (Kafka):</strong> เมื่อ <code>OrderService</code> ส่ง Event สร้างออเดอร์ บริการตัดเงินและแจ้งเตือนต้องดึงข้อมูลไปประมวลผลได้อย่างถูกต้อง</li>
              <li><strong>ป้องกันการจองซ้ำ (Race Condition):</strong> จำลองผู้ใช้ 2 คนกดจอง "ห้องสุดท้าย" ในเสี้ยววินาทีเดียวกัน ระบบต้องมี Distributed Lock ให้คนแรกจองได้ และปฏิเสธคนที่สองอย่างถูกต้อง</li>
              <li><strong>Contract Testing:</strong> ตรวจสอบ Schema JSON ของแต่ละ Service ว่าคุยภาษาเดียวกันก่อน Deploy</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 14: Senior Answering Framework -->
    <section id="sec-framework">
      <div class="section-header">
        <span class="section-num">PART 14</span>
        <h2>The 3-Step Senior Answering Framework for Any Scenario</h2>
      </div>
      <p>When interviewers give you an open-ended scenario (e.g. <em>"How would you test Payment?"</em>), follow this 3-step formula:</p>

      <div class="grid-3">
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-amber">Step 1: Clarify</span>
          <div class="lang-en">
            <h3>1. Clarify Scope & Constraints</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">Ask 2-3 smart questions before answering:</p>
            <ul style="font-size: 0.82rem;">
              <li><em>"Which platforms are we targeting (Mobile App, Desktop Web, or API)?"</em></li>
              <li><em>"Are we integrating with third-party providers (e.g., Stripe, 2C2P)?"</em></li>
              <li><em>"What are the SLA latency expectations?"</em></li>
            </ul>
          </div>
          <div class="lang-th">
            <h3 style="color: #fbbf24;">สเต็ป 1: ถามเพื่อล็อกขอบเขตก่อน</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">ถามคำถามฉลาดๆ 2-3 ข้อก่อนเริ่มตอบ:</p>
            <ul style="font-size: 0.82rem;">
              <li><em>"เราโฟกัสแพลตฟอร์มไหนเป็นหลักคะ (Mobile App, Web, หรือยิงระดับ API)?"</em></li>
              <li><em>"ระบบเชื่อมต่อกับ Gateway ภายนอกอย่าง 2C2P หรือ Stripe หรือไม่?"</em></li>
              <li><em>"มีข้อกำหนดเรื่องความเร็ว Response Time SLA เท่าไหร่คะ?"</em></li>
            </ul>
          </div>
        </div>

        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-blue">Step 2: 4-Pillar Breakdown</span>
          <div class="lang-en">
            <h3>2. Structure by 4 Dimensions</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">Divide your testing strategy into 4 clean buckets:</p>
            <ul style="font-size: 0.82rem;">
              <li><strong>Functional:</strong> Happy path + Business rules.</li>
              <li><strong>Boundary & Negative:</strong> Edge cases + Invalid inputs.</li>
              <li><strong>API & Database:</strong> Payload schema + SQL integrity.</li>
              <li><strong>Non-Functional:</strong> Cross-device + Concurrency load.</li>
            </ul>
          </div>
          <div class="lang-th">
            <h3 style="color: #38bdf8;">สเต็ป 2: แจกแจงเป็น 4 กล่องความคิด</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">แบ่งคำตอบออกเป็น 4 มิติให้กรรมการฟังง่าย:</p>
            <ul style="font-size: 0.82rem;">
              <li><strong>Functional:</strong> เส้นทางหลัก Happy Path + กฎธุรกิจ</li>
              <li><strong>Boundary & Negative:</strong> ค่าขอบเขต BVA + ข้อมูลผิดปกติ</li>
              <li><strong>API & Database:</strong> ตรวจ Status Code + ความถูกต้องใน DB</li>
              <li><strong>Non-Functional:</strong> ความเข้ากันได้ของอุปกรณ์ + ปริมาณโหลด</li>
            </ul>
          </div>
        </div>

        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-emerald">Step 3: Automation Priority</span>
          <div class="lang-en">
            <h3>3. Define Automation Strategy</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">Conclude with ROI prioritization:</p>
            <ul style="font-size: 0.82rem;">
              <li><em>"I would automate the core critical flow in CI/CD Smoke suite using Playwright & Postman, while keeping exploratory edge cases manual."</em></li>
            </ul>
          </div>
          <div class="lang-th">
            <h3 style="color: #34d399;">สเต็ป 3: สรุปแผน Automation</h3>
            <p style="font-size: 0.85rem; color: #cbd5e1;">สรุปด้วยความคุ้มค่าในการเขียนสคริปต์:</p>
            <ul style="font-size: 0.82rem;">
              <li><em>"เคสหลักที่สำคัญ หนูจะเขียนเป็น Automated Smoke Suite ด้วย Playwright และ Postman บน CI/CD ส่วนเคสทดลองพฤติกรรมแปลกๆ จะใช้การเทสด้วย Manual ค่ะ"</em></li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 15: Live Interview Scenarios -->
    <section id="sec-scenarios">
      <div class="section-header">
        <span class="section-num">PART 15</span>
        <h2>High-Frequency Standard Live Scenarios & Answers</h2>
      </div>

      <!-- Scenario 1: Search & Filter -->
      <div class="qa-box scenario" onclick="toggleCardLang(this)">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="qa-question">
          <span>🎯 Scenario 1:</span> "How would you test a High-Scale Search & Filter feature?"
        </div>
        <div class="lang-en">
          <div class="qa-answer">
            "I structure my test approach across 4 structured dimensions to ensure full coverage:
            <ol style="margin: 0.75rem 0 0 1.25rem; line-height: 1.8;">
              <li><strong>Functional & Happy Path Testing:</strong> Search valid destination, date ranges, filter by Price & Star rating, sorting by Lowest Price.</li>
              <li><strong>Boundary & Negative Testing:</strong> Same-day booking (today), max 365 days advance, invalid characters, past dates.</li>
              <li><strong>API & Contract Testing:</strong> Inspect <code>POST /api/v1/search</code>, status codes (200, 400), response payload schema and price calculation.</li>
              <li><strong>Non-Functional:</strong> Cross-browser compatibility on Chrome & Safari Mobile, search results load &lt; 1.5s under concurrency."</li>
            </ol>
          </div>
        </div>
        <div class="lang-th">
          <div class="qa-answer">
            "หนูจะแบ่งการทดสอบออกเป็น 4 มิติเพื่อให้ครอบคลุม 100% ค่ะ:
            <ol style="margin: 0.75rem 0 0 1.25rem; line-height: 1.8;">
              <li><strong>Functional & Happy Path:</strong> ค้นหาเมืองที่มีอยู่จริง, เลือกวันที่ถูกต้อง, กรองช่วงราคาและดาว, และทดสอบการเรียงลำดับราคาถูกสุด</li>
              <li><strong>Boundary & Negative:</strong> จองวันเดียวกัน (วันนี้), จองล่วงหน้า 365 วัน, ดักจับการกรอกวันที่ในอดีต และอักขระพิเศษ SQL Injection</li>
              <li><strong>API Testing:</strong> ตรวจสอบ API ค้นหา สถานะ 200/400 และความถูกต้องของ Schema ราคาที่ตอบกลับมา</li>
              <li><strong>Non-Functional:</strong> ตรวจสอบการแสดงผลข้ามเบราว์เซอร์ Chrome และ iOS Safari และเช็กว่าผลการค้นหาต้องโหลดเสร็จใน &lt; 1.5 วินาทีค่ะ"</li>
            </ol>
          </div>
        </div>
      </div>

      <!-- Scenario 2: Payment Gateway -->
      <div class="qa-box purple" onclick="toggleCardLang(this)">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="qa-question">
          <span>🎯 Scenario 2:</span> "How would you test a Payment Gateway & Handle Concurrency / Race Conditions?"
        </div>
        <div class="lang-en">
          <div class="qa-answer">
            "I validate payment across transaction integrity, security, and edge failure cases:
            <ol style="margin: 0.75rem 0 0 1.25rem; line-height: 1.8;">
              <li><strong>Happy Path & Currency Integrity:</strong> Successful checkout with Visa/Mastercard, ensuring charged amount matches checkout total with taxes and discounts.</li>
              <li><strong>Failure & Network Drop:</strong> Insufficient balance, wrong OTP, and simulating network drop right after clicking 'Pay' ➔ Verify system does NOT double-charge via <strong>Idempotency Key</strong>.</li>
              <li><strong>Race Conditions:</strong> 2 users booking the very last room at the exact same millisecond ➔ Ensure database distributed locks allow only 1 transaction to succeed.</li>
              <li><strong>Security (PCI-DSS):</strong> Masked card numbers (<code>**** 1234</code>) and zero storage of CVV in server database."</li>
            </ol>
          </div>
        </div>
        <div class="lang-th">
          <div class="qa-answer">
            "หนูจะทดสอบระบบชำระเงินโดยเน้นความถูกต้องของธุรกรรม ความปลอดภัย และเคสระบบขัดข้องค่ะ:
            <ol style="margin: 0.75rem 0 0 1.25rem; line-height: 1.8;">
              <li><strong>Happy Path & ตรวจสอบยอดเงิน:</strong> จ่ายเงินสำเร็จด้วยบัตร Visa/Mastercard ยอดที่ตัดจริงต้องตรงกับหน้าจอเป๊ะๆ รวมภาษีและหักส่วนลดแล้ว</li>
              <li><strong>เคสเน็ตหลุดกะทันหัน:</strong> ลูกค้ากดปุ่มจ่ายเงินแล้วเน็ตตัดทันที ➔ ระบบต้องมี <strong>Idempotency Key</strong> ป้องกันไม่ให้ตัดเงินเบิ้ลซ้ำสองรอบ</li>
              <li><strong>Race Condition (จองห้องสุดท้ายพร้อมกัน):</strong> ผู้ใช้ 2 คนกดแย่งห้องสุดท้ายในเสี้ยววินาทีเดียวกัน ระบบต้องมี Distributed Lock ให้คนแรกได้ไป และปฏิเสธคนที่สองอย่างนุ่มนวล</li>
              <li><strong>ความปลอดภัย (PCI-DSS):</strong> บัตรเครดิตต้องถูก Mask หมายเลข และห้ามเก็บเลข CVV/CVC ลงในฐานข้อมูลเด็ดขาดค่ะ"</li>
            </ol>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 16: Conflict & Mindset -->
    <section id="sec-behavioral">
      <div class="section-header">
        <span class="section-num">PART 16</span>
        <h2>Engineering Collaboration & Conflict Resolution</h2>
      </div>

      <!-- Conflict Scenario 1 -->
      <div class="qa-box warning" onclick="toggleCardLang(this)">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="qa-question">
          <span>💼 Question 1:</span> "What do you do when a developer says: 'This is not a bug, it's a feature'?"
        </div>
        <div class="lang-en">
          <div class="qa-answer">
            "I maintain a factual, collaborative approach without emotional arguments:
            <ol style="margin: 0.5rem 0 0 1.25rem;">
              <li><strong>Review Requirement:</strong> Check the PRD and User Story Acceptance Criteria in Jira.</li>
              <li><strong>Gather Evidence:</strong> Provide reproduction steps, network HAR logs, and screenshots.</li>
              <li><strong>Align with PO:</strong> If ambiguous, I schedule a quick 5-minute sync with Product Owner and Developer to clarify business intent."</li>
            </ol>
          </div>
        </div>
        <div class="lang-th">
          <div class="qa-answer">
            "หนูจะยึดหลักข้อเท็จจริงและการทำงานร่วมกันโดยไม่ใช้อารมณ์ค่ะ:
            <ol style="margin: 0.5rem 0 0 1.25rem;">
              <li><strong>ย้อนกลับไปดูสเปก:</strong> เปิดเช็กเอกสาร PRD และ Acceptance Criteria ใน Jira</li>
              <li><strong>เตรียมหลักฐานเชิงประจักษ์:</strong> แนบขั้นตอนการทำซ้ำ, ภาพแคปหน้าจอ, และ Log เครือข่ายให้ Dev ดู</li>
              <li><strong>ประสานงานกับ Product Owner:</strong> หากสเปกเขียนคลุมเครือ หนูจะขอนัดคุยสั้นๆ 5 นาทีระหว่าง PO, Dev และ QA เพื่อยืนยันความต้องการของธุรกิจให้ตรงกันค่ะ"</li>
            </ol>
          </div>
        </div>
      </div>

      <!-- Conflict Scenario 2 -->
      <div class="qa-box mindset" onclick="toggleCardLang(this)">
        <div class="card-lang-indicator">EN / TH</div>
        <div class="qa-question">
          <span>💼 Question 2:</span> "How do you handle a situation where testing time is cut short before release?"
        </div>
        <div class="lang-en">
          <div class="qa-answer">
            "I apply <strong>Risk-Based Testing (RBT)</strong>:
            <ol style="margin: 0.5rem 0 0 1.25rem;">
              <li><strong>Focus on P0/P1:</strong> Dedicate available time executing Smoke and critical payment/booking flows.</li>
              <li><strong>Automate Fast Regression:</strong> Trigger automated API/UI regression suites in parallel.</li>
              <li><strong>Transparent Risk Communication:</strong> Document untested peripheral areas (P2/P3) and communicate calculated risks clearly to the Product Owner."</li>
            </ol>
          </div>
        </div>
        <div class="lang-th">
          <div class="qa-answer">
            "หนูจะใช้หลักการ <strong>Risk-Based Testing (RBT)</strong> ในการบริหารความเสี่ยงค่ะ:
            <ol style="margin: 0.5rem 0 0 1.25rem;">
              <li><strong>ทุ่มเวลาให้เส้นทางวิกฤต (P0 / P1):</strong> โฟกัสการเทสระบบค้นหาและจ่ายเงินหลักที่เป็นหัวใจของธุรกิจ</li>
              <li><strong>รัน Automation Regression คู่ขนาน:</strong> ยิงสคริปต์อัตโนมัติเพื่อกวาดฟังก์ชันรอบข้างอย่างรวดเร็ว</li>
              <li><strong>สื่อสารความเสี่ยงอย่างโปร่งใส:</strong> ระบุฟีเจอร์ส่วนเสริมที่ยังไม่ได้เทสลงใน Test Summary Report และแจ้งความเสี่ยงให้ PO และ Lead ทราบก่อนตัดสินใจ Release ค่ะ"</li>
            </ol>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 17: High-Signal Questions to Ask -->
    <section id="sec-questions">
      <div class="section-header">
        <span class="section-num">PART 17</span>
        <h2>High-Signal Questions to Ask the Interviewer</h2>
      </div>
      <p>At the end of the interview when they ask <em>"Do you have any questions for us?"</em>, ask these smart questions:</p>

      <div class="grid-2">
        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-blue">Engineering Culture</span>
          <div class="lang-en">
            <h3>1. Test Automation & CI/CD Pipeline</h3>
            <p style="font-size: 0.9rem; color: #cbd5e1;">
              <em>"Could you tell me more about your test automation pipeline? How are automated test suites integrated into your CI/CD deployment cycles?"</em>
            </p>
          </div>
          <div class="lang-th">
            <h3 style="color: #38bdf8;">1. ถามเรื่องระบบ CI/CD & Automation</h3>
            <p style="font-size: 0.9rem; color: #cbd5e1;">
              <em>"รบกวนสอบถามเพิ่มเติมเกี่ยวกับ Pipeline การทำ Automation ของทีมค่ะ ว่าปัจจุบันมีการเชื่อมต่อ Test Suite เข้ากับกระบวนการ CI/CD ในการ Deploy รอบต่างๆ อย่างไรบ้างคะ?"</em>
            </p>
          </div>
        </div>

        <div class="card" onclick="toggleCardLang(this)">
          <div class="card-lang-indicator">EN / TH</div>
          <span class="card-tag tag-emerald">Team Collaboration</span>
          <div class="lang-en">
            <h3>2. QA & Developer Collaboration Model</h3>
            <p style="font-size: 0.9rem; color: #cbd5e1;">
              <em>"How do QA engineers collaborate with Developers and Product Managers in sprint planning—are QA engineers involved early in requirement grooming?"</em>
            </p>
          </div>
          <div class="lang-th">
            <h3 style="color: #34d399;">2. ถามเรื่องรูปแบบการทำงานร่วมกับ Dev และ PO</h3>
            <p style="font-size: 0.9rem; color: #cbd5e1;">
              <em>"ในทีมมีการทำงานร่วมกันระหว่าง QA, Developer และ Product Manager อย่างไรบ้างคะ เช่น QA จะได้เข้าไปช่วยดู Requirement Grooming ตั้งแต่ช่วงต้น Sprint เลยไหมคะ?"</em>
            </p>
          </div>
        </div>
      </div>
    </section>

    <footer>
      <p>Global Software Testing Standard & Master Guide • Prepared for Namo (Natawat Tephassadin na Ayutaya)</p>
      <p style="font-family: 'JetBrains Mono'; font-size: 0.75rem; color: var(--text-dim); margin-top: 0.25rem;">Designed by Malli • Bilingual Interactive Edition with Instant Tap-to-Translate</p>
    </footer>
  </main>

  <script>
    // Smooth scrolling & active nav state tracking
    const navLinks = document.querySelectorAll('.nav-item');
    window.addEventListener('scroll', () => {
      let current = '';
      const sections = document.querySelectorAll('section');
      sections.forEach(section => {
        const sectionTop = section.offsetTop;
        if (window.pageYOffset >= sectionTop - 140) {
          current = section.getAttribute('id');
        }
      });

      navLinks.forEach(link => {
        link.classList.remove('active');
        if (link.getAttribute('href') === '#' + current) {
          link.classList.add('active');
        }
      });
    });

    // Individual Card Click/Tap to Toggle Language
    function toggleCardLang(element) {
      element.classList.toggle('is-th-active');
    }

    // Global Language Toggle (EN / TH for the entire page)
    function setGlobalLang(lang) {
      const btnEn = document.getElementById('btn-en');
      const btnTh = document.getElementById('btn-th');

      if (lang === 'th') {
        document.body.classList.add('global-th');
        btnTh.classList.add('active');
        btnEn.classList.remove('active');
      } else {
        document.body.classList.remove('global-th');
        btnEn.classList.add('active');
        btnTh.classList.remove('active');
        // Reset individual overrides
        document.querySelectorAll('.is-th-active').forEach(el => el.classList.remove('is-th-active'));
      }
    }
  </script>
</body>
</html>
"""

with open(target_file, 'w', encoding='utf-8') as f:
    f.write(html_content.strip() + "\n")

print(f"Successfully upgraded {target_file} with Bilingual Tap-to-Translate features!")
