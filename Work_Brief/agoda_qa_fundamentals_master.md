# 🚀 Comprehensive QA Fundamentals & Agoda Interview Master Guide

**Target Company:** Agoda (Booking Holdings)  
**Role:** Software Tester (Contract / Enterprise Scale)  
**Candidate:** Natawat Tephassadin na Ayutaya (Namo)  
**Language:** Professional International English (with Thai key takeaway notes)

---

# 📚 Part 1: Core QA Fundamentals & Terminology

## 1. Bug vs. Defect vs. Error vs. Failure
* **Error (Mistake):** A human mistake made by a developer (e.g., a typo in code, wrong logic).
* **Defect / Bug:** The flaw in the software code or documentation caused by an Error.
* **Failure:** When the software is executed and does **not** behave as expected by the user (the defect manifests during runtime).

> 💡 **Interview Punchline:**  
> *"An **Error** is made by a developer, creating a **Bug/Defect** in the code, which leads to a software **Failure** when executed by a user."*

---

## 2. Verification vs. Validation (V&V)
* **Verification (Static Testing):** "Are we building the product **right**?"  
  * Focus: Checking documents, design, architecture, and code without running the software (Code Reviews, Walkthroughs, Inspections).
* **Validation (Dynamic Testing):** "Are we building the **right** product?"  
  * Focus: Executing the software to ensure it satisfies user needs and business requirements (Functional testing, End-to-End testing, UAT).

---

## 3. Severity vs. Priority
* **Severity (Technical Impact):** How badly the bug breaks the technical functionality. (Set by **QA**).
  * *Critical / Blocker:* System crash, data corruption, database leak.
  * *Low:* Typo on a footer button.
