import os
import zipfile

workspace_dir = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
answers_dir = os.path.join(workspace_dir, "Work_Brief", "TrueMoney_QA_Test_Answers")
zip_output_path = os.path.join(workspace_dir, "Work_Brief", "TrueMoney_QA_PreTest_Natawat.zip")

files_to_zip = [
    ("solution1_print_n.py", os.path.join(answers_dir, "solution1_print_n.py")),
    ("solution2_facebook_login_testcases.xlsx", os.path.join(answers_dir, "solution2_facebook_login_testcases.xlsx")),
    ("solution2_facebook_login_testcases.html", os.path.join(answers_dir, "solution2_facebook_login_testcases.html")),
    ("solution2_facebook_login_testcases.md", os.path.join(answers_dir, "solution2_facebook_login_testcases.md")),
    ("solution3_web_automation.robot", os.path.join(answers_dir, "solution3_web_automation.robot")),
    ("solution4_api_automation.robot", os.path.join(answers_dir, "solution4_api_automation.robot")),
    ("README_TrueMoney_Submission.md", os.path.join(answers_dir, "README_TrueMoney_Submission.md"))
]

def create_zip():
    with zipfile.ZipFile(zip_output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for arcname, file_path in files_to_zip:
            if os.path.exists(file_path):
                zipf.write(file_path, arcname)
                print(f"Added to zip: {arcname}")

    print(f"Successfully created zip package at: {zip_output_path}")

if __name__ == "__main__":
    create_zip()
