# 📦 TrueMoney / Ascend Money QA Pre-Test Submission Package

**Candidate Name:** Natawat Tephassadin na Ayutaya (Namo)  
**Target Role:** Quality Assurance Engineer (TrueMoney)  
**Email:** `namo.nanon5@gmail.com` | **Phone:** 063-435-8908  
**Submission Deadline:** Tuesday, August 11, 2026  

---

## 📂 Package Contents

1. **`solution1_print_n.py`**
   - Python code implementing function `Print(y)` to output a square of size `y*y` plotting a capital letter **"N"** with `X` and filling the rest with `O`.
   - Verified with test inputs `y=5` and `y=7`.

2. **`solution2_facebook_login_testcases.md`**
   - Comprehensive Mobile Test Scenarios & Test Cases table for **Facebook Log-in feature on mobile applications**.
   - Contains 10 detailed test cases covering Functional, Negative, 2FA Security, Offline Handling, and Session Persistence.

3. **`solution3_web_automation.robot`**
   - Robot Framework Web Automation script using `SeleniumLibrary`.
   - Tests `http://the-internet.herokuapp.com/login` covering:
     - Login Success (tomsmith / SuperSecretPassword!) -> Verify secure area -> Logout -> Verify logged out.
     - Login Failed - Password Incorrect -> Verify 'Your password is invalid!'.
     - Login Failed - Username Not Found -> Verify 'Your username is invalid!'.

4. **`solution4_api_automation.robot`**
   - Robot Framework API Automation script using `RequestsLibrary`.
   - Tests REST API GET requests at `https://potterapi-fedeperin.vercel.app/en/houses`:
     - Get House Data Success (`index=3` -> Status 200, compare JSON body for Slytherin).
     - Get House Data But User Not Found (`index=5` -> Status 404, verify JSON body `{"error": "Invalid Index"}`).

---

## 🚀 How to Run Tests Locally

### 1. Test Python Function (Problem 1)
```bash
python solution1_print_n.py
```

### 2. Test Robot Framework Web & API Scripts (Problem 3 & 4)
Make sure dependencies are installed:
```bash
pip install robotframework robotframework-seleniumlibrary robotframework-requests
```
Run Robot Framework test suites:
```bash
robot solution3_web_automation.robot
robot solution4_api_automation.robot
```

---

## 📤 Submission Instructions
Zip all files into `TrueMoney_QA_PreTest_Natawat.zip` and reply to `puntharee.suw@ascendcorp.com`.
