import os
import openpyxl
from copy import copy

workspace_dir = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
backup_path = os.path.join(workspace_dir, "Work_Brief", "TrueMoney_QA_Test_Answers", "facebook_login_testcases.xlsx")
target_path = os.path.join(workspace_dir, "Work_Brief", "TrueMoney_QA_Test_Answers", "solution2_facebook_login_testcases.xlsx")
html_path = os.path.join(workspace_dir, "Work_Brief", "TrueMoney_QA_Test_Answers", "solution2_facebook_login_testcases.html")
md_path = os.path.join(workspace_dir, "Work_Brief", "TrueMoney_QA_Test_Answers", "solution2_facebook_login_testcases.md")

def reorganize_excel():
    # Load Boss's original backup workbook to capture styles
    wb_orig = openpyxl.load_workbook(backup_path)
    ws_orig = wb_orig.active

    # Create new workbook with exact same sheet title
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = ws_orig.title
    ws.views.sheetView[0].showGridLines = True

    # Copy header formatting from Boss's original header
    headers = [ws_orig.cell(row=1, column=c).value for c in range(1, 7)]
    ws.append(headers)
    ws.row_dimensions[1].height = ws_orig.row_dimensions[1].height or 28

    for c in range(1, 7):
        cell = ws.cell(row=1, column=c)
        ref = ws_orig.cell(row=1, column=c)
        if ref.font: cell.font = copy(ref.font)
        if ref.fill: cell.fill = copy(ref.fill)
        if ref.alignment: cell.alignment = copy(ref.alignment)
        if ref.border: cell.border = copy(ref.border)

    # Harmonized 15 Test Cases in Logical Grouped Order
    ordered_rows = [
        # Group 1: Valid Logins & Input Handling
        [
            "Valid Login with Email",
            "To verify that user can login successfully when they put a correct registered email and password.",
            "1. Facebook Mobile App installed.\n2. Active internet connection.\n3. Registered account with email.",
            "1. Open Facebook Mobile App.\n2. Enter registered email.\n3. Enter correct password.\n4. Tap 'Log In' button.",
            "1. Login successful.\n2. Redirected to Facebook News Feed.\n3. User session token saved.",
            "High"
        ],
        [
            "Valid Login with Phone Number",
            "To verify that user can login successfully when they put a correct registered phone number and password.",
            "1. Facebook Mobile App installed.\n2. Active internet connection.\n3. Registered account with phone number.",
            "1. Open Facebook Mobile App.\n2. Enter registered phone number (e.g. 0812345678).\n3. Enter correct password.\n4. Tap 'Log In' button.",
            "1. Login successful.\n2. Redirected to Facebook News Feed.",
            "High"
        ],
        [
            "Valid Login with Leading/Trailing Spaces in Email",
            "To verify that app automatically trims leading and trailing whitespaces when user enters email with spaces.",
            "1. Facebook Mobile App installed.\n2. Active internet connection.",
            "1. Open Facebook Mobile App.\n2. Enter email with leading/trailing spaces (e.g. '  namo.nanon5@gmail.com  ').\n3. Enter correct password.\n4. Tap 'Log In' button.",
            "1. App automatically trims whitespace.\n2. User logs in successfully to News Feed.",
            "Medium"
        ],
        # Group 2: Invalid Logins & Error Validations
        [
            "Invalid Login - Password Incorrect",
            "To verify that user can login unsuccessfully when they put a correct username but wrong password.",
            "1. Facebook Mobile App installed.\n2. Active internet connection.",
            "1. Open Facebook Mobile App.\n2. Enter valid email/phone.\n3. Enter incorrect password.\n4. Tap 'Log In' button.",
            "1. Login failed.\n2. Alert message displayed: 'Incorrect Password'.\n3. Password field cleared.",
            "High"
        ],
        [
            "Invalid Login - Password Case Sensitive",
            "To verify that password field is strictly case-sensitive when user enters password with wrong letter case.",
            "1. Facebook Mobile App installed.\n2. Active internet connection.\n3. Registered account password: 'Password123!'.",
            "1. Open Facebook Mobile App.\n2. Enter valid email.\n3. Enter password with incorrect letter case (e.g. 'password123!').\n4. Tap 'Log In' button.",
            "1. Login failed.\n2. Alert message displayed: 'Incorrect Password' (confirming case-sensitivity).",
            "High"
        ],
        [
            "Invalid Login - Username Not Found",
            "To verify that user can login unsuccessfully when they put an unregistered email or phone number.",
            "1. Facebook Mobile App installed.\n2. Active internet connection.",
            "1. Open Facebook Mobile App.\n2. Enter non-existent email (e.g. unknown_user9999@test.com).\n3. Enter any password.\n4. Tap 'Log In' button.",
            "1. Login failed.\n2. Alert message displayed: 'Invalid Credentials' or 'Account Not Found'.",
            "High"
        ],
        [
            "Invalid Login - Invalid Email Format",
            "To verify app validation message when user enters an email with invalid format (missing '@' or domain).",
            "1. Facebook Mobile App installed.",
            "1. Open Facebook Mobile App.\n2. Enter email with invalid format (e.g. 'namo.nanon5gmail.com' or 'namo@').\n3. Enter any password.\n4. Tap 'Log In' button.",
            "1. Login action prevented.\n2. Validation message displayed: 'Please enter a valid email address'.",
            "Medium"
        ],
        # Group 3: Field Validations (Blank Inputs)
        [
            "Invalid Login - Blank Email Field",
            "To verify inline validation when user leaves email/phone field blank while entering password.",
            "1. Facebook Mobile App installed.",
            "1. Open Facebook Mobile App.\n2. Leave Email/Phone field empty.\n3. Enter valid password.\n4. Tap 'Log In' button.",
            "1. Login action prevented.\n2. Inline error displayed: 'Please enter your email address or phone number'.",
            "High"
        ],
        [
            "Invalid Login - Blank Password Field",
            "To verify inline validation when user enters valid email/phone while leaving password field blank.",
            "1. Facebook Mobile App installed.",
            "1. Open Facebook Mobile App.\n2. Enter valid registered email.\n3. Leave Password field empty.\n4. Tap 'Log In' button.",
            "1. Login action prevented.\n2. Inline error displayed: 'Please enter your password'.",
            "High"
        ],
        [
            "Invalid Login - Blank Both Fields",
            "To verify inline validation when tapping Log In with both email/phone and password fields blank.",
            "1. Facebook Mobile App installed.",
            "1. Open Facebook Mobile App.\n2. Leave both Email/Phone and Password fields empty.\n3. Tap 'Log In' button.",
            "1. Login action prevented.\n2. Prompt message displays: 'Please enter your email and password'.",
            "Medium"
        ],
        # Group 4: Account Recovery & Security
        [
            "Forgot Password Flow",
            "To verify password recovery flow via 'Forgot Password?' link.",
            "1. Facebook Mobile App installed.\n2. Active internet connection.",
            "1. Open Facebook Mobile App.\n2. Tap 'Forgot Password?' link.\n3. Enter registered email/phone.\n4. Tap 'Search Account'.",
            "1. User account identified.\n2. Displays options to send OTP code via SMS or Email.",
            "High"
        ],
        [
            "Two-Factor Authentication (2FA)",
            "To verify 2FA prompt when logging in from a new unrecognized mobile device.",
            "1. Account has 2FA enabled.\n2. New unrecognized device.",
            "1. Open Facebook Mobile App.\n2. Enter valid email and password.\n3. Tap 'Log In' button.",
            "1. 2FA verification screen is displayed.\n2. Prompts for 6-digit OTP code sent via SMS or Authenticator App.",
            "High"
        ],
        # Group 5: App Behavior & Session
        [
            "Offline Network Handling",
            "To verify app behavior when attempting to login without internet connection.",
            "1. Mobile Wi-Fi and Cellular Data turned OFF.",
            "1. Open Facebook Mobile App.\n2. Enter valid credentials.\n3. Tap 'Log In' button.",
            "Error popup displays: 'No Internet Connection. Please check your network and try again.'",
            "High"
        ],
        [
            "Show/Hide Password Toggle",
            "To verify visibility toggle icon in password input field.",
            "1. Facebook Mobile App installed.",
            "1. Open App.\n2. Enter password text.\n3. Tap eye icon (Show password).\n4. Tap eye icon again (Hide password).",
            "1. Password text becomes visible.\n2. Password text gets masked again (••••••).",
            "Low"
        ],
        [
            "App Relaunch Session Persistence",
            "To verify that user remains logged in after closing and reopening the app.",
            "1. User logged in successfully.",
            "1. Close Facebook App from Recent Apps (Kill process).\n2. Relaunch Facebook App.",
            "App opens directly to News Feed without requiring re-login.",
            "High"
        ]
    ]

    # Style mapping by priority from original sheet
    prio_styles = {}
    for r in range(2, ws_orig.max_row + 1):
        p_val = str(ws_orig.cell(row=r, column=6).value).strip().lower()
        if p_val not in prio_styles:
            cell_ref = ws_orig.cell(row=r, column=6)
            prio_styles[p_val] = (copy(cell_ref.fill), copy(cell_ref.font))

    # Populate rows with Boss's formatting
    for idx, row_data in enumerate(ordered_rows, start=2):
        ws.append(row_data)
        ws.row_dimensions[idx].height = 65

        for col_idx in range(1, 7):
            cell = ws.cell(row=idx, column=col_idx)
            ref_cell = ws.cell(row=2, column=col_idx) # Template from Boss's Row 2
            
            if ref_cell.font: cell.font = copy(ref_cell.font)
            if ref_cell.alignment: cell.alignment = copy(ref_cell.alignment)
            if ref_cell.border: cell.border = copy(ref_cell.border)
            if ref_cell.fill: cell.fill = copy(ref_cell.fill)

            # Apply priority style
            if col_idx == 6:
                pv = str(cell.value).strip().lower()
                if pv in prio_styles:
                    fill_st, font_st = prio_styles[pv]
                    if fill_st: cell.fill = fill_st
                    if font_st: cell.font = font_st

    # Copy column widths from Boss's original worksheet
    for col_letter in ['A', 'B', 'C', 'D', 'E', 'F']:
        ws.column_dimensions[col_letter].width = ws_orig.column_dimensions[col_letter].width or 30

    # Save to backup_path
    wb.save(backup_path)
    try:
        wb.save(target_path)
    except PermissionError:
        pass
    print("Reorganized Excel file successfully!")

if __name__ == "__main__":
    reorganize_excel()
