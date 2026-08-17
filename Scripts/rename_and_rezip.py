import os
import shutil
import zipfile

workspace_dir = r"C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace"
answers_dir = os.path.join(workspace_dir, "Work_Brief", "TrueMoney_QA_Test_Answers")
zip_output_path = os.path.join(workspace_dir, "Work_Brief", "TrueMoney_QA_PreTest_Natawat.zip")

# Mapping original files to new test1, test2, test3, test4 filenames
file_mapping = [
    (os.path.join(answers_dir, "solution1_print_n.py"), os.path.join(answers_dir, "test1.py"), "test1.py"),
    (os.path.join(answers_dir, "facebook_login_testcases.xlsx"), os.path.join(answers_dir, "test2.xlsx"), "test2.xlsx"),
    (os.path.join(answers_dir, "solution3_web_automation.robot"), os.path.join(answers_dir, "test3.robot"), "test3.robot"),
    (os.path.join(answers_dir, "solution4_api_automation.robot"), os.path.join(answers_dir, "test4.robot"), "test4.robot")
]

def rename_and_zip():
    # Copy/Rename files to test1, test2, test3, test4
    zipped_files = []
    for src, dst, arcname in file_mapping:
        if os.path.exists(src):
            shutil.copyfile(src, dst)
            zipped_files.append((dst, arcname))
            print(f"Created renamed file: {arcname}")
        elif os.path.exists(os.path.join(answers_dir, "solution2_facebook_login_testcases.xlsx")) and arcname == "test2.xlsx":
            shutil.copyfile(os.path.join(answers_dir, "solution2_facebook_login_testcases.xlsx"), dst)
            zipped_files.append((dst, arcname))
            print(f"Created renamed file: {arcname}")

    # Re-create TrueMoney_QA_PreTest_Natawat.zip containing strictly these 4 files
    with zipfile.ZipFile(zip_output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path, arcname in zipped_files:
            zipf.write(file_path, arcname)
            print(f"Added to zip: {arcname}")

    print(f"\nSuccessfully updated {zip_output_path} with 4 test files.")

if __name__ == "__main__":
    rename_and_zip()
