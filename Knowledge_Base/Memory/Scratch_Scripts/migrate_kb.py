import os
import shutil

base_dir = r'C:\Users\namo_\OneDrive\เอกสาร\gemini-cli\antigravity-office-workspace'

new_dirs = [
    os.path.join(base_dir, 'Knowledge_Base', 'Insights'),
    os.path.join(base_dir, 'Knowledge_Base', 'Research_Deepdive'),
    os.path.join(base_dir, 'Team_Reports', 'Executive_Briefings'),
]

for d in new_dirs:
    os.makedirs(d, exist_ok=True)

old_insights_dir = os.path.join(base_dir, 'insights')
if os.path.exists(old_insights_dir):
    for f in os.listdir(old_insights_dir):
        shutil.move(os.path.join(old_insights_dir, f), os.path.join(base_dir, 'Knowledge_Base', 'Insights', f))
    os.rmdir(old_insights_dir)

portfolio_dir = os.path.join(base_dir, 'portfolio')
if os.path.exists(portfolio_dir):
    for f in os.listdir(portfolio_dir):
        if f.endswith('Executive-Briefing.md'):
            shutil.move(os.path.join(portfolio_dir, f), os.path.join(base_dir, 'Team_Reports', 'Executive_Briefings', f))