* **Priority (Business Urgency):** How quickly the business needs this bug fixed. (Set by **Product Owner / Business**).
  * *High Priority / Low Severity Example:* A misspelled company logo or wrong brand color on the Agoda Homepage. (Doesn't break the app, but hurts brand image immediately).
  * *High Severity / Low Priority Example:* App crashes when using an obsolete OS (e.g., Windows 98) that 0.001% of users have.

---

## 4. Software Testing Life Cycle (STLC)
1. **Requirement Analysis:** Understand what needs to be tested; identify testable requirements.
2. **Test Planning:** Define scope, objectives, schedule, test environment, and tools.
3. **Test Case Development:** Write detailed test cases, test data, and automation scripts.
4. **Test Environment Setup:** Prepare staging servers, databases, test accounts, and browser grids.
5. **Test Execution:** Execute manual & automated tests, log defects in Jira.
6. **Test Closure / Reporting:** Analyze test metrics, pass/fail rates, and write the Test Summary Report.

---

# 🎯 Part 2: Black-Box Test Design Techniques (When to use Which?)

Interviewers love testing whether you know **HOW** to design test cases efficiently without testing every single combination.

```
┌────────────────────────────────┬──────────────────────────────────────────────────────────┐
│ Test Design Technique          │ Best Scenario to Use (When to apply?)                    │
├────────────────────────────────┼──────────────────────────────────────────────────────────┤
│ 1. Boundary Value Analysis     │ Range inputs (e.g., Age 18-60, Hotel booking 1-30 days,  │
│    (BVA)                       │ Password length 8-20 characters).                        │
├────────────────────────────────┼──────────────────────────────────────────────────────────┤
│ 2. Equivalence Partitioning   │ Discrete categories (e.g., Payment methods: Visa,       │
│    (EP)                        │ Mastercard, PayPal; User Roles: Admin, Customer, Guest). │
├────────────────────────────────┼──────────────────────────────────────────────────────────┤
│ 3. Decision Table Testing      │ Complex business logic with multiple condition rules     │
│                                │ (e.g., Agoda VIP discounts + promo codes + room types).  │
├────────────────────────────────┼──────────────────────────────────────────────────────────┤
│ 4. State Transition Testing    │ Workflows with status changes (e.g., Booking Created ➔   │
│                                │ Confirmed ➔ Paid ➔ Checked-In ➔ Cancelled/Refunded).     │
├────────────────────────────────┼──────────────────────────────────────────────────────────┤
│ 5. Use Case / E2E Testing      │ Full real user journey (Search Hotel ➔ Select Room ➔     │
│                                │ Enter Guest Info ➔ Pay ➔ Receive Booking Voucher).       │
└────────────────────────────────┴──────────────────────────────────────────────────────────┘
```

### Deep-Dive Examples:
* **Boundary Value Analysis (BVA):**  
  * If a hotel booking allows **1 to 30 nights**:
  * Test: `Min-1 (0)`, `Min (1)`, `Min+1 (2)`, `Nominal (15)`, `Max-1 (29)`, `Max (30)`, `Max+1 (31)`.
  * *Why:* Most bugs hide at the edges/boundaries (e.g., off-by-one errors `<` vs `<=`).
* **Equivalence Partitioning (EP):**  
  * Divide inputs into valid and invalid partitions. Test one representative value from each partition instead of testing all numbers.
  * Valid: 18–60 (Pick 25) | Invalid Low: <18 (Pick 10) | Invalid High: >60 (Pick 75).

---

# 🔍 Part 3: Test Levels & Testing Types (Classification Matrix)

## 1. Test Levels (From Smallest to Largest)
1. **Unit Testing:** Testing individual functions/methods (done by Developers using Jest/JUnit).
2. **Integration Testing:** Testing how two or more modules communicate (e.g., Booking Service communicating with Payment Gateway API).
3. **System Testing:** Testing the complete, integrated system end-to-end against specifications.
4. **Acceptance Testing (UAT):** Validating the system with real business stakeholders or users before release.

---

## 2. Testing Types & Scenarios

### 🔹 Smoke Testing vs. Sanity Testing
* **Smoke Testing (Build Verification Test):**
  * *When:* Executed on a **new build** straight from CI/CD pipeline.
  * *Goal:* Verify if the core critical functionalities work before accepting the build for deep testing. (Shallow & Wide).
  * *Example:* Can user open Agoda web? Can user search? Can user log in?
* **Sanity Testing:**
  * *When:* Executed after **a bug fix or minor release**.
  * *Goal:* Verify that the specific bug fix works and related small areas are not broken. (Deep & Narrow).

### 🔹 Regression Testing vs. Retesting
* **Retesting:** Testing the **exact same bug** that developer fixed to confirm it is resolved.
* **Regression Testing:** Testing the **unmodified areas** of the application to ensure that new code changes or bug fixes did not break existing features.

### 🔹 Non-Functional Testing (Enterprise Focus)
* **Performance Testing:** Load testing (normal traffic), Stress testing (breaking point), Spike testing (sudden traffic surges like New Year flash sale).
* **Security Testing:** Authentication, Authorization, SQL Injection, Cross-Site Scripting (XSS), Data Encryption.
* **Compatibility Testing:** Cross-browser (Chrome, Safari, Edge, Firefox) and Cross-device (Mobile Web, iOS, Android).

---

# 🤖 Part 4: Test Automation & API Testing (Agoda Scale)

## 1. The Automation Test Pyramid
* **70% Unit Tests:** Fast, cheap, isolated.
* **20% API / Service Tests:** Reliable, fast execution, validates business logic and response codes (200, 400, 401, 404, 500).
* **10% UI E2E Tests (Playwright / Robot):** Realistic user journeys, visual validation, but slower and prone to flakiness if selectors change.

## 2. API Testing Essentials (Postman & REST)
* **HTTP Methods:**
  * `GET`: Retrieve data (e.g., `/api/hotels?city=Bangkok`)
  * `POST`: Create new record (e.g., `/api/bookings`)
  * `PUT`: Replace/update entire resource
  * `PATCH`: Update partial fields (e.g., change guest phone number)
  * `DELETE`: Remove resource
* **Status Codes:**
  * `200 OK` / `201 Created`: Success
  * `400 Bad Request`: Client error (invalid payload)
  * `401 Unauthorized` vs `403 Forbidden`: 
    * `401` = Who are you? (Missing or expired JWT Token)
    * `403` = I know who you are, but you don't have permission! (e.g., Customer trying to access Admin API)
  * `404 Not Found`: Endpoint or data does not exist
  * `500 Internal Server Error`: Backend crashed or unhandled exception

---

# 🎤 Part 5: High-Frequency Agoda Interview Scenarios & Fluent Answers

### Scenario 1: "How would you test the Hotel Search & Booking feature on Agoda?"
> **Answer Structure:**  
> "I break it down into 4 key dimensions:
> 1. **Functional Testing (Happy Path & Edge Cases):**
>    - Search with valid destination, check-in/out dates, and guest count. Verify search result filters (Price, Star rating, Free cancellation).
>    - Apply **Boundary Value Analysis** on dates (same-day booking, maximum advance booking 365 days).
> 2. **Negative & Error Handling:**
>    - Invalid inputs: Check-out date before check-in date, zero guests, special characters in destination input.
> 3. **API & Integration Testing:**
>    - Inspect network traffic using Postman/DevTools. Validate `POST /api/search` and `POST /api/checkout` status codes, latency, and JSON payload contracts.
> 4. **Non-Functional Testing:**
>    - **Cross-browser:** Ensure UI renders properly on Mobile Safari, Chrome, and Desktop.
>    - **Performance:** Check page load times under high search concurrency."

---

### Scenario 2: "What do you do when a developer says 'This is not a bug, it's a feature'?"
> **Answer:**  
> "I don't argue emotionally. First, I refer to the **Product Requirement Document (PRD) or User Story Acceptance Criteria**.  
> If the requirement is ambiguous, I reproduce the issue with clear steps and screen recordings, then schedule a quick 5-minute alignment with the **Product Owner (PO)** and Developer to clarify the intended user experience."

---

### Scenario 3: "How do you decide what test cases to automate vs. keep manual?"
> **Answer:**  
> "I use ROI (Return on Investment) prioritization:
> - **Automate:** Repetitive tests (Regression Suite, Smoke Tests), Critical Business Paths (Login, Checkout, Payment), Multi-browser matrix, and Data-driven tests with large datasets.
> - **Keep Manual:** One-off features, rapidly changing exploratory features, UX/Usability evaluations, and ad-hoc edge cases."

---

### Scenario 4: "Tell me about a challenging bug you found during your internship."
> **Answer:**  
> "During my internship testing the **iNT Connect** platform, I found a critical **Role-Based Access Control (RBAC)** vulnerability. A normal user could view administrative ticketing data simply by modifying the ID parameter in the API endpoint (`GET /api/tickets/{id}`).  
> I caught this by performing API security testing with Postman. I documented the reproduction steps, flagged it as **Critical Severity**, and worked closely with the backend developer to enforce JWT token authorization middleware before deployment."

---

# 🏆 Part 6: Quick Vocabulary & Acronym Flashcard

* **SLA:** Service Level Agreement (System uptime / response time guarantees).
* **PRD:** Product Requirement Document.
* **AC:** Acceptance Criteria (Conditions a software product must satisfy).
* **Flaky Test:** An automated test that passes and fails inconsistently without code changes. (Handled by: improving locator strategy, explicit waits instead of sleep, isolating test data).
* **CI/CD:** Continuous Integration & Continuous Delivery (GitHub Actions, GitLab CI, Jenkins).
* **Test Harness / Test Driver:** Stubs and drivers used to simulate missing modules during integration testing.
